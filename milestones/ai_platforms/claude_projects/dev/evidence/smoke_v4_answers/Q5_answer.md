# Q5 — FA vs QS vs CE 三场景 (Claude Projects)

> **Chat**: fresh (`/chat/2252eb11-3fa3-4326-8140-07ce54686b92`)
> **采集时间**: 2026-04-22 晚
> **Verdict**: **PASS+** (三场景 full 表格 + FA Assumption 5/5a + QRS Shared Assumption + CE Assumption 1/1b + §8.6.1/§8.6.3 锚点 + 对比总表)

## 场景 A — DAS28 量化 (对既往 MH)
| 项 | 值 |
|---|---|
| 域 | **FA** (Findings About Events or Interventions) |
| Class | Findings About |
| Structure | One record per finding, per object, per time point, per visit per subject |

- 理由: 已有 Events 记录 (MH RA) 的量化 findings, 典型 Findings About (SDTMIG §6.4.1, §8.6.3)
- **FA Assumption 5**: 当 FA 与 events/interventions 关系建立时需 RELREC 或 --LNKID/--LNKGRP
- **FA Assumption 5a**: "FAOBJ alone is not sufficient to establish a relationship" → 不能只靠 FAOBJ, 需显式 RELREC
- Topic: FATESTCD="DAS28", FATEST="DAS-28 Score", FAOBJ="RHEUMATOID ARTHRITIS" (←MH.MHTERM), FACAT="DISEASE ACTIVITY", FAORRES/FASTRESN=4.2
- 关联: RELREC FA↔MH (IDVAR=FASEQ ↔ IDVAR=MHSEQ)
- 扩展: 拆 TJC28/SJC28 两条 FATESTCD 组件

## 场景 B — SF-36 问卷
| 项 | 值 |
|---|---|
| 域 | **QS** (Questionnaires) |
| Class | Findings |
| Structure | One record per questionnaire per question per time point per visit per subject |

- 理由: SF-36 是标准化 QRS instrument; QS 是 QRS 三域之一 (FT/QS/RS)
- **QRS Shared Assumption 1**: instrument 名称放 QSCAT, 每题一条记录
- **QRS Shared Assumption 4**: 若 CRF 列出视为收集, 否则视为派生 (QSDRVFL=Y), 每维度一条 QSTESTCD 记录 (e.g. SF36PF)
- CDISC CT 例: RAND 36-Item Health Survey **C113862**
- Topic: QSTESTCD="SF3601"/"SF3602"..., QSTEST="SF36-General Health" etc, QSCAT="SF36", QSSCAT="PHYSICAL FUNCTIONING"/"MENTAL HEALTH", QSORRES/QSSTRESN

## 场景 C — 轻微头晕 未达 AE 阈值
| 项 | 值 |
|---|---|
| 域 | **CE** (Clinical Events) |
| Class | Events |
| Structure | One record per clinical event per subject |

- 理由: CE Assumption 1: "events considered clinical events versus adverse events should be done carefully" — CE 是 "不满足 AE 报告条件" 的归宿
- **SDTMIG §8.6.1 (ch08)**: "MH and CE are the appropriate places to store most medical events that are not adverse events"
- 发生在研究期 (非既往 → 不是 MH) + 未达 AE 阈 → CE
- **CE Assumption 1b**: 若后续升级 serious, 同步填 CESER 等
- Topic: CETERM="Dizziness" (verbatim), CEDECOD="DIZZINESS", CEOCCUR="Y", CESEV="MILD", CESTDTC/CEENDTC ISO 8601

## 对比总表
| 场景 | 域 | Class | Topic | 关键判据 |
|---|---|---|---|---|
| A DAS28 评 MH | FA | Findings About | FATESTCD=DAS28, FAOBJ=RA | 对 Events 量化 → FA + RELREC |
| B SF-36 | QS | Findings | QSTESTCD=SF36xx, QSCAT=SF36 | 标准化问卷 → QRS.QS |
| C 轻微头晕 | CE | Events | CETERM=Dizziness | 研究期非 AE → CE (§8.6.1) |

## 源溯源 (Claude 自列)
- FA/spec.md + FA/assumptions.md (5, 5a)
- QS/spec.md + QRS Shared Assumptions (FT/QS 共享)
- CE/spec.md + CE/assumptions.md (1, 1b)
- sdtmig/ch08.md §8.6.1, §8.6.3

## Verdict
**PASS+** — 三场景 full 表 (项/值/Class/Structure) + Assumption 引用 (FA 5/5a + QRS 1/4 + CE 1/1b) + §8.6.1/§8.6.3 锚点 + RELREC + QSDRVFL=Y + CT C113862 + 对比总表. 最强答案之一, 远超题目要求.

**备注**: 75% 周 usage 警告仍在, 但答案完整, 未触 cap.
