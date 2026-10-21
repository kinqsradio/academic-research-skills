---
name: research-presentations
description: Create, edit, or review academic slides and speaker notes from research evidence, preserving requested scope, existing decks, accessibility, and verifiable output. Use for presentation outlines or actual decks; use academic-paper for manuscripts.
---

# Research presentations

Read [folder guidance](GUIDELINES.md). Match the requested artifact: an outline stays an outline; a review produces findings without editing unless authorized. A slide request need not become a manuscript or a research pipeline.

## Establish the brief and inputs

Identify audience, purpose, research stage, duration, slide-count constraints, language, required format, rubric or venue, and available AI-use policy. Reuse settled choices; state consequential assumptions and unresolved requirements. Continue independent work when a requirement is missing, but do not declare an assessed artifact finalized without resolving applicable policy requirements.

Identify the exact source versions and output destination. Distinguish a deck to edit from a visual reference or template. Inspect the original's slides, hidden slides, notes, order, assets, theme, and requested changes. Preserve the original and unaffected content. Respect user templates and counts; count cover and closing slides within a requested total unless specified otherwise. Do not add a cover to a one-slide request by default. Explain a material conflict before changing the brief.

Keep canonical Markdown slide text, notes, citations, and visual specifications in a purpose-based `submissions/drafts/<topic>/` folder with its own GUIDELINES.md. Keep reviews in `submissions/reviews/` and meaningful snapshots under `submissions/version/`. Use [the storyboard](STORYBOARD_TEMPLATE.md) when useful, scaling it down for a single slide. Actual decks or exports use only requested formats or formats required by the authorized deliverable.

## Build an evidence-backed story

Read the supplied evidence, retaining page, section, table, or figure locators. Map each consequential claim and exhibit to its support. Separate findings, interpretation, hypotheses, and proposed work; a proposal has no completed results. Mark gaps or narrow claims instead of inventing values, citations, approvals, author decisions, or checks. Put concise citations near claims and full references in the agreed reference location; keep notes traceable too.

Use [deep-research](../deep-research/SKILL.md) for substantial evidence discovery, [research-design](../research-design/SKILL.md) for methodological decisions, and [academic-paper](../academic-paper/SKILL.md) for manuscript work. For any paper acquisition follow [paper guidance](../../papers/GUIDELINES.md), [DOWNLOADS.md](../../papers/DOWNLOADS.md), and [REFERENCES.md](../../papers/REFERENCES.md): register every download, verify metadata/provenance, record size and SHA-256 for verified local PDFs, and mark uncomputed legacy fields unknown. Keep PDFs local and ignored, never staged, committed, or pushed; preserve stable source IDs separately from slide citation numbers.

Sequence the question, necessary context, approach, evidence or proposed evaluation, limitations, and implication as the audience needs them. Give each slide a purpose and a clear relationship to the next. Use a supported takeaway title when the slide establishes one; topic or question titles suit orientation, methods, and unresolved questions. Assertion–evidence is an optional design approach, not a requirement to make every title a finding.

Write concise, concrete prose that preserves qualifications, units, and technical meaning. Follow the writer's [clear-prose rules](../academic-paper/argument-and-revision.md#clear-specific-prose); use [prose-quality-review](../prose-quality-review/SKILL.md) for a focused editorial check. Avoid slogans, generic claims of importance, and compression that obscures reasoning.

## Design and implement the requested artifact

Consult [design guidance](DESIGN_GUIDANCE.md) for source scope and practical choices. Establish reader-centric hierarchy with consistent alignment, spacing, limited colors, and typography. Adapt layouts to content; avoid repeated card grids or dashboard styling without a communication purpose. Cut or split content before shrinking text. Do not impose rigid word, font, or slides-per-minute quotas.

Choose explanatory visuals when they clarify a relationship, mechanism, comparison, or result. Stock images and decoration are optional. Use scientific plotting tools for research figures and [research-diagrams](../research-diagrams/SKILL.md) for suitable Mermaid diagrams. Verify chart values, axes, units, uncertainty, legends, and table labels against inputs. Use native editable charts, tables, and requested diagrams when supported by the format; preserve their data/source. Do not flatten content into images to claim editability. Report unavoidable conversion limits.

When building or editing a deck, select and read the current host's relevant presentation tool/skill instructions. Check supported import/export behavior before converting. Preserve editable elements, notes, assets, and order; inspect round trips rather than assuming fidelity. A design reference does not authorize replacing source wording or claims.

Support logical reading order, descriptive slide titles, meaningful alt text, sufficient contrast, labels as well as color, captions for relevant media, and spoken descriptions of important visuals in notes. Check readability at likely viewing distance. Use available accessibility checkers as partial checks; inspect manually and provide accessible materials in the agreed format.

## Verify and hand off

Check the exact candidate's text, numbers, citations, references, notes, slide count/order, required sections, assets, and editability against the brief and source. For an edited deck compare unaffected slides and notes with the original. Render and inspect every slide, including relevant builds, for clipping, overlaps, missing glyphs/assets, unreadable figures, and hierarchy. Automated bounds checks do not establish visual quality. Recheck content and notes after export; identify the files and hashes or commit plus working-tree state actually checked.

Use at most two targeted repair passes after the initial inspection; report remaining defects and needed decisions rather than looping. If rendering or native inspection is unavailable, deliver useful source or permitted output and label that verification gap; do not claim the deck passed visual/native checks. Distinguish estimated speaking time from an actual human rehearsal and record only observed rehearsal evidence.

For substantial multi-stage work use [academic-pipeline](../academic-pipeline/SKILL.md) and bounded roles under [team guidance](../../agents/README.md); ordinary single-slide work stays direct. Route consequential claim/exhibit validation to [academic-paper-reviewer](../academic-paper-reviewer/SKILL.md). Changed candidates reopen affected checks. State the actual reviewer arrangement; self-review is not independent review.

Return changed paths and exact versions, requested formats delivered, source coverage, checks actually performed, remaining evidence/design/accessibility/tool limits, and human decisions. Use [generative-ai-use](../generative-ai-use/SKILL.md) when disclosure is required or requested, grounded in actual author guidance and work records. Preparation does not establish approval or submission. Do not publish, upload, or share by default.
