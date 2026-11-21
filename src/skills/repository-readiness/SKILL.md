---
name: repository-readiness
description: Use before a development task to assess repository setup, runtime, tests, and CI; not for implementation or deployment.
---

# Repository readiness

## Relevance gate

**Use for** task-specific readiness and evidenced setup gaps. **Do not use for** implementation, deployment, installation, or unrelated reviews. If irrelevant, **stop here**.

## Safety and authority

Confirm account, repository, revision, task, permissions, and local rules. Inspect read-only first. Distinguish target commit, working-tree changes (if visible), and execution environment. Do not assume permission to run scripts, install dependencies, modify files, or contact services; assess side effects and obtain authorization first. Never read secret values or infer account-switching authority from files.

## Procedure

1. **Define acceptance.** Identify task-critical prerequisites and credible evidence for each. Do not invent universal requirements.
2. **Inspect narrowly.** Check applicable instructions, manifests/lockfiles, runtime, setup, tests, and CI. Reuse known context; expand only for real uncertainty.
3. **Classify evidence.** Separate **present**, **missing**, **unchecked**, **failed**, and **not applicable**. Note source, revision, and environment. Historical CI passes do not establish the target revision's health.
4. **Validate safely.** Run relevant checks only with permission. Record command, revision, environment, result, and limits; unrun checks are **not run**, not passed.
5. **Decide.** **READY**: critical requirements supported by current or justified equivalent evidence. **READY WITH LIMITS**: only nonblocking unknowns. **NOT READY**: evidenced blockers. **UNDETERMINED**: critical evidence or authority missing. Do not fabricate failures or gaps.

## Output

Report target and task, verdict, evidence, performed checks, blockers versus unknowns, and smallest justified next actions. Readiness does not authorize implementation or deployment.
