# MindStudio 工具链官方文档全集

MindStudio是华为面向昇腾AI开发者提供的全流程工具链，致力于提供端到端的昇腾AI应用开发解决方案，使能开发者高效完成训练开发、推理开发和算子开发。

## 工具简介及资料入口

| 工具目录 | 功能简介 | README |
| --- | --- | --- |
| mstt | **【训练开发工具链】** 提供分析迁移、精度调试与性能调优能力，助力实现精度与性能双优。 | [mstt/README.md](mstt/README.md) |
| msit | **【推理开发工具链】** 提供模型压缩、调试与调优等能力，助力用户实现最优推理性能。 | [msit/README.md](msit/README.md) |
| msot | **【算子开发工具链】** 提供算子设计、开发框架生成、功能调试、异常检测与多维性能调优等能力。 | [msot/README.md](msot/README.md) |
| msprobe | **【精度调试】** 昇腾全场景精度工具，用于精度调试与问题定位。 | [msprobe/README.md](msprobe/README.md) |
| msprof | **【模型调优】** 全场景性能调优底座，采集软硬件全栈性能数据，提升设备调优效率。 | [msprof/README.md](msprof/README.md) |
| msprof-analyze | **【性能分析】** 基于采集数据做性能分析，快速识别性能瓶颈。 | [msprof-analyze/README.md](msprof-analyze/README.md) |
| msmemscope | **【内存调优】** 内存调优专用工具：整网级多维度内存采集，支持自动诊断与优化分析。 | [msmemscope/README.md](msmemscope/README.md) |
| msinsight | **【可视调优】** 可视化性能分析，覆盖系统、算子、服务化等场景，辅助完成性能诊断。 | [msinsight/README.md](msinsight/README.md) |
| mspti | **【性能剖析】** 面向昇腾的 Profiling API，可据此开发 NPU 应用性能分析工具。 | [mspti/README.md](mspti/README.md) |
| msmonitor | **【在线监控】** 一站式监控，支持落盘与在线采集，面向集群的监测与问题定位。 | [msmonitor/README.md](msmonitor/README.md) |
| msmodelslim | **【模型压缩】** 包含量化和压缩等推理优化技术，支持大语言稠密模型、MoE 模型、多模态模型等。 | [msmodelslim/README.md](msmodelslim/README.md) |
| msserviceprofiler | **【服务调优】** 支持请求调度、模型执行过程可视化，提升服务化性能分析效率。 | [msserviceprofiler/README.md](msserviceprofiler/README.md) |
| mskpp | **【性能预测】** 支持输入算子描述，预测算子在特定算法实现下的性能上限。 | [mskpp/README.md](mskpp/README.md) |
| msopgen | **【工程生成】** 算子开发效率提升工具，提供模板工程生成能力，简化工程搭建。 | [msopgen/README.md](msopgen/README.md) |
| mskl | **【快捷调用】** 提供 Python 接口，快速实现 Kernel 的下发运行，便于快速完成功能验证。 | [mskl/README.md](mskl/README.md) |
| mssanitizer | **【异常检测】** 提供内存、竞争、未初始化及同步检测，支持多核程序内存问题的精准定位。 | [mssanitizer/README.md](mssanitizer/README.md) |
| msdebug | **【原生调试】** 基于昇腾处理器的原生环境调试，支持变量查看、单步执行及上板调试。 | [msdebug/README.md](msdebug/README.md) |
| msopprof | **【性能分析】** 支持上板与仿真数据采集，通过 MindStudio Insight 可视化工具定位性能瓶颈。 | [msopprof/README.md](msopprof/README.md) |
| msmodeling | **【建模寻优】** 评估模型及服务化等场景下的理论性能，并寻找性能较优的部署策略等参数。 | [msmodeling/README.md](msmodeling/README.md) |
| msopcom | **【基础组件】** 为算子工具提供统一劫持能力，支持桩函数注入、接口劫持与注入函数管理。 | [msopcom/README.md](msopcom/README.md) |
| msopmodeling | **【算子建模】** 基于 TileSim 支持理论与工程双模性能预测，实现免上板的高精度算子性能建模。 | [msopmodeling/README.md](msopmodeling/README.md) |
| msoptuner | **【Tiling 寻优】** 面向 CATLASS 模板库算子，支持自定义搜索空间并批量完成在板性能测试。 | [msoptuner/README.md](msoptuner/README.md) |
| mstx | **【扩展打点】** 提供打点接口，用于标记关键函数或时间段，辅助性能和算子问题快速定界。 | [mstx/README.md](mstx/README.md) |
