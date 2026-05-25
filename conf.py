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
master_doc = "index"

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
    "README.md",
]

suppress_warnings = [
    "myst.header",
    "myst.xref_missing",
    "toc.not_included",
    "toc.not_readable",
    "image.not_readable",
    "docutils",
    "misc.highlighting_failure",
]


def drop_directory_images(app, env):
    for filename in list(env.images.keys()):
        if (app.srcdir / filename).is_dir():
            env.images.pop(filename, None)


def setup(app):
    app.connect("env-updated", drop_directory_images)
