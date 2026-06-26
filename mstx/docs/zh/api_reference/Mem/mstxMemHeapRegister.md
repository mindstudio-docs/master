# mstxMemHeapRegister<a id="mstxMemHeapRegister"></a>

**产品支持情况<a id="section8178181118225"></a>**

|产品|是否支持|
|--|:-:|
|Atlas 350 加速卡|√|
|Atlas A3 训练系列产品/Atlas A3 推理系列产品|√|
|Atlas A2 训练系列产品/Atlas A2 推理系列产品|√|
|Atlas 200I/500 A2 推理产品|√|
|Atlas 推理系列产品|√|
|Atlas 训练系列产品|√|

**功能说明<a id="zh-cn_topic_0000002216005989_section20806203412478"></a>**

注册内存池。用户在调用该接口注册内存池时，需确保该内存已提前申请。

**函数原型<a id="zh-cn_topic_0000002216005989_section1121883194711"></a>**

```c
mstxMemHeapHandle_t mstxMemHeapRegister(mstxDomainHandle_t domain, mstxMemHeapDesc_t const *desc)
```

**参数说明<a id="zh-cn_topic_0000002216005989_section11506138144714"></a>**

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

<pre class="screen" id="zh-cn_topic_0000002216005989_screen47021458121411"><a name="zh-cn_topic_0000002216005989_screen47021458121411"></a><a name="zh-cn_topic_0000002216005989_screen47021458121411"></a>typedef enum mstxMemHeapUsageType {
    /* @brief 此堆内存作为内存池使用
     * 使用此使用方式注册的堆内存，需要使用二次分配注册后才可以访问
     */
    MSTX_MEM_HEAP_USAGE_TYPE_SUB_ALLOCATOR = 0,
} mstxMemHeapUsageType;

/** @brief 堆内存的类型

 * 此处的“类型”是指通过何种方式来描述堆内存指针。当前仅支持线性排布的
 * 内存，但此处保留日后支持更多内存类型的扩展能力。比如某些API返回
 * 多个句柄来描述内存范围，或者一些高维内存需要使用stride、tiling或
 * interlace来描述
 */
typedef enum mstxMemType {
    /** @brief 标准线性排布的虚拟内存
      * 此时mstxMemHeapRegister接收mstxMemVirtualRangeDesc_t类型的描述
      */
    MSTX_MEM_TYPE_VIRTUAL_ADDRESS = 0,
} mstxMemType;

typedef struct mstxMemVirtualRangeDesc_t {
    uint32_t deviceId;  // 内存区域对应的设备 ID
    void const *ptr;  // 内存区域的起始地址
    uint64_t size;  // 内存区域的长度
} mstxMemVirtualRangeDesc_t;

typedef struct mstxMemHeapDesc_t {
    mstxMemHeapUsageType usage;  // 堆内存的使用方式
    mstxMemType type;  // 堆内存的类型
    void const *typeSpecificDesc;  // 堆内存在指定内存类型下的描述信息
} mstxMemHeapDesc_t;</pre>
</td>
</tr>
</tbody>
</table>

**返回值说明<a id="zh-cn_topic_0000002216005989_section16621124213476"></a>**

内存池对应的句柄。

**调用示例<a id="zh-cn_topic_0000002216005989_section377820328555"></a>**

```c
mstxMemVirtualRangeDesc_t rangeDesc = {};
    rangeDesc.deviceId = deviceId;       // 设备编号
    rangeDesc.ptr = gm;                  // 注册的内存池gm首地址
    rangeDesc.size = 1024;               // 内存池大小
    heapDesc.typeSpecificDesc = &rangeDesc;
    mstxMemHeapDesc_t heapDesc{};
    mstxMemHeapHandle_t memPool = mstxMemHeapRegister(globalDomain, &heapDesc); // 注册内存池  
```
