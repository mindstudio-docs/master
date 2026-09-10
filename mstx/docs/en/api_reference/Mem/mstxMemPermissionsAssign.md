# mstxMemPermissionsAssign<a id="mstxMemPermissionsAssign"></a>

**Supported Products<a id="section8178181118225"></a>**

|Product|Supported|
|--|:-:|
|Ascend 950 products|√|
|Atlas A3 training products/Atlas A3 inference products|√|
|Atlas A2 training products/Atlas A2 inference products|√|
|Atlas 200I/500 A2 inference products|√|
|Atlas inference products|√|
|Atlas training products|√|

**Function<a id="zh-cn_topic_0000002216005989_section20806203412478"></a>**

Specifies read, write, and share access permissions for a virtual memory interval. Before specifying permissions, ensure that this interval has been registered as a region.

**Prototype<a id="zh-cn_topic_0000002216005989_section1121883194711"></a>**

```c
void mstxMemPermissionsAssign(mstxDomainHandle_t domain, mstxMemPermissionsAssignBatch_t const *desc);
```

**Parameter Description<a id="zh-cn_topic_0000002216005989_section11506138144714"></a>**

**Table 1** Parameter description

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

<pre class="screen" id="zh-cn_topic_0000002216005989_screen47021458121411"><a name="zh-cn_topic_0000002216005989_screen47021458121411"></a><a name="zh-cn_topic_0000002216005989_screen47021458121411"></a>
/** @brief No access permission for this memory
 */
#define MSTX_MEM_PERMISSIONS_REGION_FLAGS_NONE 0x00

/** @brief This memory is readable
 */
#define MSTX_MEM_PERMISSIONS_REGION_FLAGS_READ 0x01

/** @brief This memory is writable
 */
#define MSTX_MEM_PERMISSIONS_REGION_FLAGS_WRITE 0x02

/** @brief This memory can be shared across multiple devices
 */
#define MSTX_MEM_PERMISSIONS_REGION_FLAGS_SHARED 0x04

/** @brief Describes the memory permissions assigned to a region
  * @member flags - Permission flags represented by MSTX_MEM_PERMISSIONS_REGION_FLAGS_*
  * @member region - Reference to a registered virtual memory region
  */
typedef struct mstxMemPermissionsAssignRegionsDesc_t {
    uint32_t flags;
    mstxMemRegionRef_t region;
} mstxMemPermissionsAssignRegionsDesc_t;

/** @brief Used to describe memory permissions for multiple regions
  * @member regionCount - Length of the regionDescArray
  * @member regionDescArray - Array of permission descriptors
  */
typedef struct mstxMemPermissionsAssignBatch_t {
    size_t regionCount;
    mstxMemPermissionsAssignRegionsDesc_t const *regionDescArray;
} mstxMemPermissionsAssignBatch_t;</pre>
</td>
</tr>
</tbody>
</table>

**Returns<a id="zh-cn_topic_0000002216005989_section16621124213476"></a>**

None.

**Example<a id="zh-cn_topic_0000002216005989_section377820328555"></a>**

```c
// Assume handles have been initialized by mstxMemRegionsRegister
mstxMemRegionHandle_t handles[2];

mstxMemPermissionsAssignRegionsDesc_t perms[2];
mstxMemPermissionsAssignBatch_t permBatch{};
perms[0].flags = MSTX_MEM_PERMISSIONS_REGION_FLAGS_READ;
perms[0].region.refType = MSTX_MEM_REGION_REF_TYPE_HANDLE;
perms[0].region.handle = handles[0];
perms[1].flags = MSTX_MEM_PERMISSIONS_REGION_FLAGS_WRITE;
perms[1].region.refType = MSTX_MEM_REGION_REF_TYPE_HANDLE;
perms[1].region.handle = handles[0];
permBatch.regionCount = 2;
permBatch.regionDescArray = perms;

// Assume globalDomain has been initialized by mstxMemRegionsRegister
mstxMemPermissionsAssign(globalDomain, &permBatch);
```
