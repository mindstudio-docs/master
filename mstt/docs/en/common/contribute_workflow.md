# Contribution Workflow and Guidelines

<br>

Thank you for considering contributing to this project! We welcome any form of contribution, including bug fixes, feature enhancements, documentation improvements, and even simple usage feedback.  
Whether you are an experienced developer or a first-time open source contributor, your contribution is highly valued.

You can support this project in the following ways:

- **Code Contributions**: Fix known bugs, optimize performance, refactor improvements, or implement new features. Follow the [Contribution Workflow](#1-contribution-workflow) and [Code Guidelines](#2-code-guidelines) when committing code.
- **Issue Feedback**: Report bugs, propose features, ask questions through Issues, or participate in requirement reviews and solution discussions.
- **Documentation Improvements**: Correct errors, fill in missing content, improve phrasing, or write usage examples and tutorials. Follow the [Documentation Guidelines](#3-documentation-guidelines).
- **Quality Assurance**: Add or improve test cases, review Pull Requests (PRs) and provide constructive feedback, and help other contributors improve code quality.
- **Community Promotion**: Answer questions in Issues/PRs, share usage experiences and best practices, or promote the project by writing blogs, tutorials, and sharing on tech communities and social media.

## 1. Contribution Workflow

1. **Repository Forking**: Fork the source code repository to your private repository, then clone it to your local development environment.
2. **Branch Creation**: Create a feature branch based on the latest main branch. The branch name should be concise and reflect the change (e.g., `fix_xxx_bug`, `feature_xxx`).
3. **Code Development**: Develop on the feature branch. Follow the [Code Guidelines](#2-code-guidelines) and keep commits clear and atomic.
4. **Local Testing**: Perform thorough functional tests on the code. Supplement unit tests as needed based on the developed module, ensuring all tests pass.
5. **Documentation Update**: Supplement or update documentation related to your changes, following the [Documentation Guidelines](#3-documentation-guidelines).
6. **Request Merge**: Submit a PR following the [Pull Request Guidelines](#4-pull-request-guidelines). For detailed steps, see the [Pull Request Process](#5-pull-request-process).
7. **Merge Tracking**: Follow the PR progress, respond promptly to review comments, and update the code until it is reviewed and merged into the main branch.

<br>

## 2. Code Guidelines

### 2.1 Python Code Guidelines

- **Coding Standards**: Follow [PEP 8](https://peps.python.org/pep-0008/). It is recommended to use `flake8` or `pylint` for static checks.
- **Style Requirements**: Line length should not exceed 120 characters. Functions longer than 30 lines should be considered for splitting to improve readability.
- **Comment Requirements**: Complex logic and public interfaces must have comments. Modules, classes, and key functions should include docstrings describing purpose, parameters, and return values.
- **Exception Handling**: Handle exceptions properly. Do not suppress exceptions without handling or logging. Ensure resources are released on critical paths.

### 2.2 C++ Code Guidelines

- **Style Consistency**: Follow the existing coding style of the project and maintain consistency with surrounding code.
- **Naming Conventions**: Class and struct names in PascalCase (e.g., `DataManager`), function names in camelCase (e.g., `parseData`).
- **Comment Requirements**: Complex logic and public interfaces must have comments explaining functionality, parameters, and return values.
- **Exception Handling**: Handle exceptions properly. Do not suppress exceptions without handling or logging. Use RAII for resource acquisition to ensure exception safety.

## 3. Documentation Guidelines

- **Concise Phrasing**: Use clear and concise phrasing, avoid ambiguity and redundancy, and keep technical terms consistent.
- **Clear Structure**: Use clear heading levels and logical section divisions. Highlight important conclusions or notes as needed.
- **Complete Samples**: Provide complete, runnable code samples, specify the runtime environment or dependencies, and include explanations for key steps.
- **Illustrations**: Use necessary diagrams or screenshots for complex workflows, configuration items, or UI operations to aid understanding.

## 4. Pull Request Guidelines

- **Moderate Size**: Keep individual PRs concise to help reviewers understand and provide feedback quickly.
- **Single Responsibility**: One PR should solve one problem or implement one feature, facilitating backtracking and merge.
- **Timely Response**: Respond to review comments and update the code promptly to avoid blocking the merge process.

<br>

## 5. Pull Request Process

### 5.1 Pre-commit Checklist

Before committing a PR, ensure that:

- [ ] Code follows the project's coding guidelines.
- [ ] Necessary test cases have been added.
- [ ] All tests pass.
- [ ] Related documentation has been updated.
- [ ] Commit messages are clear and explicit.
- [ ] Code has been self-reviewed.

### 5.2 Creating a PR

When creating a PR on [GitCode](https://gitcode.com/), complete the following:

1. **Title**: Briefly summarize the theme or functionality of this change.
2. **Description**: Explain what was changed, the reason for the change, and self-testing details (including environment and results) to help reviewers understand.
3. **Linked Issues**: Associate the PR with an Issue for traceability.

### 5.3 Code Review

1. After committing the PR, it will be reviewed by Reviewers and Committers.
2. Modify the code based on review comments and push updates. Multiple iterations may be required. Respond promptly and maintain communication.

### 5.4 Code Merge

A PR requires the following four labels to be merged into the main branch:

| Label | Description |
|-------|-------------|
| `ascend-cla/yes` | **CLA Signed**: First-time contributors must complete CLA signing. Subsequent contributions will automatically receive this label. |
| `ci-pipeline-passed` | **CI Passed**: Trigger the pipeline by commenting `compile` on the PR. If it fails, follow the prompts to fix it and resubmit. |
| `lgtm` | **Reviewer Approved**: Granted after two Reviewers approve by commenting `/lgtm`. |
| `approved` | **Committer Approved**: Granted after Committers approve by commenting `/approved`. |

Once the PR obtains all four labels, it will be merged into the main branch.
