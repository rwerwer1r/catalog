# Scope the self-review

Use after the [Skill gate](SKILL.md) and [route index](INDEX.md) select scoping.

1. **Fix the review target.** Identify the exact artifact, version or diff, expected behavior, actual change scope, relevant rules, authorized checks, and acceptance criteria. Do not critique imagined code or unseen documents.
2. **Capture a neutral baseline.** Record what already works, checks already passed, limitations, and the material acceptance conditions. Treat the prior author's intent and reviewer's suspicion as hypotheses, not evidence.
3. **Select lenses by plausible failure.** Candidates include correctness, security, usability, accessibility, performance, maintainability, operations, compatibility, cost, and documentation. For each chosen lens, name the distinct acceptance condition or material risk it could affect.
4. **Apply a necessity gate.** Drop a lens if it duplicates an existing check, has no relevant surface, cannot affect the result, or only produces superficial opinions. Do not force a predetermined number of reviewers, concerns, categories, or findings.
5. **Route.** If targeted checks are still useful, open [inspect.md](inspect.md). If reliable evidence already establishes that no further check is material, proceed to [adjudicate.md](adjudicate.md) and report the inspection limits.

When a review target or authority is missing, state the blocker or request the smallest missing artifact. Review does not authorize changes to the target.
