## Scope

Describe the affected catalog assets or documentation contracts, why this change is needed, and any non-goals.

## Policy and documentation review

- [ ] Relevant [repository policy](../docs/policies/repository.md), [asset policy](../docs/policies/assets.md) and [documentation policy](../docs/policies/documentation.md) reviewed as applicable
- [ ] [Language policy](../docs/policies/language.md), canonical source ownership, and nearest `INDEX.md` links checked
- [ ] Permissions, dependencies, consumer compatibility and migration impact assessed

## Validation

Check only commands actually run; provide a CI link or failure details in the PR description.

- [ ] `python3 scripts/validate_catalog.py`
- [ ] `python3 scripts/validate_docs.py`
- [ ] `python3 -m unittest discover -s tests/scripts -v`
- [ ] For agent behavior changes, include an [agent verification record](../docs/agents/verification.md) with scenario outcomes or explicitly mark them `not run`

## Limitations

List failed or unrun checks, unverified behavior, compatibility risks and required follow-up.
