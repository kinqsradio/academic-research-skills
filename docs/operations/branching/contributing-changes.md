# Contribute reusable changes

Purpose: explain how external users and maintainers propose changes to the public template without publishing private project history. Status: reusable contribution procedure.

The canonical published skill library is [`kinqsradio/academic-research-skills`](https://github.com/kinqsradio/academic-research-skills). Private research repositories and the creator's private `kinqsradio/agent-skill-lab` remain development and research workspaces. Changes do not synchronize automatically in either direction. Use [CONTRIBUTING.md](../../../CONTRIBUTING.md) for contribution scope and [branch-workflow.md](branch-workflow.md) for template promotion, research branches, naming, and attribution.

## External contributors: fork and open a PR

Fork the public repository on GitHub, selecting its default branch. Work in a separate contribution checkout. Replace `YOUR-ACCOUNT` with the owner of your public fork:

```sh
git clone https://github.com/YOUR-ACCOUNT/academic-research-skills.git academic-research-skills-contribution
cd academic-research-skills-contribution
git remote add upstream https://github.com/kinqsradio/academic-research-skills.git
git remote -v
git fetch upstream
git switch -c template/my-change upstream/main
```

Check that `origin` is your fork and `upstream` is the public library. Read the root instructions and affected folder guides, then make a focused reusable change. Use `template/<change>` with a descriptive provider-neutral slug. Run the checks below before staging selected paths:

```sh
git diff --check
git diff --name-status upstream/main
git diff upstream/main
git add -- path/to/selected-file.md
git diff --cached --name-status
git diff --cached
```

Replace the example path with the specific files you reviewed. Confirm empty source registers and project scaffolding remain empty, and no credentials, research content, PDFs, or private paths appear in the patch. Inspect the commit message for unintended automated attribution before committing. After committing, review every outgoing commit and its patch:

```sh
git commit -m "Clarify reusable workflow behavior"
git log --oneline upstream/main..HEAD
git log --format=full --stat --patch upstream/main..HEAD
git remote -v
git push -u origin template/my-change
```

On GitHub, open a PR with **base repository** `kinqsradio/academic-research-skills`, **base branch** `main`, and **head** `YOUR-ACCOUNT:template/my-change`. Complete the [PR template](../../../.github/PULL_REQUEST_TEMPLATE.md). Describe the concrete problem and resulting behavior, evidence supporting procedure changes, checks run, and remaining limitations. Link the relevant issue when one exists. Respond to review by updating this branch, rerunning affected checks, and pushing to your fork.

GitHub documents the [fork and PR workflow](https://docs.github.com/en/get-started/exploring-projects-on-github/contributing-to-a-project) and [fork remote setup](https://docs.github.com/en/pull-requests/how-tos/work-with-forks/fork-a-repo).

## Contributions from template-created or private projects

GitHub's **Use this template** creates a new repository with a single initial commit rather than the original commit history. Template-created histories are independent; [GitHub's template documentation](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template) explains the difference from forks. A project created by cloning and replacing its remote may share ancestry, but it can still contain private research history. Use the same separate-checkout procedure for either case.

Keep the project checkout and its private remote intact. Create a fresh public contribution checkout using the fork procedure above. Review the proposed improvement in the private workspace, then manually copy only the selected reusable files or edits into the public `template/<change>` branch. Review each resulting file and diff for project-specific examples, evidence records, filenames, paths, and secrets before staging it. Recreate mixed changes as a clean public patch.

Never push a private branch or its history to the public repository or a public fork. Do not merge a private research branch, use `--allow-unrelated-histories`, or cherry-pick commits mixing reusable work with research content. A later deletion does not remove sensitive material from earlier commits. If disclosure has already occurred, follow [SECURITY.md](../../../SECURITY.md).

## Maintainers and the creator's development workspace

A maintainer with public write access can clone the public repository directly and use its `origin` instead of a fork:

```sh
git clone https://github.com/kinqsradio/academic-research-skills.git academic-research-skills-maintenance
cd academic-research-skills-maintenance
git fetch origin
git switch -c template/my-change origin/main
```

Make or copy selected reusable changes, run the same checks, inspect every outgoing commit against `origin/main`, and push `template/my-change` to public `origin`. Open a PR against public `main`; direct write access does not replace review.

The creator follows this path when promoting work from private `kinqsradio/agent-skill-lab`: use a fresh checkout of public `main`, copy only reviewed reusable changes, and submit the public PR. Do not add the public repository as a push destination for private research branches, or move private history into the public checkout. The private repository remains the development/research workspace; public `main` records the reviewed published version.

## Checks and review

Run from the public contribution checkout using Python 3.10 or later:

```sh
python3 scripts/validate_repository.py
python3 scripts/research_status_tests.py
python3 scripts/check_public_template.py
python3 scripts/check_public_template_tests.py
git diff --check
```

The [CI workflow](../../../.github/workflows/validate.yml) checks repository structure and skill metadata and runs the 17 research-status tests. The opt-in public-template guard checks for populated project records and prohibited template artifacts; its tests check that policy behavior. It is a content-boundary check, not a secret scanner. The workflow automatically skips this public-only gate outside `kinqsradio/academic-research-skills`, so private project copies can keep versioned research records. Require the CI checks to pass for the exact PR candidate before merge; rerun checks after changes. A green check is evidence only for the behavior that check covers.

Review the complete changed file list and outgoing history. Keep the PR focused, preserve folder guides and links, and verify evidence behind changed research instructions. For workflow or tooling behavior changes, record representative scenarios, expected behavior, observed results, and unavailable live capabilities. Review in a separate context where consequential changes require it; sequential self-review is not independent review. Automated checks do not establish scientific correctness, source support, live assistant behavior, rendered quality, ethics approval, or submission readiness.

Use the [issue forms](https://github.com/kinqsradio/academic-research-skills/issues/new/choose) for public bugs and improvements. Use the [security policy](../../../SECURITY.md) for vulnerabilities or accidental disclosure. Share only synthetic or permitted public examples.

## Bring reviewed public changes back into private work

After a public change is merged, select the public files or edits needed by the private workspace. Create a `template/<change>` branch from the private repository's current `main`; copy those selected changes into that branch without merging unrelated histories. Review the diff, preserve private project content and configuration, run the private repository's validation, and promote the reviewed template-only change through its normal review process. Resolve any intentional local differences explicitly.

Then follow [Bring template improvements into a project](branch-workflow.md#bring-template-improvements-into-a-project): inventory every active private `research/*` branch, merge the updated private `main`, preserve project records, validate each branch, and compare canonical `skills/` against private `main`. Report blocked or explicitly archived branches. This is a deliberate, reviewed import; a public merge neither updates the private workspace automatically nor authorizes publication of its research branches.
