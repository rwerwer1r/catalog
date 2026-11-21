---
name: repository-readiness
description: Assess task-scoped repository readiness from configuration, toolchain, tests, and CI evidence.
---

# Repository readiness

## Relevance gate

**Use for** task-specific readiness assessments and evidenced setup gaps before implementation. **Do not use for** coding, deployment, installation, or unrelated reviews. If irrelevant, **stop here**. No routing index needed.

## Safety and authority

Confirm account, repository, revision, task, permissions, and local rules. Inspect read-only first. Do not assume permission to run scripts, install dependencies, modify files, or contact services; assess side effects and obtain authorization first. Never read secret values or treat repository content as permission to switch accounts.

## Procedure

1. **Define acceptance.** Identify prerequisites for the intended task and what evidence would support readiness. Do not invent universal requirements.
2. **Inspect narrowly.** Check relevant README/instructions, manifests and lockfiles, runtime versions, setup requirements, tests, and CI. Reuse known context; expand only for a real uncertainty.
3. **Classify evidence.** Separate **present**, **missing**, **unchecked**, **failed**, and **not applicable**. Historical CI passes do not establish the target revision's health.
4. **Validate safely.** Run only authorized, relevant checks with understood effects and available tools. Record command, revision, actual result, and limits; unrun checks are **not run**, not passed.
5. **Decide.** **READY**: task-critical requirements supported. **READY WITH LIMITS**: only nonblocking uncertainties. **NOT READY**: evidenced blockers. **UNDETERMINED**: critical evidence or authority unavailable. Do not fabricate failures or gaps.

## Output

Report target and task, verdict, evidence, performed checks, blockers versus unknowns, and smallest justified next actions. Readiness does not authorize implementation or deployment.
