# mstxGetToolId<a id="mstxGetToolId"></a>

**产品支持情况<a id="section8178181118225"></a>**

|产品|是否支持|
|--|:-:|
|Ascend 950 系列产品|√|
|Atlas A3 训练系列产品/Atlas A3 推理系列产品|√|
|Atlas A2 训练系列产品/Atlas A2 推理系列产品|√|
|Atlas 200I/500 A2 推理产品|√|
|Atlas 推理系列产品|√|
|Atlas 训练系列产品|√|

**功能说明<a id="zh-cn_topic_0000002446914857_section20806203412478"></a>**

用于获取当前劫持mstx接口的工具ID，工具ID宏定义如下：

无效值0，表示无工具拉起程序

```c
#define MSTX_TOOL_INVALID_ID 0x0
```  

0x1000，表示程序由《[msprof模型调优工具](https://www.hiascend.com/document/detail/zh/canncommercial/83RC1/devaids/Profiling/atlasprofiling_16_0010.html)》或《[MSPTI](https://www.hiascend.com/document/detail/zh/canncommercial/83RC1/devaids/Profiling/atlasprofiling_16_1153.html)》工具拉起

```c
#define MSTX_TOOL_MSPROF_ID 0x1000
```

0x1001，表示程序由[算子调优（msProf）](https://www.hiascend.com/document/detail/zh/canncommercial/83RC1/devaids/optool/atlasopdev_16_0082.html)工具拉起

```c
#define MSTX_TOOL_MSOPPROF_ID 0x1001
```     

0x1002，表示程序由[异常检测（msSanitizer）](https://www.hiascend.com/document/detail/zh/canncommercial/83RC1/devaids/optool/atlasopdev_16_0039.html)工具拉起

```c
#define MSTX_TOOL_MSSANITIZER_ID 0x1002  
```

0x1003，表示程序由《[msLeaks内存泄漏检测工具](https://www.hiascend.com/document/detail/zh/canncommercial/83RC1/devaids/msleaks/atlas_msleaks_0001.html)》拉起

```c
#define MSTX_TOOL_MSLEAKS_ID 0x1003      
```

**函数原型<a id="zh-cn_topic_0000002446914857_section1121883194711"></a>**

```c
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

```c
uint64 id;
mstxGetToolId(&id);
```
