# 大模型训练性能瓶颈定位流程案例

## 常见性能问题场景

大模型从其他设备迁移至昇腾设备，并在昇腾设备上训练的过程中，可能会出现性能问题。性能问题主要体现在开箱性能不足和长期运行后的性能衰退两个方面。

- **开箱性能优化**：用户在昇腾平台使用模型时，发现性能差，直接进行性能层面的优化。
- **性能长跑劣化**：用户在训练过程中，由于引入了不可预知的因素（例如算法参数的不当调整），导致模型出现了一些性能劣化的问题，需要定位性能劣化的原因并解决。

**图1** 场景介绍

![img](../figures/best_practices/case_of_troubleshooting_performance_bottleneck_in_llm_training/zh-cn_image_0000002535808243.png)

## 问题定位方法

### 性能问题定位流程

大模型训练的基本性能调优流程如下：

**图1** 基本性能调优流程

![img](../figures/best_practices/case_of_troubleshooting_performance_bottleneck_in_llm_training/zh-cn_image_0000002504088268.png)

性能调优第一步是先明确问题，再进行针对性优化。

1. 进行性能数据采集，可以使用Ascend PyTorch Profiler提供的接口进行数据采集和解析。
2. 使用MindStudio Insight可视化工具定界性能问题，定界结果通常分为计算、调度、通信三个方向。
3. 使用[advisor专家建议工具](https://gitcode.com/Ascend/msprof-analyze/blob/master/docs/zh/user_guide/advisor_instruct.md)辅助定位问题，advisor工具通过内置案例集，自动对性能数据进行分析，并输出性能调优建议。
4. 针对具体问题使用对应的调优手段进行调优，每次调优后**重跑训练**，**采集性能数据**，使用MindStudio Insight可视化工具查看调优手段是否生效。重复这个过程，直到解决性能问题。

### Ascend PyTorch Profiler采集性能数据<a name="case_of_troubleshooting_performance_bottleneck_in_llm_training01"></a>

Ascend PyTorch Profiler是大模型在Ascend PyTorch框架下训练过程中提供的一套采集性能数据的API接口，能够采集到框架侧、CANN侧和Device侧的原始性能数据，并完成解析。

Ascend PyTorch Profiler详细介绍请参见[Ascend PyTorch Profiler](https://gitcode.com/Ascend/pytorch/blob/master/docs/zh/developer_notes/ascend_pytorch_profiler_user_guide.md)。

在训练脚本（如train_*.py文件）内添加如下示例代码进行性能数据采集参数配置，之后启动训练。

```python
import torch
import torch_npu

# Profiler采集、解析的前置配置参数
experimental_config = torch_npu.profiler._ExperimentalConfig(
    export_type=torch_npu.profiler.ExportType.Text,
    profiler_level=torch_npu.profiler.ProfilerLevel.Level1,
    msprof_tx=False,
    aic_metrics=torch_npu.profiler.AiCMetrics.PipeUtilization,
    l2_cache=False,
    op_attr=False,
    data_simplification=False,
    record_op_args=False,
    gc_detect_threshold=None
)
# 大模型训练的次数
steps = 7
with torch_npu.profiler.profile(
        activities=[
            torch_npu.profiler.ProfilerActivity.CPU,
            torch_npu.profiler.ProfilerActivity.NPU
        ],
        schedule=torch_npu.profiler.schedule(wait=0, warmup=0, active=2, repeat=2, skip_first=1),
        on_trace_ready=torch_npu.profiler.tensorboard_trace_handler("./result"),
        record_shapes=False,
        profile_memory=True,
        with_stack=False,
        with_modules=False,
        with_flops=False,
        experimental_config=experimental_config) as prof:
    for step in range(steps):
        # 模型训练
        train_one_step(step, steps, train_loader, model, optimizer, criterion)
        # 调用step方法进行采集、解析数据
        prof.step()
```

采集生成的文件结构如下所示：

```text
└── localhost.localdomain_139247_20240628101435_ascend_pt
    ├── profiler_info.json
    ├── profiler_metadata.json
    ├── ASCEND_PROFILER_OUTPUT
    │   ├── communication.json
    │   ├── communication_matrix.json
    │   ├── kernel_details.csv
    │   ├── memory_record.csv
    │   ├── npu_module_mem.csv
    │   ├── operator_details.csv
    │   ├── operator_memory.csv
    │   ├── step_trace_time.csv
    │   ├── op_statistic.csv
    │   ├── api_statistic.csv
    │   └── trace_view.json
    ├── FRAMEWORK
    └── PROF_000001_20230628101435646_FKFLNPEPPRRCFCBA
          ├── analyze
          ├── device_*
          ├── host
          ├── mindstudio_profiler_log
          └── mindstudio_profiler_output
```

### MindStudio Insight定位

MindStudio Insight提供了丰富的调优分析手段：可视化呈现真实软硬件运行数据；多维度分析性能数据，定位性能瓶颈点；支持百卡、千卡及以上规模的集群性能分析。

可以根据《[MindStudio Insight工具用户指南](https://gitcode.com/Ascend/msinsight/blob/master/docs/zh/user_guide/overview.md)》中的“基础操作 > [导入数据](https://gitcode.com/Ascend/msinsight/blob/master/docs/zh/user_guide/basic_operations.md#%E5%AF%BC%E5%85%A5%E6%95%B0%E6%8D%AE)”，在MindStudio Insight中导入[Ascend PyTorch Profiler采集性能数据](#case_of_troubleshooting_performance_bottleneck_in_llm_training01)采集的性能数据，根据以下步骤进行性能数据分析。

#### 通过概览界面查看数据总体情况

可以通过概览页了解每个模块的具体内容。详细介绍请参见《[MindStudio Insight工具用户指南](https://gitcode.com/Ascend/msinsight/blob/master/docs/zh/user_guide/overview.md)》中的“系统调优 > [概览（Summary）](https://gitcode.com/Ascend/msinsight/blob/master/docs/zh/user_guide/system_tuning.md#%E6%A6%82%E8%A7%88%EF%BC%88summary%EF%BC%89)”。

1. 在“并行策略分析”模块，提供PP、TP、CP、DP、EP等不同并行策略分析视角。

   1. 单击复选框选择并行策略，通过方框标注识别并行分组。
   2. 选择不同的“数据类型”会展示对应的热力图，根据热力图找到存在性能问题的通信域，越偏向红色表示性能越差。

   **图1** 并行策略分析

   ![img](../figures/best_practices/case_of_troubleshooting_performance_bottleneck_in_llm_training/zh-cn_image_0000002504088304.png)

2. 在计算/通信概览部分展示所选通信域下每张卡的计算、通信、空闲时间占比情况，并提供专家建议，如下图。

   **图2** 计算/通信概览

   ![img](../figures/best_practices/case_of_troubleshooting_performance_bottleneck_in_llm_training/zh-cn_image_0000002504088280.png)

   各图例相关数据指标的含义如下：

   **表1** 数据指标

   | 数据指标             | 含义                                           |
   | -------------------- | ---------------------------------------------- |
   | 总计算时间           | 昇腾设备上的内核时间总和。                     |
   | 纯计算时间           | 纯计算时间 = 总计算时间 – 通信时间（被覆盖）。 |
   | 通信时间（被覆盖）   | 被覆盖的通信时长，即计算和通信同时进行的时长。 |
   | 通信时间（未被覆盖） | 未被覆盖的通信时长，即纯通信时长。             |
   | 空闲时间             | 未进行计算或通信的时长。                       |

不同的指标现象可以定界不同的性能问题：

- **计算问题**：通常表现为通信域中总计算时间占比的极大值和极小值差异过大。如果某些计算卡的计算时间明显超出了正常范围，那很可能意味着这张卡承担了过于繁重的计算任务，例如要处理的数据量过大，或者模型计算的复杂程度过高，也有可能是卡本身的性能受到了限制。
- **调度问题**：通常表现为通信域中空闲时间占比的极大值和极小值差异过大。如果计算卡的空闲时间过长，那就说明存在Host侧至Device侧的下发异常，这同样会对集群的性能造成不利影响。
- **通信问题**：若通信时间（未被覆盖）过长，表明计算和通信之间的协同存在问题。可能是通信方式存在优化空间；或是网络带宽不稳定，导致通信无法和计算良好配合。

#### 计算问题

当数据指标现象指示为计算问题时，可以直接查看异常卡的算子数据，并与正常卡进行比较。此时可以使用MindStudio Insight的卡间性能比对功能，根据《[MindStudio Insight工具用户指南](https://gitcode.com/Ascend/msinsight/blob/master/docs/zh/user_guide/overview.md)》中的使用说明，设置两卡进入比对模式，并在算子界面查看结果。以下图中存在的计算问题为例，可以看到在算子数量相等的前提下，MatMul类算子平均耗时明显增加，造成了两张单卡的计算时间差异。

**图3** 计算算子类型

![img](../figures/best_practices/case_of_troubleshooting_performance_bottleneck_in_llm_training/zh-cn_image_0000002503928464.png)

根据经验，MatMul类算子很可能在特定shape下劣化，可以将分组方式切换到“计算算子名称和输入shape”，并根据总耗时排序，进一步定位在哪些shape下MatMul类算子的劣化最为严重。定位到算子问题后，可以找相关算子开发人员进一步确认问题原因。

**图4** 计算算子名称和输入shape

![img](../figures/best_practices/case_of_troubleshooting_performance_bottleneck_in_llm_training/zh-cn_image_0000002535888257.png)

#### 调度问题

当数据指标现象指示为调度问题时，需要到时间线界面将异常卡和正常卡进行比较，进一步定位出现问题的算子，可以根据《[MindStudio Insight工具用户指南](https://gitcode.com/Ascend/msinsight/blob/master/docs/zh/user_guide/overview.md)》中的“系统调优 > [时间线（Timeline）](https://gitcode.com/Ascend/msinsight/blob/master/docs/zh/user_guide/system_tuning.md#%E6%97%B6%E9%97%B4%E7%BA%BF%EF%BC%88timeline%EF%BC%89)”了解界面详情。进入时间线界面，选择HostToDevice连线类型，HostToDevice展示了CANN层算子到Ascend Hardware的算子的下发执行关系和CANN层算子到HCCL通信算子的下发执行关系，用于定位调度问题。

HostToDevice的连线通常有两种形态，倾斜和竖直。下图是一个存在调度问题的案例，如果HostToDevice连线如左侧所示，是倾斜的，说明此时间段调度任务安排合理，昇腾设备是满负荷执行计算和通信任务的。如果HostToDevice连线如右侧所示，是竖直的，说明昇腾设备此时快速执行完了CPU下发的任务，未满负荷进行计算和通信任务，这一般表示存在调度问题。此时，可以通过增大batch size、绑核、融合算子替换等方法进行调优。

**图5** 调度问题

![img](../figures/best_practices/case_of_troubleshooting_performance_bottleneck_in_llm_training/zh-cn_image_0000002504088290.png)

#### 通信问题

当数据指标现象指示为通信问题时，需要进入通信界面进一步分析。通信界面用于展示集群中全网链路性能以及所有节点的通信性能，通过集群通信与计算重叠时间的分析可以找出集群训练中的慢主机或慢节点。通常，我们会根据关键指标通信矩阵、通信时长来分析性能问题。

**通信矩阵**

**图6** 通信矩阵

![img](../figures/best_practices/case_of_troubleshooting_performance_bottleneck_in_llm_training/zh-cn_image_0000002503928450.png)

上图是MindStudio Insight通信矩阵可视化界面，可以获取各个通信域下，卡间的带宽、传输大小、链路方式和传输时长情况等信息。

1. 首先查看传输大小，分析在该集合通信中，每张卡的传输量是否存在差异，是否有分配不均的情况。
2. 其次，再查看传输时长和带宽情况，如果不同卡间的传输时长和带宽数值异常或者差异过大，那都意味着通信域中存在异常链路。

**通信时长**

通信时长是指计算卡之间进行通信所花费的时间。导致通信耗时过长的因素很多，例如通信协议配置错误、传输数据量过大等，只有找到这些通信耗时过长的链路并解决问题，才能让数据在计算卡之间更加顺畅地传输，进而提高集群的整体性能。

用户选择具体通信域后，可进入通信时长界面中查看通信域中各个计算卡的耗时汇总情况，以及通信算子的HCCL缩略图和通信时长的分布图，从而快速获得通信算子的相对位置关系以及详细通信数据。

**图7** HCCL缩略图

![img](../figures/best_practices/case_of_troubleshooting_performance_bottleneck_in_llm_training/zh-cn_image_0000002535888279.png)

**图8** 通信时长分布图

![img](../figures/best_practices/case_of_troubleshooting_performance_bottleneck_in_llm_training/zh-cn_image_0000002535808251.png)

上图是一份性能数据中某一个通信域内的通信耗时分析。从通信时长数据中，我们发现3卡的同步时间最长，4卡的同步时间最短，且同步时间差距明显。同步时间较长一般意味着这张卡在等待其它卡，而同步时间较短一般意味着其它卡在等待这张卡，据此可以初步定界出3卡是快卡，4卡是慢卡。

## 性能调优案例

### 案例描述

某多模态模型在训练时突然出现性能大幅度劣化问题，我们将根据上述介绍的流程进行性能调优。

使用Ascend PyTorch Profiler采集大模型训练过程中的性能数据，此案例集群共有16张卡。

> [!NOTE]
>
> 本案例数据基于历史版本的工具和数据进行分析，仅作为案例指导，若数据及工具输出与最新版本有出入，请以最新版本输出为准。

### MindStudio Insight分析定位

MindStudio Insight加载全部数据，进行问题定位。

1. 概览界面分析：该通信域内各卡的通信时间占比也较高，总体计算时间（纯计算时间+通信重叠时间）只占了总耗时的1/3，可以定界为通信问题。

   **图1** 概览界面

   ![img](../figures/best_practices/case_of_troubleshooting_performance_bottleneck_in_llm_training/zh-cn_image_0000002503928436.png)

2. 切换通信界面：发现存在大量卡间不同步现象（框中红色部分），这表示很多算子在长时间的等待，挑选了一张最明显的慢卡（第12卡）分析详细原因。

   **图2** 通信界面

   ![img](../figures/best_practices/case_of_troubleshooting_performance_bottleneck_in_llm_training/zh-cn_image_0000002535888243.png)

3. 切换时间线界面：明显看出12卡存在大段的Free（空闲时间），同时，AscendCL侧有大量的事件在占用资源。可初步判断是由于该卡内存占用过高，新申请数据时需要内存重整，从而导致存在较长空闲时间。我们可以使用`export PYTORCH_NPU_ALLOC_CONF="expandable_segments:True"`解决内存碎片问题，提高内存利用率。在完成调试后解决该性能问题。

   **图3** 时间线界面

   ![img](../figures/best_practices/case_of_troubleshooting_performance_bottleneck_in_llm_training/zh-cn_image_0000002503928442.png)

   **图4** 时间线界面

   ![img](../figures/best_practices/case_of_troubleshooting_performance_bottleneck_in_llm_training/zh-cn_image_0000002504088272.png)

### advisor辅助定位

此案例还可以使用[advisor专家建议工具](https://gitcode.com/Ascend/msprof-analyze/blob/master/docs/zh/user_guide/advisor_instruct.md)辅助定位。

1. 执行`msprof-analyze advisor all -d $HOME/profiling_data/`命令，获得保存专家建议的文件路径。其中$HOME/profiling_data/为性能数据所在路径。

   **图1** advisor输出

   ![img](../figures/best_practices/case_of_troubleshooting_performance_bottleneck_in_llm_training/zh-cn_image_0000002535808225.png)

2. 打开html文件，得到红框中的建议，与我们分析结论一致，可以解决性能问题。

   **图2** advisor专家建议

   ![img](../figures/best_practices/case_of_troubleshooting_performance_bottleneck_in_llm_training/zh-cn_image_0000002535808233.png)
