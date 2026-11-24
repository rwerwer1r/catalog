---
description: "Guidance for coherent multi-page documentation bundles with concise introductions and indexes."
---

# Bundle documents

## When to bundle

Use a bundle when a topic requires several closely related pages with shared prerequisites, ownership or lifecycle. Do not create one for a single short procedure or merely to mirror existing canonical content.

## Layout

Each bundle has a **short `README.md` introduction** and a separate `INDEX.md` listing its member pages in the intended reading order:

```text
docs/<area>/<topic>/
  README.md
  INDEX.md
  overview.md
  procedure.md
  verification.md
```

The README states the goal, audience and an index link. The index links to every immediate member and any child indexes; include selection and reading order where useful. Each member must be understandable independently and follow [frontmatter rules](frontmatter.md).

## Ownership and reuse

Give the bundle one canonical home. Reusable Skills, modules and references belong under `src/` and are discovered through their category `INDEX.md`; bundles may link to them but must not copy authoritative source. A bundle cannot change repository permissions or automatically install assets.

## Review

Check that the index covers all member pages, all relative links exist, prerequisites are explicit and instructions do not contradict repository policy. Run the [documentation checks](../development/validation.md) and report any untested behavior as not run.
