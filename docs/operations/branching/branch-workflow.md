# Template and research branches

Use `main` as the project-neutral workspace template. Keep reusable skills, shared root instructions, role and model-routing guidance, maintenance tooling, and empty folder scaffolding there. Empty registers such as `papers/DOWNLOADS.md`, `papers/REFERENCES.md`, and `submissions/VERSION.md` may stay in the template so skill links and folder structure are ready to use.

Keep project-specific research records on a project branch. This includes populated source registers, literature and methods records, decisions, plans, drafts, reviews, and project setup or validation audits. Research PDFs stay local and ignored in `papers/`; never stage, commit, or push them on any branch. A file belongs on `main` only when it is useful across projects and contains no project-specific evidence or content. Keep reusable operations guidance generic; do not put a project audit on `main`.

Version `papers/DOWNLOADS.md` and `papers/REFERENCES.md` on the project branch as persistent source metadata. Keep stable source IDs, bibliographic details, provenance, versions, file sizes and SHA-256 checksums where computed, and evidence locators when a local PDF is unavailable or removed. A fresh clone contains those records but no research PDFs; retrieve permitted copies via the recorded DOI, landing page, or retrieval URL and verify identity and intended version before reading. Check recorded size and SHA-256 when available; retain unavailable-source records and record a changed checksum as a distinct file/version. A metadata entry does not establish current local full-text availability. Keep the corresponding registers empty on `main`.

## Provider-neutral names and attribution

Use `research/<project>` for project branches and `template/<change>` for reusable template improvements, with short, stable slugs describing the work. Branch names and pull request titles must not contain Codex or Claude, regardless of the assistant used. This repository policy takes precedence over assistant-specific branch-prefix defaults. Keep PR titles focused on the change.

Do not add Codex or Claude `Co-authored-by` commit trailers or generated-by attribution to PR titles or bodies. Inspect the proposed commit message and PR text before creating them and remove automatically inserted assistant attribution. Preserve ordinary human authorship metadata. This policy governs Git and PR attribution; it does not remove required academic AI-use disclosures or factual tool details needed in research methods, evidence, or validation records.

## Public template and private projects

Every branch, commit, issue, and pull request in a public repository is public. A `research/<project>` branch separates project content from the template but provides no access control. Create a private repository from this template before adding unpublished research, assessment material, populated registers, or participant information. Run the project-branch workflow below inside that private repository. Keep contributions to the public template reusable and project-neutral.

## Start a project

Clone or update the repository from `main`, then create the project branch before adding research material. Use the provider-neutral research prefix:

```sh
git switch main
git pull --ff-only
git switch -c research/my-project
```

For another project, use `research/<project>` with a short, stable project slug. If the branch already exists, switch to it instead of creating a duplicate. Run the selected research skill only after switching to the project branch; the empty folder guides and registers provide the expected structure.

Do not put populated research files on `main`. Before committing on any branch, check the current branch and inspect the staged paths and diff; confirm no research PDF is staged. Ignore rules do not protect files already tracked or force-added. If a research PDF is tracked, stop the commit or push and arrange its removal from tracking while preserving the local copy; do not silently delete it or rewrite history. Inspect outgoing commits before a push, because removing a PDF in a later commit does not remove it from earlier outgoing commits. Keep each project's source IDs and records on its project branch; stable IDs such as `P001` identify sources within that project, while manuscript citation numbering remains independent.

## Promote reusable improvements to `main`

When a project branch produces a reusable improvement, including a new skill, first decide whether it is genuinely project-neutral. Create a `template/<change>` branch from `main` for the reusable improvement. Make a dedicated template-only commit that changes only approved reusable files, such as a skill, shared instruction, role or routing guide, generic maintenance script, or generic operations document. Do not mix that commit with research records or artifacts.

Review the complete file list and diff before promotion. Cherry-pick only the dedicated, reviewed template commit onto `main`. If the source commit also contains project content, do not cherry-pick it; recreate the reusable change as a clean file-scoped commit on a `template/<change>` branch created from `main`, then review it before promotion. Preserve empty scaffolding where the template needs it, and keep every populated register, PDF, note, plan, draft, review, and project audit out of the promotion.

Push or publish a template improvement only when the human has authorized that external action, including a standing instruction for the designated pair under [paired skill synchronization](skill-synchronization.md). Public skill publication must use that procedure's PR and exact-candidate CI/review gates. Before doing so, verify the intended repository and destination branch and inspect the outgoing commit paths and diff for project-specific material and research PDFs. Never merge a research branch into `main`, manually or automatically; promote only the reviewed template-only commits.

## Bring template improvements into a project

Every reusable skill change, including creation, gap fixes, renames, deletions, and supporting-resource updates, follows [paired skill synchronization](skill-synchronization.md). That canonical procedure owns pair verification, safe transfer between independent histories, public PR gates, private template integration, and propagation to all active private `research/*` branches in the same task. Preserve unrelated work and research records; report blocked or explicitly archived branches. A pending public PR or an unsynchronized active branch is incomplete maintenance.

For each active research branch:

```sh
git fetch origin
git switch research/my-project
git merge main
python3 scripts/validate_repository.py
git diff --exit-code main HEAD -- skills/
```

Before merging, verify local `main` includes the latest approved remote template changes. The skills comparison must be empty; investigate and reconcile divergence instead of overwriting skills blindly. Keep project-specific instructions outside the canonical skills library. Push synchronized research branches when publication is authorized and verify their remote tips.

Resolve any conflicts while preserving project evidence and records. Review the merge diff to confirm it adds the intended reusable changes without removing project material. Record substantive research decisions and evidence in the project branch, not in the template history.

## Branch review checklist

- Check branch names and PR titles against the provider-neutral policy, and inspect commit trailers and PR text for automated assistant attribution. Preserve required academic AI-use disclosures.
- On `main`, confirm content is reusable and project-neutral; empty scaffolding is allowed.
- On a project branch, confirm populated registers, project records, and writing stay with that project; research PDFs remain local and ignored.
- On every branch, inspect staged and outgoing commits and confirm no research PDF is included; preserve persistent source metadata even when local PDFs are absent.
- Before template promotion, review the exact files and diff; promote only a dedicated template-only commit.
- Before pushing, confirm human authorization, destination branch, outgoing file list, and the absence of research PDFs throughout outgoing commits.
- Before finishing skill maintenance, complete [paired skill synchronization](skill-synchronization.md): verify the merged public PR, private template and all active private research branches, complete `skills/` tree equality, and pushed remote tips; report pending or blocked work accurately.
