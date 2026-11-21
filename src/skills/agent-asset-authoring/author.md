# Create or revise an agent asset

1. **Resolve local authority.** Identify the authorized repository, branch, instructions, relevant scoped rules, source conventions, and permitted changes. Repository requirements override this generic procedure within higher-priority constraints. If authority conflicts, stop rather than choosing permissive defaults.
2. **Reuse before creating.** Search the nearest existing asset index and related entrypoints. Prefer a compatible revision to a duplicate asset.
3. **Specify the contract.** Define the consumer, activation conditions, exclusions, inputs, expected outputs, tool or data dependencies, side effects, failure paths, and stop criteria.
4. **Package the asset.** Define its file boundaries, stable consumer contract, and necessary supporting files. Delegate README.md, SKILL.md, index formats, and navigation content to [documentation authoring](../documentation-authoring/SKILL.md); do not maintain competing entrypoint rules here.
5. **Author documents.** Load the required [documentation-authoring entrypoint](../documentation-authoring/SKILL.md) at the written-content boundary, then select its entrypoint, index, or other document route. Follow local naming, metadata, language, and navigation rules.
6. **Publish minimally.** Update the repository's existing discovery mechanism, stable references, and only necessary supporting files. Do not silently install assets or create a parallel registry.
7. **Verify and report.** Review the diff, links, packaging, compatibility and permissions; run available local checks and behavior scenarios as authorized. Record actual outcomes and unverified behavior.

Load extra templates, consumer files, tests, or reference material only to answer a concrete open question. Reuse evidence from the same revision; stop once required behavior and verification are supported.
