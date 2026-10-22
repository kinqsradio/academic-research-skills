"""Synthetic Git fixtures: python3 scripts/check_public_template_tests.py."""

from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from check_public_template import check_public_template


class PublicTemplateTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.git("init", "--quiet")
        self.write("papers/DOWNLOADS.md", "# Downloads\n\n| Source ID | Filename |\n| --- | --- |\n")
        self.write("papers/REFERENCES.md", "# References\n\nUse `## P001` with an IEEE reference on a private branch.\n")
        self.write("submissions/VERSION.md", "# Versions\n\n| Version | Status |\n| --- | --- |\n")
        for folder in ("docs/planning", "docs/literature", "docs/methods", "docs/decisions", "submissions/drafts"):
            self.write(f"{folder}/GUIDELINES.md", "# Folder guidance\n")
        self.git("add", ".")

    def git(self, *args):
        return subprocess.run(["git", "-C", str(self.root), *args], check=True, capture_output=True)

    def write(self, name, content):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    def check(self):
        return check_public_template(self.root)

    def assert_rejected(self, phrase):
        self.assertTrue(any(phrase in error for error in self.check()), self.check())

    def test_empty_scaffold(self):
        self.assertEqual(self.check(), [])

    def test_schema_and_documentation_can_change(self):
        self.write("papers/DOWNLOADS.md", "# Downloads\n\n| Identifier | Extra metadata | URL |\n| :--- | ---: | :---: |\n")
        self.write("papers/REFERENCES.md", "# Catalog\n\n## Record format\n\nUse `P001` as a stable ID.\n\n```markdown\n## P001\n[1] Example reference\n```\n")
        self.assertEqual(self.check(), [])

    def test_untracked_local_research_is_ignored(self):
        self.write("papers/local.PDF", "%PDF-1.7\n")
        self.write("docs/planning/private-notes.md", "Private project plan\n")
        self.assertEqual(self.check(), [])

    def test_tracked_pdfs_anywhere_case_insensitive(self):
        self.write("examples/path with spaces/paper.PdF", "%PDF-1.7\n")
        self.git("add", ".")
        self.assert_rejected("tracked PDFs")

    def test_research_categories_and_submission_artifacts(self):
        for name in ("docs/planning/study/plan.md", "docs/literature/search.csv", "docs/methods/design.md", "docs/decisions/decision.md", "submissions/final/manuscript.docx"):
            with self.subTest(name=name):
                self.write(name, "project record\n")
                self.git("add", name)
                self.assert_rejected(f"{name}: research scaffolding")

    def test_populated_download_table(self):
        with (self.root / "papers/DOWNLOADS.md").open("a") as stream:
            stream.write("| `P001` | [paper](paper.pdf) |\n")
        self.assert_rejected("populated register table")

    def test_populated_submission_version_table(self):
        with (self.root / "submissions/VERSION.md").open("a") as stream:
            stream.write("| v001 | reviewed |\n")
        self.assert_rejected("populated register table")

    def test_actual_reference_records(self):
        for content in ("## P001\nA. Author, Study, 2026.\n", "[1] A. Author, Study, 2026.\n", "Source ID: P1234\n", "Local file: [paper](study.PDF)\n"):
            with self.subTest(content=content):
                self.write("papers/REFERENCES.md", content)
                self.assert_rejected("source record detected")

    def test_submission_version_heading(self):
        self.write("submissions/VERSION.md", "# Versions\n\n## v001\nReviewed manuscript\n")
        self.assert_rejected("submission version record")

    def test_untracked_or_deleted_register_fails(self):
        self.git("rm", "--cached", "papers/REFERENCES.md")
        self.assert_rejected("required empty template register is not tracked")
        (self.root / "submissions/VERSION.md").unlink()
        self.assert_rejected("register must be a regular local file")

    def test_symlink_register_fails(self):
        target = self.root / "papers/REFERENCES.md"
        target.unlink()
        target.symlink_to("DOWNLOADS.md")
        self.assert_rejected("register must be a regular local file")

    def test_no_git_metadata_fails(self):
        with tempfile.TemporaryDirectory() as folder:
            errors = check_public_template(Path(folder))
        self.assertTrue(any("Cannot inspect Git index" in error for error in errors), errors)

    def test_cli_exit_status(self):
        script = Path(__file__).with_name("check_public_template.py")
        result = subprocess.run([sys.executable, str(script), "--root", str(self.root)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.write("submissions/drafts/draft.md", "private manuscript\n")
        self.git("add", ".")
        result = subprocess.run([sys.executable, str(script), "--root", str(self.root)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 1)
        self.assertIn("draft.md", result.stderr)


if __name__ == "__main__":
    unittest.main()
