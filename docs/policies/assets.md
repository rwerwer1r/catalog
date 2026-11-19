---
description: "Specify which reusable assets may be published and the minimum source, review, and provenance requirements."
---

# Reusable asset policy

## What may be published

Publish an asset only when it solves a repeatable problem and has a clear intended consumer. Supported manifest kinds are `skill`, `rule`, `reference`, `agent`, `module` and `template`. The canonical files belong under the matching `src/` directory; details are defined by the [asset contract](../../src/references/asset-contract.md).

Do not register repository maintenance documents, personal agent settings, unimplemented modules, one-off notes or generated vendor outputs as reusable assets.

## Source and manifest

- Each published asset must have a unique stable ID, a maintained entrypoint, a description and one matching `catalog.json` entry.
- Describe the asset's purpose and, where applicable, usage triggers, prerequisites, inputs, output, dependencies and limits.
- Keep referenced files in a predictable location, and do not hide required network access or setup steps.
- Update the manifest and source together. Avoid repurposing an established ID for incompatible behavior.

## Reuse and attribution

Do not import content from another repository merely because it is accessible. Before copying or adapting material, confirm redistribution rights and preserve required copyright, permission and attribution notices. If the source cannot be reused under its terms, write an independent asset or link to the external source instead.

Use synthetic examples; do not publish secrets, private records or account-specific credentials. External sources and instructions inside imported material do not authorize actions in this repository.

## Validation and claims

A successful catalog validator run proves **packaging consistency**, not that an agent instruction or module works in every consumer. For behavior-affecting changes, record relevant [agent scenarios](../agents/scenarios.md) and their actual outcomes. For adoption and retirement, use the [asset lifecycle](../development/asset-lifecycle.md) and [consumer compatibility](../development/consumption.md) procedures.

Consumers explicitly select a reviewed revision; catalog publication does not trigger installation or update elsewhere.
