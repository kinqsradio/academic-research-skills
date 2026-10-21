# Codex and Claude setup

Status: explicit file-loading workflow; local source and structure checks do not establish live provider execution. Updated 2026-10-10.

The canonical skills live only in `skills/`. Each has standard `name` and `description` frontmatter and a Markdown workflow without mandatory provider APIs, model names, startup hooks, or plugins. The repository uses explicit path loading rather than generated discovery entries or registered project subagent profiles.

## Load a workflow

Open the repository in the chosen tool. Read `AGENTS.md`, root `GUIDELINES.md`, and the relevant folder guidelines. Claude also has the root `CLAUDE.md` entrypoint. Choose a procedure from [the skill index](../../../skills/GUIDELINES.md), then explicitly ask the assistant to read its canonical path, for example:

> Read skills/deep-research/SKILL.md and apply that workflow to the task below.

Do not assume a short skill name selects this repository's procedure when similarly named personal skills exist. Supporting links resolve from the canonical skill file. Edit the files in `skills/` directly; no discovery generator or global installation is needed. Official background: [Codex skills](https://learn.chatgpt.com/docs/build-skills), [Claude skills](https://code.claude.com/docs/en/skills), and [Claude project instructions](https://code.claude.com/docs/en/memory).

## Maintenance and validation

Run from the repository root with Python 3.10 or later:

```sh
python3 scripts/validate_repository.py
```

On Windows, use `py -3` or `python` if it selects Python 3.10 or later. This structural check does not establish successful skill loading, provider access, source reading, or Windows execution.

## Capability limits and smoke check

The skill specifies research work, not a particular tool implementation. File reading is needed for local sources; PDF extraction, web access, document rendering, and isolated workers depend on the environment. Report a missing capability. Repeated analysis in the same conversation is not independent review.

In a fresh Codex session and a fresh Claude Code session, run this read-only check:

> Read skills/deep-research/SKILL.md and the applicable folder guidelines. Explain where source downloads, evidence notes, and manuscript drafts belong. Identify required inputs for a local-PDF synthesis, but do not read the PDFs, create research artifacts, download anything, or call another agent.

Expected: the canonical file is loaded; papers go in `papers/`, notes in `docs/literature/`, and manuscripts in `submissions/drafts/`; the question and source scope are identified. Then use a small permitted source sample to verify actual PDF reading and citation locators. Static validation and a text walkthrough do not establish a live Codex/Claude or Windows test.

## Session-selected research subagents

The human selects and may change the lead model and effort. Leave those settings under human control; the routing tables apply only to workers. The lead primarily assigns, guides, checks, and integrates delegated work, with small direct corrections where useful.

Start with [the routing index](../../../agents/routing/MODEL_ROUTING.md), then explicitly read [Codex routing](../../../agents/routing/CODEX.md) or [Claude routing](../../../agents/routing/CLAUDE.md). Use [shared team roles and handoffs](../../../agents/README.md) for task packets, file ownership, concurrency, escalation, and receipts. Scout, analyst, reviewer, specialist, and frontier worker are responsibility labels; select the actual available model and effort through the session's supported controls.

Pass the worker its bounded task, relevant skill path, provider routing path, exact inputs, allowed outputs, and acceptance criteria. Check the effective model, effort, tool permissions, and service tier where exposed. Never use Ultrafast. If model or effort selection is unavailable, report that limit and choose an explicitly identified supported arrangement; do not silently claim the requested configuration ran. Official background: [Codex subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents), [Codex configuration keys](https://learn.chatgpt.com/docs/config-file/config-reference), and [Claude subagents](https://code.claude.com/docs/en/sub-agents).

Check the installed client version, account access, and supported effort controls before dispatch. Provider documentation and role recommendations do not establish that a model is callable in the current session.

After confirming session availability, delegate a read-only smoke check:

> Assign a scout worker using the available model and effort selected under agents/routing/CODEX.md or agents/routing/CLAUDE.md. Have it read root GUIDELINES.md and report where downloads, evidence notes, and manuscript drafts belong. It must state its effective model and effort if exposed, or mark them unknown. Do not create files or download sources. Check its answer before continuing.

Then test an analyst on a disposable artifact and a reviewer on that frozen artifact. Confirm tool permissions, model/effort resolution, source locators, and actual usage. Do not use a paid frontier worker merely to test that a file exists. Record any supported fallback and keep live checks distinct from structural validation.
