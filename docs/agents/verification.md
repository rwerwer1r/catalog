---
description: "Capture reproducible evidence for agent, documentation, packaging, and integration checks."
---

# Agent verification record

Use this structure in a pull request or review note when an agent asset's behavior changes. Keep evidence reproducible and redact secrets.

## Context

- Asset ID and canonical path:
- Catalog revision and intended consumer:
- Scenario, environment and expected result:
- Explicit authorization and restricted side effects:

## Check matrix

| Layer | Performed check | Result | Evidence |
| --- | --- | --- | --- |
| Documentation | Policy, source and link review | Not run | |
| Packaging | Asset and documentation validators, tests | Not run | |
| Behavior | [Representative scenario](scenarios.md) | Not run | |
| Integration | Authorized consumer check | Not run | |

Use exactly **passed**, **failed**, **not run**, or **not applicable** as outcomes. A missing result is not a pass. Name the tool/command, revision and meaningful evidence for each performed check.

## Failure and follow-up

Record defects, risk, unavailable tooling, missing permissions and the next smallest action. Link to the [handoff guide](handoff.md) for continuation. A passing packaging run never guarantees behavior or production readiness.
