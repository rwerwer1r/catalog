# Agent asset authoring

## Use when

Create, extend, review, or retire reusable assets that guide or support AI agents, such as Skills, rules, agent roles, prompts, references, templates, and executable modules. Use this workflow in any repository or workspace with authorization to maintain those assets. It does not install, deploy, or synchronize them into other environments.

## Required dependency

[Documentation authoring](../documentation-authoring/SKILL.md) is a **required companion Skill**, not an optional reference.

1. Load and apply the documentation-authoring Skill before drafting or modifying any asset entrypoint, supporting Markdown, README, or index.
2. Use **this Skill** for asset identity, behavior contracts, packaging, dependencies, compatibility, and verification. Use **documentation authoring** for reader intent, accurate prose, information architecture, examples, links, and metadata.
3. The destination repository's authorized conventions take precedence over either Skill's fallback defaults. Do not treat the companion Skill as permission to edit unrelated documents.
4. When distributing this Skill, include its sibling `documentation-authoring/SKILL.md` or explicitly remap the dependency to an equivalent installed path. If the required dependency cannot be loaded, report the blockage; do not claim the complete authoring workflow was followed.

Documentation authoring has no dependency on this Skill, so the dependency direction is one-way.

## Inputs

- Requested reusable capability, intended agent or consumer, triggering conditions, and observable success criteria.
- Authorized repository, account or workspace, target branch, and permitted side effects.
- Existing asset contracts, source layout, category indexes, supported runtime, and known compatibility constraints.
- Available tests, scenarios, and publication requirements.

## Workflow

1. **Resolve authority and context.** Confirm the target and permissions. Inspect only relevant project instructions, source conventions, index pages, and related assets. Never assume a specific repository name, directory layout, account, runtime, or installation method.
2. **Decide whether to create or revise.** Identify a repeatable problem and check for equivalent assets. Prefer extending an existing contract where compatible; document the intended consumer, non-goals, inputs, output, dependencies, and failure boundaries.
3. **Select an asset type and stable identifier.** Respect the target repository's asset categories, naming, packaging, and entrypoint schema. If no contract exists, propose a small, explicit layout before introducing new directories. Paths such as `skills/<name>/SKILL.md` are examples, not universal requirements.
4. **Define operational behavior.** Specify when the asset activates, what context it needs, ordered actions and decisions, stop or escalation conditions, tool access, prohibited effects, and the evidence to return. Prefer progressive loading of optional references over broad context injection.
5. **Author through the required documentation Skill.** Apply [Documentation authoring](../documentation-authoring/SKILL.md) to the entrypoint, adjacent instructions, examples, metadata, and discovery pages. Keep the contract self-contained enough to function without conversation history. Keep reusable behavior separate from repository-specific governance; link to local policy only when the target repository requires it.
6. **Package and register.** Put the canonical entrypoint and genuinely necessary supporting files in their owning location. Update the nearest existing index or registry according to local conventions; do not create competing inventories. Preserve stable public paths or document migration steps for breaking changes. Do not publish empty modules as working implementations.
7. **Validate in layers.** Review the diff, links, naming, language, licenses, privacy and side effects. Run available structural checks and tests. For behavior changes, define and execute a representative controlled scenario when authorized; record its actual outcome. Consumer integration requires separate authorization.
8. **Report.** List changed paths, the reusable contract, dependency packaging, compatibility impact, performed checks, and unverified behavior or blockers.

## Asset contract checklist

An independent consumer should be able to determine **when to use the asset**, **what to provide**, **what it does**, **what it produces**, **which dependencies are required**, **when it must stop**, and **what evidence supports its readiness**. For Skills, keep the entrypoint concise and make supporting documents loadable only when relevant.

## Verification and output

Prefer the destination repository's documented validation commands; do not assume that another project's scripts or CI exist. Distinguish structural checks, behavior scenarios, and authorized downstream integration. Report each relevant check as **passed**, **failed**, **not run**, or **not applicable** with evidence. Structural validity is not proof of correct agent behavior; source publication is not consumer installation or approval.
