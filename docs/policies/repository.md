---
description: "Define the catalog repository's purpose, canonical structure, and boundaries."
---

# Repository policy

## Purpose and scope

`rwerwer1r/catalog` is a **source library for reusable components used by other repositories**. Its primary contents are implementation modules, AI agent Skills and roles, rules, references, and document templates. It also contains the documentation and checks required to maintain those assets.

This repository is **not** an application, a project worklog, an installer, or a central controller of consuming repositories.

## Canonical structure

| Location | Responsibility |
| --- | --- |
| `src/skills/` | Reusable task workflows with `SKILL.md` entrypoints |
| `src/rules/` | Task-scoped operating rules |
| `src/references/` | Shared technical knowledge and contracts |
| `src/agents/` | Reusable agent role definitions |
| `src/modules/` | Reusable implementation code with its own requirements |
| `src/templates/` | Reusable document templates |
| `catalog.json` | Machine-readable published asset index |
| `docs/` | Repository development, policies, agent maintenance and documentation guidance |
| `tools/`, `tests/` | Local verification utilities and tests |
| `.github/workflows/` | Repository CI checks |

Keep each item in the directory that owns it. Do not duplicate the canonical source in `docs/` or register documentation maintenance pages as distributable assets.

## Repository content rules

- Keep material reusable rather than tied to a single consumer's private work.
- Do not commit credentials, personal data, private workspace exports, generated agent projections, or transient work records.
- Avoid placeholder directories and modules without a real use case or implementation. A directory `README.md` may document the intended contract before a module exists.
- Maintain readable entrypoints and a coherent `catalog.json`; follow [asset policy](assets.md) for publishable files.
- Keep the repository's documentation in English per [language policy](language.md).

## Consumer boundaries

Other repositories may select and adapt individual catalog assets, but no automatic installation, synchronization or cross-repository update mechanism is supplied. A consuming repository retains its own policies, dependencies, release process, and authorization.

A change to `rwerwer1r/catalog` must not silently modify a consumer or any other account's resources. Discuss consumer compatibility in [development guidance](../development/consumption.md), not as an implied repository permission.

## Maintenance expectations

Before merging a change, review the intended files and update affected entrypoints, manifests and tests together. Run the checks described in [validation](../development/validation.md) and distinguish structural validity from unverified agent behavior. Do not publish readiness claims without evidence.
