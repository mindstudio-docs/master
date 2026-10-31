# msTX Installation Guide

<br>

## 1. Installation Notes

This tool is integrated into CANN. If CANN is already installed and you do not need to update this tool, you can use it directly without following the installation steps in this document.

If CANN is not yet installed in your environment, refer to the [CANN Quick Installation](https://www.hiascend.com/cann/download) guide to install the Ascend NPU driver and CANN software (including Toolkit and the ops package), and configure the environment variables.

If you need to upgrade this tool separately or use the latest version, you can install it in the following ways: [online installation](#21-online-installation), [offline installation](#22-offline-installation), [source installation](#23-source-installation).

## 2. Installation Methods

### 2.1 Online Installation

If your device has internet access, you can automatically download and install the tool with a single command. Please visit the Ascend Community MindStudio [download](https://www.hiascend.com/developer/software/mindstudio/download) page, select the corresponding CANN version, and choose online installation as the installation method. The system will guide you through the subsequent operations.

### 2.2 Offline Installation

For devices in environments without external network access, such as enterprise intranets, first download the complete offline installation package on a machine with internet access, then transfer it to the target device for installation. Please visit the MindStudio [download](https://www.hiascend.com/developer/software/mindstudio/download) page on the Ascend Community, select the corresponding CANN version, choose offline installation as the installation method, and obtain the corresponding installation package and operation guide.

### 2.3 Source Installation

If you need to use the latest code features or modify the source code to enhance functionality, you can download the repository code, compile and package the tool yourself, and complete the installation.

#### 2.3.1 Environment Preparation

All source code compilation uses the standard MindStudio build environment.

- For daily development or when you use a released image, refer to the [MindStudio Tool Development Environment Installation Guide](https://gitcode.com/Ascend/msot/blob/master/docs/en/common/dev_env_setup.md).
- If you need to reproduce the environment from a base operating system, or to perform source code build verification or unit test verification, you must refer to the [MindStudio Unified Build Image Creation Guide](https://gitcode.com/Ascend/msot/blob/master/docs/en/common/docker_image_build_guide.md) to build the environment image on site from the openEuler base image.

The source code compilation and unit test commands later in this document all run in the container of the specified image or of the environment image built on site. The CANN software package version, GCC version, and Python version are subject to the *Unified Build Image Creation Guide*, and this repository does not maintain them separately.

After the image is built, you must use the `ctr_in.py` command provided in Chapter 7 of the *Unified Build Image Creation Guide* to start and enter the container in an interactive terminal. Do not use a plain `docker run` to create a container, and do not use `docker exec <container_name> bash -c '<command>'` to replace the interactive environment. Otherwise, the initialization of the Python, GCC, and CANN environments may be skipped.

After you enter the interactive container shell opened by `ctr_in.py`, run the following command to clone this repository:

```bash
cd ~
git clone https://gitcode.com/Ascend/mstx.git
```

#### 2.3.2 Compilation

Stay in the same interactive container shell opened by `ctr_in.py`, and run the following command in the repository root directory to automatically download dependencies and build:

```bash
cd ~/mstx
python3 build.py
```

After the build succeeds, the installation package is generated in the `artifacts/` directory.

#### 2.3.3 Unit Tests (Optional)

This step is not required for installation. If you need to verify the basic functions of the code, you can run the unit tests:

```bash
cd ~/mstx
python3 build.py test
```

If the return code of the command is 0 and no test case fails, the unit tests pass.

#### 2.3.4 Installation

##### 2.3.4.1 Installation Package

Copy the whl package to the operating environment (not required for local installation) and perform the following installation:

```shell
cd ~/mstx/artifacts
pip3 install mstx-xxxxx.whl
```

## 3. Installation Verification

After installation, run the following command to verify whether the tool was installed successfully:

```shell
python3 -c "import mstx; print('All is OK')"
```

If no error is reported and `All is OK` is displayed, the installation is successful.

## 4. Uninstallation

You can uninstall it by following these steps:

1. Download the script.

   ```bash
   curl -O https://inst.obs.cn-north-4.myhuaweicloud.com/26.2.0/ms_install.py
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

You can run the `pip show mstx` command to check the version information of the current environment and select the version you want to upgrade to. When upgrading the version, pay attention to version compatibility. Refer to the [Release Notes](https://gitcode.com/Ascend/release-management/blob/master/MindStudio/master/release_notes.md).
