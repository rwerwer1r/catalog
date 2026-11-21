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

## Reuse and compatibility

Consumers select relevant files, review their assumptions and pin a repository revision for reproducibility. Keep published paths stable or provide a migration plan for renames. Directory presence is not evidence of behavioral readiness; use controlled tests where needed.

## Portability boundary

This contract describes **catalog source layout**, not how every agent runtime discovers or executes assets. General-purpose assets should not require the catalog's directory tree, maintenance policies, account, or tool availability unless those dependencies are explicit in the consumer contract. Repository-specific assets may refer to local policies, but must clearly state their limited scope.

A referenced document or companion Skill is a real dependency when the workflow requires it. When copying an asset, include or adapt required support files and links; a standalone `SKILL.md` is not automatically self-contained. Verify the intended runtime's discovery and instruction-precedence behavior in the consuming environment rather than assuming universal portability. See [consumption guidance](../../docs/development/consumption.md).

## Verification

The source validator checks directory naming, entrypoint files, basic Markdown headings and category index link coverage. It does not test arbitrary module runtime behavior, third-party dependencies or agent performance.
