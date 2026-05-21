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
```

---

## 4. 准备输入文件

输入为一个 JSON 数组，每个元素描述一个待预测的算子。

### 4.1 公共字段说明

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `op_name` | string | 是 | 算子名称，如 `"MatMul"`、`"Add"` |
| `backend_type` | string | 是 | 建模模式：`"theo"` 或 `"eng"` |
| `input_shapes` | list[list[int]] | 是* | 各输入 Tensor 的形状，如 `[[2048, 512], [512, 1024]]` |
| `output_shapes` | list[list[int]] | 是* | 各输出 Tensor 的形状 |
| `input_precision` | list[string] | 是 | 各输入 Tensor 的数据类型，如 `["FLOAT16", "FLOAT16"]` |
| `output_precision` | list[string] | 是 | 各输出 Tensor 的数据类型 |
| `core_num` | int | 否 | 使用的计算核数，默认取芯片最大核数 |

**支持的数据类型：** `FLOAT`、`FLOAT16`、`BF16`、`INT8`、`INT32`、`INT64`

**支持的芯片型号（用于 `-s` 参数）：**

| 系列 | 型号              |
|------|-----------------|
| 昇腾 910 系列 | `910B1`,`910B4` |


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

---

## 5. 运行

```shell
# 理论极限模式，针对 910B1 芯片
msopmodeling -i input_theo.json -s 910B1

# 工程可达模式，结果写入文件
msopmodeling -i input_eng.json -s 910B4 -o result.json
```

**完整参数说明：**

| 参数 | 必填 | 说明 |
|------|----|------|
| `-i / --input` | 是  | 输入 JSON 文件路径 |
| `-o / --output` | 否  | 输出 JSON 文件路径；省略则打印到标准输出 |
| `-s / --soc-type` | 是  | 芯片型号（如 `910B1`、`910B4`） |
| `-v / --verbose` | 否  | 输出 DEBUG 级别详细日志，便于排查问题 |

---

## 6. 查看输出结果

成功执行后，输出如下 JSON 结构（以 MatMul 工程模式为例）：

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

输出 JSON 中每个键（`OP_0`、`OP_1` …）对应输入数组中的一个算子，按顺序编号。

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
