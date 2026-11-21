"""Guard lightweight entrypoints and on-demand path size.

Character counts are a stable context-size proxy, NOT measured model tokens.
The limits are regression guardrails rather than targets for arbitrary shortening.
"""
import unittest
from pathlib import Path


SKILLS = Path(__file__).resolve().parents[2] / "src" / "skills"
ROUTES = {
    "agent-asset-authoring": ("author.md", "review.md"),
    "documentation-authoring": ("write.md", "maintain.md"),
    "general-purpose-loop": ("prepare.md", "cycle.md", "focus.md", "close.md"),
    "self-debate": ("frame.md", "examine.md", "resolve.md"),
    "self-review": ("scope.md", "inspect.md", "adjudicate.md"),
}


class ContextEconomyTests(unittest.TestCase):
    def test_every_skill_gate_has_bounded_context(self):
        for skill in sorted(SKILLS.iterdir()):
            if not (skill / "SKILL.md").is_file():
                continue
            with self.subTest(skill=skill.name):
                body = (skill / "SKILL.md").read_text(encoding="utf-8")
                self.assertLessEqual(len(body), 2000, "Skill entrypoint is too large for a gate")
                self.assertIn("Relevance gate", body)
                self.assertIn("stop here", body.lower())

    def test_routing_indexes_stay_small_and_selective(self):
        for name, targets in ROUTES.items():
            with self.subTest(skill=name):
                skill = SKILLS / name
                gate = (skill / "SKILL.md").read_text(encoding="utf-8")
                routes = (skill / "INDEX.md").read_text(encoding="utf-8")
                self.assertLessEqual(len(routes), 1000, "Routing index should not be a guide")
                self.assertIn("(INDEX.md)", gate)
                self.assertIn("only", routes.lower())
                for target in targets:
                    self.assertIn(f"({target})", routes)
                    self.assertTrue((skill / target).is_file())

    def test_single_route_loading_path_is_bounded(self):
        for name, targets in ROUTES.items():
            with self.subTest(skill=name):
                skill = SKILLS / name
                front = len((skill / "SKILL.md").read_text(encoding="utf-8"))
                route = len((skill / "INDEX.md").read_text(encoding="utf-8"))
                largest_selected_step = max(
                    len((skill / target).read_text(encoding="utf-8"))
                    for target in targets
                )
                # Only one procedure is selected at a time; dependencies
                # are loaded when actually needed and have separate budgets.
                self.assertLessEqual(front + route + largest_selected_step, 4700)

    def test_companion_only_at_document_boundary(self):
        skill = SKILLS / "agent-asset-authoring"
        entry = (skill / "SKILL.md").read_text(encoding="utf-8")
        index = (skill / "INDEX.md").read_text(encoding="utf-8")
        self.assertIn("required one-way dependency", entry)
        self.assertIn("just before editing or reviewing written asset content", entry)
        self.assertIn("Before editing or reviewing written content", index)

    def test_small_skill_does_not_need_routing_scaffold(self):
        skill = SKILLS / "repository-readiness"
        self.assertFalse((skill / "INDEX.md").exists())
        self.assertTrue((skill / "SKILL.md").is_file())


if __name__ == "__main__":
    unittest.main()
