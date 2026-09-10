# MindStudio Tools Extension Library Development Guide

<br>

## 1. Prerequisites

First read the [msTX API List](../api_reference/README.md) to learn about the core APIs provided by msTX and their functions.

## 2. Development Environment Preparation

For details, see [Operator Tool Development Environment Setup Guide](https://gitcode.com/Ascend/msot/blob/master/docs/en/common/dev_env_setup.md).

Compilation also requires installing python3-dev (the header files required to compile Python bindings):

```sh
# openEuler
yum install python3-devel

# Ubuntu
apt-get install python3-dev
```

> **NOTE:** If you are not a root user, add `sudo` before the command.

## 3. Compilation and Packaging

The following two methods are available, with their advantages and disadvantages:

| Method | Application Scenario | Advantages | Disadvantages |
|------|---------|------|------|
| One-click script | First build and CI/CD pipeline | Zero configuration, one-step setup | Steps cannot be executed independently. |
| Step-by-step script | Daily development and incremental build | Flexible and efficient | Multiple steps are required. |

### 3.1 Method 1: One-click Script

```shell
python build.py
```

### 3.2 Method 2: Step-by-Step Script

#### 3.2.1 Downloading Dependencies

```shell
python download_dependencies.py
```

#### 3.2.2 Starting Compilation

Run the following command to start compilation:

```shell
mkdir build
cd build
cmake .. && make -j$(nproc)
make install
```

After compilation is complete, check the `output/` directory. If the file generation time has been updated to the current compilation time, the compilation has completed successfully.

#### 3.2.3 Compilation Result Description

The compilation results are generated in the `output/` directory:

```text
output/
├── mstx/                         # Installation directory
│   └── lib64/                    # Dynamic libraries (libms_tools_ext.so, mstx.so)
└── mstx-<version>.whl            # Python installation package
```

#### 3.2.4 Cleanup and Recompilation

Delete the build directory and rerun [Section 3.2.2](#322-starting-compilation):

```shell
rm -rf build
```

## 4. Unit Testing

```shell
python build.py test
```

This command sequentially downloads test dependencies, compiles C/CPP test targets in Debug mode, runs C/C++ unit tests, and runs Python unit tests.

If the output is similar to the following, and the number of run test cases equals the number of passed test cases, it indicates success:

```text
[----------] 4 tests from CoreApi (8ms total)
```

```text
============= 4 passed in 0.03s =============
```

NOTE: You need to install `pytest` in the environment beforehand to run Python tests. There are multiple independent test suites. If the output results are similar to the example, it indicates successful execution.

## 5. FAQ

### 5.1 Compilation Error: `Python.h` Not Found

```text
fatal error: Python.h: No such file or directory
```

**Solution:** Install the Python development package:

```sh
# OpenEuler
yum install python3-devel

# Ubuntu
apt-get install python3-dev
```

### 5.2 Test Error: `pytest` Not Found

```text
pytest: command not found
```

**Solution:** Install `pytest`:

```sh
pip3 install pytest
```

### 5.3 Only the whl Package Exists in the Output Folder, No Dynamic Library

The one-click script `python build.py` generates the whl package and installs dynamic libraries to `output/mstx/lib64/` at the same time. If you only see the whl package, it is usually because only `cmake .. && make` was run during the step-by-step compilation and `make install` was missed. Run `make install` in the `build/` directory to fix this.
