---
description: "Conventions for scalable documentation navigation and agent entrypoints."
---

# Documentation entrypoints

## Purpose

An entrypoint tells a reader where to begin, which material to select next and where the authoritative instructions live. Keep it short and navigable rather than duplicating detailed procedures.

## Required structure

- Root `README.md` introduces purpose and links to documentation domains.
- `docs/README.md` lists maintained domains.
- Every directory under `docs/` has a `README.md` with direct links to each immediate document and child directory.
- Root `AGENTS.md` is the agent entrypoint for **this repository**; it routes to policies and task-specific guides.
- `catalog.json` is the entrypoint map for reusable `src/` assets, not a documentation index.

## Linking and growth

Use repository-relative links and descriptive anchor text. Make each document reachable from its nearest directory README; reserve the root navigation for major domains. An entrypoint describes scope and reading order but does not reproduce full procedures.

When moving or retiring files, update inbound links and the nearest index in one change. A link to external material does not authorize account changes, installations or writes.

## Review

Run `python3 tools/validate_docs.py` to check directory index coverage and file-link existence. Manually inspect heading anchors, external URLs, rendered navigation and reader clarity; the script does not validate those.
