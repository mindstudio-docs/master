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


NON_TOOL_DIRS = {"assets", "hooks", "site"}


def on_config(config):
    docs_dir = Path(config["docs_dir"])

    # 自动发现所有工具目录（排除隐藏目录和非工具目录）
    discovered = {
        d.name
        for d in docs_dir.iterdir()
        if d.is_dir() and not d.name.startswith(".") and d.name not in NON_TOOL_DIRS
    }

    # 按 TOOL_ORDER 排序，未列出的目录追加到末尾（字母序）
    ordered = [t for t in TOOL_ORDER if t in discovered]
    ordered += sorted(discovered - set(TOOL_ORDER))

    tools = []
    for tool in ordered:
        tool_dir = docs_dir / tool
        nav_items = build_directory_nav(tool_dir, docs_dir)
        if nav_items:
            tools.append({tool: nav_items})

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

    for child in sorted(directory.iterdir(), key=sort_key):
        if should_skip_child(child):
            continue
        if child.is_dir():
            child_items = build_directory_nav(child, docs_dir)
            if child_items:
                items.append({child.name: child_items})
        elif child.suffix.lower() == ".md" and child.name not in {"README.md", "index.md"}:
            items.append({get_title(child): to_nav_path(child, docs_dir)})

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
