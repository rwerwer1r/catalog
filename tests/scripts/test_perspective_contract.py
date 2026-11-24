"""Structural contracts for evidence-led debate and review without forced findings.

These tests verify documented gates, not simulated agent reasoning quality.
"""
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SKILLS = ROOT / "src" / "skills"


class PerspectiveContracts(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.debate = {
            p.name: p.read_text(encoding="utf-8")
            for p in (SKILLS / "self-debate").rglob("*.md")
        }
        cls.review = {
            p.name: p.read_text(encoding="utf-8")
            for p in (SKILLS / "self-review").rglob("*.md")
        }

    def test_discovery_metadata_and_lightweight_gates(self):
        for name, pages in (("self-debate", self.debate), ("self-review", self.review)):
            with self.subTest(skill=name):
                entry = pages["SKILL.md"]
                self.assertIn(f"name: {name}", entry)
                self.assertIn("description:", entry)
                self.assertIn("Relevance gate", entry)
                self.assertIn("(references/INDEX.md)", entry)
                self.assertIn("stop here", entry.lower())

    def test_routes_are_selective_and_targets_exist(self):
        expected = (
            (self.debate, ("frame.md", "examine.md", "resolve.md")),
            (self.review, ("scope.md", "inspect.md", "adjudicate.md")),
        )
        for pages, targets in expected:
            routes = pages["INDEX.md"]
            self.assertIn("only", routes.lower())
            for path in targets:
                with self.subTest(path=path):
                    self.assertIn(f"({path})", routes)
                    self.assertIn(path, pages)

    def test_debate_prohibits_manufactured_disagreement(self):
        entry = self.debate["SKILL.md"]
        frame = self.debate["frame.md"]
        examine = self.debate["examine.md"]
        resolve = self.debate["resolve.md"]
        self.assertIn("no credible opposition", entry)
        self.assertIn("disagreement gate", frame)
        self.assertIn("Prune", frame)
        self.assertIn("forcing equal plausibility", examine)
        self.assertIn("no substantive disagreement identified", resolve)
        self.assertIn("zero new objections", resolve)
        self.assertIn("Do not force a contest", resolve)

    def test_review_prohibits_manufactured_findings(self):
        entry = self.review["SKILL.md"]
        scope = self.review["scope.md"]
        inspect = self.review["inspect.md"]
        adjudicate = self.review["adjudicate.md"]
        self.assertIn("Passing without actionable findings is legitimate", entry)
        self.assertIn("necessity gate", scope)
        self.assertIn("Challenge the candidate criticism", inspect)
        self.assertIn("no actionable findings in the reviewed scope", adjudicate)
        self.assertIn("no change", adjudicate)
        self.assertIn("zero confirmed issues", adjudicate)

    def test_criticism_has_evidence_and_uncertainty_gate(self):
        debate = self.debate["examine.md"] + self.debate["resolve.md"]
        review = self.review["inspect.md"] + self.review["adjudicate.md"]
        self.assertIn("disconfirm", debate)
        self.assertIn("unresolved", debate)
        self.assertIn("Try to disprove", review)
        self.assertIn("unresolved", review)
        self.assertIn("not verified", review)

    def test_no_fake_independent_reviewers_or_fixed_quotas(self):
        for pages in (self.debate, self.review):
            combined = "\n".join(pages.values())
            self.assertIn("independent", combined)
            self.assertIn("no", combined.lower())
            self.assertIn("quota", combined.lower())
            self.assertIn("material", combined.lower())

    def test_optional_integration_into_outer_loop(self):
        loop = (SKILLS / "general-purpose-loop" / "references" / "cycle.md").read_text(encoding="utf-8")
        self.assertIn("(../../self-debate/SKILL.md)", loop)
        self.assertIn("(../../self-review/SKILL.md)", loop)
        self.assertIn("optionally use", loop)
        self.assertIn("do not invoke them merely", loop)

    def test_portable_without_named_person_or_workspace(self):
        for name, pages in (("self-debate", self.debate), ("self-review", self.review)):
            for filename, content in pages.items():
                with self.subTest(skill=name, path=filename):
                    self.assertNotIn("mols", content.lower())
                    self.assertNotIn("rwerwer1r", content.lower())
                    self.assertNotIn("github.com/", content.lower())


if __name__ == "__main__":
    unittest.main()
