# Team research skills

These twelve skills are the canonical English workflows for our research team. Each skill has one main responsibility and a small set of supporting files. Read the selected SKILL.md and its folder guidance; do not load the whole library by default.

| Skill | Use it for | Main output |
| --- | --- | --- |
| [deep-research](deep-research/SKILL.md) | Investigate a question and compare source evidence. | Evidence records and synthesis in docs/literature/. |
| [research-design](research-design/SKILL.md) | Specify or audit a study design and preregistration readiness without executing or registering it. | Versioned design and open decisions in docs/methods/. |
| [academic-paper](academic-paper/SKILL.md) | Plan, draft, or revise a manuscript using available evidence. | Writing in submissions/drafts/. |
| [research-presentations](research-presentations/SKILL.md) | Plan, create, revise or review evidence-based research slides and speaker notes. | Canonical slide source in submissions/drafts/, plus explicitly requested deck formats. |
| [generative-ai-use](generative-ai-use/SKILL.md) | Prepare an evidence-based Generative AI Use appendix for a final submission. | Disclosure draft in submissions/drafts/ and a supporting use record in docs/planning/. |
| [academic-paper-reviewer](academic-paper-reviewer/SKILL.md) | Assess an identified draft without rewriting it. | Findings in submissions/reviews/. |
| [prose-quality-review](prose-quality-review/SKILL.md) | Check a draft for vague, repetitive, inflated, or formulaic prose while preserving meaning. | Focused findings in chat or submissions/reviews/. |
| [sr-screener](sr-screener/SKILL.md) | Apply explicit eligibility criteria to study records. | Screening decisions and counts in docs/literature/. |
| [research-diagrams](research-diagrams/SKILL.md) | Clarify research concepts, methods, selection flows and dependencies with evidence-aware Mermaid diagrams when useful. | Mermaid source and text explanations alongside the relevant Markdown record. |
| [skill-creator](skill-creator/SKILL.md) | Create or improve a portable team skill and validate its behavior. | Maintained workflows in skills/. |
| [orbyn](orbyn/SKILL.md) | Reconcile Orbyn briefs, rubrics, documents, tasks, and user edits with repository work when accessible and authorized. | Versioned source snapshots and verified per-item reconciliation status, or a repository-only fallback. |
| [academic-pipeline](academic-pipeline/SKILL.md) | Coordinate a task spanning research, writing, and review. | Task status and handoffs in docs/planning/. |

A literature review request routes by purpose: evidence discovery and synthesis use deep-research; composing a manuscript section from evidence uses academic-paper. Screening is appropriate only when eligibility decisions are requested. Use coordination only for a task that crosses stages.

Maintain name and description YAML fields in SKILL.md. Use relative Markdown links, English guidance, and capabilities such as reading files or searching sources rather than mandatory tool APIs. Use the shared [model routing policy](../agents/routing/MODEL_ROUTING.md) for role/model choices; keep provider-specific IDs out of the research procedures. Shared rules live in AGENTS.md. Load each selected SKILL.md directly by path in either assistant; automatic skill discovery is not configured by this repository.

Research prose and manuscript outputs use canonical Markdown in the repository; export or transfer to a shared document only when requested. Structured research records may use CSV or JSON.

Team manuscripts and evidence reports use IEEE references unless an explicit brief, venue rule, or author instruction requires another style. The canonical [paper guidance](../papers/GUIDELINES.md), [download register](../papers/DOWNLOADS.md), and [reference catalog](../papers/REFERENCES.md) govern paper registration. Stable catalog IDs and artifact-specific first-citation numbers serve different purposes. Research PDFs stay local and ignored in papers/ and must never be staged, committed, or pushed on any branch; source metadata remains persistently versioned on the research branch even when a local PDF is unavailable.

The lead gives bounded worker instructions, checks acceptance criteria, and integrates substantive returns. Workers do not create nested delegations. The human chooses the lead model and effort; the routing policy governs delegated workers. Never use Ultrafast. For skill creation or maintenance, use skill-creator rather than treating a research workflow as an authoring template. Promote new or improved reusable skills to `main` only through reviewed template-only commits under the [branch workflow](../docs/operations/branching/branch-workflow.md); never merge a research branch into `main`. Keep populated research records and writing on the project branch and only empty research scaffolding/registers in the template.

Follow the canonical [branch and attribution policy](../docs/operations/branching/branch-workflow.md#provider-neutral-names-and-attribution): use `research/<project>` for research and `template/<change>` for reusable improvements. Keep branch names and PR titles provider-neutral and omit automated assistant attribution in commits and PRs. Required academic AI-use disclosures remain applicable.

Every reusable skill change, including gap fixes, renames, deletions, and supporting resources, must follow [paired skill synchronization](../docs/operations/branching/skill-synchronization.md) in the same maintenance task. It governs the designated public/private pair, publication gates, and propagation into every active private `research/*` branch; report incomplete or blocked synchronization explicitly.

For repeatable multi-stage work, academic-pipeline includes a machine-readable run manifest and read-only readiness checker. It checks dependencies, input versions, and recorded gates; it does not execute research or certify evidence. Use the reviewer's claim/exhibit audit for source support and exact-candidate coverage.
