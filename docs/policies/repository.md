---
description: "Define the catalog's purpose, source directory ownership, and repository boundaries."
---

# Repository policy

## Purpose

`rwerwer1r/catalog` maintains reusable components for other repositories: Skills, rules, references, agent roles, modules and templates. Documentation and checks support this source library. This repository is not an application, worklog, installer or controller of consumer repositories.

## Canonical structure

| Path | Responsibility |
| --- | --- |
| `src/skills/` | Task workflows with `SKILL.md` entrypoints |
| `src/rules/` | Task-scoped instructions |
| `src/references/` | Reusable knowledge and technical contracts |
| `src/agents/` | Agent role definitions |
| `src/modules/` | Reusable implementation code |
| `src/templates/` | Document templates |
| `src/index.md` and category `index.md` files | Canonical source discovery and published entrypoint links |
| `src/README.md` and category `README.md` files | Brief introductions linking to the corresponding indexes |
| `docs/` | Repository policies, development and agent maintenance guidance |
| `scripts/`, `tests/scripts/` | Verification utilities and tests |
| `.github/workflows/` | Repository CI |

**The directory `index.md` files are the canonical source discovery interface; READMEs are concise introductions.** Do not introduce a second registry that duplicates the same asset inventory. Keep canonical source under its owner; documentation should link to it rather than copy it.

## Content boundaries

- Keep assets reusable and independent of any single consumer's private work.
- Do not commit credentials, personal data, private workspace exports, generated vendor projections or transient records.
- Publish implementation modules only with real source and documented requirements. An empty category may keep a README but must not claim ready-to-use modules.
- Apply [asset policy](assets.md) for source entries, [documentation policy](documentation.md) for docs and [language policy](language.md) for English.
- Maintain relevant category links and tests whenever the source structure changes.

## Consumers and maintenance

Downstream repositories explicitly select their assets and revisions; there is no automatic installation or synchronization. No catalog change may silently mutate a consumer or another account. Review source diffs and run [validation](../development/validation.md) before reporting completion. Structural validity is not proof of agent behavior.
