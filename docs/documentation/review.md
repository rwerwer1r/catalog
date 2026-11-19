---
description: "Review documentation for factual correctness, discoverability, safety, and maintainability."
---

# Documentation review

## Review order

1. **Scope and ownership:** the page belongs to the correct directory and does not duplicate another canonical rule.
2. **Accuracy:** commands, file paths, defaults, examples and claims match the current repository or are clearly labeled as proposals.
3. **Reader completion:** the document explains prerequisites, actions, expected results, limitations and troubleshooting where relevant.
4. **Navigation:** the nearest [entrypoint](entrypoints.md) links to it; relative links, headings and bundle membership are sound.
5. **Metadata and language:** [frontmatter](frontmatter.md) applies when required; maintained prose follows the [English policy](../policies/language.md).
6. **Safety:** examples contain no secrets or unapproved personal data; external writes, permissions and destructive actions are not hidden.
7. **Change scope:** the diff does not introduce unrelated edits, conflicting versions or obsolete references.

## Verification evidence

Inspect changed Markdown as rendered where possible. Follow local links from the root or nearest entrypoint, and inspect both target files and anchors for renamed headings. Execute documented non-destructive commands only when dependencies are present and authorization permits. If a command cannot be run, report it as **not run**, not passed.

Use the existing catalog checks:

```sh
python3 tools/validate_catalog.py
python3 -m unittest discover -s tests -v
```

These commands check asset metadata and tests, **not** documentation link integrity or YAML frontmatter. Manual documentation review remains necessary until a dedicated validator is introduced.

## Review output

Record the changed pages, review scope, actual checks and results, confirmed defects, and outstanding uncertainties. Do not treat a document-only PR or a passing CI job as proof that an agent or downstream workflow behaves correctly.
