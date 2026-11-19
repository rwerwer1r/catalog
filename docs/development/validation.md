---
description: "Explain the catalog's automated checks and review requirements for documentation and assets."
---

# Validation and tests

## Baseline checks

Run from the repository root with Python 3.11 or later:

```sh
python3 tools/validate_catalog.py
python3 tools/validate_docs.py
python3 -m unittest discover -s tests -v
```

The asset validator checks the catalog manifest, safe paths and registered source files. The documentation validator checks YAML frontmatter shape, H1 headings, local Markdown file links, directory entrypoints and that documents are listed in their nearest directory index. Both validators use the Python standard library; [CI](../../.github/workflows/validate.yml) repeats them.

## Review beyond automation

The Markdown checker intentionally does not verify external URLs, resolve heading anchors, fully parse arbitrary Markdown/YAML, assess semantics, run example commands, or establish agent behavior. Follow the [documentation review](../documentation/review.md) and [document-first harness](../agents/harness.md) for those checks. Treat unsupported situations as unverified.

## Reporting

Distinguish passed, failed, not run and not applicable checks. Include evidence of behavioral or integration checks when the change affects agent assets.
