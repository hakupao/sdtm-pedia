# T1 分诊标定集 (calibration set) v1.0

> PLAN §3.2: writer (`t1_triage_writer_v1.0.md`) 与 reviewer (`t1_triage_reviewer_v1.0.md`) 共用本集.
> 10 条全部取自真实 §5.0 范围原子 (C04 附带 1 条范围外的尺度说明), 由 executor 在 2026-11-25 逐条对 PDF 页缓存 (`work/pdf_pages/`) 与现 KB 行号核过.
> 引文 ≤ 25 词 (CDISC 版权: 不要大段复制 PDF). 每条先写**规则**, 再写例子; 判别时套规则, 不要套例子的字面.

覆盖: PRESENT 2 / REWRITE_OK 2 / REAL_GAP 2 / IE_CAND 1 / VALUE_DIFF 1 / ATOM_ERR 1 / FIGURE 1 / LOCATE 1 (C11, 共 11 条).
**RELOCATE 没有核实过的真实例子** (查过的候选池与证伪结果见文末). 不编造; 遇到按定义判, `reason` 写清"现位置 → 应在位置".

---

## C01 PRESENT — 逐字在目标节
- 规则: 归一化后 (大小写 / 空白 / markdown 符号 / 弯引号) 与 PDF 一致, 且位于目标文件的对应节. 给 `kb_loc` = 文件:行.
- 原子 `ig34_p0220_a024` (§6.3.5.4 GF, p220, SENTENCE). PDF p220: "This domain includes but is not limited to assessments and results for genetic variation and transcription…"
- KB `knowledge_base/domains/GF/assumptions.md:7` 同句, 位于 "GF - Description/Overview" 下. → **PRESENT**, high.

## C02 REWRITE_OK — prose 改成表格, 信息点逐一都在
- 规则: KB 改写了形式 (句子 → 表格 / 合并段落), 但 PDF 原子的**每个**信息点 (主语、谓语含义、限定词、取值) 都能在 KB 指出位置. `reason` 里逐点列 "信息点 → KB 行".
- 原子 `ig34_p0043_a012` (§4.4.7, p43). PDF: "--STRF is used to identify the start of an observation relative to the sponsor-defined study reference period."
- KB `chapters/ch04_general_assumptions.md:898` 表格行 `--STRF | … | Start relative to the sponsor-defined reference period`; "observation" 由 :894 段首 "timing of an observation relative to the sponsor-defined study reference period" 覆盖.
  信息点: 变量 --STRF ✓ (:898) / 标识"开始" ✓ (:898) / 相对 sponsor-defined study reference period ✓ (:894, :898). → **REWRITE_OK**, high.

## C03 REWRITE_OK — 表格改成行内赋值 (指纹完全不命中也可能是 REWRITE_OK)
- 规则: 预筛 `NO_HIT` 不等于缺. 表格行的值可能被改写成 `QNAM = "…"` 列表. 只要每个单元格值都在且对应关系正确 → REWRITE_OK.
- 原子 `ig34_p0032_a020` (§4.2.7.1, p32, TABLE_ROW `CMINDOTH | Other Indication | BROKEN ARM`, 表头 QNAM | QLABEL | QVAL).
- KB `ch04_general_assumptions.md:414`: `SUPPCM QNAM = "CMINDOTH", QLABEL = "Other Indication", QVAL = "BROKEN ARM"` (option 1, 与 PDF 同序). 3 格 3 值, 列对应正确. → **REWRITE_OK**, high.
- 反例提醒: 同值出现在 :419 (option 2) 也是对的 — PDF 本身两次出现 (a020 / a024). 各自按所属 option 对位, 不要把两条都指向同一行.

## C04 REAL_GAP — 改写块里漏掉的句子; "相似"不等于"同义"
- 规则: 一段被改写 / 合并后, 要逐句核原段落每个原子. KB 有几乎一样的句子但限定的变量 / 范围 / 例外不同, 缺的就是那个限定.
  拿不准 REWRITE_OK vs REAL_GAP 时判 REAL_GAP.
- 原子 `ig34_p0043_a016` (§4.4.7, p43 第 21-23 行). PDF: "It would be unusual for an event or intervention to be recorded as starting "AFTER" the study reference period, but could be possible…"
- KB `ch04_general_assumptions.md:892-903` (--STRF / --ENRF 改写块: 段落 + 表 + 两条粗体提示) 没有这层意思; 全 KB grep "unusual for an" 无.
  → **REAL_GAP**, high; `kb_loc` null; `reason`: "缺: --STRF=AFTER 罕见但可能, 取决于参考期定义".
- 同段的"相似陷阱" (不在 §5.0 范围, 仅作尺度说明): `ig34_p0043_a015` PDF 说 COINCIDENT/ONGOING "not appropriate for use with **--STRF** variables";
  KB :901 只有 "**Important restriction on --ENRF:** … not appropriate for use with --ENRF variables". PDF 对 --STRF 与 --ENRF 各说一次 (p43 第 20-21 / 26-27 行),
  KB 丢了 --STRF 那条 → 按本规则是 REAL_GAP (ledger 却标 EQUIVALENT).

## C05 REAL_GAP — 只在 terminology / 索引类文件命中, 不算 RELOCATE
- 规则: 命中位置若是**另有用途的合法文本** (CT codelist 定义 `terminology/**`、`VARIABLE_INDEX.md`、`INDEX.md`), 它不是"放错地方的本节内容", 不能判 RELOCATE, 也不能判 PRESENT. 按目标节本身有没有判.
- 原子 `ig34_p0193_a003` (§6.3.4 IE, p193, "IE – Description/Overview" 下). PDF: "A findings domain that contains those criteria that cause the subject to be in violation of the inclusion/exclusion criteria."
- 预筛 `FP_HIT_ELSEWHERE` → `terminology/core/general_part4.md:196` (C61536 domain 缩写 codelist 的定义列). `domains/IE/assumptions.md` 从 assumption 1 开始, 没有 Description/Overview; 对照 `domains/GF/assumptions.md:3-5` 同类节是有的.
  → **REAL_GAP**, high; `kb_loc` null; `reason`: "IE 域文件缺 Description/Overview; 仅 CT 定义列有同文".

## C06 IE_CAND — 域 Specification 表行, spec.md 四字段全一致 (B5)
- 规则: 仅当原子是域 Specification 表行, 且 `domains/XX/spec.md` 的 name / label / type / core **全一致** (预筛 `spec_row: MATCH`, 你要再看一眼 PDF 行确认) → IE_CAND, `reason` 写 "IE类别=SPEC_TABLE_ROW, spec.md:行". 有任一不一致 → 不是 IE_CAND (看 C07 / C08).
- 原子 `ig34_p0134_a012` (§6.2.1 AE, p134). PDF 行: `AETERM  Reported Term for the  Char  Topic  Verbatim name of the event.  Req`.
- KB `domains/AE/spec.md:77-83`: Label "Reported Term for the Adverse Event" / Type Char / Core Req. → **IE_CAND**, high.

## C07 VALUE_DIFF — KB 有对应内容但值不同, 以 PDF 为准 (B6)
- 规则: 变量名 / 数值 / 代码值 / 表格单元格不同. `reason` 写 "PDF 值 → KB 值". PDF 自身疑似笔误时仍判 VALUE_DIFF, 另设 `pdf_typo_suspect: true` 并写理由 (T1.2 类集没有 PDF_TYPO, T1.4 由用户裁).
- 原子 `ig34_p0017_a022` (§3.2.1, p17, CO 行). PDF p17 第 35-36 行 Keys: "STUDYID, USUBJID, IDVAR, COREF, CODTC".
- KB `chapters/ch03_submitting_data.md:31`: `… IDVAR, COREF, COOTC | co.xpt |`. → **VALUE_DIFF**, high; `reason`: "PDF CODTC → KB COOTC".

## C08 ATOM_ERR — pdf_atoms 抽错, PDF 原页与 KB 一致 (B1: 原子只是索引)
- 规则: 先在 PDF 原页找原子. 原子文本与原页不符, 而 KB 与原页一致 → ATOM_ERR, `pdf_quote_short` 给原页真实文字. (KB 与原页也不符 → VALUE_DIFF.)
- 原子 `ig34_p0063_a017` (§5.2 DM, p63) 写 `AGEU | Age Units | Num | (AGEU) | …`. PDF p63 第 40 行: `AGEU  Age Units  Char (AGEU)  Variable …  Exp`.
- KB `domains/DM/spec.md:176-179` Type = Char. → **ATOM_ERR**, high; `reason`: "原子 Type=Num, PDF 与 KB 均为 Char".

## C09 FIGURE — 图; 说明 KB 有无对应表达
- 规则: atom_type = FIGURE 一律 FIGURE (终态 FIGURE_DEFERRED). `reason` 说明 KB 是否有对应文字 / mermaid / 表, 给位置; 没有就写 "KB 无对应".
- 原子 `ig34_p0388_a003` (§7.2.1 TA Example 1, p388, "Parallel Design Retrospective View", 3 arm × 3 epoch 网格).
- KB `domains/TA/examples.md:68-91` "**Retrospective View**" mermaid: 3 条路径 Screen → Run-In → Placebo / Drug A / Drug B, 三个 epoch 子图. → **FIGURE**, high; `kb_loc` = `domains/TA/examples.md:68`.

## C10 PRESENT — 原子的 parent_section 是翻页残留; 按 PDF 实际位置判
- 规则: pdf_atoms 在翻页处常把续段挂到错误的 `parent_section` (这里 p21 页首的续句被标成 "§3.2.1 [Findings]"). 以 PDF 页面上的实际上下文为准. KB 放在 PDF 实际所属节 → PRESENT (不是 RELOCATE).
  同理: ledger 给的目标文件只是提示. 例如 sv20 §2 的原子目标写成 `chapters/ch02_fundamentals.md`, 但 SDTM v2.0 内容在 KB 的 `model/01_concepts_and_terms.md` 是正确归属 → PRESENT + 该位置.
- 原子 `ig34_p0021_a002` (p21 第 1-2 行, 接 p20 §3.2.1.2 末句). PDF: "This means that there could be 5 records per subject (1 for each test or measurement) for a single visit or time point…"
- KB `chapters/ch03_submitting_data.md:111`, 位于 `### 3.2.1.2 CDISC Submission Value-level Metadata` (:107) 下; 预筛判 `FP_HIT_FILE_OUTSIDE_SECTION` 是因为原子节号错. → **PRESENT**, high.

---

## C11 LOCATE — KB 没有 IG 层面的归属文件
- 规则: 目标文件只是 ledger 的猜测. 若该 PDF 节在 KB 里没有对应的 IG 层文件 (只有 SDTM v2.0 model 层的同名小节, 或完全没有), 判 LOCATE, `reason` 列候选 (现有最接近的位置 + 是否需要新文件). 不要硬判 REAL_GAP 到一个归属不对的文件.
- 原子 `ig34_p0441_a007` (SDTMIG §9.1 Device Identifiers, p441 第 7-8 行). PDF: "The Device Identifiers (DI) dataset establishes identifiers for devices, which are used to populate the variable SPDEVID."
- KB: 没有 `domains/DI/` (对照: §9.2 OI 有 `domains/OI/`); 唯一的 DI 小节是 SDTM v2.0 的 `model/05_study_level_data.md:230` "### Device Identifiers (DI)", 没有这句. ledger 目标写的就是 model/05.
  → **LOCATE**, medium; `reason`: "候选: model/05:230 (v2.0 model 层) 或新建 domains/DI/ (IG 层, 与 OI 对称); 待 T1.4 定".

## RELOCATE (无真实标定例, 只给判据)
- **RELOCATE**: 内容在 KB, 但所在文件 / 节在语义上**错了** (例如 A 域的例子出现在 B 域文件, 而 B 域文件不该有它). 必须同时满足: (1) 不是 C05 那种合法的另一用途文本; (2) 不是 C10 那种原子节号 / 目标标签错; (3) 正确位置确实没有. `reason` 写 "现位置 → 应在位置".
- 查过并证伪的候选池: ledger 标 MISPLACED 的 59 条 (多为通用表头 `Row | STUDYID | RDOMAIN | …` 命中别处同构表, 或 EX/EC、EG 例子说明在本域 examples.md, 位置是对的);
  预筛 `FP_HIT_ELSEWHERE` / `FP_HIT_FILE_OUTSIDE_SECTION` 中的长句: `ig34_p0193_a003` (→ C05), `ig34_p0021_a002` (→ C10), `ig34_p0406_a033` (命中 `TA/assumptions.md:168`, 实在 "§7.2.2.1 … Transitions Between Elements" 节内, 同号节有两个 → PRESENT),
  sv20 §2 的 5 条 (→ C10 第二段, model/01 是正确归属).
- 注意: 通用表头 (TABLE_HEADER) 在 KB 任何同构表都能命中, 命中位置不说明归属; 按该表的数据行是否在正确位置判.
