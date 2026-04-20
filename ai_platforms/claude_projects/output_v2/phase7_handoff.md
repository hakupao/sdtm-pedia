# Phase 6.5 → Phase 7 交接 (RAG 衰减观察 + 长尾下沉路径)

> 触发: Phase 6.5 v2 终态 (v2.6, 2026-04-20) 完成, 24/24 A/B PASS, 0 衰减.
> 下游: `docs/DESIGN_RAG_KG.md` 的 Phase 7 RAG + 知识图谱实施.
> 本文件只写 actionable insight + 待解决问题, 不复述细节 (细节见 `rag_decay_curve.md` + `RETROSPECTIVE_V2.md`).

---

## 0. 一句话 TL;DR

v2.6 在 77% capacity / 1.29M tokens / 19 文件 / 24/24 PASS 零衰减终态, **拐点未触**, Phase 7 可以放心推高并复用 Deferred stub 模式; 剩余 302 codelist (296 quest + 6 giants) 走自建 RAG 索引最优.

---

## 1. 7 数据点 (简版, 详见 rag_decay_curve.md)

| 阶段 | tokens | 文件 | capacity | PASS | 备注 |
|------|-------:|-----:|---------:|------|------|
| v1 | 192,036 | 11 | 12% | 8/8 | baseline |
| v2.1 | 205,895 | 11 | 13% | 7/8 (T3 边界 ↓) | chapters 全展开 |
| v2.2 | 318,592 | 12 | 20% | 7/8 + 2 新 | examples 28 域 |
| v2.3 | 367,489 | 13 | 23% | 7/8 + T3 跨批 ↑ | examples 35 域 |
| v2.4 | 719,241 | 16 | 43% | 8/8 (T7 ↑ 质变) | terminology top 200 |
| v2.5 | 1,097,180 | 29 | (被 v2.6 合并) | (未独立测) | terminology rank 201-500 |
| **v2.6** | **1,286,161** | **32** | **77%** | **24/24** | **终态: tail rebalance + 优先级纠偏** |

**观察**: capacity 12% → 77% 全程未触拐点; token 增长 vs capacity 增长从 subsublinear (chapters) 到 linear (terminology) 不一; 文件数 11 → 19 对召回无影响.

---

## 2. 关键发现 (Phase 7 必读)

### 2.1 RAG 拐点 ≥77% 且本次未触

- 本次 77% 是实测最高点, T1-T22 + 2 rebalance 24/24 PASS.
- **Phase 7 insight**: "50% 中庸"原计划上限可放宽, 推到 85-90% 仍有空间, 但需每批 A/B 验证.
- **风险**: v2.6 capacity 预测 63-68% 实测 77% (+14pp 超预期), 本地 tiktoken 公式与 Claude Projects UI 不一致 — 推高前需 calibration (§4).

### 2.2 文件数不是瓶颈, 内部冗余才是

- v2.4 11b 单文件 256K tokens (含 152 QRS codelist, Related Domain 提 header 减 72K 重复), 是 v2 最大单文件.
- 零挤出 05/02/09 老文件召回, T1/T15/T3 深度回归零衰减.
- **Phase 7 insight**: 不必追求"单文件越小越好", 优先降内部冗余 (e.g. Related Domain 提 header / Definition 截断 100 字符 / Synonyms 按 tier 剥离).

### 2.3 Deferred stub 是 RAG 扩展合法产物 (T22 PASS 验证)

- 6 tail giants (C65047/C67154/C85491/C85494/C120527/C120528, 均 ≥500 terms) 走 1-行 stub + 源路径 + NCI EVS Browser 入口.
- T22 测试模型在 stub 上的行为: Claude 精准识别 "超大规模, Project 内未完整列出所有 Term 值" + 引用 stub 源文件 + NCI EVS 入口 + **零臆造 term**.
- **Phase 7 insight**: 对 MedDRA/WHODrug/LOINC/SNOMED 等超大表可直接用此模式, stub 在 Project 里作为路由卡, 实际 term 查询走 Phase 7 自建 RAG 索引. 阈值 500 terms 是本次经验值, Phase 7 可做 300/500/700/1000 灵敏度扫描.

### 2.4 跨批累积正向激活 (T3 三阶)

- v2.2 硬拒答 (§6.3.5.9.3 PC relrec narrative 未收录) → v2.3 从 09 数据推导 4 粒度 + 推断 Method A/B/C/D → v2.4 显式 Method A-D 段 + A-D 汇总矩阵 + 粒度选择建议.
- 证明 RAG 不是被动查文件, 多批累积后模型**跨文件重建缺失 narrative**.
- **Phase 7 insight**: 不必追求单文件完备, 可接受"多文件间接完备", 每批 A/B 验证一次即可. 对 narrative-heavy 内容 (e.g. ch04/ch08 prose) 可先上 structural, 等下批再补 prose, 减少单批上传时间.

### 2.5 Indexing indicator 不可信 (G3 缺口)

- 6 批全程 UI indicator 显示 "Indexing" 数十分钟 → 1+ 小时, 但每批上传后立即提问都命中.
- **Phase 7 insight**: 不要等 UI indicator, 直接试问判可用. 如果需要客观 metric, 在 client 侧计时 (chrome-devtools MCP network timing).

### 2.6 用户业务优先级必须早问 (G1 缺口 → 规则 E 候选)

- v2.5 按域引用次数打分导致 quest (用户最低优先级) 55.8% > core 53.7% > supp 25.0%, 与用户期望反向.
- 用户 2026-04-20 追加 v2.6 重平衡批: core 99.3% / supp 100% / quest 保持 55.8% (不扩容).
- 成本: 多跑一批 188K tokens ≈ 30 分钟 subagent + 60 分钟用户 A/B ≈ 1.5 小时壁钟.
- **Phase 7 insight**: 设计阶段就要问用户业务优先级, 乘入打分公式, 不要等事后重平衡.

---

## 3. 对 Phase 7 RAG 设计的 6 条 actionable

### 3.1 索引粒度建议: 文件 + 内部结构化双层

- Claude Projects 本次 file-level 索引 + 内部表格结构化 (codelist 表 / domain spec 表 / example 数据表) 已达成 24/24 PASS.
- Phase 7 自建 RAG 不必强行 pre-chunk 到段落或 term 级, 除非要跑 embeddings 相似度 (chunk 粒度则建议 200-500 token per chunk, 保持表格完整性).
- **风险**: 表格被 chunker 切断 (e.g. term 表断在 row 中间) 会严重伤召回; 建议用 TableAwareChunker 或 md-heading-based 分段.

### 3.2 capacity 推高的 ROI 评估

- 本次 core 99.3% + supp 100% 已达成用户覆盖需求, 再推 (e.g. quest 扩到 80%) 只服务 quest 优先级.
- 用户 2026-04-20 声明 quest 最低优先级, 建议 **quest 296 条全部下沉 Phase 7 RAG 自建索引**, Project 只留现有 55.8% 覆盖.
- 如果 Phase 7 用户场景翻转 (quest 变重要), 可追加 v2.7 批. 单批成本 ~180-220K tokens + 1 批 A/B.

### 3.3 terminology 自建索引而非继续塞 Project

- 302 codelist (296 quest + 6 giants) 是 Phase 7 RAG 第一批索引对象.
- 索引字段建议: codelist C-code / name / 每 term Code+Submission Value+NCI Definition+Synonyms+Preferred Term / related domains / source file path.
- 向量化: 可按 term 级 embed (~25K-30K terms 总量, 可控规模); 或按 codelist 级 embed (粗粒度, 快但召回差).

### 3.4 capacity 预测 calibration (必须做)

- Phase 7 首次上传前, 空 Project 上传一个已知 N tokens 的简单文件 (e.g. 50K / 100K / 200K 三组), 测 Δcapacity, 反推 "UI token 放大系数".
- 本次 v2.6 系数 ≈ 77/43 ÷ 1286/719 ≈ 1.00 (近线性), 但 v2.0→v2.1 系数 ≈ 1/(7.2%) ÷ 1 ≈ 0.14x (强 subsublinear). 不同内容类型系数差大, 建议分类测.

### 3.5 A/B 回归矩阵继承

- v2 的 T1-T22 + T-core-reb/T-supp-reb 矩阵 (见 `test_results_v2.md`) 可直接作为 Phase 7 回归 baseline.
- 建议 Phase 7 新增: T23 (MedDRA preferred term 查询, 验 6 giants stub + RAG 联动) / T24 (多 codelist 交叉查询, e.g. "哪些 codelist 有 Y/N/U/NA 同 shape").

### 3.6 知识图谱 (Phase 7 设计二维度)

- 本次未产出知识图谱, 但产生的两类关系数据可直接用:
  - **codelist ↔ domain 关系**: 11a/b/c + 12a/b/c + 13a/c 中每个 codelist 已标 Related Domains 行 (从 knowledge_base 解析). 可直接 load 进 graph DB (Neo4j / NetworkX).
  - **variable ↔ codelist ↔ term 三元关系**: `knowledge_base/domains/*/spec.md` 的 Controlled Terms 列 + terminology 文件 + term 值, 三层 join 即是 Phase 7 KG 的核心 edges.

---

## 4. Phase 7 实施前待办 (建议顺序)

1. **读 3 文件入门** (<20 分钟):
   - 本文件 (`phase7_handoff.md`)
   - `rag_decay_curve.md` (7 数据点 + 6 观察段)
   - `RETROSPECTIVE_V2.md` §3 关键决策复盘 (5 条)
2. **验证继承的 A/B 矩阵还能重放** (<30 分钟): 在 v2.6 Claude Project 上重跑 T1/T17/T22 三题, 确认 24/24 PASS 状态没 regress (建议在 Phase 7 启动时固化基线).
3. **做 capacity calibration 实验** (<60 分钟, §3.4)
4. **读 `docs/DESIGN_RAG_KG.md`** 并据本文件 §3 更新设计 (尤其索引粒度和 giants 阈值两段).
5. **起草 Phase 7 PLAN** 时把本文件 §3 6 条 actionable + §2.6 用户优先级早问写进 §执行规则 (P11/P12 新增).

---

## 5. 未解决问题 / 明示风险

- **Q1**: v2.6 capacity 77% 超预期 14pp, 是 UI 元数据开销还是我们 token 估算偏低? 需 calibration 实验才能回答.
- **Q2**: 拐点 ≥77% 但具体位置未知. Phase 7 推高时如果发现 ~85% 开始衰减, 回落阈值应设 ~80%.
- **Q3**: Deferred stub 阈值 500 terms 是经验值, 未做 300/500/700/1000 灵敏度扫描.
- **Q4**: 跨批累积正向激活 (T3 三阶) 是否在 Phase 7 自建 RAG 里也成立? 还是 Claude Projects 的特性? 需 Phase 7 对比实验.
- **Q5**: 文件数 19 在 Phase 7 如果扩到 30-40 仍安全? 本次没测这么多.

---

## 6. 交接清单

主控已 commit + push 以下产物, Phase 7 启动时全部可读:

- `ai_platforms/claude_projects/output_v2/` (19 上传文件 + meta)
- `ai_platforms/claude_projects/output_v2/evidence_v2/` (trace.jsonl + _progress.json + subagent_prompts/ + failures/ + checkpoints/)
- `ai_platforms/claude_projects/output_v2/STAGE_V2.{1..6}_AB_REPORT.md` (6 批 A/B 报告, v2.5 标 skipped)
- `ai_platforms/claude_projects/output_v2/rag_decay_curve.md` (7 数据点 + 结论)
- `ai_platforms/claude_projects/output_v2/test_results_v2.md` (T1-T22 完整矩阵)
- `ai_platforms/claude_projects/output_v2/phase7_handoff.md` (本文件)
- `ai_platforms/claude_projects/RETROSPECTIVE_V2.md` (复盘, 含 G1-G5 缺口)
- `ai_platforms/claude_projects/scripts_v2/` (6 个 Python 脚本)

---

*作者: 主控 Opus 4.7, 2026-04-20.*
*下一步: Phase 7 启动时读本文件前 §0-§3, 起草 `05_rag_kg/PLAN.md` (或沿用 `docs/DESIGN_RAG_KG.md` 扩展).*
