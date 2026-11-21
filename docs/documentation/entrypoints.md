---
description: "Locate this catalog's reader entrypoints and local navigation filenames."
---

# Catalog entrypoints

The reusable [entrypoint authoring](../../src/skills/documentation-authoring/references/entrypoints.md) and [index authoring](../../src/skills/documentation-authoring/references/indexes.md) procedures are the **canonical owners** of README.md, SKILL.md, manual INDEX.md, and generated INDEX.tsv authoring rules. Apply [local frontmatter](frontmatter.md) to maintained documentation here. This page lists only repository-specific paths.

## Existing paths

| Scope | Entrypoint | Manual navigation |
| --- | --- | --- |
| Repository | `README.md` | `src/INDEX.md` or `docs/INDEX.md` |
| Source category | `src/<kind>/README.md` | `src/<kind>/INDEX.md` |
| Documentation area | `docs/<area>/README.md` | `docs/<area>/INDEX.md` |
| Multi-route Skill | `src/skills/<name>/SKILL.md` | `src/skills/<name>/references/INDEX.md` |
| Single-workflow Skill | `src/skills/<name>/SKILL.md` | None required |

Uppercase `INDEX.md` files are canonical hand-maintained navigation after migration. Do not retain competing lowercase indexes. If a future authorized generator derives a metadata index from document frontmatter or fields, its output is `INDEX.tsv`, governed by the linked index procedure; no such generator is implied by these existing paths.

## Local verification

From the repository root, run `python3 scripts/validate_catalog.py` and `python3 scripts/validate_docs.py` when available. These validate structure, not real agent route selection, source accuracy, or generator output that has not been created.
