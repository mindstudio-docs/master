# **MindStudio Ops System Test Quick Start**<a id="ZH-CN_TOPIC_0000002539355243"></a>

## Introduction<a id="section040515232197"></a>

The msOpST tool is used to preliminarily test operator functions after operator development. It can be used to analyze and optimize operator performance more efficiently, improving the operator execution efficiency and reducing the development cost.

This sample generates an .om file of a single-operator based on the AscendCL API process and executes the file to verify the operator execution result.

**Core features**:

- **Generate test cases** (`msopst create`): Parses Host-side operator implementation files and automatically generates ST test case definition JSON
- **Execute test cases** (`msopst run`): Runs operators in a real hardware environment based on test case definitions and outputs test reports

## Environment Setup<a id="section81731814530"></a>

- Prepare an Atlas A2 training or inference server and install the required driver and firmware. For details, see "Installing the NPU Driver and Firmware" in [CANN Software Installation Guide](https://www.hiascend.com/document/detail/zh/CANNCommunityEdition/83RC1/softwareinst/instg/instg_0000.html).
- Install the CANN Toolkit and ops operator package of the required version and configure CANN environment variables. For details, see [CANN Software Installation Guide](https://www.hiascend.com/document/detail/zh/CANNCommunityEdition/83RC1/softwareinst/instg/instg_0000.html).
- To use MindStudio Insight for viewing, install the MindStudio Insight software package separately. For download links, see "Installation and Uninstallation" in [MindStudio Insight User Guide](https://www.hiascend.com/document/detail/zh/mindstudio/82RC1/GUI_baseddevelopmenttool/msascendinsightug/Insight_userguide_0002.html).

> [!NOTE]  
> Run the `npu-smi info` command on the server where the Ascend AI Processor is installed to obtain the chip name. Note that the actual value is represented by `AscendChip name`. For example, if the chip name is `xxxyy`, the actual value is `Ascendxxxyy`. If `Ascendxxxyy` is the path of the code sample, set this parameter to `Ascendxxxyy`.

## Quick Command Reference

| Command | Function | Example |
|------|------|------|
| `msopst create` | Generate ST test cases from Host-side .cpp | `msopst create -i add_custom.cpp -out ./st` |
| `msopst run` | Execute ST test cases | `msopst run -i ./st/case.json -soc Ascend910B4 -out ./out` |

## Procedure<a id="section1587411211202"></a>

1. Generate ST cases.
    1. After step 2 in [MindStudio Ops Generator Quick Start](msopgen_quick_start.md) is complete, run the following command and replace the command path according to [MindStudio Ops Generator Quick Start](msopgen_quick_start.md).

        ```sh
        msopst create -i "$HOME/AddCustom/op_host/add_custom.cpp" -out ./st
        ```

        **Parameter description**:
        - `-i, --input`: Path to the Host-side operator implementation file (.cpp). Required.
        - `-out, --output`: Output directory for test cases. Optional (defaults to the current directory).
        - `-m, --model`: Path to a TensorFlow model file. Optional (used to automatically extract shape info).
        - `-q, --quiet`: Silent mode, skip interactive confirmation. Optional.

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
        export NPU_HOST_LIB=${INSTALL_DIR}/{arch-os}/devlib  # In {arch-os}, arch indicates the OS architecture (select a value based on the architecture of the operating environment), and os indicates the OS (select a value based on the OS of the operating environment).
        ```

    2. Perform ST and save the test result to a specified path.

        ```sh
        msopst run -i ./st/AddCustom_case_{TIMESTAMP}.json -soc Ascendxxxyy -out ./st/out   # xxxyy indicates the actual processor type.
        ```

        **Parameter description**:
        - `-i, --input`: Path to the test case definition file (.json). Required.
        - `-soc, --soc_version`: AI processor chip type. Required.
        - `-out, --output`: Output directory for test results. Optional.
        - `-c, --case_name`: Specify case names to execute, separated by commas. Optional (defaults to running all cases).
        - `-d, --device_id`: NPU device ID. Optional (default: 0).
        - `-err_thr, --error_threshold`: Custom precision standard. Optional (default: "[0.01,0.05]").

        > [!NOTE]   
        > Replace `${INSTALL_DIR}` with the actual file storage path after the CANN software is installed. For example, if the installation is performed as the `root` user, the default file storage path after the installation is `/usr/local/Ascend/cann`.
