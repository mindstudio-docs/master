# MindStudio Ops Generator Installation Guide

<br>

## 1. Installation Description

This tool has been integrated into CANN. If CANN has been installed and this tool does not need to be updated, you can directly use it without following the instructions in this document.

If CANN has not been installed in your environment, install the Ascend NPU driver and CANN software (including the Toolkit and ops) by referring to [CANN Quick Installation](https://www.hiascend.com/en/cann/download), and configure environment variables.

If you need to upgrade this tool separately or use the latest version, you can install it in any of the following ways: [Online Installation](#21-online-installation), [Offline Installation](#22-offline-installation), and [Source Installation](#23-source-installation).

> [!WARNING]
>
> **Installation Path Risk**: If you install the `msopgen`/`msopst` `.whl` packages in the CANN environment directory, such as `$ASCEND_HOME_PATH`, or another directory that is not an independent Python virtual environment, the installation process deletes **all existing files** in the `bin/` directory and retains only the script files included in the current installation package, such as `msopgen` and `msopst`. This may accidentally delete the executable files of other CANN tools or third-party tools in the `bin/` directory and affect their normal use.
>
> **Recommendation**:
>
> - You are advised to install the packages in an independent Python virtual environment, such as one created with `conda create` or `python -m venv`.
> - If you must install the packages in the CANN directory, back up the files in the `bin/` directory before installation and restore them as needed after installation.

## 2. Installation Methods

### 2.1 Online Installation

If your device has Internet access, you can run a single command to automatically download and install the tool. Visit the [Ascend community](https://www.hiascend.com/en/developer/software/mindstudio/download), select the target CANN version, and choose "Online" installation method. The system will guide you through the subsequent operations.

### 2.2 Offline Installation

For devices that are not connected to the Internet, such as those on an enterprise intranet, download the complete offline installation package on a device that has Internet access and then transfer the package to the target device for installation. Visit the [Ascend community](https://www.hiascend.com/en/developer/software/mindstudio/download), select the target CANN version, and choose "Offline" installation method. The system will guide you through the subsequent operations.

### 2.3 Source Installation

To use the functions of the latest code or modify the source code to enhance functions, you can download the code from this repository, build and package the tool, and install it.

#### 2.3.1 Preparing the Environment

Set up the environment by referring to [Operator Tool Development Environment Installation Guide](https://gitcode.com/Ascend/msot/blob/master/docs/en/common/dev_env_setup.md).

- Clone this repository.

    ```sh
    git clone https://gitcode.com/Ascend/msopgen.git
    ```

- Install the Python dependency.

    ```sh
    cd msopgen
    pip install -r requirements.txt
    ```

#### 2.3.2 Installation

##### 2.3.2.1 Building and Packaging

After the following command is executed, the generated `.whl` packages (`mindstudio_opgen` and `mindstudio_opst`) are stored in the `output` directory.

```sh
python build.py
```

##### 2.3.2.2 Installing the `.whl` Package

```sh
cd output
pip install mindstudio_opgen-xxxxx.whl
pip install mindstudio_opst-xxxxx.whl
```

## 3. Installation Verification

After the installation is complete, run the following command to check whether the tool is successfully installed:

```shell
msopgen --help
```

If no error is reported and the help information is displayed, the installation is successful.

## 4. Uninstallation

To uninstall the tool, perform the following steps:

1. Download the script.

   ```bash
   curl -O https://inst.obs.cn-north-4.myhuaweicloud.com/26.1.0/ms_install.py
   ```

   > [!NOTE]
   >
   > - Internet access is required to download the script. If your target environment is offline or does not allow Internet access, download the script on an Internet-connected device first, then copy it to the target device.
   > - If the command does not respond, or you encounter connection failures, SSL certificate errors, or other issues, refer to the [FAQ](https://www.hiascend.com/developer/blog/details/02176213671719317003).

2. Uninstall the tool.

   ```bash
   python ms_install.py uninstall {tools_name}
   ```

   Replace `{tools_name}` with the name of the tool to be uninstalled. You can run the `python ms_install.py help` command to query the tool name, which is displayed under the `Available Tools` field in the command output.

   If the uninstallation is successful, the following information is displayed:

   ```text
   Successfully uninstalled 1 tool ({tools_name})
   ```

## 5. Upgrade

Upgrades follow the "uninstall first, then install" process. Simply run the installation command. The tool will automatically remove the previous version and guide you through the upgrade process.

You can run the `msopgen --version` command to view the version information of the current environment and then select the version to be upgraded. When upgrading the version, pay attention to the version mapping. For details, see [Release Notes](https://gitcode.com/Ascend/release-management/blob/master/MindStudio/master/release_notes_en.md).

## 6. Running UT and ST Cases

`3.7 <= Python version <= 3.11`. Replace `${INSTALL_DIR}` with the path for storing the CANN installation files. For example, if the Ascend-CANN-Toolkit software package is installed, the default installation directory is `$HOME/Ascend/cann`.

```shell
source ${INSTALL_DIR}/set_env.sh
```

The test report is stored in the `output` directory.

```sh
cd msopgen
python build.py test
```
