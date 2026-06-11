# msTT Security Statement

## System Security Hardening

You are advised to enable **address space layout randomization** (ASLR) Level in the system. Run the following command to enable it:

    echo 2 > /proc/sys/kernel/randomize_va_space

## Runtime User Recommendations

For security and the principle of least privilege, the tools in this code repository should not be run using high-privilege accounts such as the **root**. You are advised to install and execute the tools as a regular user.

## File Permission Control

 1. In the default security mode, the msMonitor online monitoring and msProbe online pre-check functions require the directory containing the root certificate, server certificate, server private key file, and certificate revocation list file. You must ensure that the directory permission is 700 and the permissions for files such as certificates are 600.

 2. When providing input files to the tool, it is recommended that the file owner be the same as the tool process owner, and that the file permissions are not modifiable by others (including `group` and `others`). By default, files written to drive by the tool are not writable by `others`. You can control permissions for the generated files as needed.

 3. Permission control must be enforced during installation and usage. You are advised to configure settings according to the following **File Permission Reference** table.

**File Permission Reference**

| Type | Maximum Linux Permission |
| ---------------------------------- | ------------------- |
| Home directory | 750 (rwxr-x---) |
| Program files (including scripts and libraries) | 550 (r-xr-x---) |
| Program file directory | 550 (r-xr-x---) |
| Configuration files | 640 (rw-r-----) |
| Configuration file directory | 750 (rwxr-x---) |
| Log files (recorded or archived) | 440 (r--r-----) |
| Log files (being recorded) | 640 (rw-r-----) |
| Log file directory | 750 (rwxr-x---) |
| Debug files | 640 (rw-r-----) |
| Debug file directory | 750 (rwxr-x---) |
| Temporary file directory | 750 (rwxr-x---) |
| Maintenance and upgrade file directory | 770 (rwxrwx---) |
| Service data files | 640 (rw-r-----) |
| Service data file directory | 750 (rwxr-x---) |
| Key components, private keys, certificates, and ciphertext file directory | 700 (rwx------) |
| Key components, private keys, certificates, and encrypted ciphertext | 600 (rw-------) |
| APIs and scripts for encryption and decryption | 500 (r-x------) |

## Vulnerability Security Statement

The tb-graph-ascend tool depends on webpack-dev-server in the development state. Version 4.x has been identified as having known security vulnerabilities (CVE-2025-30359 and CVE-2025-30360). However, the final built release artifacts (production environment code/packages) do not contain webpack-dev-server or its related code, and users will not download this dependency library during use. Therefore, these vulnerabilities do not affect the security of the final application generated using this tool, nor will they be downloaded or triggered by end users. However, developers need to ensure the security of the development process themselves.

For details about the vulnerability handling mechanism, see [MindStudio Vulnerability Handling Procedure](mindstudio_vulnerability_handling_procedure.md).

## Data Security Statement

During tool usage, data needs to be loaded and saved. Some interfaces directly or indirectly use the risky module pickle, which may pose data risks, such as the torch.load interface. For details about specific risks, see [torch.load](https://pytorch.org/docs/main/generated/torch.load.html#torch.load).

## Build Security Statement

msMonitor and msProbe support source code compilation and installation. During compilation, dependent third-party libraries are downloaded and build shell scripts are executed. Temporary program files and build directories are generated during the compilation process. Users can manage permissions for files in the source code directory as needed to reduce security risks. During the build process, users can modify build scripts as needed to avoid related security risks, and pay attention to the security of the build results.

## Runtime Security Statement

1. When the tool loads a dataset, if the memory size of the loaded dataset exceeds the memory capacity limit, an error may occur and cause the process to exit unexpectedly. If the collection time is too long and the generated data exceeds the remaining drive space, an abnormal exit may occur.

2. When an exception occurs during operation, the tool exits the process and prints an error message, which is normal. You are advised to locate the specific cause of the error based on the error message, including viewing the log file and the result files generated during collection and parsing.

3. msProbe:

   Prerequisites: The Python source code of the object to be collected must be readable and executable so that public information such as the public call stack can be obtained.

   Usage scenario: When you need to perform model accuracy analysis, they can add the dump API of msProbe to the model training script, collect accuracy data while executing training, and directly output the accuracy data file after training is completed. The data file content includes the API data in the model, the model structure, and the stack information of API calls (so that when an API with an accuracy issue is located, the position of the API in the model can be quickly found).

    Risk warning: Using this function generates accuracy data locally. You must strengthen the protection of related accuracy data files. Use it only when model accuracy analysis is required, and disable it promptly after analysis is complete.

4. To avoid remote code injection attacks, if the `--trust-remote-code` parameter is involved, set it to False.

## Public IP Address Statement

[Public IP address information](public_ip_address.md) present in the configuration files and scripts of the msTT repository tools

## Public API Statement

The msTT project is jointly developed using C++ and Python. All provided external interfaces have been disclosed in the documentation. Official interfaces are provided only as Python interfaces. Dynamic libraries do not directly provide services. Exposed interfaces are for internal use and are not recommended for user use.

For scripting languages such as Python, the source code is released. You are advised use the public interfaces described in the documentation. Directly calling the source code of interfaces that are not explicitly disclosed is not recommended.

## Instructions for Using Security Functions

Insecure functions are not forcibly disabled, but it is recommended to use the `_s` secure versions that explicitly pass the buffer length as a parameter, such as `memset_s` and `memcpy_s`.

## Communication Security Hardening

**1. Security risk of native dynolog wildcard address listening**

**Background**: msMonitor integrates the open-source third-party library dynolog. msMonitor has adapted dynolog for NPU. The adapted file **msMonitor/dynolog_npu/dynolog/src/rpc/SimpleJsonServer.cpp** contains code for wildcard address listening. To ensure tool functionality and usability, the native dynolog wildcard address listening has not been modified yet.

**Risk**: The **dynolog/src/rpc/SimpleJsonServer.cpp** file of this library contains the functionality of wildcard address listening (bind to in6addr_any), posing a network exposure security risk. This security risk originates from the dynolog open-source third-party library.

**Risk mitigation measures**: In the default security mode, you need to provide the root certificate, server certificate, server private key file, client certificate, client private key file, and certificate revocation list file. You must ensure the validity and legitimacy of the provided certificate files. At the same time, you must ensure that the directory where the certificates are located has file permissions of 700 and the certificates and other files have file permissions of 600. You are advised to configure firewall mechanisms such as `iptables` to restrict network access to the RPC port.

**2. Model hierarchical visualization TensorBoard plugin**

**Background**: The model hierarchical visualization plugin (**plugins/tensorboard-plugins/tb_graph_ascend**) is developed and debugged based on the TensorBoard framework. After installing the plugin, you need to start TensorBoard to use it.

**Risk**: When starting TensorBoard, you can specify an IP address using `--host` or bind to all zeros using `--bind-all`. Since the hierarchical visualization plugin is only a plugin for TensorBoard, it cannot perform security hardening on the TensorBoard service itself. Users are advised to ensure environmental security when using it.

**Risk mitigation measures**: You are advised to bind `--host=127.0.0.1` or localhost during use and avoid starting with the root user as much as possible. If TensorBoard needs to be started on a non-localhost address for remote access scenarios, users are advised to ensure the security of the environment itself and protect it through network security hardening solutions, such as restricting client access using access control policies like iptables, or performing HTTPS hardening through reverse proxy tools like nginx.

## Communication Matrix

**Communication Matrix**

| No. | Repository | Function | Source Device | Source IP Address | Source Port | Destination Device | Destination IP Address | Destination Port<br/>(Listening) | Protocol | Port Description | Port Configuration | Listening Port Configurable (Yes/No) | Authentication Method | Encryption Mode | Plane | Version | Special Scenarios | Remarks |
|:---|:----------------------------| :------------------------ |:--------------------------|:------------------------------| :----- |:-------------------| :---------------------------- |:--------------| :--- |:---------------------------------------------------------------------|:---------|:-------------------| :------- | :------- |:--------|:--------|:-----| :--- |
| 1 | msMonitor | dyno and dynolog RPC communication | dyno client | IP of the server running the dyno client process | | Server where the dynolog server resides | IP address of the server where the dynolog server resides | 1778 | TCP | RPC communication | N/A | Yes | Certificate key | TLS | Service plane | All versions | None | |
| 2 | tensorboard-plugins, msProbe | TensorBoard backend frontend-backend communication | Machine where the TensorBoard browser is accessed | IP address of the machine where the TensorBoard browser is accessed | | Machine where the TensorBoard service resides | IP address of the server where the TensorBoard service resides | 6006 | HTTP | The TensorBoard backend is not part of the delivery scope. If you choose to use it, a port may be opened. The default port opened by TensorBoard is 6006. You can also specify other ports to open. | `--port` | Yes | | | Service plane | All versions | None | |

## Disclaimer

- This tool is intended solely for debugging and development. Users are responsible for any risks and should carefully review the following information:

  - [X] Data processing and deletion: Users are responsible for managing and deleting any data (including but not limited to dumped data) generated while using this tool. Users are advised to delete such data promptly after use to prevent information leakage.
  - [X] Data confidentiality and transmission: Users understand and agree not to share or transmit any data generated by this tool. Neither the tool nor its developers are responsible for any information leaks, data breaches, or other negative consequences.
  - [X] User input security: Users are responsible for the security of any commands they enter and for any risks or losses resulting from improper input. The tool and its developers are not liable for issues caused by incorrect command usage.
- Disclaimer scope: This disclaimer applies to all individuals and entities using this tool. By using the tool, you acknowledge and accept this statement and assume all risks and responsibilities arising from its use. If you do not agree, please stop using the tool immediately.
- Before using this tool, **please read and understand the preceding disclaimer**. If you have any questions, contact the developer.
