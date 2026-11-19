# Catalog

**rwerwer1r/catalog** stores reusable modules, AI agent Skills, rules, references, roles and templates for selective use by other repositories.

## Find reusable assets

Start at [src/](src/README.md) and select the relevant directory:

| Directory | Content |
| --- | --- |
| [Skills](src/skills/README.md) | Task-specific agent workflows |
| [Rules](src/rules/README.md) | Scoped agent instructions |
| [References](src/references/README.md) | Reusable technical knowledge |
| [Agents](src/agents/README.md) | Role definitions |
| [Modules](src/modules/README.md) | Reusable implementation code |
| [Templates](src/templates/README.md) | Document templates |

**There is no central asset manifest.** Directory layout and per-category READMEs are the discovery interface. Choose and review an individual asset; this repository does not automatically install, synchronize or execute it elsewhere.

## Maintain the repository

- [Repository policy](docs/policies/repository.md): purpose, canonical paths and boundaries
- [Asset policy](docs/policies/assets.md): publishing and review criteria
- [Documentation](docs/README.md): development, policies, agent harness and authoring
- [Agent harness](docs/agents/harness.md): scoped context and evidence-based verification

## Checks

Requires Python 3.11+ and no third-party packages:

```sh
python3 tools/validate_catalog.py
python3 tools/validate_docs.py
python3 -m unittest discover -s tests -v
```

CI verifies file layout, source indexes and documentation structure. Behavioral agent checks and consumer integrations require separate evidence.
