"""
为所有页面中未标记 markdown="1" 的 <div> 自动注入该属性，
配合 md_in_html 扩展让 div 内的 Markdown（如徽章）正常渲染。
"""
import re


def on_page_markdown(markdown, **kwargs):
    return re.sub(
        r'<div(?![^>]*\bmarkdown=)([^>]*)>',
        r'<div\1 markdown="1">',
        markdown,
    )
