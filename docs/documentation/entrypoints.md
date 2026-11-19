---
description: "Rules for lightweight README introductions and index.md navigation."
---

# Documentation entrypoints and indexes

## Separation of responsibilities

Keep **`README.md` short**: state the directory's purpose, who should use it, and link to `index.md`. Put the maintained **list of pages and assets in `index.md`**. Do not maintain competing lists in both files.

- Root `README.md`: concise repository purpose and links to the source and documentation indexes.
- `src/README.md`: brief introduction to reusable source; `src/index.md` lists asset categories.
- Each `src/<kind>/README.md`: category scope; its `index.md` lists all published entrypoints in that category.
- `docs/README.md`: purpose of repository documentation; `docs/index.md` lists documentation areas.
- Each `docs/<area>/README.md`: area scope; its `index.md` lists immediate pages and child area indexes.
- Root `AGENTS.md`: repository-maintenance instructions. It selects task-relevant policies and sources, not a duplicate asset inventory.

## Index maintenance

Use descriptive relative links and a single canonical index in each directory. Link directly to each immediate published asset or document from its nearest index; link child directories to their own `index.md`. Avoid repeating a flat list of every file at the repository root.

When adding, moving or removing an item, update its nearest index and any affected inbound links in the same change. An index is for discovery; it does not assert that a Skill, module or procedure has been behaviorally verified.

## Verification

Run `python3 scripts/validate_catalog.py` for source entrypoints and `python3 scripts/validate_docs.py` for document indexes and local links. Check heading anchors, external URLs and navigation clarity manually; these are not fully covered by the scripts.
