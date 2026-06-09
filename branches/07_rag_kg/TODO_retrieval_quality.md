<!-- chain: 07_RAG (Phase 7 RAG+KG 旁枝)
  本文件是检索质量优化的持久 backlog. 关联:
  → _progress.json I-4 (目标记录)
  → PLAN.md §5 Phase 2 gate (KG 决策)
  → docs/PROGRESS.md (Phase 7 行)
-->

# 検索品質 TODO — Phase 1.5 Retrieval Tuning (RAG src recall → >95%)

> 创建: 2026-06-05 (用户 Bojiang 指示: **模型配置非重点, 优化索引 + RAG 检索质量是重点**)
> 状态: **Phase 1.5 单杠杆 round 完成 (2026-06-08)** — T1/T2/T4/re-chunk 全测, 证明单杠杆 @ top-15 达不到全类 95% (cosine baseline 84.0% 强局部最优). **下一方向已商定 (用户 2026-06-09): P1 查询条件路由, 追全类逼近 100%, 方案下个 session 讨论 (见 §5).**
> 目标: eval 4 类别 **src + fact recall 均 → 接近 100%** (用户 2026-06-09 上调; 现状最弱 cross_domain src 61.5% / concept src 76.9%; HyDE 最佳也仅 cross 69.2%)

## 0. 核心判断 (为什么是检索, 不是模型)

- **source recall = 检索器的活** (embedding / chunking / top-K / rerank / query 改写). **换答题 LLM 不影响这一列.**
- **fact recall** 已 93-96%, 接近 95%; 答题模型 (Sonnet / Opus / DeepSeek) 影响的是这列, 已够好.
- ∴ 把 src recall 拉到 95% = 动检索, 不是动模型. cross-model eval 不在关键路径上.

## 1. 现状 baseline (Phase 1D, 53q, DeepSeek, 2026-05-24)

| 类别 | src recall | fact recall |
|------|-----------|-------------|
| 单域 | 96.4% ✅ | 94.0% |
| 混合 | 92.3% | 96.2% ✅ |
| 概念 | 76.9% ❌ | 93.1% |
| 跨域 | 61.5% ❌ | 96.2% ✅ |

弱点集中在 **概念 (76.9%)** 与 **跨域 (61.5%)** 的 source recall.

## 2. TODO (按性价比 / 先后排)

### 最小先手 (不碰答题模型, 不部署, 先验证天花板)
- [x] **T1 检索消融实验 (Top-K 扫描)** — ✅ 完成 2026-06-08. 产物 `sdtm-rag/eval/ablation_retrieval_2026-06-08.md` + Rule D 复核 `ablation_t1/review_T1.md`.
  - **诊断: cross_domain/concept 主要是排序问题** (K=15→100 单调回升: cross 61.5%→92.3%, concept 84.6%→100%; 7/12 失败题 K=100 救回) → **rerank (T2) 对症, 候选池需 ~100**.
  - **天花板: 纯 dense retrieval K=100 = overall 95.3% 已达标**; 但逐类别 cross_domain/mixed 仍 92.3% < 95% (卡 4 硬核).
  - **副产物: 修复 q37 测试集 gold-label bug** (`04_special_purpose.md` 不存在 → `03_special_purpose_domains.md`; 全量审计仅此一处).
  - **4 硬核 (rerank 救不了, 不在 top-100)**: q34=VARIABLE_INDEX 表示缺口; q16/s04/s05=ae.md/vs.md **语义距离** (变量名↔CT code, 非截断) → 对症 **T4 HyDE/查询改写** 或 terminology 重切分.

### 检索杠杆 (按优先级)
- [x] **T2 Reranker (Cohere rerank-v3.5)** — ❌ **失败 2026-06-08**. 实测全 pool (30/50/100) → top-15 均 80.2% overall, **劣于 cosine baseline 84.0%**. 机制 (rank-tracing 证实): 通用 reranker 系统性降级简洁 spec.md 变量表 (q08 DM/spec cosine#2→rerank#17), 偏好散文章节, 破坏 cosine 对结构化内容的强排序. 详 `sdtm-rag/eval/ablation_retrieval_2026-06-08.md` §8-10. 代码保留 (rag.py 默认 off, 规则 B). **结论: rerank 非本 KB 对的工具.**
- [x] **T3 Top-K 调大** — 已被 T1 覆盖 (Top-K 扫描即 T3). 单纯调大 K 撑大 context+引噪声, 不单独上.
- [x] **T4 多查询 / Query 改写 (multi-query / HyDE)** — 测毕 2026-06-08 (DeepSeek 扩展). 结果: **multiquery 失败** (76.4% < 84.0% baseline, 4列表 RRF 稀释单域); **plain HyDE 迄今最佳** (87.7% +3.7pt, mixed 100%, concept/cross 升, single 回退仅1题); **hyde_rrf 融合反更差** (83.0%, 稀释回 baseline). 统一规律: 变换 query 帮难类伤易类. **距全类 95% 仍差** (HyDE cross 仅 69.2%). 详 `ablation_retrieval_2026-06-08.md` §12-14. 代码全留 (rag.py 默认 none).
  - **未决战略选项 (§14)**: (A) 接受 HyDE 温和增益 / (B) 重切分 4 硬核 VARIABLE_INDEX+terminology / (C) T5 embedding-large / (D) T6 KG / (E) 接受现状 (受信者自查够用).
- [ ] **T2b RRF 分数融合 (备选)** — 若仍想保 rerank 信号: reciprocal-rank-fusion 融合 cosine+rerank 排名 (非纯替换), 保住 cosine 的 spec.md 优势. 但 rerank 主动降级正确答案, 至多折中.
- [ ] **T5 embedding 升级评估** — `text-embedding-3-small` → `-large` (3072d). 全量重 ingest 成本 vs 召回收益权衡; PLAN 原写 "召回<80% 才考虑", 现 bar 提到 95% 纳入候选.

### 结构性 (前几项不够再上)
- [ ] **T6 ⭐ 重评 Phase 2 KG** — 原 gate "cross_domain < 50% 才上 KG", 61.5% > 50% 故 defer. **但 95% bar 下 cross_domain 离 95% 差 33 点, 纯向量难补 → 关系型检索 (KG) 重新成认真候选**, 尤其针对 cross_domain. 决策见 [PLAN.md §5](PLAN.md). 前置: P3 meta.yaml 生成 (spec.md + Cross References 派生 64 域; 也是 jp_delivery 02 §3.4/§3.5 同源数据).

## 3. 验证 / 规则 (沿用 PASS 五条)

- 每轮检索改动后跑 53q eval (或先 20q sanity 快验), src / fact recall **分类别**记录.
- **规则 A**: eval 题集改写率高 → scientist 独立抽检 (PASS 五条 4.c).
- **规则 D**: writer (改检索) ≠ reviewer (跑 eval / judge), 不同 subagent_type.
- **规则 B**: 失败 attempt 归 `evidence/failures/`.

## 4. 不做 (用户 2026-06-05 已定)

- ❌ 不纠结 answering model 选型 (Sonnet / Opus / DeepSeek 已够, fact recall 达标).
- ❌ 暂不部署 (Docker Compose 上线 defer).

## 5. ★ NEXT DIRECTION — P1 查询条件路由 (用户 2026-06-09 决定, 下个 session 讨论方案)

> **目标**: 全 4 类别 src recall 逼近 100% (用户愿意投入功夫). **入口**: 本节即下个 session 起点.

**为什么是 P1 (Phase 1.5 单杠杆 round 的核心揭露)**: 6 次实验 (T1/T2/T4/re-chunk) 证明 —
**每个单一检索杠杆都"帮某类、伤另类"**, cosine top-15 baseline (84.0%, single/mixed 92-96%) 是强局部最优,
任何全局性的"替换排序 / 改写查询 / 增加 chunk"都会扰动它 → 全类 95% @ top-15 单杠杆做不到 (已证)。
∴ 唯一出路 = **不做全局切换, 而是按查询类型路由**, 让每个杠杆只对它已被证明擅长的类生效, 避开 collateral。

**P1 核心思路 (用户认可)**:
- 分布/跨域查询 ("哪些域用变量 X" / "codelist Y 被谁用") → 用 **re-chunk 的 VARIABLE_INDEX 条目 chunk** (T1 已证 §一/§三 per-entry 切分对 q07/q34 有效, cross 61.5→76.9%)
- 术语/语义距离查询 ("变量 X 的 codelist") → 用 **HyDE** (T4 已证 mixed 100% / concept 92.3%, 对"变量名↔CT code"语义距离对症)
- 域内/spec 查询 ("DM 域的必填变量") → **纯 cosine** (baseline 已 96.4%, 别动它)

**下个 session 要讨论/决定的点 (尚未设计)**:
1. **query classifier 怎么做**: router.py 已有骨架 (intent 分类) 但未接检索; 用 LLM 分类 (haiku/deepseek 轻量) 还是规则/embedding 分类? 误分类的代价与兜底?
2. **多 collection 还是单 collection + 条件检索**: re-chunk 的索引条目 chunk 会污染域内查询 (已证 q02/q13/q43 回归) → 是否需要 per-route 用不同 chunk 子集 / metadata filter, 而非全塞一个 collection?
3. **terminology 注入的强化**: re-chunk 里 "Used by AE.AESEV" 太简短没修好 q16/s04/s05, HyDE 路由能否覆盖这几题?
4. **评测口径**: 追"逼近 100%"是否仍用 53q test_set? n=13/类 每题 7.7pt, 样本量是否够支撑 95%+ 的判定 (Rule A 抽检 + 可能扩题集)?
5. **工作量 vs 收益**: P1 是架构件 (classifier + 路由层 + 可能多 collection), 比单杠杆重; 先做 PoC (3 路硬编码路由跑 53q) 验证天花板, 再决定是否产品化。

**现成可复用资产 (Phase 1.5 全保留, 默认 off)**: `rag.py` 的 `query_expansion=hyde/hyde_rrf/multiquery` + `rerank` + chunker §一/§三 per-entry 拆分 (Rule D 通过, pytest 216 PASS); `run_eval.py --query-expansion/--rerank/--top-k` flags; baseline collection 已恢复 v1 (re-chunk v2 在 `data/chroma_backup_*` 可重建)。

**约束沿用**: 不碰答题模型选型; 规则 A/B/D; retrieval-only 先验证 src recall (免费) 再上 full eval。
