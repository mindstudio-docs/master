# MindStudio Ops Generator安装指南

# 安装说明
MindStudio Ops Generator（算子工程创建，msOpGen）是算子开发效率提升工具，提供模板工程生成能力，简化算子工程搭建并辅助算子测试验证。MindStudio Ops System Test（算子测试，msOpST）是算子开发效率提升工具，旨在真实的硬件环境中，对算子的输入输出进行测试，以验证算子的功能是否正确。本文主要介绍msOpGen和msOpST工具的安装方法。  

# 安装前准备

## 安装python依赖
```
pip install -r requirements.txt
```

## 生成whl包
生成的whl包位于output目录，包含msopgen和msopst两个whl包

```
python build.py
```


# 安装步骤
## 安装whl包
```
cd output
pip install msopgen-xxxxx.whl
pip install msopst-xxxxx.whl
```

## 卸载
卸载则通过如下命令卸载：
```
pip uninstall msopgen-xxxxx.whl 
pip uninstall msopst-xxxxx.whl
```

## 升级
如需使用whl包替换运行环境原有已安装的whl包，执行如下安装操作：
```
pip install msopgen-xxxxx.whl --force-reinstall
pip install msopst-xxxxx.whl --force-reinstall
```
安装过程中，若提示是否替换原有安装包：
输入"y"，则安装包会自动完成升级操作。

## 运行ut、st测试用例
`3.7 <= python版本要求 <=3.10`
```shell
source /path/to/Ascend/cann/set_env.sh
```

测试报告在output目录
```
python build.py test
```

