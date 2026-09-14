# Overview

As the scale of AI models continues to expand and application scenarios become increasingly complex, Ascend AI computing platforms face many challenges during training and deployment, such as inefficient host-device collaboration, performance deterioration of important operators, increased communication latency, and low model delivery efficiency. As a result, the performance challenge of deep learning systems has shifted from improving computing capability power to optimizing the collaboration efficiency between hardware platforms, software stacks, communication mechanisms, and model architectures.

To address such needs, it is urgent to establish a systematic performance analysis and tuning framework, covering profile data collection, operator tuning, scheduling policy adjustment, communication mechanism enhancement, and model compilation and deployment. Performance tuning is crucial for enhancing the competitiveness and user satisfaction of Ascend products, and serves as a key driver for the ongoing advancement of Ascend software and hardware platforms. By optimizing training and inference tasks end-to-end and systematically, execution efficiency for various models can be greatly improved, accelerating development and iteration cycles.

## Performance Tuning Principles

Performance tuning should follow the principles of operator-first strategy, Ascend affinity tuning strategy, and model design strategy. For details, see [Table 1](#ZH-CN_TOPIC_0000002503927264__table37106351015).

**Table 1** Performance tuning principles <a name="ZH-CN_TOPIC_0000002503927264__table37106351015"></a>

| Principle        | Description                                                        |
| ---------------- | ------------------------------------------------------------ |
| Operator first        | Operator capabilities are the foundation of performance. Strong operator capabilities are essential to achieving high performance on both single-node systems and clusters.|
| Ascend affinity tuning strategy| Based on a highly parallel architecture, Ascend AI processors have been optimized in terms of instruction-level parallelism and data transfer efficiency. For example, in data access unit design, a cache line size of Ascend reaches 512 Byte, which is significantly larger than the commonly used 32-byte size in the industry. This improves bandwidth utilization for large-granularity data transfers and reduces memory access latency. Therefore, during programming and operator tuning, align hardware features to improve data locality, enabling each memory operation to process more data and fully leverage high bandwidth and throughput.|
| Model design strategy    | Models should use matrix operations as much as possible and fully reuse the AI Core (Cube Unit) to improve the overall efficiency.|

## Performance Tuning Options

Performance tuning can be performed from four dimensions: computing, communication, delivery, and serving scheduling. For details, see [Table 2](#ZH-CN_TOPIC_0000002503927264__table986215587818)

**Table 2** Performance tuning directions <a name="ZH-CN_TOPIC_0000002503927264__table986215587818"></a>

| Dimension      | Tuning Direction                                                    |
| ---------- | ------------------------------------------------------------ |
| Compute      | • Ensure operator performance meets expectations (including matrix multiplication computing utilization and MTE pipeline usage).<br>• The computation is centralized on AI Cores and requires fully utilization of cube resources.<br>• Eliminate AI CPU operators and non-affinity operators, and optimize the algorithm logic.<br>• Make full use of fused operators.|
| Communication      | • The communication bandwidth meets the expectation, and no communication retransmission occurs.<br>• The communication time of each rank is balanced, and there is no obvious fast or slow rank.<br>• Computing and communication are parallel to overlap communication time as much as possible.|
| Delivery      | • Free time should be minimized.<br>• Computing overlaps the scheduling time.<br>• The I/O and memory faults are eliminated.|
| Serving inference| • The latency of model inference is close to that of a pure model.<br>• CPU tasks among batches should be minimized.<br>• Optimize the scheduling parameters and batch upper limit to maximize the throughput when the graphics memory is fully occupied under the latency constraint.|
