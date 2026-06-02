# MindStudio Ops Generator Installation Guide

## Installation Description

MindStudio Ops Generator (msOpGen) is a tool for improving operator development efficiency. It provides the template project generation capability, simplifies operator project setup, and facilitates operator testing and validation. MindStudio Ops System Test (msOpST) is a tool for improving operator development efficiency. It tests the input and output of an operator in a real-world hardware environment to check operator functions. This document describes how to install msOpGen and msOpST. 

## Preparing for Installation

### 1. Environment and Dependencies

#### Binary Installation

The MindStudio toolchain is integrated into the CANN package for release. You can install it in either of the following ways.

##### Method 1: Install the software according to the CANN official document

For details, see <a href="https://www.hiascend.com/document/detail/zh/canncommercial/850/softwareinst" target="_blank">CANN Installation Guide</a>.
Perform the installation and configuration step by step according to the document.

##### Method 2: Use the official CANN container image

Visit <a href="https://www.hiascend.com/developer/ascendhub/detail/17da20d1c2b6493cb38765adeba85884" target="_blank">CANN official image repository</a>.
Pull the image and start the container according to the instructions in the repository.

#### Installing Python Dependencies

```sh
pip install -r requirements.txt
```

### 2. Generating .whl Packages

The generated .whl packages (`mindstudio_opgen` and `mindstudio_opst`) are stored in the `output` directory.

```py
python build.py
```

## Installation Procedure

### Installing the .whl Packages

```sh
cd output
pip install mindstudio_opgen-xxxxx.whl
pip install mindstudio_opst-xxxxx.whl
```

### Uninstallation

Run the following commands to uninstall the packages:

```sh
pip uninstall mindstudio_opgen-xxxxx.whl 
pip uninstall mindstudio_opst-xxxxx.whl
```

### Upgrade

To replace the installed .whl package with another .whl package, run the following command:

```sh
pip install mindstudio_opgen-xxxxx.whl --force-reinstall
pip install mindstudio_opst-xxxxx.whl --force-reinstall
```

During the installation, if the system asks you whether to replace the original installation package,
enter `y`. The installation package will be automatically upgraded.

### Running UT and ST Cases

`3.7 <= Python version <= 3.10`. Replace `\${INSTALL_DIR}` with the actual CANN installation directory. For example, if the Ascend-CANN-Toolkit software package is installed, the default installation directory is `$HOME/Ascend/cann`.

```shell
source ${INSTALL_DIR}/set_env.sh
```

The test report is stored in the `output` directory.

```sh
python build.py test
```
