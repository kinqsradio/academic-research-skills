---
name: deep-research
description: Discover, verify, compare, and synthesize scholarly evidence for a research question using supplied papers or a documented search. Use when source discovery or evidence synthesis is the deliverable; use academic-paper for manuscript drafting and sr-screener for protocol-based eligibility decisions.
---

# Deep research

Produce a traceable evidence synthesis in English. Save it under `docs/literature/`; this skill does not draft manuscript prose for `submissions/drafts/`. Use the repository's existing instructions and any local `GUIDELINES.md` files. If a needed folder must be created, give it a `GUIDELINES.md` as required by the repository.

## Set the scope

Establish the research question and the boundaries that affect source selection: population or context, concepts, date range, source types, and language. Do not add constraints that the user or project has not chosen. If the user limits the work to supplied sources, keep that boundary. Otherwise, use suitable scholarly search sources available in the current environment and log the searches. Never send unpublished or confidential material to an external service without authorization.

Inventory relevant files in `papers/`. Treat filenames and numbering as local labels, not verified bibliographic records. Preserve the source files and record their repository-relative paths. If a PDF is unreadable or only partly accessible, report the limitation rather than implying full-text review.

Describe the search accurately. Keep exact query text, source or index, search date, filters, selection criteria, counts, and reasons for exclusion in a [search record](SEARCH_RECORD_TEMPLATE.md). Distinguish targeted or narrative searching from a scoping or systematic process. Do not call a search comprehensive or systematic unless its planned scope and search and selection steps are documented well enough to support that claim. For protocol-based eligibility decisions, use `sr-screener`.

## Track papers and references

Read the [paper guidance](../../papers/GUIDELINES.md), [download register](../../papers/DOWNLOADS.md), and [reference catalog](../../papers/REFERENCES.md) before downloading or using catalog records. Register every agent download in `papers/DOWNLOADS.md` and maintain its verified reference entry in `papers/REFERENCES.md`. Follow their canonical fields for filename, stable paper ID, title, authors, year, DOI or source URL, retrieval date, version/access, local size and SHA-256 checksum when computed, and verification evidence. Preserve unknown values and access limits; do not reconstruct a retrieval history or metadata from a filename. Reuse existing IDs and filenames, and coordinate catalog writes with the assigned owner when workers run concurrently.

Use stable catalog IDs such as `P001` in search and evidence records. They identify sources across tasks; they are independent of each document's IEEE citation numbers. In an IEEE synthesis, assign bracketed numbers in first-citation order, reuse the number for each repeated source, and provide a matching reference list using verified bibliographic details. Keep a document-specific mapping to catalog IDs in the working evidence record. Catalog membership does not prove a claim or full-text access.

Research PDFs stay local and ignored in `papers/`; never stage, commit, or push them on any branch. Keep populated download/reference records and research outputs persistently versioned on the project branch, retaining stable source IDs and metadata when a local PDF is unavailable. `main` keeps only reusable guidance and empty research scaffolding/registers; follow the [branch workflow](../../docs/operations/branching/branch-workflow.md).

## Verify and extract evidence

Verify each source's authors, title, year, publication status, and persistent identifier against the paper itself and, where available, a reliable publication record. A DOI or title confirms identity, not claim support. Note whether you read the full text, an abstract, or another limited portion.

For every material finding, record a precise page, section, table, figure, or stable identifier and enough context to check the claim. Use the [evidence matrix](EVIDENCE_MATRIX_TEMPLATE.md) for claim-level extraction. Separate the study's reported results from its authors' explanations and from your appraisal. Capture relevant design, sample or context, measures or data, limitations, and applicability. Do not infer methods or results from a citation, abstract, or filename when the source does not establish them.

Judge evidence in relation to the claim and study design. Preserve uncertainty, null or mixed results, and limitations. An association does not by itself establish causation; a small or selected sample does not establish broad generality. When several papers report the same study or dataset, note that relationship when supported rather than treating the reports as independent evidence.

Use [research-diagrams](../research-diagrams/SKILL.md) when a concept or evidence map makes the synthesis easier to understand. Preserve source locators and distinguish findings from interpretations and proposed relationships.

## Synthesize and hand off

Organize findings around the question or themes, comparing where studies converge, differ, or leave a gap. Explain plausible reasons for disagreement only when the sources support them. Avoid ranking evidence by publication venue alone or counting studies as votes. Use calibrated language and place citations close to the claims they support.

Write the synthesis to `docs/literature/<topic>/<topic>-evidence-synthesis.md`. Include the question and scope, a concise account of how sources were found and read, the evidence and its limitations, unresolved gaps, and repository-relative source pointers. Keep search and extraction records alongside it when they materially improve traceability. If the requested next step is manuscript prose, hand off the verified evidence and locators to `academic-paper` rather than turning this synthesis into a draft.

Use the file, PDF, search, and citation capabilities actually available in the current environment. No particular provider, model, API, account, or runtime is required. If a capability is unavailable, state what could not be checked and narrow the reported scope accordingly.

## Delegation

The human selects the lead session's model and effort; subagent routing limits do not override that choice. The lead supplies scoped instructions, owned files, inputs, acceptance criteria, and a budget/stopping condition, then checks evidence and integrates the returns. Workers perform their assigned substantive work and report limitations; they do not create another layer of workers. Apply [team model routing](../../agents/routing/MODEL_ROUTING.md) to delegated workers, including the prohibition on Ultrafast.

Split independent source batches or evidence questions among workers. Each returns source identities, reading scope, claim locators and gaps; a synthesis worker develops the substantive synthesis, and the lead compares findings, checks its claims, and integrates the output. Standing team authorization covers this delegation; missing tools or source access remain explicit limitations.
