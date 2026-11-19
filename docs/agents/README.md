---
description: "Entry point to the agent operating model, context strategy, harness, scenarios, and evidence."
---

# AI agent operations

This directory owns the **agent maintenance harness**, not reusable agent roles themselves. Publish downstream-consumable assets under [src/agents/](../../src/agents/README.md), [src/skills/](../../src/skills/README.md) or [src/rules/](../../src/rules/README.md).

| Task | Guide |
| --- | --- |
| Define an agent's authority and working sequence | [Operating model](operating-model.md) |
| Load only relevant authoritative instructions | [Context selection](context-loading.md) |
| Run the document-first harness | [Harness](harness.md) |
| Define a reproducible behavior check | [Scenarios](scenarios.md) |
| Record checks and evidence | [Verification record](verification.md) |
| Transfer or finish an agent task | [Handoff and completion](handoff.md) |

Start from [repository policies](../policies/README.md); avoid eagerly loading every document or asset.
