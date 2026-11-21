# Author consumer-oriented indexes

An index helps consumers select documents **before loading them**. Choose format by maintenance mode; follow target repository naming rules.

## Manual Markdown: INDEX.md

**INDEX.md is a hand-maintained, index-only Markdown navigator.** Use descriptive links grouped by reader intent; omit tutorials, repeated policies, copied inventories, and generation instructions. Never attach an auto-generation script to INDEX.md. Update links when destinations change; read only the chosen page.

Existing manual `index.md` files remain valid when target rules require lowercase. Do not rename or create a competing index.

## Metadata-generated index: INDEX.tsv

**Use INDEX.tsv when an authorized script builds the index from document frontmatter or structured fields.** The separate generator must not write INDEX.md; do not invent a generator without a real automation need.

- UTF-8 TSV with a single header. Required columns in order: **`path`**, **`description`**. Optional source-backed columns: **`title`**, **`audience`**, **`status`**, **`tags`**.
- One row per existing document. `path` is unique and canonical, relative to the target-approved root; reject external URLs, root escapes, and unapproved symlinks.
- `description` tells a consumer **when to read** the document. Derive it and optional values from maintained metadata; never guess a summary from its filename or invent missing values.
- Single-line values without literal tabs/newlines. Sort by path, preserve column semantics; reject duplicate or stale paths, missing descriptions, and source/TSV drift. If a generator exists, compare regenerated output before publishing.
- Consumers select using descriptions and optional fields, then load the chosen page only. Metadata is a discovery aid, not factual verification.

Example (literal tabs between columns):

```tsv
path	description
setup.md	Use when preparing the development environment.
repair.md	Use when troubleshooting a failed setup step.
```

## One source of navigation truth

Keep **one canonical index per navigation role**. Manual Markdown and TSV may coexist for different interfaces, not duplicate independently edited inventories. Existing category `index.md` stays manual unless a compatible metadata-generated replacement is requested.

Respect target rules for scripts, metadata, naming, and validation. Never create extra indexes or manufactured metadata solely to satisfy format preferences.
