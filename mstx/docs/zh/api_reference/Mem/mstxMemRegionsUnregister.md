# mstxMemRegionsUnregister<a id="mstxMemRegionsUnregister"></a>

**产品支持情况<a id="section8178181118225"></a>**

|产品|是否支持|
|--|:-:|
|Ascend 950 系列产品|√|
|Atlas A3 训练系列产品/Atlas A3 推理系列产品|√|
|Atlas A2 训练系列产品/Atlas A2 推理系列产品|√|
|Atlas 200I/500 A2 推理产品|√|
|Atlas 推理系列产品|√|
|Atlas 训练系列产品|√|

**功能说明<a id="zh-cn_topic_0000002180600118_section20806203412478"></a>**

注销内存池二次分配。

**函数原型<a id="zh-cn_topic_0000002180600118_section1121883194711"></a>**

```c
void mstxMemRegionsUnregister(mstxDomainHandle_t domain, mstxMemRegionsUnregisterBatch_t const *desc)
```

**参数说明<a id="zh-cn_topic_0000002180600118_section11506138144714"></a>**

**表 1**  参数说明

<a name="zh-cn_topic_0000002180600118_table827101275518"></a>
<table><thead align="left"><tr id="zh-cn_topic_0000002180600118_row429121265517"><th class="cellrowborder" valign="top" width="28.652865286528655%" id="mcps1.2.4.1.1"><p id="zh-cn_topic_0000002180600118_p1329121214558"><a name="zh-cn_topic_0000002180600118_p1329121214558"></a><a name="zh-cn_topic_0000002180600118_p1329121214558"></a>参数</p>
</th>
<th class="cellrowborder" valign="top" width="21.002100210021005%" id="mcps1.2.4.1.2"><p id="zh-cn_topic_0000002180600118_p10230141454318"><a name="zh-cn_topic_0000002180600118_p10230141454318"></a><a name="zh-cn_topic_0000002180600118_p10230141454318"></a>输入/输出</p>
</th>
<th class="cellrowborder" valign="top" width="50.34503450345035%" id="mcps1.2.4.1.3"><p id="zh-cn_topic_0000002180600118_p83121275519"><a name="zh-cn_topic_0000002180600118_p83121275519"></a><a name="zh-cn_topic_0000002180600118_p83121275519"></a>说明</p>
</th>
</tr>
</thead>
<tbody><tr id="zh-cn_topic_0000002180600118_row1131131265511"><td class="cellrowborder" valign="top" width="28.652865286528655%" headers="mcps1.2.4.1.1 "><p id="zh-cn_topic_0000002180600118_p7669321185110"><a name="zh-cn_topic_0000002180600118_p7669321185110"></a><a name="zh-cn_topic_0000002180600118_p7669321185110"></a>domain</p>
</td>
<td class="cellrowborder" valign="top" width="21.002100210021005%" headers="mcps1.2.4.1.2 "><p id="zh-cn_topic_0000002180600118_p723015144436"><a name="zh-cn_topic_0000002180600118_p723015144436"></a><a name="zh-cn_topic_0000002180600118_p723015144436"></a>输入</p>
</td>
<td class="cellrowborder" valign="top" width="50.34503450345035%" headers="mcps1.2.4.1.3 "><p id="zh-cn_topic_0000002180600118_p3243153110413"><a name="zh-cn_topic_0000002180600118_p3243153110413"></a><a name="zh-cn_topic_0000002180600118_p3243153110413"></a>为globalDomain或<a href="../Common/mstxDomainCreateA.md">mstxDomainCreateA</a>返回的句柄。</p>
<p id="zh-cn_topic_0000002180600118_p17135131418533"><a name="zh-cn_topic_0000002180600118_p17135131418533"></a><a name="zh-cn_topic_0000002180600118_p17135131418533"></a>数据类型：const char *。</p>
</td>
</tr>
<tr id="zh-cn_topic_0000002180600118_row18118485118"><td class="cellrowborder" valign="top" width="28.652865286528655%" headers="mcps1.2.4.1.1 "><p id="zh-cn_topic_0000002180600118_p211549516"><a name="zh-cn_topic_0000002180600118_p211549516"></a><a name="zh-cn_topic_0000002180600118_p211549516"></a>desc</p>
</td>
<td class="cellrowborder" valign="top" width="21.002100210021005%" headers="mcps1.2.4.1.2 "><p id="zh-cn_topic_0000002180600118_p1920117129516"><a name="zh-cn_topic_0000002180600118_p1920117129516"></a><a name="zh-cn_topic_0000002180600118_p1920117129516"></a>输入</p>
</td>
<td class="cellrowborder" valign="top" width="50.34503450345035%" headers="mcps1.2.4.1.3 "><p id="zh-cn_topic_0000002180600118_p14824161530710"><a name="zh-cn_topic_0000002180600118_p14824161530710"></a><a name="zh-cn_topic_0000002180600118_p14824161530710"></a>输入的描述信息必须是某一次<a href="../Mem/mstxMemHeapRegister.md">mstxMemHeapRegister</a>的输入描述信息，否则工具将打印提示错误。</p>

<pre class="screen" id="zh-cn_topic_0000002180600118_screen1854493213265"><a name="zh-cn_topic_0000002180600118_screen1854493213265"></a><a name="zh-cn_topic_0000002180600118_screen1854493213265"></a>typedef enum mstxMemRegionRefType {
    // 通过指针描述内存引用
    MSTX_MEM_REGION_REF_TYPE_POINTER = 0,
    // 通过句柄描述内存引用
    MSTX_MEM_REGION_REF_TYPE_HANDLE
} mstxMemRegionRefType;

typedef struct mstxMemRegionRef_t {
    mstxMemRegionRefType refType; // 描述内存引用的方式
    union {
        void const* pointer;  // 当前内存引用通过指针描述时，此处保存内存区域指针
        mstxMemRegionHandle_t handle;  // 当内存引用通过句柄描述时，此处保存内存区域的句柄 
    };
} mstxMemRegionRef_t;

typedef struct mstxMemRegionsUnregisterBatch_t {
    size_t refCount;  // 内存引用的个数
    mstxMemRegionRef_t const *refArray;  // 要注销的内存区域引用
} mstxMemRegionsUnregisterBatch_t;</pre>
</td>
</tr>
</tbody>
</table>

**返回值说明<a id="zh-cn_topic_0000002180600118_section16621124213476"></a>**

无

**调用示例<a id="zh-cn_topic_0000002180600118_section377820328555"></a>**

```c
mstxMemRegionsUnregisterBatch_t refsDesc = {};
refsDesc.refCount = 1;
refsDesc.refArray = regionRef;
mstxMemRegionsUnregister(globalDomain, &refsDesc);                   // 注销二次分配
```
