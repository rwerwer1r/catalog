---
description: "Repository-wide requirements for maintaining authoritative technical documentation."
---

# Documentation policy

## Canonical ownership

Use one authoritative location for each instruction: `docs/policies/` for obligations, `docs/development/` for implementation guidance, `docs/agents/` for agent workflows and harnessing, `docs/documentation/` for authoring conventions, and `src/` for reusable assets. Link to canonical text instead of copying policies into multiple documents.

## Authoring requirements

- Use English in accordance with [language policy](language.md).
- Follow [frontmatter rules](../documentation/frontmatter.md) for new or substantially revised `docs/` Markdown files.
- Follow [entrypoint rules](../documentation/entrypoints.md) when creating, moving or retiring documents and documentation areas.
- Apply [bundle rules](../documentation/bundles.md) when publishing a multi-document topic.
- Start visible content with a descriptive heading and state scope and prerequisites.
- Document current observed behavior separately from future proposals.
- Record limitations, unsafe assumptions and unverified claims explicitly.

## Maintenance

Treat stale commands, obsolete paths, broken links and ambiguous ownership as defects. Keep names stable where possible, and repair inbound links during moves. Do not claim automated document lint or agent behavior checks that have not run.
