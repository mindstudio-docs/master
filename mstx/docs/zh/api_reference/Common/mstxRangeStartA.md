# mstxRangeStartA<a id="mstxRangeStartA"></a>

**产品支持情况<a id="section8178181118225"></a>**

|产品|是否支持|
|--|:-:|
|Ascend 950 系列产品|√|
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
|message|输入|message为标记的文字，携带打点信息。<br>C/C++中数据类型：const char *。<br>Python中，message为字符串。默认None。<br>传入的message字符串长度要求：MSPTI场景：不能超过255字节。<br>message不能传入空指针。|
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
    ERROR_LOG("Run op failed");
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
    mstx.range_start("aaa", None)
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
