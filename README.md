# Catalog

**rwerwer1r/catalog** holds reusable implementation modules, agent Skills, rules, references, agent roles, and document templates for other repositories.

## Source directories

| Folder | Responsibility |
| --- | --- |
| [src/skills/](src/skills/README.md) | Task-specific, opt-in agent workflows |
| [src/rules/](src/rules/README.md) | Small, scoped operating guidelines |
| [src/references/](src/references/README.md) | Supporting knowledge and contracts |
| [src/agents/](src/agents/README.md) | Role-specific agent behavior |
| [src/modules/](src/modules/README.md) | Reusable software implementations |
| [src/templates/](src/templates/README.md) | Document templates |

[Catalog manifest](catalog.json) lists published entrypoints. [Development guide](docs/development.md) defines how to add assets.

## Initial development checks

Requires Python 3.11+ only; no dependency installation or external service is needed.

```sh
python3 tools/validate_catalog.py
python3 -m unittest discover -s tests -v
```

GitHub Actions executes both checks for pushes and pull requests. This packaging harness does **not** test downstream agent performance.

## Consumption

Choose only the relevant asset from `catalog.json`. Read its prerequisites, review permissions, and pin a revision for automatic consumers. Nothing here automatically installs, syncs, or executes assets in another repository.
