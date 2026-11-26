# 范围外发现 (T1.4 时并入批次表)
| # | 来源 | 位置 | 问题 |
|---|---|---|---|
| O1 | T0 census | PC/assumptions.md pp.xpt; PC/examples.md; PP 表头 | 42 处 DIFF 落在 ledger 标 EXACT/EQUIV 的原子上 (整列错位, DYIDRGX_A→DY1DRGX_A, PPRFDTC→PPRFTDTC) → B-PCPP 整表逐格 |
| O2 | T1.1 | SUPPQUAL/examples.md:12-13 | AEOSP / "Clinically Medically Important SAE" / AETRTEMA; PDF p433 为 AESOSP / Other Medically Important SAE / AETRTEM |
| O3 | T1.1 | ig34_p0043_a015 | ledger 标 EQUIVALENT, KB 漏 --STRF 限制 (Q9 实证: 旧 EXACT/EQUIV 标签不可信) |
| O4 | T1.1 | spec NOT_FOUND | 变量名疑似笔误 MLGRID / CEBODYSYS / TAEFORD |
| O5 | T1.2 lane C | ch03 数据集表 Keys 列 | BE/EG/FT/IS/RS (除 CO 外) 与 PDF 不一致; 仅 KB→PDF 单向, p20 未覆盖 |
| O6 | T1.2 lane C | EG Example 1 (原记 Ex3, B-EG writer 更正) | 整表损坏 (日期 / EGXFN / EGNAM / EGTESTCD) |
| O7 | T1.2 lane C | IS Examples 4-8 | Ex5/6 多格错; Ex7 表头 ISTCND; Ex4/Ex8 表头多列 |
| O8 | T1.2 lane C | AE assumption 7c / AE Example 5 | AEOSOSP→AESOSP; STUDYID T992→T002 (Ex5 仅确认此一处) |
| O9 | T1.2 lane D | MB/examples.md | 两份 Ex1-3 重复 (行 1-170 / 171-400), 各有不同错 → 去重 + 逐格 |
| O10 | T1.2 lane B | EX Ex6/Ex7, FA, TA Ex5/Ex7, CE Ex2, CP Ex1b | 系统错值 (见 t1_lane_notes § lane B) |
| O11 | T1.3 C | ig34_p0139_a010 | KB 把 "…/etc." 扩写成 6 项 (超出 PDF) |
| O12 | T1.3 D | ch04:879 | PDF p42 Week 1 VISITDY / LBDY = 7, KB 两格空 |
| O13 | T2 B-TR audit | domains/VS | ig34_p0358_a014 VS Description/Overview 定义句 VS 域文件无 (仅 terminology general_part4.md:239); ledger EQUIVALENT 疑配到术语表 → B-VS 补 |
| O14 | D6 | PP/examples.md (B-PCPP 已提交) | KB_AUTHORED 保留项需回补 `> KB note (not in SDTMIG):` 标注 → 后续小批 |
| O15 | T2 B-AE writer | domains/AE/spec.md | AE spec 首句 (ig34_p0134_a002) 与 spec 表脚注 (ig34_p0137_a010) AE 三文件皆无 → 应补 spec.md (各域 spec 首句/脚注可能普遍缺, T3 前做一次全域扫描) |
| O16 | T2 多批 | 各域 assumptions.md | Description/Overview 句缺失是系统性问题 (VS O13, EG, 及 T1 已知 MI/IE/RP/TI/CE/SM): T3 前对 63 域做一次全域扫描, 各批未覆盖者开 B-DESC 小批 |
| O17 | T2 B-EG audit | 各域 spec 首句 | D3 的 5 条 R4-blocked 数据集标题行 (CE/EG/DD/SU/AE) 按新口径应补进 assumptions.md; AE 已在 B-AE 补, 其余 4 域 (含 ig34_p0185_a022 EG) 并入 O15/O16 全域扫描; 届时 D3 对这 5 条的 IE 改为 PRESENT |
| O18 | T2 B-AE audit | §6.x 各观察类引言 | p133 §6.2 Events 类引言句 + 7 项域列表全 KB 无 (triage 未收); 对 §6.1/6.2/6.3/6.4 等类引言做全库扫描, 并入 O16 sweep, 归属按 PDF 节 (候选 chapters/ 或 model/) |
| O19 | T2 B-ch04 review L8 | ch04:1534-1536 Appendix 引导段 | "Appendix: Cross-References to Chapter 6 Examples" 引导句为 KB 自写未标 D6; 内容属 p115/p261 → 并入 O16 sweep 或 ch04 收尾小批 |
| O20 | T2 B-FA writer | 各批 pdf_ranges | B-FA pdf_ranges 从 p364 起, 漏了 §6.4 引言/§6.4.1 (p361-363), T1 从未分诊 → T3 前全检: 每个 KB 文件对应 PDF 节的完整页范围 vs 已分诊页, 漏页的补扫 |
| O21 | T2 B-FA writer | FA/spec.md (p365-366) | 不在任何批 kb_files, 未核 → 并入 O15 spec 扫描 |
| O22 | T2 B-FA writer | ledger targets | FA §6.4.2/§6.4.3 原子 targets 仍指 ch02/model02 (24 条) → T3 回写时 target 改为 FA/assumptions.md |
| O23 | T2 B-OE writer | OE/assumptions.md | 缺 p298 Description/Overview 句 + p299 spec 首句 → 并入 O16/O17 sweep |
