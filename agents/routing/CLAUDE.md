# Claude model and effort routing

Team policy, updated 2026-10-10. Use with the [shared workflow](../README.md) and [routing index](MODEL_ROUTING.md). These assignments are policy choices, not measured rankings of research ability; see [model-selection evidence](../../docs/operations/setup/model-selection.md). Claude effort labels do not imply equivalent Codex compute or quality.

The human selects and may change the lead's Claude model and effort. Preserve the selected primary model and effort; do not override them or automatically switch the lead to another model or provider. The recommendations and limits below apply only to delegated workers. Use them to choose economical worker assignments while the lead coordinates, checks, and integrates their work.

## Assignments

| Work | Model and effort | Session assignment |
| --- | --- | --- |
| Inventory, metadata, passage location, link checks | Sonnet medium; low permitted for simple tasks | Scout; explicit dispatch for low. |
| Evidence extraction and bounded screening under a piloted protocol | Sonnet medium | Analyst with a bounded extraction or screening assignment. |
| Evidence synthesis, section drafting, precise revision | Sonnet medium | Analyst |
| Consequential claim checks and review of a frozen draft in a separate context | Sonnet medium | Reviewer |
| A named difficult methodological or cross-source issue | Opus medium | Specialist; high only for a named difficult issue with justification. |
| Exceptional long-horizon or unresolved analysis | Fable low | Frontier worker; medium only for justified escalation. |

Sonnet **medium** is the routine default. Low is permitted when a simple task can pass its checks. Opus defaults to **medium**; high requires a named difficult issue, bounded evidence, acceptance criteria, and a recorded reason. Do not select high just because the role is specialist.

Fable defaults to **low** and is reserved for a named blocker or clearly demanding task. Use medium for justified escalation. Do not use Fable high, xhigh, or max by default; routine work needs no Fable review. These are independent Claude choices, not equivalents of Luna, Sol, or Astra assignments.

## Escalation and verification

Check whether a failure is missing input, tool/access trouble, or a reasoning gap. A stronger model cannot repair an unavailable source. Allow one targeted repair naming the failed criterion, then one escalation of the bounded issue and relevant evidence. Stop if unresolved; preserve the limitation and required human decision. A demanding task may justify starting with Opus or Fable without forcing a failed Sonnet attempt.

The lead verifies consequential claims against source content and locators. Screening choices must pass a representative pilot and retain human adjudication. Agreement among workers is not proof. Use [README.md](../README.md) for review arrangements, output ownership, and shared task packets.

Record the actual model, effort, source coverage, unresolved issues, and token/tool/time usage when exposed; mark unavailable usage unknown. Include repair, parent integration, and verification when comparing cost per accepted task. Validate routing changes with representative tasks rather than asserting universal savings.

## Session selection and availability

These limits are team instructions; session selection and verification are required because this repository contains no configuration that enforces them.

Read this file and the relevant `skills/<skill-name>/SKILL.md` by explicit path. Select the worker model and effort using the current session's supported delegation controls; the assignment labels above describe responsibilities, not registered profiles. Before dispatch, check the resolved model, effort, provider access, and any exposed service tier. **Never use Ultrafast.**

The routing recommendations do not establish which models can run in the current environment. Use the [setup checks](../../docs/operations/setup/assistant-setup.md) to verify version, provider access, model, and effort. If a model is unavailable, identify an available alternative within the task's requirements and report the substitution; never silently map to another generation, higher cost, or weaker review arrangement.
