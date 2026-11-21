"""Published authoring contracts that structural link checks alone cannot protect."""
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SKILLS = ROOT / "src" / "skills"


class AuthoringContractTests(unittest.TestCase):
    def test_one_way_required_documentation_dependency(self):
        asset = (SKILLS / "agent-asset-authoring" / "SKILL.md").read_text()
        docs = (SKILLS / "documentation-authoring" / "SKILL.md").read_text()
        self.assertIn("(../documentation-authoring/SKILL.md)", asset)
        self.assertIn("required one-way dependency", asset)
        self.assertNotIn("(../agent-asset-authoring/SKILL.md)", docs)

    def test_relevance_gates_route_only_after_acceptance(self):
        for name in ("agent-asset-authoring", "documentation-authoring"):
            with self.subTest(skill=name):
                entry = (SKILLS / name / "SKILL.md").read_text()
                self.assertIn("Relevance gate", entry)
                self.assertIn("Use only for", entry)
                self.assertIn("references/INDEX.md)", entry)
                self.assertIn("stop here", entry)

    def test_routes_avoid_preloading_other_workflows(self):
        expected = {
            "agent-asset-authoring": ("author.md", "review.md"),
            "documentation-authoring": ("entrypoints.md", "indexes.md", "write.md", "maintain.md"),
        }
        for name, files in expected.items():
            with self.subTest(skill=name):
                routes = (SKILLS / name / "references" / "INDEX.md").read_text()
                self.assertIn("only", routes.lower())
                for file in files:
                    self.assertIn(f"({file})", routes)


if __name__ == "__main__":
    unittest.main()
