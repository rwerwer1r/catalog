"""Focused tests for the Markdown documentation harness."""
import tempfile
import unittest
from pathlib import Path

from tools.validate_docs import validate


class DocumentationHarnessTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        (self.root / "docs").mkdir()
        (self.root / "docs/README.md").write_text(
            '---\ndescription: "Index."\n---\n\n# Docs\n\n[Topic](topic.md)\n',
            encoding="utf-8",
        )
        (self.root / "docs/topic.md").write_text(
            '---\ndescription: "Topic."\n---\n\n# Topic\n\n[Back](README.md)\n',
            encoding="utf-8",
        )

    def tearDown(self):
        self.temp.cleanup()

    def test_valid_docs(self):
        self.assertEqual([], validate(self.root))

    def test_missing_frontmatter(self):
        (self.root / "docs/topic.md").write_text("# Topic\n", encoding="utf-8")
        self.assertTrue(any("frontmatter" in x for x in validate(self.root)))

    def test_bad_local_link(self):
        with (self.root / "docs/topic.md").open("a") as out:
            out.write("\n[Missing](absent.md)\n")
        self.assertTrue(any("missing link target" in x for x in validate(self.root)))

    def test_orphan_page(self):
        (self.root / "docs/orphan.md").write_text(
            '---\ndescription: "Orphan."\n---\n\n# Orphan\n', encoding="utf-8"
        )
        self.assertTrue(any("not linked" in x for x in validate(self.root)))

    def test_fenced_link_ignored(self):
        with (self.root / "docs/topic.md").open("a") as out:
            out.write("\n```md\n[Example](missing.md)\n```\n")
        self.assertEqual([], validate(self.root))


if __name__ == "__main__":
    unittest.main()
