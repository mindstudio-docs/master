# MindStudio Sanitizer安装指南

# 安装说明
MindStudio Sanitizer（算子异常检测，msSanitizer）是一种基于昇腾AI处理器AI处理器SoCNPU IP加速器的异常检测工具，包含了单算子开发场景下的内存检测、竞争检测、未初始化检测和同步检测四个子功能。本文主要介绍msSanitizer工具的安装方法。  

# 安装前准备
## 更新依赖子仓代码

为了避免依赖下载过程中反复输入密码，可通过如下命令配置git保存用户密码：
```
git config --global credential.helper store
```

## 项目构建

开始构建之前，需要确保已安装编译器bisheng，并且其可执行文件所在路径在环境变量$PATH中，这里要求bisheng的版本信息应该是2025-11-25T20:00:35+08:00 clang version 15.0.5 (clang-5c68a1cb1231 flang-5c68a1cb1231)或更新的版本；
如果cann算子工具包，可在工具包安装路径下执行source set_env.sh，这里注意的是需要安装8.5.0或更高的cann版本。

- 命令行方式
    通过以下脚本下载项目构建依赖的子仓库，并更新依赖到最新代码：
    ```
    python download_dependencies.py
    ```

    然后通过如下命令构建run包：
    ```
    mkdir build
    cd build
    cmake ../cmake && make -j8  # 如果只做编译，不打run包，这里需要执行的是cmake ..  && make -j8 install 
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
    make -j8 mssanitizer_test
    ./test/ut/mssanitizer_test
    ```

- 一键式脚本方式
    也可以调用一键式脚本完成UT构建依赖仓下载和UT测试流程：
    ```
    python build.py test
    ```

# 安装步骤
## run包安装与卸载

安装前需给run包添加可执行权限：
```
chmod +x Ascend-mindstudio-sanitizer-*.run
```

### 安装
构建产物run包默认在output目录下，将此run包拷贝到运行环境中，执行如下安装操作：
```
./Ascend-mindstudio-sanitizer-*.run --run  # 如果环境中配置过ASCEND_HOME_PATH变量，则会安装到$ASCEND_HOME_PATH目录下；否则会默认安装到$HOME/Ascend目录下；
如果要指定路径安装，则需添加--install-path选项，如./Ascend-mindstudio-sanitizer-*.run  --install-path=./xxx --run ，则将此run包安装到当前目录下的xxx目录下。
```
安装完成后，需设置环境变量，以确保能正常运行算子工具：
```
export ASCEND_HOME_PATH=$HOME/Ascend  # 或 export ASCEND_HOME_PATH=$PWD/xxx  (指定路径安装场景)
export PATH=$ASCEND_HOME_PATH/bin:$PATH
export LD_LIBRARY_PATH=$ASCEND_HOME_PATH/lib64:$LD_LIBRARY_PATH
```

### 卸载
卸载则通过如下命令卸载：
```
./Ascend-mindstudio-sanitizer-*.run --uninstall  # 默认会在$HOME/Ascend目录下卸载operator-tools，如果要前面安装时通过--install-path指定路径安装，则卸载时也需添加--install-path选项，如./Ascend-mindstudio-sanitizer-*.run  --install-path=./xxx --uninstall
```
如果run包已经删除，则可通过如下命令卸载：
```
bash $HOME/Ascend/share/info/mindstudio-sanitizer/script/uninstall.sh 或 bash ./xxx/share/info/mindstudio-sanitizer/script/uninstall.sh （制定路径安装场景）
```

### 升级
如需使用构建产物run包替换运行环境原有已安装的mindstudio-sanitizer包，执行如下安装操作：
```
./Ascend-mindstudio-sanitizer-*.run --run  # 默认会升级到$HOME/Ascend目录下的mindstudio-sanitizer，如果老版本是通过指定路径安装的，则需添加--install-path选项，如./Ascend-mindstudio-sanitizer-*.run  --install-path=./xxx --run ,其中xxx是老版本的安装路径
```
安装过程中，会提示是否替换原有安装包：
do you want to overwrite current installation? [y/n]
输入"y"，则安装包会自动完成升级操作。
