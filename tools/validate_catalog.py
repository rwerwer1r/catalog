"""Standard-library validation for the reusable asset catalog."""
import json
import re
import sys
from pathlib import Path, PurePosixPath

KINDS = {"skill": "skills", "rule": "rules", "reference": "references", "agent": "agents", "module": "modules", "template": "templates"}
IDENTIFIER = re.compile(r"^[a-z][a-z0-9]*(?:-[a-z0-9]+)*$")


def validate(root: Path) -> list[str]:
    root = root.resolve()
    errors = []
    try:
        data = json.loads((root / "catalog.json").read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        return [f"catalog.json: {exc}"]
    if not isinstance(data, dict):
        return ["catalog.json must be an object"]
    if data.get("schema_version") != 2:
        errors.append("schema_version must be 2")
    if data.get("owner") != "rwerwer1r":
        errors.append("owner must be rwerwer1r")
    if data.get("source_root") != "src":
        errors.append("source_root must be src")
    entries = data.get("assets")
    if not isinstance(entries, list):
        return errors + ["assets must be a list"]
    ids, paths = set(), set()
    for index, entry in enumerate(entries):
        prefix = f"assets[{index}]"
        if not isinstance(entry, dict):
            errors.append(f"{prefix}: expected object")
            continue
        ident, kind, path = entry.get("id"), entry.get("kind"), entry.get("path")
        if not isinstance(ident, str) or not IDENTIFIER.fullmatch(ident):
            errors.append(f"{prefix}: invalid id")
            continue
        if ident in ids:
            errors.append(f"{prefix}: duplicate id {ident}")
        ids.add(ident)
        if kind not in KINDS:
            errors.append(f"{prefix}: unsupported kind")
            continue
        if not isinstance(entry.get("description"), str) or not entry["description"].strip():
            errors.append(f"{prefix}: missing description")
        if not isinstance(path, str):
            errors.append(f"{prefix}: invalid path")
            continue
        pp = PurePosixPath(path)
        if pp.is_absolute() or ".." in pp.parts or "\\" in path:
            errors.append(f"{prefix}: unsafe path")
            continue
        if kind == "skill":
            allowed = {f"src/skills/{ident}/SKILL.md"}
        elif kind == "module":
            allowed = {f"src/modules/{ident}.py", f"src/modules/{ident}/README.md"}
        else:
            allowed = {f"src/{KINDS[kind]}/{ident}.md"}
        if path not in allowed:
            errors.append(f"{prefix}: unexpected path {path}")
            continue
        if path in paths:
            errors.append(f"{prefix}: duplicate path {path}")
        paths.add(path)
        full = root / path
        if full.is_symlink() or not full.is_file() or not full.resolve().is_relative_to(root):
            errors.append(f"{prefix}: missing or unsafe file {path}")
        elif path.endswith(".md"):
            try:
                content = full.read_text(encoding="utf-8")
                if not content.lstrip().startswith("# "):
                    errors.append(f"{prefix}: missing Markdown heading")
            except (OSError, UnicodeError) as exc:
                errors.append(f"{prefix}: cannot read file: {exc}")
    for folder in KINDS.values():
        directory = root / "src" / folder
        if not directory.is_dir():
            errors.append(f"missing directory: src/{folder}")
            continue
        for item in directory.rglob("*"):
            if item.is_symlink():
                errors.append(f"symlink not allowed: {item.relative_to(root)}")
            elif item.is_file() and item.name not in {"README.md", ".gitkeep"}:
                rel = item.relative_to(root).as_posix()
                if rel not in paths:
                    errors.append(f"unregistered source: {rel}")
    return errors


def main() -> int:
    problems = validate(Path(__file__).resolve().parents[1])
    for error in problems:
        print(f"ERROR: {error}", file=sys.stderr)
    if problems:
        return 1
    print("Catalog validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
