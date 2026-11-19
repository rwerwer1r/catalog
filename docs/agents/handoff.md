---
description: "Transfer agent-assisted work with scoped evidence, remaining actions, and authorization boundaries."
---

# Agent handoff and completion

## Minimum handoff

A continuation should receive only the information needed to resume correctly:

- Intended repository, account, branch and authorized task
- Current revision or working state and files changed
- Decisions made and canonical documents used
- Tests run with outcomes and evidence locations
- Known risks, blocked steps and unresolved questions
- Explicit next actions and any approval requirements

Do not include secrets, personal records or unverified assumptions disguised as facts.

## Stop conditions

Stop the affected operation when account identity cannot be confirmed, instructions conflict materially, required authority is missing, a potentially destructive effect was not approved, or verification shows a safety-critical failure. Report a precise blocker rather than silently changing scope.

## Completion criteria

A work item is complete when the requested change is present, the diff is scoped, applicable checks have been performed or declared unavailable, and the user has a concise record of the result. A generated plan, successful tool call or green metadata check alone is not sufficient evidence for behavioral claims.

Follow [verification records](verification.md) for scenario outcomes and [context selection](context-loading.md) for authoritative input.
