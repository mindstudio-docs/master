# mstxMemHeapUnregister<a id="mstxMemHeapUnregister"></a>

**产品支持情况<a id="section8178181118225"></a>**

|产品|是否支持|
|--|:-:|
|Atlas 350 加速卡|√|
|Atlas A3 训练系列产品/Atlas A3 推理系列产品|√|
|Atlas A2 训练系列产品/Atlas A2 推理系列产品|√|
|Atlas 200I/500 A2 推理产品|√|
|Atlas 推理系列产品|√|
|Atlas 训练系列产品|√|

**功能说明<a id="zh-cn_topic_0000002215920417_section20806203412478"></a>**

注销内存池时，与之关联的Regions将一并被注销。

**函数原型<a id="zh-cn_topic_0000002215920417_section1121883194711"></a>**

```cpp
void mstxMemHeapUnregister(mstxDomainHandle_t domain, mstxMemHeapHandle_t heap)
```

**参数说明<a id="zh-cn_topic_0000002215920417_section11506138144714"></a>**

**表 1**  参数说明

<a name="zh-cn_topic_0000002215920417_table827101275518"></a>
<table><thead align="left"><tr id="zh-cn_topic_0000002215920417_row429121265517"><th class="cellrowborder" valign="top" width="28.65286528652865%" id="mcps1.2.4.1.1"><p id="zh-cn_topic_0000002215920417_p1329121214558"><a name="zh-cn_topic_0000002215920417_p1329121214558"></a><a name="zh-cn_topic_0000002215920417_p1329121214558"></a>参数</p>
</th>
<th class="cellrowborder" valign="top" width="26.72267226722672%" id="mcps1.2.4.1.2"><p id="zh-cn_topic_0000002215920417_p10230141454318"><a name="zh-cn_topic_0000002215920417_p10230141454318"></a><a name="zh-cn_topic_0000002215920417_p10230141454318"></a>输入/输出</p>
</th>
<th class="cellrowborder" valign="top" width="44.62446244624462%" id="mcps1.2.4.1.3"><p id="zh-cn_topic_0000002215920417_p83121275519"><a name="zh-cn_topic_0000002215920417_p83121275519"></a><a name="zh-cn_topic_0000002215920417_p83121275519"></a>说明</p>
</th>
</tr>
</thead>
<tbody><tr id="zh-cn_topic_0000002215920417_row1131131265511"><td class="cellrowborder" valign="top" width="28.65286528652865%" headers="mcps1.2.4.1.1 "><p id="zh-cn_topic_0000002215920417_p7669321185110"><a name="zh-cn_topic_0000002215920417_p7669321185110"></a><a name="zh-cn_topic_0000002215920417_p7669321185110"></a>domain</p>
</td>
<td class="cellrowborder" valign="top" width="26.72267226722672%" headers="mcps1.2.4.1.2 "><p id="zh-cn_topic_0000002215920417_p723015144436"><a name="zh-cn_topic_0000002215920417_p723015144436"></a><a name="zh-cn_topic_0000002215920417_p723015144436"></a>输入</p>
</td>
<td class="cellrowborder" valign="top" width="44.62446244624462%" headers="mcps1.2.4.1.3 "><p id="zh-cn_topic_0000002215920417_p3243153110413"><a name="zh-cn_topic_0000002215920417_p3243153110413"></a><a name="zh-cn_topic_0000002215920417_p3243153110413"></a>domain为内存池所属的域，为globalDomain或<a href="../Common/mstxDomainCreateA.md">mstxDomainCreateA</a>返回的句柄。</p>
<p id="zh-cn_topic_0000002215920417_p17135131418533"><a name="zh-cn_topic_0000002215920417_p17135131418533"></a><a name="zh-cn_topic_0000002215920417_p17135131418533"></a>数据类型：const char *。</p>
</td>
</tr>
<tr id="zh-cn_topic_0000002215920417_row18118485118"><td class="cellrowborder" valign="top" width="28.65286528652865%" headers="mcps1.2.4.1.1 "><p id="zh-cn_topic_0000002215920417_p17725843815"><a name="zh-cn_topic_0000002215920417_p17725843815"></a><a name="zh-cn_topic_0000002215920417_p17725843815"></a>heap</p>
</td>
<td class="cellrowborder" valign="top" width="26.72267226722672%" headers="mcps1.2.4.1.2 "><p id="zh-cn_topic_0000002215920417_p1920117129516"><a name="zh-cn_topic_0000002215920417_p1920117129516"></a><a name="zh-cn_topic_0000002215920417_p1920117129516"></a>输入</p>
</td>
<td class="cellrowborder" valign="top" width="44.62446244624462%" headers="mcps1.2.4.1.3 "><p id="zh-cn_topic_0000002215920417_p15419387397"><a name="zh-cn_topic_0000002215920417_p15419387397"></a><a name="zh-cn_topic_0000002215920417_p15419387397"></a>heap为需要注销内存池的句柄，为<a href="../Mem/mstxMemHeapRegister.md">mstxMemHeapRegister</a>的返回值。</p>
<pre class="screen" id="zh-cn_topic_0000002215920417_screen977616221627"><a name="zh-cn_topic_0000002215920417_screen977616221627"></a><a name="zh-cn_topic_0000002215920417_screen977616221627"></a>struct mstxMemHeap_st;
typedef struct mstxMemHeap_st mstxMemHeap_t; 
typedef mstxMemHeap_t* mstxMemHeapHandle_t;</pre>
</td>
</tr>
</tbody>
</table>

**返回值说明<a id="zh-cn_topic_0000002215920417_section16621124213476"></a>**

无

**调用示例<a id="zh-cn_topic_0000002215920417_section7800053122316"></a>**

```cpp
mstxMemHeapDesc_t heapDesc{};
mstxMemHeapHandle_t memPool = mstxMemHeapRegister(globalDomain, &heapDesc); // 注册内存池
...
mstxMemHeapUnregister(globalDomain, memPool);                        // 注销内存池
```
