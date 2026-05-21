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
```

---

## 4. 准备输入文件

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
| `backend_type` | string | 是 | 建模模式：`"theo"` 或 `"eng"` |
| `input_shapes` | list[list[int]] | 是 | 各输入 Tensor 的形状，如 `[[2048, 512], [512, 1024]]` |
| `output_shapes` | list[list[int]] | 是 | 各输出 Tensor 的形状 |
| `input_precision` | list[string] | 是 | 各输入 Tensor 的数据类型，如 `["FLOAT16", "FLOAT16"]` |
| `output_precision` | list[string] | 是 | 各输出 Tensor 的数据类型 |
| `core_num` | int | 否 | 使用的计算核数，默认取芯片最大核数 |


---

## 5. 运行

```shell
msopmodeling -i input.json -s 910B4
```

**参数说明：**

| 参数 | 必填 | 说明 |
|------|----|------|
| `-i / --input` | 是  | 输入 JSON 文件路径 |
| `-s / --soc-type` | 是  | 芯片型号，当前支持 `910B1`、`910B4` |

---

## 6. 查看输出结果

成功执行后，输出如下 JSON 结构：

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
