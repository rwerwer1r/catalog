---
description: "Workflow for contributing reusable assets and documentation to the catalog."
---

# Contributing assets

1. Identify the reusable problem and intended consumers. Check `catalog.json` and [architecture](architecture.md) for duplicates and ownership.
2. Read [policies](../policies/README.md), especially [language](../policies/language.md), [security](../policies/security.md) and [provenance](../policies/provenance.md).
3. Follow [asset lifecycle](asset-lifecycle.md); choose the kind and write a canonical `src/` entrypoint that declares prerequisites, inputs, outputs and limits.
4. Register the entrypoint in `catalog.json`, update relevant indexes and follow [documentation conventions](../documentation/README.md).
5. Run [validation](validation.md). For changes affecting agent behavior, define [representative scenarios](../agents/scenarios.md) and record actual [verification](../agents/verification.md).
6. Review compatibility with consumers through [consumption guidance](consumption.md), especially if an ID, contract or dependency changes.
7. Inspect the final diff for unrelated changes, secrets, unsupported claims and stale links before proposing the change.

## Review and adoption

A passing metadata check means an asset is structurally valid, not that it is operationally verified. The consumer must approve integration and retain responsibility for its account, tests and releases. Keep transient private notes and generated vendor projections out of the reusable tree.
