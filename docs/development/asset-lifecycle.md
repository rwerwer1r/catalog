---
description: "Manage reusable assets from proposal through validation, adoption, revision, and retirement."
---

# Asset lifecycle

## States and evidence

A source asset listed in its category index is **discoverable**, not automatically production-ready. The following working states belong in review records, not in a central registry.

| State | Meaning | Required evidence |
| --- | --- | --- |
| Proposed | Scope, consumers, and entrypoint are being defined | Problem statement and non-goals |
| Implemented | Canonical source and category index are in sync | Source diff and packaging checks |
| Evaluated | Representative scenarios have been tested | [Scenario results](../agents/scenarios.md) and environment |
| Adopted | A named consumer uses a reviewed revision | Consumer reference and explicit approval |
| Deprecated | A replacement or removal plan exists | Replacement link and impact assessment |
| Retired | No supported consumer requires the entrypoint | Migration note and source/index link cleanup |

Do not treat these labels as API guarantees. Avoid untracked status claims in prose; record concrete evidence alongside any readiness statement.

## Create and revise

1. Identify the consumer problem; confirm the asset does not duplicate an existing entry.
2. Choose a kind and unique ID using [architecture](architecture.md), [asset policy](../policies/assets.md) and [asset contract](../../src/references/asset-contract.md).
3. Implement canonical source under `src/`, declare prerequisites and constraints, then update its category index.
4. Run [validation](validation.md) and execute representative scenarios for behavior-affecting changes.
5. Describe compatibility, migration impact and test evidence in the pull request.

## Deprecate and retire

Never silently repurpose an established asset ID. Identify consumers when known, publish a replacement and migration instructions, and avoid removing an entrypoint until the impact is reviewed. If no consumer inventory exists, record that uncertainty. Removal and renaming may be breaking changes even when CI passes.

## Boundaries

The catalog does not automatically deploy, update or inspect consuming repositories. Adoption and rollback belong to each authorized consumer; see [consumption](consumption.md).
