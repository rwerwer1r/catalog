# Development and harness

## Source layout

`src/` is editable source; `catalog.json` is the published index. Skill entrypoints are `src/skills/<id>/SKILL.md`. Rules, references, agents, and templates use `src/<folder>/<id>.md`. Modules use `src/modules/<id>.py` or `src/modules/<id>/README.md` with implementation and tests.

Add or change an asset in its owner directory, update the manifest, and update links as appropriate. One-off project notes and generated agent projections do not belong in this repository.

## Verification

```sh
python3 tools/validate_catalog.py
python3 -m unittest discover -s tests -v
```

The validator checks schema version, owner, entrypoints, duplicate identifiers, safe paths, and manifest coverage. Tests use temporary repositories and verify failure cases. [CI](../.github/workflows/validate.yml) runs both checks without network downloads beyond the Python and checkout actions.

## Quality gate

Check that the asset is reusable, has declared inputs or prerequisites, describes output and limitations, and avoids hidden privileges. Run behavioral checks in a representative consumer before claiming an agent Skill or module works in production. Metadata checks alone cannot validate agent behavior.
