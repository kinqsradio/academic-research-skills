# Model routing index

Team policy, updated 2026-10-10. Choose the provider already in use, then read its routing file:

| Provider | Model and effort policy |
| --- | --- |
| Codex | [CODEX.md](CODEX.md): Luna, Sol, and Astra. |
| Claude | [CLAUDE.md](CLAUDE.md): Sonnet, Opus, and Fable. |

These are independent policies. Effort labels, price, and performance are not equivalent across providers. Do not run both providers or switch providers merely to obtain another opinion. The human selects and may change the lead's model and effort; the lead preserves that selection and does not automatically change the primary model or provider. The model and effort limits below apply only to delegated workers.

Use the [shared team workflow](../README.md) for roles, concurrency, bounded task packets, ownership, evidence checks, review arrangements, and handoff receipts. Keep simple work direct; delegate substantial independent work under the team's standing authorization.

Start with the lightest available model and effort likely to meet the acceptance criteria. A demanding task may justify a stronger initial choice. Routine work needs no frontier-model review.

Delegated-worker limits:

- Sol has a hard effort ceiling of medium. Luna max is an exception, not a default.
- Astra and Fable default to low; use medium for a named difficult issue. Do not default to high, xhigh, or max.
- Never use Ultrafast. Check the resolved model, effort, and service tier before dispatch.
- Diagnose missing evidence and access failures first; a stronger model cannot restore an unavailable source or authorize an ethics decision.
- Allow one targeted repair, then one justified escalation. Stop if unresolved and record the required human decision or missing input.
- Record actual model, effort, source coverage, and measured usage where exposed; mark unavailable usage unknown. Compare total work per accepted task, including repair and integration.

See [model-selection evidence](../../docs/operations/setup/model-selection.md) for capabilities versus team recommendations and [setup checks](../../docs/operations/setup/assistant-setup.md) for live availability. Documented role choices do not establish provider access or successful execution.
