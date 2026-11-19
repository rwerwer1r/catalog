---
description: "Boundaries and scaling model for reusable source and documentation."
---

# Repository architecture

## Purpose

The catalog holds reusable assets for adoption by other repositories, independently of any particular consumer, runtime, or agent product.

## Ownership model

- `src/` contains canonical reusable source, grouped by kind (`skills`, `rules`, `references`, `agents`, `modules`, `templates`).
- `catalog.json` is a machine-readable inventory and entrypoint map; it is not the authority for behavior or permission.
- `docs/` contains maintenance contracts, policies and agent harness guidance.
- `tools/` and `tests/` implement mechanical validation of the catalog.
- `.github/workflows/` runs repository checks but does not verify downstream agent behavior.

## Scale and discoverability

Give each topic one canonical document and each publishable asset one unique ID. Keep indexes short and organized by intent. Prefer links to copying long instructions. Add a new document when it has a distinct owner or review lifecycle, not merely to increase file count.

Consumers select specific assets and reviewed revisions. No automatic sync, installation, or cross-account write is implied by catalog membership.
