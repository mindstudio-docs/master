# msTT 工具选型指南

<br>

msTT 工具链包含多款专项工具，覆盖训练开发的各个阶段。面对具体任务时，精准选型往往比盲目尝试更具效率。

本文以 **”我要做什么”** 为导向，帮助您快速锁定最匹配的工具及直达入口。

<br>

## 场景化工具推荐

| 我要做什么                                                       | 推荐工具                                                     | 为什么推荐                                                   |
|:------------------------------------------------------------| :----------------------------------------------------------- | :----------------------------------------------------------- |
| 我想将GPU的训练或推理脚本迁移到NPU上运行                                     | [**msTransplant**](https://gitcode.com/Ascend/mstt/tree/master/msfmktransplt) | PyTorch训练脚本一键迁移至昇腾NPU，支持少量改码或零改码完成迁移 |
| 我想要做训练或推理模型精度调试，定位精度问题                                      | [**msProbe**](https://gitcode.com/Ascend/msprobe)            | 昇腾全场景精度工具，用于训练精度调试与问题定位               |
| 我想使用命令行采集昇腾AI任务的性能数据                                        | [**msProf**](https://gitcode.com/Ascend/msprof)              | 默认集成在CANN包，无需安装，命令行采集CANN与NPU性能数据      |
| 我想快速分析Profiling数据，分析性能瓶颈给出调优建议                              | [**msprof-analyze**](https://gitcode.com/Ascend/msprof-analyze) | 基于采集得到的Profiling数据进行统计、比对和诊断，帮助定位计算、通信、调度及集群场景下的性能瓶颈 |
| 我想分析训练或推理任务的显存使用，对显存调试调优                                    | [**msMemScope**](https://gitcode.com/Ascend/msmemscope)      | 昇腾全场景显存数据采集，配套可视化、比对、拆解等分析能力     |
| 我想在定位性能问题时，可以通过图形化呈现的方式直观反映性能问题                             | [**msInsight**](https://gitcode.com/Ascend/msinsight)        | 可视化性能分析，覆盖系统、算子、服务化等场景，辅助完成性能诊断 |
| 我想做MindSpeed-LLM训练任务并行策略的自动寻优                               | [**Tinker**](https://gitcode.com/Ascend/mstt/tree/master/profiler/tinker) | 按训练脚本做单节点NPU测评并推荐高性能并行方案                |
| 我想在HostBound场景做CPU绑核提升性能                                    | [**bind_core**](https://gitcode.com/Ascend/mstt/tree/master/profiler/affinity_cpu_bind) | 无需侵入修改工程即可按CPU亲和性策略绑核                      |
| 我想通过Profiling API在线获取NPU性能数据                                | [**msPTI**](https://gitcode.com/Ascend/mspti)                | 提供在线获取NPU性能数据的基础能力                            |
| 我想在通过在线监控轻量获取集群性能数据                                         | [**msMonitor**](https://gitcode.com/Ascend/msmonitor)        | 一站式监控，支持落盘与在线采集，面向集群的监测与问题定位     |
