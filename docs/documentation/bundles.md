---
description: "Requirements for organizing and reviewing self-contained document bundles."
---

# Bundle documents

## Definition

A **documentation bundle** is a small, coherent set of related documents with one explicit starting page. It is useful when a topic needs multiple procedures, decisions or references that should travel together. Do not create bundles for single-page topics or to duplicate content already owned elsewhere.

## Layout

Use a dedicated directory with a `README.md` entrypoint and descriptive filenames. Example:

```text
docs/<area>/<topic>/
  README.md
  overview.md
  procedure.md
  verification.md
```

The `README.md` must state the bundle's goal, intended audience, scope, prerequisites, reading order and links to each member. Member files should link back to the bundle entrypoint when readers are likely to encounter them independently. Follow [frontmatter rules](frontmatter.md) for new bundle documents.

## Ownership and boundaries

Give the bundle one canonical owning directory and one clear lifecycle. A bundle groups documents; it does not create a new permission boundary, override policies or automatically become a reusable `src/` asset.

If a downstream repository needs a reusable Skill, module or reference, publish that source under `src/` and register it in `catalog.json`. Link to the asset from the bundle instead of copying its source or treating a bundle as an installer.

## Verification

Before publishing or moving a bundle:

1. Check that its entrypoint explains selection and reading order.
2. Verify every included document is linked and every local link resolves.
3. Confirm that procedures can be followed using stated prerequisites, without hidden dependencies.
4. Check that ownership is unambiguous and no contradictory policy copies exist.
5. Document untested behavior as unverified; a complete bundle is not proof that instructions work in a real environment.

Do not mark bundles as validated by automation unless the actual checks have run.
