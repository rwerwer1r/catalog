"""Ensure PR validation instructions stay aligned with one-line CI commands."""
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


class PullRequestTemplateTests(unittest.TestCase):
    def test_validation_commands_match_workflow(self):
        workflow = (ROOT / ".github/workflows/validate.yml").read_text(encoding="utf-8")
        template = (ROOT / ".github/pull_request_template.md").read_text(encoding="utf-8")
        ci_commands = {
            command.strip()
            for command in re.findall(r"^\s*- run: (python3 [^\n#]+)$", workflow, re.MULTILINE)
        }
        self.assertTrue(ci_commands, "No one-line Python CI validation commands found")
        template_commands = set(re.findall(r"`(python3 [^`]+)`", template))
        self.assertEqual(template_commands, ci_commands)


if __name__ == "__main__":
    unittest.main()
