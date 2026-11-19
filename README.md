# Catalog

**rwerwer1r/catalog** maintains reusable modules, agent Skills, rules, references, agent roles and document templates for selective use by other repositories.

## Source

| Folder | Purpose |
| --- | --- |
| [src/skills/](src/skills/README.md) | Opt-in agent workflows |
| [src/rules/](src/rules/README.md) | Scoped reusable guidelines |
| [src/references/](src/references/README.md) | Supporting knowledge and contracts |
| [src/agents/](src/agents/README.md) | Role-specific agent behavior |
| [src/modules/](src/modules/README.md) | Software implementations |
| [src/templates/](src/templates/README.md) | Document templates |

The [manifest](catalog.json) lists entrypoints. Assets are not automatically installed, synchronized or executed.

## Documentation and harness

- [Documentation index](docs/README.md)
- [Development](docs/development/README.md): architecture, [asset lifecycle](docs/development/asset-lifecycle.md), consumer compatibility
- [Policies](docs/policies/README.md): English, documentation, [security](docs/policies/security.md) and [provenance](docs/policies/provenance.md)
- [AI agent operations](docs/agents/README.md): context routing, [document-first harness](docs/agents/harness.md), [scenarios](docs/agents/scenarios.md)
- [Documentation handbook](docs/documentation/README.md): authoring, structure, review and maintenance

English is canonical for committed repository material.

## Checks

Python 3.11+ and the standard library are sufficient:

```sh
python3 tools/validate_catalog.py
python3 tools/validate_docs.py
python3 -m unittest discover -s tests -v
```

GitHub Actions runs structural checks. Behavioral scenarios and downstream integrations require separate observed evidence; see [verification](docs/agents/verification.md).
