# T2S S-TUFA reviewer checkpoint

## attempt 1 (2026-11-26, oh-my-claudecode:code-reviewer / opus)

**Verdict: PASS** (无 CRITICAL/HIGH/MEDIUM; 6 条 LOW 观察, 不阻断)

- 对象: `git diff HEAD -- knowledge_base/domains/{TR,FA,SR}` (含 writer attempt 1 delta: TR T-5 照录, KB 未再改). TU: `git diff HEAD --stat -- knowledge_base/domains/TU` 空 (0 改动).
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/d6800696-3318-4d1d-9806-05c60470220c/scratchpad/t2s_S-TUFA_reviewer/`
  自写脚本 (未复用 writer 的): `ascan.py` (pdf_atoms 逐原子 → TR/TU/FA/SR/VS 五组 KB 归属, 自写归一), `bscan.py` (KB 行→PDF layout 逐句/逐格), `spec_bb.py` / `spec_ct.py` (`pdftotext -bbox` 按表头 x 分列, 逐变量逐字段, 去页脚), 内联 md5 / 逐字 (不归一 dash/引号) 校验; 渲染 110dpi p351/352/355-358/364/365/367/369/371-374/376-378.
- 授权范围: 本批 diff 只落 TR/assumptions, TR/spec, FA/assumptions, FA/spec, SR/spec (全部 ∈ kb_files; narrow_files 空). 4 个 examples/SR asm 未动. 工作树其他域改动属并行批, 未看.

### 命令与结果 (可复跑)
```
S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/d6800696-3318-4d1d-9806-05c60470220c/scratchpad/t2s_S-TUFA_reviewer
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json   # exit 1; KB 37 表: OK 23 / DIFF 3 / UNPARSEABLE 11; cells 3207; diffs 34 (= TR T-1 32 + TR T-2 1 + SR T-1 1)
echo '[{"file":"knowledge_base/domains/TU/examples.md","src":"ig34","lo":353,"hi":356}]' > $S/man_tu.json; python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/man_tu.json --out $S/census_tu.json   # TU 5 表全 OK, diffs 0 (§6.3.12.3 TU 份)
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl   # RED; 71 regress, 去 t2_fp_expected_regressions 后余 4 (ig34_p0079_a004/6/9/10, 他批页) → 本批页 p350-381 回归 0
python3 -I $S/spec_bb.py $S TR 350,351,352 ; python3 -I $S/spec_bb.py $S FA 365,366 ; python3 -I $S/spec_bb.py $S SR 376,377
python3 -I $S/ascan.py 350 358 TR ; python3 -I $S/ascan.py 361 375 FA ; python3 -I $S/ascan.py 375 382 SR     # PDF→KB
cd knowledge_base/domains && python3 -I $S/bscan.py k2p 350 358 TR/assumptions.md TR/examples.md   # KB→PDF (FA 361-375 / SR 375-381 同)
python3 tools/check_links.py 2>&1 | grep "live docs"   # live docs: 42
```
- census PDF_ONLY 落本批页的 6 张: p353/354×3/356 = TU 表 (在 TU/examples.md, 上面 TU census 5/5 OK); p360-361 = VS 表 (§6.3.13). 均非本批文件, 不计.

### 页范围复核 (O20)
- TR §6.3.12.2 = p350 顶 - p353 上部 (asm 8 止); §6.3.12.3 共用例 p353 中部 - p358 上部 (relrec 止; 其下 §6.3.13 VS). 同意 json 更正 350-358.
- FA: §6.4 起于 p361 中部 (上部 VS Ex 表别节), §6.4.4 标题 p364 下部, Ex6 止于 p375 上部. 全扫 361-375.
- SR §6.4.5 = p375 下部 - p381; p382 全为 §7 (原子 a001 `7 Trial Design Model Datasets`), hi=381 正确.

### 双向全扫 — 逐页 (reviewer 自己的计数: 该页原子 / 本域命中; 别节原子另列)
| 页 | PDF→KB | KB→PDF | 表 | 结论 |
|---|---|---|---|---|
| 350 | 26 / 22: 未中 a001 节号标题 (H1 结构)、a017 spec 表头、a020/a021 (原子抽取错: bbox 逐字段 USUBJID/TRSEQ Notes 与 KB 一致) | TR/asm:1-19 全有出处 (bscan 0 miss) | spec bbox | 一致 |
| 351 | 22 / 9: 未中 13 = U5 C-code 格 | spec 逐字段一致 | spec bbox (TRTESTCD 页首行已取到) | 一致 (U5 范围外) |
| 352 | 10 / 10 (含脚注 a002、A 标题 a003) | TR/asm:21-35 全有出处 | asm 4 例表渲染逐格 (下) | 一致 |
| 353 | TR 4 / 4; TU 14 在 TU (a009 aorta-iliac = TU T-1) | TR/asm:37-43 全有出处 | — | 一致 |
| 354 | TR 5 / 5; TU 30 在 TU | TR/ex:5-13 全有出处 | — | 一致 |
| 355 | 27 / 27 | 同 | tr.xpt Ex2 渲染逐行 (下) | 一致 (T-1) |
| 356 | 29 = TR 15 + TU 14, 全命中 | TR/ex:46-66 全有出处 | 渲染 | 一致 (T-3/T-4) |
| 357 | 25 / 24: a014 = T-2 | 同 | 渲染逐行 | 一致 (T-2) |
| 358 | TR 14 / 14; VS 12 别节 | TR/ex:67-110 全有出处 | 渲染 | 一致 |
| 361 | FA 9 / 7: a016/a017 = B-FA T-2 ("6.4.4.,") | FA/asm:1-17: :15/:17 = T-2 改正值 | — | 一致 |
| 362 | 10 / 6: a002/a006/a008 = T-2; a010 = 原子抽错 (layout "thought be" = KB, T-4) | :23/:31/:35 = T-2 | — | 一致 |
| 363 | 19 / 18: a008 = T-5 | :50 = T-5 改正值 | — | 一致 |
| 364 | 22 / 21: a020 `6.4.4 Findings About Events or Interventions (FA)` (见 L-1) | FA/asm:53-97 全有出处 | FATESTCD 表渲染 | 一致 |
| 365 | 22 / 16: a004 表头 + U5 5 格 | spec 逐字段一致 | `*` 2 格渲染确认 | 一致 |
| 366 | 19 / 13: U5 6 格; 脚注 a013 / A 标题 a014 / asm 1-4a (a015-a019) 命中 | FA/asm:99-112 全有出处 | — | 一致 |
| 367 | 19 / 19 (asm 5-6 a001-a003 + Ex1) | FA/asm:114-117, FA/ex:1-20 | Ex1 CRF 渲染 | 一致 |
| 368-372 | 22/22, 25/25, 25/24 (a021 = T-7), 23/23, 29/29 | 全有出处 (:118 = T-7) | census OK + CRF 渲染 | 一致 |
| 373 | 29 / 28: a013 = T-9 | :228 = T-9 | census OK + CRF 渲染 | 一致 |
| 374 | 22 / 22 | :283 D6 已标 (B-FA) | CRF ×3 渲染 | 一致 |
| 375 | FA 24/24 (含 §6.4.5 标题 → FA/asm:119 导航); SR a025/a026 在 SR/asm | FA/ex:285-322; SR/asm:1-5 | census OK | 一致 |
| 376 | 26 / 16: a004 表头, U5 7 格, a014 SROBJ = SR T-1, a010 原子抽错 (bbox: SRREFID = KB) | SR/asm:7-9; spec 逐字段 (仅 SROBJ T-1) | bbox | 一致 |
| 377 | 21 / 12: U5 6 格, a015 SRELTM = SR T-4, a016 原子抽错 (bbox 无差 = KB), a021 = SR T-3; 脚注 a018 命中 | SR/asm:11-15 (:15 = T-3) | bbox | 一致 |
| 378-381 | 21/20 (a017 T-1), 23/22 (a009 原子抽错), 35/34 (a029 原子抽错), 5/5 | SR/ex 全有出处 (表格多行折行格人工核) | census OK / DIFF(T-1) 渲染 | 一致 |
- bscan KB→PDF 表格 "miss" 全部为 PDF 折行单元格 (如 `2010-02-18` / `ACE IMAGING` / `Flare Mean Diameter`), 由 census + 渲染核过, 非缺陷.

### spec.md Controlled Terms 逐变量 (bbox 分列 + layout grep + 渲染 p365)
- **TR 32 变量** (p350-352; 顺序全同, Label/Type/Role/Core/CDISC Notes 全一致): PDF 空 = KB 空 17 (STUDYID USUBJID TRSEQ TRGRPID TRREFID TRSPID TRLNKID TRLNKGRP TRORRES TRSTRESN TRREASND TRNAM VISITNUM VISIT VISITDY TAETORD TRDY); 字面一致 1 (TRDTC ISO 8601 datetime or interval); U6 1 (DOMAIN `TR`/空); U5 13 (TRTESTCD TRTEST TRORRESU TRSTRESC TRSTRESU TRSTAT TRMETHOD TRLOBXFL TRBLFL TREVAL TREVALID TRACPTFL EPOCH). `*` 0 (layout grep 0). 17+1+1+13 = 32.
- **FA 30 变量** (p365-366; 非 CT 字段全一致): `*` 2 = KB 2 (FACAT FASCAT; p365 渲染确认); 空 15; 字面 1 (FADTC); U6 1; U5 11 (FATESTCD FATEST FAORRESU FASTRESU FASTAT FALOC FALAT FALOBXFL FABLFL FAEVAL EPOCH). 2+15+1+1+11 = 30.
- **SR 39 变量** (p376-377): 非 CT 字段仅 SROBJ Notes (SR T-1 BAU mL) / SRELTM Notes (SR T-4 EGTPTREF) 两处既有登记差异; 空 22; 字面 3 (SRDTC SRELTM SRRFTDTC); U6 1; U5 13; `*` 0. 22+3+1+13 = 39.
- TR TAETORD CDISC Notes: KB = PDF p351 逐字 ("Epoch associated with the date/time at which the assessment was made."); 与 Label 不符, FA/SR 同变量 PDF 为 "Number that gives the planned order of the element within the arm." → 同意 writer delta 登记 **TR T-5 照录 + T4**.

### gaps / footnote 逐项
| 项 | 位置 | 逐字 | 签字 |
|---|---|---|---|
| TR D (p0350_a002) | TR/asm:3 `## TR – Description/Overview` (U+2013 同 PDF) | 逐字节 | ✔ |
| TR Desc 首句拆段 (a003) | TR/asm:5 / :7 两段 (PDF 两段) | 文字不变 | ✔ |
| TR S (a015/a016) | TR/asm:17-19, Description 与 Assumptions 之间 (CM/IS 先例); `—` U+2014 同 PDF | 逐字节 | ✔ |
| TR A (p0352_a003) | TR/asm:21 | 逐字节 | ✔ |
| TR F (p0352_a002) | TR/spec.md:294, TRDY `---` 后、`## Cross References` (:296) 前 (U7) | 逐字; ¹ 写法同 S-EVT 先例 | ✔ |
| FA A (p0366_a014) | FA/asm:103 | 逐字节 | ✔ |
| FA F (p0366_a013) | FA/spec.md:276, FADY `---` 后、Cross References (:278) 前 | 逐字 | ✔ |
| SR F (p0377_a018) | SR/spec.md:357, SRRFTDTC `---` 后、Cross References (:359) 前 | 逐字 | ✔ |
- 新增 `+` 行逐字核 (不归一 dash/引号): 22 行在 p350/352/365/366/367/377 layout 中全部命中; 唯 2 行 `Controlled Terms: *` 为字段值 (bbox + 渲染核). 新增非 ASCII 仅 ¹ – — (均 PDF 原字符).
- fp_match.norm 直查: 本批 27 个 gap/移位原子 (p0350_a002-a016, p0352_a002/a003, p0366_a013-a019, p0367_a001-a003, p0377_a018) 在目标文件全部 HIT.
- intros: json 为空; FA 顶 §6.4-§6.4.3 (p361-364) 复核: 双向全扫仅 T-2/T-5 已登记改正值 + 1 原子抽错, 位置在 FA/asm H1 后、§6.4.4 前, 顺序同 PDF. ✔

### 结构改动 / 移位 / 删除 逐条签字
| # | 改动 | 依据 / 复核 | 签字 |
|---|---|---|---|
| S-1 | TR 新增 3 个 `## TR – …` 标题 | p350 a002/a015, p352 a003 | ✔ |
| S-2 / D-2 | TR 逗号句 → 冒号 + 5 项 `- ` 列表 (去 KB 自加 ", and"; 末项无句点) | p350 PDF 为 • 列表, 5 项逐字, 末项无句点 | ✔ |
| S-3 / D-1 | FA asm 1-6 (含 4a/5a) 自文件顶移到 `## FA – Specification` 首句之后 + 新 `## FA – Assumptions` | HEAD :3-15 与新 :105-117 md5 同 `0ab77983…` (逐字节); 去掉移位块+新标题后文件其余部分 diff 为空; "shares all qualities and conventions of findings observations" 全 KB 仅 1 处 (源处无残留); 顺序 = PDF p361 §6.4 → p364 Desc → p365 Spec → p366-367 Assumptions → FA – Examples | ✔ |
| D-3 | FA FACAT/FASCAT CT 空 → `*` | p365 渲染 | ✔ |
- G-TB6 结构行: 4 个新 `##` 标题; 5 个 `- ` 列表标记; 3 处 `> ¹…` 引用块前缀 (PDF 文字承载格式, 非 D6). 新增行无出处 0.
- D6: 本批无新增; 既有 FA/ex:283 KB note 与 p374-375 不矛盾 (复核). 纯导航: TR/ex:3 TU↔TR 互引 + `## Example 2/3 (continued from TU)`; FA/asm:119-121 §6.4.5 + See; spec `> Class|Structure` + Cross References (U8).

### census_items 人工逐格 (渲染 110dpi, 不采信 writer)
| # | 表 | PDF | 结果 |
|---|---|---|---|
| 1 | TR/asm.md:31-33 asm 4 例表 | p352 | 表头 8 格 + r1 8 格一致 (TOO SMALL / TO MEASURE 折行 = 1 格) |
| 2 | FA/asm.md:83-87 FATESTCD/FATEST | p364 | 表头 + OCCUR/SEV/TOXGR 3×2 一致 |
| 3 | FA/ex.md:7 Ex1 CRF | p367 | 13 行 × 2 格一致; 症状 4 项 + ○ No ○ Yes ×4 同格 (KB 并行); 粗体未保留 (格式) |
| 4 | FA/ex.md:76 Ex2 CRF | p369 | 11 行一致 (6 类 × ○ 0 … ○ >300) |
| 5 | FA/ex.md:133 Ex3 CRF 上半 | p371 | 3 行一致; PDF 表题行 `Rheumatoid Arthritis History` → KB `###` (既有, L-4) |
| 6 | FA/ex.md:138 Ex3 CRF 下半 | p371 | 表头 + 5 行 × 3 格一致 (填空线长度为版面) |
| 7 | FA/ex.md:176 Ex4 CRF | p372 | 一致; 表题行 → KB `###` (L-4); 3 症状同格 → KB 3 行 |
| 8 | FA/ex.md:219 Ex5 CRF | p373 | 2 表头行 + 3 行 × 5 列一致 (灰底未表达) |
| 9 | FA/ex.md:263 Ex6 纸质 CRF | p374 | 合并标题行 + AE ID…Visit 6 + 3 数据行 × 9 列一致 |
| 10 | FA/ex.md:273 AE 模块 | p374 | 4 列 + 空行一致 |
| 11 | FA/ex.md:279 严重度模块 | p374 | 3 列 + 1 行一致 |
| 12 | SR/ex.md:14 Ex1 sr.xpt | p378 | 8 行 × 17 列; 仅 r7 SROBJ PDF `0.15 BAU mL` / KB `BAU/mL` = SR T-1 (同表他行 BAU/mL 自证); 其余一致 |
| 13 | TR/ex.md:17 Ex2 tr.xpt | p355-356 | 27 行 × 23 列逐行一致; PDF Row 列 1-11,13-28 (跳 12) ↔ KB 1-27, TRSEQ 同 = TR T-1 (32 格); r25 TRREASND `NOT ASSESSABLE: POOR IMAGEQUALITY` 跨页 (T-3); r26 NT01 结果空 (T-4, PDF 忠实) |
| 14 | TR/ex.md:68 Ex3 tr.xpt | p356-358 | 32 行 × 23 列逐行一致; 仅 r15 TRSTRESC PDF `-60` / KB `-50` = TR T-2 (同行 TRORRES/TRSTRESN -50 自证) |
- census 全 37 表: DIFF 3 张 (#12/#13/#14) 差异全为已登记 T-n; UNPARSEABLE 11 张 = #1-#11 全部人工逐格一致.

### 问题表 (全部 LOW, 不阻断)
| ref | 检查项 | 问题 | 建议 |
|---|---|---|---|
| L-1 FA/asm.md:95 | 标题 | `## §6.4.4 FA – Description/Overview` 合并了 PDF `6.4.4 Findings About Events or Interventions (FA)` 与 `FA – Description/Overview` 两级; p364 a020 文字未单独承载 | 主控已裁 (规则 6 不改), 仅记录 |
| L-2 TR/asm.md:27 | 段落 | asm 3 PDF 段内另起段 "The sponsor should not derive…", KB 并为一段 | S-FND 口径 (仅段落拆合) 不改 |
| L-3 TR/asm.md:29 | 排版 | PDF `“too small to measure."` 开引号弯; KB 直引号 (既有文字) | 归 S-TYPO (U1) |
| L-4 FA/ex.md:131/174 | 表题 | Ex3/Ex4 CRF 的 PDF 表题行在 KB 为 `###` 标题 + 表 (Ex3 拆 2 表); 文字无丢 | 既有 (B-FA review 已核), 不改 |
| L-5 S-TUFA.writer.jsonl | 台账枚举 | `VERIFIED` / `MOVED` 非 v1.0 枚举 (同 S-EVT L-3) | 可接受 |
| L-6 TR/spec.md:264 | PDF_TYPO | TAETORD Notes 与 Label 不符 | 已登记 TR T-5 (T4 用户裁), 同意 |

### R2 recheck
- json 无 `t2_recheck[]`. 全扫: TR 列表并句 (R2) 已由 writer 恢复; 未发现其他改写丢短语项. 新增 REAL_GAP 0.

### 总结
- G-TB4: census 37 表 = OK 23 + DIFF 3 (34 格, 全为 TR T-1/T-2、SR T-1) + UNPARSEABLE 11 (人工逐格一致); TU 共用例 5 表 OK.
- G-TB6: 新增 41+/17- 行 (5 文件) 全有 PDF 出处或为签字结构行; 无出处 0. FA 移位块逐字节不变、源处无残留.
- spec CT: TR 32 / FA 30 / SR 39 变量逐个列明; `*` PDF 2 = KB 2; U5 37 / U6 3 归 S-CT.
- fp 本批页回归 0; check_links live docs 42.
