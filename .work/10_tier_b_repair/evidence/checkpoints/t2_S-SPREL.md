# T2S S-SPREL writer checkpoint (扫描批: SE / RELREC / RELSUB / RELSPEC / OI + DI narrow)

## attempt 1 (2026-11-26, oh-my-claudecode:executor / opus)

- base HEAD `f534395`; 本批 15 kb_files + DI/assumptions.md 改前与 HEAD 一致 (`git diff --quiet HEAD --` 逐个). scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/d6800696-3318-4d1d-9806-05c60470220c/scratchpad/t2s_S-SPREL_writer/`
  (base/ = HEAD 副本; kbbase/ = `git archive HEAD`; apply.py = 精确替换 + 命中 1 次断言; speccmp.py / lscan.py / rscan2.py / scan2.py 沿用 S-SPC2 writer; manifest.json = 复核后页范围; census_before/after.json; fp_before/after.jsonl; 渲染 110dpi p79/80/82/83/84/429/438/441)
- md5 after: SE/assumptions `3a157a3a…` (50→54); SE/examples `858c6e80…` (82, 行数不变); SE/spec `a242c866…` (136→138); RELREC/spec `e4d10504…` (86→88); RELSUB/spec `89ec7021…` (67→69); RELSPEC/spec `9d638a26…` (77→79); OI/assumptions `20d44d18…` (22→30); OI/spec `9785c072…` (80→82); DI/assumptions `7e925b39…` (5→12).
  未动: RELREC/assumptions `69882fb2…`, RELREC/examples `e88209df…`, RELSUB/assumptions `c4e13086…`, RELSUB/examples `ec54eaa9…`, RELSPEC/assumptions `92e92ac4…`, RELSPEC/examples `c3da4fad…`, OI/examples `2720823f…` (= B-REL 终态 / HEAD).

### 完整节页范围 (O20 复核)
| 单元 | 节 | json lo-hi | 复核结果 | 依据 |
|---|---|---|---|---|
| domains/SE | §5.3 | 79-84 | **79-84** | p79 上部 DM Ex7 suppdm (Row 1/2 + 表) 属 §5.2, 不归本批; §5.3 标题 p79 中部; p84 上部 dm Ex2 Row 2 续表止, 其下 `5.4 Subject Disease Milestones (SM)` 起为 SM |
| domains/RELREC | §8.2 / §8.2.1 / §8.2.2 | 429-430 | **429-430** (§8.2.2 止于 p430 中部 §8.3 标题) | 另: RELREC 文件按 D7/B-REL 还承载 §8 引言 IDVAR 段 (p427 下部) 与 §8.3 / §8.3.1 (p430 下部-p431 中部, §8.4 标题止) → 本批全扫页 = **427, 429-431** (p427 上部章引言 + 8 bullet、p428 §8.1 属 ch08, 不在 RELREC 文件) |
| domains/RELSUB | §8.7 | 437-439 | **437-439** | p437 上部 §8.6 表 + 叙述属 ch08; §8.7 标题 p437 下部; p439 中部 relsub 表后 §8.8 标题止 |
| domains/RELSPEC | §8.8 | 439-441 | **439-440** | p440 relspec 表即 §8 末; p441 首行 `9 Study References` → p441 无本节内容 |
| domains/OI | §9.2 | 442-444 | **441-443** | §9.2 标题、OI Description/Overview、Specification 与 spec 表 + 脚注均在 **p441** 下半; p443 oi.xpt 续表 Row 6-14 止; p444 首行 `10 Appendices` 属 ch10 |
| DI (narrow) | §9 章引言 | 441 | **441** 上部 | `9 Study References` 标题至 `9.1 Device Identifiers` 之前 (1 段 + 2 bullet) |

### 双向全扫 — 逐页日志
方法: PDF→KB = lscan.py (layout 逐句) + 原子 fp_match; spec 表 = speccmp.py (bbox 分列逐变量逐字段) + 渲染 / layout 补核 bbox 漏读行; 例表 = table_census.py (bbox) + 渲染逐格. KB→PDF = rscan2.py (按复核页范围, 仅 layout). "句数" = lscan 切句数 (含别节); 未命中只列真缺口, 其余归类在备注.

| 页 | 节 | PDF→KB: 句 / 未命中 / 缺→已补 | KB→PDF: KB 段, 无出处行→处理 | 表 (逐格/census) | 备注 |
|---|---|---|---|---|---|
| 79 | DM Ex7 尾 (别节) / §5.3 Description / SE Spec / spec | 19 / 11 / 6→6 | SE/asm :3-19 改后全有出处 | speccmp 3 变量 + STUDYID 渲染核 (bbox 漏读); census 无 SE 表 | 补: :7 "epochs and elements"; :11 "(TESTRL values)"; :17 `--DTC`; :18 "relate" / `(--DY)`; `## SE – Specification` + se.xpt 首句 (gap S). 其余未命中 = 别节 suppdm Row 1/2/Note、标题粘连、bullet 拼接伪差 |
| 80 | SE spec 尾 / 脚注 / SE – Assumptions 引言 + 1-3 | 18 / 4 / 3→3 (CT `*` ETCD/ELEMENT + 脚注) | SE/asm :25-35 一致 | speccmp 8 变量 + ETCD 渲染核 (bbox 漏读: Label/Type/CT `*`/Role/Core/Notes 1-2 一致) | 未命中 = spec 列粘连; 脚注 gap F → SE/spec.md:123 |
| 81 | asm 4-11 / SE – Examples 引言 | 28 / 0 / 0 | SE/asm :37-54、SE/ex :3 一致 | — | :39 `where -\n-SEQ` 换行伪差 |
| 82 | Ex1 叙述 / se.xpt / dm.xpt r1-2 | 29 / 1 / 0 | SE/ex :5-47 一致 | se.xpt census OK (10×9); dm.xpt 渲染逐格 (下) | 未命中 = dm 表头 (BIRTHDTC, SE T-1) |
| 83 | dm r3 / Ex2 叙述 / se.xpt / Row 1-2 / dm r1 | 24 / 2 / 1→1 | SE/ex :48-81 一致 | se.xpt census OK (6×9); dm 渲染逐格 | 补: Ex2 Row 2 "The subject's assignment to Rescue treatment … proceeded as planned." (SE/ex:75 句中插入) |
| 84 | dm Ex2 r2 / (§5.4 SM 别节) | 15 / 15 / 0 | SE/ex :82 一致 | dm 渲染逐格 | 15 未命中全属 SM (别节) 与表尾残字 |
| 427 | §8 章引言 (ch08) / §8 IDVAR 段 + 3 bullet | 25 / 11 / 0 | RELREC/asm :5-10 (D6 note + 段 + 3 bullet) 一致 | — | 11 未命中 = 章标题 + 首段 + 8 bullet (§8 章引言, 见需主控定 #2) |
| 428 | §8.1 (ch08 别节) | 21 / 17 / 0 | — | (cm.xpt 不在本批文件) | 全页别节 |
| 429 | §8.2 / §8.2.1 Description / Spec / spec / 脚注 | 24 / 11 / 2→2 (CT `*` IDVAR + 脚注) | RELREC/asm :12-30 一致 | speccmp 7 变量 | 未命中 = 标题粘连、列表拼接 ("either: explicit…" KB :20-22 实有)、spec 列粘连; 脚注 gap F → RELREC/spec.md:71 |
| 430 | §8.2.2 Ex1-3 / §8.3 | 14 / 2 / 0 | RELREC/ex :5-53、RELREC/asm :32-36 一致 | relrec Ex1-3 census OK | 2 未命中 = 标题粘连; "COMBO 1" vs 表 COMBO1 照录 (B-REL 已登记) |
| 431 | §8.3.1 Ex1 / RELTYPE 组合 / (§8.4 别节) | 28 / 11 / 0 | RELREC/ex :55-68、RELREC/asm :38-46 一致 | relrec census OK | 未命中 = 标题/表头粘连 + §8.4 SUPPQUAL 别节; `‑‑LNKID` U+2011 (S-TYPO) |
| 437 | (§8.6 别节) / §8.7 / RELSUB Description | 23 / 20 / 0 | RELSUB/asm :5-9 一致 | — | 20 未命中全属 §8.6 (ch08) |
| 438 | RELSUB Spec / spec / 脚注 / asm 1-8 | 30 / 7 / 1→1 (脚注) | RELSUB/asm :11-31 一致 | speccmp 5 变量 | 未命中 = spec 列粘连 + asm 7 句末无句号 (T-9 沿用); 脚注 (PDF 上标 1 独占一行) → RELSUB/spec.md:53 |
| 439 | RELSUB Ex1 / §8.8 / RELSPEC Description / Spec / spec / 脚注 | 24 / 13 / 1→1 (脚注) | RELSUB/ex 全文、RELSPEC/asm :5-13 一致 | dm / relsub census OK; speccmp 5 变量 + STUDYID layout 核 (bbox 漏读: 一致) | 未命中 = 标题粘连、spec 列粘连、他域文件内容 (lscan 按域分跑); 脚注 → RELSPEC/spec.md:62 |
| 440 | RELSPEC asm 1-3 / Examples / 图 / relspec | 11 / 2 / 0 | RELSPEC/asm :15-21、RELSPEC/ex 全文一致 (Mermaid = D6 既有) | relspec census OK | 2 未命中 = 标题与图题粘连; T-7 "is does not" 照录 (沿用) |
| 441 | §9 章引言 / §9.1 (DI) / §9.2 / OI Description / Spec / spec / 脚注 | 18 / 15 / 6→6 | DI/asm 全文、OI/asm :1-11 一致 | speccmp 7 变量; 渲染 p441 | 补: DI 顶部 `## §9 Study References` + 段 + 2 bullet (U3/O46); OI `## OI – Description/Overview` (gap D)、`## OI – Specification` + oi.xpt 首句 (gap S)、CT `*` OIVAL、脚注 (gap F; 原子 id 标 p0443, 实在 p441 OI 表下). DI/OI 合跑 lscan 未命中仅标题粘连 |
| 442 | OI – Assumptions 1-5 / Examples / Ex1 / oi r1-5 | 28 / 2 / 1→1 | OI/asm :13-30、OI/ex :1-23 一致 | oi.xpt census OK | 补 `## OI – Assumptions` (gap A); 另 1 未命中 = Examples 标题粘连; rscan OI/asm :15/:21 = `non-\ntaxonomy`、`HCV1a-\nH77` 折行伪差 |
| 443 | oi r6-14 | 1 / 0 / 0 | OI/ex :24-32 一致 | census OK | |
| 444 | (§10 ch10 别节) | 别节 | — | — | |

- spec.md 非变量行 (KB→PDF): H1、`> Source text:` (D7)、`> Class: … | Structure: …`、`---`、`## Cross References` 块 = 纯导航 (U8), 不标 D6.
- 五域 spec 变量集合 / 顺序与 PDF 一致 (SE 13 / RELREC 7 / RELSUB 5 / RELSPEC 6 / OI 7); Label/Type/Role/Core/CDISC Notes 全一致; CT 列剩余差异仅 DOMAIN (U6: SE, OI) 与 C-code 记法 (U5: EPOCH, RDOMAIN, RELTYPE, SREL, SPEC, OIPARMCD, OIPARM), 归 S-CT 批.

### spec.md Controlled Terms `*` (`grep -c "Char \*"` p79/80/429/438/439/441 = 0/2/1/0/0/1 = 4 + 渲染)
| 域 | 变量 | PDF 页 | KB 改后行 |
|---|---|---|---|
| SE | ETCD / ELEMENT | 80 | spec.md:45 / :54 |
| RELREC | IDVAR | 429 | spec.md:38 |
| OI | OIVAL | 441 | spec.md:63 |

### census_items 逐格 (渲染 110dpi)
| 表 | 渲染 | 结果 |
|---|---|---|
| SE/examples.md:44 Ex1 dm.xpt (p82-83) | p82 / p83 | 3 行 × 20 列逐格一致 (r1-2 p82, r3 p83; ARMNRS/ACTARMUD 空; r2 ARMCD OI / ARM ORAL-IV / ACTARMCD IO / ACTARM IV-ORAL); 表头仅 col 8 PDF `BIRTHDTC` / KB `BRTHDTC` = **SE T-1**, KB 不改 |
| SE/examples.md:79 Ex2 dm.xpt (p83-84) | p83 / p84 | 2 行 × 20 列逐格一致 (r1 ARMCD/ARM/ACTARMCD/ACTARM 全 A; r2 ACTARMCD/ACTARM 空、ARMNRS UNPLANNED TREATMENT、ACTARMUD "Drug B dispensed for part of Drug A element"); 表头 col 8 = **SE T-1** |
- table_census.py (manifest = 复核页范围): before = after `KB 表 12: OK 10 / DIFF 2, diffs 2`; DIFF 2 = 上表 SE T-1 两处 (HEADER col 7 BRTHDTC/BIRTHDTC).
- 其余 10 表 census OK (SE se.xpt ×2; RELREC relrec ×4; RELSUB dm/relsub; RELSPEC relspec; OI oi.xpt 跨 p442-443); B-REL 已渲染逐格 7 张 REL 表, 本批未改表.

### 变更清单 (行号 = 改后)
| # | kb_file:line | ref | action | before → after 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 1 | SE/assumptions.md:7 | ig34_p0079_a004 (原子 verbatim 抄自旧 KB) | REPLACED | "through the study elements" → "through the epochs and elements" (渲染确认) | 79 |
| 2 | SE/assumptions.md:11 | ig34_p0079_a006 (同上) | REPLACED | "definitions of ELEMENT values in" → "definitions (TESTRL values) in" | 79 |
| 3 | SE/assumptions.md:17 | ig34_p0079_a009 (同上) | REPLACED | `– DTC` (en dash + 空格) → `--DTC` (变量前缀 CODE_LITERAL, 非单纯排版字符; 见需主控定 #4) | 79 |
| 4 | SE/assumptions.md:18 | ig34_p0079_a010 (同上) | REPLACED | "Such variables can relate" → "Such variables relate"; `(–DY)` → `(--DY)` | 79 |
| 5 | SE/assumptions.md:21-23 | pdf:p79 SE – Specification + se.xpt 句 | INSERTED | `## SE – Specification` + spec 首句 (gap S; CM/PP 先例, Description 与 Assumptions 之间) | 79 |
| 6-7 | SE/spec.md:45 / :54 | pdf:p80 ETCD / ELEMENT CT | REPLACED | Controlled Terms 空 → `*` | 80 |
| 8 | SE/spec.md:123 | ig34_p0080_a010 | INSERTED | `> ¹In this column…` (U2/U7, `---` 后、Cross References 前; gap F) | 80 |
| 9 | SE/examples.md:75 | pdf:p83 Ex2 Row 2 句 3 | INSERTED | "…deviated from plan." 后补 "The subject's assignment to Rescue treatment for the open treatment epoch proceeded as planned." (R3 新增) | 83 |
| 10 | RELREC/spec.md:38 | pdf:p429 IDVAR CT | REPLACED | 空 → `*` | 429 |
| 11 | RELREC/spec.md:71 | ig34_p0429_a030 | INSERTED | 脚注 (gap F) | 429 |
| 12 | RELSUB/spec.md:53 | ig34_p0438_a011 | INSERTED | 脚注 (gap F; PDF 上标 1) | 438 |
| 13 | RELSPEC/spec.md:62 | ig34_p0439_a039 | INSERTED | 脚注 (gap F) | 439 |
| 14 | OI/spec.md:63 | pdf:p441 OIVAL CT | REPLACED | 空 → `*` | 441 |
| 15 | OI/spec.md:69 | ig34_p0443_a001 (内容在 p441) | INSERTED | 脚注 (gap F) | 441 |
| 16 | OI/assumptions.md:3 | pdf:p441 OI – Description/Overview | INSERTED | 标题 (gap D; 两段描述原在 H1 下, 文字未改) | 441 |
| 17 | OI/assumptions.md:9-11 | pdf:p441 OI – Specification + oi.xpt 句 | INSERTED | 标题 + spec 首句 (gap S) | 441 |
| 18 | OI/assumptions.md:13 | pdf:p442 OI – Assumptions | INSERTED | 标题 (gap A) | 442 |
| 19 | DI/assumptions.md:3-8 | intros §9 / O46 (ig34_p0441_a002/a003…) | INSERTED | `## §9 Study References` + 章引言段 + 2 bullet (U3; narrow (a)); 逐字核 True (命令见下) | 441 |
| 20 | DI/assumptions.md | narrow (b) DI spec 脚注 | SKIPPED_STRUCT | 不适用: SDTMIG v3.4 §9.1 无 DI spec 表 (仅指向 SDTMIG-MD), p441 唯一脚注属 OI 表 (已入 OI/spec.md) | 441 |
| 21 | RELREC/assumptions/examples, RELSUB/*, RELSPEC/asm+ex, OI/examples | 全扫 | VERIFIED | 无差异 (B-REL 终态) | 427-443 |
- 实改 19 处 (#1-#19); #20 跳过; #21 核验. 新增 atom 清单 (R3, gaps 之外): #1-#4 (原子 verbatim 抄自旧错 KB, 见 fp 段)、#9、CT `*` 4 格.

### 结构改动清单 (reviewer 逐条签字)
| # | 位置 | 改动 | 依据 |
|---|---|---|---|
| S-1 | SE/assumptions.md:21 | 新增 `## SE – Specification` | gap S; PDF p79 标题 |
| S-2 | OI/assumptions.md:3 / :9 / :13 | 新增 `## OI – Description/Overview` / `– Specification` / `– Assumptions` | gaps D/S/A; PDF p441-442 标题 |
| S-3 | DI/assumptions.md:3 | 新增 `## §9 Study References` (H2, NV §6.3.7 / FT §6.3.9 先例) | U3 / O46 |
- 无整条 assumptions 增删 / 挪位 / 拆合.

### 删除清单
| # | 原位置 (base) | 改后 | 原因 |
|---|---|---|---|
| D-1 | SE/assumptions.md:7 / :11 / :17 / :18 旧词 ("study elements"、"of ELEMENT values"、`– `/`–`、"can") | #1-#4 | VALUE_DIFF 旧值替换 (行仅承载本句原子, 原子 verbatim 即旧 KB 文本) |
| D-2 | SE/RELREC/OI spec CT 空值 4 格 | `*` | U2 |
- 无整条删除.

### D6 / KB_AUTHORED
- 本批无新增 D6. 既有: RELREC/assumptions.md:5 (B-REL §8 引言说明)、RELSPEC/examples.md:11 (Mermaid) — 复核不矛盾, 不变.
- 纯导航保留不标: 各 `> Source text:` 行 (D7)、RELREC/examples `## Peer Record Examples` / `## Dataset Relationship Example` / `### Example n`、表前 `**xx.xpt**`、`**Row n:**` 标签; 五域 spec `> Class|Structure` 与 Cross References (U8); DI `## DI – Description/Overview (§9.1)` 既有标题 (规则 6).

### PDF_TYPO (复核沿用编号; 新增 SE T-1/T-2, OI T-1/T-2)
- **SE T-1 (新)**: SE/examples.md:44 / :79 dm.xpt 表头 PDF `BIRTHDTC` (p82, p83, p84) vs KB `BRTHDTC`. 依据: DM spec 与 DM 例 (p63/65/66/68 layout `grep -c BRTHDTC` 2/1/1/1; p60-79 `BIRTHDTC` 仅 p82-84) → 正确值由 PDF 自身确定, KB 保留 `BRTHDTC`.
- **SE T-2 (新, 照录)**: SE/spec.md:39 SESEQ "Should be assigned to be consistent chronological order" (p79, 缺 "with"); KB 与 PDF 同, 照录 (同 MS T-5 口径).
- **OI T-1 (新, 照录)**: OI/spec.md:39 OISEQ "Sequence number to given to ensure…" (p441); 照录.
- **OI T-2 (新, 照录)**: OI/spec.md:30 NHOID "…pairs of OIPARMCD and OIVAL ." (句点前空格, p441 渲染); 照录.
- 沿用 (B-REL / B-ch08): T-7 RELSPEC "is does not" 照录 (RELSPEC/assumptions.md:19); T-9 RELSUB asm 7 句末句号 KB 补 (RELSUB/assumptions.md:29); RELREC Ex3 "COMBO 1" vs 表 COMBO1、RELSPEC 图 "(Brain)" vs 表 TISSUE 照录 — p430/p440 复核成立.
- 未登记排版差 (S-TYPO): SE/asm :7/:11/:15 等 `subject's` 直引号 vs PDF 弯引号、:18 `"Day within Element"` 直引号; RELREC/ex:68 `--LNKID` vs PDF U+2011; RELREC/ex:42 "COMBO 1" 直引号 (B-REL 已记).

### 范围外 / out_of_scope 处理
- **O46** → DI 顶部已补 §9 章引言 (#19). OI 不再加交叉引用 (U3 只要求首域). ch10 副本见需主控定 #3.
- 新范围外: 无 KB 错. 原子抽取错 (供 T3 台账): ig34_p0079_a004/a006/a009/a010 verbatim = 旧错 KB 文本 (非 PDF).

### 需主控定
1. **DI narrow (b) 不适用**: DI 无 spec 表 (IG v3.4 §9.1 只一段, spec 在 SDTMIG-MD), p441 脚注属 OI; 未在 DI 加脚注 (#20). 请确认关闭.
2. **§8 章引言 (p427 首段 + 8 bullet)**: U3 口径会指向 §8 首域 (RELREC/assumptions 顶部), 但本批 `intros[]` 未列, 且全文已在 ch08 (B-ch08). 本批未补; RELREC 仅保留 B-REL 已有的 IDVAR 段. 是否补 (或只加一行交叉引用) 由主控定.
3. **ch10 重复**: `chapters/ch10_appendices.md:64-69` `## Section 9: Study References (p441)` 现与 DI/assumptions.md §9 引言逐字重复. 按 dispatch notes "KB 自写附录与 PDF 重复 → 留 PDF 所属节那份, 附录改一行交叉引用", 但 ch10 非本批文件 (S-CH 批), 未改.
4. **SE `– DTC` → `--DTC` (#3/#4)**: 按 CODE_LITERAL 值差修 (en dash + 空格替代两个连字符, 改变变量前缀写法), 非 U1 排版字符; 若主控认定归 S-TYPO, 回退两处即可.
5. **json 页范围 (O20)**: RELSPEC hi 441→440; OI 442-444 → 441-443 (§9.2 标题 / spec 在 p441); RELREC 实际承载 p427、p429-431. gap 原子 `ig34_p0443_a001` 页号与内容 (p441 OI 脚注) 不符.
6. fp 预期回归 4 条 (ig34_p0079_a004/a006/a009/a010, verbatim 抄自旧错 KB) 需主控并入 `work/t2_fp_expected_regressions.jsonl`.

### fp_match (before = kbbase HEAD; after = 工作区, 含并行批改动)
- 批内页 (79-84, 427-431, 437-443) 逐原子变化 6 条: 预期回归 4 (上条 #6, 渲染 p79 证 KB 改后 = PDF); 新命中 2: ig34_p0441_a002 / a003 hit_any ch10 → DI/assumptions.md (§9 引言). 其余无变化.

### 验证命令
```
S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/d6800696-3318-4d1d-9806-05c60470220c/scratchpad/t2s_S-SPREL_writer
K=knowledge_base/domains
for d in SE:79,80 RELREC:429 RELSUB:438 RELSPEC:439 OI:441; do python3 -I $S/speccmp.py $S ${d%%:*} ${d#*:} | grep -v " OK$"; done   # 剩 DOMAIN (U6) + C-code (U5); SE STUDYID/ETCD、RELSPEC STUDYID bbox 漏读 → 渲染/layout 核
python3 -I $S/lscan.py SE 79 84; python3 -I $S/lscan.py RELREC 427 431; python3 -I $S/lscan.py RELSUB 437 439; python3 -I $S/lscan.py RELSPEC 439 440; python3 -I $S/lscan.py OI 441 443
python3 -I $S/rscan2.py 79-84 $K/SE/assumptions.md $K/SE/examples.md; python3 -I $S/rscan2.py 441-443 $K/OI/assumptions.md $K/OI/examples.md; python3 -I $S/rscan2.py 441-441 $K/DI/assumptions.md   # 余: SE :39 / OI :15 :21 折行伪差
python3 -I -c "import re;t=open('.work/10_tier_b_repair/work/pdf_pages/ig34_p0441.txt').read();p=re.sub(r'\s+',' ',t[t.index('There are occasions'):t.index('9.1 Device')].replace('•','')).strip();k=open('$K/DI/assumptions.md').read();k=re.sub(r'\s+',' ',k[k.index('There are occasions'):k.index('## DI –')].replace('\n- ',' ')).strip();print(p==k)"   # True
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json   # KB 表 12: OK 10 / DIFF 2 (SE T-1)
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --kb-root $S/kbbase/knowledge_base --out $S/fp_before.jsonl; python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl
python3 tools/check_links.py 2>&1 | grep "live docs"   # 42
```

### git diff --stat (本批文件)
```
 knowledge_base/domains/DI/assumptions.md |  7 +++++++
 knowledge_base/domains/OI/assumptions.md |  8 ++++++++
 knowledge_base/domains/OI/spec.md        |  4 +++-
 knowledge_base/domains/RELREC/spec.md    |  4 +++-
 knowledge_base/domains/RELSPEC/spec.md   |  2 ++
 knowledge_base/domains/RELSUB/spec.md    |  2 ++
 knowledge_base/domains/SE/assumptions.md | 12 ++++++++----
 knowledge_base/domains/SE/examples.md    |  2 +-
 knowledge_base/domains/SE/spec.md        |  6 ++++--
 9 files changed, 38 insertions(+), 9 deletions(-)
```
- writer.jsonl: `work/t2_batches/S-SPREL.writer.jsonl`.

### 更正 (同 attempt, 自查后; 以本段为准)
- **逐页日志 "PDF→KB 未命中" 列**: 表中 p79 11 / p80 4 / p83 2 为改前数. 改后全部重跑 (`$S/lscan_after.txt`, 命令同验证块): p79 6 / p80 3 / p81 0 / p82 1 / p83 1 / p84 14 / p427 11 / p428 17 / p429 10 / p430 2 / p431 11 / p437 20 / p438 6 / p439 12 (RELSUB 跑) · 13 (RELSPEC 跑) / p440 2 / p441 13 / p442 1 / p443 0. 残留全部归类: 别节 (p79 上部 DM、p84 SM、p427 章引言、p428 §8.1、p431 §8.4、p437 §8.6)、标题/表名粘连、spec 列粘连、bullet 拼接伪差、RELSUB T-9 (p438)、按域分跑时他域内容 (p439). 无未归类残留.
- **p441 行 "DI/OI 合跑 lscan"**: 该命令因 DI 无 examples.md 报 FileNotFoundError, 未跑成. 实际证据 = `rscan2.py 441-441 DI/assumptions.md` 无输出 (KB→PDF 全命中) + 逐字比较一行命令输出 `True` (PDF→KB). OI 侧 = `lscan.py OI 441 443` (p441 13 未命中 = DI §9/§9.1 文本 (不在 OI 文件) + 标题/列粘连).
- **渲染**: 本 session 实际打开 p79/80/82/83/84/429/438/440/441 (110dpi). p429 确认 IDVAR CT `*` 与脚注上标 1; p438 确认 RELSUB 脚注上标 1、asm 7 句末无句号 (T-9); p440 确认图: L1 SPC-001(Tissue)/SPC-003(Brain), L2 SPC-001-A/-B(Tissue)/SPC-003-A(RNA), L3 SPC-001-B-1(DNA), 边 4 条 = RELSPEC/examples.md Mermaid 一致 (D6 不矛盾); relspec 表 6×7 一致, Row 5 SPEC=TISSUE vs 图 "(Brain)" 照录. **p430 未渲染**: "COMBO 1" vs COMBO1 仅 layout 文本复核.
- **SE T-1 依据措辞**: "p60-79 BIRTHDTC 仅 p82-84" → 实际 grep 范围为 p60-89 (`grep -l BIRTHDTC ig34_p00{6,7,8}*.txt` → 仅 p82/p83/p84); BRTHDTC 见 p63 (2) / p65 / p66 / p68.
- **覆盖矩阵** (`MATRIX_TAG=S-SPREL python3 .work/10_tier_b_repair/work/scratch/t2/global/t2_coverage_matrix.py`, 输出 `work/scratch/t2/global/t2_coverage_matrix.S-SPREL.md`): OI / RELREC / RELSPEC / RELSUB 全 Y、脚注 1/1、a:F e:F s:F; **SE 脚注 0/1** = 原子 ig34_p0080_a010 verbatim 以 `*In this column` 开头 (上标 1 被抽成 `*`, 渲染 p80 为上标 1), strip_fn 不剥 `*` → 仅 PARTIAL; KB SE/spec.md:123 正确 (原子抽取错, 需主控在矩阵侧豁免). **DI 脚注 0/1** (B-DI 行, 页 441-442) = 矩阵把 p441 OI 表脚注算进 §9.1 → 与需主控定 #1 同源 (narrow (b) 即由此而来), 非 DI 缺口. O46 PASS.
- 验证块逐字粘贴复跑: DI 逐字比较 `True`; check_links live docs 42; census OK 10 / DIFF 2.
