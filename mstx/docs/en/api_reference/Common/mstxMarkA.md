# mstxMarkA<a id="mstxMarkA"></a>

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

Marks an instantaneous event.

**Prototype<a id="section1121883194711"></a>**

```c
void mstxMarkA(const char *message, aclrtStream stream)
```

**Parameter Description<a id="section11506138144714"></a>**

**Table 1** Parameter description

|Parameter|Input/Output|Description|
|--|--|--|
|message|Input|Pointer to the string carrying information for the trace event.<br>Length requirement for the input message string: MSPTI scenario: cannot exceed 255 bytes.<br>Non-MSPTI scenario (for example, msprof command line, Ascend PyTorch Profiler): cannot exceed 156 bytes.<br>message cannot be a null pointer.|
|stream|Input|Stream used to execute the trace task.<br>When set to nullptr, only marks the instantaneous event on the Host side.<br>When set to a valid stream, marks the instantaneous event on both the Host side and the corresponding Device side.|

**Returns<a id="section16621124213476"></a>**

None
