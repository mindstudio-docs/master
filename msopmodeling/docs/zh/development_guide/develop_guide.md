# 算子性能建模工具开发指南

<br>

## 1. 预备知识

请参考 [《msOpModeling 开发指南》](../development_guide/develop_guide.md) 学习代码框架及核心流程介绍。

---

## 2. 开发环境准备

### 2.1 环境要求

- Python ≥ 3.10
- Git
- pip ≥ 23.0

### 2.2 克隆代码仓库

```shell
git clone https://gitcode.com/Ascend/msopmodeling.git
cd msopmodeling
```

### 2.3 创建并激活虚拟环境（可选）

**Linux / macOS：**

```shell
python3 -m venv .venv
source .venv/bin/activate
```

**Windows：**

```shell
python -m venv .venv
.venv\Scripts\activate
```

### 2.4 安装开发依赖

```shell
pip install -e ".[dev]" -i https://mirrors.aliyun.com/pypi/simple/
```

>[!NOTE] 说明
> `-e` 参数以可编辑模式安装，修改源码后无需重新安装即可生效。`.[dev]` 同时安装测试、构建等开发额外依赖。

---

## 3. 编译打包

```shell
python build.py
```

构建成功后，wheel 包生成至 `dist/` 目录：

```text
dist/
└── msopmodeling-x.x.x-py3-none-any.whl
```

---

## 4. 执行UT测试

```shell
python build.py test
```

输出类似如下，测试通过数与运行数相同即表示成功：

```text
============================== test session starts ==============================
...
========================= 42 passed in 3.21s =================================
```

如需单独执行某个测试文件：

```shell
python -m pytest tests/ut/app/service/test_prediction_service.py -v
```

---

## 5. 项目结构说明

```text
msopmodeling/
├── src/
│   ├── main.py                        # CLI 入口
│   ├── app/                           # 应用层（CLI解析、配置加载、结果输出）
│   └── tilesim/                       # 核心引擎
│       ├── api/                       # 对外 API 接口
│       │   └── operator_api/          # 算子级预测入口
│       ├── core/                      # 核心实现
│       │   ├── frontend/              # 前端：DSL 解析与 IR 构建
│       │   ├── backend/               # 后端：性能建模与评估
│       │   ├── pipeline/              # 流水线：端到端处理流程
│       │   ├── common/                # 公共定义（枚举、注册中心）
│       │   └── config/                # 芯片配置文件（arc_config/）
│       ├── ops/                       # 算子模型实现
│       │   ├── eng/                   # 工程模式算子
│       │   └── theo/                  # 理论模式算子
│       └── tilesim/                   # 推荐的公开 Python API
├── tests/                             # 宿主应用与集成测试
├── docs/                              # 用户文档
├── build.py                           # 构建脚本
├── download_dependencies.py           # 依赖下载脚本
├── dependencies.json                  # 依赖声明
└── pyproject.toml                     # 项目配置
```

---

## 6. FAQ

### 6.1 执行测试时报 `ModuleNotFoundError: No module named 'core'`

**原因：** 仓库统一从 `src/` 导入命名空间包（如 `tilesim._internal.core`、`msopmodeling._internal.app`）。根目录 `pyproject.toml` 的 `[tool.pytest.ini_options]` 声明了 `pythonpath = ["src"]`，pytest 会自动完成注入。

**解决方案：** 确认从**项目根目录**运行 pytest，不要 `cd` 进子目录后运行，否则 pytest 不会读取根目录的配置：

```shell
# 正确：从项目根目录运行
python -m pytest tests/ut/ -v --tb=short
```

### 6.2 `python build.py` 提示 `hatch` 未安装

**解决方案：** 手动安装 hatch：

```shell
pip install hatch -i https://mirrors.aliyun.com/pypi/simple/
```

### 6.3 Windows 下激活虚拟环境失败

**解决方案：** 以管理员权限运行 PowerShell，先设置执行策略：

```shell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.venv\Scripts\activate
```
