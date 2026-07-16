# mstxDomainDestroy<a id="mstxDomainDestroy"></a>

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

销毁指定的domain，销毁后的domain不能再次使用，需要重新创建。

**函数原型<a id="section1121883194711"></a>**

```c
void mstxDomainDestroy (mstxDomainHandle_t domain)
```

**参数说明<a id="section11506138144714"></a>**

**表 1**  参数说明

|参数名|输入/输出|说明|
|--|--|--|
|domain|输入|指定要销毁的domain句柄。|

**返回值说明<a id="section16621124213476"></a>**

无
