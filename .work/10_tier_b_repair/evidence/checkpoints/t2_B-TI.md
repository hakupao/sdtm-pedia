# T2 B-TI writer checkpoint

## attempt 1 (2026-11-26T05:06:32Z, oh-my-claudecode:executor / opus)

- base HEAD: `beaefa9cbea4bdd86deffb7091650174ca411c83` (TI 文件改前工作树 clean; 基线 = `git show HEAD:<file>`)
- md5: TI/assumptions.md `5dc6dd0a7b16c5ad40e33c72196a973b` → `c0ed079fe45939eeba5ed6a1af1bfdd7` (47 → 57 行); TI/examples.md `9ee76513092a9daa2511830efc4c0441` (未改)
- 白名单: examples.md (batch json) + assumptions.md (主控授权: Description/Overview、spec 首句、节标题与 Description 之间的引言段, 逐字, CM/TS 先例结构)
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-TI_writer/` (assumptions.before.md, examples.before.md, p-416/p-417 渲染 110dpi, manifest.json (lo 416 hi 417), census_before/after.json, scan.py, fp_after.jsonl, fp_regress.jsonl)
- 本批 atoms 1 (REAL_GAP) / t2_recheck 0 / census DIFF 0 / pdf_only 0 / unparseable 0 / out_of_scope 0.
- **节页范围核 (O20)**: §7.4 引言 = p415 末 (KB 承载于 TI/assumptions.md 顶部); §7.4.1 TI = p416 (节标题 + "TI – Proposed Removal of Variable TIRL" + Description/Overview + Specification 首句 + spec 表 + Assumptions 1-3) → p417 上半 (Assumptions 4-5 + Examples Ex1 ti.xpt; p417 中部起 §7.4.2 TS, 已由 B-TS 提交, 未碰). batch pdf_ranges 418-419 **偏移**, 实际 **p416-417** (+ p415 末 §7.4 引言); TI/assumptions.md 尾部另含 §7.5 (p425-426), 一并反向扫描.
- **p417 "PDF_ONLY ti.xpt" 核**: B-TS reviewer 所见 pdf_only 是其 manifest 只含 TS 文件 (417-425) 所致; 全量 census manifest 对 TI 给的是 418-419 (偏移). 以 manifest lo=416 hi=417 重跑 `table_census.py`: TI/examples.md:13 ti.xpt **OK** (pdf_pages [417]), 无 pdf_only. 另对 p417 渲染图人工逐格核 (6 行 × 7 列, 表头 Row/STUDYID/DOMAIN/IETESTCD/IETEST/IECAT/TIVERS) 全一致 → **KB 不缺该表, 不补**.

### 变更清单 (行号 = 改后)

| # | kb_file:line | ref | action | before → after 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 1 | TI/assumptions.md:16-18 | ig34_p0416_a006 | INSERTED | 新增 `## TI – Description/Overview` + 首段 "A trial design domain that contains one record for each of the inclusion and exclusion criteria for the trial. This domain is not subject oriented." 逐字 | 416 |
| 2 | TI/assumptions.md:12 | R3 / 归节 (主控授权: 节标题与 Description 间引言段) | INSERTED (标题) + MOVED (同文件) | 新增 PDF 原标题 `## TI – Proposed Removal of Variable TIRL`; TIRL 段原在 `## TI – Assumptions` 下, 现移到该标题下 (内容逐字未改) | 416 |
| 3 | TI/assumptions.md:20 | 归节 (同文件 RELOCATE) | MOVED | "TI contains all the inclusion and exclusion criteria …" 段原在 Assumptions 下, 现归 Description/Overview 第 2 段 (内容逐字未改) | 416 |
| 4 | TI/assumptions.md:22-24 | spec 首句 (主控授权) | INSERTED | 新增 `## TI – Specification` + "ti.xpt, Trial Inclusion/Exclusion Criteria — Trial Design. One record per I/E criterion, Tabulation." 逐字 | 416 |
| 5 | TI/assumptions.md:26 | — | (未改) | `## TI – Assumptions` 标题文字/锚点不变, 现紧接列表 1-5 (PDF 顺序) | 416-417 |
| 6 | TI/examples.md:5 | R3 反扫 | SKIPPED_PDF_TYPO | KB "a trial with 2 versions" 保留; PDF "a trial that with" 多余 "that" → T-1 | 417 |

- 覆盖率自查: atoms 1 = #1; census DIFF 0 / pdf_only 0 (p417 ti.xpt 核 OK, 见上); 新增 atom 清单 (R3): #2 (标题), #4 (spec 首句); 同文件归节 2 (#2/#3 段落).
- 删除清单: 无 (只删了原 `## TI – Assumptions` 标题在 TIRL 段前的那一处位置, 标题本身挪到 #5 处保留; 无内容删除).

### PDF_TYPO
- T-1: p417 Ex1 引言 "a trial that with 2 versions" — "that" 多余, 正确值由句法自明; KB 保留 "a trial with" (按 "PDF 自身笔误 KB 保留正确写法" 口径). 若用户要求照录, 改回即可.

### 双向全扫 (`python3 -I /private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-TI_writer/scan.py`, 规范化引号/折行连字符/列表符号)
- PDF→KB (p415 §7.4 起 — p417 §7.4.2 前; p425 §7.5 起 — p426): 叙述 0 缺. 残余 MISS = 标题与正文粘连 (标题均在 KB) / spec 表 (属 spec.md, 范围外) / ti.xpt 表行 (census OK + 渲染逐格) / T-1.
- KB→PDF (TI/assumptions.md + examples.md 全部非表格非标题行): KB-ONLY 仅 1 = T-1 句. 无 KB 自写解释内容, 无伪节号.
- 表格原子: ti.xpt 6 行 × 7 列对渲染图逐格一致.

### 范围外发现
- F-1: TI/assumptions.md:3 标题 `## §7.4 Trial Eligibility and Summary (TI, TS) — Introduction` vs PDF "7.4 Trial Eligibility and Summary (TI and TS)"; 规则 6 不改标题, 仅登记.
- F-2: TI/assumptions.md 尾部 §7.5 (p425-426): 文字逐句一致, 但 (a) PDF 引言为 1 段, KB 拆 3 段; (b) PDF step 6 弯引号 “split”/“lump”, KB 为直引号. 不在本批授权内, 未改 (主控定是否归他批/O 项).
- F-3: TI/spec.md 未核 (不在白名单) → 归 O15 spec 扫描.
- F-4: 全量 census manifest (`work/census_full_manifest.json`) TI 文件页范围 418-419 偏移, 实为 416-417 (TM 给 417 也偏, 实为 415).

### 验证
- `python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest /private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-TI_writer/manifest.json --out /private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-TI_writer/census_after.json` → TI/examples.md:13 OK [417]
- `python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out /private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-TI_writer/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out /private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-TI_writer/fp_regress.jsonl` → RED (60 行全为他批页); `grep -E '"ig34_p041[5-7]|domains/TI/' /private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-TI_writer/fp_regress.jsonl` → 0 行; ig34_p0416_a006 hit_target = TI/assumptions.md.
- `python3 tools/check_links.py 2>&1 | grep "live docs"` → live docs: 42
- `git diff --stat -- knowledge_base/domains/TI` → assumptions.md | 12 +++++++++++- (1 file, 11+/1-); examples.md 无改动

### 需主控定
- F-2 (§7.5 分段/弯引号) 是否追加授权或归他批.

## attempt 2 (2026-11-26T05:07:24Z, 主控裁定 F-2)

| # | kb_file:line | ref | action | before → after 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 7 | TI/assumptions.md:40 | F-2 (主控授权) | REPLACED (段落切分) | §7.5 引言 3 段 → 1 段 (按 PDF p425); 文字未改, 只去掉 2 处空行 | 425 |

- "split"/"lump" 弯引号 → 归 O40, 未改; F-1 / F-4 → O48.
- md5 TI/assumptions.md → `cf4905bc8d4d2acef3b092c897ceb871` (57 → 53 行); `git diff --stat -- knowledge_base/domains/TI` → assumptions.md | 18 ++++++++++++------ (12+/6-, 相对 HEAD).
- `python3 tools/check_links.py 2>&1 | grep "live docs"` → live docs: 42.
