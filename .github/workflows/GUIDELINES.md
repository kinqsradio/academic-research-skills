# Validation workflows

`validate.yml` runs the repository structural validator and research-readiness checker tests on pushes to `main`, pull requests, and manual dispatch. It uses read-only repository permissions and Python standard-library checks. Passing automation establishes structure and checker behavior, not research validity, model execution, or author approval. Keep workflows free of provider credentials and research data.
