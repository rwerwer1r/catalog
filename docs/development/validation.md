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

The source validator checks canonical asset paths, naming, entrypoint headings, category index link coverage, required Skill frontmatter fields, and local Markdown links within Skill directories. For Skills with `INDEX.md`, it requires a real Markdown link from the entrypoint and at least one existing **local** procedure route. Plain link-like text, remote-only routes, and paths outside the Skill's `references/` do not satisfy routing. Extra Markdown procedures at the Skill root are rejected. Its metadata check covers the catalog's simple scalar frontmatter convention, not every valid YAML construction. The documentation validator checks supported frontmatter syntax, single H1, local Markdown file targets and nearest index coverage. Unit tests exercise validation edge cases and guard lightweight Skill entrypoints, routing indexes, and one-procedure loading paths with **character-count proxies**. These are maintainability bounds, not measured model token use, latency, or behavioral compliance. [CI](../../.github/workflows/validate.yml) runs the same commands.

## Manual and behavioral review

The documentation validator does not check external URLs, heading anchors, full Markdown/YAML parsing or the truth of claims. Review [documentation quality](../documentation/review.md) and run representative [agent scenarios](../agents/scenarios.md) when instructions change behavior.

No metadata-driven `INDEX.tsv` generator or generated index is introduced by the current work; future generators must validate source-backed descriptions, destinations and reproducible output under the [documentation Skill index contract](../../src/skills/documentation-authoring/references/indexes.md). Scenario execution is **not automated in the current CI**. Integration tests are consumer-specific and require explicit access. Record actual results using [verification evidence](../agents/verification.md) and avoid implying that missing checks passed.

## Decision rules

- Documentation-only change: check canonical ownership, frontmatter, internal links and language.
- Asset source or directory-index change: run packaging validation and unit tests.
- Behavior-affecting asset change: review scenario coverage and execute applicable controlled cases or state what is unverified.
- Breaking interface, installation or permission change: assess consumers, approval and rollback.

Report passed, failed, not run and not applicable separately; a green CI job proves only its configured steps.
