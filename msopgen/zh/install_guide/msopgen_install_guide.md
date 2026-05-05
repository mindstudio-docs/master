# MindStudio Ops Generator安装指南

<br>

## 1. 安装说明

MindStudio Ops Generator（算子工程创建，msOpGen）是算子开发效率提升工具，提供模板工程生成能力，简化算子工程搭建并辅助算子测试验证。MindStudio Ops System Test（算子测试，msOpST）是算子开发效率提升工具，旨在真实的硬件环境中，对算子的输入输出进行测试，以验证算子的功能是否正确。本文主要介绍msOpGen和msOpST工具的安装方法。

- 使用CANN包安装：msKPP工具完整功能已集成在CANN包中，请参考《[CANN 快速安装](https://www.hiascend.com/cann/download)》安装昇腾NPU驱动和CANN软件（包含Toolkit和ops包），并配置环境变量。
- 源码编译安装：如需使用最新代码的功能，或对源码进行修改以增强功能，可下载本仓库代码，自行编译、打包工具并完成安装，具体请参见[源码编译安装](#2-源码编译安装)。

## 2. 源码编译安装

如需使用最新代码的功能，或对源码进行修改以增强功能，可下载本仓库代码，自行编译、打包工具并完成安装。

### 2.1 环境准备

请按照以下文档进行环境配置：《[算子工具开发环境安装指导](https://gitcode.com/Ascend/msot/blob/26.0.0/docs/zh/common/dev_env_setup.md)》。

- 克隆本仓库

    ```sh
    git clone https://gitcode.com/Ascend/msopgen.git
    ```

- 安装python依赖

    ```sh
    cd msopgen
    pip install -r requirements.txt
    ```

### 2.2 安装

#### 2.2.1 执行编译打包

生成的whl包位于output目录，包含mindstudio_opgen和mindstudio_opst两个whl包。

```py
python build.py
```

#### 2.2.2 安装whl包

```sh
cd output
pip install mindstudio_opgen-xxxxx.whl
pip install mindstudio_opst-xxxxx.whl
```

### 2.3 卸载

卸载操作可通过如下命令执行：

```sh
pip uninstall mindstudio_opgen
pip uninstall mindstudio_opst
```

### 2.4 升级

如需使用whl包替换运行环境原有已安装的whl包，执行如下安装操作：

```sh
pip install mindstudio_opgen-xxxxx.whl --force-reinstall
pip install mindstudio_opst-xxxxx.whl --force-reinstall
```

### 2.5 运行ut、st测试用例

`3.7 <= python版本要求 <=3.10`，`${INSTALL_DIR}`请替换为CANN软件安装后文件存储路径。例如，若安装的Ascend-cann-toolkit软件包，安装后文件存储路径示例为：`$HOME/Ascend/cann`。

```shell
source ${INSTALL_DIR}/set_env.sh
```

测试报告在output目录

```sh
python build.py test
```
