---
description: "Define lightweight entrypoint gates and routing-only index documents for catalog navigation."
---

# Documentation entrypoints and indexes

## Separation of responsibilities

An entrypoint is a **small decision gate**, not the full content of a directory or Skill. A reader or agent who arrived at the wrong entrypoint should be able to reject it **before loading detailed context**.

- **`README.md`:** briefly state directory purpose, intended audience, boundaries, and link to its `index.md`. Keep inventories and detailed procedures out of the README.
- **`SKILL.md`:** begin with Agent Skills `name` and `description` discovery metadata. The description must state **when** the Skill applies, not only what it does; make overlapping task boundaries distinguishable. In the body, state triggers, exclusions, essential authority/dependencies, and next step. Stop before further loading when irrelevant.
- **`index.md` / `INDEX.md`:** use lowercase `index.md` for directory and category listings, and uppercase `INDEX.md` for routing within a Skill. Both should link to specific destinations rather than duplicate guides or policies. Read the selected target **only when needed**, not every link.
- **`AGENTS.md`:** select applicable repository maintenance rules and source, not a duplicate asset inventory or an unrestricted command to load everything.

For a catalog Skill with multiple workflows, a lightweight `SKILL.md` can link to a sibling `INDEX.md`, which links to on-demand procedures. A small Skill need not be split just to create routing layers. Never hide essential activation, permission, or safety gates exclusively in a deep document.

## Canonical entrypoints in this repository

- Root `README.md`: concise repository purpose and links to source and documentation indexes.
- `src/README.md`: brief source introduction; `src/index.md` lists asset categories.
- `src/<kind>/README.md`: category scope; `src/<kind>/index.md` lists published assets.
- `docs/README.md`: purpose of repository documentation; `docs/index.md` lists documentation areas.
- `docs/<area>/README.md`: area scope; its `index.md` lists immediate pages and child indexes.
- `src/skills/<name>/SKILL.md`: Skill activation gate; optional sibling `INDEX.md` routes to supporting files.

This catalog uses **`index.md` for directory/category inventories** and **`INDEX.md` for Skill-local routing**. Other repositories may specify different names; reusable Skills must obey the **target repository's** convention, not impose this one. Never maintain competing routing indexes in different cases.

## Gate before routing

1. Read only the entrypoint and applicable higher-priority/local rules needed to decide relevance.
2. If the reader's task does not match the stated scope, stop or redirect **without reading the index, procedures, or unrelated references**.
3. If it matches and a routing index exists, select one task-relevant destination; otherwise follow the single-workflow entrypoint directly. Do not invent an index just to satisfy a routing pattern.
4. Expand to another route only for a concrete separate task or unresolved requirement. Reuse unchanged context for the same revision.

Keep the gate concise, but explicit about the triggers, exclusions, essential dependency, authority, and where to continue. A small cost saving never justifies omitting a mandatory safety or permission check.

## Index maintenance

Use a descriptive relative link and short intent label for each immediate published asset, page, or selected workflow. Link child directories to their own `index.md`; do not duplicate the entire subtree at the root. Avoid writing full procedures, lengthy summaries, or competing policies in a routing index.

When adding, moving, or removing a document, update its nearest index and affected inbound links together. An index proves discoverability, not readiness or behavioral correctness.

## Verification

Run `python3 scripts/validate_catalog.py` for source entrypoints and `python3 scripts/validate_docs.py` for documentation metadata and local links. Manually test a matching request, a nonmatching request, and a route selection: a mismatch should stop before deeper context loads. Automated checks do not currently establish correct agent routing, external links, or technical truth.
