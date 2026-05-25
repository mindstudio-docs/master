project = "MindStudio 统一资料"
author = "MindStudio"
language = "zh_CN"

extensions = [
    "myst_parser",
]

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}
master_doc = "README"

html_theme = "sphinx_rtd_theme"
html_theme_options = {
    "collapse_navigation": False,
    "navigation_depth": 3,
    "titles_only": False,
}

myst_heading_anchors = 3

exclude_patterns = [
    "_build",
    "site",
    ".git",
    ".idea",
    ".devin",
    ".venv",
    ".venv/**",
    ".sphinx*",
    ".readthedocs.yaml",
    "mkdocs.yml",
    "requirements.txt",
    "*/docs/**",
    "*/src/**",
    "*/example/**",
    "*/examples/**",
    "*/test/**",
    "*/tests/**",
]

suppress_warnings = [
    "myst.header",
    "myst.xref_missing",
    "toc.not_included",
    "misc.highlighting_failure",
]
