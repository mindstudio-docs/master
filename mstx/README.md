<h1 align="center">MindStudio Tools Extension Library</h1>

<div align="center">
<h2>昇腾 AI 算子工具扩展接口库</h2>
  
 [![Ascend](https://img.shields.io/badge/Community-MindStudio-blue.svg)](https://www.hiascend.com/developer/software/mindstudio) 
 [![License](https://badgen.net/badge/License/MulanPSL-2.0/blue)](./LICENSE)

</div>

## ✨ 最新消息

<span style="font-size:14px;">

🔹 **[2025.12.31]**：MindStudio Tools Extension Library 项目全面开源

</span>

## ️ ℹ️ 简介

MindStudio Tools Extension Library（工具扩展接口库，msTX）介绍msTX打点接口。可以自定义采集时间段或者关键函数的开始和结束时间点，识别关键函数或迭代等信息，对性能和算子问题快速定界。

## ⚙️ 功能介绍

默认情况下mstx API无任何功能，需要在用户应用程序中调用mstx API后，根据不同场景使能mstx打点功能，例如使用msprof命令行采集时配置--mstx=on、使用AscendCL API采集时配置ACL_PROF_MSPROFTX以及Ascend PyTorch Profiler接口采集时配置mstx=True等。

## 📦 安装指南

介绍工具的环境依赖与安装方法，请参见《[msTX 安装指南](docs/zh/install_guide/mstx_install_guide.md)》。

## 💡 典型案例

典型使用场景请参见《[msOpProf工具 mstx扩展功能](https://gitcode.com/Ascend/msopprof/blob/master/docs/zh/user_guide/extended_functions.md#mstx扩展功能)》和《[msSanitizer工具 mstx扩展功能](https://gitcode.com/Ascend/mssanitizer/blob/master/docs/zh/api_reference/mssanitizer_api_reference.md#mstx扩展功能)》。

## 📚 API参考

msTX接口具体内容请参见《[msTX 接口参考](docs/zh/api_reference/README.md)》。

## 🛠️ 贡献指南

欢迎参与项目贡献，请参见《[贡献指南](./docs/zh/contributing/contributing_guide.md)》。  

## ⚖️ 相关说明

🔹《[版本说明](./docs/zh/release_notes/release_notes.md)》  
🔹《[许可证声明](./docs/zh/legal/license_notice.md)》  
🔹《[安全声明](./docs/zh/legal/security_statement.md)》  
🔹《[免责声明](./docs/zh/legal/disclaimer.md)》   

## 🤝 建议与交流

欢迎大家为社区做贡献。如果有任何疑问或建议，请提交[Issues](https://gitcode.com/Ascend/mstx/issues)，我们会尽快回复。感谢您的支持。

|                                      📱 关注 MindStudio 公众号                                       | 💬 更多交流与支持                                                                                                                                                                                                                                                                                                                                                                                                                     |
|:-----------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <img src="https://gitcode.com/Ascend/msot/blob/master/docs/zh/figures/readme/officialAccount.png" width="120"><br><sub>*扫码关注获取最新动态*</sub> | 💡 **加入微信交流群**：<br>关注公众号，回复“交流群”即可获取入群二维码。<br><br>🛠️ **其他渠道**：<br>👉 昇腾助手：[![WeChat](https://img.shields.io/badge/WeChat-07C160?style=flat-square&logo=wechat&logoColor=white)](https://gitcode.com/Ascend/msot/blob/master/docs/zh/figures/readme/xiaozhushou.png)<br>👉 昇腾论坛：[![Website](https://img.shields.io/badge/Website-%231e37ff?style=flat-square&logo=RSS&logoColor=white)](https://www.hiascend.com/forum/) |

## 🙏 致谢

本工具由华为公司的下列部门联合贡献：    
🔹 昇腾计算MindStudio开发部  
🔹 昇腾计算生态使能部  
🔹 华为云昇腾云服务  
🔹 2012编译器实验室  
🔹 2012马尔科夫实验室  
感谢来自社区的每一个 PR，欢迎贡献！
