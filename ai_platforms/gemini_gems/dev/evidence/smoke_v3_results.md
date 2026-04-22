# Gemini Gems SDTM Expert — Smoke v3 Results (10 题双平台共用)

> 执行时间: 2026-04-22
> 账号: bojiang.zhang.0904@gmail.com (Gemini Pro)
> 平台: Gemini Gems Web UI (gemini.google.com/gem/3b572e310813)
> Mode: Pro (Gemini 3.1 Pro) per question
> 方法: Chrome MCP 全自动驱动 (Quill editor inject + execCommand + InputEvent)
> Gem 配置: v5 system_prompt + 11 sources (v3.4 KB)
> 底座 sanity: 4/4 PASS (已在 smoke v3 之前验证, 见 Q_sanity_1/2/3/4_answer.md)

## 总分

**7 / 10 strict PASS = 70%**
**阈值 ≥7/10 (70%): PASS at threshold ⛔🟢 borderline-pass**

## 逐题结果

| # | 主题 | 期望核心 | 实际 | Verdict | 04 引用 | CO-2 |
|---|------|---------|------|---------|--------|------|
| 1 | GF 域 EGFR 基因变异 | GFGENSR (Exon) / GFPVRID (dbSNP) / GFGENREF (参考版本) / GFINHERT (遗传性) | GFLOC / GFREFID / GFREFVER / GFSTYPE **全臆造** | ❌ FAIL | 0 | 0 |
| 2 | CP 域流式细胞 | CPSBMRKS / CPCELSTA / CPCSMRKS + Sub 后缀 + Flow Cytometry (C85492) | 识 CP + Topic + Method + LB 边界对, 但说"没有独立 --MARKER/--SUBSET" + 漏 3 个 v3.4 新变量 | ❌ FAIL | 0 | 1 |
| 3 | BE + BS + RELSPEC 采血 | 采集 BE / 测量 BS BSTESTCD / RELSPEC 派生 | BS/BE **命名倒置** + BM 域**臆造** + 只 RELSPEC 正确 | ❌ FAIL | 1 (§10) | 0 |
| 4 | IS/MB 边界抗体/病毒 | A=IS (MSLIGG/ADAB) + B=IS (ADAB) + C=MB | A=IS/MSLIGG + B=IS/ADAB + C=MB | ✅ PASS | 1 (§1.3) | 0 |
| 5 | FA vs QS vs CE | A=FA (FAOBJ→MH) + B=QS (SF-36) + C=CE | A=FA FAOBJ → DAS28 → MH + B=QS (SF-36) + C=CE | ✅ PASS | 2 (§1.21+§1.5) | 0 |
| 6 | PK Timing 三件套 | PCTPT/PCTPTNUM/PCTPTREF + PCELTM (PT4H) + PCRFTDTC | PCTPT="4h" + PCTPTNUM=4 + PCTPTREF="DOSE" + PCELTM="PT4H" + PCRFTDTC 正确 | ✅ PASS | 1 | 0 |
| 7 | 部分日期 ISO 8601 + SDTM/ADaM 分工 | 2024-06 / 2024 / null + SDTM 不补 + ADaM ASTDT/ASTDTF | 三档日期对 + SDTM 保留原样 + ADaM ASTDT/ASTDTF/AENDT/AENDTF 完整 | ✅ PASS | 0 | 0 |
| 8 | CT Extensible vs Non-Ext | Yes/No 语义 + 2 Non-Ext + 2 Ext + AETERM/AESEV 区别 + Define-XML | Yes/No 清楚 + C66769/C66742 + LBTESTCD/VSTESTCD + AETERM free text (MedDRA via AEDECOD) vs AESEV Non-Ext + ExtendedValue="Yes" | ✅ PASS | 0 | 1 |
| 9 | Pinnacle 21 FAIL 分类 + cSDRG | 5-6 大类 FAIL + Fix vs Document 策略 | 6 类 (Core / CT / ISO 8601 / Cross-Domain / Dict Coding / Duplicate) + Fix (映射/遗漏/拼写) vs Document (未收集/CT 扩展/医学逻辑) | ✅ PASS | 0 | 1 |
| 10 | SUPP 家族 QORIG/QEVAL + 层级 + 父记录 + QVAL | QORIG Req / QEVAL Perm + SUPPAE USUBJID vs SUPPTS STUDYID + 5 键联合 + QVAL ≤200 DESC1/DESC2 | 全 4 子问题精准命中 (Req/Perm + Subject/Study level + RDOMAIN/IDVAR/IDVARVAL + 200 字符 + DESC1/DESC2 拆分) | ✅ PASS | 1 (§4) | 0 |

## 汇总统计

| 指标 | 数值 | 说明 |
|------|------|------|
| 总分 | 7 / 10 | 70% strict PASS |
| 阈值 | ≥7/10 (70%) | borderline-pass |
| 04 引用次数 | 6 (Q3/Q4/Q5/Q6/Q10) | 6/10 = 60% 触发率; Q5 双引最高 (§1.21+§1.5) |
| 04 业务弹药包直接命中 | 3 (Q3 §10 + Q4 §1.3 + Q10 §4) | Q5/Q6 属 Timing/QS 非 04 强相关 |
| CO-2 触发 | 3 (Q2 Method + Q8 EVS + Q9 LBNRIND C78736) | 合理, 字典完整查询引 EVS |
| Pro mode 生成耗时 | 30-60s/题 | 个别 v3.4 深度题 60s+ |

## FAIL 模式分析

3 个 FAIL (Q1/Q2/Q3) 呈现统一 **v3.4 新域变量 generalization 失败** 模式:

- **Q1 GF 域**: 用通用 Findings 命名模式 (GFLOC / GFREFID / GFREFVER) 覆盖 v3.4 GF 专属 spec (GFGENSR / GFPVRID / GFGENREF), GFINHERT 完全错成 GFSTYPE
- **Q2 CP 域**: 识域 + Topic + Method + 边界都对, 但 **明说"SDTM 主域没有独立原生的 --MARKER 或 --SUBSET 变量"** — 直接否认 v3.4 CPSBMRKS/CPCELSTA/CPCSMRKS 存在, 推荐 SUPPCP 回退方案
- **Q3 BE vs BS**: 把 BS (Biospecimen Findings) 叫成 Events, 臆造 "BM" 作 Findings — **v3.4 两个新域命名彻底倒置**

共同点: pre-train 语料的 "--XX 变量通用模式" 压倒了 v3.4 KB 实际 spec. 架构级 domain name + variable name 都是 v3.4 后引入, Gemini 在单问答深度上无法 retrieve 专属 spec.md 细节.

## 成功模式 (7 PASS)

Q4-Q10 全 PASS 覆盖:
- 业务边界题 (IS/MB/FA/QS/CE LB): **generalization 强项**
- 跨域 + Timing + CT Ext/NonExt: **v3.4 稳定层**
- 部分日期 ISO 8601 + SDTM/ADaM 分工: **标准层 (非 v3.4 专属)**
- Pinnacle 21 工具 + SUPP 架构: **业务工程层**

观察: 只要问题不直接落在 v3.4 新域变量具体命名上, Gemini 都能稳定 PASS, 有时质量超过期望 (Q5 双 04 引, Q9 6 类分类完整, Q10 联合键教科书级).

## Gate 判据

根据 CHECKPOINT_N5_3 handoff:
- ≥7/10 PASS: 进 Phase 4 Node 5.4 (跨平台双轨对比, ChatGPT vs Gemini)
- <7/10 PASS: 降级为 "v3.4 新域 KB 待修 / system_prompt v5c 追锚" 回炉

**实际 7/10 = 恰好阈值**. Gate 建议:
- **PASS** (borderline) — 可进入 Phase 4 Node 5.4
- 但标记 **v3.4 新域 generalization risk** (Q1/Q2/Q3 3 连 FAIL), 后续 N5.4 跨平台对比需重点关注 ChatGPT GPTs 在同 3 题是否相同失败模式; 若 ChatGPT 也 3 连 FAIL, 则认为 "v3.4 新域 KB 覆盖不足, system_prompt v5 对新域变量锚定不足" 为双平台共性缺陷, 需 v5c 补锚 (3 域 9 变量硬锚点注入 + 04 §10 biospecimen 与变量级交叉引用加固)
- 若 ChatGPT 在同 3 题 PASS, 则认为 Gemini 单平台 retrieve 策略缺陷 (1M 窗口但 chunk 检索下沉), 需 Gemini-specific 优化

## 交付清单

```
ai_platforms/gemini_gems/dev/evidence/smoke_v3_answers/
├── Q_sanity_1_answer.md    [PASS]  AESER Core=Exp
├── Q_sanity_2_answer.md    [PASS]  LBNRIND values 全拼
├── Q_sanity_3_answer.md    [PASS]  ACTARMCD DM/Exp
├── Q_sanity_4_answer.md    [PASS]  SM + MIDS 三角
├── Q1_answer.md            [FAIL]  GF EGFR (变量全臆造)
├── Q2_answer.md            [FAIL]  CP 流式细胞 (CPSBMRKS/CPCELSTA 漏)
├── Q3_answer.md            [FAIL]  BE/BS 命名倒置
├── Q4_answer.md            [PASS]  IS/MB 抗体病毒
├── Q5_answer.md            [PASS]  FA/QS/CE (FA→MH)
├── Q6_answer.md            [PASS]  PK Timing PT4H
├── Q7_answer.md            [PASS]  部分日期 + SDTM/ADaM 分工
├── Q8_answer.md            [PASS]  CT Ext/NonExt + Define-XML
├── Q9_answer.md            [PASS]  Pinnacle 21 + cSDRG
└── Q10_answer.md           [PASS]  SUPP--家族
```

总计 14 个 answer.md (4 sanity + 10 smoke v3), 所有对话 URL 均记录在各 answer.md header.
