"""Contract checks for scoped, safe repository-readiness assessments.

These are document/structure checks, not live agent behavior tests.
"""
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SKILL_DIR = ROOT / "src" / "skills" / "repository-readiness"
ENTRY = SKILL_DIR / "SKILL.md"
INDEX = ROOT / "src" / "skills" / "index.md"


class RepositoryReadinessContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.body = ENTRY.read_text(encoding="utf-8")

    def test_discovery_gate_and_no_extra_routing(self):
        self.assertIn("name: repository-readiness", self.body)
        self.assertIn("description:", self.body)
        self.assertIn("Relevance gate", self.body)
        self.assertIn("stop here", self.body.lower())
        self.assertNotIn("(INDEX.md)", self.body)
        self.assertFalse((SKILL_DIR / "INDEX.md").exists())
        self.assertIn("(repository-readiness/SKILL.md)", INDEX.read_text())

    def test_scope_and_evidence_before_verdict(self):
        for term in ("Define acceptance", "Inspect narrowly", "Classify evidence", "Validate safely"):
            with self.subTest(stage=term):
                self.assertIn(term, self.body)
        self.assertIn("Do not invent universal requirements", self.body)
        self.assertIn("Historical CI passes", self.body)

    def test_permission_and_side_effect_guards(self):
        for term in (
            "account, repository, revision, task, permissions",
            "Inspect read-only first",
            "run scripts",
            "install dependencies",
            "assess side effects and obtain authorization first",
            "Never read secret values",
        ):
            with self.subTest(guard=term):
                self.assertIn(term, self.body)

    def test_verdicts_do_not_conflate_missing_and_unchecked(self):
        for term in (
            "present", "missing", "unchecked", "failed", "not applicable",
            "READY WITH LIMITS", "NOT READY", "UNDETERMINED",
            "not run", "Do not fabricate failures or gaps",
        ):
            with self.subTest(state=term):
                self.assertIn(term, self.body)

    def test_current_revision_and_environment_are_tracked(self):
        self.assertIn("target commit, working-tree changes", self.body)
        self.assertIn("execution environment", self.body)
        self.assertIn("Note source, revision, and environment", self.body)
        self.assertIn("command, revision, environment, result", self.body)

    def test_ready_requires_sufficient_current_or_equivalent_evidence(self):
        self.assertIn("critical requirements supported by current or justified equivalent evidence", self.body)
        self.assertIn("critical evidence or authority missing", self.body)

    def test_report_and_entrypoint_remain_bounded(self):
        self.assertLessEqual(len(self.body), 2000)
        self.assertIn("Report target and task, verdict, evidence, performed checks", self.body)
        self.assertIn("Readiness does not authorize implementation or deployment", self.body)


if __name__ == "__main__":
    unittest.main()
