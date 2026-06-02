# **Typical Cases of MindStudio Ops Generator**

## Ascend C Custom Operator Development Practice <a id="ZH-CN_TOPIC_0000002495336760"></a>

Explains how to use the msOpGen tool to generate, build, and deploy an Ascend C custom operator project, and how to use the msOpST tool to test the functions of the operator.

**Prerequisites**

You have prepared for using the msOpGen tool by referring to "Preparations" in [MindStudio Ops Generator User Guide](../user_guide/msopgen_user_guide.md).

**Procedure**

1. Prepare the operator prototype file by referring to the following JSON file. The MatmulCustom operator is used as an example:

    ```json
    [
        {
            "op": "MatmulCustom",
            "language": "cpp",
            "input_desc": [
                {
                    "name": "a",
                    "param_type": "required",
                    "format": [
                        "ND"
                    ],
                    "type": [
                        "float16"
                    ]
                },
                {
                    "name": "b",
                    "param_type": "required",
                    "format": [
                        "ND"
                    ],
                    "type": [
                        "float16"
                    ]
                },
                {
                    "name": "bias",
                    "param_type": "required",
                    "format": [
                        "ND"
                    ],
                    "type": [
                        "float"
                    ]
                }
            ],
            "output_desc": [
                {
                    "name": "c",
                    "param_type": "required",
                    "format": [
                        "ND"
                    ],
                    "type": [
                        "float"
                    ]
                }
            ]
        }
    ]
    ```

2. Use the msOpGen tool to run the following command to generate an operator project:

    > [!NOTE]NOTE  
    > The msOpGen tool generates only an empty operator project template. You need to add operators. For details, see "Operator Implementation" > "Project-based Operator Development" in [Ascend C Operator Development Guide](https://www.hiascend.com/document/detail/zh/canncommercial/83RC1/opdevg/Ascendcopdevg/atlas_ascendc_10_0059.html).

    ```sh
    msopgen gen -i MatmulCustom.json -f tf -c ai_core-Ascendxxxyy -lan cpp -out MatmulCustom
    ```

3. After the command is executed, the following operator project directory is generated in the specified directory.

    ```tex
    MatmulCustom/
    ├── build.sh         // Compilation entry script
    ├── CMakeLists.txt   // CMakeLists.txt script of the operator project
    ├── CMakePresets.json // Compilation configuration items
    ├── framework        // Directory for storing the implementation file of the operator plugin. The generation of single-operator model files does not depend on the operator plugin and can be ignored.
    ├── op_host                      // Implementation file on the host.
    │   ├── matmul_custom.cpp         // Content file for operator prototype registration, shape derivation, information library, and tiling implementation.
    │   ├── CMakeLists.txt
    ├── op_kernel                   // Implementation file on the kernel
    │   ├── CMakeLists.txt   
    │   ├── matmul_custom.cpp        // Operator implementation file
    │   ├── matmul_custom_tiling.h    // Operator tiling definition file
    ```

4. Build the operator project.

    ```sh
    ./build.sh
    ```

5. Deploy the custom OPP.
    - Run the following command to deploy the operator on CANN:

        ```sh
        ./build_out/custom_opp_<target_os>_<target_architecture>.run
        ```

    - Run the following command to deploy the operator to a custom path. `xxx/MatmulCustom/installed` is used as an example.

        ```sh
        ./build_out/custom_opp_<target_os>_<target_architecture>.run --install-path="xxx/MatmulCustom/installed" 
        ```

6. <a id="zh-cn_topic_0000001979357392_li2121117163612"></a>Run the following command to generate ST case: Replace `xxx` with the actual project path.

    ```sh
    msopst create -i "xxx/MatmulCustom/op_host/matmul_custom.cpp" -out ./st
    ```

7. Perform ST.
    1. Configure the following environment variables according to the CANN package installation path:

        ```sh
        export DDK_PATH=${INSTALL_DIR}
        export NPU_HOST_LIB=${INSTALL_DIR}/{arch-os}/devlib
        ```

    2. Run the following command to perform ST and save the test result to the specified path: `xxx.json` is the test case obtained in [Step 6](#zh-cn_topic_0000001979357392_li2121117163612).

        ```sh
        msopst run -i ./st/xxx.json -soc Ascendxxxyy -out ./st/out  
        ```

## msOpST Test Case Definition File <a id="ZH-CN_TOPIC_0000002539685293"></a>

- The following describes the Less operator's test case definition file (`Less\_case.json`).

    ```json
    [
        {
            "case_name": "Test_Less_001",       // Test case name
            "op": "Less",                       // Operator type
            "input_desc": [                     // Operator input description
                {                               // The first input
                    "format": ["ND"],            
                    "type": ["int32","float"],
                    "shape": [12,32],
                    "data_distribute": [       // Distribution mode selected for test data generation
                        "uniform"
                    ],
                    "value_range": [      // Value range of the input
                        [
                            1.0,
                            384.0
                        ]
                    ]
                },
                {                                // The second input
                    "format": ["ND"],
                    "type": ["int32","float"],
                    "shape": [12,32],
                    "data_distribute": [
                        "uniform"
                    ],
                    "value_range": [
                        [
                            1.0,
                            384.0
                        ]
                    ]
                }
            ],
            "output_desc": [                    // Operator output description
                {
                    "format": ["ND"],
                    "type": ["bool","bool"],
                    "shape": [12,32]
                }
            ]
        },
        {
            "case_name": "Test_Less_002",
            "op": "Less",
            "input_desc": [
                {                               
                 ...
                },
                {                   
                 ... 
                }
            ],
            "output_desc": [
                {
                  ...
                }
            ]
        }
    ]
    ```

- If the operator has attributes, the test case definition file is as follows:

    ```json
    [
        {
            "case_name":"Test_Conv2D_001",        // Test case name
            "op": "Conv2D",                      // Operator type, which is unique
            "input_desc": [            // Input description of the operator
                {                     // The first input
                    "format": [      // User-defined input tensor format
                        "ND",
                        "NCHW"
                    ],
                    "type": [         // Input data types
                        "float",
                        "float16"
                    ],
                    "shape": [8,512,7,7],     // User-defined shape of the input tensor
                    "data_distribute": [            // Distribution mode selected for test data generation
                        "uniform"                 
                    ],
                    "value_range": [      // Value range of the input
                        [
                            0.1,
                            200000.0
                        ]
                    ]
                },
                {                     // The second input
                    "format": [
                        "ND",
                        "NCHW"
                    ],
                    "type": [
                        "float",
                        "float16"
                    ],
                    "shape": [512,512,3,3],
                    "data_distribute": [
                        "uniform"
                    ],
                    "value_range": [
                        [
                            0.1,
                            200000.0
                        ]
                    ]
                }
            ],  
            "output_desc": [                       // (Required) The same as the input tensor description
                {
                    "format": [
                        "ND",
                        "NCHW"
                    ],
                    "type": [
                        "float",
                        "float16"
                    ],
                    "shape": [8,512,7,7]
                }
            ],
            "attr": [                           // Operator attributes
                {
                    "name": "strides",          // Attribute name
                    "type": "list_int",         // Attribute data type
                    "value": [1,1,1,1]          // Attribute value, which matches the configured type
                },
               {
                    "name": "pads",
                    "type": "list_int",
                    "value": [1,1,1,1]
                },
                {
                    "name": "dilations",
                    "type": "list_int",
                    "value": [1,1,1,1]
                }
    
            ]
        }
    ]
    ```

- If you need to specify an input, for example, to specify the `axes` parameter of the ReduceSum operator, the test case definition file is as follows:

    ```json
    [
        {
            "case_name": "Test_ReduceSum_001",
            "op": "ReduceSum",
            "input_desc": [
                {
                    "format": ["ND"],
                    "type": ["int32"],         // If the value needs to be set, only one data type can be specified per test case.
                    "shape": [3,6,3,4],
                    "data_distribute": [
                        "uniform"
                    ],
                    "value_range": [
                        [
                            -384,
                            384
                        ]
                    ]
                },
            {
            "format": ["ND"],
                    "type": ["int32"],
                    "shape": [2],
                    "data_distribute": [
                        "uniform"
                    ],
                    "value_range": [
                        [
                            -3,
                            1
                        ]
                    ],
            "value":[0,2]            // Configure a specific value, which must match that of shape.
                }
        ],
        "output_desc": [
                {
                    "format": ["ND"],
                    "type": ["int32"],
                    "shape": [6,4]
                }
            ],
        "attr":[
            {
            "name":"keep_dims",
            "type":"bool",
            "value":false
            }
        ]
        }
    ]
    ```

- If `type` of an operator is set to `data_type`, the test case definition file is as follows:

    ```json
    [
        {
        "case_name": "Test_ArgMin_001",
            "op": "ArgMin",
            "input_desc": [
                {
                ...
                },
            {
                ...
                }
        ],
        "output_desc": [
                {
                ...
                }
            ],
        "attr":[
            {
            "name":"dtype",
            "type":"data_type",
            "value":"int64"
            }
        ]
        }
    ]
    ```

- The following is an example operator that allows an uncertain number of inputs (dynamic multi-input operator).

    The following uses the AddN operator as an example. If the value of attribute `N` is `3`, configure three inputs with names `x0`, `x1`, and `x2`. That is, the number of inputs must match the value of attribute `N`.

    ```json
    [
        {
            "op": "AddN",
            "input_desc": [
                {
            "name":"x0",
                    "format": "NCHW",
                    "shape": [1,3,166,166],
                    "type": "float32"
                },
                {
            "name":"x1",
                    "format": "NCHW",
                    "shape": [1,3,166,166],
                    "type": "int32"
                },
                {
            "name":"x2",
                    "format": "NCHW",
                    "shape": [1,3,166,166],
                    "type": "float32"
                }
            ],
            "output_desc": [
                {
                    "format": "NCHW",
                    "shape": [1,3,166,166],
                    "type": "float32"
                }
            ],
            "attr": [
                {
                    "name": "N",
                    "type": "int",
                    "value": 3
                }
            ]
        }
    ]
    ```

- If an input of the operator is a constant, the test case definition file is as follows:

    ```json
    [
        {
            "case_name":"Test_OpType_001", 
            "op": "OpType", 
            "input_desc": [            
                {                     
                    "format": ["ND"],
                    "type": ["int32"],
                    "shape": [1], 
                    "is_const":true,           // The input is a constant.
                    "data_distribute": [            
                        "uniform"                 
                    ],
                    "value":[11],              // Constant value
                    "value_range": [           // Set both min_value and max_value to constants.
                        [
                            11,
                            11
                        ]
                    ]
                },
                {                     
                      ...
                }
            ],  
            "output_desc": [                     
                {
                    ...
                }
            ]
        }
    ]
    ```

- If the data types of the operator inputs and outputs are complex numbers, the test case definition file is as follows:

    ```json
    [
       {
            "case_name": "Test_ReduceSum_001",
            "op": "ReduceSum",
            "input_desc": [
                {
                    "format": ["ND"],
                    "type": [
                        "complex64",    // The input is of the complex type.
                        "complex128"    // The input is of the complex type.
                            ],
                    "shape": [3,6],
                    "data_distribute": [
                        "uniform"
                    ],
                    "value_range": [ // Value range of the real part
                        [
                            1,
                            10
                        ]
                    ]
                },
             {
                 "format": ["ND"],
                 "type": [
                         "int32",
                         "int64"],
                 "shape": [1],
                 "data_distribute": [
                        "uniform"
                    ],
                 "value_range": [
                        [
                            1,
                            1
                        ]
                    ]
                }
            ],
             "output_desc": [
                {
                    "format": ["ND"],
                    "type": [
                        "complex64",    // The input is of the complex type.
                        "complex128"    // The input is of the complex type.
                            ],
                    "shape": [3]
                }
            ],
            "attr":[
              {
                   "name":"keep_dims",
                   "type":"bool",
                   "value":false
              }
           ]
        }
    ]
    ```
