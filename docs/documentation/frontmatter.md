---
description: "Rules for consistent YAML frontmatter in maintained catalog documentation."
---

# Frontmatter rules

## Scope

All maintained Markdown files under `docs/`, including directory README and index files, use a frontmatter block. This requirement does not automatically apply to `src/` assets, root `README.md`, or root `AGENTS.md`.

## Format

Place `---` on the first line, followed by one metadata entry per line and closing `---`. Leave one blank line before exactly one H1.

```yaml
---
description: "How to select and review documentation entrypoints."
---
```

- **Required:** `description` — one nonempty, plain-English sentence telling a consumer **when and why to read** the document, with enough distinction from neighboring pages to choose before loading their full contents.
- **Optional:** `status` — `draft`, `active`, or `deprecated` when relevant.
- **Optional:** `audience` — a short intended reader group where necessary.
- Do not add timestamps, personal identifiers, generated metadata or unreviewed keys.
- Use simple scalar values; do not embed executable content or multiline instructions.

## Consistency

Metadata aids discovery but never overrides policies, displayed text or canonical source files. Keep the description accurate after changes. If an authorized generator derives `INDEX.tsv` from frontmatter, use these maintained fields as its source; do not generate `INDEX.md` or infer missing descriptions. The reusable [index contract](../../src/skills/documentation-authoring/references/indexes.md) owns generated-versus-manual behavior. Write a clear H1 and logical subordinate headings.

## Verification

The [documentation validator](../development/validation.md) checks supported flat frontmatter keys, required description and one H1. It is not a general YAML parser. Human review remains responsible for accuracy, meaningful summaries and language.
