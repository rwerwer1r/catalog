# Catalog agent instructions

This repository is `rwerwer1r/catalog`: a source library for assets reused by other repositories. Check the intended account, branch and task before editing.

## Find the right instructions

1. Start with [repository policy](docs/policies/repository.md) and [policies index](docs/policies/README.md).
2. For asset changes, read [asset policy](docs/policies/assets.md), [development](docs/development/README.md), and only the relevant `src/<kind>/README.md` and manifest entry.
3. For documentation changes, read [documentation policy](docs/policies/documentation.md) and the relevant [authoring guide](docs/documentation/README.md).
4. For agent-assisted tasks, follow [operating model](docs/agents/operating-model.md) and [document-first harness](docs/agents/harness.md).
5. Apply [English language policy](docs/policies/language.md) to all committed content.

## Verify

- Keep changes scoped and update canonical assets, `catalog.json`, and documentation together when necessary.
- Do not store credentials, private project data or material without the necessary reuse rights.
- Run `python3 tools/validate_catalog.py`, `python3 tools/validate_docs.py`, and `python3 -m unittest discover -s tests -v` when available.
- Report actual outcomes and unverified behavior; a structural check does not verify agents in consumers.
