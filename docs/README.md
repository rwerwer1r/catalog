# Documentation

The documentation system describes **how the catalog is maintained and consumed**. Reusable content belongs in [src/](../src/README.md), not in this directory.

| Area | Responsibility |
| --- | --- |
| [Development](development/README.md) | Architecture, contribution workflow, tests and release readiness |
| [Policies](policies/README.md) | Cross-cutting repository requirements including language |
| [AI agents](agents/README.md) | Agent instructions, document-first harnessing and verification |

## Ownership and precedence

Policy documents state repository requirements. Development documents explain implementation. Agent documents describe how agents apply and verify those requirements. Individual `src/` assets define their own task behavior but do not override repository policies when maintained here.

Keep documentation discoverable through the area indexes; avoid duplicating rules across files. When behavior or an asset entrypoint changes, update its owning document and inbound links.
