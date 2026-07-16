# MindStudio Tools Extension Library接口文档

本节介绍MindStudio Tools Extension Library（工具扩展接口库，msTX）打点接口。可以自定义采集时间段或者关键函数的开始和结束时间点，识别关键函数或迭代等信息，对性能和算子问题快速定界。

默认情况下msTX API无任何功能，需要在用户应用程序中调用msTX API后，根据不同场景使能msTX打点功能，例如使用msopprof命令行采集时配置--mstx=on、使用AscendCL API采集时配置ACL_PROF_MSPROFTX以及Ascend PyTorch Profiler接口采集时配置mstx=True等。

- 库文件libms_tools_ext.so路径：**${INSTALL_DIR}**/lib64/。
- 使用头文件编译时，用户程序编译时需链接dl库。头文件ms_tools_ext.h路径：**${INSTALL_DIR}**/include/mstx。

`${INSTALL_DIR}`请替换为CANN软件安装后文件存储路径。以root用户安装为例，安装后文件默认存储路径为：`/usr/local/Ascend/cann`。

**接口列表<a id="section6371427124715"></a>**

**表 1**  MindStudio mstx接口列表

|接口名称|功能简介|
|--|--|
|[mstxGetToolId](./Common/mstxGetToolId.md)|用于获取当前劫持mstx接口的工具ID。|
|[mstxMarkA](./Common/mstxMarkA.md)|标识瞬时事件。|
|[mstxRangeStartA](./Common/mstxRangeStartA.md)|标识时间段事件的开始。|
|[mstxRangeEnd](./Common/mstxRangeEnd.md)|标识时间段事件的结束。|
|[mstxDomainCreateA](./Common/mstxDomainCreateA.md)|创建自定义domain。|
|[mstxDomainDestroy](./Common/mstxDomainDestroy.md)|销毁指定的domain，销毁后的domain不能再次使用，需要重新创建。|
|[mstxDomainMarkA](./Common/mstxDomainMarkA.md)|在指定的domain内，标记瞬时事件。|
|[mstxDomainRangeStartA](./Common/mstxDomainRangeStartA.md)|在指定的domain内，标识时间段事件的开始。|
|[mstxDomainRangeEnd](./Common/mstxDomainRangeEnd.md)|在指定的domain内，标识时间段事件的结束。|
|[mstxMemHeapRegister](./Mem/mstxMemHeapRegister.md)|注册内存池。|
|[mstxMemRegionsRegister](./Mem/mstxMemRegionsRegister.md)|注册内存池二次分配。|
|[mstxMemRegionsUnregister](./Mem/mstxMemRegionsUnregister.md)|注销内存池二次分配。|
|[mstxMemHeapUnregister](./Mem/mstxMemHeapUnregister.md)|注销内存池时，与之关联的Regions将一并被注销。|
|[mstxMemPermissionsAssign](./Mem/mstxMemPermissionsAssign.md)|为虚拟内存区间指定权限|
