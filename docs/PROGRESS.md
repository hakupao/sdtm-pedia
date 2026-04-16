# 进度看板

> 最后更新: 2026-04-16

## 总体状态

**Phase 5 验证 — 全部完成** (2026-04-16)

## 阶段进度

| # | 阶段 | 产出 | 状态 |
|---|------|------|------|
| 0 | 分析与方案设计 | `.work/00_planning/` | **已完成** |
| 1 | xlsx 自动生成 | `domains/*/spec.md` + `terminology/` | **已完成** |
| 2 | PDF 页码索引 | `.work/02_indexing/page_index.json` | **已完成** |
| 3 | PDF 逐批提取 | `domains/*/assumptions.md` + `examples.md` | **已完成** (全部11批次) |
| 4 | 补充内容 | `model/` + `chapters/` | **已完成** |
| 5 | 验证与收尾 | 验证报告 + 溯源矩阵 | **已完成** (2026-04-16) |

## Phase 5: 验证明细

| 步骤 | 内容 | 状态 | 日期 |
|------|------|------|------|
| Step 0 | 修正 page_index.json (63域页码) | **已完成** | 2026-04-14 |
| Step 1 | 验证 assumptions.md (61域) | **已完成** | 2026-04-14 |
| Step 2 | 验证 examples.md (63域, 21组) | **已完成** | 2026-04-14 |
| Step 2-final | 补全 13 幅图表 (Mermaid) | **已完成** | 2026-04-14 |
| Step 3-1 | model/ 页码映射 + 验证小文件 (01, 04) | **已完成** | 2026-04-14 |
| Step 3-2 | 验证 model/ 剩余 4 文件 (02, 03, 05, 06) | **已完成** | 2026-04-15 |
| Step 3-3 | 验证 chapters/ 小文件 (ch01, ch02, ch03) | **已完成** | 2026-04-15 |
| Step 3-4 | 验证 ch04_general_assumptions | **已完成** | 2026-04-15 |
| Step 3-5 | 验证 ch08 + ch10 | **已完成** | 2026-04-15 |
| Step 3-final | 补全 chapters/ 6幅图表 (Mermaid) | **已完成** | 2026-04-15 |
| Step 3.5 | 编写溯源矩阵 (TRACEABILITY.md) | **已完成** | 2026-04-15 |
| Followup | M1-M5 中等风险项验证 | **已完成** | 2026-04-16 |
| Step 4 | 汇总报告 | **已完成** | 2026-04-16 |

### 验证统计

| 来源 | 文件数 | 发现问题 | 已修复 | 结果 |
|------|--------|----------|--------|------|
| Step 1: assumptions.md | 61 | 16 | 16 | 全部 PASS |
| Step 2: examples.md | 63 | 30 | 30 | 全部 PASS |
| Step 2-final: 图表补全 | — | 13幅图 | 13 | 全部完成 |
| Step 3-1/3-2: model/ | 6 | 72 | 72 | 全部 PASS |
| Step 3-3: ch01/02/03 | 3 | 72 | 12高 | 全部 PASS |
| Followup: ch01/02/03 | 3 | 27+ | 27+ | 全部 PASS (补全后) |
| Step 3-4: ch04 | 1 | 95 | 重构 | PASS |
| Step 3-5: ch08/ch10 | 2 | 86 | 28高 | 全部 PASS |
| Step 3-final: 图表补全 | — | 6幅图 | 6 | 全部完成 |
| **合计** | **136文件+19图** | **371+** | **全部** | |

## Phase 1 明细

| 步骤 | 产出 | 状态 |
|------|------|------|
| Python 生成 spec.md（63 domain） | `domains/*/spec.md` (63个) | **已完成** |
| Python 生成 terminology/ | `terminology/core/` `questionnaires/` `supplementary/` (91个文件) | **已完成** |
| spec.md 自动校验 | 63 domain / 1917 变量 / 13419 字段 全部 PASS | **已完成** |

## Phase 3 批次明细

| 批次 | Class | Domain 数 | 状态 |
|------|-------|----------|------|
| 1 | Special Purpose | 5 (CO, DM, SE, SM, SV) | **已完成** |
| 2 | Interventions | 7 (AG, CM, EC, EX, ML, PR, SU) | **已完成** |
| 3 | Events | 7 (AE, BE, CE, DS, DV, HO, MH) | **已完成** |
| 4 | Findings General | 4 (DA, DD, EG, IE) | **已完成** |
| 5 | Specimen-based Findings | 7 (BS, CP, GF, IS, LB, MB, MS) | **已完成** |
| 6 | Specimen-based Findings 2 | 3 (MI, PC, PP) | **已完成** |
| 7 | Morphology/Physiology | 7 (CV, MK, NV, OE, RE, RP, UR) | **已完成** |
| 8 | Other Findings | 7 (PE, FT, QS, RS, SC, SS, VS) | **已完成** |
| 9 | Findings About | 2 (FA, SR) | **已完成** |
| 10 | Trial Design | 7 (TA, TD, TE, TI, TM, TS, TV) | **已完成** |
| 11 | Relationships + Study Ref | 5 (RELREC, RELSPEC, RELSUB, OI, SUPPQUAL) | **已完成** |
| — | TU/TR 补漏 | 2 (TU, TR) | **已完成** |

## Phase 6: 检索精度优化

> 目标：提升 knowledge_base 的 AI 检索精度，减少幻觉

| # | 任务 | 说明 | 预估工作量 | 状态 |
|---|------|------|-----------|------|
| 6.1 | ROUTING.md 问题路由索引 | 7 类问题路由规则 + 多文件查询策略 + 文件类型速查 | 1-2 小时 | **已验证** |
| 6.2 | 交叉引用 | 63 spec.md 末尾追加 Cross References (CT 映射 + 域间关联 + 通用引用) | 3-4 小时 | **已验证** |
| 6.3 | 变量级反向索引 | VARIABLE_INDEX.md (1523 变量, 131KB) — 脚本自动生成+校验通过 | 半天 | **已验证** |
| 6.V | **P0/P1/P2 独立验证** | V1-V5 程序化 + V6-V8 功能性，8 项全 PASS，1 问题已修复 | — | **已完成** |
| 6.4 | 结构化元数据 | 将 spec.md 转为 YAML/JSON 元数据 — 已合并为 Phase 7 二期 Step 7 | 数天 | → Phase 7 |

## Phase 6.5: AI 平台部署（进行中）

> 目标：将知识库部署到三大 AI 平台，Phase 7 自建 RAG 之前先让知识库可用
> 总览文档：[ai_platforms/README.md](../ai_platforms/README.md)

| 平台 | 着重方向 | 内容策略 | 路线文档 | 状态 |
|------|---------|---------|---------|------|
| Claude Projects | 精确查询 + 规则推理 | 精选核心 ~200K tokens | [ROADMAP.md](../ai_platforms/claude_projects/ROADMAP.md) | 待开始 |
| ChatGPT GPTs | 全量覆盖 + 团队分享 | 合并文件 ~9.6MB 全量 | [ROADMAP.md](../ai_platforms/chatgpt_gpt/ROADMAP.md) | 待开始 |
| Gemini Gems | 大范围探索 + 全域对比 | 核心全量 ~512K tokens | [ROADMAP.md](../ai_platforms/gemini_gems/ROADMAP.md) | 待开始 |

## Phase 7: RAG + 知识图谱 + 数据集校验（设计完成）

> 目标：语义检索 + 关系查询 + SDTM 数据集自动校验
> 设计文档：[docs/DESIGN_RAG_KG.md](DESIGN_RAG_KG.md)
> Session 记录：[.work/05_rag_kg/session_2026-04-16_design.md](../.work/05_rag_kg/session_2026-04-16_design.md)

**一期：RAG + 数据集校验（本地）**

| Step | 任务 | 说明 | 状态 |
|------|------|------|------|
| 1 | 项目初始化 | sdtm-rag/ 目录 + pyproject.toml + Docker Compose | 待开始 |
| 2 | 数据入库 | Markdown → 分片 → Embedding → Chroma | 待开始 |
| 3 | 问答服务 | FastAPI + ROUTING.md 注入 + LiteLLM | 待开始 |
| 4 | 数据集校验 | 规则型校验 + RAG 语义评审 + 报告生成 | 待开始 |
| 5 | 前端 | Streamlit 对话 + 校验上传 | 待开始 |
| 6 | 评测 | 50 题评测集 + baseline | 待开始 |

**二期：知识图谱 + 混合路由**

| Step | 任务 | 说明 | 状态 |
|------|------|------|------|
| 7 | P3 结构化元数据 | spec.md + Cross References → meta.yaml (63域) | 待开始 |
| 8 | 图数据库 | Neo4j 导入节点+关系 | 待开始 |
| 9 | 图查询服务 | LLM → Cypher → Neo4j | 待开始 |
| 10 | 混合路由 | 意图分类 → RAG/Graph/Hybrid 三路 | 待开始 |
| 11 | 图增强校验 | 跨域依赖 + CT 级联 + 影响分析 | 待开始 |
| 12 | 二期评测 | 扩充评测集 + 对比一期 baseline | 待开始 |

---

## 文件统计

| 类型 | 预计数量 | 已完成 | 质量问题 |
|------|---------|--------|---------|
| spec.md | 63 | **63** | 0 |
| assumptions.md | 63 | **63** | 0 (已验证) |
| examples.md | 63 | **63** | 0 (已验证+13图) |
| terminology/ | 91 | **91** | 0 |
| model/ | 6 | **6** | 0 (已验证) |
| chapters/ | 6 | **6** | 0 (已验证+6图) |
| INDEX.md | 1 | **1** | 0 |
| **总计** | **293** | **293** | **0** |
