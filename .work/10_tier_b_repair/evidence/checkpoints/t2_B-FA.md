# T2 B-FA writer checkpoint

## attempt 1

> 状态: writer 完成, 待 reviewer (未 commit). writer = oh-my-claudecode:executor (opus), 2026-11-26.
> base HEAD `4f8bde87767ddcb26f5b49dc14c6ea048b06a4cf` (B-ch02 已提交; B-model01 已提交, model/02 md5 与 B-model01 checkpoint 记录一致 `15682cb0…`).

## md5
| file | base | after |
|---|---|---|
| domains/FA/assumptions.md | 074c5af033b5380230e8b5409f4c3066 | 99f5b2377c38a486a3d58be8de9cd5a0 |
| domains/FA/examples.md | 818e7b88e34ac394ab01d0895e21c2b6 | 23bbc598756018cfa41a2d4a12ed4248 |
| chapters/ch02_fundamentals.md | 4cc3de33cdbb3e103be04e31cc23cdd5 | 1c39874b259c58ba0e84630941acf7cb |
| model/02_observation_classes.md | 15682cb09de2806b06177ec25f386ffa | 2180f14252707992e232175953dd0e5d |

`git diff --stat` (仅本批 4 文件): ch02 0+/33-; FA/assumptions 89 行变动; FA/examples 41 行变动; model/02 0+/18-; 合计 86 insertions, 95 deletions.

## 范围决定 (主控须确认 #1-#2)
1. **RELOCATE 源侧整块删除 (超出字面 `delete_only_source_lines`)**: 只删 anchor 两行会让 ch02 列表 2/3 的子项成孤儿、model/02 留无头 §6.4.3 残段 (违规则 5). 按 B-FA.json notes 第 4 条 ("源侧文字不受其所在 PDF 节支持则删, 不留指针"):
   - ch02:187-219 (base 行号; 空行 + `## Findings About — Naming Findings About Domains (Reference Material)` 整节: KB 自写引导句 + §6.4.2 全文 + §6.4.1 Points to Consider 首条) 删除. 逐句核: 0 句在 ig34 p7-16, 全部已在 FA/assumptions.md 新文本中 (KB 自写引导句 + 节标题除外).
   - model/02:206-223 (`### §6.4.3 Variables Unique to Findings About (Reference Material, SDTMIG v3.4 p364)` 整块 + 尾空行) 删除. 逐句核: 0 句在 sv20 任何页 (表格单格 SEV/TOXGR 偶合除外); 全部已在 FA §6.4.3. **保留** model/02 `### Findings About (Subtype)` (:198-204, sv20 p32 §3.1.3.1 支持).
   - 两文件各 1 个连续删除 hunk, 0 插入. 全仓 (除 archive/releases) grep 两标题 0 引用, 不断链.
2. **FA §6.4 / §6.4.1 整节按 p361-363 逐字重建** (atoms 未列: `pdf_ranges` 从 364 起, p361-363 的 28 个原子 (p361 a010-a018 / p362 a001-a010 / p363 a001-a009) fp 无记录, T1 从未分诊). 原 KB :17-60 多处与 PDF 矛盾 (例: :31 "maximum severity of headache" vs PDF "number of episodes of vomiting"; :49 FAOBJ 结尾改义; Criterion 2 标题被改; Criterion 3 正文缺; Points to Consider 4 条被改写), 无行承载 fp 记账原子 → 旧改写全删 (D2), 原文逐字补. **改写率 >50% → 规则 A 抽检须覆盖本节.**
3. **PDF_TYPO 取舍**: 拼写/标点类且 PDF 自身可定 (T-1 引号字形, T-2 "6.4.4.," ×5, T-5 "e.g,") → KB 写正确值; 语法类 (T-3/T-4/T-6/T-8) 与跨表矛盾 (T-7/T-9/T-10) → 照录 + T4. 主控可改判.

## 变更清单
| # | kb_file:line (改后) | ref | action | before → after 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 1 | FA/assumptions.md:17-19 | ig34_p0361_a010/a011 (新增) | INSERTED | 新增 `## §6.4 Findings About Events or Interventions` + 引言 1 句 | 361 |
| 2 | FA/assumptions.md:21-65 | ig34_p0361_a012..p0363_a009 (新增 26; 连 #1 共 28) | REPLACED | §6.4.1 旧改写 (:19-60 base) → PDF 逐字 (Criterion 1-3, 两段 Previous versions, symptom 段, Points to Consider 4 条+子条) | 361-363 |
| 3 | FA/assumptions.md:67-89 | ig34_p0363_a014, ig34_p0364_a003 (+a011..a019, p0364_a001..a009) | MOVED | §6.4.2 空标题下补 PDF 全文 (1/2/3 → o → ▪ 嵌套; 弯引号 “FA” 照 PDF) ; 源 ch02 删 | 363-364 |
| 4 | FA/assumptions.md:91-107 | ig34_p0364_a011 (+a012..a019) | MOVED | §6.4.3 空标题下补 PDF 全文 + FATESTCD/FATEST 3 行表; 源 model/02 删 | 364 |
| 5 | FA/assumptions.md:111 | ig34_p0364_a022 (新增) | REPLACED | Description 截断 "...events or interventions record." → "...domain record or as a supplemental qualifier." | 364 |
| 6 | ch02_fundamentals.md:187-219 (base) | RELOCATE 源 | MOVED (删源) | 见范围决定 1 | — |
| 7 | model/02_observation_classes.md:206-223 (base) | RELOCATE 源 | MOVED (删源) | 见范围决定 1 | — |
| 8 | FA/examples.md:30 | 新增 (ig34_p0368 ex 叙述) | REPLACED | "The time the migraine medication" → "The time migraine medication" (KB 多加 the) | 368 |
| 9 | FA/examples.md:97 | 新增 (顺序) | MOVED | Ex2 "Additional data about the rash…" 段从 ae.xpt 前移到 ae.xpt 后 (PDF 顺序) | 370 |
| 10 | FA/examples.md:105 | ig34_p0370_a009 / census:FA/examples.md:105:3:FATESTCD | REPLACED | FAPRNG → PAPRNG | 370 |
| 11 | FA/examples.md:112 | ig34_p0370_a016 / census:…:112:10:FATESTCD | REPLACED | FAPRNG → PAPRNG | 370 |
| 12 | FA/examples.md:155 | ig34_p0371_a018 / census:…:155:1:MHEVLINT | REPLACED | MHEVLINT -P6M → 空 (渲染核) | 371 |
| 13 | FA/examples.md:156-160 | census:…:156-160:2-6:MHSCAT | REPLACED | MHSCAT "SYMPTOMS" → "RHEUMATOID ARTHRITIS SYMPTOMS" ×5 | 371 |
| 14 | FA/examples.md:160 | census:…:160:6:MHOCCUR | REPLACED | MHOCCUR 空 → Y | 371 |
| 15 | FA/examples.md:205-206 | 新增 (顺序) | MOVED | Ex4 Row 1/Row 2 注释从 ae.xpt 后移到 ae.xpt 前 (PDF p372→p373 顺序) | 372-373 |
| 16 | FA/examples.md:226 | ig34_p0373_a012 | INSERTED | 补 "In this study, GERD symptoms were considered clinical events." (句中原位); ("about") → (“about”) 弯引号照 PDF | 373 |
| 17 | FA/examples.md:243 | ig34_p0373_a024 / census:…:244:3:FATESTCD | REPLACED | NUMEPISO → NUMEPISD | 373 |
| 18 | FA/examples.md:246,249,253 | census:…:247/250/254 | REPLACED | NUMEPISO → NUMEPISD ×3 | 373-374 |
| 19 | FA/examples.md:283 | KB_AUTHORED (D6) | REPLACED | 斜体 "*Note: The FA Example 6 CRF shows…*" → 前缀 `> KB note (not in SDTMIG):` (不矛盾, 保留) | — |

atoms 覆盖: 8/8 (ig34_p0373_a012 #16; p0363_a014 #3; p0364_a003 #3; p0370_a009 #10; p0370_a016 #11; p0371_a018 #12; p0373_a024 #17; p0364_a011 #4). t2_recheck 4 条 (p0367_a013/a016/a019, p0374_a011) **未改**, 待 reviewer.

## census 处理
- DIFF :101 faae.xpt (Ex2) 2 格 → #10/#11.
- DIFF :153 mh.xpt (Ex3) 7 格 → #12/#13/#14 (渲染 p371 逐格核: row1 MHSCAT 空、MHEVLINT 空; row2-6 MHSCAT 全称; row6 MHOCCUR Y, MHSEV 空).
- DIFF :240 face.xpt (Ex5) 4 格 → #17/#18 (渲染 p373-374; 其余格含 FASTRESN 250/2/1/1 一致).
- pdf_only / pdf_unparsed: 无.
- unparseable KB 表 9 张: **均未改动** (Ex1 CRF :7 / Ex2 CRF :76 / Ex3 CRF :133,:138 / Ex4 CRF :176 / Ex5 CRF :220 / Ex6 CRF :264,:274,:280). 对 layout+渲染人工核: 内容一致; 唯 :14/:17/:20 (症状 4 行合并) 与 :264 (表头 6 列/数据 9 列) 为 t2_recheck, 留 reviewer. 下划线空格长度 (Ex2 `_________` 9 vs PDF 8; Ex3 `___` vs PDF `_____`) 未动, 视为填空线非文本.

## 新增 atom 清单 (不在 atoms[], R3/全扫纳入)
ig34_p0361_a010..a018 (9), p0362_a001..a010 (10), p0363_a001..a009 (9) = 28 (§6.4/§6.4.1 全部; trace 行写 "38" 有误, 以此为准); p0364_a022 (Description 截断); Ex1 :30 词插入; Ex2 / Ex4 段落顺序.

## 删除清单 (reviewer 逐条确认)
| # | file:line (base) | 原因 | 保留位置 |
|---|---|---|---|
| D-1 | FA/assumptions.md:19-60 | §6.4.1 旧改写/与 PDF 矛盾 (D2), 由 PDF 原文取代 | FA/assumptions.md:21-65 |
| D-2 | FA/assumptions.md:68 旧 Description 截断句 | 被完整原文替换 | :111 |
| D-3 | ch02:187-219 | RELOCATE 源 (含 KB 自写引导句 :190, 节标题 :188) | FA/assumptions.md §6.4.1 Points to Consider / §6.4.2 |
| D-4 | model/02:206-223 | RELOCATE 源 (含 KB 自写节标题) | FA/assumptions.md §6.4.3 |
| D-5 | FA/examples.md:30 "the" | 词插入改写, 恢复 PDF 原词 | — |
| D-6 | FA/examples.md:91 (base) Ex2 "Additional data…" 段 | 顺序移动 (删+原文插入 ae.xpt 后) | :97 |
| D-7 | FA/examples.md:212-214 (base) Ex4 Row 1/Row 2 注释 | 顺序移动到 ae.xpt 前 | :205-206 |

## PDF_TYPO 清单 (按 dispatch 取舍规则: 拼写/标点且 PDF 自身可定 → KB 写正确值; 语法/跨表矛盾 → 照录 + T4)
| T | 位置 | PDF 原样 | KB | 依据 |
|---|---|---|---|---|
| T-1 | p361 §6.4.1 首段 → FA/assumptions.md:23 | ”findings about” (两个右引号) | “findings about” | 引号字形错, 改正 |
| T-2 | p361×2, p362×3 → :29,:31,:37,:45,:49 | "Section 6.4.4.," | "Section 6.4.4," | 多余句点; PDF 同节 "Section 6.4.1," 等均无; 改正 |
| T-3 | p361 Occasionally 段 → :33 | "These type of assessments" | 照录 | 语法, T4 |
| T-4 | p362 Previous versions 段 → :53 | "thought be related" (渲染确认) | 照录 | 漏词 (语法), T4; pdf_atoms p0362_a010 抽成 "thought to be" = 原子抽错 |
| T-5 | p363 PtC 第 3 条 → :64 | "(e.g, When?, …)" | "(e.g., When?, …)" | 标点; PDF 他处均 "e.g.,"; 改正 |
| T-6 | p363 PtC 第 4 条 → :65 | "FA may provided" | 照录 | 语法, T4 |
| T-7 | p370 Ex2 → examples.md:117 | "linked to the parent CE record" (父实为 AE) | 照录 (原已如此) | 跨表矛盾, T4 |
| T-8 | p372 Ex4 → examples.md:183 | "used to populated FADTC" | 照录 (原已如此) | 语法, T4 |
| T-9 | p373 Ex5 | 叙述 "FAEVINTX" vs 表列 FAEVLINT | 两处照录 | 跨表矛盾, T4; pdf_atoms p0373_a021 表头抽成 FAEVINTX = 原子抽错 (渲染为 FAEVLINT) |
| T-10 | p375 Ex6 relrec | STUDYID ABC vs ae/faae XYZ | 照录 (原已如此) | 跨表矛盾, T4 |
| — | p370 PAPRNG / p373-374 NUMEPISD | 非笔误: PDF 2/4 处一致, KB 无 CT 反证 → VALUE_DIFF 改成 PDF 值 | | |

## fp 变化 (实测)
命令 (repo 根; S=scratchpad/t2_B-FA_writer; basekb = 当前 KB 拷贝 + 本批 4 文件换回 base 版本):
`python3 -I .work/10_tier_b_repair/scripts/fp_match.py --kb-root $S/basekb --out $S/fp_before.jsonl` ;
`python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl` ; `python3 $S/fpdiff.py $S/fp_before.jsonl $S/fp_after.jsonl`
(注: fp_after 为 T-1/T-2/T-5 修正前跑; 这些行所在原子 p361-363 不在 fp 台账, 修正不影响下列结果.)
- **hit_target 丢失 24 (全部为 target 迁移, 非内容丢失)**: ig34_p0363_a011-a013, a015-a019, p0364_a001-a009 (原 target ch02) 与 p0364_a011-a013, a017-a019 (原 target model/02); 现 hit_any 全为 FA/assumptions.md (a013 表头命中 FA/examples.md). 实查 targets: p0363_a011 = [ch02, ch04], p0364_a012 = [model/02] — **不含 FA/assumptions.md → 须主控更新台账 targets**, 否则 fp --baseline 会报这 24 条回归.
- p0363_a014 仍 hit_target (targets 含 FA). p0364_a014-a016 (FATESTCD 表行) 前后不变.
- 新增 hit_target 13: p0368_a005, p0370_a009/a016, p0371_a019-a023, p0373_a012/a024/a027, p0374_a001/a005.
- PDF_TYPO 修正 (T-1/T-2/T-5) 致 fp 回归: 当前台账 **0** (p361-363 原子未入台账); 若日后入账, 预期非 EXACT: p0361_a016/a017, p0362_a002/a006/a008 (6.4.4.,), p0363_a008 (e.g,), p0361_a013 (引号字形, 归一化后应无影响).
- 原子抽错致永久非 EXACT: p0361_a016 (原子漏 "so"), p0362_a010 (原子多 "to"), p0373_a021 (表头 FAEVINTX).

## 范围外发现
- OOS-1 FA/spec.md (p365-366, 非白名单): 未核; 本批 PDF→KB 扫描显示 spec 行在 spec.md 为不同版式, 建议 B-spec 类批次处理.
- OOS-2 FA/assumptions.md:113 `## §6.4.5 Skin Response (SR)` 空标题 + p375 SR Description 句 → 属 B-SR.
- OOS-3 `pdf_ranges` 漏 p361-363 (FA §6.4/§6.4.1), 其他批是否有同类区间漏洞值得 T3 前全检.

## O10 (FA 部分)
lane B 记 "FA PAPRNG→FAPRNG, NUMEPISD→NUMEPISO" 即 KB 系统错值 → #10/#11/#17/#18 已改回 PDF 值. O10 其余 (EX/TA/CE/CP) 非本批.

## 校验 (可复跑)
- 渲染: `pdftoppm -f 361 -l 375 -r 110 -png "source/cdisc/SDTMIG v3.4 (no header footer).pdf" $S/p`; 已逐页看 p361-364, p367-375 (p365-366 为 spec, 非白名单未核).
  CRF 表 (Ex1 p367, Ex2 p369, Ex3 p371, Ex4 p372, Ex5 p373, Ex6 p374) 与数据表 (ce/ex/face p368-369, ae/faae/relrec p370, mh p371, suppmh/faae p372, ae/face p373-374, ae/faae/relrec p375) 均对渲染核过, 除本清单所列外无差异.
- KB→PDF 逐句: `python3 -I $S/scan_kb2pdf.py` — 未命中 = 标题行; :19/:41 `--OBJ`/`--OCCUR` 跨行折断 (人工核一致); T-2/T-5 修正行 (:29/:31/:37/:45/:49/:64); :283 D6 KB note.
- PDF→KB: `python3 -I $S/scan_pdf2kb.py` — 未命中 = p365-366 spec 表 (非白名单) + 标题 + SR 句 (B-SR) + T-2/T-5 所在原子 + 3 个原子抽错.
- RELOCATE 源侧核: 删前逐句对 ig34 p7-16 / sv20 全页 0 命中 (仅表格单格 SEV/TOXGR 偶合 sv20); `git diff --numstat` ch02 0/33, model/02 0/18, 各 1 hunk.
- `python3 tools/check_links.py`: live docs 45 (基线 42); 新增 3 条在他批 checkpoint (t2_B-GF*.md), 本批 4 文件 0 断链.
- `git diff --stat` (本批 4 文件): 4 files changed, 86 insertions(+), 95 deletions(-).

## attempt 1 续 (按 t2_B-FA_review.md CONDITIONAL C-1..C-3)
| # | kb_file:line | ref | action | 摘要 | PDF 页 |
|---|---|---|---|---|---|
| C-1 | FA/assumptions.md:113-115 | ig34_p0365_a001/a002 | INSERTED | 新增 `## FA – Specification` + spec 首句 (fa.xpt, … Tabulation.) 逐字 | 365 |
| C-2 | FA/examples.md:263-265 | ig34_p0374_a011 (REAL_GAP 结案) | TABLE_REBUILT | Ex6 CRF 表头/分隔行补到 9 列; 按渲染 p374: 首行 = 4 空格 + 合并格 "At each visit…", 次行 = AE ID/Adverse Event/Start Date/End Date/Visit 2-6 (原 KB 把 AE ID 等放首行、次行留空) | 374 |
| C-3a | FA/examples.md:118 | T-7 (改判 keep-correct) | REPLACED | "parent CE record" → "parent AE record" (同例 rash 记 AE, relrec RDOMAIN=AE) | 370 |
| C-3b | FA/examples.md:228 | T-9 (改判 keep-correct) | REPLACED | 叙述 "FAEVINTX indicates…previous 24 hours" → "FAEVLINT": 同例 face.xpt 列为 FAEVLINT, 值 -PT24H 为 ISO 时长 (§6.4.1 slice 用 FAEVLINT), 可由 PDF 自身确定 | 373 |
其余 3 条 recheck (p0367_a013/a016/a019) 按 reviewer 判 REWRITE_OK 不改. 顺序问题 (假设 1-6 在 §6.4 前、6.4.4 标题) 未动.

md5 after: FA/assumptions.md b56ccc20cfe93860462abe1d9ad0bd62, FA/examples.md f7178ec1da2e7fcc667598e401cc25cd; ch02 / model/02 未再改.

复跑 (S=scratchpad/t2_B-FA_writer):
- `python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after2.jsonl` ; `python3 $S/fpdiff.py $S/fp_before.jsonl $S/fp_after2.jsonl`
  hit_target 丢失 30 = 本批 27 + 他批并行改动 3 (p0174_a0012 MH, p0262_a029/a030 MS, p0396_a009 TA — base 拷贝时点早于这些批, 与本批无关).
  本批 27 = 23 条 target 迁移 (→FA/assumptions.md) + p0364_a013 表头 (INTENTIONAL_EXCLUDE, 现在 FA/examples.md 也命中) + **3 条 PDF_TYPO 改正预期**: p0370_a021 (T-7), p0373_a013 (T-9), p0374_a011 (C-2).
  p0374_a011 说明: 原子把 "AE ID…End Date" 与合并格抽在同一行 (`| AE ID | … | At each visit… | | | | |`), 渲染 p374 显示 AE ID 等与 Visit 2-6 同行 → 原子结构抽错; KB 按渲染. 若 reviewer 坚持按原子形状, 改 2 行即可.
  新增 hit_target 85 (含他批).
- `python3 -I .work/10_tier_b_repair/scripts/table_census.py --pages ig34:367-375 --kb knowledge_base/domains/FA/examples.md --out $S/census_after.json` → OK 15 / UNPARSEABLE 9 / PDF_ONLY 0 / diffs 0, GREEN.
- `python3 tools/check_links.py` → live docs 42 (= 基线).
