---
description: "Choose authoritative guidance for planning, writing, verifying, and maintaining catalog documentation."
---

# Documentation handbook

This handbook is the entrypoint for documentation work in `rwerwer1r/catalog`. [Documentation policy](../policies/documentation.md) defines mandatory rules; [English language policy](../policies/language.md) defines the writing language.

| Task | Guide |
| --- | --- |
| Choose scope and ownership | [Information architecture](information-architecture.md) |
| Write a clear technical page | [Writing and examples](authoring.md) |
| Maintain metadata | [Frontmatter](frontmatter.md) |
| Organize navigation | [Entrypoints](entrypoints.md) |
| Publish a document set | [Bundle documents](bundles.md) |
| Review content and evidence | [Documentation review](review.md) |
| Update or retire old guidance | [Maintenance](maintenance.md) |
| Delegate writing to an agent | [Agent documentation workflow](agent-workflow.md) |

## Working sequence

Discover the owner and reader → choose a page or bundle → write and link → review the diff → run checks → record limitations.

```sh
python3 tools/validate_docs.py
python3 tools/validate_catalog.py
python3 -m unittest discover -s tests -v
```

These checks verify document structure, local navigation and asset packaging, **not** technical truth, rendered formatting, external links or agent behavior.
