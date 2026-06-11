# Security Statement

## System Security Hardening

You are advised to enable **address space layout randomization** (ASLR) level 2 in the system. Run the following command to enable it:

```sh
echo 2 > /proc/sys/kernel/randomize_va_space
```

## Running User Recommendations

1. All tools in this repository are designed to be installed and used with minimal permissions. For security reasons and to follow the principle of least privilege, do not use `root` or other privileged accounts to run any of the tools. You are advised to install and execute them as a regular user.

2. If a tool depends on CANN, use the CANN package installed by the same non-privileged user. After running the `source` command, do not modify environment variables in `set_env.sh`.

3. Before using any tool in this repository, you are advised to set `umask` to `0027` or a more restrictive value to ensure that generated files meet the minimum permission security requirements.

## File Permission Control

1. When providing input files to the tool as command inputs, it is recommended that the file owner match the process owner of the tool and that file permissions restrict write access for `group` and `others`. By default, tool files written to the drive are not writable by others. You can manually control the permissions for the generated files as needed.

2. Proper permission control is essential during installation and use. For details, see the following table.

## File Permission Reference

| Type                              | Maximum Linux Permission|
| ---------------------------------- | ------------------- |
| Home directory                        | 750 (rwxr-x---)   |
| Program files (including scripts and libraries)    | 550 (r-xr-x---)   |
| Program file directory                      | 550 (r-xr-x---)   |
| Configuration files                          | 640 (rw-r-----)   |
| Configuration file directory                      | 750 (rwxr-x---)   |
| Log files (recorded or archived)    | 440 (r--r-----)   |
| Log files (being recorded)                | 640 (rw-r-----)   |
| Log file directory                      | 750 (rwxr-x---)   |
| Debug files                         | 640 (rw-r-----)   |
| Debug file directory                     | 750 (rwxr-x---)   |
| Temporary file directory                      | 750 (rwxr-x---)   |
| Maintenance and upgrade file directory                  | 770 (rwxrwx---)   |
| Service data files                      | 640 (rw-r-----)   |
| Service data file directory                  | 750 (rwxr-x---)   |
| Key components, private keys, certificates, and ciphertext file directory| 700 (rwx------)   |
| Key components, private keys, certificates, and ciphertext files    | 600 (rw-------)   |
| APIs and scripts for encryption and decryption            | 500 (r-x------)   |

## Vulnerability Security Statement

For details, see [MindStudio Vulnerability Handling Procedure](./vulnerability_handling_procedure.md).

## Data Security

During the use of this tool, certain code-line-related features may access the user's operator code. If the operator code is confidential and must not be leaked, you should delete the corresponding deliverables promptly after use to prevent unnecessary information disclosure.

## Build Security

This tool supports source code compilation and installation. During compilation, third-party dependencies may be downloaded and build shell scripts executed, resulting in temporary program files and build directories. You may control permissions on files within the source code directory as needed to mitigate security risks. During the build process, you may also modify build scripts as necessary to avoid related security risks and ensure the security of build artifacts.

## Runtime Security

1. If an exception occurs during operation, the tool will exit the process and print error messages. This is expected behavior. You are advised to locate the specific cause of the error based on the error prompts, such as by viewing log files or result files generated during the collection and parsing process.

2. During tool usage, no security validation is performed on user input programs. You need to ensure the security of the programs yourself.

## Public Network Address Statement

The tool does not involve the use of public IP addresses.

## Public API Statement

This project is developed in Python with source code released. It is recommended to use the public APIs specified in the documentation. Directly calling source code APIs that are not explicitly disclosed is not recommended.

## Usage of Secure Functions

While unsecure functions are not forcibly disabled, you are advised to use their secure variants that explicitly take a buffer length parameter, for example, `memset_s` and `memcpy_s`.

## Communication Security Hardening

Remote communication is not involved. You are advised to use the tool in a secure network environment with a firewall or LAN, and pay attention to the communication security of other third-party software.

## Communication Matrix

External port communication is not involved.
