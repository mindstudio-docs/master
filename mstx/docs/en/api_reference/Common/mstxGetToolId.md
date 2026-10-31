# `mstxGetToolId`<a id="mstxGetToolId"></a>

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

**Function<a id="zh-cn_topic_0000002446914857_section20806203412478"></a>**

Obtains the tool ID that currently intercepts the mstx APIs. The tool ID macro is defined as follows:

Invalid value 0, indicating that no tool has launched the program.

```c
#define MSTX_TOOL_INVALID_ID 0x0
```  

0x1000, indicating that the program is launched by [msprof Model Tuning Tool](https://www.hiascend.com/document/detail/en/canncommercial/83RC1/devaids/Profiling/atlasprofiling_16_0010.html) or [msPTI](https://www.hiascend.com/document/detail/en/canncommercial/83RC1/devaids/Profiling/atlasprofiling_16_1153.html)

```c
#define MSTX_TOOL_MSPROF_ID 0x1000
```

0x1001, indicating that the program is launched by the [Operator Tuning (msProf)](https://www.hiascend.com/document/detail/en/canncommercial/83RC1/devaids/optool/atlasopdev_16_0082.html) tool

```c
#define MSTX_TOOL_MSOPPROF_ID 0x1001
```     

0x1002, indicating that the program is launched by the [Exception Detection (msSanitizer)](https://www.hiascend.com/document/detail/en/canncommercial/83RC1/devaids/optool/atlasopdev_16_0039.html) tool

```c
#define MSTX_TOOL_MSSANITIZER_ID 0x1002  
```

0x1003, indicating that the program is launched by the [msLeaks Memory Leak Detection Tool](https://www.hiascend.com/document/detail/en/canncommercial/83RC1/devaids/msleaks/atlas_msleaks_0001.html)

```c
#define MSTX_TOOL_MSLEAKS_ID 0x1003      
```

**Prototype<a id="zh-cn_topic_0000002446914857_section1121883194711"></a>**

```c
void mstxGetToolId(uint64 *id)
```

**Parameter Description<a id="zh-cn_topic_0000002446914857_section11506138144714"></a>**

**Table 1** Parameter description

|Parameter|Input/Output|Description|
|--|--|--|
|id|Output|As an output parameter, returns the tool ID that currently intercepts the mstx API.<br>Data Type: uint64 *.|

**Returns<a id="zh-cn_topic_0000002446914857_section446682320445"></a>**

None

**Example<a id="zh-cn_topic_0000002446914857_section16621124213476"></a>**

```py
uint64 id;
mstxGetToolId(&id);
```
