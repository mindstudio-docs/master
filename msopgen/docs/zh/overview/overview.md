# 简介

MindStudio Ops Generator（算子工程工具，msOpGen）是算子开发效率提升工具，集成于 MindStudio 工具链中。完成算子分析和原型定义后，可使用 msOpGen 工具生成自定义算子工程，并进行编译部署。

**核心功能**：

- **算子工程生成**（`msopgen gen`）：基于算子原型定义 JSON 文件，自动生成完整的算子工程框架（含 Host 侧和 Kernel 侧代码模板、编译脚本等）
- **仿真流水图解析**（`msopgen sim`）：解析性能仿真环境生成的 dump 数据，生成可在 Chrome tracing 中查看的算子仿真流水图文件

**配套工具**：

- **msOpST**（算子测试工具）：在真实硬件环境中对算子进行 ST（System Test）测试，验证算子功能正确性
- **msProf**（性能分析工具） / **msSanitizer**（异常检测工具） / **msDebug**（调试工具）：与 msOpGen 生成的算子工程深度集成，覆盖性能调优、内存检测和上板调试场景

**适用场景**：

- Ascend C 自定义算子开发
- TBE / AI CPU 算子工程搭建
- 多框架适配（TensorFlow、PyTorch、MindSpore、ONNX）
