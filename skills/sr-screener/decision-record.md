# Screening decision record

Use a CSV or Markdown table for a small corpus; use a tool-supported structured format for a larger one. Preserve a stable record ID through deduplication, screening and reporting.

| Field | What to record |
|---|---|
| Record ID and source | Stable import record ID, import source and local file or source pointer |
| Catalog paper ID | Existing stable paper ID such as P001, or pending registration; separate from IEEE numbers |
| Access and registration | Canonical download/reference entry and known retrieval or metadata gaps |
| Study/report link | Established relationship, or unknown |
| Protocol revision | Rules applied to this decision |
| Screening stage | Title/abstract or full text |
| Reviewer and arrangement | Person or actual model; single, dual or adjudication role |
| Decision | Include, exclude or uncertain |
| Reason | Criterion and ordered exclusion code when applicable |
| Evidence | Relevant text and page/section, or the missing information |
| Resolution | Final decision, adjudicator and rationale; original decisions retained |

## Incomplete decisions

Keep absent reviewer returns and inaccessible full text pending. If an exclusion rule cannot be evaluated, record the information required to settle it. Do not convert a parser error, model failure or missing response into an eligibility decision.

A protocol amendment may invalidate earlier decisions. Identify which records and criteria it affects, preserve the prior log, and re-screen the affected set. Do not mix decisions under different revisions into a single apparently consistent result.

## Counts

State the counting unit. A record is an imported reference, a report is a document about a study, and a study may have multiple reports. Maintain the mapping where known. Reconcile transitions within each unit and identify pending or unlinked items instead of forcing totals to match.

An exclusion summary should list the reason assigned under the protocol and its count. Report not-retrieved full texts separately from full-text exclusions. Retain the log needed to regenerate every count in a selection diagram or report.

Use [paper guidance](../../papers/GUIDELINES.md), the [download register](../../papers/DOWNLOADS.md), and the [reference catalog](../../papers/REFERENCES.md) as the maintained source records. Do not duplicate the metadata schema or infer retrieval history. Any IEEE report assigns reference numbers by its own first-citation order and maps those numbers to stable paper IDs separately.
