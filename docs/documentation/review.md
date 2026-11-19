---
description: "Review documentation for factual correctness, discoverability, safety, and maintainability."
---

# Documentation review

## Review order

1. **Scope and ownership:** the page belongs to the correct directory and does not duplicate another canonical rule.
2. **Accuracy:** commands, file paths, defaults, examples and claims match current source or are labeled as proposals.
3. **Reader completion:** prerequisites, actions, expected results, limitations and troubleshooting are clear where relevant.
4. **Navigation:** nearest entrypoints, relative links, headings and bundle membership are coherent.
5. **Metadata and language:** follow [frontmatter](frontmatter.md) and the [English policy](../policies/language.md).
6. **Safety:** no secrets or personal data; external writes and destructive effects are disclosed.
7. **Diff scope:** no unrelated edits, conflicting versions or stale references.

## Mechanical verification

```sh
python3 scripts/validate_catalog.py
python3 scripts/validate_docs.py
python3 -m unittest discover -s tests/scripts -v
```

The document validator checks frontmatter structure, a single H1, local Markdown file targets and directory-index coverage. It does not check external links, anchors, technical accuracy, full Markdown rendering or downstream behavior. Review those separately.

## Review output

Record changed files, actual checks and results, confirmed defects, and unresolved risks. A passing CI job proves only the checks actually executed.
