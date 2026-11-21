---
description: "Define canonical documentation ownership and quality requirements inside the catalog."
---

# Documentation policy

## Scope

Documentation under `docs/` explains how **this catalog repository** is maintained. Do not present these pages as assets that other repositories must adopt.

| Directory | Document responsibility |
| --- | --- |
| `docs/development/` | Source layout, contribution process, validation, lifecycle and consumption |
| `docs/policies/` | Repository-specific requirements |
| `docs/agents/` | Agent workflow and evidence for maintaining this repository |
| `docs/documentation/` | Authoring, navigation, review and maintenance conventions |

Publish reusable source under `src/` and link it from its category `INDEX.md` instead of duplicating it in documentation.

## Requirements

- Write maintained prose in English per [language policy](language.md).
- Follow [frontmatter](../documentation/frontmatter.md) for `docs/` Markdown pages; the reusable [documentation-authoring Skill](../../src/skills/documentation-authoring/SKILL.md) owns entrypoint and index authoring guidance. See [local entrypoint paths](../documentation/entrypoints.md) for this repository's filenames.
- Maintain one canonical page per topic and repair relevant relative links and indexes when documents move.
- Use [bundle conventions](../documentation/bundles.md) only when several pages share a purpose and lifecycle.
- Separate observed behavior from proposed behavior and label unsupported claims and unrun checks.

## Verification

Run the [document checks](../development/validation.md) and review correctness using the [documentation handbook](../documentation/README.md). Structure checks do not establish factual accuracy, external link health or agent behavior.
