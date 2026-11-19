"""Validate source structure and index.md coverage without external dependencies."""
import re
import sys
from pathlib import Path

KINDS = ("skills", "rules", "references", "agents", "modules", "templates")
NAME = re.compile(r"^[a-z][a-z0-9]*(?:-[a-z0-9]+)*$")


def validate(root: Path) -> list[str]:
    root = root.resolve()
    errors = []
    source = root / "src"

    def read_markdown(path: Path) -> str:
        if not path.is_file() or path.is_symlink():
            errors.append(f"{path.relative_to(root)}: missing or unsafe entrypoint")
            return ""
        body = path.read_text(encoding="utf-8")
        if not body.lstrip().startswith("# "):
            errors.append(f"{path.relative_to(root)}: missing Markdown heading")
        return body

    def require_link(body: str, target: str, index: Path) -> None:
        if f"({target})" not in body:
            errors.append(f"{index.relative_to(root)}: missing index link to {target}")

    readme = source / "README.md"
    home = source / "index.md"
    intro = read_markdown(readme)
    home_body = read_markdown(home)
    require_link(intro, "index.md", readme)

    for kind in KINDS:
        folder = source / kind
        if not folder.is_dir():
            errors.append(f"src/{kind}: missing category directory")
            continue
        readme, index = folder / "README.md", folder / "index.md"
        if not readme.is_file() or not index.is_file() or readme.is_symlink() or index.is_symlink():
            errors.append(f"src/{kind}: missing or unsafe category entrypoint")
            continue
        require_link(home_body, f"{kind}/index.md", home)
        require_link(read_markdown(readme), "index.md", readme)
        listing = read_markdown(index)
        for item in folder.rglob("*"):
            if item.is_symlink():
                errors.append(f"{item.relative_to(root)}: symlinks are not allowed")
        for item in sorted(folder.iterdir()):
            if item.name in {"README.md", "index.md"}:
                continue
            if item.is_file():
                if kind in {"skills", "modules"}:
                    errors.append(f"{item.relative_to(root)}: skills and modules require directories")
                elif item.suffix != ".md" or not NAME.fullmatch(item.stem):
                    errors.append(f"{item.relative_to(root)}: invalid asset filename")
                else:
                    read_markdown(item)
                    require_link(listing, item.name, index)
            elif item.is_dir():
                if kind not in {"skills", "modules"} or not NAME.fullmatch(item.name):
                    errors.append(f"{item.relative_to(root)}: unexpected asset directory")
                    continue
                entry = item / ("SKILL.md" if kind == "skills" else "README.md")
                if not entry.is_file() or entry.is_symlink():
                    errors.append(f"{entry.relative_to(root)}: missing or unsafe asset entrypoint")
                else:
                    read_markdown(entry)
                    require_link(listing, f"{item.name}/{entry.name}", index)
    return errors


def main() -> int:
    errors = validate(Path(__file__).resolve().parents[1])
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    if not errors:
        print("Source layout validation passed.")
    return int(bool(errors))


if __name__ == "__main__":
    raise SystemExit(main())
