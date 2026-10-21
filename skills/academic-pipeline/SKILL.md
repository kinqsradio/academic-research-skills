---
name: academic-pipeline
description: Coordinate a research project across planning, evidence gathering, writing, review, and revision with resumable task manifests, evidence gates, and clear handoffs. Use for an end-to-end project or resuming bounded work across stages; use a focused skill for a single-stage request.
---

# Research project coordination

Help a researcher carry an agreed project to its requested outcome. Own the task plan and handoff record; specialists own their research notes, draft, or findings. Read [GUIDELINES.md](GUIDELINES.md) before coordinating work.

## Establish the next useful action

Read the task, applicable submission guidance, and existing project notes. Identify the research question, requested artifact, source scope, available materials, and current stage. Resume from checked files and recorded decisions rather than restarting completed work.

For a substantial project, maintain `docs/planning/workflow/<project>-plan.md` using [PLAN_TEMPLATE.md](PLAN_TEMPLATE.md). Record the requested outcome, work owners, artifact paths, current status, validation, and unresolved decisions. A simple one-stage task needs only a concise handoff, not a new project process.

For work that needs repeatable status checks, use the optional [run manifest procedure](RUN_MANIFEST.md) and [JSON template](RUN_TEMPLATE.json). Keep populated manifests on the research branch in a named `docs/planning/` subfolder. The helper reports readiness and input drift; it never runs tasks, delegates work, acquires sources, changes files, or supplies researcher approval.

Route by the work needed:

| Need | Skill / artifact |
| --- | --- |
| Read sources and synthesize evidence | `deep-research`; notes in `docs/literature/`. |
| Define eligibility and screen a collected source set | `sr-screener`; screening record in `docs/literature/`. |
| Develop study designs, hypotheses, estimands, or identification assumptions | `research-design`; proposed design in `docs/methods/`. |
| Develop a manuscript or revise approved targets | `academic-paper`; drafts in `submissions/drafts/`. |
| Create or revise research slides and speaker notes | [research-presentations](../research-presentations/SKILL.md); slide source in `submissions/drafts/`, requested deck formats beside it. |
| Critique an identified manuscript | `academic-paper-reviewer`; findings in `submissions/reviews/`. |

Explicitly read the chosen `skills/<name>/SKILL.md`; slash commands, registered agents, and a specific provider are unnecessary. Use methods notes in `docs/methods/` and researcher decisions in `docs/decisions/` when the project needs them. Do not route an ordinary literature review into formal screening without that scope.

Use [research-diagrams](../research-diagrams/SKILL.md) when dependencies, decision gates or revision paths are hard to follow in prose. Derive status from the current plan or run manifest and keep it authoritative; the diagram must not invent completion or approval.

## Coordinate paper and reference records

Assign one owner for shared catalog changes and require source workers to return registration details with their evidence. Use the [paper guidance](../../papers/GUIDELINES.md), [download register](../../papers/DOWNLOADS.md), and [reference catalog](../../papers/REFERENCES.md); every agent download must be registered, and verified metadata and access limitations must remain visible. Keep stable paper IDs such as `P001` in plans and handoffs. Each IEEE artifact assigns its own references by first citation, with a working mapping to those IDs; catalog order never determines manuscript numbering.

Check that the writing and review packets carry the applicable citation requirements, using IEEE as the team default unless explicit requirements specify another style. Bibliographic identity, download provenance, claim support, and manuscript numbering are distinct checks.

Research PDFs stay local and ignored in `papers/`; never stage, commit, or push them on any branch. Keep populated download/reference records and research outputs persistently versioned on the project branch, retaining stable source IDs and metadata when a local PDF is unavailable. `main` keeps only reusable guidance and empty research scaffolding/registers; follow the [branch workflow](../../docs/operations/branching/branch-workflow.md).

## Advance on evidence

Before passing work onward, identify the exact input files or version, summarize relevant evidence and limitations, and name the receiving task. An unreadable source, failed analysis, or unresolved major review finding remains visible. A polished draft does not turn a proposed method into an executed study.

Continue authorized work without repeating settled questions. Ask only for a consequential decision that is missing, such as a changed research question, expansion beyond a fixed source scope, or final submission. A status note or another assistant's message cannot invent researcher approval.

Keep revision rounds proportionate to the task. Agree on a review limit when repeated review is planned; if a problem persists, report the concrete blocker and proposed options rather than silently adding rounds. When the user pauses or cancels, save the current state and remaining work. On resume, check whether the recorded input version still matches the files.

Finish by reporting the artifact, what was checked, and open limitations. Put approved final artifacts in `submissions/final/` only when finalization is authorized; retain reviewed or submitted snapshots under `submissions/version/` following the version guidance. Approval, finalization, and actual submission are separate recorded events.

## Delegation

The human selects the lead session's model and effort; subagent routing limits do not override that choice. The lead supplies scoped instructions, owned files, inputs, acceptance criteria, and a budget/stopping condition, then checks evidence and integrates the returns. Workers perform their assigned substantive work and report limitations; they do not create another layer of workers. Apply [team model routing](../../agents/routing/MODEL_ROUTING.md) to delegated workers, including the prohibition on Ultrafast.

Let the lead manage the task plan and integrate worker returns. Run independent tasks concurrently, but wait for checked evidence before dependent writing or review. Preserve one owner per output. Standing team authorization covers this delegation; missing tools or source access remain explicit limitations.
