# R4 Sanity Q2 — CP CD4+ T 细胞 (Gemini v8.1 LIVE, 3.1 Pro)

**Date**: 2026-05-20 AM
**Platform**: Gemini Gem v8.1 LIVE (SDTM Knowledge Base Gem; `ai_platforms/gemini_gems/current/system_prompt.md` 525 行)
**Model**: Gemini 3.1 Pro (mode picker 明确选 "3.1 Pro Advanced math & code"; **caveat**: Q1 用 Gem 默认 mode 未明示, Q2 起明确 Pro; v8.1 prompt 一致, 不影响 v8.1 regression 判定)
**Conversation URL**: https://gemini.google.com/u/1/gem/3b572e310813/2888c1adda4700bb
**Question source**: `ai_platforms/SMOKE_V4.md:469-489`
**Execution**: Chrome DevTools MCP, fully automated, 新 conversation (per 用户要求"每题新 conversation + Pro")

---

## 题目

> 某免疫治疗试验用流式细胞仪检测受试者 PBMC 样本里 "活化的 CD4+ T 辅助细胞" (通过 Ki67+ 表达识别为 ACTIVATED 状态). SDTMIG v3.4 里这个测量属于哪个域? 请说明: (a) Topic 变量是什么; (b) 如何区别"T Lym Help" 这个**命名**细胞群与 CD4+Ki67+ 这个**子集**亚群; (c) 用哪些变量记录"哪些 marker 被用来定义'活化'状态"; (d) Method 变量应填什么 (测量方法); (e) 这个域和 LB 的边界是什么.

---

## Gemini v8.1 答案 (a11y snapshot 完整抽取)

**结论**: 该测量应归入 **CP (Cell Phenotype Findings)** 域。

**(a) Topic 变量**: CP 域的 Topic 变量是 **CPTESTCD** 和 **CPTEST**。

**(b) 区别命名细胞群与子集亚群**:
- 对于科学界公认命名的细胞群, 直接将其名称填入 **CPTEST** (例如 "TLym Help")
- 当表示基于额外 marker 限定的特定子集亚群时, 必须在 **CPTEST** 的值后附加 **"Sub" 后缀** (即变为 "TLym Help Sub")
- 同时, 用于定义该子集的 marker 组合必须记录在 **CPSBMRKS** (Sublineage Marker String) 变量中 (例如包含 "CD4+")

**(c) "活化"状态及定义该状态的 marker**:
- 细胞的生物学状态本身应记录在 **CPCELSTA** (Cell State) 变量中, 在此场景下其值为 "ACTIVATED"
- 用来明确定义该"活化"状态的标志物 (即 Ki67 的阳性表达) 应记录在 **CPCSMRKS** (Cell State Marker String) 变量中, 取值为 "Ki67+"

**(d) Method 变量填写**:
- 测量方法应记录在 **CPMETHOD** (Method of Test or Examination) 变量中
- 本场景使用流式细胞仪检测, 因此该变量应填入 **"FLOW CYTOMETRY"**

**(e) CP 域与 LB 域的边界**:
- CP 域专门设计用于单细胞或颗粒悬液中, 基于特定表型或状态 marker 表达来表征细胞表型、谱系和功能的测试
- CP 域的引入并不旨在取代 LB 域; 常规的实验室血液学检查 (例如常规血细胞分类计数) 仍应归入 LB 域

**来源**: SDTMIG v3.4 CP domain — spec / assumptions
**段落**: CP domain spec (§CPTEST, §CPSBMRKS, §CPCELSTA, §CPCSMRKS, §CPMETHOD) / CP domain assumptions §1, §2

---

## Strict 判据 evaluation

| 项 | 判据 | v8.1 答案 | 命中 |
|---|---|---|:---:|
| 1 | 识别 CP (Cell Phenotype Findings) 域 v3.4 新增 | ✅ "CP (Cell Phenotype Findings) 域" | ✓ |
| 2 | (a) Topic: CPTESTCD + CPTEST | ✅ 两个全列 | ✓ |
| 3 | (b) 命名群 CPTEST="T Lym Help"; 子集 + "Sub" 后缀 + CPSBMRKS | ✅ 答案给 "TLym Help" / "TLym Help Sub" + CPSBMRKS "CD4+" (注: 空格 "T Lym Help" vs "TLym Help" 是 Gemini 抽取差异, 不影响概念) | ✓ |
| 4 | (c) CPCELSTA "ACTIVATED" + CPCSMRKS "Ki67+" | ✅ 两个变量 + 两个取值全对 | ✓ |
| 5 | (d) CPMETHOD = "FLOW CYTOMETRY" (C85492) | ✅ "FLOW CYTOMETRY" (未给 C85492 但 KB 锚) | ✓ |
| 6 | (e) CP vs LB 边界 (CP 单细胞 marker; LB 血生化常规) | ✅ "CP 单细胞/颗粒悬液 marker 表达" + "LB 血液学常规" + 明确"CP 不取代 LB" | ✓ |
| 7 | FAIL: 答 LB/IS/FC 域? | ✅ 无 | ✓ |
| 8 | FAIL: CPSBMRKS vs CPCELSTA 弄混? | ✅ 严格区分 (sublineage 定义子集 vs cell state 定义状态) | ✓ |
| 9 | FAIL: 漏 Sub 后缀? | ✅ 明确 "TLym Help Sub" | ✓ |
| 10 | FAIL: Method 答 PCR/ELISA? | ✅ FLOW CYTOMETRY | ✓ |

**10/10 命中, 0 FAIL**

---

## Watch finding (Rule D #17 — Q2 关注 M2 候选数限)

| Watch | 该题观察 | 风险 |
|---|---|---|
| M2 候选数限 (v8.1 可能输出 <5 候选) | Q2 涉及变量: CPTESTCD/CPTEST/CPSBMRKS/CPCELSTA/CPCSMRKS/CPMETHOD = **6 个 CP 变量全列**, 无 over-limit | ✓ no risk |
| 多变量场景 default reflection 是否过度 | 答案直接给出, 无过度自我修正; 但也没主动列"禁止臆造"对照 (vs Q1) | LOW (caveat) |

---

## 与 Q1 (PASS+) 对比

| 维度 | Q1 (PASS+) | Q2 (PASS) |
|---|---|---|
| 主动 anti-hallucination 列禁忌变量 | ✅ 5 个 (GFGENE/GFVARIANT/GFLOC/GFREFVER/GFSTYPE) | ❌ 无 |
| 主动跨域提及 | ✅ BE (Biospecimen Events) | ❌ 仅 CP vs LB (题目要求) |
| 主动引用 CT Code | ✅ C181177 | ❌ 仅暗示 C85492 (KB 锚) |
| KB section citation 精确度 | ✅ "GF domain — spec" | ✅ "§CPTEST, §CPSBMRKS, §CPCELSTA, §CPCSMRKS, §CPMETHOD + assumptions §1, §2" (Q2 更精确) |

**观察**: Q2 KB citation 比 Q1 更精细 (具体 § 锚点); 但 Q1 在 default reflection 触发 anti-hallucination 表现强. **可能因素**: Q1 题目含"臆造"风险 (基因变量易自创), CO-5 触发; Q2 题目变量名都给定/KB 明确, CO-5 不强触发. 这是 v8.1 prompt 的正常分化, 不算 regression.

---

## Conclusion

**Verdict: PASS** (R3 baseline PASS, v8.1 持平, **不退化**)

**Regression status**: ✅ 无回归. v8.1 在 Q2 上与 v7.1 等价 (核心 10 项判据全 PASS).

**Pro Mode 验证**: 本题用 3.1 Pro 明确切换. 答案长度 ~1300 字符, KB citation 精确度 § 级 — Pro 在 KB-heavy 题里偏 grounded.

**Next**: Q5 (FA vs QS vs CE 边界, 域判别题, watch CO-2f 文件格式 gate 是否误锁正常域判别).
