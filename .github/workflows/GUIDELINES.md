# Validation workflows

`validate.yml` runs on pushes to `main`, pull requests targeting `main` (including forks), and manual dispatch. It validates structure/links/skill metadata, tests the readiness checker, and tests the public-template guard on Python 3.10 and 3.12. The `Public template boundary` job checks the public upstream's tracked files and source registers; it runs only when `github.repository` is `kinqsradio/academic-research-skills`, so private template copies can keep research records. See [script guidance](../../scripts/GUIDELINES.md) for exact scope and limits.

The workflow uses `pull_request`, a read-only token, no provider secrets, checkout without persisted credentials, pinned action commits, job timeouts, and cancellation of superseded runs. Fork runs remain subject to GitHub's approval policies; a first-time contributor may need maintainer approval for a run. Do not use `pull_request_target` to execute contribution code with privileged access.

Passing checks establish structure and tested checker behavior, not claim support, scientific quality, live assistant execution, absence of all sensitive content, or author approval. Keep workflows free of private research and provider credentials. Tests run without model calls or paid provider APIs. A separately authorized evaluation using assistants would need its own data, budget, and access controls.
