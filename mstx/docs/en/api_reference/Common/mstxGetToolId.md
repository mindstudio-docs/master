# mstxGetToolId<a id="mstxGetToolId"></a>

**Product Support<a id="section8178181118225"></a>**

|Product|Supported|
|--|:-:|
|Ascend 950 products|√|
|Atlas A3 training products/Atlas A3 inference products|√|
|Atlas A2 training products/Atlas A2 inference products|√|
|Atlas 200I/500 A2 inference products|√|
|Atlas inference products|√|
|Atlas training products|√|

**Function<a id="zh-cn_topic_0000002446914857_section20806203412478"></a>**

Obtains the tool ID that currently intercepts the mstx APIs. The tool ID macro is defined as follows:

Invalid value 0, indicating that no tool has launched the program.

```c
#define MSTX_TOOL_INVALID_ID 0x0
```

0x1000, indicating that the program is launched by [msProf](https://www.hiascend.com/document/detail/en/CANNCommunityEdition/910/devaids/Profiling/atlasprofiling_16_0010.html) or [MSPTI](https://www.hiascend.com/document/detail/en/CANNCommunityEdition/910/devaids/Profiling/atlasprofiling_16_0031.html)

```c
#define MSTX_TOOL_MSPROF_ID 0x1000
```

0x1001, indicating that the program is launched by the [msProf](https://gitcode.com/Ascend/msopprof/blob/26.1.0/docs/en/user_guide/msopprof_user_guide.md) tool

```c
#define MSTX_TOOL_MSOPPROF_ID 0x1001
```

0x1002, indicating that the program is launched by the [msSanitizer](https://gitcode.com/Ascend/mssanitizer/blob/26.1.0/docs/en/user_guide/mssanitizer_user_guide.md) tool

```c
#define MSTX_TOOL_MSSANITIZER_ID 0x1002
```

0x1003, indicating that the program is launched by the [msLeaks Memory Leak Detection Tool](https://gitcode.com/Ascend/msmemscope/blob/26.1.0/docs/en/quick_start/quick_start.md)

```c
#define MSTX_TOOL_MSLEAKS_ID 0x1003
```

**Prototype<a id="zh-cn_topic_0000002446914857_section1121883194711"></a>**

```c
void mstxGetToolId(uint64_t *id)
```

**Parameter Description<a id="zh-cn_topic_0000002446914857_section11506138144714"></a>**

**Table 1** Parameter description

|Parameter|Input/Output|Description|
|--|--|--|
|id|Output|As an output parameter, returns the tool ID that currently intercepts the mstx API.<br>Data Type: uint64 *.|

**Returns<a id="zh-cn_topic_0000002446914857_section446682320445"></a>**

None

**Example<a id="zh-cn_topic_0000002446914857_section16621124213476"></a>**

```c
uint64 id;
mstxGetToolId(&id);
```
