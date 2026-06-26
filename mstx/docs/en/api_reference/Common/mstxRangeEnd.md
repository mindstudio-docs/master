# mstxRangeEnd<a id="mstxRangeEnd"></a>

**Supported Products<a id="section8178181118225"></a>**

|Product|Supported|
|--|:-:|
|Ascend 910_95 AI Processors|√|
|Atlas A3 training products/Atlas A3 inference products|√|
|Atlas A2 training products/Atlas A2 inference products|√|
|Atlas 200I/500 A2 inference products|√|
|Atlas inference products|√|
|Atlas training products|√|

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
