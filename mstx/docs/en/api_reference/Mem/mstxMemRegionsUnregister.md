# mstxMemRegionsUnregister<a id="mstxMemRegionsUnregister"></a>

**Supported Products<a id="section8178181118225"></a>**

|Product|Supported|
|--|:-:|
|Ascend 910_95 AI Processors|√|
|Atlas A3 training products/Atlas A3 inference products|√|
|Atlas A2 training products/Atlas A2 inference products|√|
|Atlas 200I/500 A2 inference products|√|
|Atlas inference products|√|
|Atlas training products|√|

**Function<a id="zh-cn_topic_0000002180600118_section20806203412478"></a>**

Unregisters secondary allocation of a memory pool.

**Prototype<a id="zh-cn_topic_0000002180600118_section1121883194711"></a>**

```c
void mstxMemRegionsUnregister(mstxDomainHandle_t domain, mstxMemRegionsUnregisterBatch_t const *desc)
```

**Parameter Description<a id="zh-cn_topic_0000002180600118_section11506138144714"></a>**

**Table 1** Parameter description

<a name="zh-cn_topic_0000002180600118_table827101275518"></a>
<table><thead align="left"><tr id="zh-cn_topic_0000002180600118_row429121265517"><th class="cellrowborder" valign="top" width="28.652865286528655%" id="mcps1.2.4.1.1"><p id="zh-cn_topic_0000002180600118_p1329121214558"><a name="zh-cn_topic_0000002180600118_p1329121214558"></a><a name="zh-cn_topic_0000002180600118_p1329121214558"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="21.002100210021005%" id="mcps1.2.4.1.2"><p id="zh-cn_topic_0000002180600118_p10230141454318"><a name="zh-cn_topic_0000002180600118_p10230141454318"></a><a name="zh-cn_topic_0000002180600118_p10230141454318"></a>Input/Output</p>
</th>
<th class="cellrowborder" valign="top" width="50.34503450345035%" id="mcps1.2.4.1.3"><p id="zh-cn_topic_0000002180600118_p83121275519"><a name="zh-cn_topic_0000002180600118_p83121275519"></a><a name="zh-cn_topic_0000002180600118_p83121275519"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="zh-cn_topic_0000002180600118_row1131131265511"><td class="cellrowborder" valign="top" width="28.652865286528655%" headers="mcps1.2.4.1.1 "><p id="zh-cn_topic_0000002180600118_p7669321185110"><a name="zh-cn_topic_0000002180600118_p7669321185110"></a><a name="zh-cn_topic_0000002180600118_p7669321185110"></a>domain</p>
</td>
<td class="cellrowborder" valign="top" width="21.002100210021005%" headers="mcps1.2.4.1.2 "><p id="zh-cn_topic_0000002180600118_p723015144436"><a name="zh-cn_topic_0000002180600118_p723015144436"></a><a name="zh-cn_topic_0000002180600118_p723015144436"></a>Input</p>
</td>
<td class="cellrowborder" valign="top" width="50.34503450345035%" headers="mcps1.2.4.1.3 "><p id="zh-cn_topic_0000002180600118_p3243153110413"><a name="zh-cn_topic_0000002180600118_p3243153110413"></a><a name="zh-cn_topic_0000002180600118_p3243153110413"></a>Either globalDomain or the handle returned by <a href="../Common/mstxDomainCreateA.md">mstxDomainCreateA</a>.</p>
<p id="zh-cn_topic_0000002180600118_p17135131418533"><a name="zh-cn_topic_0000002180600118_p17135131418533"></a><a name="zh-cn_topic_0000002180600118_p17135131418533"></a>Data Type: const char *.</p>
</td>
</tr>
<tr id="zh-cn_topic_0000002180600118_row18118485118"><td class="cellrowborder" valign="top" width="28.652865286528655%" headers="mcps1.2.4.1.1 "><p id="zh-cn_topic_0000002180600118_p211549516"><a name="zh-cn_topic_0000002180600118_p211549516"></a><a name="zh-cn_topic_0000002180600118_p211549516"></a>desc</p>
</td>
<td class="cellrowborder" valign="top" width="21.002100210021005%" headers="mcps1.2.4.1.2 "><p id="zh-cn_topic_0000002180600118_p1920117129516"><a name="zh-cn_topic_0000002180600118_p1920117129516"></a><a name="zh-cn_topic_0000002180600118_p1920117129516"></a>Input</p>
</td>
<td class="cellrowborder" valign="top" width="50.34503450345035%" headers="mcps1.2.4.1.3 "><p id="zh-cn_topic_0000002180600118_p14824161520710"><a name="zh-cn_topic_0000002180600118_p14824161520710"></a><a name="zh-cn_topic_0000002180600118_p14824161520710"></a>The input description information must be the input description information from a previous <a href="mstxMemHeapRegister.md">mstxMemHeapRegister</a> call; otherwise, the tool will print an error message.</p>

<pre class="screen" id="zh-cn_topic_0000002180600118_screen1854493213265"><a name="zh-cn_topic_0000002180600118_screen1854493213265"></a><a name="zh-cn_topic_0000002180600118_screen1854493213265"></a>typedef enum mstxMemRegionRefType {
    // Describes a memory reference via a pointer
    MSTX_MEM_REGION_REF_TYPE_POINTER = 0,
    // Describes a memory reference via a handle
    MSTX_MEM_REGION_REF_TYPE_HANDLE
} mstxMemRegionRefType;

typedef struct mstxMemRegionRef_t {
    mstxMemRegionRefType refType; // Describes how the memory is referenced
    union {
        void const* pointer;  // When the current memory reference is described by a pointer, this stores the memory region pointer
        mstxMemRegionHandle_t handle;  // When the memory reference is described by a handle, this stores the handle of the memory region
    };
} mstxMemRegionRef_t;

typedef struct mstxMemRegionsUnregisterBatch_t {
    size_t refCount;  // Number of memory references
    mstxMemRegionRef_t const *refArray;  // Array of memory region references to unregister
} mstxMemRegionsUnregisterBatch_t;</pre>
</td>
</tr>
</tbody>
</table>

**Returns<a id="zh-cn_topic_0000002180600118_section16621124213476"></a>**

None

**Example<a id="zh-cn_topic_0000002180600118_section377820328555"></a>**

```python
mstxMemRegionsUnregisterBatch_t refsDesc = {}
refsDesc.refCount = 1;
refsDesc.refArray = regionRef;
mstxMemRegionsUnregister(globalDomain, &refsDesc);                   // Unregister secondary allocationster Secondary Allocation
```
