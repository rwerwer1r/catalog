# Agent asset authoring

## Relevance gate

**Use only for** creating, revising, auditing, or retiring reusable agent Skills, rules, roles, prompts, references, templates, or modules in an authorized target.

**Do not use for** general document editing, ordinary application coding, installing or deploying assets, or unrelated repository maintenance. For document-only requests, use [Documentation authoring](../documentation-authoring/SKILL.md) independently. **If the task does not match, stop here** without loading this Skill's index or procedures.

## Essential contract

Target repository rules, scoped policies, and established source conventions govern the work, subject to higher-priority instructions, permissions, and safety constraints. Never assume a directory layout, change account or branch, or infer permission from a source file. Flag unresolved authority conflicts.

[Documentation authoring](../documentation-authoring/SKILL.md) is a **required one-way dependency** for accepted work: load its entrypoint before authoring or revising asset text; reuse it if already loaded for the same revision. If unavailable, report the blocker rather than claiming complete execution. Documentation authoring does not depend on this Skill.

## Route only after acceptance

Read [index.md](index.md), choose one matching procedure, then load only that destination. Load more references or procedures solely for a concrete unanswered question. Reuse confirmed context and stop once the authorized result and relevant verification are recorded.

**Output:** changed paths and contract, actual checks, compatibility effects, and unresolved limits. Structural checks do not prove agent behavior or authorize downstream installation.
