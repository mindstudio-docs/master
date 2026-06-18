# MindStudio Ops Common构建指南

# 构建说明
MindStudio Ops Common（算子工具基础组件，msOpCom）是算子工具基础组件，对于昇腾产品工具而言，在开发维测环境下，需要将运行时进行改变，以支持"隐式"行为的隐藏。本文主要介绍msOpCom组件的构建方法。


# 构建前准备
## 配置用户名和密钥

为了避免依赖下载过程中反复输入密码，可通过如下命令配置git保存用户密码：
```
git config --global credential.helper store
```

# 构建步骤
## 项目构建
开始构建之前，需要确保已安装bisheng编译器，并且其可执行文件所在路径在环境变量$PATH中(如果已安装cann算子工具包，可在工具包安装路径下执行source set_env.sh).

- 命令行方式
    通过以下脚本下载项目构建依赖的子仓库，并更新依赖到最新代码：
    ```
    python download_dependencies.py
    ```

    然后通过如下命令构建：
    ```
    mkdir build
    cd build
    cmake ..
    make -j8 && make install
    ```
- 一键式脚本方式
    调用一键式脚本完成依赖仓下载和构建流程：
    ```
    python build.py
    ```

    > [!NOTE] 说明
    > 如果本地更改了依赖子仓中的代码，不想构建过程中执行更新动作，可以执行 `python build.py local`

## UT测试

- 命令行方式
    通过以下脚本下载UT构建依赖的子仓库，并更新依赖到最新代码：

    ```
    python download_dependencies.py test
    ```

    然后通过如下命令构建并执行UT测试：

    ```
    mkdir build_ut
    cd build_ut
    cmake .. –DBUILD_TEST=on
    make -j8 injectionTest
    export LD_LIBRARY_PATH=$PWD/test/stub:$LD_LIBRARY_PATH
    ./test/injectionTest
    ```

- 一键式脚本方式
    调用一键式脚本完成UT构建依赖仓下载和UT测试流程：
    ```
    python build.py test
    ```
