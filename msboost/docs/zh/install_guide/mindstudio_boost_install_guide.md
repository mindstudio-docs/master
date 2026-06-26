# MindStudio Boost 安装指南

## 1. 安装说明

MindStudio Boost 用于 AI 训练/推理场景下 HostBound 问题的性能优化。本文档介绍 MindStudio Boost 组件的安装和验证方法。

### 1.1 工具集成说明

本工具已集成于 CANN 软件包中，若您的环境已安装 CANN 且无需更新此工具，可直接使用，无需单独安装。

### 1.2 CANN 环境准备

若您的环境尚未安装 CANN，请参见以下步骤：

1. 访问昇腾社区下载页面：[CANN 快速安装](https://www.hiascend.com/cann/download)
2. 下载并安装 CANN 软件包（Toolkit）
3. 配置 CANN 环境变量

---

## 2. 安装验证

安装完成后，可通过以下步骤验证 MindStudio Boost 是否安装成功。

### 2.1 配置环境变量

若 CANN 已安装，需要先配置 CANN 环境变量。以默认安装路径为例：

```bash
source /usr/local/Ascend/cann/set_env.sh
```

**说明**：
- 若使用自定义安装路径，请将路径替换为实际安装路径
- 例如：`source /your/custom/path/Ascend/cann/set_env.sh`

### 2.2 验证模块导入

执行以下命令验证 mindstudio-boost模块是否可以正常导入，若正常输出如下信息，则表明安装成功：

```bash
python3 -c "import affinity_sched; print('mindstudio-boost安装成功')"
```

## 3. 相关文档

- [MindStudio Boost 使用指南](../user_guide/mindstudio_boost_user_guide.md)
- [CANN 安装指南](https://www.hiascend.com/document)
- [昇腾社区文档中心](https://www.hiascend.com/document)

---

## 4. 技术支持

如有安装问题，可通过以下渠道获取帮助：

- 提交 [Issues](https://gitcode.com/Ascend/msboost/issues)
- 加入昇腾技术交流群
- 参阅昇腾社区 FAQ