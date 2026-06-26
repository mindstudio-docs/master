# MindStudio Tools Extension Library Development Guide

<br>

## 1. Development Environment Preparation

For details, see [Operator Tool Development Environment Setup Guide](https://gitcode.com/Ascend/msot/blob/master/docs/en/common/dev_env_setup.md).

## 2. Compilation and Packaging

```shell
python build.py
```

## 3. Unit Testing

You can run UT tests for C/CPP/PYTHON code using a one-click script:

```sh
python build.py test
```

If the output is similar to the following, and the number of run test cases equals the number of passed test cases, it indicates success:

```text
[----------] 4 tests from CoreApi (8ms total) 
```

```text
============= 4 passed in 0.03s =============
```

NOTE: You need to install pytest in the environment beforehand to run Python tests. There are multiple independent test suites. If the output results are similar to the example, it indicates successful execution.
