# **MindStudio Ops System Test Quick Start**<a id="ZH-CN_TOPIC_0000002539355243"></a>

## Introduction<a id="section040515232197"></a>

The msOpST tool is used to preliminarily test operator functions after operator development. It can be used to analyze and optimize operator performance more efficiently, improving the operator execution efficiency and reducing the development cost.

This sample generates an .om file of a single-operator based on the AscendCL API process and executes the file to verify the operator execution result.

## Environment Setup<a id="section81731814530"></a>

- Prepare an Atlas A2 training or inference server and install the required driver and firmware. For details, see "Installing the NPU Driver and Firmware" in [CANN Software Installation Guide](https://www.hiascend.com/document/detail/zh/CANNCommunityEdition/83RC1/softwareinst/instg/instg_0000.html).
- Install the CANN Toolkit and ops operator package of the required version and configure CANN environment variables. For details, see [CANN Software Installation Guide](https://www.hiascend.com/document/detail/zh/CANNCommunityEdition/83RC1/softwareinst/instg/instg_0000.html).
- To use MindStudio Insight for viewing, install the MindStudio Insight software package separately. For download links, see "Installation and Uninstallation" in [MindStudio Insight User Guide](https://www.hiascend.com/document/detail/zh/mindstudio/82RC1/GUI_baseddevelopmenttool/msascendinsightug/Insight_userguide_0002.html).

> [!NOTE]NOTE  
> Run the `npu-smi info` command on the server where the Ascend AI Processor is installed to obtain the chip name. Note that the actual value is represented by `AscendChip name`. For example, if the chip name is `xxxyy`, the actual value is `Ascendxxxyy`. If `Ascendxxxyy` is the path of the code sample, set this parameter to `Ascendxxxyy`.

## Procedure<a id="section1587411211202"></a>

1. Generate ST cases.
    1. After step 2 in [MindStudio Ops Generator Quick Start](msopgen_quick_start.md) is complete, run the following command and replace the command path according to [MindStudio Ops Generator Quick Start](msopgen_quick_start.md).

        ```sh
        msopst create -i "$HOME/AddCustom/op_host/add_custom.cpp" -out ./st
        ```

    2. Generate ST cases.

        ```text
        2024-09-10 19:47:15 (3995495) - [INFO] Start to parse AscendC operator prototype definition in $HOME/AddCustom/op_host/add_custom.cpp.
        2024-09-10 19:47:15 (3995495) - [INFO] Start to check valid for op info.
        2024-09-10 19:47:15 (3995495) - [INFO] Finish to check valid for op info.
        2024-09-10 19:47:15 (3995495) - [INFO] Generate test case file $HOME/AddCustom/st/AddCustom_case_20240910194715.json successfully.
        2024-09-10 19:47:15 (3995495) - [INFO] Process finished!
        ```

    3. ST cases are generated in the `./st` directory.

2. Perform ST.
   1. Set environment variables based on the CANN package path.

       ```sh
       export DDK_PATH=${INSTALL_DIR}
       export NPU_HOST_LIB=${INSTALL_DIR}/{arch-os}/devlib  // In {arch-os}, arch indicates the OS architecture (select a value based on the architecture of the operating environment), and os indicates the OS (select a value based on the OS of the operating environment).
       ```

   2. Perform ST and save the test result to a specified path.

       ```sh
       msopst run -i ./st/AddCustom_case_{TIMESTAMP}.json -soc Ascendxxxyy -out ./st/out   // xxxyy indicates the actual processor type.
       ```

        > [!NOTE]NOTE  
        > Replace `$\{INSTALL\_DIR\}` with the actual file storage path after the CANN software is installed. For example, if the installation is performed as the `root` user, the default file storage path after the installation is `/usr/local/Ascend/cann`.

3. After the test is successful, the test result is output to the `st.report.json` file in the `./st/out/_\{TIMESTAMP\}_/` directory. For details, see the table "Fields in the st\_report.json report" in "Operator Test (msOpST) \> "Usage Example" \> "Generating/Executing Test Cases" in [MindStudio Ops Generator User Guide](../user_guide/msopgen_user_guide.md).
