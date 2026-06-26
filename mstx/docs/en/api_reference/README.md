# **MindStudio Tools Extension Library API Reference**

This section describes the instrumentation APIs of the MindStudio Tools Extension Library (msTX). You can customize the collection period or the start and end timestamps of key functions to identify information such as key functions or iterations, enabling quick delimitation of performance and operator issues.

By default, the msTX APIs have no functionality. After calling the msTX APIs in your user application, you need to enable the msTX instrumentation feature according to different scenarios, for example, configuring `--mstx=on` when collecting data using the msprof command line, configuring `ACL_PROF_MSPROFTX` when collecting data using the AscendCL API, and configuring `mstx=True` when collecting data using the Ascend PyTorch Profiler interface.

- Library file `libms_tools_ext.so` path: `${INSTALL_DIR}/lib64/`.
- When compiling with the header file, the user program needs to link the dl library during compilation. Header file `ms_tools_ext.h` path: `${INSTALL_DIR}/include/mstx`.

Replace `${INSTALL_DIR}` with the file storage path after CANN software installation. For example, if you install CANN as the root user, the default file storage path is: `/usr/local/Ascend/cann`.

**API List<a id="section6371427124715"></a>**

**Table 1** MindStudio mstx API list

|API|Description|
|--|--|
|[mstxGetToolId](./Common/mstxGetToolId.md)|Obtains the ID of the tool currently intercepting mstx APIs.|
|[mstxMarkA](./Common/mstxMarkA.md)|Marks an instantaneous event.|
|[mstxRangeStartA](./Common/mstxRangeStartA.md)|Marks the start of a range event.|
|[mstxRangeEnd](./Common/mstxRangeEnd.md)|Marks the end of a range event.|
|[mstxDomainCreateA](./Common/mstxDomainCreateA.md)|Creates a custom domain.|
|[mstxDomainDestroy](./Common/mstxDomainDestroy.md)|Destroys a specified domain. A destroyed domain cannot be used again and must be re-created.|
|[mstxDomainMarkA](./Common/mstxDomainMarkA.md)|Marks an instantaneous event within a specified domain.|
|[mstxDomainRangeStartA](./Common/mstxDomainRangeStartA.md)|Marks the start of a range event within a specified domain.|
|[mstxDomainRangeEnd](./Common/mstxDomainRangeEnd.md)|Marks the end of a range event within a specified domain.|
|[mstxMemHeapRegister](./Mem/mstxMemHeapRegister.md)|Registers a memory pool.|
|[mstxMemRegionsRegister](./Mem/mstxMemRegionsRegister.md)|Registers secondary allocation of a memory pool.|
|[mstxMemRegionsUnregister](./Mem/mstxMemRegionsUnregister.md)|Unregisters secondary allocation of a memory pool.|
|[mstxMemHeapUnregister](./Mem/mstxMemHeapUnregister.md)|When a memory pool is unregistered, the associated regions are also unregistered.|
