# Training Development Toolchain Quick Start

<br>

## 1. Overview

### 1.1 Features

MindStudio Training Tools (msTT) is an open-source, full-process toolchain for AI training development on Ascend. It provides developers with full-lifecycle tool support, from accuracy debugging to online O&M. The toolchain covers accuracy, performance, monitoring, and migration. It helps developers efficiently address typical challenges in training development on Ascend hardware, such as abnormal loss and substandard performance, and achieve excellence in both accuracy and performance.

### 1.2 Core Capabilities

msTT provides the following core capabilities across the key stages of training development:

- **Accuracy debugging**: Supports full-scenario accuracy collection and tiered comparison analysis. Combined with visualization, it helps developers quickly identify the root cause of accuracy deviations.
- **Performance tuning**: Covers data collection, bottleneck analysis, visualization-based diagnosis, memory tuning, and performance profiling, and provides multi-level performance optimization methods, from a single operator to a cluster.
- **Online monitoring**: Provides real-time performance monitoring and fault location for clusters, and supports trace data dumping to the drive and online collection to ensure that training tasks run stably.
- **Script migration**: Provides NPU compatibility analysis and adaptation for PyTorch training scripts, helping you complete the migration from GPU to Ascend NPU.

### 1.3 Purpose of This Document

This document summarizes the functional positioning of the tools in the toolchain and their quick-start entry points. Based on your current development stage and business requirements, you can quickly select the appropriate tool and get started.

## 2. Quick Start

| Category | Tool | Description | Quick Start Link |
|:--:|:--|:--|:--:|
| Accuracy | **msProbe** | **Accuracy debugging**: An Ascend accuracy tool for all scenarios, used for training accuracy debugging and issue location. | [View](https://gitcode.com/Ascend/msprobe/blob/master/docs/en/quick_start/pytorch_quick_start.md) |
| Accuracy | **TensorBoard** | **Tiered visualization**: Displays model structure and accuracy in tiers, and supports debugging and comparison with benchmark models to locate accuracy issues. | [View](https://gitcode.com/Ascend/msprobe/blob/master/docs/en/quick_start/pytorch_quick_start.md) |
| Performance | **msProf** | **Model tuning**: A full-scenario performance tuning foundation that collects CANN and NPU data to improve device tuning efficiency. | [View](https://gitcode.com/Ascend/msprof/blob/master/docs/en/quick_start/msprof_quick_start.md) |
| Performance | **msprof-analyze** | **Performance analysis**: Performs performance analysis on the collected data to quickly identify performance bottlenecks. | [View](https://gitcode.com/Ascend/msprof-analyze/blob/master/docs/en/quick_start/msprof-analyze_quick_start.md) |
| Performance | **msMemScope** | **Memory tuning**: A dedicated memory tuning tool that provides network-wide, multi-dimensional memory collection, with support for automatic diagnosis and optimization analysis. | [View](https://gitcode.com/Ascend/msmemscope/blob/master/docs/en/quick_start/quick_start.md) |
| Performance | **msInsight** | **Visual tuning**: Visual performance analysis covering system, operator, and service scenarios, assisting in performance diagnosis. | [View](https://gitcode.com/Ascend/msinsight/blob/master/docs/en/quick_start/system_tuning_quick_start.md) |
| Performance | **msPTI** | **Performance profiling**: An Ascend-oriented profiling API that you can use to develop performance analysis tools for NPU applications. | [View](https://gitcode.com/Ascend/mspti/blob/master/docs/en/quick_start/mspti_quick_start.md) |
| Monitoring | **msMonitor** | **Online monitoring**: One-stop monitoring with support for trace data dumping to the drive and online collection, for cluster monitoring and issue location. | [View](https://gitcode.com/Ascend/msmonitor/blob/master/docs/en/quick_start/msmonitor_quick_start.md) |
| Migration | **msTransplant** | **Migration analysis**: One-click migration of PyTorch training scripts to Ascend NPU, requiring minimal or zero code changes. | [View](../../../msfmktransplt/README_EN.md#quick-start) |
