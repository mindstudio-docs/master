# MindStudio Tools Extension Library Development Guide

<br>

This document describes how to set up the development environment for MindStudio Tools Extension Library (msTX), build the project, and run UT unit tests.

## 1. Prerequisites

### 1.1 Prerequisite Knowledge

Before starting development, read [msTX API List](../api_reference/README.md) to learn about the core APIs provided by msTX and their functions.

### 1.2 Environment Preparation

Follow [msTX Installation Guide — Source Installation](../install_guide/mstx_install_guide.md#231-environment-preparation) to set up the build and test environment.

> **Note:** The environment image build method and the supporting software versions are maintained by the *MindStudio Unified Build Image Creation Guide* and are not redefined in this repository.

## 2. Build

Run the following in the project root directory:

```bash
python3 build.py
```

### 2.1 Build Artifacts

After a successful build, the output is generated in the `artifacts` directory.

### 2.2 Build Cleanup

To perform a full rebuild, delete the build directory and run the preceding steps again:

```bash
rm -rf build
```

## 3. Unit Tests

### 3.1 Running Tests

```bash
python3 build.py test
```

This command sequentially downloads test dependencies, compiles C++ test targets in Debug mode, runs C++ unit tests, and runs Python unit tests.

When all tests pass, the output is similar to the following example:

```text
[----------] 4 tests from CoreApi (8ms total)
```

```text
============= 4 passed in 0.03s =============
```

> **Pass criteria:** The tests pass when the number of `ran` test cases matches the number of `PASSED` test cases. If any `FAILED` test cases exist, locate the cause of the failure from the logs. There are multiple independent test suites. If the output results are similar to the example, it indicates successful execution.

### 3.2 Cleaning the Test Environment

Delete the UT build directory and run the tests again:

```bash
rm -rf build_ut
```
