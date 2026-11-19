---
description: "Rules for concise YAML frontmatter in catalog Markdown documents."
---

# Frontmatter rules

## Scope

Use a YAML frontmatter block at the beginning of **new and substantially rewritten Markdown documents under `docs/`**. Existing files may adopt it progressively; do not rewrite unrelated documents solely to add metadata. Repository-level `README.md`, `AGENTS.md`, and reusable asset entrypoints under `src/` are outside this requirement unless their own contracts say otherwise.

## Format

Place the opening `---` on the first line, followed by a short set of metadata fields and a closing `---`. Leave one blank line before the page's single H1 heading.

```yaml
---
description: "How to select and review documentation entrypoints."
---
```

- **Required:** `description` — a single nonempty, plain-English sentence describing when the document is useful.
- **Optional:** `status` — `draft`, `active`, or `deprecated`, only if lifecycle tracking is meaningful.
- **Optional:** `audience` — a short human-readable audience such as `maintainers` or `consumers`, when the audience is not obvious.
- Do not add timestamps, author identifiers, generated fields, arbitrary tags or ownership fields without an established maintainer workflow that uses them.
- Quote values containing punctuation and do not embed multiline instructions, secrets, or executable expressions in metadata.

## Consistency rules

Frontmatter supports discovery; it does **not** override the visible text, a policy, or the manifest. Write one H1 after the metadata and use descriptive H2 headings. Keep the description accurate when a document changes. A reader must understand the document even if their renderer ignores frontmatter.

## Review

Confirm the delimiters, required description, valid optional values, H1, and language policy. The existing catalog validator does not parse documentation frontmatter; these are manual review requirements unless a dedicated check is added.
