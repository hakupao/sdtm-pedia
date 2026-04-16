<!-- chain: B (工作日志链)
  修改本文件后，必须检查:
  → meta/worklog.md                    (记录工作内容)
  → progress.json                      (更新状态字段)
  → ../docs/PROGRESS.md                (更新看板)
-->

# Session 记录: RAG + 知识图谱方案设计

> 日期: 2026-04-16
> 类型: 需求讨论 + 方案设计
> 产出: docs/DESIGN_RAG_KG.md

---

## 1. 背景

Phase 1-5（知识库构建 + 验证）和 Phase 6 P0-P2（检索优化）全部完成后，用户提出下一步需求：
- 用向量数据库实现语义检索（轻量方案）
- 用知识图谱实现关系查询（重量方案）
- 两者结合形成混合架构

## 2. 需求澄清（6 个问题）

| # | 问题 | 用户选择 |
|---|------|---------|
| 1 | 用途场景 | A 自己用 + B 团队服务 + D 技术探索 |
| 2 | 技术栈 | C 都可以，选最合适的 |
| 3 | 部署环境 | C 本地开发 + 云端部署（但不着急部署，先本地跑通） |
| 4 | AI 模型 | C 不锁定供应商 + D 你推荐 |
| 5 | 预算 | C 不太在意成本，优先效果 |
| 6 | 成功标准 | D 全部（准确率 + 速度 + 可发现性） |

## 3. 方案选型

提出三个方案对比后，用户确认 **方案 C（混合架构）**，分两期：
- 一期: RAG Pipeline（向量数据库 Chroma + LiteLLM + FastAPI + Streamlit）
- 二期: 知识图谱（Neo4j）+ 意图路由

关键技术决策：
- Python 技术栈（RAG 生态最成熟）
- Chroma 本地向量库（零运维，数据量小够用）
- LiteLLM 模型抽象层（不锁定供应商）
- Neo4j Community 社区版（本地 Docker）
- 本地优先，Docker Compose 一键启动

## 4. 设计验证：场景模拟

用两个临床场景测试知识库的检索能力：

### 场景 1: "患者的 CT 检查 + 结果应该放什么 domain"
- **检索效果**: 强 — 命中 PR assumptions（明确列出 CT scan）、TU assumptions（CT SCAN 示例）
- **回答**: 区分肿瘤场景（TU+TR+PR+RS 四域联动）和非肿瘤场景（PR + Findings --METHOD）
- **跨域关联**: 需 Cross References 引导补查，一期 RAG 可覆盖大部分

### 场景 2: "癌症研究中 TU 域如何使用，转移癌和多发癌怎么记录"
- **检索效果**: 非常强 — TU assumptions + examples 高度匹配
- **回答**: 一个病灶一条记录（非一个患者一条），新发肿瘤 TUORRES="NEW"，分裂用 TUSPLIT
- **数据表**: TU Example 2/3 直接提供了完整的 RECIST 1.1 数据表

## 5. 新增需求：数据集校验功能

用户提出重要需求：上传自己映射的 SDTM 数据集，评估完成度和正确性。

纳入一期设计，两层架构：
- Layer 1: 规则型校验（validator.py）— Req 完整性、CT 合规、主键唯一性、数据类型
- Layer 2: 语义型评审（reviewer.py）— RAG 检索 assumptions/examples，LLM 评估业务规则合规性

产出结构化校验报告（完成度百分比 + ERROR/WARN/INFO 分级问题清单）。

## 6. 设计文档

完整设计写入 `docs/DESIGN_RAG_KG.md`，含 8 个章节：
1. Goals & Requirements
2. Architecture Overview
3. Phase 1: RAG Pipeline（分片策略、Embedding、检索流程）
4. Dataset Validation Module（两层校验 + 报告格式）
5. Phase 2: Knowledge Graph + Hybrid Routing（Schema、Cypher 示例、路由）
6. Evaluation System（50 题评测集 + 指标）
7. Implementation Roadmap（12 步）
8. Out of Scope

## 7. 下一步

进入实施计划阶段（writing-plans），按设计文档的 12 步路线图细化为可执行任务。

---

## 关联文件

| 文件 | 关系 |
|------|------|
| [docs/DESIGN_RAG_KG.md](../../docs/DESIGN_RAG_KG.md) | 设计文档（本 session 主产出） |
| [04_optimization/retrieval_optimization.md](../04_optimization/retrieval_optimization.md) | Phase 6 优化（P3 结构化元数据是二期前置依赖） |
| [meta/worklog.md](../meta/worklog.md) | 工作日志 |
| [meta/retrospective.md](../meta/retrospective.md) | 质量规则（一期开发也必须遵守） |
