# mstxMemRegionsRegister<a id="mstxMemRegionsRegister"></a>

**产品支持情况<a id="section8178181118225"></a>**

|产品|是否支持|
|--|:-:|
|Atlas 350 加速卡|√|
|Atlas A3 训练系列产品/Atlas A3 推理系列产品|√|
|Atlas A2 训练系列产品/Atlas A2 推理系列产品|√|
|Atlas 200I/500 A2 推理产品|√|
|Atlas 推理系列产品|√|
|Atlas 训练系列产品|√|

**功能说明<a id="zh-cn_topic_0000002180759810_section20806203412478"></a>**

注册内存池二次分配。用户需保证mstxRegionsRegister的内存位于[mstxMemHeapRegister](../Mem/mstxMemHeapRegister.md)注册的范围内，否则工具会提示越界读写。

**函数原型<a id="zh-cn_topic_0000002180759810_section1121883194711"></a>**

```c
void mstxMemRegionsRegister(mstxDomainHandle_t domain, mstxMemRegionsRegisterBatch_t const *desc)
```

**参数说明<a id="zh-cn_topic_0000002180759810_section11506138144714"></a>**

**表 1**  参数说明

<a name="zh-cn_topic_0000002180759810_table827101275518"></a>
<table><thead align="left"><tr id="zh-cn_topic_0000002180759810_row429121265517"><th class="cellrowborder" valign="top" width="28.65286528652865%" id="mcps1.2.4.1.1"><p id="zh-cn_topic_0000002180759810_p1329121214558"><a name="zh-cn_topic_0000002180759810_p1329121214558"></a><a name="zh-cn_topic_0000002180759810_p1329121214558"></a>参数</p>
</th>
<th class="cellrowborder" valign="top" width="26.7026702670267%" id="mcps1.2.4.1.2"><p id="zh-cn_topic_0000002180759810_p10230141454318"><a name="zh-cn_topic_0000002180759810_p10230141454318"></a><a name="zh-cn_topic_0000002180759810_p10230141454318"></a>输入/输出</p>
</th>
<th class="cellrowborder" valign="top" width="44.64446444644465%" id="mcps1.2.4.1.3"><p id="zh-cn_topic_0000002180759810_p83121275519"><a name="zh-cn_topic_0000002180759810_p83121275519"></a><a name="zh-cn_topic_0000002180759810_p83121275519"></a>说明</p>
</th>
</tr>
</thead>
<tbody><tr id="zh-cn_topic_0000002180759810_row1131131265511"><td class="cellrowborder" valign="top" width="28.65286528652865%" headers="mcps1.2.4.1.1 "><p id="zh-cn_topic_0000002180759810_p7669321185110"><a name="zh-cn_topic_0000002180759810_p7669321185110"></a><a name="zh-cn_topic_0000002180759810_p7669321185110"></a>domain</p>
</td>
<td class="cellrowborder" valign="top" width="26.7026702670267%" headers="mcps1.2.4.1.2 "><p id="zh-cn_topic_0000002180759810_p723015144436"><a name="zh-cn_topic_0000002180759810_p723015144436"></a><a name="zh-cn_topic_0000002180759810_p723015144436"></a>输入</p>
</td>
<td class="cellrowborder" valign="top" width="44.64446444644465%" headers="mcps1.2.4.1.3 "><p id="zh-cn_topic_0000002180759810_p3243153110413"><a name="zh-cn_topic_0000002180759810_p3243153110413"></a><a name="zh-cn_topic_0000002180759810_p3243153110413"></a>为globalDomain或<a href="../Common/mstxDomainCreateA.md">mstxDomainCreateA</a>返回的句柄。</p>
<p id="zh-cn_topic_0000002180759810_p17135131418533"><a name="zh-cn_topic_0000002180759810_p17135131418533"></a><a name="zh-cn_topic_0000002180759810_p17135131418533"></a>数据类型：const char *。</p>
</td>
</tr>
<tr id="zh-cn_topic_0000002180759810_row18118485118"><td class="cellrowborder" valign="top" width="28.65286528652865%" headers="mcps1.2.4.1.1 "><p id="zh-cn_topic_0000002180759810_p211549516"><a name="zh-cn_topic_0000002180759810_p211549516"></a><a name="zh-cn_topic_0000002180759810_p211549516"></a>desc</p>
</td>
<td class="cellrowborder" valign="top" width="26.7026702670267%" headers="mcps1.2.4.1.2 "><p id="zh-cn_topic_0000002180759810_p1920117129516"><a name="zh-cn_topic_0000002180759810_p1920117129516"></a><a name="zh-cn_topic_0000002180759810_p1920117129516"></a>输入</p>
</td>
<td class="cellrowborder" valign="top" width="44.64446444644465%" headers="mcps1.2.4.1.3 "><p id="zh-cn_topic_0000002180759810_p14824161530710"><a name="zh-cn_topic_0000002180759810_p14824161530710"></a><a name="zh-cn_topic_0000002180759810_p14824161530710"></a>内存池待二次分配的内存区域描述信息，不能为空。</p>

<pre class="screen" id="zh-cn_topic_0000002180759810_screen19859174319117"><a name="zh-cn_topic_0000002180759810_screen19859174319117"></a><a name="zh-cn_topic_0000002180759810_screen19859174319117"></a>struct mstxMemRegion_st;
typedef struct mstxMemRegion_st mstxMemRegion_t;
typedef mstxMemRegion_t* mstxMemRegionHandle_t;

typedef struct mstxMemRegionsRegisterBatch_t {
    mstxMemHeapHandle_t heap;  // 要进行二次分配的内存池句柄
    mstxMemType regionType;  // 内存区域的内存类型
    size_t regionCount;  // 内存区域的个数
    void const *regionDescArray;  // 内存区域描述数据
    mstxMemRegionHandle_t* regionHandleArrayOut;  // 返回的注册二次分配得到的句柄数组
} mstxMemRegionsRegisterBatch_t;</pre>
</td>
</tr>
</tbody>
</table>

**返回值说明<a id="zh-cn_topic_0000002180759810_section16621124213476"></a>**

无

**调用示例<a id="zh-cn_topic_0000002180759810_section377820328555"></a>**

```c
mstxMemRegionsRegisterBatch_t regionsDesc{};
regionsDesc.heap = memPool;
regionsDesc.regionType = MSTX_MEM_TYPE_VIRTUAL_ADDRESS;
regionsDesc.regionCount = 1;
regionsDesc.regionDescArray = rangesDesc;
regionsDesc.regionHandleArrayOut = regionHandles;
mstxMemRegionsRegister(globalDomain, regionsDesc);              // 二次分配注册 
```
