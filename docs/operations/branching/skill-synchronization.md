# Paired skill synchronization

This is the canonical procedure for maintaining the reusable `skills/` library in the [public library](https://github.com/kinqsradio/academic-research-skills) and its designated private counterpart. It applies to every skill creation, modification, gap fix, rename, deletion, and supporting-resource change. Complete the paired update and private research-branch propagation in the same maintenance task. This procedure documents required work; it does not install an automatic synchronization service.

## Establish the pair and authority

Confirm both repository identities and remotes against explicit maintainer instructions or trusted maintainer configuration. Verify the counterpart is private through the hosting service; an ambiguous name or unavailable visibility check is insufficient. Keep private identity, URLs, configuration, and local paths out of public files and PRs. A fork or a research project is not automatically the designated private counterpart.

The maintainer's standing instruction authorizes reviewed publication to the designated pair in the same task, subject to the gates below; do not ask repeatedly for authorization already given. This policy does not itself grant external-action authority. Other users' private projects or forks require their own explicit permission and access; do not infer access to the maintainer's private repository. External contributors follow the public fork/PR process; the designated maintainer owns paired propagation after merge. If identity, visibility, access, or authority is missing, prepare safe local changes and report the specific blocker.

## Inspect and reconcile

Fetch both repositories before preparing a candidate. Record their current `main` tips, local changes, active private `research/*` branches, and any existing synchronization PRs. Compare both complete `skills/` trees, including supporting files, filenames, deletions, and modes. Investigate every divergence and preserve unrelated work; never overwrite either side wholesale. Recheck fetched tips before integration and reconcile changes made during the task.

The public `main` is the canonical published skill library. The private `main` remains a generic template; actual research stays on private `research/<project>` branches. Whole repositories, READMEs, CI configuration, and private-specific instructions are not mirrors. Keep project-specific instructions outside the canonical skill library.

## Prepare a public-safe candidate

Create a fresh `template/<change>` branch from current public `main` in the public repository's independent history. Make an explicit path allowlist for the reviewed reusable changes and any necessary generic policy or index updates. Copy only those reviewed contents, including intended deletions; inspect each file rather than trusting its location. Recreate a clean candidate when source commits mix reusable and research content.

Never merge a research branch into either `main`, cherry-pick mixed research history, transfer private history to the public repository, or use mirror, all-branch, or all-tag pushes. Never publish manuscripts, research plans, reviews, participant data, populated registers, course-specific scripts or assets, or other research content, even when placed under `skills/`. No PDF may enter Git on any branch. Inspect the complete candidate diff, file list, and outgoing history, including earlier outgoing commits; deleting a sensitive file later does not remove it from that history.

Run the applicable structural validation and meaningful checks for changed helpers or behavior. Review links, indexes, renames, and removals. Run `python3 scripts/check_public_template.py` and its synthetic tests in the public checkout, require the `Public template boundary` CI job, and inspect the diff and history manually. A passing guard is not a guarantee that secrets or research content are absent.

## Publish and integrate

Open or update a public PR; direct pushes to public `main` do not satisfy this procedure. Require passing CI, including `Public template boundary`, and review of the exact candidate before merge. If the candidate changes, recheck the final diff and history and obtain the applicable CI and review again. A pending PR is partial progress, not completed synchronization.

After the approved public PR merges, fetch and verify public `main`. Bring its reviewed reusable changes into private `main` through clean, reviewed template-only updates. Preserve private-specific documentation and configuration; transfer no public history wholesale. Reconcile any private skill improvements through the public review process before declaring the trees equal. Follow the [branch workflow](branch-workflow.md) for promotion, provider-neutral naming, and attribution.

Merge updated private `main` into every active private `research/*` branch. Preserve each branch's research records and unrelated changes; resolve conflicts deliberately and validate every result. Inventory local and remote branches rather than assuming one project is the only active branch. Only explicitly archived branches may remain frozen. Never force-push, rewrite history, or discard research to achieve synchronization.

## Verify completion and hand off

Run repository validation on both templates and every synchronized research branch. Compare the complete Git tree IDs, running this in each repository with its actual reviewed ref:

```sh
git rev-parse '<ref>:skills'
```

Identical tree IDs establish equality of tracked contents, filenames, and modes across independent histories, including removals. Compare public `main`, private `main`, and every active private research branch; a changed-files-only comparison is insufficient. Inspect working-tree changes separately because uncommitted files are not included in a ref's tree.

For authorized pushes, confirm destination, outgoing paths and history, push only intended branches, then fetch and verify remote tips match the intended commits. Report the public PR and merged commit, private template and research tips, tree IDs, checks and review evidence, and any explicitly archived branches. Distinguish local checks from CI and remote verification. Unknown visibility, a pending public PR, or any blocked active branch leaves synchronization incomplete: report the actionable partial state and next step without claiming publication or completion.
