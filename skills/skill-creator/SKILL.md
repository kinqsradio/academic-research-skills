---
name: skill-creator
description: Create or improve an original team skill with a focused workflow, necessary supporting resources, and structural and behavioral checks. Use for reusable instructions in skills/, rather than executing a one-off research or manuscript task.
---

# Create a team skill

Turn a recurring task into instructions another capable assistant can follow with the inputs and tools actually available. Maintain the canonical skill in `skills/<name>/`; the same file must be readable by path in Codex and Claude. Read [folder guidance](GUIDELINES.md) and the [skill index](../GUIDELINES.md) before writing.

## Choose the boundary

Identify the repeated request, intended output, likely inputs, and decisions the skill should improve. Inspect the existing skill before updating it. Use supplied examples and project context to proceed; ask only when missing information changes the workflow or destination. A one-off task does not require a new skill.

Give the skill one recognizable responsibility. Check adjacent skills in the index to avoid overlapping triggers. Its description should explain when to select it; its body should describe how to produce the requested outcome. Preserve explicit user scope, settled research decisions, existing authorization, and unrelated resources. A skill cannot grant permission for external actions, submission, or confidential uploads.

## Author the smallest useful workflow

Use a lowercase hyphenated folder name and matching YAML `name`, with a concise `description` in `SKILL.md` frontmatter. Write the team's own English instructions. Preserve source titles or quotations accurately and label translations when citation accuracy matters.

Use canonical Markdown for research prose and manuscript outputs, following the root format policy. Allow structured records and explicitly requested exports without requiring proprietary editors or cloud access.

Explain the required inputs, output location, material decisions, evidence requirements, and handoff. Use capabilities such as reading a file, checking source metadata, or searching a publication record. Avoid mandatory proprietary APIs, provider model IDs, host-specific paths, hidden adapter directories, or claims that host auto-discovery is configured. Missing capabilities should result in an accurately described limitation and usable partial work where possible.

Keep the entrypoint short enough to read for an ordinary task. Add a template, reference, or executable helper only when it materially supports repeated work. Link conditional resources where they are needed and explain when to load them. Add meaningful `GUIDELINES.md` to every new maintained folder. Shared team rules belong in root instructions or their canonical policy files, rather than copies that can drift.

Place research records in the appropriate `docs/` category and manuscripts or reviews in `submissions/`. Workflows that acquire or cite papers must link [paper guidance](../../papers/GUIDELINES.md), the [download register](../../papers/DOWNLOADS.md), and the [reference catalog](../../papers/REFERENCES.md). Require registration of every agent download, verified metadata and provenance, size and SHA-256 checksum for successfully verified local PDFs, and explicit unknown fields for uncomputed legacy values. Keep research PDFs local and ignored in papers/; never stage, commit, or push them on any branch. Keep source metadata persistently versioned on the research branch and retain stable IDs when local files are unavailable. Use stable paper IDs independently of IEEE reference numbers assigned in each artifact's first-citation order; do not duplicate the catalog schema inside a new skill.

## Design coordination when needed

Keep simple tasks direct. For substantial independent work, use the [shared team workflow](../../agents/README.md) and [model routing policy](../../agents/routing/MODEL_ROUTING.md), reading only the selected host's provider guide. The human selects the lead model and effort; subagent routing constraints apply to workers and do not override that lead choice. Never use Ultrafast.

The lead gives workers substantive, bounded tasks with owned files, inputs, acceptance criteria, and a budget/stopping condition. Workers return their work and limitations without nested delegation. The lead checks evidence and acceptance criteria and integrates the result. If a separate evaluation is warranted, provide the evaluator with a realistic request, the skill, and raw inputs; avoid supplying the desired answer. Keep evaluation outputs isolated from maintained research. Disclose whether review used a separate worker or sequential self-review.

## Validate what was authored

Read the complete skill and check that the trigger, workflow, resources, and output agree. Inspect every changed relative link, name/frontmatter, new folder guideline, and supporting template. Run the repository's structural validator from the root:

```sh
python3 scripts/validate_repository.py
```

Run new or changed helpers on representative safe inputs and inspect their outputs. For a substantial workflow, exercise a realistic request and an important failure or missing-input case, checking observable outcomes rather than matching wording. A paper workflow should preserve unknown metadata and keep paper IDs distinct from document references; a coordinating workflow should retain ownership and evidence gates.

Revise only demonstrated gaps. Structural checks establish file conventions, behavioral exercises establish performance on those cases, and live Codex or Claude invocation establishes only the host behavior actually observed. Do not label an unrun check as passed or self-review as independent validation.

## Deliver the maintained skill

Follow [the branch workflow](../../docs/operations/branching/branch-workflow.md) and its canonical [provider-neutral naming and attribution policy](../../docs/operations/branching/branch-workflow.md#provider-neutral-names-and-attribution). Use `template/<change>` for reusable improvements and `research/<project>` for research; keep branch names and PR titles provider-neutral and omit automated assistant attribution in commits and PRs. Preserve required academic AI-use disclosures. Promote new or improved reusable skills to `main` only in reviewed, dedicated template-only commits; never merge a research branch into `main`. Keep populated registers, research records, and writing on the project branch, and keep research PDFs local and ignored on every branch. Preserve empty research scaffolding and registers on `main`. Update the index when adding, renaming, or changing the purpose of a skill. Keep related templates and cross-links consistent. Report changed paths, the intended use, checks performed, and remaining capability or evidence limits. Do not describe the skill as installed, automatically registered, committed, or pushed unless that action occurred.

New or updated reusable skills must be synchronized from `main` into every active `research/*` branch in the same maintenance task. Validate each branch and confirm its canonical `skills/` matches `main`; report blocked or intentionally archived branches explicitly. Follow the branch workflow for merging, preserving project records, and authorized pushes.
