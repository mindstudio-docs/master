# MindStudio Tools Extension Library Installation Guide

<br>

## 1. Installation Notes

This tool is integrated into CANN. If CANN is already installed and you do not need to update this tool, you can use it directly without following the installation steps in this document.

If CANN is not yet installed in your environment, refer to the [CANN Quick Installation](https://www.hiascend.com/en/cann/download) guide to install the Ascend NPU driver and CANN software (including Toolkit and the ops package), and configure the environment variables.

If you need to upgrade this tool separately or use the latest version, you can install it in the following three ways: [online installation](#21-online-installation), [offline installation](#22-offline-installation), [source installation](#23-source-installation).

## 2. Installation Methods

### 2.1 Online Installation

If your device has internet access, you can automatically download and install the tool with a single command. Please visit the Ascend Community MindStudio [download](https://www.hiascend.com/en/developer/software/mindstudio/download) page, select the corresponding CANN version, and choose online installation as the installation method. The system will guide you through the subsequent operations.

### 2.2 Offline Installation

For devices in environments without external network access, such as enterprise intranets, first download the complete offline installation package on a machine with internet access, then transfer it to the target device for installation. Please visit the MindStudio [download](https://www.hiascend.com/en/developer/software/mindstudio/download) page on the Ascend Community, select the corresponding CANN version, choose offline installation as the installation method, and obtain the corresponding installation package and operation guide.

### 2.3 Source Installation

If you need to use the latest code features or modify the source code to enhance functionality, you can download the repository code, compile and package the tool yourself, and complete the installation.

#### 2.3.1 Environment Preparation

Please follow the documentation below for environment configuration: [Operator Tool Development Environment Setup Guide](https://gitcode.com/Ascend/msot/blob/master/docs/en/common/dev_env_setup.md).

#### 2.3.2 Project Dependencies

- Clone this repository

    ```sh
    git clone https://gitcode.com/Ascend/mstx.git
    ```

- Download dependencies

    Since the code in this project depends on the header files of Python 3, the python3-dev package needs to be installed in the build environment. This can be done with the following commands:

    - OpenEuler environment:

        ```sh
        yum install python3-devel
        ```

    - Ubuntu environment:

        ```sh
        apt-get install python3-dev
        ```

    NOTE: Non-root users need to add sudo before the command, for example: `sudo yum install python3-devel`.

#### 2.3.3 Building and Packaging

```sh
cd mstx
python build.py
```

#### 2.3.4 whl Package Installation

```sh
cd output
pip3 install mstx-xxxxx.whl
```

## 3. Installation Verification

After installation, run the following command to verify whether the tool was installed successfully:

```shell
pip show mstx
```

If no error is reported and relevant information is displayed, the installation is successful.

## 4. Uninstallation

You can uninstall it by following these steps:

1. Download the script.

   ```bash
   curl -O https://inst.obs.cn-north-4.myhuaweicloud.com/26.1.0/ms_install.py
   ```

   > [!NOTE]
   >
   > - An internet connection is required for downloading. If the environment does not allow internet access or is offline, please download the script in an environment with internet access first, and then copy it to the target device.
   > - If the command does not respond or issues such as connection failure or SSL certificate errors occur, please refer to [FAQ](https://www.hiascend.com/developer/blog/details/02176213671719317003).

2. Execute the uninstallation.

   ```bash
   python ms_install.py uninstall {tools_name}
   ```

   Where `{tools_name}` refers to the name of the tool to be uninstalled. You can query it using the `python ms_install.py help` command, and the tool name will be displayed under the Available Tools field in the printed information.

   If the uninstallation is successful, the following information is printed:

   ```text
   Successfully uninstalled 1 tool ({tools_name})
   ```

## 5. Upgrade

Upgrade means "uninstall first, then install". Directly execute the installation command, and the tool will automatically uninstall the old version and guide you through the overwrite installation.

You can run the `pip show mstx` command to check the version information of the current environment and select the version you want to upgrade to. When upgrading the version, pay attention to version compatibility. Refer to the [Release Notes](https://gitcode.com/Ascend/release-management/blob/master/MindStudio/master/release_notes_en.md).
