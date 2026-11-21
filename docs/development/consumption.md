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

## Portable integration check

Before describing an asset as usable outside this repository:

1. Identify the target runtime's supported entrypoints, discovery and instruction-precedence rules. The catalog path convention alone does not establish target support.
2. List the asset's required references, companion Skills, tools, configuration and repository-specific policies. Carry the necessary files into the approved destination or adapt links and assumptions explicitly; do not treat a copied entrypoint as self-contained by default.
3. In an isolated consumer fixture, check one intended invocation, one out-of-scope request and the missing-dependency behavior. Avoid production writes and unapproved installations.
4. Record the selected revision, resolved dependencies, runtime, actual results and unverified cases. Structural validation within the catalog does not substitute for this check.

## Compatibility and upgrades

Review triggers, input/output contracts, changed rules, runtime assumptions, file paths and security implications before updating. Compare old and proposed behavior; run asset-specific scenarios and consumer tests. Document breaking changes and a rollback path. Retaining an old revision may be safer than unreviewed migration.

## Evidence

Use [asset lifecycle](asset-lifecycle.md) and [agent verification](../agents/verification.md) to distinguish package validity, behavioral tests and authorized consumer integration.
