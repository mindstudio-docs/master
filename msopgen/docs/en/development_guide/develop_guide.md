# MindStudio msOpGen Development Environment Setup and UT Methods

<br>

## 1. Background Knowledge Required

Before developing msOpGen, you need to understand the following fundamentals:

- **Python project structure**: msOpGen is a Python-based CLI tool. Its source code is in the `msopgen/` directory, and it uses `setuptools` to build the wheel package.
- **Tool components**: msOpGen generates operator projects (`msopgen gen`) and parses simulation process diagrams (`msopgen sim`). msOpST generates and runs ST test cases (`msopst create/run`).
- For details on the architecture design and module breakdown, see the [msOpGen Architecture Design](./architecture.md).

## 2. Development Environment Setup

Set up the environment by referring to the [Operator Tool Development Environment Setup Guide](https://gitcode.com/Ascend/msot/blob/master/docs/en/common/dev_env_setup.md).

## 3. One-click Build

```shell
python build.py
```

The generated wheel packages are located in the `output/` directory and include the `mindstudio_opgen` and `mindstudio_opst` packages.

## 4. Project Directory Structure

```text
├── msopgen/          // msopgen source code directory (core engine)
├── tools/msopst/     // msopst source code directory (ST test tool)
├── test/
│   ├── msopgen/      // msopgen unit tests
│   └── msopst/       // msopst unit tests
├── example/          // Tool examples
├── docs/             // Project documentation
├── setup.py          // build script for the msopgen wheel package
├── build.py          // Build entry script
└── requirements.txt  // Python dependencies
```

## 5. UT Tests

```shell
python build.py test
```

### 5.1 Test coverage

UT tests cover the following core functions:

- Operator project template generation (`msopgen gen`)
- Simulation process diagram parsing (`msopgen sim`)
- ST test case generation (`msopst create`)
- ST test case execution (`msopst run`)

## 6. Code standards

- When you add a feature, also write UT test cases.
- Add docstrings to public functions and classes.
