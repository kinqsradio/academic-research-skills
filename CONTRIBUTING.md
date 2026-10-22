# Contributing

This public repository maintains reusable academic research skills, tooling, and empty project scaffolding. Contributions are welcome through focused pull requests against `kinqsradio/academic-research-skills:main`. Follow the [community code of conduct](CODE_OF_CONDUCT.md).

Use the [issue forms](https://github.com/kinqsradio/academic-research-skills/issues/new/choose) for reproducible problems and proposed improvements. Include the affected workflow, expected and observed behavior, and a small synthetic example where useful. Follow [SECURITY.md](SECURITY.md) for vulnerabilities and accidental disclosure; keep sensitive details out of public issues and pull requests.

## Choose the right checkout

- **External contributors:** fork the public repository, clone the fork, add the public repository as `upstream`, and create `template/<change>` from current `upstream/main`. Push that branch to your fork and open a PR against the public repository's `main`.
- **Template users and private research projects:** use a separate fresh checkout based on public `main` for contributions. Copy only selected reusable file changes into it, then follow the same fork and PR process. GitHub's **Use this template** creates independent history, so a template-created project is not a contribution fork.
- **Maintainers with public write access:** create `template/<change>` from current public `main` in a separate public checkout, push that branch to the public repository, and open a PR against `main`.

The [contribution walkthrough](docs/operations/branching/contributing-changes.md) provides commands, PR review gates, and the creator's private development workflow. Never push a private research branch to the public repository or a public fork. Do not merge unrelated histories or cherry-pick mixed research commits to make a contribution.

## Prepare a focused change

Read [AGENTS.md](AGENTS.md), [README.md](README.md), root [GUIDELINES.md](GUIDELINES.md), and each affected folder's `GUIDELINES.md` before editing. Check applicable `CLAUDE.md`, `.cursorrules`, and `codex.md` files. Write team documentation in English and follow the [provider-neutral naming and attribution policy](docs/operations/branching/branch-workflow.md#provider-neutral-names-and-attribution).

1. Identify the problem, intended behavior, and affected files. For concurrent work, name one owner per file and a reviewer for the integrated result.
2. Keep the patch reusable and project-neutral. Public `main` keeps source registers and research scaffolding empty. Keep populated registers, manuscripts, assessment material, research records, participant data, and downloaded papers out of the contribution. Research PDFs stay local and ignored on every branch.
3. For skill creation or revision, follow [skill-creator](skills/skill-creator/SKILL.md). Keep canonical instructions in `skills/`, update metadata and supporting links where needed, and update the [skill index](skills/GUIDELINES.md) when routing changes. Add `GUIDELINES.md` to each new maintained folder.
4. Cite evidence for changes to research procedures, retaining source locators and limitations. Use synthetic examples or material you have permission to publish. Never invent references, results, completed checks, or approvals.
5. Run the [required checks and manual review](docs/operations/branching/contributing-changes.md#checks-and-review), inspect the full diff and outgoing commits, and report unverified behavior. Use the [PR template](.github/PULL_REQUEST_TEMPLATE.md) to explain the problem, scope, evidence, validation, and remaining limits.

Contributions are under the [MIT License](LICENSE). Confirm you have the right to contribute the material and preserve required source attribution. Required academic AI-use disclosures remain applicable; repository setup does not authorize submission of assessed work.

## Keep research work private

Every branch, commit, issue, and PR published here is public. A `research/<project>` branch provides no privacy. Create a private repository before adding project content, following the [README setup](README.md#start-a-private-research-project) and [branch workflow](docs/operations/branching/branch-workflow.md).

The public-template CI gate is automatically skipped in other repositories, including private projects created from this template. Keep the standard structure and checker tests enabled there.

The public repository is the canonical published skill library. Private projects remain separate workspaces; there is no automatic synchronization. Import selected, reviewed public updates into a private template branch before promoting them to private `main`. Within that private repository, new or updated skills must then reach every active `research/*` branch in the same maintenance task, with validation and a canonical `skills/` comparison as specified in the [branch workflow](docs/operations/branching/branch-workflow.md#bring-template-improvements-into-a-project). Report blocked or explicitly archived branches. Do not send private project records back to the public repository during synchronization.
