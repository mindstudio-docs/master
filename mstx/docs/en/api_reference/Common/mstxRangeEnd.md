# `mstxRangeEnd`<a id="mstxRangeEnd"></a>

**Supported Products<a id="section8178181118225"></a>**

<!-- npu="950" id1 -->
- Ascend 950PR and 950DT products: supported
<!-- end id1 -->
<!-- npu="A3" id2 -->
- Atlas A3 products: supported
<!-- end id2 -->
<!-- npu="910b" id3 -->
- Atlas A2 products: supported
<!-- end id3 -->
<!-- npu="310b" id4 -->
- Atlas 200I/500 A2 inference products: supported
<!-- end id4 -->
<!-- npu="310p" id5 -->
- Atlas inference products: supported
<!-- end id5 -->
<!-- npu="910" id6 -->
- Atlas training products: supported
<!-- end id6 -->

**Function<a id="zh-cn_topic_0000001979850148_section20806203412478"></a>**

Marks the end position of the mstx range capability.

**Prototype<a id="zh-cn_topic_0000001979850148_section1121883194711"></a>**

C/C++ function prototype:

```c
void mstxRangeEnd(mstxRangeId id)
```

Python function:

```py
mstx.range_end(range_id)
```

**Parameter Description<a id="zh-cn_topic_0000001979850148_section11506138144714"></a>**

**Table 1**  Parameter description

| Parameter | Input/Output | Description |
|--|--|--|
| id (C/C++) | Input | ID returned by mstxRangeStartA (C/C++). |
| range_id (Python) | Input | range_id returned by mstx.range_start (Python). |

**Returns<a id="zh-cn_topic_0000001979850148_section16621124213476"></a>**

If 0 is returned, it indicates failure.

**Example<a id="zh-cn_topic_0000001979850148_section377820328555"></a>**

C/C++ call: The mstxRangeEnd API must be used together with mstxRangeStartA. For details, see [C/C++ Calling Method](mstxRangeStartA.md#c-calling-method).

Python call: The mstx.range_end API must be used together with mstx.range_start. For a specific example, see [Python Calling Method](mstxRangeStartA.md#python-calling-method).
