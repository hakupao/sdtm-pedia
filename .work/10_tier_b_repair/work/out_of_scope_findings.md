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
| O19 | T2 B-ch04 review L8 | ch04:1534-1536 Appendix 引导段 | "Appendix: Cross-References to Chapter 6 Examples" 引导句为 KB 自写未标 D6; 内容属 p115/p261 → 并入 O16 sweep 或 ch04 收尾小批 (S-CH4 已关闭: D2 去重为交叉引用) |
| O20 | T2 B-FA writer | 各批 pdf_ranges | B-FA pdf_ranges 从 p364 起, 漏了 §6.4 引言/§6.4.1 (p361-363), T1 从未分诊 → T3 前全检: 每个 KB 文件对应 PDF 节的完整页范围 vs 已分诊页, 漏页的补扫 |
| O21 | T2 B-FA writer | FA/spec.md (p365-366) | 不在任何批 kb_files, 未核 → 并入 O15 spec 扫描 |
| O22 | T2 B-FA writer | ledger targets | FA §6.4.2/§6.4.3 原子 targets 仍指 ch02/model02 (24 条) → T3 回写时 target 改为 FA/assumptions.md |
| O23 | T2 B-OE writer | OE/assumptions.md | 缺 p298 Description/Overview 句 + p299 spec 首句 → 并入 O16/O17 sweep |
| O24 | T2 B-REL writer | 全库 spec.md 记法 | IDVAR 等 CT 列 "*" 写成空; codelist 名用 C-code; spec 表脚注 ¹ 缺失 — 全库 spec.md 共性 → 并入 O15 spec 扫描 (先定统一口径再改) |
| O25 | 主控 | T4 汇总 | 各批 checkpoint 中 '照录 + T4' 项分散登记 → T4.2 前生成 evidence/checkpoints/t4_user_decisions.md 汇总表 (批次 / 位置 / PDF 原值 / 候选值 / 依据) |
| O26 | T2 B-RP review | 全库 domains/*/spec.md | (已点名 DM/ML/CM/BS/SV/IE/QS/FT 等; 注意 GF/CO 先例放置位置须统一) spec 表脚注 0/64 域收录 → O15 spec 扫描 (与 O24 合并) |
| O27 | B-TE writer | work/t2_batches/B-TE.json | pdf_ranges 写 404-409, TE 实际 p402-407 (O20 同类) |
| O28 | B-BE review | BE/examples.md Ex2 bs Row1 | BSORRES 12 mL vs BSSTRESN 6: KB=PDF, PDF 自身无法定对错 → T4 用户裁定项 (并入 O25 汇总) |
| O29 | 主控 (B-MK review fp) | fp_regress 全量 48 条 | 未入 errata 的: p0174_a0012, p0363_a011-a019 / p0364_a001-a019 (B-FA §6.4.2), p0396_a009 (B-TA) — 均为已提交批, T3 ledger 回写时逐条定 REMAP/ATOM_ERR |
| O30 | B-RE writer | RE/assumptions.md:17 (assumption 3) | 缺 "variables" 一词 (PDF "Any Identifier variables, Timing variables"); assumptions 列表错 → 主控授权 B-RE a2 已补 (关闭) |
| O31 | B-NV writer | p285 §6.3.6 MO "Domain Decommissioning Update" 框 | 全 KB 无; 无 MO 域目录 → 与 O17 §6.x 类引言扫描同批定宿主 (候选: NV/assumptions.md §6.3.7 前单列 §6.3.6 节) |
| O32 | B-SM review | SM/examples.md p85 Row1 叙述 "SMDY" | 非 SM 变量 (疑 SMSTDY), PDF 自身不能唯一确定 → KB 照录, T4 用户裁定项 (并入 O25) |
| O33 | B-SM audit | SV/assumptions.md Description/Overview | 缺 p86 a003-a007 + 改义改写 → 已写入 B-SV notes (通用授权内修) |
| O34 | B-DM writer | DM/spec.md p64 spec 表 FDA 脚注 2 (REAL_GAP ig34_p0064_a012) + B-DM.json pdf_ranges 漏 p79 | 脚注 → O26 spec 脚注扫描 (DEFERRED); 页范围 O20 同类 |
| O35 | B-model05 writer | model/05_study_level_data.md | T4 用户裁定: (1) 既有标题缺 PDF 节号/原名、层级扁平 (规则 6 未改); (2) TT/TP "Notes" 列实为 Usage Restrictions; (3) TS 缺 Usage Restrictions "Not in nonclinical trials" (R1 缺列不补); (4) Role 括注不统一 |
| O36 | B-TS writer | fp_match / coverage ledger 全局 | EQUIVALENT 判得过宽: TS §7.4.2.1 语义不同的 KB 改写句被判 EQUIVALENT (他批可能同样) → T3/T4: 对 ledger EQUIVALENT 原子做语义抽检 (Rule A), 不只看 hit_target |
| O37 | B-TS writer | R4 IE 清单 ig34_p0425_a003 (NullFlavor NA 行) | IE 理由误为 spec 表行; 实为 TS NullFlavor 表行 → 主控裁补入 (覆盖 IE), T3 回写 ledger |
| O38 | B-model06 writer | model/06_relationship_datasets.md | T4 用户裁定: (1) 6.1-6.7 标题与 H1 不同于 PDF (6.6 KB "Related Subjects" vs PDF "Relationships"; 规则 6 未改); (2) Role 括号约定: RELSPEC "(REFID)" 有而 SUPP-- QLABEL 无 "(QNAM)"; (3) RELREC USUBJID/POOLID Notes 为 KB 自写 (PDF 空) 但属 R1 IE 行, 未加 D6 (主控维持 M-2a); (4) RELREC APID Notes 格截断 (缺 POOLDEF 句, 同属 R1 IE 行, B-model06 audit) |
| O39 | B-DA writer | p180 §6.3 "Models for Findings Domains" 章引言 2 句 | 全 KB 无逐字对应 → 并入 O17 §6.x 类引言扫描 (与 §6.1/§6.2 章引言统一定宿主) |
| O40 | B-FT writer / 多批 | 全库引号/撇号/破折号风格 | PDF 弯引号/en dash vs KB 直引号/hyphen 普遍不一致 (B-MK L-2, B-NV, B-DD F-2); B-RS QRS 副本已改弯引号, FT/QS 副本仍直引号 → T4 用户定全局口径后统一 (逐词内容已一致); 含省略号 '…' vs '...' 与 en dash (B-SUPPQUAL/ch08 §8.4 'Scale–Cognitive') |
| O41 | B-model06 review | model/06_relationship_datasets.md:50 RELTYPE Combinations 表 (D6) + Summary 表 SUPP-- Subject-level "Yes" | KB 自写表按记录级解释 RELTYPE 并列 MANY/ONE, 与 SDTMIG ch08 (数据集级, 3 种组合) 不一致 → T4: 改为指向 ch08 交叉引用或删; Summary "Yes" 为简化 |
| O42 | B-CE review | 全库 CRF 选项符号 | ○→`( )` / □→`[ ]` 映射 (CE) vs FA 保留 "○" 原样, 口径不统一 → T4 / O40 同批定 |
| O43 | B-MI review | MI/examples.md:23 "is a represented in a derived record" | PDF 原句语法错, 不可唯一确定 → KB 照录, T4 用户裁定项 |
| O44 | B-CE review a2 | CE/examples.md USUBJID `ABC -US-701-002` ×8 (T-2) + supp `001-001` (T-3) | T4 用户裁定; T-2 登记中 "间隙<3.5pt 疑为字距" 依据实测不成立 (与正常词间隙同), T4 汇总时改措辞; fp p153-155 8 条回归 = 照录预期, 待 T4 后更正原子 |
| O45 | B-CM audit | p103 §6.1.3 Exposure Domains 父节引言 (ig34_p0103_a021/a022) | 全 KB 0 命中 → 并入 O17 §6.x 类引言扫描 (候选宿主 EX/assumptions.md 顶部, NV/FT 先例); 另: CM spec 脚注 ledger 误记 EQUIVALENT → 佐证 O36 |
| O46 | B-DI writer | p441 §9 章引言 ("There are occasions…" + 2 bullet) | 已在 ch10_appendices.md:66-69; DI/OI 域文件未收 → 并入 O17 (DI/OI 一起定是否加交叉引用); model/05:257 附近 §9 bullet 未核 |
| O47 | B-TV writer | B-TE audit 称 §7.3 引言在 TI/assumptions.md | 不准确: §7.3 引言在 TV/assumptions.md:3-11, TI 仅 §7.4/§7.5; B-TV.json pdf_ranges 409-412 应为 407-410 (O20 同类) |
| O48 | B-TI writer | TI/assumptions.md §7.4 标题 + census_full_manifest | §7.4 标题与 PDF "(TI and TS)" 不同 (规则 6 未改, T4); census_full_manifest TI/TM 页范围偏移 (TI 实为 p416-417); B-TS 报 p417 ti.xpt PDF_ONLY 为 manifest 假阳 (TI census OK) |
| O49 | B-CE audit | p155 DS Description/Overview 句 | DS 三文件均无 → O16 全域 Description 扫描点名 DS |
| O50 | B-SU audit | p133 §6.2 "Models for Events Domains" 章引言 + 域列表 (a011-a018) | KB 无对应节引言 → 并入 O17 §6.x 类引言扫描 (与 O39 §6.3、O45 §6.1.3 同批) |
| O51 | B-TV writer/review | TV/examples.md Mermaid (及 T2 期间新/改的全部 Mermaid: TA/DM/model05/TV) | agent 环境 mermaid-cli 权限被拒, 仅语法对照核 → T4 前用渲染器 (或 web build) 统一渲染一次确认无语法错 |
| O52 | B-SC review | SC/examples.md p342 Ex2 Row 3 SCDTC 2017-06-10 vs SCDY 297 | PDF 自身矛盾 (推算应 296), KB 照录 → T4 用户裁定项 |
| O53 | B-ch03 writer/review | ch03 数据集表 T-3 UR "per per" / T-4 ISSCMBCL | 照录 PDF → T4 用户裁定 (T-4 候选: p456 IS 新增变量 ISMSCBCE, PDF 自身不足断定); O5 已在本批关闭 |
| O54 | 主控 (S-EVT 关闭) | O8 / O15 / O18 / O49 / O50 | S-EVT (T2S 试点) 内已处理, 关闭 (证据 `evidence/checkpoints/t2_S-EVT.md`) |
| O55 | S-FND review L1 | UR/spec.md:3 Structure 行 "per per" | 与 UR spec 首句 U-1 同源; T4 用户裁 U-1 时两处一并改 (O25 汇总) |
| O56 | S-SPC2 audit 观察 1 | PP/examples.md "RELREC Method Quick Reference (PP-side view)" 整节 | KB 自写摘要 (含 Method 映射表), 与 PC/examples.md 内容部分重复; 本批按主控裁定 D6 整节保留. 备选 = dispatch notes "KB 自写摘要与 PDF 重复 → 一行交叉引用". T4 用户裁定 (O25 汇总) |
| O57 | S-SPC2 audit 观察 2 | pdf_atoms p252_a011 / p271_a011 / p276_a008 / p278_a051 | 原子抽取错, KB 与渲染一致 → T3 t3_atom_err |
| O58 | S-SPREL writer | SE spec 脚注原子 ig34_p0080_a010 抽成 `*In…` | 覆盖矩阵 SE fn 0/1 为原子抽取错假阳 (KB 已承载脚注); T3 t3_atom_err + 矩阵终版判读时豁免 |
| O59 | S-CH8 writer | S-TYPO 范围补充 | (1) em dash 两侧空格按 PDF 去掉 (如 SUPPQUAL/examples.md 同句); (2) spec 表脚注上标写法 `^1^` / `1In` → PDF 原字符 ¹ (全库统一); 均归 S-TYPO 脚本 |
| O60 | 主控 (S-MOD3) | KB 自拟标题 vs PDF 原标题口径不一 | S-MOD2/S-MOD3 在 0 入站链接时已改为 PDF 原标题; 先前按规则 6 保留的 TA §7.1/§7.2 (X-4)、FA §6.4.4 合并标题、MB H2 "and"、SS `#####` 层级等 → T4 统一处理 (或 S-TYPO 后一次性脚本 + 抽检) |
| O61 | S-SPEC1 review | 原子 ig34_p0122_a015 文本 "CDISC/NCIBI" | PDF 原文 "CDISC/NCI", KB 正确 → T3 t3_atom_err |
