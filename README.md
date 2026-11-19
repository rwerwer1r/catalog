# Catalog

**rwerwer1r/catalog** is a source library for reusable modules, AI agent Skills, rules, references, roles and templates that other repositories can select and adapt.

## Repository layout

| Path | Purpose |
| --- | --- |
| [src/](src/README.md) | Canonical reusable assets |
| [catalog.json](catalog.json) | Published asset IDs, kinds and entrypoints |
| [docs/](docs/README.md) | Development guides, repository policies and agent-maintenance documentation |
| [tools/](tools/) and [tests/](tests/) | Structural validation and regression tests |

Assets are organized under `src/skills/`, `src/rules/`, `src/references/`, `src/agents/`, `src/modules/` and `src/templates/`. No asset is automatically installed or synchronized into another repository.

## Repository rules and development

- [Repository policy](docs/policies/repository.md): what belongs here and who controls downstream adoption
- [Asset policy](docs/policies/assets.md): source, manifest, reuse and verification criteria
- [Language and documentation](docs/policies/README.md): English content and maintenance conventions
- [Development](docs/development/README.md) and [agent harness](docs/agents/harness.md): working and checking procedures

## Validation

Python 3.11+ with the standard library:

```sh
python3 tools/validate_catalog.py
python3 tools/validate_docs.py
python3 -m unittest discover -s tests -v
```

CI validates structural consistency. Actual agent behavior and consumer integrations require separate evidence.
