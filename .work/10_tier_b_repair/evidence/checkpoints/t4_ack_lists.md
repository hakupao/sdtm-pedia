# T4 用户确认清单: ATOM_ERR / PDF_TYPO / FIGURE_DEFERRED

<!-- chain: E (plans) -->
> 状态: **委托代裁整类确认 (U-5=B, C7 38 全检成立), 见 t4_user_decisions.md §000; 非主人逐条确认** (2026-11-27 T4 解冻轮 W3 重生成). U-5 裁定时 (ledger @3a24a1c) 为 ATOM_ERR 197 / PDF_TYPO 122 / FIG 11; 之后进入这三类的原子按 "决定来源" 列标注 (U-2 / U-8 / U-7 委托代裁, 见 t4_user_decisions.md §000), 不归入 U-5; 明细见 `evidence/checkpoints/t4_thaw_W3.md`. 生成: `python3 -I .work/10_tier_b_repair/scripts/t4/t4_ack_lists.py`.
> 单位 = PDF 原子 (不是登记行; 一条登记行可覆盖多个原子, 一个原子也可挂多条登记). 数据源: 最终 ledger `work/coverage_ledger.wc.jsonl` + `work/t3_writeback_decisions.json` + `work/t3_errata.json`.
> G-TB1 要求这三类 "每条有登记 + 用户 ack". 这三类在 G-TB3 mapped 口径中从分母去掉, 在 strict 口径中算未覆盖.

## 汇总

| 终态 | 原子数 | 按判定规则 | 决定来源 | 用户确认 |
|---|--:|---|---|---|
| ATOM_ERR | 197 | S1-R1 157, C7-atom-not-in-PDF 38, C7-K4-rereview 2 | U-5 196, U-2 委托代裁 1 | ☐ 整类确认　☐ 有异议 (在下表备注) |
| PDF_TYPO | 149 | K3b-registry 61, S1-R2 53, writer-Tn-registry 35 | U-5 122, U-7 委托代裁 22, U-8 委托代裁 4, 主控决定 M-4 1 | ☐ 整类确认　☐ 有异议 (在下表备注) |
| FIGURE_DEFERRED | 11 | FIGURE 11 | U-5 11 | ☐ 整类确认　☐ 有异议 (在下表备注) |

规则含义: `S1-R1` = 原子 verbatim 与 PDF 不符 (原子抽错, KB 按 PDF); `S1-R2` = PDF 自身笔误且已登记; `C7-atom-not-in-PDF` = 原子文本在 PDF 页中不存在; `K3b-registry` / `writer-Tn-registry` = 由 PDF 笔误登记 (T-n) 触及; `FIGURE` = 图, 暂缓.

## ATOM_ERR (197)

| # | atom_id | 页 | 节 | 规则 | 依据 / 登记 | 出处 | 决定来源 | 异议 |
|--:|---|--:|---|---|---|---|---|---|
| 1 | `ig34_p0009_a024` | 9 | §1.4.1 [How to Read a Domain Specification] | S1-R1 | B-ch01 review: 原子缺逗号 | `evidence/checkpoints/t2_B-ch01_review.md:22` | U-5 (整类, 委托代裁) | |
| 2 | `ig34_p0018_a046` | 18 | §3.2.1 Dataset-level Metadata | S1-R1 | B-ch03 writer: 原子漏 'specimen'; KB 正确 | `evidence/checkpoints/t2_B-ch03_audit.md:33` | U-5 (整类, 委托代裁) | |
| 3 | `ig34_p0056_a001` | 56 | §4.5.3.2 [Text Strings Greater than 200 Characters | S1-R1 | T1 triage ATOM_ERR (writer, reviewed=True) | `work/triage_merged.json:16375 (lane D pack_028; T1.3 reviewer 100%)` | U-5 (整类, 委托代裁) | |
| 4 | `ig34_p0056_a006` | 56 | §4.5.3.2 [Text Strings Greater than 200 Characters | S1-R1 | T4 U-2 A (委托代裁): 原子第 2/3 格漏 'to improve readability' 与句点; PDF p56:37-40 与 KB ch04:1478 一致 | `evidence/checkpoints/t4_user_decisions.md:33` | U-2 委托代裁 (§000), 非 U-5 | |
| 5 | `ig34_p0057_a002` | 57 | §4.5.4 [Evaluators in the Interventions and Events | S1-R1 | T1 triage ATOM_ERR (writer, reviewed=True) | `work/triage_merged.json:16428 (lane D pack_028; T1.3 reviewer 100%)` | U-5 (整类, 委托代裁) | |
| 6 | `ig34_p0063_a017` | 63 | §5.2 [Demographics (DM)] | S1-R1 | T1 triage ATOM_ERR (writer, reviewed=True) | `work/triage_merged.json:1368 (lane A pack_004; T1.3 reviewer 100%)` | U-5 (整类, 委托代裁) | |
| 7 | `ig34_p0067_a014` | 67 | §5.2 [Demographics (DM)] | S1-R1 | T1 triage ATOM_ERR (writer, reviewed=True) | `work/triage_merged.json:1746 (lane A pack_004; T1.3 reviewer 100%)` | U-5 (整类, 委托代裁) | |
| 8 | `ig34_p0068_a017` | 68 | §5.2 [DM – Examples] | S1-R1 | T1 triage ATOM_ERR (writer, reviewed=True) | `work/triage_merged.json:1759 (lane A pack_004; T1.3 reviewer 100%)` | U-5 (整类, 委托代裁) | |
| 9 | `ig34_p0069_a013` | 69 | §5.2 [DM – Examples] | S1-R1 | T1 triage ATOM_ERR (writer, reviewed=True) | `work/triage_merged.json:1798 (lane A pack_004; T1.3 reviewer 100%)` | U-5 (整类, 委托代裁) | |
| 10 | `ig34_p0069_a023` | 69 | §5.2 [DM – Examples] | S1-R1 | T1 triage ATOM_ERR (writer, reviewed=True) | `work/triage_merged.json:1811 (lane A pack_004; T1.3 reviewer 100%)` | U-5 (整类, 委托代裁) | |
| 11 | `ig34_p0069_a024` | 69 | §5.2 [DM – Examples] | S1-R1 | T1 triage ATOM_ERR (writer, reviewed=True) | `work/triage_merged.json:1824 (lane A pack_004; T1.3 reviewer 100%)` | U-5 (整类, 委托代裁) | |
| 12 | `ig34_p0069_a025` | 69 | §5.2 [DM – Examples] | S1-R1 | T1 triage ATOM_ERR (writer, reviewed=True) | `work/triage_merged.json:1837 (lane A pack_004; T1.3 reviewer 100%)` | U-5 (整类, 委托代裁) | |
| 13 | `ig34_p0069_a027` | 69 | §5.2 [DM – Examples] | S1-R1 | T1 triage ATOM_ERR (writer, reviewed=True) | `work/triage_merged.json:1850 (lane A pack_004; T1.3 reviewer 100%)` | U-5 (整类, 委托代裁) | |
| 14 | `ig34_p0069_a029` | 69 | §5.2 [DM – Examples] | S1-R1 | T1 triage ATOM_ERR (writer, reviewed=True) | `work/triage_merged.json:1863 (lane A pack_004; T1.3 reviewer 100%)` | U-5 (整类, 委托代裁) | |
| 15 | `ig34_p0069_a030` | 69 | §5.2 [DM – Examples] | S1-R1 | T1 triage ATOM_ERR (writer, reviewed=True) | `work/triage_merged.json:1876 (lane A pack_004; T1.3 reviewer 100%)` | U-5 (整类, 委托代裁) | |
| 16 | `ig34_p0069_a031` | 69 | §5.2 [DM – Examples] | S1-R1 | T1 triage ATOM_ERR (writer, reviewed=True) | `work/triage_merged.json:1889 (lane A pack_004; T1.3 reviewer 100%)` | U-5 (整类, 委托代裁) | |
| 17 | `ig34_p0069_a032` | 69 | §5.2 [DM – Examples] | S1-R1 | T1 triage ATOM_ERR (writer, reviewed=True) | `work/triage_merged.json:1902 (lane A pack_004; T1.3 reviewer 100%)` | U-5 (整类, 委托代裁) | |
| 18 | `ig34_p0070_a022` | 70 | §5.2 [DM – Examples] | S1-R1 | T1 triage ATOM_ERR (writer, reviewed=True) | `work/triage_merged.json:1967 (lane A pack_004; T1.3 reviewer 100%)` | U-5 (整类, 委托代裁) | |
| 19 | `ig34_p0077_a015` | 77 | §5.2 [Demographics (DM)] | S1-R1 | T1 triage ATOM_ERR (writer, reviewed=True) | `work/triage_merged.json:2071 (lane A pack_004; T1.3 reviewer 100%)` | U-5 (整类, 委托代裁) | |
| 20 | `ig34_p0078_a007` | 78 | §5.2 [Demographics (DM)] | S1-R1 | T1 triage ATOM_ERR (writer, reviewed=True) | `work/triage_merged.json:2084 (lane A pack_004; T1.3 reviewer 100%)` | U-5 (整类, 委托代裁) | |
| 21 | `ig34_p0078_a021` | 78 | §5.2 [Demographics (DM)] | S1-R1 | T1 triage ATOM_ERR (writer, reviewed=True) | `work/triage_merged.json:2097 (lane A pack_004; T1.3 reviewer 100%)` | U-5 (整类, 委托代裁) | |
| 22 | `ig34_p0079_a004` | 79 | §5.3 [Subject Elements] | S1-R1 | S-SPREL SE asm 按 p79 渲染改词 (epochs and elements); 原子抄自旧错 KB \| errata: t3_atom_err \| new_t | `work/t3_fp_expected_regressions.jsonl:2` | U-5 (整类, 委托代裁) | |
| 23 | `ig34_p0079_a006` | 79 | §5.3 [Subject Elements] | S1-R1 | S-SPREL SE asm 按 p79 渲染改词 (definitions (TESTRL values)); 原子抄自旧错 KB \| errata: t3_atom_err  | `work/t3_fp_expected_regressions.jsonl:3` | U-5 (整类, 委托代裁) | |
| 24 | `ig34_p0079_a009` | 79 | §5.3 [Subject Elements] | S1-R1 | S-SPREL SE asm 按 p79 渲染 (--DTC); 原子抄自旧错 KB \| errata: t3_atom_err \| new_target: domains/S | `work/t3_fp_expected_regressions.jsonl:4` | U-5 (整类, 委托代裁) | |
| 25 | `ig34_p0079_a010` | 79 | §5.3 [Subject Elements] | S1-R1 | S-SPREL SE asm 按 p79 渲染 (Such variables relate / --DY); 原子抄自旧错 KB \| errata: t3_atom_err \ | `work/t3_fp_expected_regressions.jsonl:5` | U-5 (整类, 委托代裁) | |
| 26 | `ig34_p0080_a002` | 80 | §5.3 [Subject Elements] | S1-R1 | T1 triage ATOM_ERR (writer, reviewed=True) | `work/triage_merged.json:19045 (lane D pack_033; T1.3 reviewer 100%)` | U-5 (整类, 委托代裁) | |
| 27 | `ig34_p0086_a011` | 86 | §5.5 [Subject Visits (SV)] | S1-R1 | B-SM audit: verbatim 错, 以渲染图为准 (SV Description) | `evidence/checkpoints/t2_B-SM_audit.md:26` | U-5 (整类, 委托代裁) | |
| 28 | `ig34_p0101_a011` | 101 | §6.1.2 [Concomitant/Prior Medications (CM)] | S1-R1 | T1 triage ATOM_ERR (writer, reviewed=True) | `work/triage_merged.json:9352 (lane B pack_017; T1.3 reviewer 100%)` | U-5 (整类, 委托代裁) | |
| 29 | `ig34_p0112_a009` | 112 | §6.1.3.3 [Exposure/Exposure as Collected Examples] | S1-R1 | T1 triage ATOM_ERR (writer, reviewed=True) | `work/triage_merged.json:6978 (lane B pack_013; T1.3 reviewer 100%)` | U-5 (整类, 委托代裁) | |
| 30 | `ig34_p0116_a009` | 116 | §6.1.3.3 [Exposure/Exposure as Collected Examples] | S1-R1 | T1 triage ATOM_ERR (writer, reviewed=True) | `work/triage_merged.json:7004 (lane B pack_013; T1.3 reviewer 100%)` | U-5 (整类, 委托代裁) | |
| 31 | `ig34_p0116_a010` | 116 | §6.1.3.3 [Exposure/Exposure as Collected Examples] | S1-R1 | T1 triage ATOM_ERR (writer, reviewed=True) | `work/triage_merged.json:7017 (lane B pack_013; T1.3 reviewer 100%)` | U-5 (整类, 委托代裁) | |
| 32 | `ig34_p0116_a012` | 116 | §6.1.3.3 [Exposure/Exposure as Collected Examples] | S1-R1 | T1 triage ATOM_ERR (writer, reviewed=True) | `work/triage_merged.json:7043 (lane B pack_013; T1.3 reviewer 100%)` | U-5 (整类, 委托代裁) | |
| 33 | `ig34_p0116_a014` | 116 | §6.1.3.3 [Exposure/Exposure as Collected Examples] | S1-R1 | T1 triage ATOM_ERR (writer, reviewed=True) | `work/triage_merged.json:7069 (lane B pack_013; T1.3 reviewer 100%)` | U-5 (整类, 委托代裁) | |
| 34 | `ig34_p0116_a016` | 116 | §6.1.3.3 [Exposure/Exposure as Collected Examples] | S1-R1 | T1 triage ATOM_ERR (writer, reviewed=True) | `work/triage_merged.json:7095 (lane B pack_013; T1.3 reviewer 100%)` | U-5 (整类, 委托代裁) | |
| 35 | `ig34_p0116_a018` | 116 | §6.1.3.3 [Exposure/Exposure as Collected Examples] | S1-R1 | T1 triage ATOM_ERR (writer, reviewed=True) | `work/triage_merged.json:7121 (lane B pack_013; T1.3 reviewer 100%)` | U-5 (整类, 委托代裁) | |
| 36 | `ig34_p0116_a020` | 116 | §6.1.3.3 [Exposure/Exposure as Collected Examples] | S1-R1 | T1 triage ATOM_ERR (writer, reviewed=True) | `work/triage_merged.json:7147 (lane B pack_013; T1.3 reviewer 100%)` | U-5 (整类, 委托代裁) | |
| 37 | `ig34_p0117_a001` | 117 | §6.1.3.3 [Exposure/Exposure as Collected Examples] | S1-R1 | T1 triage ATOM_ERR (writer, reviewed=True) | `work/triage_merged.json:7173 (lane B pack_013; T1.3 reviewer 100%)` | U-5 (整类, 委托代裁) | |
| 38 | `ig34_p0120_a003` | 120 | §6.1.3.3 [Exposure/Exposure as Collected Examples] | S1-R1 | T1 triage ATOM_ERR (writer, reviewed=True) | `work/triage_merged.json:7407 (lane B pack_013; T1.3 reviewer 100%)` | U-5 (整类, 委托代裁) | |
| 39 | `ig34_p0121_a011` | 121 | §6.1.4 [Meal Data (ML)] | S1-R1 | B-ML writer: 原子 MLGRID 抽错, PDF/KB 均 MLGRPID (O4 ML 部分关闭) | `evidence/checkpoints/t2_B-ML.md:22` | U-5 (整类, 委托代裁) | |
| 40 | `ig34_p0122_a010` | 122 | §6.1.4 [Meal Data (ML)] | S1-R1 | T1 triage ATOM_ERR (writer, reviewed=True) | `work/triage_merged.json:17553 (lane D pack_030; T1.3 reviewer 100%)` | U-5 (整类, 委托代裁) | |
| 41 | `ig34_p0122_a011` | 122 | §6.1.4 [Meal Data (ML)] | S1-R1 | T1 triage ATOM_ERR (writer, reviewed=True) | `work/triage_merged.json:17566 (lane D pack_030; T1.3 reviewer 100%)` | U-5 (整类, 委托代裁) | |
| 42 | `ig34_p0122_a015` | 122 | §6.1.4 [Meal Data (ML)] | S1-R1 | B-ML review: 原子 verbatim 写成 NCIBI; KB 与 PDF 一致 | `evidence/checkpoints/t2_B-ML_review.md:70` | U-5 (整类, 委托代裁) | |
| 43 | `ig34_p0122_a017` | 122 | §6.1.4 [Meal Data (ML)] | S1-R1 | B-ML review: 原子 verbatim 多 'not'; KB 与 PDF 一致 | `evidence/checkpoints/t2_B-ML_review.md:70` | U-5 (整类, 委托代裁) | |
| 44 | `ig34_p0123_a012` | 123 | §6.1.4 [Meal Data (ML)] | S1-R1 | B-ML review: 原子 verbatim 写成 'row.'; KB 与 PDF 一致 | `evidence/checkpoints/t2_B-ML_review.md:70` | U-5 (整类, 委托代裁) | |
| 45 | `ig34_p0124_a001` | 124 | §6.1.4 [Meal Data (ML)] | S1-R1 | B-ML review: 原子 verbatim MIDSDTC 截断; KB 与 PDF 一致 | `evidence/checkpoints/t2_B-ML_review.md:70` | U-5 (整类, 委托代裁) | |
| 46 | `ig34_p0133_a003` | 133 | §6.1.6 [Substance Use (SU)] | S1-R1 | B-SU review: 原子 verbatim 串列 (多 '2006-01-01'); KB 按渲染图正确 | `evidence/checkpoints/t2_B-SU_review.md:28` | U-5 (整类, 委托代裁) | |
| 47 | `ig34_p0149_a006` | 149 | §6.2.3 [Clinical Events (CE)] | S1-R1 | B-CE writer: 原子 CEBODYSYS 抽错, PDF/KB 均 CEBODSYS (O4 关闭) | `evidence/checkpoints/t2_B-CE.md:59` | U-5 (整类, 委托代裁) | |
| 48 | `ig34_p0149_a009` | 149 | §6.2.3 [Clinical Events (CE)] | S1-R1 | T1 triage ATOM_ERR (writer, reviewed=True) | `work/triage_merged.json:5236 (lane B pack_010; T1.3 reviewer 100%)` | U-5 (整类, 委托代裁) | |
| 49 | `ig34_p0149_a013` | 149 | §6.2.3 [Clinical Events (CE)] | S1-R1 | T1 triage ATOM_ERR (writer, reviewed=True) | `work/triage_merged.json:5249 (lane B pack_010; T1.3 reviewer 100%)` | U-5 (整类, 委托代裁) | |
| 50 | `ig34_p0149_a016` | 149 | §6.2.3 [Clinical Events (CE)] | S1-R1 | T1 triage ATOM_ERR (writer, reviewed=True) | `work/triage_merged.json:5262 (lane B pack_010; T1.3 reviewer 100%)` | U-5 (整类, 委托代裁) | |
| 51 | `ig34_p0149_a019` | 149 | §6.2.3 [Clinical Events (CE)] | S1-R1 | T1 triage ATOM_ERR (writer, reviewed=True) | `work/triage_merged.json:5275 (lane B pack_010; T1.3 reviewer 100%)` | U-5 (整类, 委托代裁) | |
| 52 | `ig34_p0150_a001` | 150 | §6.2.3 [Clinical Events (CE)] | S1-R1 | T1 triage ATOM_ERR (writer, reviewed=True) | `work/triage_merged.json:5288 (lane B pack_010; T1.3 reviewer 100%)` | U-5 (整类, 委托代裁) | |
| 53 | `ig34_p0150_a002` | 150 | §6.2.3 [Clinical Events (CE)] | S1-R1 | T1 triage ATOM_ERR (writer, reviewed=True) | `work/triage_merged.json:5301 (lane B pack_010; T1.3 reviewer 100%)` | U-5 (整类, 委托代裁) | |
| 54 | `ig34_p0150_a003` | 150 | §6.2.3 [Clinical Events (CE)] | S1-R1 | T1 triage ATOM_ERR (writer, reviewed=True) | `work/triage_merged.json:5314 (lane B pack_010; T1.3 reviewer 100%)` | U-5 (整类, 委托代裁) | |
| 55 | `ig34_p0150_a007` | 150 | §6.2.3 [Clinical Events (CE)] | S1-R1 | B-CE writer: 原子抽错, KB 按渲染图正确 | `evidence/checkpoints/t2_B-CE.md:63` | U-5 (整类, 委托代裁) | |
| 56 | `ig34_p0150_a008` | 150 | §6.2.3 [Clinical Events (CE)] | S1-R1 | B-CE writer: 原子抽错, KB 按渲染图正确 | `evidence/checkpoints/t2_B-CE_audit.md:19` | U-5 (整类, 委托代裁) | |
| 57 | `ig34_p0150_a009` | 150 | §6.2.3 [Clinical Events (CE)] | S1-R1 | B-CE writer: 原子抽错, KB 按渲染图正确 | `evidence/checkpoints/t2_B-CE.md:63 (页级行; 该批以范围/页号记这组原子)` | U-5 (整类, 委托代裁) | |
| 58 | `ig34_p0150_a012` | 150 | §6.2.3 [Clinical Events (CE)] | S1-R1 | B-CE writer: 原子抽错, KB 按渲染图正确 | `evidence/checkpoints/t2_B-CE.md:63 (页级行; 该批以范围/页号记这组原子)` | U-5 (整类, 委托代裁) | |
| 59 | `ig34_p0153_a0034` | 153 | §6.2.3 [Clinical Events] | S1-R1 | T2 global fp audit R1: 原子 USUBJID 无空格, 与 PDF 文本层 `ABC -US-701-002` 不符; KB = PDF (B-CE T-2  | `evidence/t2_fp_expected_regressions.md:62` | U-5 (整类, 委托代裁) | |
| 60 | `ig34_p0154_a0002` | 154 | §6.2.3 [Clinical Events] | S1-R1 | T2 global fp audit R1: 原子 USUBJID 无空格, 与 PDF 文本层 `ABC -US-701-002` 不符; KB = PDF (B-CE T-2  | `evidence/t2_fp_expected_regressions.md:63` | U-5 (整类, 委托代裁) | |
| 61 | `ig34_p0154_a0013` | 154 | §6.2.3 [Clinical Events] | S1-R1 | T2 global fp audit R1: 原子 USUBJID 无空格, 与 PDF 文本层 `ABC -US-701-002` 不符; KB = PDF (B-CE T-2  | `evidence/t2_fp_expected_regressions.md:64` | U-5 (整类, 委托代裁) | |
| 62 | `ig34_p0154_a0014` | 154 | §6.2.3 [Clinical Events] | S1-R1 | T2 global fp audit R1: 原子 USUBJID 无空格, 与 PDF 文本层 `ABC -US-701-002` 不符; KB = PDF (B-CE T-2  | `evidence/t2_fp_expected_regressions.md:65` | U-5 (整类, 委托代裁) | |
| 63 | `ig34_p0154_a0015` | 154 | §6.2.3 [Clinical Events] | S1-R1 | T2 global fp audit R1: 原子 USUBJID 无空格, 与 PDF 文本层 `ABC -US-701-002` 不符; KB = PDF (B-CE T-2  | `evidence/t2_fp_expected_regressions.md:66` | U-5 (整类, 委托代裁) | |
| 64 | `ig34_p0154_a0029` | 154 | §6.2.3 [Clinical Events] | S1-R1 | T2 global fp audit R1: 原子 USUBJID 无空格, 与 PDF 文本层 `ABC -US-701-002` 不符; KB = PDF (B-CE T-2  | `evidence/t2_fp_expected_regressions.md:67` | U-5 (整类, 委托代裁) | |
| 65 | `ig34_p0154_a0030` | 154 | §6.2.3 [Clinical Events] | S1-R1 | T2 global fp audit R1: 原子 USUBJID 无空格, 与 PDF 文本层 `ABC -US-701-002` 不符; KB = PDF (B-CE T-2  | `evidence/t2_fp_expected_regressions.md:68` | U-5 (整类, 委托代裁) | |
| 66 | `ig34_p0155_a0002` | 155 | §6.2.3 [Clinical Events] | S1-R1 | T2 global fp audit R1: 原子 USUBJID 无空格, 与 PDF 文本层 `ABC -US-701-002` 不符; KB = PDF (B-CE T-2  | `evidence/t2_fp_expected_regressions.md:69` | U-5 (整类, 委托代裁) | |
| 67 | `ig34_p0161_a0012` | 161 | §6.2.4 Disposition (DS) | S1-R1 | B-DS audit: verbatim DSCAT 应为 DSSCAT (渲染页) | `evidence/checkpoints/t2_B-DS.md:137` | U-5 (整类, 委托代裁) | |
| 68 | `ig34_p0167_a0010` | 167 | §6.2.4 Disposition (DS) | S1-R1 | B-DS writer: 表头 DSEQ 应为 DSSEQ | `evidence/checkpoints/t2_B-DS.md:138` | U-5 (整类, 委托代裁) | |
| 69 | `ig34_p0168_a0002` | 168 | §6.2.5 Healthcare Encounters (HO) | S1-R1 | T1 triage ATOM_ERR (writer, reviewed=True) | `work/triage_merged.json:3816 (lane A pack_007; T1.3 reviewer 100%)` | U-5 (整类, 委托代裁) | |
| 70 | `ig34_p0168_a0003` | 168 | §6.2.5 Healthcare Encounters (HO) | S1-R1 | T1 triage ATOM_ERR (writer, reviewed=True) | `work/triage_merged.json:3829 (lane A pack_007; T1.3 reviewer 100%)` | U-5 (整类, 委托代裁) | |
| 71 | `ig34_p0168_a0004` | 168 | §6.2.5 Healthcare Encounters (HO) | S1-R1 | T1 triage ATOM_ERR (writer, reviewed=True) | `work/triage_merged.json:3842 (lane A pack_007; T1.3 reviewer 100%)` | U-5 (整类, 委托代裁) | |
| 72 | `ig34_p0168_a0005` | 168 | §6.2.5 Healthcare Encounters (HO) | S1-R1 | T1 triage ATOM_ERR (writer, reviewed=True) | `work/triage_merged.json:3855 (lane A pack_007; T1.3 reviewer 100%)` | U-5 (整类, 委托代裁) | |
| 73 | `ig34_p0168_a0007` | 168 | §6.2.5 Healthcare Encounters (HO) | S1-R1 | T1 triage ATOM_ERR (writer, reviewed=True) | `work/triage_merged.json:3868 (lane A pack_007; T1.3 reviewer 100%)` | U-5 (整类, 委托代裁) | |
| 74 | `ig34_p0169_a0011` | 169 | §6.2.5 Healthcare Encounters (HO) | S1-R1 | B-HO audit: 原子 '--BODYS' 抽错, PDF/KB 均 --BODSYS | `evidence/checkpoints/t2_B-HO_audit.md:12` | U-5 (整类, 委托代裁) | |
| 75 | `ig34_p0169_a0021` | 169 | §6.2.5 Healthcare Encounters (HO) | S1-R1 | T1 triage ATOM_ERR (writer, reviewed=True) | `work/triage_merged.json:3881 (lane A pack_007; T1.3 reviewer 100%)` | U-5 (整类, 委托代裁) | |
| 76 | `ig34_p0169_a0022` | 169 | §6.2.5 Healthcare Encounters (HO) | S1-R1 | T1 triage ATOM_ERR (writer, reviewed=True) | `work/triage_merged.json:3894 (lane A pack_007; T1.3 reviewer 100%)` | U-5 (整类, 委托代裁) | |
| 77 | `ig34_p0169_a0023` | 169 | §6.2.5 Healthcare Encounters (HO) | S1-R1 | T1 triage ATOM_ERR (writer, reviewed=True) | `work/triage_merged.json:3907 (lane A pack_007; T1.3 reviewer 100%)` | U-5 (整类, 委托代裁) | |
| 78 | `ig34_p0169_a0025` | 169 | §6.2.5 Healthcare Encounters (HO) | S1-R1 | T1 triage ATOM_ERR (writer, reviewed=True) | `work/triage_merged.json:3933 (lane A pack_007; T1.3 reviewer 100%)` | U-5 (整类, 委托代裁) | |
| 79 | `ig34_p0169_a0029` | 169 | §6.2.5 Healthcare Encounters (HO) | S1-R1 | T1 triage ATOM_ERR (writer, reviewed=True) | `work/triage_merged.json:3946 (lane A pack_007; T1.3 reviewer 100%)` | U-5 (整类, 委托代裁) | |
| 80 | `ig34_p0170_a0004` | 170 | §6.2.5 Healthcare Encounters (HO) | S1-R1 | T1 triage ATOM_ERR (writer, reviewed=True) | `work/triage_merged.json:3998 (lane A pack_007; T1.3 reviewer 100%)` | U-5 (整类, 委托代裁) | |
| 81 | `ig34_p0170_a0006` | 170 | §6.2.5 Healthcare Encounters (HO) | S1-R1 | T1 triage ATOM_ERR (writer, reviewed=True) | `work/triage_merged.json:4011 (lane A pack_007; T1.3 reviewer 100%)` | U-5 (整类, 委托代裁) | |
| 82 | `ig34_p0179_a0018` | 179 | §6.2.7 Protocol Deviations (DV) | S1-R1 | B-DV review E-1: 原子抽取丢 DVTERM 句点; KB 照 PDF 渲染带句点 (T-1 照录+T4) | `evidence/checkpoints/t2_B-DV_review.md:17` | U-5 (整类, 委托代裁) | |
| 83 | `ig34_p0190_a011` | 190 | §6.3.3 ECG Test Results (EG) | S1-R1 | B-EG review: verbatim P0W 应为 PQW, VISIT 漏折行 1 | `evidence/checkpoints/t2_B-EG_review.md:33` | U-5 (整类, 委托代裁) | |
| 84 | `ig34_p0192_a006` | 192 | §6.3.3 ECG Test Results (EG) | S1-R1 | T1 triage ATOM_ERR (writer, reviewed=True) | `work/triage_merged.json:11482 (lane C pack_020; T1.3 reviewer 100%)` | U-5 (整类, 委托代裁) | |
| 85 | `ig34_p0192_a009` | 192 | §6.3.3 ECG Test Results (EG) | S1-R1 | T1 triage ATOM_ERR (writer, reviewed=True) | `work/triage_merged.json:11495 (lane C pack_020; T1.3 reviewer 100%)` | U-5 (整类, 委托代裁) | |
| 86 | `ig34_p0196_a006` | 196 | §6.3.5.1 Generic Specimen-based Lab Findings Domai | C7-K4-rereview | t3_delta_rereview.md:58 (原子写 'Operationally defined', PDF/KB 'Operationally derived') | `-` | U-5 (整类, 委托代裁) | |
| 87 | `ig34_p0199_a003` | 199 | §6.3.5.2 Biospecimen Findings (BS) | S1-R1 | B-BS review: VISITDY 抽空; KB 与 PDF 一致 | `evidence/checkpoints/t2_B-BS_review.md:35 (页级行; 该批以范围/页号记这组原子)` | U-5 (整类, 委托代裁) | |
| 88 | `ig34_p0199_a004` | 199 | §6.3.5.2 Biospecimen Findings (BS) | S1-R1 | B-BS review: VISITDY 抽空; KB 与 PDF 一致 | `evidence/checkpoints/t2_B-BS_review.md:35 (页级行; 该批以范围/页号记这组原子)` | U-5 (整类, 委托代裁) | |
| 89 | `ig34_p0199_a005` | 199 | §6.3.5.2 Biospecimen Findings (BS) | S1-R1 | B-BS review: VISITDY 抽空; KB 与 PDF 一致 | `evidence/checkpoints/t2_B-BS_review.md:35 (页级行; 该批以范围/页号记这组原子)` | U-5 (整类, 委托代裁) | |
| 90 | `ig34_p0199_a006` | 199 | §6.3.5.2 Biospecimen Findings (BS) | S1-R1 | B-BS review: VISITDY 抽空; KB 与 PDF 一致 | `evidence/checkpoints/t2_B-BS_review.md:35 (页级行; 该批以范围/页号记这组原子)` | U-5 (整类, 委托代裁) | |
| 91 | `ig34_p0210_a002` | 210 | §6.3.5.3 Cell Phenotype Findings (CP) | C7-atom-not-in-PDF | atom_in_pdf=False; 修订行 .work/10_tier_b_repair/work/t2_batches/B-CP.writer.jsonl:40 | `evidence/checkpoints/t2_B-CP.md:55` | U-5 (整类, 委托代裁) | |
| 92 | `ig34_p0210_a007` | 210 | §6.3.5.3 Cell Phenotype Findings (CP) | C7-atom-not-in-PDF | atom_in_pdf=False; 修订行 .work/10_tier_b_repair/work/t2_batches/B-CP.writer.jsonl:42 | `evidence/checkpoints/t2_B-CP.md:57` | U-5 (整类, 委托代裁) | |
| 93 | `ig34_p0212_a006` | 212 | §6.3.5.3 Cell Phenotype Findings (CP) | C7-atom-not-in-PDF | atom_in_pdf=False; 修订行 .work/10_tier_b_repair/work/t2_batches/B-CP.writer.jsonl:9 | `evidence/checkpoints/t2_B-CP.md:24` | U-5 (整类, 委托代裁) | |
| 94 | `ig34_p0213_a013` | 213 | §6.3.5.3 Cell Phenotype Findings (CP) | C7-atom-not-in-PDF | atom_in_pdf=False; 修订行 .work/10_tier_b_repair/work/t2_batches/B-CP.writer.jsonl:18 | `evidence/checkpoints/t2_B-CP.md:33` | U-5 (整类, 委托代裁) | |
| 95 | `ig34_p0214_a008` | 214 | §6.3.5.3 Cell Phenotype Findings (CP) | C7-atom-not-in-PDF | atom_in_pdf=False; 修订行 .work/10_tier_b_repair/work/t2_batches/B-CP.writer.jsonl:22 | `evidence/checkpoints/t2_B-CP.md:37` | U-5 (整类, 委托代裁) | |
| 96 | `ig34_p0214_a009` | 214 | §6.3.5.3 Cell Phenotype Findings (CP) | C7-atom-not-in-PDF | atom_in_pdf=False; 修订行 .work/10_tier_b_repair/work/t2_batches/B-CP.writer.jsonl:23 | `evidence/checkpoints/t2_B-CP.md:38` | U-5 (整类, 委托代裁) | |
| 97 | `ig34_p0214_a010` | 214 | §6.3.5.3 Cell Phenotype Findings (CP) | C7-atom-not-in-PDF | atom_in_pdf=False; 修订行 .work/10_tier_b_repair/work/t2_batches/B-CP.writer.jsonl:24 | `evidence/checkpoints/t2_B-CP.md:39` | U-5 (整类, 委托代裁) | |
| 98 | `ig34_p0214_a011` | 214 | §6.3.5.3 Cell Phenotype Findings (CP) | C7-atom-not-in-PDF | atom_in_pdf=False; 修订行 .work/10_tier_b_repair/work/t2_batches/B-CP.writer.jsonl:25 | `evidence/checkpoints/t2_B-CP.md:40` | U-5 (整类, 委托代裁) | |
| 99 | `ig34_p0214_a012` | 214 | §6.3.5.3 Cell Phenotype Findings (CP) | C7-atom-not-in-PDF | atom_in_pdf=False; 修订行 .work/10_tier_b_repair/work/t2_batches/B-CP.writer.jsonl:26 | `evidence/checkpoints/t2_B-CP.md:41` | U-5 (整类, 委托代裁) | |
| 100 | `ig34_p0214_a013` | 214 | §6.3.5.3 Cell Phenotype Findings (CP) | C7-atom-not-in-PDF | atom_in_pdf=False; 修订行 .work/10_tier_b_repair/work/t2_batches/B-CP.writer.jsonl:27 | `evidence/checkpoints/t2_B-CP.md:42` | U-5 (整类, 委托代裁) | |
| 101 | `ig34_p0214_a014` | 214 | §6.3.5.3 Cell Phenotype Findings (CP) | C7-atom-not-in-PDF | atom_in_pdf=False; 修订行 .work/10_tier_b_repair/work/t2_batches/B-CP.writer.jsonl:28 | `evidence/checkpoints/t2_B-CP.md:43` | U-5 (整类, 委托代裁) | |
| 102 | `ig34_p0215_a005` | 215 | §6.3.5.3 Cell Phenotype Findings (CP) | C7-atom-not-in-PDF | atom_in_pdf=False; 修订行 .work/10_tier_b_repair/work/t2_batches/B-CP.writer.jsonl:29 | `evidence/checkpoints/t2_B-CP.md:44` | U-5 (整类, 委托代裁) | |
| 103 | `ig34_p0215_a010` | 215 | §6.3.5.3 Cell Phenotype Findings (CP) | C7-atom-not-in-PDF | atom_in_pdf=False; 修订行 .work/10_tier_b_repair/work/t2_batches/B-CP.writer.jsonl:30 | `evidence/checkpoints/t2_B-CP.md:45` | U-5 (整类, 委托代裁) | |
| 104 | `ig34_p0218_a002` | 218 | §6.3.5.3 Cell Phenotype Findings (CP) | C7-atom-not-in-PDF | atom_in_pdf=False; 修订行 .work/10_tier_b_repair/work/t2_batches/B-CP.writer.jsonl:35 | `evidence/checkpoints/t2_B-CP.md:50` | U-5 (整类, 委托代裁) | |
| 105 | `ig34_p0219_a002` | 219 | §6.3.5.3 Cell Phenotype Findings (CP) | C7-atom-not-in-PDF | atom_in_pdf=False; 修订行 .work/10_tier_b_repair/work/t2_batches/B-CP.writer.jsonl:37 | `evidence/checkpoints/t2_B-CP.md:52` | U-5 (整类, 委托代裁) | |
| 106 | `ig34_p0220_a006` | 220 | §6.3.5.3 Cell Phenotype Findings (CP) | C7-atom-not-in-PDF | atom_in_pdf=False; 修订行 .work/10_tier_b_repair/work/t2_batches/B-CP.writer.jsonl:38 | `evidence/checkpoints/t2_B-CP.md:53` | U-5 (整类, 委托代裁) | |
| 107 | `ig34_p0226_a008` | 226 | §6.3.5.4 Genomics Findings (GF) | S1-R1 | T1 triage ATOM_ERR (writer, reviewed=True) | `work/triage_merged.json:8897 (lane B pack_016; T1.3 reviewer 100%)` | U-5 (整类, 委托代裁) | |
| 108 | `ig34_p0226_a009` | 226 | §6.3.5.4 Genomics Findings (GF) | S1-R1 | T1 triage ATOM_ERR (writer, reviewed=True) | `work/triage_merged.json:8910 (lane B pack_016; T1.3 reviewer 100%)` | U-5 (整类, 委托代裁) | |
| 109 | `ig34_p0226_a010` | 226 | §6.3.5.4 Genomics Findings (GF) | S1-R1 | T1 triage ATOM_ERR (writer, reviewed=True) | `work/triage_merged.json:8923 (lane B pack_016; T1.3 reviewer 100%)` | U-5 (整类, 委托代裁) | |
| 110 | `ig34_p0226_a011` | 226 | §6.3.5.4 Genomics Findings (GF) | S1-R1 | T1 triage ATOM_ERR (writer, reviewed=True) | `work/triage_merged.json:8936 (lane B pack_016; T1.3 reviewer 100%)` | U-5 (整类, 委托代裁) | |
| 111 | `ig34_p0226_a012` | 226 | §6.3.5.4 Genomics Findings (GF) | S1-R1 | T1 triage ATOM_ERR (writer, reviewed=True) | `work/triage_merged.json:8949 (lane B pack_016; T1.3 reviewer 100%)` | U-5 (整类, 委托代裁) | |
| 112 | `ig34_p0226_a013` | 226 | §6.3.5.4 Genomics Findings (GF) | S1-R1 | T1 triage ATOM_ERR (writer, reviewed=True) | `work/triage_merged.json:8962 (lane B pack_016; T1.3 reviewer 100%)` | U-5 (整类, 委托代裁) | |
| 113 | `ig34_p0226_a014` | 226 | §6.3.5.4 Genomics Findings (GF) | S1-R1 | T1 triage ATOM_ERR (writer, reviewed=True) | `work/triage_merged.json:8975 (lane B pack_016; T1.3 reviewer 100%)` | U-5 (整类, 委托代裁) | |
| 114 | `ig34_p0226_a015` | 226 | §6.3.5.4 Genomics Findings (GF) | S1-R1 | T1 triage ATOM_ERR (writer, reviewed=True) | `work/triage_merged.json:8988 (lane B pack_016; T1.3 reviewer 100%)` | U-5 (整类, 委托代裁) | |
| 115 | `ig34_p0226_a016` | 226 | §6.3.5.4 Genomics Findings (GF) | S1-R1 | T1 triage ATOM_ERR (writer, reviewed=True) | `work/triage_merged.json:9001 (lane B pack_016; T1.3 reviewer 100%)` | U-5 (整类, 委托代裁) | |
| 116 | `ig34_p0226_a017` | 226 | §6.3.5.4 Genomics Findings (GF) | S1-R1 | T1 triage ATOM_ERR (writer, reviewed=True) | `work/triage_merged.json:9014 (lane B pack_016; T1.3 reviewer 100%)` | U-5 (整类, 委托代裁) | |
| 117 | `ig34_p0226_a018` | 226 | §6.3.5.4 Genomics Findings (GF) | S1-R1 | T1 triage ATOM_ERR (writer, reviewed=True) | `work/triage_merged.json:9027 (lane B pack_016; T1.3 reviewer 100%)` | U-5 (整类, 委托代裁) | |
| 118 | `ig34_p0226_a019` | 226 | §6.3.5.4 Genomics Findings (GF) | S1-R1 | T1 triage ATOM_ERR (writer, reviewed=True) | `work/triage_merged.json:9040 (lane B pack_016; T1.3 reviewer 100%)` | U-5 (整类, 委托代裁) | |
| 119 | `ig34_p0226_a020` | 226 | §6.3.5.4 Genomics Findings (GF) | S1-R1 | T1 triage ATOM_ERR (writer, reviewed=True) | `work/triage_merged.json:9053 (lane B pack_016; T1.3 reviewer 100%)` | U-5 (整类, 委托代裁) | |
| 120 | `ig34_p0226_a021` | 226 | §6.3.5.4 Genomics Findings (GF) | S1-R1 | T1 triage ATOM_ERR (writer, reviewed=True) | `work/triage_merged.json:9066 (lane B pack_016; T1.3 reviewer 100%)` | U-5 (整类, 委托代裁) | |
| 121 | `ig34_p0226_a022` | 226 | §6.3.5.4 Genomics Findings (GF) | S1-R1 | T1 triage ATOM_ERR (writer, reviewed=True) | `work/triage_merged.json:9079 (lane B pack_016; T1.3 reviewer 100%)` | U-5 (整类, 委托代裁) | |
| 122 | `ig34_p0226_a023` | 226 | §6.3.5.4 Genomics Findings (GF) | S1-R1 | T1 triage ATOM_ERR (writer, reviewed=True) | `work/triage_merged.json:9092 (lane B pack_016; T1.3 reviewer 100%)` | U-5 (整类, 委托代裁) | |
| 123 | `ig34_p0226_a024` | 226 | §6.3.5.4 Genomics Findings (GF) | S1-R1 | T1 triage ATOM_ERR (writer, reviewed=True) | `work/triage_merged.json:9105 (lane B pack_016; T1.3 reviewer 100%)` | U-5 (整类, 委托代裁) | |
| 124 | `ig34_p0236_a008` | 236 | §6.3.5.5 Immunogenicity Specimen Assessments (IS) | S1-R1 | B-IS review: verbatim 漏 ISSCAT | `evidence/checkpoints/t2_B-IS_review.md:70` | U-5 (整类, 委托代裁) | |
| 125 | `ig34_p0238_a005` | 238 | §6.3.5.5 Immunogenicity Specimen Assessments (IS) | S1-R1 | B-IS review: verbatim ISSEQ 记成 3 | `evidence/checkpoints/t2_B-IS_review.md:71` | U-5 (整类, 委托代裁) | |
| 126 | `ig34_p0240_a011` | 240 | §6.3.5.5 Immunogenicity Specimen Assessments (IS) | S1-R1 | B-IS review: verbatim 列错位 | `evidence/checkpoints/t2_B-IS_review.md:72` | U-5 (整类, 委托代裁) | |
| 127 | `ig34_p0241_a022` | 241 | §6.3.5.5 Immunogenicity Specimen Assessments (IS) | S1-R1 | B-IS review: verbatim CA, 记成 CA. | `evidence/checkpoints/t2_B-IS_review.md:73` | U-5 (整类, 委托代裁) | |
| 128 | `ig34_p0247_a005` | 247 | §6.3.5.6 Laboratory Test Results (LB) | C7-atom-not-in-PDF | atom_in_pdf=False; 修订行 .work/10_tier_b_repair/work/t2_batches/B-LB.writer.jsonl:47 | `evidence/checkpoints/t2_B-LB.md:47` | U-5 (整类, 委托代裁) | |
| 129 | `ig34_p0247_a011` | 247 | §6.3.5.6 Laboratory Test Results (LB) | C7-atom-not-in-PDF | atom_in_pdf=False; 修订行 .work/10_tier_b_repair/work/t2_batches/B-LB.writer.jsonl:52 | `evidence/checkpoints/t2_B-LB.md:48` | U-5 (整类, 委托代裁) | |
| 130 | `ig34_p0247_a021` | 247 | §6.3.5.6 Laboratory Test Results (LB) | C7-K4-rereview | t3_delta_rereview.md:51,59 (原子写 'PtFtv / 1999-05-15', PDF/KB 'PrThr / 1999-06-19T04:00') | `-` | U-5 (整类, 委托代裁) | |
| 131 | `ig34_p0247_a022` | 247 | §6.3.5.6 Laboratory Test Results (LB) | C7-atom-not-in-PDF | atom_in_pdf=False; 修订行 .work/10_tier_b_repair/work/t2_batches/B-LB.writer.jsonl:58 | `evidence/checkpoints/t2_B-LB.md:51` | U-5 (整类, 委托代裁) | |
| 132 | `ig34_p0257_a010` | 257 | §6.3.5.7.3 Microbiology Specimen/Microbiology Susc | S1-R1 | B-MB review: verbatim 为旧 KB 错值, 按 PDF 改 | `evidence/checkpoints/t2_B-MB_review.md:61` | U-5 (整类, 委托代裁) | |
| 133 | `ig34_p0258_a019` | 258 | §6.3.5.7.3 Microbiology Specimen/Microbiology Susc | S1-R1 | B-MB review: verbatim 为旧 KB 错值, 按 PDF 改 | `evidence/checkpoints/t2_B-MB_review.md:62` | U-5 (整类, 委托代裁) | |
| 134 | `ig34_p0258_a020` | 258 | §6.3.5.7.3 Microbiology Specimen/Microbiology Susc | S1-R1 | B-MB review: verbatim 为旧 KB 错值, 按 PDF 改 | `evidence/checkpoints/t2_B-MB_review.md:62 (页级行; 该批以范围/页号记这组原子)` | U-5 (整类, 委托代裁) | |
| 135 | `ig34_p0258_a021` | 258 | §6.3.5.7.3 Microbiology Specimen/Microbiology Susc | S1-R1 | B-MB review: verbatim 为旧 KB 错值, 按 PDF 改 | `evidence/checkpoints/t2_B-MB_review.md:62 (页级行; 该批以范围/页号记这组原子)` | U-5 (整类, 委托代裁) | |
| 136 | `ig34_p0258_a022` | 258 | §6.3.5.7.3 Microbiology Specimen/Microbiology Susc | S1-R1 | B-MB review: verbatim 为旧 KB 错值, 按 PDF 改 | `evidence/checkpoints/t2_B-MB_review.md:62 (页级行; 该批以范围/页号记这组原子)` | U-5 (整类, 委托代裁) | |
| 137 | `ig34_p0258_a023` | 258 | §6.3.5.7.3 Microbiology Specimen/Microbiology Susc | S1-R1 | B-MB review: verbatim 为旧 KB 错值, 按 PDF 改 | `evidence/checkpoints/t2_B-MB_review.md:62 (页级行; 该批以范围/页号记这组原子)` | U-5 (整类, 委托代裁) | |
| 138 | `ig34_p0258_a024` | 258 | §6.3.5.7.3 Microbiology Specimen/Microbiology Susc | S1-R1 | B-MB review: verbatim 为旧 KB 错值, 按 PDF 改 | `evidence/checkpoints/t2_B-MB_review.md:62 (页级行; 该批以范围/页号记这组原子)` | U-5 (整类, 委托代裁) | |
| 139 | `ig34_p0260_a009` | 260 | §6.3.5.7.3 Microbiology Specimen/Microbiology Susc | S1-R1 | B-MB review: verbatim 为旧 KB 错值, 按 PDF 改 | `evidence/checkpoints/t2_B-MB_review.md:63` | U-5 (整类, 委托代裁) | |
| 140 | `ig34_p0260_a015` | 260 | §6.3.5.7.3 Microbiology Specimen/Microbiology Susc | S1-R1 | B-MB review: verbatim 为旧 KB 错值, 按 PDF 改 | `evidence/checkpoints/t2_B-MB_review.md:64` | U-5 (整类, 委托代裁) | |
| 141 | `ig34_p0263_a021` | 263 | §6.3.5.7.3 Microbiology Specimen/Microbiology Susc | S1-R1 | B-MB review: verbatim 为旧 KB 错值, 按 PDF 改 | `evidence/checkpoints/t2_B-MB_review.md:65` | U-5 (整类, 委托代裁) | |
| 142 | `ig34_p0263_a022` | 263 | §6.3.5.7.3 Microbiology Specimen/Microbiology Susc | S1-R1 | B-MB review: verbatim 为旧 KB 错值, 按 PDF 改 | `evidence/checkpoints/t2_B-MB_review.md:65 (页级行; 该批以范围/页号记这组原子)` | U-5 (整类, 委托代裁) | |
| 143 | `ig34_p0270_a013` | 270 | §6.3.5.9.1 Pharmacokinetics Concentrations (PC) | C7-atom-not-in-PDF | atom_in_pdf=False; 修订行 .work/10_tier_b_repair/work/t2_batches/B-PCPP.writer.jsonl:2 | `evidence/checkpoints/t2_B-PCPP.md:17` | U-5 (整类, 委托代裁) | |
| 144 | `ig34_p0270_a014` | 270 | §6.3.5.9.1 Pharmacokinetics Concentrations (PC) | C7-atom-not-in-PDF | atom_in_pdf=False; 修订行 .work/10_tier_b_repair/work/t2_batches/B-PCPP.writer.jsonl:3 | `evidence/checkpoints/t2_B-PCPP.md:18` | U-5 (整类, 委托代裁) | |
| 145 | `ig34_p0270_a023` | 270 | §6.3.5.9.1 Pharmacokinetics Concentrations (PC) | C7-atom-not-in-PDF | atom_in_pdf=False; 修订行 .work/10_tier_b_repair/work/t2_batches/B-PCPP.writer.jsonl:4 | `evidence/checkpoints/t2_B-PCPP.md:19` | U-5 (整类, 委托代裁) | |
| 146 | `ig34_p0271_a007` | 271 | §6.3.5.9.1 Pharmacokinetics Concentrations (PC) | C7-atom-not-in-PDF | atom_in_pdf=False; 修订行 .work/10_tier_b_repair/work/t2_batches/B-PCPP.writer.jsonl:5 | `evidence/checkpoints/t2_B-PCPP.md:20` | U-5 (整类, 委托代裁) | |
| 147 | `ig34_p0271_a009` | 271 | §6.3.5.9.1 Pharmacokinetics Concentrations (PC) | C7-atom-not-in-PDF | atom_in_pdf=False; 修订行 .work/10_tier_b_repair/work/t2_batches/B-PCPP.writer.jsonl:6 | `evidence/checkpoints/t2_B-PCPP.md:21` | U-5 (整类, 委托代裁) | |
| 148 | `ig34_p0271_a010` | 271 | §6.3.5.9.1 Pharmacokinetics Concentrations (PC) | C7-atom-not-in-PDF | atom_in_pdf=False; 修订行 .work/10_tier_b_repair/work/t2_batches/B-PCPP.writer.jsonl:7 | `evidence/checkpoints/t2_B-PCPP.md:22` | U-5 (整类, 委托代裁) | |
| 149 | `ig34_p0271_a011` | 271 | §6.3.5.9.1 Pharmacokinetics Concentrations (PC) | C7-atom-not-in-PDF | atom_in_pdf=False; 修订行 .work/10_tier_b_repair/work/t2_batches/B-PCPP.writer.jsonl:8 | `evidence/checkpoints/t2_B-PCPP.md:23` | U-5 (整类, 委托代裁) | |
| 150 | `ig34_p0274_a019` | 274 | §6.3.5.9.2 Pharmacokinetics Parameters (PP) | S1-R1 | 原子 row 7 多 `Collected`; PDF p274 文本层 :35 row 7 = SINGLE DOSE 无 Collected; KB PP/examples.m | `work/t3_fp_expected_regressions.jsonl:49` | U-5 (整类, 委托代裁) | |
| 151 | `ig34_p0277_a004` | 277 | §6.3.5.9.3 Relating PP Records to PC Records | C7-atom-not-in-PDF | atom_in_pdf=False; 修订行 .work/10_tier_b_repair/work/t2_batches/B-PCPP.writer.jsonl:9 | `evidence/checkpoints/t2_B-PCPP.md:24` | U-5 (整类, 委托代裁) | |
| 152 | `ig34_p0277_a005` | 277 | §6.3.5.9.3 Relating PP Records to PC Records | C7-atom-not-in-PDF | atom_in_pdf=False; 修订行 .work/10_tier_b_repair/work/t2_batches/B-PCPP.writer.jsonl:10 | `evidence/checkpoints/t2_B-PCPP.md:25` | U-5 (整类, 委托代裁) | |
| 153 | `ig34_p0277_a006` | 277 | §6.3.5.9.3 Relating PP Records to PC Records | C7-atom-not-in-PDF | atom_in_pdf=False; 修订行 .work/10_tier_b_repair/work/t2_batches/B-PCPP.writer.jsonl:11 | `evidence/checkpoints/t2_B-PCPP.md:26` | U-5 (整类, 委托代裁) | |
| 154 | `ig34_p0277_a007` | 277 | §6.3.5.9.3 Relating PP Records to PC Records | C7-atom-not-in-PDF | atom_in_pdf=False; 修订行 .work/10_tier_b_repair/work/t2_batches/B-PCPP.writer.jsonl:12 | `evidence/checkpoints/t2_B-PCPP.md:27` | U-5 (整类, 委托代裁) | |
| 155 | `ig34_p0277_a008` | 277 | §6.3.5.9.3 Relating PP Records to PC Records | C7-atom-not-in-PDF | atom_in_pdf=False; 修订行 .work/10_tier_b_repair/work/t2_batches/B-PCPP.writer.jsonl:13 | `evidence/checkpoints/t2_B-PCPP.md:28` | U-5 (整类, 委托代裁) | |
| 156 | `ig34_p0277_a009` | 277 | §6.3.5.9.3 Relating PP Records to PC Records | C7-atom-not-in-PDF | atom_in_pdf=False; 修订行 .work/10_tier_b_repair/work/t2_batches/B-PCPP.writer.jsonl:14 | `evidence/checkpoints/t2_B-PCPP.md:29` | U-5 (整类, 委托代裁) | |
| 157 | `ig34_p0277_a010` | 277 | §6.3.5.9.3 Relating PP Records to PC Records | C7-atom-not-in-PDF | atom_in_pdf=False; 修订行 .work/10_tier_b_repair/work/t2_batches/B-PCPP.writer.jsonl:15 | `evidence/checkpoints/t2_B-PCPP.md:30` | U-5 (整类, 委托代裁) | |
| 158 | `ig34_p0277_a011` | 277 | §6.3.5.9.3 Relating PP Records to PC Records | C7-atom-not-in-PDF | atom_in_pdf=False; 修订行 .work/10_tier_b_repair/work/t2_batches/B-PCPP.writer.jsonl:16 | `evidence/checkpoints/t2_B-PCPP.md:31` | U-5 (整类, 委托代裁) | |
| 159 | `ig34_p0277_a012` | 277 | §6.3.5.9.3 Relating PP Records to PC Records | C7-atom-not-in-PDF | atom_in_pdf=False; 修订行 .work/10_tier_b_repair/work/t2_batches/B-PCPP.writer.jsonl:17 | `evidence/checkpoints/t2_B-PCPP.md:32` | U-5 (整类, 委托代裁) | |
| 160 | `ig34_p0277_a013` | 277 | §6.3.5.9.3 Relating PP Records to PC Records | C7-atom-not-in-PDF | atom_in_pdf=False; 修订行 .work/10_tier_b_repair/work/t2_batches/B-PCPP.writer.jsonl:18 | `evidence/checkpoints/t2_B-PCPP.md:33` | U-5 (整类, 委托代裁) | |
| 161 | `ig34_p0277_a014` | 277 | §6.3.5.9.3 Relating PP Records to PC Records | C7-atom-not-in-PDF | atom_in_pdf=False; 修订行 .work/10_tier_b_repair/work/t2_batches/B-PCPP.writer.jsonl:19 | `evidence/checkpoints/t2_B-PCPP.md:34` | U-5 (整类, 委托代裁) | |
| 162 | `ig34_p0277_a015` | 277 | §6.3.5.9.3 Relating PP Records to PC Records | C7-atom-not-in-PDF | atom_in_pdf=False; 修订行 .work/10_tier_b_repair/work/t2_batches/B-PCPP.writer.jsonl:20 | `evidence/checkpoints/t2_B-PCPP.md:35` | U-5 (整类, 委托代裁) | |
| 163 | `ig34_p0278_a051` | 278 | §6.3.5.9.3 Relating PP Records to PC Records — Exa | S1-R1 | S-SPC2 #15: 原子抄自旧错 KB (多 and "10" through "12"/individual); KB PC/examples.md:146 = p278 渲 | `work/t3_fp_expected_regressions.jsonl:64` | U-5 (整类, 委托代裁) | |
| 164 | `ig34_p0289_a024` | 289 | §6.3.7.2 Cardiovascular System Findings (CV) | S1-R1 | B-CV review: verbatim 漏 'Cross-sec.' 的点; KB 与渲染图一致 | `evidence/checkpoints/t2_B-CV_review.md:37` | U-5 (整类, 委托代裁) | |
| 165 | `ig34_p0289_a025` | 289 | §6.3.7.2 Cardiovascular System Findings (CV) | S1-R1 | B-CV review: verbatim 漏 'Cross-sec.' 的点; KB 与渲染图一致 | `evidence/checkpoints/t2_B-CV_review.md:37 (页级行; 该批以范围/页号记这组原子)` | U-5 (整类, 委托代裁) | |
| 166 | `ig34_p0301_a017` | 301 | §6.3.7.5 Ophthalmic Examinations (OE) | S1-R1 | B-OE review: verbatim 抽错 (多值/乱码/installation→instillation) | `evidence/checkpoints/t2_B-OE.md:65` | U-5 (整类, 委托代裁) | |
| 167 | `ig34_p0301_a018` | 301 | §6.3.7.5 Ophthalmic Examinations (OE) | S1-R1 | B-OE review: verbatim 抽错 (多值/乱码/installation→instillation) | `evidence/checkpoints/t2_B-OE.md:65` | U-5 (整类, 委托代裁) | |
| 168 | `ig34_p0304_a020` | 304 | §6.3.7.5 Ophthalmic Examinations (OE) | S1-R1 | B-OE review: verbatim 抽错 (多值/乱码/installation→instillation) | `evidence/checkpoints/t2_B-OE.md:65` | U-5 (整类, 委托代裁) | |
| 169 | `ig34_p0304_a021` | 304 | §6.3.7.5 Ophthalmic Examinations (OE) | S1-R1 | B-OE review: verbatim 抽错 (多值/乱码/installation→instillation) | `evidence/checkpoints/t2_B-OE.md:61 (页级行; 该批以范围/页号记这组原子)` | U-5 (整类, 委托代裁) | |
| 170 | `ig34_p0304_a022` | 304 | §6.3.7.5 Ophthalmic Examinations (OE) | S1-R1 | B-OE review: verbatim 抽错 (多值/乱码/installation→instillation) | `evidence/checkpoints/t2_B-OE.md:61 (页级行; 该批以范围/页号记这组原子)` | U-5 (整类, 委托代裁) | |
| 171 | `ig34_p0304_a023` | 304 | §6.3.7.5 Ophthalmic Examinations (OE) | S1-R1 | B-OE review: verbatim 抽错 (多值/乱码/installation→instillation) | `evidence/checkpoints/t2_B-OE.md:61 (页级行; 该批以范围/页号记这组原子)` | U-5 (整类, 委托代裁) | |
| 172 | `ig34_p0307_a008` | 307 | §6.3.7.6 Reproductive System Findings (RP) | S1-R1 | B-RP review: 原子漏 RPSTRESN 值 (a008 编号待 T3 核) | `evidence/checkpoints/t2_B-RP_review.md:24` | U-5 (整类, 委托代裁) | |
| 173 | `ig34_p0322_a013` | 322 | §6.3.9.1 Functional Tests (FT) — FT-Assumptions —  | S1-R1 | B-FT review: 原子漏 'see Section 4 of the QRS supplement.'; PDF/KB 均有 | `evidence/checkpoints/t2_B-FT_review.md:22 (页级行; 该批以范围/页号记这组原子)` | U-5 (整类, 委托代裁) | |
| 174 | `ig34_p0327_a015` | 327 | §6.3.9.2 Questionnaires (QS) — QS-Assumptions — QR | S1-R1 | B-QS audit: 原子漏 '; see Section 4 of the QRS supplement'; PDF/KB 均有 | `evidence/checkpoints/t2_B-QS_audit.md:13` | U-5 (整类, 委托代裁) | |
| 175 | `ig34_p0337_a002` | 337 | §6.3.9.3.2 Clinical Classifications Use Case | S1-R1 | B-RS audit: verbatim 与 PDF 页文本不符 实为 p336 CC 3b; KB 与页文本一致 | `evidence/checkpoints/t2_B-RS_audit.md:11 (页级行; 该批以范围/页号记这组原子)` | U-5 (整类, 委托代裁) | |
| 176 | `ig34_p0337_a003` | 337 | §6.3.9.3.2 Clinical Classifications Use Case | S1-R1 | B-RS audit: verbatim 与 PDF 页文本不符 实为 p336 CC 3c; KB 与页文本一致 | `evidence/checkpoints/t2_B-RS_audit.md:11 (页级行; 该批以范围/页号记这组原子)` | U-5 (整类, 委托代裁) | |
| 177 | `ig34_p0337_a006` | 337 | §6.3.9.3.2 Clinical Classifications Use Case | S1-R1 | B-RS audit: verbatim 与 PDF 页文本不符; KB 与页文本一致 | `evidence/checkpoints/t2_B-RS_audit.md:11 (页级行; 该批以范围/页号记这组原子)` | U-5 (整类, 委托代裁) | |
| 178 | `ig34_p0337_a015` | 337 | §6.3.9.3.2 Clinical Classifications Use Case | S1-R1 | B-RS audit: verbatim 与 PDF 页文本不符; KB 与页文本一致 | `evidence/checkpoints/t2_B-RS_audit.md:11 (页级行; 该批以范围/页号记这组原子)` | U-5 (整类, 委托代裁) | |
| 179 | `ig34_p0338_a002` | 338 | §6.3.9.3.2 Clinical Classifications Use Case | S1-R1 | B-RS audit: verbatim 与 PDF 页文本不符; KB 与页文本一致 | `evidence/checkpoints/t2_B-RS_audit.md:14 (页级行; 该批以范围/页号记这组原子)` | U-5 (整类, 委托代裁) | |
| 180 | `ig34_p0338_a003` | 338 | §6.3.9.3.2 Clinical Classifications Use Case | S1-R1 | B-RS audit: verbatim 与 PDF 页文本不符; KB 与页文本一致 | `evidence/checkpoints/t2_B-RS_audit.md:14 (页级行; 该批以范围/页号记这组原子)` | U-5 (整类, 委托代裁) | |
| 181 | `ig34_p0338_a010` | 338 | §6.3.9.3.2 Clinical Classifications Use Case | S1-R1 | B-RS audit: verbatim 与 PDF 页文本不符; KB 与页文本一致 | `evidence/checkpoints/t2_B-RS_audit.md:14 (页级行; 该批以范围/页号记这组原子)` | U-5 (整类, 委托代裁) | |
| 182 | `ig34_p0338_a013` | 338 | §6.3.9.3.2 Clinical Classifications Use Case | S1-R1 | B-RS audit: verbatim 与 PDF 页文本不符; KB 与页文本一致 | `evidence/checkpoints/t2_B-RS_audit.md:19` | U-5 (整类, 委托代裁) | |
| 183 | `ig34_p0339_a001` | 339 | §6.3.9.3.2 Clinical Classifications Use Case | S1-R1 | B-RS audit: verbatim 与 PDF 页文本不符; KB 与页文本一致 | `evidence/checkpoints/t2_B-RS_audit.md:15 (页级行; 该批以范围/页号记这组原子)` | U-5 (整类, 委托代裁) | |
| 184 | `ig34_p0342_a004` | 342 | SC – Examples | S1-R1 | 原子表头 SCORESU; PDF p342 与 KB 均 SCORRESU \| errata: t3_atom_err \| new_target: domains/SC/ex | `work/t3_fp_expected_regressions.jsonl:88` | U-5 (整类, 委托代裁) | |
| 185 | `ig34_p0347_a003` | 347 | TU – Assumptions | S1-R1 | B-TU audit: verbatim 'TULORRES' 为抽取错, PDF 文本层 TUORRES; KB 与 PDF 一致 | `evidence/checkpoints/t2_B-TU_audit.md:21` | U-5 (整类, 委托代裁) | |
| 186 | `ig34_p0348_a010` | 348 | TU – Assumptions | S1-R1 | B-TU audit: verbatim 'TUTEST' 为抽取错, PDF 文本层 TUTESTs; KB 与 PDF 一致 | `evidence/checkpoints/t2_B-TU_audit.md:17` | U-5 (整类, 委托代裁) | |
| 187 | `ig34_p0360_a021` | 360 | §6.3.13 VS – Examples | S1-R1 | B-VS audit: VSDY 读空 / VSTPT 截成 BASELINE | `evidence/checkpoints/t2_B-VS_audit.md:43` | U-5 (整类, 委托代裁) | |
| 188 | `ig34_p0360_a022` | 360 | §6.3.13 VS – Examples | S1-R1 | B-VS audit: VSDY 读空 / VSTPT 截成 BASELINE | `evidence/checkpoints/t2_B-VS_audit.md:43` | U-5 (整类, 委托代裁) | |
| 189 | `ig34_p0360_a023` | 360 | §6.3.13 VS – Examples | S1-R1 | B-VS audit: VSDY 读空 / VSTPT 截成 BASELINE | `evidence/checkpoints/t2_B-VS_audit.md:43` | U-5 (整类, 委托代裁) | |
| 190 | `ig34_p0360_a024` | 360 | §6.3.13 VS – Examples | S1-R1 | B-VS audit: VSDY 读空 / VSTPT 截成 BASELINE | `evidence/checkpoints/t2_B-VS_audit.md:43` | U-5 (整类, 委托代裁) | |
| 191 | `ig34_p0361_a016` | 361 | §6.4.1 When to Use Findings About Events or Interv | S1-R1 | B-FA audit: 原子抽错 | `evidence/checkpoints/t2_B-FA_audit.md:36` | U-5 (整类, 委托代裁) | |
| 192 | `ig34_p0373_a021` | 373 | FA – Examples | S1-R1 | B-FA audit: 原子抽错 | `evidence/checkpoints/t2_B-FA_audit.md:58` | U-5 (整类, 委托代裁) | |
| 193 | `ig34_p0374_a011` | 374 | FA – Examples | S1-R1 | B-FA: 原子把 AE ID 与合并格抽在同一行, 与渲染不符 | `evidence/checkpoints/t2_B-FA.md:119` | U-5 (整类, 委托代裁) | |
| 194 | `ig34_p0389_a012` | 389 | §7.2.1 Trial Arms (TA) – Example 1 | S1-R1 | T1 triage ATOM_ERR (writer, reviewed=True) | `work/triage_merged.json:7628 (lane B pack_014; T1.3 reviewer 100%)` | U-5 (整类, 委托代裁) | |
| 195 | `ig34_p0389_a013` | 389 | §7.2.1 Trial Arms (TA) – Example 1 | S1-R1 | T1 triage ATOM_ERR (writer, reviewed=True) | `work/triage_merged.json:7641 (lane B pack_014; T1.3 reviewer 100%)` | U-5 (整类, 委托代裁) | |
| 196 | `ig34_p0396_a009` | 396 | §7.2.1 Trial Arms (TA) – Example 4 | S1-R1 | T2 global fp audit R1: 原子 `represents`; PDF p396 为 `represented this rule`, KB 同 (B-TA #31 | `evidence/t2_fp_expected_regressions.md:53` | U-5 (整类, 委托代裁) | |
| 197 | `ig34_p0419_a004` | 419 | §7.4.2 Trial Summary (TS) – Assumptions | S1-R1 | B-TS writer: 原子抽取错, KB 正确 | `evidence/checkpoints/t2_B-TS.md:86` | U-5 (整类, 委托代裁) | |

## PDF_TYPO (149)

| # | atom_id | 页 | 节 | 规则 | 依据 / 登记 | 出处 | 决定来源 | 异议 |
|--:|---|--:|---|---|---|---|---|---|
| 1 | `ig34_p0010_a002` | 10 | §1.4.1 [How to Read a Domain Specification] | S1-R2 | B-ch01 T-1: PDF 缺 has, KB 补 | `evidence/checkpoints/t2_B-ch01.md:98` | U-5 (整类, 委托代裁) | |
| 2 | `ig34_p0010_a023` | 10 | §1.5 [Known Issues] | S1-R2 | B-ch01 T-2: --LNKID/--LNKGRP 对调 | `evidence/checkpoints/t2_B-ch01.md:26` | U-5 (整类, 委托代裁) | |
| 3 | `ig34_p0016_a019` | 16 | §2.7 SDTM Variables Not Allowed in the SDTMIG | writer-Tn-registry | B-ch02 T-1 (KB 写正确值) | `work/t2_batches/B-ch02.writer.jsonl:34` | U-7 委托代裁 (§000), 非 U-5; B-ch02 T-1: U-7 B (委托代裁 2026-11-27) [A2-11] | |
| 4 | `ig34_p0018_a012` | 18 | §3.2.1 Dataset-level Metadata | K3b-registry | B-ch03 T-1 | `-` | U-5 (整类, 委托代裁) | |
| 5 | `ig34_p0018_a036` | 18 | §3.2.1 Dataset-level Metadata | K3b-registry | B-ch03 T-2 | `-` | U-5 (整类, 委托代裁) | |
| 6 | `ig34_p0026_a037` | 26 | §4.1.9 [Assigning Natural Keys in the Metadata] | K3b-registry | B-ch04 T-7 | `-` | U-8 委托代裁 (§000), 非 U-5 | |
| 7 | `ig34_p0041_a038` | 41 | §4.4.3.2 [Interval with Uncertainty] | K3b-registry | B-ch04 N-1 | `-` | U-7 委托代裁 (§000), 非 U-5; B-ch04 N-1: U-7 B (委托代裁 2026-11-27) [A3-34] | |
| 8 | `ig34_p0049_a008` | 49 | §4.4.11 [Disease Milestones and Disease Milestone  | K3b-registry | B-ch04 T-4 | `-` | U-5 (整类, 委托代裁) | |
| 9 | `ig34_p0063_a023` | 63 | §5.2 [Demographics (DM)] | K3b-registry | S-SPEC1 T-1 | `-` | U-5 (整类, 委托代裁) | |
| 10 | `ig34_p0068_a010` | 68 | §5.2 [DM – Examples] | K3b-registry | B-DM T-2 | `-` | U-5 (整类, 委托代裁) | |
| 11 | `ig34_p0082_a025` | 82 | §5.3 [Subject Elements (SE)] | K3b-registry | S-SPREL SE T-1 | `-` | U-8 委托代裁 (§000), 非 U-5 | |
| 12 | `ig34_p0085_a010` | 85 | §5.4 [Subject Disease Milestones (SM)] | S1-R2 | T4 U-7 (委托代裁 2026-11-27) KB 写正确值, 原子 = PDF: A2-8 B-SM O32 SMDY→SMSTDY \| errata: t3_atom_e | `work/t3_fp_expected_regressions.jsonl:6` | U-7 委托代裁 (§000), 非 U-5; B-SM O32: U-7 B (委托代裁 2026-11-27) [A2-8] | |
| 13 | `ig34_p0085_a019` | 85 | §5.4 [Subject Disease Milestones (SM)] | K3b-registry | B-SM T-3 | `-` | U-5 (整类, 委托代裁) | |
| 14 | `ig34_p0089_a026` | 89 | §5.5 [Subject Visits (SV)] | K3b-registry | B-SV T-1 | `-` | U-5 (整类, 委托代裁) | |
| 15 | `ig34_p0107_a002` | 107 | §6.1.3.1 [Exposure (EX)] | K3b-registry | S-INT EX T-7 | `-` | U-5 (整类, 委托代裁) | |
| 16 | `ig34_p0113_a011` | 113 | §6.1.3.3 [Exposure/Exposure as Collected Examples] | K3b-registry | B-EX T-3 | `-` | U-5 (整类, 委托代裁) | |
| 17 | `ig34_p0115_a009` | 115 | §6.1.3.3 [Exposure/Exposure as Collected Examples] | K3b-registry | B-EX T-4 | `-` | U-5 (整类, 委托代裁) | |
| 18 | `ig34_p0118_a017` | 118 | §6.1.3.3 [Exposure/Exposure as Collected Examples] | S1-R2 | B-EX T-6: verbatim mg/mL 为 PDF 笔误, KB 改 mg/kg | `evidence/checkpoints/t2_B-EX.md:133` | U-5 (整类, 委托代裁) | |
| 19 | `ig34_p0119_a011` | 119 | §6.1.3.3 [Exposure/Exposure as Collected Examples] | writer-Tn-registry | B-EX T-2 (KB 写正确值) | `work/t2_batches/B-EX.writer.jsonl:37` | U-5 (整类, 委托代裁) | |
| 20 | `ig34_p0123_a005` | 123 | §6.1.4 [Meal Data (ML)] | writer-Tn-registry | B-ML T-2 (KB 写正确值) | `work/t2_batches/B-ML.writer.jsonl:8` | U-5 (整类, 委托代裁) | |
| 21 | `ig34_p0124_a017` | 124 | §6.1.4 [Meal Data (ML)] | K3b-registry | B-ML T-1 | `-` | U-5 (整类, 委托代裁) | |
| 22 | `ig34_p0132_a014` | 132 | §6.1.6 [Substance Use (SU)] | K3b-registry | B-SU T-1 | `-` | U-5 (整类, 委托代裁) | |
| 23 | `ig34_p0142_a012` | 142 | §6.2.1 [Adverse Events (AE)] | writer-Tn-registry | B-AE T-3 (KB 写正确值) | `work/t2_batches/B-AE.writer.jsonl:5` | U-5 (整类, 委托代裁) | |
| 24 | `ig34_p0142_a014` | 142 | §6.2.1 [Adverse Events (AE)] | K3b-registry | B-AE T-4 | `-` | U-5 (整类, 委托代裁) | |
| 25 | `ig34_p0142_a015` | 142 | §6.2.1 [Adverse Events (AE)] | K3b-registry | B-AE T-1 | `-` | U-5 (整类, 委托代裁) | |
| 26 | `ig34_p0142_a016` | 142 | §6.2.1 [Adverse Events (AE)] | K3b-registry | B-AE T-2 | `-` | U-5 (整类, 委托代裁) | |
| 27 | `ig34_p0146_a005` | 146 | §6.2.2 [Biospecimen Events (BE)] | K3b-registry | B-BE T-1, B-BE T-2 | `-` | U-5 (整类, 委托代裁) | |
| 28 | `ig34_p0152_a0019` | 152 | §6.2.3 [Clinical Events] | writer-Tn-registry | B-CE T-1 (KB 写正确值) | `work/t2_batches/B-CE.writer.jsonl:9` | U-5 (整类, 委托代裁) | |
| 29 | `ig34_p0160_a0026` | 160 | §6.2.4 Disposition (DS) | S1-R2 | T4 U-7 (委托代裁 2026-11-27) KB 写正确值, 原子 = PDF: A3-2 B-DS U-4 删 in \| errata: t3_atom_err \| n | `work/t3_fp_expected_regressions.jsonl:17` | U-7 委托代裁 (§000), 非 U-5; B-DS U-4: U-7 B (委托代裁 2026-11-27) [A3-2] | |
| 30 | `ig34_p0160_a0028` | 160 | §6.2.4 Disposition (DS) | S1-R2 | B-DS T-3 PDF_TYPO (DSDTDTC)→(DSSTDTC) (t2_B-DS.md:35) \| errata: t3_atom_err \| new_target | `work/t3_fp_expected_regressions.jsonl:18` | U-5 (整类, 委托代裁) | |
| 31 | `ig34_p0165_a0007` | 165 | §6.2.4 Disposition (DS) | S1-R2 | T4 U-7 (委托代裁 2026-11-27) KB 写正确值, 原子 = PDF: A1-9 B-DS U-1 se ETCD SCREEN→SCRN \| errata: t | `work/t3_fp_expected_regressions.jsonl:19` | U-7 委托代裁 (§000), 非 U-5; B-DS U-1: U-7 B (委托代裁 2026-11-27) [A1-9] | |
| 32 | `ig34_p0166_a0035` | 166 | §6.2.4 Disposition (DS) | K3b-registry | B-DS T-5 | `-` | U-5 (整类, 委托代裁) | |
| 33 | `ig34_p0169_a0024` | 169 | §6.2.5 Healthcare Encounters (HO) | writer-Tn-registry | B-HO T-1 (KB 写正确值) | `work/t2_batches/B-HO.writer.jsonl:1` | U-5 (整类, 委托代裁) | |
| 34 | `ig34_p0173_a0007` | 173 | §6.2.6 Medical History (MH) | writer-Tn-registry | B-MH T-3 (KB 写正确值) | `work/t2_batches/B-MH.writer.jsonl:11` | U-5 (整类, 委托代裁) | |
| 35 | `ig34_p0174_a0012` | 174 | §6.2.6 Medical History (MH) | S1-R2 | T2 global fp audit R2: B-MH T-1 PDF_TYPO 第二处 MHENDTYP→MHEVDTYP (原子=PDF) \| errata: t3_atom | `evidence/t2_fp_expected_regressions.md:53` | U-5 (整类, 委托代裁) | |
| 36 | `ig34_p0190_a017` | 190 | §6.3.3 ECG Test Results (EG) | S1-R2 | T4 U-7 (委托代裁 2026-11-27) KB 写正确值, 原子 = PDF: A3-5 B-EG T-3 investigation→investigator \| er | `work/t3_fp_expected_regressions.jsonl:22` | U-7 委托代裁 (§000), 非 U-5; B-EG T-3: U-7 B (委托代裁 2026-11-27) [A3-5] | |
| 37 | `ig34_p0198_a012` | 198 | §6.3.5.2 Biospecimen Findings (BS) | S1-R2 | B-BS review: PDF 'part the' (PDF_TYPO) 被抽成 'part of the'; KB 正确拼写 [B-BS T-2] | `evidence/checkpoints/t2_B-BS_review.md:54 (页级行; 该批以范围/页号记这组原子)` | U-5 (整类, 委托代裁) | |
| 38 | `ig34_p0198_a014` | 198 | §6.3.5.2 Biospecimen Findings (BS) | K3b-registry | B-BS T-3 | `-` | U-5 (整类, 委托代裁) | |
| 39 | `ig34_p0198_a020` | 198 | §6.3.5.2 Biospecimen Findings (BS) | K3b-registry | B-BS T-1a, B-BS T-1b | `-` | U-5 (整类, 委托代裁) | |
| 40 | `ig34_p0199_a020` | 199 | §6.3.5.3 Cell Phenotype Findings (CP) | S1-R2 | S-SPC1 CP T-21 PDF_TYPO --BNDAGT/--GATEDEF→--BDAGNT/--GATDEF (spec 变量名) \| errata: t3_atom | `work/t3_fp_expected_regressions.jsonl:23` | U-5 (整类, 委托代裁) | |
| 41 | `ig34_p0200_a006` | 200 | §6.3.5.3 Cell Phenotype Findings (CP) | S1-R2 | S-SPC1 CP T-17 PDF_TYPO sting→string \| errata: t3_atom_err \| new_target: domains/CP/assu | `work/t3_fp_expected_regressions.jsonl:24` | U-5 (整类, 委托代裁) | |
| 42 | `ig34_p0200_a007` | 200 | §6.3.5.3 Cell Phenotype Findings (CP) | S1-R2 | S-SPC1 CP T-21 PDF_TYPO --GATEDEF→--GATDEF \| errata: t3_atom_err \| new_target: domains/C | `work/t3_fp_expected_regressions.jsonl:25` | U-5 (整类, 委托代裁) | |
| 43 | `ig34_p0205_a005` | 205 | §6.3.5.3 Cell Phenotype Findings (CP) | K3b-registry | S-SPC1 CP T-16b | `-` | U-5 (整类, 委托代裁) | |
| 44 | `ig34_p0206_a001` | 206 | §6.3.5.3 Cell Phenotype Findings (CP) | S1-R2 | S-SPC1 CP T-21 PDF_TYPO CPBNDAGT→CPBDAGNT \| errata: t3_atom_err \| new_target: domains/CP | `work/t3_fp_expected_regressions.jsonl:26` | U-5 (整类, 委托代裁) | |
| 45 | `ig34_p0206_a003` | 206 | §6.3.5.3 Cell Phenotype Findings (CP) | S1-R2 | S-SPC1 CP T-18 PDF_TYPO CSMRKS→CPCSMRKS \| errata: t3_atom_err \| new_target: domains/CP/a | `work/t3_fp_expected_regressions.jsonl:27` | U-5 (整类, 委托代裁) | |
| 46 | `ig34_p0206_a009` | 206 | §6.3.5.3 Cell Phenotype Findings (CP) | K3b-registry | S-SPC1 CP T-19 | `-` | U-5 (整类, 委托代裁) | |
| 47 | `ig34_p0211_a004` | 211 | §6.3.5.3 Cell Phenotype Findings (CP) | S1-R2 | B-CP T-15: verbatim CPGATEDEF 为 PDF 叙述笔误, KB 改 CPGATDEF (p202 spec) | `evidence/checkpoints/t2_B-CP.md:80` | U-5 (整类, 委托代裁) | |
| 48 | `ig34_p0212_a012` | 212 | §6.3.5.3 Cell Phenotype Findings (CP) | S1-R2 | B-CP T-15: verbatim CPGATEDEF 为 PDF 叙述笔误, KB 改 CPGATDEF (p202 spec) | `evidence/checkpoints/t2_B-CP.md:83` | U-5 (整类, 委托代裁) | |
| 49 | `ig34_p0213_a002` | 213 | §6.3.5.3 Cell Phenotype Findings (CP) | S1-R2 | B-CP T-15: verbatim CPGATEDEF 为 PDF 叙述笔误, KB 改 CPGATDEF (p202 spec) | `evidence/checkpoints/t2_B-CP.md:30` | U-5 (整类, 委托代裁) | |
| 50 | `ig34_p0213_a009` | 213 | §6.3.5.3 Cell Phenotype Findings (CP) | K3b-registry | B-CP T-6 | `-` | U-5 (整类, 委托代裁) | |
| 51 | `ig34_p0215_a017` | 215 | §6.3.5.3 Cell Phenotype Findings (CP) | writer-Tn-registry | B-CP T-3 (KB 写正确值) | `work/t2_batches/B-CP.writer.jsonl:34` | U-5 (整类, 委托代裁) | |
| 52 | `ig34_p0215_a018` | 215 | §6.3.5.3 Cell Phenotype Findings (CP) | S1-R2 | B-CP T-2: verbatim CPCSMRKR 为 PDF 笔误, KB 改 CPCSMRKS 后不命中 (预期) | `evidence/checkpoints/t2_B-CP.md:199` | U-5 (整类, 委托代裁) | |
| 53 | `ig34_p0217_a015` | 217 | §6.3.5.3 Cell Phenotype Findings (CP) | S1-R2 | B-CP T-15: verbatim CPGATEDEF 为 PDF 叙述笔误, KB 改 CPGATDEF (p202 spec) | `evidence/checkpoints/t2_B-CP.md:85` | U-5 (整类, 委托代裁) | |
| 54 | `ig34_p0218_a014` | 218 | §6.3.5.3 Cell Phenotype Findings (CP) | S1-R2 | B-CP T-15: verbatim CPGATEDEF 为 PDF 叙述笔误, KB 改 CPGATDEF (p202 spec) | `evidence/checkpoints/t2_B-CP.md:308` | U-5 (整类, 委托代裁) | |
| 55 | `ig34_p0218_a017` | 218 | §6.3.5.3 Cell Phenotype Findings (CP) | writer-Tn-registry | B-CP T-4 (KB 写正确值) | `work/t2_batches/B-CP.writer.jsonl:79` | U-5 (整类, 委托代裁) | |
| 56 | `ig34_p0220_a001` | 220 | §6.3.5.3 Cell Phenotype Findings (CP) | S1-R2 | B-CP T-15: verbatim CPGATEDEF 为 PDF 叙述笔误, KB 改 CPGATDEF (p202 spec) | `evidence/checkpoints/t2_B-CP.md:95` | U-5 (整类, 委托代裁) | |
| 57 | `ig34_p0224_a010` | 224 | §6.3.5.4 Genomics Findings (GF) | writer-Tn-registry | B-GF T-6 (KB 写正确值) | `work/t2_batches/B-GF.writer.jsonl:367` | U-5 (整类, 委托代裁) | |
| 58 | `ig34_p0224_a013` | 224 | §6.3.5.4 Genomics Findings (GF) | K3b-registry | B-GF T-1 | `-` | U-5 (整类, 委托代裁) | |
| 59 | `ig34_p0225_a019` | 225 | §6.3.5.4 Genomics Findings (GF) | writer-Tn-registry | B-GF T-3 (KB 写正确值) | `work/t2_batches/B-GF.writer.jsonl:361` | U-5 (整类, 委托代裁) | |
| 60 | `ig34_p0227_a018` | 227 | §6.3.5.4 Genomics Findings (GF) | K3b-registry | B-GF T-2 | `-` | U-5 (整类, 委托代裁) | |
| 61 | `ig34_p0228_a002` | 228 | §6.3.5.4 Genomics Findings (GF) | K3b-registry | B-GF T-5 | `-` | U-5 (整类, 委托代裁) | |
| 62 | `ig34_p0228_a009` | 228 | §6.3.5.4 Genomics Findings (GF) | K3b-registry | B-GF T-4 | `-` | U-5 (整类, 委托代裁) | |
| 63 | `ig34_p0236_a005` | 236 | §6.3.5.5 Immunogenicity Specimen Assessments (IS) | K3b-registry | B-IS T-3 | `-` | U-5 (整类, 委托代裁) | |
| 64 | `ig34_p0236_a014` | 236 | §6.3.5.5 Immunogenicity Specimen Assessments (IS) | K3b-registry | B-IS T-1, B-IS T-2 | `-` | U-5 (整类, 委托代裁) | |
| 65 | `ig34_p0236_a015` | 236 | §6.3.5.5 Immunogenicity Specimen Assessments (IS) | K3b-registry | B-IS T-1, B-IS T-2 | `-` | U-5 (整类, 委托代裁) | |
| 66 | `ig34_p0237_a018` | 237 | §6.3.5.5 Immunogenicity Specimen Assessments (IS) | writer-Tn-registry | B-IS T-5 (KB 写正确值) | `work/t2_batches/B-IS.writer.jsonl:118` | U-5 (整类, 委托代裁) | |
| 67 | `ig34_p0240_a004` | 240 | §6.3.5.5 Immunogenicity Specimen Assessments (IS) | S1-R2 | B-IS T-4 PDF_TYPO nucleoar→nucleolar; S-SPC1 D2 删 IS/assumptions 附录副本, 现在 IS/examples.md:2 | `work/t3_fp_expected_regressions.jsonl:30` | U-5 (整类, 委托代裁) | |
| 68 | `ig34_p0247_a020` | 247 | §6.3.5.6 Laboratory Test Results (LB) | K3b-registry | B-LB T-1 | `-` | U-5 (整类, 委托代裁) | |
| 69 | `ig34_p0257_a016` | 257 | §6.3.5.7.3 Microbiology Specimen/Microbiology Susc | S1-R2 | B-MS T-1: MSSTRESC PDF 空, KB 保留 25 | `evidence/checkpoints/t2_B-MS.md:115` | U-5 (整类, 委托代裁) | |
| 70 | `ig34_p0262_a020` | 262 | §6.3.5.7 Microbiology Domains | K3b-registry | B-MS T-2 | `-` | U-5 (整类, 委托代裁) | |
| 71 | `ig34_p0262_a029` | 262 | §6.3.5.7 Microbiology Domains | S1-R2 | B-MS T-3: verbatim IDVAR=MBREFID 为 PDF 笔误, KB 改 MSREFID | `evidence/checkpoints/t2_B-MS.md:133` | U-5 (整类, 委托代裁) | |
| 72 | `ig34_p0262_a030` | 262 | §6.3.5.7 Microbiology Domains | S1-R2 | B-MS T-3: verbatim IDVAR=MBREFID 为 PDF 笔误, KB 改 MSREFID | `evidence/checkpoints/t2_B-MS.md:62 (T-n 行; 原子 id 未出现在该文件)` | U-5 (整类, 委托代裁) | |
| 73 | `ig34_p0263_a020` | 263 | §6.3.5.7.3 Microbiology Specimen/Microbiology Susc | S1-R2 | B-MB T-3: verbatim MBTRESN 为 PDF 印刷错, KB 改 MBSTRESN 后不命中 (预期) | `evidence/checkpoints/t2_B-MB.md:145` | U-5 (整类, 委托代裁) | |
| 74 | `ig34_p0267_a006` | 267 | §6.3.5.8 Microscopic Findings (MI) | K3b-registry | B-MI T-1 | `-` | U-5 (整类, 委托代裁) | |
| 75 | `ig34_p0273_a037` | 273 | §6.3.5.9.2 Pharmacokinetics Parameters (PP) | K3b-registry | B-PCPP T-9 | `-` | U-5 (整类, 委托代裁) | |
| 76 | `ig34_p0274_a009` | 274 | §6.3.5.9.2 Pharmacokinetics Parameters (PP) | K3b-registry | B-PCPP T-5 | `-` | U-5 (整类, 委托代裁) | |
| 77 | `ig34_p0280_a036` | 280 | §6.3.5.9.3 Relating PP Records to PC Records | S1-R2 | T4 U-7 (委托代裁 2026-11-27) KB 写正确值, 原子 = PDF: A2-3 B-PCPP T-8b DYDRGX_HALF→DY1DRGX_HALF \| e | `work/t3_fp_expected_regressions.jsonl:66` | U-7 委托代裁 (§000), 非 U-5; B-PCPP T-8b: U-7 B (委托代裁 2026-11-27) [A2-3] | |
| 78 | `ig34_p0280_a039` | 280 | §6.3.5.9.3 Relating PP Records to PC Records — Exa | S1-R2 | T4 U-7 (委托代裁 2026-11-27) KB 写正确值, 原子 = PDF: A2-2 B-PCPP T-8 DYIDRGX_A→DY1DRGX_A \| errata: | `work/t3_fp_expected_regressions.jsonl:67` | U-7 委托代裁 (§000), 非 U-5; B-PCPP T-8: U-7 B (委托代裁 2026-11-27) [A2-2] | |
| 79 | `ig34_p0280_a040` | 280 | §6.3.5.9.3 Relating PP Records to PC Records — Exa | S1-R2 | T4 U-7 (委托代裁 2026-11-27) KB 写正确值, 原子 = PDF: A2-2 B-PCPP T-8 DYIDRGX_HALF→DY1DRGX_HALF \| e | `work/t3_fp_expected_regressions.jsonl:68` | U-7 委托代裁 (§000), 非 U-5; B-PCPP T-8: U-7 B (委托代裁 2026-11-27) [A2-2] | |
| 80 | `ig34_p0281_a002` | 281 | §6.3.5.9.3 Relating PP Records to PC Records — Exa | S1-R2 | T4 U-7 (委托代裁 2026-11-27) KB 写正确值, 原子 = PDF: A2-15 S-SPC2 N-1 PP→PC records with PCSEQ \| e | `work/t3_fp_expected_regressions.jsonl:69` | U-7 委托代裁 (§000), 非 U-5; S-SPC2 N-1: U-7 B (委托代裁 2026-11-27) [A2-15] | |
| 81 | `ig34_p0281_a003` | 281 | §6.3.5.9.3 Relating PP Records to PC Records — Exa | S1-R2 | T4 U-7 (委托代裁 2026-11-27) KB 写正确值, 原子 = PDF: A2-15 S-SPC2 N-1 PP→PC records with PCSEQ \| e | `work/t3_fp_expected_regressions.jsonl:70` | U-7 委托代裁 (§000), 非 U-5; S-SPC2 N-1: U-7 B (委托代裁 2026-11-27) [A2-15] | |
| 82 | `ig34_p0281_a031` | 281 | §6.3.5.9.3 Relating PP Records to PC Records — Exa | S1-R2 | T4 U-7 (委托代裁 2026-11-27) KB 写正确值, 原子 = PDF: A2-16 S-SPC2 N-2 PP/PGRPID→PC/PCGRPID \| errat | `work/t3_fp_expected_regressions.jsonl:71` | U-7 委托代裁 (§000), 非 U-5; S-SPC2 N-2: U-7 B (委托代裁 2026-11-27) [A2-16] | |
| 83 | `ig34_p0281_a032` | 281 | §6.3.5.9.3 Relating PP Records to PC Records — Exa | S1-R2 | T4 U-7 (委托代裁 2026-11-27) KB 写正确值, 原子 = PDF: A2-16 S-SPC2 N-2 PP/PGRPID→PC/PCGRPID \| errat | `work/t3_fp_expected_regressions.jsonl:72` | U-7 委托代裁 (§000), 非 U-5; S-SPC2 N-2: U-7 B (委托代裁 2026-11-27) [A2-16] | |
| 84 | `ig34_p0285_a015` | 285 | §6.3.7.1 Generic Morphology/Physiology Specificati | S1-R2 | T4 U-7 (委托代裁 2026-11-27) KB 写正确值, 原子 = PDF: A3-14 B-NV N-1 may included→include \| errata: | `work/t3_fp_expected_regressions.jsonl:77` | U-7 委托代裁 (§000), 非 U-5; B-NV N-1: U-7 B (委托代裁 2026-11-27) [A3-14] | |
| 85 | `ig34_p0293_a038` | 293 | §6.3.7.3 Musculoskeletal System Findings (MK) | K3b-registry | B-MK T-2 | `-` | U-5 (整类, 委托代裁) | |
| 86 | `ig34_p0296_a019` | 296 | §6.3.7.4 Nervous System Findings (NV) | writer-Tn-registry | B-NV T-1 (KB 写正确值) | `work/t2_batches/B-NV.writer.jsonl:11` | U-5 (整类, 委托代裁) | |
| 87 | `ig34_p0298_a001` | 298 | §6.3.7.4 Nervous System Findings (NV) | S1-R2 | T4 U-7 (委托代裁 2026-11-27) KB 写正确值, 原子 = PDF: A3-15 B-NV N-2 删 the \| errata: t3_atom_err \| | `work/t3_fp_expected_regressions.jsonl:80` | U-7 委托代裁 (§000), 非 U-5; B-NV N-2: U-7 B (委托代裁 2026-11-27) [A3-15] | |
| 88 | `ig34_p0304_a012` | 304 | §6.3.7.5 Ophthalmic Examinations (OE) | K3b-registry | B-OE T-1 | `-` | U-5 (整类, 委托代裁) | |
| 89 | `ig34_p0311_a035` | 311 | §6.3.7.7 Respiratory System Findings (RE) | S1-R2 | B-RE T-1: PDF 叙述 IREEA2 印刷错, KB 改 IRREA2 后不命中 (预期) | `evidence/checkpoints/t2_B-RE_review.md:83` | U-5 (整类, 委托代裁) | |
| 90 | `ig34_p0323_a006` | 323 | §6.3.9.1 Functional Tests (FT) — FT-Assumptions —  | K3b-registry | B-RS T-6 (FT 副本) | `-` | U-5 (整类, 委托代裁) | |
| 91 | `ig34_p0328_a007` | 328 | §6.3.9.2 Questionnaires (QS) — QS-Assumptions — QR | K3b-registry | B-RS T-6 (QS 副本) | `-` | U-5 (整类, 委托代裁) | |
| 92 | `ig34_p0332_a009` | 332 | §6.3.9.3.1 Disease Response Use Case | K3b-registry | B-RS T-2 | `-` | U-5 (整类, 委托代裁) | |
| 93 | `ig34_p0334_a011` | 334 | §6.3.9.3.1 Disease Response Use Case | S1-R2 | B-RS audit: verbatim 与 PDF 页文本不符 Rows 4-7 段被拆; KB 与页文本一致 [B-RS T-8] | `evidence/checkpoints/t2_B-RS_audit.md:17` | U-5 (整类, 委托代裁) | |
| 94 | `ig34_p0335_a015` | 335 | §6.3.9.3.1 Disease Response Use Case | S1-R2 | B-RS T-7 PDF_TYPO 叙述 RSPLNKGRP→RSLNKGRP \| errata: t3_atom_err \| new_target: domains/RS/e | `work/t3_fp_expected_regressions.jsonl:83` | U-5 (整类, 委托代裁) | |
| 95 | `ig34_p0335_a016` | 335 | §6.3.9.3.1 Disease Response Use Case | S1-R2 | B-RS T-7 PDF_TYPO 叙述 RSPLNKGRP→RSLNKGRP \| errata: t3_atom_err \| new_target: domains/RS/e | `work/t3_fp_expected_regressions.jsonl:84` | U-5 (整类, 委托代裁) | |
| 96 | `ig34_p0335_a017` | 335 | §6.3.9.3.1 Disease Response Use Case | S1-R2 | B-RS T-7 PDF_TYPO 叙述 RSPLNKGRP→RSLNKGRP \| errata: t3_atom_err \| new_target: domains/RS/e | `work/t3_fp_expected_regressions.jsonl:85` | U-5 (整类, 委托代裁) | |
| 97 | `ig34_p0335_a018` | 335 | §6.3.9.3.1 Disease Response Use Case | S1-R2 | B-RS T-7 PDF_TYPO 叙述 RSPLNKGRP→RSLNKGRP \| errata: t3_atom_err \| new_target: domains/RS/e | `work/t3_fp_expected_regressions.jsonl:86` | U-5 (整类, 委托代裁) | |
| 98 | `ig34_p0336_a005` | 336 | §6.3.9.3.1 Disease Response Use Case | K3b-registry | B-RS T-1 | `-` | U-5 (整类, 委托代裁) | |
| 99 | `ig34_p0338_a006` | 338 | §6.3.9.3.2 Clinical Classifications Use Case | S1-R2 | [K4 改判] 原子 = PDF (norm ⊂ p337-339); KB 有登记偏离 B-RS T-5 (RS 副本): PDF 'providing an resolutio | `evidence/checkpoints/t2_B-RS_audit.md:14 (页级行; 该批以范围/页号记这组原子)` | U-5 (整类, 委托代裁) | |
| 100 | `ig34_p0342_a006` | 342 | SC – Examples | K3b-registry | B-SC T-1 | `-` | U-8 委托代裁 (§000), 非 U-5 | |
| 101 | `ig34_p0342_a007` | 342 | SC – Examples | K3b-registry | B-SC T-1 | `-` | U-8 委托代裁 (§000), 非 U-5 | |
| 102 | `ig34_p0353_a009` | 353 | §6.3.12.3 Tumor Identification/Tumor Results Examp | K3b-registry | B-TU T-1 | `-` | U-5 (整类, 委托代裁) | |
| 103 | `ig34_p0355_a014` | 355 | §6.3.12.3 Tumor Identification/Tumor Results Examp | writer-Tn-registry | B-TR T-1 (KB 写正确值) | `work/t2_batches/B-TR.writer.jsonl:4` | U-5 (整类, 委托代裁) | |
| 104 | `ig34_p0355_a015` | 355 | §6.3.12.3 Tumor Identification/Tumor Results Examp | writer-Tn-registry | B-TR T-1 (KB 写正确值) | `work/t2_batches/B-TR.writer.jsonl:5` | U-5 (整类, 委托代裁) | |
| 105 | `ig34_p0355_a016` | 355 | §6.3.12.3 Tumor Identification/Tumor Results Examp | writer-Tn-registry | B-TR T-1 (KB 写正确值) | `work/t2_batches/B-TR.writer.jsonl:6` | U-5 (整类, 委托代裁) | |
| 106 | `ig34_p0355_a017` | 355 | §6.3.12.3 Tumor Identification/Tumor Results Examp | writer-Tn-registry | B-TR T-1 (KB 写正确值) | `work/t2_batches/B-TR.writer.jsonl:7` | U-5 (整类, 委托代裁) | |
| 107 | `ig34_p0355_a018` | 355 | §6.3.12.3 Tumor Identification/Tumor Results Examp | writer-Tn-registry | B-TR T-1 (KB 写正确值) | `work/t2_batches/B-TR.writer.jsonl:8` | U-5 (整类, 委托代裁) | |
| 108 | `ig34_p0355_a019` | 355 | §6.3.12.3 Tumor Identification/Tumor Results Examp | writer-Tn-registry | B-TR T-1 (KB 写正确值) | `work/t2_batches/B-TR.writer.jsonl:9` | U-5 (整类, 委托代裁) | |
| 109 | `ig34_p0355_a020` | 355 | §6.3.12.3 Tumor Identification/Tumor Results Examp | writer-Tn-registry | B-TR T-1 (KB 写正确值) | `work/t2_batches/B-TR.writer.jsonl:10` | U-5 (整类, 委托代裁) | |
| 110 | `ig34_p0355_a021` | 355 | §6.3.12.3 Tumor Identification/Tumor Results Examp | writer-Tn-registry | B-TR T-1 (KB 写正确值) | `work/t2_batches/B-TR.writer.jsonl:11` | U-5 (整类, 委托代裁) | |
| 111 | `ig34_p0355_a022` | 355 | §6.3.12.3 Tumor Identification/Tumor Results Examp | writer-Tn-registry | B-TR T-1 (KB 写正确值) | `work/t2_batches/B-TR.writer.jsonl:12` | U-5 (整类, 委托代裁) | |
| 112 | `ig34_p0355_a023` | 355 | §6.3.12.3 Tumor Identification/Tumor Results Examp | writer-Tn-registry | B-TR T-1 (KB 写正确值) | `work/t2_batches/B-TR.writer.jsonl:13` | U-5 (整类, 委托代裁) | |
| 113 | `ig34_p0355_a024` | 355 | §6.3.12.3 Tumor Identification/Tumor Results Examp | writer-Tn-registry | B-TR T-1 (KB 写正确值) | `work/t2_batches/B-TR.writer.jsonl:14` | U-5 (整类, 委托代裁) | |
| 114 | `ig34_p0355_a025` | 355 | §6.3.12.3 Tumor Identification/Tumor Results Examp | writer-Tn-registry | B-TR T-1 (KB 写正确值) | `work/t2_batches/B-TR.writer.jsonl:15` | U-5 (整类, 委托代裁) | |
| 115 | `ig34_p0355_a026` | 355 | §6.3.12.3 Tumor Identification/Tumor Results Examp | writer-Tn-registry | B-TR T-1 (KB 写正确值) | `work/t2_batches/B-TR.writer.jsonl:16` | U-5 (整类, 委托代裁) | |
| 116 | `ig34_p0355_a027` | 355 | §6.3.12.3 Tumor Identification/Tumor Results Examp | writer-Tn-registry | B-TR T-3 (KB 写正确值) | `work/t2_batches/B-TR.writer.jsonl:17` | U-5 (整类, 委托代裁) | |
| 117 | `ig34_p0356_a001` | 356 | §6.3.12.3 Tumor Identification/Tumor Results Examp | K3b-registry | B-TR T-3 | `-` | U-5 (整类, 委托代裁) | |
| 118 | `ig34_p0356_a002` | 356 | §6.3.12.3 Tumor Identification/Tumor Results Examp | writer-Tn-registry | B-TR T-1 (KB 写正确值) | `work/t2_batches/B-TR.writer.jsonl:19` | U-5 (整类, 委托代裁) | |
| 119 | `ig34_p0362_a010` | 362 | §6.4.1 When to Use Findings About Events or Interv | S1-R2 | T4 U-7 后依据变更: KB 按 U-7 A3-7 写正确值 'thought to be related' (= 原子), PDF p362 'thought be rela [B-FA T-4] | `evidence/checkpoints/t2_B-FA_audit.md:36` | 主控决定 M-4 (§000b; 非委托代裁, 待主人追认); 登记 B-FA T-4 本身 = U-7 A3-7 | |
| 120 | `ig34_p0363_a008` | 363 | §6.4.1 When to Use Findings About Events or Interv | writer-Tn-registry | B-FA T-5 (KB 写正确值) | `work/t2_batches/B-FA.writer.jsonl:22` | U-5 (整类, 委托代裁) | |
| 121 | `ig34_p0363_a009` | 363 | §6.4.1 When to Use Findings About Events or Interv | K3b-registry | B-FA T-6 | `-` | U-7 委托代裁 (§000), 非 U-5; B-FA T-6: U-7 B (委托代裁 2026-11-27) [A3-8] | |
| 122 | `ig34_p0370_a021` | 370 | FA – Examples | S1-R2 | B-FA T-7: PDF parent CE record → KB AE | `evidence/checkpoints/t2_B-FA.md:129` | U-5 (整类, 委托代裁) | |
| 123 | `ig34_p0372_a013` | 372 | FA – Examples | S1-R2 | T4 U-7 (委托代裁 2026-11-27) KB 写正确值, 原子 = PDF: A3-9 B-FA T-8 populated→populate \| errata: t3 | `work/t3_fp_expected_regressions.jsonl:113` | U-7 委托代裁 (§000), 非 U-5; B-FA T-8: U-7 B (委托代裁 2026-11-27) [A3-9] | |
| 124 | `ig34_p0373_a013` | 373 | FA – Examples | S1-R2 | B-FA T-9: FAEVINTX → FAEVLINT | `evidence/checkpoints/t2_B-FA.md:129` | U-5 (整类, 委托代裁) | |
| 125 | `ig34_p0377_a015` | 377 | SR – Specification | S1-R2 | B-SR T-4: verbatim EGTPTREF 为 PDF 笔误, KB 改 SRTPTREF | `evidence/checkpoints/t2_B-SR.md:116` | U-5 (整类, 委托代裁) | |
| 126 | `ig34_p0377_a021` | 377 | SR – Assumptions | K3b-registry | B-SR T-3 | `-` | U-5 (整类, 委托代裁) | |
| 127 | `ig34_p0378_a017` | 378 | SR – Examples | K3b-registry | B-SR T-1 (examples) | `-` | U-5 (整类, 委托代裁) | |
| 128 | `ig34_p0412_a006` | 412 | §7.3.2 Trial Disease Assessments (TD) – Examples | K3b-registry | S-TDM TD T-1 | `-` | U-5 (整类, 委托代裁) | |
| 129 | `ig34_p0412_a007` | 412 | §7.3.2 Trial Disease Assessments (TD) – Examples | K3b-registry | S-TDM TD T-1 | `-` | U-5 (整类, 委托代裁) | |
| 130 | `ig34_p0412_a008` | 412 | §7.3.2 Trial Disease Assessments (TD) – Examples | K3b-registry | S-TDM TD T-1 | `-` | U-5 (整类, 委托代裁) | |
| 131 | `ig34_p0412_a009` | 412 | §7.3.2 Trial Disease Assessments (TD) – Examples | writer-Tn-registry | S-TDM TD T-1 (KB 写正确值) | `work/t2_batches/S-TDM.writer.jsonl:18` | U-5 (整类, 委托代裁) | |
| 132 | `ig34_p0413_a010` | 413 | §7.3.2 Trial Disease Assessments (TD) – Examples | K3b-registry | S-TDM TD T-4 | `-` | U-5 (整类, 委托代裁) | |
| 133 | `ig34_p0414_a006` | 414 | §7.3.2 Trial Disease Assessments (TD) – Examples | writer-Tn-registry | S-TDM TD T-2 (KB 写正确值) | `work/t2_batches/S-TDM.writer.jsonl:25` | U-5 (整类, 委托代裁) | |
| 134 | `ig34_p0414_a008` | 414 | §7.3.2 Trial Disease Assessments (TD) – Examples | writer-Tn-registry | S-TDM TD T-3 (KB 写正确值) | `work/t2_batches/S-TDM.writer.jsonl:26` | U-5 (整类, 委托代裁) | |
| 135 | `ig34_p0414_a013` | 414 | §7.3.2 Trial Disease Assessments (TD) – Examples | K3b-registry | S-TDM TD T-4 | `-` | U-5 (整类, 委托代裁) | |
| 136 | `ig34_p0419_a006` | 419 | §7.4.2 Trial Summary (TS) – Assumptions | S1-R2 | T4 U-7 (委托代裁 2026-11-27) KB 写正确值, 原子 = PDF: A2-5 B-TS T-3 DOSFREQ→DOSFRQ (+A2-4 B-TS T-2 D [B-TS T-3, B-TS T-2] | `work/t3_fp_expected_regressions.jsonl:117` | U-7 委托代裁 (§000), 非 U-5; B-TS T-3: U-7 B (委托代裁 2026-11-27) [A2-5]; B-TS T-2: U-7 B (委托代裁 2026-11-27) [A2-4] | |
| 137 | `ig34_p0419_a011` | 419 | §7.4.2 Trial Summary (TS) – Assumptions | S1-R2 | T4 U-7 (委托代裁 2026-11-27) KB 写正确值, 原子 = PDF: A2-5 B-TS T-3 DOSFREQ→DOSFRQ \| errata: t3_ato | `work/t3_fp_expected_regressions.jsonl:118` | U-7 委托代裁 (§000), 非 U-5; B-TS T-3: U-7 B (委托代裁 2026-11-27) [A2-5] | |
| 138 | `ig34_p0419_a013` | 419 | §7.4.2 Trial Summary (TS) – Assumptions | S1-R2 | T4 U-7 (委托代裁 2026-11-27) KB 写正确值, 原子 = PDF: A2-5 B-TS T-3 DOSFREQ→DOSFRQ \| errata: t3_ato | `work/t3_fp_expected_regressions.jsonl:119` | U-7 委托代裁 (§000), 非 U-5; B-TS T-3: U-7 B (委托代裁 2026-11-27) [A2-5] | |
| 139 | `ig34_p0419_a017` | 419 | §7.4.2 Trial Summary (TS) – Assumptions | S1-R2 | T4 U-7 (委托代裁 2026-11-27) KB 写正确值, 原子 = PDF: A2-6 B-TS T-4 OUTMSPR→OUTMSPRI \| errata: t3_a | `work/t3_fp_expected_regressions.jsonl:120` | U-7 委托代裁 (§000), 非 U-5; B-TS T-4: U-7 B (委托代裁 2026-11-27) [A2-6] | |
| 140 | `ig34_p0425_a024` | 425 | §7.4.2.1 Use of Null Flavor | S1-R2 | T4 U-7 (委托代裁 2026-11-27) KB 写正确值, 原子 = PDF: A2-7 B-TS T-6 MAXAGE→AGEMAX \| errata: t3_atom | `work/t3_fp_expected_regressions.jsonl:121` | U-7 委托代裁 (§000), 非 U-5; B-TS T-6: U-7 B (委托代裁 2026-11-27) [A2-7] | |
| 141 | `ig34_p0427_a011` | 427 | §8 [REPRESENTING RELATIONSHIPS AND DATA] | K3b-registry | B-ch08 T-1 | `-` | U-5 (整类, 委托代裁) | |
| 142 | `ig34_p0428_a006` | 428 | §8.1.1 --GRPID Example | K3b-registry | B-ch08 T-2 | `-` | U-5 (整类, 委托代裁) | |
| 143 | `ig34_p0428_a008` | 428 | §8.1.1 --GRPID Example | K3b-registry | B-ch08 T-2 | `-` | U-5 (整类, 委托代裁) | |
| 144 | `ig34_p0433_a017` | 433 | §8.4.2 Submitting Supplemental Qualifiers in Separ | writer-Tn-registry | B-ch08 T-3 (KB 写正确值) | `work/t2_batches/B-ch08.writer.jsonl:65` | U-5 (整类, 委托代裁) | |
| 145 | `ig34_p0433_a019` | 433 | §8.4.3 SUPP-- Examples | K3b-registry | B-ch08 T-4 | `-` | U-5 (整类, 委托代裁) | |
| 146 | `ig34_p0436_a022` | 436 | §8.6.3 Guidelines for Differentiating Between Inte | writer-Tn-registry | B-ch08 T-6 (KB 写正确值) | `work/t2_batches/B-ch08.writer.jsonl:60` | U-5 (整类, 委托代裁) | |
| 147 | `ig34_p0438_a019` | 438 | RELSUB – Assumptions | K3b-registry | B-REL T-9 (RELSUB 副本), B-ch08 T-9 (ch08 副本) | `-` | U-5 (整类, 委托代裁) | |
| 148 | `ig34_p0457_a004` | 457 | §10.E Appendix E: Revision History | K3b-registry | S-CH10 T-2 | `-` | U-5 (整类, 委托代裁) | |
| 149 | `sv20_p0006_a020` | 6 | §1.4 Significant Changes from Prior Versions | writer-Tn-registry | B-model01 T-1 (KB 写正确值) | `work/t2_batches/B-model01.writer.jsonl:82` | U-5 (整类, 委托代裁) | |

## FIGURE_DEFERRED (11)

| # | atom_id | 页 | 节 | 规则 | 依据 / 登记 | 出处 | 决定来源 | 异议 |
|--:|---|--:|---|---|---|---|---|---|
| 1 | `ig34_p0044_a023` | 44 | §4.4.7 [Use of Relative Timing Variables] | FIGURE | knowledge_base/chapters/ch04_general_assumptions.md:933 | `-` | U-5 (整类, 委托代裁) | |
| 2 | `ig34_p0387_a011` | 387 | §7.2.1 Trial Arms (TA) – Example 1 | FIGURE | knowledge_base/domains/TA/examples.md:32 | `-` | U-5 (整类, 委托代裁) | |
| 3 | `ig34_p0388_a001` | 388 | §7.2.1 Trial Arms (TA) – Example 1 | FIGURE | knowledge_base/domains/TA/examples.md:47 | `-` | U-5 (整类, 委托代裁) | |
| 4 | `ig34_p0388_a003` | 388 | §7.2.1 Trial Arms (TA) – Example 1 | FIGURE | knowledge_base/domains/TA/examples.md:68 | `-` | U-5 (整类, 委托代裁) | |
| 5 | `ig34_p0388_a005` | 388 | §7.2.1 Trial Arms (TA) – Example 1 | FIGURE | knowledge_base/domains/TA/examples.md:92 | `-` | U-5 (整类, 委托代裁) | |
| 6 | `ig34_p0397_a005` | 397 | §7.2.1 Trial Arms (TA) – Example 5 | FIGURE | knowledge_base/domains/TA/examples.md:500 | `-` | U-5 (整类, 委托代裁) | |
| 7 | `ig34_p0397_a009` | 397 | §7.2.1 Trial Arms (TA) – Example 5 | FIGURE | knowledge_base/domains/TA/examples.md:516 | `-` | U-5 (整类, 委托代裁) | |
| 8 | `ig34_p0398_a012` | 398 | §7.2.1 Trial Arms (TA) – Example 6 | FIGURE | knowledge_base/domains/TA/examples.md:570 | `-` | U-5 (整类, 委托代裁) | |
| 9 | `ig34_p0398_a016` | 398 | §7.2.1 Trial Arms (TA) – Example 6 | FIGURE | knowledge_base/domains/TA/examples.md:586 | `-` | U-5 (整类, 委托代裁) | |
| 10 | `ig34_p0409_a007` | 409 | §7.3.1 Trial Visits (TV) – Example 1 | FIGURE | knowledge_base/domains/TV/examples.md:9 | `-` | U-5 (整类, 委托代裁) | |
| 11 | `ig34_p0440_a009` | 440 | RELSPEC – Examples | FIGURE | knowledge_base/domains/RELSPEC/examples.md:9 | `-` | U-5 (整类, 委托代裁) | |

