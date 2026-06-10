# msOpGen 常见问题

<br>

## 编译报错：fatal error: aclnn_xxx.h: No such file or directory

**问题现象**

编译调用算子的程序时，提示找不到 `aclnn_xxx.h` 头文件。

**原因分析**

算子部署时，头文件未正确安装到 `op_api/include` 目录。常见原因包括：
- 环境变量 `ASCEND_CUSTOM_OPP_PATH` 值不正确
- 存在多个以冒号分隔的路径，但头文件仅拷贝到了第一个路径

**解决方案**

1. 删除环境变量：`unset ASCEND_CUSTOM_OPP_PATH`
2. 重新部署算子包：`./build_out/custom_opp_*.run`
3. 确认已追加动态库路径：`export LD_LIBRARY_PATH=${ASCEND_OPP_PATH}/vendors/customize/op_api/lib:$LD_LIBRARY_PATH`

## 编译时提示 soc_version 不匹配

**问题现象**

创建算子工程或编译时提示芯片型号（soc_version）配置错误。

**解决方案**

1. 执行 `npu-smi info` 查询 Chip Name
2. 将 `-c ai_core-Ascend<Chip_Name>` 改为正确值
3. 注意 `ai_core` 与芯片型号之间用中划线 `-` 连接，例如：`ai_core-ascend910b`

## 运行报错：aclrtSetDevice failed

**问题现象**

执行算子调用程序时提示 `aclrtSetDevice failed. ERROR: xxxxxx`。

**原因分析**

可能原因包括：
- NPU 设备繁忙或硬件故障
- `/dev/hisi_hdc` 设备异常（如容器内未成功挂载、缺乏访问权限）
- 驱动/固件版本不匹配
- 系统资源（如内存）不足

**解决方案**

1. 使用 `npu-smi info` 检查 NPU 状态
2. 尝试切换 NPU 设备：通过 `-d <device_id>` 指定其他空闲设备
3. 容器环境中确认 `--device=/dev/davinciX` 已正确挂载
4. 检查驱动安装是否正确，参考《[CANN 软件安装指南](https://www.hiascend.com/document/detail/zh/CANNCommunityEdition/83RC1/softwareinst/instg/instg_0000.html)》
5. 错误码详见《[ACL错误码表](https://www.hiascend.com/document/detail/zh/canncommercial/83RC1/API/appdevgapi/aclcppdevg_03_1345.html)》

## 运行结果全为 0 或随机值

**问题现象**

算子执行完成但输出结果与预期不符，全部为 0 或包含随机值。

**原因分析**

常见原因包括：
- Kernel 侧代码中 EnQue/DeQue 流水线同步错误
- DataCopy 的数据长度（repeatTimes）与实际数据量不匹配
- Tiling 分块计算参数（totalLength、tileNum）有误

**解决方案**

1. 检查 `op_kernel/*.cpp` 中每个 `AllocTensor` 是否都有对应的 `FreeTensor`
2. 确认 `EnQue` 和 `DeQue` 成对调用且顺序正确
3. 验证 Tiling 参数传递是否正确
4. 可使用 msOpST 工具进行精度对比验证

## 算子包部署时提示权限不足

**问题现象**

执行 `.run` 算子安装包时提示权限不足。

**解决方案**

1. 使用 `--install-path=<path>` 指定有写权限的自定义安装目录
2. 执行 `source <path>/vendors/<vendor_name>/bin/set_env.bash` 使环境生效
3. 或联系 CANN 安装用户修改 `vendors` 目录权限

## 算子部署后未生效

**问题现象**

算子包已部署但在程序中仍找不到算子。

**解决方案**

1. 确认 `.run` 包执行成功（无错误输出）
2. 检查 `ASCEND_CUSTOM_OPP_PATH` 环境变量是否包含正确的部署路径
3. 检查 `opp/vendors/config.ini` 中的 `load_priority` 配置
4. 指定目录安装时需执行 `source <path>/vendors/<vendor_name>/bin/set_env.bash`
