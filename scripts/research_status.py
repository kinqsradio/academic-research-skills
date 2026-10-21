#!/usr/bin/env python3
"""Read-only validation and readiness report for a research-run manifest.

Uses Python 3.10+ standard library. File existence and hashes establish only
structural consistency, never research correctness or human authorization.
"""

import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import sys


TASK_STATES = {"pending", "in_progress", "blocked", "complete"}
RUN_STATES = {"active", "paused", "cancelled"}


def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def validate_manifest(data, root):
    """Return JSON-serializable status; do not write or execute anything."""
    root = Path(root).resolve()
    errors = []
    records = []

    def issue(message):
        errors.append(message)

    if not root.is_dir():
        issue("repository root must be an existing directory")

    def safe_path(value, label, must_exist=False):
        if not isinstance(value, str) or not value.strip():
            issue(f"{label}: expected a nonempty repository-relative path")
            return None
        pure = PurePosixPath(value)
        if (pure.is_absolute() or ".." in pure.parts or "\\" in value
                or re.match(r"^[A-Za-z]:", value) or not pure.parts):
            issue(f"{label}: unsafe path {value!r}")
            return None
        try:
            resolved = (root / value).resolve()
            resolved.relative_to(root)
            if must_exist and not resolved.is_file():
                issue(f"{label}: missing file {value!r}")
                return None
        except (OSError, ValueError, RuntimeError) as exc:
            issue(f"{label}: path escapes root or cannot be resolved ({exc})")
            return None
        return resolved

    def paths(value, label, must_exist=False, nonempty=False):
        if not isinstance(value, list) or (nonempty and not value):
            issue(f"{label}: expected {'nonempty ' if nonempty else ''}path list")
            return
        for index, entry in enumerate(value):
            safe_path(entry, f"{label}[{index}]", must_exist)

    if not isinstance(data, dict):
        return {"valid": False, "errors": ["manifest must be an object"],
                "eligible_tasks": [], "tasks": []}
    if type(data.get("schema_version")) is not int or data["schema_version"] != 1:
        issue("schema_version must be 1")
    if not isinstance(data.get("run_id"), str) or not data["run_id"].strip():
        issue("run_id must be a nonempty string")
    run_state = data.get("status")
    if not isinstance(run_state, str) or run_state not in RUN_STATES:
        issue("run status must be active, paused, or cancelled")
    tasks = data.get("tasks")
    if not isinstance(tasks, list):
        issue("tasks must be a list")
        tasks = []
    by_id = {}
    for index, task in enumerate(tasks):
        if not isinstance(task, dict):
            issue(f"tasks[{index}] must be an object")
            continue
        task_id = task.get("id")
        if not isinstance(task_id, str) or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]*", task_id):
            issue(f"tasks[{index}].id must be a stable alphanumeric/hyphen/underscore ID")
            continue
        if task_id in by_id:
            issue(f"duplicate task ID {task_id}")
            continue
        by_id[task_id] = task

    dependencies = {}
    for task_id, task in by_id.items():
        start_errors = len(errors)
        state = task.get("status")
        complete = state == "complete"
        started = state in ("in_progress", "complete") if isinstance(state, str) else False
        if not isinstance(state, str) or state not in TASK_STATES:
            issue(f"{task_id}: invalid task status")
        if not isinstance(task.get("owner"), str) or not task["owner"].strip():
            issue(f"{task_id}: owner must be a nonempty string")
        deps = task.get("depends_on")
        if not isinstance(deps, list) or any(not isinstance(dep, str) for dep in deps):
            issue(f"{task_id}: depends_on must be a list of task IDs")
            deps = []
        elif len(set(deps)) != len(deps):
            issue(f"{task_id}: duplicate dependency")
        dependencies[task_id] = deps
        for dep in deps:
            if dep not in by_id:
                issue(f"{task_id}: missing dependency {dep}")
        inputs = task.get("inputs")
        if not isinstance(inputs, list):
            issue(f"{task_id}: inputs must be a list of path/SHA256 snapshots")
            inputs = []
        for index, item in enumerate(inputs):
            label = f"{task_id}.inputs[{index}]"
            if not isinstance(item, dict):
                issue(f"{label}: expected path/SHA256 object")
                continue
            path = safe_path(item.get("path"), label, True)
            checksum = item.get("sha256")
            if not isinstance(checksum, str) or not re.fullmatch(r"[0-9a-f]{64}", checksum):
                issue(f"{label}: sha256 must be 64 lowercase hex characters")
            elif path:
                try:
                    if sha256(path) != checksum:
                        issue(f"{label}: stale input {item['path']!r}")
                except OSError as exc:
                    issue(f"{label}: cannot read input ({exc})")
        paths(task.get("outputs"), f"{task_id}.outputs", complete, complete)
        paths(task.get("evidence"), f"{task_id}.evidence", complete, complete)
        approval = task.get("approval")
        gate_open = False
        if not isinstance(approval, dict) or type(approval.get("required")) is not bool:
            issue(f"{task_id}: approval must contain boolean required")
        else:
            required = approval["required"]
            allowed = {"pending", "approved", "rejected"} if required else {"not_required"}
            approval_state = approval.get("state")
            if not isinstance(approval_state, str) or approval_state not in allowed:
                issue(f"{task_id}: invalid approval state")
            decision_path = approval.get("decision_path")
            if required and approval_state == "approved":
                safe_path(decision_path, f"{task_id}.approval.decision_path", True)
            elif decision_path is not None:
                safe_path(decision_path, f"{task_id}.approval.decision_path")
            gate_open = (not required and approval_state == "not_required") or approval_state == "approved"
            if started and not gate_open:
                issue(f"{task_id}: {state} with unmet human approval gate")
        receipt = task.get("receipt")
        if complete and not isinstance(receipt, dict):
            issue(f"{task_id}: complete requires a receipt")
        elif receipt is not None:
            if not isinstance(receipt, dict):
                issue(f"{task_id}: receipt must be null or an object")
            else:
                safe_path(receipt.get("path"), f"{task_id}.receipt.path", complete)
                paths(receipt.get("validation_evidence"),
                      f"{task_id}.receipt.validation_evidence", complete, complete)
        unmet = [dep for dep in deps if dep not in by_id or by_id[dep].get("status") != "complete"]
        if started and unmet:
            issue(f"{task_id}: {state} with unmet dependencies: {', '.join(unmet)}")
        reasons = []
        if state != "pending":
            reasons.append(f"task is {state}")
        if unmet:
            reasons.append("unmet dependencies: " + ", ".join(unmet))
        if not gate_open:
            reasons.append("human decision gate is not approved")
        if len(errors) > start_errors:
            reasons.append("task has validation errors")
        records.append({"id": task_id, "status": state, "owner": task.get("owner"),
                        "waiting_reasons": reasons})

    # Iterative DFS avoids recursion limits on long valid task chains.
    colours = {}
    for task_id in by_id:
        if colours.get(task_id):
            continue
        stack = [(task_id, False)]
        while stack:
            node, exiting = stack.pop()
            if exiting:
                colours[node] = 2
                continue
            if colours.get(node) == 1:
                issue(f"dependency cycle involving {node}")
                continue
            if colours.get(node) == 2:
                continue
            colours[node] = 1
            stack.append((node, True))
            stack.extend((dep, False) for dep in reversed(dependencies[node]) if dep in by_id)
    eligible = [record["id"] for record in records if not record["waiting_reasons"]]
    # A malformed manifest never recommends work, even if a sibling seems ready.
    if errors or run_state != "active":
        eligible = []
    return {"valid": not errors, "run_id": data.get("run_id"), "status": run_state,
            "errors": errors, "eligible_tasks": eligible, "tasks": records,
            "execution_note": "Read-only readiness; no task was executed or approved."}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path, help="JSON manifest file (quote paths containing spaces)")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1],
                        help="repository root used for all manifest paths")
    parser.add_argument("--json", action="store_true", help="emit a machine-readable status report")
    args = parser.parse_args(argv)
    try:
        # Reject duplicate JSON keys rather than silently accepting the last value.
        def unique_object(pairs):
            result = {}
            for key, value in pairs:
                if key in result:
                    raise ValueError(f"duplicate JSON key {key!r}")
                result[key] = value
            return result
        data = json.loads(args.manifest.read_text(encoding="utf-8"), object_pairs_hook=unique_object)
        report = validate_manifest(data, args.root)
    except (OSError, ValueError, RecursionError) as exc:
        print(f"Cannot read manifest: {exc}", file=sys.stderr)
        return 2
    if args.json:
        print(json.dumps(report, indent=2))
    else:
        print(f"Run {report.get('run_id', '?')}: {report.get('status', '?')}; "
              f"{'valid' if report['valid'] else 'invalid'}")
        for error in report["errors"]:
            print(f"ERROR: {error}")
        for record in report["tasks"]:
            reasons = "; ".join(record["waiting_reasons"]) or "ready subject to run status"
            print(f"{record['id']} [{record['status']}], owner {record['owner']}: {reasons}")
        print("Eligible tasks: " + (", ".join(report["eligible_tasks"]) or "none"))
        print("Read-only readiness; no task was executed or approved.")
    return 0 if report["valid"] else 1


if __name__ == "__main__":
    sys.exit(main())
