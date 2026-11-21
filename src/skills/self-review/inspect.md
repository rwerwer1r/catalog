# Inspect and challenge material risks

Use after [scope.md](scope.md) selects evidence-bearing review checks. Operate only on the authorized artifact and selected relevant lenses.

1. **Inspect actual evidence.** Compare the artifact or diff to applicable instructions, acceptance criteria, source contracts, and tests. Prefer direct inspection, deterministic checks, and reproducible counterexamples over conjecture.
2. **Make a candidate issue testable.** Identify the exact location or decision, the violated requirement or credible failure path, user-visible impact, and the observation needed to confirm or refute it. Distinguish known bug, plausible concern, and unverified hypothesis.
3. **Challenge the candidate criticism.** Try to disprove it: check whether the alleged requirement applies, the behavior is intentional, tests already cover it, a narrower explanation fits, or the issue is immaterial or duplicative. A failure does not prove a proposed diagnosis or fix.
4. **Use genuinely distinct perspectives only.** Assess security, consumer, operator, maintainability or other lenses if they raise different testable risks. Label different questions, not theatrical personas. Do not call one model's sequential passes independent agents.
5. **Stop based on expected value.** When further investigation cannot plausibly change acceptance or risk, stop. Do not keep searching for negatives because an earlier review found none, or demand a compensating criticism for every strength.

Return evidence-backed candidate findings and unresolved material uncertainties to [adjudicate.md](adjudicate.md). Do not silently modify the artifact or enlarge scope during inspection.
