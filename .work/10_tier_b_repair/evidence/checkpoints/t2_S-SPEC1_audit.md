# T2S.S-SPEC1 Rule A 独立抽检 (auditor = `oh-my-claudecode:verifier`, attempt 1, 2026-11-26)

> verdict: **PASS** — 独有丢失 0 / 忠实度错误 0 (N=22). 先独立判, 判完才读 writer/reviewer 报告 (对照见末段). 只读 KB, 未 commit.

## 口径 (主控 spec-only 覆盖)
- P = 8 域 PDF spec 表全部变量行 (每变量 1 单元, 以 PDF 原页为准, 不依赖 pdf_atoms) + spec 表脚注段. CT C-code 记法 (U5) 与 DOMAIN CT 空 (U6) 不计.
- 页: CO p60 / DM p62-64 / SM p84 / SV p86-87 / CM p98-100 / ML p121-122 / SU p129-131 / BE p143-144 (BE 表无脚注: p144 表头有 Format¹ 但页内无脚注文本, KB 不补 = 正确).
- 独立解析器 (auditor 自写, 未用 writer/reviewer 脚本): `pdfspec.py` 读 `work/pdf_bbox/ig34_pNNNN.tsv`, 按表头词 xMin 分列, 续页沿用列位; `cmp.py` 对 KB `### VAR` 块 7 字段比对 (NFKC + 弯引号/dash 归一, 去空白). 脚本存 scratch `t2s_S-SPEC1_auditor/`.

## 全量机械比对 (211 变量, 全部 7 字段)
- 计数闸: CO 13/13, DM 32/32, SM 10/10, SV 16/16, CM 41/41, ML 37/37, SU 37/37, BE 25/25; 8 域变量顺序全等, Order 1..n 全对.
- 差异 56 条, 全部可归类: U6 DOMAIN CT 空 ×8; U5 C-code vs 括号短名 ×45; T-1 DM ETHNIC "guidance¹"(PDF)→"guidance²"(KB) ×1; T-2 SV SVSTDTC/SVENDTC "IS0"(PDF)→"ISO"(KB) ×2. 其余字段 (Label/Type/Role/Core/Notes 及全部 CT `*`) 0 差异.
- 脚注: CO/SM/SV/CM/ML/SU 脚注¹ 与 DM 脚注¹² 逐字 = PDF; 唯 DM 脚注² 去掉 URL 后孤立 ")" (T-3). 位置: 8 个 spec.md 均在最后变量块 `---` 之后、`## Cross References` 之前 (U7); CO/assumptions.md 只删脚注段 1 段 (MOVED 源), 无他改.
- 反向 KB→PDF (8 文件全文): 非字段行仅 `# XX — …` 标题、`> Class|Structure` 行、脚注段、Cross References 块 (U8 导航). 无出处且未 D6 的解释性内容 0; BE BECAT 原 KB 扩写 "(CDISC canonical examples…)" / sponsor-extensible 句已删, Notes = PDF p143 原文.

## 抽样 (可复跑; seed 20261126)
```
S=<scratch>/t2s_S-SPEC1_auditor; python3 -I $S/pdfspec.py $S/pdf.json && python3 -I $S/sample.py
# U = 211 变量 "DOM:VAR@pN" + 8 脚注 (CO/DM¹/DM²/SM/SV/CM/ML/SU); |P|=219
# C (writer 改动单元) = CT * 17 + DM Type 2 + BE BECAT + DM RACE/ETHNIC + SV SVSTDTC/SVENDTC + 脚注 8 = 32
# N = min(30, max(20, ceil(0.1*219))) = 22; rng=random.Random(20261126); s1 = rng.sample(sorted(C), ceil(N/3)=8); 余 14 = rng.sample(sorted(U - s1), 14)
```
P=219, C=32, N=22 (C 8 + 其余 14; 其余中又含 C 单元 SUDECOD/SUCLAS/SUCAT/MLTRT).

| # | 单元 | PDF 页 + 摘要 (渲染 130dpi 逐格) | KB file:line | 丢失? | 忠实? | 位置? | 说明 |
|---|---|---|---|---|---|---|---|
| 1 | SV:SVSTDTC | p87 Start Date/Time of Observation / Char / ISO 8601 datetime or interval / Timing / Exp; Notes "…IS0 8601 character format." | SV/spec.md:104 | 否 | 是 | 是 | T-2: PDF 数字 0 印刷错, 同表 CT 列可定 → KB "ISO" |
| 2 | DM:fn1 | p64 脚注¹ CT 星号说明 | DM/spec.md:294 | 否 | 是 | 是 | 逐字; 最后块后、Cross References 前 |
| 3 | BE:BEPARTY | p143 Accountable Party / Char / `*` / Record Qualifier / Perm; Notes 三句 | BE/spec.md:131 | 否 | 是 | 是 | CT `*` 照录 |
| 4 | ML:fn1 | p122 脚注¹ | ML/spec.md:339 | 否 | 是 | 是 | 逐字 |
| 5 | SM:MIDSTYPE | p84 Disease Milestone Type / Char / `*` / Record Qualifier / Req; Notes 例 "HYPOGLYCEMIC EVENT" | SM/spec.md:50 | 否 | 是 | 是 | CT `*` 照录 |
| 6 | CM:fn1 | p100 脚注¹ | CM/spec.md:375 | 否 | 是 | 是 | 逐字 |
| 7 | DM:ETHNIC | p63 Ethnicity / Char / (ETHNIC) / Record Qualifier / Perm; Notes "…FDA guidance¹ regarding…" | DM/spec.md:203 | 否 | 是 | 是 | T-1: 上标¹ 指 CT 脚注为 PDF 错, 脚注² 才是 FDA guidance (RACE 同句用 ²) → KB ²; CT C66790 = U5 |
| 8 | DM:RACE | p63 Race / Char / (RACE) / Record Qualifier / Exp; Notes "…guidance² … See assumption below regarding RACE." | DM/spec.md:194 | 否 | 是 | 是 | 上标 ² 照 PDF; C-code U5 |
| 9 | SU:SUDECOD | p129 Standardized Substance Name / Char / `*` / Synonym Qualifier / Perm; Notes 两句 | SU/spec.md:77 | 否 | 是 | 是 | |
| 10 | CM:CMSTRTPT | p100 Start Relative to Reference Time Point / Char / (STENRF) / Timing / Perm; Notes 含 "See Section 4.4.7, Use of Relative Timing Variables." | CM/spec.md:338 | 否 | 是 | 是 | C66728 = U5 |
| 11 | SU:SUCLAS | p129 Substance Use Class / Char / `*` / Variable Qualifier / Perm; Notes 含 Section 4.2.8.3 引用 | SU/spec.md:140 | 否 | 是 | 是 | |
| 12 | SU:SUCAT | p129 Category for Substance Use / Char / `*` / Grouping Qualifier / Perm; 例 TOBACCO/ALCOHOL/CAFFEINE | SU/spec.md:86 | 否 | 是 | 是 | |
| 13 | CO:RDOMAIN | p60 Related Domain Abbreviation / Char / (DOMAIN) / Record Qualifier / Perm; Notes 两句 | CO/spec.md:23 | 否 | 是 | 是 | C66734 = U5 |
| 14 | CM:CMCLAS | p98 Medication Class / Char / 空 / Variable Qualifier / Perm; Notes 含 4.2.8.3 引用 | CM/spec.md:149 | 否 | 是 | 是 | PDF CT 空 = KB 空 |
| 15 | DM:SEX | p63 Sex / Char / (SEX) / Record Qualifier / Req; "Sex of the subject." | DM/spec.md:185 | 否 | 是 | 是 | C66731 = U5 |
| 16 | DM:COUNTRY | p64 Country / Char / 空 / Record Qualifier / Req; Notes 两段 (ISO 3166-1 Alpha-3; US FDA) | DM/spec.md:266 | 否 | 是 | 是 | 段落合并 (空白差) 不计 |
| 17 | CM:TAETORD | p99 Planned Order of Element within Arm / Num / 空 / Timing / Perm | CM/spec.md:257 | 否 | 是 | 是 | |
| 18 | ML:MLTRT | p121 Name of Meal / Char / `*` / Topic / Req | ML/spec.md:59 | 否 | 是 | 是 | |
| 19 | SV:SVOCCUR | p86 Occurrence / Char / (NY) / Record Qualifier / Exp | SV/spec.md:59 | 否 | 是 | 是 | C66742 = U5 |
| 20 | CM:CMDOSRGM | p99 Intended Dose Regimen / Char / 空 / Record Qualifier / Perm; 例 "TWO WEEKS ON, TWO WEEKS OFF" | CM/spec.md:221 | 否 | 是 | 是 | |
| 21 | ML:MLTPTNUM | p122 Planned Time Point Number / Num / 空 / Timing / Perm | ML/spec.md:275 | 否 | 是 | 是 | |
| 22 | SU:SUDOSTOT | p130 Total Daily Consumption / Num / 空 / Record Qualifier / Perm; Notes 两句 (supplemental qualifier) | SU/spec.md:203 | 否 | 是 | 是 | |

**独有丢失 0 / 忠实度错误 0 → PASS.**

## 另查
- gaps (DM/SM/SV/CM/ML/SU fn 原子) 全部落地, 逐字 + U7 位置 ✓; footnote_moves CO assumptions→spec MOVED ✓ (先插后删, assumptions 仅删该段); intros 空.
- 授权范围: `git diff HEAD --stat` 本批仅 8 spec.md + CO/assumptions.md (-2 行, 仅脚注段).
- PDF_TYPO 3 条 (T-1 ETHNIC 上标 / T-2 IS0 / T-3 DM 脚注² 孤立 ")") 均渲染核实 PDF 原样, 正确值可由 PDF 自身确定, 已登记于 writer checkpoint; "Services;2016" 照录 = PDF.
- G-TB8: trace 373/377 writer `oh-my-claudecode:executor` subagent_done (含 delta), 381 reviewer `oh-my-claudecode:code-reviewer` PASS (晚于 delta, 终态已审); 无 main 写 KB 记录 ✓.
- `python3 tools/check_links.py 2>&1 | grep "live docs"` → live docs: 42 (= 基线).

## 与 writer / reviewer 对照 (判完后读)
- 计数闸 8 域数字与两报告一致; 差异归类 (U5/U6/T-1/T-2/T-3) 一致; BE BECAT 终态 D2 删除 (主控裁定) 与本审 KB=PDF 原文一致; D6 = 0 一致. 无分歧.
