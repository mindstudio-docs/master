# MindStudio Ops Tuner Installation Guide

## Overview

MindStudio Ops Tuner (operator Tiling optimization, msOpTuner) is a tool for optimizing the tiling parameters of operators in the CATLASS template library. It allows you to define a custom search space, instantiates all operators within that space, and performs batch on-board performance tests, providing a reference for operator tiling parameter optimization. This document describes how to install the msOpTuner tool.

## Preparation Before Installation

**Configuring Username and SSH Key**

To avoid repeatedly entering passwords during dependency downloads, run the following command to configure Git to save user passwords:

```
git config --global credential.helper store
```

### Environment Preparation

- Ascend NPU 910B hardware environment

Before starting the build, ensure that the bisheng compiler is installed and that the path to its executable is in the `$PATH` environment variable. (If the CANN operator toolkit is installed, you can run `source set_env.sh` in the toolkit installation path.)

```shell
source /path/to/Ascend/cann/set_env.sh
```

## Installation Steps

### Project Build

- One-click script method
Build the software package using the one-click script.

    ```shell
    python build.py
    ```

> [!NOTE] NOTE
> If you have modified the code in the dependent sub-repositories locally and do not want the update action to be executed during the build process, run `python build.py local`.

## Testing

- One-click script method
    Run the one-click script to download UT build dependencies and execute UT tests:

    ```shell
    python build.py test
    ```
