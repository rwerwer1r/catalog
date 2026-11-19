# Change review

**Use when:** assessing a proposed patch, release, or pull request.

Review the intended behavior first, then inspect the changed code and its callers. Prioritize observable defects over style preferences.

Consider:
- Correctness: expected results, boundary cases, and failure paths.
- Data and security: permissions, secret handling, validation, and irreversible effects.
- Compatibility: interfaces, migrations, configuration defaults, and rollback.
- Tests: coverage of the actual change and evidence of execution.
- Documentation: whether usage instructions still match the implementation.

Report actionable findings with file locations, impact, and a concrete condition under which the issue occurs. Distinguish confirmed bugs from questions and unverified risks. If no issue is found, state the scope and limitations of the review rather than implying certainty.
