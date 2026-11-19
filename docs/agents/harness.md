---
description: "Document-first loading and verification model for repository-maintenance agents."
---

# Document-first agent harness

## Goal

Make agent behavior reviewable through a stable hierarchy of documents before introducing complex runtime integration. The harness combines policies, operational instructions, task-specific source, evidence and small mechanical checks.

## Document loading

1. Repository-level entrypoint: [AGENTS.md](../../AGENTS.md).
2. Mandatory maintenance policies: [policies index](../policies/README.md).
3. Task guidance: [operating model](operating-model.md) plus the relevant [development topic](../development/README.md) or [documentation topic](../documentation/README.md).
4. Only the selected reusable asset in `src/`, using `catalog.json` for discovery.

Use [entrypoint conventions](../documentation/entrypoints.md) to find canonical material and [bundle rules](../documentation/bundles.md) when a task spans a document set. Avoid loading unrelated assets, copying policy text or allowing selected assets to override repository authority.

## Verification layers

- **Documentation:** check scope, expected behavior, inputs, permissions, frontmatter, entrypoints and links against the canonical source.
- **Packaging:** run `tools/validate_catalog.py` and the standard-library unit tests.
- **Behavior:** perform a representative controlled agent task when the changed asset affects agent actions, and record actual evidence.
- **Integration:** validate the asset in an authorized consumer repository before claiming production readiness.

These layers are distinct. A successful packaging check does not prove agent behavior, and a written procedure is not evidence that it ran.

## Change control

Update the asset and its manifest entry together. Modify harness guidance when its contract changes. Use [verification records](verification.md) to disclose checks, failures and unverified behaviors.
