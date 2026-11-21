# Review or retire an agent asset

1. Read applicable repository rules, the asset entrypoint, its nearest index, and only the directly affected implementation or dependency. Follow the required documentation-authoring Skill for textual review and edits.
2. Check the trigger and exclusion gate: an unrelated request must not load the asset's workflows or optional references. Confirm that the entrypoint contains only essential authority, prerequisites, dependency and routing guidance.
3. Inspect routing-only indexes for distinct, descriptive choices; verify each route target exists, is relevant, and does not force loading unrelated files. Confirm that unsupported or ambiguous tasks stop before deeper context expansion.
4. Review the contract: input/output, permissions, side effects, compatibility, source ownership, security, and how failure is reported. For deprecation or removal, check consumers when known and document migration.
5. Run focused structural checks and an authorized representative scenario when possible. Report which checks actually ran, failures, remaining risks, and any changes made.

Avoid speculative improvements unrelated to the request. Fix evidenced defects and rerun affected checks rather than repeating the full review without cause.
