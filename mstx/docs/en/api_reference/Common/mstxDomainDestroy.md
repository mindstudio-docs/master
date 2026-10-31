# `mstxDomainDestroy`<a id="mstxDomainDestroy"></a>

**Supported Products<a id="section8178181118225"></a>**

<!-- npu="950" id1 -->
- Ascend 950PR and 950DT products: supported
<!-- end id1 -->
<!-- npu="A3" id2 -->
- Atlas A3 products: supported
<!-- end id2 -->
<!-- npu="910b" id3 -->
- Atlas A2 products: supported
<!-- end id3 -->
<!-- npu="310b" id4 -->
- Atlas 200I/500 A2 inference products: supported
<!-- end id4 -->
<!-- npu="310p" id5 -->
- Atlas inference products: supported
<!-- end id5 -->
<!-- npu="910" id6 -->
- Atlas training products: supported
<!-- end id6 -->

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
