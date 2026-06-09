# 为 MindStudio Tools Extension Library 贡献

感谢您考虑为 MindStudio Tools Extension Library（msTX）做出贡献！我们欢迎任何形式的贡献，包括错误修复、功能增强、文档改进等，甚至只是反馈。无论您是经验丰富的开发者还是第一次参与开源项目，您的帮助都是非常宝贵的。

您可以通过多种方式支持本项目：

- 通过 [Issues](https://gitcode.com/Ascend/mstx/issues) 反馈问题。
- 建议或实现新功能。
- 改进或扩展文档。
- 审查 Pull Request 并协助其他贡献者。

---

## 1. 贡献流程

### 1.1 环境要求

| 项目       | 要求                                    |
| ---------- | --------------------------------------- |
| 操作系统   | Linux（OpenEuler / Ubuntu 18.04+）      |
| C/C++ 编译器 | GCC 7.3+（支持 C++11）               |
| CMake      | 3.16+                                   |
| Python     | 3.7+（编译绑定需要 python3-dev）        |

### 1.2 开发与测试

1. **Fork 仓库**

   ```bash
   git clone https://gitcode.com/<your-username>/mstx.git
   cd mstx
   ```

2. **代码开发**

   代码开发请遵循[第 2 节代码规范](#2-代码规范)。

3. **代码测试**

   参见[第 3 节代码测试](#3-代码测试)。

4. **编译验证**

   将开发完成的代码编译验证，详细步骤请参见 [msTX 开发指南](../development_guide/develop_guide.md)。

5. **文档开发**

   若涉及新增、变更或删除特性，请同步更新相关文档，详细要求请参见[第 4 节文档开发](#4-文档开发)。

6. **提交 Pull Request**

   参见[第 5 节提交 Pull Request 流程](#5-提交-pull-request-流程)。

---

## 2. 代码规范

### 2.1 C/C++ 规范

- 使用 4 个空格进行缩进
- 公开接口声明在 `c/include/mstx/` 头文件中，使用 `extern "C"` 保证 C 语言兼容
- 函数命名遵循 `mstx<Module><Action><Variant>` 模式（如 `mstxDomainCreateA`）
- 类名使用大驼峰命名法；变量和函数使用小驼峰命名法
- 添加必要的注释说明复杂逻辑

### 2.2 Python 规范

- 遵循 PEP 8 编码规范
- 使用 4 个空格进行缩进
- 类名使用大驼峰命名法（如 `BuildManager`）
- 函数和变量使用小写加下划线命名法（如 `download_dependencies`）
- 添加必要的类型注解和文档字符串

### 2.3 pre-commit 自动检查

项目配置了 [pre-commit](https://pre-commit.com/) 钩子，在提交代码时自动执行格式检查和规范校验，帮助提前发现问题。

#### 安装 pre-commit

```bash
pip install pre-commit
```

在仓库根目录执行以下命令安装钩子：

```bash
pre-commit install
```

安装后，每次执行 `git commit` 时都会自动运行检查。

#### 检查内容

| 检查项 | 工具 | 说明 |
|--------|------|------|
| 行尾空格 | trailing-whitespace | 自动删除行尾多余空格 |
| 文件末尾换行 | end-of-file-fixer | 确保文件以换行符结尾 |
| YAML 格式 | check-yaml | 校验 `.yaml`/`.yml` 文件语法 |
| JSON 格式 | check-json | 校验 `.json` 文件语法 |
| 大文件检查 | check-added-large-files | 阻止意外提交大文件 |
| 合并冲突标记 | check-merge-conflict | 检查是否残留冲突标记 |
| 私钥泄露 | detect-private-key | 检测是否误提交私钥 |
| 拼写检查 | codespell + typos | 英文拼写检查（已排除 CANN、Ascend 等领域专有名词） |
| C++ 代码格式化 | clang-format | 自动格式化 C/C++ 源码（`*.c`、`*.h`、`*.cpp`、`*.hpp` 等） |

#### 手动运行

如需在不提交的情况下手动检查：

```bash
pre-commit run
```

#### 跳过检查（不推荐）

特殊情况可临时跳过钩子：

```bash
git commit --no-verify -m "your message"
```

> [!WARNING]
> 跳过检查可能导致 CI 流水线不通过，请谨慎使用。

---

## 3. 代码测试

### 3.1 运行测试

在提交代码前，请确保所有测试通过：

```sh
# 一键运行全部测试
python build.py test
```

### 3.2 添加测试

- 为新功能添加相应的单元测试
- 确保测试覆盖主要逻辑分支
- C/C++ 测试放在 `test/c/` 目录下
- Python 测试放在 `test/python/` 目录下

### 3.3 代码覆盖率

```sh
bash test/scripts/generate_coverage.sh
```

---

## 4. 文档开发

### 4.1 文档路径

如果您的更改影响用户使用方式，请更新相关文档：

- API 参考：`docs/zh/api_reference/`
- 安装指南：`docs/zh/install_guide/`
- 开发指南：`docs/zh/development_guide/`
- 版本说明：`docs/zh/release_notes/`

### 4.2 文档规范

- 使用简洁明了的中文表述
- 提供完整的示例代码
- 确保链接的有效性

---

## 5. 提交 Pull Request 流程

### 5.1 提交前检查清单

在提交 Pull Request 之前，请确保：

- [ ] 代码遵循项目的编码规范
- [ ] 添加了必要的测试用例
- [ ] 所有测试通过
- [ ] 更新了相关文档
- [ ] 提交信息清晰明确
- [ ] 代码已经过自我审查

### 5.2 提交流程

1. **创建分支**

   ```bash
   git checkout -b feature/<your-feature-name>
   ```

2. **提交更改**

   ```bash
   git add .
   git commit -m "feat: <your feature description>"
   ```

3. **推送到远程仓库**

   ```bash
   git push origin feature/<your-feature-name>
   ```

4. **创建 Pull Request**

   在 GitCode 上创建 Pull Request，并填写：

   - 清晰的标题，遵循[提交信息规范](#53-提交信息规范)
   - 详细的描述，包括更改内容、原因、测试情况等
   - 关联相关的 Issue

5. **代码审查**

   - 提交 PR 后，通知相关负责人进行内容审核
   - 根据反馈意见修改代码，并重新提交更新。此流程可能涉及多轮迭代
   - 相关负责人可在 PR 流程中指定，或通过 [README](../../../README.md) 联系 MindStudio 团队

6. **代码合并**

   PR 需要依次集齐如下四个标签即可完成代码合入：

   | 标签 | 说明 |
   |------|------|
   | `ascend-cla/yes` | CLA 检查，首次开发需签署 CLA，完成后每次提交自动获得 |
   | `ci-pipeline-passed` | CI 流水线，在 PR 中评论 `compile` 触发 |
   | `lgtm` | Reviewers 审核通过后在 PR 中评论 `/lgtm` 触发 |
   | `approved` | Committers 审核通过后在 PR 中评论 `/approved` 触发 |

### 5.3 提交信息规范

提交信息应该清晰地描述更改的内容和原因：

```bash
<type>: <subject>

<body>

<footer>
```

类型（type）包括：

- `feature`：新功能
- `bugfix`：错误修复
- `doc`：文档更新
- `refactor`：代码重构
- `test`：测试相关

示例：

```bash
[feature]: 添加内存追踪 API 支持

- 实现 mstxMemHeapRegister / mstxMemRegionsRegister 接口
- 提供功能实现截图
- 提供UT通过截图
```

### 5.4 Pull Request 最佳实践

- 保持 PR 的大小适中，便于审查
- 一个 PR 只解决一个问题或实现一个功能
- 及时响应审查意见
- 保持与主分支同步，及时解决冲突

---

## 6. 社区准则

### 6.1 行为准则

我们致力于为所有参与者提供一个友好、安全和包容的环境。参与本项目即表示您同意：

- 尊重不同的观点和经验
- 接受建设性的批评
- 关注对社区最有利的事情
- 对其他社区成员表示同理心

### 6.2 沟通渠道

- **Issues**：用于报告 Bug、提出功能建议和讨论技术问题
- **Pull Requests**：用于代码审查和讨论具体实现

---

## 致谢

感谢您为 msTX 做出的贡献。您的努力使这个项目变得更加强大和用户友好。期待您的参与！

如有任何疑问或需要帮助，请随时在 [Issues](https://gitcode.com/Ascend/mstx/issues) 中提问。
