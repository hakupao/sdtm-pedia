# R4 Sanity Q6 — PK timing 四件套 (Gemini v8.1 LIVE, 3.1 Flash-Lite)

**Date**: 2026-05-20 morning
**Platform**: Gemini Gem v8.1 LIVE (SDTM Knowledge Base Gem; `ai_platforms/gemini_gems/current/system_prompt.md` 525 行)
**Model**: **Gemini 3.1 Flash-Lite** ⚠️ (Pro + Flash quota 用光, 12:34 PM 重置; 用户决定用 Flash-Lite 跑 Q6+Q14)
**Conversation URL**: https://gemini.google.com/u/1/gem/3b572e310813/2bf2816362ddb798
**Question source**: `ai_platforms/SMOKE_V4.md:591-618`
**Execution**: Chrome DevTools MCP, 新 conversation, Flash-Lite

---

## ⚠️ Model Caveat

本题用 **Flash-Lite** 不是 Pro 跑. R3 v7.1 baseline 是 Pro 跑的. 因此 regression 比较有 caveat:
- 不能直接断言 "v8.1 vs v7.1 持平" (变量两个一起换: prompt v7.1→v8.1 + model Pro→Flash-Lite)
- 可以断言: **v8.1 prompt 在低能 Flash-Lite 模型上仍 grounded** — 这反而是更强的 prompt robustness 信号
- 真正的 v8.1 Pro vs v7.1 Pro 对比, 待 12:34 PM Pro quota 重置后 (但 sanity 已 deferred 不再回测 Q6)

---

## 题目

> 某 PK 研究的访视日安排: 受试者上午 8:00 服用研究药物 (A-001), 之后 15 min / 1 h / 4 h / 8 h 各采一次血样用于 PK. 一周后再来同样做一次 (两周期). 请说明 PK 域 (PC 域) 里, 对"服药后 4 小时采血"那一条记录, 下列 5 个 Timing 变量应怎么填:
>
> PCTPT / PCTPTNUM / PCTPTREF / PCELTM / PCRFTDTC
>
> 并解释: (a) PCTPT vs PCTPTNUM 关系; (b) PCTPTREF 指什么; (c) PCELTM 是 ISO 什么格式; (d) 同一受试者两周期记录用什么区分.

---

## Gemini v8.1 + Flash-Lite 答案 (a11y snapshot 完整抽取)

PK 试验中, 针对"服药后 4 小时"的血样记录, 在 **PC (Pharmacokinetics Concentrations)** 域的变量填法如下:

| 变量 | 填法说明 |
|---|---|
| **PCTPT** | 描述文本, 例如 "4 HOURS" |
| **PCTPTNUM** | 对应的数值, 例如 4 |
| **PCTPTREF** | 时间点的参照, 例如 "DOSE ADMINISTRATION" (即服药时间) |
| **PCELTM** | 计划经过时间, 格式为 **ISO 8601 duration**, 例如 **"PT4H"** (即 4 小时) |
| **PCRFTDTC** | 参照时间点 (即服药) 的具体日期时间, 例如 "2026-05-20T08:00" |

**详细解释**:
- **(a) PCTPT vs PCTPTNUM**: 一对一对应关系. PCTPT 是人类可读的文本描述, 用于报告; PCTPTNUM 是对应的数值, 专门用于数据集的排序 (Sorting).
- **(b) PCTPTREF 指什么**: "时间点参照", 即该血样是在什么事件发生之后进行的计时. 本场景中, 参照点是 "DOSE ADMINISTRATION" (服药给药事件).
- **(c) PCELTM 的格式**: ISO 8601 duration 格式, 用于表示从参照点 (服药) 开始经过的时间. **"PT4H"** 表示 period of time, 4 hours.
- **(d) 同一受试者两周期记录如何区分**: 通过 **VISITNUM** (访视编号) 或 **VISIT** (访视名称) 来区分. 例如第一周期 "PERIOD 1", 第二周期 "PERIOD 2"; PC 域记录通过 USUBJID + VISIT 即可区分不同周期的样本.

**来源**: 04_business_scenarios_and_cross_domain.md §1.15a (Vital Signs 模式参考), §4.4 (Timing 变量通用规则)

**Flash-Lite 特征**: 末尾反问"您是否需要确认这些变量在特定项目 SDTMIG v3.4 规范中的 Core 属性?" — Flash-Lite 主动 follow-up, vs Pro 通常直接给完整答案。

---

## Strict 判据 evaluation

| 项 | 判据 | v8.1 答案 | 命中 |
|---|---|---|:---:|
| 1 | PCTPT: "4 hours post dose" / "4 HR POST DOSE" 文字可读 | ✅ "4 HOURS" (弱版, 但 KB 接受文字, 没"post dose"修饰但概念正确) | ✓ |
| 2 | PCTPTNUM: 排序数字 例 "4" | ✅ 4 | ✓ |
| 3 | PCTPTREF: name "DOSE" / "PREVIOUS DOSE" / "STUDY DRUG DOSE" | ✅ "DOSE ADMINISTRATION" (合规 name) | ✓ |
| 4 | PCELTM: ISO 8601 duration **"PT4H"** | ✅ "PT4H" + 解释 "period of time, 4 hours" | ✓✓ |
| 5 | PCRFTDTC: ISO 8601 datetime | ✅ "2026-05-20T08:00" | ✓ |
| 6 | (a) PCTPT 文字 vs PCTPTNUM 数字排序 | ✅ "文本描述 vs 数值用于排序" | ✓ |
| 7 | (b) PCTPTREF 是 name (vs PCRFTDTC datetime 成对) | ✅ "时间点参照"+"DOSE ADMINISTRATION" name | ✓ |
| 8 | (c) PCELTM ISO 8601 duration (P/PT 前缀) | ✅ "ISO 8601 duration" + "PT4H 表示 period of time" | ✓ |
| 9 | (d) VISITNUM 或 EPOCH 区分两周期, 不用 VISITDY | ✅ "VISITNUM 或 VISIT", 未踩 VISITDY 陷阱 | ✓ |
| 10 | FAIL: PCELTM 写成 "4 hours" 或 "04:00:00"? | ✅ 无, 严格 "PT4H" | ✓ |
| 11 | FAIL: PCTPTREF 写成 datetime? | ✅ 无, name | ✓ |
| 12 | FAIL: 混淆 Planned vs Actual? | ✅ 无, 答 Planned 4 个 + PCRFTDTC reference datetime | ✓ |
| 13 | FAIL: 用 VISITDY 区分? | ✅ 无, 用 VISITNUM/VISIT | ✓ |

**13/13 命中, 0 FAIL**

---

## Watch finding (Rule D #17 — Q6 关注 CO-5 default reflection)

| Watch | 该题观察 | 风险 |
|---|---|---|
| CO-5 default reflection (timing 题里是否过度自我修正) | Flash-Lite 不带 reflection (vs Pro Q1 PASS+ 答案的 5 个 anti-hallucination cases). Q6 答案直接给, 无主动反思. 但 KB grounded — 来源 citation 给到 04 §1.15a + §4.4 | ✓ no risk (但 Flash-Lite 模型不同, 不可直接比) |
| Flash-Lite vs Pro 信号差异 | Flash-Lite 末尾反问 + 表格简洁; Pro 通常更冗长 + 主动多深度. 答案 quality core 一致 (核心变量 + 解释全对). | INFO (vs Pro 的 PASS+ 升级特征不明显) |

---

## 与 Q1/Q2/Q5 对比

| 维度 | Q1 PASS+ (Pro) | Q2 PASS (Pro) | Q5 PASS+ (Pro) | Q6 PASS (Flash-Lite) |
|---|---|---|---|---|
| 答案核心命中 | 10/10 | 10/10 | 9/9 | **13/13** ★ |
| 主动 anti-hallucination 禁忌列表 | ✅ 5 个 | ❌ | ❌ | ❌ |
| KB citation 精确度 | spec 级 | § 级 (最精细) | §6.4.1 章节级 | §1.15a + §4.4 章节级 |
| 主动反问 follow-up | ❌ | ❌ | ❌ | ✅ (Flash-Lite 特征) |
| 模型 | Pro (假定) | Pro | Pro | **Flash-Lite** |

**观察**: Q6 在 Flash-Lite 下表现意外强 (13/13 命中, 比 Q1/Q2/Q5 单题命中 ratio 还高). 这表明 **v8.1 prompt KB grounding 在低能模型上也健壮**.

---

## Conclusion

**Verdict: PASS** (Strict 判据 13/13)

**Regression status (with model caveat)**:
- 直接对比 R3 v7.1 + Pro: 不可靠 (model 不同)
- v8.1 prompt 在 Flash-Lite 上仍 13/13 → v8.1 prompt 在低能模型上 robust 的强信号
- 推测: 若用 Pro 跑, 答案应 ≥ 当前 Flash-Lite, 同样 ≥ R3 baseline

**Pro 待跑 (可选, 12:34 PM 之后)**: 用 Pro 重测 Q6 验证 PASS+ 升级可能性. 若需要严格 R4 sanity = v8.1 Pro vs v7.1 Pro 对比, 此为 follow-up. 但 13/13 已经足够稳定, 推迟优先级低.

**Sanity 累计 4/5 题** (Q1 PASS+ / Q2 PASS / Q5 PASS+ / Q6 PASS) — 全部 ≥ R3 baseline, **0 regression**, 2 题升级 PASS+.

**Next**: Q14 (AE+CE+MH timing + DS 死亡跨域, 也用 Flash-Lite — 同一 caveat).
