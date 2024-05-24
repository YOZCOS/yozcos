### HeMem论文解析

**论文标题**: HeMem: Scalable Tiered Memory Management for Big Data Applications and Real NVM

**作者**: Amanda Raybuck, Tim Stamler, Wei Zhang, Mattan Erez, Simon Peter

**所属机构**: The University of Texas at Austin, Microsoft

**发表会议**: ACM SIGOPS 28th Symposium on Operating Systems Principles (SOSP ’21)

**核心贡献**:
HeMem是一个为商业可用的非易失性内存（NVM）和使用它的大数据应用程序从头设计的分层主存管理系统。HeMem异步地管理分层内存，批量处理内存访问跟踪、迁移和相关的TLB同步开销。它通过CPU事件采样而非页表来监控应用程序的内存使用情况，这使得HeMem能够扩展到TB级别的内存，保持小的和短暂的数据结构在快速内存中，并根据访问模式分配稀缺的、不对称的NVM带宽。此外，HeMem通过将每个应用程序的内存管理策略放在用户级来提供灵活性。

**关键概念**:
1. **分层内存管理（Tiered Memory Management）**: HeMem通过管理DRAM和NVM之间的内存层次结构来优化性能和容量。
2. **异步内存访问跟踪**: 使用基于CPU事件的采样来减少CPU开销，并提高内存访问跟踪的准确性。
3. **用户级内存管理策略**: 允许云操作员和用户在不修改操作系统的情况下实现每个应用程序的内存管理策略。

**系统设计**:
- **内存访问采样**: HeMem利用CPU事件（如PEBS）来异步处理内存访问事件，减少CPU开销。
- **内存管理**: 采用DMA（直接内存访问）来异步迁移内存，减少对处理器负载和存储器性能的影响。
- **数据可扩展性意识**: 识别并保留小型和短暂的数据结构在DRAM中，以提高内存访问性能。

**工作流程**:
1. **内存分配与放置**: HeMem根据其策略在DRAM和NVM之间分配内存，并跟踪虚拟地址到文件偏移的映射。
2. **内存迁移**: 通过用户故障文件描述符（userfaultfd）和DMA引擎或迁移线程来异步迁移内存。
3. **页面错误处理**: 使用userfaultfd来处理页面错误，并根据需要提供页面给应用程序。

**性能优化**:
HeMem通过以下方式实现性能优化：
- **减少NVM磨损**: 通过减少对NVM的写入次数，延长NVM设备的使用寿命。
- **提高吞吐量和降低延迟**: 在Silo数据库和GAP图处理基准测试中，HeMem提供了比硬件、Linux Nimble和X-Mem更高的吞吐量和更低的延迟。

**实验结果**:
在Intel Optane DC NVM系统上，HeMem在GAP图处理基准测试中提供了高达50%的运行时间减少，在Silo内存数据库的TPC-C上提供了13%的吞吐量提升，在键值存储的性能隔离下提供了16%的尾部延迟降低，并且比下一个最佳解决方案减少了高达10倍的NVM磨损，所有这些都没有对应用程序进行修改。

**总结**:
HeMem是第一个为商业NVM从头设计的软件基础的分层内存管理系统。它通过先进的策略支持，针对各种内存访问和分配模式以及优先级，动态地管理分层内存，无需CPU开销。HeMem在处理大型数据集时，提供了显著的性能提升和NVM设备的磨损减少，证明了其在大数据应用和实际NVM环境中的有效性和可扩展性。