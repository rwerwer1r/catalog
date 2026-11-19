---
description: "Top-level navigation and ownership for catalog maintenance documentation."
---

# Documentation

Documentation governs **how this reusable catalog is maintained**, while distributable source belongs under [src/](../src/README.md).

| Area | Responsibility |
| --- | --- |
| [Development](development/README.md) | Architecture, asset lifecycle, contributions and consumer compatibility |
| [Policies](policies/README.md) | Language, documentation, permission/security and provenance requirements |
| [AI agents](agents/README.md) | Agent context selection, document-first harness, behavior evaluation and handoff |
| [Documentation authoring](documentation/README.md) | Page quality, frontmatter, entrypoints, bundles and maintenance |

## Precedence and ownership

Repository policies govern contributions. Development documents describe procedures; agent documents describe controlled execution and evidence; authoring guides govern document structure. `src/` assets describe optional reusable behavior but cannot override authorization or repository policy.

Keep one canonical owner per topic, link rather than duplicate long instructions, and repair inbound links when documents move. Follow [document review](documentation/review.md) and report unverified behavior honestly.
