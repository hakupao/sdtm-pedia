# Plan B Phase 3 勘察报告 — CDISC 变量索引挤占修复

> 日期: 2026-08-06 · 性质: **只读勘察, 零代码改动, 零 commit**
> 题集: `sdtm-rag/eval/test_set_v3.yml` (CDISC 140 题) · retrieval-only · top_k=15
> 索引: `sdtm_kb_v1`, 4303 chunks

## 0. 结论先行

**不值得做。** 在生产配置 (hybrid + structured-lookup) 下, VARIABLE_INDEX 挤占对 source
recall 的代价**实测为 0**: 140 题中受挤占影响而失分的题数 = **0**。我把 spec 描述的触发
形状实现出来跑了反事实对照, **Δrecall = +0.00pt, 零回归也零收益**。spec 写这条时的依据
(`cdisc_gold_scope_review.md` §6 待办的 q43/q100/q132 三题共因) 成立于 **hybrid-only 通道**,
而这三题在生产通道里**已经被 S1 的域名直查通道修好了, 现在全是 1.0**。

Phase 3 是在修一个**已经被 Phase 之前的工作修掉的问题**。

## 1. 基线复现 (记账口径)

两条通道都用同一索引、同一题集实跑复现, 与团队给的基线逐位吻合:

| 通道 | overall source recall |
|---|---|
| **hybrid-only** (S1 关) | **81.07%** |
| **hybrid + structured-lookup (S1)** = 生产 | **98.93%** |

生产通道 140 题里**只有 2 题不满分**, 且两题的 top-15 里 **VARIABLE_INDEX chunk 数均为 0** ——
与挤占无关:

| 题 | recall | miss | 归因 |
|---|---|---|---|
| q38 | 0.0 | `chapters/ch02` | chapters ≤20KB 整 file 单块策略 (scope review §2, 另一条待办) |
| q126 | 0.5 | `domains/TE/spec.md` | 已归档的**永久 known limit** |

## 2. 挤占量化 (生产通道, 140 题)

| 指标 | 数值 |
|---|---|
| top-15 里出现 ≥1 个 VARIABLE_INDEX chunk 的题 | **100 / 140** |
| 其中 gold **就是** VARIABLE_INDEX (对冲风险集) | **18** |
| 其中 gold **不是** VI 的题 | 82 |
| … 且 gold 含 domain spec (= **挤占候选集**) | **63** |
| **挤占候选集里 recall < 1.0 的题** | **0** (63 题全部 1.0) |
| VI 占用的 top-k 槽位总数 | 224 / 2100 = **10.7%** |
| 其中落在挤占候选集内 | 160 |
| 其中由 S1 主动 union-add 的 | 29 (其余 195 是 cosine/BM25 自己捞上来的) |

**挤占候选集 63 题的 recall 分布: `{1.0: 63}` —— 单点分布, 没有任何离散。**

### 2.1 hybrid-only 通道 (spec 依据所在的那条通道)

hybrid-only 下挤占确实存在且严重, 但**已被 S1 全额吸收**:

- 挤占候选集 66 题, 其中 **17 题** recall < 1.0
- 其中 **13 题** 明确 miss 了自己的 domain spec gold
- 这 13 题 (q02/q04/q09/q24/q06/q32/q43/q64/q100/q129/q132/q134/q135) **在生产通道里全部 = 1.0**

也就是说 spec §Phase 3 想要的"提升"**已经兑现了**, 兑现者是 S1 的 named-domain 通道
(`structured_lookup.py:442` 把 `domains/<CODE>/spec.md` 前置注入), 不是一个新的降权规则。

## 3. 触发形状候选 (pattern 级, 非题号特判)

从数据反推的确定性判据 —— 与 spec 描述一致, 且是纯 pattern:

> **域特定问句** := `_query_domains(query)` 非空 (查询命中某个域码 token 或该域长名, 且该域
> 有 `domains/<CODE>/spec.md`) **AND** `_is_distribution_intent(query)` 为假。

两个子句都已是 `structured_lookup.py` 里现成的、meta.yaml 驱动的通用函数, 不含任何题号、
题面或硬编码变量名。

**触发面: 140 题中 80 题命中 (57%)。**

| 性质 | 数值 |
|---|---|
| 触发的 80 题当前 recall 分布 | `{1.0: 80}` — 全满分 |
| 触发的 80 题里 gold 含 VARIABLE_INDEX 的 | **0** |
| 触发的 80 题里 VI 占的槽位 | 154 |

`not dist_intent` 这一子句是**载荷子句**: 18 道 gold=VI 的题 **全部** `dist_intent=True`,
所以该子句把对冲风险集**完整、无重叠地**排除掉了。

## 4. 反事实实测 (把修法跑出来)

按上述判据实现"命中即从 top-15 过滤掉全部 VARIABLE_INDEX chunk 并从深池 (top-40) 回填",
对 140 题全量实跑:

```
baseline (top15 of deep40)     = 0.9893
VI-filtered on trigger shape   = 0.9893
delta                          = +0.00 pt
changed questions              = []          ← 一道题的分都没动
REGRESSIONS                    = []
```

**收益 0, 风险 0, 净值 0。** 这不是"改动太保守没生效", 而是被挤占的题在生产通道里本来就
没有失分点可捡 —— 天花板就是 0。

## 5. 对冲风险评估 (最大风险点)

gold **就是** VARIABLE_INDEX 的题共 **18 道**, 即 S1 的 (2) 类分布/关系通道:

`q07 / q34 / q66 / q67 / q68 / q69 / q71 / q77 / q103 / q104 / q105 / q106 / q107 / q108 / q109 / q110 / q111 / q112`

这 18 题当前**全部 recall = 1.0**, 全部 `dist_intent=True`, 全部依赖 VI chunk 得分
(共占 35 个槽位)。

**带 `not dist_intent` 守卫的版本对这 18 题零影响** (已实测, 见 §4)。

但我实测了**去掉守卫的朴素版本** (只看"是否命名了域"), 用来量化守卫的价值:

```
NAIVE (无 dist 守卫) = 0.9821    delta = -0.71 pt
REGRESSION: q67  1.0 → 0.0
  "Many SDTM variables use the No Yes Response codelist C66742. How many ..."
```

q67 同时命名了域 `AE` 且 gold 是 VARIABLE_INDEX —— 这就是对冲风险的真实形态。守卫能挡住
它, 但这也说明: **该修法的下行风险是真实的, 上行收益是 0**。风险收益比无穷差。

## 6. 挤占的真实残余: 答案组装侧, 且很小

source recall 看不见的那一层, 我也量化了。挤占最难看的样本是 **q43**:

```
q43 "What is the CT codelist for the SEX variable in the DM domain? ..."
  rank 0  [S1] domains/DM/spec.md § SEX          ← gold
  rank 1  [S1] terminology/core/dm.md § Sex      ← gold
  rank 2-14: 12 个 VARIABLE_INDEX "§三 CT 交叉引用" 一行式 chunk
             其中 7 个与本题完全无关 (AE.AEACNDEV / BE.BEDECOD / IS.ISBDAGNT / DD.DDTEST ...)
```

recall = 1.0 (两条 gold 都在 rank 0/1), 但 15 个槽位里 12 个被 VI 的模板化一行 chunk 吃掉。
根因是 §三 CT 交叉引用 chunk 全是同一句式模板, BM25 对模板文本高度同质匹配。

全量量化这类"纯噪声槽位":

| 指标 | 数值 |
|---|---|
| VI chunk 按小节分类 (全 140 题, 共 224) | §三 CT 交叉引用 114 / 域表 73 / §一 通用变量 37 |
| 挤占候选集内的 §三 chunk 中, **与问题相关**的 | 66 |
| 挤占候选集内的 §三 chunk 中, **完全无关**的 | **28** |
| 无关槽位占比 | 28 / 2100 = **1.3%** |
| 受影响题数 (≥1 个无关槽位) | **9** (q43/q16/s05/q48/q59/s01/q92/q44/q45) |

即使把这 28 个槽位全清干净, 也只腾出 1.3% 的上下文, 分散在 9 道题上, 且这 9 道题的
source recall 已全是 1.0。要证明它对**答案质量**有正收益, 得跑带 judge 的全量答题评测 —— 而
1.3% 的槽位变化预期效应远小于 judge 评测本身的噪声, 属于**不可证伪的改动**。

另附一条对 scope review 原文的订正: 该文档担心 q100 会被 VI 里"带星号的跨域聚合值"误导
(`ARMCD ... Record Qualifier*, Core Exp*`)。实测该 chunk 在 rank **10**, 而 `domains/TA/spec.md § ARMCD`
在 rank **0**, 且被召回的另一个 VI chunk 恰是 TA 域自己的小节表。误导风险比原文估计的低得多。

## 7. 建议

**放弃 Phase 3, 或把它降级为一条已关闭的待办。** 理由三条, 每条都有实测支撑:

1. spec 圈定的受影响题集 (q43/q100/q132 及其同类共 13 题) **已在生产通道全部修复**, 修复者
   是既有的 S1 named-domain 通道。
2. 按 spec 描述实现触发形状并全量实跑, **Δrecall 精确为 0**, 一道题的分都没动。
3. 唯一残余是 1.3% 的上下文噪声槽位 (28/2100, 9 题), 其收益不可证伪, 而下行风险 (18 道
   gold=VI 的分布题) 真实存在 —— 守卫写错一处就是 -0.71pt。

若将来仍想动这块, **正确的靶子不是"域特定问句降权 VARIABLE_INDEX", 而是 §三 CT 交叉引用
chunk 的同质化模板文本** (114/224 的 VI 槽位来自它)。那属于 chunk 构造/索引侧问题, 与
Phase 3 的路由侧修法是两回事, 且应先有能测出答案质量差异的评测手段再动。

同一份数据也重申了另外两条**未关闭**的待办, 它们比 Phase 3 值钱:
- **q38**: `chapters/` ≤20KB 整 file 单块策略 (ch01/ch02/ch03 各只有 1 个 chunk, 语义稀释) —— 唯一
  一道 0.0 的题。
- **source 判据 chunk 粒度化**: Plan B Phase 0 已加的 `路径#节` 语法尚未在 CDISC 题集铺开;
  VARIABLE_INDEX 有 222 chunk, 路径级匹配对它判别力≈0 (scope review §0 的血教训)。

## 附: 复现方式

勘察脚本置于本 session scratchpad (`.../scratchpad/p3probe/`), 未写入仓库。产物
`probe_hybrid_s1.json` / `probe_hybrid_only.json` 含 140 题逐题的 top-15 来源、VI 槽位、
S1 通道命中标记与 recall。基线可用仓库内命令直接复核:

```
cd sdtm-rag
.venv/bin/python eval/run_eval.py eval/test_set_v3.yml --retrieval-only --hybrid              # 81.07%
.venv/bin/python eval/run_eval.py eval/test_set_v3.yml --retrieval-only --hybrid --structured-lookup  # 98.93%
```
