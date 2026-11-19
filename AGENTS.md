# Catalog contributor instructions

This is the canonical source for reusable assets owned by `rwerwer1r`.

- Check repository, account and working branch before writes; do not switch accounts.
- Read `docs/development.md` and the relevant `src/<kind>/README.md`.
- Add each publishable asset to `catalog.json` and place its source under `src/`.
- Never store credentials, personal work logs, or implicit cross-repository permissions.
- Make Skills opt-in and describe prerequisites and verification.
- Review licensing and attribution before importing third-party content.
- Run `python3 tools/validate_catalog.py` and `python3 -m unittest discover -s tests -v` when available; report skipped checks accurately.
