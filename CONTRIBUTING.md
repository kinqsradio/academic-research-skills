# Contributing

This public repository maintains reusable academic research skills and empty project scaffolding. Use GitHub issues for reproducible problems or proposed improvements, and pull requests for focused template changes. Include the affected skill, expected behavior, observed behavior, and validation commands. Share synthetic examples or material you have permission to publish.

Create a **private repository** from this template for your research. Every branch and pull request in this public repository is public: a `research/<project>` branch does not provide privacy. Keep manuscripts, populated source registers, assessment records, and participant data in your own project repository. When contributing back, submit only reusable changes on a `template/<change>` branch.

Contributions are made under the [MIT License](LICENSE). Confirm you have the right to contribute the material; retain source attribution and cite evidence supporting changes to research procedures.

Read [AGENTS.md](AGENTS.md) and the relevant folder's GUIDELINES.md before editing. Write team documentation and research outputs in English.

Use [the branch workflow](docs/operations/branching/branch-workflow.md): `main` is the project-neutral template, and each project gets a `research/<project>` branch created from `main`. Keep populated source registers, research records, and writing on the project branch; keep research PDFs locally in `papers/`, never staged, committed, or pushed on any branch. Keep `main` research scaffolding and registers empty. Promote reusable changes, including new skills, through reviewed template-only commits, never by merging a research branch into `main`. Use `template/<change>` for reusable improvements. Merge approved `main` updates into the project branch. Follow the canonical [provider-neutral naming and attribution policy](docs/operations/branching/branch-workflow.md#provider-neutral-names-and-attribution) for branch names, PR titles, commit trailers, and PR bodies; required academic AI-use disclosures remain applicable.

1. Identify the intended output and affected files. For concurrent work, name one owner per file and a reviewer for the integrated result.
2. Preserve source papers and existing research. Record source locators, scope decisions, and limitations alongside the work they support. Register every paper download in [DOWNLOADS.md](papers/DOWNLOADS.md) and maintain its IEEE entry in [REFERENCES.md](papers/REFERENCES.md).
3. Use [the team skill creator](skills/skill-creator/SKILL.md) to create or improve canonical skills in skills/. Keep each skill focused on its own output; put only necessary supporting material beside it. Add GUIDELINES.md when creating a folder.
4. When changing a skill, update its metadata, supporting links, and the skill index as needed. Keep all skill instructions in skills/.
5. Keep research prose and manuscripts in canonical Markdown; verify imported Word text before removing originals, and record conversion limits. Export or transfer to a shared document only within the requested scope.
6. Run the [validation commands](README.md#validation), review the diff, and report unverified behavior. Research claims and final document layout need their own review.
7. Preserve reviewed versions using [submission version records](submissions/VERSION.md). Human approval and an actual submission are separate events.

Do not commit credentials, confidential participant material, or generated scratch files. Agent downloads stay locally in papers/ with provenance in the persistent DOWNLOADS.md and REFERENCES.md records; research PDFs are excluded from Git on every branch, regardless of distribution rights. Preserve source IDs and metadata when a local file is missing. Do not assume repository setup constitutes permission to submit assessed work.

New or updated reusable skills must be synchronized from `main` into every active `research/*` branch in the same maintenance task. Validate each branch and confirm its canonical `skills/` matches `main`; report blocked or intentionally archived branches explicitly. Follow the branch workflow for merging, preserving project records, and authorized pushes.
