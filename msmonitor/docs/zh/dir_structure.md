# 项目目录

项目全量目录层级介绍如下：

```ColdFusion
├── docs                                                     # 项目文档目录
│   └── zh                                                   # 中文文档目录
├── dynolog_npu                                              # dynolog_npu模块代码目录
│   ├── CMakeLists.txt
│   ├── cli                                                  # dyno客户端源代码目录
│   │   └── src
│   ├── cmake                                                # CMake相关配置文件
│   ├── dynolog                                              # dynolog服务端源代码目录
│   │   └── src
│   └── scripts                                              # RPM打包脚本
│       └── rpm                                              # RPM打包相关文件
├── plugin                                                   # 插件模块代码目录
│   ├── CMakeLists.txt
│   ├── IPCMonitor                                           # IPC监测Python模块
│   ├── ipc_monitor                                          # IPC监测核心代码
│   ├── cmake                                                # CMake相关配置文件
│   ├── stub
│   └── third_party                                          # 第三方依赖库
├── scripts                                                  # 构建、测试等脚本目录
│   ├── apply_dyno_patches.sh                                # dyno补丁应用脚本
│   ├── build.sh                                             # 主构建脚本
│   ├── gen_dyno_patches.sh                                  # dyno补丁生成脚本
│   ├── run_presmoke.sh                                      # 前冒烟测试运行脚本
│   ├── run_st.sh                                            # 系统测试运行脚本
│   └── run_ut.sh                                            # 单元测试运行脚本
├── test                                                     # 测试代码目录
│   ├── presmoke                                             # 前冒烟测试用例目录
│   ├── st                                                   # 系统测试用例目录
│   └── ut                                                   # 单元测试用例目录
├── third_party                                              # 第三方依赖库
│   └── dynolog                                              # dynolog第三方依赖
├── LICENSE                                                  # 项目许可证
├── Third_Party_Open_Source_Software_Notice                  # 第三方开源软件声明
└── README.md                                                # 项目说明文档
```
