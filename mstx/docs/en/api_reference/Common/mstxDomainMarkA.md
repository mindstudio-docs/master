# mstxDomainMarkA<a id="mstxDomainMarkA"></a>

**Supported Products<a id="section8178181118225"></a>**

|Product|Supported|
|--|:-:|
|Ascend 910_95 AI Processors|√|
|Atlas A3 training products/Atlas A3 inference products|√|
|Atlas A2 training products/Atlas A2 inference products|√|
|Atlas 200I/500 A2 inference products|√|
|Atlas inference products|√|
|Atlas training products|√|

**Function<a id="section20806203412478"></a>**

Marks an instantaneous event within the specified domain.

If the passed domain has been destroyed, a warning is logged and the API no longer executes the instrumentation process.

**Prototype<a id="section1121883194711"></a>**

```c
void mstxDomainMarkA(mstxDomainHandle_t domain, const char *message, aclrtStream stream)
```

**Parameter Description<a id="section11506138144714"></a>**

**Table 1** Parameter description

|Parameter|Input/Output|Description|
|--|--|--|
|domain|Input|Handle of the specified domain.|
|message|Input|Pointer to the message string carried by the instrumentation. Length requirements for the passed message string: MSPTI scenario: cannot exceed 255 bytes. Non-MSPTI scenarios (for example, msprof command line, Ascend PyTorch Profiler): cannot exceed 156 bytes.|
|stream|Input|Stream used to execute the instrumentation task. When set to nullptr, only the instantaneous event on the Host side is marked. When set to a valid stream, the instantaneous events on both the Host side and the corresponding Device side are marked.|

**Returns<a id="section16621124213476"></a>**

None
