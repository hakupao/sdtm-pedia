# T2 B-SR writer checkpoint
## attempt 1 (2026-11-26, oh-my-claudecode:executor / opus)
- base HEAD `c8802bf54719883e69429efd312833bfbce63692`; kb_files = `knowledge_base/domains/SR/examples.md`
- md5 before `692176191e5a13f3d9236c4f843305ec` → after `7a922f67c013c4e6148bfd3d63226571`
- atoms 0 / t2_recheck 0 / census DIFF 4 tables (13 KB rows) / pdf_only 0 / unparseable 0
- Truth: `work/pdf_pages/ig34_p0375..0381.txt` + renders p378-381 (r110) + p380 (r200), scratch `scratchpad/t2_B-SR_writer/`
- pdf_ranges ig34 375-381 covers whole §6.4.5 incl. intro page p375 (O20 OK). Note p375-378 Description/Spec/Assumptions belong to SR/assumptions.md + spec.md (not in kb_files).

### 变更清单
| # | kb_file:line (改后) | ref | action | before → after 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 1 | examples.md:22 | census:SR/examples.md:14 Row7 SROBJ | SKIPPED_PDF_TYPO (T-1) | KB `Johnson Grass 0.15 BAU/mL` 保留; PDF `0.15 BAU mL` (缺斜杠) | 378 |
| 2 | examples.md:67 | census:SR/examples.md:64 Row2 | REPLACED | EX/EXSPID/1 → SR/SRSPID/7 (按 PDF 行序) | 380 |
| 3 | examples.md:68 | census Row3 | REPLACED | SR/SRSPID/7 → EX/EXSPID/1 | 380 |
| 4 | examples.md:69 | census Row4 | verified, no change | SR SRSPID 2 R2 = PDF | 380 |
| 5 | examples.md:70 | census Row5 | REPLACED | EX/EXSPID/2 → SR/SRSPID/8 | 380 |
| 6 | examples.md:71 | census Row6 | REPLACED | SR/SRSPID/8 → EX/EXSPID/2 | 380 |
| 7 | examples.md:72 | census Row7 | verified, no change | SR SRSPID 3 R3 = PDF | 380 |
| 8 | examples.md:73 | census Row8 | REPLACED | EX/EXSPID/3 → SR/SRSPID/9 | 380 |
| 9 | examples.md:74 | census Row9 | REPLACED | SR/SRSPID/9 → EX/EXSPID/3 | 380 |
| 10 | examples.md:97 | census:SR/examples.md:95 Row1 SRTESTCD | REPLACED | `DRLDOM` → `IDRLDIAM` | 380 |
| 11 | examples.md:97-99 | census Row1-3 SRDTC | REPLACED (T-2, 主控/T4 裁定) | `2011-01-19T14:26` → `2011-01-19T14:08:24` (×3) | 380 |
| 12 | examples.md:107 | census:SR/examples.md:105 Row1 AGTRT | REPLACED | `tuberculin PPD-S` → `Tuberculin PPD-S` | 380 |
| 13 | examples.md:87 | new-atom N-1 (Ex3 叙述) | REPLACED (R2 词丢失, 原位恢复) | "standard PPD" → "standard tuberculin PPD" | 380 |
| 14 | examples.md:87 | new-atom N-2 (Ex3 叙述) | REPLACED | "Time point variables show" → "The time point variables show" | 380 |

Ex2 relrec: 只交换行内容, Row 号不动 (PDF 每组 R1-R3 为 SR, SR, EX; KB 原为 SR, EX, SR). R4-R6 原本已与 PDF 一致. census 的 PDF_ROW_MISSING/KB_ROW_UNMATCHED 各 1 即此错位所致.
#13/#14 行 :87 是单段叙述, 不承载其他已判原子 (本批 atoms=0), 故原位恢复 PDF 原词而非追加重复句 (按 "词替换型改写" 口径).

### 新增 atom 清单 (R3)
- N-1, N-2: 见 #13/#14 (Ex3 叙述 p380, census 不覆盖叙述).

### PDF_TYPO 登记
- **T-1** (p378 Ex1 Row 7 SROBJ): PDF 写 `0.15 BAU mL`, 同表 Row 5/6/8 均 `BAU/mL` → 正确值可由同表确定, KB 保留 `BAU/mL`. 注意 p376 SROBJ CDISC Notes 也写 `"Johnson Grass IgE 0.15 BAU mL"` (spec.md:93 照录, 非本批).
- **T-2** (p380 Ex3 SRDTC, 需主控 / T4 用户裁定): 表 3 格一致为 `2011-01-19T14:08:24`; 叙述称 SRDTC 与 SRRFTDTC (`2011-01-17T08:30:00`) 相差 53 h 56 min (→ 推得 14:26:00), 而表值推得 53 h 38 min 24 s. PDF 自相矛盾, 无第三来源判定哪边错 → 按 B-CP 补充口径 "无法由 PDF 自身确定 → 照录 PDF 并登记 T4" 改成表值; 叙述逐字保留. 旧 KB 值 `14:26` 在 PDF 任何位置都不存在 (KB 自推). 与 writer v1.0 规则 2 ("文字与表矛盾 → 不改 KB") 冲突, 已按较新的 dispatch notes 执行, 请主控确认; 若改判, 回退 3 格即可.

### 双向扫描 (examples.md 全文件 vs p378-381)
- KB→PDF: 全部非表行逐句命中 (规范化空白/粗体), 唯一未命中 :1 文件标题 `# SR — Examples` (导航).
- PDF→KB: p378-381 叙述句全部命中; 未命中只有 p378 假设 3/4 (属 SR/assumptions.md, 已逐字在) 和 "SR – Examples" 节标题 (KB 用文件标题承载).
- 表格: Ex1 sr (8 行)、Ex2 sr (12 行)、ex (6 行)、relrec (18 行)、Ex3 sr (3 行)、ag (1 行)、relrec (2 行) 全部对渲染逐格核过, 改后一致 (除 T-1).

### 范围外发现 (不在 kb_files, 只报告)
- O-1 SR/assumptions.md 缺 p375 `SR – Description/Overview` 标题 + 句 "A findings about domain for submitting dermal responses to antigens." (= B-FA review 的 p0375_a025/a026 未命中原子) 和 p376 spec 首句 `sr.xpt, Skin Response — Findings About. One record per finding, per object, per time point, per visit per subject, Tabulation.`; 建议按 CM/IS 先例补在 SR/assumptions.md 标题后、Assumptions 前 (该句目前只在 terminology/core/general_part4.md:225 的 CT 定义中出现).
- O-2 SR/assumptions.md 无 `SR – Assumptions` 节标题 (文件标题承载, 导航, 可不改).
- O-3 FA/assumptions.md 末尾 `## §6.4.5 Skin Response (SR)` 标题下为空; 建议改为一行交叉引用到 `domains/SR/assumptions.md` (FA 不在本批白名单).
- O-4 PDF p377 假设 2 `reactogencity` 是 PDF 拼写错; SR/assumptions.md:5 写 `reactogenicity` (正确拼写, 按口径保留, 登记即可). 假设 1-4 其余逐字一致.
- O-5 spec.md:93 SROBJ 例 `BAU mL` 照录 PDF p376 (与 T-1 同型, 若主控要统一请定).

### 删除清单
无 (仅 VALUE_DIFF 替换旧值).

### 触碰的 unparseable 表
无.

### git diff --stat
```
 knowledge_base/domains/SR/examples.md | 22 +++++++++++-----------
 1 file changed, 11 insertions(+), 11 deletions(-)
```

## attempt 1 续 (主控裁定后, 2026-11-26)
主控裁定: T-2 照录 PDF 表值 + T4 维持; kb_files 扩入 SR/assumptions.md、SR/spec.md、FA/assumptions.md.
- md5 base (HEAD c8802bf) → after: SR/assumptions.md `513cc3f2…2b96a2d4490615ac23` → `07dc4c58871d5cb2bcee81e75c38e362`; SR/spec.md `dee060f5f1f38ab888e233a9e6eb0841` → `98701503013afc84824ac2a3e8a3e603`; FA/assumptions.md `b56ccc20cfe93860462abe1d9ad0bd62` → `7f72cfcc6a119808ee97e91d2cfb4317`; SR/examples.md 不变 (`7a922f67…6571`)

### 变更清单 (续)
| # | kb_file:line (改后) | ref | action | before → after 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 15 | SR/assumptions.md:3 | ig34_p0375_a025 (heading) | INSERTED | 新增 `## SR – Description/Overview` (PDF 原标题) | 375 |
| 16 | SR/assumptions.md:5 | ig34_p0375_a026 | INSERTED | Description 句逐字 ("A findings about domain for … antigens.") | 375 |
| 17 | SR/assumptions.md:7 | new-atom N-3 (p376 heading) | INSERTED | 新增 `## SR – Specification` | 376 |
| 18 | SR/assumptions.md:9 | new-atom N-4 (spec 首句) | INSERTED | `sr.xpt, Skin Response — Findings About. One record per …, Tabulation.` 逐字 | 376 |
| 19 | SR/assumptions.md:11 | new-atom N-5 (p377 heading) | INSERTED | 新增 `## SR – Assumptions` (CM 先例结构; 假设 1-4 原文不动) | 377 |
| 20 | SR/spec.md:93 | T-1 同型 (SROBJ CDISC Notes) | SKIPPED_PDF_TYPO → REPLACED | `"Johnson Grass IgE 0.15 BAU mL"` → `BAU/mL` (主控指令, 按 T-1 口径) | 376 |
| 21 | FA/assumptions.md:119 | O-3 | INSERTED | 空 `## §6.4.5 Skin Response (SR)` 下加一行交叉引用 `> See [SR – Assumptions](../SR/assumptions.md) …` (导航, 不加 D6) | 375 |

结构按 CM/assumptions.md 先例 (Description/Overview → Specification → Assumptions 三标题). 原文件标题 `# SR — Assumptions` 和假设 1-4 未改.
FA 交叉引用: grep `6.4.5` 全 KB (除 terminology) 仅 FA:69/:82 叙述引用与 ch10:283 表格行, 无指向该标题锚点的链接; 未改标题文字, 锚点不受影响.

### PDF_TYPO 登记 (续)
- **T-1** 扩展: spec.md:93 同型 `BAU mL` 亦改为 `BAU/mL` (依据同 T-1: p378 同表 Row 5/6/8 + 单位写法).
- **T-3** (p377 假设 2 `reactogencity`): PDF 拼写错, SR/assumptions.md:15 保留正确拼写 `reactogenicity`, 只登记.
- **T-2** 主控已裁定: 照录表值, T4 用户裁定项保留.

### spec.md 逐格复核 (39 变量 vs p376-377)
- 方法: `pdftotext -f 376 -l 377 -bbox` 词框按表头 x 列界拼格 ($S/spec_cmp.py, 独立于 layout 文本), 比 Label / Type / Role / CDISC Notes / Core 全字段; Controlled Terms 列人工比对.
- 结果: 39/39 变量、顺序一致; Label/Type/Role/Core 0 差. Notes 差 3 条均非缺陷: SROBJ = 本次 T-1 改动; SRDY `sponsor- defined` KB 与 PDF 原样一致 (脚本归一化伪差); SRRFTDTC = 页尾脚注/假设文本串入脚本格 (前缀全一致).
- Controlled Terms: KB 用 C-code (SRTESTCD C112024 / SRTEST C112023 / UNIT C71620 / ND C66789 / SPECTYPE C78734 / LOC C74456 / LAT C99073 / METHOD C85492 / NY C66742 / EVAL C78735 / EPOCH C99079), 对应 PDF 括号 codelist 名, KB 全库惯例, 未改. DOMAIN 行 PDF CT 列为 `SR`, KB 空 — 与 FA/CM/AE/IS spec.md 同为空 (全库惯例), 记范围外 O-6, 未改.
- spec 脚注 "1 In this column, an asterisk (*) …" (p377): KB spec.md 无; 与其他域 spec.md 一致 (全库格式), 记 O-6 一并, 未改.

### 复跑校验 (隔离: $S/before_root = git archive HEAD; $S/after_root = HEAD + 本批 4 文件; diff -rq 仅 4 文件不同)
- census: `python3 -I .work/10_tier_b_repair/scripts/table_census.py --pages ig34:378-381 --kb knowledge_base/domains/SR/examples.md --kb-root $S/{before,after}_root/knowledge_base --out $S/census_{before,after}.json` → before `DIFF 4 / OK 3, cells 641, diffs 21`; after `DIFF 1 / OK 6, cells 649, diffs 1` (仅 T-1 Row7 SROBJ, 有意保留). (p375 范围含 FA 表会被报 PDF_ONLY, 故取 378-381.)
- fp: `python3 -I .work/10_tier_b_repair/scripts/fp_match.py --kb-root $S/before_root/knowledge_base --out $S/fp_before.jsonl`; `… --kb-root $S/after_root/knowledge_base --out $S/fp_after.jsonl --baseline $S/fp_before.jsonl --regress-out $S/fp_regress.jsonl` → `regressions=0 new_hits=0 RESULT: GREEN` (SR+FA 回归 0). p0375_a025/a026 不在 fp 原子集 (ledger 记 EQUIVALENT, md_atom_ids 空), 另用 `fp_match.norm` 直查 SR/assumptions.md: 5 条新增标题/句全部命中.
- check_links: `python3 tools/check_links.py | tail -1` → `broken relative links: 18668 (live docs: 42)` (基线 42, 不升).

### 删除清单 (续)
无.

### 范围外 (续)
- O-6 spec.md DOMAIN 行 CT `SR` 空 + 无 spec 表脚注: 全库 spec.md 格式惯例, 交 O15/O16 全域扫描定.

### git diff --stat (4 文件)
```
 knowledge_base/domains/FA/assumptions.md |  2 ++
 knowledge_base/domains/SR/assumptions.md | 10 ++++++++++
 knowledge_base/domains/SR/examples.md    | 22 +++++++++++-----------
 knowledge_base/domains/SR/spec.md        |  2 +-
 4 files changed, 24 insertions(+), 12 deletions(-)
```

## attempt 1 续 2 (reviewer PASS 后 LOW 收尾, 2026-11-26)
| # | kb_file:line | ref | action | before → after | PDF 页 |
|---|---|---|---|---|---|
| 22 | SR/spec.md:336 | T-4 (SRELTM CDISC Notes) | REPLACED (keep-correct) | `indicated by EGTPTREF` → `indicated by SRTPTREF` | 377 |

- **T-4** PDF_TYPO keep-correct: p377 SRELTM 注释首例写 `EGTPTREF` (EG 域复制残留); 依据 = 同表全部 SR-- 前缀 + 该行 label "Planned Elapsed Time from Time Point Ref" + 同一注释第二例与 Notes 前句均为 SRTPTREF → 可由 PDF 自身确定.
- 因此不再逐字命中的原子: `ig34_p0377_a015` (TABLE_ROW, SRELTM 整行; ledger PARTIAL → md_dmSR_ex_a072). 该原子不在 fp_match 原子集, fp 无影响; 由 T-4 登记覆盖. 其他含 EGTPTREF 的 p377 原子: 无.
- md5 SR/spec.md → `357560ced94a7af7cd13b48723094ec8`; 文件内 EGTPTREF 剩 0.
- fp: `python3 -I .work/10_tier_b_repair/scripts/fp_match.py --kb-root $S/after_root/knowledge_base --out $S/fp_after2.jsonl --baseline $S/fp_before.jsonl --regress-out $S/fp_regress2.jsonl` → `regressions=0 new_hits=0 RESULT: GREEN` (after_root 已同步新 spec.md).
- check_links: `python3 tools/check_links.py | tail -1` → `live docs: 42` (不升).
