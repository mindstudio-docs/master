# 算子性能建模工具使用指南

<br>

## 1. 简介

**msOpModeling** 是昇腾 NPU 算子性能建模工具，无需真实硬件即可预测算子时延。支持两种建模模式：

| 模式 | `backend_type` 值 | 适用场景 | 说明 |
|------|-------------------|----------|------|
| 理论极限 | `theo` | 快速评估算子计算/访存上限 | 基于 Roofline 模型，忽略流水/同步开销，给出性能理论上限 |
| 工程可达 | `eng` | 贴近真实上板性能的精细预测 | Tile 级仿真，考虑 tiling、流水线排布、缓存命中，预测最优 tiling 下的真实时延 |

> **选哪种模式？**
> - 快速筛查瓶颈算子、评估设计方案 → `theo`
> - 指导 tiling 调优、验证优化效果 → `eng`

---

## 2. 环境要求

- Python ≥ 3.10

---

## 3. 安装

```shell
pip install msopmodeling -i https://mirrors.aliyun.com/pypi/simple/
```

安装后验证：

```shell
msopmodeling --help
msopmodeling --version
msopmodeling -V
```

> `-v` 表示 `--verbose`，查看版本请使用 `msopmodeling -V` 或 `--version`。

两个版本参数输出相同的工具版本、Git 提交 ID、版权、许可证、UTC 时间和项目仓库地址。
wheel 安装后显示构建时记录的提交 ID 和时间；可编辑安装显示当前源码提交 ID 和最近一次
`pip install -e .` 时记录的时间。该时间不会随源码修改或再次运行命令而改变。
直接运行未经安装的源码时，时间显示为 `Not recorded (source checkout)`。

---

## 4. 准备输入文件

`-i` 根据文件内容自动识别输入格式，不依赖文件名或扩展名。支持以下输入：

| 输入格式 | 识别内容 | 支持模式 | 芯片配置 |
|------|------|------|------|
| JSON 数组 | 每个元素描述一个待预测的算子 | `theo`、`eng` | 指定 `-s`，或由每个元素提供 `accelerator` |
| profiler `op_summary` CSV | 包含 `Op Name`、`OP Type` 列的表头 | 仅 `theo` | 必须指定 `-s` |
| profiler `kernel_details` CSV | 包含 `Name`、`Type`、`Accelerator Core` 列的表头 | 仅 `theo` | 必须指定 `-s` |

以下第 4.1 至 4.3 节说明 JSON 输入；CSV 输入见第 4.4 节。JSON 的两种建模模式及现有配置方式保持不变。

**JSON 重复预测加速：** 同一次 JSON 批量预测中，`theo` 和 `eng` 均会复用完整建模配置相同的首次成功结果和六种标准交付件。缓存键包含建模模式、输入输出形状与精度、硬件目标与核数、布局、`input_dict` 及 `extra_param` 等全部配置。缓存键统一按对象字段名排序，字段排列顺序不同仍可复用，候选列表等数组的顺序保持不变。配置不得同时包含大小写归一化后重名的字段，例如同一对象中的 `ROW` 和 `row`。每项仍有独立的 `OP_i`、结果、优化建议和交付件目录，已有目录的无关文件不会被删除。失败不缓存，交付件快照不完整或读取失败时不启用该项缓存；回放写入失败只记录当前项错误。缓存仅在当前批次内存中有效，不跨批次共享拟合状态，也不改变独立 API 调用的行为。

GEMM 等模型包含随机搜索，重复配置共享首次成功搜索结果；跳过重复搜索可能改变后续不同配置的随机搜索轨迹，因此不保证与未缓存时的逐项结果完全一致。缓存也复用首次预测的 `runtime_profile.json`，其中耗时并非命中项重新计算的耗时。`eng` 的 trace、events 和 diagnostics 同样回放首次预测的内容，不重新执行仿真。此优化不改变模型公式、搜索参数或仿真逻辑；缓存占用的内存随不同成功配置及其交付件总大小增长。

### 4.1 公共字段说明

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `op_name` | string | 是 | 算子名称，如 `"MatMul"`、`"Add"` |
| `backend_type` | string | 否 | 建模模式：`"theo"` 或 `"eng"`；省略时由命令行模式注入，填写时必须与命令行模式一致 |
| `input_shapes` | list[list[int]] | 是* | 各输入 Tensor 的形状，如 `[[2048, 512], [512, 1024]]` |
| `output_shapes` | list[list[int]] | 是* | 各输出 Tensor 的形状 |
| `input_precision` | list[string] | 是 | 各输入 Tensor 的数据类型，如 `["FLOAT16", "FLOAT16"]` |
| `output_precision` | list[string] | 是 | 各输出 Tensor 的数据类型 |
| `core_num` | int | 否 | 使用的计算核数，默认取芯片最大核数 |

**支持的数据类型：** `FLOAT`、`FLOAT16`、`BF16`、`INT8`、`INT32`、`INT64`

**支持的芯片型号（用于 `-s` 参数）：**

`-s` 的可选型号由 `ArchName` 枚举定义，每个型号对应 `arc_config/<soc>/<soc>.yaml` 硬件配置。当前支持以下型号：

| 系列 | 型号 |
|------|------|
| 昇腾 910 系列 | `910B1`、`910B4`、`910B3`、`910B4-1` |
| A5 系列 | `950` |

`910C` 是 `910B1` 的命令行别名。新增内置 SoC 时，需要同时更新 `src/msopmodeling/_internal/core/arch/names.py` 中的 `ArchName` 和对应硬件配置；仅增加配置文件不会自动成为命令行可选型号。

`-s` 选择用于预测的硬件配置，包括带宽、算力和核数等参数，并覆盖输入 JSON 中各算子的 `accelerator`。JSON 性能预测时可以省略 `-s`，但此时每条算子配置必须提供 `accelerator` 配置路径；CSV 预测必须指定 `-s`。硬件配置存在不代表所有算子都可用：工具还会根据配置中的 `arch_family` 和算子注册的支持范围校验。JSON 中不支持的算子会在输入转换和算子实例化之前报错；CSV 中则记录该行错误并继续处理后续行。可先使用第 5.1 节的命令查询清单。


### 4.2 示例一：理论极限模式（Add 算子）

将如下内容保存为 `input_theo.json`：

```json
[
  {
    "op_name": "Add",
    "backend_type": "theo",
    "input_shapes": [[2048, 2048], [2048, 2048]],
    "output_shapes": [[2048, 2048]],
    "input_precision": ["FLOAT16", "FLOAT16"],
    "output_precision": ["FLOAT16"],
    "core_num": 24
  }
]
```

### 4.3 示例二：工程可达模式（MatMul 算子）

将如下内容保存为 `input_eng.json`：

```json
[
  {
    "op_name": "MatMul",
    "backend_type": "eng",
    "input_shapes": [[2048, 512], [512, 1024]],
    "output_shapes": [[2048, 1024]],
    "input_precision": ["FLOAT16", "FLOAT16"],
    "output_precision": ["FLOAT32"],
    "aic_core_num": 24,
    "extra_param": {
      "tuning_candidates": [
        {"tm": 128, "tn": 256, "tk1": 256, "tk0": 64}
      ]
    }
  }
]
```

> `extra_param.tuning_candidates`：指定候选 tiling 参数组合，工具将从中挑选时延最优的方案。可提供多组候选，工具自动搜索最优。

### 4.4 profiler CSV 输入

可直接传入 `op_summary` 或 `kernel_details` CSV，无需先转换为 JSON。两者都仅支持理论极限模式 `theo`，不支持 CSV 工程可达模式 `eng`，且必须通过 `-s` 指定 SoC。即使文件改名或使用其他扩展名，也仍按内容识别。

**形状单元格规则：**

- 分号 `;` 分隔不同 Tensor，逗号 `,` 分隔同一 Tensor 的维度。例如 `2048,512;512,1024` 表示 `[[2048, 512], [512, 1024]]`。
- 空的 Tensor 片段表示标量 `[]`，必须保留其位置，不能删除空片段。例如 `;2048,512;` 表示 `[[], [2048, 512], []]`，单个空形状单元格表示一个标量 Tensor。
- `N/A` 是无效形状值，不能按空标量处理；该行会记录错误。
- 形状单元格含逗号时，应保留 CSV 的字段引号，避免将维度逗号误解析为列分隔符。

**建模边界：**

- 使用所选 SoC 的最大核数，不将 profiler 的 `Block Num` 映射为物理核数。
- 使用模型已有的默认属性，不从 CSV 推断算子属性；`ND` 仅是格式信息，不能据此推断 attention 所需的语义布局。
- 模型要求的必需属性若缺失且没有默认值，该行预测失败，不会中断其他行。
- 默认属性不保证恢复原算子的真实语义。例如 ReduceSum 默认归约最后一轴，不能据此认定原算子也沿最后一轴归约。若需明确指定属性，应使用包含完整算子配置的 JSON 输入。

**重复记录加速：** 同一次 CSV theo 预测中，完整建模配置相同的记录复用首次成功的预测结果和交付件，避免跨 step 重复建模。每行仍保留独立的 `OP_i`、`source` 和交付件目录，已有目录中的无关文件不会被删除。失败记录不会被缓存；缓存不跨批次保留。JSON 的 theo/eng 缓存见本节开头；CSV 仍仅支持 theo。GEMM 等模型包含随机搜索，重复记录共享首次成功搜索的结果，而不再逐行独立搜索；跳过重复搜索也可能改变后续不同配置的随机搜索轨迹，因此不保证与未复用时的逐行结果完全一致。此优化不补全缺失属性，也不改变模型公式或搜索参数。

---

## 5. 运行

```shell
# 理论极限模式，针对 910B1 芯片，结果写入 msopmodeling_output/
msopmodeling theo -i input_theo.json -s 910B1

# 工程可达模式，结果写入 result_dir/
msopmodeling eng -i input_eng.json -s 910B4 -o result_dir

# profiler op_summary CSV，仅支持 theo，必须指定 -s
msopmodeling theo -i op_summary.csv -s 910B4 -o result_op_summary

# profiler kernel_details CSV，仅支持 theo，必须指定 -s
msopmodeling theo -i kernel_details.csv -s 910B4 -o result_kernel_details
```

**完整参数说明：**

| 参数 | 必填 | 说明 |
|------|----|------|
| `theo` / `eng` | 是  | 建模模式；与 JSON 中 `backend_type` 冲突时终止程序 |
| `list` | 否  | 指定时查询算子清单；省略时执行性能预测 |
| `-i / --input` | 预测时必填 | 输入文件路径，按内容识别 JSON 数组、`op_summary` CSV 或 `kernel_details` CSV，与文件名无关；CSV 仅支持 `theo`；`list` 不接受此参数 |
| `-o / --output` | 否  | 输出目录，默认 `msopmodeling_output`；不存在时自动创建，已存在时直接复用 |
| `-s / --soc-type` | 清单查询、CSV 预测时必填 | 选择 `ArchName` 中的芯片型号，如 `910B1`、`950`；JSON 预测时省略则要求每条输入提供 `accelerator` |
| `-v / --verbose` | 否  | 输出 DEBUG 级别详细日志，便于排查问题 |

### 5.1 查看算子清单

```shell
msopmodeling theo list -s 910B1
msopmodeling eng  list -s 910B1
msopmodeling eng  list -s 950
```

输出包含建模模式、SoC、架构族和按注册支持范围过滤的算子，以及供 JSON `op_name` 使用的别名。同一算子在 `theo`、`eng` 模式下的支持范围可能不同。`list` 不接受 `-i`、`-o`，不执行预测、不写输出文件，`-s` 必填。

---

## 6. 查看输出结果

成功执行后，输出目录结构如下：

```text
result_dir/
├── result.json          # 所有算子的预测结果
├── OP_0/                # 第 1 个算子的交付件
│   ├── trace.json
│   ├── events.json
│   ├── OpBasicInfo.csv
│   ├── PipeUtilization.csv
│   ├── diagnostics.json
│   ├── runtime_profile.json
│   └── optimization_hints_OP_0.csv
└── OP_1/
    └── ...
```

> 输出目录不存在时会自动创建；已存在时直接复用，不会清空其中已有文件，`result.json` 与对应 `OP_x/` 内容会被覆盖更新。

`result.json` 的结构如下（以 MatMul 工程模式为例）：

```json
{
  "OP_0": {
    "op_name": "EngMatmulL0",
    "latency": 8.56,
    "component_latency": {
      "CUBE": 6.64,
      "MTE1": 4.15,
      "MTE2": 6.33,
      "FIXPIPE": 5.23,
      "VEC": 0,
      "MTE2_AIV": 0,
      "MTE3": 0
    },
    "l2_hit_rate": 0.327,
    "cube_utilization_rate": 0.776,
    "vec_utilization_rate": 0.0,
    "mem_volume": {
      "GM_2_L1": 17301504,
      "L1_2_L0A": 8388608,
      "L1_2_L0B": 16777216,
      "L0C_2_GM": 8388608
    },
    "compute_workload": {
      "CUBE": 12288,
      "VEC": 0
    },
    "tiling_info": {}
  }
}
```

输出 JSON 中每个键（`OP_0`、`OP_1` …）对应 JSON 输入数组中的一个算子，或 CSV 中的一条数据行，按顺序从 0 编号。CSV 表头不计入编号，不支持、无效或预测失败的行仍占用原来的 `OP_i`，后续行不会重新编号。

### 6.1 CSV 结果与错误处理

CSV 成功行保留正常的 `latency` 等预测结果字段，并附带来源信息，用于追溯原始 CSV 数据行及算子。错误行也保留来源信息，并通过以下字段说明原因，而不是提供有效的预测时延：

| 字段 | 说明 |
|------|------|
| `error` | 该行不支持、输入无效或预测失败的具体原因 |
| `error_kind` | 错误类别，便于分类检查失败结果 |

不支持的算子、无效形状、缺少必需属性和预测失败等行级问题均不会中断后续行。所有行处理结束后，终端按错误类别分组汇总错误，便于集中排查；成功结果和错误记录都会写入 `result.json`。

只要存在失败或不支持的行，工具就会在保存结果后以退出码 `1` 结束。因此，非零退出码不一定表示没有结果，应结合 `result.json` 和终端汇总检查。文件无法读取、输入格式无法识别等文件级错误会直接终止，不适用逐行继续处理的规则。

### 6.2 预测字段说明

**关键字段解读：**

| 字段 | 单位    | 含义                             |
|------|-------|--------------------------------|
| `latency` | μs    | **算子总时延**（核心指标），流水仿真给出的端到端时延   |
| `component_latency.CUBE` | μs    | Cube 矩阵运算单元耗时                  |
| `component_latency.MTE1` | μs    | L1→L0 数据搬运耗时                   |
| `component_latency.MTE2` | μs    | GM→L1 数据搬运耗时（通常为访存瓶颈所在）        |
| `component_latency.FIXPIPE` | μs    | L0→GM 数据搬运耗时                   |
| `component_latency.VEC` | μs    | 向量运算耗时（向量算子为主要耗时段）             |
| `cube_utilization_rate` | -     | Cube 单元利用率，越接近 `1.0` 说明计算效率越高  |
| `vec_utilization_rate` | -     | 向量单元利用率                        |
| `l2_hit_rate` | -     | L2 缓存命中率，越高说明访存局部性越好，搬运开销越小    |
| `mem_volume` | Bytes | 各存储层间的数据搬运量（GM↔L1↔L0A/L0B/L0C） |
| `compute_workload.CUBE` | -     | Cube 单元实际计算工作量                 |
| `tiling_info` | -     | 最优 tiling 参数（工程模式下有值）          |

**性能瓶颈快速判断：**

- `MTE2 > CUBE`：访存受限（带宽瓶颈），考虑提高 L2 命中率或减少搬运量
- `CUBE > MTE2`：计算受限（算力瓶颈），`cube_utilization_rate` 越高越好
- `cube_utilization_rate < 0.7`：tiling 参数可能不优，可增加 `tuning_candidates` 数量重新搜索

---

## 7. 常见问题

**Q：如何一次预测多个算子？**

在输入 JSON 数组中添加多个对象即可，输出结果依次以 `OP_0`、`OP_1`、`OP_2` … 标识。

也可以使用 profiler `op_summary` 或 `kernel_details` CSV 批量执行 `theo` 预测，并指定 `-s`。每条数据行保留自己的 `OP_i`，即使该行不支持或失败，也不影响其他行继续处理。
