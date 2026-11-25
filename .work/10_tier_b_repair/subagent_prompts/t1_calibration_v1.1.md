# T1 分诊标定集 (calibration set) v1.1

> PLAN §3.2: writer 与 reviewer 共用本集. v1.0 (`t1_calibration.md`) 保留不改 (规则 B); 本版只做下列改动, C01-C10 原样沿用.
> v1.1 改动 (2026-11-26, 依据 `evidence/checkpoints/t1_lane_notes.md` 的 T1.2/T1.3 回报):
> 1. **C11 前提错误已修**: v1.0 写 "KB 没有 `domains/DI/`", 实际 `domains/DI/assumptions.md` 存在 (:3 标题 "DI – Description/Overview (§9.1)", :5 起正文, 缺 §9.1 首句).
>    `ig34_p0441_a007` 改判 **REAL_GAP** (T1.3 lane C reviewer). C11 换成真实 LOCATE 例 (§6.3.5.1), 并加 "判 LOCATE 前先 `ls knowledge_base/domains/`" 规则.
>    按 v1.0 C11 判过的条目须复查 (已复查: lane A 报 29 条 §6.3.5.1 LOCATE, 经 `ls domains/` 确认无对应文件; merge 后 28 条, ig34_p0195_a008 被 reviewer 改 IE_CAND).
> 2. **RELOCATE 有真实例子了** (C12 / C13), 替换 v1.0 文末 "无真实标定例".
> 3. 新规则 C14: atom_type = FIGURE 但实为数据表 → 按表逐格核值, 不判 FIGURE; 图像页先渲染原页再判.
> 4. **R-OPEN-1 (待用户裁, 未生效)**: "丢失短语在同节上下文 / 同表行已有 → REWRITE_OK". 见文末.
> 引文 ≤ 25 词 (CDISC 版权). 新增条目只给 atom_id / 位置, 不抄 PDF 原文.

覆盖: PRESENT 2 / REWRITE_OK 2 / REAL_GAP 3 (含 C11b) / IE_CAND 1 / VALUE_DIFF 2 (含 C14) / ATOM_ERR 1 / FIGURE 1 / LOCATE 1 / RELOCATE 2.

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

## C11 LOCATE — PDF 节在 KB 没有 IG 层归属文件 (v1.1 换例)
- 规则: 目标文件只是 ledger 的猜测. **判 LOCATE 前必须 `ls knowledge_base/domains/` (以及 `chapters/`, `model/`) 确认确实没有对应文件**;
  文件存在但缺这句 → 不是 LOCATE, 按 C04 判 REAL_GAP (见 C11b). 确无归属文件时判 LOCATE, `reason` 列候选位置 + 先例.
  "文件不存在"类说法一律附 `ls` 结果, 不凭印象.
- 原子 `ig34_p0194_a022` (§6.3.5.1 Generic Specimen-based Lab Findings Domain Specification, p194, SENTENCE; 同节共 28 条).
  `ls knowledge_base/domains/` 无 §6.3.5.1 的通用 lab 文件; ledger 目标写 `model/02_observation_classes.md` (SDTM v2.0 层, 不对).
  → **LOCATE**, medium; `reason`: "候选: domains/LB/assumptions.md (先例: NV/assumptions.md 承载 §6.3.7.1 通用 morphology/physiology 说明); 待 T1.4 定".

## C11b REAL_GAP — 文件存在但缺首句 (v1.0 C11 的原例, 改判)
- 原子 `ig34_p0441_a007` (§9.1 Device Identifiers, p441). `domains/DI/assumptions.md` 存在 (:3 标题, :5 起正文), §9.1 首句不在.
  → **REAL_GAP**, high; `kb_loc` = `knowledge_base/domains/DI/assumptions.md:5` (插入点). (DI 无 examples.md: MB Ex3 的 di.xpt 表另记, 见 census PDF_ONLY p263.)

## C12 RELOCATE — IG 节内容在 chapter 层, 域文件同号标题下为空
- 规则: PDF 某节 (如 §6.4.x) 的内容只出现在别的章节文件里, 而域文件里**有该节同号标题但标题下为空** → RELOCATE (不是 PRESENT, 也不是 C10:
  C10 是原子节号错、KB 放对了; 这里是 KB 放错了). `reason` 写 "现位置 → 应在位置".
- 原子 `ig34_p0363_a014` / `ig34_p0364_a003` (§6.4.2 Naming Findings About Domains, p363-364).
  内容在 `chapters/ch02_fundamentals.md:219` / `:227` (FA 拆分 / 命名列表); `domains/FA/assumptions.md:62` "## §6.4.2 Naming Findings About Domains" 标题下为空.
  → **RELOCATE**, high; `reason`: "ch02:219/227 → FA/assumptions.md:62 (§6.4.2)". (T1.2 lane D writer 发现, T1.3 reviewer 核实.)

## C13 RELOCATE — 唯一副本在 model 层且自注 "Reference Material", 原节空标题
- 规则: 唯一副本在另一层文件里, 且该处自注 "Reference Material, SDTMIG v3.4 p…" 之类的借放说明, 原 IG 节同号标题下为空 → RELOCATE.
  这不是 C05 (C05 是有独立用途的合法文本, 如 CT 定义列; 借放的参考材料不算独立用途).
- 原子 `ig34_p0364_a011` (§6.4.3 Variables Unique to Findings About, p364).
  内容在 `model/02_observation_classes.md:188-190` ("### §6.4.3 … (Reference Material, SDTMIG v3.4 p…)" 下); `domains/FA/assumptions.md:64` "## §6.4.3" 标题下为空.
  → **RELOCATE**, high; `reason`: "model/02:188-190 → FA/assumptions.md:64 (§6.4.3)". (T1.3 lane A reviewer 由 PRESENT 改判.)

## C14 FIGURE 标签但实为数据表 → 逐格核值
- 规则: atom_type = FIGURE 时先看 PDF 原页 (图像页先渲染原页: `pdftoppm -f N -l N -r 110 -png`). 若该"图"其实是数据集表 (有 Row / 变量列),
  不判 FIGURE, 按表格逐格核 (VALUE_DIFF / PRESENT / REAL_GAP). 真图才判 FIGURE (C09).
- 原子 `ig34_p0225_a004` / `ig34_p0225_a017` (§6.3.5.4 GF Example 1 / 2 的 gf.xpt, p225). 原子标 FIGURE, 实为 gf.xpt 数据表;
  KB `domains/GF/examples.md:27` 起整表值与 PDF 不符 (census v2: GF/examples.md 多格 diff). → **VALUE_DIFF**, high. (T1.3 lane B reviewer 由 FIGURE 改判.)

## 附: v1.0 RELOCATE 判据仍有效
- 必须同时满足: (1) 不是 C05 的合法另一用途文本; (2) 不是 C10 的原子节号 / 目标标签错; (3) 正确位置确实没有 (空标题或无内容).
- T1.1 预筛的 RELOCATE 建议已报的 21 条全部不成立 (lane A 4/4, C 7/7, D 10/10; lane B 未报): 预筛 RELOCATE 只当线索, 必须人工确认 (3).
- 通用表头 (TABLE_HEADER) 在任何同构表都能命中, 命中位置不说明归属.

---

## R-OPEN-1 (待用户裁, **未生效** — 在用户 T1.4 ack 前不得用于判定)
- 提议 (T1.3 lane D reviewer): 原子里被 KB "丢掉"的短语, 若在**同节上下文**或**同一表行**已有同义表达 → REWRITE_OK, 不是 REAL_GAP.
- 现状: 涉及的 4 条 (`ig34_p0010_a023` "in RELREC" 隐含; `ig34_p0011_a020` 例句语境给出; `ig34_p0012_a005` ch02:25 有; `ig34_p0056_a006` ch04:1362 同行有)
  按 `t1_errata.json` 的 `pending_user` 暂计 **REAL_GAP** (错判 REWRITE_OK 是终态, 风险更大). 在用户裁定前, writer / reviewer 仍按 C04 "拿不准判 REAL_GAP".
- 若用户采纳: 须同时写明 "同节" 的边界 (同一 `###` 节? 同一段?) 与 "同义" 的举证要求 (逐信息点给 KB 行号, 同 C02).
