# Repository layout

Read AGENTS.md for working rules. Keep reusable instructions separate from research records and submission artifacts. Read the GUIDELINES.md in a folder before using it; create one whenever adding a maintained folder.

Group Markdown content by purpose within each category. Category roots hold navigation guides or indexes and required registers or entrypoints; put substantive content in named subfolders with their own GUIDELINES.md. Keep parent guides linked to those subfolders so a person can browse the repository without guessing paths. Avoid catch-all folders.

Branch policy: `main` is the project-neutral template. It may contain reusable skills, shared instructions, tooling, generic operations guidance, and empty folder scaffolding or registers. Keep populated registers, research notes, plans, decisions, drafts, reviews, and project-specific setup audits on the corresponding `research/<project>` branch. Downloaded research PDFs stay local in papers/ and must never be staged, committed, or pushed on any branch. Start each project branch from `main`; promote new skills and other reusable improvements only through reviewed template-only commits, never merge a research branch into `main`, and merge approved template updates from `main` into project branches. Use `template/<change>` for reusable improvements. Follow [the full branch workflow](docs/operations/branching/branch-workflow.md), including its canonical [provider-neutral naming and attribution policy](docs/operations/branching/branch-workflow.md#provider-neutral-names-and-attribution).

| Folder | Contents |
| --- | --- |
| papers/ | Local, ignored source PDFs; persistent download and IEEE reference registers. |
| docs/planning/ | Research questions, scope, schedules, and task plans. |
| docs/literature/ | Search logs, reading notes, evidence tables, and synthesis notes. |
| docs/methods/ | Study designs, analysis plans, and reproducibility notes. |
| docs/decisions/ | Decisions, alternatives, rationale, and unresolved issues. |
| docs/operations/ | Navigation for branching, setup, compatibility, and validation records. |
| submissions/drafts/ | Working manuscripts, outlines, abstracts, and response drafts. |
| submissions/reviews/ | Reviews tied to a specific draft and revision responses. |
| submissions/final/ | Candidate final exports awaiting or carrying human approval. |
| submissions/version/ | Preserved review and submission snapshots. |
| skills/ | Canonical, team-authored research workflows. |
| agents/ | Shared role and handoff conventions. |
| scripts/ | Repository maintenance helpers. |
| [.github/](.github/GUIDELINES.md) | Public repository validation automation. |

Use lowercase hyphenated names for new files where practical. Keep existing paper filenames stable. Date logs as YYYY-MM-DD and identify the draft or source they concern. A file in final/ is not evidence of approval or submission.
