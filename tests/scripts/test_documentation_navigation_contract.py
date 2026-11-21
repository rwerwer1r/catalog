"""Contract checks for documentation Skill ownership and navigation formats.

These test documented routes, not real agent behavior or a future generator.
"""
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SKILL = ROOT / "src" / "skills" / "documentation-authoring"


class DocumentationNavigationContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.skill = (SKILL / "SKILL.md").read_text(encoding="utf-8")
        cls.routes = (SKILL / "INDEX.md").read_text(encoding="utf-8")
        cls.entrypoints = (SKILL / "entrypoints.md").read_text(encoding="utf-8")
        cls.indexes = (SKILL / "indexes.md").read_text(encoding="utf-8")

    def test_entrypoint_and_index_rules_have_one_reusable_owner(self):
        self.assertIn("owns reader-facing entrypoint, index", self.skill)
        self.assertIn("(entrypoints.md)", self.routes)
        self.assertIn("(indexes.md)", self.routes)
        handbook = (
            ROOT / "docs" / "documentation" / "entrypoints.md"
        ).read_text(encoding="utf-8")
        self.assertIn(
            "(../../src/skills/documentation-authoring/entrypoints.md)", handbook
        )
        self.assertIn(
            "(../../src/skills/documentation-authoring/indexes.md)", handbook
        )

    def test_asset_skill_delegates_document_navigation(self):
        asset = ROOT / "src" / "skills" / "agent-asset-authoring"
        for file in ("author.md", "review.md"):
            with self.subTest(file=file):
                text = (asset / file).read_text(encoding="utf-8")
                self.assertIn("(../documentation-authoring/SKILL.md)", text)

    def test_entrypoint_gate_and_metadata_are_consumer_oriented(self):
        for term in (
            "README.md", "SKILL.md", "description saying when to use it",
            "relevance gate", "stop", "single compact workflow",
        ):
            with self.subTest(term=term):
                self.assertIn(term, self.entrypoints)
        self.assertIn("discovery-metadata guidance", self.skill)

    def test_manual_markdown_index_is_not_generated(self):
        for term in (
            "INDEX.md", "hand-maintained", "index-only",
            "Never attach an auto-generation script to INDEX.md",
            "Existing manual", "index.md",
        ):
            with self.subTest(term=term):
                self.assertIn(term, self.indexes)

    def test_tsv_is_reserved_for_metadata_driven_generation(self):
        for term in (
            "INDEX.tsv", "authorized script", "frontmatter",
            "Required columns in order", "`path`", "`description`",
            "UTF-8 TSV", "Sort", "stale paths",
        ):
            with self.subTest(term=term):
                self.assertIn(term, self.indexes)

    def test_consumers_select_by_description_and_open_one_page(self):
        for term in (
            "when to read", "Consumers select using descriptions",
            "load the chosen page only", "never guess",
            "not factual verification",
        ):
            with self.subTest(term=term):
                self.assertIn(term, self.indexes)

    def test_no_duplicate_authoritative_index(self):
        for term in (
            "one canonical index per navigation role",
            "different interfaces", "not duplicate independently edited",
            "Existing category", "Do not rename",
        ):
            with self.subTest(term=term):
                self.assertIn(term, self.indexes)

    def test_tsv_contract_is_not_implicitly_executed(self):
        validation = (
            ROOT / "docs" / "development" / "validation.md"
        ).read_text(encoding="utf-8")
        local = (
            ROOT / "docs" / "documentation" / "entrypoints.md"
        ).read_text(encoding="utf-8")
        self.assertIn("No metadata-driven `INDEX.tsv` generator", validation)
        self.assertIn("no such generator is implied", local)


if __name__ == "__main__":
    unittest.main()
