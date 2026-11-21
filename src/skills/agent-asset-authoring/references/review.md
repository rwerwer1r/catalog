# Review or retire an agent asset

1. Read applicable repository rules, the asset entrypoint, its nearest index, and only the directly affected implementation or dependency. Follow the required documentation-authoring Skill for textual review and edits.
2. For README.md, SKILL.md, or other reader-facing entrypoints, apply [documentation-authoring](../../documentation-authoring/SKILL.md) and its entrypoint procedure. Check whether the intended consumer can reject irrelevant assets before deeper loading.
3. For manual indexes or generated metadata indexes, apply the documentation Skill's index procedure. The asset review retains responsibility for packaging compatibility, consumer dependency changes, and source ownership.
4. Review the contract: input/output, permissions, side effects, compatibility, source ownership, security, and how failure is reported. For deprecation or removal, check consumers when known and document migration.
5. Run focused structural checks and an authorized representative scenario when possible. Report which checks actually ran, failures, remaining risks, and any changes made.

Avoid speculative improvements unrelated to the request. Fix evidenced defects and rerun affected checks rather than repeating the full review without cause.
