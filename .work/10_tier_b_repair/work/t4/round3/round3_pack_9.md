# T4.1 第三轮补检包 9 — R3_PDF_TYPO (25 条; 编号 T201-T225)

> 由 `scripts/t4/t4_round3_sample.py` 生成 (KB = HEAD 内容). 只读材料. 编号全局连续 (前缀 T).

### T201. `ig34_p0267_a006` — r3:R3_PDF_TYPO

- PDF 页 267 · 原子类型 TABLE_HEADER · 所在节 `§6.3.5.8 Microscopic Findings (MI)`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EXACT) · 判定规则 `K3b-registry` · 批 `B-MI`
- 登记 `B-MI T-1`: PDF 写 "Ex3 表头 MIDRVL" → KB 写 "MIDRVFL" (处理: KB 写正确值; 依据: Ex2 同列 MIDRVFL; --DRVFL; KB `knowledge_base/domains/MI/examples.md:50`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Row | STUDYID | DOMAIN | USUBJID | MISEQ | MIGRPID | MITESTCD | MITEST | MITSTDTL | MIORRES | MIORRESU | MISTRESC | MISTRESN | MISTRESU | MISPEC | MILOC | MIMETHOD | MIDRVFL | VISIT | MIDTC
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0267.txt` 第 8-8 行 (自动定位, 词覆盖 0.95; 版式以原 PDF 为准):

~~~~
  7| mi.xpt
  8| Row   STUDYID   DOMAIN   USUBJID   MISEQ    MIGRPID   MITESTCD   MITEST       MITSTDTL               MIORRES   MIORRESU    MISTRESC    MISTRESN   MISTRESU   MISPEC   MILOC   MIMETHOD   MIDRVL   VISIT       MIDTC
  9| 1     ABC       MI       ABC-      1        1         NKX2_1     NK2          H SCORE STAINING       25        %           25          25         %          TISSUE   LUNG    IHC                 SCREENING   2001-06-
~~~~

KB 现文: `knowledge_base/domains/MI/examples.md:50` (来源: decision.evidence.hit):

~~~~
  50| | Row | STUDYID | DOMAIN | USUBJID | MISEQ | MIGRPID | MITESTCD | MITEST | MITSTDTL | MIORRES | MIORRESU | MISTRESC | MISTRESN | MISTRESU | MISPEC | MILOC | MIMETHOD | MIDRVFL | VISIT | MIDTC |
~~~~

### T202. `ig34_p0273_a037` — r3:R3_PDF_TYPO

- PDF 页 273 · 原子类型 LIST_ITEM · 所在节 `§6.3.5.9.2 Pharmacokinetics Parameters (PP)`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EQUIVALENT) · 判定规则 `K3b-registry` · 批 `B-PCPP`
- 登记 `B-PCPP T-9`: PDF 写 "pre-corrdinating" → KB 写 "pre-coordinating" (处理: KB 写正确值; 依据: 拼写; KB `knowledge_base/domains/PP/examples.md:46`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Row 4: Shows the "Ratio AUC" measurement of Drug Metabolite 1 to Drug Parent. Instead of pre-corrdinating "Ratio AUC of Drug Metabolite 1 to Drug Parent" all into the PPTEST, PPANMETH is used to describe the numerator (Drug Metabolite 1) and the denominator (Drug Parent) values that contribute to the Ratio AUC calculation in PPTEST. This post-coordination approach liberates the PPTEST variable from having to house hyper-specific, pre-coordinated PK parameter values.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0273.txt` 第 41-43 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 40|                METHOD which is in PPANMETH.
 41| Row 4:         Shows the "Ratio AUC" measurement of Drug Metabolite 1 to Drug Parent. Instead of pre-corrdinating "Ratio AUC of Drug Metabolite 1 to Drug Parent" all into the PPTEST, PPANMETH is used to
 42|                describe the numerator (Drug Metabolite 1) and the denominator (Drug Parent) values that contribute to the Ratio AUC calculation in PPTEST. This post-coordination approach liberates the PPTEST
 43|                variable from having to house hyper-specific, pre-coordinated PK parameter values.
 44| 
~~~~

KB 现文: `knowledge_base/domains/PP/examples.md:46` (来源: registry B-PCPP T-9 kb_line_now):

~~~~
  46| **Row 4:** Shows the "Ratio AUC" measurement of Drug Metabolite 1 to Drug Parent. Instead of pre-coordinating "Ratio AUC of Drug Metabolite 1 to Drug Parent" all into the PPTEST, PPANMETH is used to describe the numerator (Drug Metabolite 1) and the denominator (Drug Parent) values that contribute to the Ratio AUC calculation in PPTEST. This post-coordination approach liberates the PPTEST variable from having to house hyper-specific, pre-coordinated PK parameter values.
~~~~

### T203. `ig34_p0274_a009` — r3:R3_PDF_TYPO

- PDF 页 274 · 原子类型 TABLE_ROW · 所在节 `§6.3.5.9.2 Pharmacokinetics Parameters (PP)`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EXACT) · 判定规则 `K3b-registry` · 批 `B-PCPP`
- 登记 `B-PCPP T-5`: PDF 写 "Ex2 r6/r7 PPSEQ 1/2" → KB 写 "6/7" (处理: KB 写正确值; 依据: 同受试者 PPSEQ 重复无效; SUPPPP IDVARVAL 1-7; KB `knowledge_base/domains/PP/examples.md:59`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
6 | ABC-123 | PP | 123-1001 | 6 | B2222 | AUCIFO | AUC Infinity Obs | DRUG PARENT | NCA | 520 | h*ng/L | 520 | 520 | h*ng/L | PLASMA | LIN-LOG TRAPEZOIDAL METHOD | Y | 1 | 2001-02-01T12:00
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0274.txt` 第 20-22 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 19|                                                                                     METABOLITE 2                                                                                                    METABOLITE 1                               01T12:00
 20|                                                                      AUC Infinity                                                                                                               LIN-LOG TRAPEZOIDAL                            2001-02-
 21|   6      ABC-123      PP      123-1001     1    B2222    AUCIFO                     DRUG PARENT         NCA          520        h*ng/L          520            520         h*ng/L    PLASMA                               Y        1
 22|                                                                        Obs                                                                                                                            METHOD                                   01T12:00
 23|                                                                      AUC Infinity                                                                                                               LIN-LOG TRAPEZOIDAL                            2001-02-
~~~~

KB 现文: `knowledge_base/domains/PP/examples.md:59` (来源: decision.evidence.hit):

~~~~
  59| | 6 | ABC-123 | PP | 123-1001 | 6 | B2222 | AUCIFO | AUC Infinity Obs | DRUG PARENT | NCA | 520 | h*ng/L | 520 | 520 | h*ng/L | PLASMA | LIN-LOG TRAPEZOIDAL METHOD | Y | 1 | 2001-02-01T12:00 |
~~~~

### T204. `ig34_p0280_a036` — r3:R3_PDF_TYPO

- PDF 页 280 · 原子类型 SENTENCE · 所在节 `§6.3.5.9.3 Relating PP Records to PC Records`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EQUIVALENT) · 判定规则 `S1-R2` · 批 `B-PCPP`
- 原子抽错登记: R2 → PDF_TYPO; 依据: T4 U-7 (委托代裁 2026-11-27) KB 写正确值, 原子 = PDF: A2-3 B-PCPP T-8b DYDRGX_HALF→DY1DRGX_HALF | errata: t3_atom_err | new_target: domains/PC/examples.md | v∈KB=False; kbTok=True; pdfTok=True; atom∈PDF=True; 出处 `.work/10_tier_b_repair/work/t3_fp_expected_regressions.jsonl:66`
- 登记 `B-PCPP T-8b`: PDF 写 "Ex3 引言 DYDRGX_HALF" → KB 写 "DY1DRGX_HALF (同页 relrec)" (处理: KB 写正确值; 依据: 应为 DY1DRGX_HALF, 不单值; KB `knowledge_base/domains/PC/examples.md:278`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
This example uses --GRPID values in the PCGRPID (Example 3) and PPGRPID (Example 3) columns. Note that the 2 excluded PC records have PCGRPID = "DY1_DRGX_B"; the other PC records have PCGRPID = "DY1_DRGX_A". Note also that the PP records for half-life calculations have PPGRPID = "DYDRGX_HALF", whereas the other PP records have PPGRPID = "DY1DRGX_A".
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0280.txt` 第 42-45 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 41| half-life calculations, but were used for other parameters.
 42| This example uses --GRPID values in the PCGRPID (Example 3) and PPGRPID (Example 3) columns. Note that
 43| the 2 excluded PC records have PCGRPID = "DY1_DRGX_B"; the other PC records have PCGRPID =
 44| "DY1_DRGX_A". Note also that the PP records for half-life calculations have PPGRPID = "DYDRGX_HALF",
 45| whereas the other PP records have PPGRPID = "DY1DRGX_A".
 46| All pharmacokinetic concentrations for day 8 were used to calculate all pharmacokinetic parameters. Because day 8
~~~~

KB 现文: `knowledge_base/domains/PC/examples.md:278` (来源: registry B-PCPP T-8b kb_line_now):

~~~~
 278| This example uses --GRPID values in the PCGRPID (Example 3) and PPGRPID (Example 3) columns. Note that the 2 excluded PC records have PCGRPID = "DY1_DRGX_B"; the other PC records have PCGRPID = "DY1_DRGX_A". Note also that the PP records for half-life calculations have PPGRPID = "DY1DRGX_HALF", whereas the other PP records have PPGRPID = "DY1DRGX_A".
~~~~

### T205. `ig34_p0280_a039` — r3:R3_PDF_TYPO

- PDF 页 280 · 原子类型 LIST_ITEM · 所在节 `§6.3.5.9.3 Relating PP Records to PC Records — Example 3`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EQUIVALENT) · 判定规则 `S1-R2` · 批 `B-PCPP`
- 原子抽错登记: R2 → PDF_TYPO; 依据: T4 U-7 (委托代裁 2026-11-27) KB 写正确值, 原子 = PDF: A2-2 B-PCPP T-8 DYIDRGX_A→DY1DRGX_A | errata: t3_atom_err | new_target: domains/PC/examples.md | v∈KB=False; kbTok=True; pdfTok=True; atom∈PDF=True; 出处 `.work/10_tier_b_repair/work/t3_fp_expected_regressions.jsonl:67`
- 登记 `B-PCPP T-8`: PDF 写 "散文 DYIDRGX_A / DYIDRGX_HALF" → KB 写 "DY1DRGX_A / DY1DRGX_HALF (同页 relrec IDVARVAL)" (处理: KB 写正确值; 依据: 文本层即如此, 与表 DY1DRGX_* 不一致; KB `knowledge_base/domains/PC/examples.md:284`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Rows 1-3: The relationship with RELID "1" includes all PC records with PCGRPID = "DY1_DRGX_A", all PC records with PCGRPID = "DY1_DRGX_B" (which in this case is all the PP records for Day 1) and all PP records with PPGRPID = "DYIDRGX_A".
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0280.txt` 第 50-52 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 49| Method A (Many to Many, Using PCGRPID and PPGRPID)
 50| Rows 1-3:    The relationship with RELID "1" includes all PC records with PCGRPID = "DY1_DRGX_A", all PC
 51|              records with PCGRPID = "DY1_DRGX_B" (which in this case is all the PP records for Day 1) and all
 52|              PP records with PPGRPID = "DYIDRGX_A".
 53| Rows 4-6:    The relationship with RELID "2" includes only PC records with PCGRPID = "DY1_DRGX_A" and
~~~~

KB 现文: `knowledge_base/domains/PC/examples.md:284` (来源: registry B-PCPP T-8 kb_line_now):

~~~~
 284| - Rows 1-3: The relationship with RELID "1" includes all PC records with PCGRPID = "DY1_DRGX_A", all PC records with PCGRPID = "DY1_DRGX_B" (which in this case is all the PP records for Day 1) and all PP records with PPGRPID = "DY1DRGX_A".
~~~~

### T206. `ig34_p0281_a002` — r3:R3_PDF_TYPO

- PDF 页 281 · 原子类型 LIST_ITEM · 所在节 `§6.3.5.9.3 Relating PP Records to PC Records — Example 3`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EQUIVALENT) · 判定规则 `S1-R2` · 批 `S-SPC2`
- 原子抽错登记: R2 → PDF_TYPO; 依据: T4 U-7 (委托代裁 2026-11-27) KB 写正确值, 原子 = PDF: A2-15 S-SPC2 N-1 PP→PC records with PCSEQ | errata: t3_atom_err | new_target: domains/PC/examples.md | v∈KB=False; kbTok=True; pdfTok=True; atom∈PDF=True; 出处 `.work/10_tier_b_repair/work/t3_fp_expected_regressions.jsonl:69`
- 登记 `S-SPC2 N-1`: PDF 写 "PP records with PCSEQ values" → KB 写 "PC records with PCSEQ (:299/:300; span 另匹配本就正确的 :438-:441)" (处理: KB 写正确值; 依据: 应为 PC records (PCSEQ 属 PC), 照录; KB `knowledge_base/domains/PC/examples.md:299`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Rows 1-13:	The relationship with RELID "1" includes PP records with PCSEQ values "1" through "12" and PP records with PPGRPID = "DY1DRGX_A".
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0281.txt` 第 2-3 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  1| Method B (One to Many, Using PCSEQ and PPGRPID)
  2| Rows 1-13:       The relationship with RELID "1" includes PP records with PCSEQ values "1" through "12" and PP
  3|                  records with PPGRPID = "DY1DRGX_A".
  4| Rows 14-24: The relationship with RELID "2" includes PP records with PCSEQ values "1" through "7" and "10"
~~~~

KB 现文: `knowledge_base/domains/PC/examples.md:299` (来源: registry S-SPC2 N-1 kb_line_now):

~~~~
 299| - Rows 1-13: The relationship with RELID "1" includes PC records with PCSEQ values "1" through "12" and PP records with PPGRPID = "DY1DRGX_A".
~~~~

### T207. `ig34_p0281_a003` — r3:R3_PDF_TYPO

- PDF 页 281 · 原子类型 LIST_ITEM · 所在节 `§6.3.5.9.3 Relating PP Records to PC Records — Example 3`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EQUIVALENT) · 判定规则 `S1-R2` · 批 `S-SPC2`
- 原子抽错登记: R2 → PDF_TYPO; 依据: T4 U-7 (委托代裁 2026-11-27) KB 写正确值, 原子 = PDF: A2-15 S-SPC2 N-1 PP→PC records with PCSEQ | errata: t3_atom_err | new_target: domains/PC/examples.md | v∈KB=False; kbTok=True; pdfTok=True; atom∈PDF=True; 出处 `.work/10_tier_b_repair/work/t3_fp_expected_regressions.jsonl:70`
- 登记 `S-SPC2 N-1`: PDF 写 "PP records with PCSEQ values" → KB 写 "PC records with PCSEQ (:299/:300; span 另匹配本就正确的 :438-:441)" (处理: KB 写正确值; 依据: 应为 PC records (PCSEQ 属 PC), 照录; KB `knowledge_base/domains/PC/examples.md:299`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Rows 14-24:	The relationship with RELID "2" includes PP records with PCSEQ values "1" through "7" and "10" through "12" and PP records with PPGRPID = "DY1DRGX_HALF".
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0281.txt` 第 4-5 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  3|                  records with PPGRPID = "DY1DRGX_A".
  4| Rows 14-24: The relationship with RELID "2" includes PP records with PCSEQ values "1" through "7" and "10"
  5|             through "12" and PP records with PPGRPID = "DY1DRGX_HALF".
  6| relrec.xpt
~~~~

KB 现文: `knowledge_base/domains/PC/examples.md:299` (来源: registry S-SPC2 N-1 kb_line_now):

~~~~
 299| - Rows 1-13: The relationship with RELID "1" includes PC records with PCSEQ values "1" through "12" and PP records with PPGRPID = "DY1DRGX_A".
~~~~

### T208. `ig34_p0281_a031` — r3:R3_PDF_TYPO

- PDF 页 281 · 原子类型 LIST_ITEM · 所在节 `§6.3.5.9.3 Relating PP Records to PC Records — Example 3`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EQUIVALENT) · 判定规则 `S1-R2` · 批 `S-SPC2`
- 原子抽错登记: R2 → PDF_TYPO; 依据: T4 U-7 (委托代裁 2026-11-27) KB 写正确值, 原子 = PDF: A2-16 S-SPC2 N-2 PP/PGRPID→PC/PCGRPID | errata: t3_atom_err | new_target: domains/PC/examples.md | v∈KB=False; kbTok=True; pdfTok=True; atom∈PDF=True; 出处 `.work/10_tier_b_repair/work/t3_fp_expected_regressions.jsonl:71`
- 登记 `S-SPC2 N-2`: PDF 写 "PP records with PGRPID values" → KB 写 "all PC records with PCGRPID value(s) (:333/:334; 同页 relrec RDOMAIN=PC, IDVAR=PCGRPID)" (处理: KB 写正确值; 依据: 应为 PPGRPID, 照录; KB `knowledge_base/domains/PC/examples.md:333`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Rows 1-7:	The relationship with RELID "1" includes all PP records with PGRPID values "DY1_DRGX_A" and "DY1_DRGX_B" and PP records with PPSEQ values "1" through "3", "6", and "7".
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0281.txt` 第 35-36 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 34| Method C (Many to One, Using PCGRPID and PPSEQ)
 35| Rows 1-7:    The relationship with RELID "1" includes all PP records with PGRPID values "DY1_DRGX_A" and
 36|              "DY1_DRGX_B" and PP records with PPSEQ values "1" through "3", "6", and "7".
 37| Rows 8-10: The relationship with RELID "2" includes all PP records with PGRPID value "DY1_DRGX_A" and
~~~~

KB 现文: `knowledge_base/domains/PC/examples.md:333` (来源: registry S-SPC2 N-2 kb_line_now):

~~~~
 333| - Rows 1-7: The relationship with RELID "1" includes all PC records with PCGRPID values "DY1_DRGX_A" and "DY1_DRGX_B" and PP records with PPSEQ values "1" through "3", "6", and "7".
~~~~

### T209. `ig34_p0281_a032` — r3:R3_PDF_TYPO

- PDF 页 281 · 原子类型 LIST_ITEM · 所在节 `§6.3.5.9.3 Relating PP Records to PC Records — Example 3`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EQUIVALENT) · 判定规则 `S1-R2` · 批 `S-SPC2`
- 原子抽错登记: R2 → PDF_TYPO; 依据: T4 U-7 (委托代裁 2026-11-27) KB 写正确值, 原子 = PDF: A2-16 S-SPC2 N-2 PP/PGRPID→PC/PCGRPID | errata: t3_atom_err | new_target: domains/PC/examples.md | v∈KB=False; kbTok=True; pdfTok=True; atom∈PDF=True; 出处 `.work/10_tier_b_repair/work/t3_fp_expected_regressions.jsonl:72`
- 登记 `S-SPC2 N-2`: PDF 写 "PP records with PGRPID values" → KB 写 "all PC records with PCGRPID value(s) (:333/:334; 同页 relrec RDOMAIN=PC, IDVAR=PCGRPID)" (处理: KB 写正确值; 依据: 应为 PPGRPID, 照录; KB `knowledge_base/domains/PC/examples.md:333`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Rows 8-10:	The relationship with RELID "2" includes all PP records with PGRPID value "DY1_DRGX_A" and PP records with PPSEQ values "4" and "5".
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0281.txt` 第 37-38 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 36|              "DY1_DRGX_B" and PP records with PPSEQ values "1" through "3", "6", and "7".
 37| Rows 8-10: The relationship with RELID "2" includes all PP records with PGRPID value "DY1_DRGX_A" and
 38|            PP records with PPSEQ values "4" and "5".
 39| relrec.xpt
~~~~

KB 现文: `knowledge_base/domains/PC/examples.md:333` (来源: registry S-SPC2 N-2 kb_line_now):

~~~~
 333| - Rows 1-7: The relationship with RELID "1" includes all PC records with PCGRPID values "DY1_DRGX_A" and "DY1_DRGX_B" and PP records with PPSEQ values "1" through "3", "6", and "7".
~~~~

### T210. `ig34_p0285_a015` — r3:R3_PDF_TYPO

- PDF 页 285 · 原子类型 LIST_ITEM · 所在节 `§6.3.7.1 Generic Morphology/Physiology Specification`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EQUIVALENT) · 判定规则 `S1-R2` · 批 `B-NV`
- 原子抽错登记: R2 → PDF_TYPO; 依据: T4 U-7 (委托代裁 2026-11-27) KB 写正确值, 原子 = PDF: A3-14 B-NV N-1 may included→include | errata: t3_atom_err | new_target: domains/NV/assumptions.md | v∈KB=False; kbTok=True; pdfTok=True; atom∈PDF=True; 出处 `.work/10_tier_b_repair/work/t3_fp_expected_regressions.jsonl:77`
- 登记 `B-NV N-1`: PDF 写 "may included" → KB 写 "may include" (处理: KB 写正确值; 依据: PDF 语法, 照录; KB `knowledge_base/domains/NV/assumptions.md:23`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
The variables included in the generic morphology/physiology domain specification table are those required or expected in the individual body system-based morphology/physiology domains. Individual morphology/physiology domains may included additional expected variables. All other variables allowed in findings domains are allowed in the body system-based morphology/physiology domains
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0285.txt` 第 30-33 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 29|         domain code.
 30|     •   The variables included in the generic morphology/physiology domain specification table are those required
 31|         or expected in the individual body system-based morphology/physiology domains. Individual
 32|         morphology/physiology domains may included additional expected variables. All other variables allowed
 33|         in findings domains are allowed in the body system-based morphology/physiology domains
 34|     •   All body system-based physiology/morphology domains share the same structure, provided here. Although
~~~~

KB 现文: `knowledge_base/domains/NV/assumptions.md:23` (来源: registry B-NV N-1 kb_line_now):

~~~~
  23| - The variables included in the generic morphology/physiology domain specification table are those required or expected in the individual body system-based morphology/physiology domains. Individual morphology/physiology domains may include additional expected variables. All other variables allowed in findings domains are allowed in the body system-based morphology/physiology domains
~~~~

### T211. `ig34_p0293_a038` — r3:R3_PDF_TYPO

- PDF 页 293 · 原子类型 TABLE_ROW · 所在节 `§6.3.7.3 Musculoskeletal System Findings (MK)`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EQUIVALENT) · 判定规则 `K3b-registry` · 批 `B-MK`
- 登记 `B-MK T-2`: PDF 写 "REPLACEMENT/ SURGICAL" → KB 写 "REPLACEMENT/SURGICAL" (处理: KB 写正确值; 依据: r12 同值无空格; KB `knowledge_base/domains/MK/examples.md:53`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 3 | XYZ | MK | XYZ-002 | 3 | SGJSNSCR | Sharp/Genant JSN Score | | | | NOT DONE | AMPUTATION/MISSING ANATOMY/JOINT REPLACEMENT/SURGICAL ALTERATION | PROXIMAL INTERPHALANGEAL JOINT 2 OF THE HAND | RIGHT | X-RAY | INDEPENDENT ASSESSOR | READER 1 | 4 | WEEK 12 | 2013-08-12 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0293.txt` 第 38-40 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 37|                                                                   SPACE
 38| 3     XYZ       MK     XYZ-002   3      SGJSNSCR   Sharp/Genant                                                NOT       AMPUTATION/MISSING            PROXIMAL                  RIGHT    X-RAY        INDEPENDENT   READER 1   4       WEEK    2013-
 39|                                                    JSN Score                                                   DONE      ANATOMY/JOINT REPLACEMENT/    INTERPHALANGEAL JOINT 2                         ASSESSOR                         12      08-12
 40|                                                                                                                          SURGICAL ALTERATION           OF THE HAND
 41| 4     XYZ       MK     XYZ-002   4      SGJSNSCR   Sharp/Genant   SEVERE; PARTIAL OR      3.5       3.5                                                PROXIMAL                  LEFT     X-RAY        INDEPENDENT   READER 1   4       WEEK    2013-
~~~~

KB 现文: `knowledge_base/domains/MK/examples.md:53` (来源: decision.evidence.hit):

~~~~
  53| | 3 | XYZ | MK | XYZ-002 | 3 | SGJSNSCR | Sharp/Genant JSN Score | | | | NOT DONE | AMPUTATION/MISSING ANATOMY/JOINT REPLACEMENT/SURGICAL ALTERATION | PROXIMAL INTERPHALANGEAL JOINT 2 OF THE HAND | RIGHT | X-RAY | INDEPENDENT ASSESSOR | READER 1 | 4 | WEEK 12 | 2013-08-12 |
~~~~

### T212. `ig34_p0296_a019` — r3:R3_PDF_TYPO

- PDF 页 296 · 原子类型 LIST_ITEM · 所在节 `§6.3.7.4 Nervous System Findings (NV)`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EQUIVALENT) · 判定规则 `writer-Tn-registry` · 批 `B-NV`
- 登记 `B-NV T-1`: PDF 写 "an fluorodeoxyglucose" → KB 写 "a fluorodeoxyglucose" (处理: KB 写正确值; 依据: 冠词; KB `knowledge_base/domains/NV/examples.md:11`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Rows 5-6:   Show the SUVR findings based on an fluorodeoxyglucose (FDG)-PET scan for a subject.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0296.txt` 第 28-28 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 27| Rows 3-4:       Show the SUVR findings based on a PET/CT scan for a subject.
 28| Rows 5-6:       Show the SUVR findings based on an fluorodeoxyglucose (FDG)-PET scan for a subject.
 29| nv.xpt
~~~~

KB 现文: `knowledge_base/domains/NV/examples.md:11` (来源: registry B-NV T-1 kb_line_now):

~~~~
  11| **Rows 5-6:** Show the SUVR findings based on a fluorodeoxyglucose (FDG)-PET scan for a subject.
~~~~

### T213. `ig34_p0298_a001` — r3:R3_PDF_TYPO

- PDF 页 298 · 原子类型 SENTENCE · 所在节 `§6.3.7.4 Nervous System Findings (NV)`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EQUIVALENT) · 判定规则 `S1-R2` · 批 `B-NV`
- 原子抽错登记: R2 → PDF_TYPO; 依据: T4 U-7 (委托代裁 2026-11-27) KB 写正确值, 原子 = PDF: A3-15 B-NV N-2 删 the | errata: t3_atom_err | new_target: domains/NV/examples.md | v∈KB=False; kbTok=True; pdfTok=True; atom∈PDF=True; 出处 `.work/10_tier_b_repair/work/t3_fp_expected_regressions.jsonl:80`
- 登记 `B-NV N-2`: PDF 写 "links the each" → KB 写 "links each (删 the)" (处理: KB 写正确值; 依据: PDF 语法, 照录; KB `knowledge_base/domains/NV/examples.md:63`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
interpretation. In this scenario, NVTESTCD/NVTEST should be equal to "INTP" (Interpretation) and NVORRES should represent whether the overall test in each eye is normal or abnormal. NVGRPID links the each VEP component to the overall interpretation.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0298.txt` 第 1-2 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  1| interpretation. In this scenario, NVTESTCD/NVTEST should be equal to "INTP" (Interpretation) and NVORRES should represent whether the overall test in each eye is normal or abnormal. NVGRPID links the
  2| each VEP component to the overall interpretation.
  3| The NV domain should be used to represent the VEP latencies, P100 peak-to-peak amplitude, and their interpretations. SPDEVID allows the results to be related to both the VEP testing device and the checkerboard
~~~~

KB 现文: `knowledge_base/domains/NV/examples.md:63` (来源: registry B-NV N-2 kb_line_now):

~~~~
  63| In this example, a VEP component is considered abnormal if it falls outside of 3 standard deviations from the normative lab mean. These low and high values are stored in NVORNRLO and NVORNRHI, respectively, and the interpretation of each VEP component is represented in NVNRIND. In addition to interpreting each VEP component as normal or abnormal, the overall test for each eye may have an interpretation. In this scenario, NVTESTCD/NVTEST should be equal to "INTP" (Interpretation) and NVORRES should represent whether the overall test in each eye is normal or abnormal. NVGRPID links each VEP component to the overall interpretation.
~~~~

### T214. `ig34_p0304_a012` — r3:R3_PDF_TYPO

- PDF 页 304 · 原子类型 TABLE_HEADER · 所在节 `§6.3.7.5 Ophthalmic Examinations (OE)`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EQUIVALENT) · 判定规则 `K3b-registry` · 批 `B-OE`
- 登记 `B-OE T-1`: PDF 写 "Ex3 relrec 表头 IDVARAL" → KB 写 "IDVARVAL" (处理: KB 写正确值; 依据: supp 表头均 IDVARVAL; KB `knowledge_base/domains/OE/examples.md:121`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | RELTYPE | RELID |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0304.txt` 第 14-14 行 (自动定位, 词覆盖 0.875; 版式以原 PDF 为准) ⚠ **定位不完整或在相邻页, 请直接看原 PDF 该页**:

~~~~
 13| relrec.xpt
 14| Row       STUDYID   RDOMAIN    USUBJID       IDVAR     IDVARAL    RELTYPE    RELID
 15| 1         XYZ       PR                       PRLNKID              ONE        13
~~~~

KB 现文: `knowledge_base/domains/OE/examples.md:121` (来源: decision.evidence.hit):

~~~~
 121| | Row | STUDYID | RDOMAIN | USUBJID | IDVAR | IDVARVAL | RELTYPE | RELID |
~~~~

### T215. `ig34_p0311_a035` — r3:R3_PDF_TYPO

- PDF 页 311 · 原子类型 LIST_ITEM · 所在节 `§6.3.7.7 Respiratory System Findings (RE)`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EQUIVALENT) · 判定规则 `S1-R2` · 批 `B-RE`
- 原子抽错登记: R2 → PDF_TYPO; 依据: B-RE T-1: PDF 叙述 IREEA2 印刷错, KB 改 IRREA2 后不命中 (预期); 出处 `.work/10_tier_b_repair/evidence/checkpoints/t2_B-RE_review.md:83`
- 登记 `B-RE T-1`: PDF 写 "QNAM "IREEA2"" → KB 写 ""IRREA2"" (处理: KB 写正确值; 依据: 同句 IRREA1; suppre QNAM REIRREA2; KB `knowledge_base/domains/RE/examples.md:59`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Rows 2-4:	The presence of a flag, IRESFL, indicates that the data were inadequate. The 2 reasons why this was the case are represented by QNAM="IRREA1" and "IREEA2".
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0311.txt` 第 43-44 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 42| Row 1:         Shows the record with RESEQ="1" was the best test result, indicated by BRESFL="Y".
 43| Rows 2-4:      The presence of a flag, IRESFL, indicates that the data were inadequate. The 2 reasons why this was the case are represented by
 44|                QNAM="IRREA1" and "IREEA2".
 45| 
~~~~

KB 现文: `knowledge_base/domains/RE/examples.md:59` (来源: registry B-RE T-1 kb_line_now):

~~~~
  59| **Rows 2-4:** The presence of a flag, IRESFL, indicates that the data were inadequate. The 2 reasons why this was the case are represented by QNAM="IRREA1" and "IRREA2".
~~~~

### T216. `ig34_p0328_a007` — r3:R3_PDF_TYPO

- PDF 页 328 · 原子类型 LIST_ITEM · 所在节 `§6.3.9.2 Questionnaires (QS) — QS-Assumptions — QRS Shared Assumptions`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EQUIVALENT) · 判定规则 `K3b-registry` · 批 `B-RS`
- 登记 `B-RS T-6 (QS 副本)`: PDF 写 "--STRNC" → KB 写 "--STNRC" (处理: KB 写正确值; 依据: 同节 DR 11 与 spec 为 --STNRC; KB `knowledge_base/domains/QS/assumptions.md:59`)
- 登记 `B-RS T-6 (RS 副本)`: PDF 写 "--STRNC" → KB 写 "--STNRC" (处理: KB 写正确值; 依据: 同节 DR 11 与 spec 为 --STNRC; KB `knowledge_base/domains/RS/assumptions.md:128`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
10. Any identifiers, timing variables, or findings general observation class qualifiers may be added to a QRS domain, but the following qualifiers would generally not be used: --POS, --BODSYS, --ORNRLO, --ORNRHI, --STNRLO, --STNRHI, --STRNC, --NRIND, --XFN, --LOINC, --SPEC, --SPCCND, --LOC, --FAST, --TOX, --TOXGR, --SEV.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0328.txt` 第 14-16 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 13|                 ii. Sponsors should always consult the published QRS supplements for guidance on submitting derived information in SDTMIG-based domains.
 14|      10. Any identifiers, timing variables, or findings general observation class qualifiers may be added to a QRS domain, but the following qualifiers would
 15|          generally not be used: --POS, --BODSYS, --ORNRLO, --ORNRHI, --STNRLO, --STNRHI, --STRNC, --NRIND, --XFN, --LOINC, --SPEC, --
 16|          SPCCND, --LOC, --FAST, --TOX, --TOXGR, --SEV.
 17| QS – Examples
~~~~

KB 现文: `knowledge_base/domains/QS/assumptions.md:59-59` (来源: fuzzy locate (score 0.976)) ⚠ **近似定位, 可能不是对应那一处, 请在该文件附近自行核对**:

~~~~
  59| 10. Any identifiers, timing variables, or findings general observation class qualifiers may be added to a QRS domain, but the following qualifiers would generally not be used: --POS, --BODSYS, --ORNRLO, --ORNRHI, --STNRLO, --STNRHI, --STNRC, --NRIND, --XFN, --LOINC, --SPEC, --SPCCND, --LOC, --FAST, --TOX, --TOXGR, --SEV.
~~~~

### T217. `ig34_p0332_a009` — r3:R3_PDF_TYPO

- PDF 页 332 · 原子类型 LIST_ITEM · 所在节 `§6.3.9.3.1 Disease Response Use Case`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EQUIVALENT) · 判定规则 `K3b-registry` · 批 `B-RS`
- 登记 `B-RS T-2`: PDF 写 "will contained" → KB 写 "will contain" (处理: KB 写正确值; 依据: 语法; KB `knowledge_base/domains/RS/assumptions.md:28`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
2.  Oncology response criteria assess the change in tumor burden, an important feature of the clinical evaluation of cancer therapeutics: Both tumor shrinkage (objective response) and disease progression are useful endpoints in cancer clinical trials. The RS domain is applicable for representing responses to assessment criteria such as RECIST[1] or Lugano classification.[2] The SDTM domain examples provided reference RECIST. Disease Response supplements will be developed as 1 supplement per response criterion and will contained criterion-specific guidance and examples.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0332.txt` 第 21-24 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 20|            ONCRSCAT. The ONCRSCAT codelist contains controlled terminology for oncology disease response assessments.
 21|      2.    Oncology response criteria assess the change in tumor burden, an important feature of the clinical evaluation of cancer therapeutics: Both tumor
 22|            shrinkage (objective response) and disease progression are useful endpoints in cancer clinical trials. The RS domain is applicable for representing
 23|            responses to assessment criteria such as RECIST[1] or Lugano classification.[2] The SDTM domain examples provided reference RECIST. Disease
 24|            Response supplements will be developed as 1 supplement per response criterion and will contained criterion-specific guidance and examples.
 25|            a.   CDISC submission values and definitions in the ONCRSR codelist have been developed to facilitate reuse by keeping the definitions focused on the
~~~~

KB 现文: `knowledge_base/domains/RS/assumptions.md:28` (来源: registry B-RS T-2 kb_line_now):

~~~~
  28| 2. Oncology response criteria assess the change in tumor burden, an important feature of the clinical evaluation of cancer therapeutics: Both tumor shrinkage (objective response) and disease progression are useful endpoints in cancer clinical trials. The RS domain is applicable for representing responses to assessment criteria such as RECIST[1] or Lugano classification.[2] The SDTM domain examples provided reference RECIST. Disease Response supplements will be developed as 1 supplement per response criterion and will contain criterion-specific guidance and examples.
~~~~

### T218. `ig34_p0334_a011` — r3:R3_PDF_TYPO

- PDF 页 334 · 原子类型 LIST_ITEM · 所在节 `§6.3.9.3.1 Disease Response Use Case`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EQUIVALENT) · 判定规则 `S1-R2` · 批 `B-RS`
- 原子抽错登记: R2 → PDF_TYPO; 依据: B-RS audit: verbatim 与 PDF 页文本不符 Rows 4-7 段被拆; KB 与页文本一致; 出处 `.work/10_tier_b_repair/evidence/checkpoints/t2_B-RS_audit.md:17`
- 登记 `B-RS T-8`: PDF 写 "symptomatic determination" → KB 写 "symptomatic deterioration" (处理: KB 写正确值; 依据: 同例 RSTEST Symptomatic Deterioration; KB `knowledge_base/domains/RS/examples.md:12`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Rows 4-7:  Show the target response and non-target response by the investigator using RECIST 1.1, as well as the determination of symptomatic determination (pleural effusion) and overall response using protocol-defined response criteria, at the week 12 visit.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0334.txt` 第 18-19 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 17| Rows 1-3:       Show the target response, non-target response, and the overall response by the investigator using RECIST 1.1 at the week 6 visit.
 18| Rows 4-7:       Show the target response and non-target response by the investigator using RECIST 1.1, as well as the determination of symptomatic determination
 19|                 (pleural effusion) and overall response using protocol-defined response criteria, at the week 12 visit.
 20| rs.xpt
~~~~

KB 现文: `knowledge_base/domains/RS/examples.md:12` (来源: registry B-RS T-8 kb_line_now):

~~~~
  12| **Rows 4-7:** Show the target response and non-target response by the investigator using RECIST 1.1, as well as the determination of symptomatic deterioration (pleural effusion) and overall response using protocol-defined response criteria, at the week 12 visit.
~~~~

### T219. `ig34_p0335_a016` — r3:R3_PDF_TYPO

- PDF 页 335 · 原子类型 LIST_ITEM · 所在节 `§6.3.9.3.1 Disease Response Use Case`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EQUIVALENT) · 判定规则 `S1-R2` · 批 `B-RS`
- 原子抽错登记: R2 → PDF_TYPO; 依据: B-RS T-7 PDF_TYPO 叙述 RSPLNKGRP→RSLNKGRP | errata: t3_atom_err | new_target: domains/RS/examples.md | v∈KB=False; kbTok=True; pdfTok=True; atom∈PDF=True; 出处 `.work/10_tier_b_repair/work/t3_fp_expected_regressions.jsonl:84`
- 登记 `B-RS T-7`: PDF 写 "叙述 RSPLNKGRP ×4" → KB 写 "RSLNKGRP" (处理: KB 写正确值; 依据: 表头/spec/DR 6a; KB `knowledge_base/domains/RS/examples.md:50`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Row 2:  Shows best response to prior chemotherapy regimen. The date of best response is represented in RSDTC. RSENTPT and RSENRTPT represent that the best response was prior to screening. RSCAT = "UNSPECIFIED" indicates that the criteria used to determine the best response was unknown or not collected. RSPLNKGRP = "CM2" is used to link this record in RS to the prior chemotherapy in CM where the CMLNKGRP = "CM2".
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0335.txt` 第 28-30 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 27|                screening. RSCAT = "UNSPECIFIED" indicates that the criteria used to determine the disease progression was unknown or not collected. RSPLNKGRP = "CM1" is used to link this record in RS to the
 28|                prior chemotherapy in CM where the CMLNKGRP = "CM1".
 29| Row 2:         Shows best response to prior chemotherapy regimen. The date of best response is represented in RSDTC. RSENTPT and RSENRTPT represent that the best response was prior to screening. RSCAT =
 30|                "UNSPECIFIED" indicates that the criteria used to determine the best response was unknown or not collected. RSPLNKGRP = "CM2" is used to link this record in RS to the prior chemotherapy in CM
 31|                where the CMLNKGRP = "CM2".
~~~~

KB 现文: `knowledge_base/domains/RS/examples.md:50` (来源: registry B-RS T-7 kb_line_now):

~~~~
  50| **Row 1:** Shows disease progression on or after a prior chemotherapy regimen. The date of progression is represented in RSDTC. RSENTPT and RSENRTPT represent that the disease progression was prior to screening. RSCAT = "UNSPECIFIED" indicates that the criteria used to determine the disease progression was unknown or not collected. RSLNKGRP = "CM1" is used to link this record in RS to the prior chemotherapy in CM where the CMLNKGRP = "CM1".
~~~~

### T220. `ig34_p0335_a017` — r3:R3_PDF_TYPO

- PDF 页 335 · 原子类型 LIST_ITEM · 所在节 `§6.3.9.3.1 Disease Response Use Case`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EQUIVALENT) · 判定规则 `S1-R2` · 批 `B-RS`
- 原子抽错登记: R2 → PDF_TYPO; 依据: B-RS T-7 PDF_TYPO 叙述 RSPLNKGRP→RSLNKGRP | errata: t3_atom_err | new_target: domains/RS/examples.md | v∈KB=False; kbTok=True; pdfTok=True; atom∈PDF=True; 出处 `.work/10_tier_b_repair/work/t3_fp_expected_regressions.jsonl:85`
- 登记 `B-RS T-7`: PDF 写 "叙述 RSPLNKGRP ×4" → KB 写 "RSLNKGRP" (处理: KB 写正确值; 依据: 表头/spec/DR 6a; KB `knowledge_base/domains/RS/examples.md:50`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Row 3:  Shows best response to prior radiotherapy. The date of best response is represented in RSDTC. RSENTPT and RSENRTPT represent that the best response was prior to screening. RSCAT = "UNSPECIFIED" indicates that the criteria used to determine the best response was unknown or not collected. RSPLNKGRP = "PR2" is used to link this record in RS to the prior radiotherapy in PR where the PRLNKGRP = "PR2".
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0335.txt` 第 32-34 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 31|                where the CMLNKGRP = "CM2".
 32| Row 3:         Shows best response to prior radiotherapy. The date of best response is represented in RSDTC. RSENTPT and RSENRTPT represent that the best response was prior to screening. RSCAT =
 33|                "UNSPECIFIED" indicates that the criteria used to determine the best response was unknown or not collected. RSPLNKGRP = "PR2" is used to link this record in RS to the prior radiotherapy in PR
 34|                where the PRLNKGRP = "PR2".
 35| Rows 4-5:      Show best response and progression to a follow-up anti-cancer therapy. The date of best response and date of progression are represented in RSDTC. RSSTTPT and RSSTRTPT represent that the best
~~~~

KB 现文: `knowledge_base/domains/RS/examples.md:50` (来源: registry B-RS T-7 kb_line_now):

~~~~
  50| **Row 1:** Shows disease progression on or after a prior chemotherapy regimen. The date of progression is represented in RSDTC. RSENTPT and RSENRTPT represent that the disease progression was prior to screening. RSCAT = "UNSPECIFIED" indicates that the criteria used to determine the disease progression was unknown or not collected. RSLNKGRP = "CM1" is used to link this record in RS to the prior chemotherapy in CM where the CMLNKGRP = "CM1".
~~~~

### T221. `ig34_p0335_a018` — r3:R3_PDF_TYPO

- PDF 页 335 · 原子类型 LIST_ITEM · 所在节 `§6.3.9.3.1 Disease Response Use Case`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EQUIVALENT) · 判定规则 `S1-R2` · 批 `B-RS`
- 原子抽错登记: R2 → PDF_TYPO; 依据: B-RS T-7 PDF_TYPO 叙述 RSPLNKGRP→RSLNKGRP | errata: t3_atom_err | new_target: domains/RS/examples.md | v∈KB=False; kbTok=True; pdfTok=True; atom∈PDF=True; 出处 `.work/10_tier_b_repair/work/t3_fp_expected_regressions.jsonl:86`
- 登记 `B-RS T-7`: PDF 写 "叙述 RSPLNKGRP ×4" → KB 写 "RSLNKGRP" (处理: KB 写正确值; 依据: 表头/spec/DR 6a; KB `knowledge_base/domains/RS/examples.md:50`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Rows 4-5:  Show best response and progression to a follow-up anti-cancer therapy. The date of best response and date of progression are represented in RSDTC. RSSTTPT and RSSTRTPT represent that the best response and progression were after study treatment discontinuation. RSCAT = "UNSPECIFIED" indicates that the criteria used to determine the best response and progression was unknown or not collected. RSPLNKGRP = "CM3" is used to link this record in RS to the prior chemotherapy in CM where the CMLNKGRP = "CM3".
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0335.txt` 第 35-37 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 34|                where the PRLNKGRP = "PR2".
 35| Rows 4-5:      Show best response and progression to a follow-up anti-cancer therapy. The date of best response and date of progression are represented in RSDTC. RSSTTPT and RSSTRTPT represent that the best
 36|                response and progression were after study treatment discontinuation. RSCAT = "UNSPECIFIED" indicates that the criteria used to determine the best response and progression was unknown or not
 37|                collected. RSPLNKGRP = "CM3" is used to link this record in RS to the prior chemotherapy in CM where the CMLNKGRP = "CM3".
 38| 
~~~~

KB 现文: `knowledge_base/domains/RS/examples.md:50` (来源: registry B-RS T-7 kb_line_now):

~~~~
  50| **Row 1:** Shows disease progression on or after a prior chemotherapy regimen. The date of progression is represented in RSDTC. RSENTPT and RSENRTPT represent that the disease progression was prior to screening. RSCAT = "UNSPECIFIED" indicates that the criteria used to determine the disease progression was unknown or not collected. RSLNKGRP = "CM1" is used to link this record in RS to the prior chemotherapy in CM where the CMLNKGRP = "CM1".
~~~~

### T222. `ig34_p0336_a005` — r3:R3_PDF_TYPO

- PDF 页 336 · 原子类型 TABLE_ROW · 所在节 `§6.3.9.3.1 Disease Response Use Case`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EXACT) · 判定规则 `K3b-registry` · 批 `B-RS`
- 登记 `B-RS T-1`: PDF 写 "r3 RSSTRESC MINIMAL REPSONSE" → KB 写 "MINIMAL RESPONSE" (处理: KB 写正确值; 依据: 同行 RSORRES; KB `knowledge_base/domains/RS/examples.md:61`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 3 | ABC | RS | 66666 | 3 | PR2 | BESTRESP | Best Response | UNSPECIFIED | MINIMAL RESPONSE | | MINIMAL RESPONSE | | | INVESTIGATOR | 10 | SCREEN | | | | BEFORE | SCREEN |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0336.txt` 第 6-7 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
  5| 2     ABC        RS     66666    2     CM2      BESTRESP Best          UNSPECIFIED SD                  SD                             INVESTIGATOR 10       SCREEN                                             BEFORE    SCREEN
  6|                                                          Response
  7| 3     ABC        RS     66666    3     PR2      BESTRESP Best          UNSPECIFIED MINIMAL             MINIMAL                        INVESTIGATOR 10       SCREEN                                             BEFORE    SCREEN
  8|                                                          Response                  RESPONSE            REPSONSE
~~~~

KB 现文: `knowledge_base/domains/RS/examples.md:61` (来源: decision.evidence.hit):

~~~~
  61| | 3 | ABC | RS | 66666 | 3 | PR2 | BESTRESP | Best Response | UNSPECIFIED | MINIMAL RESPONSE | | MINIMAL RESPONSE | | | INVESTIGATOR | 10 | SCREEN | | | | | BEFORE | SCREEN |
~~~~

### T223. `ig34_p0338_a006` — r3:R3_PDF_TYPO

- PDF 页 338 · 原子类型 LIST_ITEM · 所在节 `§6.3.9.3.2 Clinical Classifications Use Case`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EQUIVALENT) · 判定规则 `S1-R2` · 批 `B-RS`
- 原子抽错登记: R2 → PDF_TYPO; 依据: [K4 改判] 原子 = PDF (norm ⊂ p337-339); KB 有登记偏离 B-RS T-5 (RS 副本): PDF 'providing an resolution' → KB 'a resolution'. 原 basis: B-RS audit: verbatim 与 PDF 页文本不符; KB 与页文本一致; 出处 `.work/10_tier_b_repair/evidence/checkpoints/t2_B-RS_audit.md:14 (页级行; 该批以范围/页号记这组原子)`
- 登记 `B-RS T-5 (RS 副本)`: PDF 写 "providing an resolution" → KB 写 "a resolution" (处理: KB 写正确值; 依据: 冠词; PDF 三份 QRS 副本同错; KB `knowledge_base/domains/RS/assumptions.md:113`)
- 登记 `B-RS T-5 (RS 副本)`: PDF 写 "providing an resolution" → KB 写 "a resolution" (处理: KB 写正确值; 依据: 冠词; PDF 三份 QRS 副本同错; KB `knowledge_base/domains/RS/assumptions.md:113`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
Notify the QRS Terminology Team that the instrument has a specific or multiple version numbers. This team will assist in providing an resolution on how the situation will be handled.
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0338.txt` 第 13-14 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 12|           is not the case for an instrument:
 13|           a.   Notify the QRS Terminology Team that the instrument has a specific or multiple version numbers. This team will assist in providing an resolution
 14|                on how the situation will be handled.
 15|           b.   Consider the use of the --GRPID variable to indicate the instrument's version number prior to a decision by the QRS Terminology Team.
~~~~

KB 现文: `knowledge_base/domains/RS/assumptions.md:113` (来源: registry B-RS T-5 (RS 副本) kb_line_now):

~~~~
 113|    a. Notify the QRS Terminology Team that the instrument has a specific or multiple version numbers. This team will assist in providing a resolution on how the situation will be handled.
~~~~

### T224. `ig34_p0342_a006` — r3:R3_PDF_TYPO

- PDF 页 342 · 原子类型 TABLE_ROW · 所在节 `SC – Examples`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EQUIVALENT) · 判定规则 `K3b-registry` · 批 `B-SC`
- 登记 `B-SC T-1`: PDF 写 "SCDTC 20-17-04-01 / 20-17-06-10" → KB 写 "2017-04-01 / 2017-06-10" (处理: KB 写正确值; 依据: ISO 8601 + Row 1 格式去多余连字符; KB `knowledge_base/domains/SC/examples.md:35`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 2 | ABC-123 | SC | 101 | 2 | EGESTAGE | Estimated Gestational Age | PREGNANCY-RELATED FINDINGS | 135 | DAYS | 135 | 135 | DAYS | ULTRASOUND | 11 | 20-17-04-01 | 226 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0342.txt` 第 14-18 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 13|                                                                                                                                                      HISTORY                03-02
 14|                                                              Age          FINDINGS
 15|                                                           Estimated      PREGNANCY-
 16|                                                                                                                                                                             20-17-
 17|   2      ABC-123       SC        101       2   EGESTAGE   Gestational      RELATED             135        DAYS         135      135      DAYS       ULTRASOUND      11               226
 18|                                                                                                                                                                             04-01
 19|                                                              Age          FINDINGS
~~~~

KB 现文: `knowledge_base/domains/SC/examples.md:35` (来源: registry B-SC T-1 kb_line_now):

~~~~
  35| | 2 | ABC-123 | SC | 101 | 2 | EGESTAGE | Estimated Gestational Age | PREGNANCY-RELATED FINDINGS | 135 | DAYS | 135 | 135 | DAYS | ULTRASOUND | 11 | 2017-04-01 | 226 |
~~~~

### T225. `ig34_p0342_a007` — r3:R3_PDF_TYPO

- PDF 页 342 · 原子类型 TABLE_ROW · 所在节 `SC – Examples`
- triage 类 **-** · 终态 **PDF_TYPO** (T3 前 EQUIVALENT) · 判定规则 `K3b-registry` · 批 `B-SC`
- 登记 `B-SC T-1`: PDF 写 "SCDTC 20-17-04-01 / 20-17-06-10" → KB 写 "2017-04-01 / 2017-06-10" (处理: KB 写正确值; 依据: ISO 8601 + Row 1 格式去多余连字符; KB `knowledge_base/domains/SC/examples.md:35`)

原子 verbatim (抽取物, 可能抽错, 仅供对照):

~~~~
| 3 | ABC-123 | SC | 101 | 3 | EGESTAGE | Estimated Gestational Age | PREGNANCY-RELATED FINDINGS | 265 | DAYS | 265 | 265 | DAYS | BALLARD | 13.1 | 20-17-06-10 | 297 |
~~~~

PDF 原文: `.work/10_tier_b_repair/work/pdf_pages/ig34_p0342.txt` 第 19-23 行 (自动定位, 词覆盖 1.0; 版式以原 PDF 为准):

~~~~
 18|                                                                                                                                                                             04-01
 19|                                                              Age          FINDINGS
 20|                                                           Estimated      PREGNANCY-
 21|                                                                                                                                                                             20-17-
 22|   3      ABC-123       SC        101       3   EGESTAGE   Gestational      RELATED             265        DAYS         265      265      DAYS        BALLARD       13.1              297
 23|                                                                                                                                                                             06-10
 24|                                                              Age          FINDINGS
~~~~

KB 现文: `knowledge_base/domains/SC/examples.md:35` (来源: registry B-SC T-1 kb_line_now):

~~~~
  35| | 2 | ABC-123 | SC | 101 | 2 | EGESTAGE | Estimated Gestational Age | PREGNANCY-RELATED FINDINGS | 135 | DAYS | 135 | 135 | DAYS | ULTRASOUND | 11 | 2017-04-01 | 226 |
~~~~

