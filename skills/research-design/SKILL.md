---
name: research-design
description: Develop or audit a study design, analysis plan or preregistration draft with explicit assumptions, decisions, dependencies and readiness limits. Use for methods planning before execution; use deep-research for evidence discovery, sr-screener for eligibility decisions and academic-paper for manuscript prose.
---

# Research design and readiness

Produce a traceable methods record in `docs/methods/<study>/<study>-design.md` using [DESIGN_TEMPLATE.md](DESIGN_TEMPLATE.md). Read [folder guidance](GUIDELINES.md), [methods guidance](../../docs/methods/GUIDELINES.md), the task, applicable brief and existing decisions. Keep the requested scope; an audit need not become a new study design or a preregistration.

## Establish the design basis

Identify the question, research type, intended inference, available resources, source scope and current stage. Read existing protocols before proposing changes. Record the version and date, relevant input paths, and whether work is proposed, piloted, collected or analyzed; mixed stages need separate labels. Missing documents and unknown chronology stay visible.

Separate documented researcher decisions from suggestions. Explain alternatives and trade-offs with evidence; a suggested answer is not an approved choice. Continue work that does not depend on missing consequential choices. Record each such choice with its owner, dependencies and what would resolve it; ask the researcher when it affects the design's scope, participants, outcomes or interpretation. Do not invent consent, approval, recruitment, data, power calculations or completed analyses.

## Connect the question to observations

For empirical work, specify the intended population or setting, unit of observation, constructs and their actual measures, outcomes, timing, and any comparison or intervention. Explain how these observations answer the question and what evidence would challenge the proposed explanation. Identify plausible competing explanations, design assumptions and threats to inference.

For quantitative work, name the target quantity or estimand when it helps define the intended inference; distinguish it from the estimator or model. State contrasts, units and uncertainty. Justify sampling and sample size through the chosen precision, power, feasibility or other appropriate basis. If a power calculation is needed but unavailable, record its inputs and the missing calculation; never manufacture a number or treat a conventional sample size as proof of adequate power.

For qualitative work, identify case selection, data generation, interpretive approach, reflexivity and how contrary cases or rival interpretations will be examined. State the basis for adequacy of the material rather than importing statistical power requirements. For conceptual work, identify definitions, premises, argumentative steps, counterexamples and the scope of the conclusion; participant and sampling fields can be explicitly not applicable.

Use [research-diagrams](../research-diagrams/SKILL.md) when a conceptual model or study flow clarifies the design. Label causal assumptions and proposed relationships explicitly; a diagram does not establish identification or replace methodological review.

## Make the analysis plan inspectable

Describe the proposed steps from inputs to conclusions and name the evidence or output each step needs. Keep assumptions and dependencies explicit. For quantitative analyses, specify outcome coding, inclusion/exclusion rules, missing-data treatment, models or tests, uncertainty reporting and multiplicity handling where relevant. Separate prespecified questions from exploratory work. An unknown analysis choice remains pending, not silently filled with a default.

For qualitative or conceptual analyses, document the coding, interpretation or argument procedure, treatment of conflicting evidence, and an appropriate review trail. Do not force hypothesis tests, causal contrasts or a numeric stopping rule onto work that does not use them. Link instruments, codebooks, example data or scripts only when they exist; label simulations and mock materials as such.

Record data handling, storage/access, confidentiality, consent and required approvals where applicable. Use explicit statuses such as proposed, unknown, pending or documented, with evidence for documented claims. A design-readiness record never authorizes collection, confidential uploads, release or external submission.

## Check preregistration and amendments when requested

A preregistration draft is a local proposed record. A registered protocol requires verified registration evidence, its identifier/version and timing relative to recruitment, collection and analysis. Do not describe late documentation as prospective registration. Verify current registry or venue rules from authoritative sources if the task requires selecting or using one; this skill does not publish or register anything.

Check that planned decisions are specific enough for another researcher to distinguish following the plan from departing from it. Record foreseeable contingencies and unresolved choices. Preserve the prior version when amending a protocol; date the change, state why it changed, who decided it, what data or results were already known and which earlier decisions or analyses need reassessment. Separate amendments from retrospective deviations.

## Preserve evidence and hand off

Use [paper guidance](../../papers/GUIDELINES.md), [DOWNLOADS.md](../../papers/DOWNLOADS.md) and [REFERENCES.md](../../papers/REFERENCES.md) for any source acquisition or citation. Register every agent download through that process, including verified metadata/provenance and size/SHA-256 for a verified local PDF; leave uncomputed legacy values unknown. PDFs remain local and ignored. Reuse stable source IDs with page, section, table or figure locators for design justifications; source identity alone does not establish methodological support. IEEE artifact numbering is separate from catalog IDs. Preserve source scope and access limits; use `deep-research` for substantial new evidence work.

Finish with a readiness table naming the criteria actually checked, observed evidence, unresolved dependencies and next owner. Report readiness for a named next step, not generic approval or research correctness. A complete draft can still have open registration, ethics or execution gates. Hand off the exact design version to `academic-pipeline`, the requested implementation task or `academic-paper`; state which choices remain proposed and which checks were not run.

## Delegation

Use [team roles](../../agents/README.md) and [model routing](../../agents/routing/MODEL_ROUTING.md) for substantial independent evidence or design checks. Give workers bounded inputs, owned outputs, acceptance criteria and a stopping condition; keep one owner for the design. Workers do not delegate further. Preserve the human-selected lead model and effort. Label a single-session check accurately rather than claiming independent review.
