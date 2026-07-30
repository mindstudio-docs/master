# MindStudio msOpGen 开发环境搭建和UT方法

<br>

## 1. 预备知识

进行 msOpGen 开发前，需了解以下基础知识：

- **Python 项目结构**：msOpGen 是基于 Python 的命令行工具，源码位于 `msopgen/` 目录，使用 `setuptools` 构建 whl 包。
- **工具组成**：msOpGen 负责算子工程生成（`msopgen gen`）和仿真流水图解析（`msopgen sim`）；msOpST 负责 ST 测试用例生成与执行（`msopst create/run`）。
- 详细的架构设计和模块划分请参考[《msOpGen架构设计文档》](./architecture.md)。

## 2. 开发环境准备

按照《[msOpGen工具安装指南 安装指南 — 编译环境准备](../install_guide/msopgen_install_guide.md#231-环境准备)》章节完成编译和测试环境的搭建。

> **说明：** 环境镜像的构建方法及配套软件版本由 MindStudio 统一镜像制作指南维护，本仓库不重复定义。

## 3. 一键式构建

```shell
python3 build.py
```

生成的 whl 包位于 `artifacts/` 目录，包含 `mindstudio_opgen` 和 `mindstudio_opst` 两个包。

## 4. 项目目录结构

```text
├── msopgen/          // msopgen 源码目录（核心引擎）
├── tools/msopst/     // msopst 源码目录（ST 测试工具）
├── test/
│   ├── test_msopgen/ // msopgen 单元测试
│   └── test_msopst/  // msopst 单元测试
├── example/          // 工具样例
├── docs/             // 项目文档
├── setup.py          // msopgen whl 包构建脚本
├── build.py          // 构建入口脚本
└── requirements.txt  // Python 依赖库
```

## 5. UT 测试

```shell
python3 build.py test
```

### 5.1 测试覆盖范围

UT 测试覆盖以下核心功能：
- 算子工程模板生成（`msopgen gen`）
- 仿真流水图解析（`msopgen sim`）
- ST 测试用例生成（`msopst create`）
- ST 测试用例执行（`msopst run`）


## 6. 代码规范

- 新增功能需同步编写 UT 测试用例
- 公共函数和类需添加 docstring 文档字符串
