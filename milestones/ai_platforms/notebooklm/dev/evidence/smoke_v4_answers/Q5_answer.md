# Q5 — FA vs QS vs CE 三场景 (NotebookLM)

> **Chat**: fresh session (post Delete chat history)
> **采集时间**: 2026-04-22 晚
> **Verdict**: **PASS** (A=FA, B=QS, C=CE + Topic 变量 + citations)

## A — DAS28 量化评分 对既往 MH
- 域: **FA** (Findings About Events or Interventions)
- 理由: 不是事件本身而是对既往 MH 的测量/评估 (Findings about events); 不放 MH, 通过 FAOBJ 指向 MH 症状 + RELREC 关联父记录
- Topic: FATESTCD="DAS28", FATEST="Disease Activity Score 28", FAOBJ="RHEUMATOID ARTHRITIS", FAORRES=4.2
- 源: [20_fnd_about_fa_sr.md], [30_ig_ch08_ch10.md]

## B — SF-36 生活质量问卷
- 域: **QS** (Questionnaires)
- 理由: SF-36 是标准的 QRS 类问卷工具, 必须用 CDISC 发布的问卷 CT
- Topic: QSTESTCD="SF36101" (Codelist C177716), QSTEST="SF361-In General You Say Your Health Is"
- 源: [14_fnd_questionnaire_qs_ie.md], [33_ct_general.md]

## C — 轻微头晕未达 AE 阈值
- 域: **CE** (Clinical Events)
- 理由: 自然发生但未达 untoward medical occurrence, CE 专记非 AE signs/symptoms
- Topic: CETERM="DIZZINESS"
- 源: [09_ev_disposition_ds_dv_ce.md], [33_ct_general.md]

## Verdict
**PASS** — 3/3 场景正确 + 理由 + Topic 变量 + 18 条 inline citations. SF-36 给到具体 Codelist C177716 + QSTESTCD SF36101 是加分细节 (超 smoke v3 Q5 同题).
