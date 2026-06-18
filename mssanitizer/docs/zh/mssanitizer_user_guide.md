# **MindStudio Sanitizer工具用户指南**

## 简介<a id="ZH-CN_TOPIC_0000002509517928"></a>

MindStudio Sanitizer（异常检测工具，msSanitizer）是一种基于AI处理器的工具，包含了单算子开发场景下的内存检测、竞争检测、未初始化检测和同步检测四个子功能。用户使用msOpST工具在真实的硬件环境中对算子的功能进行测试后，可根据实际测试情况选择是否使用msSanitizer工具进行异常检测。

- 内存检测：工具可以在用户开发算子的过程中，协助定位非法读写、多核踩踏、非对齐访问、内存泄漏以及非法释放等内存问题。同时工具也支持对CANN软件栈的内存检测，帮助用户定界软件栈内存异常发生的模块。
- 竞争检测：工具可以协助用户定位由于竞争风险可能导致的数据竞争问题，包含核内竞争和核间竞争问题。其中，核内竞争包含流水间竞争和流水内竞争。
- 未初始化检测：工具可以协助用户定位由于内存未初始化可能导致的脏数据读取问题。
- 同步检测：工具可以协助用户定位由于前序算子中的未配对同步指令导致的后续算子同步失败的问题。

> [!NOTE] 说明       
> msSanitizer工具不支持对多线程算子及使用了掩码的向量类计算指令进行检测。

## 使用前准备<a id="ZH-CN_TOPIC_0000002541157907"></a>

**环境准备<a id="section6797195245014"></a>**

进行算子开发之前，需要安装配套版本的CANN Toolkit开发套件包和ops算子包并配置CANN环境变量，请参见《[CANN 软件安装指南](https://www.hiascend.com/document/detail/zh/CANNCommunityEdition/83RC1/softwareinst/instg/instg_0000.html)》。本节不再给出安装示例。

**约束<a id="section160697141319"></a>**

- 出于安全性及权限最小化角度考虑，本代码仓中的工具均不应使用root等高权限账户进行操作，建议使用普通用户权限安装执行。
- 使用算子开发工具前，请确保执行用户的umask值大于等于0027，否则会造成获取的性能数据所在目录和文件权限过大。
- 使用算子工具前，请保证使用最小权限原则（如：禁止other用户可写，禁止666或777）。

- 不建议配置或运行其他用户目录下的自定义脚本，避免提权风险。
- 下载代码样例时，需执行以下命令指定分支版本。

    ```sh
    git clone https://gitee.com/ascend/samples.git -b master
    ```

**配置编译选项（可选）<a id="section1819973616410"></a>**

用户可根据需求自行选择是否添加编译选项，具体请参见[表1 编译场景介绍](#table146461578432)。

**表 1**  编译场景介绍

<a id="table146461578432"></a>
<table><thead align="left"><tr id="row164619764311"><th class="cellrowborder" valign="top" width="12.57%" id="mcps1.2.5.1.1"><p id="p68551813114319"><a id="p68551813114319"></a><a id="p68551813114319"></a>是否添加编译选项</p>
</th>
<th class="cellrowborder" valign="top" width="13.01%" id="mcps1.2.5.1.2"><p id="p17855213104311"><a id="p17855213104311"></a><a id="p17855213104311"></a>指令检测范围</p>
</th>
<th class="cellrowborder" valign="top" width="43.09%" id="mcps1.2.5.1.3"><p id="p08551131436"><a id="p08551131436"></a><a id="p08551131436"></a>异常检测范围</p>
</th>
<th class="cellrowborder" valign="top" width="31.330000000000002%" id="mcps1.2.5.1.4"><p id="p9855111324313"><a id="p9855111324313"></a><a id="p9855111324313"></a>适用场景</p>
</th>
</tr>
</thead>
<tbody><tr id="row66463704312"><td class="cellrowborder" valign="top" width="12.57%" headers="mcps1.2.5.1.1 "><p id="p1585620132439"><a id="p1585620132439"></a><a id="p1585620132439"></a>不添加</p>
</td>
<td class="cellrowborder" valign="top" width="13.01%" headers="mcps1.2.5.1.2 "><p id="p12856201364311"><a id="p12856201364311"></a><a id="p12856201364311"></a>与GM相关的搬运指令</p>
</td>
<td class="cellrowborder" valign="top" width="43.09%" headers="mcps1.2.5.1.3 "><a id="ul1385641310433"></a><a id="ul1385641310433"></a><ul id="ul1385641310433"><li>仅支持内存检测中的非法读写和非对齐访问。</li><li>异常报告中不显示调用栈信息。<div class="note" id="note1885611133438"><a id="note1885611133438"></a><a id="note1885611133438"></a><span class="notetitle"> 说明： </span><div class="notebody"><a id="ul1048722320242"></a><a id="ul1048722320242"></a><ul id="ul1048722320242"><li>该场景算子的优化等级需为<strong id="b332715273818"><a id="b332715273818"></a><a id="b332715273818"></a>O2</strong>，并保证算子链接阶段增加<strong id="b2919195823718"><a id="b2919195823718"></a><a id="b2919195823718"></a>-q</strong>选项，保留符号重定位信息，否则会导致检测功能失效。</li><li>该场景不适用于<span id="ph791462511154"><a id="ph791462511154"></a><a id="ph791462511154"></a><term id="zh-cn_topic_0000001312391781_term4363218112215"><a id="zh-cn_topic_0000001312391781_term4363218112215"></a><a id="zh-cn_topic_0000001312391781_term4363218112215"></a>Atlas 推理系列产品</term></span>。</li><li>该场景仅适用于算子内核调用符场景。</li></ul>
</div></div>
</li></ul>
</td>
<td class="cellrowborder" valign="top" width="31.330000000000002%" headers="mcps1.2.5.1.4 "><p id="p68561613184319"><a id="p68561613184319"></a><a id="p68561613184319"></a>该场景支持的功能上有限制，仅适用于对算子内存异常中的非法读写和非对齐访问异常的快速定界。</p>
</td>
</tr>
<tr id="row86462734319"><td class="cellrowborder" valign="top" width="12.57%" headers="mcps1.2.5.1.1 "><p id="p58561513144319"><a id="p58561513144319"></a><a id="p58561513144319"></a>添加</p>
</td>
<td class="cellrowborder" valign="top" width="13.01%" headers="mcps1.2.5.1.2 "><p id="p1985611354318"><a id="p1985611354318"></a><a id="p1985611354318"></a>全量指令</p>
</td>
<td class="cellrowborder" valign="top" width="43.09%" headers="mcps1.2.5.1.3 "><a id="ul885681384319"></a><a id="ul885681384319"></a><ul id="ul885681384319"><li>支持全量检测。</li><li>在编译选项中增加-g选项后，异常报告将会显示调用栈信息。</li></ul>
</td>
<td class="cellrowborder" valign="top" width="31.330000000000002%" headers="mcps1.2.5.1.4 "><p id="p16856101314314"><a id="p16856101314314"></a><a id="p16856101314314"></a>通过不添加编译选项的功能快速定位异常算子后，再添加编译选项对异常算子进行全量检测，具体操作请参见<a href="#section1587001013184">开启全量检测</a>。</p>
</td>
</tr>
</tbody>
</table>

**开启全量检测<a id="section1587001013184"></a>**

如需要开启全量检测，需要在算子代码的编译阶段增加编译选项，不同算子工程添加编译选项的位置不同，下面分别介绍[模板库场景](#li12181135152611)、[内核调用符场景](#li159191517103114)、[Triton算子调用场景](#li338910473313)和[msOpGen算子工程编译场景](#li710224318317)为例进行：

-   <a id="li12181135152611"></a>模板库场景

    修改模板库中的**examples/CMakeLists.txt**文件，新增`-g --cce-enable-sanitizer`编译选项。

    ```
    set(BISHENG_COMPILER_OPTIONS -g --cce-enable-sanitizer)
    ```

-   <a id="li159191517103114"></a>内核调用符场景
    1.  样例工程代码请参考[Link](https://gitee.com/ascend/samples/tree/8.0.RC2/operator/AddCustomSample/KernelLaunch/AddKernelInvocation)，执行以下命令，下载分支版本的样例代码。

        ```
        git clone https://gitee.com/ascend/samples.git -b 8.0.RC2
        ```

        > [!NOTE] 说明       
        > 此样例工程不支持Atlas A3 训练系列产品/Atlas A3 推理系列产品和昇腾910\_95 AI处理器。

    2.  进行算子代码编译，需添加以下编译选项：

        -   -g
        -   --cce-enable-sanitizer或--sanitizer

        编辑样例工程目录下的“cmake/npu/CMakeLists.txt”文件，参考核函数开发和运行验证的完整样例。

        ```
        target_compile_options(${smoke_testcase}_npu PRIVATE
                             -O2
                             -std=c++17
                             --cce-enable-sanitizer
                             -g
        )
        ```

        增加--cce-enable-sanitizer或--sanitizer选项代表使能异常检测。

        增加-g选项使编译器生成定位信息，将会在异常报告输出时打印异常发生的具体位置（文件名、行号以及调用栈等信息）。

        > [!NOTE] 说明       
        >-   --cce-enable-sanitizer和-O0同时开启的情况下，需要增加编译选项 --cce-ignore-always-inline=false。
        >-   添加-g编译选项会在生成的二进制文件中附带调试信息，建议限制带有调试信息的用户程序的访问权限，确保只有授权人员可以访问该二进制文件。
        >-   增加--cce-enable-sanitizer编译选项生成的算子二进制，需与msSanitizer工具配套使用。不建议单独使用该二进制，单独使用可能会导致不可预见的问题。
        >-   因**llvm-symbolizer**开源软件限制，调用栈的异常信息可能会获取失败。此时，用户可再次执行检测命令，就可以获取调用栈的异常信息。
        >-   目前昇腾910\_95 AI处理器不支持--cce-enable-sanitizer或--sanitizer以及-O0编译选项，用于添加-g kernel侧编译选项后，如算子中有异常信息，则工具会展示异常信息对应的调用栈信息。

    3.  链接阶段需增加target\_link\_options选项。
        -   编辑样例工程目录下的“cmake/npu/CMakeLists.txt”文件。

            ```
            target_link_options(${smoke_testcase}_npu PRIVATE
                --cce-fatobj-link
                --cce-enable-sanitizer
            )
            ```

        -   编辑样例工程目录下的“cmake/Modules/CMakeCCEInformation.cmake”文件。

            ```
            if(NOT CMAKE_CCE_LINK_EXECUTABLE)
              set(CMAKE_CCE_LINK_EXECUTABLE
                "<CMAKE_CCE_COMPILER> ${CMAKE_LIBRARY_CREATE_CCE_FLAGS} ${_CMAKE_COMPILE_AS_CCE_FLAG} <FLAGS> <CMAKE_CCE_LINK_FLAGS> <LINK_FLAGS> <OBJECTS> -o <TARGET> <LINK_LIBRARIES>${__IMPLICIT_LINKS}")
            endif()
            ```

    4.  启用msSanitizer检测工具时，需要加载NPU侧可执行文件_<kernel\_name\>_\_npu，该文件的获取可参考《Ascend C算子开发指南》中的“Kernel直调算子开发 \>[Kernel直调](https://www.hiascend.com/document/detail/zh/canncommercial/83RC1/opdevg/Ascendcopdevg/atlas_ascendc_10_0056.html)”章节。

-   <a id="li710224318317"></a>msOpGen算子工程编译场景
    1.  单击[Link](https://gitee.com/ascend/samples/tree/master/operator/ascendc/0_introduction/1_add_frameworklaunch/AddCustom)，在$\{git\_clone\_path\}/samples/operator/ascendc/0\_introduction/1\_add\_frameworklaunch目录下运行install.sh脚本，生成自定义算子工程。

        > [!NOTE] 说明       
        > 下载代码样例时，需执行以下命令指定分支版本。
        > ```
        > git clone https://gitee.com/ascend/samples.git -b master
        > ```

        ```
        bash install.sh -v Ascendxxxyy    # xxxyy为用户实际使用的具体芯片类型
        ```

    2.  切换至自定义算子工程目录。

        ```
        cd CustomOp
        ```

    3.  编辑样例工程目录下的“op\_kernel/CMakeLists.txt”文件，在编译选项中添加-sanitizer选项，具体请参考《MindStudio Ops Generator工具用户指南》中的“算子编译部署\>支持自定义编译选项”章节。

        ```
        add_ops_compile_options(ALL OPTIONS -sanitizer)
        ```

-   <a id="li338910473313"></a>Triton算子调用场景

    Triton算子采用Python语言进行开发，并且采用即时编译（JIT）方式来编译算子Kernel。在执行算子脚本前，需要配置以下环境变量支持全量检测。

    ```
    export TRITON_ENABLE_SANITIZER=1
    ```

**启动工具<a id="section19811114085517"></a>**

完成[环境准备](#section6797195245014)和[配置编译选项（可选）](#section1819973616410)后，请参见[启用内存检测](#zh-cn_topic_0000001820455825_section1371111444516)、[启用竞争检测](#zh-cn_topic_0000001773496140_section12419444163310)、[启用未初始化检测](#zh-cn_topic_0000001820455825_section1371111444516)和[同步检测](#同步检测)章节使能msSanitizer工具的相关功能。

> [!NOTE] 说明       
>异常报告具有以下级别：
>-   WARNING：此级别被定义为不确定性的风险，可能出现的异常现象由实际情况决定，如多核踩踏、内存分配未使用等。其中，多核踩踏风险涉及多个核对同一块内存的操作，高阶用户可以通过核间同步的手段来规避此风险，初级用户遇到此类异常，应该将其视为危险源。目前，多核踩踏的WARNING级别的报告仅能识别atomic类的核间同步信息。
>-   ERROR：最高严重级别的异常，涉及针对内存操作的确定性错误，如非法读写、内存泄漏、非对齐访问、内存未初始化、竞争异常等。强烈建议用户检查此严重级别的异常。

## 异常检测功能介绍<a id="ZH-CN_TOPIC_0000002541159389"></a> 

### 功能说明<a id="ZH-CN_TOPIC_0000002509519396"></a>

msSanitizer通过不同子功能提供了不同类型的异常检测功能，目前已支持的功能如下：

**表 1**  msSanitizer工具功能

<a id="zh-cn_topic_0000001691887174_table2520191519210"></a>
<table><thead align="left"><tr id="zh-cn_topic_0000001691887174_row17520215162117"><th class="cellrowborder" valign="top" width="24.13241324132413%" id="mcps1.2.4.1.1"><p id="zh-cn_topic_0000001691887174_p4521815102112"><a id="zh-cn_topic_0000001691887174_p4521815102112"></a><a id="zh-cn_topic_0000001691887174_p4521815102112"></a>使用场景</p>
</th>
<th class="cellrowborder" valign="top" width="18.201820182018203%" id="mcps1.2.4.1.2"><p id="zh-cn_topic_0000001691887174_p7521415172116"><a id="zh-cn_topic_0000001691887174_p7521415172116"></a><a id="zh-cn_topic_0000001691887174_p7521415172116"></a>使用说明</p>
</th>
<th class="cellrowborder" valign="top" width="57.66576657665766%" id="mcps1.2.4.1.3"><p id="zh-cn_topic_0000001691887174_p12521201513214"><a id="zh-cn_topic_0000001691887174_p12521201513214"></a><a id="zh-cn_topic_0000001691887174_p12521201513214"></a>使用示例</p>
</th>
</tr>
</thead>
<tbody><tr id="zh-cn_topic_0000001691887174_row1152171542120"><td class="cellrowborder" valign="top" width="24.13241324132413%" headers="mcps1.2.4.1.1 "><p id="zh-cn_topic_0000001691887174_p16149193723113"><a id="zh-cn_topic_0000001691887174_p16149193723113"></a><a id="zh-cn_topic_0000001691887174_p16149193723113"></a>算子内存检测</p>
</td>
<td class="cellrowborder" valign="top" width="18.201820182018203%" headers="mcps1.2.4.1.2 "><p id="zh-cn_topic_0000001691887174_p1452121582114"><a id="zh-cn_topic_0000001691887174_p1452121582114"></a><a id="zh-cn_topic_0000001691887174_p1452121582114"></a><a href="#内存检测">内存检测</a></p>
</td>
<td class="cellrowborder" valign="top" width="57.66576657665766%" headers="mcps1.2.4.1.3 "><p id="p122711722817"><a id="p122711722817"></a><a id="p122711722817"></a>msSanitizer支持内核调用符调用的<span id="zh-cn_topic_0000001691887174_ph74518512337"><a id="zh-cn_topic_0000001691887174_ph74518512337"></a><a id="zh-cn_topic_0000001691887174_ph74518512337"></a>Ascend C</span>算子（包括Vector、Cube算子和Mix融合算子）内存和竞争的检测，可参考<a href="#内存检测">内存检测</a>。</p>
</td>
</tr>
<tr id="zh-cn_topic_0000001691887174_row13521315132112"><td class="cellrowborder" valign="top" width="24.13241324132413%" headers="mcps1.2.4.1.1 "><p id="zh-cn_topic_0000001691887174_p20233184653111"><a id="zh-cn_topic_0000001691887174_p20233184653111"></a><a id="zh-cn_topic_0000001691887174_p20233184653111"></a>算子竞争检测</p>
</td>
<td class="cellrowborder" valign="top" width="18.201820182018203%" headers="mcps1.2.4.1.2 "><p id="zh-cn_topic_0000001691887174_p25211015152117"><a id="zh-cn_topic_0000001691887174_p25211015152117"></a><a id="zh-cn_topic_0000001691887174_p25211015152117"></a><a href="#竞争检测">竞争检测</a></p>
</td>

<td class="cellrowborder" valign="top" width="57.66576657665766%" headers="mcps1.2.4.1.3 "><p id="p1594575152811"><a id="p1594575152811"></a><a id="p1594575152811"></a>msSanitizer支持对单算子API调用的<span id="zh-cn_topic_0000001691887174_ph9854191019354"><a id="zh-cn_topic_0000001691887174_ph9854191019354"></a><a id="zh-cn_topic_0000001691887174_ph9854191019354"></a>Ascend C</span>算子（包括Vector、Cube算子和Mix融合算子）内存和竞争的检测，可参考<a href="#竞争检测">竞争检测</a>。</p>
</td>
</tr>
<tr id="row8723816143214"><td class="cellrowborder" valign="top" width="24.13241324132413%" headers="mcps1.2.4.1.1 "><p id="p1396725985710"><a id="p1396725985710"></a><a id="p1396725985710"></a>算子未初始化检测</p>
</td>
<td class="cellrowborder" valign="top" width="18.201820182018203%" headers="mcps1.2.4.1.2 "><p id="p832015178273"><a id="p832015178273"></a><a id="p832015178273"></a><a href="#未初始化检测">未初始化检测</a></p>
</td>
<td class="cellrowborder" valign="top" width="57.66576657665766%" headers="mcps1.2.4.1.3 "><p id="p9365115115282"><a id="p9365115115282"></a><a id="p9365115115282"></a>msSanitizer支持Ascend CL调用的<span id="ph7196749112810"><a id="ph7196749112810"></a><a id="ph7196749112810"></a>Ascend C</span>算子（包括Vector、Cube算子和Mix融合算子）未初始化的检测，可参考<a href="#未初始化检测">未初始化检测</a>。</p>
</td>
</tr>
<tr id="row199663517810"><td class="cellrowborder" valign="top" width="24.13241324132413%" headers="mcps1.2.4.1.1 "><p id="p396611511814"><a id="p396611511814"></a><a id="p396611511814"></a>同步检测</p>
</td>
<td class="cellrowborder" valign="top" width="18.201820182018203%" headers="mcps1.2.4.1.2 "><p id="p39661251188"><a id="p39661251188"></a><a id="p39661251188"></a><a href="#同步检测">同步检测</a></p>
</td>
<td class="cellrowborder" valign="top" width="57.66576657665766%" headers="mcps1.2.4.1.3 "><p id="p131542574519"><a id="p131542574519"></a><a id="p131542574519"></a>msSanitizer支持内核调用符或单算子API调用的<span id="ph1793735132913"><a id="ph1793735132913"></a><a id="ph1793735132913"></a>Ascend C</span>算子（包括Vector、Cube算子和Mix融合算子）同步指令配对情况的检测，可参考<a href="#同步检测">同步检测</a>。</p>
</td>
</tr>
<tr id="row1267856165716"><td class="cellrowborder" valign="top" width="24.13241324132413%" headers="mcps1.2.4.1.1 "><p id="zh-cn_topic_0000001691887174_p13521201582115"><a id="zh-cn_topic_0000001691887174_p13521201582115"></a><a id="zh-cn_topic_0000001691887174_p13521201582115"></a>CANN软件栈的内存检测</p>
</td>
<td class="cellrowborder" valign="top" width="18.201820182018203%" headers="mcps1.2.4.1.2 "><p id="p15363172215347"><a id="p15363172215347"></a><a id="p15363172215347"></a><a href="#内存检测">内存检测</a></p>
</td>
<td class="cellrowborder" valign="top" width="57.66576657665766%" headers="mcps1.2.4.1.3 "><p id="p182415137384"><a id="p182415137384"></a><a id="p182415137384"></a>支持CANN软件栈内存检测，详细可参考《<a href="./example.md">example</a>》中的“检测CANN软件栈的内存”章节。</p>
</td>
</tr>
</tbody>
</table>

**异常检测功能启用原则<a id="section1051122665518"></a>**

异常检测工具提供内存检测（memcheck）、竞争检测（racecheck）、未初始化检测（initcheck）和同步检测（synccheck）四种检测功能，多种检测功能可以组合开启，组合启用检测功能需满足以下原则：

-   多个检测功能可通过多次指定--tool参数同时开启。如执行以下命令可同时开启内存检测和竞争检测：

    ```sh
    mssanitizer -t memcheck -t racecheck ./application
    ```

-   若开启了检测功能对应的子选项，则对应的检测功能也会被默认开启。如开启了内存检测对应的泄漏检测子选项，则内存检测功能会被自动开启：

    ```sh
    mssanitizer -t racecheck --leak-check=yes ./application
    ```

    以上命令等价于：

    ```sh
    mssanitizer -t racecheck -t memcheck --leak-check=yes ./application
    ```

-   若不指定任何检测功能，则默认启用内存检测：

    ```
    mssanitizer ./application
    ```

    以上命令等价于：

    ```
    mssanitizer -t memcheck ./application
    ```

**调用场景<a id="section156511357135"></a>**

支持如下调用算子的场景：

-   Kernel直调算子开发：Kernel直调。

    > [!NOTE] 说明    
    > Kernel直调场景，详细信息可参考《[Ascend C算子开发指南](https://www.hiascend.com/document/detail/zh/canncommercial/83RC1/opdevg/Ascendcopdevg/atlas_ascendc_10_0056.html)》中“Kernel直调算子开发 \> Kernel直调”章节。具体操作请参见《[example](./example.md)》中的“检测内核调用符方式的Ascend C算子”。

-   工程化算子开发：单算子API调用。

    > [!NOTE] 说明    
    >-   单算子API调用场景，详细信息可参考《[Ascend C算子开发指南](https://www.hiascend.com/document/detail/zh/canncommercial/83RC1/opdevg/Ascendcopdevg/atlas_ascendc_10_0070.html)》中“工程化算子开发 \>  单算子API调用”章节。具体操作请参见《[example](./example.md)》中的“检测API调用的单算子”。
    >-   在调用含有aclnn前缀的API时，需执行以下命令，通过aclInit接口传入acl.json文件以保证内存检测的准确性。
    >    ```
    >    auto ret = aclInit("./acl.json"); // acl.json文件内容为{"dump":{"dump_scene":"lite_exception"}}
    >    ```

-   AI框架算子适配：PyTorch框架。

    > [!NOTE] 说明    
    >-   PyTorch图模式（TorchAir）下，仅支持在msSanitizer工具不添加编译选项的情况下进行检测，具体请参见[配置编译选项（可选）](#section1819973616410)。
    >-   PyTorch图模式（TorchAir）下，支持Ascend IR图执行模式和aclgraph图执行模式，具体请参见《[Ascend Extension for PyTorch](https://www.hiascend.com/document/detail/zh/Pytorch/720/modthirdparty/torchairuseguide/torchair_00015.html)》中“PyTorch图模式使用\(TorchAir\)\>reduce-overhead模式功能\>reduce-overhead模式配置”章节。
    >-   PyTorch框架调用场景，详细信息可参考《[Ascend Extension for PyTorch](https://www.hiascend.com/document/detail/zh/Pytorch/720/ptmoddevg/Frameworkfeatures/featuresguide_00021.html) 》中“PyTorch框架特性指南\>自定义算子适配开发\>基于OpPlugin算子适配开发”章节。具体操作请参见《[example](./example.md)》中的“检测PyTorch接口调用的算子”。

-   Triton算子开发：Triton算子调用。

    > [!NOTE] 说明    
    >-   Triton算子调用场景，详细信息可参考《[example](./example.md)》中的“检测Triton算子”章节。
    >-   已完成Triton及Triton-Ascend插件的安装和配置，具体操作请参见[Link](https://gitcode.com/Ascend/triton-ascend)。
    >-   Triton算子调用场景不适用于Atlas 推理系列产品。
    >-   为了防止未重新编译的算子造成影响，建议您启用以下环境变量：
    >    ```
    >    export TRITON_ALWAYS_COMPILE=1
    >    ```
    >-   Triton场景会使用PyTorch创建Tensor，PyTorch框架内默认使用内存池的方式管理GM内存，会对内存检测产生干扰。因此，在检测前需要额外设置如下环境变量关闭内存池，以保证检测结果准确。
    >    ```
    >    export PYTORCH_NO_NPU_MEMORY_CACHING=1
    >    ```

### 注意事项<a id="ZH-CN_TOPIC_0000002509279390"></a>

-   用户需保证可执行文件及用户自定义程序的安全性。
-   用户需自行保证可执行文件或用户程序（_application_）执行的安全性。
    -   建议限制对可执行文件或用户程序（_application_）的操作权限，避免提权风险。
    -   不建议进行高危操作（删除文件、删除目录、修改密码及提权命令等），避免安全风险。

### 命令格式<a id="ZH-CN_TOPIC_0000002541039377"></a>

可以通过运行以下命令来调用msSanitizer工具。

```sh
mssanitizer <options> -- <user_program> <user_options>   
```

> [!NOTE] 说明    
>-   options为检测工具的命令行选项，详细的参数选项及其默认值，请参考[表1 通用参数说明](#zh-cn_topic_0000001691887174_table716213104506)和[表2 内存检测参数说明](#zh-cn_topic_0000001691887174_table1796112119339)，user\_program为用户算子程序，user\_options为用户程序的命令行选项。
>-   如要加载的可执行文件或用户自定义程序本身带有命令行参数时，在可执行文件或用户程序（_application_）之前使用“--“分隔检测工具和用户命令。
>    ```sh
>    mssanitizer -- application parameter1 parameter2 ...
>    ```

### 参数说明<a id="ZH-CN_TOPIC_0000002541159391"></a>

**表 1**  通用参数说明

| 参数名称 | 参数描述 | 参数取值 | 是否必选 |
| -- | -- | -- | -- |
| -v，--version | 查询msSanitizer工具版本。| - | 否 |
| -t，--tool | 指定异常检测的子工具。| <ul><li>memcheck：内存检测（默认）</li><li>racecheck：竞争检测</li><li>initcheck：未初始化检测</li><li>synccheck：同步检测</li></ul> | 否 |
| --log-file | 指定检测报告输出到文件。| {file_name}，如配置为test_log。<br>说明：<ul><li>仅支持数字、大小写字母和- . / _四种符号。</li><li>为避免日志泄漏风险，建议限制该文件权限，确保只有授权人员才能访问该文件。</li><li>工具会以覆盖的方式将报告输出到test_log文件。若test_log文件中已有内容，这些内容将会被清空。因此，建议指定一个空文件用于输出报告。</li></ul> | 否 |
| --log-level | 指定检测报告输出等级。| <ul><li>info：输出info/warn/error级别的运行信息。</li><li>warn：输出warn/error级别的运行信息（默认）。</li><li>error：输出error级别的运行信息。</li></ul> | 否 |
| --max-debuglog-size | 指定检测工具调试输出日志中单个文件大小的上限。| 可设定范围为1~10240之间的整数，单位为MB。<br>默认值为1024。<br>说明：<br>--max-debuglog-size=100就表示单个调试日志的大小上限为100MB。| 否 |
| --block-id | 是否启用单block检测功能。| 可设定范围为0~200之间的整数。<br>启用前<br><ul><li>内存检测、未初始化检测和同步检测：默认检测所有block。</li><li>竞争检测：核间默认检测所有block，核内默认检测block 0的流水内及流水间的竞争。</li></ul>启用后<br><ul><li>内存检测、未初始化检测和同步检测：检测指定block。</li><li>竞争检测：核间不进行检测，检测指定block的流水内及流水间的竞争。</li></ul> | 否 |
| --cache-size | 表示单block的GM内存大小。| 单block可设定范围为1~8192之间的整数，单位为MB。<br>单block默认值为100MB，表示单block可申请100MB的内存大小。<br>说明：<br><ul><li>启用单block检测时，--cache-size的最大值为8192MB。不启用单block检测时，--cache-size可设置的最大值为(24*1024 / block数量) 。</li><li>当--cache-size值不满足需求时，异常检测工具将会打印信息提示用户重新设置--cache-size值，具体请参见《MindStudio Sanitizier常见问题》中的msSanitizer工具提示--cache-size异常。</li></ul> | 否 |
| --kernel-name | 指定要检测的算子名称。| 支持使用算子名中的部分字符串来进行模糊匹配。如果不指定，则系统默认会对整个程序执行期间所调度的所有算子进行检测。<br>例如，需要同时检测名为"abcd"和"bcd"的算子时，可以通过配置--kernel-name="bc"来实现这一需求，系统会自动识别并检测所有包含"bc"字符串的算子。| 否 |
| --full-backtrace | 显示 AscendC API 内的调用栈回溯 | <ul><li>yes：显示完整的调用栈回溯。</li><li>no（默认）：不显示 AscendC API 内的调用栈。</li></ul> | 否 |
| --demangle | 设置输出中函数名显示的 demangle 模式 | <ul><li>full（默认）：显示完整的 demangle 后的函数名。</li><li>simple：仅显示函数名，不包含返回值、参数列表。</li><li>no：显示未 demangle 的函数名。</li></ul> | 否 |
| -h，--help | 输出帮助信息。| - | 否 |

**表 2**  内存检测参数说明

<a id="zh-cn_topic_0000001691887174_table1796112119339"></a>
<table><thead align="left"><tr id="zh-cn_topic_0000001691887174_row1496132173311"><th class="cellrowborder" valign="top" width="25.580000000000002%" id="mcps1.2.5.1.1"><p id="zh-cn_topic_0000001691887174_p156591934113313"><a id="zh-cn_topic_0000001691887174_p156591934113313"></a><a id="zh-cn_topic_0000001691887174_p156591934113313"></a>参数名称</p>
</th>
<th class="cellrowborder" valign="top" width="42.13%" id="mcps1.2.5.1.2"><p id="zh-cn_topic_0000001691887174_p166023403315"><a id="zh-cn_topic_0000001691887174_p166023403315"></a><a id="zh-cn_topic_0000001691887174_p166023403315"></a>参数描述</p>
</th>
<th class="cellrowborder" valign="top" width="19.61%" id="mcps1.2.5.1.3"><p id="zh-cn_topic_0000001691887174_p740613812427"><a id="zh-cn_topic_0000001691887174_p740613812427"></a><a id="zh-cn_topic_0000001691887174_p740613812427"></a>参数取值</p>
</th>
<th class="cellrowborder" valign="top" width="12.68%" id="mcps1.2.5.1.4"><p id="zh-cn_topic_0000001691887174_p176601234163310"><a id="zh-cn_topic_0000001691887174_p176601234163310"></a><a id="zh-cn_topic_0000001691887174_p176601234163310"></a>是否必选</p>
</th>
</tr>
</thead>
<tbody><tr id="row84691348101613"><td class="cellrowborder" valign="top" width="25.580000000000002%" headers="mcps1.2.5.1.1 "><p id="p346944801616"><a id="p346944801616"></a><a id="p346944801616"></a>--check-unused-memory</p>
</td>
<td class="cellrowborder" valign="top" width="42.13%" headers="mcps1.2.5.1.2 "><p id="p17470124816169"><a id="p17470124816169"></a><a id="p17470124816169"></a>使能分配内存未使用检测。</p>
</td>
<td class="cellrowborder" valign="top" width="19.61%" headers="mcps1.2.5.1.3 "><a id="ul14357945101717"></a><a id="ul14357945101717"></a><ul id="ul14357945101717"><li>yes</li><li>no（默认）</li></ul>
</td>
<td class="cellrowborder" valign="top" width="12.68%" headers="mcps1.2.5.1.4 "><p id="p3357184511719"><a id="p3357184511719"></a><a id="p3357184511719"></a>否</p>
</td>
</tr>
<tr id="zh-cn_topic_0000001691887174_row17961221193316"><td class="cellrowborder" valign="top" width="25.580000000000002%" headers="mcps1.2.5.1.1 "><p id="zh-cn_topic_0000001691887174_p1623217521238"><a id="zh-cn_topic_0000001691887174_p1623217521238"></a><a id="zh-cn_topic_0000001691887174_p1623217521238"></a>--leak-check</p>
</td>
<td class="cellrowborder" valign="top" width="42.13%" headers="mcps1.2.5.1.2 "><p id="zh-cn_topic_0000001691887174_p172322521231"><a id="zh-cn_topic_0000001691887174_p172322521231"></a><a id="zh-cn_topic_0000001691887174_p172322521231"></a>使能内存泄漏检测。</p>
</td>
<td class="cellrowborder" valign="top" width="19.61%" headers="mcps1.2.5.1.3 "><a id="zh-cn_topic_0000001691887174_ul8795651174311"></a><a id="zh-cn_topic_0000001691887174_ul8795651174311"></a><ul id="zh-cn_topic_0000001691887174_ul8795651174311"><li>yes</li><li>no（默认）</li></ul>
</td>
<td class="cellrowborder" valign="top" width="12.68%" headers="mcps1.2.5.1.4 "><p id="zh-cn_topic_0000001691887174_p923313521738"><a id="zh-cn_topic_0000001691887174_p923313521738"></a><a id="zh-cn_topic_0000001691887174_p923313521738"></a>否</p>
</td>
</tr>
<tr id="zh-cn_topic_0000001691887174_row159611221123310"><td class="cellrowborder" valign="top" width="25.580000000000002%" headers="mcps1.2.5.1.1 "><p id="zh-cn_topic_0000001691887174_p1283420591833"><a id="zh-cn_topic_0000001691887174_p1283420591833"></a><a id="zh-cn_topic_0000001691887174_p1283420591833"></a>--check-device-heap</p>
</td>
<td class="cellrowborder" valign="top" width="42.13%" headers="mcps1.2.5.1.2 "><p id="zh-cn_topic_0000001691887174_p78341359833"><a id="zh-cn_topic_0000001691887174_p78341359833"></a><a id="zh-cn_topic_0000001691887174_p78341359833"></a>使能Device侧内存检测。</p>
</td>
<td class="cellrowborder" valign="top" width="19.61%" headers="mcps1.2.5.1.3 "><a id="zh-cn_topic_0000001691887174_ul143801346194215"></a><a id="zh-cn_topic_0000001691887174_ul143801346194215"></a><ul id="zh-cn_topic_0000001691887174_ul143801346194215"><li>yes</li><li>no（默认）</li></ul>
</td>
<td class="cellrowborder" valign="top" width="12.68%" headers="mcps1.2.5.1.4 "><p id="zh-cn_topic_0000001691887174_p28348596312"><a id="zh-cn_topic_0000001691887174_p28348596312"></a><a id="zh-cn_topic_0000001691887174_p28348596312"></a>否</p>
</td>
</tr>
<tr id="zh-cn_topic_0000001691887174_row59611021203316"><td class="cellrowborder" valign="top" width="25.580000000000002%" headers="mcps1.2.5.1.1 "><p id="zh-cn_topic_0000001691887174_p81461021412"><a id="zh-cn_topic_0000001691887174_p81461021412"></a><a id="zh-cn_topic_0000001691887174_p81461021412"></a>--check-cann-heap</p>
</td>
<td class="cellrowborder" valign="top" width="42.13%" headers="mcps1.2.5.1.2 "><p id="zh-cn_topic_0000001691887174_p18146626415"><a id="zh-cn_topic_0000001691887174_p18146626415"></a><a id="zh-cn_topic_0000001691887174_p18146626415"></a>使能CANN软件栈内存检测。</p>
</td>
<td class="cellrowborder" valign="top" width="19.61%" headers="mcps1.2.5.1.3 "><a id="zh-cn_topic_0000001691887174_ul616411483423"></a><a id="zh-cn_topic_0000001691887174_ul616411483423"></a><ul id="zh-cn_topic_0000001691887174_ul616411483423"><li>yes</li><li>no（默认）</li></ul>
</td>
<td class="cellrowborder" valign="top" width="12.68%" headers="mcps1.2.5.1.4 "><p id="zh-cn_topic_0000001691887174_p4146152247"><a id="zh-cn_topic_0000001691887174_p4146152247"></a><a id="zh-cn_topic_0000001691887174_p4146152247"></a>否</p>
</td>
</tr>
</tbody>
</table>

> [!NOTE] 说明    
>-   --check-device-heap或--check-cann-heap使能后，将不会对Kernel内进行检测。
>-   Device侧内存检测和CANN软件栈内存检测不能同时使能，若同时使能会提示“CANNOT enable both --check-cann-heap and --check-device-heap”。
>-   使用msSanitizer工具提供的API头文件重新编译的待检测程序只能用于Ascend CL系列接口的泄漏检测，无法用于Device接口的检测。

### 使用示例<a id="ZH-CN_TOPIC_0000002509519398"></a> 

#### 内存检测<a id="内存检测"></a>

内存检测是针对用户程序运行时的一种异常检测，该工具可以检测并报告算子运行中对外部存储（Global Memory）和内部存储（Local Memory）的越界及未对齐等内存访问异常。

**支持的内存异常类型<a id="zh-cn_topic_0000001820455825_section1047315213512"></a>**

内存检测能够检测并报告诸如内存非法读写、多核踩踏、非对齐访问、内存泄漏、非法释放及分配内存未使用等异常操作，如下表所示。

**表 1**  内存异常类型

<a id="zh-cn_topic_0000001820455825_table1944445964014"></a>
<table><thead align="left"><tr id="zh-cn_topic_0000001820455825_row444419596409"><th class="cellrowborder" valign="top" width="16.55%" id="mcps1.2.5.1.1"><p id="zh-cn_topic_0000001820455825_p108671312419"><a id="zh-cn_topic_0000001820455825_p108671312419"></a><a id="zh-cn_topic_0000001820455825_p108671312419"></a>异常名</p>
</th>
<th class="cellrowborder" valign="top" width="53.339999999999996%" id="mcps1.2.5.1.2"><p id="zh-cn_topic_0000001820455825_p1886713134116"><a id="zh-cn_topic_0000001820455825_p1886713134116"></a><a id="zh-cn_topic_0000001820455825_p1886713134116"></a>描述</p>
</th>
<th class="cellrowborder" valign="top" width="15.4%" id="mcps1.2.5.1.3"><p id="zh-cn_topic_0000001820455825_p186715119410"><a id="zh-cn_topic_0000001820455825_p186715119410"></a><a id="zh-cn_topic_0000001820455825_p186715119410"></a>位置</p>
</th>
<th class="cellrowborder" valign="top" width="14.71%" id="mcps1.2.5.1.4"><p id="zh-cn_topic_0000001820455825_p1386841154119"><a id="zh-cn_topic_0000001820455825_p1386841154119"></a><a id="zh-cn_topic_0000001820455825_p1386841154119"></a>支持地址空间</p>
</th>
</tr>
</thead>
<tbody><tr id="zh-cn_topic_0000001820455825_row194441959184018"><td class="cellrowborder" valign="top" width="16.55%" headers="mcps1.2.5.1.1 "><p id="zh-cn_topic_0000001820455825_p1086819118416"><a id="zh-cn_topic_0000001820455825_p1086819118416"></a><a id="zh-cn_topic_0000001820455825_p1086819118416"></a><a href="#zh-cn_topic_0000001820455825_li125301729105314">非法读写</a></p>
</td>
<td class="cellrowborder" valign="top" width="53.339999999999996%" headers="mcps1.2.5.1.2 "><p id="zh-cn_topic_0000001820455825_p2868141194114"><a id="zh-cn_topic_0000001820455825_p2868141194114"></a><a id="zh-cn_topic_0000001820455825_p2868141194114"></a>由于访问了未分配的内存导致的异常。</p>
</td>
<td class="cellrowborder" valign="top" width="15.4%" headers="mcps1.2.5.1.3 "><p id="zh-cn_topic_0000001820455825_p786820174119"><a id="zh-cn_topic_0000001820455825_p786820174119"></a><a id="zh-cn_topic_0000001820455825_p786820174119"></a>Kernel、Host</p>
</td>
<td class="cellrowborder" valign="top" width="14.71%" headers="mcps1.2.5.1.4 "><p id="zh-cn_topic_0000001820455825_p1086811118413"><a id="zh-cn_topic_0000001820455825_p1086811118413"></a><a id="zh-cn_topic_0000001820455825_p1086811118413"></a>GM、UB、L0{A,B,C}、L1</p>
</td>
</tr>
<tr id="zh-cn_topic_0000001820455825_row1244445954014"><td class="cellrowborder" valign="top" width="16.55%" headers="mcps1.2.5.1.1 "><p id="zh-cn_topic_0000001820455825_p886816111410"><a id="zh-cn_topic_0000001820455825_p886816111410"></a><a id="zh-cn_topic_0000001820455825_p886816111410"></a><a href="#zh-cn_topic_0000001820455825_li1423173985318">多核踩踏</a></p>
</td>
<td class="cellrowborder" valign="top" width="53.339999999999996%" headers="mcps1.2.5.1.2 "><p id="zh-cn_topic_0000001820455825_p20868713418"><a id="zh-cn_topic_0000001820455825_p20868713418"></a><a id="zh-cn_topic_0000001820455825_p20868713418"></a><span id="zh-cn_topic_0000001820455825_zh-cn_topic_0000001588832845_ph1521173113358"><a id="zh-cn_topic_0000001820455825_zh-cn_topic_0000001588832845_ph1521173113358"></a><a id="zh-cn_topic_0000001820455825_zh-cn_topic_0000001588832845_ph1521173113358"></a>AI Core</span>核心访问了重叠的内存导致的踩踏问题。</p>
</td>
<td class="cellrowborder" valign="top" width="15.4%" headers="mcps1.2.5.1.3 "><p id="zh-cn_topic_0000001820455825_p1986814154114"><a id="zh-cn_topic_0000001820455825_p1986814154114"></a><a id="zh-cn_topic_0000001820455825_p1986814154114"></a>Kernel</p>
</td>
<td class="cellrowborder" valign="top" width="14.71%" headers="mcps1.2.5.1.4 "><p id="zh-cn_topic_0000001820455825_p8868131154117"><a id="zh-cn_topic_0000001820455825_p8868131154117"></a><a id="zh-cn_topic_0000001820455825_p8868131154117"></a>GM</p>
</td>
</tr>
<tr id="zh-cn_topic_0000001820455825_row174451359184019"><td class="cellrowborder" valign="top" width="16.55%" headers="mcps1.2.5.1.1 "><p id="zh-cn_topic_0000001820455825_p686821154118"><a id="zh-cn_topic_0000001820455825_p686821154118"></a><a id="zh-cn_topic_0000001820455825_p686821154118"></a><a href="#zh-cn_topic_0000001820455825_li1322945295318">非对齐访问</a></p>
</td>
<td class="cellrowborder" valign="top" width="53.339999999999996%" headers="mcps1.2.5.1.2 "><p id="zh-cn_topic_0000001820455825_p138681113413"><a id="zh-cn_topic_0000001820455825_p138681113413"></a><a id="zh-cn_topic_0000001820455825_p138681113413"></a>DMA（负责在Global Memory和Local Memory之间搬运数据）搬运的地址与内存的最小访问粒度未对齐导致的异常。</p>
</td>
<td class="cellrowborder" valign="top" width="15.4%" headers="mcps1.2.5.1.3 "><p id="zh-cn_topic_0000001820455825_p158689118414"><a id="zh-cn_topic_0000001820455825_p158689118414"></a><a id="zh-cn_topic_0000001820455825_p158689118414"></a>Kernel</p>
</td>
<td class="cellrowborder" valign="top" width="14.71%" headers="mcps1.2.5.1.4 "><p id="zh-cn_topic_0000001820455825_p9868714416"><a id="zh-cn_topic_0000001820455825_p9868714416"></a><a id="zh-cn_topic_0000001820455825_p9868714416"></a>GM、UB、L0{A,B,C}、L1</p>
</td>
</tr>
<tr id="row38014745717"><td class="cellrowborder" valign="top" width="16.55%" headers="mcps1.2.5.1.1 "><p id="zh-cn_topic_0000001820455825_p786814119411"><a id="zh-cn_topic_0000001820455825_p786814119411"></a><a id="zh-cn_topic_0000001820455825_p786814119411"></a><a href="#zh-cn_topic_0000001820455825_li172874102543">非法释放</a></p>
</td>
<td class="cellrowborder" valign="top" width="53.339999999999996%" headers="mcps1.2.5.1.2 "><p id="zh-cn_topic_0000001820455825_p7868191174113"><a id="zh-cn_topic_0000001820455825_p7868191174113"></a><a id="zh-cn_topic_0000001820455825_p7868191174113"></a>对未分配或已释放的地址进行释放导致的异常。</p>
</td>
<td class="cellrowborder" valign="top" width="15.4%" headers="mcps1.2.5.1.3 "><p id="zh-cn_topic_0000001820455825_p78681154112"><a id="zh-cn_topic_0000001820455825_p78681154112"></a><a id="zh-cn_topic_0000001820455825_p78681154112"></a>Host</p>
</td>
<td class="cellrowborder" valign="top" width="14.71%" headers="mcps1.2.5.1.4 "><p id="zh-cn_topic_0000001820455825_p108697144111"><a id="zh-cn_topic_0000001820455825_p108697144111"></a><a id="zh-cn_topic_0000001820455825_p108697144111"></a>GM</p>
</td>
</tr>
<tr id="zh-cn_topic_0000001820455825_row14451459184013"><td class="cellrowborder" valign="top" width="16.55%" headers="mcps1.2.5.1.1 "><p id="zh-cn_topic_0000001820455825_p138684184112"><a id="zh-cn_topic_0000001820455825_p138684184112"></a><a id="zh-cn_topic_0000001820455825_p138684184112"></a><a href="#zh-cn_topic_0000001820455825_li888655915315">内存泄漏</a></p>
</td>
<td class="cellrowborder" valign="top" width="53.339999999999996%" headers="mcps1.2.5.1.2 "><p id="zh-cn_topic_0000001820455825_p208681104116"><a id="zh-cn_topic_0000001820455825_p208681104116"></a><a id="zh-cn_topic_0000001820455825_p208681104116"></a>申请内存使用后未释放，导致程序在运行过程中内存占用持续增加的异常。</p>
</td>
<td class="cellrowborder" valign="top" width="15.4%" headers="mcps1.2.5.1.3 "><p id="zh-cn_topic_0000001820455825_p16868121194112"><a id="zh-cn_topic_0000001820455825_p16868121194112"></a><a id="zh-cn_topic_0000001820455825_p16868121194112"></a>Host</p>
</td>
<td class="cellrowborder" valign="top" width="14.71%" headers="mcps1.2.5.1.4 "><p id="zh-cn_topic_0000001820455825_p6868813417"><a id="zh-cn_topic_0000001820455825_p6868813417"></a><a id="zh-cn_topic_0000001820455825_p6868813417"></a>GM</p>
</td>
</tr>
<tr id="zh-cn_topic_0000001820455825_row91942018151815"><td class="cellrowborder" valign="top" width="16.55%" headers="mcps1.2.5.1.1 "><p id="zh-cn_topic_0000001820455825_p968917472254"><a id="zh-cn_topic_0000001820455825_p968917472254"></a><a id="zh-cn_topic_0000001820455825_p968917472254"></a><a href="#li1789816476297">分配内存未使用</a></p>
</td>
<td class="cellrowborder" valign="top" width="53.339999999999996%" headers="mcps1.2.5.1.2 "><p id="zh-cn_topic_0000001820455825_p1619441811811"><a id="zh-cn_topic_0000001820455825_p1619441811811"></a><a id="zh-cn_topic_0000001820455825_p1619441811811"></a>对内存分配后未使用导致的异常。</p>
</td>
<td class="cellrowborder" valign="top" width="15.4%" headers="mcps1.2.5.1.3 "><p id="zh-cn_topic_0000001820455825_p226917191630"><a id="zh-cn_topic_0000001820455825_p226917191630"></a><a id="zh-cn_topic_0000001820455825_p226917191630"></a>Kernel、Host</p>
</td>
<td class="cellrowborder" valign="top" width="14.71%" headers="mcps1.2.5.1.4 "><p id="zh-cn_topic_0000001820455825_p174971517141915"><a id="zh-cn_topic_0000001820455825_p174971517141915"></a><a id="zh-cn_topic_0000001820455825_p174971517141915"></a>GM</p>
</td>
</tr>
<tr id="row112579422159"><td class="cellrowborder" valign="top" width="16.55%" headers="mcps1.2.5.1.1 "><p id="p425812424156"><a id="p425812424156"></a><a id="p425812424156"></a><a href="#li0925115378">线程间踩踏</a></p>
</td>
<td class="cellrowborder" valign="top" width="53.339999999999996%" headers="mcps1.2.5.1.2 "><p id="p16258144219152"><a id="p16258144219152"></a><a id="p16258144219152"></a>AI Core核心内线程间访问了重叠的内存导致的踩踏问题。</p>
</td>
<td class="cellrowborder" valign="top" width="15.4%" headers="mcps1.2.5.1.3 "><p id="p42581842191512"><a id="p42581842191512"></a><a id="p42581842191512"></a>Kernel</p>
</td>
<td class="cellrowborder" valign="top" width="14.71%" headers="mcps1.2.5.1.4 "><p id="p625824261518"><a id="p625824261518"></a><a id="p625824261518"></a>GM</p>
</td>
</tr>
</tbody>
</table>

**启用内存检测<a id="zh-cn_topic_0000001820455825_section1371111444516"></a>**

运行msSanitizer工具时，默认启用内存检测功能（**memcheck**）。其中_，application_为用户程序。

-   <a id="zh-cn_topic_0000001820455825_li1424892023610"></a>执行如下命令可显式指定内存检测，默认会开启非法读写、多核踩踏、非对齐访问和非法释放的检测功能：

    ```
    mssanitizer --tool=memcheck application
    ```

-   执行如下命令，可在[步骤一](#zh-cn_topic_0000001820455825_li1424892023610)检测功能项的基础上，手动启用内存泄漏的检测功能：

    ```
    mssanitizer --tool=memcheck --leak-check=yes application
    ```

-   执行如下命令，可在[步骤一](#zh-cn_topic_0000001820455825_li1424892023610)检测功能项的基础上，手动启用分配内存未使用的检测功能：

    ```
    mssanitizer --tool=memcheck --check-unused-memory=yes application
    ```

> [!NOTE] 说明       
>-   当用户程序运行完成后，界面将会打印异常报告，异常的具体含义请参见[内存异常报告解析](#内存异常报告解析)。
>-   当用户使用PyTorch等框架接入算子时，框架内部可能会通过内存池管理GM内存，而内存池通常会一次性分配大量GM内存，并在运行过程中复用。此时，若用户对算子进行检测并记录GM上所有内存分配和释放的信息，会因为内存池的内存管理方式导致检测信息不准确。因此检测工具提供了手动上报GM内存分配信息的接口，方便用户在算子调用时手动上报该算子应当使用的GM内存范围，详细接口介绍请参见《[MindStudio Sanitizer对外接口使用说明](./mssanitizer_api_reference)》中的sanitizerReportMalloc和sanitizerReportFree接口。
>-   msSanitizer工具也支持对Atlas A2 训练系列产品/Atlas A2 推理系列产品的AllReduce、AllGather、ReduceScatter、AlltoAll接口及Atlas A3 训练系列产品/Atlas A3 推理系列产品的AllGather、ReduceScatter、AlltoAllV接口进行非法读写的检测，具体介绍请参见《[Ascend C算子开发接口](https://www.hiascend.com/document/detail/zh/canncommercial/83RC1/API/ascendcopapi/atlasascendc_api_07_0869.html)》中的“高阶API \> Hccl \>  Hccl Kernel侧接口”章节
>-   msSanitizer工具也支持对通算融合类算子的非法读写检测。
>-   当前仅内存检测中GM越界支持昇腾910\_95 AI处理器，其他暂不支持。

**内存异常报告解析<a id="内存异常报告解析"></a>**

内存检测异常报告会输出多种不同类型的异常信息，以下将对一些简单的异常信息示例进行说明，帮助用户解读异常报告中的信息。

-   <a id="zh-cn_topic_0000001820455825_li125301729105314"></a>非法读写

    非法读写异常信息的产生是由于算子程序中，通过读或写的方式访问了一块未分配的内存。此错误一般发生在GM或片上内存上，GM异常是由于GM分配的大小与实际算子程序中访问的范围不一致导致，而片上内存的异常是由于算子程序的访问范围超过硬件容量上限导致。

    ```
    ====== ERROR: illegal read of size 224  // 异常的基本信息,包含非法读写的类型以及被非法访问的字节数,非法读写包括read(非法读取)和write(非法写入)
    ======    at 0x12c0c0015000 on GM in add_custom_kernel  // 异常发生的内存位置信息，包含发生的核函数名、地址空间与内存地址，此处的内存地址指一次内存访问中的首地址
    ======    in block aiv(0) on device 0  // 异常代码对应Vector核的block索引
    ======    code in pc current 0x77c (serialNo:10) // 当前异常发生的pc指针和调用api行为的序列号
    ======    #0 ${ASCEND_HOME_PATH}/compiler/tikcpp/tikcfw/impl/dav_c220/kernel_operator_data_copy_impl.h:58:9  // 以下为异常发生代码的调用栈，包含文件名、行号和列号
    ======    #1 ${ASCEND_HOME_PATH}/compiler/tikcpp/tikcfw/inner_interface/inner_kernel_operator_data_copy_intf.cppm:58:9
    ======    #2 ${ASCEND_HOME_PATH}/compiler/tikcpp/tikcfw/inner_interface/inner_kernel_operator_data_copy_intf.cppm:443:5
    ======    #3 illegal_read_and_write/add_custom.cpp:18:5
    ```

    以上示例中，对GM上的“0x12c0c0015000“地址存在非法读取，且导致异常发生的指令对应于算子实现文件add\_custom.cpp的第18行。

    > [!NOTE] 说明       
    >不添加编译选项的情况下，异常报告将不会出现以下调用栈信息：
    >```
    >======    #0 ${ASCEND_HOME_PATH}/compiler/tikcpp/tikcfw/impl/dav_c220/kernel_operator_data_copy_impl.h:58:9  // 以下为异常发生代码的调用栈，包含文件名、行号和列号
    >======    #1 ${ASCEND_HOME_PATH}/compiler/tikcpp/tikcfw/inner_interface/inner_kernel_operator_data_copy_intf.cppm:58:9
    >======    #2 ${ASCEND_HOME_PATH}/compiler/tikcpp/tikcfw/inner_interface/inner_kernel_operator_data_copy_intf.cppm:443:5
    >======    #3 illegal_read_and_write/add_custom.cpp:18:5
    >```

-   <a id="zh-cn_topic_0000001820455825_li1423173985318"></a>多核踩踏

    AI Core是AI处理器中的计算核心，AI处理器内部有多个AI Core，算子运行就在这些AI Core上。这些AI Core会在计算过程中从GM上搬入或搬出数据。当没有显式地进行核间同步时，如果各个核之间访问的GM内存存在重叠并且至少有一个核对重叠地址进行写入时，则会发生多核踩踏问题。这里我们通过所有者的概念来保证多核之间不会发生踩踏问题，当一块内存被某一个核写入后，这块内存就由该核所有。当其他核对这块内存进行访问时就会产生out of bounds异常。

    ```
    ====== WARNING: out of bounds of size 256  // 异常的基本信息，包含发生踩踏的字节数
    ======    at 0x12c0c00150fc on GM when writing data in add_custom_kernel  // 异常发生的内存位置信息，包含发生的核函数名、地址空间与内存地址，此处的内存地址指一次内存访问中的首地址
    ======    in block aiv(9) on device 0  // 异常代码对应Vector核的block索引
    ======    code in pc current 0x7b8 (serialNo:22)  // 当前异常发生的pc指针和调用api行为的序列号
    ======    #0 ${ASCEND_HOME_PATH}/compiler/tikcpp/tikcfw/impl/dav_c220/kernel_operator_data_copy_impl.h:103:9  // 以下为异常发生代码的调用栈，包含文件名、行号和列号
    ======    #1 ${ASCEND_HOME_PATH}/compiler/tikcpp/tikcfw/inner_interface/inner_kernel_operator_data_copy_intf.cppm:155:9
    ======    #2 ${ASCEND_HOME_PATH}/compiler/tikcpp/tikcfw/inner_interface/inner_kernel_operator_data_copy_intf.cppm:461:5
    ======    #3 out_of_bound/add_custom.cpp:21:5
    ```

    以上示例中，共有256个字节的访问发生踩踏，对GM上的“0x12c0c00150fc“地址进行访问时存在多核踩踏，且导致异常发生的指令对应于算子实现文件add\_custom.cpp的第21行。

-   <a id="zh-cn_topic_0000001820455825_li1322945295318"></a>非对齐访问

    昇腾处理器上包含多种类型的内存，当通过DMA进行访问时，不同类型的内存在不同处理器上有不同的最小访问粒度。当访问的内存地址与最小访问粒度不对齐时，会发生数据异常或AI Core异常等问题。访问对齐检测可以在对齐问题发生时输出对齐异常信息。

    ```
    ====== ERROR: misaligned access of size 13  // 异常的基本信息，包含发生对齐异常操作的字节数
    ======    at 0x6 on UB in add_custom_kernel   // 异常发生的内存位置信息，包含发生的核函数名、地址空间与内存地址
    ======    in block aiv(0) on device 0  // 异常代码对应Vector核的block索引
    ======    code in pc current 0x780 (serialNo:33)  // 当前异常发生的pc指针和调用api行为的序列号
    ======    #0 ${ASCEND_HOME_PATH}/compiler/tikcpp/tikcfw/impl/dav_c220/kernel_operator_data_copy_impl.h:103:9  // 以下为异常发生代码的调用栈，包含文件名、行号和列号
    ======    #1 ${ASCEND_HOME_PATH}/compiler/tikcpp/tikcfw/inner_interface/inner_kernel_operator_data_copy_intf.cppm:155:9
    ======    #2 ${ASCEND_HOME_PATH}/compiler/tikcpp/tikcfw/inner_interface/inner_kernel_operator_data_copy_intf.cppm:461:5
    ======    #3 illegal_align/add_custom.cpp:18:5
    ```

    以上示例中，共有针对13个字节的对齐异常访问，对UB上的“0x6“地址进行访问时存在对齐问题，且导致异常发生的指令对应于算子实现文件add\_custom.cpp的第18行。

    > [!NOTE] 说明       
    >不添加编译选项的情况下，异常报告将不会出现以下调用栈信息：
    >```
    >======    #0 ${ASCEND_HOME_PATH}/compiler/tikcpp/tikcfw/impl/dav_c220/kernel_operator_data_copy_impl.h:103:9  // 以下为异常发生代码的调用栈，包含文件名、行号和列号
    >======    #1 ${ASCEND_HOME_PATH}/compiler/tikcpp/tikcfw/inner_interface/inner_kernel_operator_data_copy_intf.cppm:155:9
    >======    #2 ${ASCEND_HOME_PATH}/compiler/tikcpp/tikcfw/inner_interface/inner_kernel_operator_data_copy_intf.cppm:461:5
    >======    #3 illegal_align/add_custom.cpp:18:5
    >```

-   <a id="zh-cn_topic_0000001820455825_li888655915315"></a>内存泄漏

    内存检测可以检测出Device侧的内存泄漏问题，这些问题通常是开发者没有正确释放使用AscendCL接口申请的内存导致的，由于内部存储（Local Memory）目前不存在内存分配的概念，因此内存泄漏只可能出现在GM上。通过指定命令行参数“--leak-check=yes“可以开启内存泄漏检测。

    ```
    ====== ERROR: LeakCheck: detected memory leaks     // 检测到内存泄漏
    ======    Direct leak of 100 byte(s)      // 具体每次的内存泄漏信息
    ======      at 0x124080013000 on GM allocated in add_custom.cpp:14 (serialNo:37)
    ======    Direct leak of 1000 byte(s)
    ======      at 0x124080014000 on GM allocated in add_custom.cpp:15 (serialNo:55)
    ====== SUMMARY: 1100 byte(s) leaked in 2 allocation(s)     // 全部内存泄漏的总结，包括发生泄漏的次数以及总共泄漏了多少字节等信息
    ```

    以上示例中，第一个内存泄漏信息包含了地址空间、内存地址、内存长度以及代码定位信息，代码定位信息指向具体分配这块内存的调用所在的文件名和行号。

-   <a id="zh-cn_topic_0000001820455825_li172874102543"></a>非法释放

    非法释放是指对一个未分配的地址或者已释放的地址进行了释放操作，一般发生在GM上。

    ```
    ====== ERROR: illegal free()     // 异常的基本信息，表明发生了非法释放异常
    ======    at 0x124080013000 on GM      // 异常发生的内存位置信息，包含发生的地址空间与内存地址
    ======    code in add_custom.cpp:84 (serialNo:63)    // 异常发生的代码定位信息,包含文件名、行号和调用api行为的序列号
    ```

    以上示例中，对GM上的“0x124080013000“地址进行了非法释放，且导致异常发生的指令对应于算子实现文件add\_custom.cpp的第84行。

-   <a id="li1789816476297"></a>分配内存未使用

    分配内存未使用是指算子运行时申请了内存，但直到算子运行完成，都没有使用该内存。该异常场景一般是算子使用了错误的内存或算子逻辑存在问题，一般发生在GM上。

    ```
    ====== WARNING: Unused memory of 1000 byte(s)     //异常的基本信息，表明检测到内存分配未使用异常
    ======    at 1240c0016000 on GM                    // 异常发生的内存位置信息,包含发生的地址空间与内存地址
    ======    code in add_custom.cpp:2 (serialNo:69)   //异常发生的代码定位信息,包含文件名、行号和调用api行为的序列号
    ====== SUMMARY: 1100byte(s) unused memory in 2 allocation(s) // 内存分配未使用的总结信息，包括未使用内存块的个数及字节等信息
    ```

-   昇腾910\_95 AI处理器simt单元异常信息

    SIMT架构下异常信息的展示会额外提供异常信息发生的线程位置，线程id从0开始计数，例如下方异常信息发生在线程idX=1 idY=0，idZ=0处。昇腾910\_95 AI处理器SIMT单元异常时，错误信息展示如下：

    ```
    ====== ERROR: illegal read of size 4     
    ======    at 0x300000018ffc on GM in vec_add                    
    ======    by thread (1,0,0) in block aiv(0-1) on device 0
    ======    code in pc current 0x178 (serialNo:16)
    ======    #0 ${ASCEND_HOME_PATH}/illegal_read_and_write_simt_gm_float/kernel.cpp:16:21
    ```

-   <a id="li0925115378"></a>线程间踩踏

    SIMT架构下多线程编程时，如果各线程对GM的访问未正确处理，可能导致多个线程同时向同一内存地址写入数据，从而引发线程间“内存踩踏”问题。线程间踩踏的检测机制与“多核踩踏”类似：假设某线程首次写入某块内存后，该内存即被视为由该线程独占。若其他线程尝试对该内存位置进行写操作，则会触发out of bounds异常。

    ```
    ====== WARNING: out of bounds of size 4
    ======    at 0x300000056000 on GM when writing data in vec_add
    ======    by thread (1,0,0) in block aiv(0) on device 0
    ======    code in pc current 0xd8 (serialNo:16)
    ======    #0 vec_add_simt.cpp:20:12
    ```

#### 竞争检测<a id="竞争检测"></a>

竞争检测用于解决在并行计算环境中内存访问竞争的问题。在昇腾处理器架构下，外部存储和内部存储通常被用作临时缓冲区保存正在处理的数据，外部存储或内部存储可以同时被多个流水访问，外部存储还可以被多个核访问，算子程序若没有正确处理核间、流水间或流水内的同步，就可能会导致数据竞争的问题。

**内存竞争类型<a id="zh-cn_topic_0000001773496140_section24411410155514"></a>**

内存竞争是指两个内存事件（其中至少有一个为写事件）尝试访问同一块内存时，出现不符合基于预期执行顺序的结果。这种异常会导致数据竞争，从而使程序的运行或输出取决于内存事件的实际执行顺序。竞争检测功能可识别以下三种典型的内存竞争：

**表 1**  内存竞争类型

<a id="zh-cn_topic_0000001773496140_table1944445964014"></a>
<table><thead align="left"><tr id="zh-cn_topic_0000001773496140_row444419596409"><th class="cellrowborder" valign="top" width="24.529999999999998%" id="mcps1.2.5.1.1"><p id="zh-cn_topic_0000001773496140_p108671312419"><a id="zh-cn_topic_0000001773496140_p108671312419"></a><a id="zh-cn_topic_0000001773496140_p108671312419"></a>异常名</p>
</th>
<th class="cellrowborder" valign="top" width="47.410000000000004%" id="mcps1.2.5.1.2"><p id="zh-cn_topic_0000001773496140_p1886713134116"><a id="zh-cn_topic_0000001773496140_p1886713134116"></a><a id="zh-cn_topic_0000001773496140_p1886713134116"></a>描述</p>
</th>
<th class="cellrowborder" valign="top" width="12%" id="mcps1.2.5.1.3"><p id="zh-cn_topic_0000001773496140_p186715119410"><a id="zh-cn_topic_0000001773496140_p186715119410"></a><a id="zh-cn_topic_0000001773496140_p186715119410"></a>位置</p>
</th>
<th class="cellrowborder" valign="top" width="16.06%" id="mcps1.2.5.1.4"><p id="zh-cn_topic_0000001773496140_p1386841154119"><a id="zh-cn_topic_0000001773496140_p1386841154119"></a><a id="zh-cn_topic_0000001773496140_p1386841154119"></a>支持地址空间</p>
</th>
</tr>
</thead>
<tbody><tr id="zh-cn_topic_0000001773496140_row194441959184018"><td class="cellrowborder" valign="top" width="24.529999999999998%" headers="mcps1.2.5.1.1 "><p id="zh-cn_topic_0000001773496140_p1086819118416"><a id="zh-cn_topic_0000001773496140_p1086819118416"></a><a id="zh-cn_topic_0000001773496140_p1086819118416"></a>Write-After-Write(WAW)</p>
</td>
<td class="cellrowborder" valign="top" width="47.410000000000004%" headers="mcps1.2.5.1.2 "><p id="zh-cn_topic_0000001773496140_p9419162995516"><a id="zh-cn_topic_0000001773496140_p9419162995516"></a><a id="zh-cn_topic_0000001773496140_p9419162995516"></a>当两个内存事件尝试向同一块内存写入时，可能存在这种异常，导致内存结果值取决于两个内存事件的实际访问顺序。</p>
</td>
<td class="cellrowborder" rowspan="3" valign="top" width="12%" headers="mcps1.2.5.1.3 "><p id="zh-cn_topic_0000001773496140_p786820174119"><a id="zh-cn_topic_0000001773496140_p786820174119"></a><a id="zh-cn_topic_0000001773496140_p786820174119"></a>Kernel</p>
</td>
<td class="cellrowborder" rowspan="3" valign="top" width="16.06%" headers="mcps1.2.5.1.4 "><p id="zh-cn_topic_0000001773496140_p9868714416"><a id="zh-cn_topic_0000001773496140_p9868714416"></a><a id="zh-cn_topic_0000001773496140_p9868714416"></a>GM、UB、L0{A,B,C}、L1</p>
</td>
</tr>
<tr id="zh-cn_topic_0000001773496140_row1244445954014"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="zh-cn_topic_0000001773496140_p886816111410"><a id="zh-cn_topic_0000001773496140_p886816111410"></a><a id="zh-cn_topic_0000001773496140_p886816111410"></a>Write-After-Read(WAR)</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="zh-cn_topic_0000001773496140_p20868713418"><a id="zh-cn_topic_0000001773496140_p20868713418"></a><a id="zh-cn_topic_0000001773496140_p20868713418"></a>当两个内存事件（一个事件执行读取操作，另一个事件执行写入操作）尝试访问同一块内存时，可能存在这种异常，即写操作事件实际在读操作事件之前执行完毕，并导致读取到的内存值并非预期起始值。</p>
</td>
</tr>
<tr id="zh-cn_topic_0000001773496140_row174451359184019"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="zh-cn_topic_0000001773496140_p686821154118"><a id="zh-cn_topic_0000001773496140_p686821154118"></a><a id="zh-cn_topic_0000001773496140_p686821154118"></a>Read-After-Write(RAW)</p>
</td>
<td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="zh-cn_topic_0000001773496140_p33131752135518"><a id="zh-cn_topic_0000001773496140_p33131752135518"></a><a id="zh-cn_topic_0000001773496140_p33131752135518"></a>当两个内存事件（一个事件执行读取操作，另一个事件执行写入操作）尝试访问同一块内存时，可能存在这种异常，即读操作事件实际在写操作事件之前执行完毕，并导致读取到的内存值还未更新。</p>
</td>
</tr>
</tbody>
</table>

当竞争检测识别出异常，用户就可以修改程序以确保该异常不再存在。在出现先写后读或先读后写的情况下，会根据serialNo大小顺序确定先后顺序，serialNo小的在PIPE\_S上先执行。

**启用竞争检测<a id="zh-cn_topic_0000001773496140_section12419444163310"></a>**

运行msSanitizer工具时，执行如下命令，启用竞争检测功能（racecheck）。

```sh
mssanitizer --tool=racecheck application    // application为用户程序
```

> [!NOTE] 说明       
>- 竞争检测不会执行内存错误检查，建议用户先运行[内存检测](#内存检测)，确保算子程序能够正常执行，没有运行异常。
>- 当用户程序运行完成后，界面将会打印异常报告，异常的具体含义见[竞争异常报告解析](#zh-cn_topic_0000001773496140_section1028444063620)。
>- 启动工具后，将会在当前目录下自动生成工具运行日志文件mssanitizer\__\{TIMESTAMP\}_\_\{_PID_\}.log。
>- 竞争检测不支持昇腾910\_95 AI处理器。

**竞争异常报告解析<a id="竞争异常报告解析"></a>**

竞争检测会输出一系列信息，详细说明有关算子各PIPE之间存在的内存数据竞争访问风险。

```
====== ERROR: Potential RAW hazard detected at GM in kernel_float on device 0:  // 竞争事件类型、异常内存块信息、竞争发生的核函数名
======    PIPE_MTE2 Write at RAW()+0x0 in block 0 (aiv) on device 0 at pc current 0xa98 (serialNo:14)  // 竞争事件的详细信息,包含该事件所在的PIPE、操作类型、内存访问起始地址、核类型、AICore信息以及代码执行的pc指针和调用api行为的序列号
======    #0 ${ASCEND_HOME_PATH}/compiler/tikcpp/tikcfw/impl/dav_c220/kernel_operator_data_copy_impl.h:58:9  // 以下为异常发生代码的调用栈，包含文件名、行号和列号
======    #1 ${ASCEND_HOME_PATH}/compiler/tikcpp/tikcfw/inner_interface/inner_kernel_operator_data_copy_intf.cppm:58:9
======    #2 ${ASCEND_HOME_PATH}/compiler/tikcpp/tikcfw/inner_interface/inner_kernel_operator_data_copy_intf.cppm:443:5
======    #3 Racecheck/add_custom.cpp:17:5
======    PIPE_MTE3 Read at RAW()+0x0 in block 0 (aiv) on device 0 at pc current 0xad4 (serialNo:17)
======    #0 ${ASCEND_HOME_PATH}/compiler/tikcpp/tikcfw/impl/dav_c220/kernel_operator_data_copy_impl.h:103:9
======    #1 ${ASCEND_HOME_PATH}/compiler/tikcpp/tikcfw/inner_interface/inner_kernel_operator_data_copy_intf.cppm:155:9
======    #2 ${ASCEND_HOME_PATH}/compiler/tikcpp/tikcfw/inner_interface/inner_kernel_operator_data_copy_intf.cppm:461:5
======    #3 Racecheck/add_custom.cpp:22:5
```

以上示例中表示了AICore 0的Vector核内部中存在对UB的先写后读竞争风险，PIPE\_MTE2流水中存在对“0x0“地址的写入操作事件，该操作对应算子实现文件add\_custom.cpp中的第17行，PIPE\_MTE3流水中存在对“0x0“地址的读取操作事件，该操作对应算子实现文件add\_custom.cpp中的第22行。

#### 未初始化检测<a id="未初始化检测"></a>

未初始化检测功能是一种重要的内存安全保护机制，旨在识别并防止由于使用未初始化的变量而导致的内存异常。

**支持的未初始化异常类型<a id="zh-cn_topic_0000001820455825_section1047315213512"></a>**

**表 1**  未初始化异常类型

<a id="zh-cn_topic_0000001820455825_table1944445964014"></a>
<table><thead align="left"><tr id="zh-cn_topic_0000001820455825_row444419596409"><th class="cellrowborder" valign="top" width="16.55%" id="mcps1.2.5.1.1"><p id="zh-cn_topic_0000001820455825_p108671312419"><a id="zh-cn_topic_0000001820455825_p108671312419"></a><a id="zh-cn_topic_0000001820455825_p108671312419"></a>异常名</p>
</th>
<th class="cellrowborder" valign="top" width="53.339999999999996%" id="mcps1.2.5.1.2"><p id="zh-cn_topic_0000001820455825_p1886713134116"><a id="zh-cn_topic_0000001820455825_p1886713134116"></a><a id="zh-cn_topic_0000001820455825_p1886713134116"></a>描述</p>
</th>
<th class="cellrowborder" valign="top" width="15.4%" id="mcps1.2.5.1.3"><p id="zh-cn_topic_0000001820455825_p186715119410"><a id="zh-cn_topic_0000001820455825_p186715119410"></a><a id="zh-cn_topic_0000001820455825_p186715119410"></a>位置</p>
</th>
<th class="cellrowborder" valign="top" width="14.71%" id="mcps1.2.5.1.4"><p id="zh-cn_topic_0000001820455825_p1386841154119"><a id="zh-cn_topic_0000001820455825_p1386841154119"></a><a id="zh-cn_topic_0000001820455825_p1386841154119"></a>支持地址空间</p>
</th>
</tr>
</thead>
<tbody><tr id="row183412266287"><td class="cellrowborder" valign="top" width="16.55%" headers="mcps1.2.5.1.1 "><p id="p1237965017374"><a id="p1237965017374"></a><a id="p1237965017374"></a><a href="#未初始化异常报告解析">未初始化</a></p>
</td>
<td class="cellrowborder" valign="top" width="53.339999999999996%" headers="mcps1.2.5.1.2 "><p id="p16380105010373"><a id="p16380105010373"></a><a id="p16380105010373"></a>内存申请后为未初始化状态，未对内存进行写入，直接读取未初始化的值导致的异常。</p>
</td>
<td class="cellrowborder" valign="top" width="15.4%" headers="mcps1.2.5.1.3 "><p id="p8380125043712"><a id="p8380125043712"></a><a id="p8380125043712"></a>Kernel、Host</p>
</td>
<td class="cellrowborder" valign="top" width="14.71%" headers="mcps1.2.5.1.4 "><p id="p177116196401"><a id="p177116196401"></a><a id="p177116196401"></a>GM、UB、L1、L0{ABC}、栈空间</p>
</td>
</tr>
</tbody>
</table>

**启用未初始化检测<a id="zh-cn_topic_0000001820455825_section1371111444516"></a>**

运行msSanitizer工具时，执行如下命令，启用未初始化检测功能**（initcheck）。**

```
mssanitizer --tool=initcheck application   // application为用户程序
```

> [!NOTE] 说明       
>-   启动工具后，将会在当前目录下自动生成工具运行日志文件mssanitizer\__\{TIMESTAMP\}_\_\{_PID_\}.log。
>-   当用户程序运行完成后，界面将会打印异常报告，异常的具体含义请参见[未初始化异常报告解析](#未初始化异常报告解析)。
>-   由于硬件限制，某些指令仅支持以Block形式进行数据搬运。当参与计算的实际数据量不是Block大小的整数倍时，可能会不可避免地带入部分无效数据（即“脏数据”），这可能导致工具报告初始化异常，用户需自行判断这些“脏数据”是否会影响计算结果。
>-   未初始化检测不支持昇腾910\_95 AI处理器。

**未初始化异常报告解析<a id="未初始化异常报告解析"></a>**

未初始化检测异常报告会输出多种不同类型的异常信息，以下将对一些简单的异常信息示例进行说明，帮助用户解读异常报告中的信息。

未初始化的异常场景一般是算子读取了已申请但未初始化的内存，发生在GM、UB、L1、L0\{ABC\}、栈空间上。

```
====== ERROR: uninitialized read of size 224  // 异常的基本信息，包含读取的未初始化字节数
======    at 0x12c0c0015000 on GM in add_custom_kernel  // 异常发生的内存位置信息，包含发生的核函数名、地址空间与内存地址，此处的内存地址指一次内存访问中的首地址
======    in block aiv(0) on device 0  // 异常代码对应Vector核的block索引
======    code in pc current 0x77c (serialNo:10) // 当前异常发生的pc指针和调用api行为的序列号
======    #0 ${ASCEND_HOME_PATH}/compiler/tikcpp/tikcfw/impl/dav_c220/kernel_operator_data_copy_impl.h:58:9  // 以下为异常发生代码的调用栈，包含文件名、行号和列号
======    #1 ${ASCEND_HOME_PATH}/compiler/tikcpp/tikcfw/inner_interface/inner_kernel_operator_data_copy_intf.cppm:58:9
======    #2 ${ASCEND_HOME_PATH}/compiler/tikcpp/tikcfw/inner_interface/inner_kernel_operator_data_copy_intf.cppm:443:5
======    #3 uninitialized_read/add_custom.cpp:18:5
```

#### 同步检测<a id="同步检测"></a>

在Ascend C算子开发过程中，必须成对使用SetFlag和WaitFlag，同步检测功能用于找出算子中未配对的SetFlag指令。

若存在多余SetFlag指令，不会直接导致当前算子的竞争问题，却会改变硬件计数器的状态，进而可能导致后续算子的同步指令配对错误。若这些后续算子本身不存在竞争，竞争检测也不会报错，但前序算子的计数器变化可能导致实际竞争情况的发生，通过同步检测功能，能够有效识别前序算子中的多余SetFlag指令问题，避免后续算子受影响。

> [!NOTE] 说明       
>-   同步检测单独启用时不会执行内存检测和竞争检测，因此建议用户先使用[内存检测](#内存检测)和[竞争检测](#竞争检测)，若竞争检测无异常报告，但算子存在竞争现象时，再考虑使用同步检测对前序算子进行检查。
>-   若存在多余WaitFlag指令，将会导致当前算子的后续指令被阻塞，从而出现算子运行停滞的现象。此时，开发者无需工具提示，便可自行发现问题。

**支持的同步异常类型<a id="zh-cn_topic_0000001820455825_section1047315213512"></a>**

**表 1**  同步异常类型

<a id="zh-cn_topic_0000001820455825_table1944445964014"></a>
<table><thead align="left"><tr id="zh-cn_topic_0000001820455825_row444419596409"><th class="cellrowborder" valign="top" width="19.400000000000002%" id="mcps1.2.4.1.1"><p id="zh-cn_topic_0000001820455825_p108671312419"><a id="zh-cn_topic_0000001820455825_p108671312419"></a><a id="zh-cn_topic_0000001820455825_p108671312419"></a>异常名</p>
</th>
<th class="cellrowborder" valign="top" width="62.540000000000006%" id="mcps1.2.4.1.2"><p id="zh-cn_topic_0000001820455825_p1886713134116"><a id="zh-cn_topic_0000001820455825_p1886713134116"></a><a id="zh-cn_topic_0000001820455825_p1886713134116"></a>描述</p>
</th>
<th class="cellrowborder" valign="top" width="18.060000000000002%" id="mcps1.2.4.1.3"><p id="zh-cn_topic_0000001820455825_p186715119410"><a id="zh-cn_topic_0000001820455825_p186715119410"></a><a id="zh-cn_topic_0000001820455825_p186715119410"></a>位置</p>
</th>
</tr>
</thead>
<tbody><tr id="row183412266287"><td class="cellrowborder" valign="top" width="19.400000000000002%" headers="mcps1.2.4.1.1 "><p id="p1237965017374"><a id="p1237965017374"></a><a id="p1237965017374"></a>同步检测</p>
</td>
<td class="cellrowborder" valign="top" width="62.540000000000006%" headers="mcps1.2.4.1.2 "><p id="p16562138547"><a id="p16562138547"></a><a id="p16562138547"></a>算子中存在未配对的SetFlag同步指令时，虽然对当前算子的功能没有直接影响，却会引发计数器状态错误。可能会扰乱后续算子的同步指令配对，进而影响后续算子的计算精度。</p>
</td>
<td class="cellrowborder" valign="top" width="18.060000000000002%" headers="mcps1.2.4.1.3 "><p id="p8380125043712"><a id="p8380125043712"></a><a id="p8380125043712"></a>Kernel</p>
</td>
</tr>
</tbody>
</table>

**启用同步检测<a id="zh-cn_topic_0000001820455825_section1371111444516"></a>**

运行msSanitizer工具时，执行如下命令，启用同步检测功能（synccheck）。

```
mssanitizer --tool=synccheck application   // application为用户程序
```

> [!NOTE] 说明       
>-   启动工具后，将会在当前目录下自动生成工具运行日志文件mssanitizer\__\{TIMESTAMP\}_\_\{_PID_\}.log。
>-   当用户程序运行完成后，界面将会打印异常报告，异常的具体含义请参见[同步异常报告解析](#同步异常报告解析)。
>-   同步检测不支持昇腾910\_95 AI处理器。

**同步异常报告解析<a id="同步异常报告解析"></a>**

同步检测异常报告会依次列出每个算子中未配对的SetFlag指令的相关信息，包括源流水和目标流水以及具体位置。

```
====== WARNING: Unpaired set_flag instructions detected  // 提示检出未配对的set_flag指令
======    from PIPE_S to PIPE_MTE3 in kernel  // 标识从PIPE_S到PIPE_MTE3的同步，PIPE_MTE3等待PIPE_S
======    in block aiv(0) on device 1  // 异常代码对应Vector核的block索引和设备号，此处为0核1卡
======    code in pc current 0x2c94 (serialNo:31) // 当前异常发生的pc指针和调用api行为的序列号
======    #0 /home/Ascend/compiler/tikcpp/tikcfw/impl/kernel_event.h:785:13  // 以下为异常发生代码的调用栈，包含文件名、行号和列号
======    #1 /home/Ascend/compiler/tikcpp/tikcfw/interface/kernel_common.h:150:5
======    #2 /home/test/ascendc_test_syncall/kernel.cpp:26:9
```

### 输出说明<a id="ZH-CN_TOPIC_0000002509279392"></a>

**表 1**  异常检测使用示例输出说明

<a id="table1654092618346"></a>
<table><thead align="left"><tr id="row754022613410"><th class="cellrowborder" valign="top" width="15.07%" id="mcps1.2.4.1.1"><p id="p128023193612"><a id="p128023193612"></a><a id="p128023193612"></a>示例名称</p>
</th>
<th class="cellrowborder" valign="top" width="38.690000000000005%" id="mcps1.2.4.1.2"><p id="p854014265348"><a id="p854014265348"></a><a id="p854014265348"></a>输出内容</p>
</th>
<th class="cellrowborder" valign="top" width="46.239999999999995%" id="mcps1.2.4.1.3"><p id="p175402268344"><a id="p175402268344"></a><a id="p175402268344"></a>说明</p>
</th>
</tr>
</thead>
<tbody><tr id="row554062612349"><td class="cellrowborder" valign="top" width="15.07%" headers="mcps1.2.4.1.1 "><p id="p202801731173613"><a id="p202801731173613"></a><a id="p202801731173613"></a>内存检测</p>
</td>
<td class="cellrowborder" valign="top" width="38.690000000000005%" headers="mcps1.2.4.1.2 "><p id="p19540162618340"><a id="p19540162618340"></a><a id="p19540162618340"></a><a href="#内存异常报告解析">内存异常报告解析</a></p>
</td>
<td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.2.4.1.3 "><p id="p75401726133411"><a id="p75401726133411"></a><a id="p75401726133411"></a>内存检测异常报告会输出多种不同类型的异常信息，对一些简单的异常信息示例进行说明，帮助用户解读异常报告中的信息。</p>
</td>
</tr>
<tr id="row8541122623413"><td class="cellrowborder" valign="top" width="15.07%" headers="mcps1.2.4.1.1 "><p id="p10280331153615"><a id="p10280331153615"></a><a id="p10280331153615"></a>竞争检测</p>
</td>
<td class="cellrowborder" valign="top" width="38.690000000000005%" headers="mcps1.2.4.1.2 "><p id="p1654117262342"><a id="p1654117262342"></a><a id="p1654117262342"></a><a href="#竞争异常报告解析">竞争异常报告解析</a></p>
</td>
<td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.2.4.1.3 "><p id="zh-cn_topic_0000001773496140_p154184213617"><a id="zh-cn_topic_0000001773496140_p154184213617"></a><a id="zh-cn_topic_0000001773496140_p154184213617"></a>竞争检测会输出一系列信息，详细说明有关算子各PIPE之间存在的内存数据竞争访问风险。</p>
</td>
</tr>
<tr id="row172232595343"><td class="cellrowborder" valign="top" width="15.07%" headers="mcps1.2.4.1.1 "><p id="p1028013112360"><a id="p1028013112360"></a><a id="p1028013112360"></a>未初始化检测</p>
</td>
<td class="cellrowborder" valign="top" width="38.690000000000005%" headers="mcps1.2.4.1.2 "><p id="p9224135917346"><a id="p9224135917346"></a><a id="p9224135917346"></a><a href="#未初始化异常报告解析">未初始化异常报告解析</a></p>
<p id="p123412429412"><a id="p123412429412"></a><a id="p123412429412"></a></p>
</td>
<td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.2.4.1.3 "><p id="p52246594342"><a id="p52246594342"></a><a id="p52246594342"></a>未初始化检测异常报告会输出多种不同类型的异常信息，对一些简单的异常信息示例进行说明，帮助用户解读异常报告中的信息。</p>
</td>
</tr>
<tr id="row1654142610342"><td class="cellrowborder" valign="top" width="15.07%" headers="mcps1.2.4.1.1 "><p id="p172801531163616"><a id="p172801531163616"></a><a id="p172801531163616"></a>同步检测</p>
</td>
<td class="cellrowborder" valign="top" width="38.690000000000005%" headers="mcps1.2.4.1.2 "><p id="p1254172616342"><a id="p1254172616342"></a><a id="p1254172616342"></a><a href="
#同步异常报告解析">同步异常报告解析</a></p>
</td>
<td class="cellrowborder" valign="top" width="46.239999999999995%" headers="mcps1.2.4.1.3 "><p id="zh-cn_topic_0000001820455825_p11959811105314"><a id="zh-cn_topic_0000001820455825_p11959811105314"></a><a id="zh-cn_topic_0000001820455825_p11959811105314"></a>同步检测异常报告会依次列出每个算子中未配对的SetFlag指令的相关信息，包括源流水和目标流水以及具体位置。</p>
</td>
</tr>
</tbody>
</table>

## 输出结果文件说明<a id="ZH-CN_TOPIC_0000002541039379"></a>

**结果件说明<a id="section25511327164711"></a>**

<a id="table7482194643919"></a>
<table><thead align="left"><tr id="row0483164673915"><th class="cellrowborder" valign="top" width="37.78%" id="mcps1.1.3.1.1"><p id="p14483246153911"><a id="p14483246153911"></a><a id="p14483246153911"></a>结果件名称</p>
</th>
<th class="cellrowborder" valign="top" width="62.22%" id="mcps1.1.3.1.2"><p id="p8483114620391"><a id="p8483114620391"></a><a id="p8483114620391"></a>说明</p>
</th>
</tr>
</thead>
<tbody><tr id="row1848364683919"><td class="cellrowborder" valign="top" width="37.78%" headers="mcps1.1.3.1.1 "><p id="p20483154615397"><a id="p20483154615397"></a><a id="p20483154615397"></a>mssanitizer_<em id="i3676027172715"><a id="i3676027172715"></a><a id="i3676027172715"></a>{TIMESTAMP}</em>_{<em id="i1492020148272"><a id="i1492020148272"></a><a id="i1492020148272"></a>PID</em>}.log</p>
</td>
<td class="cellrowborder" valign="top" width="62.22%" headers="mcps1.1.3.1.2 "><p id="p748344663911"><a id="p748344663911"></a><a id="p748344663911"></a>msSanitizer工具运行过程中，在mindstudio_sanitizer_log目录下生成的工具日志，<em id="i1666765818447"><a id="i1666765818447"></a><a id="i1666765818447"></a>TIMESTAMP</em>为当前时间戳，<em id="i206338381712"><a id="i206338381712"></a><a id="i206338381712"></a>PID</em>为当前检测工具的<em id="i1477574418505"><a id="i1477574418505"></a><a id="i1477574418505"></a>PID</em>。</p>
</td>
</tr>
<tr id="row6483174683917"><td class="cellrowborder" valign="top" width="37.78%" headers="mcps1.1.3.1.1 "><p id="p5331113143713"><a id="p5331113143713"></a><a id="p5331113143713"></a>kernel.{<em id="i1791553123017"><a id="i1791553123017"></a><a id="i1791553123017"></a>PID</em>}.o</p>
</td>
<td class="cellrowborder" valign="top" width="62.22%" headers="mcps1.1.3.1.2 "><p id="p859219217437"><a id="p859219217437"></a><a id="p859219217437"></a>msSanitizer工具运行过程中，会在当前路径下生成的算子缓存文件。其中，<em id="i1150151944513"><a id="i1150151944513"></a><a id="i1150151944513"></a>PID</em>为当前使用的检测工具的<em id="i4341369518"><a id="i4341369518"></a><a id="i4341369518"></a>PID</em>，该算子缓存文件用于解析异常调用栈。</p>
<a id="ul6440143019436"></a><a id="ul6440143019436"></a><ul id="ul6440143019436"><li>正常情况下，msSanitizer工具退出时会自动清理该算子缓存文件。</li><li>当msSanitizer工具异常退出（如被用户<span class="uicontrol" id="zh-cn_topic_0000001826702481_uicontrol44351721535"><a id="zh-cn_topic_0000001826702481_uicontrol44351721535"></a><a id="zh-cn_topic_0000001826702481_uicontrol44351721535"></a>“CTRL+C”</span>中止）时，该算子缓存文件会保留在文件系统中。因为该算子缓存文件包含算子的调试信息，建议限制其他用户对此文件的访问权限，并在检测工具运行完成后及时删除。</li></ul>
</td>
</tr>
<tr id="row4316202162419"><td class="cellrowborder" valign="top" width="37.78%" headers="mcps1.1.3.1.1 "><p id="p23169213249"><a id="p23169213249"></a><a id="p23169213249"></a>tmp_{<em id="i1282093165514"><a id="i1282093165514"></a><a id="i1282093165514"></a>PID</em>}_{<em id="i198795244558"><a id="i198795244558"></a><a id="i198795244558"></a>TIMESTAMP</em>}</p>
</td>
<td class="cellrowborder" valign="top" width="62.22%" headers="mcps1.1.3.1.2 "><p id="p122868425496"><a id="p122868425496"></a><a id="p122868425496"></a>msSanitizer工具运行过程中，会在当前路径下生成的临时文件夹。其中，PID为当前使用的检测工具的PID，TIMESTAMP为当前时间戳，该文件夹用于生成算子Kernel二进制。</p>
<a id="ul181031755144917"></a><a id="ul181031755144917"></a><ul id="ul181031755144917"><li>正常情况下，msSanitizer工具退出时会自动清理该文件夹。</li><li>当通过环境变量export INJ_LOG_LEVEL=0开启DEBUG等级日志，或工具异常退出（如被用户“CTRL+C”中止）时，该文件夹会保留在文件系统中，方便用户调测使用。因为该文件夹包含算子的调试信息，建议限制其他用户对此文件的访问权限，并在调测完成后及时删除。</li></ul>
</td>
</tr>
</tbody>
</table>

