---
name: documentation-authoring
description: Writes, revises, reviews, and organizes technical documentation, READMEs, indexes, procedures, and agent asset instructions. Use for documentation tasks and the documentation portion of agent asset authoring.
---

# Documentation authoring

## Relevance gate

**Use only for** writing, revising, reviewing, or organizing documents, including README files, indexes, guides, technical references, and documentation within agent assets.

**Do not use for** implementing software behavior, packaging agent assets outside their documentation, changing permissions, or deployment. When invoked as the required dependency of agent asset authoring, handle **only the documentation subtask**; the parent Skill retains control of asset contracts and packaging. **If neither a documentation task nor a documentation subtask applies, stop here**; do not open this Skill's index or procedures.

## Essential contract

Higher-priority instructions and explicit authority always apply. The **target repository's applicable policies and scoped rules take precedence over this Skill's defaults**, including language, format, frontmatter, entrypoints, routing filename, and validation. Resolve material conflicts instead of choosing permissive defaults.

Keep a small working context: governing rules, relevant canonical page, confirmed evidence, and open questions. Read the nearest instructions and targeted files only after the relevance gate; do not recursively preload documentation. Reuse unchanged evidence for the same revision.

## Route only after acceptance

Read [index.md](INDEX.md) and load one task-specific procedure. Expand only when a concrete uncertainty or failure justifies it. For optional details, follow the target repository's routing conventions (`INDEX.md`, `index.md`, or another required name), not this Skill's preferences.

**Output:** changed paths and links, source-backed claims, actual checks, and unresolved limitations. A successful structural check is not proof of factual correctness.
