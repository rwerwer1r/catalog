"""Validate documentation metadata, entrypoints and local Markdown links.

Only standard-library facilities are used. This is intentionally a focused checker:
it does not parse arbitrary YAML or guarantee that every rendering engine agrees.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

LINK = re.compile(r"!?\[[^\]]*\]\((<[^>]+>|[^)]+)\)")
FRONTMATTER = re.compile(r"\A---\n(.*?)\n---\n\n", re.DOTALL)
KEY_VALUE = re.compile(r"^([a-z][a-z_-]*):\s*(.*)$")
ALLOWED = {"description", "status", "audience"}
STATUS = {"draft", "active", "deprecated"}


def without_fences(text: str) -> str:
    """Exclude fenced examples from link and heading inspection."""
    output = []
    fence = None
    for line in text.splitlines():
        match = re.match(r"^\s{0,3}(`{3,}|~{3,})", line)
        if match:
            marker = match.group(1)
            if fence is None:
                fence = marker
            elif marker[0] == fence[0] and len(marker) >= len(fence):
                fence = None
            output.append("")
        else:
            output.append("" if fence else line)
    return "\n".join(output)


def frontmatter_errors(relative: str, content: str) -> list[str]:
    match = FRONTMATTER.match(content)
    if not match:
        return [f"{relative}: missing frontmatter or blank line after closing delimiter"]
    errors = []
    values = {}
    for line in match.group(1).splitlines():
        item = KEY_VALUE.fullmatch(line)
        if item is None:
            errors.append(f"{relative}: unsupported frontmatter syntax")
            continue
        key, value = item.groups()
        if key not in ALLOWED or key in values:
            errors.append(f"{relative}: unknown or duplicate key: {key}")
        values[key] = value.strip().strip('"').strip("'")
    if not values.get("description"):
        errors.append(f"{relative}: nonempty description is required")
    if values.get("status") and values["status"] not in STATUS:
        errors.append(f"{relative}: invalid status")
    body = content[match.end():]
    if not body.startswith("# "):
        errors.append(f"{relative}: first content heading must be H1")
    if len(re.findall(r"^# ", without_fences(body), re.MULTILINE)) != 1:
        errors.append(f"{relative}: exactly one H1 is required")
    return errors


def local_links(relative: str, content: str, root: Path) -> list[str]:
    errors = []
    for match in LINK.finditer(without_fences(content)):
        target = match.group(1).strip()
        if target.startswith("<") and target.endswith(">"):
            target = target[1:-1]
        target = target.split(' "')[0].split(" '")[0]
        if re.match(r"^[A-Za-z][A-Za-z0-9+.-]*:", target) or target.startswith("//"):
            continue
        path_part = unquote(target.split("#", 1)[0].split("?", 1)[0])
        if not path_part:
            continue
        if path_part.startswith("/"):
            errors.append(f"{relative}: use repository-relative link: {target}")
            continue
        destination = (root / relative).parent / path_part
        resolved = destination.resolve()
        if not resolved.is_relative_to(root.resolve()):
            errors.append(f"{relative}: link escapes repository: {target}")
        elif destination.is_dir():
            if not (destination / "INDEX.md").is_file():
                errors.append(f"{relative}: directory lacks INDEX.md: {target}")
        elif not destination.is_file():
            errors.append(f"{relative}: missing link target: {target}")
    return errors


def validate(root: Path) -> list[str]:
    root = root.resolve()
    docs = root / "docs"
    if not docs.is_dir():
        return ["docs/: directory not found"]
    errors = []
    markdown = sorted(docs.rglob("*.md"))
    for file in markdown:
        relative = file.relative_to(root).as_posix()
        if file.is_symlink():
            errors.append(f"{relative}: symlinks are not allowed")
            continue
        try:
            content = file.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            errors.append(f"{relative}: cannot read file: {exc}")
            continue
        errors.extend(frontmatter_errors(relative, content))
        errors.extend(local_links(relative, content, root))

    for directory in [docs, *[d for d in docs.rglob("*") if d.is_dir()]]:
        readme, index = directory / "README.md", directory / "INDEX.md"
        names = {item.name for item in directory.iterdir()}
        if "index.md" in names:
            errors.append(f"{directory.relative_to(root)}: legacy index.md; use INDEX.md")
        if not {"README.md", "INDEX.md"}.issubset(names) or not readme.is_file() or not index.is_file():
            errors.append(f"{directory.relative_to(root)}: missing README.md or INDEX.md")
            continue
        intro = without_fences(readme.read_text(encoding="utf-8"))
        listing = without_fences(index.read_text(encoding="utf-8"))
        if "(INDEX.md)" not in intro:
            errors.append(f"{readme.relative_to(root)}: missing link to INDEX.md")
        for page in directory.glob("*.md"):
            if page.name not in {"README.md", "INDEX.md"} and f"({page.name})" not in listing:
                errors.append(f"{page.relative_to(root)}: not linked from directory index")
        for child in directory.iterdir():
            if child.is_dir() and f"({child.name}/INDEX.md)" not in listing:
                errors.append(f"{child.relative_to(root)}: not linked from parent index")
    return errors


def main() -> int:
    errors = validate(Path(__file__).resolve().parents[1])
    for error in errors:
        print("ERROR:", error, file=sys.stderr)
    if errors:
        return 1
    print("Documentation validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
