# MindStudio Ops Tuner

# 最新消息
* [2025.12.30]：MindStudio Ops Tuner项目首次上线 

# 简介
MindStudio Ops Tuner（算子Tiling寻优，msOpTuner）是一款用于 CATLASS 模板库算子 Tiling 参数寻优的工具，支持用户自定义搜索空间，能够实例化搜索空间内的所有算子，并批量完成在板性能测试，为算子 Tiling 参数的寻优提供参考依据。

# 目录结构
针对该软件仓，整体目录设计思路如下：
```shell
MindStudio-Ops-Tuner
├── .gitsubmodules           # 管理依赖的submodule文件
├── library                  # 算子用例库
│      ├── scripts           # 代码生成脚本
│      ├── include
│      └── src  
├── tuner                    # 命令行工具
│      ├── dfx_kernel
│      ├── include
│      └── src     
├── test                     # 测试部分
├── CMakeLists.txt           # cmake工程入口
├── build.py                 # 一键式构建脚本入口
|-- docs                    # 项目文档介绍
└── README.md               # 整体仓代码说明
```
---

# 环境部署
## 环境依赖
- 硬件环境请参见《[昇腾产品形态说明](https://www.hiascend.com/document/detail/zh/AscendFAQ/ProduTech/productform/hardwaredesc_0001.html)》。
- 工具的使用运行需要提前获取并安装CANN开源版本，当前CANN开源版本正在发布中，敬请期待。
## 工具安装
介绍msOpTuner工具的环境依赖及安装方式，具体请参见[msOpTuner安装指南](./docs/zh/msoptuner_install_guide.md)。


# 免责声明
## 致msOpTuner使用者
- 本工具仅供调试和开发之用，使用者需自行承担使用风险，并理解以下内容：
    - 数据处理及删除：用户在使用本工具过程中产生的数据属于用户责任范畴。建议用户在使用完毕后及时删除相关数据，以防信息泄露。
    - 数据保密与传播：使用者了解并同意不得将通过本工具产生的数据随意外发或传播。对于由此产生的信息泄露、数据泄露或其他不良后果，本工具及其开发者概不负责。
    - 用户输入安全性：用户需自行保证输入的命令行的安全性，并承担因输入不当而导致的任何安全风险或损失。对于由于输入命令行不当所导致的问题，本工具及其开发者概不负责。
- 免责声明范围：本免责声明适用于所有使用本工具的个人或实体。使用本工具即表示您同意并接受本声明的内容，并愿意承担因使用该功能而产生的风险和责任，如有异议请停止使用本工具。
- 在使用本工具之前，请谨慎阅读并理解以上免责声明的内容。对于使用本工具所产生的任何问题或疑问，请及时联系开发者。
## 致数据所有者
如果您不希望您的模型或数据集等信息在msOpTuner中被提及，或希望更新msOpTuner中有关的描述，请在Gitcode提交issue，我们将根据您的issue要求删除或更新您相关描述。衷心感谢您对msOpTuner的理解和贡献。

# License

msOpTuner产品的使用许可证，具体请参见[LICENSE](./LICENSE)文件。  
msOpTuner工具docs目录下的文档适用CC-BY 4.0许可证，具体请参见[LICENSE](./docs/LICENSE)。


# 贡献声明
1. 提交错误报告：如果您在msOpTuner中发现了一个不存在安全问题的漏洞，请在msOpTuner仓库中的Issues中搜索，以防该漏洞已被提交，如果找不到漏洞可以创建一个新的Issues。如果发现了一个安全问题请不要将其公开，请参阅安全问题处理方式。提交错误报告时应该包含完整信息。
2. 安全问题处理：本项目中对安全问题处理的形式，请通过邮箱通知项目核心人员确认编辑。
3. 解决现有问题：通过查看仓库的Issues列表可以发现需要处理的问题信息, 可以尝试解决其中的某个问题。
4. 如何提出新功能：请使用Issues的Feature标签进行标记，我们会定期处理和确认开发。
5. 开始贡献：  
    a. Fork本项目的仓库。  
    b. Clone到本地。  
    c. 创建开发分支。  
    d. 本地测试：提交前请通过所有单元测试，包括新增的测试用例。  
    e. 提交代码。  
    f. 新建Pull Request。  
    g. 代码检视，您需要根据评审意见修改代码，并重新提交更新。此流程可能涉及多轮迭代。  
    h. 当您的PR获得足够数量的检视者批准后，Committer会进行最终审核。  
    i. 审核和测试通过后，CI会将您的PR合并入到项目的主干分支。

# 建议与交流

欢迎大家为社区做贡献。如果有任何疑问或建议，请提交[Issues](https://gitcode.com/Ascend/msoptuner/issues)，我们会尽快回复。感谢您的支持。


#  致谢

msOpTuner由华为公司的下列部门联合贡献：

- 计算产品线

  感谢来自社区的每一个PR，欢迎贡献msOpTuner。
