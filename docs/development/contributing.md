---
description: "Workflow for contributing reusable assets and documentation to the catalog."
---

# Contributing assets

1. Identify the reusable problem and intended consumers. Browse the relevant category index and files for duplicates and read the [repository policy](../policies/repository.md).
2. Choose the appropriate `src/` kind and apply the [asset policy](../policies/assets.md) and [asset contract](../../src/references/asset-contract.md).
3. Write a canonical entrypoint describing triggers, prerequisites, expected output, dependencies and limits where relevant.
4. Update the category index, relevant entrypoints and any affected documentation following [documentation conventions](../documentation/README.md).
5. Run [validation](validation.md). For behavior changes, execute [agent scenarios](../agents/scenarios.md) or record unverified cases using [verification](../agents/verification.md).
6. Check consumer compatibility and migrations through [asset lifecycle](asset-lifecycle.md) and [consumption](consumption.md) when applicable.
7. Review the diff for licensing obligations, unrelated edits, private content and stale links.

## Review and adoption

Catalog publication is not automatic consumer adoption. A passing structural check is not proof of runtime behavior. Consumer repositories select their own compatible versions and retain their own permissions.
