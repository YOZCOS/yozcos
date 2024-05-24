### TMTS论文解析

**论文标题**: Towards an Adaptable Systems Architecture for Memory Tiering at Warehouse-Scale

**作者**: Padmapriya Duraisamy, Wei Xu, Scott Hare, Ravi Rajwar, David Culler, Zhiyi Xu, Jianing Fan, Christopher Kennelly, Bill McCloskey, Danijela Mijailovic, Brian Morris, Chiranjit Mukherjee, Jingliang Ren, Greg Thelen, Paul Turner, Carlos Villavieja, Parthasarathy Ranganathan, Amin Vahdat

**所属机构**: Google, USA; University of California at Berkeley

**发表会议**: ASPLOS ’23

**核心贡献**:
TMTS（Transparent Memory Tiering System）是一个应用透明的内存分层管理系统，它实现了一个自适应的、硬件引导的架构，用于动态优化对各种直接寻址内存层的访问，无需发生故障。TMTS已经在大规模生产环境中部署了两年，为数千个生产服务提供支持，成功地在多样化的应用类别中满足了服务级别目标（SLOs）。

**关键概念**:
1. **内存分层（Memory Tiering）**: 通过将部分传统DRAM替换为成本较低但速度较慢的内存媒介，创建了一个分层内存系统，其中两个层都是直接可寻址和可缓存的。
2. **应用透明（Application-Transparent）**: 系统在管理内存层次时无需应用程序的参与或修改，对应用是透明的。
3. **硬件引导（Hardware-Guided）**: 系统的管理策略受到硬件特性的引导和影响。

**系统设计**:
- **自适应硬件引导架构**: TMTS利用硬件特性来动态优化内存访问，通过硬件辅助的事件分析来确定哪些页面应该被提升或降级。
- **无故障页面管理**: 系统设计避免了在页面迁移过程中发生故障，确保了服务的连续性和稳定性。

**工作流程**:
1. **页面放置管理**: 系统主动管理页面放置和相关的虚拟到物理映射，以保持最频繁访问的（热）页面在tier1，最不频繁访问的（冷）页面在tier2。
2. **页面迁移**: 系统使用特定的度量标准来交付强大的性能，并满足各种SLOs，通过软件和硬件层的合作来透明地识别和迁移应用程序页面。
3. **性能和利用率优化**: 系统通过优化机器级度量标准，平衡了复杂的高级车队范围应用性能和利用率目标。

**性能优化**:
TMTS通过以下方式实现性能优化：
- **性能影响限制**: 在替换25%的DRAM与更慢的媒介的情况下，维持了不到5%的整体性能下降。
- **应用特定策略**: 允许根据应用的具体需求定制内存管理策略。

**实验结果**:
TMTS在生产环境中的成功部署证明了其有效性。它通过硬件辅助的事件分析，实现了高性能要求下的有效策略，并展示了如何通过自适应策略减少性能影响的尾部。

**总结**:
TMTS是Google开发的一项创新技术，它为大规模计算环境中的内存分层提供了一种有效的解决方案。通过应用透明的设计和硬件引导的架构，TMTS能够在保持高性能的同时，显著降低内存成本。这项工作的实践和研究成果为未来在类似环境中部署和优化内存分层系统提供了宝贵的经验和见解。