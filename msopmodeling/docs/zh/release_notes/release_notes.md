# 版本说明

当前版本以 `msopmodeling -V`（或 `msopmodeling --version`）输出为准。

默认版本维护在 `pyproject.toml` 的 `[project] version`，`build.py` 自动读取，无需另外维护脚本中的默认版本。
发布构建可通过 `python build.py --version=x.y.z` 临时覆盖 wheel 版本，构建后自动恢复 `pyproject.toml`。

## 版本记录

<!-- 按版本倒序记录历史版本 -->
