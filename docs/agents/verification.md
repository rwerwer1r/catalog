---
description: "Template for documenting agent behavior checks and their evidence."
---

# Agent verification record

Use this structure in a pull request, issue or review note when an asset changes agent instructions or downstream behavior.

## Context

- Asset ID and path:
- Repository, commit and intended consumer:
- Scenario and expected outcome:
- Explicit permissions and environment:

## Evidence

| Layer | Check performed | Outcome | Evidence |
| --- | --- | --- | --- |
| Documentation | Reviewed policy and task instructions | Not run | |
| Packaging | Manifest validator and unit tests | Not run | |
| Behavior | Representative controlled agent task | Not run | |
| Integration | Authorized consuming repository | Not run | |

Outcome must be **passed**, **failed**, **not run**, or **not applicable**, supported by a concise explanation. Replace placeholders with actual observations; do not claim a check was run from this template alone.

## Limitations and follow-up

List unsupported cases, environmental constraints, unresolved risk and next actions. A passing document check never substitutes for end-to-end verification.
