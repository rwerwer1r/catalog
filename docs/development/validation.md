---
description: "Explain the catalog's automated checks and additional review requirements for documentation."
---

# Validation and tests

## Baseline checks

Run from the repository root with Python 3.11 or later:

```sh
python3 tools/validate_catalog.py
python3 -m unittest discover -s tests -v
```

The validator checks manifest schema, owner, IDs, paths and coverage. Unit tests exercise accepted and rejected layouts. [GitHub Actions](../../.github/workflows/validate.yml) executes these checks on supported events.

## Document-first checks

For changes in `docs/`, follow the [documentation handbook](../documentation/README.md), apply [documentation review](../documentation/review.md), update relevant indexes, inspect relative links and verify the actual English text against changed behavior. Follow [agent documentation workflow](../documentation/agent-workflow.md) for agent-authored changes.

For `src/skills/` or `src/agents/` changes, also follow [agent harnessing](../agents/harness.md). Keep a record of what was actually observed. A document review is not an end-to-end test.

## Reporting

Distinguish passed, failed, not run and not applicable checks. The current Python validator does not parse all documentation frontmatter or crawl all Markdown links; review those separately. Describe unavailable tooling and unresolved risk rather than converting it into a successful outcome.
