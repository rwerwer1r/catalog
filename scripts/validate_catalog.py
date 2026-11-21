"""Validate source structure and INDEX.md coverage without external dependencies."""
import re
import sys
from pathlib import Path
from urllib.parse import unquote

KINDS = ("skills", "rules", "references", "agents", "modules", "templates")
NAME = re.compile(r"^[a-z][a-z0-9]*(?:-[a-z0-9]+)*$")



SKILL_FRONTMATTER = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.DOTALL)
MD_LINK = re.compile(r"!?\[[^\]]*\]\((<[^>]+>|[^)]+)\)")


def _without_fences(content: str) -> str:
    lines = []
    fence = None
    for line in content.splitlines():
        marker = re.match(r"^\s{0,3}((?:\x60){3,}|~{3,})", line)
        if marker:
            token = marker.group(1)
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence):
                fence = None
            lines.append("")
        else:
            lines.append("" if fence else line)
    return "\n".join(lines)


def _link_targets(content: str):
    for match in MD_LINK.finditer(_without_fences(content)):
        target = match.group(1).strip()
        if target.startswith("<") and target.endswith(">"):
            target = target[1:-1]
        yield target.split(' "')[0].split(" '")[0]


def _skill_frontmatter_errors(entry: Path, root: Path, content: str) -> list[str]:
    relative = entry.relative_to(root)
    match = SKILL_FRONTMATTER.match(content)
    if not match:
        return [f"{relative}: missing Agent Skills YAML frontmatter"]
    values = {}
    errors = []
    for line in match.group(1).splitlines():
        field = re.fullmatch(r"([a-z][a-z-]*):\s*(.*)", line)
        if field:
            key, value = field.groups()
            if key in values:
                errors.append(f"{relative}: duplicate frontmatter key: {key}")
            values[key] = value.strip().strip("\"'")
    name = values.get("name", "")
    description = values.get("description", "")
    if not NAME.fullmatch(name) or len(name) > 64 or name != entry.parent.name:
        errors.append(f"{relative}: invalid or mismatched Skill name")
    if not 1 <= len(description) <= 1024 or description in {"|", ">", "|-", ">-"}:
        errors.append(f"{relative}: missing or invalid Skill description")
    if not content[match.end():].lstrip().startswith("# "):
        errors.append(f"{relative}: Markdown body must begin with an H1")
    return errors


def _skill_errors(skill: Path, root: Path) -> list[str]:
    entry = skill / "SKILL.md"
    if not entry.is_file() or entry.is_symlink():
        return []  # the source layout validator reports missing entrypoints
    errors = []
    body = entry.read_text(encoding="utf-8")
    errors.extend(_skill_frontmatter_errors(entry, root, body))

    for extra in skill.iterdir():
        if extra.is_file() and extra.suffix == ".md" and extra.name != "SKILL.md":
            errors.append(f"{extra.relative_to(root)}: Skill support Markdown belongs in references/")

    route = skill / "references" / "INDEX.md"
    legacy = (skill / "INDEX.md", skill / "index.md", skill / "references" / "index.md")
    for old in legacy:
        if old.exists():
            errors.append(f"{old.relative_to(root)}: Skill routes belong in references/INDEX.md")
    if route.is_file():
        entry_links = {
            unquote(target.split("#", 1)[0].split("?", 1)[0])
            for target in _link_targets(body)
        }
        if "references/INDEX.md" not in entry_links:
            errors.append(f"{entry.relative_to(root)}: missing link to Skill-local references/INDEX.md")
        routes = []
        for target in _link_targets(route.read_text(encoding="utf-8")):
            if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target) or target.startswith("//"):
                continue
            local = unquote(target.split("#", 1)[0].split("?", 1)[0])
            if not local or local.startswith("/"):
                continue
            destination = (route.parent / local).resolve()
            if (
                destination.is_relative_to(route.parent.resolve())
                and destination.is_file()
                and destination.suffix == ".md"
                and destination not in {entry.resolve(), route.resolve()}
                and not (route.parent / local).is_symlink()
            ):
                routes.append(local)
        if not routes:
            errors.append(f"{route.relative_to(root)}: routing index has no local procedure targets")

    for page in sorted(skill.rglob("*.md")):
        if page.is_symlink():
            continue  # already rejected by the category validator
        relative = page.relative_to(root)
        for target in _link_targets(page.read_text(encoding="utf-8")):
            if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target) or target.startswith("//"):
                continue
            local = unquote(target.split("#", 1)[0].split("?", 1)[0])
            if not local:
                continue
            if local.startswith("/"):
                errors.append(f"{relative}: absolute local link: {target}")
                continue
            destination = (page.parent / local).resolve()
            if not destination.is_relative_to(root):
                errors.append(f"{relative}: link escapes repository: {target}")
            elif not destination.is_file():
                errors.append(f"{relative}: missing Skill link target: {target}")
    return errors



def validate(root: Path) -> list[str]:
    root = root.resolve()
    errors = []
    source = root / "src"

    def read_markdown(path: Path) -> str:
        if not path.is_file() or path.is_symlink():
            errors.append(f"{path.relative_to(root)}: missing or unsafe entrypoint")
            return ""
        body = path.read_text(encoding="utf-8")
        if not re.sub(r"\A---\r?\n.*?\r?\n---\r?\n", "", body, count=1, flags=re.DOTALL).lstrip().startswith("# "):
            errors.append(f"{path.relative_to(root)}: missing Markdown heading")
        return body

    def require_link(body: str, target: str, index: Path) -> None:
        targets = {
            unquote(link.split("#", 1)[0].split("?", 1)[0])
            for link in _link_targets(body)
        }
        if target not in targets:
            errors.append(f"{index.relative_to(root)}: missing index link to {target}")

    readme = source / "README.md"
    home = source / "INDEX.md"
    intro = read_markdown(readme)
    home_body = read_markdown(home)
    require_link(intro, "INDEX.md", readme)

    for kind in KINDS:
        folder = source / kind
        if not folder.is_dir():
            errors.append(f"src/{kind}: missing category directory")
            continue
        readme, index = folder / "README.md", folder / "INDEX.md"
        if (folder / "index.md").exists():
            errors.append(f"src/{kind}: remove legacy index.md; use INDEX.md")
        if not readme.is_file() or not index.is_file() or readme.is_symlink() or index.is_symlink():
            errors.append(f"src/{kind}: missing or unsafe category entrypoint")
            continue
        require_link(home_body, f"{kind}/INDEX.md", home)
        require_link(read_markdown(readme), "INDEX.md", readme)
        listing = read_markdown(index)
        for item in folder.rglob("*"):
            if item.is_symlink():
                errors.append(f"{item.relative_to(root)}: symlinks are not allowed")
        for item in sorted(folder.iterdir()):
            if item.name in {"README.md", "INDEX.md"}:
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
    skills = source / "skills"
    if skills.is_dir():
        for skill in sorted(skills.iterdir()):
            if skill.is_dir() and NAME.fullmatch(skill.name):
                errors.extend(_skill_errors(skill, root))
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
