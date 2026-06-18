# **MindStudio Ops Generator快速入门**



## 简介<a id="section040515232197"></a>

msOpGen工具用于算子开发时，可生成自定义算子工程，方便用户专注于算子的核心逻辑和算法实现，而无需花费大量时间在项目搭建、编译配置等重复性工作上，从而大大提高了开发效率。

## 环境准备<a id="section81731814530"></a>

- 准备Atlas A2 训练系列产品/Atlas A2 推理系列产品的服务器，并安装对应的驱动和固件，具体安装过程请参见《[CANN 软件安装指南](https://www.hiascend.com/document/detail/zh/CANNCommunityEdition/83RC1/softwareinst/instg/instg_0000.html)》中的“安装NPU驱动和固件”章节。
- 安装配套版本的CANN Toolkit开发套件包和ops算子包并配置CANN环境变量，具体请参见《[CANN 软件安装指南](https://www.hiascend.com/document/detail/zh/CANNCommunityEdition/83RC1/softwareinst/instg/instg_0000.html)》。
- 若要使用MindStudio Insight进行查看时，需要单独安装MindStudio Insight软件包，具体下载链接请参见《[MindStudio Insight工具用户指南](https://www.hiascend.com/document/detail/zh/mindstudio/82RC1/GUI_baseddevelopmenttool/msascendinsightug/Insight_userguide_0002.html)》的“安装与卸载”章节。

> [!NOTE] 说明  
> 在安装昇腾AI处理器的服务器执行`npu-smi info`命令进行查询，获取**Chip Name**信息。实际配置值为AscendChip Name，例如**Chip Name**取值为xxxyy，实际配置值为Ascendxxxyy。当Ascendxxxyy为代码样例路径时，需要配置Ascendxxxyy。

## 操作步骤<a id="section17986111619274"></a>

1. 生成算子目录。
    1. 把算子定义的AddCustom.json文件放到工作目录当中，json文件的配置参数详细说明请参考《[MindStudio Ops Generator工具用户指南](./msopgen_user_guide.md)》中的“算子工程创建功能介绍>使用示例>创建算子工程>表 json文件配置参数说明”。

        ```json
        [
            {
                "op": "AddCustom",
                "language": "cpp",
                "input_desc": [
                    {
                        "name": "x",
                        "param_type": "required",
                        "format": [
                            "ND"
                        ],
                        "type": [
                            "float16"
                        ]
                    },
                    {
                        "name": "y",
                        "param_type": "required",
                        "format": [
                            "ND"
                        ],
                        "type": [
                            "float16"
                        ]
                    }
                ],
                "output_desc": [
                    {
                        "name": "z",
                        "param_type": "required",
                        "format": [
                            "ND"
                        ],
                        "type": [
                            "float16"
                        ]
                    }
                ]
            }
        ]
        ```

    2. 执行以下命令，生成算子开发工程，参数说明请参见《[MindStudio Ops Generator工具用户指南](./msopgen_user_guide.md)》中的“算子工程创建功能介绍>使用示例>创建算子工程>表 创建算子工程参数说明”。

        ```sh
        msopgen gen -i AddCustom.json -f tf -c ai_core-ascendxxxyy -lan cpp -out AddCustom  # xxxyy为用户实际使用的具体芯片类型
        ```

    3. 执行以下命令，查看生成目录。

        ```sh
        tree -C -L 2 AddCustom/
        ```

    4. <span id="li20608132944115"></a>在指定目录下生成的算子工程目录。

        ```tex
        AddCustom
        ├── build.sh               // 编译入口脚本
        ├── cmake
        ├── CMakeLists.txt         // 算子工程的CMakeLists.txt
        ├── CMakePresets.json      // 编译配置项
        ├── framework             // 算子插件实现文件目录，单算子模型文件的生成不依赖算子适配插件，无需关注
        │   ├── CMakeLists.txt
        │   └── tf_plugin
        ├── op_host                // Host侧实现文件
        │   ├── add_custom.cpp       // 算子原型注册、shape推导、信息库、tiling实现等内容文件
        │   ├── add_custom_tiling.h  // 算子tiling定义文件
        │   └── CMakeLists.txt
        ├── op_kernel                 // Kernel侧实现文件
        │   ├── add_custom.cpp      // 算子代码实现文件 
        │   └── CMakeLists.txt
        └── scripts                 // 自定义算子工程打包相关脚本所在目录
        ```

2. 单击[Link](https://gitee.com/ascend/samples/tree/master/operator/ascendc/0_introduction/1_add_frameworklaunch/AddCustom)，获取算子核函数开发和Tiling实现的代码样例。执行以下命令，将样例目录中的算子实现文件移动至msOpGen步骤1[第四点](#li20608132944115)生成的目录中。

   ```sh
   cp -r ${git_clone_path}/samples/operator/ascendc/0_introduction/1_add_frameworklaunch/AddCustom/* AddCustom/
   ```

   > [!NOTE] 说明
   > 
   >-  $\{git\_clone\_path\}为sample仓的存放路径。
   >-  完成算子工程创建后，需参考《[Ascend C算子开发指南](https://www.hiascend.com/document/detail/zh/canncommercial/83RC1/opdevg/Ascendcopdevg/atlas_ascendc_10_0001.html)》进行算子开发，但此步骤只需体现算子开发工具的功能，因此直接使用代码样例。
   >-  下载代码样例时，需执行以下命令指定分支版本。
   >   ```sh
   >   git clone https://gitee.com/ascend/samples.git -b r0.2
   >   ```

3. 编译算子工程。
    1. 参考《[MindStudio Ops Generator工具用户指南](./msopgen_user_guide.md)》中的“算子工程创建功能介绍>使用示例>算子编译部署 \>编译前准备”章节，完成编译相关配置。
    2. 在算子工程目录下，执行如下命令，进行算子工程编译。

        编译完成后，将会在build\_out目录生成.run算子包。

        ```sh
        ./build.sh
        ```

4. 在自定义算子包所在路径下，执行如下命令，部署算子包。

    ```sh
    ./build_out/custom_opp_<target_os>_<target_architecture>.run
    ```

5. 验证算子功能，生成可执行文件**execute\_add\_op**。
    1. 切换到AclNNInvocation仓的目录。

        ```sh
        cd ${git_clone_path}/samples/operator/ascendc/0_introduction/1_add_frameworklaunch/AclNNInvocation
        ```

    2. 执行以下命令。

        ```sh
        ./run.sh
        ```

    3. 成功对比精度，并生成可执行文件execute\_add\_op。

        ```
        INFO: execute op!
        [INFO]  Set device[0] success
        [INFO]  Get RunMode[1] success
        [INFO]  Init resource success
        [INFO]  Set input success
        [INFO]  Copy input[0] success
        [INFO]  Copy input[1] success
        [INFO]  Create stream success
        [INFO]  Execute aclnnAddCustomGetWorkspaceSize success, workspace size 0
        [INFO]  Execute aclnnAddCustom success
        [INFO]  Synchronize stream success
        [INFO]  Copy output[0] success
        [INFO]  Write output success
        [INFO]  Run op success
        [INFO]  Reset Device success
        [INFO]  Destroy resource success
        INFO: acl executable run success!
        error ratio: 0.0000, tolerance: 0.0010
        test pass
        ```


