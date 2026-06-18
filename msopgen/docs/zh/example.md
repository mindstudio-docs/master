# **MindStudio Ops Generator典型案例**

## Ascend C自定义算子开发实践<a id="ZH-CN_TOPIC_0000002495336760"></a>

展示如何使用msOpGen工具进行Ascend C自定义算子的工程创建、编译和部署，并使用msOpST工具对Ascend C自定义算子进行功能测试。

**前提条件**

参考《[MindStudio Ops Generator工具用户指南](./msopgen_user_guide.md)》中的“使用前准备”章节，完成msOpGen工具的使用准备。

**操作步骤**

1. 参考以下json文件，准备算子原型文件（以MatmulCustom算子为例）。

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

2. 使用msOpGen工具执行以下命令，创建算子工程。

    > [!NOTE] 说明  
    > msOpGen工具仅生成空的算子工程模板，需要用户自行添加算子实现，具体请参见《[Ascend C算子开发指南](https://www.hiascend.com/document/detail/zh/canncommercial/83RC1/opdevg/Ascendcopdevg/atlas_ascendc_10_0059.html)》中的“算子实现\>工程化算子开发”章节。

    ```sh
    msopgen gen -i MatmulCustom.json -f tf -c ai_core-Ascendxxxyy -lan cpp -out MatmulCustom
    ```

3. 命令执行完毕，会在指定目录下生成如下算子工程目录。

    ```tex
    MatmulCustom/
    ├── build.sh         // 编译入口脚本
    ├── cmake 
    │   ├── xx.cmake
    │   ├── ....
    │   ├── util        // 算子工程编译所需脚本及公共编译文件存放目录
    ├── CMakeLists.txt   // 算子工程的CMakeLists.txt
    ├── CMakePresets.json // 编译配置项
    ├── framework        // 算子插件实现文件目录，单算子模型文件的生成不依赖算子适配插件，无需关注
    ├── op_host                      // Host侧实现文件
    │   ├── matmul_custom_tiling.h    // 算子tiling定义文件
    │   ├── matmul_custom.cpp         // 算子原型注册、shape推导、信息库、tiling实现等内容文件
    │   ├── CMakeLists.txt
    ├── op_kernel                   // Kernel侧实现文件
    │   ├── CMakeLists.txt   
    │   ├── matmul_custom.cpp        // 算子代码实现文件 
    ├── scripts                     // 自定义算子工程打包相关脚本所在目录
    ```

4. 执行算子工程编译。

    ```sh
    ./build.sh
    ```

5. 进行自定义算子包部署。
    - 执行以下命令，将算子部署到CANN：

        ```sh
        ./build_out/custom_opp_<target_os>_<target_architecture>.run
        ```

    - 执行以下命令，将算子部署到自定义路径（以_xxx_/MatmulCustom/installed为例）：

        ```sh
        ./build_out/custom_opp_<target_os>_<target_architecture>.run --install-path="xxx/MatmulCustom/installed" 
        ```

6. <a id="zh-cn_topic_0000001979357392_li2121117163612"></a>执行以下命令，生成ST测试用例。xxx需要修改为用户实际工程路径。

    ```sh
    msopst create -i "xxx/MatmulCustom/op_host/matmul_custom.cpp" -out ./st
    ```

7.  进行ST测试。
    1.  根据CANN包安装路径，配置以下环境变量：

        ```sh
        export DDK_PATH=${INSTALL_DIR}
        export NPU_HOST_LIB=${INSTALL_DIR}/{arch-os}/devlib
        ```

    2.  执行以下命令，进行ST测试，并将输出结果到指定路径。xxx.json为[步骤6](#zh-cn_topic_0000001979357392_li2121117163612)获得的测试用例：

        ```sh
        msopst run -i ./st/xxx.json -soc Ascendxxxyy -out ./st/out  
        ```

## msOpST测试用例定义文件<a id="ZH-CN_TOPIC_0000002539685293"></a>

- Less算子的测试用例定义文件“Less\_case.json”如下所示。

    ```json
    [
        {
            "case_name": "Test_Less_001",       //测试用例名称
            "op": "Less",                       //算子的类型
            "input_desc": [                     //算子输入描述
                {                               //第一个输入
                    "format": ["ND"],            
                    "type": ["int32","float"],
                    "shape": [12,32],
                    "data_distribute": [       //生成测试数据时选择的分布方式
                        "uniform"
                    ],
                    "value_range": [      //输入数据的取值范围
                        [
                            1.0,
                            384.0
                        ]
                    ]
                },
                {                                //第二个输入
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
            "output_desc": [                    //算子的输出
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

- 若算子包含属性，测试用例定义文件如下所示。

    ```json
    [
        {
            "case_name":"Test_Conv2D_001",        //测试用例名称
            "op": "Conv2D",                      // 算子的Type，唯一
            "input_desc": [            // 算子的输入描述
                {                     //算子的第一个输入
                    "format": [      //用户在此处配置待测试的输入Tensor的排布格式
                        "ND",
                        "NCHW"
                    ],
                    "type": [         // 输入数据支持的数据类型
                        "float",
                        "float16"
                    ],
                    "shape": [8,512,7,7],     // 输入Tensor的shape,用户需要自行修改
                    "data_distribute": [            //生成测试数据时选择的分布方式
                        "uniform"                 
                    ],
                    "value_range": [      // 输入数据值的取值范围
                        [
                            0.1,
                            200000.0
                        ]
                    ]
                },
                {                     //算子的第二个输入
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
            "output_desc": [                       //必选,含义同输入Tensor描述
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
            "attr": [                           // 算子的属性
                {
                    "name": "strides",          //属性的名称
                    "type": "list_int",         // 属性的支持的类型
                    "value": [1,1,1,1]          // 属性值,跟type的类型对应
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

- 若指定固定输入，例如ReduceSum的axes参数，测试用例定义文件如下所示。

    ```json
    [
        {
    	"case_name": "Test_ReduceSum_001",
            "op": "ReduceSum",
            "input_desc": [
                {
                    "format": ["ND"],
                    "type": ["int32"],         //若需要设置value,则每个用例只能测试一种数据类型
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
    		"value":[0,2]            //设置具体值,需要与shape对应
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

- 若算子属性的type为类型，测试用例定义文件如下所示。

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

- 若算子的输入个数不确定（动态多输入场景）。

    以AddN算子为例，属性“N”的取值为3，则需要配置3个输入描述，name分别为x0、x1、x2，即输入个数需要与属性“N”的取值匹配。

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

- 若算子的某个输入为常量，测试用例定义文件如下所示。

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
                    "is_const":true,           // 标识此输入为常量
                    "data_distribute": [            
                        "uniform"                 
                    ],
                    "value":[11],              //常量的值
                    "value_range": [           //min_value与max_value都配置为常量的值
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

- 若算子的输入输出类型为复数，测试用例定义文件如下所示。

    ```json
    [
       {
            "case_name": "Test_ReduceSum_001",
            "op": "ReduceSum",
            "input_desc": [
                {
                    "format": ["ND"],
                    "type": [
                        "complex64",    //输入类型为复数
                        "complex128"    //输入类型为复数
                            ],
                    "shape": [3,6],
                    "data_distribute": [
                        "uniform"
                    ],
                    "value_range": [ //实部取值范围
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
                        "complex64",    //输入类型为复数
                        "complex128"    //输入类型为复数
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

