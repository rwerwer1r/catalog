---
name: repository-readiness
description: Assesses a repository's development readiness by examining project structure, tooling, checks, and CI. Use before implementation when repository prerequisites or missing capabilities need review.
---

# Repository readiness

## Use when

A repository needs a development-readiness assessment before implementation.

## Inputs

Repository and branch, intended stack if known, authorization to inspect or run checks.

## Steps

1. Verify account, repository, branch, and current working state. Inspect before making changes.
2. Find the README, runtime declarations, tests, formatters, CI and branch policies.
3. Note missing files separately from files not yet inspected.
4. Execute safe checks only when dependencies and permission are available.
5. Record the evidence, failures, unverified items, and smallest next steps.

## Output

A readiness report with observed facts, commands executed, results, gaps and recommended follow-up. Do not claim a test passed unless it ran successfully.
