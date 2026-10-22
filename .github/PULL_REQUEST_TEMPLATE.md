## Problem and resulting behavior

Describe the concrete problem, the change, and who benefits. Link a related issue when applicable.

## Scope and evidence

- Affected skills, scripts, or documentation:
- Source support and locators for changed research guidance (or not applicable):
- Representative example and expected outcome:

## Validation

List the commands actually run and their results. Distinguish structural checks, synthetic tests, live assistant behavior, and research evidence. Record checks not performed and why.

```sh
python3 scripts/validate_repository.py
python3 scripts/research_status_tests.py
python3 scripts/check_public_template.py
python3 scripts/check_public_template_tests.py
```

## Contributor checklist

- [ ] I have read the contribution guide and community code of conduct.
- [ ] This targets public `main` from a `template/<change>` branch based on the public repository.
- [ ] The files and outgoing commits contain reusable changes only: no research PDFs, populated research records, unpublished manuscripts, credentials, or participant data.
- [ ] I have permission to contribute this material under the MIT License; source attributions are preserved.
- [ ] Applicable folder guides and skill metadata/navigation are updated.
- [ ] The branch name, PR title, and commit messages follow the provider-neutral attribution policy.
- [ ] I have described evidence, validation limits, and any remaining manual checks.

Report security vulnerabilities through [private vulnerability reporting](https://github.com/kinqsradio/academic-research-skills/security/advisories/new), not this public PR.
