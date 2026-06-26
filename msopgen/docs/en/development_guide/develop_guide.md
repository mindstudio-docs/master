# MindStudio msOpGen Development Environment Setup and UT Methods

<br>

## 1. Background Knowledge Required

Before developing msOpGen, understand the following basics:

- **Python project structure**: msOpGen is a Python-based CLI tool. Source code is in the `msopgen/` directory, built with `setuptools`.
- **Tool components**: msOpGen handles operator project generation (`msopgen gen`) and simulation pipeline parsing (`msopgen sim`). msOpST handles ST test case generation and execution (`msopst create/run`).
- For detailed architecture design and module descriptions, see [msOpGen Architecture Design](./architecture.md).

## 2. Development Environment Setup

Please configure the environment in accordance with the document: .[《Installation Guide for Operator Tool Development Environment》](https://gitcode.com/Ascend/msot/blob/master/docs/zh/common/dev_env_setup.md)

## 3. One-Click Build

```shell
python build.py
```

The generated `.whl` packages are stored in the `output/` directory, including both `mindstudio_opgen` and `mindstudio_opst`.

## 4. Project Directory Structure

```text
├── msopgen/          // msopgen source code (core engine)
├── tools/msopst/     // msopst source code (ST test tool)
├── test/
│   ├── msopgen/      // msopgen unit tests
│   └── msopst/       // msopst unit tests
├── example/          // Tool examples
├── docs/             // Project documentation
├── setup.py          // msopgen WHL build script
├── build.py          // Build entry script
└── requirements.txt  // Python dependencies
```

## 5. UT Testing

```shell
python build.py test
```

### 5.1 Test Coverage Scope

UT tests cover the following core functionality:
- Operator project template generation (`msopgen gen`)
- Simulation pipeline parsing (`msopgen sim`)
- ST test case generation (`msopst create`)
- ST test case execution (`msopst run`)

## 6. Coding Standards

- New features must include corresponding UT test cases
- Public functions and classes must include docstring documentation
