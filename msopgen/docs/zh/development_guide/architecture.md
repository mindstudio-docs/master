# msOpGen 架构设计说明书

<br>

## 1 项目概述

### 1.1 背景与动机

算子开发涉及大量框架代码（Host 侧原型注册、Tiling 策略、Kernel 侧算子实现、编译配置等），手动搭建算子工程繁琐且易出错。msOpGen 通过算子原型定义 JSON 文件自动生成完整的算子工程框架，使开发者聚焦于核心算法逻辑。

### 1.2 功能清单

| 类型 | 功能 | 描述 |
|-----|------|------|
| 业务功能 | 算子工程生成 | 基于 JSON 原型定义生成完整的 AscendC/TBE/AI CPU 算子工程 |
| 业务功能 | 多框架适配 | 支持 TensorFlow、PyTorch、MindSpore、ONNX 框架 |
| 业务功能 | 算子追加 | 支持在已有算子工程中追加新算子（`-m 1` 模式） |
| 业务功能 | 仿真流水图解析 | 解析性能仿真 dump 数据，生成可在 Chrome tracing 中查看的流水图 |
| 业务功能 | 编译部署集成 | 生成 build.sh 编译脚本和 .run 算子部署包 |
| 配套工具 | ST 测试 | msOpST 工具自动生成测试用例并在硬件环境中执行 |

---

## 2 设计目标

| 设计目标 | 描述 |
|---------|------|
| **工程完整性** | 生成的工程可直接编译部署，无需手动补充框架代码 |
| **多框架覆盖** | 统一 JSON 接口适配多种 AI 框架，降低学习成本 |
| **编译可配置** | 通过 CMakePresets.json 灵活配置编译选项、芯片型号、发布方式 |
| **命令行易用性** | 参数设计清晰直观，支持默认值和自动推断 |

---

## 3 架构总览

### 3.1 系统架构图

```text
┌──────────────────────────────────────────────┐
│                 CLI 入口层                     │
│   msopgen gen    msopgen sim    msopst         │
└──────────────────┬───────────────────────────┘
                   │
┌──────────────────▼───────────────────────────┐
│                核心引擎层                       │
│  ┌──────────┐  ┌──────────┐  ┌────────────┐  │
│  │ JSON     │  │ Template │  │ Dump       │  │
│  │ Parser   │  │ Engine   │  │ Analyzer   │  │
│  └──────────┘  └──────────┘  └────────────┘  │
│  ┌──────────┐  ┌──────────────────────────┐  │
│  │ ST Test  │  │ Project Builder          │  │
│  │ Generator│  │ (CMake/编译集成)          │  │
│  └──────────┘  └──────────────────────────┘  │
└──────────────────┬───────────────────────────┘
                   │
┌──────────────────▼───────────────────────────┐
│                输出层                          │
│  算子工程目录 / .run 部署包 / trace.json /    │
│  ST 用例 .json / st_report.json              │
└──────────────────────────────────────────────┘
```

### 3.2 模块划分

| 模块 | 职责 | 输入 | 输出 |
|------|------|------|------|
| JSON Parser | 解析算子原型定义文件，校验字段合法性 | `*.json` 原型定义 | 结构化算子描述 |
| Template Engine | 基于算子描述和芯片型号生成工程模板 | 算子描述 + soc_version | 完整算子工程目录 |
| Dump Analyzer | 解析性能仿真 dump 数据 | dump 数据文件 | trace.json 流水图 |
| Project Builder | 生成 CMakeLists.txt、CMakePresets.json、build.sh | 算子描述 + 编译选项 | 可编译的工程 |
| ST Test Generator | 解析 Host 侧源码生成 ST 测试用例 | `op_host/*.cpp` | `*_case.json` |
| ST Test Runner | 执行硬件测试并生成报表 | `*_case.json` + soc | `st_report.json` |

### 3.3 数据流

```text
算子原型 JSON ──→ [JSON Parser] ──→ 算子描述结构体
                                       │
                                [Template Engine] ──→ 算子工程目录
                                       │
                                [用户编写 Kernel 实现]
                                       │
                              [build.sh 编译] ──→ .run 部署包
                                       │                               
                                [msopst create]                       
                                       │                                     
                                ST 用例 .json                          
                                [msopst run]                       
                                       │                                 
                                st_report.json                           
```

---

## 4 关键技术点

### 4.1 模板替换机制

msOpGen 根据 JSON 原型定义中的算子名称、输入输出参数类型和格式，使用模板引擎自动替换 C++ 源码模板中的占位符，生成 Host 侧（原型注册、Shape 推导、Tiling 实现、信息库）和 Kernel 侧（算子计算逻辑）的框架代码。

### 4.2 命名规则

算子类型（OpType）与文件名、核函数名之间存在严格的转换规则：
- 大驼峰（PascalCase）→ 下划线命名（snake_case）
- 例如：`AddCustom` → `add_custom.cpp` / `add_custom`

### 4.3 发布模式

- **源码发布**：保留 Kernel 源码 .cpp，支持在线编译和 ATC 模型转换
- **二进制发布**：编译生成 .o 和 .json 信息文件，直接调用算子二进制

---

## 5 目录结构

```text
├── example/       // 工具样例
├── docs/          // 项目文档
├── msopgen/       // msopgen 源码目录
├── tools/msopst/  // msopst 代码目录
├── test/
│   ├── msopgen/   // msopgen 单元测试
│   └── msopst/    // msopst 单元测试
├── output/        // whl 包输出、测试报告
├── setup.py       // msopgen whl 构建脚本
└── build.py       // 构建入口脚本
```

## 6 msOpGen 类图

![alt text](../figures/msOpGenClass.png)
