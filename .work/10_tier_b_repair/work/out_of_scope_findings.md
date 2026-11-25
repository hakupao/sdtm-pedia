# 范围外发现 (T1.4 时并入批次表)
| # | 来源 | 位置 | 问题 |
|---|---|---|---|
| O1 | T0 census | PC/assumptions.md pp.xpt; PC/examples.md; PP 表头 | 42 处 DIFF 落在 ledger 标 EXACT/EQUIV 的原子上 (整列错位, DYIDRGX_A→DY1DRGX_A, PPRFDTC→PPRFTDTC) → B-PCPP 整表逐格 |
| O2 | T1.1 | SUPPQUAL/examples.md:12-13 | AEOSP / "Clinically Medically Important SAE" / AETRTEMA; PDF p433 为 AESOSP / Other Medically Important SAE / AETRTEM |
| O3 | T1.1 | ig34_p0043_a015 | ledger 标 EQUIVALENT, KB 漏 --STRF 限制 (Q9 实证: 旧 EXACT/EQUIV 标签不可信) |
| O4 | T1.1 | spec NOT_FOUND | 变量名疑似笔误 MLGRID / CEBODYSYS / TAEFORD |
| O5 | T1.2 lane C | ch03 数据集表 Keys 列 | BE/EG/FT/IS/RS (除 CO 外) 与 PDF 不一致; 仅 KB→PDF 单向, p20 未覆盖 |
| O6 | T1.2 lane C | EG Example 3 | 整表损坏 (日期 / EGXFN / EGNAM / EGTESTCD) |
| O7 | T1.2 lane C | IS Examples 4-8 | Ex5/6 多格错; Ex7 表头 ISTCND; Ex4/Ex8 表头多列 |
| O8 | T1.2 lane C | AE assumption 7c / AE Example 5 | AEOSOSP→AESOSP; STUDYID T992→T002 (Ex5 仅确认此一处) |
| O9 | T1.2 lane D | MB/examples.md | 两份 Ex1-3 重复 (行 1-170 / 171-400), 各有不同错 → 去重 + 逐格 |
| O10 | T1.2 lane B | EX Ex6/Ex7, FA, TA Ex5/Ex7, CE Ex2, CP Ex1b | 系统错值 (见 t1_lane_notes § lane B) |
| O11 | T1.3 C | ig34_p0139_a010 | KB 把 "…/etc." 扩写成 6 项 (超出 PDF) |
| O12 | T1.3 D | ch04:879 | PDF p42 Week 1 VISITDY / LBDY = 7, KB 两格空 |
