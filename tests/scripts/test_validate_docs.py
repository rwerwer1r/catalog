"""Tests for documentation metadata, navigation and local links."""
import tempfile
import unittest
from pathlib import Path
from scripts.validate_docs import validate


class DocumentationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        docs = self.root / "docs"
        docs.mkdir()
        (docs / "README.md").write_text(
            '---\ndescription: "Intro."\n---\n\n# Docs\n\n[Index](index.md)\n'
        )
        (docs / "index.md").write_text(
            '---\ndescription: "Index."\n---\n\n# Index\n\n[Topic](topic.md)\n'
        )
        (docs / "topic.md").write_text(
            '---\ndescription: "Topic."\n---\n\n# Topic\n\n[Back](index.md)\n'
        )

    def tearDown(self):
        self.tmp.cleanup()

    def test_valid(self):
        self.assertEqual(validate(self.root), [])

    def test_frontmatter(self):
        (self.root / "docs/topic.md").write_text("# Topic\n")
        self.assertTrue(any("frontmatter" in e for e in validate(self.root)))

    def test_broken_link(self):
        with (self.root / "docs/topic.md").open("a") as f:
            f.write("\n[Broken](missing.md)\n")
        self.assertTrue(any("missing link target" in e for e in validate(self.root)))

    def test_unindexed_document(self):
        (self.root / "docs/extra.md").write_text(
            '---\ndescription: "Extra."\n---\n\n# Extra\n'
        )
        self.assertTrue(any("not linked" in e for e in validate(self.root)))

    def test_missing_index(self):
        (self.root / "docs/index.md").unlink()
        self.assertTrue(any("missing README.md or index.md" in e for e in validate(self.root)))

    def test_fenced_link(self):
        with (self.root / "docs/topic.md").open("a") as f:
            f.write("\n" + chr(96) * 3 + "md\n[Example](absent.md)\n" + chr(96) * 3 + "\n")
        self.assertEqual(validate(self.root), [])


if __name__ == "__main__":
    unittest.main()
