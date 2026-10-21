# Resumable research run

Use a manifest when a substantial project needs bounded, repeatable coordination. The original [template](RUN_TEMPLATE.json) contains proposed tasks only and starts paused. Copy it to `docs/planning/workflow/<project>-run.json` on the project research branch, rename its placeholders, and remove or add tasks to match authorized scope. Keep a human-readable plan alongside it. Do not store populated project records in this skill folder or on `main`.

## Read-only status check

From the repository root, with Python 3.10+:

```sh
python3 scripts/research_status.py "docs/planning/workflow/project-run.json"
python3 scripts/research_status.py "docs/planning/workflow/project-run.json" --json
```

`--root PATH` optionally sets the repository root for the manifest's paths, for example during isolated tests. The default is the repository containing the script, not the manifest's parent directory. Quote paths containing spaces. Exit 0 means structurally valid, 1 means validation issues, and 2 means unreadable or malformed JSON or a command-line error. The JSON report contains `valid`, `errors`, `tasks`, and `eligible_tasks`; the text report shows task owners and waiting reasons. A malformed manifest, paused run, or cancelled run has no eligible tasks. Pending tasks are eligible only when dependencies are complete, inputs match their snapshots, and any required human gate has an approved decision file.

The helper uses only Python's standard library and reads files. It does not execute arbitrary commands, call models, download papers, change statuses, schedule work, authenticate approval, or contact anyone. A checker can repeat this command within an authorized automation, but actual execution uses available agent tools and the user's authority. Do not treat a readiness result as new authorization. Establish a task budget and stopping condition in the plan before starting work; stop at the bound and retain blockers rather than silently extending a run.

## Manifest contract

Top-level fields are `schema_version` (integer `1`), nonempty `run_id`, `status` (`active`, `paused`, or `cancelled`), and `tasks` (list). Task IDs are stable strings composed of letters, digits, underscores, and hyphens, beginning with a letter or digit. Dependencies refer to these IDs and must form an acyclic graph. No duplicate IDs, duplicate dependencies, or missing dependencies are permitted.

| Task field | Meaning |
| --- | --- |
| `id` | Stable task identity, separate from paper IDs and citation numbers. |
| `depends_on` | List of prerequisite task IDs; all must be complete before eligibility. |
| `status` | `pending`, `in_progress`, `blocked`, or `complete`. |
| `owner` | Nonempty responsible person or role; assign one owner per output. |
| `inputs` | List of `{ "path": "relative/file", "sha256": "64 lowercase hex characters" }` snapshots. Every listed file must exist and match, at every task status. |
| `outputs` | Planned repository-relative file paths; a complete task needs a nonempty list of existing files. |
| `evidence` | Paths to supporting records; a complete task needs a nonempty list of existing files. |
| `approval` | `{ "required": true, "state": "pending", "decision_path": null }` for a human gate; state may become `approved` or `rejected`. Approved gates require an existing decision file. Ungated tasks use `required: false`, `state: "not_required"`, `decision_path: null`. |
| `receipt` | `null` while uncompleted, or `{ "path": "relative/receipt.md", "validation_evidence": ["relative/check-record.md"] }`; complete tasks require the receipt file and a nonempty list of existing validation records. |

Use forward-slash repository-relative paths. Absolute paths, drive-prefixed paths, backslashes, parent traversal, and symlinks escaping the chosen repository root are rejected, including planned outputs. Files and paths may contain spaces. Unknown extra fields are ignored; they are never interpreted as actions. Keep substantive blocker descriptions, review budgets, and authority in the plan or receipt rather than embedding executable commands in the manifest.

The pending template has empty input snapshots because no actual files have been selected. For downstream inputs that do not yet exist, leave the snapshots empty until prerequisites produce those files; then populate their actual SHA-256 before starting the downstream task. Never invent a hash for a planned output. Before starting a task, enumerate and hash its actual inputs, including scope decisions, source records, methods notes, analysis inputs, and the exact draft for review. Use an available SHA-256 tool or Python's `hashlib`; capture the bytes actually read. A snapshot hash establishes byte identity, not content truth. Empty inputs are structurally allowed for initial intake, but must not be used to conceal material dependencies.

## State updates and recovery

1. The coordinator checks the manifest and the plan, confirms the requested scope and each owner's budget, and selects one eligible task using existing authorization. Record `in_progress` before its bounded work begins. Do not restart another owner's in-progress task merely because it is absent from the eligible list.
2. The owner produces the scoped output, evidence records, and a receipt. The coordinator checks acceptance criteria and evidence before recording `complete`. Neither an in-progress nor a complete task may have unmet dependencies or an unapproved required gate. Planned outputs and receipts need not exist during work; they must exist on completion. File presence alone does not establish acceptance.
3. Missing access, unresolved evidence, or an exceeded repair/review limit becomes `blocked`, with the needed input or decision in the plan. A pending gate may remain `pending`; neither state is eligible. Do not replace a required decision with an assistant's agreement, silence, or elapsed time.
4. Only record a required gate as `approved` when the human's actual decision and its scope are documented in `docs/decisions/`, with date, author, rationale, and the exact artifact/version where relevant. Set `decision_path` to that record. The helper checks existence, not authenticity, scope, or whether approval still applies; the coordinator must inspect those. Approval, finalization, and submission remain distinct acts.
5. On pause or cancellation, set the run state accordingly and save the current work and handoff. The status helper will recommend no execution. Resume only under the user's current instruction; cancellation does not authorize later automatic resumption.
6. On resume or rerun, check every frozen input again. A changed draft invalidates its old review snapshot; a changed evidence packet may invalidate dependent writing. Reopen the affected task and downstream tasks as pending or blocked, preserve prior receipts as history, and explicitly review which approvals remain applicable. Rebaseline hashes only after inspecting the change and recording the rerun decision. Never silently refresh hashes to erase drift or keep an obsolete completed claim.

Use the plan to record revisions and explain why tasks were reopened. Keep historical outputs and review receipts under the repository's version guidance where appropriate. The status helper conservatively suppresses all readiness recommendations if any recorded task is invalid, so resolve or accurately reopen stale history before scheduling new work.

## Evidence and handoff receipts

Follow the [team handoff format](../../agents/README.md#handoff-receipt). A receipt identifies the task and owner, exact input paths and hashes or version, performed work, produced files, checks actually run, their results, limits, and next decision. `validation_evidence` links to existing test records, rendered-layout checks, source checks, or review findings according to the output's purpose; the receipt itself may also carry the validation record. Do not invent a passed check because a file exists.

Source receipts carry stable paper IDs, source locators, search scope and selection decisions, and explicit full-text or abstract-only limits. Maintain both [download](../../papers/DOWNLOADS.md) and [IEEE reference](../../papers/REFERENCES.md) registers under [paper guidance](../../papers/GUIDELINES.md); retain size and SHA-256 for successfully verified PDFs, and unknown values when not checked. Registered sources do not imply locally available PDFs or supported claims.

Review receipts identify the exact reviewed draft snapshot, findings with locations and severity, evidence inspected, and reviewer arrangement. Sequential self-review is described as such. Preserve unresolved findings and the agreed round limit; do not silently begin another round. Completed review means the review was performed, not that every issue was resolved or the human approved submission.

Structural manifest validation and the helper's behavioral tests establish only the checks actually exercised. Claim verification, analysis reproducibility, rendered artifact quality, assessment-policy compliance, live-host execution, and human decisions still require their appropriate evidence.
