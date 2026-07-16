# mstxDomainRangeStartA<a id="mstxDomainRangeStartA"></a>

**产品支持情况<a id="section8178181118225"></a>**

|产品|是否支持|
|--|:-:|
|Ascend 950 系列产品|√|
|Atlas A3 训练系列产品/Atlas A3 推理系列产品|√|
|Atlas A2 训练系列产品/Atlas A2 推理系列产品|√|
|Atlas 200I/500 A2 推理产品|√|
|Atlas 推理系列产品|√|
|Atlas 训练系列产品|√|

**功能说明<a id="section20806203412478"></a>**

在指定的domain内，标识时间段事件的开始。

如果传入的domain已被销毁，日志打印告警提示，接口不再执行打点流程。

**函数原型<a id="section1121883194711"></a>**

```c
mstxRangeId mstxDomainRangeStartA(mstxDomainHandle_t domain, const char *message, aclrtStream stream)
```

**参数说明<a id="section11506138144714"></a>**

**表 1**  参数说明

|参数名|输入/输出|说明|
|--|--|--|
|domain|输入|指定的domain句柄。|
|message|输入|打点携带信息字符串指针。<br>传入的message字符串长度要求：MSPTI场景：不能超过255字节。|
|stream|输入|用于执行打点任务的stream。配置为nullptr时，只标记Host侧的瞬时事件。配置为有效的stream时，标识Host侧和对应Device侧的瞬时事件。|

**返回值说明<a id="section16621124213476"></a>**

range_id：标识该range，如果打点失败或domain已销毁，则返回0。
