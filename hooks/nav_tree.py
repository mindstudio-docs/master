import re
from pathlib import Path


TOOL_ORDER = [
    "msdebug",
    "msinsight",
    "msit",
    "mskl",
    "mskpp",
    "msmemscope",
    "msmodeling",
    "msmodelslim",
    "msmonitor",
    "msopcom",
    "msopgen",
    "msopmodeling",
    "msopprof",
    "msoptuner",
    "msot",
    "msprobe",
    "msprof",
    "msprof-analyze",
    "mspti",
    "mssanitizer",
    "msserviceprofiler",
    "mstt",
    "mstx",
]

TITLE_RE = re.compile(r"^#\s+(.+?)\s*$")
MARKDOWN_LINK_RE = re.compile(r"!?\[([^\]]*)\]\([^)]+\)")
INLINE_MARKUP_RE = re.compile(r"[`*_]+")


def on_config(config):
    docs_dir = Path(config["docs_dir"])
    tools = []

    for tool in TOOL_ORDER:
        tool_dir = docs_dir / tool
        if tool_dir.is_dir():
            tools.append({tool: build_directory_nav(tool_dir, docs_dir)})

    config["nav"] = [
        {"Home": "README.md"},
        {"Tools": tools},
    ]

    return config


def build_directory_nav(directory, docs_dir):
    items = []
    readme = directory / "README.md"

    if readme.is_file():
        items.append({"Overview": to_nav_path(readme, docs_dir)})

    index = directory / "index.md"
    if index.is_file():
        items.append({get_title(index): to_nav_path(index, docs_dir)})

    for child in sorted(directory.rglob("*.md"), key=lambda path: path.as_posix().lower()):
        if child.name in {"README.md", "index.md"}:
            continue
        items.append({get_flat_title(child, directory): to_nav_path(child, docs_dir)})

    return items


def should_skip_child(path):
    return path.name.startswith(".") or path.name in {"README.md", "index.md"}


def sort_key(path):
    priority = 0 if path.is_dir() else 1
    return (priority, path.name.lower())


def to_nav_path(path, docs_dir):
    return path.relative_to(docs_dir).as_posix()


def get_title(path):
    try:
        for line in path.read_text(encoding="utf-8").splitlines()[:80]:
            match = TITLE_RE.match(line)
            if match:
                return clean_title(match.group(1))
    except UnicodeDecodeError:
        pass

    return path.stem


def clean_title(title):
    title = MARKDOWN_LINK_RE.sub(r"\1", title)
    title = INLINE_MARKUP_RE.sub("", title)
    return title.strip() or "Untitled"


def get_flat_title(path, tool_dir):
    title = get_title(path)
    relative_parent = path.parent.relative_to(tool_dir).as_posix()

    if relative_parent == ".":
        return title

    return f"{relative_parent} / {title}"
