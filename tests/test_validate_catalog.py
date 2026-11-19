"""Tests for the directory-first asset layout validator."""
import tempfile
import unittest
from pathlib import Path

from tools.validate_catalog import KINDS, validate


class SourceLayoutTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        source = self.root / "src"
        source.mkdir()
        (source / "README.md").write_text(
            "# Source\n\n" + "\n".join(f"[{k}]({k}/README.md)" for k in KINDS) + "\n",
            encoding="utf-8",
        )
        for kind in KINDS:
            folder = source / kind
            folder.mkdir()
            (folder / "README.md").write_text("# " + kind + "\n", encoding="utf-8")
        self.rule = source / "rules" / "example.md"
        self.rule.write_text("# Example\n", encoding="utf-8")
        (source / "rules" / "README.md").write_text(
            "# Rules\n\n[Example](example.md)\n", encoding="utf-8"
        )

    def tearDown(self):
        self.temp.cleanup()

    def test_valid_layout(self):
        self.assertEqual([], validate(self.root))

    def test_unindexed_asset(self):
        self.rule.rename(self.rule.with_name("other.md"))
        self.assertTrue(any("missing index link" in e for e in validate(self.root)))

    def test_missing_category_entrypoint(self):
        (self.root / "src/templates/README.md").unlink()
        self.assertTrue(any("missing or unsafe category" in e for e in validate(self.root)))

    def test_invalid_filename(self):
        self.rule.rename(self.rule.with_name("Bad Name.md"))
        self.assertTrue(any("invalid asset filename" in e for e in validate(self.root)))

    def test_skill_requires_entrypoint(self):
        (self.root / "src/skills/sample").mkdir()
        self.assertTrue(any("missing or unsafe asset entrypoint" in e for e in validate(self.root)))

    def test_missing_heading(self):
        self.rule.write_text("No heading\n", encoding="utf-8")
        self.assertTrue(any("missing Markdown heading" in e for e in validate(self.root)))

    def test_module_package_indexed(self):
        entry = self.root / "src/modules/example-package/README.md"
        entry.parent.mkdir()
        entry.write_text("# Example package\n", encoding="utf-8")
        (entry.parent / "lib.ts").write_text("export const value = 1;\n", encoding="utf-8")
        with (self.root / "src/modules/README.md").open("a", encoding="utf-8") as out:
            out.write("\n[Example package](example-package/README.md)\n")
        self.assertEqual([], validate(self.root))

    def test_skill_indexed(self):
        entry = self.root / "src/skills/sample/SKILL.md"
        entry.parent.mkdir()
        entry.write_text("# Sample skill\n", encoding="utf-8")
        with (self.root / "src/skills/README.md").open("a", encoding="utf-8") as out:
            out.write("\n[Sample](sample/SKILL.md)\n")
        self.assertEqual([], validate(self.root))


if __name__ == "__main__":
    unittest.main()
