# msTT Tool Selection Guide

<br>

The msTT toolchain includes multiple specialized tools that cover all stages of training development. When facing a specific task, choosing the right tool is often more efficient than trying tools at random.

This document is organized around **what you want to do** and helps you quickly pinpoint the best-matching tool and its direct entry point.

<br>

## Scenario-Based Tool Recommendations

| What You Want to Do | Recommended Tool | Why It Is Recommended |
|:------------------------------------------------------------| :----------------------------------------------------------- | :----------------------------------------------------------- |
| I want to migrate GPU training or inference scripts to run on NPUs | [**msTransplant**](https://gitcode.com/Ascend/mstt/tree/master/msfmktransplt) | One-click migration of PyTorch training scripts to Ascend NPUs, requiring minimal or zero code changes |
| I want to debug training or inference model accuracy and locate accuracy issues | [**msProbe**](https://gitcode.com/Ascend/msprobe/tree/master) | Ascend accuracy tool for all scenarios, used for training accuracy debugging and issue location |
| I want to collect performance data for Ascend AI tasks from the CLI | [**msProf**](https://gitcode.com/Ascend/msprof/tree/master) | Bundled by default in the CANN package with no installation required, collecting CANN and NPU performance data from the CLI |
| I want to quickly analyze profiling data, identify performance bottlenecks, and receive tuning recommendations | [**msprof-analyze**](https://gitcode.com/Ascend/msprof-analyze/tree/master) | Performs statistics, comparison, and diagnosis on collected profiling data to help locate performance bottlenecks in compute, communication, scheduling, and cluster scenarios. |
| I want to analyze memory usage in training or inference tasks and debug or tune memory | [**msMemScope**](https://gitcode.com/Ascend/msmemscope/tree/master) | Collects memory data across all Ascend scenarios, with analysis capabilities such as visualization, comparison, and breakdown. |
| I want to present performance issues graphically when locating them | [**msInsight**](https://gitcode.com/Ascend/msinsight/tree/master) | Visual performance analysis covering system, operator, service-oriented, and other scenarios, assisting with performance diagnosis |
| I want to automatically find the optimal parallel strategy for MindSpeed-LLM training tasks | [**Tinker**](https://gitcode.com/Ascend/mstt/tree/master/profiler/tinker) | Evaluates NPUs on a single node according to the training script and recommends high-performance parallel solutions. |
| I want to bind CPU cores to improve performance in HostBound scenarios | [**bind_core**](https://gitcode.com/Ascend/mstt/tree/master/profiler/affinity_cpu_bind) | Binds cores according to CPU affinity policies without intrusive modifications to the project. |
| I want to obtain NPU performance data online through the Profiling API | [**msPTI**](https://gitcode.com/Ascend/mspti/tree/master) | Provides the basic capability to obtain NPU performance data online. |
| I want to obtain cluster performance data in a lightweight manner through online monitoring | [**msMonitor**](https://gitcode.com/Ascend/msmonitor/tree/master) | One-stop monitoring that supports trace data dumping to the drive and online collection, providing cluster-oriented monitoring and issue location |
