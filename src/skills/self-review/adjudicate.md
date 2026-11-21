# Adjudicate review findings

1. **Evidence gate.** For each candidate, verify an applicable requirement or credible failure mechanism, exact evidence or reproducer, realistic impact, and whether the suggested correction actually addresses it. Mark as **confirmed**, **rejected**, or **unresolved**; delete duplicate or immaterial criticism rather than padding the report.
2. **Calibrate severity.** Reserve severity labels for credible impact and likelihood, not rhetorical urgency. Do not promote a hypothetical low-probability edge case to a blocker without evidence or a relevant risk policy.
3. **Protect valid results.** If checks pass and no actionable defect is supported, report **no actionable findings in the reviewed scope** and preserve the accepted result. Never invent a defect or forced improvement to satisfy an assumed review quota.
4. **Handle unknowns correctly.** Unrun tests and inaccessible surfaces are **not verified**, not failed and not passed. Preserve unresolved material risk, missing authority, or unsafe assumptions as limits; do not call the whole artifact sound on partial inspection.
5. **Recommend only justified changes.** For confirmed actionable findings, propose the smallest valid correction and a focused verification method. Review alone does not authorize changing the artifact. If all proposals are rejected, advise **no change**.
6. **Report a bounded verdict.** Summarize scope, validated strengths where relevant, confirmed findings and evidence, meaningful unresolved questions, checks performed, and limits. Stop when another pass has no credible expected value.

Never fabricate criticisms, praise, measurements, source independence, review sign-off, or test outcomes. A review with **zero confirmed issues** is complete when the authorized scope and necessary evidence checks are satisfied.
