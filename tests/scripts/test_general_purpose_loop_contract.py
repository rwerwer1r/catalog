"""Static contracts for the portable general-purpose loop Skill.

These checks protect packaging and documented gates; they do not simulate an agent.
"""
import unittest
from pathlib import Path


SKILL = Path(__file__).resolve().parents[2] / "src" / "skills" / "general-purpose-loop"


class GeneralPurposeLoopContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pages = {
            path.name: path.read_text(encoding="utf-8")
            for path in SKILL.rglob("*.md")
        }

    def test_discovery_and_gate(self):
        entry = self.pages["SKILL.md"]
        self.assertIn("name: general-purpose-loop", entry)
        self.assertIn("description:", entry)
        self.assertIn("Relevance gate", entry)
        self.assertIn("If irrelevant, stop here", entry)
        self.assertIn("(references/INDEX.md)", entry)

    def test_on_demand_routes(self):
        routes = self.pages["INDEX.md"]
        for page in ("prepare.md", "cycle.md", "focus.md", "close.md"):
            with self.subTest(page=page):
                self.assertIn(f"({page})", routes)
                self.assertIn(page, self.pages)
        self.assertIn("do not preload", routes)

    def test_bounded_run_and_review_accounting(self):
        entry = self.pages["SKILL.md"]
        prepare = self.pages["prepare.md"]
        cycle = self.pages["cycle.md"]
        self.assertIn("30 Reviews per run", entry)
        self.assertIn("30 substantive Reviews", prepare)
        self.assertIn("once", cycle)
        self.assertIn("earliest stale prerequisite", cycle)

    def test_scope_and_child_budget_are_not_expandable(self):
        cycle = self.pages["cycle.md"]
        focus = self.pages["focus.md"]
        self.assertIn("Scope expansion is", cycle)
        self.assertIn("before", cycle)
        self.assertIn("strict subset", focus)
        self.assertIn("same cycle counter and ceiling", focus)
        self.assertIn("Never create a new run", focus)

    def test_terminal_states_and_monotonic_closure(self):
        prep = self.pages["prepare.md"]
        end = self.pages["close.md"]
        self.assertIn("READY WITH LIMITS", prep)
        self.assertIn("BLOCKED", prep)
        self.assertIn("COMPLETE", end)
        self.assertIn("HANDOFF", end)
        self.assertIn("BLOCKED", end)
        self.assertIn("not a new cycle", end)
        self.assertIn("Do not reopen broad investigation", end)

    def test_repository_independence(self):
        for filename, page in self.pages.items():
            with self.subTest(filename=filename):
                self.assertNotIn("src/skills/", page)
                self.assertNotIn("github.com/", page)


if __name__ == "__main__":
    unittest.main()
