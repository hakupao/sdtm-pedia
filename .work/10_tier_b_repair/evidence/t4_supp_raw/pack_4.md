# T4.1 补检 pack 4/8 — TRIAGE_ATOM_ERR (全局 #84-108, 25 条) 审查结果

- 审查者类型: `oh-my-claudecode:tracer` (opus), 只读
- 时间: 2026-11-27T04:53:48Z (`date -u`)
- brief: `.work/10_tier_b_repair/subagent_prompts/t4/t4_supp_fullcheck_v1.0.md`; 样本包: `.work/10_tier_b_repair/work/t4/supp/supp_pack_4.md`
- 看过的渲染页 (SDTMIG v3.4 物理页): 116, 117, 120 (另 250dpi 放大 EC 表右半), 170
- 文本层页: `ig34_p0116/0117/0120/0121/0122/0149/0150/0168/0169/0170.txt` (`.work/10_tier_b_repair/work/pdf_pages/`)
- 用过的命令 (临时目录 `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/4fbae0a7-da27-4851-8814-ac846216a212/scratchpad/supp4/`):
  - `cat -n ig34_p0NNN.txt | sed -n a,bp` (各页)
  - `pdftoppm -r 110 -f N -l N -png "source/cdisc/SDTMIG v3.4 (no header footer).pdf" pN` (N=116,117,120,170); `pdftoppm -r 250 -f 120 -l 120 -x 1300 -y 280 -W 1500 -H 200 -png ... z120`
  - `grep -n "" knowledge_base/domains/EX/examples.md | sed -n 255,300p`; `... sed -n 425,447p`; `sed -n 15,32p knowledge_base/domains/HO/examples.md`
  - `grep -n -A8 "^### <VAR>$" knowledge_base/domains/{CE,HO,ML}/spec.md` (CEBODSYS TAETORD CEENDTC CEENDY CESTRTPT CESTTPT CEENRTPT CEENTPT HOSEQ HOGRPID HOREFID HOSPID HODECOD MLGRPID MLTPTREF MLRFTDTC)
  - `grep -n "REHABILIA" .work/10_tier_b_repair/work/t2_pdf_typo_registry.jsonl`; `grep -n '"ig34_p0169_a00' .work/10_tier_b_repair/work/coverage_ledger.wc.jsonl` (查 #105-108 的 md_atom 映射)

## 判定表

| # | atom_id | 层 | 终态 | 判定 | 依据 | 说明 |
|---|---|---|---|---|---|---|
| 84 | ig34_p0116_a016 | TRIAGE_ATOM_ERR | ATOM_ERR | HOLDS | PDF p116 渲染页 Row 7 / `ig34_p0116.txt:24-25`; KB `knowledge_base/domains/EX/examples.md:273` | ① 原子: ECTRT "BOTTLE" (漏 1)、ECDOSU/ECDOSFRM "TABLET, COATED" (PDF CAPSULE)、EPOCH "TREATMENT" (漏 2)、日期 2002-07-03T07:30 (PDF 2002-07-09T07:30)、STDY/ENDY 3/3 (PDF 9/9) → ≠PDF。② KB 21 格逐格 = PDF |
| 85 | ig34_p0116_a018 | TRIAGE_ATOM_ERR | ATOM_ERR | HOLDS | PDF p116 Row 9 / `ig34_p0116.txt:28-29`; KB `EX/examples.md:275` | ① 原子: TABLET, COATED (PDF CAPSULE)、2002-07-08T07:30 (PDF 2002-07-10T07:30)、8/8 (PDF 10/10)、BOTTLE/TREATMENT 漏 1/2 → ≠PDF。② KB:275 逐格 = PDF (包里指针给的是 :274 Row 8, 偏一行) |
| 86 | ig34_p0116_a020 | TRIAGE_ATOM_ERR | ATOM_ERR | HOLDS | PDF p116 Row 11 / `ig34_p0116.txt:32-33`; KB `EX/examples.md:277` | ① 原子: "TABLET, CAPSULE" (PDF CAPSULE)、BOTTLE/TREATMENT 漏 1/2 → ≠PDF。② KB:277 = PDF (BOTTLE 1, CAPSULE, TREATMENT 2, 2002-07-11T07:34, 11/11) |
| 87 | ig34_p0117_a001 | TRIAGE_ATOM_ERR | ATOM_ERR | HOLDS | PDF p117 渲染页 Row 23 / `ig34_p0117.txt:2-3`; KB `EX/examples.md:289` | ① 原子: "TABLET, CAPSULE" (PDF CAPSULE)、STDY/ENDY 13/13 (PDF 11/11)、漏 1/2 → ≠PDF。② KB:289 = PDF |
| 88 | ig34_p0120_a003 | TRIAGE_ATOM_ERR | ATOM_ERR | HOLDS | PDF p120 渲染页 (250dpi 放大) Row 1 / `ig34_p0120.txt:3`; KB `EX/examples.md:443-445` | ① 原子: ECCAT "FIRST DOSE INTERVAL" (PDF "FIRST TO LAST DOSE INTERVAL"), 且只有 10 格, 漏 ECDOSE..ECENDY 全部 → ≠PDF。② KB:445 17 格 = PDF (1, TABLET, QD, TREATMENT, 2012-01-13, 2012-01-20, 1, 8), 表头 :443 与 PDF 一致。包里指针 :416 偏到 Example 7 的 RELREC 表, 实际在 :445 |
| 89 | ig34_p0121_a011 | TRIAGE_ATOM_ERR | ATOM_ERR | HOLDS | `ig34_p0121.txt:14`; KB `knowledge_base/domains/ML/spec.md:41-48` | ① 原子变量名 MLGRID (PDF MLGRPID) → ≠PDF。② KB ### MLGRPID, Label/Type/CT 空/Role/Core/Notes 全 = PDF |
| 90 | ig34_p0122_a010 | TRIAGE_ATOM_ERR | ATOM_ERR | HOLDS | `ig34_p0122.txt:22`; KB `ML/spec.md:293-300` | ① 原子: MLTPREF (PDF MLTPTREF)、CT 填 "ISO 8601 date/time or interval" (PDF 空)、"fixed reference time point" (PDF "fixed reference point") → ≠PDF。② KB 全 = PDF |
| 91 | ig34_p0122_a011 | TRIAGE_ATOM_ERR | ATOM_ERR | HOLDS | `ig34_p0122.txt:23-24`; KB `ML/spec.md:302-309` | ① 原子: MLRFDTC (PDF MLRFTDTC)、Label 缺 "Time Point"、CT "date/time" (PDF "datetime")、Notes 改写为 "Baseline for ... MLTPREF in the MLRFDTC..." → ≠PDF。② KB Label "Date/Time of Reference Time Point"、CT "ISO 8601 datetime or interval"、Notes 逐字 = PDF |
| 92 | ig34_p0149_a006 | TRIAGE_ATOM_ERR | ATOM_ERR | HOLDS | `ig34_p0149.txt:14-17`; KB `knowledge_base/domains/CE/spec.md:140-147` | ① 原子: CEBODYSYS (PDF CEBODSYS)、CT 空 (PDF "*")、"coding dictionary"/"multi-level"/"whichever approach..." (PDF "standard hierarchy"/"multi-axial"/"which may not necessarily be the primary SOC") → ≠PDF。② KB 全 = PDF |
| 93 | ig34_p0149_a009 | TRIAGE_ATOM_ERR | ATOM_ERR | HOLDS | `ig34_p0149.txt:23-24`; KB `CE/spec.md:167-174` | ① 原子: TAEFORD (PDF TAETORD)、Notes 尾 "for the element in the study arm" (PDF "in which the clinical event started") → ≠PDF。② KB 全 = PDF |
| 94 | ig34_p0149_a013 | TRIAGE_ATOM_ERR | ATOM_ERR | HOLDS | `ig34_p0149.txt:30-31`; KB `CE/spec.md:203-210` | ① 原子: Label 多 "the" ("End Date/Time of the Clinical Event")、Notes "End datetime" (PDF "End date/time") → ≠PDF。② KB Label "End Date/Time of Clinical Event"、Notes 逐字 = PDF |
| 95 | ig34_p0149_a016 | TRIAGE_ATOM_ERR | ATOM_ERR | HOLDS | `ig34_p0149.txt:37-38`; KB `CE/spec.md:230-237` | ① 原子变量名 CEEDDY (PDF CEENDY) → ≠PDF。② KB 全 = PDF |
| 96 | ig34_p0149_a019 | TRIAGE_ATOM_ERR | ATOM_ERR | HOLDS | `ig34_p0149.txt:49-52`; KB `CE/spec.md:257-264` | ① 原子: CESTRPT (PDF CESTRTPT)、CT "(STNREF)" (PDF "(STENRF)")、"variable CETRPT" (PDF "CESTTPT") → ≠PDF。② KB = PDF (Notes 句间双空格属空白归一; CT 另附 C66728, 见样本外备注) |
| 97 | ig34_p0150_a001 | TRIAGE_ATOM_ERR | ATOM_ERR | HOLDS | `ig34_p0150.txt:4-5`; KB `CE/spec.md:266-273` | ① 原子: CETRPT (PDF CESTTPT)、"Description of datetime" (PDF "Description or date/time")、"--STRPT" (PDF "--STRTPT")、"VISIT 2" (PDF "VISIT 1") → ≠PDF。② KB 全 = PDF |
| 98 | ig34_p0150_a002 | TRIAGE_ATOM_ERR | ATOM_ERR | HOLDS | `ig34_p0150.txt:6-9`; KB `CE/spec.md:275-282` | ① 原子: CEENRPT (PDF CEENRTPT)、"(STNREF)" (PDF "(STENRF)")、"Describes" (PDF "Identifies")、"CEENTRPT" (PDF "CEENTPT") → ≠PDF。② KB = PDF (CT 附 C66728 同 #96) |
| 99 | ig34_p0150_a003 | TRIAGE_ATOM_ERR | ATOM_ERR | HOLDS | `ig34_p0150.txt:10-11`; KB `CE/spec.md:284-291` | ① 原子: CEENTRPT (PDF CEENTPT)、"Description of datetime" (PDF "Description or date/time")、"referred to by CEENTRPT" (PDF "CEENRTPT") → ≠PDF。② KB 全 = PDF |
| 100 | ig34_p0168_a0002 | TRIAGE_ATOM_ERR | ATOM_ERR | HOLDS | `ig34_p0168.txt:5-6`; KB `knowledge_base/domains/HO/spec.md:32-39` | ① 原子变量名 TIOSEQ (PDF HOSEQ) → ≠PDF。② KB 全 = PDF (Req) |
| 101 | ig34_p0168_a0003 | TRIAGE_ATOM_ERR | ATOM_ERR | HOLDS | `ig34_p0168.txt:7`; KB `HO/spec.md:41-48` | ① 原子 TIOGRIPID (PDF HOGRPID) → ≠PDF。② KB 全 = PDF |
| 102 | ig34_p0168_a0004 | TRIAGE_ATOM_ERR | ATOM_ERR | HOLDS | `ig34_p0168.txt:8`; KB `HO/spec.md:50-57` | ① 原子: HIOREFID (PDF HOREFID)、Notes "Sponsor identifier for a healthcare encounter." (PDF "Internal or external healthcare encounter identifier.") → ≠PDF。② KB 全 = PDF |
| 103 | ig34_p0168_a0005 | TRIAGE_ATOM_ERR | ATOM_ERR | HOLDS | `ig34_p0168.txt:9-11`; KB `HO/spec.md:59-66` | ① 原子 HIOSIPID (PDF HOSPID) → ≠PDF。② KB 全 = PDF |
| 104 | ig34_p0168_a0007 | TRIAGE_ATOM_ERR | ATOM_ERR | HOLDS | `ig34_p0168.txt:14-15`; KB `HO/spec.md:77-84` | ① 原子: TIODECOD (PDF HODECOD)、Role "Synonym" (PDF "Synonym Qualifier")、"(HOMODIFY')" 多撇号 → ≠PDF。② KB Role "Synonym Qualifier"、Notes 逐字 = PDF (CT 附 C171444, 见样本外备注) |
| 105 | ig34_p0169_a0021 | TRIAGE_ATOM_ERR | ATOM_ERR | HOLDS | PDF p170 渲染页 ho.xpt Row 2 / `ig34_p0170.txt:5`; KB `HO/examples.md:22` (台账映射 md_dmHO_ex_a012) | ① 原子: 多一空列; HOSTDTC/HOENDTC 填 2011-08-06/2011-08-08 (PDF 两格皆空) → ≠PDF。原子页号标 169, 表实际在 p170。② KB:22 10 格 = PDF (日期空, HODUR P6D) |
| 106 | ig34_p0169_a0022 | TRIAGE_ATOM_ERR | ATOM_ERR | HOLDS | PDF p170 Row 3 / `ig34_p0170.txt:6`; KB `HO/examples.md:23` | ① 原子: USUBJID ABC123103 (PDF ABC123102)、HOSTDTC 2011-08-02 (PDF 2011-08-06)、HOENDTC 空 (PDF 2011-08-08)、多空列 → ≠PDF。② KB:23 = PDF |
| 107 | ig34_p0169_a0023 | TRIAGE_ATOM_ERR | ATOM_ERR | HOLDS | PDF p170 Row 4 / `ig34_p0170.txt:7`; KB `HO/examples.md:24` | ① 原子: ABC123103 / GENERAL WARD / 2011-08-15~2011-08-20 / P6D (PDF ABC123102 / INTENSIVE CARE / 2011-08-08~2011-08-15 / HODUR 空) → ≠PDF。② KB:24 = PDF |
| 108 | ig34_p0169_a0025 | TRIAGE_ATOM_ERR | ATOM_ERR | HOLDS | PDF p170 Row 5/Row 6 / `ig34_p0170.txt:8-9`; KB `HO/examples.md:25-26`; 笔误登记 `t2_pdf_typo_registry.jsonl:98` (id `B-HO T-1`) | ① 原子 "Row 6, ABC123105, HOSEQ 1, REHABILITATION FACILITY, 2011-08-15~2011-08-20" 与 PDF 任何一行都不符 (按行号对 Row 6 = ABC123103/HOSPITAL/2011-09-09~11; 按内容对 Row 5 = ABC123102/HOSEQ 3) → ≠PDF。② 台账映射 md_dmHO_ex_a015 对应 KB Row 5 (:25): 除 HOTERM 外逐格 = PDF; HOTERM PDF "REHABILIATION FACILITY" vs KB "REHABILITATION FACILITY" 属已登记 PDF 笔误 `B-HO T-1` (handling "KB 写正确值"), 按口径不算 NOT_HOLD。若按行号对 Row 6, KB:26 也逐格 = PDF。两种对法都成立 |

## 计数

| 层 | HOLDS | HOLDS_AS_EQUIV | NOT_HOLD | UNVERIFIABLE |
|---|---|---|---|---|
| TRIAGE_ATOM_ERR | 25 | 0 | 0 | 0 |
| 合计 | 25 | 0 | 0 | 0 |

层通过条件 (NOT_HOLD 0 且 UNVERIFIABLE 0): 满足。

附注 (不影响判定): #108 依赖已登记笔误 `B-HO T-1`; 包里 KB 指针偏位的有 #85 (实为 :275)、#88 (实为 :445), 已按实际行核对。

## 样本外发现 / 备注

无 KB 内容错误。仅记录观察 (不算样本判定, 不修):
- `knowledge_base/domains/CE/spec.md:261,279` 与 `knowledge_base/domains/HO/spec.md:81` 的 Controlled Terms 在 PDF 码表名后附了 NCI C-code (C66728 / C171444), PDF p149/150/168 该列只有 "(STENRF)" / "(HODECOD)"。是 KB 附加信息 (来自 xlsx 规格), 不改 PDF 值; 若严格按 EXACT 计, 这类格属 "附加" 而非逐字, 供标签口径参考。
- 原子页号: #105-108 原子标为 p169, 但 HO Example 1 ho.xpt 表实际在 p170 (p169 只有表前叙述)。属原子抽取问题, 与 KB 无关。
