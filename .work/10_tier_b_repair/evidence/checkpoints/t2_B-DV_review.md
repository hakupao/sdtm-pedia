# T2 B-DV reviewer

## attempt 1 (2026-11-26, oh-my-claudecode:code-reviewer / opus)

**verdict: PASS** (KB 内容) + 1 条 evidence 勘误 E-1 (writer checkpoint 的 fp 结论表述错误, 不涉及 KB; 主控 commit 前在 `t2_B-DV.md` 追加勘误即可)

### 范围 / 无副作用
- `git diff HEAD -- knowledge_base/domains/DV/` = assumptions.md +10 行 (纯插入) / examples.md 2 行替换; spec.md 未动. `git status --short knowledge_base/` 中 DV 以外改动 (CE/CM/CO/HO/IE/MI/ML) 属他批.
- assumptions.md 改动仅为主控授权项 (Description/Overview、spec 首句、PDF 原有小标题 `DV – Assumptions`); assumptions 1-3 未动. 无节引言 NOTE (p178 `6.2.7 Protocol Deviations (DV)` 后直接 `DV – Description/Overview`).
- 页范围: p178 中部 (上半为 MH Ex 末表) - p179 末 (References); p180 起 6.3. 同 writer.

### 命令 (可复跑, S=scratchpad/t2_B-DV_reviewer)
```
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json
#  -> KB tables: 1; status: {'OK': 1}; cells compared: 36; diffs: 0 ; exit 1 (全局 PDF_ONLY 338; p178-179 内仅 p178 mh.xpt = MH 批, 非本批)
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl
#  -> RESULT: RED (60 条全局); p178/179 仅 ig34_p0179_a0018 (见 E-1); p178-179 43 原子 verdict 计数 EXACT 19 / INTENTIONAL_EXCLUDE 19 / EQUIVALENT 5, 与 baseline 0 变化
python3 tools/check_links.py 2>&1 | grep "live docs"   # live docs: 42
pdftotext -f 178 -l 179 -layout "source/cdisc/SDTMIG v3.4 (no header footer).pdf" -
pdftoppm -f 179 -l 179 -r 130 -png <PDF> $S/p179   # 渲染图逐格核
```

### 问题表
| ref | 检查项 | 问题 | 证据 |
|---|---|---|---|
| E-1 (writer checkpoint "PDF_TYPO" 段注 + "fp 回归" 段) | 证据准确性 (MEDIUM, HIGH conf) | writer 称 a0018 "fp 改后仍 EXACT (matcher 忽略标点), 无回归". 实测: `norm()` 不去句点; fp_after 中 a0018 `hit_target: null, hit_any: null` (baseline hit_target = DV/examples.md), 即真实回归; `verdict` 字段为继承值不反映命中. 回归成因 = 原子抽取丢句点 (baseline 与 after 均 `in_pdf_page: false`, 即原子文本本就与原页不符), KB 现值与 PDF 一致 → 回归可接受, 但 writer 表述须勘误 | `grep '"ig34_p0179_a0018"' $S/fp_after.jsonl` vs baseline; p179 渲染 "NO DOSE CALL PERFORMED." |

无 FAIL 项; 无 CONDITIONAL 修正项 (KB).

### T-1 依据核 (examples.md:17)
- p179 渲染图 (130dpi) Row 1 DVTERM = `IVRS PROCESS DEVIATION - NO DOSE CALL PERFORMED.` 带句点; `pdftotext -layout` 同.
- 反证: p178 spec DVTERM Notes `Example: "IVRS PROCESS DEVIATION - NO DOSE CALL PERFORMED".` 句点在引号外.
- 判: DVTERM 为 verbatim 自由文本, 尾句点不构成 PDF 自身可证错误; 同类先例照录 (B-DS Ex10 TESTRL "…with Drug 1." 照录; B-CP T-12 照录). 照录 + 登记 T4 合规. 同意.

### URL 逐字 (examples.md:24)
- KB: `https://www.ema.europa.eu/en/ich-e3-structure-content-clinical-study-reports`; p179 渲染图与文本层逐字一致. 全库 grep `ich-e3` 仅此 1 处. 同意.

### 人工逐格 (dv.xpt, p179 渲染图; census 同时 OK 36 格 0 diff)
| Row | 9 列 (STUDYID DOMAIN USUBJID DVSEQ DVTERM DVDECOD EPOCH DVSTDTC) | 结果 |
|---|---|---|
| 表头 | Row + 8 列名, 列序 | 一致 |
| 1 | ABC123 DV 123101 1 / …PERFORMED. / TREATMENT DEVIATION / TREATMENT / 2003-09-21 | 一致 |
| 2 | ABC123 DV 123103 1 / DRUG XXX ADMINISTERED DURING STUDY TREATMENT PERIOD / EXCLUDED CONCOMITANT MEDICATION / TREATMENT / 2003-10-30 | 一致 |
| 3 | ABC123 DV 123103 2 / VISIT 3 DOSE <15 MG / TREATMENT DEVIATION / TREATMENT / 2003-10-30 | 一致 |
| 4 | ABC123 DV 123104 1 / TOOK ASPIRIN / PROHIBITED MEDS / TREATMENT / 2003-11-30 | 一致 |

### 双向全扫 (p178 DV 部分 - p179, 含表格原子)
- PDF→KB: 6.2.7 节标题 (KB 文件标题承载, 导航); Description/Overview 句 = assumptions.md:5 逐字; spec 首句 = :9 逐字 (码位核: 小标题 U+2013, 首句 U+2014, 与 PDF 同); spec 表 + 脚注¹ → spec.md (F-1 范围外, 同意); `DV – Assumptions` = :11; Assumptions 1-3 = :13/:15/:17 逐字 (`‑‑ACNOTH` U+2011 与折行 `--\nPATT` 归 ASCII `--`, 通行); `DV – Examples` (examples.md 文件标题承载); Example 1 标题、引言句 (折行 "free\ntext" 合并)、Rows 1,3 / Row 2 / Row 4 三条、dv.xpt 标签、表 4×9、References 标题 + 条目 1 → examples.md:3-24 全部逐字. 无缺失.
- KB→PDF: examples.md 24 行、assumptions.md 17 行逐行均有 PDF 出处; 无 KB 自写解释 (D6 无)、无伪节号、无 "Note:".
- G-TB6 结构行签字: `## DV – Description/Overview` / `## DV – Specification` / `## DV – Assumptions` (PDF 原有小标题, 格式同 CM/CE/HO 先例) ✓; 空行 ✓; 表头/分隔线未改 ✓.

### R2 recheck
- t2_recheck 0 条; atoms 0 条. 无.

### 汇总
G-TB4 1 表 OK (36 格 0 diff, 人工逐格一致); G-TB6 新增/改动 12 行, 无出处 0; recheck 0; live docs 42.
