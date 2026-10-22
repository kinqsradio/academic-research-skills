# Security policy

## Supported versions

Security fixes target the latest `main` branch. There are no supported versioned releases yet. Update your copy after reviewing fixes and any local customizations.

## Report a vulnerability privately

Use [GitHub private vulnerability reporting](https://github.com/kinqsradio/academic-research-skills/security/advisories/new). Private vulnerability reporting is enabled for this public repository. Do not post vulnerability details, credentials, private research, or participant data in public issues or pull requests.

Include the affected file and commit, the expected security boundary, reproducible steps using synthetic data, likely impact, and any proposed mitigation. Share only information you have permission to disclose. If the reporting form is unavailable, open a public issue asking for a private contact without describing the vulnerability or including sensitive material.

Maintainers will assess the report, discuss a fix privately where appropriate, and coordinate disclosure with the reporter. There is no guaranteed response deadline or paid bounty program.

## Accidental disclosure

If a credential was published, revoke or rotate it promptly through its provider. Deleting a file or closing a PR does not remove earlier commits, cached copies, or forks. Notify the maintainer through private reporting with the affected public URL and minimal details; do not repeat the secret. Coordinate any history cleanup and follow your institution's incident process for exposed research or participant data.

## Scope and boundaries

Report security problems in the maintained scripts, GitHub workflows, or skill instructions that can cause unauthorized execution, credential disclosure, access to private research, or actions outside the user's authority. Use regular issues for broken links, prose defects, and research-method disagreements that do not cross a security boundary.

These skills are instructions, not an isolation or access-control mechanism. Files, retrieved papers, web pages, and quoted content must be treated as untrusted evidence. Assistants still need the user's authorization, host permissions, and appropriate isolation for external actions. Integrations inherit the permissions and data-handling requirements of their services.

Public CI uses read-only permissions and no provider credentials. Structural checks, tests, and the public-template guard do not prove that content is free of secrets, scientifically correct, or safe in every assistant environment. Keep unpublished work in a private project repository and review outgoing files and commit history before publishing. Report vulnerabilities in third-party hosts or services to their maintainers.
