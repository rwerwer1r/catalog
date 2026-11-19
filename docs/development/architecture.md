---
description: "Boundaries and scaling model for reusable source, documentation, tooling, and consumers."
---

# Repository architecture

## Purpose

The catalog is a versioned collection of reusable source assets intended for selective use by other repositories. It is not a central controller of consumer accounts.

## Ownership map

- `src/` owns canonical Skills, rules, references, agent roles, modules and templates.
- `src/README.md` and each category README index source entrypoints; directory paths identify assets. No separate registry is maintained.
- `docs/` owns maintenance policies, development procedures, documentation conventions and agent harness guidance.
- `tools/` and `tests/` validate structural contracts using standard-library Python.
- `.github/workflows/` runs repository checks; CI does not exercise all downstream agent behavior.

## Design for growth

Use one stable ID per asset and one canonical page per maintenance topic. Keep directory indexes focused on immediate children and selection criteria. Use links rather than duplicating lengthy text. Add subdirectories only when there is a real distinct owner, interface or lifecycle; never turn every change into a new global rule.

Distinguish **asset publication**, **behavioral evaluation** and **consumer adoption**. A README link is a source of discovery, not a release badge. Follow [lifecycle](asset-lifecycle.md) and [compatibility](consumption.md) guidance.

## No hidden deployment

There is no automatic installer or synchronization. Any downstream deployment, upgrade, runtime, or account-specific process belongs to the consuming repository and requires its own authorization.
