---
name: academic-paper-reviewer
description: Review an academic draft for claim support, research design, argument coherence, and stated assessment or venue requirements. Produce actionable findings tied to an exact manuscript version; do not rewrite the manuscript unless a separate revision task is requested.
---

# Evidence-based manuscript review

Give the author a useful account of what the draft supports, what needs correction, and what could not be assessed. Read [GUIDELINES.md](GUIDELINES.md) before reviewing.

## Define the review

Review the canonical Markdown manuscript; write findings in Markdown. When reviewing a conversion, distinguish text fidelity from layout fidelity and citation corrections; check the conversion receipt before assuming an original was preserved completely.

Identify the manuscript path and version, requested review scope, research type, available source material, and any supplied rubric or brief. If no target rubric exists, review against the stated research aim and explain that limitation. Do not invent a journal's current rules or claim authority to accept or reject submissions.

Read the complete relevant draft before judging its argument. For partial review, name the sections covered. Keep the manuscript and source files unchanged; save a review to `submissions/reviews/<topic>/<draft-name>-<version>-review.md` when a file output is requested or established, using [REVIEW_TEMPLATE.md](REVIEW_TEMPLATE.md). Preserve prior reports during re-review and link the new report to the earlier findings. A chat-only request needs no new file.

## Examine the evidence and reasoning

- Check whether the question, method, evidence, and conclusion align. Distinguish a proposal from completed research and a descriptive association from a causal result.
- Trace consequential factual claims to the actual cited source and a page, section, table, or figure. Check population, conditions, numbers, uncertainty, and contrary evidence. A plausible reference title does not prove support.
- Assess methods appropriate to this research type. Check eligibility and search transparency for reviews; sampling, measures, comparisons, and analysis for empirical work; definitions, premises, and counterarguments for conceptual work.
- Check the team report-style default in prose: use `Section` or `Sections` rather than `§` or `§§`, and flag paragraph signs or arrows used in place of words. Preserve meaningful mathematical notation, bracketed citations, accurate titles and quotations, and explicit assessment, venue, or author requirements. Check that variables and operators are introduced and worked examples explain the quantities and reasoning. Treat this as a scoped style check, not a universal IEEE prohibition.
- Check supplied requirements, citations, internal consistency, and clarity. Prioritize research validity over presentation preferences. Report inaccessible references separately from demonstrated citation errors.

For a slide-deck review, use [research-presentations](../research-presentations/SKILL.md) for the slide-specific checks while retaining this skill’s evidence and read-only boundaries. Check the exact deck and notes against the source manuscript, requirements and supporting evidence; assess rendered slides separately from source text. Do not infer native editability, accessibility, rehearsal or correct playback from a montage alone.

For a focused clarity or slop review, use [prose-quality-review](../prose-quality-review/SKILL.md) and its report format. The full manuscript review remains responsible for consequential source, method, and exhibit checks; do not count a focused prose pass as that audit.

For a prose or punctuation review, apply the writer's [clear-prose guidance](../academic-paper/argument-and-revision.md#clear-specific-prose) and [punctuation checks](../academic-paper/argument-and-revision.md#punctuation-by-function), including their linked source rationale. Check concrete actors/actions, unsupported praise, empty transitions, repetitive framing, and unnecessary abstraction against the intended meaning and available evidence. Check compound modifiers, `-ly` adverbs, ranges, parenthetical dash consistency, introductory elements and list commas, restrictive clauses, comma splices, semicolon clause/list structure, and running-prose colon placement. Preserve source titles, quotations, code, mathematics, established terms, and necessary uncertainty.

Label each finding as a grammatical/meaning error, a breach of an identified brief or venue requirement, an inconsistency with the chosen house style, or an optional clarity suggestion. Name the actual rule and reader consequence. Do not require a serial comma or a particular parenthetical dash convention when another consistent convention is permitted. Do not impose word bans, quotas, forced synonyms, random variation, or an absolute active/passive rule. Do not infer AI authorship from punctuation or vocabulary or recommend detector evasion. A request to remove “AI slop” calls for specific editorial findings, not an authorship verdict.

For each actionable finding, identify its exact manuscript location, observed problem, supporting evidence, consequence, and practical correction. Use **major** when the issue changes a central claim, interpretation, method validity, or required deliverable; use **minor** for a local issue with limited effect. Label optional suggestions separately. Explain uncertainty rather than inventing confidence scores or findings to fill a quota.

## Freeze and audit the candidate

Record the draft commit or SHA-256 and source versions before substantive review. Use [CLAIM_AUDIT_TEMPLATE.md](CLAIM_AUDIT_TEMPLATE.md) for consequential claims and exhibits. Count the inventoried, examined, inaccessible, and unchecked claims so partial coverage stays explicit. Separate source identity, claim support, numerical consistency, and rendered presentation checks. A failed lookup does not prove a fabricated source. Read original sources where possible; summaries alone cannot justify fine-grained or negative evidence claims.

Map each consequential exhibit to its input data or source locator and producing code or documented manual process. Inspect the rendered candidate when available; mark this gate unrun otherwise. Check exact numbers from data/tables rather than estimating them from graphics. For executable analyses, record command, environment, seed where relevant, exit result, and comparison with expected outputs; never call an unexecuted analysis reproduced. Treat changed inputs or a revised draft as invalidating affected earlier checks.

For Mermaid exhibits, apply [research-diagrams](../research-diagrams/SKILL.md) to audit arrow meanings, evidence locators, counts, assumptions and consistency with the exact draft. Review the rendering separately from claim support; preserve the reviewer boundary against silently editing the manuscript.

For a final-submission review, check the AI-use disclosure against [generative-ai-use](../generative-ai-use/SKILL.md), the applicable requirements, and available interaction records. Verify the appendix label and applicable format. Under the four-part default, check tool/principle, a stage-level workflow with the author-action column before the AI-action column and performer-specific checks, concrete controls, and traceable sample instructions/responses. Check that the account keeps the human as author and foregrounds documented guidance, decisions, and revisions, preferably in active first person when appropriate. Distinguish human authorship from wording generation: flag unsupported claims that every sentence was human-written or human-verified, omitted substantive AI drafting, and invented human actions. Acknowledging substantial AI-generated wording does not itself make the AI an author. Flag a generic assistance list that omits these details. Check affected-material mapping and actual assistance, keep internal readiness notes separate from submission prose, and preserve material limits and pending human confirmations without inventing attestations. Report unavailable history and policy gaps; do not infer complete disclosure, no AI use, or permission from an appendix alone. Keep the reviewer boundary: report findings without editing the manuscript or composing declarations for its authors.

## Check IEEE references and catalog traceability

For team manuscripts, check IEEE style unless the supplied brief, venue, or author requires another style. Verify first-citation ordering, bracketed in-text numbers, reuse of the same number for repeated citations, and correspondence with each reference-list entry. Check metadata against source content or authoritative publication records and report unknown or inaccessible fields. Renumbering alone does not establish claim support.

Use the [paper guidance](../../papers/GUIDELINES.md), [download register](../../papers/DOWNLOADS.md), and [reference catalog](../../papers/REFERENCES.md) to trace local sources and access history. Check the working mapping between document reference numbers and stable catalog IDs such as `P001`; the two numbering systems have different purposes. Flag a missing download or reference entry without silently changing the author's sources or inventing provenance. If an authorized task requires a new download, follow the canonical register process and coordinate writes with its owner.

Research PDFs stay local and ignored in `papers/`; never stage, commit, or push them on any branch. Keep populated download/reference records and research outputs persistently versioned on the project branch, retaining stable source IDs and metadata when a local PDF is unavailable. `main` keeps only reusable guidance and empty research scaffolding/registers; follow the [branch workflow](../../docs/operations/branching/branch-workflow.md).

## Deliver a bounded review

Summarize the draft's strongest supported contribution and its most important unresolved issues. State the review coverage, source checks performed, inaccessible evidence, and any analyses not reproduced. Findings about omitted content must name the places checked; absence cannot be supported by a fabricated quotation.

Do not convert this review into an acceptance probability, grade, or proof of research correctness. If asked to re-review, compare the new version with the previous findings and mark each addressed, partly addressed, unresolved, or no longer applicable with evidence. Identify material new issues without reopening stylistic choices already settled by the author.

## Delegation

The human selects the lead session's model and effort; subagent routing limits do not override that choice. The lead supplies scoped instructions, owned files, inputs, acceptance criteria, and a budget/stopping condition, then checks evidence and integrates the returns. Workers perform their assigned substantive work and report limitations; they do not create another layer of workers. Apply [team model routing](../../agents/routing/MODEL_ROUTING.md) to delegated workers, including the prohibition on Ultrafast.

For substantial reviews, divide distinct checks or use a second reader for consequential claims. Give a blind reviewer the frozen draft, criteria and sources without the first verdict; report the actual review arrangement. Standing team authorization covers this delegation; missing tools or source access remain explicit limitations.
