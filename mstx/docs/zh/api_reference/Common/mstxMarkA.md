# mstxMarkA<a id="mstxMarkA"></a>

**产品支持情况<a id="section8178181118225"></a>**

<!-- npu="950" id1 -->
- 昇腾950PR&950DT系列产品：支持
<!-- end id1 -->
<!-- npu="A3" id2 -->
- 昇腾A3系列产品：支持
<!-- end id2 -->
<!-- npu="910b" id3 -->
- 昇腾A2系列产品：支持
<!-- end id3 -->
<!-- npu="310b" id4 -->
- 昇腾310B系列产品：支持
<!-- end id4 -->
<!-- npu="310p" id5 -->
- 昇腾310P系列产品：支持
<!-- end id5 -->
<!-- npu="910" id6 -->
- 昇腾910系列产品：支持
<!-- end id6 -->

**功能说明<a id="section20806203412478"></a>**

标识瞬时事件。

**函数原型<a id="section1121883194711"></a>**

```c
void mstxMarkA(const char *message, aclrtStream stream)
```

**参数说明<a id="section11506138144714"></a>**

**表 1**  参数说明

|参数名|输入/输出|说明|
|--|--|--|
|message|输入|打点携带信息字符串指针。<br>传入的message字符串长度要求：MSPTI场景：不能超过255字节。<br>message不能传入空指针。|
|stream|输入|用于执行打点任务的stream。<br>配置为nullptr时，只标记Host侧的瞬时事件。<br>配置为有效的stream时，标识Host侧和对应Device侧的瞬时事件。|

**返回值说明<a id="section16621124213476"></a>**

无
