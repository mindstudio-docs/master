# 贡献指南

<br>

## 1. 贡献流程和规范

参与开发前，请熟悉贡献流程及相关规范，详细请详见 [《贡献流程和规范说明》](https://gitcode.com/Ascend/msot/blob/master/docs/zh/common/contribute_workflow.md)。

## 2. 开发指南

### 2.1 代码架构说明

介绍工具的整体架构、代码框架及核心设计思路，请参见 [《msOpModeling 开发指南》](../development_guide/develop_guide.md)。

### 2.2 开发环境与编译测试

介绍开发环境搭建、代码编译及测试方法等，详细请参见 [《msOpModeling 开发指南》](../development_guide/develop_guide.md)。

## 3. 版本号约定

默认版本维护在 `pyproject.toml` 的 `[project] version`，并保持 `build.py` 的 `--version` 默认值一致。
发布构建可通过 `python build.py --version=...` 覆盖 wheel 版本。
文档和 release notes 引用当前版本时，以 `msopmodeling -V` / `msopmodeling --version` 输出为准。
