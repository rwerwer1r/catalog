# Catalog agent instructions

This is `rwerwer1r/catalog`, a maintained source library for reusable assets. Confirm the intended account, branch and task before editing.

## Discover source and rules

1. Read [repository policy](docs/policies/repository.md) and the relevant [policy index](docs/policies/README.md).
2. For source changes, read [asset policy](docs/policies/assets.md) and the affected asset. Use the corresponding `src/<kind>/index.md` when discovering assets or updating category navigation; skip rediscovery if the target path is already known.
3. For documentation changes, follow [documentation policy](docs/policies/documentation.md) and the relevant [authoring guide](docs/documentation/README.md). For README.md, SKILL.md, or index work, use the owning [documentation-authoring Skill](src/skills/documentation-authoring/SKILL.md) and its task route.
4. For agent work, use [operating model](docs/agents/operating-model.md) and [document-first harness](docs/agents/harness.md).
5. Follow [English language policy](docs/policies/language.md) for all committed content.

When the target is unknown, discover directory-first through `src/index.md` and the relevant category index. When known, go directly to its entrypoint after applicable rules. Do not create a duplicate machine-readable asset registry.

## Verify

- Keep edits scoped and update source files and their category index links together.
- Do not publish secrets, private project records or material lacking reuse rights.
- Run `python3 scripts/validate_catalog.py`, `python3 scripts/validate_docs.py` and `python3 -m unittest discover -s tests/scripts -v` when available.
- Report actual outcomes and unverified behavior; passing structural checks does not prove consumer behavior.
