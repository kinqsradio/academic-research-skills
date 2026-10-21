# Model selection evidence

Date: 2026-10-10. Status: provider documentation checked; research-team routing proposed and not benchmarked in this repository. Purpose: explain the evidence behind [the team routing policy](../../../agents/routing/MODEL_ROUTING.md), which owns assignments and escalation rules.

## Documented capabilities

| Provider / model | Exact model ID | Documented positioning | Qualitative cost / speed |
| --- | --- | --- | --- |
| OpenAI GPT-6 Luna | `gpt-6-luna` | Focused, high-volume tasks; scoped work and extraction. | Most efficient OpenAI option in this selection. |
| OpenAI GPT-6.1 Sol | `gpt-6.1-sol` | Complex coding and professional work with near-Astra performance. | Lower cost than Astra; compare quality on the same task. |
| OpenAI GPT-6 Astra | `gpt-6-astra` | Most demanding reasoning, research and document creation. | Highest capability tier; higher resource commitment. |
| Anthropic Claude Sonnet 5.5 | `claude-sonnet-5-5` | Everyday coding, data analysis, content and agent work. | Fast; lower base token price than Opus and Fable. |
| Anthropic Claude Opus 5.5 | `claude-opus-5-5` | Long-running agentic coding and knowledge work. | Moderate latency; middle base token price in this Claude selection. |
| Anthropic Claude Fable 5.1 | `claude-fable-5-1` | Demanding reasoning, multistep research and long-horizon work. | Slower; highest base token price in this Claude selection. |

Sources and locators: OpenAI [Luna](https://developers.openai.com/api/docs/models/gpt-6-luna), [Sol](https://developers.openai.com/api/docs/models/gpt-6.1-sol), and [Astra](https://developers.openai.com/api/docs/models/gpt-6-astra), model overview descriptions; [model-selection guide](https://developers.openai.com/api/docs/guides/model-selection), “When to consider GPT-6.1 Sol” and “How to think about models and reasoning effort.” Claude [model comparison](https://platform.claude.com/docs/en/models/overview), “Compare models”; [model-selection guide](https://platform.claude.com/docs/en/about-claude/models/choosing-a-model), “Model selection matrix.” These are provider claims, not measured research performance here or cross-provider equivalence.

Fable 5.1 is documented as active, released 2026-09-01, with Claude API and cloud-platform availability. Its overview includes research and finished document work. Anthropic suggests Opus 5.5 as a starting point and Fable for demanding tasks that still miss the quality bar at higher Opus effort. See [Fable overview](https://platform.claude.com/docs/en/models/fable-5-1/overview), “Overview” and “Availability.” This does not establish access for this account.

## Team recommendations

Use [MODEL_ROUTING.md](../../../agents/routing/MODEL_ROUTING.md) as the index; [Codex routing](../../../agents/routing/CODEX.md) and [Claude routing](../../../agents/routing/CLAUDE.md) own provider-specific worker assignments and effort limits. The human selects and may change the lead model and effort; these worker defaults do not override the primary session. The following rationale is our recommendation, not a provider guarantee:

- Use Luna low/medium or Sonnet medium for bounded evidence extraction, source-locator checks, mechanical edits and protocol-based screening with clear acceptance criteria; follow the routing table for complex criteria and pilots.
- Use Sol medium or Sonnet medium for routine coordinated synthesis, drafting and separate substantive review. Sol remains limited to low or medium effort under the user's constraint.
- Start difficult specialist work at Astra low or Opus medium. Astra medium or Opus high requires a named reasoning gap. Start exceptional Fable work at low and consider medium only if needed. Do not default Astra or Fable to high, xhigh, or max; highest settings are outside the normal routing policy.
- Keep source verification at every tier. A stronger model cannot establish a claim from an unread source, resolve a human research decision, or supply missing assessment policy.

These pairings express responsibility tiers, not equal capabilities. A reviewer requires a separate review context and an identified artifact version; changing the model during self-review does not make review independent.

## Claude session controls

Select model and effort explicitly through the current session's supported controls after loading the routing and skill paths. The repository registers no project subagent definitions. Claude documents model aliases `sonnet`, `opus`, `haiku`, `fable`, full IDs, and `inherit`; effort supports `low`, `medium`, `high`, `xhigh`, `max`, subject to model support. Documented native model precedence is invocation, definition if supplied elsewhere, `CLAUDE_CODE_SUBAGENT_MODEL`, then parent. `CLAUDE_CODE_SUBAGENT_MODEL_FORCE=1` can override routing. `CLAUDE_CODE_EFFORT_LEVEL` overrides invocation and any definition effort. Per-invocation effort requires v2.1.292. See [subagent documentation](https://code.claude.com/docs/en/sub-agents), “Frontmatter reference,” “Choose a model,” and “Choose an effort level.”

On the Anthropic API, current aliases select Sonnet/Opus 5.5 and Fable 5.1; some providers and gateways resolve older versions. Prefer explicit IDs for recorded assignments. Minimum Claude Code versions: Fable 5.1 v2.1.257, Opus 5.5 v2.1.280, Sonnet 5.5 v2.1.284. Claude Code defaults Sonnet/Opus 5.5 to medium; the platform API lists Sonnet's default as high. Set effort explicitly. See [model configuration](https://code.claude.com/docs/en/model-config), “Model aliases,” “Work with Fable,” and “Adjust effort level.”

Built-in Explore and Plan have their own model behavior and do not establish our selected research assignments. Explore may inherit an expensive parent; select a lower-cost worker explicitly through supported controls and verify the effective settings. Source: [built-in subagents](https://code.claude.com/docs/en/sub-agents#built-in-subagents).

## Availability and measurement

API specifications do not establish Codex or Claude subscription access, host tool support, model allowlists, or available effort levels. Check the actual host before dispatch, record requested and effective model/effort, and report substitutions. An instruction naming a model does not make it callable. OpenAI explicitly distinguishes availability by product/version in its [selection guide](https://developers.openai.com/api/docs/guides/model-selection), model-line descriptions. Claude provider aliases, environment overrides, organization restrictions and Fable usage-credit requirements are documented in [model configuration](https://code.claude.com/docs/en/model-config), “Model aliases,” “Fable and usage credits,” and “Restrict model selection.”

Use qualitative costs here because rates and billing modes change, and OpenAI pages inspected during setup did not present fully consistent dollar rates. Recheck current provider pricing before any budget decision. API rates do not translate directly into subscription usage limits or actual charged cost.

Optimize total usage per accepted result. Include the coordinator, every worker, reasoning/output tokens, repeated context, retries and review; report cached and uncached input separately when available. Compare acceptance, errors, elapsed time and actual billed cost or subscription usage on identical tasks. Do not claim a token-saving percentage without measurements. Smaller token price or more parallel workers alone does not prove lower total cost.

Anthropic recommends trimming context and using caching, measuring cost per completed task, and evaluating model/effort tradeoffs locally. Its examples are directional provider benchmarks. See [cost optimization](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence), “Start here” and “Cut spend without losing quality.” OpenAI recommends comparing identical inputs and retaining the lightest setting meeting the quality bar in [model selection](https://developers.openai.com/api/docs/guides/model-selection), “Experiment.”

## Validation limits

Official pages were opened and relevant sections inspected on the date above. No six-model repository benchmark, subscription-cost experiment, or live execution of the proposed session-selected assignments has been completed. Remaining checks: installed host versions, account/provider model access, effective environment overrides, session-selected worker invocation and accepted-task usage measurements. Revisit this record when provider models, aliases or local access change.

Verify the active client and provider access before live qualification; follow [assistant setup](assistant-setup.md).
