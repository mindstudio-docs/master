# 算子性能建模工具安装指南

<br>

## 1. 简介

本文档介绍 **msOpModeling**（昇腾算子性能建模工具）的安装方法，提供两种安装方式：
- **pip 安装**：推荐普通用户使用，快速便捷
- **源码安装**：推荐开发者使用，便于二次开发和调试

---

## 2. 环境要求

- **Python 版本**：≥ 3.10
- **操作系统**：Linux / macOS / Windows
- **网络要求**：可访问 PyPI 镜像源（用于下载依赖包）

---

## 3. pip 安装（推荐）

### 3.1 安装命令

```shell
pip install msopmodeling -i https://mirrors.aliyun.com/pypi/simple/
```

### 3.2 验证安装

```shell
msopmodeling --help
```

成功安装后，将显示命令行帮助信息。

---

## 4. 源码安装（开发者）

适用于需要修改源码、参与贡献或调试的场景。

### 4.1 克隆代码仓库

```shell
git clone https://gitcode.com/Ascend/msopmodeling.git
cd msopmodeling
```

### 4.2 创建虚拟环境

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

### 4.3 安装依赖

```shell
pip install -e ".[dev]" -i https://mirrors.aliyun.com/pypi/simple/
```

**参数说明：**
- `-e`：以可编辑模式安装，修改源码后无需重新安装
- `.[dev]`：安装开发依赖（包含测试、构建等额外工具）

### 4.4 验证安装

```shell
msopmodeling --help
```

---

## 5. 常见问题

### Q1：安装时提示 Python 版本不满足要求？

**解决方案：** 检查当前 Python 版本，确保 ≥ 3.10：
```shell
python --version
```

如版本过低，请升级 Python 或使用 pyenv 管理多版本。

### Q2：pip 安装速度慢或超时？

**解决方案：** 使用国内镜像源加速：
```shell
pip install msopmodeling -i https://mirrors.aliyun.com/pypi/simple/
# 其他可选镜像：
# -i https://pypi.tuna.tsinghua.edu.cn/simple/
# -i https://pypi.mirrors.ustc.edu.cn/simple/
```

### Q3：源码安装后修改代码未生效？

**解决方案：** 确认可编辑模式安装正确：
```shell
pip list | grep msopmodeling
```

应显示类似 `msopmodeling  x.x.x  /path/to/msopmodeling (editable)`。

### Q4：Windows 下激活虚拟环境失败？

**解决方案：** 以管理员权限运行 PowerShell，然后执行：
```shell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.venv\Scripts\activate
```
