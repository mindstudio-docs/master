# **MindStudio Ops System Test快速入门**<a id="ZH-CN_TOPIC_0000002539355243"></a>

## 简介<a id="section040515232197"></a>

msOpST工具用于算子开发完成后，对算子功能进行初步测试，该工具可以更加高效地进行算子性能的分析和优化，提高算子的执行效率，降低开发成本。

本样例基于AscendCL接口的流程，生成单算子的OM文件，并执行该文件以验证算子执行结果的正确性。

**核心功能**：

- **生成测试用例** (`msopst create`)：解析 Host 侧算子实现文件，自动生成 ST 测试用例定义 JSON
- **执行测试用例** (`msopst run`)：基于测试用例定义，在真实硬件环境中执行算子并输出测试报告

## 环境准备<a id="section81731814530"></a>

- 准备Atlas A2 训练系列产品/Atlas A2 推理系列产品的服务器，并安装对应的驱动和固件，具体安装过程请参见《[CANN 软件安装指南](https://www.hiascend.com/document/detail/zh/CANNCommunityEdition/83RC1/softwareinst/instg/instg_0000.html)》中的"安装NPU驱动和固件"章节。
- 安装配套版本的CANN Toolkit开发套件包和ops算子包并配置CANN环境变量，具体请参见《[CANN 软件安装指南](https://www.hiascend.com/document/detail/zh/CANNCommunityEdition/83RC1/softwareinst/instg/instg_0000.html)》。
- 若要使用MindStudio Insight进行查看时，需要单独安装MindStudio Insight软件包，具体下载链接请参见《[MindStudio Insight工具用户指南](https://www.hiascend.com/document/detail/zh/mindstudio/82RC1/GUI_baseddevelopmenttool/msascendinsightug/Insight_userguide_0002.html)》的"安装与卸载"章节。

> [!NOTE]  
> 在安装昇腾AI处理器的服务器执行`npu-smi info`命令进行查询，获取**Chip Name**信息。实际配置值为AscendChip Name，例如**Chip Name**取值为xxxyy，实际配置值为Ascendxxxyy。当Ascendxxxyy为代码样例路径时，需要配置Ascendxxxyy。

## 常用命令速查

| 命令 | 功能 | 示例 |
|------|------|------|
| `msopst create` | 从 Host 侧 .cpp 生成 ST 测试用例 | `msopst create -i add_custom.cpp -out ./st` |
| `msopst run` | 执行 ST 测试用例 | `msopst run -i ./st/case.json -soc Ascend910B4 -out ./out` |

## 操作步骤<a id="section1587411211202"></a>

1. 生成ST测试用例。
    1. 在《[MindStudio Ops Generator快速入门](msopgen_quick_start.md)》创建算子工程中的步骤2执行完成后，再执行以下命令，并根据《[MindStudio Ops Generator快速入门](msopgen_quick_start.md)》步骤1的第四点生成的目录替换命令路径。

        ```sh
        msopst create -i "$HOME/AddCustom/op_host/add_custom.cpp" -out ./st
        ```

        **参数说明**：
        - `-i, --input`：Host 侧算子实现文件路径（.cpp），必选
        - `-out, --output`：测试用例输出目录，可选（默认当前目录）
        - `-m, --model`：TensorFlow 模型文件路径，可选（用于自动提取 shape 信息）
        - `-q, --quiet`：静默模式，不进行人机交互确认，可选

    2. 查看生成结果。

        ```text
        2024-09-10 19:47:15 (3995495) - [INFO] Start to parse AscendC operator prototype definition in $HOME/AddCustom/op_host/add_custom.cpp.
        2024-09-10 19:47:15 (3995495) - [INFO] Start to check valid for op info.
        2024-09-10 19:47:15 (3995495) - [INFO] Finish to check valid for op info.
        2024-09-10 19:47:15 (3995495) - [INFO] Generate test case file $HOME/AddCustom/st/AddCustom_case_20240910194715.json successfully.
        2024-09-10 19:47:15 (3995495) - [INFO] Process finished!
        ```

    3. 在./st目录下生成ST测试用例。

2. 执行ST测试。
    1. 根据CANN包路径设置环境变量。

        ```sh
        export DDK_PATH=${INSTALL_DIR}
        export NPU_HOST_LIB=${INSTALL_DIR}/{arch-os}/devlib  # {arch-os}中arch表示操作系统架构（需根据运行环境的架构选择），os表示操作系统（需根据运行环境的操作系统选择）
        ```

    2. 执行ST测试，并将输出结果保存到指定路径。

        ```sh
        msopst run -i ./st/AddCustom_case_{TIMESTAMP}.json -soc Ascendxxxyy -out ./st/out   # xxxyy为用户实际使用的具体芯片类型
        ```

        **参数说明**：
        - `-i, --input`：测试用例定义文件（.json）路径，必选。
        - `-soc, --soc_version`：AI 处理器芯片类型，必选
        - `-out, --output`：测试输出目录，可选
        - `-c, --case_name`：指定执行的 case 名称，多个用逗号分隔，可选（默认执行全部）
        - `-d, --device_id`：NPU 设备 ID，可选（默认 0）
        - `-err_thr, --error_threshold`：自定义精度标准，可选（默认 "[0.01,0.05]"）

        > [!NOTE]   
        > `${INSTALL_DIR}`请替换为CANN软件安装后文件存储路径。以root用户安装为例，安装后文件默认存储路径为：/usr/local/Ascend/cann。
