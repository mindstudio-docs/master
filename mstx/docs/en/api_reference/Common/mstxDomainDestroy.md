# mstxDomainDestroy<a id="mstxDomainDestroy"></a>

**Supported Products<a id="section8178181118225"></a>**

|Product|Supported|
|--|:-:|
|Ascend 950 products|√|
|Atlas A3 training products/Atlas A3 inference products|√|
|Atlas A2 training products/Atlas A2 inference products|√|
|Atlas 200I/500 A2 inference products|√|
|Atlas inference products|√|
|Atlas training products|√|

**Function<a id="section20806203412478"></a>**

Destroys the specified domain. The destroyed domain cannot be used again and must be recreated.

**Prototype<a id="section1121883194711"></a>**

```c
void mstxDomainDestroy (mstxDomainHandle_t domain)
```

**Parameter Description<a id="section11506138144714"></a>**

**Table 1** Parameter description

|Parameter|Input/Output|Description|
|--|--|--|
|domain|Input|Specifies the domain handle to destroy.|

**Returns<a id="section16621124213476"></a>**

None
