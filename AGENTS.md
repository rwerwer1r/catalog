# Catalog agent instructions

This repository maintains reusable assets for `rwerwer1r`. Confirm account, repository and target branch before any write. Do not select or switch accounts without authorization.

## Load the relevant documentation

1. Read [documentation ownership](docs/README.md) and [repository policies](docs/policies/README.md).
2. Apply the [English language policy](docs/policies/language.md) to committed content.
3. Follow the [agent operating model](docs/agents/operating-model.md) and [document-first harness](docs/agents/harness.md) when an agent changes source or instructions.
4. For asset work, read [development](docs/development/README.md), the relevant `src/<kind>/README.md`, and the asset manifest entry. Do not load all assets by default.

## Work and verify

- Edit canonical `src/` assets and register their entrypoints in `catalog.json`.
- Respect unrelated work, permission boundaries, secrets and third-party licensing.
- Run `python3 tools/validate_catalog.py` and `python3 -m unittest discover -s tests -v` when available.
- Record the difference between documentation checks, mechanical validation and actual agent behavior. Report any skipped or unavailable verification accurately.
