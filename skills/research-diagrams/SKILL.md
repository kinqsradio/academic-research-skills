---
name: research-diagrams
description: Create or revise an evidence-aware Mermaid diagram for a research explanation, process, or conceptual model when a visual clarifies relationships or decisions.
---

# Research diagrams

Use a diagram when it makes a research argument, method, workflow, or set of relationships easier to inspect. If prose or a small table communicates the point more clearly, use that instead. This skill creates an explanatory diagram; it does not establish that a research claim is true or that a method has been executed.

Read [folder guidance](GUIDELINES.md) before using or maintaining this skill.

## Define the figure

Identify the audience, the question the figure answers, its unit of analysis, and the exact draft or evidence records it represents. Choose a suitable Mermaid form, such as a flowchart for decisions, a sequence diagram for interactions, or a timeline for ordered events. Keep one central purpose per figure. For quantitative scientific plots, use plotting tools and the verified dataset rather than drawing approximate values in Mermaid.

Place the canonical fenced `mermaid` source, caption, and accompanying explanation in the appropriate purpose-based Markdown subfolder: working evidence or process records under `docs/`, manuscript figures under `submissions/drafts/`, and review findings under `submissions/reviews/`. Read the destination folder's `GUIDELINES.md`; create one for any new maintained folder. Keep paths and links repository-relative. Create image, PDF, or cloud exports only when the task requests them.

## Trace the content

Map each substantive node, arrow, count, and label to a source or project record. Record page, section, table, figure, row, or decision-log locators close to the figure. Distinguish observed or source-supported relationships from interpretations, hypotheses, and proposed steps in the labels, legend, or caption. Do not present an association as an established causal effect. A proposed causal model may include assumed causal arrows, but label them as assumptions requiring methodological review rather than findings. Mark unknown or disputed links rather than completing the picture by guesswork.

Calculate any displayed count from the underlying records at the correct level (for example records, reports, studies, or participants); reconcile totals and exclusions before drawing a flow. For a workflow, include relevant approval, revision, pause, cancellation, error, and recovery paths as well as the main path. Do not imply that a planned action, ethics approval, participant consent, or validation has occurred.

If this work downloads or cites papers, follow [paper guidance](../../papers/GUIDELINES.md), update the [download register](../../papers/DOWNLOADS.md) and [IEEE reference catalog](../../papers/REFERENCES.md) for every agent download, and retain stable paper IDs separately from manuscript citation numbers. Keep PDFs local and ignored.

## Make it reviewable

Add a short text explanation that conveys the same essential relationships and decisions without relying on color, layout, or rendering. Use readable labels and a legend for any special line styles or status codes. Avoid visual density that hides important exceptions; split a figure when necessary and link the parts in the prose.

Use the [Mermaid documentation](https://mermaid.js.org/intro/) for syntax and the [GitHub diagram guidance](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams) for repository display. Prefer syntax supported by the target viewer; do not assume every host uses the latest Mermaid version.

Check Mermaid syntax with an available renderer or parser suited to the target Markdown viewer, and inspect the rendered result for clipped labels, ambiguous arrows, and readable order when that capability is available. If it is unavailable, inspect the source and report rendering as unverified. Recheck the figure against its cited records; syntax or rendering success does not verify research claims or counts. Report the changed Markdown path, source scope, checks performed, and unresolved evidence or display limits.

For optional project coordination in Orbyn, use [the Orbyn skill](../orbyn/SKILL.md) only when the user requests that integration or it is otherwise authorized and accessible.
