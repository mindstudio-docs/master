# mstxDomainRangeEnd<a id="mstxDomainRangeEnd"></a>

**产品支持情况<a id="section8178181118225"></a>**

|产品|是否支持|
|--|:-:|
|Atlas 350 加速卡|√|
|Atlas A3 训练系列产品/Atlas A3 推理系列产品|√|
|Atlas A2 训练系列产品/Atlas A2 推理系列产品|√|
|Atlas 200I/500 A2 推理产品|√|
|Atlas 推理系列产品|√|
|Atlas 训练系列产品|√|

**功能说明<a id="section20806203412478"></a>**

在指定的domain内，标识时间段事件的结束。

如果传入的domain已被销毁，日志打印告警提示，接口不再执行打点流程。

**函数原型<a id="section1121883194711"></a>**

```c
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
