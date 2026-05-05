# msOpGen 架构设计说明书

## 简介

MindStudio Ops Generator（算子工程创建，msOpGen）是算子开发效率提升工具，提供模板工程生成能力，简化算子工程搭建并辅助算子测试验证。完成算子分析和原型定义后，可使用msOpGen工具生成自定义算子工程。

## 目录结构

整体目录设计如下：

```text
├── example  // 工具样例
├── docs              // 项目文档介绍
├── msopgen  // msopgen源码目录
├── test
│     ├── msopgen  // msopgen测试用例
│     └── msopst   // msopst测试用例
├── tools  // 存放一些工程相关工具，当前仅放msopst
│     └── msopst  // msopst代码目录
│           └── setup.py  // msopst whl包构建脚本
├── build  // 打包whl过程中的中间文件
├── output  // whl包输出目录、测试用例报告
├── setup.py  // msopgen whl包构建脚本
├── build.py  // 执行测试用例，生成安装包
├── requirements.txt  // python依赖库
└── README.md  // 整体仓库代码说明
```

## msOpGen 类图

![alt text](../figures/msOpGenClass.png)
