# Codex model and effort routing

Team policy, updated 2026-10-10. Use with the [shared workflow](../README.md) and [routing index](MODEL_ROUTING.md). These assignments are policy choices, not measured rankings of research ability; see [model-selection evidence](../../docs/operations/setup/model-selection.md).

The human selects and may change the lead's Codex model and effort. Preserve the selected primary model and effort; do not override them or automatically switch the lead to another model or provider. The recommendations and hard limits below apply only to delegated workers. Use them to choose economical worker assignments while the lead coordinates, checks, and integrates their work.

## Assignments

| Work | Model and effort | Session assignment |
| --- | --- | --- |
| Inventory, metadata, passage location, link checks | Luna low | Scout |
| Evidence extraction and bounded screening under a piloted protocol | Luna medium; high when extraction or criteria are difficult | Explicit spawn; use Sol medium for complex interpretation. |
| Evidence synthesis, section drafting, precise revision | Sol medium | Analyst |
| Consequential claim checks and review of a frozen draft in a separate context | Sol medium | Reviewer |
| A named difficult methodological or cross-source issue | Astra low | Specialist; medium only for justified escalation. |
| Exceptional difficult extraction or analysis suited to Luna | Luna max | Explicit, bounded exception with a recorded reason and acceptance checks. |

Sol must use **low or medium only**. This is a hard ceiling; never raise Sol to high, xhigh, or max. For simple Sol work, low is permitted. Luna low is the scouting default; medium/high extraction must be chosen explicitly, and max is exceptional.

Astra defaults to **low**. Use medium only when a named issue justifies it. Do not use Astra high, xhigh, or max by default. Clearly demanding work may start with Astra without forcing a failed cheaper attempt; routine work needs no Astra review.

## Escalation and verification

Check whether a failure is missing input, tool/access trouble, or a reasoning gap. A stronger model cannot repair an unavailable source. Allow one targeted repair naming the failed criterion, then one escalation of the bounded issue and relevant evidence. Stop if unresolved; preserve the limitation and required human decision. Escalating from Sol must respect its medium ceiling, using Astra when stronger reasoning is justified.

The lead verifies consequential claims against source content and locators. Screening choices must pass a representative pilot and retain human adjudication. Agreement among workers is not proof. Use [README.md](../README.md) for review arrangements, output ownership, and shared task packets.

Record the actual model, effort, source coverage, unresolved issues, and token/tool/time usage when exposed; mark unavailable usage unknown. Include repair, parent integration, and verification when comparing cost per accepted task. Validate routing changes with representative tasks rather than asserting universal savings.

## Session selection and availability

These limits are team instructions; session selection and verification are required because this repository contains no configuration that enforces them.

Read this file and the relevant `skills/<skill-name>/SKILL.md` by explicit path. Select the worker model and effort using the current session's supported delegation controls; the assignment labels above describe responsibilities, not registered profiles. Before dispatch, check the resolved model, effort, and effective service tier. **Never use Ultrafast.**

Check whether the current Codex session exposes Luna, Sol, and Astra before assigning a worker. Use the [setup checks](../../docs/operations/setup/assistant-setup.md). If a model is unavailable, identify an available alternative within the task's requirements and report the substitution; never silently map to another generation, higher cost, or weaker review arrangement.
