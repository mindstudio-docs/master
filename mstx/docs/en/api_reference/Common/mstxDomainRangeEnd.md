# mstxDomainRangeEnd<a id="mstxDomainRangeEnd"></a>

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

Marks the end of a timestamp event within the specified domain.

If the passed domain has been destroyed, a warning is printed in the log, and the API no longer executes the instrumentation process.

**Prototype<a id="section1121883194711"></a>**

```c
void mstxDomainRangeEnd(mstxDomainHandle_t domain, mstxRangeId id)
```

**Parameter Description<a id="section11506138144714"></a>**

**Table 1** Parameter description

|Parameter|Input/Output|Description|
|--|--|--|
|domain|Input|Specified domain handle.|
|id|Input|ID returned by the mstxDomainRangeStartA API.|

**Returns<a id="section16621124213476"></a>**

None
