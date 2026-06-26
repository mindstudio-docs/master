# mstxDomainCreateA<a id="mstxDomainCreateA"></a>

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

创建自定义的mstx域。

**domain（域）**：用于对打点数据进行划分，便于用户自定义管理打点数据，不指定domain的打点数据均属于默认域（域名：default）。默认情况下，所有打点数据均属于默认域。

**函数原型<a id="section1121883194711"></a>**

```python
mstxDomainHandle_t mstxDomainCreateA(const char* id)
```

**参数说明<a id="section11506138144714"></a>**

**表 1**  参数说明

|参数名|输入/输出|说明|
|--|--|--|
|id|输入|要创建的域的名称。<br>数据类型：const char *。<br>默认域名为globalDomain。<br>最大长度为1023字节，仅支持数字、大小写字母和_符号。<br>MSPTI场景：不能超过255字节。<br>非MSPTI场景（例如msprof命令行、Ascend PyTorch Profiler）：不能超过1024字节。|

**返回值说明<a id="section16621124213476"></a>**

返回有效的domain句柄，表示接口执行成功；返回nullptr，表示接口执行失败。

**调用示例<a id="zh-cn_topic_0000002180600114_section16621124213476"></a>**

```python
mstxDomainHandle_t domain = mstxDomainCreateA("sample")
```
