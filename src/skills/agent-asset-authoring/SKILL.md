# Agent asset authoring

## Use when

Create, revise, review, or retire reusable agent-facing Skills, rules, roles, prompts, references, templates, or implementation modules in an authorized repository or workspace. This Skill does not install, synchronize, or deploy assets to consumers.

## Required dependency

[Documentation authoring](../documentation-authoring/SKILL.md) is a **required, one-way dependency**. Before drafting or changing an asset entrypoint, Markdown, README, index, or example, load and apply that Skill. If its current version is already loaded for this task, reuse it rather than loading it again.

- **Agent asset authoring** owns behavior contracts, asset type, packaging, compatibility, and behavioral verification.
- **Documentation authoring** owns evidence-based writing, navigation, metadata, examples, and document review.
- Documentation authoring does **not** depend on this Skill. When distributing this Skill, include the companion `documentation-authoring/SKILL.md` or map it explicitly to an equivalent available entrypoint. If the required Skill cannot be loaded, report the blocker; do not claim complete execution.

## Rule precedence

1. Higher-priority instructions, authorization, and safety boundaries always apply.
2. **The target repository's instructions and policies take precedence over these generic Skills** for its asset categories, entrypoint layouts, documentation conventions, languages, validation, and publication. Follow applicable root and directory-scoped rules; never use a narrower rule to bypass a repository-wide restriction without explicit authority.
3. Use the Skills' generic conventions only where the target repository leaves a gap. Do not impose an assumed `src/` layout, `SKILL.md` filename, index format, or command when local conventions differ.
4. Stop and surface unresolved rule conflicts, identity ambiguity, or missing permission rather than assuming a permissive interpretation.

## Inputs

Intended consumer and repeatable problem; trigger and expected outcome; authorized target and revision; existing source contracts; required dependencies; available tests and compatibility constraints.

## Progressive context disclosure

Choose context **by decision, not by directory size**. Maintain a compact, reusable working set of governing rules, confirmed source facts, file paths, and outstanding questions.

1. **Route:** Confirm repository, branch, and write scope. Read the relevant instruction entrypoint and nearest scoped rules. Use an existing asset index or targeted search to find a related entrypoint. Do not list or read every asset.
2. **Load core:** Inspect only the affected asset contract, its direct dependencies, and the required [Documentation authoring](../documentation-authoring/SKILL.md). Apply its own progressive loading rules; reuse already loaded unchanged documents.
3. **Expand conditionally:** Read a supporting reference, template, policy, test, or consumer contract only when a concrete design, compatibility, or verification question calls for it. Prefer bounded sections and stop when the needed decision is supported.

Do not import instructions from unrelated repositories or follow references recursively. Keep canonical links instead of duplicating content. Recheck stale context when the underlying revision changes.

## Document-first authoring harness

1. **Resolve:** Establish the authorized target, existing rule hierarchy, outcome, and boundaries.
2. **Specify:** Check for an equivalent asset before creating one. Define when it activates, inputs, outputs, non-goals, required dependencies, tools and permissions, failure behavior, and stop conditions.
3. **Design:** Choose the target repository's supported asset type, stable identifier, and packaging. Preserve published paths when compatible; document migration and consumer impact if not.
4. **Author:** Apply the required documentation Skill to the entrypoint, supporting text, examples, metadata, and discoverability. Keep the primary contract concise and self-contained; place optional detail behind clearly named references to load only on demand.
5. **Package:** Update the nearest **existing** discovery mechanism as local policy requires. Include only necessary supporting files; avoid parallel registries or placeholder modules.
6. **Check:** Inspect the smallest relevant diff, source/index links, license, privacy, scope, and compatibility. Run the available project-specific structural checks, then focused behavioral scenarios when authorized. Broaden testing only for demonstrated risk, failure, or affected interfaces.
7. **Record:** Report changed paths, dependency packaging, actual test outcomes, behavior or integration not tested, and material risks. Iterate only on an observed defect or unmet acceptance criterion.

## Token and reasoning economy

- Minimize **input/output tokens, repeated reasoning, tool calls, and unnecessary iterations** by reusing verified context and the companion Skill within the same revision.
- Use one focused search before broad discovery; load optional files only at the step that needs them. Avoid repeated re-summaries, duplicate policy text, speculative scaffolding, and exhaustive reference traversal.
- Prefer explicit contracts, short decision gates, deterministic validators, and representative scenarios over long open-ended deliberation. Batch independent reads when useful; do not skip mandatory reviews or tests solely to save tokens.
- Stop once the authorized outcome and required evidence are complete. Report unknowns plainly rather than exploring unrelated branches.

## Acceptance and output

A consumer can identify the trigger, prerequisites, outputs, dependencies, limits, stop behavior, and verification evidence without relying on chat history. Report each relevant check as **passed**, **failed**, **not run**, or **not applicable**. Passing structural checks is not proof of correct agent behavior; publication never implies downstream installation or authorization.
