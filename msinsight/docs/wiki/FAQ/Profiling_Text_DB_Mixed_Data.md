# profiling db跟text数据混合，如何只看text数据

## 问题现象

### 为什么泳道看着不习惯

想要这样的👇

![image.png](figures/Profiling_Text_DB_Mixed_Data/674afda0-2977-4cdd-b0df-c6adf33ba740.png)

但得到了这样的👇

![image.png](figures/Profiling_Text_DB_Mixed_Data/b1669ac4-44f8-4e0e-ac19-72963d7d2b2f.png)

### 为什么常见的csv交付件不见了

想要这样的：

![image.png](figures/Profiling_Text_DB_Mixed_Data/23f7f0f4-0e27-45aa-9a48-e31694abd93e.png)

但得到了这样的：

![image.png](figures/Profiling_Text_DB_Mixed_Data/8b7b6f87-f92c-461e-a9d0-03c1353d9e9c.png)

## 原因

profiling采集交付件分为**Text类型**与**DB类型**，8.1.RC1之后的CANN包Profiling采集时，若选择输出Text交付件，会同时生成Text与DB类型数据，Insight会优先识别为DB数据。

DB数据的优点是磁盘占用小，文件解析加载更快。但部分用户可能不习惯新的DB交付件，和新的泳道排布关系，想要恢复为text场景。

## 解决方式

在数据目录搜索并删除所有DB交付件，包括ascend_pytorch_profiler_x.db、analysis.db文件，则Insight只会识别Text数据。

![image.png](figures/Profiling_Text_DB_Mixed_Data/6d0ff384-aeb4-4944-bcbd-3a90ab33e7de.png)

![image.png](figures/Profiling_Text_DB_Mixed_Data/d3e1ab5a-a2be-4dd2-afdf-0fe84b8d66a2.png)
