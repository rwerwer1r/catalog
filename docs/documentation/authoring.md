---
description: "Write concise, accurate, task-oriented Markdown and verifiable technical examples."
---

# Writing and examples

## Start from reader intent

Identify the audience, prerequisite knowledge, action or question, and observable result. Choose the page form that fits the reader:

- **Concept:** explain what something is, why it exists, boundaries, and links to procedures.
- **How-to:** state prerequisites, numbered actions, expected output, failure handling and verification.
- **Reference:** provide precise interfaces, allowed values, defaults, constraints and exceptions.
- **Decision record:** preserve context, alternatives, rationale and consequences without presenting an opinion as universal policy.

Avoid mixing a tutorial, API reference and roadmap into one page unless the separation would make the task harder.

## Structure

Use [frontmatter](frontmatter.md), one descriptive H1 and task-oriented H2 sections. Start with a short statement of purpose; put essential prerequisites before commands. Use lists for steps, tables only for genuinely comparable attributes, and code blocks with language identifiers. Keep paragraphs focused. Prefer direct English and defined technical terms; follow the [language policy](../policies/language.md).

For procedures, show what success looks like and how to recover from common failures. For references, distinguish required fields, optional fields and implementation-dependent behavior. Use explicit version or environment qualifiers when needed.

## Evidence and examples

- Verify repository paths, command names, configuration keys and API shapes against the actual source before describing them as current.
- Never invent successful test outcomes, supported integrations, performance numbers or security guarantees.
- Prefer minimal realistic examples without credentials or private identifiers. Label pseudocode, illustrative output and untested commands.
- Explain destructive effects, required permissions and external downloads **before** the relevant step.
- Separate observed behavior from recommendations and planned work. Link to the authoritative code or document when appropriate.

## Markdown conventions

Use repository-relative links for local files and descriptive link text. Avoid raw absolute links to the current branch when a relative link survives moves more reliably. Prefer fenced code blocks with a language (such as `sh`, `json`, or `python`). Ensure headings form a logical outline and link labels describe destinations. Provide meaningful alternative text when adding informative images.

## Final read-through

Ask whether a reader can follow this page without access to conversation history, whether every required input is named, and whether every claimed result is observable. Remove redundant explanation and stale placeholders before publication.
