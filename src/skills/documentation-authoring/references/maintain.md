# Maintain or audit documentation

1. Read applicable rules and the **known target directly**, plus evidence relevant to its maintenance. Consult a README or INDEX.md only to locate an unknown target, evaluate discoverability, or repair affected navigation; do not preload unrelated directories.
2. When the target is an entrypoint, use [entrypoint guidance](entrypoints.md) to test reader relevance, exclusions, and the stop-before-load gate.
3. When the target is a manual or metadata-based index, use [index guidance](indexes.md) for the format, consumer discovery, and source-of-truth contract.
4. Check accuracy, task completeness, headings, metadata, relative links, examples, accessibility, and safe handling of secrets or permissions.
5. For moves and deprecations, preserve stable links where possible, update affected inbound navigation, and state replacements or compatibility impact.
6. Run focused, authorized validators and inspect what they cannot prove. Record passed, failed, not run, or not applicable results with evidence.

Fix the smallest evidenced defect. Do not expand reviews or repeat unchanged checks without a concrete cause.
