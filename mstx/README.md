<h1 align="center">MindStudio Tools Extension Library</h1>

<div align="center">
<p><b><span style="font-size:24px;">昇腾 AI 算子工具扩展接口库</span></b></p>

 [![AI问答(DeepWiki)](https://badgen.net/badge/AI问答/DeepWiki/blue)](https://deepwiki.com/mindstudio-docs/master)
 [![AI问答(ZRead)](https://badgen.net/badge/AI问答/ZRead/blue)](https://zread.ai/mindstudio-docs/master)
 [![精确搜索](https://badgen.net/badge/精确搜索/ReadTheDocs/blue)](https://mindstudio-operator-tools-docs.readthedocs.io/zh-cn/latest/)
 [![昇腾社区](https://badgen.net/badge/昇腾社区/Community/blue)](https://www.hiascend.com/cn/developer/software/mindstudio)
 [![报告问题](https://badgen.net/badge/报告问题/Issues/blue)](https://gitcode.com/Ascend/mstx/issues)

</div>

## ✨ 最新消息

<span style="font-size:14px;">

🔹 **[2025.12.31]**：MindStudio Tools Extension Library 项目全面开源

</span>

## ️ ℹ️ 简介

MindStudio Tools Extension Library（工具扩展接口库，msTX）介绍msTX打点接口。可以自定义采集时间段或者关键函数的开始和结束时间点，识别关键函数或迭代等信息，对性能和算子问题快速定界。

## ⚙️ 功能介绍

默认情况下mstx API无任何功能，需要在用户应用程序中调用mstx API后，根据不同场景使能mstx打点功能，例如使用msprof命令行采集时配置--mstx=on、使用AscendCL API采集时配置ACL_PROF_MSPROFTX以及Ascend PyTorch Profiler接口采集时配置mstx=True等。

## 🌌 智能检索

为提升文档查阅效率，我们提供多种高效检索方式：  
🔹 [AI 问答（DeepWiki）](https://deepwiki.com/mindstudio-docs/master)：自然语言问答，快速把握项目架构与模块关系。   
🔹 [AI 问答（ZRead）](https://zread.ai/mindstudio-docs/master)：中文问答体验更优，精准定位功能用法与细节。   
🔹 [精确搜索（ReadTheDocs）](https://mindstudio-operator-tools-docs.readthedocs.io/zh-cn/latest/)：关键词全文检索，直达接口、参数与报错等信息。  

## 📦 安装指南

介绍工具的环境依赖与安装方法，请参见《[msTX 安装指南](docs/zh/install_guide/mstx_install_guide.md)》。

## 💡 典型案例

典型使用场景请参见《[msOpProf工具 mstx扩展功能](https://gitcode.com/Ascend/msopprof/blob/master/docs/zh/user_guide/extended_functions.md#mstx扩展功能)》和《[msSanitizer工具 mstx扩展功能](https://gitcode.com/Ascend/mssanitizer/blob/master/docs/zh/api_reference/mssanitizer_api_reference.md#mstx扩展功能)》。

## 📚 API参考

msTX接口具体内容请参见《[msTX 接口参考](docs/zh/api_reference/README.md)》。

## 🛠️ 贡献指南

欢迎参与项目贡献，请参见《[贡献指南](./docs/zh/contributing/contributing_guide.md)》。  

## ⚖️ 相关说明

🔹《[版本说明](https://gitcode.com/Ascend/mstx/releases)》  
🔹《[许可证声明](./docs/zh/legal/license_notice.md)》  
🔹《[安全声明](./docs/zh/legal/security_statement.md)》  
🔹《[免责声明](./docs/zh/legal/disclaimer.md)》   

## 🤝 建议与交流

欢迎大家为社区做贡献。如果有任何疑问或建议，请提交 [Issues](https://gitcode.com/Ascend/mstx/issues)，我们会尽快回复。感谢您的支持。

|                                                                            即时互动（微信群）                                                                             |                                                                                  官方资讯（公众号）                                                                                   | 深度支持（助手/论坛）                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|:------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <img src="https://raw.gitcode.com/Ascend/docs/files/master/common/Writing_Template/figures/qr_code_wechat_work.png" width="120"><br><sub>*扫码加入技术交流群*</sub> | <img src="https://raw.gitcode.com/Ascend/docs/files/master/common/Writing_Template/figures/qr_code_wechat_official_account.png" width="120"><br><sub>*扫码关注官方公众号*</sub> | 扫码入群并关注公众号，直达 MindStudio 用户与开发者最快捷的交流平台：<br> **快速提问：** 与社区小伙伴即时探讨技术问题<br>**掌握动态：** 第一时间获取版本发布与功能更新通知<br> **经验共享：** 与广大开发者交流最佳实践与实战心得  <br> <br> **更多支持渠道**：👉 昇腾助手：[![WeChat](https://img.shields.io/badge/WeChat-07C160?style=flat-square&logo=wechat&logoColor=white)](https://gitcode.com/Ascend/msit/blob/master/docs/zh/figures/readme/xiaozhushou.png) 👉 昇腾论坛：[![Website](https://img.shields.io/badge/Website-%231e37ff?style=flat-square&logo=RSS&logoColor=white)](https://www.hiascend.com/forum/) |

## 🙏 致谢

本工具由华为公司的下列部门联合贡献：    
🔹 昇腾计算MindStudio开发部  
🔹 昇腾计算生态使能部  
🔹 华为云昇腾云服务  
🔹 2012编译器实验室  
🔹 2012马尔科夫实验室  
感谢来自社区的每一个 PR，欢迎贡献！
