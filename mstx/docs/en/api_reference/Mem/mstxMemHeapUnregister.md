# mstxMemHeapUnregister<a id="mstxMemHeapUnregister"></a>

**Supported Products<a id="section8178181118225"></a>**

|Product|Supported|
|--|:-:|
|Ascend 910_95 AI Processors|√|
|Atlas A3 training products/Atlas A3 inference products|√|
|Atlas A2 training products/Atlas A2 inference products|√|
|Atlas 200I/500 A2 inference products|√|
|Atlas inference products|√|
|Atlas training products|√|

**Function<a id="zh-cn_topic_0000002215920417_section20806203412478"></a>**

When a memory pool is unregistered, the regions associated with it are also unregistered.

**Prototype<a id="zh-cn_topic_0000002215920417_section1121883194711"></a>**

```python
void mstxMemHeapUnregister(mstxDomainHandle_t domain, mstxMemHeapHandle_t heap)
```

**Parameter Description<a id="zh-cn_topic_0000002215920417_section11506138144714"></a>**

**Table 1** Parameter description

<a name="zh-cn_topic_0000002215920417_table827101275518"></a>
<table><thead align="left"><tr id="zh-cn_topic_0000002215920417_row429121265517"><th class="cellrowborder" valign="top" width="28.65286528652865%" id="mcps1.2.4.1.1"><p id="zh-cn_topic_0000002215920417_p1329121214558"><a name="zh-cn_topic_0000002215920417_p1329121214558"></a><a name="zh-cn_topic_0000002215920417_p1329121214558"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="26.72267226722672%" id="mcps1.2.4.1.2"><p id="zh-cn_topic_0000002215920417_p10230141454318"><a name="zh-cn_topic_0000002215920417_p10230141454318"></a><a name="zh-cn_topic_0000002215920417_p10230141454318"></a>Input/Output</p>
</th>
<th class="cellrowborder" valign="top" width="44.62446244624462%" id="mcps1.2.4.1.3"><p id="zh-cn_topic_0000002215920417_p83121275519"><a name="zh-cn_topic_0000002215920417_p83121275519"></a><a name="zh-cn_topic_0000002215920417_p83121275519"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="zh-cn_topic_0000002215920417_row1131131265511"><td class="cellrowborder" valign="top" width="28.65286528652865%" headers="mcps1.2.4.1.1 "><p id="zh-cn_topic_0000002215920417_p7669321185110"><a name="zh-cn_topic_0000002215920417_p7669321185110"></a><a name="zh-cn_topic_0000002215920417_p7669321185110"></a>domain</p>
</td>
<td class="cellrowborder" valign="top" width="26.72267226722672%" headers="mcps1.2.4.1.2 "><p id="zh-cn_topic_0000002215920417_p723015144436"><a name="zh-cn_topic_0000002215920417_p723015144436"></a><a name="zh-cn_topic_0000002215920417_p723015144436"></a>Input</p>
</td>
<td class="cellrowborder" valign="top" width="44.62446244624462%" headers="mcps1.2.4.1.3 "><p id="zh-cn_topic_0000002215920417_p3243153110413"><a name="zh-cn_topic_0000002215920417_p3243153110413"></a><a name="zh-cn_topic_0000002215920417_p3243153110413"></a>domain is the domain to which the memory pool belongs. It can be globalDomain or the handle returned by <a href="../Common/mstxDomainCreateA.md">mstxDomainCreateA</a>.</p>
<p id="zh-cn_topic_0000002215920417_p17135131418533"><a name="zh-cn_topic_0000002215920417_p17135131418533"></a><a name="zh-cn_topic_0000002215920417_p17135131418533"></a>Data Type: const char *.</p>
</td>
</tr>
<tr id="zh-cn_topic_0000002215920417_row18118485118"><td class="cellrowborder" valign="top" width="28.65286528652865%" headers="mcps1.2.4.1.1 "><p id="zh-cn_topic_0000002215920417_p17725843815"><a name="zh-cn_topic_0000002215920417_p17725843815"></a><a name="zh-cn_topic_0000002215920417_p17725843815"></a>heap</p>
</td>
<td class="cellrowborder" valign="top" width="26.72267226722672%" headers="mcps1.2.4.1.2 "><p id="zh-cn_topic_0000002215920417_p1920117129516"><a name="zh-cn_topic_0000002215920417_p1920117129516"></a><a name="zh-cn_topic_0000002215920417_p1920117129516"></a>Input</p>
</td>
<td class="cellrowborder" valign="top" width="44.62446244624462%" headers="mcps1.2.4.1.3 "><p id="zh-cn_topic_0000002215920417_p15419387397"><a name="zh-cn_topic_0000002215920417_p15419387397"></a><a name="zh-cn_topic_0000002215920417_p15419387397"></a>heap is the handle of the memory pool to be unregistered. It is the return value of <a href="mstxMemHeapRegister.md">mstxMemHeapRegister</a>.</p>
<pre class="screen" id="zh-cn_topic_0000002215920417_screen977616221627"><a name="zh-cn_topic_0000002215920417_screen977616221627"></a><a name="zh-cn_topic_0000002215920417_screen977616221627"></a>struct mstxMemHeap_st;
typedef struct mstxMemHeap_st mstxMemHeap_t; 
typedef mstxMemHeap_t* mstxMemHeapHandle_t;</pre>
</td>
</tr>
</tbody>
</table>

**Returns<a id="zh-cn_topic_0000002215920417_section16621124213476"></a>**

None

**Example<a id="zh-cn_topic_0000002215920417_section7800053122316"></a>**

```py
mstxMemHeapDesc_t heapDesc{};
mstxMemHeapHandle_t memPool = mstxMemHeapRegister(globalDomain, &heapDesc); // Register Memory Poolter Memory Pool
...
mstxMemHeapUnregister(globalDomain, memPool);                        // Unregister Memory Poolister Memory Pool
```
