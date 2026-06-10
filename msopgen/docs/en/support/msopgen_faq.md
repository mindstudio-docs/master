# msOpGen FAQ

<br>

## Compilation Error: fatal error: aclnn_xxx.h: No such file or directory

**Symptom**

When compiling a program that invokes an operator, the `aclnn_xxx.h` header file cannot be found.

**Cause Analysis**

The header file was not correctly installed to the `op_api/include` directory during operator deployment. Common causes include:
- An incorrect `ASCEND_CUSTOM_OPP_PATH` environment variable
- Multiple colon-separated paths where the header file was only copied to the first path

**Solution**

1. Clear the environment variable: `unset ASCEND_CUSTOM_OPP_PATH`
2. Redeploy the operator package: `./build_out/custom_opp_*.run`
3. Verify the library path: `export LD_LIBRARY_PATH=${ASCEND_OPP_PATH}/vendors/customize/op_api/lib:$LD_LIBRARY_PATH`

## Compilation Error: soc_version Mismatch

**Symptom**

When creating or compiling an operator project, a chip model (soc_version) configuration error is reported.

**Solution**

1. Run `npu-smi info` to query the Chip Name
2. Change `-c ai_core-Ascend<Chip_Name>` to the correct value
3. Note that `ai_core` and the chip model are separated by a dash `-`, e.g. `ai_core-ascend910b`

## Runtime Error: aclrtSetDevice failed

**Symptom**

When executing an operator invocation program, `aclrtSetDevice failed. ERROR: xxxxxx` is displayed.

**Cause Analysis**

Possible causes include:
- NPU device busy or hardware failure
- `/dev/hisi_hdc` device issue (not mounted in container, insufficient permissions)
- Driver/firmware version mismatch
- Insufficient system resources (memory, etc.)

**Solution**

1. Run `npu-smi info` to check NPU status
2. Try switching NPU devices via `-d <device_id>`
3. In container environments, verify that `--device=/dev/davinciX` is correctly mounted
4. Check the driver installation. See [CANN Software Installation Guide](https://www.hiascend.com/document/detail/zh/CANNCommunityEdition/83RC1/softwareinst/instg/instg_0000.html)
5. See [ACL Error Code Reference](https://www.hiascend.com/document/detail/zh/canncommercial/83RC1/API/appdevgapi/aclcppdevg_03_1345.html) for error code details

## Output Is All Zeros or Random Values

**Symptom**

The operator execution completes but the output differs from the expected result — all zeros or random values.

**Cause Analysis**

Common causes include:
- Pipeline synchronization errors in EnQue/DeQue in kernel-side code
- DataCopy length (repeatTimes) mismatch with actual data size
- Incorrect Tiling block computation parameters (totalLength, tileNum)

**Solution**

1. Check that every `AllocTensor` in `op_kernel/*.cpp` has a corresponding `FreeTensor`
2. Verify that `EnQue` and `DeQue` are called in matching pairs with correct order
3. Validate Tiling parameter passing
4. Use the msOpST tool for precision comparison validation

## Permission Denied During Operator Package Deployment

**Symptom**

Permission denied error when executing the `.run` operator installation package.

**Solution**

1. Use `--install-path=<path>` to specify a writable custom installation directory
2. Run `source <path>/vendors/<vendor_name>/bin/set_env.bash` to apply the changes
3. Or contact the CANN installation user to modify the `vendors` directory permissions

## Operator Not Found After Deployment

**Symptom**

The operator package has been deployed but the operator cannot be found in the program.

**Solution**

1. Confirm the `.run` package executed successfully (no error output)
2. Check that the `ASCEND_CUSTOM_OPP_PATH` environment variable contains the correct deployment path
3. Check the `load_priority` configuration in `opp/vendors/config.ini`
4. When installing to a custom path, run `source <path>/vendors/<vendor_name>/bin/set_env.bash`
