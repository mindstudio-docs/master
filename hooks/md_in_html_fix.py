"""
1. 为所有未标记 markdown="1" 的 <div> 自动注入该属性，
   配合 md_in_html 扩展让 div 内的 Markdown（如徽章）正常渲染。
2. 将 raw.gitcode.com/Ascend/{repo}/raw/master/{path} 外链替换为
   本地相对路径，解决 ReadTheDocs 无法加载防盗链图片的问题。
"""
import os
import re
from pathlib import Path

# 匹配 raw.gitcode.com 外链，提取 repo 和文件路径
_GITCODE_RAW = re.compile(
    r'https?://raw\.gitcode\.com/Ascend/([^/]+)/raw/[^/]+/(.+?)(?=["\'\s>])'
)


def _replace_gitcode_url(m, page_dir: Path, docs_dir: Path):
    repo, file_path = m.group(1), m.group(2)
    local_abs = docs_dir / repo / file_path
    if not local_abs.exists():
        return m.group(0)  # 本地不存在则保留原链接
    return os.path.relpath(local_abs, page_dir)


def on_page_markdown(markdown, page, config, **kwargs):
    # 1. 给 <div> 注入 markdown="1"
    markdown = re.sub(
        r'<div(?![^>]*\bmarkdown=)([^>]*)>',
        r'<div\1 markdown="1">',
        markdown,
    )

    # 2. 替换 raw.gitcode.com 外链为本地相对路径
    page_dir = Path(page.file.abs_src_path).parent
    markdown = _GITCODE_RAW.sub(
        lambda m: _replace_gitcode_url(m, page_dir, Path(config.docs_dir)),
        markdown,
    )

    return markdown
