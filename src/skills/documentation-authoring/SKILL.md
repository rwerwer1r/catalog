# Documentation authoring

## Use when

Create, revise, restructure, or review documentation in any authorized repository or workspace: READMEs, indexes, guides, references, procedures, decisions, and written instructions in agent assets. This Skill provides a workflow, **not** authority to change code, policy, accounts, permissions, or external systems.

## Rule precedence

1. Respect higher-priority instructions, explicit authorization, and safety constraints.
2. Within that boundary, **the target repository's applicable rules are authoritative over this Skill**: repository instructions, scoped directory guidance, documentation policies, schemas, language, and established conventions. A narrower rule refines a broader one only when permitted; it cannot silently negate an applicable repository-wide constraint.
3. Use this Skill's defaults **only** where local guidance is absent. Never impose this Skill's paths, frontmatter, README/index split, tooling, or language over a repository's rules.
4. If applicable rules conflict or permission is unclear, identify the conflict and request resolution for consequential changes; do not choose the easiest rule or invent authority.

## Inputs

Target and authorized scope; document or reader goal; available evidence; relevant repository revision and tooling. Do not assume a specific host, project structure, language, or validation command.

## Progressive context disclosure

Load the **smallest authoritative context sufficient for the next decision**. Reuse already verified context from the same repository/revision; reload only when the task, scope, or underlying file changes.

1. **Route:** Inspect the target's instruction entrypoint (such as `AGENTS.md`) and the nearest applicable scoped instructions. Locate the documentation owner using an existing index, README, or a targeted path search. Do not recursively read the repository.
2. **Focus:** Read the document being changed, relevant local writing conventions, and only the source-of-truth files that support its claims. Prefer specific sections or bounded excerpts to full files when sufficient.
3. **Expand on demand:** Follow a reference, inspect neighboring pages, load a template, or inspect code **only to resolve a concrete uncertainty or requirement**. Stop expanding once the draft and review criteria are supported. Do not traverse every linked document.

Keep a small working context: task, governing rules, canonical paths, confirmed facts, open questions, and verification status. Reference canonical pages instead of copying large passages. Do not repeatedly fetch unchanged files or re-derive settled decisions.

## Document-first workflow

1. **Resolve:** Confirm the destination, reader, outcome, authority, and applicable rules.
2. **Plan only the needed shape:** Search for an existing canonical page before creating one. Choose a section, page, or bundle according to local conventions and genuine reader needs; avoid duplicate sources of truth.
3. **Draft from evidence:** Match the repository's terminology, metadata, navigation, and style. For procedures state prerequisites, actions, expected results, and recovery. For references specify interfaces, defaults, and limits. Mark illustrative or untested examples.
4. **Maintain navigation:** Update only affected indexes and inbound links. Preserve stable paths where possible. Do not create a new index, registry, bundle, or frontmatter schema unless local rules or reader needs justify one.
5. **Verify in layers:** Review claims, links, headings, privacy, and diff scope; run **documented, available** targeted validators and tests when authorized. Escalate to broader checks when risk, changed scope, or failures require them.
6. **Report:** Summarize changed paths, decisions, actual checks, remaining uncertainty, and effects. Do not claim that a check passed unless it ran.

## Context and execution economy

- Optimize **token use, reasoning effort, latency, and tool calls** without sacrificing correctness. Prefer one targeted lookup over broad browsing, reuse evidence rather than re-reading, and batch independent reads when useful.
- Use concise drafts and references instead of repeated prose; do not produce speculative variants or lengthy plans for straightforward edits.
- Prefer deterministic linters, link checks, and focused tests to repeated subjective review loops. When a check fails, fix the evidenced cause and rerun the affected check; avoid arbitrary iteration.
- Stop when the requested document and its necessary navigation are complete and relevant checks are recorded. Expand the search or review only for a concrete defect or unresolved material risk.

## Fallback defaults and output

When local rules provide no answer, use a clear title, focused Markdown sections, source-backed examples, and relative local links; keep introductions short and avoid unnecessary metadata. Use the target's language preference.

Report checks as **passed**, **failed**, **not run**, or **not applicable**, with evidence. Structural validity does not establish factual truth or behavior.
