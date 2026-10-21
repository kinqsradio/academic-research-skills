---
name: academic-paper
description: Plan and write English research manuscripts, revise existing drafts, prepare abstracts and reviewer responses, or format an approved submission. Use when the requested result is a scholarly draft rather than discovery of a new literature corpus.
---

# Academic paper

Turn a research argument and its evidence into the specific artifact the user needs. Write in English. The assignment rubric, venue instructions and author's choices determine the structure and citation style.

## Start from the intended artifact

Read the assignment or brief and the current draft. Identify the requested sections, audience, word limit, citation style and submission requirements. Reuse settled decisions from `docs/decisions/`; ask only about missing information that changes the writing. A request for an outline, abstract or revision does not automatically become a complete manuscript.

When the requested artifact is a slide presentation or oral companion, use [research-presentations](../research-presentations/SKILL.md). Keep the manuscript as an evidence source; adapt its argument for the audience and speaking time rather than copying paragraphs onto slides.

Read supplied sources in `papers/` and source notes in `docs/literature/` before using them. Record the actual reading scope and page/section locations. If the evidence is inadequate, mark the gap or narrow the claim; never fill it with an invented reference or result. Use `deep-research` when substantial reading, searching or evidence synthesis is needed.

## References and paper traceability

Use IEEE references by default for team manuscripts; an explicit assessment brief, venue rule, or author instruction can require another style. In IEEE drafts, number references in first-citation order, cite them with bracketed numbers such as `[1]`, reuse the assigned number for the same work, and keep the numbered reference list aligned after revisions. Use verified bibliographic details appropriate to the source type, including DOI or URL where applicable. Mark missing details for verification rather than inventing them.

Consult the [paper guidance](../../papers/GUIDELINES.md), [download register](../../papers/DOWNLOADS.md), and [reference catalog](../../papers/REFERENCES.md). Reuse stable paper IDs such as `P001` in working records, and map manuscript citation numbers to those IDs; never use catalog IDs or filename prefixes as IEEE reference numbers. Before downloading additional papers, follow the paper guidance and register each download with provenance and verified reference metadata. Preserve an unknown retrieval date or unverified field explicitly.

Research PDFs stay local and ignored in `papers/`; never stage, commit, or push them on any branch. Keep populated download/reference records and research outputs persistently versioned on the project branch, retaining stable source IDs and metadata when a local PDF is unavailable. `main` keeps only reusable guidance and empty research scaffolding/registers; follow the [branch workflow](../../docs/operations/branching/branch-workflow.md).

## Build and write the argument

Use [the argument and revision guide](argument-and-revision.md) to connect the question, contribution, evidence and section plan. Apply its [clear-prose guidance](argument-and-revision.md#clear-specific-prose) and [punctuation checks](argument-and-revision.md#punctuation-by-function) during drafting and revision. Diagnose vague or repetitive prose directly; preserve meaning and technical terminology, distinguish grammar from house preferences, and follow explicit brief, venue, or author rules. Punctuation and vocabulary are not grounds for an AI-authorship allegation; do not edit to evade detectors. Keep planned research distinct from completed studies. A proposed method has no results; an observed association does not establish causation without the required design and evidence.

Write the requested draft as canonical Markdown (`.md`) in a purpose-based `submissions/drafts/<topic>/` subfolder with its own GUIDELINES.md. Keep the team's review and revisions in that source; after team finalization, the human can copy it into the shared Google Drive document. Do not create a parallel DOCX or update a cloud document unless requested. Give sections a clear purpose and use transitions that explain how the reasoning develops. Preserve source qualifications, numerical results and the author's intended meaning. Follow disciplinary reporting conventions where applicable; do not force every paper into the same structure.

Use full words in report prose: write `Section` or `Sections` instead of `§` or `§§`, and avoid paragraph signs or arrows that substitute for words. Preserve meaningful mathematical notation, bracketed citations, and accurate source titles or quotations. Introduce variables and operators before using them, and explain worked examples in words so readers can follow the quantities and reasoning. Apply explicit assessment, venue, or author requirements when they differ; this is a team style default, not a claim that IEEE universally prohibits these symbols.

Write one English abstract from the actual manuscript when requested or required. Match its claims, numbers and scope to the body, and honor the applicable word and keyword limits. Do not add a second language unless requested.

Use [research-diagrams](../research-diagrams/SKILL.md) when a Mermaid diagram clarifies the argument or method. Keep its source in the manuscript Markdown with a caption, evidence pointers and text explanation; check the target format before export. Use scientific plotting tools for statistical figures.

## Keep an analysis and reporting record

For empirical work, connect the draft to the versioned study design and any dated amendments in `docs/methods/`. Separate planned, executed, exploratory, and confirmatory analyses using their actual chronology. When design work is the requested output, use `research-design` rather than inventing methodological choices while drafting.

Map reported results and exhibits to source data or cited passages, code/commands, environment versions, seeds where applicable, and expected outputs. Keep a receipt for executions actually performed and record restricted or missing inputs. Preserve reference outputs and run reproductions in a separate destination. State data/code/material availability accurately; a file inventory does not prove reproducibility, open access, or permission to release. Use the reviewer's [claim and exhibit audit](../academic-paper-reviewer/CLAIM_AUDIT_TEMPLATE.md) to hand off the exact candidate, numerical checks, and coverage.

## Revise and finish

For a revision, map each requested change to a location and evidence. Address reviewer comments through the tracker in the guide; distinguish completed edits, justified disagreements and unresolved questions. Keep reviewer reports and resolution trackers in `submissions/reviews/`; write response-letter drafts in `submissions/drafts/`.

During manuscript quality checks, use [prose-quality-review](../prose-quality-review/SKILL.md) for focused findings on vague, repetitive, inflated, or formulaic prose. Apply only authorized revisions and recheck meaning; a polished sentence does not establish source support.

When preparing a final submission, use [generative-ai-use](../generative-ai-use/SKILL.md) to prepare or update the requested `Appendix <letter>. Generative AI Use` from actual records. Use its four-part default: Tool and principle; a stage-by-stage Workflow placing documented author guidance, decisions, and revisions before AI work and checks; Controls; and Sample interactions. Prefer active first-person author voice when appropriate. Keep the human as author while distinguishing authorship from who generated wording; disclose substantive AI drafting actually used or adapted without implying every sentence was human-written or human-verified. Follow the actual brief or venue when it prescribes another format. Do not substitute a generic assistance list or internal status report for this account. Keep unresolved readiness in the working record or handoff, retain material limits where needed, and never turn unconfirmed author actions into completed checks.

Check the current candidate for claim support, internal consistency, citation accuracy, argument flow, length and required sections. Include ethics, data, funding, conflict and contribution statements when applicable; missing information stays explicit rather than becoming a fabricated declaration.

Use Markdown for working manuscripts and preserved text snapshots. Produce other formats only when explicitly requested or required by an authorized deliverable. When importing DOCX, preserve wording, punctuation, reference entries and numbering, paragraph order, lists, tables, links, and meaningful equations or notes. Inspect nontext elements and tracked changes; record unresolved conversion limits instead of silently dropping them. Compare the converted content with the original and record source/output hashes before removing an original when authorized. Keep faithful transcription separate from citation corrections or editorial changes; report those in a linked review. Inspect a rendered export when tools are available, and report conversion or verification limits. Save meaningful prior snapshots in `submissions/version/`; put a submission-ready candidate in `submissions/final/` only when its required checks and unresolved limitations are recorded. Preparing a final file does not imply submission or publication.

## Host compatibility

These instructions work as a local Markdown skill in Codex or Claude. Use whichever file, search, document and shell capabilities are actually available; no specific tool name or model is required. Use separate workers for substantial evidence checks and review under the standing team delegation policy when supported. Otherwise perform a disclosed single-session review without claiming independent agreement.

## Delegation

The human selects the lead session's model and effort; subagent routing limits do not override that choice. The lead supplies scoped instructions, owned files, inputs, acceptance criteria, and a budget/stopping condition, then checks evidence and integrates the returns. Workers perform their assigned substantive work and report limitations; they do not create another layer of workers. Apply [team model routing](../../agents/routing/MODEL_ROUTING.md) to delegated workers, including the prohibition on Ultrafast.

Keep one owner for the draft. Delegate bounded source checks or argument reviews to separate outputs, then integrate the checked findings before revising shared prose. Standing team authorization covers this delegation; missing tools or source access remain explicit limitations.
