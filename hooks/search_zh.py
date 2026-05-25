import re

import jieba


TAG_RE = re.compile(r"(<[^>]+>)")
HAN_RE = re.compile(r"[\u4e00-\u9fff]+")


def segment_chinese(text):
    def replace(match):
        words = [word for word in jieba.cut(match.group(0)) if word.strip()]
        return "\u200b".join(words)

    return HAN_RE.sub(replace, text)


def on_page_content(html, **kwargs):
    parts = TAG_RE.split(html)
    for index, part in enumerate(parts):
        if part.startswith("<") and part.endswith(">"):
            continue
        parts[index] = segment_chinese(part)
    return "".join(parts)
