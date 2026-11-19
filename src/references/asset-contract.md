# Asset publishing contract

`catalog.json` is a UTF-8 JSON object with `schema_version: 2`, `owner: "rwerwer1r"`, `source_root: "src"` and an `assets` array.

Each asset has a unique lowercase kebab-case `id`, `kind`, repository-relative `path` and nonempty `description`.

Supported kinds: `skill`, `rule`, `reference`, `agent`, `module`, `template`. Skill entrypoints use `src/skills/<id>/SKILL.md`; standard Markdown entrypoints use `src/<plural-kind>/<id>.md`. Modules may use a Python file or package README.

Asset paths must not escape the repository. Published source files must be registered exactly once. Consumers explicitly select and review assets; the catalog is not an installer or account authorization mechanism.
