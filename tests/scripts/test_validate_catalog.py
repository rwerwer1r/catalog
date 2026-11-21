"""Tests for directory-first source discovery."""
import tempfile
import unittest
from pathlib import Path
from scripts.validate_catalog import KINDS, validate


class SourceLayoutTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        src = self.root / "src"
        src.mkdir()
        (src / "README.md").write_text("# Source\n\n[Index](INDEX.md)\n")
        (src / "INDEX.md").write_text(
            "# Index\n\n" + "\n".join(f"[{k}]({k}/INDEX.md)" for k in KINDS) + "\n"
        )
        for kind in KINDS:
            folder = src / kind
            folder.mkdir()
            (folder / "README.md").write_text(f"# {kind}\n\n[Index](INDEX.md)\n")
            (folder / "INDEX.md").write_text(f"# {kind} index\n")
        self.rule = src / "rules/example.md"
        self.rule.write_text("# Example\n")
        (src / "rules/INDEX.md").write_text("# Rules index\n\n[Example](example.md)\n")

    def tearDown(self):
        self.tmp.cleanup()

    def test_valid(self):
        self.assertEqual(validate(self.root), [])

    def test_unindexed(self):
        self.rule.rename(self.rule.with_name("other.md"))
        self.assertTrue(any("missing index link" in e for e in validate(self.root)))

    def test_missing_category_index(self):
        (self.root / "src/templates/INDEX.md").unlink()
        self.assertTrue(any("missing or unsafe category" in e for e in validate(self.root)))

    def test_invalid_name(self):
        self.rule.rename(self.rule.with_name("Bad Name.md"))
        self.assertTrue(any("invalid asset filename" in e for e in validate(self.root)))

    def test_missing_heading(self):
        self.rule.write_text("no heading\n")
        self.assertTrue(any("missing Markdown heading" in e for e in validate(self.root)))

    def test_missing_skill_entrypoint(self):
        (self.root / "src/skills/other").mkdir()
        self.assertTrue(any("missing or unsafe asset entrypoint" in e for e in validate(self.root)))

    def test_module(self):
        entry = self.root / "src/modules/example/README.md"
        entry.parent.mkdir()
        entry.write_text("# Example\n")
        (entry.parent / "lib.ts").write_text("export const x = 1;\n")
        (self.root / "src/modules/INDEX.md").write_text(
            "# Modules\n\n[Example](example/README.md)\n"
        )
        self.assertEqual(validate(self.root), [])


if __name__ == "__main__":
    unittest.main()
