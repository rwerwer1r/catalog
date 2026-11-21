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

## Entrypoints and on-demand routing

A Skill's `SKILL.md` is a lightweight **relevance gate**: include activation and exclusion criteria, essential permissions and dependencies, and a clear route for accepted tasks. If the request does not match, stop before loading further files.

When a Skill has distinct workflows, a sibling `INDEX.md` may route to task-specific supporting files. Keep that index a concise map; load only the selected destination. The canonical category index remains `src/skills/index.md`, while a Skill-local `INDEX.md` routes **within** that Skill. Do not confuse these roles or introduce duplicate inventories.

These are the catalog's packaging conventions, not mandatory layouts for other repositories. Published entrypoint paths must remain stable when consumers may rely on them.

## Reuse and compatibility

Consumers select relevant files, review their assumptions and pin a repository revision for reproducibility. Keep published paths stable or provide a migration plan for renames. Directory presence is not evidence of behavioral readiness; use controlled tests where needed.

## Verification

The source validator checks directory naming, entrypoint files, basic Markdown headings and category index link coverage. It does not test arbitrary module runtime behavior, third-party dependencies or agent performance.
