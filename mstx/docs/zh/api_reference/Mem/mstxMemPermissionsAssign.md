# mstxMemPermissionsAssign<a id="mstxMemPermissionsAssign"></a>

**产品支持情况**

|产品|是否支持|
|--|:-:|
|Atlas 350 加速卡|√|
|Atlas A3 训练系列产品/Atlas A3 推理系列产品|√|
|Atlas A2 训练系列产品/Atlas A2 推理系列产品|√|
|Atlas 200I/500 A2 推理产品|√|
|Atlas 推理系列产品|√|
|Atlas 训练系列产品|√|

**功能说明**

为虚拟内存区间指定读、写、共享访问权限，指定权限前需保证此区间已注册为 region。

**函数原型**

```c
void mstxMemPermissionsAssign(mstxDomainHandle_t domain, mstxMemPermissionsAssignBatch_t const *desc);
```

**参数说明**

**表 1**  参数说明

<a name="zh-cn_topic_0000002216005989_table827101275518"></a>
<table><thead align="left"><tr id="zh-cn_topic_0000002216005989_row429121265517"><th class="cellrowborder" valign="top" width="16.881688168816883%" id="mcps1.2.4.1.1"><p id="zh-cn_topic_0000002216005989_p1329121214558"><a name="zh-cn_topic_0000002216005989_p1329121214558"></a><a name="zh-cn_topic_0000002216005989_p1329121214558"></a>参数</p>
</th>
<th class="cellrowborder" valign="top" width="11.401140114011401%" id="mcps1.2.4.1.2"><p id="zh-cn_topic_0000002216005989_p10230141454318"><a name="zh-cn_topic_0000002216005989_p10230141454318"></a><a name="zh-cn_topic_0000002216005989_p10230141454318"></a>输入/输出</p>
</th>
<th class="cellrowborder" valign="top" width="71.71717171717171%" id="mcps1.2.4.1.3"><p id="zh-cn_topic_0000002216005989_p83121275519"><a name="zh-cn_topic_0000002216005989_p83121275519"></a><a name="zh-cn_topic_0000002216005989_p83121275519"></a>说明</p>
</th>
</tr>
</thead>
<tbody><tr id="zh-cn_topic_0000002216005989_row1131131265511"><td class="cellrowborder" valign="top" width="16.881688168816883%" headers="mcps1.2.4.1.1 "><p id="zh-cn_topic_0000002216005989_p7669321185110"><a name="zh-cn_topic_0000002216005989_p7669321185110"></a><a name="zh-cn_topic_0000002216005989_p7669321185110"></a>domain</p>
</td>
<td class="cellrowborder" valign="top" width="11.401140114011401%" headers="mcps1.2.4.1.2 "><p id="zh-cn_topic_0000002216005989_p723015144436"><a name="zh-cn_topic_0000002216005989_p723015144436"></a><a name="zh-cn_topic_0000002216005989_p723015144436"></a>输入</p>
</td>
<td class="cellrowborder" valign="top" width="71.71717171717171%" headers="mcps1.2.4.1.3 "><p id="zh-cn_topic_0000002216005989_p3243153110413"><a name="zh-cn_topic_0000002216005989_p3243153110413"></a><a name="zh-cn_topic_0000002216005989_p3243153110413"></a>为globalDomain或<a href="../Common/mstxDomainCreateA.md">mstxDomainCreateA</a>返回的句柄。</p>
<p id="zh-cn_topic_0000002216005989_p17135131418533"><a name="zh-cn_topic_0000002216005989_p17135131418533"></a><a name="zh-cn_topic_0000002216005989_p17135131418533"></a>数据类型：const char *。</p>
</td>
</tr>
<tr id="zh-cn_topic_0000002216005989_row18118485118"><td class="cellrowborder" valign="top" width="16.881688168816883%" headers="mcps1.2.4.1.1 "><p id="zh-cn_topic_0000002216005989_p211549516"><a name="zh-cn_topic_0000002216005989_p211549516"></a><a name="zh-cn_topic_0000002216005989_p211549516"></a>desc</p>
</td>
<td class="cellrowborder" valign="top" width="11.401140114011401%" headers="mcps1.2.4.1.2 "><p id="zh-cn_topic_0000002216005989_p1920117129516"><a name="zh-cn_topic_0000002216005989_p1920117129516"></a><a name="zh-cn_topic_0000002216005989_p1920117129516"></a>输入</p>
</td>
<td class="cellrowborder" valign="top" width="71.71717171717171%" headers="mcps1.2.4.1.3 ">

<pre class="screen" id="zh-cn_topic_0000002216005989_screen47021458121411"><a name="zh-cn_topic_0000002216005989_screen47021458121411"></a><a name="zh-cn_topic_0000002216005989_screen47021458121411"></a>
/** @brief 该内存无访问权限
 */
#define MSTX_MEM_PERMISSIONS_REGION_FLAGS_NONE 0x00

/** @brief 该内存可读
 */
#define MSTX_MEM_PERMISSIONS_REGION_FLAGS_READ 0x01

/** @brief 该内存可写
 */
#define MSTX_MEM_PERMISSIONS_REGION_FLAGS_WRITE 0x02

/** @brief 该内存可在多设备间共享访问
 */
#define MSTX_MEM_PERMISSIONS_REGION_FLAGS_SHARED 0x04

/** @brief 用于描述为 Region 指定的内存权限
  * @member flags - 使用 MSTX_MEM_PERMISSIONS_REGION_FLAGS_* 表示的权限标志位
  * @member region - 指向已注册的虚拟内存区间的引用
  */
typedef struct mstxMemPermissionsAssignRegionsDesc_t {
    uint32_t flags;
    mstxMemRegionRef_t region;
} mstxMemPermissionsAssignRegionsDesc_t;

/** @brief 用于描述为多个 Region 指定内存权限
  * @member regionCount - regionDescArray 数组长度
  * @member regionDescArray - 权限描述数组
  */
typedef struct mstxMemPermissionsAssignBatch_t {
    size_t regionCount;
    mstxMemPermissionsAssignRegionsDesc_t const *regionDescArray;
} mstxMemPermissionsAssignBatch_t;</pre>
</td>
</tr>
</tbody>
</table>

**返回值说明<a id="zh-cn_topic_0000002216005989_section16621124213476"></a>**

无。

**调用示例<a id="zh-cn_topic_0000002216005989_section377820328555"></a>**

```c
// 假定 handles 已由 mstxMemRegionsRegister 初始化
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
mstxMemPermissionsAssign(globalDomain, &permBatch);
```
