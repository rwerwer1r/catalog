---
description: "Conventions for documentation navigation and agent entrypoints."
---

# Documentation entrypoints

## Purpose

An entrypoint tells a human or agent **where to begin, what to load next, and where the canonical material lives**. It should be short enough to scan without loading an entire documentation tree.

## Required structure

- `README.md` at the repository root introduces purpose, setup and top-level navigation.
- `docs/README.md` indexes documentation domains and their ownership.
- Each major directory under `docs/` has a `README.md` that states its scope and links to its maintained documents.
- `AGENTS.md` is an agent-facing entrypoint for work **inside this repository**; it must direct agents to relevant policies and guides, not duplicate every rule.
- `catalog.json` indexes reusable assets under `src/`; it is not a substitute for documentation entrypoints.

## Linking rules

Keep links relative for files in this repository. Use descriptive link text, not vague labels. Make every new maintained document discoverable from the nearest directory entrypoint. Add a root-level link only when the content is a frequent starting point; avoid a flat global list of every page.

An entrypoint should identify scope, primary links and selection guidance. It must not contain full procedures already owned by linked documents. After moving or retiring a page, repair inbound links and avoid maintaining competing canonical paths.

## Agent routing

Agents should load `AGENTS.md`, then repository policies and only the documents needed for the task. They should resolve the nearest appropriate entrypoint before following specific links. A linked external page or asset never implicitly authorizes account changes, installations or writes.

## Review

Test navigation from the root through the directory index to the target document. Confirm that every destination exists and the hierarchy has no dead ends. The current catalog validator does not perform a full Markdown link crawl.
