---
name: prose-quality-review
description: Review prose when asked to check for slop, AI slop, generic or formulaic writing, padding, or weak argument continuity. Give located, evidence-aware editorial findings without changing the manuscript or diagnosing authorship; use academic-paper-reviewer for full research validation.
---

# Review prose quality

Use this skill for a focused editorial review of an identified artifact. “Check for slop” means examine whether the prose serves its reader and argument. It does not request an AI-authorship verdict, detector score, detector evasion, or automatic rewriting. Read [folder guidance](GUIDELINES.md).

## Establish the candidate and scope

Identify the artifact, audience, genre, purpose, supplied brief or requested format, and requested depth. Use available context; state consequential assumptions and missing requirements. Record the exact candidate by commit plus working-tree state or file SHA-256; for pasted text, identify the supplied message and passage. Record sections actually read and exclusions. Read the complete relevant passage and its surrounding argument before reporting continuity or repetition problems; a sample is not a whole-document review. Changed inputs reopen affected findings.

Keep the manuscript and source files unchanged. Return findings in chat unless a report file is requested or established; then use `submissions/reviews/<topic>/<candidate>-prose-review.md`, preserving earlier reports and following that folder's guidance. Do not put manuscript reviews in this skill folder.

For assessed work, distinguish permitted proofreading from substantial drafting under the available assessment brief and AI-use policy before offering illustrative rewrites. Missing policy leaves that distinction unresolved; continue observational review and keep the limitation visible. Preserve actual AI-use disclosures. A review request does not authorize editing, exporting, uploading, submitting, or changing research decisions.

## Examine meaning and reader effect

Apply the shared [clear-prose guidance](../academic-paper/argument-and-revision.md#clear-specific-prose) and, when relevant, [punctuation checks](../academic-paper/argument-and-revision.md#punctuation-by-function). These are the canonical writing standards; do not duplicate or override them with a second style manual. Use [REVIEW_CRITERIA.md](REVIEW_CRITERIA.md) for the focused checks, evidence rationale, and negative cases.

Look for vagueness or unsupported specificity; low-information repetition, padding and generic closers; formulaic framing that supplies no useful relationship; broken argument continuity or unjustified causal/inferential transitions; literature lists that do not perform the synthesis required by this passage; inflated contribution or praise; and abstraction or terminology that obstructs the intended audience. Judge each in context. Repetition, passive voice, hedges, formal language, an isolated citation, and non-native English are not errors by themselves.

Inspect original supporting sources or records when available and within scope, retaining locators. Mark unexamined support as unverified; textual plausibility does not establish truth, and a missing source does not establish falsehood. Separate an observable textual gap from a verified contradiction. Route consequential claim, numerical, exhibit, methods, or reproducibility validation to [academic-paper-reviewer](../academic-paper-reviewer/SKILL.md) and its [claim/exhibit audit](../academic-paper-reviewer/CLAIM_AUDIT_TEMPLATE.md). Do not imply that this prose pass completed that audit. Follow [paper guidance](../../papers/GUIDELINES.md), [download register](../../papers/DOWNLOADS.md), and [reference catalog](../../papers/REFERENCES.md) if an independently authorized task needs source acquisition; this review needs no download by default.

## Report only useful findings

Use [REVIEW_TEMPLATE.md](REVIEW_TEMPLATE.md), scaling it to the request. Prioritize demonstrated effects on understanding, reasoning, or a supplied requirement; bound the report to meaningful changes rather than filling a quota. Group a repeated pattern with representative locations and state how much was examined. A calibrated “no actionable issue found in the examined passage” is valid.

For each finding provide a stable ID, location, exact short excerpt, category, specific reader effect, supporting text/requirement/source locator or unavailable evidence, and the smallest optional correction. For an omission, quote an actual nearby passage and identify the complete scope checked; never invent an excerpt of absent text. Distinguish a meaning/grammar problem, an identified requirement breach, a house-style inconsistency, and an optional preference. Label importance by the demonstrated effect, not how “AI-like” it sounds. Do not invent numerical quality or authorship scores.

The correction may be a bounded action such as “identify the comparison if the source supports it.” Do not rewrite the passage unless separately asked; any later example must remain within the authorized policy scope. Explicitly retain numbers, units, qualifiers, negation, citations and attribution, technical terms, source quotations, code, mathematics, and proposed/completed distinctions. Never invent specificity, first-person experience, emotion, results, or author verification to make prose appear human. Do not use blacklists, punctuation quotas, forced active voice, forced synonyms, or random sentence-length variation.

Close with actual read/source coverage, unresolved evidence or policy limits, and any requested follow-up. On re-review, compare the new exact candidate with prior findings and report addressed, partly addressed, unresolved, or no longer applicable. State whether review was performed by one assistant or an actual separate reviewer; sequential self-review is not independent review.
