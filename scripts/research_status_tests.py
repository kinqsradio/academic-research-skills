"""Portable behavioral cases: python3 scripts/research_status_tests.py."""

import copy
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from research_status import validate_manifest


class ResearchStatusTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for name in ("source with spaces.txt", "output.md", "evidence.md", "receipt.md", "validation.md", "decision.md"):
            (self.root / name).write_text("fixture content\n", encoding="utf-8")
        self.task = {"id": "read-sources", "depends_on": [], "status": "pending",
                     "owner": "researcher", "inputs": [{"path": "source with spaces.txt",
                     "sha256": hashlib.sha256(b"fixture content\n").hexdigest()}],
                     "outputs": ["output.md"], "evidence": ["evidence.md"],
                     "approval": {"required": False, "state": "not_required", "decision_path": None},
                     "receipt": None}
        self.manifest = {"schema_version": 1, "run_id": "example", "status": "active", "tasks": [self.task]}

    def report(self):
        return validate_manifest(self.manifest, self.root)

    def finish(self, task=None):
        task = task or self.task
        task["status"] = "complete"
        task["receipt"] = {"path": "receipt.md", "validation_evidence": ["validation.md"]}

    def assert_invalid(self, phrase):
        report = self.report()
        self.assertFalse(report["valid"], report)
        self.assertEqual(report["eligible_tasks"], [])
        self.assertTrue(any(phrase in error for error in report["errors"]), report)

    def test_ready_and_spaces(self):
        self.assertEqual(self.report()["eligible_tasks"], ["read-sources"])

    def test_completed_receipt_and_dependent_ready(self):
        dependent = copy.deepcopy(self.task)
        dependent.update(id="write", depends_on=["read-sources"])
        self.manifest["tasks"].append(dependent)
        self.finish()
        self.assertTrue(self.report()["valid"])
        self.assertEqual(self.report()["eligible_tasks"], ["write"])

    def test_missing_input(self):
        (self.root / "source with spaces.txt").unlink()
        self.assert_invalid("missing file")

    def test_stale_input(self):
        (self.root / "source with spaces.txt").write_text("changed", encoding="utf-8")
        self.assert_invalid("stale input")

    def test_downstream_review_snapshot_stale(self):
        self.finish()
        review = copy.deepcopy(self.task)
        review.update(id="review", status="pending", depends_on=["read-sources"], receipt=None)
        review["inputs"] = [{"path": "output.md", "sha256": hashlib.sha256(b"fixture content\n").hexdigest()}]
        self.manifest["tasks"].append(review)
        (self.root / "output.md").write_text("revision", encoding="utf-8")
        self.assert_invalid("stale input")

    def test_complete_missing_output(self):
        self.finish()
        (self.root / "output.md").unlink()
        self.assert_invalid("missing file")

    def test_complete_requires_receipt_and_validation(self):
        self.task["status"] = "complete"
        self.assert_invalid("requires a receipt")
        self.finish()
        self.task["receipt"]["validation_evidence"] = []
        self.assert_invalid("nonempty path list")

    def test_blocked_in_progress_paused_cancelled(self):
        for state in ("blocked", "in_progress"):
            self.task["status"] = state
            self.assertTrue(self.report()["valid"])
            self.assertEqual(self.report()["eligible_tasks"], [])
        self.task["status"] = "pending"
        for state in ("paused", "cancelled"):
            self.manifest["status"] = state
            self.assertTrue(self.report()["valid"])
            self.assertEqual(self.report()["eligible_tasks"], [])

    def test_human_gate_pending_rejected_approved(self):
        self.task["approval"] = {"required": True, "state": "pending", "decision_path": None}
        self.assertTrue(self.report()["valid"])
        self.assertEqual(self.report()["eligible_tasks"], [])
        self.task["approval"]["state"] = "rejected"
        self.assertEqual(self.report()["eligible_tasks"], [])
        self.finish()
        self.assert_invalid("unmet human approval")
        self.task["approval"].update(state="approved", decision_path="decision.md")
        self.assertTrue(self.report()["valid"])
        (self.root / "decision.md").unlink()
        self.assert_invalid("missing file")

    def test_dependency_missing_duplicate_and_cycle(self):
        self.task["depends_on"] = ["absent"]
        self.assert_invalid("missing dependency")
        self.task["depends_on"] = []
        self.manifest["tasks"].append(copy.deepcopy(self.task))
        self.assert_invalid("duplicate task ID")
        self.manifest["tasks"].pop()
        self.task["depends_on"] = ["read-sources"]
        self.assert_invalid("dependency cycle")

    def test_in_progress_requires_dependencies_and_gate(self):
        self.task["status"] = "in_progress"
        self.task["approval"] = {"required": True, "state": "pending", "decision_path": None}
        self.assert_invalid("in_progress with unmet human approval")
        self.task["approval"].update(state="approved", decision_path="decision.md")
        prerequisite = copy.deepcopy(self.task)
        prerequisite.update(id="scope", status="pending")
        self.manifest["tasks"].append(prerequisite)
        self.task["depends_on"] = ["scope"]
        self.assert_invalid("in_progress with unmet dependencies")

    def test_multitask_cycle_and_complete_unmet_dependency(self):
        second = copy.deepcopy(self.task)
        second.update(id="second", depends_on=["read-sources"])
        self.manifest["tasks"].append(second)
        self.task["depends_on"] = ["second"]
        self.assert_invalid("dependency cycle")
        self.task["depends_on"] = []
        self.finish(second)
        self.assert_invalid("complete with unmet dependencies")

    def test_unsafe_paths(self):
        for path in ("../outside", "/tmp/outside", "C:/outside", "folder\\outside", ""):
            self.task["outputs"] = [path]
            self.assertFalse(self.report()["valid"], path)
            self.assertEqual(self.report()["eligible_tasks"], [])

    def test_symlink_escape(self):
        with tempfile.TemporaryDirectory() as outside:
            try:
                (self.root / "escape").symlink_to(outside, target_is_directory=True)
            except (OSError, NotImplementedError):
                self.skipTest("symlinks unavailable on this host")
            self.task["outputs"] = ["escape/secret.md"]
            self.assert_invalid("escapes root")

    def test_malformed_types_fail_without_crashing(self):
        for field in ("status", "id", "depends_on", "approval", "inputs", "outputs", "receipt"):
            manifest = copy.deepcopy(self.manifest)
            manifest["tasks"][0][field] = {"unexpected": []}
            self.assertFalse(validate_manifest(manifest, self.root)["valid"], field)

    def test_cli_json_and_read_only(self):
        manifest_path = self.root / "run with spaces.json"
        manifest_path.write_text(json.dumps(self.manifest), encoding="utf-8")
        before = {path.name: path.read_bytes() for path in self.root.iterdir()}
        result = subprocess.run([sys.executable, str(Path(__file__).with_name("research_status.py")),
                                 str(manifest_path), "--root", str(self.root), "--json"],
                                capture_output=True, text=True, check=False)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)["eligible_tasks"], ["read-sources"])
        self.assertEqual(before, {path.name: path.read_bytes() for path in self.root.iterdir()})

    def test_template_has_no_completed_claims(self):
        repo = Path(__file__).resolve().parents[1]
        template = json.loads((repo / "skills/academic-pipeline/RUN_TEMPLATE.json").read_text(encoding="utf-8"))
        self.assertTrue(validate_manifest(template, repo)["valid"])
        self.assertTrue(all(task["status"] == "pending" for task in template["tasks"]))


if __name__ == "__main__":
    unittest.main()
