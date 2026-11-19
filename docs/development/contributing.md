# Contributing assets

1. Identify the reusable problem and intended consumers. Check `catalog.json` for an existing entry before adding another.
2. Read [repository policies](../policies/README.md), especially the [language policy](../policies/language.md).
3. Select the correct `src/` kind and write the canonical source. Describe triggers, prerequisites, outputs, dependencies, failure conditions and limits as appropriate.
4. Add or update the unique entry in `catalog.json` and repair local links.
5. Run the [validation checks](validation.md). If an asset changes agent behavior, prepare the [agent verification record](../agents/verification.md).
6. Review the diff for secrets, stale references, unapproved external material, accidental assumptions and changes outside the intended scope.

## Review and adoption

A passing metadata check means the asset is well-formed, **not** that it works in a consuming environment. Require representative downstream evidence before calling a Skill, rule or module operationally verified.

Keep user-specific records and generated vendor files out of `src/`. Publish only reusable material.
