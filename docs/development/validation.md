---
description: "Explain catalog checks, evidence requirements, and limits of automated verification."
---

# Validation and tests

## Available checks

From the repository root with Python 3.11+:

```sh
python3 scripts/validate_catalog.py
python3 scripts/validate_docs.py
python3 -m unittest discover -s tests/scripts -v
```

The PR template's validation commands must match the executable CI checks; a unit test guards against drift in the current one-line workflow format. The source validator checks canonical asset paths, naming, entrypoint headings and category index link coverage. The documentation validator checks supported frontmatter syntax, single H1, local Markdown file targets and nearest index coverage. Unit tests exercise validation edge cases. [CI](../../.github/workflows/validate.yml) runs the same commands.

## Manual and behavioral review

The documentation validator does not check external URLs, heading anchors, full Markdown/YAML parsing or the truth of claims. Review [documentation quality](../documentation/review.md) and run representative [agent scenarios](../agents/scenarios.md) when instructions change behavior.

Scenario execution is **not automated in the current CI**. Integration tests are consumer-specific and require explicit access. Record actual results using [verification evidence](../agents/verification.md) and avoid implying that missing checks passed.

## Decision rules

- Documentation-only change: check canonical ownership, frontmatter, internal links and language.
- Asset source or directory-index change: run packaging validation and unit tests.
- Behavior-affecting asset change: review scenario coverage and execute applicable controlled cases or state what is unverified.
- Breaking interface, installation or permission change: assess consumers, approval and rollback.

Report passed, failed, not run and not applicable separately; a green CI job proves only its configured steps.
