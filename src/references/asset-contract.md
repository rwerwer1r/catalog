# Asset source contract

## Canonical structure

The repository's `src/` directories own reusable assets. The **source path is the asset identifier**. There is no duplicate machine-readable inventory.

| Kind | Entry point |
| --- | --- |
| Skill | `src/skills/<name>/SKILL.md` |
| Rule | `src/rules/<name>.md` |
| Reference | `src/references/<name>.md` |
| Agent | `src/agents/<name>.md` |
| Module | `src/modules/<name>/README.md` |
| Template | `src/templates/<name>.md` |

Use lowercase kebab-case names. The nearest `src/<kind>/index.md` provides a descriptive link to each published entrypoint, and `src/index.md` links to each kind. A Skill or module may keep supporting files inside its own directory.

## Content contract

Each asset explains its purpose and the requirements necessary to use it. Operational assets should state triggers, inputs, outputs, dependencies and limitations. Avoid hidden setup, implicit permissions or internal-only context.

Each `SKILL.md` uses Agent Skills discovery metadata: `name` matches the Skill directory and `description` states when it applies. The reusable [documentation-authoring entrypoint guidance](../skills/documentation-authoring/entrypoints.md) owns reader-facing structure and metadata usage. See the [Agent Skills specification](https://agentskills.io/specification) for the full metadata contract.

## Entrypoints and on-demand routing

Apply the [documentation-authoring entrypoint procedure](../skills/documentation-authoring/entrypoints.md) to README.md and SKILL.md, and the [index procedure](../skills/documentation-authoring/indexes.md) to manual or metadata-generated navigation. This repository retains `src/skills/index.md` for category discovery; a Skill-local `INDEX.md` selects on-demand procedures. Generated, metadata-backed indexes use `INDEX.tsv` rather than a script-generated Markdown index.

These are the catalog's packaging conventions, not mandatory layouts for other repositories. Published entrypoint paths must remain stable when consumers may rely on them.

## Reuse and compatibility

Consumers select relevant files, review their assumptions and pin a repository revision for reproducibility. Keep published paths stable or provide a migration plan for renames. Directory presence is not evidence of behavioral readiness; use controlled tests where needed.

## Verification

The source validator checks directory naming, entrypoint files, basic Markdown headings and category index link coverage. It does not test arbitrary module runtime behavior, third-party dependencies or agent performance.
