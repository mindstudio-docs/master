# mstxRangeEnd<a id="mstxRangeEnd"></a>

**产品支持情况<a id="section8178181118225"></a>**

|产品|是否支持|
|--|:-:|
|Atlas 350 加速卡|√|
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

C/C++调用：mstxRangeEnd接口需要与mstxRangeStartA配合使用，具体示例请参考[C/C++调用方法](mstxRangeStartA.md#c调用方法)。

Python调用：mstx.range_end接口需要与mstx.range_start配合使用，具体示例请参考[Python调用方法](mstxRangeStartA.md#python调用方法)。
