<h1 align="center">MindStudio-Ops-Modeling</h1>

<div align="center">
<h2>昇腾 AI 算子性能建模工具</h2>

 [![Powered by TileSim](https://img.shields.io/badge/Powered%20by-TileSim-blue)](./README.md)
 [![Ascend](https://img.shields.io/badge/Community-MindStudio-blue.svg)](https://www.hiascend.com/developer/software/mindstudio) 
 [![License](https://badgen.net/badge/License/MulanPSL-2.0/blue)](./LICENSE)

</div>

## ✨ 最新消息

<span style="font-size:14px;">

🔹 **[2026.04.13]**：本项目启动上线

</span>

## ℹ️ 简介

MindStudio-Ops-Modeling（msOpModeling）算子性能建模工具，基于 **TileSim** (由 **2012马尔科夫实验室** 自研的仿真引擎)，支持理论（Roofline 模型）与工程（Tile 级仿真）双模性能预测；通过 JSON 即可评估内置算子或基于 DSL 扩展自定义算子，实现免上板的高精度性能预测。

## ⚙️ 功能介绍

通过多个子功能模块提供 NPU 算子性能的预测与建模能力，当前已支持的功能如下：

| 功能名称 | 功能描述 |
|---------|--------|
| **理论极限性能建模** | 给定 Tensor 级运算逻辑与少量微架构信息，预测算子忽略流水/同步开销下的 E2E 上限性能。 |
| **工程可达性能建模** | 给定 Tile 级搬运与运算逻辑及详细微架构参数，通过 SnowCat 模型预测最优 tiling 下的真实时延。 |
| **DSL 算子建模前端** | 提供基于 Python 的 DSL 语言，以理论和工程两种粒度描述算子逻辑，无需手动编写搬运或同步代码。 |

## 🧠 核心引擎

本工具的性能预测能力由 **TileSim** 全面驱动。**TileSim** 是由 **2012马尔科夫实验室** 自主研发的 Tile 级 NPU 仿真引擎；该华为实验室长期深耕复杂系统建模与仿真基础技术研究。作为面向 NPU 算子性能建模的重要底层引擎，TileSim 为 msOpModeling 提供了高精度的 Tile 级仿真能力，团队将长期深度参与项目核心能力建设，不断夯实底层建模与仿真能力。

## 🚀 快速入门

2分钟快速体验核心功能，请参见 [《msOpModeling 快速入门》](docs/zh/quick_start/msopmodeling_quick_start.md)。

## 📦 安装指南

介绍工具的环境依赖与安装方法，请参见 [《msOpModeling 安装指南》](docs/zh/install_guide/msopmodeling_install_guide.md)。

## 📘 使用指南

工具的详细使用方法，请参见 [《msOpModeling 使用指南》](docs/zh/user_guide/msopmodeling_user_guide.md)。

## 📚 API参考

扩展自定义算子的 DSL API 接口信息，请参见 [《msOpModeling API说明》](src/tilesim/docs/OPERATOR_MODELING_GUIDE.md)。

## 🛠️ 贡献指南

欢迎参与项目贡献，请参见 [《贡献指南》](./docs/zh/contributing/contributing_guide.md)。  

## ⚖️ 相关说明

🔹 [《版本说明》](./docs/zh/release_notes/release_notes.md)  
🔹 [《许可证声明》](./docs/zh/legal/license_notice.md)  
🔹 [《安全声明》](./docs/zh/legal/security_statement.md)  
🔹 [《免责声明》](./docs/zh/legal/disclaimer.md)  

## 🤝 建议与交流

欢迎大家为社区做贡献。如果有任何疑问或建议，请提交 [Issues](https://gitcode.com/Ascend/msopmodeling/issues)，我们会尽快回复。感谢您的支持。

|                                      📱 关注 MindStudio 公众号                                       | 💬 更多交流与支持                                                                                                                                                                                                                                                                                                                                                                                                                     |
|:-----------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <img src="https://gitcode.com/Ascend/msot/blob/master/docs/zh/figures/readme/officialAccount.png" width="120"><br><sub>*扫码关注获取最新动态*</sub> | 💡 **加入微信交流群**：<br>关注公众号，回复“交流群”即可获取入群二维码。<br><br>🛠️ **其他渠道**：<br>👉 昇腾助手：[![WeChat](https://img.shields.io/badge/WeChat-07C160?style=flat-square&logo=wechat&logoColor=white)](https://gitcode.com/Ascend/msot/blob/master/docs/zh/figures/readme/xiaozhushou.png)<br>👉 昇腾论坛：[![Website](https://img.shields.io/badge/Website-%231e37ff?style=flat-square&logo=RSS&logoColor=white)](https://www.hiascend.com/forum/) |

## 🙏 致谢

本工具由华为公司的下列部门联合贡献：    
🔹 昇腾计算MindStudio开发部  
🔹 2012马尔科夫实验室  
🔹 华为云昇腾云服务  
感谢来自社区的每一个 PR，欢迎贡献！
