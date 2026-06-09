# MindStudio Tools Extension Library 开发指南

<br>

## 1. 预备知识

请先阅读 [msTX 接口列表](../api_reference/README.md) 了解 msTX 提供的核心 API 及其功能简介。

## 2. 开发环境准备

请按照以下文档进行环境配置：《[算子工具开发环境安装指导](https://gitcode.com/Ascend/msot/blob/master/docs/zh/common/dev_env_setup.md)》。

编译需要额外安装 python3-dev（编译 Python 绑定所需头文件）：

```sh
# OpenEuler
yum install python3-devel

# Ubuntu
apt-get install python3-dev
```

> **注意：** 非 root 用户请在命令前加 `sudo`。

## 3. 编译打包

分为如下两种方式，优缺点如下：

| 方法 | 适用场景 | 优点 | 缺点 |
|------|---------|------|------|
| 一键式脚本 | 首次构建、CI/CD 流水线 | 零配置，一步到位 | 无法单独执行某一步骤 |
| 分步骤脚本 | 日常开发、增量编译 | 灵活，效率高 | 需要多步操作 |

### 3.1 方法一：一键式脚本

```shell
python build.py
```

### 3.2 方法二：分步骤脚本

#### 3.2.1 下载依赖

```shell
python download_dependencies.py
```

#### 3.2.2 启动编译

执行如下命令启动编译：

```shell
mkdir build
cd build
cmake .. && make -j$(nproc)
make install
```

编译完成后检查 `output/` 目录，文件生成时间已更新为当前编译时间，则表明编译已成功完成。

#### 3.2.3 编译结果说明

编译结果生成到 `output/` 目录下：

```text
output/
├── mstx/                         # 安装目录
│   └── lib64/                    # 动态库（libms_tools_ext.so、mstx.so）
└── mstx-<version>.whl            # Python 安装包
```

#### 3.2.4 清理/重新编译

删除构建目录，重新执行[第 3.2.2 节](#322-启动编译)：

```shell
rm -rf build
```

## 4. 执行UT测试

```shell
python build.py test
```

该命令会依次执行：下载测试依赖 → Debug 编译 C/CPP 测试目标 → 运行 C/C++ 单元测试 → 运行 Python 单元测试。

如果输出类似如下，且运行的用例数和通过用例数相同，即表示成功：

```text
[----------] 4 tests from CoreApi (8ms total)
```

```text
============= 4 passed in 0.03s =============
```

注：需要环境中提前安装 pytest 以执行 Python 测试。存在多个独立测试套，输出结果与样例类似时，即表示运行成功。

## 5. FAQ

### 5.1 编译报错：找不到 Python.h

```text
fatal error: Python.h: No such file or directory
```

**解决：** 安装 Python 开发包：

```sh
# OpenEuler
yum install python3-devel

# Ubuntu
apt-get install python3-dev
```

### 5.2 测试报错：pytest 未找到

```text
pytest: command not found
```

**解决：** 安装 pytest：

```sh
pip3 install pytest
```

### 5.3 output 文件夹下只有 whl 安装包，没有动态链接库

使用一键式脚本 `python build.py` 会同时生成 whl 包和安装动态库到 `output/mstx/lib64/`。若只看到 whl 包，通常是因为分步骤编译时只执行了 `cmake .. && make`，遗漏了 `make install`。在 `build/` 目录下补执行 `make install` 即可。
