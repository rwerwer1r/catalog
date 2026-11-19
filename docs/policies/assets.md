---
description: "Specify the source layout and review criteria for reusable catalog assets."
---

# Reusable asset policy

## Published source

Publish a reusable item only when it solves a repeatable problem with a defined consumer. Supported source categories are `skills`, `rules`, `references`, `agents`, `modules` and `templates`.

The source path is the durable identifier. Use lowercase kebab-case filenames or directories and preserve existing paths when consumers may depend on them. File and entrypoint rules are explained in the [asset contract](../../src/references/asset-contract.md).

## Source and discovery

- Maintain one canonical entrypoint per asset under its category.
- Add a descriptive link from the **nearest category README**; keep the `src/README.md` index at category level.
- State purpose, prerequisites, inputs, outputs and relevant dependencies or limitations in the asset itself.
- Do not duplicate the directory inventory in a separate JSON, YAML or generated registration file.
- Keep required supporting files alongside their owning Skill or module.
- Avoid reusing an existing path for an incompatible contract.

## Publication review

Before adapting external material, verify that its license allows redistribution and preserve required notices. Do not include credentials, private records or undocumented account-specific assumptions. Confirm dependencies and any external effects before recommending use.

Run [validation](../development/validation.md) and verify source-index links. If an agent behavior contract changes, review [scenarios](../agents/scenarios.md) and record actual outcomes. Structural validation does not establish downstream safety or correctness.

## Consumers

Consumers select reviewed revisions. Source publication does not install, synchronize, deploy or grant write permissions in another repository. See [consumption guidance](../development/consumption.md) and [lifecycle](../development/asset-lifecycle.md) for compatibility and retirement.
