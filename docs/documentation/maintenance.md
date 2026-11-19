---
description: "Update, move, deprecate, and retire documentation without breaking canonical navigation."
---

# Documentation maintenance

## Triggers

Review documentation when source behavior, paths, commands, dependencies, security assumptions, supported versions or consumer expectations change. Also review when a page repeatedly causes navigation failures or has competing sources of truth.

## Update in place first

Prefer editing the canonical page over creating another page with almost the same content. Keep filenames and headings stable when readers may link to them. When behavior changes, update the example, prerequisites, verification instructions and index descriptions in the same change.

## Move or split

1. Identify the current owning page and inbound references.
2. Select the new canonical location according to [information architecture](information-architecture.md).
3. Move content without silently changing its meaning. Split only along clear reader tasks or ownership boundaries.
4. Repair relative links, anchors, directory entrypoints, policy links and agent routing references.
5. Check navigation from the repository index and the closest domain entrypoint.

A simple file move should not implicitly expand the document's authority.

## Deprecate or retire

When a page must remain visible during migration, set `status: deprecated` in its [frontmatter](frontmatter.md) and add a prominent replacement link and reason near the heading. Give migration instructions if the old procedure is still in use. When the page is no longer referenced or needed, remove it with its inbound links and indexes in the same change.

Do not add an expiration date unless someone owns the review process. Do not preserve obsolete instructions only to avoid changing links.

## Periodic hygiene

At meaningful release or workflow changes, sample high-traffic entrypoints, check stale commands and external references, and reconcile instructions with the actual code. Document which checks were run; never imply that an automated site-wide scan exists unless it does.
