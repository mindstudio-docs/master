# **MindStudio Ops System Test Quick Start**<a id="ZH-CN_TOPIC_0000002539355243"></a>

## Introduction<a id="section040515232197"></a>

The msOpST tool is used to preliminarily test operator functions after operator development. It can be used to analyze and optimize operator performance more efficiently, improving the operator execution efficiency and reducing the development cost.

This sample generates an `.om` file of a single-operator based on the AscendCL API process and executes the file to verify the operator execution result.

**Core Functions**:

- **Generate test cases** (`msopst create`): Parses the host-side operator implementation file and automatically generates the ST test case definition JSON.
- **Run test cases** (`msopst run`): Executes the operator in a real hardware environment based on the test case definition and outputs a test report.

## Environment Setup<a id="section81731814530"></a>

- Prepare an Atlas A2 training or inference server and install the required driver and firmware. For details, see "Installing the NPU Driver and Firmware" in [CANN Software Installation Guide](https://www.hiascend.com/document/detail/en/CANNCommunityEdition/910/softwareinst/instg/instg_0000.html?OS=openEuler&InstallType=netconda).
- Install the CANN Toolkit and ops operator package of the required version and configure CANN environment variables. For details, see [CANN Software Installation Guide](https://www.hiascend.com/document/detail/en/CANNCommunityEdition/910/softwareinst/instg/instg_0000.html?OS=openEuler&InstallType=netconda).
- To use MindStudio Insight for viewing, install the MindStudio Insight software package separately. For download links, see "Installation Guide" in [MindStudio Insight User Guide](https://www.hiascend.com/document/detail/en/mindstudio/2610/GUI_baseddevelopmenttool/MindStudioInsight/docs/en/install_guide/mindstudio_insight_install_guide.md?framework=mindspore).

> [!NOTE]
> 
> Run the `npu-smi info` command on the server where the Ascend AI Processor is installed to obtain the chip name. Note that the actual value is represented by `AscendChip name`. For example, if the chip name is `xxxyy`, the actual value is `Ascendxxxyy`. If the chip name is `xxxyy`, set this parameter to `Ascendxxxyy`.

## Common Commands Quick Reference

| Command | Function | Example |
|---------|----------|---------|
| msopst create | Generates ST test cases from the host-side .cpp file. | msopst create -i add_custom.cpp -out ./st |
| msopst run | Runs ST test cases. | msopst run -i ./st/case.json -soc Ascend910B4 -out ./out |

## Procedure<a id="section1587411211202"></a>

1. Generate ST test cases.
    1. After step 2 in [MindStudio Ops Generator Quick Start](msopgen_quick_start.md) is complete, run the following command and replace the command path according to [MindStudio Ops Generator Quick Start](msopgen_quick_start.md).

        ```sh
        msopst create -i "$HOME/AddCustom/op_host/add_custom.cpp" -out ./st
        ```

        **Parameters**:
        - `-i, --input`: host-side operator implementation file path (.cpp). Required.
        - `-out, --output`: test case output directory. Optional (the current directory by default).
        - `-m, --model`: TensorFlow model file path. Optional (used to automatically extract shape information).
        - `-q, --quiet`: quiet mode, without human-machine interaction confirmation. Optional.

    2. View the generation result.

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
        export NPU_HOST_LIB=${INSTALL_DIR}/{arch-os}/devlib  // In {arch-os}, arch indicates the OS architecture (select a value based on the architecture of the operating environment), and os indicates the OS (select a value based on the OS of the operating environment)
        ```

    2. Perform ST and save the test result to a specified path.

        ```sh
        msopst run -i ./st/AddCustom_case_{TIMESTAMP}.json -soc Ascendxxxyy -out ./st/out   // xxxyy indicates the actual processor type
        ```

        **Parameters**:
        - `-i, --input`: test case definition file (.json) path. Required.
        - `-soc, --soc_version`: AI processor chip type. Required.
        - `-out, --output`: test output directory. Optional.
        - `-c, --case_name`: name of the case to run, with multiple names separated by commas. Optional (all cases are run by default).
        - `-d, --device_id`: NPU device ID. Optional (0 by default).
        - `-err_thr, --error_threshold`: custom accuracy criteria. Optional (`"[0.01,0.05]"` by default).

        > [!NOTE]
        > 
        > Replace `${INSTALL_DIR}` with the actual file storage path after the CANN software is installed. For example, if the installation is performed as the `root` user, the default file storage path after the installation is `/usr/local/Ascend/cann`.
