# T2 B-EX auditor report — attempt 1
> auditor: oh-my-claudecode:verifier (opus), 2026-11-26; 独立判定 (先判后对照 writer/reviewer). 未改 KB. scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/7fe38595-6d99-4b86-881d-0dfb0d270167/scratchpad/t2_B-EX_auditor/`

## 抽样
- 命令: `subagent_prompts/t2_auditor_v1.0.md` 抽样脚本原样 (b=B-EX, seed=20261126; 仅 S 改到 scratchpad, 按 dispatch notes)
- 结果: C=0 (本批 10 atoms 全 TABLE_ROW), P=36, N=10 → 全部从 P−C 对照抽
- 样本: p0119_a028, p0119_a012, p0112_a001, p0112_a030, p0118_a018, p0117_a007, p0118_a020, p0117_a003, p0119_a022, p0119_a011

| # | atom_id | PDF 页:行 + 摘要 | KB file:line | 丢失? | 忠实? | 位置? | 说明 |
|---|---|---|---|---|---|---|---|
| 1 | ig34_p0119_a028 | p119 Ex8: EC dataset shows administrations as collected | EX/examples.md:431 | 否 | 是 | 是 (Ex8, CRF 后) | 逐字 |
| 2 | ig34_p0119_a012 | p119 Rows 4-6: many-to-one-to-one EC/EX/VS via --LNKGRP | :403 | 否 | 是 | 是 (relrec 前) | 逐字 |
| 3 | ig34_p0112_a001 | p112 relrec one-to-one dataset-level EC↔EX via --LNKID | :50 | 否 | 是 | 是 (Ex1 末) | 逐字 |
| 4 | ig34_p0112_a030 | p112 sponsor 视 3 次注射为单次给药; EXLOC="ABDOMEN" 因 "this location" 共有; 引 §4.2.8.3 | :92 | 否 | 是 | 是 (Ex2 ec 后) | 本批把 "the location" 恢复为 PDF "this location" |
| 5 | ig34_p0118_a018 | p118 Rows 2,4: 实际给药量 mL, ECMOOD PERFORMED, 剂量+浓度 | :362 | 否 | 是 | 是 | 逐字 |
| 6 | ig34_p0117_a007 | p117 CRF 为受试者 ABC123-0201, 体重 55 kg | :329 | 否 | 是 | 是 (Ex7, 本批拆成 PDF 的独立段) | 逐字 |
| 7 | ig34_p0118_a020 | p118 Row 6: 未给药剂量 | :364 | 否 | 是 | 是 | 逐字 (同行续句 ECREASOC/ECDOSE null 亦在) |
| 8 | ig34_p0117_a003 | p117 EX dataset shows unblinded administrations | :290 | 否 | 是 | 是 | 本批把 Rows 1-12/13-24 移到此句后 = PDF p117 顺序 |
| 9 | ig34_p0119_a022 | p119 Ex8: 100 mg 片每日; 起止+偏离; 与现行 CDASH 不一致 | :418 | 否 | 是 | 是 | 逐字 |
| 10 | ig34_p0119_a011 | p119 Rows 1-3: one-to-one-to-one PERFORMED EC/EX/VS via --LNKID | :401 | 否 | 是 | 是 | PDF 多余 ", ." 去掉 (T-2 已登记), 不算改义 |

- **独有丢失 0, 忠实度错误 0** (样本 10/10 PASS)

## 表格单元格复核 (渲染 p116/p117/p118 @110dpi, 本人目视; 抽样 seed 20261126 从 3 表全格随机)
| 表 | KB 行 | Row | 列 | KB 值 | PDF | 判 |
|---|---|---|---|---|---|---|
| Ex7 ec | :372 | 3 | ECPSTRGU | (空) | 空 | OK |
| Ex6 ex | :323 | 24 | EXTPTREF | STD BREAKFAST | 同 | OK |
| Ex6 ec | :268 | 4 | ECTRT | BOTTLE 2 | 同 | OK |
| Ex6 ec | :273 | 9 | ECPRESP | Y | 同 | OK |
| Ex6 ex | :306 | 7 | EXDOSFRQ | QD | 同 | OK |
| Ex6 ex | :310 | 11 | EXDOSE | 0 | 同 (PLACEBO) | OK |
| Ex6 ec | :288 | 24 | STUDYID | 56789 | 同 (p117) | OK |
| Ex6 ex | :306 | 7 | EXTPT | 30 MINUTES PRIOR | 同 | OK |
| Ex6 ec | :275 | 11 | ECSTDTC | 2002-07-11T07:34 | 同 | OK |
| Ex6 ex | :319 | 20 | EXSTDY | 9 | 同 | OK |
- 3 表每行列数 = 表头列数 (脚本 assert 通过); 表头列序与 PDF 一致 (Ex6 ex 含 EXELTM; Ex7 ec VISITNUM/VISIT/EPOCH 顺序; Ex2 ec 补 VISITNUM). 另目视 Ex6 ex 24 行 EXTRT/EXDOSFRM/EPOCH 与 p117 全一致.
- **Ex7 CRF (p118) 勾选项全核**: V1 = 10 mg/kg, Yes; V2 = 7.5 mg/kg, Dose-limiting toxicity, Yes, Injection site reaction; V3 = 7.5 mg/kg, No, Other specify: Personal reason. KB :341-356 粗体与之完全一致, 未勾选项均非粗体 (旧 KB "Injection site reaction / Personal reason" 错位已纠正).

## 删除行核对
`git diff 470b473 -- knowledge_base/domains/EX/` 51 删除行 = 头注改 D6 KB note 前缀 1, CRF 标签 2 (Ex1 "Exposure CRF:" p111 / Ex2 "Exposure CRF" p112), Ex2 ec 表头+3 行 (+VISITNUM), Ex2 叙述句 1 ("this location"), Ex6 CRF 表头 4, Ex6 Rows 1-12/13-24 说明 (移至 "The EX dataset shows…" 后, 非删除), Ex6 ec 12 行 (ECDOSFRM), Ex6 ex 表头+8 行 (→24 行), Ex7 引言 1 (拆两段, 文字未变), Ex7 CRF 表 6 行 (重建), Ex7 ec 表头+6 行. 无其他内容被删.

## 回归
- `python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl` → 全局 13 regress (p215 1 / p257 1 / p258 6 / p260 2 / p263 3, 均他批), **EX p104-120 = 0**.

## G-TB8
- trace.jsonl: T2.B-EX writer `oh-my-claudecode:executor` subagent_done ×2 (行 65, 67), reviewer `oh-my-claudecode:code-reviewer` PASS (行 70); 无 `agent: main` 写 EX KB 记录. PASS.

## 观察 (不计 FAIL)
- p118 Rows 1,3,5 "Scheduled dose is represented in mg/mL" (KB :360 照录 PDF) 与同句 "(mg/kg)" 及 ECDOSU=mg/kg 矛盾, 疑 PDF 印刷错, writer 未登记 T-n; 建议主控 T4 补登.
- 对照 writer/reviewer 报告 (判后): T-1..T-5 与本人所见一致; T-5 EXENDTC 全空照录 PDF 正确 (p117 列空).

## 结论: **PASS** (丢失 0, 忠实 0; 10 格 0 错; CRF 勾选全一致; EX fp 回归 0)
