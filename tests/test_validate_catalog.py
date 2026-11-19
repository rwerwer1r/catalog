import json
import tempfile
import unittest
from pathlib import Path
from tools.validate_catalog import KINDS, validate


class CatalogHarnessTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        for folder in KINDS.values():
            (self.root / "src" / folder).mkdir(parents=True)
        self.entry = {"id": "sample", "kind": "rule", "path": "src/rules/sample.md", "description": "Sample rule"}
        self.data = {"schema_version": 2, "owner": "rwerwer1r", "source_root": "src", "assets": [self.entry]}
        (self.root / "src/rules/sample.md").write_text("# Sample\n", encoding="utf-8")
        self.save()

    def tearDown(self):
        self.tmp.cleanup()

    def save(self):
        (self.root / "catalog.json").write_text(json.dumps(self.data), encoding="utf-8")

    def test_valid(self):
        self.assertEqual(validate(self.root), [])

    def test_duplicate_id(self):
        self.data["assets"].append(dict(self.entry))
        self.save()
        self.assertTrue(any("duplicate id" in error for error in validate(self.root)))

    def test_unsafe_path(self):
        self.entry["path"] = "../outside.md"
        self.save()
        self.assertTrue(any("unsafe path" in error for error in validate(self.root)))

    def test_missing_file(self):
        (self.root / "src/rules/sample.md").unlink()
        self.assertTrue(any("missing or unsafe file" in error for error in validate(self.root)))

    def test_unregistered_file(self):
        (self.root / "src/rules/extra.md").write_text("# Extra\n", encoding="utf-8")
        self.assertTrue(any("unregistered source" in error for error in validate(self.root)))

    def test_missing_heading(self):
        (self.root / "src/rules/sample.md").write_text("not a heading\n", encoding="utf-8")
        self.assertTrue(any("missing Markdown heading" in error for error in validate(self.root)))


if __name__ == "__main__":
    unittest.main()
