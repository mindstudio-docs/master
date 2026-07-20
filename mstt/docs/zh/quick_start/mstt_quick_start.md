# 训练开发工具链快速入门

<br>

## 1. 概述

### 1.1 功能简介

MindStudio Training Tools（msTT）是面向昇腾 AI 训练开发场景的开源全流程工具链，为开发者提供从精度调试到在线运维的全周期工具支持。工具链涵盖精度、性能、监控、迁移四大环节，帮助开发者在昇腾硬件上高效应对 Loss 异常、性能不达标等训练开发中的典型挑战，实现精度与性能双优。

### 1.2 核心能力

msTT 围绕训练开发的关键阶段，提供以下核心能力：

- **精度调试**：支持全场景精度采集与分级对比分析，结合可视化手段帮助开发者快速定位精度偏差根因。
- **性能调优**：覆盖数据采集、瓶颈分析、可视化诊断、内存调优和性能剖析，提供从单算子到集群的多层级性能优化手段。
- **在线监控**：面向集群的实时性能监控与故障定位，支持落盘与在线采集，保障训练任务的稳定运行。
- **脚本迁移**：提供 PyTorch 训练脚本的 NPU 兼容性分析与适配能力，辅助完成从 GPU 到昇腾 NPU 的迁移。

### 1.3 本文用途

本文汇总工具链中各工具的功能定位与快速入门入口，帮助您根据当前的开发阶段和业务需求，快速选择合适的工具并完成上手操作。

## 2. 快速入门

| 类别 | 工具名称                                                                                                                             | 功能简介                                               |                                                      快速入门链接                                                       |
|:--:|:----------------------|:---------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------:|
| 精度 | **msProbe**        | **【精度调试】** 昇腾全场景精度工具，用于训练精度调试与问题定位。                |         [点击查看](https://gitcode.com/Ascend/msprobe/blob/master/docs/zh/quick_start/pytorch_quick_start.md)         |
| 精度 | **TensorBoard**    | **【分级可视】** 分级展示模型结构与精度，支持调试与标杆模型对比以定位精度问题。         |         [点击查看](https://gitcode.com/Ascend/msprobe/blob/master/docs/zh/quick_start/pytorch_quick_start.md)         |
| 性能 | **msProf**           | **【模型调优】** 全场景性能调优底座，采集 CANN 与 NPU 数据，提升设备调优效率。    |          [点击查看](https://gitcode.com/Ascend/msprof/blob/master/docs/zh/quick_start/msprof_quick_start.md)          |
| 性能 | **msprof-analyze**  | **【性能分析】** 基于采集数据做性能分析，快速识别性能瓶颈。                   |  [点击查看](https://gitcode.com/Ascend/msprof-analyze/blob/master/docs/zh/quick_start/msprof-analyze_quick_start.md)  |
| 性能 | **msMemScope**       | **【内存调优】** 内存调优专用工具：整网级多维度内存采集，支持自动诊断与优化分析。        |           [点击查看](https://gitcode.com/Ascend/msmemscope/blob/master/docs/zh/quick_start/quick_start.md)            |
| 性能 | **msInsight**       | **【可视调优】** 可视化性能分析，覆盖系统、算子、服务化等场景，辅助完成性能诊断。        |     [点击查看](https://gitcode.com/Ascend/msinsight/blob/master/docs/zh/quick_start/system_tuning_quick_start.md)     |
| 性能 | **msPTI**          | **【性能剖析】** 面向昇腾的 Profiling API，可据此开发 NPU 应用性能分析工具。 |           [点击查看](https://gitcode.com/Ascend/mspti/blob/master/docs/zh/quick_start/mspti_quick_start.md)           |
| 监控 | **msMonitor**      | **【在线监控】** 一站式监控，支持落盘与在线采集，面向集群的监测与问题定位。           |       [点击查看](https://gitcode.com/Ascend/msmonitor/blob/master/docs/zh/quick_start/msmonitor_quick_start.md)       |
| 迁移 | **msTransplant**  | **【分析迁移】** PyTorch 训练脚本一键迁移至昇腾 NPU，支持少量改码或零改码完成迁移。 |                                   [点击查看](../../../msfmktransplt/README.md#快速入门)                                   |
