# T2S S-SPEC1 — reviewer attempt 1 (终态 = writer attempt 1 + delta Δ1/Δ2)

> verdict: **PASS** (2026-11-26). reviewer = `oh-my-claudecode:code-reviewer` (与 writer executor 不同 agent). 只读 KB, 未 commit.
> scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/d6800696-3318-4d1d-9806-05c60470220c/scratchpad/t2s_S-SPEC1_reviewer/`

## 方法 (独立于 writer 的 speccmp2 / 主控 sc2·sc2w)
1. 自写 bbox 列解析器 `rvparse.py` (scratch, 非派生): 表头行 (`Variable … CDISC … Core`) 各列首词 xMin 定列界; 词按 xMin 归列; Name 列大写词开新变量; 无表头续页沿用前页列界, 页顶续行并入前一变量; 止于 `In this column` 脚注 / `– Assumptions` / ©.
   `pdftotext -bbox -f N -l N "source/cdisc/SDTMIG v3.4 (no header footer).pdf" $S/BN.html` (N = 60 62 63 64 84 86 87 98 99 100 121 122 129 130 131 143 144); `python3 -I $S/rvparse.py $S <D> <pages>`.
2. `rvcmp.py`: KB spec.md 逐变量 7 字段 vs 解析结果 (去空白比 + 折叠空白比两档), Order = 1..n, 变量序列逐个相等.
3. 旁证: 自写 stdlib xlsx 读取 `xl.py` 读 `source/cdisc/SDTMIG_v3.4.xlsx` Variables 表, `kbcmp.py` KB vs xlsx (xlsx 即 KB 原始来源, 用来定位"本批改了什么", 不作 PDF 证据).
4. 渲染 110dpi 目视: p60 p63 p64 p84 p121 p122 p129 p143 全页; p87 300dpi 局部 (IS0).
5. `grep -c '>\*<' $S/BN.html` 逐页数 CT 列星号.

## 页范围复核
CO p60 / DM p62-64 / SM p84 / SV p86-87 / CM p98-100 / ML p121-122 / SU p129-131 / BE p143-144 — 与 writer 一致 (表头→末变量→脚注/`XX – Assumptions`, 解析器与渲染双证).

## 计数闸 (reviewer 自算)
| 域 | PDF 变量 (rvparse) | KB `###` 块 | 序列逐个相等 | Order 1..n | xlsx 行 |
|---|---|---|---|---|---|
| CO | 13 | 13 | ✓ | ✓ | 13 |
| DM | 32 | 32 | ✓ | ✓ | 32 |
| SM | 10 | 10 | ✓ | ✓ | 10 |
| SV | 16 | 16 | ✓ | ✓ | 16 |
| CM | 41 | 41 | ✓ | ✓ | 41 |
| ML | 37 | 37 | ✓ | ✓ | 37 |
| SU | 37 | 37 | ✓ | ✓ | 37 |
| BE | 25 | 25 | ✓ | ✓ | 25 |
合计 211 = 211. 每块恰 7 字段行, 块内其它行 0 (kbcmp `extra-lines []` ×8; BE BECAT D6 行已按 Δ1 删除).

## CT `*` (17 格, 逐格对渲染)
bbox 星号计数: p60 1 / p63 2 / p64 3 / p84 2 / p121 3 / p129 5 / p143 1 = 17; p62 p86 p87 p98 p99 p100 p122 p130 p131 p144 = 0.
渲染逐格: CO IDVAR; DM SITEID ARMCD (p63) ARM ACTARMCD ACTARM (p64); SM MIDS MIDSTYPE; ML MLTRT MLCAT MLSCAT; SU SUDECOD SUCAT SUSCAT SUCLAS SUCLASCD; BE BEPARTY — PDF 均为 `*`, KB 均为 `- **Controlled Terms:** *` (`grep -c` 每文件: CO1 DM5 SM2 SV0 CM0 ML3 SU5 BE1 = 17). SV/CM 无星号 = PDF. ML MIDS CT 空 = PDF (与 SM MIDS 不同, 已渲染 p122 核).

## 指定核点
| 项 | 结论 | 证据 |
|---|---|---|
| DM RFSTDTC/RFENDTC Type DateTime→Char | 成立 | 渲染 p63 两行 Type 列 "Char"; bbox 词 `Char` x=192.98 落 Type 列. xlsx 为 DateTime (xlsx 与 PDF 不一致, 以 PDF 为准) |
| T-1 ETHNIC guidance¹→² | 依据成立 | bbox p63: RACE 后上标 `2` (h≈6.7), ETHNIC 后上标 `1`; 脚注¹ = CT 星号说明, 脚注² = FDA Race/Ethnicity guidance → PDF 自身可定 |
| T-2 SV IS0→ISO | 依据成立 | bbox p87 词 `IS0` ×2; 300dpi 渲染字形为窄数字 0; 同表 CT 列 "ISO 8601 datetime or interval" |
| T-3 DM 脚注² 孤立 ")" 删除 | 依据成立 | 渲染 p64 脚注² 全文无 "(" , 末尾 "ucm126396.pdf)"; "Services;2016" 照录未动 (= PDF) |
| 7 段脚注逐字 | 一致 | rvparse FOOT: CO p60 / DM p64 (¹ + ²) / SM p84 / SV p87 / CM p100 / ML p122 / SU p131; KB 文字逐字 (¹ 上标前置), DM ² 除 T-3 外逐字 |
| U7 位置 | 一致 | 8 文件均为: 末变量块 → `---` → 脚注 (DM ¹ ² 各一独立 `>` 段) → `## Cross References`; BE 无脚注 (PDF p143-144 无 "In this column", 表头虽有 Format¹) |
| CO 脚注 MOVED | 一致 | CO/assumptions.md diff = 仅删脚注行 + 其前空行 (-2 行), 文本与 CO/spec.md:123 逐字相同; narrow 授权内 |
| BE BECAT | 恢复 PDF 原文 | KB "Used to define a category of topic-variable values. Example: COLLECTION, PREPARATION, TRANSPORT." = 渲染 p143; 扩写句与括注均删 (D-2/D-3) |
| U5/U6 | 未触碰 | C-code 54 格 / DOMAIN CT 8 格 原样 (留 S-CT) |

## 逐变量结果 (211 行; reviewer 解析器 + 渲染, 非 writer 表)
| 域 | 页 | 变量 | KB 行 | reviewer 判定 (Order/Label/Type/CT/Role/Core/Notes) |
|---|---|---|---|---|
| CO | 60 | STUDYID | 5 | OK |
| CO | 60 | DOMAIN | 14 | U6 (DOMAIN CT) |
| CO | 60 | RDOMAIN | 23 | U5 (DOMAIN) |
| CO | 60 | USUBJID | 32 | OK |
| CO | 60 | COSEQ | 41 | OK |
| CO | 60 | IDVAR | 50 | OK; CT `*` ✓渲染 |
| CO | 60 | IDVARVAL | 59 | OK |
| CO | 60 | COREF | 68 | OK (仅 PDF 折行连字符/空白) |
| CO | 60 | COVAL | 77 | OK (仅 PDF 折行连字符/空白) |
| CO | 60 | COEVAL | 86 | U5 (EVAL) |
| CO | 60 | COEVALID | 95 | U5 (MEDEVAL) |
| CO | 60 | CODTC | 104 | OK |
| CO | 60 | CODY | 113 | OK (仅 PDF 折行连字符/空白) |
| DM | 62 | STUDYID | 5 | OK |
| DM | 62 | DOMAIN | 14 | U6 (DOMAIN CT) |
| DM | 62 | USUBJID | 23 | OK |
| DM | 62 | SUBJID | 32 | OK |
| DM | 63 | RFSTDTC | 41 | OK; Type Char ✓渲染 p63 |
| DM | 63 | RFENDTC | 50 | OK; Type Char ✓渲染 p63 |
| DM | 63 | RFXSTDTC | 59 | OK |
| DM | 63 | RFXENDTC | 68 | OK |
| DM | 63 | RFCSTDTC | 77 | OK |
| DM | 63 | RFCENDTC | 86 | OK |
| DM | 63 | RFICDTC | 95 | OK |
| DM | 63 | RFPENDTC | 104 | OK |
| DM | 63 | DTHDTC | 113 | OK |
| DM | 63 | DTHFL | 122 | U5 (NY) |
| DM | 63 | SITEID | 131 | OK; CT `*` ✓渲染 |
| DM | 63 | INVID | 140 | OK |
| DM | 63 | INVNAM | 149 | OK |
| DM | 63 | BRTHDTC | 158 | OK |
| DM | 63 | AGE | 167 | OK |
| DM | 63 | AGEU | 176 | U5 (AGEU) |
| DM | 63 | SEX | 185 | U5 (SEX) |
| DM | 63 | RACE | 194 | U5 (RACE); OK (PDF 上标²; 解析器读作 " 2") |
| DM | 63 | ETHNIC | 203 | U5 (ETHNIC); T-1 (PDF guidance¹ → KB ²) |
| DM | 63 | ARMCD | 212 | OK; CT `*` ✓渲染 |
| DM | 64 | ARM | 221 | OK; CT `*` ✓渲染 |
| DM | 64 | ACTARMCD | 230 | OK; CT `*` ✓渲染 |
| DM | 64 | ACTARM | 239 | OK; CT `*` ✓渲染 |
| DM | 64 | ARMNRS | 248 | U5 (ARMNULRS) |
| DM | 64 | ACTARMUD | 257 | OK |
| DM | 64 | COUNTRY | 266 | OK |
| DM | 64 | DMDTC | 275 | OK |
| DM | 64 | DMDY | 284 | OK |
| SM | 84 | STUDYID | 5 | OK |
| SM | 84 | DOMAIN | 14 | U6 (DOMAIN CT) |
| SM | 84 | USUBJID | 23 | OK |
| SM | 84 | SMSEQ | 32 | OK |
| SM | 84 | MIDS | 41 | OK; CT `*` ✓渲染 |
| SM | 84 | MIDSTYPE | 50 | OK; CT `*` ✓渲染 |
| SM | 84 | SMSTDTC | 59 | OK |
| SM | 84 | SMENDTC | 68 | OK |
| SM | 84 | SMSTDY | 77 | OK |
| SM | 84 | SMENDY | 86 | OK |
| SV | 86 | STUDYID | 5 | OK |
| SV | 86 | DOMAIN | 14 | U6 (DOMAIN CT) |
| SV | 86 | USUBJID | 23 | OK |
| SV | 86 | VISITNUM | 32 | OK |
| SV | 86 | VISIT | 41 | OK |
| SV | 86 | SVPRESP | 50 | U5 (NY) |
| SV | 86 | SVOCCUR | 59 | U5 (NY) |
| SV | 86 | SVREASOC | 68 | OK |
| SV | 87 | SVCNTMOD | 77 | U5 (CNTMODE) |
| SV | 87 | SVEPCHGI | 86 | U5 (NY) |
| SV | 87 | VISITDY | 95 | OK |
| SV | 87 | SVSTDTC | 104 | T-2 (PDF IS0 → KB ISO) |
| SV | 87 | SVENDTC | 113 | T-2 (PDF IS0 → KB ISO) |
| SV | 87 | SVSTDY | 122 | OK (仅 PDF 折行连字符/空白) |
| SV | 87 | SVENDY | 131 | OK (仅 PDF 折行连字符/空白) |
| SV | 87 | SVUPDES | 140 | OK |
| CM | 98 | STUDYID | 5 | OK |
| CM | 98 | DOMAIN | 14 | U6 (DOMAIN CT) |
| CM | 98 | USUBJID | 23 | OK |
| CM | 98 | CMSEQ | 32 | OK |
| CM | 98 | CMGRPID | 41 | OK |
| CM | 98 | CMSPID | 50 | OK |
| CM | 98 | CMTRT | 59 | OK |
| CM | 98 | CMMODIFY | 68 | OK |
| CM | 98 | CMDECOD | 77 | OK |
| CM | 98 | CMCAT | 86 | OK (仅 PDF 折行连字符/空白) |
| CM | 98 | CMSCAT | 95 | OK |
| CM | 98 | CMPRESP | 104 | U5 (NY) |
| CM | 98 | CMOCCUR | 113 | U5 (NY) |
| CM | 98 | CMSTAT | 122 | U5 (ND) |
| CM | 98 | CMREASND | 131 | OK |
| CM | 98 | CMINDC | 140 | OK |
| CM | 98 | CMCLAS | 149 | OK |
| CM | 99 | CMCLASCD | 158 | OK |
| CM | 99 | CMDOSE | 167 | OK |
| CM | 99 | CMDOSTXT | 176 | OK |
| CM | 99 | CMDOSU | 185 | U5 (UNIT) |
| CM | 99 | CMDOSFRM | 194 | U5 (FRM) |
| CM | 99 | CMDOSFRQ | 203 | U5 (FREQ) |
| CM | 99 | CMDOSTOT | 212 | OK |
| CM | 99 | CMDOSRGM | 221 | OK |
| CM | 99 | CMROUTE | 230 | U5 (ROUTE) |
| CM | 99 | CMADJ | 239 | OK |
| CM | 99 | CMRSDISC | 248 | OK |
| CM | 99 | TAETORD | 257 | OK |
| CM | 99 | EPOCH | 266 | U5 (EPOCH) |
| CM | 99 | CMSTDTC | 275 | OK |
| CM | 99 | CMENDTC | 284 | OK |
| CM | 99 | CMSTDY | 293 | OK |
| CM | 99 | CMENDY | 302 | OK |
| CM | 99 | CMDUR | 311 | OK |
| CM | 99 | CMSTRF | 320 | U5 (STENRF) |
| CM | 99 | CMENRF | 329 | U5 (STENRF) |
| CM | 100 | CMSTRTPT | 338 | U5 (STENRF) |
| CM | 100 | CMSTTPT | 347 | OK |
| CM | 100 | CMENRTPT | 356 | U5 (STENRF) |
| CM | 100 | CMENTPT | 365 | OK |
| ML | 121 | STUDYID | 5 | OK |
| ML | 121 | DOMAIN | 14 | U6 (DOMAIN CT) |
| ML | 121 | USUBJID | 23 | OK |
| ML | 121 | MLSEQ | 32 | OK |
| ML | 121 | MLGRPID | 41 | OK |
| ML | 121 | MLSPID | 50 | OK |
| ML | 121 | MLTRT | 59 | OK; CT `*` ✓渲染 |
| ML | 121 | MLCAT | 68 | OK; CT `*` ✓渲染 |
| ML | 121 | MLSCAT | 77 | OK; CT `*` ✓渲染 |
| ML | 121 | MLPRESP | 86 | U5 (NY) |
| ML | 121 | MLOCCUR | 95 | U5 (NY) |
| ML | 121 | MLSTAT | 104 | U5 (ND) |
| ML | 121 | MLREASND | 113 | OK |
| ML | 121 | MLDOSE | 122 | OK |
| ML | 121 | MLDOSTXT | 131 | OK |
| ML | 121 | MLDOSU | 140 | U5 (UNIT) |
| ML | 121 | MLDOSFRM | 149 | U5 (FRM) |
| ML | 121 | VISITNUM | 158 | OK |
| ML | 121 | VISIT | 167 | OK |
| ML | 121 | VISITDY | 176 | OK |
| ML | 121 | TAETORD | 185 | OK |
| ML | 121 | EPOCH | 194 | U5 (EPOCH) |
| ML | 121 | MLDTC | 203 | OK |
| ML | 122 | MLSTDTC | 212 | OK |
| ML | 122 | MLENDTC | 221 | OK |
| ML | 122 | MLDY | 230 | OK (仅 PDF 折行连字符/空白) |
| ML | 122 | MLSTDY | 239 | OK |
| ML | 122 | MLENDY | 248 | OK |
| ML | 122 | MLDUR | 257 | OK |
| ML | 122 | MLTPT | 266 | OK |
| ML | 122 | MLTPTNUM | 275 | OK |
| ML | 122 | MLELTM | 284 | OK |
| ML | 122 | MLTPTREF | 293 | OK |
| ML | 122 | MLRFTDTC | 302 | OK |
| ML | 122 | MIDS | 311 | OK (CT 空 = PDF) |
| ML | 122 | RELMIDS | 320 | OK |
| ML | 122 | MIDSDTC | 329 | OK |
| SU | 129 | STUDYID | 5 | OK |
| SU | 129 | DOMAIN | 14 | U6 (DOMAIN CT) |
| SU | 129 | USUBJID | 23 | OK |
| SU | 129 | SUSEQ | 32 | OK |
| SU | 129 | SUGRPID | 41 | OK |
| SU | 129 | SUSPID | 50 | OK |
| SU | 129 | SUTRT | 59 | OK |
| SU | 129 | SUMODIFY | 68 | OK |
| SU | 129 | SUDECOD | 77 | OK; CT `*` ✓渲染 |
| SU | 129 | SUCAT | 86 | OK; CT `*` ✓渲染 |
| SU | 129 | SUSCAT | 95 | OK; CT `*` ✓渲染 |
| SU | 129 | SUPRESP | 104 | U5 (NY) |
| SU | 129 | SUOCCUR | 113 | U5 (NY) |
| SU | 129 | SUSTAT | 122 | U5 (ND) |
| SU | 129 | SUREASND | 131 | OK |
| SU | 129 | SUCLAS | 140 | OK; CT `*` ✓渲染 |
| SU | 129 | SUCLASCD | 149 | OK; CT `*` ✓渲染 |
| SU | 129 | SUDOSE | 158 | OK |
| SU | 130 | SUDOSTXT | 167 | OK |
| SU | 130 | SUDOSU | 176 | U5 (UNIT) |
| SU | 130 | SUDOSFRM | 185 | U5 (FRM) |
| SU | 130 | SUDOSFRQ | 194 | U5 (FREQ) |
| SU | 130 | SUDOSTOT | 203 | OK |
| SU | 130 | SUROUTE | 212 | U5 (ROUTE) |
| SU | 130 | TAETORD | 221 | OK |
| SU | 130 | EPOCH | 230 | U5 (EPOCH) |
| SU | 130 | SUSTDTC | 239 | OK |
| SU | 130 | SUENDTC | 248 | OK |
| SU | 130 | SUSTDY | 257 | OK |
| SU | 130 | SUENDY | 266 | OK |
| SU | 130 | SUDUR | 275 | OK |
| SU | 130 | SUSTRF | 284 | U5 (STENRF); OK (仅 PDF 折行连字符/空白) |
| SU | 130 | SUENRF | 293 | U5 (STENRF); OK (仅 PDF 折行连字符/空白) |
| SU | 130 | SUSTRTPT | 302 | U5 (STENRF) |
| SU | 130 | SUSTTPT | 311 | OK |
| SU | 130 | SUENRTPT | 320 | U5 (STENRF) |
| SU | 131 | SUENTPT | 329 | OK |
| BE | 143 | STUDYID | 5 | OK |
| BE | 143 | DOMAIN | 14 | U6 (DOMAIN CT) |
| BE | 143 | USUBJID | 23 | OK |
| BE | 143 | SPDEVID | 32 | OK |
| BE | 143 | BESEQ | 41 | OK |
| BE | 143 | BEGRPID | 50 | OK |
| BE | 143 | BEREFID | 59 | OK |
| BE | 143 | BESPID | 68 | OK |
| BE | 143 | BETERM | 77 | OK |
| BE | 143 | BEMODIFY | 86 | OK |
| BE | 143 | BEDECOD | 95 | U5 (BEDECOD) |
| BE | 143 | BECAT | 104 | OK; Notes = PDF 原文 ✓渲染 p143 |
| BE | 143 | BESCAT | 113 | OK |
| BE | 143 | BELOC | 122 | U5 (LOC) |
| BE | 143 | BEPARTY | 131 | OK; CT `*` ✓渲染 |
| BE | 143 | BEPRTYID | 140 | OK |
| BE | 144 | VISITNUM | 149 | OK |
| BE | 144 | VISIT | 158 | OK |
| BE | 144 | VISITDY | 167 | OK |
| BE | 144 | BEDTC | 176 | OK |
| BE | 144 | BESTDTC | 185 | OK |
| BE | 144 | BEENDTC | 194 | OK |
| BE | 144 | BESTDY | 203 | OK |
| BE | 144 | BEENDY | 212 | OK |
| BE | 144 | BEDUR | 221 | OK |

分类: OK = 7 字段与 PDF 一致; "仅 PDF 折行连字符/空白" = PDF 单元格内行尾连字符折行 (sponsor-␣defined / 650-␣VITALS / COVAL1-␣COVALn / ANTI-␣CANCER), 渲染核 KB 连写正确; U5 = C-code vs PDF 括号短名 (S-CT); U6 = DOMAIN CT (S-CT).
跨页续行 DM ARMCD (p63→p64) / SU SUENRTPT (p130→p131) 由 rvparse 并入, 比对一致.

## KB→PDF 反向 (8 文件全文)
- 变量块外行: `# XX — …` 标题 + `> Class: … | Structure: …` (U8 导航) + `---` + 脚注 + Cross References 块 (U8 导航). 无其它行. 
- diff 新增/改动行逐条出处: CT `*` ×17 (渲染 p60/63/64/84/121/129/143); Type Char ×2 (p63); RACE ² / ETHNIC ² (p63, T-1); IS0→ISO ×2 (p87, T-2); 脚注 8 段 (p60/64×2/84/87/100/122/131); BECAT Notes (p143). 无出处行 0. D6 0.

## 授权范围
`git diff HEAD --stat -- knowledge_base/`: 本批文件 = 8 spec.md + CO/assumptions.md (-2). 其余改动文件 (BS CE DA DD DV HO IE MH spec.md = S-SPEC2 kb_files; model/01 03 04 = S-MOD1; model/05 = S-MOD3) 属他批. writer.jsonl 37 行 kb_file 集合 = 本批 9 文件.

## fp_match
`python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl` → RESULT: RED, 回归 72; 去 `work/t2_fp_expected_regressions.jsonl` 后余 1 条, 即本批页:
| atom | 定性 | 证据 |
|---|---|---|
| ig34_p0060_a024 (CO 脚注¹) | 预期 (MOVED 源删除; fp targets 只列 CO/assumptions+examples, 不含 spec.md) | `norm(verbatim) in norm(CO/spec.md)` = True |
- 本批 gap 原子直查目标文件: ig34_p0064_a011 / a012 (DM) / p0084_a018 (SM) / p0087_a009 (SV) / p0100_a005 (CM) / p0131_a003 (SU) = True; **ig34_p0122_a015 (ML) = False — 原子文本错 "CDISC/NCIBI"**, PDF p122 渲染与 layout 均为 "CDISC/NCI", KB = PDF (原子勘误, 非 KB 缺陷).
- census: `pdf_ranges` 为空 (spec-only 批无 Row 表), 跳过.

## 问题表
| ref | 检查项 | 问题 | 证据 |
|---|---|---|---|
| ig34_p0060_a024 | fp 回归 | 预期回归未登记在 expected 列表 | 主控: 加入 `t2_fp_expected_regressions.jsonl` (class MOVED) — LOW, 非阻塞 |
| ig34_p0122_a015 | 原子勘误 | 原子 verbatim "NCIBI" ≠ PDF "NCI" | p122 脚注 "CDISC/NCI codelist values are enclosed in parentheses." — 主控登记 atom errata, LOW |
| KB 既有 Notes 双空格 (DM ARMCD/ARM/ACTARM*/COUNTRY, CM/SU *RF/*RTPT) | 排版 | PDF 单元格内换行以双/三空格表示, 非本批改动, 无信息丢失 | — 不处理 |

## 删除清单 / D6 签字
- D-1 CO/assumptions.md 脚注段 (MOVED 源) ✓; D-2 BECAT 括注 "(CDISC canonical examples per SDTMIG v3.4)" ✓ (PDF 无); D-3 BECAT D6 行 ✓ (主控 D2 裁定; PDF BECAT CT 空, "controlled-vocabulary convention" 无依据). D6 = 0.
- 结构改动: 无 (仅 CO 脚注跨文件 MOVED).

## 自查
`python3 tools/check_links.py 2>&1 | grep "live docs"` → `broken relative links: 18668 (live docs: 42)` (= 基线 42).
