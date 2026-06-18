# **MindStudio Tools Extension Library接口文档**

本节介绍MindStudio Tools Extension Library（工具扩展接口库，msTX）打点接口。可以自定义采集时间段或者关键函数的开始和结束时间点，识别关键函数或迭代等信息，对性能和算子问题快速定界。

默认情况下msTX API无任何功能，需要在用户应用程序中调用msTX API后，根据不同场景使能msTX打点功能，例如使用msprof命令行采集时配置--mstx=on、使用AscendCL API采集时配置ACL_PROF_MSPROFTX以及Ascend PyTorch Profiler接口采集时配置mstx=True等。

- 库文件libms_tools_ext.so路径：**${INSTALL_DIR}**/lib64/。
- 使用头文件编译时，用户程序编译时需链接dl库。头文件ms_tools_ext.h路径：**${INSTALL_DIR}**/include/mstx。

${INSTALL_DIR}请替换为CANN软件安装后文件存储路径。以root用户安装为例，安装后文件默认存储路径为：`/usr/local/Ascend/cann`。

**接口列表<a id="section6371427124715"></a>**

**表 1**  MindStudio mstx接口列表

|接口名称|功能简介|
|--|--|
|[mstxGetToolId](#mstxGetToolId)|用于获取当前劫持mstx接口的工具ID。|
|[mstxMarkA](#mstxMarkA)|标识瞬时事件。|
|[mstxRangeStartA](#mstxRangeStartA)|标识时间段事件的开始。|
|[mstxRangeEnd](#mstxRangeEnd)|标识时间段事件的结束。|
|[mstxDomainCreateA](#mstxDomainCreateA)|创建自定义domain。|
|[mstxDomainDestroy](#mstxDomainDestroy)|销毁指定的domain，销毁后的domain不能再次使用，需要重新创建。|
|[mstxDomainMarkA](#mstxDomainMarkA)|在指定的domain内，标记瞬时事件。|
|[mstxDomainRangeStartA](#mstxDomainRangeStartA)|在指定的domain内，标识时间段事件的开始。|
|[mstxDomainRangeEnd](#mstxDomainRangeEnd)|在指定的domain内，标识时间段事件的结束。|
|[mstxMemHeapRegister](#mstxMemHeapRegister)|注册内存池。|
|[mstxMemRegionsRegister](#mstxMemRegionsRegister)|注册内存池二次分配。|
|[mstxMemRegionsUnregister](#mstxMemRegionsUnregister)|注销内存池二次分配。|
|[mstxMemHeapUnregister](#mstxMemHeapUnregister)|注销内存池时，与之关联的Regions将一并被注销。|


## mstxGetToolId<a id="mstxGetToolId"></a>

**产品支持情况<a id="section8178181118225"></a>**

|产品|是否支持|
|--|:-:|
|昇腾910_95 AI处理器|√|
|Atlas A3 训练系列产品/Atlas A3 推理系列产品|√|
|Atlas A2 训练系列产品/Atlas A2 推理系列产品|√|
|Atlas 200I/500 A2 推理产品|√|
|Atlas 推理系列产品|√|
|Atlas 训练系列产品|√|


**功能说明<a id="zh-cn_topic_0000002446914857_section20806203412478"></a>**

用于获取当前劫持mstx接口的工具ID，工具ID宏定义如下：

无效值0，表示无工具拉起程序
```
#define MSTX_TOOL_INVALID_ID 0x0
```  

0x1000，表示程序由《[msprof模型调优工具](https://www.hiascend.com/document/detail/zh/canncommercial/83RC1/devaids/Profiling/atlasprofiling_16_0010.html)》或《[MSPTI](https://www.hiascend.com/document/detail/zh/canncommercial/83RC1/devaids/Profiling/atlasprofiling_16_1153.html)》工具拉起
```
#define MSTX_TOOL_MSPROF_ID 0x1000
```

0x1001，表示程序由[算子调优（msProf）](https://www.hiascend.com/document/detail/zh/canncommercial/83RC1/devaids/optool/atlasopdev_16_0082.html)工具拉起
```
#define MSTX_TOOL_MSOPPROF_ID 0x1001
```     

0x1002，表示程序由[异常检测（msSanitizer）](https://www.hiascend.com/document/detail/zh/canncommercial/83RC1/devaids/optool/atlasopdev_16_0039.html)工具拉起
```
#define MSTX_TOOL_MSSANITIZER_ID 0x1002  
```

0x1003，表示程序由《[msLeaks内存泄漏检测工具](https://www.hiascend.com/document/detail/zh/canncommercial/83RC1/devaids/msleaks/atlas_msleaks_0001.html)》拉起
```
#define MSTX_TOOL_MSLEAKS_ID 0x1003      
```

**函数原型<a id="zh-cn_topic_0000002446914857_section1121883194711"></a>**

```
void mstxGetToolId(uint64 *id)
```

**参数说明<a id="zh-cn_topic_0000002446914857_section11506138144714"></a>**

**表 1**  参数说明

|参数|输入/输出|说明|
|--|--|--|
|id|输出|作为出参，返回当前劫持mstx接口的工具ID。<br>数据类型：uint64 *。|


**返回值说明<a id="zh-cn_topic_0000002446914857_section446682320445"></a>**

无

**调用示例<a id="zh-cn_topic_0000002446914857_section16621124213476"></a>**

```py
uint64 id;
mstxGetToolId(&id);
```

## mstxMarkA<a id="mstxMarkA"></a>

**产品支持情况<a id="section8178181118225"></a>**

|产品|是否支持|
|--|:-:|
|昇腾910_95 AI处理器|√|
|Atlas A3 训练系列产品/Atlas A3 推理系列产品|√|
|Atlas A2 训练系列产品/Atlas A2 推理系列产品|√|
|Atlas 200I/500 A2 推理产品|√|
|Atlas 推理系列产品|√|
|Atlas 训练系列产品|√|


**功能说明<a id="section20806203412478"></a>**

标识瞬时事件。

**函数原型<a id="section1121883194711"></a>**

```
void mstxMarkA(const char *message, aclrtStream stream)
```

**参数说明<a id="section11506138144714"></a>**

**表 1**  参数说明

|参数名|输入/输出|说明|
|--|--|--|
|message|输入|打点携带信息字符串指针。<br>传入的message字符串长度要求：MSPTI场景：不能超过255字节。<br>非MSPTI场景（例如msprof命令行、Ascend PyTorch Profiler）：不能超过156字节。<br>message不能传入空指针。|
|stream|输入|用于执行打点任务的stream。<br>配置为nullptr时，只标记Host侧的瞬时事件。<br>配置为有效的stream时，标识Host侧和对应Device侧的瞬时事件。|


**返回值说明<a id="section16621124213476"></a>**

无

## mstxRangeStartA<a id="mstxRangeStartA"></a>

**产品支持情况<a id="section8178181118225"></a>**

|产品|是否支持|
|--|:-:|
|昇腾910_95 AI处理器|√|
|Atlas A3 训练系列产品/Atlas A3 推理系列产品|√|
|Atlas A2 训练系列产品/Atlas A2 推理系列产品|√|
|Atlas 200I/500 A2 推理产品|√|
|Atlas 推理系列产品|√|
|Atlas 训练系列产品|√|


**功能说明<a id="zh-cn_topic_0000002016210401_section20806203412478"></a>**

mstx range指定范围能力的起始位置标记。

**函数原型<a id="section1121883194711"></a>**

C/C++：

```c
mstxRangeId mstxRangeStartA(const char *message, aclrtStream stream)
```

Python：

```py
mstx.range_start(message, stream)
```

**参数说明<a id="zh-cn_topic_0000002016210401_section11506138144714"></a>**

**表 1**  参数说明

|参数|输入/输出|说明|
|--|--|--|
|message|输入|message为标记的文字，携带打点信息。<br>C/C++中数据类型：const char *。<br>Python中，message为字符串。默认None。<br>传入的message字符串长度要求：MSPTI场景：不能超过255字节。<br>非MSPTI场景（例如msprof命令行、Ascend PyTorch Profiler）：不能超过156字节。<br>message不能传入空指针。|
|stream|输入|stream表示使用mark的线程。<br>C/C++中数据类型：aclrtStream。<br>Python中stream是aclrtStream对象。默认None。<br>配置为nullptr时，只标记Host侧的瞬时事件。<br>配置为有效的stream时，标识Host侧和对应Device侧的瞬时事件。|


**返回值说明<a id="zh-cn_topic_0000002016210401_section16621124213476"></a>**

如果返回0，则表示失败。

**调用示例<a id="zh-cn_topic_0000002016210401_section377820328555"></a>**

- C/C++调用方法：<a id="c调用方法"></a>

    ```c
    ...
    bool RunOp()
    {
    // create op desc
    ...
    const char *message = "h1";
    mstxRangeId id = mstxRangeStartA(message, NULL);
    ...
    // Run op
    if
    (!opRunner.RunOp()) {
    ERROR_LOG("Run
    op failed");
    return false;
    }
    mstxRangeEnd(id);
    ...
    }
    ```

- **Python**调用方法一：<a id="python调用方法"></a>

    通过Python API接口，以C/C++语言实现相关接口内容并编译生成so，相关so在PYTHONPATH中可以被Python直接引用。

    ```py
    import mstx
    mstx.range_start("aaa")
    print(1)
    mstx.range_end(1)
    import torch
    import torch_npu
    a = torch.Tensor([1,2,3,4]).npu()
    b = torch.Tensor([1,2,3,4]).npu()
    hi_str = "hi"
    hello_str = "hello"
    hi_id = mstx.range_start(hi_str, None)
    c = a + b
    hello_id = mstx.range_start(hello_str, stream=None)
    d = a - b
    mstx.range_end(hi_id)
    e = a * b
    mstx.range_end(hello_id)
    ```

- **Python**调用方法二：

    直接使用Python开发，通过ctypes.CDLL("libms_tools_ext.so")直接引用原mstx的so文件，并使用其中提供的API。

    ```py
    import mstx
    import torch
    import torch_npu
    import acl
    import sys
    import ctypes
    lib = ctypes.CDLL("libms_tools_ext.so")
    # 定义函数的参数类型和返回类型
    lib.mstxRangeStartA.argtypes = [ctypes.c_char_p, ctypes.c_void_p]
    lib.mstxRangeStartA.restype = ctypes.c_uint64
    lib.mstxRangeEnd.argtypes = [ctypes.c_uint64]
    lib.mstxRangeEnd.restype = None
    a = torch.Tensor([1,2,3,4]).npu()
    b = torch.Tensor([1,2,3,4]).npu()
    # 创建一个ctypes.c_char_p指针
    hi_str = b"hi"
    hi_ptr = ctypes.c_char_p(hi_str)
    hi_id = ctypes.c_uint64()
    # 创建一个ctypes.c_char_p指针
    hello_str = b"hello"
    hello_ptr = ctypes.c_char_p(hello_str)
    hello_id = ctypes.c_uint64()
    # 调用函数
    hi_id.value = lib.mstxRangeStartA(hi_ptr, None)
    c = a + b
    hello_id.value = lib.mstxRangeStartA(hello_ptr, None)
    d = a - b
    lib.mstxRangeEnd(hi_id)
    e = a * b
    lib.mstxRangeEnd(hello_id)
    ```

## mstxRangeEnd<a id="mstxRangeEnd"></a>

**产品支持情况<a id="section8178181118225"></a>**

|产品|是否支持|
|--|:-:|
|昇腾910_95 AI处理器|√|
|Atlas A3 训练系列产品/Atlas A3 推理系列产品|√|
|Atlas A2 训练系列产品/Atlas A2 推理系列产品|√|
|Atlas 200I/500 A2 推理产品|√|
|Atlas 推理系列产品|√|
|Atlas 训练系列产品|√|


**功能说明<a id="zh-cn_topic_0000001979850148_section20806203412478"></a>**

mstx range指定范围能力的结束位置标记。

**函数原型<a id="zh-cn_topic_0000001979850148_section1121883194711"></a>**

C/C++函数原型：

```c
void mstxRangeEnd(mstxRangeId id)
```

Python函数：

```py
mstx.range_end(range_id)
```

**参数说明<a id="zh-cn_topic_0000001979850148_section11506138144714"></a>**

**表 1**  参数说明

|参数|输入/输出|说明|
|--|--|--|
|id（C/C++）|输入|通过mstxRangeStartA返回的ID（C/C++）。|
|range_id（Python）|输入|通过mstx.range_start返回的range_id（Python）。|


**返回值说明<a id="zh-cn_topic_0000001979850148_section16621124213476"></a>**

如果返回0，则表示失败。

**调用示例<a id="zh-cn_topic_0000001979850148_section377820328555"></a>**

C/C++调用：mstxRangeEnd接口需要与mstxRangeStartA配合使用，具体示例请参考[C/C++调用方法](#c调用方法)。

Python调用：mstx.range_end接口需要与mstx.range_start配合使用，具体示例请参考[Python调用方法](#python调用方法)。

## mstxDomainCreateA<a id="mstxDomainCreateA"></a>

**产品支持情况<a id="section8178181118225"></a>**

|产品|是否支持|
|--|:-:|
|昇腾910_95 AI处理器|√|
|Atlas A3 训练系列产品/Atlas A3 推理系列产品|√|
|Atlas A2 训练系列产品/Atlas A2 推理系列产品|√|
|Atlas 200I/500 A2 推理产品|√|
|Atlas 推理系列产品|√|
|Atlas 训练系列产品|√|


**功能说明<a id="section20806203412478"></a>**

创建自定义的mstx域。

**domain（域）**：用于对打点数据进行划分，便于用户自定义管理打点数据，不指定domain的打点数据均属于默认域（域名：default）。默认情况下，所有打点数据均属于默认域。

**函数原型<a id="section1121883194711"></a>**

```
mstxDomainHandle_t mstxDomainCreateA(const char* id)
```

**参数说明<a id="section11506138144714"></a>**

**表 1**  参数说明

|参数名|输入/输出|说明|
|--|--|--|
|id|输入|要创建的域的名称。<br>数据类型：const char *。<br>默认域名为globalDomain。<br>最大长度为1023字节，仅支持数字、大小写字母和_符号。<br>MSPTI场景：不能超过255字节。<br>非MSPTI场景（例如msprof命令行、Ascend PyTorch Profiler）：不能超过1024字节。|


**返回值说明<a id="section16621124213476"></a>**

返回有效的domain句柄，表示接口执行成功；返回nullptr，表示接口执行失败。

**调用示例<a id="zh-cn_topic_0000002180600114_section16621124213476"></a>**

```
mstxDomainHandle_t domain = mstxDomainCreateA("sample")
```

## mstxDomainDestroy<a id="mstxDomainDestroy"></a>

**产品支持情况<a id="section8178181118225"></a>**

|产品|是否支持|
|--|:-:|
|昇腾910_95 AI处理器|√|
|Atlas A3 训练系列产品/Atlas A3 推理系列产品|√|
|Atlas A2 训练系列产品/Atlas A2 推理系列产品|√|
|Atlas 200I/500 A2 推理产品|√|
|Atlas 推理系列产品|√|
|Atlas 训练系列产品|√|


**功能说明<a id="section20806203412478"></a>**

销毁指定的domain，销毁后的domain不能再次使用，需要重新创建。

**函数原型<a id="section1121883194711"></a>**

```
void mstxDomainDestroy (mstxDomainHandle_t domain)
```

**参数说明<a id="section11506138144714"></a>**

**表 1**  参数说明

|参数名|输入/输出|说明|
|--|--|--|
|domain|输入|指定要销毁的domain句柄。|


**返回值说明<a id="section16621124213476"></a>**

无

## mstxDomainMarkA<a id="mstxDomainMarkA"></a>

**产品支持情况<a id="section8178181118225"></a>**

|产品|是否支持|
|--|:-:|
|昇腾910_95 AI处理器|√|
|Atlas A3 训练系列产品/Atlas A3 推理系列产品|√|
|Atlas A2 训练系列产品/Atlas A2 推理系列产品|√|
|Atlas 200I/500 A2 推理产品|√|
|Atlas 推理系列产品|√|
|Atlas 训练系列产品|√|


**功能说明<a id="section20806203412478"></a>**

在指定的domain内，标记瞬时事件。

如果传入的domain已被销毁，日志生成告警提示，接口不再执行打点流程。

**函数原型<a id="section1121883194711"></a>**

```
void mstxDomainMarkA(mstxDomainHandle_t domain, const char *message, aclrtStream stream)
```

**参数说明<a id="section11506138144714"></a>**

**表 1**  参数说明

|参数名|输入/输出|说明|
|--|--|--|
|domain|输入|指定的domain句柄。|
|message|输入|打点携带信息字符串指针。传入的message字符串长度要求：MSPTI场景：不能超过255字节。非MSPTI场景（例如msprof命令行、Ascend PyTorch Profiler）：不能超过156字节。|
|stream|输入|用于执行打点任务的stream。配置为nullptr时，只标记Host侧的瞬时事件。配置为有效的stream时，标记Host侧和对应Device侧的瞬时事件。|


**返回值说明<a id="section16621124213476"></a>**

无

## mstxDomainRangeStartA<a id="mstxDomainRangeStartA"></a>

**产品支持情况<a id="section8178181118225"></a>**

|产品|是否支持|
|--|:-:|
|昇腾910_95 AI处理器|√|
|Atlas A3 训练系列产品/Atlas A3 推理系列产品|√|
|Atlas A2 训练系列产品/Atlas A2 推理系列产品|√|
|Atlas 200I/500 A2 推理产品|√|
|Atlas 推理系列产品|√|
|Atlas 训练系列产品|√|


**功能说明<a id="section20806203412478"></a>**

在指定的domain内，标识时间段事件的开始。

如果传入的domain已被销毁，日志打印告警提示，接口不再执行打点流程。

**函数原型<a id="section1121883194711"></a>**

```
mstxRangeId mstxDomainRangeStartA(mstxDomainHandle_t domain, const char *message, aclrtStream stream)
```

**参数说明<a id="section11506138144714"></a>**

**表 1**  参数说明

|参数名|输入/输出|说明|
|--|--|--|
|domain|输入|指定的domain句柄。|
|message|输入|打点携带信息字符串指针。<br>传入的message字符串长度要求：MSPTI场景：不能超过255字节。非MSPTI场景（例如msprof命令行、Ascend PyTorch Profiler）：不能超过156字节。|
|stream|输入|用于执行打点任务的stream。配置为nullptr时，只标记Host侧的瞬时事件。配置为有效的stream时，标识Host侧和对应Device侧的瞬时事件。|


**返回值说明<a id="section16621124213476"></a>**

range_id：标识该range，如果打点失败或domain已销毁，则返回0。

## mstxDomainRangeEnd<a id="mstxDomainRangeEnd"></a>

**产品支持情况<a id="section8178181118225"></a>**

|产品|是否支持|
|--|:-:|
|昇腾910_95 AI处理器|√|
|Atlas A3 训练系列产品/Atlas A3 推理系列产品|√|
|Atlas A2 训练系列产品/Atlas A2 推理系列产品|√|
|Atlas 200I/500 A2 推理产品|√|
|Atlas 推理系列产品|√|
|Atlas 训练系列产品|√|


**功能说明<a id="section20806203412478"></a>**

在指定的domain内，标识时间段事件的结束。

如果传入的domain已被销毁，日志打印告警提示，接口不再执行打点流程。

**函数原型<a id="section1121883194711"></a>**

```
void mstxDomainRangeEnd(mstxDomainHandle_t domain, mstxRangeId id)
```

**参数说明<a id="section11506138144714"></a>**

**表 1**  参数说明

|参数名|输入/输出|说明|
|--|--|--|
|domain|输入|指定的domain句柄。|
|id|输入|通过mstxDomainRangeStartA接口返回的id。|


**返回值说明<a id="section16621124213476"></a>**

无

## mstxMemHeapRegister<a id="mstxMemHeapRegister"></a>

**产品支持情况<a id="section8178181118225"></a>**

|产品|是否支持|
|--|:-:|
|昇腾910_95 AI处理器|√|
|Atlas A3 训练系列产品/Atlas A3 推理系列产品|√|
|Atlas A2 训练系列产品/Atlas A2 推理系列产品|√|
|Atlas 200I/500 A2 推理产品|√|
|Atlas 推理系列产品|√|
|Atlas 训练系列产品|√|


**功能说明<a id="zh-cn_topic_0000002216005989_section20806203412478"></a>**

注册内存池。用户在调用该接口注册内存池时，需确保该内存已提前申请。

**函数原型<a id="zh-cn_topic_0000002216005989_section1121883194711"></a>**

```
mstxMemHeapHandle_t mstxMemHeapRegister(mstxDomainHandle_t domain, mstxMemHeapDesc_t const *desc)
```

**参数说明<a id="zh-cn_topic_0000002216005989_section11506138144714"></a>**

**表 1**  参数说明

<a name="zh-cn_topic_0000002216005989_table827101275518"></a>
<table><thead align="left"><tr id="zh-cn_topic_0000002216005989_row429121265517"><th class="cellrowborder" valign="top" width="16.881688168816883%" id="mcps1.2.4.1.1"><p id="zh-cn_topic_0000002216005989_p1329121214558"><a name="zh-cn_topic_0000002216005989_p1329121214558"></a><a name="zh-cn_topic_0000002216005989_p1329121214558"></a>参数</p>
</th>
<th class="cellrowborder" valign="top" width="11.401140114011401%" id="mcps1.2.4.1.2"><p id="zh-cn_topic_0000002216005989_p10230141454318"><a name="zh-cn_topic_0000002216005989_p10230141454318"></a><a name="zh-cn_topic_0000002216005989_p10230141454318"></a>输入/输出</p>
</th>
<th class="cellrowborder" valign="top" width="71.71717171717171%" id="mcps1.2.4.1.3"><p id="zh-cn_topic_0000002216005989_p83121275519"><a name="zh-cn_topic_0000002216005989_p83121275519"></a><a name="zh-cn_topic_0000002216005989_p83121275519"></a>说明</p>
</th>
</tr>
</thead>
<tbody><tr id="zh-cn_topic_0000002216005989_row1131131265511"><td class="cellrowborder" valign="top" width="16.881688168816883%" headers="mcps1.2.4.1.1 "><p id="zh-cn_topic_0000002216005989_p7669321185110"><a name="zh-cn_topic_0000002216005989_p7669321185110"></a><a name="zh-cn_topic_0000002216005989_p7669321185110"></a>domain</p>
</td>
<td class="cellrowborder" valign="top" width="11.401140114011401%" headers="mcps1.2.4.1.2 "><p id="zh-cn_topic_0000002216005989_p723015144436"><a name="zh-cn_topic_0000002216005989_p723015144436"></a><a name="zh-cn_topic_0000002216005989_p723015144436"></a>输入</p>
</td>
<td class="cellrowborder" valign="top" width="71.71717171717171%" headers="mcps1.2.4.1.3 "><p id="zh-cn_topic_0000002216005989_p3243153110413"><a name="zh-cn_topic_0000002216005989_p3243153110413"></a><a name="zh-cn_topic_0000002216005989_p3243153110413"></a>为globalDomain或<a href="#mstxDomainCreateA">mstxDomainCreateA</a>返回的句柄。</p>
<p id="zh-cn_topic_0000002216005989_p17135131418533"><a name="zh-cn_topic_0000002216005989_p17135131418533"></a><a name="zh-cn_topic_0000002216005989_p17135131418533"></a>数据类型：const char *。</p>
</td>
</tr>
<tr id="zh-cn_topic_0000002216005989_row18118485118"><td class="cellrowborder" valign="top" width="16.881688168816883%" headers="mcps1.2.4.1.1 "><p id="zh-cn_topic_0000002216005989_p211549516"><a name="zh-cn_topic_0000002216005989_p211549516"></a><a name="zh-cn_topic_0000002216005989_p211549516"></a>desc</p>
</td>
<td class="cellrowborder" valign="top" width="11.401140114011401%" headers="mcps1.2.4.1.2 "><p id="zh-cn_topic_0000002216005989_p1920117129516"><a name="zh-cn_topic_0000002216005989_p1920117129516"></a><a name="zh-cn_topic_0000002216005989_p1920117129516"></a>输入</p>
</td>
<td class="cellrowborder" valign="top" width="71.71717171717171%" headers="mcps1.2.4.1.3 "><pre class="screen" id="zh-cn_topic_0000002216005989_screen47021458121411"><a name="zh-cn_topic_0000002216005989_screen47021458121411"></a><a name="zh-cn_topic_0000002216005989_screen47021458121411"></a>typedef enum mstxMemHeapUsageType {
    /* @brief 此堆内存作为内存池使用
     * 使用此使用方式注册的堆内存，需要使用二次分配注册后才可以访问
     */
    MSTX_MEM_HEAP_USAGE_TYPE_SUB_ALLOCATOR = 0,
} mstxMemHeapUsageType;

/** @brief 堆内存的类型
 * 此处的“类型”是指通过何种方式来描述堆内存指针。当前仅支持线性排布的
 * 内存，但此处保留日后支持更多内存类型的扩展能力。比如某些API返回
 * 多个句柄来描述内存范围，或者一些高维内存需要使用stride、tiling或
 * interlace来描述
 */
typedef enum mstxMemType {
    /** @brief 标准线性排布的虚拟内存
      * 此时mstxMemHeapRegister接收mstxMemVirtualRangeDesc_t类型的描述
      */
    MSTX_MEM_TYPE_VIRTUAL_ADDRESS = 0,
} mstxMemType;

typedef struct mstxMemVirtualRangeDesc_t {
    uint32_t deviceId;  // 内存区域对应的设备 ID
    void const *ptr;  // 内存区域的起始地址
    uint64_t size;  // 内存区域的长度
} mstxMemVirtualRangeDesc_t;

typedef struct mstxMemHeapDesc_t {
    mstxMemHeapUsageType usage;  // 堆内存的使用方式
    mstxMemType type;  // 堆内存的类型
    void const *typeSpecificDesc;  // 堆内存在指定内存类型下的描述信息
} mstxMemHeapDesc_t;</pre>
</td>
</tr>
</tbody>
</table>


**返回值说明<a id="zh-cn_topic_0000002216005989_section16621124213476"></a>**

内存池对应的句柄。

**调用示例<a id="zh-cn_topic_0000002216005989_section377820328555"></a>**

```c
mstxMemVirtualRangeDesc_t rangeDesc = {};
    rangeDesc.deviceId = deviceId;       // 设备编号
    rangeDesc.ptr = gm;                  // 注册的内存池gm首地址
    rangeDesc.size = 1024;               // 内存池大小
    heapDesc.typeSpecificDesc = &rangeDesc;
    mstxMemHeapDesc_t heapDesc{};
    mstxMemHeapHandle_t memPool = mstxMemHeapRegister(globalDomain, &heapDesc); // 注册内存池  
```

## mstxMemRegionsRegister<a id="mstxMemRegionsRegister"></a>

**产品支持情况<a id="section8178181118225"></a>**

|产品|是否支持|
|--|:-:|
|昇腾910_95 AI处理器|√|
|Atlas A3 训练系列产品/Atlas A3 推理系列产品|√|
|Atlas A2 训练系列产品/Atlas A2 推理系列产品|√|
|Atlas 200I/500 A2 推理产品|√|
|Atlas 推理系列产品|√|
|Atlas 训练系列产品|√|


**功能说明<a id="zh-cn_topic_0000002180759810_section20806203412478"></a>**

注册内存池二次分配。用户需保证RegionsRegister的内存位于[mstxMemHeapRegister](#mstxMemHeapRegister)注册的范围内，否则工具会提示越界读写。

**函数原型<a id="zh-cn_topic_0000002180759810_section1121883194711"></a>**

```
void mstxMemRegionsRegister(mstxDomainHandle_t domain, mstxMemRegionsRegisterBatch_t const *desc)
```

**参数说明<a id="zh-cn_topic_0000002180759810_section11506138144714"></a>**

**表 1**  参数说明

<a name="zh-cn_topic_0000002180759810_table827101275518"></a>
<table><thead align="left"><tr id="zh-cn_topic_0000002180759810_row429121265517"><th class="cellrowborder" valign="top" width="28.65286528652865%" id="mcps1.2.4.1.1"><p id="zh-cn_topic_0000002180759810_p1329121214558"><a name="zh-cn_topic_0000002180759810_p1329121214558"></a><a name="zh-cn_topic_0000002180759810_p1329121214558"></a>参数</p>
</th>
<th class="cellrowborder" valign="top" width="26.7026702670267%" id="mcps1.2.4.1.2"><p id="zh-cn_topic_0000002180759810_p10230141454318"><a name="zh-cn_topic_0000002180759810_p10230141454318"></a><a name="zh-cn_topic_0000002180759810_p10230141454318"></a>输入/输出</p>
</th>
<th class="cellrowborder" valign="top" width="44.64446444644465%" id="mcps1.2.4.1.3"><p id="zh-cn_topic_0000002180759810_p83121275519"><a name="zh-cn_topic_0000002180759810_p83121275519"></a><a name="zh-cn_topic_0000002180759810_p83121275519"></a>说明</p>
</th>
</tr>
</thead>
<tbody><tr id="zh-cn_topic_0000002180759810_row1131131265511"><td class="cellrowborder" valign="top" width="28.65286528652865%" headers="mcps1.2.4.1.1 "><p id="zh-cn_topic_0000002180759810_p7669321185110"><a name="zh-cn_topic_0000002180759810_p7669321185110"></a><a name="zh-cn_topic_0000002180759810_p7669321185110"></a>domain</p>
</td>
<td class="cellrowborder" valign="top" width="26.7026702670267%" headers="mcps1.2.4.1.2 "><p id="zh-cn_topic_0000002180759810_p723015144436"><a name="zh-cn_topic_0000002180759810_p723015144436"></a><a name="zh-cn_topic_0000002180759810_p723015144436"></a>输入</p>
</td>
<td class="cellrowborder" valign="top" width="44.64446444644465%" headers="mcps1.2.4.1.3 "><p id="zh-cn_topic_0000002180759810_p3243153110413"><a name="zh-cn_topic_0000002180759810_p3243153110413"></a><a name="zh-cn_topic_0000002180759810_p3243153110413"></a>为globalDomain或<a href="#mstxDomainCreateA">mstxDomainCreateA</a>返回的句柄。</p>
<p id="zh-cn_topic_0000002180759810_p17135131418533"><a name="zh-cn_topic_0000002180759810_p17135131418533"></a><a name="zh-cn_topic_0000002180759810_p17135131418533"></a>数据类型：const char *。</p>
</td>
</tr>
<tr id="zh-cn_topic_0000002180759810_row18118485118"><td class="cellrowborder" valign="top" width="28.65286528652865%" headers="mcps1.2.4.1.1 "><p id="zh-cn_topic_0000002180759810_p211549516"><a name="zh-cn_topic_0000002180759810_p211549516"></a><a name="zh-cn_topic_0000002180759810_p211549516"></a>desc</p>
</td>
<td class="cellrowborder" valign="top" width="26.7026702670267%" headers="mcps1.2.4.1.2 "><p id="zh-cn_topic_0000002180759810_p1920117129516"><a name="zh-cn_topic_0000002180759810_p1920117129516"></a><a name="zh-cn_topic_0000002180759810_p1920117129516"></a>输入</p>
</td>
<td class="cellrowborder" valign="top" width="44.64446444644465%" headers="mcps1.2.4.1.3 "><p id="zh-cn_topic_0000002180759810_p14824161520710"><a name="zh-cn_topic_0000002180759810_p14824161520710"></a><a name="zh-cn_topic_0000002180759810_p14824161520710"></a>内存池待二次分配的内存区域描述信息，不能为空。</p>
<pre class="screen" id="zh-cn_topic_0000002180759810_screen19859174319117"><a name="zh-cn_topic_0000002180759810_screen19859174319117"></a><a name="zh-cn_topic_0000002180759810_screen19859174319117"></a>struct mstxMemRegion_st;
typedef struct mstxMemRegion_st mstxMemRegion_t;
typedef mstxMemRegion_t* mstxMemRegionHandle_t;

typedef struct mstxMemRegionsRegisterBatch_t {
    mstxMemHeapHandle_t heap;  // 要进行二次分配的内存池句柄
    mstxMemType regionType;  // 内存区域的内存类型
    size_t regionCount;  // 内存区域的个数
    void const *regionDescArray;  // 内存区域描述数据
    mstxMemRegionHandle_t* regionHandleArrayOut;  // 返回的注册二次分配得到的句柄数组
} mstxMemRegionsRegisterBatch_t;</pre>
</td>
</tr>
</tbody>
</table>


**返回值说明<a id="zh-cn_topic_0000002180759810_section16621124213476"></a>**

无

**调用示例<a id="zh-cn_topic_0000002180759810_section377820328555"></a>**

```
mstxMemRegionsRegisterBatch_t regionsDesc{};
regionsDesc.heap = memPool;
regionsDesc.regionType = MSTX_MEM_TYPE_VIRTUAL_ADDRESS;
regionsDesc.regionCount = 1;
regionsDesc.regionDescArray = rangesDesc;
regionsDesc.regionHandleArrayOut = regionHandles;
mstxMemRegionsRegister(globalDomain, ®ionsDesc);              // 二次分配注册 
```

## mstxMemRegionsUnregister<a id="mstxMemRegionsUnregister"></a>

**产品支持情况<a id="section8178181118225"></a>**

|产品|是否支持|
|--|:-:|
|昇腾910_95 AI处理器|√|
|Atlas A3 训练系列产品/Atlas A3 推理系列产品|√|
|Atlas A2 训练系列产品/Atlas A2 推理系列产品|√|
|Atlas 200I/500 A2 推理产品|√|
|Atlas 推理系列产品|√|
|Atlas 训练系列产品|√|


**功能说明<a id="zh-cn_topic_0000002180600118_section20806203412478"></a>**

注销内存池二次分配。

**函数原型<a id="zh-cn_topic_0000002180600118_section1121883194711"></a>**

```
void mstxMemRegionsUnregister(mstxDomainHandle_t domain, mstxMemRegionsUnregisterBatch_t const *desc)
```

**参数说明<a id="zh-cn_topic_0000002180600118_section11506138144714"></a>**

**表 1**  参数说明

<a name="zh-cn_topic_0000002180600118_table827101275518"></a>
<table><thead align="left"><tr id="zh-cn_topic_0000002180600118_row429121265517"><th class="cellrowborder" valign="top" width="28.652865286528655%" id="mcps1.2.4.1.1"><p id="zh-cn_topic_0000002180600118_p1329121214558"><a name="zh-cn_topic_0000002180600118_p1329121214558"></a><a name="zh-cn_topic_0000002180600118_p1329121214558"></a>参数</p>
</th>
<th class="cellrowborder" valign="top" width="21.002100210021005%" id="mcps1.2.4.1.2"><p id="zh-cn_topic_0000002180600118_p10230141454318"><a name="zh-cn_topic_0000002180600118_p10230141454318"></a><a name="zh-cn_topic_0000002180600118_p10230141454318"></a>输入/输出</p>
</th>
<th class="cellrowborder" valign="top" width="50.34503450345035%" id="mcps1.2.4.1.3"><p id="zh-cn_topic_0000002180600118_p83121275519"><a name="zh-cn_topic_0000002180600118_p83121275519"></a><a name="zh-cn_topic_0000002180600118_p83121275519"></a>说明</p>
</th>
</tr>
</thead>
<tbody><tr id="zh-cn_topic_0000002180600118_row1131131265511"><td class="cellrowborder" valign="top" width="28.652865286528655%" headers="mcps1.2.4.1.1 "><p id="zh-cn_topic_0000002180600118_p7669321185110"><a name="zh-cn_topic_0000002180600118_p7669321185110"></a><a name="zh-cn_topic_0000002180600118_p7669321185110"></a>domain</p>
</td>
<td class="cellrowborder" valign="top" width="21.002100210021005%" headers="mcps1.2.4.1.2 "><p id="zh-cn_topic_0000002180600118_p723015144436"><a name="zh-cn_topic_0000002180600118_p723015144436"></a><a name="zh-cn_topic_0000002180600118_p723015144436"></a>输入</p>
</td>
<td class="cellrowborder" valign="top" width="50.34503450345035%" headers="mcps1.2.4.1.3 "><p id="zh-cn_topic_0000002180600118_p3243153110413"><a name="zh-cn_topic_0000002180600118_p3243153110413"></a><a name="zh-cn_topic_0000002180600118_p3243153110413"></a>为globalDomain或<a href="#mstxDomainCreateA">mstxDomainCreateA</a>返回的句柄。</p>
<p id="zh-cn_topic_0000002180600118_p17135131418533"><a name="zh-cn_topic_0000002180600118_p17135131418533"></a><a name="zh-cn_topic_0000002180600118_p17135131418533"></a>数据类型：const char *。</p>
</td>
</tr>
<tr id="zh-cn_topic_0000002180600118_row18118485118"><td class="cellrowborder" valign="top" width="28.652865286528655%" headers="mcps1.2.4.1.1 "><p id="zh-cn_topic_0000002180600118_p211549516"><a name="zh-cn_topic_0000002180600118_p211549516"></a><a name="zh-cn_topic_0000002180600118_p211549516"></a>desc</p>
</td>
<td class="cellrowborder" valign="top" width="21.002100210021005%" headers="mcps1.2.4.1.2 "><p id="zh-cn_topic_0000002180600118_p1920117129516"><a name="zh-cn_topic_0000002180600118_p1920117129516"></a><a name="zh-cn_topic_0000002180600118_p1920117129516"></a>输入</p>
</td>
<td class="cellrowborder" valign="top" width="50.34503450345035%" headers="mcps1.2.4.1.3 "><p id="zh-cn_topic_0000002180600118_p14824161520710"><a name="zh-cn_topic_0000002180600118_p14824161520710"></a><a name="zh-cn_topic_0000002180600118_p14824161520710"></a>输入的描述信息必须是某一次<a href="#mstxMemHeapRegister">mstxMemHeapRegister</a>的输入描述信息，否则工具将打印提示错误。</p>
<pre class="screen" id="zh-cn_topic_0000002180600118_screen1854493213265"><a name="zh-cn_topic_0000002180600118_screen1854493213265"></a><a name="zh-cn_topic_0000002180600118_screen1854493213265"></a>typedef enum mstxMemRegionRefType {
    // 通过指针描述内存引用
    MSTX_MEM_REGION_REF_TYPE_POINTER = 0,
    // 通过句柄描述内存引用
    MSTX_MEM_REGION_REF_TYPE_HANDLE
} mstxMemRegionRefType;

typedef struct mstxMemRegionRef_t {
    mstxMemRegionRefType refType; // 描述内存引用的方式
    union {
        void const* pointer;  // 当前内存引用通过指针描述时，此处保存内存区域指针
        mstxMemRegionHandle_t handle;  // 当内存引用通过句柄描述时，此处保存内存区域的句柄 
    };
} mstxMemRegionRef_t;

typedef struct mstxMemRegionsUnregisterBatch_t {
    size_t refCount;  // 内存引用的个数
    mstxMemRegionRef_t const *refArray;  // 要注销的内存区域引用
} mstxMemRegionsUnregisterBatch_t;</pre>
</td>
</tr>
</tbody>
</table>


**返回值说明<a id="zh-cn_topic_0000002180600118_section16621124213476"></a>**

无

**调用示例<a id="zh-cn_topic_0000002180600118_section377820328555"></a>**

```
mstxMemRegionsUnregisterBatch_t refsDesc = {}
refsDesc.refCount = 1;
refsDesc.refArray = regionRef;
mstxMemRegionsUnregister(globalDomain, &refsDesc);                   // 注销二次分配
```

## mstxMemHeapUnregister<a id="mstxMemHeapUnregister"></a>

**产品支持情况<a id="section8178181118225"></a>**

|产品|是否支持|
|--|:-:|
|昇腾910_95 AI处理器|√|
|Atlas A3 训练系列产品/Atlas A3 推理系列产品|√|
|Atlas A2 训练系列产品/Atlas A2 推理系列产品|√|
|Atlas 200I/500 A2 推理产品|√|
|Atlas 推理系列产品|√|
|Atlas 训练系列产品|√|


**功能说明<a id="zh-cn_topic_0000002215920417_section20806203412478"></a>**

注销内存池时，与之关联的Regions将一并被注销。

**函数原型<a id="zh-cn_topic_0000002215920417_section1121883194711"></a>**

```
void mstxMemHeapUnregister(mstxDomainHandle_t domain, mstxMemHeapHandle_t heap)
```

**参数说明<a id="zh-cn_topic_0000002215920417_section11506138144714"></a>**

**表 1**  参数说明


<a name="zh-cn_topic_0000002215920417_table827101275518"></a>
<table><thead align="left"><tr id="zh-cn_topic_0000002215920417_row429121265517"><th class="cellrowborder" valign="top" width="28.65286528652865%" id="mcps1.2.4.1.1"><p id="zh-cn_topic_0000002215920417_p1329121214558"><a name="zh-cn_topic_0000002215920417_p1329121214558"></a><a name="zh-cn_topic_0000002215920417_p1329121214558"></a>参数</p>
</th>
<th class="cellrowborder" valign="top" width="26.72267226722672%" id="mcps1.2.4.1.2"><p id="zh-cn_topic_0000002215920417_p10230141454318"><a name="zh-cn_topic_0000002215920417_p10230141454318"></a><a name="zh-cn_topic_0000002215920417_p10230141454318"></a>输入/输出</p>
</th>
<th class="cellrowborder" valign="top" width="44.62446244624462%" id="mcps1.2.4.1.3"><p id="zh-cn_topic_0000002215920417_p83121275519"><a name="zh-cn_topic_0000002215920417_p83121275519"></a><a name="zh-cn_topic_0000002215920417_p83121275519"></a>说明</p>
</th>
</tr>
</thead>
<tbody><tr id="zh-cn_topic_0000002215920417_row1131131265511"><td class="cellrowborder" valign="top" width="28.65286528652865%" headers="mcps1.2.4.1.1 "><p id="zh-cn_topic_0000002215920417_p7669321185110"><a name="zh-cn_topic_0000002215920417_p7669321185110"></a><a name="zh-cn_topic_0000002215920417_p7669321185110"></a>domain</p>
</td>
<td class="cellrowborder" valign="top" width="26.72267226722672%" headers="mcps1.2.4.1.2 "><p id="zh-cn_topic_0000002215920417_p723015144436"><a name="zh-cn_topic_0000002215920417_p723015144436"></a><a name="zh-cn_topic_0000002215920417_p723015144436"></a>输入</p>
</td>
<td class="cellrowborder" valign="top" width="44.62446244624462%" headers="mcps1.2.4.1.3 "><p id="zh-cn_topic_0000002215920417_p3243153110413"><a name="zh-cn_topic_0000002215920417_p3243153110413"></a><a name="zh-cn_topic_0000002215920417_p3243153110413"></a>domain为内存池所属的域，为globalDomain或<a href="#mstxDomainCreateA">mstxDomainCreateA</a>返回的句柄。</p>
<p id="zh-cn_topic_0000002215920417_p17135131418533"><a name="zh-cn_topic_0000002215920417_p17135131418533"></a><a name="zh-cn_topic_0000002215920417_p17135131418533"></a>数据类型：const char *。</p>
</td>
</tr>
<tr id="zh-cn_topic_0000002215920417_row18118485118"><td class="cellrowborder" valign="top" width="28.65286528652865%" headers="mcps1.2.4.1.1 "><p id="zh-cn_topic_0000002215920417_p17725843815"><a name="zh-cn_topic_0000002215920417_p17725843815"></a><a name="zh-cn_topic_0000002215920417_p17725843815"></a>heap</p>
</td>
<td class="cellrowborder" valign="top" width="26.72267226722672%" headers="mcps1.2.4.1.2 "><p id="zh-cn_topic_0000002215920417_p1920117129516"><a name="zh-cn_topic_0000002215920417_p1920117129516"></a><a name="zh-cn_topic_0000002215920417_p1920117129516"></a>输入</p>
</td>
<td class="cellrowborder" valign="top" width="44.62446244624462%" headers="mcps1.2.4.1.3 "><p id="zh-cn_topic_0000002215920417_p15419387397"><a name="zh-cn_topic_0000002215920417_p15419387397"></a><a name="zh-cn_topic_0000002215920417_p15419387397"></a>heap为需要注销内存池的句柄，为<a href="#mstxMemHeapRegister">mstxMemHeapRegister</a>的返回值。</p>
<pre class="screen" id="zh-cn_topic_0000002215920417_screen977616221627"><a name="zh-cn_topic_0000002215920417_screen977616221627"></a><a name="zh-cn_topic_0000002215920417_screen977616221627"></a>struct mstxMemHeap_st;
typedef struct mstxMemHeap_st mstxMemHeap_t; 
typedef mstxMemHeap_t* mstxMemHeapHandle_t;</pre>
</td>
</tr>
</tbody>
</table>


**返回值说明<a id="zh-cn_topic_0000002215920417_section16621124213476"></a>**

无

**调用示例<a id="zh-cn_topic_0000002215920417_section7800053122316"></a>**

```
mstxMemHeapDesc_t heapDesc{};
mstxMemHeapHandle_t memPool = mstxMemHeapRegister(globalDomain, &heapDesc); // 注册内存池
...
mstxMemHeapUnregister(globalDomain, memPool);                        // 注销内存池
```

