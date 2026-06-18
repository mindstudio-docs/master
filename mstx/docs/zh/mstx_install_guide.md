# MindStudio Tools Extension Library安装指南

# 安装说明
MindStudio Tools Extension Library（工具扩展接口库，msTX）介绍mstx打点接口。可以自定义采集时间段或者关键函数的开始和结束时间点，识别关键函数或迭代等信息，对性能和算子问题快速定界。本文主要介绍msTX工具的安装方法。  

# 安装前准备
## 项目构建

由于本项目中的代码依赖python3的头文件，因此需要编译环境中安装python3-dev包，可通过如下命令执行：
```
apt-get install python3-dev
```

可以通过如下命令构建whl包：
```
mkdir build
cd build
cmake .. && make -j8 install 
```
也可以通过一键式脚本来执行：
```
python build.py
```

# 安装步骤

## 安装whl包
```
cd output
pip install mstx-xxxxx.whl
```

## 卸载
卸载则通过如下命令卸载：
```
pip uninstall mstx-xxxxx.whl 
```

## 升级
如需使用whl包替换运行环境原有已安装的whl包，执行如下安装操作：
```
pip install mstx-xxxxx.whl --force-reinstall
```
安装过程中，若提示是否替换原有安装包：
输入"y"，则安装包会自动完成升级操作。

## UT测试
可以通过一键式脚本来执行C/CPP/PYTHON代码的UT测试：
```
python build.py test
```
注：需要环境中提前安装pytest以执行python测试