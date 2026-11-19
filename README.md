# Catalog

**rwerwer1r/catalog** maintains reusable modules, agent Skills, rules, references, agent roles and document templates for other repositories.

## Source

| Folder | Purpose |
| --- | --- |
| [src/skills/](src/skills/README.md) | Opt-in agent workflows |
| [src/rules/](src/rules/README.md) | Scoped reusable guidelines |
| [src/references/](src/references/README.md) | Supporting knowledge and contracts |
| [src/agents/](src/agents/README.md) | Role-specific agent behavior |
| [src/modules/](src/modules/README.md) | Software implementations |
| [src/templates/](src/templates/README.md) | Document templates |

The [manifest](catalog.json) lists published entrypoints. Consumers select and review specific assets; the repository does not automatically install, sync or execute them.

## Documentation and agent harness

- [Documentation index](docs/README.md)
- [Development](docs/development/README.md)
- [Policies](docs/policies/README.md), including the [English language policy](docs/policies/language.md)
- [AI agent operations](docs/agents/README.md) and [document-first harness](docs/agents/harness.md)
- [Documentation handbook](docs/documentation/README.md): authoring, structure, review and maintenance

English is the canonical language for maintained repository content.

## Validation

Requires Python 3.11+ with no third-party dependencies:

```sh
python3 tools/validate_catalog.py
python3 tools/validate_docs.py
python3 -m unittest discover -s tests -v
```

CI checks packaging and document structure. See [validation](docs/development/validation.md) for scope and [agent verification](docs/agents/verification.md) for behavioral evidence requirements.
