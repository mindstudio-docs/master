# mstxRangeStartA<a id="mstxRangeStartA"></a>

**Supported Products<a id="section8178181118225"></a>**

|Product|Supported|
|--|:-:|
|Ascend 910_95 AI Processors|√|
|Atlas A3 training products/Atlas A3 inference products|√|
|Atlas A2 training products/Atlas A2 inference products|√|
|Atlas 200I/500 A2 inference products|√|
|Atlas inference products|√|
|Atlas training products|√|

**Function<a id="zh-cn_topic_0000002016210401_section20806203412478"></a>**

Marks the start position of the mstx range capability.

**Prototype<a id="section1121883194711"></a>**

C/C++:

```c
mstxRangeId mstxRangeStartA(const char *message, aclrtStream stream)
```

Python:

```py
mstx.range_start(message, stream)
```

**Parameter Description<a id="zh-cn_topic_0000002016210401_section11506138144714"></a>**

**Table 1** Parameter description

|Parameter|Input/Output|Description|
|--|--|--|
|message|Input|message is a text marker that carries trace information.<br>Data type in C/C++: const char *.<br>In Python, message is a string. Defaults to None.<br>Length requirement for the input message string: MSPTI scenario: cannot exceed 255 bytes.<br>Non-MSPTI scenario (for example, msprof command line, Ascend PyTorch Profiler): cannot exceed 156 bytes.<br>message cannot be a null pointer.|
|stream|Input|stream indicates the thread that uses the mark.<br>Data type in C/C++: aclrtStream.<br>In Python, stream is an aclrtStream object. Defaults to None.<br>When set to nullptr, only the instantaneous event on the Host side is marked.<br>When set to a valid stream, the instantaneous events on the Host side and the corresponding Device side are marked.|

**Returns<a id="zh-cn_topic_0000002016210401_section16621124213476"></a>**

If 0 is returned, it indicates failure.

**Example<a id="zh-cn_topic_0000002016210401_section377820328555"></a>**

- C/C++ Calling Method:<a id="c-calling-method"></a>

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

- **Python** Calling Method 1:<a id="python-calling-method"></a>

    Through the Python API interface, implement the relevant interface content in C/C++ language and compile it to generate an so file. The relevant so file can be directly referenced by Python in PYTHONPATH.

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

- **Python** Calling Method 2:

    Directly use Python for development, reference the original mstx .so file via ctypes.CDLL("libms_tools_ext.so"), and use the APIs provided within it.

    ```py
    import mstx
    import torch
    import torch_npu
    import acl
    import sys
    import ctypes
    lib = ctypes.CDLL("libms_tools_ext.so")
    # Define the parameter types and return type of the function
    lib.mstxRangeStartA.argtypes = [ctypes.c_char_p, ctypes.c_void_p]
    lib.mstxRangeStartA.restype = ctypes.c_uint64
    lib.mstxRangeEnd.argtypes = [ctypes.c_uint64]
    lib.mstxRangeEnd.restype = None
    a = torch.Tensor([1,2,3,4]).npu()
    b = torch.Tensor([1,2,3,4]).npu()
    # Create a ctypes.c_char_p pointer
    hi_str = b"hi"
    hi_ptr = ctypes.c_char_p(hi_str)
    hi_id = ctypes.c_uint64()
    # Create a ctypes.c_char_p pointer
    hello_str = b"hello"
    hello_ptr = ctypes.c_char_p(hello_str)
    hello_id = ctypes.c_uint64()
    # Call the function
    hi_id.value = lib.mstxRangeStartA(hi_ptr, None)
    c = a + b
    hello_id.value = lib.mstxRangeStartA(hello_ptr, None)
    d = a - b
    lib.mstxRangeEnd(hi_id)
    e = a * b
    lib.mstxRangeEnd(hello_id)
    ```
