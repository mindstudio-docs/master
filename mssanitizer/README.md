# MindStudio Sanitizer

## 最新消息
* [2025.12.30]：MindStudio Sanitizer项目首次上线


## 简介
MindStudio Sanitizer（算子异常检测，msSanitizer）是一种基于昇腾AI处理器AI处理器SoCNPU IP加速器的异常检测工具，包含了单算子开发场景下的内存检测、竞争检测、未初始化检测和同步检测四个子功能。用户使用msOpST工具在真实的硬件环境中对算子的功能进行测试后，可根据实际测试情况选择是否使用msSanitizer工具进行异常检测。



## 目录结构
整体目录设计如下：
```
MindStudio-Sanitizer
|-- .gitsubmodule           # 管理依赖的submodule文件
|-- build.py                # 一键式构建脚本入口
|-- CMakeLists.txt          # cmake构建入口，只包含编译过程，不包含打包
|-- cmake
    |-- CMakeLists.txt      # 集成构建cmake入口，包含打包过程
|-- csrc
   |-- address_sanitizer    # 此处提供外部信息输入接口，在明确芯片类型后，能依据输入信息，调用统一信息展示接口
      |-- config
      |--
      |-- address_sanitizer.h # 提供外部接口
   |-- core
      |-- stub_def          # 桩空间，会针对不同的文件组合生成不同场景的桩
      |-- framework         # 此处需要针对信息
         |-- parse          # 依据不同工具要求，将信息加工后提供给不同工具
         |-- msg_def.h      # 统一信息展示接口
         |-- process_ctl.h  # 整体看流程代码固定而且每个流程不多，如果不涉及针对不同工具需要抽象的，建议一个。
   |-- main.cpp
|-- msopscommon             # 公共组件子仓
|-- test
   |-- address_sanitizer
   |-- framework
|-- thirdparty              # 三方依赖子仓存放目录
|-- docs                    # 项目文档介绍
└── README.md               # 整体仓代码说明
```
---
## 环境部署
### 环境依赖
- 硬件环境请参见《[昇腾产品形态说明](https://www.hiascend.com/document/detail/zh/AscendFAQ/ProduTech/productform/hardwaredesc_0001.html)》。
- 工具的使用运行需要提前获取并安装CANN开源版本，当前CANN开源版本正在发布中，敬请期待。
### 工具安装
介绍msSanitizer工具的环境依赖及安装方式，具体请参见[MindStudio Sanitizer安装指南](./docs/zh/mssanitizer_install_guide.md)。




## 快速入门
详细操作步骤请参见[快速入门](./docs/zh/quick_start/mssanitizer_quick_start.md)。

## 工具限制与注意事项
- msSanitizer工具不支持对多线程算子及使用了掩码的向量类计算指令进行检测。
- check-device-heap或--check-cann-heap使能后，将不会对Kernel内进行检测。Device侧内存检测和CANN软件栈内存检测不能同时使能，若同时使能会提示“CANNOT enable both --check-cann-heap and --check-device-heap”。
- 使用msSanitizer工具提供的API头文件重新编译的待检测程序只能用于Ascend CL系列接口的泄漏检测，无法用于Device接口的检测。



## 功能介绍
msSanitizer通过不同子功能提供了不同类型的异常检测功能，目前已支持的功能如下：
| 功能 | 使用说明  |
|---------|--------|
| [内存检测](./docs/zh/mssanitizer_user_guide.md#内存检测) |内存检测是针对用户程序运行时的一种异常检测，该工具可以检测并报告算子运行中对外部存储（Global Memory）和内部存储（Local Memory）的越界及未对齐等内存访问异常。 |
| [竞争检测](./docs/zh/mssanitizer_user_guide.md#竞争检测) | 竞争检测用于解决在并行计算环境中内存访问竞争的问题。 |
| [未初始化检测](./docs/zh/mssanitizer_user_guide.md#未初始化检测)  | 未初始化检测功能是一种重要的内存安全保护机制，旨在识别并防止由于使用未初始化的变量而导致的内存异常。 |
|  [同步检测](./docs/zh/mssanitizer_user_guide.md#同步检测)   |在Ascend C算子开发过程中，必须成对使用SetFlag和WaitFlag，同步检测功能用于找出算子中未配对的SetFlag指令。 |


## API参考
msSanitizer工具包含sanitizer接口和mstx扩展接口两种类型。具体内容请参见[MindStudio Sanitizer对外接口使用说明](./docs/zh/mssanitizer_api_reference.md)。

## FAQ
msSanitizer工具常见问题请参见[FAQ](./docs/zh/faq.md)。


## 典型案例
msSanitizer工具通过一些典型案例帮助用户理解并熟悉工具，具体案例请参见[MindStudio Sanitizer典型案例](./docs/zh/example.md)。

## 免责声明
### 致msSanitizer使用者
- 本工具仅供调试和开发之用，使用者需自行承担使用风险，并理解以下内容：
    - 数据处理及删除：用户在使用本工具过程中产生的数据属于用户责任范畴。建议用户在使用完毕后及时删除相关数据，以防信息泄露。
    - 数据保密与传播：使用者了解并同意不得将通过本工具产生的数据随意外发或传播。对于由此产生的信息泄露、数据泄露或其他不良后果，本工具及其开发者概不负责。
    - 用户输入安全性：用户需自行保证输入的命令行的安全性，并承担因输入不当而导致的任何安全风险或损失。对于由于输入命令行不当所导致的问题，本工具及其开发者概不负责。
- 免责声明范围：本免责声明适用于所有使用本工具的个人或实体。使用本工具即表示您同意并接受本声明的内容，并愿意承担因使用该功能而产生的风险和责任，如有异议请停止使用本工具。
- 在使用本工具之前，请谨慎阅读并理解以上免责声明的内容。对于使用本工具所产生的任何问题或疑问，请及时联系开发者。
### 致数据所有者
如果您不希望您的模型或数据集等信息在msSanitizer中被提及，或希望更新msSanitizer中有关的描述，请在Gitcode提交issue，我们将根据您的issue要求删除或更新您相关描述。衷心感谢您对msSanitizer的理解和贡献。

## License

msSanitizer产品的使用许可证，具体请参见[LICENSE](./LICENSE)文件。  
msSanitizer工具docs目录下的文档适用CC-BY 4.0许可证，具体请参见[LICENSE](./docs/LICENSE)。


## 贡献声明
1. 提交错误报告：如果您在msSanitizer中发现了一个不存在安全问题的漏洞，请在msSanitizer仓库中的Issues中搜索，以防该漏洞已被提交，如果找不到漏洞可以创建一个新的Issues。如果发现了一个安全问题请不要将其公开，请参阅安全问题处理方式。提交错误报告时应该包含完整信息。
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

欢迎大家为社区做贡献。如果有任何疑问或建议，请提交[Issues](https://gitcode.com/Ascend/mssanitizer/issues)，我们会尽快回复。感谢您的支持。

##  致谢

msSanitizer由华为公司的下列部门联合贡献：

- 计算产品线

感谢来自社区的每一个PR，欢迎贡献msSanitizer。
