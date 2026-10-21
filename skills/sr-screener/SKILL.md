---
name: sr-screener
description: Apply a confirmed review protocol to supplied study records or full texts, pilot eligibility decisions, resolve screening disagreements and report traceable selection counts. Use for study selection rather than literature searching or manuscript writing.
---

# Study screening

Make eligibility decisions reproducible and reviewable. Write instructions, decisions and reports in English. Preserve source titles and quotations accurately when needed as evidence.

## Establish the rules

Read the review question and protocol from `docs/methods/`. Convert eligibility requirements into criteria that a reviewer can apply, including the order of exclusion reasons, title/abstract versus full-text rules, duplicate handling and treatment of missing information. The review team confirms unresolved interpretations before they affect exclusions.

Inventory the supplied exports and PDFs in `papers/`. Give each record a stable identifier and preserve its source pointer. Record duplicate groups and their chosen representative; do not count a duplicate as a study excluded for eligibility. Link multiple reports of one study when the available evidence establishes that relationship; keep uncertain links explicit.

Use [the decision record](decision-record.md) for a lightweight screening log. Record the confirmed protocol version with each screening run. Do not assume a reference manager, database connector or runtime script exists.

## Keep source identities stable

Use the [paper guidance](../../papers/GUIDELINES.md), [download register](../../papers/DOWNLOADS.md), and [reference catalog](../../papers/REFERENCES.md). Reuse a paper's stable catalog ID such as `P001`; preserve imported record IDs separately when several imported records map to the same paper. Establish report/study links from evidence. Do not assign IEEE numbers at import or use a manuscript citation number as a screening identity.

Register every agent download with its filename, stable paper ID, verified bibliographic metadata, retrieval/version/access details, and verification evidence according to the canonical paper guidance. Coordinate catalog writes with the assigned owner. Missing retrieval history or metadata remains unknown; unsuccessful retrieval stays recorded as an access gap. If a narrative screening report uses IEEE citations, number its references by first citation and keep a report-specific mapping to catalog IDs.

Research PDFs stay local and ignored in `papers/`; never stage, commit, or push them on any branch. Keep populated download/reference records and research outputs persistently versioned on the project branch, retaining stable source IDs and metadata when a local PDF is unavailable. `main` keeps only reusable guidance and empty research scaffolding/registers; follow the [branch workflow](../../docs/operations/branching/branch-workflow.md).

## Pilot before scaling

Screen a small, varied sample, including known relevant studies and plausible exclusions. Compare decisions with human review and inspect disagreements. Assess whether ambiguous rules, unreadable text or missing evidence explain the differences. Amend the protocol when needed, preserve its revision and recheck decisions affected by the change.

A pilot establishes whether this workflow is usable for this corpus; it does not establish general screening accuracy. Scale after the team resolves the pilot's decision rules and confirms the planned workload. Record the actual reviewer/model arrangement rather than assigning a provider alias by default.

## Apply the protocol

For each record, evaluate the criteria against the available title/abstract or full text. Return **include**, **exclude** or **uncertain**, with the applicable reason and evidence location. Unread text or missing metadata is a pending information problem; it is not a default exclusion.

When dual review is required, use separate reviewers with the same protocol and restricted views. Each makes an initial decision without seeing the other's output. Separate human reviewers or isolated assistant workers can support this arrangement; repeated reading in one conversation is a single-reviewer procedure and must be labeled accordingly. Separate model calls do not establish independent error processes.

Reconcile disagreements against the criteria and evidence. If still unresolved, refer the record to the designated human adjudicator. Preserve the original decisions and the resolution. Sample agreed exclusions for quality review when the protocol calls for it; agreement alone does not establish correctness.

## Report and hand off

Keep screening logs and selection summaries in a purpose-based `docs/literature/<review>/` subfolder; place a requested review report in `submissions/reviews/<review>/`. Add a GUIDELINES.md to each new maintained subfolder. Reconcile imported, deduplicated, screened, excluded, sought, retrieved and included counts at their correct record/report/study level. Report pending decisions and unavailable full texts separately. A flow diagram must derive from the log, not from guessed totals.

Hand off included sources with reading scope and locators to `deep-research` or `academic-paper` when synthesis or writing is requested. Describe protocol changes, actual reviewer arrangement, human decisions and unresolved limits. A selected source list is not a completed systematic review.

Use [research-diagrams](../research-diagrams/SKILL.md) when a selection flow helps communicate the reconciled log. Keep records, reports and studies distinct, expose pending counts, and follow any required reporting standard; a Mermaid flow alone does not establish compliance.

## Host compatibility

Use local Markdown, CSV or another explicitly chosen format. Codex and Claude can follow the same workflow with their available file-reading and worker capabilities. If parsing, PDF extraction or isolated workers are unavailable, report the limitation and complete only the supported, accurately labeled portion.

## Delegation

The human selects the lead session's model and effort; subagent routing limits do not override that choice. The lead supplies scoped instructions, owned files, inputs, acceptance criteria, and a budget/stopping condition, then checks evidence and integrates the returns. Workers perform their assigned substantive work and report limitations; they do not create another layer of workers. Apply [team model routing](../../agents/routing/MODEL_ROUTING.md) to delegated workers, including the prohibition on Ultrafast.

Delegate bounded record batches only after the pilot. Dual reviewers receive the same protocol and isolated initial decision tasks. Save both decisions before reconciliation; do not merge their context to save tokens. Standing team authorization covers this delegation; missing tools or source access remain explicit limitations.
