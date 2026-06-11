# mstxDomainCreateA<a id="mstxDomainCreateA"></a>

**Product Support<a id="section8178181118225"></a>**

|Product|Supported|
|--|:-:|
|Ascend 910_95 AI Processors|√|
|Atlas A3 training products/Atlas A3 inference products|√|
|Atlas A2 training products/Atlas A2 inference products|√|
|Atlas 200I/500 A2 inference products|√|
|Atlas inference products|√|
|Atlas training products|√|

**Function<a id="section20806203412478"></a>**

Creates a custom mstx domain.

**Domain**: Used to partition trace data, allowing users to manage trace data in a customized manner. Trace data without a specified domain belongs to the default domain (domain name: default). By default, all trace data belongs to the default domain.

**Prototype<a id="section1121883194711"></a>**

```python
mstxDomainHandle_t mstxDomainCreateA(const char* id)
```

**Parameter Description<a id="section11506138144714"></a>**

**Table 1** Parameter description

|Parameter|Input/Output|Description|
|--|--|--|
|id|Input|Name of the domain to be created.<br>Data Type: const char *.<br>The default domain name is globalDomain.<br>The maximum length is 1,023 bytes. Only digits, uppercase and lowercase letters, and underscores (_) are supported.<br>MSPTI scenario: cannot exceed 255 bytes.<br>Non-MSPTI scenarios (such as the msprof command line and Ascend PyTorch Profiler): cannot exceed 1,024 bytes.|

**Returns<a id="section16621124213476"></a>**

Returns a valid domain handle, indicating that the API is executed successfully; returns nullptr, indicating that the API execution fails.

**Example<a id="zh-cn_topic_0000002180600114_section16621124213476"></a>**

```python
mstxDomainHandle_t domain = mstxDomainCreateA("sample")
```
