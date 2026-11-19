---
description: "Choose the canonical guidance for planning, writing, reviewing, and maintaining catalog documentation."
---

# Documentation handbook

This handbook is the **working guide for documentation changes** in `rwerwer1r/catalog`. The [documentation policy](../policies/documentation.md) defines mandatory requirements, and the [English language policy](../policies/language.md) defines the written language. This handbook explains how to apply them without creating duplicate authorities.

## Select the right guide

| Task | Guide |
| --- | --- |
| Decide whether a page, section, or bundle is needed | [Information architecture](information-architecture.md) |
| Write or substantially revise a technical page | [Writing and examples](authoring.md) |
| Add metadata and lifecycle information | [Frontmatter](frontmatter.md) |
| Create navigation or an agent starting point | [Entrypoints](entrypoints.md) |
| Group related pages into a portable set | [Bundle documents](bundles.md) |
| Review quality, accuracy, and links | [Documentation review](review.md) |
| Update, move, deprecate, or retire a page | [Maintenance](maintenance.md) |
| Delegate documentation work to an AI agent | [Agent documentation workflow](agent-workflow.md) |

## Default workflow

1. **Discover** — read the relevant domain index and locate the current canonical source. Identify the reader and the requested outcome.
2. **Design** — choose the owning domain and smallest sustainable information unit; use a bundle only when several pages must be consumed together.
3. **Write** — follow English, frontmatter, task-oriented writing, evidence, and link conventions. Keep examples executable or explicitly illustrative.
4. **Connect** — update the closest entrypoint and links from any directly affected pages. Do not add every page to the root index.
5. **Verify** — inspect the resulting Markdown, metadata, navigation, claims, commands, and changed-file diff. Run project checks where available.
6. **Maintain** — record unresolved assumptions, replace stale references, and prefer revision over parallel documents describing the same topic.

## Boundaries

- `docs/` explains maintenance, policies, and operational guidance; `src/` owns distributable agent assets and modules.
- `catalog.json` describes publishable assets, not the documentation tree.
- A passed catalog manifest check does not validate prose, Markdown links, agent behavior, or downstream integrations.
- Loading a document never implies permission to install tools, change accounts, or write to another repository.
