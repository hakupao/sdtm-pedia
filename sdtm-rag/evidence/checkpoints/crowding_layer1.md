# 层① 同质簇挤占的结构量化 (全 140 题, k=15)

> 探针: `eval/crowding_probe.py` · 单测: `scripts/tests/test_crowding_probe.py` (12 passed)
> 数据: `crowding_layer1.json` (单次快照, 140 题) · `crowding_layer1_stability.json` (跨进程验稳, 16 题 × 20 进程)
> 口径: 生产口径 hybrid + structured_lookup, `top_k=15`, `hybrid_pool=30`

**本探针只描述结构, 不判定好坏。** 挤占是否有害归层② (Task 6) 的 context A/B + LLM judge ——
用 gold 判据永远判不出来, 因为 S1 前置注入已经确定性地钉死了 gold recall。

复跑:

```bash
.venv/bin/python -m eval.crowding_probe --output evidence/checkpoints/crowding_layer1.json
```

## 1. 汇总

| 指标 | 值 |
|---|---|
| 最大同名 section 簇 ≥3 席 | **40/140 (28.6%)** |
| ≥5 席 | 11 题 (7.9%) |
| ≥8 席 | 3 题 (2.1%) |
| 平均 `dup_seats` | 1.73 / 15 |
| 平均 `distinct_sections` | 13.27 / 15 |

重灾 (按 `max_cluster`; 同值间的先后无意义):
q38 `§DOMAIN` **14/15 席** · q104 `§VISIT` 9 · q39 `§Model Definition` 8 ·
q08 `§USUBJID` 7 · q29 `§Related Domains` 7 · q81 `§DOMAIN` 7。

以上六个数字与 spec §0 (scratchpad 版探针跑出) **逐值相同**; 落库版与 scratchpad 版的
全部差异见 `evidence/failures/task4_step5_probe_landing_diff.md` (差异只在 1 题的
`max_cluster_section` 标签, 且根因是已知抖动, 不是口径改动)。

## 2. 可复现性声明 (引用本表任何数字都必须连这段一起带)

> 本表逐题数字出自**单次** top-15 (生产口径 hybrid + S1), 并已按 Task 3B 的口径做过稳定性验证:
> **20 个独立进程**各跑一遍全 140 题 (跨进程取样是必须的 —— 进程内取样严重偏向单一状态, ~95%),
> 结果 `max_cluster` **0/140 题**变化, `dup_seats` / `distinct_sections` **1/140 题**变化 (q47);
> 另有 8400 次向量扰动的独立测量结论一致。
> 故基于 `max_cluster` 的数字可直接引用; **q47 (接近四六开) 与 q117 的
> `dup_seats`/`distinct_sections` 不稳定, 已按分布单独标注**。
> 抖动的完整量化与方法论见 `evidence/checkpoints/topk_jitter.md`
> (含"同进程内重复 N 次不是 N 个独立样本"这一坑, 以及根因: Chroma HNSW 在一批向量完全相同的
> 重复 chunk 之间的选择进程内稳定、换进程会变)。
> **排位一律不可复现**, 本表不含也不支持任何按排位下的结论。

`max_cluster` 豁免的**机制与失效条件** (topk_jitter.md §5.6, 引用豁免必须一起带):
抖动换的是"哪个域"(TE↔OE↔TR↔RP), 而这些 chunk 全是 `domains/*/spec.md#1`、section 一律
`DOMAIN` ⇒ **换人不换 section** ⇒ 簇大小恒定。根因是重复 chunk **正文逐字节相同**, 正文相同则
**section 必相同** ⇒ **抖动天然发生在簇内部**。**失效条件 (任一成立即须重测)**:
Task 6 去重拆掉歧义源 / Task 8 重灌索引 / 改切分或 section 命名 / 改 `top_k`、`hybrid_pool`、融合权重。

## 3. 落库版自己的跨进程验稳 (16 题 × 20 进程 = 320 个独立样本)

Task 3B 的 140 题验稳出自它自己的一次性脚本; 本节是**用落库的 `crowding_stats`** 重新取样,
确认换了实现之后结论不变。取样一律走 `eval.jitter_probe.stability_across_processes`
(真子进程) —— 本仓不许有第二份跨进程逻辑。

题面 = `max_cluster ≥5` 的 11 题 ∪ 3B 报过成分或统计会变的 5 题 (q38/q47/q117/q120/q31/q133)。

```bash
.venv/bin/python -m eval.crowding_probe --cross-process 20 \
  --ids q38,q47,q117,q120,q104,q39,q08,q29,q81,q77,q108,q07,q84,q118,q31,q133 \
  --stability-output evidence/checkpoints/crowding_layer1_stability.json
```

| 题 | 见到几种 top-15 成分 | 进出的条目数 | 见到几种统计取值 | 取值分布 `(max_cluster, dup_seats, distinct_sections)` |
|---|---|---|---|---|
| q38 | **3** | 4 | 1 | (14,13,2)×20 |
| **q47** | 2 | 2 | **2** | **(2,2,13)×12 / (2,1,14)×8** |
| **q117** | 1 | 0 | 1 | (2,2,13)×20 |
| q120 | 2 | 4 | 1 | (2,1,14)×20 |
| q31 | 2 | 2 | 1 | (4,6,9)×20 |
| q133 | 2 | 2 | 1 | (2,1,14)×20 |
| q104 | 1 | 0 | 1 | (9,8,7)×20 |
| q39 | 1 | 0 | 1 | (8,8,7)×20 |
| q08 | 1 | 0 | 1 | (7,7,8)×20 |
| q29 | 1 | 0 | 1 | (7,9,6)×20 |
| q81 | 1 | 0 | 1 | (7,6,9)×20 |
| q77 | 1 | 0 | 1 | (6,5,10)×20 |
| q108 | 1 | 0 | 1 | (6,5,10)×20 |
| q07 | 1 | 0 | 1 | (5,5,10)×20 |
| q84 | 1 | 0 | 1 | (5,4,11)×20 |
| q118 | 1 | 0 | 1 | (5,4,11)×20 |

**q47 (点名, 必须按分布读)**: 落库版**逐值复现** 3B 的 `(2,2,13)` 12/20 vs `(2,1,14)` 8/20
—— **接近四六开, 不是罕见抖动。它的 `dup_seats`/`distinct_sections` 逐题值不能当事实引用。**

**q117 (点名)**: 本批 20 个进程见到 **1 种**取值。3B 见到它翻是在**固定 query 向量**那批
(1/20)。**这不是"3B 错了", 正是"不同批次见到的状态集合不同"的实例** —— 恰恰因此,
q117 的逐题值同样不能当事实引用。

**q38 的成分变了 3 种, 统计纹丝不动** —— §5.6 豁免机制的一次独立现场验证:
换掉的是 `domains/{TE,TR,OE,TU}/spec.md`, 它们的 section 全是 `DOMAIN`, 换人不换 section。

**能证明什么 / 不能证明什么**:

- 能: 这 16 题里**见到**统计取值多于一种的只有 q47; 其余 15 题在 320 个独立样本里没见到变化。
- 不能: `n_procs=20` 是**检出不稳定的下限**, 不足以刻画分布尾部 —— 实测稀有态在 1/20 量级,
  且不同批次见到的状态集合不同 (q117 本批就没见到)。**"×20" 是次数, 不是概率**;
  "没见到变化" ≠ "不会变"。
- 不能: 本节只覆盖 16 题, 不能替代 3B 那次 140 题全集验稳; 两者结论一致 (q47 是唯一统计翻的题)。
- 不能: 任何按**排位**的结论 —— 那个维度本身不可复现, 一律作废。

## 4. 两条使用禁忌

1. **`composition` 是单次快照**。"有 14 席被 §DOMAIN 占掉"可引用; "AE 排在 FA 前面"不可引用。
2. **`max_cluster_section` 在并列时由排位决定** (`Counter.most_common(1)` 按插入顺序打破并列,
   而插入顺序 = top-k 排位)。实测 140 题里 **71 题**的最大簇存在并列 (其中 **49 题**是
   `max_cluster == 1`, 即压根没有簇, 那个 section 名纯属排位产物)。**只有 `max_cluster ≥2`
   且无并列时, 这个字段才有意义**; 跨进程分布的取值键因此**不含**该字段
   (否则会把排位噪声伪装成"统计量不稳")。
