# mstxMemHeapRegister<a id="mstxMemHeapRegister"></a>

**Supported Products<a id="section8178181118225"></a>**

|Product|Supported|
|--|:-:|
|Ascend 910_95 AI Processors|√|
|Atlas A3 training products/Atlas A3 inference products|√|
|Atlas A2 training products/Atlas A2 inference products|√|
|Atlas 200I/500 A2 inference products|√|
|Atlas inference products|√|
|Atlas training products|√|

**Function<a id="zh-cn_topic_0000002216005989_section20806203412478"></a>**

Registers a memory pool. When calling this API to register a memory pool, the user must ensure that the memory has been allocated in advance.

**Prototype<a id="zh-cn_topic_0000002216005989_section1121883194711"></a>**

```python
mstxMemHeapHandle_t mstxMemHeapRegister(mstxDomainHandle_t domain, mstxMemHeapDesc_t const *desc)
```

**Parameter Description<a id="zh-cn_topic_0000002216005989_section11506138144714"></a>**

**Table 1**  Parameter description

<a name="zh-cn_topic_0000002216005989_table827101275518"></a>
<table><thead align="left"><tr id="zh-cn_topic_0000002216005989_row429121265517"><th class="cellrowborder" valign="top" width="16.881688168816883%" id="mcps1.2.4.1.1"><p id="zh-cn_topic_0000002216005989_p1329121214558"><a name="zh-cn_topic_0000002216005989_p1329121214558"></a><a name="zh-cn_topic_0000002216005989_p1329121214558"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="11.401140114011401%" id="mcps1.2.4.1.2"><p id="zh-cn_topic_0000002216005989_p10230141454318"><a name="zh-cn_topic_0000002216005989_p10230141454318"></a><a name="zh-cn_topic_0000002216005989_p10230141454318"></a>Input/Output</p>
</th>
<th class="cellrowborder" valign="top" width="71.71717171717171%" id="mcps1.2.4.1.3"><p id="zh-cn_topic_0000002216005989_p83121275519"><a name="zh-cn_topic_0000002216005989_p83121275519"></a><a name="zh-cn_topic_0000002216005989_p83121275519"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="zh-cn_topic_0000002216005989_row1131131265511"><td class="cellrowborder" valign="top" width="16.881688168816883%" headers="mcps1.2.4.1.1 "><p id="zh-cn_topic_0000002216005989_p7669321185110"><a name="zh-cn_topic_0000002216005989_p7669321185110"></a><a name="zh-cn_topic_0000002216005989_p7669321185110"></a>domain</p>
</td>
<td class="cellrowborder" valign="top" width="11.401140114011401%" headers="mcps1.2.4.1.2 "><p id="zh-cn_topic_0000002216005989_p723015144436"><a name="zh-cn_topic_0000002216005989_p723015144436"></a><a name="zh-cn_topic_0000002216005989_p723015144436"></a>Input</p>
</td>
<td class="cellrowborder" valign="top" width="71.71717171717171%" headers="mcps1.2.4.1.3 "><p id="zh-cn_topic_0000002216005989_p3243153110413"><a name="zh-cn_topic_0000002216005989_p3243153110413"></a><a name="zh-cn_topic_0000002216005989_p3243153110413"></a>Either globalDomain or the handle returned by <a href="../Common/mstxDomainCreateA.md">mstxDomainCreateA</a>.</p>
<p id="zh-cn_topic_0000002216005989_p17135131418533"><a name="zh-cn_topic_0000002216005989_p17135131418533"></a><a name="zh-cn_topic_0000002216005989_p17135131418533"></a>Data type: const char *.</p>
</td>
</tr>
<tr id="zh-cn_topic_0000002216005989_row18118485118"><td class="cellrowborder" valign="top" width="16.881688168816883%" headers="mcps1.2.4.1.1 "><p id="zh-cn_topic_0000002216005989_p211549516"><a name="zh-cn_topic_0000002216005989_p211549516"></a><a name="zh-cn_topic_0000002216005989_p211549516"></a>desc</p>
</td>
<td class="cellrowborder" valign="top" width="11.401140114011401%" headers="mcps1.2.4.1.2 "><p id="zh-cn_topic_0000002216005989_p1920117129516"><a name="zh-cn_topic_0000002216005989_p1920117129516"></a><a name="zh-cn_topic_0000002216005989_p1920117129516"></a>Input</p>
</td>
<td class="cellrowborder" valign="top" width="71.71717171717171%" headers="mcps1.2.4.1.3 ">

<pre class="screen" id="zh-cn_topic_0000002216005989_screen47021458121411"><a name="zh-cn_topic_0000002216005989_screen47021458121411"></a><a name="zh-cn_topic_0000002216005989_screen47021458121411"></a>typedef enum mstxMemHeapUsageType {
    /* @brief This heap memory is used as a memory pool
     * Heap memory registered using this usage type must be accessed after secondary allocation registration
     */
    MSTX_MEM_HEAP_USAGE_TYPE_SUB_ALLOCATOR = 0,
} mstxMemHeapUsageType;

/** @brief Heap memory type

 * The "type" here refers to the method used to describe the heap memory pointer. Currently, only linearly arranged memory is supported.
 * memory, but the capability to support more memory types in the future is reserved here. For example, some APIs return
 * multiple handles to describe a memory range, or some high-dimensional memory requires stride, tiling, or
 * interlace for description.
 */
typedef enum mstxMemType {
    /** @brief Standard linearly laid out virtual memory
      * In this case, mstxMemHeapRegister receives a description of the mstxMemVirtualRangeDesc_t type.
      */
    MSTX_MEM_TYPE_VIRTUAL_ADDRESS = 0,
} mstxMemType;

typedef struct mstxMemVirtualRangeDesc_t {
    uint32_t deviceId;  // Device ID corresponding to the memory region
    void const *ptr;  // Start address of the memory region
    uint64_t size;  // Length of the memory region
} mstxMemVirtualRangeDesc_t;

typedef struct mstxMemHeapDesc_t {
    mstxMemHeapUsageType usage;  // Usage mode of the heap memory
    mstxMemType type;  // Type of the heap memory
    void const *typeSpecificDesc;  // Description information of the heap memory under the specified memory type
} mstxMemHeapDesc_t;</pre>
</td>
</tr>
</tbody>
</table>

**Returns<a id="zh-cn_topic_0000002216005989_section16621124213476"></a>**

Handle corresponding to the memory pool.

**Example<a id="zh-cn_topic_0000002216005989_section377820328555"></a>**

```c
mstxMemVirtualRangeDesc_t rangeDesc = {};
    rangeDesc.deviceId = deviceId;       // Device ID
    rangeDesc.ptr = gm;                  // Start address of the registered memory pool gm
    rangeDesc.size = 1024;               // Memory pool size
    heapDesc.typeSpecificDesc = &rangeDesc;
    mstxMemHeapDesc_t heapDesc{};
    mstxMemHeapHandle_t memPool = mstxMemHeapRegister(globalDomain, &heapDesc); // Register memory pool
```
