# Asset source contract

## Canonical structure

The repository's `src/` directories own reusable assets. The **source path is the asset identifier**. There is no competing machine-readable asset registry; a derived document-discovery `INDEX.tsv`, if introduced, is not a second source of truth.

| Kind | Entry point |
| --- | --- |
| Skill | `src/skills/<name>/SKILL.md` |
| Rule | `src/rules/<name>.md` |
| Reference | `src/references/<name>.md` |
| Agent | `src/agents/<name>.md` |
| Module | `src/modules/<name>/README.md` |
| Template | `src/templates/<name>.md` |

Use lowercase kebab-case names. The nearest `src/<kind>/INDEX.md` provides a descriptive link to each published entrypoint, and `src/INDEX.md` links to each kind. A Skill or module may keep supporting files inside its own directory.

## Content contract

Each asset explains its purpose and the requirements necessary to use it. Operational assets should state triggers, inputs, outputs, dependencies and limitations. Avoid hidden setup, implicit permissions or internal-only context.

Each `SKILL.md` uses Agent Skills discovery metadata: `name` matches the Skill directory and `description` states when it applies. The reusable [documentation-authoring entrypoint guidance](../skills/documentation-authoring/references/entrypoints.md) owns reader-facing structure and metadata usage. See the [Agent Skills specification](https://agentskills.io/specification) for the full metadata contract.

## Entrypoints and on-demand routing

Apply the [documentation-authoring entrypoint procedure](../skills/documentation-authoring/references/entrypoints.md) to README.md and SKILL.md, and the [index procedure](../skills/documentation-authoring/references/indexes.md) to manual or metadata-generated navigation. This repository retains `src/skills/INDEX.md` for category discovery; a Skill-local `references/INDEX.md` selects on-demand procedures. Supporting guides are stored within that Skill's `references/` directory. Generated, metadata-backed indexes use `INDEX.tsv` rather than a script-generated Markdown index. Their rows derive from canonical document metadata; they do not replace the repository's asset source paths.

These are the catalog's packaging conventions, not mandatory layouts for other repositories. Published entrypoint paths must remain stable when consumers may rely on them.

## Reuse and compatibility

Consumers select relevant files, review their assumptions and pin a repository revision for reproducibility. Keep published paths stable or provide a migration plan for renames. Directory presence is not evidence of behavioral readiness; use controlled tests where needed.

## Portability boundary

This contract describes **catalog source layout**, not how every agent runtime discovers or executes assets. General-purpose assets should not require the catalog's directory tree, maintenance policies, account, or tool availability unless those dependencies are explicit in the consumer contract. Repository-specific assets may refer to local policies, but must clearly state their limited scope.

A referenced document or companion Skill is a real dependency when the workflow requires it. When copying an asset, include or adapt required support files and links; a standalone `SKILL.md` is not automatically self-contained. Verify the intended runtime's discovery and instruction-precedence behavior in the consuming environment rather than assuming universal portability. See [consumption guidance](../../docs/development/consumption.md).

## Verification

The source validator checks directory naming, entrypoint files, basic Markdown headings, category index link coverage, required Skill metadata, and local Skill links and routing. It does not test arbitrary module runtime behavior, third-party dependencies or agent performance.
