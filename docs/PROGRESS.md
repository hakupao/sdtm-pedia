# 进度看板

> 最后更新: 2026-04-22 (Phase 6.5 **NotebookLM Phase 3 P3.4 + P3.4.5 完成** — P3.4 indexing smoke N=10 PASS 10/10 顶阈值 (9dce0b0, 2026-04-21); P3.4.5 Q1 红线语义级自证 Rule A 正本 **CONDITIONAL_PASS 8.5/10** (语义 10/10 顶阈值 + citation 7/10 未达 ≥9/10 阈值) — 主 session 初判 → **第 10 种 subagent_type oh-my-claudecode:scientist 独立复核**终审 → 用户仲裁 A 采纳; Q1 红线结构 A4 + 语义 P3.4.5 **双锚闭合**; HC-3 bucket 38 头段 PASS (CDR) / 尾段 INCONCLUSIVE (MMSE FT 归属事件) → 单区域 PASS; F-1 状态修正重开 `F-1-recurring` (真实漂移 8/10 打脸 P3.3 CLOSED 误判); Reviewer 新发现 F-3 citation dropout T2 题型偏向系统性弱点; Rule D 链扩展 9 → 10 种; 3 new evidence (prompt_log 566 行 + sampling_log + semantic_audit 306 行) + progress.json updated; commit 34179dc; 进 P3.5 Audio Overview × 3. 异步 lane 不影响 ChatGPT/Gemini 锁步 (前日 2026-04-21 双平台 N5.2 PASS / N5.3 题库设计 commit 7edcb1c 未动))

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
| Claude Projects | 精确查询 + 规则推理 | 方案 B 二次创作压缩 → 实测 192,036 tokens (12% capacity, RAG 自动接管) | [ROADMAP.md](../ai_platforms/claude_projects/ROADMAP.md) / [README.md](../ai_platforms/claude_projects/README.md) (reorg 后入口) / [archive PLAN.md](../ai_platforms/claude_projects/archive/v1/docs/PLAN.md) / [archive UPLOAD_TUTORIAL.md](../ai_platforms/claude_projects/archive/v1/docs/UPLOAD_TUTORIAL.md) / [docs/capacity_research.md](../ai_platforms/claude_projects/docs/capacity_research.md) | **v1 完成 (Step 1-14, 9/9 PASS)** (2026-04-18) |
| Claude Projects v2 扩容 | 中庸策略推到 ~50% 容量, 实际 v2.6 终态 77% (用户优先级重平衡后) | 6 批渐进 + 1 tail 重平衡 (chapters 全展开 → examples 高频 → examples 全 → terminology 高 → terminology mid → terminology tail core+supp) | [v2 design](superpowers/specs/2026-04-18-phase6.5-claude-v2-expansion-design.md) / [docs/PLAN_V2.md](../ai_platforms/claude_projects/docs/PLAN_V2.md) / [docs/RETROSPECTIVE_V2.md](../ai_platforms/claude_projects/docs/RETROSPECTIVE_V2.md) / [docs/rag_decay_curve.md](../ai_platforms/claude_projects/docs/rag_decay_curve.md) / [docs/phase7_handoff.md](../ai_platforms/claude_projects/docs/phase7_handoff.md) / [dev/test_results.md](../ai_platforms/claude_projects/dev/test_results.md) | **终态 v2.6 完成 (19 文件 / 1,286,161 tokens / capacity 77% / 24/24 A/B PASS / 0 衰减)** (2026-04-20, reorg 完成) |
| ChatGPT GPTs | 全量覆盖 + 团队分享 + GPT Store 发布 | 9 文件 / 2.53M tokens / 20 槽位 (11 剩余, 可扩) | [README.md](../ai_platforms/chatgpt_gpt/README.md) / [ROADMAP.md](../ai_platforms/chatgpt_gpt/ROADMAP.md) / [docs/platform_profile.md](../ai_platforms/chatgpt_gpt/docs/platform_profile.md) | **Phase 4 N5.2 PASS 10/10 strict** (2026-04-21, v2.1 system_prompt + batch 1+2, Phase 4 Gate CONFIRM → N5.3 Full A/B 待) |
| Gemini Gems | 大范围探索 + 全域对比 | 4 文件 / 637K tokens / 1M context (62% 占用) | [README.md](../ai_platforms/gemini_gems/README.md) / [ROADMAP.md](../ai_platforms/gemini_gems/ROADMAP.md) / [docs/platform_profile.md](../ai_platforms/gemini_gems/docs/platform_profile.md) | **Phase 4 N5.2 PASS 9/10 → Q3 补测后等价 10/10** (2026-04-21, v5 system_prompt + v5b 04 双修; Phase 4 Gate CONFIRM → N5.3 Full A/B 待 generalization probe) |
| **NotebookLM** | Audio Overview + Mind Map + Grounded citation (ABC 三场景分享档位切换) | **v2**: 1 notebook × 42 bucket concept cluster (≤50 sources target, 295 md 全覆盖 + 176 Req ∅ gap); pivot from v1 3 notebook × 293 架构 | [README.md](../ai_platforms/notebooklm/README.md) / [docs/PLAN.md](../ai_platforms/notebooklm/docs/PLAN.md) / [dev/checkpoints/CHECKPOINT_P3.2_HANDOFF.md](../ai_platforms/notebooklm/dev/checkpoints/CHECKPOINT_P3.2_HANDOFF.md) / [CHECKPOINT_P3.4_HANDOFF.md](../ai_platforms/notebooklm/dev/checkpoints/CHECKPOINT_P3.4_HANDOFF.md) / [CHECKPOINT_P3.4.5_HANDOFF.md](../ai_platforms/notebooklm/dev/checkpoints/CHECKPOINT_P3.4.5_HANDOFF.md) / [p3_2_upload_log.md](../ai_platforms/notebooklm/dev/evidence/p3_2_upload_log.md) / [chat_mode_toggle_test.md](../ai_platforms/notebooklm/dev/evidence/chat_mode_toggle_test.md) / [indexing_smoke.md](../ai_platforms/notebooklm/dev/evidence/indexing_smoke.md) / [phase3_task_P3.4.5_req_semantic_audit.md](../ai_platforms/notebooklm/dev/evidence/phase3_task_P3.4.5_req_semantic_audit.md) / [p3_4_5_prompt_log.md](../ai_platforms/notebooklm/dev/evidence/p3_4_5_prompt_log.md) / [p3_4_5_sampling_log.md](../ai_platforms/notebooklm/dev/evidence/p3_4_5_sampling_log.md) / [current/uploads/MANIFEST.md](../ai_platforms/notebooklm/current/uploads/MANIFEST.md) / [current/instructions.md](../ai_platforms/notebooklm/current/instructions.md) / [ARCHITECTURE_PIVOT_RECORD.md](../ai_platforms/notebooklm/archive/v1_3notebook_SUPERSEDED_2026-04-21/ARCHITECTURE_PIVOT_RECORD.md) | **Phase 3 P3.4.5 完成 (2026-04-22): Q1 红线语义级自证 Rule A 正本 CONDITIONAL_PASS 8.5/10 (语义 10/10 + citation 7/10); 10th subagent_type scientist 终审 + 用户仲裁 A; HC-3 bucket 38 头段 PASS (CDR) / 尾段 inconclusive (MMSE FT 归属); F-1 重开 F-1-recurring; Reviewer 新发现 F-3 citation T2 题型偏向; Rule D 链 9→10; Q1 红线双锚闭合; 进 P3.5 Audio Overview × 3** |
| **通用部署范本** | 10 维度规范 (抽象自 Claude v2) | `_template/` 12 文件 (README + APPLY_CHECKLIST + 00-09) | [_template/README.md](../ai_platforms/_template/README.md) | **就绪 (2026-04-20), 10 补丁候选待 Phase 5 收束 (原 7 + NotebookLM pivot 新增 3: 单/多 notebook 决策树 / per-day rate limit / Writer 叙事合成伪约束 10a+10b.1+10b.2)** |

### Phase 6.5 Claude v2 批次进度 (渐进式 RAG 扩容, 终态)

| 批次 | 阶段 | 内容 | 文件增量 | 累计 tokens | Capacity | 回归衰减 | 新 PASS | 决议 |
|------|------|------|----------|-------------|----------|----------|---------|------|
| 1 | v2.1 | chapters 全展开 | +0 (02_chapters 替换) | 205,895 | 13% | 1/8 (T3 边界 ↓) | T9-T12 4/4 | continue (D1) |
| 2 | v2.2 | examples 高频 28 域 | +1 (09) | 318,592 | 20% | 0/2 | T13-T14 2/2 | continue (E1) |
| 3 | v2.3 | examples 其余 35 域 | +1 (10) | 367,489 | 23% | 0/2 (T3 反向 ↑) | T15-T16 2/2 | continue (F1) |
| 4 | v2.4 | terminology 高频 top 200 codelist | +3 (11a/b/c) | 719,241 | 43% | 0/4 (T7 ↑ 质变) | T17-T18 2/2 | continue (G1) |
| 5 | v2.5 | terminology 中频 rank 201-500 | +3 (12a/b/c) | 1,097,180 | (合并测) | (合并测) | (合并测) | skipped → 合并 v2.6 |
| 6 | v2.6 | **终态 + 用户优先级重平衡** (tail core+supp) | +2 (13a/13c, 13b by design 不存在) | **1,286,161** | **77%** | **0/20 (T1-T20 全持平)** | **T21/T22 + T-core-reb/T-supp-reb 4/4** | **Phase H 收尾** |

**终态覆盖率** (用户优先级: core > supp > quest):
- core 99.3% (146/147, 1 个 MedDRA-level giant 走 Deferred stub)
- supp 100% (188/188)
- quest 55.8% (374/670, 保持不扩容, 归 Phase 7 RAG)
- Long tail 302 codelist (296 quest + 6 tail giants) → Phase 7 自建索引

**Rule D 三 lane 独立复核**: v2.4 F4 + V6.2 (v2.6) + H1 RETROSPECTIVE_V2 三次全部过 — Cowork writer (A/B 测试) + 主控 writer (脚本/产物/复盘) + 独立 reviewer subagent (code-reviewer 7 维度审) 三 lane 隔离全程到位, 规则 D 固化完成

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
