# `mstxMemHeapUnregister`<a id="mstxMemHeapUnregister"></a>

**Supported Products<a id="section8178181118225"></a>**

<!-- npu="950" id1 -->
- Ascend 950PR and 950DT products: supported
<!-- end id1 -->
<!-- npu="A3" id2 -->
- Atlas A3 products: supported
<!-- end id2 -->
<!-- npu="910b" id3 -->
- Atlas A2 products: supported
<!-- end id3 -->
<!-- npu="310b" id4 -->
- Atlas 200I/500 A2 inference products: supported
<!-- end id4 -->
<!-- npu="310p" id5 -->
- Atlas inference products: supported
<!-- end id5 -->
<!-- npu="910" id6 -->
- Atlas training products: supported
<!-- end id6 -->

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
