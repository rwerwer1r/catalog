# Language policy

## Default language

**English is the canonical language for this repository.** Write all new and substantially revised documentation, agent instructions, Skills, rules, references, templates, source-code comments, test descriptions, commit messages and pull-request descriptions in English.

This policy applies to `README.md`, `AGENTS.md`, `docs/`, `src/`, `tools/`, `tests/` and repository metadata written by maintainers.

## Technical exceptions

Preserve exact identifiers, file paths, command names, API fields, external titles, quoted source text and required localized literals when changing them would alter meaning or behavior. A translation example or internationalization fixture may contain other languages when explicitly labeled and justified.

If existing content requires translation, make its English canonical version the maintained source. Do not create parallel translations as alternative authorities by default.

## User-facing communication

This policy controls committed repository content; it does not mandate the language of a maintainer's conversation with a user or a consumer application's interface. Follow the target application's language requirements when generating downstream content.

## Review

Reviewers and agents should flag unintentional non-English prose in changed files, check terminology for consistency, and verify that translation does not change technical behavior.
