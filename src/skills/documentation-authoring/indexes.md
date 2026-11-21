# Author and maintain consumer-oriented indexes

Choose the index format by **how it is maintained**, not by how many documents exist. An index lets a consumer choose relevant documents **before loading their full contents**. Describe reader intent, not just filenames.

## Manual Markdown index: INDEX.md

- **INDEX.md** is a human-maintained, *index-only* Markdown navigation file. Use concise descriptive links, grouped by distinct consumer intents. It is not a tutorial, a repeated policy document, a generated manifest, or a home for executable generation instructions.
- Update links and labels as documents change; preserve stable destinations. Read only the selected document, not the entire set.
- **Do not add an automatic index generation script for INDEX.md.** If the target repository already uses a different case (for example, category `index.md`), preserve that established manual-index path; do not rename it or create a competing `INDEX.md` merely to match this example.

## Generated metadata index: INDEX.tsv

When a script builds or refreshes an index **from document frontmatter or structured fields**, use **INDEX.tsv**, not INDEX.md. Keep the generator as a separate authorized script, never embedded in an index. Do not invent a generator when no automation is needed.

- UTF-8, tab-separated, **one header line**. Required columns, in order: `path` and `description`. Optional named columns, added only for genuine consumer needs: `title`, `audience`, `status`, `tags`.
- `path`: unique, canonical, repository- or index-relative existing document path according to the target's convention; no traversal outside the authorized root, URLs, or unapproved symlinks. `description`: nonempty, concise, **source-backed** explanation of when to read that document. Do not substitute a filename or fabricate missing metadata.
- Other fields come from maintained frontmatter or equivalent source fields. Use one line per record; disallow raw tabs/newlines in cells. Normalize and sort deterministically by path; keep column meanings stable for consumers.
- Generation must detect missing or duplicate paths, absent descriptions, outdated or unsupported source metadata, and stale rows. Fail or surface a gap instead of quietly guessing. If generation is available, compare the regenerated TSV with the committed artifact before publishing.
- Consumers select by `description` first, using optional audience/status/tags only if present. Resolve the chosen `path` to its canonical document and load that target on demand. Metadata is a discovery hint, not evidence that the content is accurate.

Example minimal TSV (the separator between columns is a literal tab):

```tsv
path	description
getting-started.md	Start here to configure the project's development environment.
troubleshooting.md	Use when a setup check fails or produces an unexpected result.
```

## Ownership and coexistence

Maintain **one canonical index for a given navigation role**. A manual README/INDEX.md can point consumers to an INDEX.tsv only when it offers a *different interface* (human navigation versus machine-readable metadata); never keep two independently authoritative duplicate inventories. Existing repository-mandated lowercase `index.md` listings remain manual Markdown; do not convert them to TSV unless actual metadata-driven generation is requested and compatible.

The target's policies govern allowed fields, frontmatter syntax, scripts, validation, and naming. Do not make a metadata index mandatory for simple hand-maintained navigation or claim a generator ran when it did not.
