# Release Notes

## Version Mapping

### Product Version Information

| Product Name | Product Version | Version Type |
|------|-------|------|
| msTT | 8.3.0 | Official Release |

### Related Product Version Mapping

| msTT Version | CANN Version          | PyTorch Version | torch_npu Version | Python Version    |
|--------------|-----------------------|-----------------|-------------------|-------------------|
| 8.3.0        | 8.2.RC1 and later     | 2.1 and later   | 2.1 and later     | Python 3.8 and later |

## Version Compatibility Notes

None

## Feature Change Notes

### 8.3.0

#### I. New Features

##### Accuracy Tool

1. Supports accuracy data collection for VeRL and MsRL frameworks.
2. Provides L2-level accuracy explainability metric collection and analysis capabilities to assist in forward positioning during native training.
3. Supports training status monitoring for VeRL and MsRL frameworks.
4. Supports automatic identification of the first divergent node in MD5 data, enabling quick identification of the first divergent node in deterministic scenarios.
5. msProbe adds support for cross-framework automated comparison of MindSpeed and MindFormers.

##### Performance Tools

1. The NPU Monitor component of msMonitor adds lightweight data persistence capability: supports data persistence in jsonl format, providing more efficient and easier-to-process data format support for subsequent data analysis and system integration.
2. The command-line interaction experience of msMonitor is optimized: the status subcommand supports real-time query of the currently executing step status, improving the tool's ease of use.
3. msprof-analyze adds the module_statistic analysis capability: Provides the ability to automatically parse the model hierarchy for PyTorch models, helping to precisely locate performance bottlenecks.

##### Visualization Tool

1. UI optimization for the tb_graph_ascend component: Adjusted some layout and option styles to improve interface neatness and operation experience.
2. Added shortcut key instructions: Makes it easier for users to quickly master common operations and improve usage efficiency.

#### II. Deleted Features

##### Performance Tools

1. Removed redundant GPU-related instructions from the msMonitor NPU Trace component.

##### Visualization Tool

1. Removed the "Accuracy Color Custom Configuration" option: accuracy colors, previously represented by numbers, are now uniformly adjusted to use three status identifiers, "pass", "warning", and "error", making them more intuitive and clear.

#### III. Bugfix

##### Visualization Tool

1. Fixed the adaptation issue of some precision loss data in earlier versions to prevent system misjudgment and ensure judgment accuracy.
