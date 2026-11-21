"""Regression tests for Agent Skills metadata, route coverage, and links."""
import tempfile
import unittest
from pathlib import Path

from scripts.validate_catalog import KINDS, validate


class SkillRoutingTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        src = self.root / "src"
        src.mkdir()
        (src / "README.md").write_text("# Source\n\n[Index](INDEX.md)\n")
        (src / "INDEX.md").write_text(
            "# Index\n\n" + "\n".join(f"[{kind}]({kind}/INDEX.md)" for kind in KINDS) + "\n"
        )
        for kind in KINDS:
            category = src / kind
            category.mkdir()
            (category / "README.md").write_text(f"# {kind}\n\n[Index](INDEX.md)\n")
            (category / "INDEX.md").write_text(f"# {kind} index\n")
        self.skill = src / "skills" / "example"
        self.skill.mkdir()
        (self.skill / "references").mkdir()
        (src / "skills" / "INDEX.md").write_text(
            "# Skills index\n\n[Example](example/SKILL.md)\n"
        )
        self.entry = self.skill / "SKILL.md"
        self.entry.write_text(
            "---\nname: example\n"
            "description: Use for an example agent workflow.\n"
            "---\n\n# Example\n\n[Routes](INDEX.md)\n"
        )
        (self.skill / "references" / "INDEX.md").write_text(
            "# Routes\n\n[Write](write.md)\n"
        )
        (self.skill / "references" / "write.md").write_text("# Write\n\nUse repository rules.\n")

    def tearDown(self):
        self.tmp.cleanup()

    def issues(self):
        return validate(self.root)

    def test_complete_skill_passes(self):
        self.assertEqual(self.issues(), [])

    def test_missing_frontmatter_fails(self):
        self.entry.write_text("# Example\n\n[Routes](INDEX.md)\n")
        self.assertTrue(any("missing Agent Skills YAML frontmatter" in e for e in self.issues()))

    def test_mismatched_name_fails(self):
        self.entry.write_text(self.entry.read_text().replace("name: example", "name: wrong"))
        self.assertTrue(any("mismatched Skill name" in e for e in self.issues()))

    def test_missing_description_fails(self):
        self.entry.write_text(
            self.entry.read_text().replace(
                "description: Use for an example agent workflow.\n", ""
            )
        )
        self.assertTrue(any("Skill description" in e for e in self.issues()))

    def test_missing_route_file_fails(self):
        (self.skill / "references" / "write.md").unlink()
        self.assertTrue(any("missing Skill link target" in e for e in self.issues()))

    def test_unlinked_index_fails(self):
        self.entry.write_text(self.entry.read_text().replace("[Routes](references/INDEX.md)", "No route."))
        self.assertTrue(any("missing link to Skill-local references/INDEX.md" in e for e in self.issues()))

    def test_plain_index_marker_does_not_count_as_entrypoint_link(self):
        self.entry.write_text(
            self.entry.read_text().replace("[Routes](references/INDEX.md)", "See (references/INDEX.md).")
        )
        self.assertTrue(any("missing link to Skill-local references/INDEX.md" in e for e in self.issues()))

    def test_fenced_index_marker_does_not_count_as_route_link(self):
        self.entry.write_text(
            self.entry.read_text().replace(
                "[Routes](references/INDEX.md)",
                "```markdown\n[Routes](references/INDEX.md)\n```",
            )
        )
        self.assertTrue(any("missing link to Skill-local references/INDEX.md" in e for e in self.issues()))

    def test_external_only_routes_are_rejected(self):
        (self.skill / "references" / "INDEX.md").write_text(
            "# Routes\n\n[Remote](https://example.com/write.md)\n"
        )
        self.assertTrue(any("no local procedure targets" in e for e in self.issues()))

    def test_sibling_skill_is_not_an_internal_procedure(self):
        other = self.root / "src" / "skills" / "other"
        other.mkdir()
        (other / "SKILL.md").write_text(
            "---\nname: other\ndescription: Other workflow.\n---\n\n# Other\n"
        )
        index = self.root / "src" / "skills" / "INDEX.md"
        index.write_text(index.read_text() + "[Other](other/SKILL.md)\n")
        (self.skill / "references" / "INDEX.md").write_text(
            "# Routes\n\n[Other](../other/SKILL.md)\n"
        )
        self.assertTrue(any("no local procedure targets" in e for e in self.issues()))

    def test_plain_category_marker_is_not_an_index_link(self):
        index = self.root / "src" / "skills" / "INDEX.md"
        index.write_text("# Skills index\n\nExample: (example/SKILL.md)\n")
        self.assertTrue(any("missing index link to example/SKILL.md" in e for e in self.issues()))

    def test_plain_source_index_marker_is_not_a_readme_link(self):
        readme = self.root / "src" / "README.md"
        readme.write_text("# Source\n\nSee (INDEX.md).\n")
        self.assertTrue(any("missing index link to INDEX.md" in e for e in self.issues()))

    def test_lowercase_duplicate_fails(self):
        (self.skill / "index.md").write_text("# Duplicate routes\n")
        self.assertTrue(any("Skill routes belong in references/INDEX.md" in e for e in self.issues()))

    def test_legacy_root_skill_index_is_rejected(self):
        (self.skill / "INDEX.md").write_text("# Legacy routes\\n")
        self.assertTrue(any(
            "Skill routes belong in references/INDEX.md" in e for e in self.issues()
        ))

    def test_index_without_procedure_fails(self):
        (self.skill / "references" / "INDEX.md").write_text("# Routes\n\n[Gate](SKILL.md)\n")
        self.assertTrue(any("no local procedure targets" in e for e in self.issues()))

    def test_missing_required_dependency_fails(self):
        with self.entry.open("a") as file:
            file.write("\n[Required Skill](../missing/SKILL.md)\n")
        self.assertTrue(any("missing Skill link target" in e for e in self.issues()))

    def test_remote_and_fenced_examples_are_ignored(self):
        with self.entry.open("a") as file:
            file.write("\n[Official spec](https://agentskills.io/specification)\n")
            file.write("\n" + chr(96) * 3 + "markdown\n")
            file.write("[Not a link](nonexistent.md)\n" + chr(96) * 3 + "\n")
        self.assertEqual(self.issues(), [])

    def test_empty_skill_without_routes_is_valid(self):
        (self.skill / "references" / "INDEX.md").unlink()
        (self.skill / "references" / "write.md").unlink()
        self.entry.write_text(self.entry.read_text().replace("[Routes](references/INDEX.md)", ""))
        self.assertEqual(self.issues(), [])


if __name__ == "__main__":
    unittest.main()
