<!-- chain: 07_RAG (Phase 7 RAG+KG 旁枝 / Phase 1.5 检索优化)
  本文件是 T1 检索消融实验的 evidence 产物 (TODO_retrieval_quality.md T1 指定路径).
  关联:
  → ../../TODO_retrieval_quality.md   (T1 任务定义 + 后续 T2-T6 决策)
  → ../../_progress.json              (I-4 检索优化进度)
  → ablation_t1/review_T1.md          (Rule D 独立复核, 异 subagent_type)
  → ablation_t1/k{15..100}.json       (buggy-baseline raw, q37 gold-label 修复前)
  → ablation_t1/k{15..100}_fixed.json (corrected raw, q37 修复后 — 决策依据)
-->

# T1 检索消融实验 — Top-K 扫描 (诊断: 排序问题 vs 表示问题)

> 日期: 2026-06-08
> 执行: main session (writer)；独立复核见 `ablation_t1/review_T1.md` (Rule D, verifier subagent)
> 模式: `run_eval.py --retrieval-only` (只跑 embedding + 向量检索, **不调答题 LLM**, 免费)
> 基准: Phase 1D baseline (53q, 2026-05-24, commit dbfea50), `eval/1d_report_retrieval.json`
> 数据集: `eval/test_set_v1.yml` (53q: single 14 / cross_domain 13 / concept 13 / mixed 13)
> 硬约束遵守: source recall 与答题模型无关；不改答题模型；不部署
>
> ⚠️ **本实验中途发现并修复了一个测试集 gold-label bug (q37, 见 §2)。下方 §3 主表为修复后数据；
> 修复前 buggy 数据并列保留以示透明 (规则 B: 旧产物不删)。**

---

## 1. 实验目的

T1 是 `TODO_retrieval_quality.md` 的"最小先手, 先验证天花板"。核心问题不是"哪个杠杆最好",
而是一个**决定后续 T2-T6 路线**的诊断:

> **cross_domain / concept 的 source recall 偏低, 是 (A) 排序问题 [正确 chunk 检索得到但排名太低]
> 还是 (B) 表示问题 [正确 chunk 根本不在向量近邻里]?**

- 若 (A) → **rerank (T2)** 是对症解: 宽召回 + 重排压回 top-K。
- 若 (B) → rerank 无用, 需 **embedding 升级 (T5)** / 重切分 / 查询改写 (T4) / **KG (T6)**。

Top-K 扫描 (K=15→100) 看 recall 是否随之回升: 回升 = chunk 本就可检索, 只是排名靠后 = 排序问题。

## 2. 中途发现: q37 测试集 gold-label bug (已修复 + 全量审计)

诊断过程中, q37 在所有 K 都 0%。独立核查发现其 `expected_sources` 指向 `model/04_special_purpose.md`,
**该文件在 KB 中不存在** (真实文件为 `model/03_special_purpose_domains.md`)。q37 问的正是 special-purpose
datasets, 03 文件正好作答 → 这是 gold-label 路径 bug, 非检索失败。

**全量审计**: 对 53 题所有 expected_sources 逐一对照 296 个 KB md 文件, **仅 q37 一处路径 bug**, 余 52 题全部命中真实文件。

**修复**: `test_set_v1.yml` q37 expected_sources `04_special_purpose.md` → `03_special_purpose_domains.md`
(带 inline 注释 + 指向本审计)。修复后 q37 在 K=15 即 100% (03 文件本就在 top-15)。

**影响**: concept baseline (K=15) 76.9% → **84.6%**; K=100 ceiling 93.4% → **95.3%**。此修复改变了
紧迫性判断 (见 §4.3): 修复前看似离 95% 差 1.6pt 且 concept 弱, 修复后纯 dense retrieval 在 K=100 **已达标 95.3%**。

## 3. 代码改动 (T1 唯一逻辑改动)

`eval/run_eval.py` 加 `--top-k` CLI flag (原 `TOP_K=15` 仅模块常量, 无 flag):
`run_evaluation(top_k=...)` 形参化 + argparse `--top-k` + `RAGEngine(top_k=args.top_k)` + `summary["top_k"]` 写入输出 JSON。
未改任何检索逻辑 / chunker / embedding / 答题模型。纯参数扫描。

## 4. 结果 — Top-K 扫描 source recall (53q, retrieval-only)

### 4.1 主表 (q37 gold-label 修复后, 决策依据)

| K | overall | concept | cross_domain | mixed | single_domain |
|---|---------|---------|--------------|-------|---------------|
| 15 (baseline) | 84.0% | 84.6% | **61.5%** | 92.3% | 96.4% |
| 20 | 84.9% | 84.6% | 65.4% | 92.3% | 96.4% |
| 30 | 84.9% | 84.6% | 65.4% | 92.3% | 96.4% |
| 50 | 89.6% | 92.3% | 76.9% | 92.3% | 96.4% |
| **100** | **95.3%** | **100.0%** | 92.3% | 92.3% | 96.4% |

raw: `ablation_t1/k{15,20,30,50,100}_fixed.json`。

### 4.2 对照表 (q37 修复前 buggy, 仅供透明对照, 勿用于决策)

| K | overall | concept | cross_domain | mixed | single |
|---|---------|---------|------|-------|--------|
| 15 | 82.1% | 76.9% | 61.5% | 92.3% | 96.4% |
| 100 | 93.4% | 92.3% | 92.3% | 92.3% | 96.4% |

buggy K=15 与旧 `1d_report_retrieval.json` 逐类别一字不差 → 复现成立, 环境可信。raw: `ablation_t1/k*.json` (无 _fixed 后缀)。

## 5. 诊断结论

### 5.1 主结论: cross_domain / concept 低 recall 主要是【排序问题】(Rule D: CONDITIONAL PASS)

K 从 15→100: cross_domain **61.5% → 92.3%** (+30.8pt), concept **84.6% → 100.0%** (+15.4pt)。
全 53 题 source_recall 随 K 单调非降 (verifier 验证: 0 违反)。7/12 失败题在 K=100 救回 →
正确 chunk 在 top-100 内可检索, 只是排名 >15。**→ rerank (T2) 对症**。

verifier 加注 (采纳): "mainly" 对 cross_domain 成立 (5/8 失败题可救), 对 concept 是 50/50;
且关键 ranking band 在 **K=30-100** (异常深) — q07/q09 要 K>50 才救回, **rerank 候选池需 ~100 (非 50)** 才吃满。

### 5.2 硬核残留: 4 题 K=100 仍漏 = 真检索缺口 (rerank 救不了, 因不在 top-100)

(注: q37 已剔除 — 它是 §2 的测试集 bug, 非检索失败。修复前误记为 5 题。)

| 题 | 类别 | 漏的 source | 根因 (经 verifier 逐例核实修正) |
|----|------|------------|------|
| q34 | cross_domain | VARIABLE_INDEX.md | ✅ 表示缺口: 131KB 索引按域切 65 chunk, "变量跨域分布"类查询信号稀释 |
| q16 | mixed | terminology/core/ae.md | ⚠️ **语义距离** (非截断): ae.md 切 4 个小 chunk (138-330 tok, 未截断); query 用变量名 "AESEV", 正确 chunk 标题是 CT code "C66769" → embedding 距离远, 不进 top-100 |
| s04 | mixed | terminology/core/ae.md | 同 q16 |
| s05 | single_domain | terminology/core/vs.md | ⚠️ 语义距离 (非截断): vs.md 3 chunk (最大 2727 tok, 未截断); "VSTESTCD codelist" query 与 codelist section 标题 embedding 距离远 |

**重要更正**: 初稿误把 ae.md/vs.md 归因为"超大 chunk >8191 tok 截断" (套 PLAN 已知 finding 未逐例核实)。
verifier 实测 chunk 大小 138-2727 tok, **无截断**。真实根因是**变量名 query 与 CT-code-标题 chunk 的语义距离** →
对症解是**查询改写 (T4: 变量名→CT code / HyDE)** 或 **terminology 重切分 (chunk 文本/metadata 带变量名)**, 非重切大小。

### 5.3 天花板量化 (修复后)

- 纯 dense retrieval 在 K=100 的天花板 = **overall 95.3%** — **已达 95% 总目标**。
- 但**逐类别 95% 目标未全达**: cross_domain 92.3% (卡 q34) / mixed 92.3% (卡 q16+s04) 仍 < 95%。
- 缺口构成 (11 题, 修复后): 7 题排序问题 (rerank 可救) + 4 题真检索缺口 (q34 + ae/vs 语义距离)。
- ∴ 逐类别 >95% 需 **rerank (T2) [把 K=100 recall 压到可用 top-8] + 针对 4 硬核的查询改写/重切分 (T4 或部分 T5)** 组合。

## 6. 对 T2-T6 的影响 (路线更新建议)

| 任务 | T1 前 | T1 后判断 |
|------|------|----------|
| **T2 Reranker** | 杠杆 | ⬆️ **首选** — 把 K=100 的 95.3% recall 压到可用 top-8 (否则得喂 100 chunk 进 LLM, context 爆+噪声); 救 7 个排序问题题 |
| **T3 Top-K 调大** | 杠杆 | ⬇️ **已被 T1 覆盖** — 单纯调大 K 撑大 context 引噪声; 必须配 rerank, 不单独上 |
| **T4 多查询/HyDE** | 杠杆 | ⬆️ **升为次选** — 对 4 硬核里 ae.md/vs.md 的"变量名↔CT code 语义距离"正好对症 (HyDE 生成含 CT 术语的假想答案再检索) |
| **T5 embedding -large** | 候选 | ➡️ 针对性候选 — 仅对 4 硬核评估; 非全量先决 |
| **T6 KG** | 结构性 | ⬇️ **暂不需要** — cross_domain 是排名问题非"关系检索缺失"; KG gate 维持 defer |

## 7. 下一步 (待用户决策)

T2 rerank 原型需选 reranker provider (本地模型已排除, 见用户 constraint):
- **(a) Cohere Rerank API** — 有免费层 (trial key), 需开 `COHERE_API_KEY` (.env 当前无)
- **(b) LLM-as-reranker (DeepSeek/OpenAI)** — 无新依赖/key, 用现有云 API, 每查询多一次 LLM 调用 (有成本)

决策后实现 rerank (候选池 K=100 → top-8), 跑 53q retrieval-only 对照 §4.1, 看 cross_domain (61.5%) / mixed
能否在**可用 top-K** 下保住 K=100 的 recall。遵守规则 A (改写抽检) / B (失败归档) / D (writer≠reviewer)。

并行可做 (不依赖 provider 决策): 针对 4 硬核试 **T4 HyDE/查询改写** — 对 ae.md/vs.md 语义距离最对症。

---

# 第二部分: T2 Cohere Rerank 实测 (2026-06-08) — ❌ 失败 (负面结果)

> 用户 2026-06-08 选定 Cohere Rerank 起 T2 原型。实现经独立 code-reviewer (Rule D) CONDITIONAL PASS +
> 2 HIGH/3 建议全修。下面是实测结果: **rerank 在本 KB 上全面劣于纯 cosine, 确认失败。**

## 8. T2 结果: 没有任何 rerank 配置超过 cosine baseline

全部 retrieval-only, q37 已修, Cohere `rerank-v3.5`, 候选池 → top-15。raw: `ablation_t1/rerank_*.json`。

| 配置 | overall | concept | cross_domain | mixed | single_domain |
|------|---------|---------|--------------|-------|---------------|
| **cosine top-15 (baseline)** | **84.0%** | 84.6% | 61.5% | 92.3% | 96.4% |
| rerank pool30 → top-15 | 80.2% | 84.6% | 53.8% | 92.3% | 89.3% |
| rerank pool50 → top-15 | 80.2% | 92.3% | 53.8% | 92.3% | 82.1% |
| rerank pool100 → top-15 | 80.2% | 100.0% | 46.2% | 92.3% | 82.1% |
| rerank pool100 → top-8 | 67.9% | 96.2% | 26.9% | 88.5% | 60.7% |
| cosine K=100 (天花板, 仅参照) | 95.3% | 100.0% | 92.3% | 92.3% | 96.4% |

**三个 pool 全 80.2% overall, 均 < baseline 84.0%。** 清晰 tradeoff: pool↑ → concept↑ (84.6→100%),
但 cross_domain↓ (61.5→46.2%) + single_domain↓ (96.4→82.1%)。

## 9. 机制 (直接 rank-tracing 证实, 非推测)

对真实 test 问题追踪 gold source 在 cosine vs rerank 的排名 (rerank off 取 cosine top-100, 再 rerank 同池):

| 题 | 类别 | gold | cosine 排名 | rerank 排名 | 判定 |
|----|------|------|------------|------------|------|
| q08 | cross_domain | domains/DM/spec.md | **#2** | **#17** | ❌ reranker 把 cosine 第 2 降到 17, 挤出 top-15 |
| q04 | single_domain | domains/TV/spec.md | **#7** | **#22** | ❌ 同样被降级出 top-15 |
| q02 | single_domain | domains/DM/spec.md | #22 | #20 | 两者都 >15 (本就难) |
| q07 | cross_domain | VARIABLE_INDEX.md | #75 | #71 | 深位, rerank 几乎没动 |
| q34 | cross_domain | VARIABLE_INDEX.md | None | None | 不在 top-100 (T1 已知表示缺口) |

**结论 (证实)**: 通用 reranker (`rerank-v3.5`) **系统性降级简洁的 spec.md 变量表 / 索引**, 偏好"用散文讨论该话题
的 chapter 块"。q08 是铁证: cosine 把 DM/spec.md 排第 2, rerank 推到 17。rerank **替换**了 cosine 排序,
而 cosine 对结构化 spec/index 内容本来就强 → rerank 破坏了强信号。

(注: 此前对 ae.md/vs.md 误判为"截断"的教训已记取 — 本次机制用直接 rank-tracing 测量, 非套假设。)

## 10. 路线更新 (T2 后, 取代 §6)

| 任务 | 判断 |
|------|------|
| **T2 Cohere rerank** | ❌ **死亡** — 全 pool 劣于 cosine; 通用 reranker 与"权威 source = spec/index"目标相悖 |
| **T4 多查询/HyDE** | ⬆️⬆️ **升为首选** — 不替换 cosine 排序, 而是**改进 query** (cosine 对结构化内容强, 该保留); 对 cross_domain 多查询分检索合并最对症 |
| **RRF 分数融合** | 候选 — 若仍想用 rerank 信号, 用 reciprocal-rank-fusion 融合 cosine+rerank 排名 (而非纯 rerank 替换), 保住 cosine 的 spec.md 优势; 但 rerank 主动降级正确答案, 融合至多折中 |
| **T5 embedding -large** | 针对性候选 — 对 4 硬核 (尤其 ae/vs 语义距离) 评估 |
| **T6 KG** | 维持 defer |

## 11. T2 后下一步 (待用户决策)

**rerank 不是这个 KB 的对的工具。** 建议 pivot 到 **T4 (多查询/HyDE)**: 保留 cosine 排序 (对 single/mixed 已 92-96%),
用查询改写把 cross_domain 深位 chunk 在各自子查询里顶上来。无需新 provider/key (用现有 OpenAI/DeepSeek)。
RRF 融合为备选。代码改动 (rerank pipeline) 保留在 `rag.py` (默认 off, 向后兼容), 不删 (规则 B)。

---

# 第三部分: T4 查询扩展 (multiquery / HyDE / hyde_rrf) — 2026-06-08

> 用户 2026-06-08 选 T4。实现 multiquery (LLM 分解→RRF 融合) + HyDE (LLM 假想答案→嵌入) + hyde_rrf
> (原 query + HyDE 双列表 RRF, "增强非替换")。扩展用 DeepSeek (现有 key), 通用 prompt (非 eval 调优)。
> 全 retrieval-only, q37 修, top-15, 0 fallback (扩展全程真跑)。raw: `ablation_t1/t4_*.json`。

## 12. T4 结果

| 配置 | overall | concept | cross_domain | mixed | single_domain |
|------|---------|---------|--------------|-------|---------------|
| cosine baseline top-15 | 84.0% | 84.6% | 61.5% | 92.3% | 96.4% |
| T4 multiquery (4列表RRF) | 76.4% ⬇️ | 80.8% | 53.8% | 92.3% | 78.6% ⬇️ |
| **T4 HyDE (replace)** | **87.7%** ⬆️ | 92.3% ⬆️ | 69.2% ⬆️ | **100.0%** ⬆️ | 89.3% ⬇️(1题) |
| T4 hyde_rrf (原+HyDE融合) | 83.0% | 84.6% | 61.5% | 96.2% | 89.3% |
| cosine K=100 (天花板参照) | 95.3% | 100.0% | 92.3% | 92.3% | 96.4% |

向后兼容: expansion=none = 84.0% (refactor 未破坏单查询路径)。

## 13. 结论

- **multiquery 失败** (76.4% < baseline): 4 个子查询列表 RRF, 子查询共识噪声 outvote 原 query 的强命中, single_domain 大跌 (96.4→78.6%)。与 rerank 同病: 稀释/替换强信号。
- **plain HyDE 是迄今最佳单一结果** (87.7%, +3.7pt): mixed 打满 100%, concept/cross 升; single 回退仅 1 题 (噪声级)。HyDE 对"query 用变量名 / chunk 用 CT 术语"的语义距离对症 (生成的假想答案含 SDTM 术语, 拉近 embedding)。
- **hyde_rrf 反而更差** (83.0%): 2-list RRF 把 HyDE 增益稀释回 baseline, 且未恢复 single。融合非简单叠加增益。

**统一规律 (T2+T4 四次实验)**: 凡"变换 query / 重排"的技术都帮难类 (concept/mixed/cross) 但伤易类 (single_domain), 因 cosine 对结构化内容已是强局部最优。**唯一全面占优的是提高 K (K=100→95.3%), 但 top-100 不能直接喂 LLM。**

**距 95% 全类目标的真实差距**: 即便最佳 HyDE, cross_domain 仅 69.2% (远 < 95%)。cross_domain 的根因 (正确 chunk 在 cosine rank 30-100) 单查询变换到 top-15 补不上; 4 硬核 (VARIABLE_INDEX + ae/vs) 需重切分 / T5。

## 14. 战略选项 (待用户决策, T4 后)

纯检索调参在 top-15 达全类 95% 已证明很难。可选方向:
- **(A) 接受 HyDE 作温和增益** (+3.7pt, mixed 100%), 默认开 HyDE, single 1 题回退可单独修。
- **(B) 重切分 4 硬核** — VARIABLE_INDEX 按"变量→域分布"重组 + terminology chunk 文本带变量名 (治 q34/ae/vs); 这是 T1 就识别的表示缺口, 不是检索参数问题。
- **(C) T5 embedding-large (3072d)** — 全量重 ingest, 看是否抬升 cross_domain 深位 chunk 的 cosine 排名。
- **(D) T6 KG** — cross_domain 关系检索; 但 T1 已证 cross 是排名非关系缺失, KG 性价比存疑。
- **(E) 接受现状** — cosine baseline (single/mixed 92-96%) 对受信者自查够用; 95% 全类是 aspirational, 非硬需求。

代码: multiquery/hyde/hyde_rrf 全保留在 `rag.py` (默认 none, 向后兼容)。raw eval + log 全留 (规则 B)。

---

# 第四部分: 重切分 4 硬核 (re-chunk) — 2026-06-08

> 用户选"重切分 4 硬核"。executor 实现 (Rule D code review CONDITIONAL PASS, `ablation_t1/review_rechunk.md`):
> §一 24-row 表 → 24 per-variable chunk; §三 135-row 表 → 135 per-CT-code chunk; terminology codelist
> chunk 注入 "Used by variable(s): 域.变量"。VARIABLE_INDEX 65→222 chunk, 全 KB 4146→4303 chunk。
> 重 ingest (修了 ingest.py embed 无 429 重试的 bug) → collection sdtm_kb_v1 重建。pytest 216 全过。

## 15. re-chunk v2 结果

| 配置 | overall | concept | cross_domain | mixed | single_domain |
|------|---------|---------|--------------|-------|---------------|
| cosine baseline (v1) | 84.0% | 84.6% | 61.5% | 92.3% | 96.4% |
| **re-chunk v2** | **82.1%** ⬇️ | 76.9% ⬇️ | **76.9%** ⬆️ | 84.6% ⬇️ | 89.3% ⬇️ |

- ✅ **q07 + q34 修好** (0%→100%): §一/§三 拆分按验证生效, cross_domain 61.5→76.9%。
- ❌ **q16/s04/s05 仍 50%**: terminology 注入 "Used by AE.AESEV" 太简短, 未拉进 top-15 (我验证用的是更丰富的文本)。
- ❌ **3 题回归** (q02/q13/q43) + concept/mixed/single 各掉 1 题: **净 -1.9pt**。
- 根因 (已诊断, 非 bug; ID 无碰撞 4303 全唯一): 222 个新索引条目 chunk 在**域内查询**里挤占 spec.md (q02 "DM 必填变量": 2 个 VARIABLE_INDEX chunk 排 #3-4, DM/spec.md 跌出 top-15)。固有 precision/recall tradeoff。

## 16. 总结论 (T1→T4→re-chunk 全调查)

**贯穿 6 次实验的铁律: 这个 KB + eval 处在 precision/recall 前沿, 每个单一检索杠杆都"帮某类、伤另类"。**

| 杠杆 | 净效果 (overall) | 帮 | 伤 |
|------|------|----|----|
| cosine baseline | 84.0% (基准) | — | — |
| T2 rerank | 80.2% ❌ | concept | single/cross (降级 spec.md) |
| T4 multiquery | 76.4% ❌ | — | single (稀释) |
| T4 HyDE | **87.7%** 🟡 最佳 | mixed/concept/cross | single (1题) |
| T4 hyde_rrf | 83.0% ❌ | — | 稀释回 baseline |
| re-chunk v2 | 82.1% ❌ | cross (q07/q34) | 域内查询 (挤占 spec.md) |

**cosine top-15 baseline (84.0%) 是强局部最优。全类 95% @ top-15 单杠杆做不到。** 真正可能的路径只剩:
- **(P1) 查询条件路由**: 每个杠杆只对它擅长的类生效 (分布查询→VARIABLE_INDEX 条目 chunk; 术语查询→HyDE; 域内查询→纯 cosine)。需 query classifier (router.py 存在但未接)。**这是把各杠杆的局部胜利组合起来、避开 collateral 的唯一路子**, 但是更大的架构件。
- **(P2) 接受 baseline**: single/mixed 92-96% 对受信者自查够用; 95% 全类是 aspirational。
- **(P3) 提高操作点**: top-K 调大 (K=100→95.3%) 但 LLM context 成本高。

**当前 live collection = v2 (re-chunk, 净 -1.9pt)**; v1 baseline 在 `data/chroma_backup_20260608T104724Z/` 可恢复。
chunker 代码改动正确 (Rule D CONDITIONAL PASS), 保留可供 P1 条件路由复用。
