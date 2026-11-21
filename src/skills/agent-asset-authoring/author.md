# Create or revise an agent asset

Use only after the [Skill gate](SKILL.md) accepts the task and [route index](index.md) selects authoring. Apply the required documentation-authoring Skill to written entrypoints and supporting documents.

1. **Resolve local authority.** Identify the authorized repository, branch, instructions, relevant scoped rules, source conventions, and permitted changes. Repository requirements override this generic procedure within higher-priority constraints. If authority conflicts, stop rather than choosing permissive defaults.
2. **Reuse before creating.** Search the nearest existing asset index and related entrypoints. Prefer a compatible revision to a duplicate asset.
3. **Specify the contract.** Define the consumer, activation conditions, exclusions, inputs, expected outputs, tool or data dependencies, side effects, failure paths, and stop criteria.
4. **Package for progressive use.** Make the entrypoint a lightweight relevance gate with purpose, scope, essential constraints, and an explicit route to a local index **when the asset needs multiple workflows**. Keep the index routing-only; put full task procedures in separately named, on-demand files. Do not force a split for a trivial asset or when local repository rules prescribe another structure.
5. **Author documents.** Use the [documentation-authoring entrypoint](../documentation-authoring/SKILL.md) and its task-selected route. Respect local filenames, metadata, language, and navigation. Do not duplicate canonical policy content or preload optional references.
6. **Publish minimally.** Update the repository's existing discovery mechanism, stable references, and only necessary supporting files. Do not silently install assets or create a parallel registry.
7. **Verify and report.** Review the diff, links, packaging, compatibility and permissions; run available local checks and behavior scenarios as authorized. Record actual outcomes and unverified behavior.

Load extra templates, consumer files, tests, or reference material only to answer a concrete open question. Reuse evidence from the same revision; stop once required behavior and verification are supported.
