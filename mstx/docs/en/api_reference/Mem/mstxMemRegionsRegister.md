# mstxMemRegionsRegister<a id="mstxMemRegionsRegister"></a>

**Supported Products<a id="section8178181118225"></a>**

|Product|Supported|
|--|:-:|
|Ascend 910_95 AI Processors|√|
|Atlas A3 training products/Atlas A3 inference products|√|
|Atlas A2 training products/Atlas A2 inference products|√|
|Atlas 200I/500 A2 inference products|√|
|Atlas inference products|√|
|Atlas training products|√|

**Function<a id="zh-cn_topic_0000002180759810_section20806203412478"></a>**

Registers memory pool secondary allocation. The user must ensure that the memory registered by RegionsRegister is within the range registered by [mstxMemHeapRegister](mstxMemHeapRegister.md); otherwise, the tool will report an out-of-bounds read/write.

**Prototype<a id="zh-cn_topic_0000002180759810_section1121883194711"></a>**

```c
void mstxMemRegionsRegister(mstxDomainHandle_t domain, mstxMemRegionsRegisterBatch_t const *desc)
```

**Parameter Description<a id="zh-cn_topic_0000002180759810_section11506138144714"></a>**

**Table 1** Parameter description

<a name="zh-cn_topic_0000002180759810_table827101275518"></a>
<table><thead align="left"><tr id="zh-cn_topic_0000002180759810_row429121265517"><th class="cellrowborder" valign="top" width="28.65286528652865%" id="mcps1.2.4.1.1"><p id="zh-cn_topic_0000002180759810_p1329121214558"><a name="zh-cn_topic_0000002180759810_p1329121214558"></a><a name="zh-cn_topic_0000002180759810_p1329121214558"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="26.7026702670267%" id="mcps1.2.4.1.2"><p id="zh-cn_topic_0000002180759810_p10230141454318"><a name="zh-cn_topic_0000002180759810_p10230141454318"></a><a name="zh-cn_topic_0000002180759810_p10230141454318"></a>Input/Output</p>
</th>
<th class="cellrowborder" valign="top" width="44.64446444644465%" id="mcps1.2.4.1.3"><p id="zh-cn_topic_0000002180759810_p83121275519"><a name="zh-cn_topic_0000002180759810_p83121275519"></a><a name="zh-cn_topic_0000002180759810_p83121275519"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="zh-cn_topic_0000002180759810_row1131131265511"><td class="cellrowborder" valign="top" width="28.65286528652865%" headers="mcps1.2.4.1.1 "><p id="zh-cn_topic_0000002180759810_p7669321185110"><a name="zh-cn_topic_0000002180759810_p7669321185110"></a><a name="zh-cn_topic_0000002180759810_p7669321185110"></a>domain</p>
</td>
<td class="cellrowborder" valign="top" width="26.7026702670267%" headers="mcps1.2.4.1.2 "><p id="zh-cn_topic_0000002180759810_p723015144436"><a name="zh-cn_topic_0000002180759810_p723015144436"></a><a name="zh-cn_topic_0000002180759810_p723015144436"></a>Input</p>
</td>
<td class="cellrowborder" valign="top" width="44.64446444644465%" headers="mcps1.2.4.1.3 "><p id="zh-cn_topic_0000002180759810_p3243153110413"><a name="zh-cn_topic_0000002180759810_p3243153110413"></a><a name="zh-cn_topic_0000002180759810_p3243153110413"></a>Either globalDomain or the handle returned by <a href="../Common/mstxDomainCreateA.md">mstxDomainCreateA</a>.</p>
<p id="zh-cn_topic_0000002180759810_p17135131418533"><a name="zh-cn_topic_0000002180759810_p17135131418533"></a><a name="zh-cn_topic_0000002180759810_p17135131418533"></a>Data type: const char *.</p>
</td>
</tr>
<tr id="zh-cn_topic_0000002180759810_row18118485118"><td class="cellrowborder" valign="top" width="28.65286528652865%" headers="mcps1.2.4.1.1 "><p id="zh-cn_topic_0000002180759810_p211549516"><a name="zh-cn_topic_0000002180759810_p211549516"></a><a name="zh-cn_topic_0000002180759810_p211549516"></a>desc</p>
</td>
<td class="cellrowborder" valign="top" width="26.7026702670267%" headers="mcps1.2.4.1.2 "><p id="zh-cn_topic_0000002180759810_p1920117129516"><a name="zh-cn_topic_0000002180759810_p1920117129516"></a><a name="zh-cn_topic_0000002180759810_p1920117129516"></a>Input</p>
</td>
<td class="cellrowborder" valign="top" width="44.64446444644465%" headers="mcps1.2.4.1.3 "><p id="zh-cn_topic_0000002180759810_p14824161520710"><a name="zh-cn_topic_0000002180759810_p14824161520710"></a><a name="zh-cn_topic_0000002180759810_p14824161520710"></a>Description information of the memory region to be sub-allocated from the memory pool. Cannot be null.</p>

<pre class="screen" id="zh-cn_topic_0000002180759810_screen19859174319117"><a name="zh-cn_topic_0000002180759810_screen19859174319117"></a><a name="zh-cn_topic_0000002180759810_screen19859174319117"></a>struct mstxMemRegion_st;
typedef struct mstxMemRegion_st mstxMemRegion_t;
typedef mstxMemRegion_t* mstxMemRegionHandle_t;

typedef struct mstxMemRegionsRegisterBatch_t {
    mstxMemHeapHandle_t heap;  // Handle of the memory pool for sub-allocation
    mstxMemType regionType;  // Memory type of the memory region
    size_t regionCount;  // Number of memory regions
    void const *regionDescArray;  // Memory region description data
    mstxMemRegionHandle_t* regionHandleArrayOut;  // Returned handle array obtained from registering sub-allocation
} mstxMemRegionsRegisterBatch_t;</pre>
</td>
</tr>
</tbody>
</table>

**Return Value Description<a id="zh-cn_topic_0000002180759810_section16621124213476"></a>**

None

**Example<a id="zh-cn_topic_0000002180759810_section377820328555"></a>**

```shell
mstxMemRegionsRegisterBatch_t regionsDesc{};
regionsDesc.heap = memPool;
regionsDesc.regionType = MSTX_MEM_TYPE_VIRTUAL_ADDRESS;
regionsDesc.regionCount = 1;
regionsDesc.regionDescArray = rangesDesc;
regionsDesc.regionHandleArrayOut = regionHandles;
mstxMemRegionsRegister(globalDomain, regionsDesc);              // Secondary allocation registrationry Allocation Registration
```
