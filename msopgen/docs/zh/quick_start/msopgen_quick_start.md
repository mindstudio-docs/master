# msOpGen算子调试工具快速入门

<br>

## 1. 概述

msOpGen 工具在算子开发过程中可自动生成自定义算子工程，使用户能够聚焦于算子的核心逻辑与算法实现，避免在项目搭建、编译配置等重复性工作上耗费大量时间，从而显著提升开发效率。    
本文档基于入门教程中开发的简易加法算子，演示 msOpGen 工具的核心功能，帮助初学者直观体会其在算子开发过程中带来的高效性与便捷性。

### 1.1 建议

本章节以您已完成<a href="https://gitcode.com/Ascend/msot/blob/master/docs/zh/quick_start/op_tool_quick_start.md" target="_blank">《算子开发工具快速入门》</a>的全流程操作为前提；若尚未体验，建议先完成该指南以获得更佳的学习效果。

### 1.2 环境准备

请严格按照<a href="https://gitcode.com/Ascend/msot/blob/master/docs/zh/quick_start/installation_guide.md" target="_blank">《昇腾 AI 算子开发工具链学习环境安装指南》</a>完成环境安装与工作区配置。
即使您已具备类似环境，也需按该指南重新执行一遍，以确保所有依赖组件、环境变量等完整且一致。

## 2. 操作步骤

### 2.1 【环境】运行环境预检

#### 2.1.1 确认 Python 依赖包已安装

执行以下命令，若输出"All is OK"，则表明所需 Python 包及其版本均满足规范：

```shell
python3 -c "import numpy, sympy, scipy, attrs, psutil, decorator; from packaging import version; assert version.parse(numpy.__version__) <= version.parse('1.26.4'); print('All is OK')"
```

若报错，请参照[第 1.2 节](#12-环境准备)进行正确安装。

### 2.2 【开发】构建算子工程（msOpGen）

算子工程较为复杂且包含大量框架代码，msOpGen 工具可自动生成完整的算子工程框架，使开发者聚焦于核心算法实现，避免在项目搭建、编译配置等重复性工作上耗费时间。先跟着操作体验效果，原理部分可稍后阅读：

#### 2.2.1 创建子工作区目录

创建名为`src` 的子目录，作为算子源码根目录：

```shell
rm -rf ~/ot_demo/workspace/src && mkdir -p ~/ot_demo/workspace/src && cd ~/ot_demo/workspace/src
```

#### 2.2.2 开发算子定义配置文件

> [!NOTE]   
> **知识点（可选阅读）：msOpGen输入配置文件**   
> 自定义格式的JSON配置文件，可以简单类比理解为定义了一个C语言函数的声明，包括：函数名、入参及返回值的类型信息。
> 比如 msopgen_demo.json 中定义了算子的名字、输入输出变量的名字、类型、数据排布格式。
> 算子函数的声明代码统一由工具生成，生成一个空函数（只有函数名、入参和返回值），函数体需要用户自己实现。

请将如下配置文件内容保存为文件 msopgen_demo.json：

```json
[
    {
        "op": "AddCustom",
        "language": "cpp",
        "input_desc": [
            {
                "name": "x",
                "param_type": "required",
                "format": [
                    "ND"
                ],
                "type": [
                    "float16"
                ]
            },
            {
                "name": "y",
                "param_type": "required",
                "format": [
                    "ND"
                ],
                "type": [
                    "float16"
                ]
            }
        ],
        "output_desc": [
            {
                "name": "z",
                "param_type": "required",
                "format": [
                    "ND"
                ],
                "type": [
                    "float16"
                ]
            }
        ]
    }
]
```

#### 2.2.3 基于配置生成代码框架

**1. 获取芯片型号并拼接参数**   
参考《[芯片SoC类型获取方法](https://gitcode.com/Ascend/msot/blob/master/docs/zh/quick_start/get_chip_soc_type.md)》获取芯片类型，例如 Ascend910B4。

参数 -c：芯片类型，格式为 `aicpu`/`ai_core-{首字母小写芯片SoC型号}`，ai_core拼接后的示例为：ai_core-ascend910B4、ai_core-ascend910_9392。   

**2. 生成 Ascend C 算子工程**   
执行以下命令，请将 -c 参数替换上节查询的拼接值（<span style="color:#e60000;">**注意**</span>：**其中的减号和下划线不能写错，例如：ai<span style="color:#e60000;">_</span>core<span style="color:#e60000;">-</span>ascend910B4**）：

```shell
msopgen gen -i msopgen_demo.json -c xxx -lan cpp -out AddCustom
```

#### 2.2.4 查看生成的结果   

> [!NOTE]   
> **知识点（可选阅读）：关键概念**       
> Host侧：运行于CPU的代码，负责数据预处理、任务调度及算子调用；   
> Kernel侧：运行于NPU的代码，负责执行实际的大规模并行计算逻辑；   
> Tiling：将大规模数据分块处理，以提高Local Memory利用率并优化内存访问效率。

生成的工程结构看起来很庞大复杂，但我们**仅需关注标记为【用户扩展点】的三个C++文件**，其余均为框架代码，无特殊需求则无需查看或修改：

```text
AddCustom
├── build.sh                 // 编译入口脚本
├── CMakeLists.txt           // 算子工程的CMakeLists.txt
├── framework                // 算子插件实现文件目录，单算子模型文件的生成不依赖算子适配插件，无需关注
│   ├── CMakeLists.txt
│   └── tf_plugin
├── op_host                  // Host侧实现文件
│   ├── add_custom.cpp       // 【用户扩展点】算子原型注册、shape推导、信息库、tiling实现等内容文件
│   └── CMakeLists.txt
├── op_kernel                // Kernel侧实现文件
│   ├── add_custom.cpp       // 【用户扩展点】算子代码实现文件 
│   ├── add_custom_tiling.h  // 【用户扩展点】算子tiling定义文件
│   └── CMakeLists.txt
└── CMakePresets.json        // 编译配置项
```

### 2.3 实现核心逻辑

> [!NOTE]    
> **知识点（可选阅读）：算子核心代码文件实现原理**  
> op_host/add_custom.cpp：实现Host侧的Tiling计算逻辑与算子原型注册；   
> op_kernel/add_custom_tiling.h：定义Tiling分块策略的数据结构；  
> op_kernel/add_custom.cpp：实现Kernel侧加法算子的具体计算逻辑（GM→UB搬运→向量加法→UB→GM写回）；     
> 若需深入理解上述三个文件的功能与协作机制，除参考代码注释外，建议详细阅读<a href="https://www.hiascend.com/developer/blog/details/0239124507827469022" target="_blank">《昇腾Ascend C编程入门教程（纯干货）》</a>。

#### 2.3.1 开发 op_kernel/add_custom_tiling.h

按如下修改，代码实现原理请参考代码注释或阅读<a href="https://www.hiascend.com/developer/blog/details/0239124507827469022" target="_blank">《昇腾Ascend C编程入门教程（纯干货）》</a>：

```cpp
/**
 * @file add_custom_tiling.h
 *
 * Copyright (C) 2023-2024. Huawei Technologies Co., Ltd. All rights reserved.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
 */
#ifndef ADD_CUSTOM_TILING_H
#define ADD_CUSTOM_TILING_H
#include "register/tilingdata_base.h"

namespace optiling {

    // Tiling算法信息结构体定义，比如数据总长度/TileNum等，由开发者自行设计，由框架负责传递
    BEGIN_TILING_DATA_DEF(TilingData) // 声明Tiling结构体名称
        TILING_DATA_FIELD_DEF(uint32_t, totalLength);  // 自定义结构体成员的类型和名称：总计算数据量
        TILING_DATA_FIELD_DEF(uint32_t, tileNum);      // 自定义结构体成员的类型和名称：每个核上总计算数据分块个数
    END_TILING_DATA_DEF;

    // 将TilingData类注册到对应的AddCustom算子
    REGISTER_TILING_DATA_CLASS(AddCustom, TilingData)

  } // namespace optiling

#endif // ADD_CUSTOM_TILING_H
```

#### 2.3.2 开发 op_host/add_custom.cpp

打开生成的 `op_host/add_custom.cpp` 文件，定位并提取包含 `this->AICore().AddConfig` 的代码行，并保存下来，例如：

```cpp
this->AICore().AddConfig("ascend910_93");
```

按以下方式修改，但需将其中涉及 `this->AICore().AddConfig` 的代码行替换为上述保存的实际内容（因 SoC 信息随运行环境而异，不可硬编码）：

```cpp
/**
 * @file add_custom.cpp
 *
 * Copyright (C) 2023-2024. Huawei Technologies Co., Ltd. All rights reserved.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
 */
#include "../op_kernel/add_custom_tiling.h"
#include "register/op_def_registry.h"

namespace optiling {
    /**
     * 此函数使用CANN框架编程模式，若未学过可能较难理解。当前只需理解其设置了3个数字信息（数据总长、tile数、核数）
     * 并传递到核函数即可，不影响对算子工具使用的理解。详细原理流程请参考《Ascend C算子开发指南》相关章节。
     * 
     * 功能：计算算子分块的相关信息（数据总长度、tile数量等）。将其注册到下方的算子定义中后，
     * CANN框架会调用该函数，并根据返回的数据进行后续计算。
     * 
     * 参数 TilingContext* context：输入和输出都通过此上下文结构参数来承载。
     * 开发者可以从上下文结构中获取算子的输入、输出以及属性信息（即Tiling的输入）；经过Tiling计算后，
     * 获取到TilingData数据结构（带有切分算法相关参数）、blockDim变量等（即Tiling的输出），
     * 并将这些输出设置到上下文结构中，供后续计算使用。
     * 
     */
    static ge::graphStatus TilingFunc(gert::TilingContext *context)
    {
        // 第一步：设置tiling信息（数据总长、tile数量）到context上下文中
        uint32_t totalLength = context->GetInputShape(0)->GetOriginShape().GetShapeSize(); // 获取输入数据的总长度
        const uint32_t TILE_NUM = 8;  // 每个核上分8个tile进行计算
        TilingData tiling;
        tiling.set_totalLength(totalLength);
        tiling.set_tileNum(TILE_NUM);
        tiling.SaveToBuffer(context->GetRawTilingData()->GetData(), context->GetRawTilingData()->GetCapacity());
        context->GetRawTilingData()->SetDataSize(tiling.GetDataSize()); // 将tiling数据结构保存到上下文结构中

        // 第二步：设置使用多少个AICore核进行计算的信息到context上下文中
        const uint32_t BLOCK_DIM = 8; // 使用8个核进行计算
        context->SetBlockDim(BLOCK_DIM);
        
        return ge::GRAPH_SUCCESS;
    }
} // namespace optiling

namespace ops {
    /**
     * 此处使用CANN框架编程模式，若未学过可能较难理解。当前只需理解其设置了2个输入参数和1个输出参数的算子信息即可，
     * 不影响对算子工具使用的理解。详细原理流程请参考《Ascend C算子开发指南》相关章节。
     * 
     * 功能：该类定义了一个自定义的加法算子，支持两个FLOAT16类型张量的加法运算，
     * 并配置了在不同Ascend芯片上的运行参数。
     */
    class AddCustom : public OpDef {
    public:
        explicit AddCustom(const char *name) : OpDef(name)
        {
            // 配置第一个输入参数x：必需参数，数据类型为FLOAT16，格式为ND
            this->Input("x")
                .ParamType(REQUIRED)
                .DataType({ge::DT_FLOAT16})
                .Format({ge::FORMAT_ND});
            
            // 配置第二个输入参数y：必需参数，数据类型为FLOAT16，格式为ND
            this->Input("y")
                .ParamType(REQUIRED)
                .DataType({ge::DT_FLOAT16})
                .Format({ge::FORMAT_ND});
            
            // 配置输出参数z：必需参数，数据类型为FLOAT16，格式为ND
            this->Output("z")
                .ParamType(REQUIRED)
                .DataType({ge::DT_FLOAT16})
                .Format({ge::FORMAT_ND});

            // 配置AICore计算单元，设置分块策略和兼容的芯片型号
            this->AICore().SetTiling(optiling::TilingFunc);
            this->AICore().AddConfig("ascend910b");
        }
    };

    // 注册AddCustom算子到算子库中
    OP_ADD(AddCustom);
} // namespace ops
```

#### 2.3.3 开发 op_kernel/add_custom.cpp

按如下修改，代码实现原理请参考代码注释或阅读<a href="https://www.hiascend.com/developer/blog/details/0239124507827469022" target="_blank">《昇腾Ascend C编程入门教程（纯干货）》</a>：

```cpp
/**
 * @file add_custom.cpp
 *
 * Copyright (C) 2022-2024. Huawei Technologies Co., Ltd. All rights reserved.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
 */
#include "kernel_operator.h"
constexpr int32_t BUFFER_NUM = 2; // tensor num for each queue

class KernelAdd {
public:
    __aicore__ inline KernelAdd() {}
    /**
     * @brief 初始化函数，用于设置数据块长度、分片数量以及全局内存和流水线缓冲区
     *
     * @param x 全局内存中输入数据X的起始地址
     * @param y 全局内存中输入数据Y的起始地址
     * @param z 全局内存中输出数据Z的起始地址
     * @param totalLength 数据总长度
     * @param tileNum 分片数量
     */
    __aicore__ inline void Init(GM_ADDR x, GM_ADDR y, GM_ADDR z, uint32_t totalLength, uint32_t tileNum)
    {
        // 计算当前AI Core处理的数据长度，将总长度按AI Core数量均分
        this->blockLength = totalLength / AscendC::GetBlockNum();
        this->tileNum = tileNum ? tileNum : 1;
        // 计算每个Tiling分片的长度，考虑BUFFER_NUM个流水线缓冲区的划分
        this->tileLength = this->blockLength / this->tileNum / BUFFER_NUM;

        // 设置全局内存缓冲区，为当前AI Core分配其负责的全局共享内存区域
        xGm.SetGlobalBuffer((__gm__ DTYPE_X *)x + this->blockLength * AscendC::GetBlockIdx(), this->blockLength);
        yGm.SetGlobalBuffer((__gm__ DTYPE_Y *)y + this->blockLength * AscendC::GetBlockIdx(), this->blockLength);
        zGm.SetGlobalBuffer((__gm__ DTYPE_Z *)z + this->blockLength * AscendC::GetBlockIdx(), this->blockLength);

        // 初始化流水线缓冲区，分别为输入队列X、Y和输出队列Z在UB(Local Memory)中分配内存空间
        pipe.InitBuffer(inQueueX, BUFFER_NUM, this->tileLength * sizeof(DTYPE_X));
        pipe.InitBuffer(inQueueY, BUFFER_NUM, this->tileLength * sizeof(DTYPE_Y));
        pipe.InitBuffer(outQueueZ, BUFFER_NUM, this->tileLength * sizeof(DTYPE_Z));
    }
        /**
         * @brief 处理数据的核心函数，执行数据搬运、AI Core计算和结果回写的流水线循环
         *
         * 该函数通过循环处理多个Tiling分片，每个循环包含三个阶段：
         * 1. 调用CopyIn函数将数据从全局共享内存(Global Memory)搬运至UB(Local Memory)
         * 2. 调用Compute函数在AI Core上执行向量化加法计算
         * 3. 调用CopyOut函数将结果从UB(Local Memory)回写至全局共享内存(Global Memory)
         *
         * 循环次数由成员变量tileNum与常量BUFFER_NUM的乘积确定，
         * 表示需要处理的Tiling分片总数。
         */
    __aicore__ inline void Process()
    {
        // 计算总的流水线循环次数
        int32_t loopCount = this->tileNum * BUFFER_NUM;

        // 循环处理每个Tiling分片
        for (int32_t i = 0; i < loopCount; i++) {
            CopyIn(i);
            Compute(i);
            CopyOut(i);
        }
    }

private:
    /**
        * @brief 将全局内存中的数据分片搬运到本地UB缓冲区(Local Memory)
        * @param progress 当前处理的Tiling分片索引，用于计算全局共享内存中的数据偏移量
        *
        * 该函数负责从全局共享内存中读取第progress个Tiling分片，并将其搬运到本地LocalTensor中，
        * 然后将LocalTensor入队到对应的输入队列中，为后续AI Core计算做准备。
        */
    __aicore__ inline void CopyIn(int32_t progress)
    {
        // 分配本地LocalTensor用于存储输入数据
        AscendC::LocalTensor<DTYPE_X> xLocal = inQueueX.AllocTensor<DTYPE_X>();
        AscendC::LocalTensor<DTYPE_Y> yLocal = inQueueY.AllocTensor<DTYPE_Y>();

        // 从全局共享内存(Global Memory)搬运数据到本地UB(Local Memory)
        AscendC::DataCopy(xLocal, xGm[progress * this->tileLength], this->tileLength);
        AscendC::DataCopy(yLocal, yGm[progress * this->tileLength], this->tileLength);

        // 将本地LocalTensor入队供后续计算使用
        inQueueX.EnQue(xLocal);
        inQueueY.EnQue(yLocal);
    }
    /**
        * @brief 执行张量加法计算的核心函数
        * @param progress 进度标识，用于控制计算流程
        *
        * 该函数从输入队列中获取两个LocalTensor，执行向量化加法运算后将结果存入输出队列。
        * 主要包括数据出队、UB内存分配、AI Core向量化加法计算、结果入队和UB内存释放等步骤。
        */
    __aicore__ inline void Compute(int32_t progress)
    {
        // 从输入队列中取出第一个操作数LocalTensor
        AscendC::LocalTensor<DTYPE_X> xLocal = inQueueX.DeQue<DTYPE_X>();
        // 从输入队列中取出第二个操作数LocalTensor
        AscendC::LocalTensor<DTYPE_Y> yLocal = inQueueY.DeQue<DTYPE_Y>();
        // 从输出队列中分配结果LocalTensor的UB内存空间
        AscendC::LocalTensor<DTYPE_Z> zLocal = outQueueZ.AllocTensor<DTYPE_Z>();
        // 执行AI Core向量化加法运算：z = x + y
        AscendC::Add(zLocal, xLocal, yLocal, this->tileLength);
        // 将计算结果LocalTensor放入输出队列
        outQueueZ.EnQue<DTYPE_Z>(zLocal);
        // 释放第一个输入LocalTensor的UB内存资源
        inQueueX.FreeTensor(xLocal);
        // 释放第二个输入LocalTensor的UB内存资源
        inQueueY.FreeTensor(yLocal);
    }
    /**
     * @brief 将LocalTensor数据回写到全局内存(Global Memory)输出区域
     *
     * 该函数从输出队列中获取一个LocalTensor，将其数据复制到全局共享内存的指定位置，
     * 然后释放该LocalTensor的UB资源。主要用于AI Core算子的结果输出操作。
     *
     * @param progress 当前处理进度索引，用于计算全局共享内存中的目标写入位置
     */
    __aicore__ inline void CopyOut(int32_t progress)
    {
        // 从输出队列中获取LocalTensor
        AscendC::LocalTensor<DTYPE_Z> zLocal = outQueueZ.DeQue<DTYPE_Z>();
        // 将LocalTensor数据从UB(Local Memory)回写到全局共享内存(Global Memory)
        AscendC::DataCopy(zGm[progress * this->tileLength], zLocal, this->tileLength);
        // 释放LocalTensor的UB(Local Memory)资源
        outQueueZ.FreeTensor(zLocal);
    }

private:
    AscendC::TPipe pipe;
    AscendC::TQue<AscendC::TPosition::VECIN, BUFFER_NUM> inQueueX, inQueueY;
    AscendC::TQue<AscendC::TPosition::VECOUT, BUFFER_NUM> outQueueZ;
    AscendC::GlobalTensor<DTYPE_X> xGm;
    AscendC::GlobalTensor<DTYPE_Y> yGm;
    AscendC::GlobalTensor<DTYPE_Z> zGm;
    uint32_t blockLength;
    uint32_t tileNum;
    uint32_t tileLength;
};

/**
 * @brief 自定义加法核函数，在AI Core上执行向量加法操作
 *
 * 该函数作为昇腾AI Core算子的入口，负责初始化加法操作并处理Tiling分片计算。
 * 函数通过解析Tiling配置信息来管理大规模数据在多个AI Core上的协同处理。
 *
 * @param x 输入向量x的全局内存地址
 * @param y 输入向量y的全局内存地址
 * @param z 输出向量z的全局内存地址
 * @param workspace 工作空间内存地址，用于临时存储（当前未使用）
 * @param tiling Tiling配置信息的内存地址，包含数据分片策略与调度参数
 *
 * @note 该函数无返回值，计算结果直接写入输出地址z
 */
extern "C" __global__ __aicore__ void add_custom(GM_ADDR x, GM_ADDR y, GM_ADDR z, GM_ADDR workspace, GM_ADDR tiling)
{
    // 获取Tiling配置数据
    GET_TILING_DATA(tiling_data, tiling);

    // 创建并初始化加法算子对象
    KernelAdd op;
    op.Init(x, y, z, tiling_data.totalLength, tiling_data.tileNum);

    // 执行加法计算流水线
    op.Process();
}

#ifndef ASCENDC_CPU_DEBUG
// call of kernel function
/**
 * @brief 启动自定义向量加法算子的 AI Core 核函数
 *
 * 该函数封装了昇腾 AI Core 上的核函数调用，用于执行用户自定义的向量加法运算。
 * 通过传入 Tiling 配置、工作空间及设备内存指针，完成算子在 NPU 上的调度与执行。
 *
 * @param blockDim 本次启动的AI Core数量
 * @param l2ctrl 预留参数
 * @param stream 流对象，用于异步任务提交与执行依赖管理
 * @param x 输入张量 x 的设备内存地址(Global Memory)
 * @param y 输入张量 y 的设备内存地址(Global Memory)
 * @param z 输出张量 z 的设备内存地址，用于存储 x + y 的结果(Global Memory)
 * @param workspace 临时工作空间设备地址，供核函数内部中间计算使用
 * @param tiling Tiling策略数据结构地址，定义数据分块方式以优化 AI Core 计算吞吐与内存带宽利用率
 */
void add_custom_do(uint32_t blockDim, void *l2ctrl, void *stream, uint8_t *x, uint8_t *y, uint8_t *z,
                   uint8_t *workspace, uint8_t *tiling)
{
    // 启动AI Core执行自定义加法运算
    add_custom<<<blockDim, l2ctrl, stream>>>(x, y, z, workspace, tiling);
}
#endif
```

### 2.4 编译与部署算子

**1. 编译算子**  
执行构建脚本，成功后将在 build_out 目录下生成 .run 格式的算子部署包：

```shell
cd ~/ot_demo/workspace/src/AddCustom/
sed -i 's/--target $target -j$(nproc)/--target $target -j1/g' build.sh
bash ./build.sh
```

**2. 部署算子**   

> [!NOTE]   
> **知识点（可选阅读）：什么是部署算子**  
> 部署算子是指将算子注册到CANN框架中，本质上是将算子的二进制文件拷贝至系统公共目录，使其他程序能够通过标准接口（如CANN API或PyTorch等）
> 自动发现并调用该算子。\*.run格式的部署包可以简单理解为一种自解压的压缩包。

因各平台生成的算子部署包名称略有差异，执行以下脚本以自动定位并运行部署包（在固定环境中，实际等效于执行类似 ./build_out/custom_opp_ubuntu_aarch64.run 的命令）：

```shell
MY_OP_PKG=$(find ./build_out -maxdepth 1 -name "custom_opp_*.run" | head -1) && bash $MY_OP_PKG
```

**3. 加入动态库路径**   
部署成功后，按终端提示追加算子依赖的动态库路径：

```shell
export LD_LIBRARY_PATH=${ASCEND_OPP_PATH}/vendors/customize/op_api/lib:$LD_LIBRARY_PATH
echo "export LD_LIBRARY_PATH=${ASCEND_OPP_PATH}/vendors/customize/op_api/lib:$LD_LIBRARY_PATH" >> ~/.bashrc
```

### 2.5 验证算子功能

执行算子调用工程，验证算子功能（本例执行 1.0 + 2.0，预期结果为 3.0）：

```shell
mkdir ~/ot_demo/workspace/src/caller
cd ~/ot_demo/workspace/src/caller
curl -fLO --retry 10 --retry-all-errors --retry-delay 3 -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36" "https://raw.gitcode.com/Ascend/msot/raw/master/example/quick_start/msopgen/caller/{CMakeLists.txt,main.cpp,exec.py,run.sh}"
bash ./run.sh
```

> [!NOTE]
>
> **关于 NPU 设备选择的说明**   
> 执行如上 `run.sh` 脚本将实际运行算子。为便于学习，假设环境中所有 NPU 卡型号相同，系统将随机选择一张空闲卡执行任务。
> 若因随机选定的卡存在故障等原因需指定 NPU 卡，请根据 `npu-smi info` 命令返回的 NPU 信息，使用其顺序号（取值范围为 [0, NPU 数量 - 1]）按如下方式调用：
>
> ```shell
> bash ./run.sh 2
> ```

若输出如下内容，结果为 3.0，则表明算子已成功加载并计算正确：

```text
result is:
3.0 3.0 3.0 3.0 3.0 3.0 3.0 3.0 3.0 3.0 
test pass
```

若超过 30 秒未返回结果，可能是 NPU 卡繁忙，可按 Ctrl+C 终止后切换至其他空闲卡重试；若出现类似如下错误，可能原因包括：NPU卡异常（硬件故障、驱动问题等），/dev/hisi_hdc 设备异常（如容器内未成功挂载、缺乏访问权限、因线程数过多导致设备无法打开等），以及内存等系统资源不足等。    
错误码说明请参见：[《ACL错误码表》](https://www.hiascend.com/document/detail/zh/CANNCommunityEdition/850/API/appdevgapi/aclcppdevg_03_1345.html)，
请先解决 NPU 卡故障或更换为其他正常卡后再继续体验（指定 NPU 卡运行的方法详见上文“关于 NPU 设备选择的说明”）：

```text
aclrtSetDevice failed. ERROR: xxxxxx
Init acl failed. ERROR: 1
```

### 2.6 【FAQ】常见错误解决

#### 2.6.1 编译调用算子程序时报错如下，怎么解决？

```text
-- Build files have been written to: /root/ot_demo/workspace/src/caller/build
[ 50%] Building CXX object CMakeFiles/execute_add_op.dir/main.cpp.o
/root/ot_demo/workspace/src/caller/main.cpp:16:10: fatal error: aclnn_add_custom.h: No such file or directory
   16 | #include "aclnn_add_custom.h"
      |          ^~~~~~~~~~~~~~~~~~~~
compilation terminated.
gmake[2]: *** [CMakeFiles/execute_add_op.dir/build.make:76: CMakeFiles/execute_add_op.dir/main.cpp.o] Error 1
gmake[1]: *** [CMakeFiles/Makefile2:83: CMakeFiles/execute_add_op.dir/all] Error 2
```

**问题原因：** 算子部署时没有将 op_api/include/aclnn_add_custom.h 部署到正确的位置，导致找不到头文件。一种可能的原因是环境中存在环境变量 `ASCEND_CUSTOM_OPP_PATH` 且值不正确，或者存在多个以冒号间隔的路径，但目前部署头文件时只会成功拷贝到第一个路径中，后续路径均未拷贝。   
**解决方法：** 删除环境变量，执行`unset ASCEND_CUSTOM_OPP_PATH`，重新部署算子。   
