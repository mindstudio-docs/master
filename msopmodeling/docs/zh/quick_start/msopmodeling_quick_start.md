# 算子性能建模工具快速入门

<br>

## 1. 简介

**msOpModeling** 是昇腾 NPU 算子性能建模工具，无需真实硬件即可预测算子时延。支持理论极限（`theo`）和工程可达（`eng`）两种建模模式。

---

## 2. 环境要求

- Python ≥ 3.10

---

## 3. 安装

```shell
pip install msopmodeling
```

> 如果下载速度慢，请按 Ctrl + C 中止，在命令后追加 `-i https://mirrors.aliyun.com/pypi/simple/` 再次执行。

安装后验证：

```shell
msopmodeling -h
msopmodeling --version
msopmodeling -V
```

---

## 4. 准备输入文件

`-i` 根据文件内容自动识别 JSON 数组、profiler `op_summary` CSV（包含 `Op Name`、`OP Type` 列）或 `kernel_details` CSV（包含 `Name`、`Type`、`Accelerator Core` 列），不依赖文件名或扩展名。JSON 继续支持 `theo` 和 `eng`；CSV 仅支持 `theo`，且必须指定 `-s`。

以理论极限模式的ADD算子为例，将如下内容保存为 `input.json`：

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
字段说明

| 字段 | 类型 | 必填 | 说明 |
|------|------|----|------|
| `op_name` | string | 是 | 算子名称，如 `"MatMul"`、`"Add"` |
| `backend_type` | string | 否 | 建模模式：`"theo"` 或 `"eng"`；省略时由命令行模式注入，若填写则必须与命令行模式一致 |
| `input_shapes` | list[list[int]] | 是 | 各输入 Tensor 的形状，如 `[[2048, 512], [512, 1024]]` |
| `output_shapes` | list[list[int]] | 是 | 各输出 Tensor 的形状 |
| `input_precision` | list[string] | 是 | 各输入 Tensor 的数据类型，如 `["FLOAT16", "FLOAT16"]` |
| `output_precision` | list[string] | 是 | 各输出 Tensor 的数据类型 |
| `core_num` | int | 否 | 使用的计算核数，默认取芯片最大核数 |

也可以直接使用上述两种 profiler CSV。CSV 形状单元格以分号 `;` 分隔 Tensor，以逗号 `,` 分隔维度；空的 Tensor 片段表示标量 `[]`，不能删除。例如 `;2048,512;` 表示 `[[], [2048, 512], []]`；`N/A` 是无效值，不表示标量。

CSV 使用所选 SoC 的最大核数和模型默认属性，不从 `Block Num` 推断物理核数，不从 `ND` 推断 attention 的语义布局，也不推断其他算子属性。缺少必需属性会导致该行失败；即使模型有默认值，也不保证还原真实语义，例如 ReduceSum 默认归约最后一轴。


---

## 5. 运行

```shell
# 理论极限模式，结果写入默认目录 msopmodeling_output/
msopmodeling theo -i input.json -s 910B4

# 工程可达模式，结果写入 result_dir/
msopmodeling eng -i input.json -s 910B4 -o result_dir

# profiler op_summary CSV，仅支持理论极限模式，必须指定芯片
msopmodeling theo -i op_summary.csv -s 910B4 -o result_op_summary

# profiler kernel_details CSV，同样使用理论极限模式
msopmodeling theo -i kernel_details.csv -s 910B4 -o result_kernel_details
```

**参数说明：**

| 参数 | 必填 | 说明 |
|------|----|------|
| `theo` / `eng` | 是  | 建模模式；与 JSON 中 `backend_type` 冲突时会报错退出 |
| `-i / --input` | 是  | 输入文件路径，按内容识别 JSON 数组或上述两种 CSV；CSV 仅支持 `theo` |
| `-s / --soc-type` | 清单查询、CSV 预测时必填 | 芯片型号由 `ArchName` 定义，如 `910B1`、`910B4`、`950`；JSON 预测时可省略，但每条输入必须提供 `accelerator` 配置路径 |
| `-o / --output` | 否  | 输出目录，默认 `msopmodeling_output`；不存在时自动创建，已存在时直接复用 |
| `-v / --verbose` | 否  | 输出 DEBUG 级别详细日志 |

### 5.1 查看指定模式下的算子清单

```shell
msopmodeling theo list -s 910B4
msopmodeling eng  list -s 910B4
msopmodeling eng  list -s 950
```

`list` 按算子注册的架构支持范围查询清单，不接受 `-i`、`-o`，也不会产生输出文件；`-s` 必填。省略 `list` 时执行性能预测。

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

CSV 的每条数据行按原始顺序从 `OP_0` 开始编号（不含表头），不支持或无效的行也占用编号，不会跳过后重新编号。成功行保留正常的 `latency` 等预测字段，并附带 CSV 来源信息；不支持、无效或预测失败的行保留来源信息，并记录 `error` 和 `error_kind`，不能当作有效时延结果。

CSV 的单行错误不会中断后续行处理。处理结束后，终端按错误类别分组汇总；只要有失败或不支持的行，工具会先保存结果，再以退出码 `1` 结束。文件级错误（如文件无法读取、格式无法识别）则直接终止，不进入逐行容错流程。

`result.json` 的 JSON 结构如下：

```json
{
  "OP_0": {
    "op_name": "TheoAdd",
    "latency": 20.704635592517192,
    "component_latency": {
      "CUBE": 0,
      "MTE1": 0.0,
      "MTE2": 0,
      "FIXPIPE": 0,
      "VEC": 1.654949494949495,
      "MTE2_AIV": 15.682507068407942,
      "MTE3": 5.022128524109251
    },
    "l2_hit_rate": 0.0,
    "cube_utilization_rate": 0.0,
    "vec_utilization_rate": 0.07993135100371464,
    "mem_volume": {
      "GM_2_UB": 16777216,
      "UB_2_L2": 8388608
    },
    "compute_workload": {
      "CUBE": 0,
      "VEC": 0
    },
    "gm_volume": 0
  }
}
```

**关键字段解读：**

| 字段 | 单位    | 含义                             |
|------|-------|--------------------------------|
| `latency` | μs    | **算子总时延**（核心指标），流水仿真给出的端到端时延   |
| `component_latency.CUBE` | μs    | Cube 矩阵运算单元耗时（向量算子为 0）          |
| `component_latency.MTE1` | μs    | Cube 核 L1→L0 数据搬运耗时             |
| `component_latency.MTE2` | μs    | Cube 核 GM→L1 数据搬运耗时             |
| `component_latency.MTE2_AIV` | μs    | 向量核 GM→UB 数据搬运耗时（向量算子的访存主路径）   |
| `component_latency.MTE3` | μs    | 向量核 UB→GM 输出写回耗时               |
| `component_latency.FIXPIPE` | μs    | Cube 后处理流水段耗时（执行 bias 加、量化、格式转换等后处理） |
| `component_latency.VEC` | μs    | 向量运算耗时（向量算子为主要耗时段）             |
| `cube_utilization_rate` | -     | Cube 单元利用率，越接近 `1.0` 说明计算效率越高  |
| `vec_utilization_rate` | -     | 向量单元利用率                        |
| `l2_hit_rate` | -     | L2 缓存命中率，越高说明访存局部性越好，搬运开销越小    |
| `mem_volume` | Bytes | 各存储层间的数据搬运量，字段名反映具体搬运路径（如 `GM_2_UB`、`UB_2_L2`） |

**性能瓶颈快速判断（向量算子）：**

- `MTE2_AIV > VEC`：访存受限（带宽瓶颈），数据搬运耗时主导，可考虑提高 L2 命中率或减少搬运量
- `VEC > MTE2_AIV`：计算受限（算力瓶颈），`vec_utilization_rate` 越高越好
