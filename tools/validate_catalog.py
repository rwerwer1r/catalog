"""Check the on-disk reusable source layout and category index coverage.

Source directories and their README links are authoritative; no duplicate
asset registry or third-party dependency is required.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

KINDS = ("skills", "rules", "references", "agents", "modules", "templates")
NAME = re.compile(r"^[a-z][a-z0-9]*(?:-[a-z0-9]+)*$")


def _heading(path: Path, root: Path, errors: list[str]) -> None:
    relative = path.relative_to(root).as_posix()
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        errors.append(f"{relative}: cannot read file: {exc}")
        return
    if not text.lstrip().startswith("# "):
        errors.append(f"{relative}: missing Markdown heading")


def _check_link(index: str, href: str, location: Path, root: Path, errors: list[str]) -> None:
    if f"({href})" not in index:
        errors.append(f"{location.relative_to(root)}: missing index link to {href}")


def validate(root: Path) -> list[str]:
    root = root.resolve()
    errors: list[str] = []
    source = root / "src"
    index = source / "README.md"
    if not index.is_file():
        return ["src/README.md: missing source entrypoint"]
    _heading(index, root, errors)
    root_index = index.read_text(encoding="utf-8")

    for kind in KINDS:
        location = source / kind
        readme = location / "README.md"
        if not readme.is_file() or readme.is_symlink():
            errors.append(f"src/{kind}/README.md: missing or unsafe category entrypoint")
            continue
        _heading(readme, root, errors)
        _check_link(root_index, f"{kind}/README.md", index, root, errors)
        content = readme.read_text(encoding="utf-8")

        # Do not accept symlinks anywhere in reusable source.
        for item in location.rglob("*"):
            if item.is_symlink():
                errors.append(f"{item.relative_to(root)}: symlinks are not allowed")

        for item in sorted(location.iterdir()):
            if item.name == "README.md":
                continue
            if item.is_file():
                if kind in {"skills", "modules"}:
                    errors.append(f"{item.relative_to(root)}: skills and modules require directories")
                    continue
                if item.suffix != ".md" or not NAME.fullmatch(item.stem):
                    errors.append(f"{item.relative_to(root)}: invalid asset filename")
                    continue
                if item.suffix == ".md":
                    _heading(item, root, errors)
                _check_link(content, item.name, readme, root, errors)
            elif item.is_dir():
                if kind not in {"skills", "modules"} or not NAME.fullmatch(item.name):
                    errors.append(f"{item.relative_to(root)}: unexpected asset directory")
                    continue
                entryname = "SKILL.md" if kind == "skills" else "README.md"
                entry = item / entryname
                if not entry.is_file() or entry.is_symlink():
                    errors.append(f"{entry.relative_to(root)}: missing or unsafe asset entrypoint")
                    continue
                _heading(entry, root, errors)
                _check_link(content, f"{item.name}/{entryname}", readme, root, errors)
            else:
                errors.append(f"{item.relative_to(root)}: unsupported source entry")
    return errors


def main() -> int:
    problems = validate(Path(__file__).resolve().parents[1])
    for problem in problems:
        print(f"ERROR: {problem}", file=sys.stderr)
    if problems:
        return 1
    print("Source layout validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
