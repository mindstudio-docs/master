import re
from pathlib import Path

import jieba


TAG_RE = re.compile(r"(<[^>]+>)")
HAN_RE = re.compile(r"[\u4e00-\u9fff]+")


def segment_chinese(text):
    def replace(match):
        value = match.group(0)
        words = [word for word in jieba.cut(value) if word.strip()]
        chars = list(value)
        tokens = [value, *words, *chars]
        return "\u200b".join(dict.fromkeys(tokens))

    return HAN_RE.sub(replace, text)


def on_page_content(html, **kwargs):
    parts = TAG_RE.split(html)
    for index, part in enumerate(parts):
        if part.startswith("<") and part.endswith(">"):
            continue
        parts[index] = segment_chinese(part)
    return "".join(parts)


def on_post_build(config, **kwargs):
    worker_path = Path(config["site_dir"]) / "search" / "worker.js"
    if not worker_path.exists():
        return

    worker = worker_path.read_text(encoding="utf-8")
    marker = "function normalizeChineseQuery"
    if marker not in worker:
        worker = worker.replace(
            "function search (query) {",
            """
function normalizeChineseQuery(query) {
  return query.replace(/[\\u4e00-\\u9fff]+/g, function(value) {
    return value + " " + value.split("").join("\\u200b");
  });
}

function search (query) {""".lstrip(),
        )
        worker = worker.replace(
            "var results = index.search(query);",
            "var results = index.search(normalizeChineseQuery(query));",
        )
        worker = worker.replace(
            "index = lunr(function () {",
            """index = lunr(function () {
      this.pipeline.reset();
      this.searchPipeline.reset();""",
        )
        worker_path.write_text(worker, encoding="utf-8")
