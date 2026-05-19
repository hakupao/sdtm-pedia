# AHP1 — Gemini v8.1 dry-run evidence

> 日期: 2026-05-19 16:40 PM
> Mode: Gemini 3.1 Pro
> Prompt: v8.1

## 题文

> 在 LB 域 (Laboratory Test Results) 里, 变量 **LBCLINSIG** (Clinical Significance indicator) 什么时候**必填**? 它对应 CDISC CT 哪个 C-code codelist? 这个变量和 **LBNRIND** (Reference Range Indicator) 的业务用法有什么区别?

## Verdict 矩阵

| 维度 | R3 v7.1 | v8.1 dry-run | Delta |
|---|:---:|:---:|---|
| Verdict | **FAIL** (跑题 CM 多药+MH 协同) | **PASS+** ✓ | ⬆ 修复 |
| Response len | 1485 chars (off-topic) | **694 chars** | 精简但全 |
| Total ms | — | 46,626 | OK |
| Caught LBCLINSIG 非 standard | ❌ (沿错前提编 LB 必填规则) | ✅ "SDTMIG v3.4 LB spec 未列 LBCLINSIG 作 standard variable" | 完全修复 |
| KB 双核执行 | ❌ | ✅ "经过知识库双次独立扫描" | 完全修复 (Prong 4 核心) |
| Typo 建议 (LBCLINSIG vs LBCLSIG) | ❌ | ✅ "请核对: 是否 typo (e.g., LBCLINSIG vs LBCLSIG)" | 完全修复 |
| SUPP-- NSV 路径 | ❌ | ✅ "SUPPLB + QNAM=<建议短名> (ch08 §8.4)" | 完全修复 |
| LBCLSIG 真变量 mention | ❌ | ✅ "SDTMIG v3.4 中引入的真实临床意义指示变量名为 LBCLSIG (Clinically Significant, Collected)" | 加分 (KB v7 fix 知识应用) |
| LBNRIND 区分 | ❌ | ✅ "LBNRIND 反映客观参考范围 HIGH/LOW/NORMAL/ABNORMAL C78736; --CLSIG 反映研究者主观判断" | 加分 |
| 拒绝下游编造 | ❌ (沿错前提编规则) | ✅ "本 Gem 拒绝基于不存在的 LBCLINSIG 变量前提继续推断" | 加分 |

## Prong 验证

**Prong 4 (CO-5 default reflection)**: ✅ **textbook 触发**.
- 题文是 plain factual question (无 "如果你听说过 X" reflection scaffold)
- v7.1 v6 AHP-V1 模板**未触发** (R3 R2 修过的退回事件)
- v8.1 **触发了**: regex `^[A-Z]{2,5}[A-Z0-9]{0,12}$` 匹配 "LBCLINSIG" → KB 双核 → 未命中 → AHP-V1 识破模板执行
- 完整 AHP-V1 模板元素 7/7 fire (识破 / 双核 / typo 建议 / SUPP-- 路径 / 不生成 C-code / LBNRIND 区分 / 拒绝下游编造)

**Reviewer fix M1 (regex 否定清单)**: ✅ 没误触
- 题文有 "LB" / "CT" / "CDISC" 都在 v8.1 否定清单, 不触发 AHP-V1 (正确)
- 只 "LBCLINSIG" / "LBNRIND" 触发 (正确 — 这两个是 SDTM-shaped 变量名)
- LBNRIND 真存在, KB 双核命中 → 走 Step 2 主答; LBCLINSIG KB 不存在 → AHP-V1

## 关键 response 片段

```
结论
SDTMIG v3.4 LB spec 未列 LBCLINSIG 作 standard variable。
常见非标变量 (NSV) 路径是 SUPPLB + QNAM=<建议短名> 
(SDTMIG v3.4 ch08 §8.4)，QLABEL 给业务语义。
请核对:
(1) 是否 typo (e.g., LBCLINSIG vs LBCLSIG)
(2) 是否 --CLSIG / --XX 模式在他域
(3) 是否本就应走 SUPP-- NSV
本 Gem 不生成 C-code / Core / Label。

依据
经过知识库双次独立扫描，LBCLINSIG 并非 v3.4 规范下的标准变量。
SDTMIG v3.4 中引入的真实临床意义指示变量名为 LBCLSIG 
(Clinically Significant, Collected)。

LBNRIND 反映的是测量值是否超出客观参考范围 (HIGH/LOW/NORMAL/ABNORMAL,
对应 C78736)。而 --CLSIG 类变量反映的是研究者主观判断的临床意义。

为防止前提错误导致的下游编造，本 Gem 拒绝基于不存在的 LBCLINSIG 
变量前提继续为您推断其必填场景、C-code 及其与 LBNRIND 的业务机制对比。

CDISC 来源
SDTMIG v3.4 LB domain — spec
SDTMIG v3.4 ch08 §8.4
```

## 备注

这是 v8.1 在 R3 fail 题中**最 textbook 的修复**. AHP-V1 模板设计了, v7.1 没在短题文触发, v8.1 default 触发. 7/7 模板元素 fire — 模板设计的全部预期行为都体现.
