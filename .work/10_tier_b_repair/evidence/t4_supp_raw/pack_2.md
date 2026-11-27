# T4.1 补检 — 包 2/8 (PRE_EXISTING, 全局编号 30-58) 审查结果

- 审查者类型: `oh-my-claudecode:tracer` (只读, 独立于标签产生角色与总闸角色)
- 时间: 2026-11-27T04:56:19Z (`date -u`)
- 判定口径: `.work/10_tier_b_repair/subagent_prompts/t4/t4_supp_fullcheck_v1.0.md` (未改)
- 看过的渲染页: SDTMIG v3.4 PDF 第 191、192、262、289、296 页 (289/296 另用 pdftoppm -r 200 局部放大); SDTM v2.0 PDF 第 69 页.
  sv20 第 9 页、第 50 页、第 66-68 页只看了文本层 (未看渲染页; 第 9 页为纯正文列表, 第 50/67/68 页用于定位同文表格).
- 用过的命令 (均只读):
  - `cat -n .work/10_tier_b_repair/work/pdf_pages/ig34_p0191.txt` / `ig34_p0262.txt` / `ig34_p0289.txt` / `ig34_p0296.txt` / `sv20_p0009.txt` / `sv20_p0050.txt` / `sv20_p0068.txt` / `sv20_p0069.txt`
  - `sed -n 55,110p knowledge_base/domains/EG/examples.md`; `sed -n 196,206p knowledge_base/domains/MB/examples.md`; `sed -n 60,80p knowledge_base/domains/MS/examples.md`; `sed -n 15,30p knowledge_base/domains/CV/examples.md`; `sed -n 8,22p knowledge_base/domains/NV/examples.md`; `sed -n 150,180p knowledge_base/model/01_concepts_and_terms.md`; `sed -n 25,45p knowledge_base/model/04_associated_persons.md`; `sed -n 103,160p knowledge_base/model/06_relationship_datasets.md`
  - `grep -rn "Timing variables, which describe\|Topic variables, which specify" knowledge_base`; `grep -rn -i "timing variables\|topic variables" knowledge_base/model knowledge_base/chapters`
  - `grep -rn "Identifier for a single associated person\|Identifier for a related device" knowledge_base`
  - `grep -c $'\xe2\x80\xa6' .work/10_tier_b_repair/work/pdf_pages/ig34_p0191.txt` (=22 行含 U+2026); `sed -n 62,87p knowledge_base/domains/EG/examples.md | grep -c $'\xe2\x80\xa6'` (=0); 同范围 `grep -c '| \.\.\. |'` (=25)
  - `grep ... .work/10_tier_b_repair/work/t2_pdf_typo_registry.jsonl` (查 p262 / p296 登记); `grep '"sv20_p0069_a00' .work/10_tier_b_repair/work/coverage_ledger.wc.jsonl`
  - `pdftoppm -r 200 -f 296 -l 296 -x 0 -y 750 -W 2400 -H 700 -png ...`、`pdftoppm -r 200 -f 289 -l 289 -x 0 -y 400 -W 2400 -H 700 -png ...` (输出在 scratchpad `supp2/`)

## 判定表

共因 E1 (#30-45, 16 条): PDF 第 191 页 EGSEQ 与 EGTESTCD 之间、EGTPT 与 EGREPNUM 之间的省略列, 字形是 `…` (U+2026, 文本层 22 行含此字符; 渲染页同), KB `knowledge_base/domains/EG/examples.md:72-87` 写的是三个半角句点 `...` (该段 0 个 U+2026). 其余各格逐格比对全部一致 (Row / STUDYID / DOMAIN / USUBJID 2324-P0001 / EGSEQ / EGTESTCD / EGTEST / EGCAT INTERVAL / EGPOS SUPINE / EGORRES / EGORRESU msec / EGSTRESC / EGSTRESN / EGSTRESU msec / EGMETHOD 12 LEAD STANDARD / EGLEAD LEAD II / EGLOBXFL 空 / VISITNUM 2 / VISIT "VISIT 2" / EGDTC / EGTPT / EGREPNUM). 允许的归一清单 (空白 / 管道符 / 粗体 / 弯直引号) 是封闭的, 不含省略号字形, 故按口径判 HOLDS_AS_EQUIV. 若 owner 一次裁定 "`…`→`...` 并入允许归一", 这 16 条可整体改为 HOLDS. (另: 原子 verbatim 写成 `..`, 属原子抽取偏差, 不影响 KB 判定.)

| # | atom_id | 层 | 终态 | 判定 | 依据 (PDF; KB) | 说明 |
|---|---|---|---|---|---|---|
| 30 | `ig34_p0191_a006` | PRE_EXISTING | EXACT | HOLDS_AS_EQUIV | `ig34_p0191.txt:12-13` + 渲染页 191 Row 9; `knowledge_base/domains/EG/examples.md:72` | E1: 仅省略列 `…`→`...`; 值 169/169/169, 2014-03-22T10:02:14, 1 HR, 3 全对 |
| 31 | `ig34_p0191_a007` | PRE_EXISTING | EXACT | HOLDS_AS_EQUIV | `ig34_p0191.txt:14-15`, 渲染页 Row 10; `EG/examples.md:73` | E1; 661, 10:02:14, 1 HR, 3 一致 |
| 32 | `ig34_p0191_a008` | PRE_EXISTING | EXACT | HOLDS_AS_EQUIV | `ig34_p0191.txt:16-17`, Row 11; `EG/examples.md:74` | E1; 90, 10:02:14, 1 HR, 3 一致 |
| 33 | `ig34_p0191_a009` | PRE_EXISTING | EXACT | HOLDS_AS_EQUIV | `ig34_p0191.txt:18-19`, Row 12; `EG/examples.md:75` | E1; 377, 10:02:14, 1 HR, 3 一致 |
| 34 | `ig34_p0191_a010` | PRE_EXISTING | EXACT | HOLDS_AS_EQUIV | `ig34_p0191.txt:20-21`, Row 13; `EG/examples.md:76` | E1; 176, 11:00:21, 2 HR, 1 一致 |
| 35 | `ig34_p0191_a011` | PRE_EXISTING | EXACT | HOLDS_AS_EQUIV | `ig34_p0191.txt:22-23`, Row 14; `EG/examples.md:77` | E1; 771, 11:00:21, 2 HR, 1 一致 |
| 36 | `ig34_p0191_a012` | PRE_EXISTING | EXACT | HOLDS_AS_EQUIV | `ig34_p0191.txt:24-25`, Row 15; `EG/examples.md:78` | E1; 100, 11:00:21, 2 HR, 1 一致 |
| 37 | `ig34_p0191_a013` | PRE_EXISTING | EXACT | HOLDS_AS_EQUIV | `ig34_p0191.txt:26-27`, Row 16; `EG/examples.md:79` | E1; 379, 11:00:21, 2 HR, 1 一致 |
| 38 | `ig34_p0191_a014` | PRE_EXISTING | EXACT | HOLDS_AS_EQUIV | `ig34_p0191.txt:28-29`, Row 17; `EG/examples.md:80` | E1; 179, 11:01:31, 2 HR, 2 一致 |
| 39 | `ig34_p0191_a015` | PRE_EXISTING | EXACT | HOLDS_AS_EQUIV | `ig34_p0191.txt:30-31`, Row 18; `EG/examples.md:81` | E1; 749, 11:01:31, 2 HR, 2 一致 |
| 40 | `ig34_p0191_a016` | PRE_EXISTING | EXACT | HOLDS_AS_EQUIV | `ig34_p0191.txt:32-33`, Row 19; `EG/examples.md:82` | E1; 103, 11:01:31, 2 HR, 2 一致 |
| 41 | `ig34_p0191_a017` | PRE_EXISTING | EXACT | HOLDS_AS_EQUIV | `ig34_p0191.txt:34-35`, Row 20; `EG/examples.md:83` | E1; 402, 11:01:31, 2 HR, 2 一致 |
| 42 | `ig34_p0191_a018` | PRE_EXISTING | EXACT | HOLDS_AS_EQUIV | `ig34_p0191.txt:36-37`, Row 21; `EG/examples.md:84` | E1; 175, 11:02:40, 2 HR, 3 一致 |
| 43 | `ig34_p0191_a019` | PRE_EXISTING | EXACT | HOLDS_AS_EQUIV | `ig34_p0191.txt:38-39`, Row 22; `EG/examples.md:85` | E1; 771, 11:02:40, 2 HR, 3 一致 |
| 44 | `ig34_p0191_a020` | PRE_EXISTING | EXACT | HOLDS_AS_EQUIV | `ig34_p0191.txt:40-41`, Row 23; `EG/examples.md:86` | E1; 98, 11:02:40, 2 HR, 3 一致 |
| 45 | `ig34_p0191_a021` | PRE_EXISTING | EXACT | HOLDS_AS_EQUIV | `ig34_p0191.txt:42-43`, Row 24; `EG/examples.md:87` | E1; 356, 11:02:40, 2 HR, 3 一致 |
| 46 | `ig34_p0192_a002` | PRE_EXISTING | EXACT | HOLDS | `ig34_p0192.txt:2` + 渲染页 192 表头; `EG/examples.md:101` (Example 4 eg.xpt) | 22 个列名逐个一致 (含 EGSTRESU). 原子把 EGSTRESU 抽成 `EGTRESU`, 是原子错, KB=PDF |
| 47 | `ig34_p0192_a003` | PRE_EXISTING | EXACT | HOLDS | `ig34_p0192.txt:3-4` + 渲染页 Row 1; `EG/examples.md:103` | 逐格一致 (EGBEATNO=1, PRSB, "PR Interval, Single Beat", 176, SCREENING, -7, 2014-02-11T14:32:12.3). 原子把 EGBEATNO 抽成空, 是原子错 |
| 48 | `ig34_p0262_a015` | PRE_EXISTING | EXACT | HOLDS | `ig34_p0262.txt:25` + 渲染页 262 suppmb Row 4; `knowledge_base/domains/MB/examples.md:203` | 10 格逐格一致 (IDVAR MBREFID, IDVARVAL 100.3, MBMEDTYP, Medium Type, MIDDLEBROOK 7H10 AGAR, Collected). 原子 IDVARVAL 抽成 `4`, 是原子错 |
| 49 | `ig34_p0262_a016` | PRE_EXISTING | EXACT | HOLDS_AS_EQUIV | `ig34_p0262.txt:26` + 渲染页 suppmb Row 7; `MB/examples.md:204` | PDF Row=7, KB Row=5; 其余 9 格一致. 差异由已登记 PDF 笔误 **B-MB T-1** (Row 列 1,2,3,4,7,8 跳号, KB 改为 5/6) 覆盖, 不算 NOT_HOLD. 但值不同, 不是 EXACT: **应改标 PDF_TYPO (非 EQUIVALENT)** |
| 50 | `ig34_p0262_a017` | PRE_EXISTING | EXACT | HOLDS_AS_EQUIV | `ig34_p0262.txt:27` + 渲染页 suppmb Row 8; `MB/examples.md:205` | PDF Row=8, KB Row=6; 其余一致 (MBSEQ, 5, MBDILFCT, Dilution Factor, 10^-2, Collected). 同 B-MB T-1; **应改标 PDF_TYPO** |
| 51 | `ig34_p0262_a025` | PRE_EXISTING | EXACT | HOLDS | `ig34_p0262.txt:46-47` + 渲染页 ms.xpt Row 3; `knowledge_base/domains/MS/examples.md:73` (表头 :69) | 20 列逐格一致 (SPDEVID ABC765, MSSEQ 3, MSREFID 100.2, MSLNKID 空, Rifampicin, MSCONC/MSCONCU 空, RESISTANT×2, LAVAGE FLUID, STOMACH, NUCLEIC ACID AMPLIFICATION TEST, 2011-01-17T06:00). 原子多出空格/错位, 属原子错 |
| 52 | `ig34_p0262_a026` | PRE_EXISTING | EXACT | HOLDS | `ig34_p0262.txt:48-49` + 渲染页 Row 4; `MS/examples.md:74` | 同上逐格一致 (MSSEQ 4, Isoniazid, SUSCEPTIBLE×2) |
| 53 | `ig34_p0289_a018` | PRE_EXISTING | EXACT | HOLDS | `ig34_p0289.txt:23-27` + 渲染页 289 (放大) Example 2 Row 1; `knowledge_base/domains/CV/examples.md:25` | 18 列逐格一致; CVORRES/CVSTRESC 为 "NATIVE, WITHOUT INTERVENTION" (带逗号), KB 同. 原子漏逗号, 属原子错 |
| 54 | `ig34_p0296_a023` | PRE_EXISTING | EXACT | HOLDS_AS_EQUIV | `ig34_p0296.txt:33-34` + 渲染页 296 (放大) Row 2; `knowledge_base/domains/NV/examples.md:18` | PDF NVSTRESN 为空 (渲染页确认), KB 填 1.17; 其余 19 格一致. 由已登记 **B-NV T-2** 覆盖, 不算 NOT_HOLD; 值不同, **应改标 PDF_TYPO** |
| 55 | `sv20_p0009_a009` | PRE_EXISTING | EXACT | HOLDS | `sv20_p0009.txt:22`; `knowledge_base/model/01_concepts_and_terms.md:165` | KB `- **Topic variables**, which specify the focus of the observation (e.g., the name of a lab test);` 逐字 (仅加粗). 包里指针 `chapters/ch02_fundamentals.md:18` 是 SDTMIG 第 2 章的另一处, 不是该原子 (SDTM v2.0 §2.1) 的承载位置 |
| 56 | `sv20_p0009_a010` | PRE_EXISTING | EXACT | HOLDS | `sv20_p0009.txt:23`; `model/01_concepts_and_terms.md:166` | 逐字 "which describe the timing of an observation (e.g., start date, end date);" (仅加粗). 包里指针 `ch02_fundamentals.md:19` 措辞不同 ("the observation", "start date and end date"), 是 IG 原文, 非本原子位置 |
| 57 | `sv20_p0069_a001` | PRE_EXISTING | EXACT | **NOT_HOLD** | `sv20_p0069.txt:6-10` + 渲染页 69 (§6.6 APRELSUB 表 #2 APID); KB `knowledge_base/model/06_relationship_datasets.md:151` | 见下方 N1 |
| 58 | `sv20_p0069_a003` | PRE_EXISTING | EXACT | **NOT_HOLD** | `sv20_p0069.txt:16-17` + 渲染页 69 (#4 RDEVID); KB `model/06_relationship_datasets.md:153` | 见下方 N1 |

### N1 (#57、#58 的详细依据)
- PDF: SDTM v2.0 §6.6 Associated Persons Relationships 的 **APRELSUB Dataset** 表 (第 68 页起, 第 69 页续), 行 `2 APID | Associated Persons Identifier | Char | Identifier | Notes: "Identifier for a single associated person, a group of associated persons, or a pool of associated persons. If APID identifies a pool, POOLDEF records must exist for each associated person (see Section 6.3, Pool Definition Dataset, and Section 4, Associated Persons Data)."`; 行 `4 RDEVID | Related Device Identifier | Char | Identifier | Notes: "Identifier for a related device. RDEVID will be populated with the SPDEVID of the related device."`
- KB 在该节 (`model/06_relationship_datasets.md:138-156`, `## 6.6 Associated Persons Relationships (APRELSUB)`) 的表只有 `# | Variable | Label | Type | Role` 五列: `:151 | 2 | APID | Associated Persons Identifier | Char | Identifier |`, `:153 | 4 | RDEVID | Related Device Identifier | Char | Identifier |`. # / 名 / 标签 / 类型 / 角色 值都对, 但 **Notes 文字在本节完全没有** (缺内容).
- 全库 Grep "Identifier for a single associated person" / "Identifier for a related device": 命中只有 `model/04_associated_persons.md:39,41` (§4 "Associated Persons—Additional Identifier Variables" 表, 对应 PDF 第 50 页, 行号为 1 / 3, 不是 2 / 4) 以及 `model/06_relationship_datasets.md:40,69` (§6.1 RELREC / §6.2 SUPP-- 表里的 APID 行, 也是别的表). 文字虽在 KB 其它节存在, 但不在本原子所属节 / 表 → 位置错 + 本表缺内容, 按口径判 NOT_HOLD.
- 台账佐证: `coverage_ledger.wc.jsonl` 里 `sv20_p0069_a001` → `md_model04_a019`, `a003` → `md_model04_a021`, 即 06 期匹配器把 §6.6 行配到了 §4 表 (跨表匹配), 这也解释了指纹复验为何在 §6.6 位置命中不了.
- 范围提示 (不影响判定): 同表 `a002` (RSUBJID)、`a004` (SREL) 也配到 `md_model04_a020/a022` (标 EQUIVALENT), 情况同类; 邻接 `a006/a007` 是 INTENTIONAL_EXCLUDE ("SDTM v2.0 content superseded by SDTMIG v3.4"). KB §6.4 RELSUB、§6.5 DR 表同样只有五列, 而 PDF 第 67-68 页这些表有 C-code / Definition 格 — 是否同属 "有意不收 Notes/Definition 列" 需要 owner 定口径; 若属有意排除, 这两条终态应是 INTENTIONAL_EXCLUDE 而非 EXACT, 无论哪种, 现 EXACT 不成立.

## 计数

| 层 | HOLDS | HOLDS_AS_EQUIV | NOT_HOLD | UNVERIFIABLE | 合计 |
|---|---|---|---|---|---|
| PRE_EXISTING | 8 | 19 | 2 | 0 | 29 |

- HOLDS (8): #46, 47, 48, 51, 52, 53, 55, 56
- HOLDS_AS_EQUIV (19) = 16 (E1 省略号字形, #30-45) + 3 (已登记 PDF 笔误, 应改标 PDF_TYPO: #49、#50 = B-MB T-1, #54 = B-NV T-2)
- NOT_HOLD (2): #57 `sv20_p0069_a001`, #58 `sv20_p0069_a003`
- UNVERIFIABLE: 0
- 层通过条件 (NOT_HOLD 0 且 UNVERIFIABLE 0): **未通过**. PRE_EXISTING 层 NOT_HOLD ≥ 1 → 按 brief 触发 PLAN Q9 升级, 由主控上报.

## 样本外发现 (不计入判定, 不修)
1. `knowledge_base/model/06_relationship_datasets.md:146-156` — PDF SDTM v2.0 第 68-69 页 APRELSUB 表的 Notes / Definition / C-code 列 (STUDYID C83082 "A sequence of characters used by the sponsor..."; RSUBJID、SREL 的 Notes) 在 KB 本节全缺; KB §6.4 RELSUB (`:111-117`)、§6.5 DR (`:129-134`) 表同为五列, PDF 第 66-68 页对应表有 C-code / Definition. 是否属有意排除未核.
2. PDF SDTM v2.0 第 69 页 SREL 行 Notes 写 "...to the subject or pool identified in RDEVID" (疑似笔误), 第 50 页同句写 "...to the device identified in RDEVID"; KB 只在 `model/04_associated_persons.md:42` 有第 50 页措辞, 第 69 页版本 (及其笔误处理) 未见登记. 另 KB `model/04_associated_persons.md:42` SREL 的 Role 写 Identifier, 与第 50 页一致; 第 69 页 APRELSUB 中 SREL Role 为 Record Qualifier, KB `model/06:154` 为 Record Qualifier, 一致.
3. 已核未发现新问题: MS 第 262 页 "MSCONU" (KB MSCONCU, 已登记 B-MS T-2)、suppms IDVAR MBREFID (KB MSREFID, 已登记 B-MS T-3)、NV 第 296 页 "an fluorodeoxyglucose" (KB "a", 已登记 B-NV T-1) — 均有登记, 仅记录.
