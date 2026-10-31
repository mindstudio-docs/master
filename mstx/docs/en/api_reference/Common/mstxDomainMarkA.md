# `mstxDomainMarkA`<a id="mstxDomainMarkA"></a>

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
|message|Input|Pointer to the message string carried by the instrumentation. Length requirements for the passed message string: MSPTI scenario: cannot exceed 255 bytes.|
|stream|Input|Stream used to execute the instrumentation task. When set to nullptr, only the instantaneous event on the Host side is marked. When set to a valid stream, the instantaneous events on both the Host side and the corresponding Device side are marked.|

**Returns<a id="section16621124213476"></a>**

None
