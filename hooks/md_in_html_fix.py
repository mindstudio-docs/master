"""Small Markdown normalization hooks used by the aggregated MkDocs site.

The source repositories are synchronized periodically, so fixes that only
affect site rendering should stay in this root-level hook instead of editing
files under each tool directory.
"""
import posixpath
import re
from pathlib import Path

_GITCODE_RAW = re.compile(
    r'https?://raw\.gitcode\.com/Ascend/([^/]+)/raw/[^/]+/(.+?)(?=["\'\s>])'
)
_DIV_WITH_MARKDOWN_RE = re.compile(
    r'<div(?![^>]*\bmarkdown=)([^>]*)>\s*(?=(?:\n\s*)?(?:[#*>-]|\[|!\[))'
)


def _replace_gitcode_url(m, page_dir: Path, docs_dir: Path):
    repo, file_path = m.group(1), m.group(2)
    local_abs = docs_dir / repo / file_path
    if not local_abs.exists():
        return m.group(0)

    return posixpath.relpath(
        local_abs.resolve().as_posix(),
        page_dir.resolve().as_posix(),
    )


def _should_enable_md_in_html(page):
    return Path(page.file.src_path).name == "README.md"


def on_page_markdown(markdown, page, config, **kwargs):
    if _should_enable_md_in_html(page):
        markdown = _DIV_WITH_MARKDOWN_RE.sub(r'<div\1 markdown="1">', markdown)

    page_dir = Path(page.file.abs_src_path).parent
    markdown = _GITCODE_RAW.sub(
        lambda m: _replace_gitcode_url(m, page_dir, Path(config.docs_dir)),
        markdown,
    )

    return markdown
