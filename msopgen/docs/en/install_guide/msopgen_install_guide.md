# MindStudio Ops Generator Installation Guide

<br>

## 1. Installation Overview

This tool is integrated into CANN. If CANN is already installed and you do not need to update this tool, you can use it directly without following this document.

If CANN is not installed in your environment, see [CANN Quick Installation](https://www.hiascend.com/cann/download) to install the Ascend NPU driver and CANN software (including the Toolkit and ops package), and configure the environment variables.

To upgrade the tool separately or use the latest version, you can choose one of the following installation methods: [Online Installation](#21-online-installation), [Offline Installation](#22-offline-installation), or [Source Installation](#23-source-installation).

> [!WARNING]
>
> **Installation Path Risk Notice**: When installing msopgen/msopst `.whl` packages to a CANN environment directory (e.g., `$ASCEND_HOME_PATH`) or other non-isolated Python environment directories, the installation process will **clear all existing files in the `bin/` directory** under that path, retaining only the scripts from the current installation package (e.g., `msopgen`, `msopst`). This may cause the executables of other CANN tools or third-party tools in that `bin/` directory to be inadvertently deleted, affecting the normal use of other tools.
>
> **Recommendations**:
>
> - Preferably use an isolated Python virtual environment (e.g., `conda create` or `python -m venv`) for installation.
> - If installation to a CANN directory is unavoidable, back up the files in the `bin/` directory before installation and restore them as needed afterwards.

## 2. Installation Methods

### 2.1 Online Installation

If your device has internet access, you can use a single command to automatically download and install the tool. Visit the MindStudio [download page](https://www.hiascend.com/developer/software/mindstudio/download) on the Ascend Community website, select the corresponding CANN version, choose "Online Installation", and follow the prompts to complete the operation.

### 2.2 Offline Installation

For devices in enterprise intranets or other environments without internet access, first download the complete offline installation package on a machine with internet access, then transfer it to the target device for installation. Visit the MindStudio [download page](https://www.hiascend.com/developer/software/mindstudio/download) on the Ascend Community website, select the corresponding CANN version, choose "Offline Installation", and obtain the corresponding installation package and operation instructions.

### 2.3 Source Installation

If you need to use the latest code features or modify the source code to enhance functionality, download the repository code, compile and package the tool yourself, and complete the installation.

#### 2.3.1 Environment Preparation

Follow the guide [Operator Tool Development Environment Setup Guide](https://gitcode.com/Ascend/msot/blob/26.0.0/docs/en/common/dev_env_setup.md) to configure the environment.

- Clone the repository

    ```sh
    git clone https://gitcode.com/Ascend/msopgen.git
    ```

- Install Python dependencies

    ```sh
    cd msopgen
    pip install -r requirements.txt
    ```

#### 2.3.2 Installation

##### 2.3.2.1 Build the Package

Run the following command to generate `.whl` packages in the `output` directory, including both `mindstudio_opgen` and `mindstudio_opst`.

```sh
python build.py
```

##### 2.3.2.2 Install the .whl Packages

> [!WARNING]
> If you use `pip install --target <CANN directory>` to install `.whl` packages to a CANN environment directory, the installation process will clear all existing files in the `bin/` directory under the target path, retaining only the scripts from the current package. It is recommended to use an isolated Python virtual environment for installation.

```sh
cd output
pip install mindstudio_opgen-xxxxx.whl
pip install mindstudio_opst-xxxxx.whl
```

## 3. Uninstallation

To uninstall, follow these steps:

1. Download the script.

   ```bash
   curl -O https://inst.obs.cn-north-4.myhuaweicloud.com/26.0.0/ms_install.py
   ```

   > [!NOTE]
   >
   > - An internet connection is required to download the script. If the environment does not have internet access or is offline, download the script on a machine with internet access and copy it to the target device.
   > - If the command is unresponsive or a connection failure, SSL certificate error, or other problem occurs, see the [FAQ](https://www.hiascend.com/developer/blog/details/02176213671719317003).

2. Run the uninstall command.

   ```bash
   python ms_install.py uninstall {tools_name}
   ```

   Replace `{tools_name}` with the name of the tool you want to uninstall. You can query the tool name by running `python ms_install.py help`. Available tools are listed under the "Available Tools" field in the output.

   Upon successful uninstallation, the following message is displayed:

   ```text
   Successfully uninstalled 1 tool ({tools_name})
   ```

## 4. Upgrade

Upgrade means "uninstall first, then install". Run the installation command directly. The tool will automatically uninstall the old version and guide you through the upgrade installation.

## 5. Running UT and ST Test Cases

`3.7 <= Python version <= 3.11`. Replace `${INSTALL_DIR}` with the file storage path after the CANN software is installed. For example, if the Ascend-CANN-Toolkit software package is installed, the default installation path is `$HOME/Ascend/cann`.

```shell
source ${INSTALL_DIR}/set_env.sh
```

The test report is stored in the `output` directory.

```sh
python build.py test
```
