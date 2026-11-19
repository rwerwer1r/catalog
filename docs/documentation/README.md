---
description: "Index of documentation authoring conventions for the catalog."
---

# Documentation authoring

This area defines **how documentation is structured and discovered**. It is not a replacement for [repository policies](../policies/README.md), which remain authoritative for mandatory requirements.

| Topic | When to read |
| --- | --- |
| [Frontmatter](frontmatter.md) | Create or update Markdown metadata |
| [Entrypoints](entrypoints.md) | Add a documentation area or change navigation |
| [Bundle documents](bundles.md) | Publish a self-contained document set for a task or consumer |

Follow the [English language policy](../policies/language.md) and [documentation policy](../policies/documentation.md). Maintain one canonical source per topic, link from the appropriate entrypoint, and validate internal links before merging.

## Authoring workflow

1. Identify the intended reader and the document's owning directory.
2. Choose a single document or a bundle based on the reader's actual navigation needs.
3. Add the required frontmatter and a clear first-level heading.
4. Update the nearest entrypoint and any direct references to the moved or changed file.
5. Review for duplication, stale instructions and accessibility without unrelated context.
6. Run repository validation and record any manual checks separately.
