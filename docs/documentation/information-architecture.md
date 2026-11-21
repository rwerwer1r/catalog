---
description: "Choose documentation ownership, page boundaries, filenames, and scalable navigation for the catalog."
---

# Information architecture

## One owner per topic

Place a document according to **what it governs**, not who requested it:

| Owner | Content |
| --- | --- |
| `docs/policies/` | Repository-wide requirements and constraints |
| `docs/development/` | Architecture, engineering workflow, checks, and contribution processes |
| `docs/agents/` | Agent operating model, harness and verification evidence |
| `docs/documentation/` | Documentation authoring, navigation, and lifecycle conventions |
| `src/` | Reusable Skills, rules, references, agents, modules and templates for other projects |

A document should have one clear question it answers and one canonical location. When two pages prescribe the same behavior, consolidate their instructions and leave a link rather than maintaining competing versions.

## Choose a document unit

- **Section:** the information is short, has the same owner and audience, and would not be useful independently.
- **Standalone page:** a distinct task or concept deserves a stable entrypoint and can be read independently.
- **Bundle:** several pages share a single reader journey, prerequisites and lifecycle; follow [bundle guidance](bundles.md).
- **Reusable source asset:** another repository will consume the material as a Skill, rule, reference, module or template; publish under `src/` and link it from its category `index.md`.

Avoid directory hierarchies created only for anticipated future content. Split a page when independent maintenance, discoverability or task focus justifies it, not because it reached an arbitrary word count.

## Naming and structure

Use lowercase kebab-case names for topic pages, `README.md` for introductions and the existing manual `index.md` for directory lists. Reusable [entrypoint](../../src/skills/documentation-authoring/entrypoints.md) and [index](../../src/skills/documentation-authoring/indexes.md) guidance owns the authoring contract; metadata-generated listings, when authorized, use `INDEX.tsv` instead of generated Markdown. Use descriptive headings. Prefer stable conceptual names over dates, vague labels (`misc`, `notes`, `new`) or author names. Do not encode a release version into the filename unless multiple versions must be maintained concurrently.

Keep the path from `README.md` to a typical page short: repository index → domain index → topic. Link nearby detail pages from their owner instead of forcing unrelated readers through a large global index. See [local entrypoint paths](entrypoints.md).

## Expansion and change control

Before adding a domain, document its scope and relationship to existing owners. When moving a page, update inbound links and all affected indexes in the same change. Record intentional deprecation rather than silently abandoning a still-referenced page; see [maintenance](maintenance.md).
