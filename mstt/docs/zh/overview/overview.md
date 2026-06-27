# 简介

MindStudio Training Tools（msTT）训练开发工具链，聚焦训练开发中的关键挑战。通过提供分析迁移、精度调试与性能调优三大核心工具，高效应对迁移受阻、Loss 异常、性能不达标等问题，助力实现精度与性能双优的极简开发体验。

<img src="../figures/readme/fullview.svg" width="1200"/>

## 功能介绍

训练开发工具链提供以下系列化工具：

| 类别 | 工具名称                                                     | 功能简介                                                     |
| :--: | :----------------------------------------------------------- | :----------------------------------------------------------- |
| 迁移 | [**msTransplant**](https://gitcode.com/Ascend/mstt/tree/master/msfmktransplt) | **【分析迁移】** PyTorch 训练脚本一键迁移至昇腾 NPU，支持少量改码或零改码完成迁移。 |
| 精度 | [**msProbe**](https://gitcode.com/Ascend/msprobe)            | **【精度调试】** 昇腾全场景精度工具，用于训练精度调试与问题定位。 |
| 性能 | [**msProf**](https://gitcode.com/Ascend/msprof)              | **【模型调优】** 全场景性能调优底座，采集 CANN 与 NPU 数据，提升设备调优效率。 |
| 性能 | [**msprof-analyze**](https://gitcode.com/Ascend/msprof-analyze) | **【性能分析】** 基于采集数据做性能分析，快速识别性能瓶颈。  |
| 性能 | [**msMemScope**](https://gitcode.com/Ascend/msmemscope)      | **【内存调优】** 内存调优专用工具：整网级多维度内存采集，支持自动诊断与优化分析。 |
| 性能 | [**msInsight**](https://gitcode.com/Ascend/msinsight)        | **【可视调优】** 可视化性能分析，覆盖系统、算子、服务化等场景，辅助完成性能诊断。 |
| 性能 | [**Tinker**](https://gitcode.com/Ascend/mstt/tree/master/profiler/tinker) | **【并行寻优】** 大模型并行策略自动寻优：按训练脚本做单节点 NPU 测评并推荐高性能并行方案。 |
| 性能 | [**bind_core**](https://gitcode.com/Ascend/mstt/tree/master/profiler/affinity_cpu_bind) | **【一键绑核】** CPU 绑核工具，无需侵入修改工程即可按 CPU 亲和性策略绑核。 |
| 性能 | [**msPTI**](https://gitcode.com/Ascend/mspti)                | **【性能剖析】** 面向昇腾的 Profiling API，可据此开发 NPU 应用性能分析工具。 |
| 监控 | [**msMonitor**](https://gitcode.com/Ascend/msmonitor)        | **【在线监控】** 一站式监控，支持落盘与在线采集，面向集群的监测与问题定位。 |
