# Team roles and handoffs

Roles describe responsibilities, not specific models or tools. The lead primarily coordinates, gives workers bounded assignments, checks their outputs, and integrates the accepted work. The lead may do trivial work and small integration corrections directly; for substantial independent work, delegate the main assignment instead of taking it over. Use one contributor for simple or serial work. For substantial work with independent, bounded parts, use delegation by default under the user's standing authorization and the available host tools; do not ask again for authorization already given. Follow the model and effort limits in [model routing](routing/MODEL_ROUTING.md) for delegated workers.

The human selects and may change the lead's model and effort. The lead must preserve that choice and must not automatically switch models or providers. Provider model and effort limits in the routing guides apply only to delegated workers.

Use up to two delegated workers concurrently by default, with an absolute cap of three or any lower host limit. Delegate only work that can proceed independently. Do not create nested worker teams by default. The coordinator owns scope, integration, and final evidence checks.

| Role | Responsibility | Reviewable output |
| --- | --- | --- |
| Human research lead / author | Own scope, research question, course compliance, decisions, and final approval; select the assistant lead model and effort. | Accepted scope and decisions with unresolved questions. |
| Assistant lead / orchestrator | Plan assignments, guide workers, check evidence and acceptance criteria, resolve integration issues, and report to the human. | Reviewed integrated result, validation evidence, and unresolved issues. |
| Evidence researcher | Locate and read sources; verify metadata and claim support. | Source records, locators, search criteria, and limitations. |
| Methods analyst | Assess design, assumptions, analysis, and reproducibility. | Methods notes, analysis evidence, and untested assumptions. |
| Writer / editor | Produce coherent text grounded in verified evidence. | Draft with citations and marked evidence gaps. |
| Reviewer | Check claims, methods, citations, consistency, and requirements. | Findings tied to exact files and a clearly identified draft. |
| Repository maintainer | Maintain paths, shared instructions, workflows, and tooling. | Scoped changes with appropriate checks. |

Follow the canonical [branch and attribution policy](../docs/operations/branching/branch-workflow.md#provider-neutral-names-and-attribution) when preparing commits or PRs: use `research/<project>` and `template/<change>`, keep branch names and PR titles provider-neutral, and omit automated assistant attribution. Preserve required academic AI-use disclosures and factual validation records.

## Task assignment

Give each worker one bounded outcome, a named owner, disjoint output paths, exact input files or versions, relevant scope decisions, evidence sources, constraints, and review criteria. Keep the context packet to what the assignment needs; do not pass the full conversation by default. State which claims, decisions, or changes require escalation. Tell each worker to execute its assigned work and return a receipt; the lead owns coordination and final integration. Workers must not take over orchestration or spawn further agents unless explicitly assigned.

Set a task budget proportional to its importance and uncertainty, using a concrete bound such as source or record count, time, or tokens when the host exposes it. Keep the planned limit distinct from actual usage. If usage is not available, say so rather than presenting an estimate as measured. Limit routine repair to one targeted pass after identifying the problem; if it persists, stop and escalate the evidence and decision needed instead of retrying blindly.

## Handoff receipt

Return a compact receipt with each assignment:

- **Outcome:** completed, partial, or blocked, and the assigned task.
- **Inputs:** exact paths or versions examined and the scope covered.
- **Evidence:** claim or decision, source locator (page, section, table, figure, or stable identifier), and brief support; include analysis inputs and commands where applicable.
- **Files:** paths created or changed.
- **Validation:** checks actually performed and results; distinguish automated, manual, and separate-review work.
- **Limits and escalation:** unreadable or unavailable evidence, assumptions, open issues, and the specific decision or input needed next.

The coordinator integrates receipts, checks consequential claims against their sources, and rechecks any revised output against the accepted criteria. Sequential self-review, several role perspectives in one context, or agreement among workers does not establish independent error processes or independent peer review. Record the actual reviewer arrangement and do not present consensus as proof.

A role assignment does not grant permission to contact others, access unavailable services, send material to an external provider, submit work, or publish. Follow any additional authorization required for those actions. Escalate unresolved evidence or course-policy questions to the human author. If work is paused or cancelled, preserve the draft and handoff state. Do not describe an unperformed check, approval, submission, or publication as complete.

## Integration and escalation

For writing, keep one draft owner and separate evidence/review outputs. For source research, divide non-overlapping papers or questions. Dual screening uses separate initial decisions under the same protocol without exposing one reviewer's answer to the other; qualify the arrangement with a pilot and preserve human adjudication.

First distinguish missing input or tool access from a reasoning failure. After one targeted repair, allow one bounded escalation to a suitable model under the selected provider guide. If the issue remains unresolved, stop that branch and report the limitation or human decision needed. A stronger model can be the initial choice for a clearly demanding task; a deliberately inadequate first attempt is unnecessary. Never treat worker agreement as proof or a more expensive model as a remedy for missing evidence.

Keep context packets small and reuse verified extraction artifacts, but reopen sources for consequential claims. Measure total usage per accepted result, including repeated context, reasoning when reported, repair, integration and review; mark unavailable data unknown. Before changing routing defaults, compare representative metadata, conflicting-evidence and claim-review tasks against known expectations. Assess factual errors, missed material findings and correction work alongside usage; do not invent savings percentages or assume effort labels are equivalent across providers.
