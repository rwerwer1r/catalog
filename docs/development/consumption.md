---
description: "Select, pin, integrate, and upgrade catalog assets in authorized consuming repositories."
---

# Asset consumption and compatibility

## Selection

Start from `src/index.md` and the appropriate category `index.md` to find a candidate, then read the complete entrypoint and any explicitly referenced prerequisites. Choose the **smallest asset set** that solves the consumer task; do not fetch or install the entire catalog by default.

## Ownership and installation

The consumer retains authority over its working tree, policies, credentials, build tools and releases. Catalog inclusion grants no permission to write to a consumer, change accounts, run remote scripts or create network connections. Confirm the intended owner and repository before integration.

A consumer may copy, vendor or otherwise reference reviewed assets using its own approved tooling. This repository currently provides **no installer, package registry or automatic sync service**. Do not document an integration command as available unless it exists and has been tested.

## Reproducibility

Record the selected asset ID, catalog commit SHA or immutable release reference, local destination, required dependencies and any local modifications. Avoid tracking an unreviewed moving branch as the only production provenance.

## Compatibility and upgrades

Review triggers, input/output contracts, changed rules, runtime assumptions, file paths and security implications before updating. Compare old and proposed behavior; run asset-specific scenarios and consumer tests. Document breaking changes and a rollback path. Retaining an old revision may be safer than unreviewed migration.

## Evidence

Use [asset lifecycle](asset-lifecycle.md) and [agent verification](../agents/verification.md) to distinguish package validity, behavioral tests and authorized consumer integration.
