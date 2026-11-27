# 待改标签清单 (补检 + Q9 扩检查出; **未执行, 待主人裁定**)

<!-- chain: E (plans) -->
> 状态: **待主人裁定** (2026-11-27). 台账 `work/coverage_ledger.wc.jsonl` 未改 (md5 `60729f7b64b7c1dfaf2174e394f6dd9c`). 本文件由 `scripts/t4/t4_supp_report.py` 生成; 依据是独立审查者的原始结果 ("原始结果" 列), 主控未改判.
> 为什么不直接改: IE 须逐条清单经用户 ack 才生效 (PLAN §3.1 B5); PDF_TYPO 每条须用户 ack (G-TB1); 主人即将确认的 U-1 口径数字建立在当前台账上.

## 1. 要主人选的

| 组 | 条数 | 现标签 → 建议 | 选项 |
|---|--:|---|---|
| R1-row | 49 | EQUIVALENT → INTENTIONAL_EXCLUDE | A = 认 IE (与 T1.4 R1 对 70 条 v2.0 变量表行的裁定同类, 不动 KB) / B = 把 PDF 这些列补进 KB 的 model 表 (要解冻 KB, 另开批) / C = 其它 |
| R1-row | 2 | EXACT → INTENTIONAL_EXCLUDE | A = 认 IE (与 T1.4 R1 对 70 条 v2.0 变量表行的裁定同类, 不动 KB) / B = 把 PDF 这些列补进 KB 的 model 表 (要解冻 KB, 另开批) / C = 其它 |
| registered-typo | 4 | EXACT → PDF_TYPO | A = 改标 PDF_TYPO (与范围内同类一致; U-1 B 口径下仍算覆盖, strict 口径下不算) / B = 维持 EXACT (与 "逐字" 定义不符) |
| v2.0-TOC | 2 | EQUIVALENT → INTENTIONAL_EXCLUDE | A = 认 IE (同页 §7 / §8 两条目录条目已是 IE VERSION_MISMATCH) / B = 其它 |

## 2. 若三组都按建议改, 各闸数字 (在台账**副本**上算, 命令见 §4)

| 项 | 现在 (台账未改) | 改后 (预演) |
|---|---|---|
| G-TB3 strict | 9567/9986 = 95.8041% | 9510/9933 = 95.7415% |
| G-TB3 mapped | 9567/9629 = 99.3561% | 9510/9572 = 99.3523% |
| G-TB3 U-1 B 口径 | 9913/9986 = 99.2690% | 9860/9933 = 99.2651% |
| 内容指标 (EXACT+EQUIV) | 8733/9629 = 90.6948% | 8676/9572 = 90.6394% |
| G-TB1 / G-TB2 (范围内) | 174 residual_gap=0 G-TB1 pass=174/174 G-TB2 pass=157/174 | 174 residual_gap=0 G-TB1 pass=174/174 G-TB2 pass=157/174 |

- 99.02% 的闸线 (06 口径 99.0192%) 在 U-1 B 口径下改前改后都高于; strict 口径改前改后都低于 (与 attempt 2 相同的性质).
- 改标只动标签, 不动 KB. 真正执行时走 writer (`oh-my-claudecode:executor`) → reviewer, 并在同一次回写里一并处理 registry `B-IS T-6` 页号 p241 → p239 (见 `t4_owner_decisions_round2.md` 末节: 页号参与登记匹配, 单独改有改变台账的风险).

## 3. 逐条

| # | atom_id | 页 | 节 | 现标签 | 建议 | 组 | 理由 | 原始结果 |
|--:|---|--:|---|---|---|---|---|---|
| 1 | `sv20_p0046_a002` | 46 | §3.2.3.1 [Subject Elements] | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_3.md:26` |
| 2 | `sv20_p0047_a002` | 47 | §3.2.3.2 [Subject Repro Stages] | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_3.md:28` |
| 3 | `sv20_p0052_a012` | 52 | §5.1.1.2 Trial Arms | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_3.md:33` |
| 4 | `sv20_p0052_a013` | 52 | §5.1.1.2 Trial Arms | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_3.md:34` |
| 5 | `sv20_p0052_a014` | 52 | §5.1.1.2 Trial Arms | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_3.md:35` |
| 6 | `sv20_p0052_a016` | 52 | §5.1.1.2 Trial Arms | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_3.md:36` |
| 7 | `sv20_p0052_a017` | 52 | §5.1.1.2 Trial Arms | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_3.md:37` |
| 8 | `sv20_p0053_a004` | 53 | §5.1.1.2 Trial Arms | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_3.md:38` |
| 9 | `sv20_p0053_a011` | 53 | §5.1.2 Trial Sets | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_3.md:39` |
| 10 | `sv20_p0053_a012` | 53 | §5.1.2 Trial Sets | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_3.md:40` |
| 11 | `sv20_p0053_a014` | 53 | §5.1.2 Trial Sets | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_3.md:41` |
| 12 | `sv20_p0053_a015` | 53 | §5.1.2 Trial Sets | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_3.md:42` |
| 13 | `sv20_p0053_a016` | 53 | §5.1.2 Trial Sets | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_3.md:43` |
| 14 | `sv20_p0053_a018` | 53 | §5.1.2 Trial Sets | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_3.md:44` |
| 15 | `sv20_p0055_a005` | 55 | §5.1.3.2 Trial Repro Paths | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_4.md:20` |
| 16 | `sv20_p0055_a006` | 55 | §5.1.3.2 Trial Repro Paths | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_4.md:21` |
| 17 | `sv20_p0055_a007` | 55 | §5.1.3.2 Trial Repro Paths | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_4.md:22` |
| 18 | `sv20_p0055_a008` | 55 | §5.1.3.2 Trial Repro Paths | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_4.md:23` |
| 19 | `sv20_p0055_a009` | 55 | §5.1.3.2 Trial Repro Paths | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_4.md:24` |
| 20 | `sv20_p0055_a010` | 55 | §5.1.3.2 Trial Repro Paths | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_4.md:25` |
| 21 | `sv20_p0055_a011` | 55 | §5.1.3.2 Trial Repro Paths | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_4.md:26` |
| 22 | `sv20_p0055_a012` | 55 | §5.1.3.2 Trial Repro Paths | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_4.md:27` |
| 23 | `sv20_p0056_a012` | 56 | §5.1.4.1 Trial Visits | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_4.md:29` |
| 24 | `sv20_p0056_a013` | 56 | §5.1.4.1 Trial Visits | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_4.md:30` |
| 25 | `sv20_p0056_a015` | 56 | §5.1.4.1 Trial Visits | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_4.md:31` |
| 26 | `sv20_p0056_a016` | 56 | §5.1.4.1 Trial Visits | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_4.md:32` |
| 27 | `sv20_p0057_a005` | 57 | §5.1.4.2 Trial Disease Assessments | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_4.md:34` |
| 28 | `sv20_p0057_a008` | 57 | §5.1.4.2 Trial Disease Assessments | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_4.md:35` |
| 29 | `sv20_p0057_a009` | 57 | §5.1.4.2 Trial Disease Assessments | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_4.md:36` |
| 30 | `sv20_p0057_a010` | 57 | §5.1.4.2 Trial Disease Assessments | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_4.md:37` |
| 31 | `sv20_p0058_a005` | 58 | §5.1.4.3 Trial Disease Milestones | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_4.md:39` |
| 32 | `sv20_p0058_a006` | 58 | §5.1.4.3 Trial Disease Milestones | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_4.md:40` |
| 33 | `sv20_p0058_a007` | 58 | §5.1.4.3 Trial Disease Milestones | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_4.md:41` |
| 34 | `sv20_p0058_a015` | 58 | §5.1.5 Trial Inclusion/Exclusion Criteria | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_4.md:43` |
| 35 | `sv20_p0058_a017` | 58 | §5.1.5 Trial Inclusion/Exclusion Criteria | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_4.md:44` |
| 36 | `sv20_p0058_a018` | 58 | §5.1.5 Trial Inclusion/Exclusion Criteria | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_5.md:22` |
| 37 | `sv20_p0059_a001` | 59 | §5.1.5 Trial Inclusion/Exclusion Criteria | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_5.md:23` |
| 38 | `sv20_p0059_a002` | 59 | §5.1.5 Trial Inclusion/Exclusion Criteria | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_5.md:24` |
| 39 | `sv20_p0059_a010` | 59 | §5.1.6 Trial Summary Information | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_5.md:27` |
| 40 | `sv20_p0059_a011` | 59 | §5.1.6 Trial Summary Information | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_5.md:28` |
| 41 | `sv20_p0059_a012` | 59 | §5.1.6 Trial Summary Information | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_5.md:29` |
| 42 | `sv20_p0059_a014` | 59 | §5.1.6 Trial Summary Information | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_5.md:30` |
| 43 | `sv20_p0059_a015` | 59 | §5.1.6 Trial Summary Information | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_5.md:31` |
| 44 | `sv20_p0059_a016` | 59 | §5.1.6 Trial Summary Information | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_5.md:32` |
| 45 | `sv20_p0059_a017` | 59 | §5.1.6 Trial Summary Information | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_5.md:33` |
| 46 | `sv20_p0060_a001` | 60 | §5.1.6 Trial Summary Information | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_5.md:34` |
| 47 | `sv20_p0065_a003` | 65 | §6.1 [Related Records Dataset] | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_5.md:39` |
| 48 | `sv20_p0069_a001` | 69 | §6.6 [Associated Persons Relationships] | EXACT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_supp_raw/pack_2.md:50` |
| 49 | `sv20_p0069_a002` | 69 | §6.6 [Associated Persons Relationships] | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_5.md:43` |
| 50 | `sv20_p0069_a003` | 69 | §6.6 [Associated Persons Relationships] | EXACT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_supp_raw/pack_2.md:51` |
| 51 | `sv20_p0069_a004` | 69 | §6.6 [Associated Persons Relationships] | EQUIVALENT | INTENTIONAL_EXCLUDE | R1-row | SDTM v2.0 变量表行 / 表头: KB 精简列一致, PDF 其它列的内容 KB 本表未收 (T1.4 R1 类) | `evidence/t4_q9_raw/pack_5.md:44` |
| 52 | `ig34_p0147_a025` | 147 | §6.2.2 [Biospecimen Events (BE)] | EXACT | PDF_TYPO | registered-typo | KB 与 PDF 的差异 = 已登记 PDF 笔误 B-BE T-3 (KB 写正确值) | `evidence/t4_supp_raw/pack_1.md:35` |
| 53 | `ig34_p0262_a016` | 262 | §6.3.5.7 Microbiology Domains | EXACT | PDF_TYPO | registered-typo | KB 与 PDF 的差异 = 已登记 PDF 笔误 B-MB T-1 (KB 写正确值) | `evidence/t4_supp_raw/pack_2.md:42` |
| 54 | `ig34_p0262_a017` | 262 | §6.3.5.7 Microbiology Domains | EXACT | PDF_TYPO | registered-typo | KB 与 PDF 的差异 = 已登记 PDF 笔误 B-MB T-1 (KB 写正确值) | `evidence/t4_supp_raw/pack_2.md:43` |
| 55 | `ig34_p0296_a023` | 296 | §6.3.7.4 Nervous System Findings (NV) | EXACT | PDF_TYPO | registered-typo | KB 与 PDF 的差异 = 已登记 PDF 笔误 B-NV T-2 (KB 写正确值) | `evidence/t4_supp_raw/pack_2.md:47` |
| 56 | `sv20_p0003_a011` | 3 | §0 [TOC] | EQUIVALENT | INTENTIONAL_EXCLUDE | v2.0-TOC | SDTM v2.0 目录条目, 对应章节 KB 未收 (同页 a009 / a010 已是 IE VERSION_MISMATCH) | `evidence/t4_q9_raw/pack_2.md:33` |
| 57 | `sv20_p0003_a012` | 3 | §0 [TOC] | EQUIVALENT | INTENTIONAL_EXCLUDE | v2.0-TOC | SDTM v2.0 目录条目, 对应章节 KB 未收 (同页 a009 / a010 已是 IE VERSION_MISMATCH) | `evidence/t4_q9_raw/pack_2.md:34` |

## 4. 复跑

```bash
python3 -I .work/10_tier_b_repair/scripts/t4/t4_supp_report.py
# 预演台账副本: work/scratch/t4/relabel_preview/ledger_preview.jsonl (gitignored); 工作台账 md5 断言不变
```

