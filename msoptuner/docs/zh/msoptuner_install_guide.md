# MindStudio Ops Tuner安装指南

# 安装说明
MindStudio Ops Tuner（算子Tiling寻优，msOpTuner）是一款用于 CATLASS 模板库算子 Tiling 参数寻优的工具，支持用户自定义搜索空间，能够实例化搜索空间内的所有算子，并批量完成在板性能测试，为算子 Tiling 参数的寻优提供参考依据。本文主要介绍msOpTuner工具的安装方法。  


# 安装前准备

**配置用户名和密钥**

为了避免依赖下载过程中反复输入密码，可通过如下命令配置git保存用户密码：
```
git config --global credential.helper store
```

## 环境准备
- Ascend NPU 910B硬件环境

开始构建之前，需要确保已安装bisheng编译器，并且其可执行文件所在路径在环境变量$PATH中(如果已安装cann算子工具包，可在工具包安装路径下执行source set_env.sh).

```shell
source /path/to/Ascend/cann/set_env.sh
```


# 安装步骤
## 项目构建

- 命令行方式
  执行如下命令下载项目构建依赖的子仓库，并更新依赖到最新代码：
  ```shell
  python download_dependencies.py
  ```
  执行如下命令，构建软件包。

    ```shell
    mkdir build && cd build
    cmake .. -DBUILD_TESTS=ON
    make -j$(nproc)
    ```

- 一键式脚本方式  
  通过一键式脚本构建软件包。

    ```shell
    python build.py
    ```

    > [!NOTE]  说明  
    > 如果本地更改了依赖子仓库中的代码，不想构建过程中执行更新动作，可以执行`python build.py local`。

## 测试

- 命令行方式
    通过以下脚本下载UT构建依赖的子仓库，并更新依赖到最新代码：

    ```shell
    python download_dependencies.py test
    ```

    然后通过如下命令构建并执行UT测试：

    ```shell
    mkdir build && cd build
    cmake .. -DBUILD_TESTS=ON
    make -j$(nproc)
    cd ../test/
    python test_mstuner.py
    ```

- 一键式脚本方式
    调用一键式脚本完成UT构建依赖仓下载和UT测试流程：
    ```shell
    python build.py test
    ```
