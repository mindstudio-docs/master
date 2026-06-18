# **MindStudio Ops System Test快速入门**<a id="ZH-CN_TOPIC_0000002539355243"></a>

## 简介<a id="section040515232197"></a>

msOpST工具用于算子开发完成后，对算子功能进行初步测试，该工具可以更加高效地进行算子性能的分析和优化，提高算子的执行效率，降低开发成本。

本样例基于AscendCL接口的流程，生成单算子的OM文件，并执行该文件以验证算子执行结果的正确性。

## 环境准备<a id="section81731814530"></a>

- 准备Atlas A2 训练系列产品/Atlas A2 推理系列产品的服务器，并安装对应的驱动和固件，具体安装过程请参见《[CANN 软件安装指南](https://www.hiascend.com/document/detail/zh/CANNCommunityEdition/83RC1/softwareinst/instg/instg_0000.html)》中的“安装NPU驱动和固件”章节。
- 安装配套版本的CANN Toolkit开发套件包和ops算子包并配置CANN环境变量，具体请参见《[CANN 软件安装指南](https://www.hiascend.com/document/detail/zh/CANNCommunityEdition/83RC1/softwareinst/instg/instg_0000.html)》。
- 若要使用MindStudio Insight进行查看时，需要单独安装MindStudio Insight软件包，具体下载链接请参见《[MindStudio Insight工具用户指南](https://www.hiascend.com/document/detail/zh/mindstudio/82RC1/GUI_baseddevelopmenttool/msascendinsightug/Insight_userguide_0002.html)》的“安装与卸载”章节。

> [!NOTE] 说明  
> 在安装昇腾AI处理器的服务器执行`npu-smi info`命令进行查询，获取**Chip Name**信息。实际配置值为AscendChip Name，例如**Chip Name**取值为xxxyy，实际配置值为Ascendxxxyy。当Ascendxxxyy为代码样例路径时，需要配置Ascendxxxyy。

## 操作步骤<a id="section1587411211202"></a>

1. 生成ST测试用例。
    1. 在《[MindStudio Ops Generator快速入门](./msopgen_quick_start.md)》创建算子工程中的步骤2执行完成后，再执行以下命令，并根据《[MindStudio Ops Generator快速入门](./msopgen_quick_start.md)》步骤1的第四点生成的目录替换命令路径。

        ```sh
        msopst create -i "$HOME/AddCustom/op_host/add_custom.cpp" -out ./st
        ```

    2. 生成ST测试用例。

        ```
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
       export NPU_HOST_LIB=${INSTALL_DIR}/{arch-os}/devlib  // {arch-os}中arch表示操作系统架构（需根据运行环境的架构选择），os表示操作系统（需根据运行环境的操作系统选择）
       ```

   2. 执行ST测试，并将输出结果到指定路径。

       ```sh
       msopst run -i ./st/AddCustom_case_{TIMESTAMP}.json -soc Ascendxxxyy -out ./st/out   // xxxyy为用户实际使用的具体芯片类型
       ```

        > [!NOTE] 说明  
        > $\{INSTALL\_DIR\}请替换为CANN软件安装后文件存储路径。以root用户安装为例，安装后文件默认存储路径为：/usr/local/Ascend/cann。

3. 测试成功后，将测试结果输出在./st/out/_\{TIMESTAMP\}_/路径下的st.report.json文件，具体请参见《[MindStudio Ops Generator工具用户指南](./msopgen_user_guide.md)》中的“算子测试（msOpST）\>使用示例\> 生成/执行测试用例”章节中的表 st\_report.json报表主要字段及含义。

