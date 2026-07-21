# P3.4.5 抽样 Log

> **日期**: 2026-04-22
> **工具**: Python 3 `random` 分层抽样 (stratified), 每层独立 seed
> **输入**: `dev/evidence/req_vars_full_set.md` (176 Req 变量)
> **Bucket 映射**: `dev/evidence/source_mapping.md` (42 bucket)
> **手顺**: `dev/checkpoints/CHECKPOINT_P3.4.5_HANDOFF.md` Step 1
> **约束**: handoff §1.1 表
> **P3.4 已用变量 (禁重复)**: `STUDYID DOMAIN USUBJID AEDECOD AESEQ AETERM DDTEST DDTESTCD SSTEST SSTESTCD`

---

## 分层 Seed Log (可复现)

Base seed `20260422` (今日日期). 每层 `SEED + n` 递进:

| Layer | Stratum | Seed | 抽出 |
|-------|---------|------|------|
| 1 | Non-core findings 冷区 (bucket 15/18/19/20/21/22, 除 P3.4 已用 DD/SS) | 20260422 | BSSEQ, SRTESTCD, CPTEST |
| 2a | QS 类 (bucket 14 spec + 38/39 CT questionnaires, HC-3 trigger) | 20260423 | QSTEST |
| 2b | FA 类 (bucket 20 spec + 35 CT findings_about) | 20260423 | FATESTCD |
| 3 | IG ch04 权威类 (Timing/Demographics/Medical-History) | 20260424 | SESTDTC |
| 4 | Special-Purpose (DM/SE/SM/CO) | 20260425 | SEX |
| 5 | Relationships (RELREC/RELSPEC/RELSUB) | 20260426 | REFID |
| 6 | Trial Design edge (TS/TA/TI/TM) | 20260427 | TSPARM |
| 7 | Events 补多样 (MH/HO/CE/DS/DV/BE) | 20260428 | BETERM |
| 8 (丢弃) | 冗余 extra non-core (原 11 个, 删 1 保 10) | 20260429 | ~~FASEQ~~ (discarded, non-core 已 ≥3) |

---

## 最终 10 Req 变量清单

| # | 变量 | Domain | Core | Role | 预计 spec bucket | 预计 CT bucket | Stratum 标记 |
|---|------|--------|:----:|------|:----------------:|:--------------:|-------------|
| 1 | **BSSEQ** | BS (biospecimens) | Req | Identifier | 19 (fnd_morphology) | — | non-core findings_morphology |
| 2 | **SRTESTCD** | SR (skin response) | Req | Topic | 20 (fnd_about) | 35 (ct_findings) | non-core findings_about |
| 3 | **CPTEST** | CP (clinical endpoint) | Req | Synonym Qualifier | 19 (fnd_morphology) | 36 (ct_specialized_cp) | non-core findings_morphology |
| 4 | **QSTEST** | QS (questionnaires) | Req | Synonym Qualifier | 14 (fnd_questionnaire) | **38/39 (ct_questionnaires_part1-43)** | QS 类, **HC-3 trigger 潜在** |
| 5 | **FATESTCD** | FA (findings_about) | Req | Topic (C101832) | 20 (fnd_about) | 35 (ct_findings_fa) | FA 类 non-core |
| 6 | **SESTDTC** | SE (elements) | Req | Timing | 4 (sp_se_sm_sv_co) | 29 (ig_ch04 Timing 规则) | SP + IG ch04 |
| 7 | **SEX** | DM (demographics) | Req | Record Qualifier (C66731) | 3 (sp_demographics) | 37 (ct_misc_dm) | SP + IG ch04 demographics |
| 8 | **REFID** | RELSPEC (spec relationships) | Req | Identifier | 26 (rel_relrec_relspec_relsub) | — | Relationships |
| 9 | **TSPARM** | TS (trial summary) | Req | Synonym Qualifier (C67152) | 25 (td_meta_ti_ts_oi) | 37 (ct_misc_td) | TD edge non-core |
| 10 | **BETERM** | BE (biospecimen events) | Req | Topic | 10 (ev_history_mh_ho_be) | — | Events non-core |

---

## 约束达成校验

| 约束 (handoff §1.1) | 目标 | 实际 | 状态 |
|---------------------|:----:|:----:|:----:|
| Non-core 冷区 (findings_other/device/morphology/about) | ≥3 | 5 (BSSEQ, SRTESTCD, CPTEST, FATESTCD, BETERM) | ✅ |
| QS/FA 类 (大 bucket 38/39 citation 潜在触发) | ≥2 | 2 (QSTEST QS 类直接命中 38/39, FATESTCD FA 类命中 35) | ✅ |
| IG ch04 权威章 | ≥1 | 2 (SESTDTC Timing, SEX Demographics) | ✅ |
| Special-Purpose (DM/SE/SM/CO) | ≥1 | 2 (SESTDTC SE, SEX DM) | ✅ |
| 无 P3.4 重复 | 0 | 0 ✅ | ✅ |

**多命中说明**: SESTDTC 同时命中 IG ch04 + SP 两层; SEX 同时命中 IG ch04 + SP. 不重复计入, 多层命中只算一次 +1. 约束全部超额达成.

---

## HC-3 Bucket 38/39 多区域采样触发预判

- **QSTEST (Q4)** 预计 citation 落 bucket 38 或 39 (QS question long names 在 questionnaires CT part1-43)
- **HC-3 触发**: ≥1 题 citation 命中 bucket 38/39 → 主 10 题问完后, 主 session 加 **2 补验证题**:
  - **补题 A**: bucket 38 头段 (questionnaires_part1-5 范围, 如 **AJCC** 分期 / **CDR** / **CES-D** 类问卷) 的一个具体 code
  - **补题 B**: bucket 38 尾段 (questionnaires_part18-22 范围, 如 **QLQ-C30** / **SF-36** / **Karnofsky** 类问卷) 的一个具体 code
- 两题都 PASS → evidence 可写 "bucket 38 多区域验证 PASS"
- 仅单区域 PASS → evidence 写 "bucket 38 单区域 PASS, 不外推全 bucket"
- 补题不计入 10/10 主评分

---

## 主 session 审核

- [x] 抽样过程 cowork 未预览抽样结果 (本次主 session 独立执行 Python, 不派 subagent)
- [x] seed 记录落盘 (可复现)
- [x] 约束 handoff §1.1 全部达成
- [x] 无 P3.4 smoke 重复
- [x] 10 变量清单锁定, 进 Step 2 题目设计

**主 session 签字**: 抽样完成 2026-04-22, 进 Step 2.

---

*本 log 执行: 主 session. seed 复现命令见本文件 Seed Log 段, Python 3 `random.seed(<seed>)` + `random.sample()`.*
