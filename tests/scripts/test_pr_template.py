"""Ensure PR validation instructions stay aligned with one-line CI commands."""
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def python_ci_commands(workflow: str) -> set[str]:
    """Extract unquoted, one-line Python steps, including YAML comments."""
    return {
        command.strip()
        for command in re.findall(
            r"^\s*- run: (python3 [^\n#]+)(?:[ \t]+#.*)?$",
            workflow,
            re.MULTILINE,
        )
    }


class PullRequestTemplateTests(unittest.TestCase):
    def test_validation_commands_match_workflow(self):
        workflow = (ROOT / ".github/workflows/validate.yml").read_text(encoding="utf-8")
        template = (ROOT / ".github/pull_request_template.md").read_text(encoding="utf-8")
        ci_commands = python_ci_commands(workflow)
        self.assertTrue(ci_commands, "No one-line Python CI validation commands found")
        template_commands = set(re.findall(r"`(python3 [^`]+)`", template))
        self.assertEqual(template_commands, ci_commands)

    def test_inline_comment_does_not_hide_validation_command(self):
        workflow = "steps:\n  - run: python3 scripts/validate.py # validate docs\n"
        self.assertEqual(python_ci_commands(workflow), {"python3 scripts/validate.py"})


if __name__ == "__main__":
    unittest.main()
