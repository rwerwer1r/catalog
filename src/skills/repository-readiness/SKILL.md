---
name: repository-readiness
description: Assess repository readiness before implementation by examining relevant tooling, tests, configuration, and CI without making unapproved changes.
---

# Repository readiness

## Relevance gate

**Use for** assessing development prerequisites or repository gaps before implementation. For unrelated work, **stop here**. This small Skill needs no routing index.

## Procedure

1. Confirm target account, repository, branch, task scope, and permission; apply local instructions.
2. Inspect the nearest README and only relevant runtime declarations, tests, CI, and policies. Reuse verified context; expand when a specific gap warrants it.
3. Distinguish missing files from unchecked files, failures from unavailable checks, and readiness from deployment permission.
4. Run available safe checks when authorized. Report observed facts, results, gaps, and the smallest justified next steps; never claim an unrun test passed.
