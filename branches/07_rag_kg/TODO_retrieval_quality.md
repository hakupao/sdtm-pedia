<!-- chain: 07_RAG (Phase 7 RAG+KG 旁枝)
  本文件是检索质量优化的持久 backlog. 关联:
  → _progress.json I-4 (目标记录)
  → PLAN.md §5 Phase 2 gate (KG 决策)
  → docs/PROGRESS.md (Phase 7 行)
-->

# 検索品質 TODO — Phase 1.5 Retrieval Tuning (RAG src recall → >95%)

> 创建: 2026-06-05 (用户 Bojiang 指示: **模型配置非重点, 优化索引 + RAG 检索质量是重点**)
> 状态: **BACKLOG** — 今后有时间/精力时**优先执行**. Phase 1 已 CLOSED, 本表是 closed 之后的新一轮检索优化 (可视为 Phase 1.5).
> 目标: eval 4 类别 **src + fact recall 均 > 95%** (现状最弱 cross_domain src 61.5% / concept src 76.9%)

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
- [ ] **T1 检索消融实验** — rerank / Top-K 调大 / 多查询 三项分别 + 组合, 跑 53q (或先 20q sanity) eval, 看 cross_domain + concept src recall 能拉到多少. 产物 `eval/ablation_retrieval_<date>.md`. 不改 answering model, 不部署.

### 检索杠杆 (按优先级)
- [ ] **T2 Reranker** (PLAN §5 1B.2 本留 Cohere Rerank 可选) — Top-K 15→30/50 召回 → rerank 压回 Top-5/8. 对跨域/概念最直接.
- [ ] **T3 Top-K 调大** — 现 15, 跨域题 chunk 分散, 先简单加大做基线对照.
- [ ] **T4 多查询 / Query 改写 (multi-query / HyDE)** — 跨域题单 query 命不全多个域 → 拆多 query 分别检索合并. **cross_domain 61.5% 对症点.**
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
