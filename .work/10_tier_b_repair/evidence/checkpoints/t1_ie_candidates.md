# T1.4 IE 候选清单 (IE_CAND) — 待用户逐类 ack

<!-- chain: E (plans) -->
> 状态: 待用户 ack (T1.4 hard checkpoint); 生成: `scripts/helpers/t14_pkg.py` (2026-11-26) 读 `work/triage_merged.json`
> (`python3 -I .work/10_tier_b_repair/scripts/t1_merge.py` 复跑后与复跑前逐字节相同). 只列 ID / 节 / KB 位置, 不含 PDF 原文.

总计 **587** 条. 列: `det` = 确定性支撑 (SPEC_MATCH + section_domain 比对一致); `rev` = T1.3 reviewer 已复核;
`extra` = 在 `t1_extra_review_set.json` (非确定性支撑且未复核, 追加 100% 复核中); `src` = writer / reviewer (覆盖) / pending_user.

| ie_cat | 条数 | det | rev | extra |
|---|--:|--:|--:|--:|
| SPEC_TABLE_ROW | 418 | 415 | 87 | 3 |
| VERSION_MISMATCH | 70 | 0 | 15 | 55 |
| CODE_LITERAL_IE | 50 | 0 | 9 | 41 |
| SPEC_TABLE_HEADER | 24 | 0 | 7 | 17 |
| EDITORIAL_META | 14 | 0 | 2 | 12 |
| REDUNDANT_WITH_SPEC | 11 | 0 | 2 | 9 |

待裁定 (T1.4, 不在本文件内裁): VERSION_MISMATCH 口径 — lane A 23 条 sv20 §1 / lane C 24 条 sv20 (model/05/06 收了 5 列版本) /
lane D pack_032 SE/SJ 23 表行 vs pack_027 口径相反; 不认 → 对应条转 REAL_GAP 或 LOCATE (见 `t1_lane_notes.md`).
`ig34_p0195_a008` reviewer 覆盖 LOCATE→IE_CAND, merge 未取到 ie_cat, 按 reviewer 说明归 SPEC_TABLE_HEADER.

## SPEC_TABLE_ROW (418)

| atom_id | 节 | kb_loc | det | rev | extra | src |
|---|---|---|:-:|:-:|:-:|---|
| ig34_p0063_a019 | §5.2 [Demographics (DM)] | knowledge_base/domains/DM/spec.md:185 | Y |  |  | writer |
| ig34_p0063_a021 | §5.2 [Demographics (DM)] | knowledge_base/domains/DM/spec.md:194 | Y |  |  | writer |
| ig34_p0063_a023 | §5.2 [Demographics (DM)] | knowledge_base/domains/DM/spec.md:203 | Y | Y |  | writer |
| ig34_p0063_a025 | §5.2 [Demographics (DM)] | knowledge_base/domains/DM/spec.md:212 | Y |  |  | writer |
| ig34_p0064_a002 | §5.2 [Demographics (DM)] | knowledge_base/domains/DM/spec.md:221 | Y | Y |  | writer |
| ig34_p0064_a003 | §5.2 [Demographics (DM)] | knowledge_base/domains/DM/spec.md:230 | Y |  |  | writer |
| ig34_p0064_a004 | §5.2 [Demographics (DM)] | knowledge_base/domains/DM/spec.md:239 | Y |  |  | writer |
| ig34_p0064_a005 | §5.2 [Demographics (DM)] | knowledge_base/domains/DM/spec.md:248 | Y |  |  | writer |
| ig34_p0064_a007 | §5.2 [Demographics (DM)] | knowledge_base/domains/DM/spec.md:257 | Y |  |  | writer |
| ig34_p0064_a008 | §5.2 [Demographics (DM)] | knowledge_base/domains/DM/spec.md:266 | Y | Y |  | writer |
| ig34_p0064_a009 | §5.2 [Demographics (DM)] | knowledge_base/domains/DM/spec.md:275 | Y |  |  | writer |
| ig34_p0064_a010 | §5.2 [Demographics (DM)] | knowledge_base/domains/DM/spec.md:284 | Y |  |  | writer |
| ig34_p0079_a018 | §5.3 [Subject Elements] | knowledge_base/domains/SE/spec.md:32 |  |  | Y | writer |
| ig34_p0080_a001 | §5.3 [Subject Elements] | knowledge_base/domains/SE/spec.md:41 |  |  | Y | writer |
| ig34_p0080_a007 | §5.3 [Subject Elements] | knowledge_base/domains/SE/spec.md:95 |  |  | Y | writer |
| ig34_p0084_a008 | §5.4 [Subject Disease Milestones (SM)] | knowledge_base/domains/SM/spec.md:5 | Y | Y |  | writer |
| ig34_p0084_a009 | §5.4 [Subject Disease Milestones (SM)] | knowledge_base/domains/SM/spec.md:14 | Y |  |  | writer |
| ig34_p0084_a010 | §5.4 [Subject Disease Milestones (SM)] | knowledge_base/domains/SM/spec.md:23 | Y | Y |  | writer |
| ig34_p0084_a011 | §5.4 [Subject Disease Milestones (SM)] | knowledge_base/domains/SM/spec.md:32 | Y |  |  | writer |
| ig34_p0084_a012 | §5.4 [Subject Disease Milestones (SM)] | knowledge_base/domains/SM/spec.md:41 | Y |  |  | writer |
| ig34_p0084_a013 | §5.4 [Subject Disease Milestones (SM)] | knowledge_base/domains/SM/spec.md:50 | Y |  |  | writer |
| ig34_p0084_a014 | §5.4 [Subject Disease Milestones (SM)] | knowledge_base/domains/SM/spec.md:59 | Y |  |  | writer |
| ig34_p0084_a015 | §5.4 [Subject Disease Milestones (SM)] | knowledge_base/domains/SM/spec.md:68 | Y |  |  | writer |
| ig34_p0084_a016 | §5.4 [Subject Disease Milestones (SM)] | knowledge_base/domains/SM/spec.md:77 | Y |  |  | writer |
| ig34_p0084_a017 | §5.4 [Subject Disease Milestones (SM)] | knowledge_base/domains/SM/spec.md:86 | Y | Y |  | writer |
| ig34_p0121_a007 | §6.1.4 [Meal Data (ML)] | knowledge_base/domains/ML/spec.md:5 | Y | Y |  | writer |
| ig34_p0121_a008 | §6.1.4 [Meal Data (ML)] | knowledge_base/domains/ML/spec.md:14 | Y |  |  | writer |
| ig34_p0121_a009 | §6.1.4 [Meal Data (ML)] | knowledge_base/domains/ML/spec.md:23 | Y | Y |  | writer |
| ig34_p0121_a010 | §6.1.4 [Meal Data (ML)] | knowledge_base/domains/ML/spec.md:32 | Y |  |  | writer |
| ig34_p0121_a012 | §6.1.4 [Meal Data (ML)] | knowledge_base/domains/ML/spec.md:50 | Y |  |  | writer |
| ig34_p0121_a013 | §6.1.4 [Meal Data (ML)] | knowledge_base/domains/ML/spec.md:59 | Y |  |  | writer |
| ig34_p0121_a014 | §6.1.4 [Meal Data (ML)] | knowledge_base/domains/ML/spec.md:68 | Y |  |  | writer |
| ig34_p0121_a015 | §6.1.4 [Meal Data (ML)] | knowledge_base/domains/ML/spec.md:77 | Y | Y |  | writer |
| ig34_p0121_a016 | §6.1.4 [Meal Data (ML)] | knowledge_base/domains/ML/spec.md:86 | Y |  |  | writer |
| ig34_p0121_a017 | §6.1.4 [Meal Data (ML)] | knowledge_base/domains/ML/spec.md:95 | Y |  |  | writer |
| ig34_p0121_a018 | §6.1.4 [Meal Data (ML)] | knowledge_base/domains/ML/spec.md:104 | Y |  |  | writer |
| ig34_p0121_a019 | §6.1.4 [Meal Data (ML)] | knowledge_base/domains/ML/spec.md:113 | Y |  |  | writer |
| ig34_p0121_a020 | §6.1.4 [Meal Data (ML)] | knowledge_base/domains/ML/spec.md:122 | Y |  |  | writer |
| ig34_p0121_a021 | §6.1.4 [Meal Data (ML)] | knowledge_base/domains/ML/spec.md:131 | Y |  |  | writer |
| ig34_p0121_a022 | §6.1.4 [Meal Data (ML)] | knowledge_base/domains/ML/spec.md:140 | Y |  |  | writer |
| ig34_p0121_a023 | §6.1.4 [Meal Data (ML)] | knowledge_base/domains/ML/spec.md:149 | Y |  |  | writer |
| ig34_p0121_a024 | §6.1.4 [Meal Data (ML)] | knowledge_base/domains/ML/spec.md:158 | Y |  |  | writer |
| ig34_p0121_a025 | §6.1.4 [Meal Data (ML)] | knowledge_base/domains/ML/spec.md:167 | Y |  |  | writer |
| ig34_p0121_a026 | §6.1.4 [Meal Data (ML)] | knowledge_base/domains/ML/spec.md:176 | Y |  |  | writer |
| ig34_p0121_a027 | §6.1.4 [Meal Data (ML)] | knowledge_base/domains/ML/spec.md:185 | Y | Y |  | writer |
| ig34_p0121_a028 | §6.1.4 [Meal Data (ML)] | knowledge_base/domains/ML/spec.md:194 | Y |  |  | writer |
| ig34_p0121_a029 | §6.1.4 [Meal Data (ML)] | knowledge_base/domains/ML/spec.md:203 | Y |  |  | writer |
| ig34_p0122_a001 | §6.1.4 [Meal Data (ML)] | knowledge_base/domains/ML/spec.md:212 | Y |  |  | writer |
| ig34_p0122_a002 | §6.1.4 [Meal Data (ML)] | knowledge_base/domains/ML/spec.md:221 | Y |  |  | writer |
| ig34_p0122_a003 | §6.1.4 [Meal Data (ML)] | knowledge_base/domains/ML/spec.md:230 | Y |  |  | writer |
| ig34_p0122_a004 | §6.1.4 [Meal Data (ML)] | knowledge_base/domains/ML/spec.md:239 | Y |  |  | writer |
| ig34_p0122_a005 | §6.1.4 [Meal Data (ML)] | knowledge_base/domains/ML/spec.md:248 | Y |  |  | writer |
| ig34_p0122_a006 | §6.1.4 [Meal Data (ML)] | knowledge_base/domains/ML/spec.md:257 | Y | Y |  | writer |
| ig34_p0122_a007 | §6.1.4 [Meal Data (ML)] | knowledge_base/domains/ML/spec.md:266 | Y |  |  | writer |
| ig34_p0122_a008 | §6.1.4 [Meal Data (ML)] | knowledge_base/domains/ML/spec.md:275 | Y |  |  | writer |
| ig34_p0122_a009 | §6.1.4 [Meal Data (ML)] | knowledge_base/domains/ML/spec.md:284 | Y |  |  | writer |
| ig34_p0122_a012 | §6.1.4 [Meal Data (ML)] | knowledge_base/domains/ML/spec.md:311 | Y | Y |  | writer |
| ig34_p0122_a013 | §6.1.4 [Meal Data (ML)] | knowledge_base/domains/ML/spec.md:320 | Y | Y |  | writer |
| ig34_p0122_a014 | §6.1.4 [Meal Data (ML)] | knowledge_base/domains/ML/spec.md:329 | Y | Y |  | writer |
| ig34_p0134_a004 | §6.2.1 [Adverse Events (AE)] | knowledge_base/domains/AE/spec.md:5 | Y |  |  | writer |
| ig34_p0134_a005 | §6.2.1 [Adverse Events (AE)] | knowledge_base/domains/AE/spec.md:14 | Y |  |  | writer |
| ig34_p0134_a006 | §6.2.1 [Adverse Events (AE)] | knowledge_base/domains/AE/spec.md:23 | Y |  |  | writer |
| ig34_p0134_a007 | §6.2.1 [Adverse Events (AE)] | knowledge_base/domains/AE/spec.md:32 | Y |  |  | writer |
| ig34_p0134_a008 | §6.2.1 [Adverse Events (AE)] | knowledge_base/domains/AE/spec.md:41 | Y |  |  | writer |
| ig34_p0134_a009 | §6.2.1 [Adverse Events (AE)] | knowledge_base/domains/AE/spec.md:50 | Y |  |  | writer |
| ig34_p0134_a010 | §6.2.1 [Adverse Events (AE)] | knowledge_base/domains/AE/spec.md:59 | Y | Y |  | writer |
| ig34_p0134_a011 | §6.2.1 [Adverse Events (AE)] | knowledge_base/domains/AE/spec.md:68 | Y |  |  | writer |
| ig34_p0134_a012 | §6.2.1 [Adverse Events (AE)] | knowledge_base/domains/AE/spec.md:77 | Y |  |  | writer |
| ig34_p0134_a013 | §6.2.1 [Adverse Events (AE)] | knowledge_base/domains/AE/spec.md:86 | Y | Y |  | writer |
| ig34_p0134_a014 | §6.2.1 [Adverse Events (AE)] | knowledge_base/domains/AE/spec.md:95 | Y |  |  | writer |
| ig34_p0134_a015 | §6.2.1 [Adverse Events (AE)] | knowledge_base/domains/AE/spec.md:104 | Y | Y |  | writer |
| ig34_p0134_a016 | §6.2.1 [Adverse Events (AE)] | knowledge_base/domains/AE/spec.md:113 | Y |  |  | writer |
| ig34_p0134_a017 | §6.2.1 [Adverse Events (AE)] | knowledge_base/domains/AE/spec.md:122 | Y |  |  | writer |
| ig34_p0134_a018 | §6.2.1 [Adverse Events (AE)] | knowledge_base/domains/AE/spec.md:131 | Y |  |  | writer |
| ig34_p0134_a019 | §6.2.1 [Adverse Events (AE)] | knowledge_base/domains/AE/spec.md:140 | Y |  |  | writer |
| ig34_p0134_a020 | §6.2.1 [Adverse Events (AE)] | knowledge_base/domains/AE/spec.md:149 | Y | Y |  | writer |
| ig34_p0134_a021 | §6.2.1 [Adverse Events (AE)] | knowledge_base/domains/AE/spec.md:158 | Y |  |  | writer |
| ig34_p0134_a022 | §6.2.1 [Adverse Events (AE)] | knowledge_base/domains/AE/spec.md:167 | Y | Y |  | writer |
| ig34_p0134_a023 | §6.2.1 [Adverse Events (AE)] | knowledge_base/domains/AE/spec.md:176 | Y |  |  | writer |
| ig34_p0134_a024 | §6.2.1 [Adverse Events (AE)] | knowledge_base/domains/AE/spec.md:185 | Y | Y |  | writer |
| ig34_p0134_a025 | §6.2.1 [Adverse Events (AE)] | knowledge_base/domains/AE/spec.md:194 | Y |  |  | writer |
| ig34_p0135_a002 | §6.2.1 [Adverse Events (AE)] | knowledge_base/domains/AE/spec.md:203 | Y |  |  | writer |
| ig34_p0135_a003 | §6.2.1 [Adverse Events (AE)] | knowledge_base/domains/AE/spec.md:212 | Y |  |  | writer |
| ig34_p0135_a004 | §6.2.1 [Adverse Events (AE)] | knowledge_base/domains/AE/spec.md:221 | Y |  |  | writer |
| ig34_p0135_a005 | §6.2.1 [Adverse Events (AE)] | knowledge_base/domains/AE/spec.md:230 | Y |  |  | writer |
| ig34_p0135_a006 | §6.2.1 [Adverse Events (AE)] | knowledge_base/domains/AE/spec.md:239 | Y |  |  | writer |
| ig34_p0135_a007 | §6.2.1 [Adverse Events (AE)] | knowledge_base/domains/AE/spec.md:248 | Y |  |  | writer |
| ig34_p0135_a008 | §6.2.1 [Adverse Events (AE)] | knowledge_base/domains/AE/spec.md:257 | Y |  |  | writer |
| ig34_p0135_a009 | §6.2.1 [Adverse Events (AE)] | knowledge_base/domains/AE/spec.md:266 | Y |  |  | writer |
| ig34_p0135_a010 | §6.2.1 [Adverse Events (AE)] | knowledge_base/domains/AE/spec.md:275 | Y | Y |  | writer |
| ig34_p0135_a011 | §6.2.1 [Adverse Events (AE)] | knowledge_base/domains/AE/spec.md:284 | Y |  |  | writer |
| ig34_p0135_a012 | §6.2.1 [Adverse Events (AE)] | knowledge_base/domains/AE/spec.md:293 | Y |  |  | writer |
| ig34_p0135_a013 | §6.2.1 [Adverse Events (AE)] | knowledge_base/domains/AE/spec.md:302 | Y |  |  | writer |
| ig34_p0135_a014 | §6.2.1 [Adverse Events (AE)] | knowledge_base/domains/AE/spec.md:311 | Y |  |  | writer |
| ig34_p0135_a015 | §6.2.1 [Adverse Events (AE)] | knowledge_base/domains/AE/spec.md:320 | Y |  |  | writer |
| ig34_p0135_a016 | §6.2.1 [Adverse Events (AE)] | knowledge_base/domains/AE/spec.md:329 | Y |  |  | writer |
| ig34_p0135_a017 | §6.2.1 [Adverse Events (AE)] | knowledge_base/domains/AE/spec.md:338 | Y |  |  | writer |
| ig34_p0135_a018 | §6.2.1 [Adverse Events (AE)] | knowledge_base/domains/AE/spec.md:347 | Y |  |  | writer |
| ig34_p0135_a019 | §6.2.1 [Adverse Events (AE)] | knowledge_base/domains/AE/spec.md:356 | Y |  |  | writer |
| ig34_p0136_a002 | §6.2.1 [Adverse Events (AE)] | knowledge_base/domains/AE/spec.md:365 | Y | Y |  | writer |
| ig34_p0136_a003 | §6.2.1 [Adverse Events (AE)] | knowledge_base/domains/AE/spec.md:374 | Y | Y |  | writer |
| ig34_p0136_a004 | §6.2.1 [Adverse Events (AE)] | knowledge_base/domains/AE/spec.md:383 | Y |  |  | writer |
| ig34_p0136_a005 | §6.2.1 [Adverse Events (AE)] | knowledge_base/domains/AE/spec.md:392 | Y |  |  | writer |
| ig34_p0136_a006 | §6.2.1 [Adverse Events (AE)] | knowledge_base/domains/AE/spec.md:401 | Y |  |  | writer |
| ig34_p0136_a007 | §6.2.1 [Adverse Events (AE)] | knowledge_base/domains/AE/spec.md:410 | Y |  |  | writer |
| ig34_p0136_a008 | §6.2.1 [Adverse Events (AE)] | knowledge_base/domains/AE/spec.md:419 | Y | Y |  | writer |
| ig34_p0136_a009 | §6.2.1 [Adverse Events (AE)] | knowledge_base/domains/AE/spec.md:428 | Y |  |  | writer |
| ig34_p0136_a010 | §6.2.1 [Adverse Events (AE)] | knowledge_base/domains/AE/spec.md:437 | Y |  |  | writer |
| ig34_p0136_a011 | §6.2.1 [Adverse Events (AE)] | knowledge_base/domains/AE/spec.md:446 | Y |  |  | writer |
| ig34_p0136_a012 | §6.2.1 [Adverse Events (AE)] | knowledge_base/domains/AE/spec.md:455 | Y |  |  | writer |
| ig34_p0136_a013 | §6.2.1 [Adverse Events (AE)] | knowledge_base/domains/AE/spec.md:464 | Y |  |  | writer |
| ig34_p0137_a002 | §6.2.1 [Adverse Events (AE)] | knowledge_base/domains/AE/spec.md:473 | Y |  |  | writer |
| ig34_p0137_a003 | §6.2.1 [Adverse Events (AE)] | knowledge_base/domains/AE/spec.md:482 | Y |  |  | writer |
| ig34_p0137_a004 | §6.2.1 [Adverse Events (AE)] | knowledge_base/domains/AE/spec.md:491 | Y |  |  | writer |
| ig34_p0137_a005 | §6.2.1 [Adverse Events (AE)] | knowledge_base/domains/AE/spec.md:500 | Y |  |  | writer |
| ig34_p0137_a006 | §6.2.1 [Adverse Events (AE)] | knowledge_base/domains/AE/spec.md:509 | Y | Y |  | writer |
| ig34_p0137_a007 | §6.2.1 [Adverse Events (AE)] | knowledge_base/domains/AE/spec.md:518 | Y | Y |  | writer |
| ig34_p0137_a008 | §6.2.1 [Adverse Events (AE)] | knowledge_base/domains/AE/spec.md:527 | Y | Y |  | writer |
| ig34_p0137_a009 | §6.2.1 [Adverse Events (AE)] | knowledge_base/domains/AE/spec.md:536 | Y |  |  | writer |
| ig34_p0143_a024 | §6.2.2 [Biospecimen Events (BE)] | knowledge_base/domains/BE/spec.md:140 | Y |  |  | writer |
| ig34_p0144_a001 | §6.2.2 [Biospecimen Events (BE)] | knowledge_base/domains/BE/spec.md:149 | Y |  |  | writer |
| ig34_p0144_a002 | §6.2.2 [Biospecimen Events (BE)] | knowledge_base/domains/BE/spec.md:158 | Y |  |  | writer |
| ig34_p0144_a003 | §6.2.2 [Biospecimen Events (BE)] | knowledge_base/domains/BE/spec.md:167 | Y |  |  | writer |
| ig34_p0144_a004 | §6.2.2 [Biospecimen Events (BE)] | knowledge_base/domains/BE/spec.md:176 | Y | Y |  | writer |
| ig34_p0144_a005 | §6.2.2 [Biospecimen Events (BE)] | knowledge_base/domains/BE/spec.md:185 | Y |  |  | writer |
| ig34_p0144_a006 | §6.2.2 [Biospecimen Events (BE)] | knowledge_base/domains/BE/spec.md:194 | Y |  |  | writer |
| ig34_p0144_a007 | §6.2.2 [Biospecimen Events (BE)] | knowledge_base/domains/BE/spec.md:203 | Y |  |  | writer |
| ig34_p0144_a008 | §6.2.2 [Biospecimen Events (BE)] | knowledge_base/domains/BE/spec.md:212 | Y |  |  | writer |
| ig34_p0144_a009 | §6.2.2 [Biospecimen Events (BE)] | knowledge_base/domains/BE/spec.md:221 | Y |  |  | writer |
| ig34_p0148_a020 | §6.2.3 [Clinical Events (CE)] | knowledge_base/domains/CE/spec.md:5 | Y |  |  | writer |
| ig34_p0148_a021 | §6.2.3 [Clinical Events (CE)] | knowledge_base/domains/CE/spec.md:14 | Y |  |  | writer |
| ig34_p0148_a022 | §6.2.3 [Clinical Events (CE)] | knowledge_base/domains/CE/spec.md:23 | Y |  |  | writer |
| ig34_p0148_a023 | §6.2.3 [Clinical Events (CE)] | knowledge_base/domains/CE/spec.md:32 | Y |  |  | writer |
| ig34_p0148_a024 | §6.2.3 [Clinical Events (CE)] | knowledge_base/domains/CE/spec.md:41 | Y |  |  | writer |
| ig34_p0148_a025 | §6.2.3 [Clinical Events (CE)] | knowledge_base/domains/CE/spec.md:50 | Y |  |  | writer |
| ig34_p0148_a026 | §6.2.3 [Clinical Events (CE)] | knowledge_base/domains/CE/spec.md:59 | Y |  |  | writer |
| ig34_p0148_a027 | §6.2.3 [Clinical Events (CE)] | knowledge_base/domains/CE/spec.md:68 | Y |  |  | writer |
| ig34_p0148_a028 | §6.2.3 [Clinical Events (CE)] | knowledge_base/domains/CE/spec.md:77 | Y | Y |  | writer |
| ig34_p0148_a029 | §6.2.3 [Clinical Events (CE)] | knowledge_base/domains/CE/spec.md:86 | Y |  |  | writer |
| ig34_p0149_a001 | §6.2.3 [Clinical Events (CE)] | knowledge_base/domains/CE/spec.md:95 | Y |  |  | writer |
| ig34_p0149_a002 | §6.2.3 [Clinical Events (CE)] | knowledge_base/domains/CE/spec.md:104 | Y |  |  | writer |
| ig34_p0149_a003 | §6.2.3 [Clinical Events (CE)] | knowledge_base/domains/CE/spec.md:113 | Y |  |  | writer |
| ig34_p0149_a004 | §6.2.3 [Clinical Events (CE)] | knowledge_base/domains/CE/spec.md:122 | Y |  |  | writer |
| ig34_p0149_a005 | §6.2.3 [Clinical Events (CE)] | knowledge_base/domains/CE/spec.md:131 | Y |  |  | writer |
| ig34_p0149_a007 | §6.2.3 [Clinical Events (CE)] | knowledge_base/domains/CE/spec.md:149 | Y |  |  | writer |
| ig34_p0149_a008 | §6.2.3 [Clinical Events (CE)] | knowledge_base/domains/CE/spec.md:158 | Y | Y |  | writer |
| ig34_p0149_a010 | §6.2.3 [Clinical Events (CE)] | knowledge_base/domains/CE/spec.md:176 | Y |  |  | writer |
| ig34_p0149_a011 | §6.2.3 [Clinical Events (CE)] | knowledge_base/domains/CE/spec.md:185 | Y |  |  | writer |
| ig34_p0149_a012 | §6.2.3 [Clinical Events (CE)] | knowledge_base/domains/CE/spec.md:194 | Y |  |  | writer |
| ig34_p0149_a014 | §6.2.3 [Clinical Events (CE)] | knowledge_base/domains/CE/spec.md:212 | Y | Y |  | writer |
| ig34_p0149_a015 | §6.2.3 [Clinical Events (CE)] | knowledge_base/domains/CE/spec.md:221 | Y | Y |  | writer |
| ig34_p0149_a017 | §6.2.3 [Clinical Events (CE)] | knowledge_base/domains/CE/spec.md:239 | Y | Y |  | writer |
| ig34_p0149_a018 | §6.2.3 [Clinical Events (CE)] | knowledge_base/domains/CE/spec.md:248 | Y |  |  | writer |
| ig34_p0167_a0024 | §6.2.5 Healthcare Encounters (HO) | knowledge_base/domains/HO/spec.md:5 | Y |  |  | writer |
| ig34_p0167_a0025 | §6.2.5 Healthcare Encounters (HO) | knowledge_base/domains/HO/spec.md:14 | Y |  |  | writer |
| ig34_p0168_a0001 | §6.2.5 Healthcare Encounters (HO) | knowledge_base/domains/HO/spec.md:23 | Y |  |  | writer |
| ig34_p0168_a0006 | §6.2.5 Healthcare Encounters (HO) | knowledge_base/domains/HO/spec.md:68 | Y |  |  | writer |
| ig34_p0168_a0008 | §6.2.5 Healthcare Encounters (HO) | knowledge_base/domains/HO/spec.md:86 | Y |  |  | writer |
| ig34_p0168_a0009 | §6.2.5 Healthcare Encounters (HO) | knowledge_base/domains/HO/spec.md:95 | Y |  |  | writer |
| ig34_p0172_a0010 | §6.2.6 Medical History (MH) | knowledge_base/domains/MH/spec.md:221 | Y |  |  | writer |
| ig34_p0172_a0011 | §6.2.6 Medical History (MH) | knowledge_base/domains/MH/spec.md:230 | Y | Y |  | writer |
| ig34_p0172_a0012 | §6.2.6 Medical History (MH) | knowledge_base/domains/MH/spec.md:239 | Y |  |  | writer |
| ig34_p0183_a008 | §6.3.2 Death Details (DD) | knowledge_base/domains/DD/spec.md:5 | Y | Y |  | writer |
| ig34_p0183_a009 | §6.3.2 Death Details (DD) | knowledge_base/domains/DD/spec.md:14 | Y |  |  | writer |
| ig34_p0183_a010 | §6.3.2 Death Details (DD) | knowledge_base/domains/DD/spec.md:23 | Y |  |  | writer |
| ig34_p0183_a011 | §6.3.2 Death Details (DD) | knowledge_base/domains/DD/spec.md:32 | Y |  |  | writer |
| ig34_p0183_a012 | §6.3.2 Death Details (DD) | knowledge_base/domains/DD/spec.md:41 | Y |  |  | writer |
| ig34_p0183_a013 | §6.3.2 Death Details (DD) | knowledge_base/domains/DD/spec.md:50 | Y |  |  | writer |
| ig34_p0183_a014 | §6.3.2 Death Details (DD) | knowledge_base/domains/DD/spec.md:59 | Y |  |  | writer |
| ig34_p0183_a015 | §6.3.2 Death Details (DD) | knowledge_base/domains/DD/spec.md:68 | Y |  |  | writer |
| ig34_p0183_a016 | §6.3.2 Death Details (DD) | knowledge_base/domains/DD/spec.md:77 | Y |  |  | writer |
| ig34_p0183_a017 | §6.3.2 Death Details (DD) | knowledge_base/domains/DD/spec.md:86 | Y |  |  | writer |
| ig34_p0183_a018 | §6.3.2 Death Details (DD) | knowledge_base/domains/DD/spec.md:95 | Y |  |  | writer |
| ig34_p0183_a019 | §6.3.2 Death Details (DD) | knowledge_base/domains/DD/spec.md:104 | Y |  |  | writer |
| ig34_p0185_a024 | §6.3.3 ECG Test Results (EG) | knowledge_base/domains/EG/spec.md:5 | Y |  |  | writer |
| ig34_p0185_a025 | §6.3.3 ECG Test Results (EG) | knowledge_base/domains/EG/spec.md:14 | Y |  |  | writer |
| ig34_p0185_a026 | §6.3.3 ECG Test Results (EG) | knowledge_base/domains/EG/spec.md:23 | Y |  |  | writer |
| ig34_p0185_a027 | §6.3.3 ECG Test Results (EG) | knowledge_base/domains/EG/spec.md:32 | Y |  |  | writer |
| ig34_p0185_a028 | §6.3.3 ECG Test Results (EG) | knowledge_base/domains/EG/spec.md:41 | Y |  |  | writer |
| ig34_p0185_a029 | §6.3.3 ECG Test Results (EG) | knowledge_base/domains/EG/spec.md:50 | Y |  |  | writer |
| ig34_p0185_a030 | §6.3.3 ECG Test Results (EG) | knowledge_base/domains/EG/spec.md:59 | Y |  |  | writer |
| ig34_p0186_a002 | §6.3.3 ECG Test Results (EG) | knowledge_base/domains/EG/spec.md:68 | Y |  |  | writer |
| ig34_p0186_a003 | §6.3.3 ECG Test Results (EG) | knowledge_base/domains/EG/spec.md:77 | Y |  |  | writer |
| ig34_p0186_a004 | §6.3.3 ECG Test Results (EG) | knowledge_base/domains/EG/spec.md:86 | Y |  |  | writer |
| ig34_p0186_a005 | §6.3.3 ECG Test Results (EG) | knowledge_base/domains/EG/spec.md:95 | Y | Y |  | writer |
| ig34_p0186_a006 | §6.3.3 ECG Test Results (EG) | knowledge_base/domains/EG/spec.md:104 | Y |  |  | writer |
| ig34_p0186_a007 | §6.3.3 ECG Test Results (EG) | knowledge_base/domains/EG/spec.md:113 | Y |  |  | writer |
| ig34_p0186_a008 | §6.3.3 ECG Test Results (EG) | knowledge_base/domains/EG/spec.md:122 | Y |  |  | writer |
| ig34_p0186_a009 | §6.3.3 ECG Test Results (EG) | knowledge_base/domains/EG/spec.md:131 | Y |  |  | writer |
| ig34_p0186_a010 | §6.3.3 ECG Test Results (EG) | knowledge_base/domains/EG/spec.md:140 | Y |  |  | writer |
| ig34_p0186_a011 | §6.3.3 ECG Test Results (EG) | knowledge_base/domains/EG/spec.md:149 | Y |  |  | writer |
| ig34_p0186_a012 | §6.3.3 ECG Test Results (EG) | knowledge_base/domains/EG/spec.md:158 | Y | Y |  | writer |
| ig34_p0186_a013 | §6.3.3 ECG Test Results (EG) | knowledge_base/domains/EG/spec.md:167 | Y | Y |  | writer |
| ig34_p0186_a014 | §6.3.3 ECG Test Results (EG) | knowledge_base/domains/EG/spec.md:176 | Y |  |  | writer |
| ig34_p0186_a015 | §6.3.3 ECG Test Results (EG) | knowledge_base/domains/EG/spec.md:185 | Y |  |  | writer |
| ig34_p0187_a002 | §6.3.3 ECG Test Results (EG) | knowledge_base/domains/EG/spec.md:194 | Y |  |  | writer |
| ig34_p0187_a003 | §6.3.3 ECG Test Results (EG) | knowledge_base/domains/EG/spec.md:203 | Y | Y |  | writer |
| ig34_p0187_a004 | §6.3.3 ECG Test Results (EG) | knowledge_base/domains/EG/spec.md:212 | Y | Y |  | writer |
| ig34_p0187_a005 | §6.3.3 ECG Test Results (EG) | knowledge_base/domains/EG/spec.md:221 | Y | Y |  | writer |
| ig34_p0187_a006 | §6.3.3 ECG Test Results (EG) | knowledge_base/domains/EG/spec.md:230 | Y |  |  | writer |
| ig34_p0187_a007 | §6.3.3 ECG Test Results (EG) | knowledge_base/domains/EG/spec.md:239 | Y |  |  | writer |
| ig34_p0187_a008 | §6.3.3 ECG Test Results (EG) | knowledge_base/domains/EG/spec.md:248 | Y |  |  | writer |
| ig34_p0187_a009 | §6.3.3 ECG Test Results (EG) | knowledge_base/domains/EG/spec.md:257 | Y | Y |  | writer |
| ig34_p0187_a010 | §6.3.3 ECG Test Results (EG) | knowledge_base/domains/EG/spec.md:266 | Y |  |  | writer |
| ig34_p0187_a011 | §6.3.3 ECG Test Results (EG) | knowledge_base/domains/EG/spec.md:275 | Y |  |  | writer |
| ig34_p0187_a012 | §6.3.3 ECG Test Results (EG) | knowledge_base/domains/EG/spec.md:284 | Y |  |  | writer |
| ig34_p0187_a013 | §6.3.3 ECG Test Results (EG) | knowledge_base/domains/EG/spec.md:293 | Y | Y |  | writer |
| ig34_p0187_a014 | §6.3.3 ECG Test Results (EG) | knowledge_base/domains/EG/spec.md:302 | Y |  |  | writer |
| ig34_p0187_a015 | §6.3.3 ECG Test Results (EG) | knowledge_base/domains/EG/spec.md:311 | Y |  |  | writer |
| ig34_p0187_a016 | §6.3.3 ECG Test Results (EG) | knowledge_base/domains/EG/spec.md:320 | Y | Y |  | writer |
| ig34_p0187_a017 | §6.3.3 ECG Test Results (EG) | knowledge_base/domains/EG/spec.md:329 | Y |  |  | writer |
| ig34_p0187_a018 | §6.3.3 ECG Test Results (EG) | knowledge_base/domains/EG/spec.md:338 | Y |  |  | writer |
| ig34_p0187_a019 | §6.3.3 ECG Test Results (EG) | knowledge_base/domains/EG/spec.md:347 | Y |  |  | writer |
| ig34_p0187_a020 | §6.3.3 ECG Test Results (EG) | knowledge_base/domains/EG/spec.md:356 | Y |  |  | writer |
| ig34_p0187_a021 | §6.3.3 ECG Test Results (EG) | knowledge_base/domains/EG/spec.md:365 | Y |  |  | writer |
| ig34_p0188_a002 | §6.3.3 ECG Test Results (EG) | knowledge_base/domains/EG/spec.md:374 | Y |  |  | writer |
| ig34_p0188_a003 | §6.3.3 ECG Test Results (EG) | knowledge_base/domains/EG/spec.md:383 | Y | Y |  | writer |
| ig34_p0188_a004 | §6.3.3 ECG Test Results (EG) | knowledge_base/domains/EG/spec.md:392 | Y |  |  | writer |
| ig34_p0193_a007 | §6.3.4 Inclusion/Exclusion Criteria Not Met (IE) | knowledge_base/domains/IE/spec.md:5 | Y |  |  | writer |
| ig34_p0193_a008 | §6.3.4 Inclusion/Exclusion Criteria Not Met (IE) | knowledge_base/domains/IE/spec.md:14 | Y |  |  | writer |
| ig34_p0193_a009 | §6.3.4 Inclusion/Exclusion Criteria Not Met (IE) | knowledge_base/domains/IE/spec.md:23 | Y |  |  | writer |
| ig34_p0193_a010 | §6.3.4 Inclusion/Exclusion Criteria Not Met (IE) | knowledge_base/domains/IE/spec.md:32 | Y |  |  | writer |
| ig34_p0193_a011 | §6.3.4 Inclusion/Exclusion Criteria Not Met (IE) | knowledge_base/domains/IE/spec.md:41 | Y | Y |  | writer |
| ig34_p0193_a012 | §6.3.4 Inclusion/Exclusion Criteria Not Met (IE) | knowledge_base/domains/IE/spec.md:50 | Y |  |  | writer |
| ig34_p0193_a013 | §6.3.4 Inclusion/Exclusion Criteria Not Met (IE) | knowledge_base/domains/IE/spec.md:59 | Y |  |  | writer |
| ig34_p0193_a014 | §6.3.4 Inclusion/Exclusion Criteria Not Met (IE) | knowledge_base/domains/IE/spec.md:68 | Y |  |  | writer |
| ig34_p0193_a015 | §6.3.4 Inclusion/Exclusion Criteria Not Met (IE) | knowledge_base/domains/IE/spec.md:77 | Y | Y |  | writer |
| ig34_p0193_a016 | §6.3.4 Inclusion/Exclusion Criteria Not Met (IE) | knowledge_base/domains/IE/spec.md:86 | Y | Y |  | writer |
| ig34_p0193_a017 | §6.3.4 Inclusion/Exclusion Criteria Not Met (IE) | knowledge_base/domains/IE/spec.md:95 | Y | Y |  | writer |
| ig34_p0193_a018 | §6.3.4 Inclusion/Exclusion Criteria Not Met (IE) | knowledge_base/domains/IE/spec.md:104 | Y |  |  | writer |
| ig34_p0193_a019 | §6.3.4 Inclusion/Exclusion Criteria Not Met (IE) | knowledge_base/domains/IE/spec.md:113 | Y |  |  | writer |
| ig34_p0193_a020 | §6.3.4 Inclusion/Exclusion Criteria Not Met (IE) | knowledge_base/domains/IE/spec.md:122 | Y |  |  | writer |
| ig34_p0193_a021 | §6.3.4 Inclusion/Exclusion Criteria Not Met (IE) | knowledge_base/domains/IE/spec.md:131 | Y |  |  | writer |
| ig34_p0193_a022 | §6.3.4 Inclusion/Exclusion Criteria Not Met (IE) | knowledge_base/domains/IE/spec.md:140 | Y | Y |  | writer |
| ig34_p0193_a023 | §6.3.4 Inclusion/Exclusion Criteria Not Met (IE) | knowledge_base/domains/IE/spec.md:149 | Y |  |  | writer |
| ig34_p0193_a024 | §6.3.4 Inclusion/Exclusion Criteria Not Met (IE) | knowledge_base/domains/IE/spec.md:158 | Y |  |  | writer |
| ig34_p0200_a022 | §6.3.5.3 Cell Phenotype Findings (CP) | knowledge_base/domains/CP/spec.md:95 | Y |  |  | writer |
| ig34_p0201_a006 | §6.3.5.3 Cell Phenotype Findings (CP) | knowledge_base/domains/CP/spec.md:122 | Y |  |  | writer |
| ig34_p0201_a009 | §6.3.5.3 Cell Phenotype Findings (CP) | knowledge_base/domains/CP/spec.md:149 | Y | Y |  | writer |
| ig34_p0201_a011 | §6.3.5.3 Cell Phenotype Findings (CP) | knowledge_base/domains/CP/spec.md:167 | Y |  |  | writer |
| ig34_p0243_a011 | §6.3.5.6 Laboratory Test Results (LB) | knowledge_base/domains/LB/spec.md:257 | Y |  |  | writer |
| ig34_p0252_a022 | §6.3.5.7.2 Microbiology Susceptibility (MS) | knowledge_base/domains/MS/spec.md:5 | Y |  |  | writer |
| ig34_p0252_a023 | §6.3.5.7.2 Microbiology Susceptibility (MS) | knowledge_base/domains/MS/spec.md:14 | Y |  |  | writer |
| ig34_p0252_a024 | §6.3.5.7.2 Microbiology Susceptibility (MS) | knowledge_base/domains/MS/spec.md:23 | Y |  |  | writer |
| ig34_p0252_a025 | §6.3.5.7.2 Microbiology Susceptibility (MS) | knowledge_base/domains/MS/spec.md:32 | Y | Y |  | writer |
| ig34_p0264_a005 | §6.3.5.8 Microscopic Findings (MI) | knowledge_base/domains/MI/spec.md:5 | Y | Y |  | writer |
| ig34_p0264_a006 | §6.3.5.8 Microscopic Findings (MI) | knowledge_base/domains/MI/spec.md:14 | Y |  |  | writer |
| ig34_p0264_a007 | §6.3.5.8 Microscopic Findings (MI) | knowledge_base/domains/MI/spec.md:23 | Y |  |  | writer |
| ig34_p0264_a008 | §6.3.5.8 Microscopic Findings (MI) | knowledge_base/domains/MI/spec.md:32 | Y |  |  | writer |
| ig34_p0264_a009 | §6.3.5.8 Microscopic Findings (MI) | knowledge_base/domains/MI/spec.md:41 | Y |  |  | writer |
| ig34_p0264_a010 | §6.3.5.8 Microscopic Findings (MI) | knowledge_base/domains/MI/spec.md:50 | Y |  |  | writer |
| ig34_p0264_a011 | §6.3.5.8 Microscopic Findings (MI) | knowledge_base/domains/MI/spec.md:59 | Y |  |  | writer |
| ig34_p0264_a012 | §6.3.5.8 Microscopic Findings (MI) | knowledge_base/domains/MI/spec.md:68 | Y |  |  | writer |
| ig34_p0264_a013 | §6.3.5.8 Microscopic Findings (MI) | knowledge_base/domains/MI/spec.md:77 | Y | Y |  | writer |
| ig34_p0264_a014 | §6.3.5.8 Microscopic Findings (MI) | knowledge_base/domains/MI/spec.md:86 | Y |  |  | writer |
| ig34_p0264_a015 | §6.3.5.8 Microscopic Findings (MI) | knowledge_base/domains/MI/spec.md:95 | Y |  |  | writer |
| ig34_p0264_a016 | §6.3.5.8 Microscopic Findings (MI) | knowledge_base/domains/MI/spec.md:104 | Y |  |  | writer |
| ig34_p0264_a017 | §6.3.5.8 Microscopic Findings (MI) | knowledge_base/domains/MI/spec.md:113 | Y |  |  | writer |
| ig34_p0264_a018 | §6.3.5.8 Microscopic Findings (MI) | knowledge_base/domains/MI/spec.md:122 | Y |  |  | writer |
| ig34_p0264_a019 | §6.3.5.8 Microscopic Findings (MI) | knowledge_base/domains/MI/spec.md:131 | Y |  |  | writer |
| ig34_p0264_a020 | §6.3.5.8 Microscopic Findings (MI) | knowledge_base/domains/MI/spec.md:140 | Y |  |  | writer |
| ig34_p0264_a021 | §6.3.5.8 Microscopic Findings (MI) | knowledge_base/domains/MI/spec.md:149 | Y |  |  | writer |
| ig34_p0264_a022 | §6.3.5.8 Microscopic Findings (MI) | knowledge_base/domains/MI/spec.md:158 | Y |  |  | writer |
| ig34_p0264_a023 | §6.3.5.8 Microscopic Findings (MI) | knowledge_base/domains/MI/spec.md:167 | Y |  |  | writer |
| ig34_p0264_a024 | §6.3.5.8 Microscopic Findings (MI) | knowledge_base/domains/MI/spec.md:176 | Y |  |  | writer |
| ig34_p0264_a025 | §6.3.5.8 Microscopic Findings (MI) | knowledge_base/domains/MI/spec.md:185 | Y |  |  | writer |
| ig34_p0265_a001 | §6.3.5.8 Microscopic Findings (MI) | knowledge_base/domains/MI/spec.md:194 | Y |  |  | writer |
| ig34_p0265_a002 | §6.3.5.8 Microscopic Findings (MI) | knowledge_base/domains/MI/spec.md:203 | Y |  |  | writer |
| ig34_p0265_a003 | §6.3.5.8 Microscopic Findings (MI) | knowledge_base/domains/MI/spec.md:212 | Y |  |  | writer |
| ig34_p0265_a004 | §6.3.5.8 Microscopic Findings (MI) | knowledge_base/domains/MI/spec.md:221 | Y |  |  | writer |
| ig34_p0265_a005 | §6.3.5.8 Microscopic Findings (MI) | knowledge_base/domains/MI/spec.md:230 | Y | Y |  | writer |
| ig34_p0265_a006 | §6.3.5.8 Microscopic Findings (MI) | knowledge_base/domains/MI/spec.md:239 | Y |  |  | writer |
| ig34_p0265_a007 | §6.3.5.8 Microscopic Findings (MI) | knowledge_base/domains/MI/spec.md:248 | Y |  |  | writer |
| ig34_p0265_a008 | §6.3.5.8 Microscopic Findings (MI) | knowledge_base/domains/MI/spec.md:257 | Y | Y |  | writer |
| ig34_p0265_a009 | §6.3.5.8 Microscopic Findings (MI) | knowledge_base/domains/MI/spec.md:266 | Y |  |  | writer |
| ig34_p0265_a010 | §6.3.5.8 Microscopic Findings (MI) | knowledge_base/domains/MI/spec.md:275 | Y |  |  | writer |
| ig34_p0265_a011 | §6.3.5.8 Microscopic Findings (MI) | knowledge_base/domains/MI/spec.md:284 | Y |  |  | writer |
| ig34_p0265_a012 | §6.3.5.8 Microscopic Findings (MI) | knowledge_base/domains/MI/spec.md:293 | Y | Y |  | writer |
| ig34_p0265_a013 | §6.3.5.8 Microscopic Findings (MI) | knowledge_base/domains/MI/spec.md:302 | Y |  |  | writer |
| ig34_p0265_a014 | §6.3.5.8 Microscopic Findings (MI) | knowledge_base/domains/MI/spec.md:311 | Y |  |  | writer |
| ig34_p0265_a015 | §6.3.5.8 Microscopic Findings (MI) | knowledge_base/domains/MI/spec.md:320 | Y |  |  | writer |
| ig34_p0265_a016 | §6.3.5.8 Microscopic Findings (MI) | knowledge_base/domains/MI/spec.md:329 | Y | Y |  | writer |
| ig34_p0286_a021 | §6.3.7.2 Cardiovascular System Findings (CV) | knowledge_base/domains/CV/spec.md:5 | Y |  |  | writer |
| ig34_p0287_a001 | §6.3.7.2 Cardiovascular System Findings (CV) | knowledge_base/domains/CV/spec.md:14 | Y |  |  | writer |
| ig34_p0287_a002 | §6.3.7.2 Cardiovascular System Findings (CV) | knowledge_base/domains/CV/spec.md:23 | Y |  |  | writer |
| ig34_p0287_a003 | §6.3.7.2 Cardiovascular System Findings (CV) | knowledge_base/domains/CV/spec.md:32 | Y |  |  | writer |
| ig34_p0287_a004 | §6.3.7.2 Cardiovascular System Findings (CV) | knowledge_base/domains/CV/spec.md:41 | Y |  |  | writer |
| ig34_p0287_a005 | §6.3.7.2 Cardiovascular System Findings (CV) | knowledge_base/domains/CV/spec.md:50 | Y |  |  | writer |
| ig34_p0287_a006 | §6.3.7.2 Cardiovascular System Findings (CV) | knowledge_base/domains/CV/spec.md:59 | Y |  |  | writer |
| ig34_p0287_a007 | §6.3.7.2 Cardiovascular System Findings (CV) | knowledge_base/domains/CV/spec.md:68 | Y | Y |  | writer |
| ig34_p0287_a008 | §6.3.7.2 Cardiovascular System Findings (CV) | knowledge_base/domains/CV/spec.md:77 | Y |  |  | writer |
| ig34_p0287_a009 | §6.3.7.2 Cardiovascular System Findings (CV) | knowledge_base/domains/CV/spec.md:86 | Y |  |  | writer |
| ig34_p0287_a010 | §6.3.7.2 Cardiovascular System Findings (CV) | knowledge_base/domains/CV/spec.md:95 | Y |  |  | writer |
| ig34_p0287_a011 | §6.3.7.2 Cardiovascular System Findings (CV) | knowledge_base/domains/CV/spec.md:104 | Y |  |  | writer |
| ig34_p0287_a012 | §6.3.7.2 Cardiovascular System Findings (CV) | knowledge_base/domains/CV/spec.md:113 | Y |  |  | writer |
| ig34_p0287_a013 | §6.3.7.2 Cardiovascular System Findings (CV) | knowledge_base/domains/CV/spec.md:122 | Y |  |  | writer |
| ig34_p0287_a014 | §6.3.7.2 Cardiovascular System Findings (CV) | knowledge_base/domains/CV/spec.md:131 | Y |  |  | writer |
| ig34_p0287_a015 | §6.3.7.2 Cardiovascular System Findings (CV) | knowledge_base/domains/CV/spec.md:140 | Y |  |  | writer |
| ig34_p0287_a016 | §6.3.7.2 Cardiovascular System Findings (CV) | knowledge_base/domains/CV/spec.md:149 | Y |  |  | writer |
| ig34_p0287_a017 | §6.3.7.2 Cardiovascular System Findings (CV) | knowledge_base/domains/CV/spec.md:158 | Y |  |  | writer |
| ig34_p0287_a018 | §6.3.7.2 Cardiovascular System Findings (CV) | knowledge_base/domains/CV/spec.md:167 | Y |  |  | writer |
| ig34_p0287_a019 | §6.3.7.2 Cardiovascular System Findings (CV) | knowledge_base/domains/CV/spec.md:176 | Y |  |  | writer |
| ig34_p0287_a020 | §6.3.7.2 Cardiovascular System Findings (CV) | knowledge_base/domains/CV/spec.md:185 | Y |  |  | writer |
| ig34_p0287_a021 | §6.3.7.2 Cardiovascular System Findings (CV) | knowledge_base/domains/CV/spec.md:194 | Y |  |  | writer |
| ig34_p0287_a022 | §6.3.7.2 Cardiovascular System Findings (CV) | knowledge_base/domains/CV/spec.md:203 | Y |  |  | writer |
| ig34_p0287_a023 | §6.3.7.2 Cardiovascular System Findings (CV) | knowledge_base/domains/CV/spec.md:212 | Y |  |  | writer |
| ig34_p0287_a024 | §6.3.7.2 Cardiovascular System Findings (CV) | knowledge_base/domains/CV/spec.md:221 | Y | Y |  | writer |
| ig34_p0288_a001 | §6.3.7.2 Cardiovascular System Findings (CV) | knowledge_base/domains/CV/spec.md:230 | Y |  |  | writer |
| ig34_p0288_a002 | §6.3.7.2 Cardiovascular System Findings (CV) | knowledge_base/domains/CV/spec.md:239 | Y |  |  | writer |
| ig34_p0288_a003 | §6.3.7.2 Cardiovascular System Findings (CV) | knowledge_base/domains/CV/spec.md:248 | Y |  |  | writer |
| ig34_p0288_a004 | §6.3.7.2 Cardiovascular System Findings (CV) | knowledge_base/domains/CV/spec.md:257 | Y |  |  | writer |
| ig34_p0288_a005 | §6.3.7.2 Cardiovascular System Findings (CV) | knowledge_base/domains/CV/spec.md:266 | Y |  |  | writer |
| ig34_p0288_a006 | §6.3.7.2 Cardiovascular System Findings (CV) | knowledge_base/domains/CV/spec.md:275 | Y |  |  | writer |
| ig34_p0288_a007 | §6.3.7.2 Cardiovascular System Findings (CV) | knowledge_base/domains/CV/spec.md:284 | Y | Y |  | writer |
| ig34_p0288_a008 | §6.3.7.2 Cardiovascular System Findings (CV) | knowledge_base/domains/CV/spec.md:293 | Y |  |  | writer |
| ig34_p0288_a009 | §6.3.7.2 Cardiovascular System Findings (CV) | knowledge_base/domains/CV/spec.md:302 | Y | Y |  | writer |
| ig34_p0288_a010 | §6.3.7.2 Cardiovascular System Findings (CV) | knowledge_base/domains/CV/spec.md:311 | Y |  |  | writer |
| ig34_p0288_a011 | §6.3.7.2 Cardiovascular System Findings (CV) | knowledge_base/domains/CV/spec.md:320 | Y | Y |  | writer |
| ig34_p0288_a012 | §6.3.7.2 Cardiovascular System Findings (CV) | knowledge_base/domains/CV/spec.md:329 | Y |  |  | writer |
| ig34_p0288_a013 | §6.3.7.2 Cardiovascular System Findings (CV) | knowledge_base/domains/CV/spec.md:338 | Y | Y |  | writer |
| ig34_p0288_a014 | §6.3.7.2 Cardiovascular System Findings (CV) | knowledge_base/domains/CV/spec.md:347 | Y |  |  | writer |
| ig34_p0288_a015 | §6.3.7.2 Cardiovascular System Findings (CV) | knowledge_base/domains/CV/spec.md:356 | Y |  |  | writer |
| ig34_p0288_a016 | §6.3.7.2 Cardiovascular System Findings (CV) | knowledge_base/domains/CV/spec.md:365 | Y |  |  | writer |
| ig34_p0288_a017 | §6.3.7.2 Cardiovascular System Findings (CV) | knowledge_base/domains/CV/spec.md:374 | Y | Y |  | writer |
| ig34_p0294_a018 | §6.3.7.4 Nervous System Findings (NV) | knowledge_base/domains/NV/spec.md:5 | Y |  |  | writer |
| ig34_p0294_a019 | §6.3.7.4 Nervous System Findings (NV) | knowledge_base/domains/NV/spec.md:14 | Y |  |  | writer |
| ig34_p0294_a020 | §6.3.7.4 Nervous System Findings (NV) | knowledge_base/domains/NV/spec.md:23 | Y |  |  | writer |
| ig34_p0294_a021 | §6.3.7.4 Nervous System Findings (NV) | knowledge_base/domains/NV/spec.md:32 | Y |  |  | writer |
| ig34_p0294_a022 | §6.3.7.4 Nervous System Findings (NV) | knowledge_base/domains/NV/spec.md:41 | Y | Y |  | writer |
| ig34_p0294_a024 | §6.3.7.4 Nervous System Findings (NV) | knowledge_base/domains/NV/spec.md:59 | Y | Y |  | writer |
| ig34_p0294_a025 | §6.3.7.4 Nervous System Findings (NV) | knowledge_base/domains/NV/spec.md:68 | Y |  |  | writer |
| ig34_p0294_a026 | §6.3.7.4 Nervous System Findings (NV) | knowledge_base/domains/NV/spec.md:77 | Y |  |  | writer |
| ig34_p0294_a027 | §6.3.7.4 Nervous System Findings (NV) | knowledge_base/domains/NV/spec.md:86 | Y |  |  | writer |
| ig34_p0294_a028 | §6.3.7.4 Nervous System Findings (NV) | knowledge_base/domains/NV/spec.md:95 | Y |  |  | writer |
| ig34_p0295_a001 | §6.3.7.4 Nervous System Findings (NV) | knowledge_base/domains/NV/spec.md:104 | Y |  |  | writer |
| ig34_p0295_a003 | §6.3.7.4 Nervous System Findings (NV) | knowledge_base/domains/NV/spec.md:122 | Y | Y |  | writer |
| ig34_p0295_a004 | §6.3.7.4 Nervous System Findings (NV) | knowledge_base/domains/NV/spec.md:131 | Y | Y |  | writer |
| ig34_p0295_a005 | §6.3.7.4 Nervous System Findings (NV) | knowledge_base/domains/NV/spec.md:140 | Y |  |  | writer |
| ig34_p0295_a006 | §6.3.7.4 Nervous System Findings (NV) | knowledge_base/domains/NV/spec.md:149 | Y |  |  | writer |
| ig34_p0295_a007 | §6.3.7.4 Nervous System Findings (NV) | knowledge_base/domains/NV/spec.md:158 | Y |  |  | writer |
| ig34_p0295_a008 | §6.3.7.4 Nervous System Findings (NV) | knowledge_base/domains/NV/spec.md:167 | Y |  |  | writer |
| ig34_p0295_a009 | §6.3.7.4 Nervous System Findings (NV) | knowledge_base/domains/NV/spec.md:176 | Y |  |  | writer |
| ig34_p0295_a010 | §6.3.7.4 Nervous System Findings (NV) | knowledge_base/domains/NV/spec.md:185 | Y | Y |  | writer |
| ig34_p0295_a011 | §6.3.7.4 Nervous System Findings (NV) | knowledge_base/domains/NV/spec.md:194 | Y |  |  | writer |
| ig34_p0295_a012 | §6.3.7.4 Nervous System Findings (NV) | knowledge_base/domains/NV/spec.md:203 | Y | Y |  | writer |
| ig34_p0295_a013 | §6.3.7.4 Nervous System Findings (NV) | knowledge_base/domains/NV/spec.md:212 | Y |  |  | writer |
| ig34_p0295_a014 | §6.3.7.4 Nervous System Findings (NV) | knowledge_base/domains/NV/spec.md:221 | Y |  |  | writer |
| ig34_p0295_a015 | §6.3.7.4 Nervous System Findings (NV) | knowledge_base/domains/NV/spec.md:230 | Y |  |  | writer |
| ig34_p0295_a016 | §6.3.7.4 Nervous System Findings (NV) | knowledge_base/domains/NV/spec.md:239 | Y |  |  | writer |
| ig34_p0295_a017 | §6.3.7.4 Nervous System Findings (NV) | knowledge_base/domains/NV/spec.md:248 | Y |  |  | writer |
| ig34_p0295_a018 | §6.3.7.4 Nervous System Findings (NV) | knowledge_base/domains/NV/spec.md:257 | Y | Y |  | writer |
| ig34_p0295_a019 | §6.3.7.4 Nervous System Findings (NV) | knowledge_base/domains/NV/spec.md:266 | Y |  |  | writer |
| ig34_p0295_a020 | §6.3.7.4 Nervous System Findings (NV) | knowledge_base/domains/NV/spec.md:275 | Y |  |  | writer |
| ig34_p0295_a021 | §6.3.7.4 Nervous System Findings (NV) | knowledge_base/domains/NV/spec.md:284 | Y |  |  | writer |
| ig34_p0295_a022 | §6.3.7.4 Nervous System Findings (NV) | knowledge_base/domains/NV/spec.md:293 | Y |  |  | writer |
| ig34_p0295_a023 | §6.3.7.4 Nervous System Findings (NV) | knowledge_base/domains/NV/spec.md:302 | Y | Y |  | writer |
| ig34_p0295_a024 | §6.3.7.4 Nervous System Findings (NV) | knowledge_base/domains/NV/spec.md:311 | Y |  |  | writer |
| ig34_p0295_a025 | §6.3.7.4 Nervous System Findings (NV) | knowledge_base/domains/NV/spec.md:320 | Y |  |  | writer |
| ig34_p0295_a026 | §6.3.7.4 Nervous System Findings (NV) | knowledge_base/domains/NV/spec.md:329 | Y |  |  | writer |
| ig34_p0295_a027 | §6.3.7.4 Nervous System Findings (NV) | knowledge_base/domains/NV/spec.md:338 | Y |  |  | writer |
| ig34_p0296_a001 | §6.3.7.4 Nervous System Findings (NV) | knowledge_base/domains/NV/spec.md:347 | Y |  |  | writer |
| ig34_p0296_a002 | §6.3.7.4 Nervous System Findings (NV) | knowledge_base/domains/NV/spec.md:356 | Y |  |  | writer |
| ig34_p0296_a003 | §6.3.7.4 Nervous System Findings (NV) | knowledge_base/domains/NV/spec.md:365 | Y |  |  | writer |
| ig34_p0296_a004 | §6.3.7.4 Nervous System Findings (NV) | knowledge_base/domains/NV/spec.md:374 | Y |  |  | writer |
| ig34_p0309_a001 | §6.3.7.7 Respiratory System Findings (RE) | knowledge_base/domains/RE/spec.md:185 | Y |  |  | writer |
| ig34_p0309_a002 | §6.3.7.7 Respiratory System Findings (RE) | knowledge_base/domains/RE/spec.md:194 | Y |  |  | writer |
| ig34_p0309_a003 | §6.3.7.7 Respiratory System Findings (RE) | knowledge_base/domains/RE/spec.md:203 | Y |  |  | writer |
| ig34_p0309_a004 | §6.3.7.7 Respiratory System Findings (RE) | knowledge_base/domains/RE/spec.md:212 | Y | Y |  | writer |
| ig34_p0309_a005 | §6.3.7.7 Respiratory System Findings (RE) | knowledge_base/domains/RE/spec.md:221 | Y |  |  | writer |
| ig34_p0309_a006 | §6.3.7.7 Respiratory System Findings (RE) | knowledge_base/domains/RE/spec.md:230 | Y |  |  | writer |
| ig34_p0309_a007 | §6.3.7.7 Respiratory System Findings (RE) | knowledge_base/domains/RE/spec.md:239 | Y |  |  | writer |
| ig34_p0309_a008 | §6.3.7.7 Respiratory System Findings (RE) | knowledge_base/domains/RE/spec.md:248 | Y | Y |  | writer |
| ig34_p0309_a009 | §6.3.7.7 Respiratory System Findings (RE) | knowledge_base/domains/RE/spec.md:257 | Y |  |  | writer |
| ig34_p0309_a010 | §6.3.7.7 Respiratory System Findings (RE) | knowledge_base/domains/RE/spec.md:266 | Y |  |  | writer |
| ig34_p0309_a011 | §6.3.7.7 Respiratory System Findings (RE) | knowledge_base/domains/RE/spec.md:275 | Y |  |  | writer |
| ig34_p0309_a012 | §6.3.7.7 Respiratory System Findings (RE) | knowledge_base/domains/RE/spec.md:284 | Y |  |  | writer |
| ig34_p0309_a013 | §6.3.7.7 Respiratory System Findings (RE) | knowledge_base/domains/RE/spec.md:293 | Y |  |  | writer |
| ig34_p0309_a014 | §6.3.7.7 Respiratory System Findings (RE) | knowledge_base/domains/RE/spec.md:302 | Y |  |  | writer |
| ig34_p0309_a015 | §6.3.7.7 Respiratory System Findings (RE) | knowledge_base/domains/RE/spec.md:311 | Y |  |  | writer |
| ig34_p0309_a016 | §6.3.7.7 Respiratory System Findings (RE) | knowledge_base/domains/RE/spec.md:320 | Y |  |  | writer |
| ig34_p0309_a017 | §6.3.7.7 Respiratory System Findings (RE) | knowledge_base/domains/RE/spec.md:329 | Y |  |  | writer |
| ig34_p0309_a018 | §6.3.7.7 Respiratory System Findings (RE) | knowledge_base/domains/RE/spec.md:338 | Y |  |  | writer |
| ig34_p0309_a019 | §6.3.7.7 Respiratory System Findings (RE) | knowledge_base/domains/RE/spec.md:347 | Y | Y |  | writer |
| ig34_p0309_a020 | §6.3.7.7 Respiratory System Findings (RE) | knowledge_base/domains/RE/spec.md:356 | Y |  |  | writer |
| ig34_p0309_a021 | §6.3.7.7 Respiratory System Findings (RE) | knowledge_base/domains/RE/spec.md:365 | Y | Y |  | writer |
| ig34_p0309_a022 | §6.3.7.7 Respiratory System Findings (RE) | knowledge_base/domains/RE/spec.md:374 | Y |  |  | writer |
| ig34_p0309_a023 | §6.3.7.7 Respiratory System Findings (RE) | knowledge_base/domains/RE/spec.md:383 | Y |  |  | writer |
| ig34_p0310_a001 | §6.3.7.7 Respiratory System Findings (RE) | knowledge_base/domains/RE/spec.md:392 | Y | Y |  | writer |
| ig34_p0310_a002 | §6.3.7.7 Respiratory System Findings (RE) | knowledge_base/domains/RE/spec.md:401 | Y | Y |  | writer |
| ig34_p0310_a003 | §6.3.7.7 Respiratory System Findings (RE) | knowledge_base/domains/RE/spec.md:410 | Y |  |  | writer |
| ig34_p0310_a004 | §6.3.7.7 Respiratory System Findings (RE) | knowledge_base/domains/RE/spec.md:419 | Y |  |  | writer |
| ig34_p0319_a014 | §6.3.9.1 Functional Tests (FT) | knowledge_base/domains/FT/spec.md:59 | Y |  |  | writer |
| ig34_p0319_a015 | §6.3.9.1 Functional Tests (FT) | knowledge_base/domains/FT/spec.md:68 | Y | Y |  | writer |
| ig34_p0319_a016 | §6.3.9.1 Functional Tests (FT) | knowledge_base/domains/FT/spec.md:77 | Y |  |  | writer |
| ig34_p0319_a022 | §6.3.9.1 Functional Tests (FT) | knowledge_base/domains/FT/spec.md:131 | Y |  |  | writer |
| ig34_p0320_a007 | §6.3.9.1 Functional Tests (FT) | knowledge_base/domains/FT/spec.md:203 | Y | Y |  | writer |
| ig34_p0320_a008 | §6.3.9.1 Functional Tests (FT) | knowledge_base/domains/FT/spec.md:212 | Y |  |  | writer |
| ig34_p0320_a010 | §6.3.9.1 Functional Tests (FT) | knowledge_base/domains/FT/spec.md:230 | Y |  |  | writer |
| ig34_p0320_a014 | §6.3.9.1 Functional Tests (FT) | knowledge_base/domains/FT/spec.md:266 | Y |  |  | writer |
| ig34_p0329_a018 | §6.3.9.3 Disease Response and Clin Classification (RS) — RS-Specification | knowledge_base/domains/RS/spec.md:32 | Y |  |  | writer |
| ig34_p0329_a019 | §6.3.9.3 Disease Response and Clin Classification (RS) — RS-Specification | knowledge_base/domains/RS/spec.md:41 | Y | Y |  | writer |
| ig34_p0329_a021 | §6.3.9.3 Disease Response and Clin Classification (RS) — RS-Specification | knowledge_base/domains/RS/spec.md:59 | Y |  |  | writer |
| ig34_p0329_a022 | §6.3.9.3 Disease Response and Clin Classification (RS) — RS-Specification | knowledge_base/domains/RS/spec.md:68 | Y |  |  | writer |
| ig34_p0329_a023 | §6.3.9.3 Disease Response and Clin Classification (RS) — RS-Specification | knowledge_base/domains/RS/spec.md:77 | Y |  |  | writer |
| ig34_p0330_a003 | §6.3.9.3 Disease Response and Clin Classification (RS) — RS-Specification | knowledge_base/domains/RS/spec.md:95 | Y | Y |  | writer |
| ig34_p0330_a004 | §6.3.9.3 Disease Response and Clin Classification (RS) — RS-Specification | knowledge_base/domains/RS/spec.md:104 | Y |  |  | writer |
| ig34_p0330_a005 | §6.3.9.3 Disease Response and Clin Classification (RS) — RS-Specification | knowledge_base/domains/RS/spec.md:113 | Y |  |  | writer |
| ig34_p0330_a006 | §6.3.9.3 Disease Response and Clin Classification (RS) — RS-Specification | knowledge_base/domains/RS/spec.md:122 | Y | Y |  | writer |
| ig34_p0330_a011 | §6.3.9.3 Disease Response and Clin Classification (RS) — RS-Specification | knowledge_base/domains/RS/spec.md:167 | Y |  |  | writer |
| ig34_p0330_a012 | §6.3.9.3 Disease Response and Clin Classification (RS) — RS-Specification | knowledge_base/domains/RS/spec.md:176 | Y |  |  | writer |
| ig34_p0330_a015 | §6.3.9.3 Disease Response and Clin Classification (RS) — RS-Specification | knowledge_base/domains/RS/spec.md:203 | Y | Y |  | writer |
| ig34_p0330_a017 | §6.3.9.3 Disease Response and Clin Classification (RS) — RS-Specification | knowledge_base/domains/RS/spec.md:221 | Y | Y |  | writer |
| ig34_p0331_a001 | §6.3.9.3 Disease Response and Clin Classification (RS) | knowledge_base/domains/RS/spec.md:230 | Y |  |  | writer |
| ig34_p0331_a002 | §6.3.9.3 Disease Response and Clin Classification (RS) | knowledge_base/domains/RS/spec.md:239 | Y |  |  | writer |
| ig34_p0331_a003 | §6.3.9.3 Disease Response and Clin Classification (RS) | knowledge_base/domains/RS/spec.md:248 | Y | Y |  | writer |
| ig34_p0331_a010 | §6.3.9.3 Disease Response and Clin Classification (RS) | knowledge_base/domains/RS/spec.md:311 | Y |  |  | writer |
| ig34_p0331_a011 | §6.3.9.3 Disease Response and Clin Classification (RS) | knowledge_base/domains/RS/spec.md:320 | Y |  |  | writer |
| ig34_p0331_a017 | §6.3.9.3 Disease Response and Clin Classification (RS) | knowledge_base/domains/RS/spec.md:374 | Y |  |  | writer |

## VERSION_MISMATCH (70)

| atom_id | 节 | kb_loc | det | rev | extra | src |
|---|---|---|:-:|:-:|:-:|---|
| sv20_p0004_a003 | §1 [INTRODUCTION] |  |  |  | Y | writer |
| sv20_p0004_a005 | §1 [INTRODUCTION] |  |  |  | Y | writer |
| sv20_p0004_a007 | §1 [INTRODUCTION] |  |  | Y |  | writer |
| sv20_p0004_a008 | §1 [INTRODUCTION] |  |  |  | Y | writer |
| sv20_p0004_a009 | §1 [INTRODUCTION] |  |  |  | Y | writer |
| sv20_p0004_a011 | §1 [INTRODUCTION] |  |  |  | Y | writer |
| sv20_p0004_a012 | §1 [INTRODUCTION] |  |  | Y |  | writer |
| sv20_p0004_a013 | §1 [INTRODUCTION] |  |  |  | Y | writer |
| sv20_p0004_a015 | §1 [INTRODUCTION] |  |  |  | Y | writer |
| sv20_p0004_a018 | §1 [INTRODUCTION] |  |  | Y |  | writer |
| sv20_p0004_a019 | §1 [INTRODUCTION] |  |  |  | Y | writer |
| sv20_p0004_a020 | §1 [INTRODUCTION] |  |  |  | Y | writer |
| sv20_p0004_a021 | §1 [INTRODUCTION] |  |  |  | Y | writer |
| sv20_p0004_a022 | §1 [INTRODUCTION] |  |  |  | Y | writer |
| sv20_p0004_a023 | §1 [INTRODUCTION] |  |  | Y |  | writer |
| sv20_p0004_a024 | §1 [INTRODUCTION] |  |  |  | Y | writer |
| sv20_p0004_a025 | §1 [INTRODUCTION] |  |  |  | Y | writer |
| sv20_p0005_a002 | §1 [INTRODUCTION] |  |  |  | Y | writer |
| sv20_p0005_a003 | §1 [INTRODUCTION] |  |  | Y |  | writer |
| sv20_p0005_a005 | §1 [INTRODUCTION] |  |  |  | Y | writer |
| sv20_p0005_a008 | §1 [INTRODUCTION] |  |  |  | Y | writer |
| sv20_p0005_a009 | §1 [INTRODUCTION] |  |  |  | Y | writer |
| sv20_p0046_a003 | §3.2.3.1 [Subject Elements] | knowledge_base/model/03_special_purpose_domains.md:107 |  |  | Y | writer |
| sv20_p0046_a004 | §3.2.3.1 [Subject Elements] | knowledge_base/model/03_special_purpose_domains.md:108 |  | Y |  | writer |
| sv20_p0046_a005 | §3.2.3.1 [Subject Elements] | knowledge_base/model/03_special_purpose_domains.md:109 |  |  | Y | writer |
| sv20_p0046_a006 | §3.2.3.1 [Subject Elements] | knowledge_base/model/03_special_purpose_domains.md:110 |  |  | Y | writer |
| sv20_p0046_a007 | §3.2.3.1 [Subject Elements] | knowledge_base/model/03_special_purpose_domains.md:111 |  |  | Y | writer |
| sv20_p0046_a008 | §3.2.3.1 [Subject Elements] | knowledge_base/model/03_special_purpose_domains.md:112 |  |  | Y | writer |
| sv20_p0046_a009 | §3.2.3.1 [Subject Elements] | knowledge_base/model/03_special_purpose_domains.md:113 |  |  | Y | writer |
| sv20_p0046_a010 | §3.2.3.1 [Subject Elements] | knowledge_base/model/03_special_purpose_domains.md:114 |  |  | Y | writer |
| sv20_p0046_a011 | §3.2.3.1 [Subject Elements] | knowledge_base/model/03_special_purpose_domains.md:115 |  | Y |  | writer |
| sv20_p0046_a012 | §3.2.3.1 [Subject Elements] | knowledge_base/model/03_special_purpose_domains.md:116 |  | Y |  | writer |
| sv20_p0046_a013 | §3.2.3.1 [Subject Elements] | knowledge_base/model/03_special_purpose_domains.md:117 |  | Y |  | writer |
| sv20_p0046_a014 | §3.2.3.1 [Subject Elements] | knowledge_base/model/03_special_purpose_domains.md:118 |  |  | Y | writer |
| sv20_p0046_a015 | §3.2.3.1 [Subject Elements] | knowledge_base/model/03_special_purpose_domains.md:119 |  |  | Y | writer |
| sv20_p0047_a003 | §3.2.3.2 [Subject Repro Stages] | knowledge_base/model/03_special_purpose_domains.md:133 |  |  | Y | writer |
| sv20_p0047_a004 | §3.2.3.2 [Subject Repro Stages] | knowledge_base/model/03_special_purpose_domains.md:134 |  |  | Y | writer |
| sv20_p0047_a005 | §3.2.3.2 [Subject Repro Stages] | knowledge_base/model/03_special_purpose_domains.md:135 |  |  | Y | writer |
| sv20_p0047_a006 | §3.2.3.2 [Subject Repro Stages] | knowledge_base/model/03_special_purpose_domains.md:136 |  | Y |  | writer |
| sv20_p0047_a007 | §3.2.3.2 [Subject Repro Stages] | knowledge_base/model/03_special_purpose_domains.md:137 |  |  | Y | writer |
| sv20_p0047_a008 | §3.2.3.2 [Subject Repro Stages] | knowledge_base/model/03_special_purpose_domains.md:138 |  |  | Y | writer |
| sv20_p0047_a009 | §3.2.3.2 [Subject Repro Stages] | knowledge_base/model/03_special_purpose_domains.md:139 |  |  | Y | writer |
| sv20_p0047_a010 | §3.2.3.2 [Subject Repro Stages] | knowledge_base/model/03_special_purpose_domains.md:140 |  |  | Y | writer |
| sv20_p0047_a011 | §3.2.3.2 [Subject Repro Stages] | knowledge_base/model/03_special_purpose_domains.md:141 |  |  | Y | writer |
| sv20_p0047_a012 | §3.2.3.2 [Subject Repro Stages] | knowledge_base/model/03_special_purpose_domains.md:142 |  |  | Y | writer |
| sv20_p0055_a003 | §5.1.3.2 Trial Repro Paths | knowledge_base/model/05_study_level_data.md:105 |  |  | Y | writer |
| sv20_p0055_a004 | §5.1.3.2 Trial Repro Paths | knowledge_base/model/05_study_level_data.md:106 |  | Y |  | writer |
| sv20_p0056_a008 | §5.1.4.1 Trial Visits | knowledge_base/model/05_study_level_data.md:124 |  |  | Y | writer |
| sv20_p0056_a009 | §5.1.4.1 Trial Visits | knowledge_base/model/05_study_level_data.md:125 |  |  | Y | writer |
| sv20_p0056_a010 | §5.1.4.1 Trial Visits | knowledge_base/model/05_study_level_data.md:126 |  |  | Y | writer |
| sv20_p0056_a019 | §5.1.4.2 Trial Disease Assessments | knowledge_base/domains/TD/assumptions.md:3 |  |  | Y | writer |
| sv20_p0056_a020 | §5.1.4.2 Trial Disease Assessments | knowledge_base/domains/TD/assumptions.md:3 |  |  | Y | writer |
| sv20_p0056_a022 | §5.1.4.2 Trial Disease Assessments | knowledge_base/domains/TD/assumptions.md:3 |  | Y |  | writer |
| sv20_p0057_a003 | §5.1.4.2 Trial Disease Assessments | knowledge_base/model/05_study_level_data.md:142 |  |  | Y | writer |
| sv20_p0057_a004 | §5.1.4.2 Trial Disease Assessments | knowledge_base/model/05_study_level_data.md:143 |  |  | Y | writer |
| sv20_p0057_a006 | §5.1.4.2 Trial Disease Assessments | knowledge_base/model/05_study_level_data.md:145 |  | Y |  | writer |
| sv20_p0057_a007 | §5.1.4.2 Trial Disease Assessments | knowledge_base/model/05_study_level_data.md:146 |  |  | Y | writer |
| sv20_p0057_a011 | §5.1.4.2 Trial Disease Assessments | knowledge_base/model/05_study_level_data.md:150 |  |  | Y | writer |
| sv20_p0058_a003 | §5.1.4.3 Trial Disease Milestones | knowledge_base/model/05_study_level_data.md:160 |  |  | Y | writer |
| sv20_p0058_a004 | §5.1.4.3 Trial Disease Milestones | knowledge_base/model/05_study_level_data.md:161 |  |  | Y | writer |
| sv20_p0058_a013 | §5.1.5 Trial Inclusion/Exclusion Criteria | knowledge_base/model/05_study_level_data.md:174 |  |  | Y | writer |
| sv20_p0058_a014 | §5.1.5 Trial Inclusion/Exclusion Criteria | knowledge_base/model/05_study_level_data.md:175 |  |  | Y | writer |
| sv20_p0059_a008 | §5.1.6 Trial Summary Information | knowledge_base/model/05_study_level_data.md:191 |  |  | Y | writer |
| sv20_p0059_a009 | §5.1.6 Trial Summary Information | knowledge_base/model/05_study_level_data.md:192 |  |  | Y | writer |
| sv20_p0064_a017 | §6.1 [Related Records Dataset] | knowledge_base/model/06_relationship_datasets.md:31 |  |  | Y | writer |
| sv20_p0064_a019 | §6.1 [Related Records Dataset] | knowledge_base/model/06_relationship_datasets.md:33 |  |  | Y | writer |
| sv20_p0064_a020 | §6.1 [Related Records Dataset] | knowledge_base/model/06_relationship_datasets.md:34 |  |  | Y | writer |
| sv20_p0065_a001 | §6.1 [Related Records Dataset] | knowledge_base/model/06_relationship_datasets.md:35 |  | Y |  | writer |
| sv20_p0065_a002 | §6.1 [Related Records Dataset] | knowledge_base/model/06_relationship_datasets.md:36 |  |  | Y | writer |
| sv20_p0068_a023 | §6.6 [Associated Persons Relationships] | knowledge_base/model/06_relationship_datasets.md:137 |  | Y |  | writer |

## CODE_LITERAL_IE (50)

| atom_id | 节 | kb_loc | det | rev | extra | src |
|---|---|---|:-:|:-:|:-:|---|
| ig34_p0017_a029 | §3.2.1 Dataset-level Metadata | knowledge_base/chapters/ch03_submitting_data.md:34 |  |  | Y | writer |
| ig34_p0017_a031 | §3.2.1 Dataset-level Metadata | knowledge_base/chapters/ch03_submitting_data.md:35 |  |  | Y | writer |
| ig34_p0017_a033 | §3.2.1 Dataset-level Metadata | knowledge_base/chapters/ch03_submitting_data.md:36 |  |  | Y | writer |
| ig34_p0017_a035 | §3.2.1 Dataset-level Metadata | knowledge_base/chapters/ch03_submitting_data.md:37 |  |  | Y | writer |
| ig34_p0017_a037 | §3.2.1 Dataset-level Metadata | knowledge_base/chapters/ch03_submitting_data.md:38 |  | Y |  | writer |
| ig34_p0018_a003 | §3.2.1 Dataset-level Metadata | knowledge_base/chapters/ch03_submitting_data.md:39 |  |  | Y | writer |
| ig34_p0018_a005 | §3.2.1 Dataset-level Metadata | knowledge_base/chapters/ch03_submitting_data.md:40 |  | Y |  | writer |
| ig34_p0018_a007 | §3.2.1 Dataset-level Metadata | knowledge_base/chapters/ch03_submitting_data.md:41 |  |  | Y | writer |
| ig34_p0018_a009 | §3.2.1 Dataset-level Metadata | knowledge_base/chapters/ch03_submitting_data.md:42 |  |  | Y | writer |
| ig34_p0018_a011 | §3.2.1 Dataset-level Metadata | knowledge_base/chapters/ch03_submitting_data.md:43 |  |  | Y | writer |
| ig34_p0018_a013 | §3.2.1 Dataset-level Metadata | knowledge_base/chapters/ch03_submitting_data.md:44 |  |  | Y | writer |
| ig34_p0018_a015 | §3.2.1 Dataset-level Metadata | knowledge_base/chapters/ch03_submitting_data.md:45 |  |  | Y | writer |
| ig34_p0018_a017 | §3.2.1 Dataset-level Metadata | knowledge_base/chapters/ch03_submitting_data.md:46 |  | Y |  | writer |
| ig34_p0018_a019 | §3.2.1 Dataset-level Metadata | knowledge_base/chapters/ch03_submitting_data.md:47 |  |  | Y | writer |
| ig34_p0018_a021 | §3.2.1 Dataset-level Metadata | knowledge_base/chapters/ch03_submitting_data.md:48 |  |  | Y | writer |
| ig34_p0018_a023 | §3.2.1 Dataset-level Metadata | knowledge_base/chapters/ch03_submitting_data.md:49 |  |  | Y | writer |
| ig34_p0018_a025 | §3.2.1 Dataset-level Metadata | knowledge_base/chapters/ch03_submitting_data.md:50 |  |  | Y | writer |
| ig34_p0018_a027 | §3.2.1 Dataset-level Metadata | knowledge_base/chapters/ch03_submitting_data.md:51 |  |  | Y | writer |
| ig34_p0018_a029 | §3.2.1 Dataset-level Metadata | knowledge_base/chapters/ch03_submitting_data.md:52 |  |  | Y | writer |
| ig34_p0018_a031 | §3.2.1 Dataset-level Metadata | knowledge_base/chapters/ch03_submitting_data.md:53 |  |  | Y | writer |
| ig34_p0018_a033 | §3.2.1 Dataset-level Metadata | knowledge_base/chapters/ch03_submitting_data.md:54 |  |  | Y | writer |
| ig34_p0018_a035 | §3.2.1 Dataset-level Metadata | knowledge_base/chapters/ch03_submitting_data.md:55 |  | Y |  | writer |
| ig34_p0018_a037 | §3.2.1 Dataset-level Metadata | knowledge_base/chapters/ch03_submitting_data.md:56 |  | Y |  | writer |
| ig34_p0018_a039 | §3.2.1 Dataset-level Metadata | knowledge_base/chapters/ch03_submitting_data.md:57 |  |  | Y | writer |
| ig34_p0018_a041 | §3.2.1 Dataset-level Metadata | knowledge_base/chapters/ch03_submitting_data.md:58 |  |  | Y | writer |
| ig34_p0018_a043 | §3.2.1 Dataset-level Metadata | knowledge_base/chapters/ch03_submitting_data.md:59 |  |  | Y | writer |
| ig34_p0018_a045 | §3.2.1 Dataset-level Metadata | knowledge_base/chapters/ch03_submitting_data.md:60 |  |  | Y | writer |
| ig34_p0018_a047 | §3.2.1 Dataset-level Metadata | knowledge_base/chapters/ch03_submitting_data.md:61 |  | Y |  | writer |
| ig34_p0018_a049 | §3.2.1 Dataset-level Metadata | knowledge_base/chapters/ch03_submitting_data.md:62 |  |  | Y | writer |
| ig34_p0018_a051 | §3.2.1 Dataset-level Metadata | knowledge_base/chapters/ch03_submitting_data.md:63 |  |  | Y | writer |
| ig34_p0019_a003 | §3.2.1 Dataset-level Metadata | knowledge_base/chapters/ch03_submitting_data.md:65 |  | Y |  | writer |
| ig34_p0019_a005 | §3.2.1 Dataset-level Metadata | knowledge_base/chapters/ch03_submitting_data.md:66 |  |  | Y | writer |
| ig34_p0019_a007 | §3.2.1 Dataset-level Metadata | knowledge_base/chapters/ch03_submitting_data.md:67 |  |  | Y | writer |
| ig34_p0019_a009 | §3.2.1 Dataset-level Metadata | knowledge_base/chapters/ch03_submitting_data.md:68 |  |  | Y | writer |
| ig34_p0019_a011 | §3.2.1 Dataset-level Metadata | knowledge_base/chapters/ch03_submitting_data.md:69 |  |  | Y | writer |
| ig34_p0019_a013 | §3.2.1 Dataset-level Metadata | knowledge_base/chapters/ch03_submitting_data.md:70 |  |  | Y | writer |
| ig34_p0019_a015 | §3.2.1 Dataset-level Metadata | knowledge_base/chapters/ch03_submitting_data.md:71 |  |  | Y | writer |
| ig34_p0019_a017 | §3.2.1 Dataset-level Metadata | knowledge_base/chapters/ch03_submitting_data.md:72 |  |  | Y | writer |
| ig34_p0019_a019 | §3.2.1 Dataset-level Metadata | knowledge_base/chapters/ch03_submitting_data.md:73 |  | Y |  | writer |
| ig34_p0019_a021 | §3.2.1 Dataset-level Metadata | knowledge_base/chapters/ch03_submitting_data.md:74 |  |  | Y | writer |
| ig34_p0019_a023 | §3.2.1 Dataset-level Metadata | knowledge_base/chapters/ch03_submitting_data.md:75 |  |  | Y | writer |
| ig34_p0019_a025 | §3.2.1 Dataset-level Metadata | knowledge_base/chapters/ch03_submitting_data.md:76 |  |  | Y | writer |
| ig34_p0019_a027 | §3.2.1 Dataset-level Metadata | knowledge_base/chapters/ch03_submitting_data.md:77 |  |  | Y | writer |
| ig34_p0019_a029 | §3.2.1 Dataset-level Metadata | knowledge_base/chapters/ch03_submitting_data.md:78 |  |  | Y | writer |
| ig34_p0019_a031 | §3.2.1 Dataset-level Metadata | knowledge_base/chapters/ch03_submitting_data.md:79 |  |  | Y | writer |
| ig34_p0019_a033 | §3.2.1 Dataset-level Metadata | knowledge_base/chapters/ch03_submitting_data.md:80 |  | Y |  | writer |
| ig34_p0019_a035 | §3.2.1 Dataset-level Metadata | knowledge_base/chapters/ch03_submitting_data.md:81 |  |  | Y | writer |
| ig34_p0019_a037 | §3.2.1 Dataset-level Metadata | knowledge_base/chapters/ch03_submitting_data.md:82 |  |  | Y | writer |
| ig34_p0019_a039 | §3.2.1 Dataset-level Metadata | knowledge_base/chapters/ch03_submitting_data.md:83 |  |  | Y | writer |
| ig34_p0063_a022 | §5.2 [Demographics (DM)] | knowledge_base/domains/DM/spec.md:194 |  |  | Y | writer |

## SPEC_TABLE_HEADER (24)

| atom_id | 节 | kb_loc | det | rev | extra | src |
|---|---|---|:-:|:-:|:-:|---|
| ig34_p0084_a007 | §5.4 [Subject Disease Milestones (SM)] |  |  |  | Y | writer |
| ig34_p0134_a003 | §6.2.1 [Adverse Events (AE)] |  |  |  | Y | writer |
| ig34_p0135_a001 | §6.2.1 [Adverse Events (AE)] |  |  |  | Y | writer |
| ig34_p0136_a001 | §6.2.1 [Adverse Events (AE)] |  |  |  | Y | writer |
| ig34_p0137_a001 | §6.2.1 [Adverse Events (AE)] |  |  | Y |  | writer |
| ig34_p0148_a019 | §6.2.3 [Clinical Events (CE)] |  |  |  | Y | writer |
| ig34_p0167_a0023 | §6.2.5 Healthcare Encounters (HO) |  |  |  | Y | writer |
| ig34_p0183_a007 | §6.3.2 Death Details (DD) |  |  |  | Y | writer |
| ig34_p0185_a023 | §6.3.3 ECG Test Results (EG) |  |  |  | Y | writer |
| ig34_p0186_a001 | §6.3.3 ECG Test Results (EG) |  |  |  | Y | writer |
| ig34_p0187_a001 | §6.3.3 ECG Test Results (EG) |  |  |  | Y | writer |
| ig34_p0188_a001 | §6.3.3 ECG Test Results (EG) |  |  |  | Y | writer |
| ig34_p0193_a006 | §6.3.4 Inclusion/Exclusion Criteria Not Met (IE) |  |  |  | Y | writer |
| ig34_p0195_a008 | §6.3.5.1 Generic Specimen-based Lab Findings Domain Specification | knowledge_base/domains/LB/assumptions.md:1 |  | Y |  | reviewer |
| ig34_p0252_a021 | §6.3.5.7.2 Microbiology Susceptibility (MS) |  |  |  | Y | writer |
| ig34_p0264_a004 | §6.3.5.8 Microscopic Findings (MI) |  |  |  | Y | writer |
| ig34_p0286_a020 | §6.3.7.2 Cardiovascular System Findings (CV) | knowledge_base/domains/CV/spec.md:1 |  | Y |  | writer |
| ig34_p0294_a017 | §6.3.7.4 Nervous System Findings (NV) |  |  | Y |  | writer |
| sv20_p0055_a002 | §5.1.3.2 Trial Repro Paths |  |  | Y |  | writer |
| sv20_p0056_a007 | §5.1.4.1 Trial Visits |  |  | Y |  | writer |
| sv20_p0057_a002 | §5.1.4.2 Trial Disease Assessments |  |  |  | Y | writer |
| sv20_p0058_a002 | §5.1.4.3 Trial Disease Milestones |  |  |  | Y | writer |
| sv20_p0058_a012 | §5.1.5 Trial Inclusion/Exclusion Criteria |  |  |  | Y | writer |
| sv20_p0059_a007 | §5.1.6 Trial Summary Information |  |  | Y |  | writer |

## EDITORIAL_META (14)

| atom_id | 节 | kb_loc | det | rev | extra | src |
|---|---|---|:-:|:-:|:-:|---|
| ig34_p0064_a011 | §5.2 [Demographics (DM)] |  |  |  | Y | writer |
| ig34_p0172_a0013 | §6.2.6 Medical History (MH) |  |  |  | Y | writer |
| ig34_p0193_a025 | §6.3.4 Inclusion/Exclusion Criteria Not Met (IE) |  |  |  | Y | writer |
| ig34_p0288_a018 | §6.3.7.2 Cardiovascular System Findings (CV) |  |  |  | Y | writer |
| ig34_p0320_a023 | §6.3.9.1 Functional Tests (FT) |  |  | Y |  | writer |
| sv20_p0002_a002 | §0 [TOC] |  |  |  | Y | writer |
| sv20_p0002_a003 | §0 [TOC] |  |  |  | Y | writer |
| sv20_p0002_a007 | §0 [TOC] |  |  |  | Y | writer |
| sv20_p0002_a011 | §0 [TOC] |  |  |  | Y | writer |
| sv20_p0002_a015 | §0 [TOC] |  |  |  | Y | writer |
| sv20_p0002_a029 | §0 [TOC] |  |  |  | Y | writer |
| sv20_p0002_a033 | §0 [TOC] |  |  |  | Y | writer |
| sv20_p0002_a036 | §0 [TOC] |  |  |  | Y | writer |
| sv20_p0002_a041 | §0 [TOC] |  |  | Y |  | writer |

## REDUNDANT_WITH_SPEC (11)

| atom_id | 节 | kb_loc | det | rev | extra | src |
|---|---|---|:-:|:-:|:-:|---|
| ig34_p0084_a018 | §5.4 [Subject Disease Milestones (SM)] |  |  |  | Y | writer |
| ig34_p0129_a005 | §6.1.6 [Substance Use (SU)] | knowledge_base/domains/SU/spec.md:3 |  |  | Y | writer |
| ig34_p0134_a002 | §6.2.1 [Adverse Events (AE)] | knowledge_base/domains/AE/spec.md:3 |  | Y |  | writer |
| ig34_p0137_a010 | §6.2.1 [Adverse Events (AE)] |  |  |  | Y | writer |
| ig34_p0148_a017 | §6.2.3 [Clinical Events (CE)] | knowledge_base/domains/CE/spec.md:2 |  |  | Y | writer |
| ig34_p0150_a004 | §6.2.3 [Clinical Events (CE)] |  |  |  | Y | writer |
| ig34_p0183_a006 | §6.3.2 Death Details (DD) | knowledge_base/domains/DD/spec.md:3 |  |  | Y | writer |
| ig34_p0183_a020 | §6.3.2 Death Details (DD) |  |  |  | Y | writer |
| ig34_p0185_a022 | §6.3.3 ECG Test Results (EG) | knowledge_base/domains/EG/spec.md:3 |  |  | Y | writer |
| ig34_p0296_a005 | §6.3.7.4 Nervous System Findings (NV) |  |  | Y |  | writer |
| ig34_p0310_a005 | §6.3.7.7 Respiratory System Findings (RE) |  |  |  | Y | writer |
