# **MindStudio Ops Generator**

## 最新消息
* [2025.12.30]：MindStudio Ops Generator项目首次上线

## 简介
MindStudio Ops Generator（算子工程创建，msOpGen）是算子开发效率提升工具，提供模板工程生成能力，简化算子工程搭建并辅助算子测试验证。完成算子分析和原型定义后，可使用msOpGen工具生成自定义算子工程。使用msOpGen工具完成自定义算子包部署后，可选择使用MindStudio Ops System Test（算子测试，msOpST）工具进行ST（System Test）测试，在真实的硬件环境中，对算子的输入输出进行测试，以验证算子的功能是否正确。

## 目录结构
整体目录设计如下：
```
├── example  // 工具样例
├── docs              // 项目文档介绍
├── msopgen  // msopgen源码目录
├── test
│     └── msopgen  // msopgen测试用例
│     └── msopst   // msopst测试用例
├── tools  // 存放一些工程相关工具，当前仅放msopst
│     └── msopst  // msopst代码目录
│           └── setup.py  // msopst whl包构建脚本
├── build  // 打包whl过程中的中间文件
├── output  // whl包输出目录、测试用例报告
├── setup.py  // msopgen whl包构建脚本
├── build.py  // 执行测试用例，生成安装包
├── requirements.txt  // python依赖库
└── README.md  // 整体仓代码说明
```


## 环境部署
#### 环境和依赖
- 硬件环境请参见《[昇腾产品形态说明](https://www.hiascend.com/document/detail/zh/AscendFAQ/ProduTech/productform/hardwaredesc_0001.html)》。
- 工具的使用运行需要提前获取并安装CANN开源版本，当前CANN开源版本正在发布中，敬请期待。
#### 工具安装
介绍msOpGen工具的环境依赖及安装方式，具体请参见[MindStudio Ops Generator安装指南](./docs/zh/msopgen_install_guide.md)。

## 快速入门
以一个简单样例介绍如何使用msOpGen工具进行算子工程创建及使用msOpST工具进行算子测试，具体内容请参见[MindStudio Ops Generator快速入门](./docs/zh/msopgen_quick_start.md)及[MindStudio Ops System Test快速入门](./docs/zh/msopst_quick_start.md)。


## 功能介绍
- msOpGen目前已支持的功能如下：包括算子工程创建、算子实现（Host侧&Kernel侧）、算子工程编译部署以及解析算子仿真流水图文件等。  

| 功能 | 使用说明  |
|---------|--------|
| [算子工程创建](./docs/zh/msopgen_user_guide.md#创建算子工程) |按照步骤执行创建算子工程 |
|[ 算子实现（Host侧&Kernel侧）](./docs/zh/msopgen_user_guide.md#算子开发)   | 按照步骤执行完成算子开发实现 |
| [算子工程编译部署](./docs/zh/msopgen_user_guide.md#算子编译部署)   | 完成算子Kernel、Host侧的开发后，需要对算子工程进行编译，生成自定义算子安装包*.run |
|  [解析算子仿真流水图文件](./docs/zh/msopgen_user_guide.md#查看算子仿真流水图) | msOpGen工具通过解析用户生成的dump文件，并生成算子仿真流水图文件（trace.json）|


- msOpST支持生成算子的ST测试用例并在硬件环境中执行。具有如下功能：

| 功能 | 使用说明  |
|---------|--------|
| [生成测试用例定义文件](./docs/zh/msopgen_user_guide.md#生成测试用例定义文件) |根据用户定义并配置的算子期望数据生成函数，回显期望算子输出和实际算子输出的对比测试结果 |
| [生成并执行测试用例](./docs/zh/msopgen_user_guide.md#生成执行测试用例)   | 根据算子测试用例定义文件生成ST测试数据及测试用例执行代码，在硬件环境上执行算子测试用例，自动生成运行报表（st_report.json）功能，报表记录了测试用例信息及各阶段运行情况 |
| [ 生成单算子上板测试框架](./docs/zh/msopgen_user_guide.md#生成单算子上板测试框架)  | 自动生成算子调用核函数的上板测试框架，进行算子的测试验证|




## 典型案例
msOpGen工具通过一些典型案例帮助用户理解并熟悉工具，具体案例请参见[MindStudio Ops Generator典型案例](./docs/zh/example.md)。

## 免责声明
### 致MindStudio Ops Generator使用者
- 本工具仅供调试和开发之用，使用者需自行承担使用风险，并理解以下内容：
    - 数据处理及删除：用户在使用本工具过程中产生的数据属于用户责任范畴。建议用户在使用完毕后及时删除相关数据，以防信息泄露。
    - 数据保密与传播：使用者了解并同意不得将通过本工具产生的数据随意外发或传播。对于由此产生的信息泄露、数据泄露或其他不良后果，本工具及其开发者概不负责。
    - 用户输入安全性：用户需自行保证输入的命令行的安全性，并承担因输入不当而导致的任何安全风险或损失。对于由于输入命令行不当所导致的问题，本工具及其开发者概不负责。
- 免责声明范围：本免责声明适用于所有使用本工具的个人或实体。使用本工具即表示您同意并接受本声明的内容，并愿意承担因使用该功能而产生的风险和责任，如有异议请停止使用本工具。
- 在使用本工具之前，请谨慎阅读并理解以上免责声明的内容。对于使用本工具所产生的任何问题或疑问，请及时联系开发者。
### 致数据所有者
如果您不希望您的模型或数据集等信息在msOpGen中被提及，或希望更新msOpGen中有关的描述，请在Gitcode提交issue，我们将根据您的issue要求删除或更新您相关描述。衷心感谢您对msOpGen的理解和贡献。

## License

msOpGen产品的使用许可证，具体请参见[LICENSE](./LICENSE)文件。  
msOpGen工具docs目录下的文档适用CC-BY 4.0许可证，具体请参见[LICENSE](./docs/LICENSE)。


## 贡献声明
1. 提交错误报告：如果您在msOpGen中发现了一个不存在安全问题的漏洞，请在msOpGen仓库中的Issues中搜索，以防该漏洞已被提交，如果找不到漏洞可以创建一个新的Issues。如果发现了一个安全问题请不要将其公开，请参阅安全问题处理方式。提交错误报告时应该包含完整信息。
2. 安全问题处理：本项目中对安全问题处理的形式，请通过邮箱通知项目核心人员确认编辑。
3. 解决现有问题：通过查看仓库的Issues列表可以发现需要处理的问题信息, 可以尝试解决其中的某个问题。
4. 如何提出新功能：请使用Issues的Feature标签进行标记，我们会定期处理和确认开发。
5. 开始贡献：  
    1. Fork本项目的仓库。  
    2. Clone到本地。  
    3. 创建开发分支。  
    4. 本地测试：提交前请通过所有单元测试，包括新增的测试用例。  
    5. 提交代码。  
    6. 新建Pull Request。  
    7. 代码检视，您需要根据评审意见修改代码，并重新提交更新。此流程可能涉及多轮迭代。  
    8. 当您的PR获得足够数量的检视者批准后，Committer会进行最终审核。  
    9. 审核和测试通过后，CI会将您的PR合并入到项目的主干分支。

## 建议与交流

欢迎大家为社区做贡献。如果有任何疑问或建议，请提交[Issues](https://gitcode.com/Ascend/msopgen/issues)，我们会尽快回复。感谢您的支持。

##  致谢

msOpGen由华为公司的下列部门联合贡献：

- 计算产品线

感谢来自社区的每一个PR，欢迎贡献msOpGen。

