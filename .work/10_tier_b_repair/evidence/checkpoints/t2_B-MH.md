# T2 B-MH writer checkpoint

## attempt 1 (2026-11-26, oh-my-claudecode:executor / opus)

- base HEAD: `259cd49f298064afb9e1ad3735f2e7827643f8bd`
- md5 MH/assumptions.md: before `3f8131f365d4a04da606a564f44d3982` (49 行) → after `d693e9d9f52459d2898d543919af54f1` (55 行, +6 = Description/Overview 标题 + Specification 标题 + spec 首句 + 空行)
- md5 MH/examples.md: before `c979bbc0e02e3376faf65909f119143d` → after `d7642d4811cca46e92979906328848a2` (109 行不变)
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/7fe38595-6d99-4b86-881d-0dfb0d270167/scratchpad/t2_B-MH_writer/`
  (assumptions/examples.before.md, before_root/ = 改前 KB 镜像, apply.py = 精确替换 + 命中次数断言 + 表列数断言, prose_scan.py, census_before/after.json, fp_before/after.jsonl, fp_mh.py, p-171..178.png 110dpi 渲染)
- 页范围: `pdf_ranges` lo=171 已覆盖 §6.2.6 起始页 (p171 标题 / Description / Specification 首句), O20 无缺口; 实扫 p171-178 (p171 前半为 HO, p178 下半为 DV, 均非本批).
- 本批 atoms 0 / t2_recheck 0 / out_of_scope 0; census DIFF 5 表 (24 diffs) 全处理; pdf_only 0; unparseable 1 (assumptions 4d 表, 已触碰, 见下).
- 数据来源: 所有表格改动格对照渲染图 p175-178 逐格; 叙述对照 `work/pdf_pages/ig34_p0171-0178.txt` + 渲染图.

### 变更清单 (行号 = 改后)

| # | kb_file:line | ref | action | before → after 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 1 | MH/assumptions.md:5 | R3 N-1 (ig34_p0171_a0009 HEADING) | INSERTED | 在 `## 6.2.6 Medical History (MH)` 下补 `## MH – Description/Overview` (原 6.2.6 标题保留, 不动锚点) | 171 |
| 2 | :9-11 | R3 N-2/N-3 (ig34_p0171_a0011 HEADING + a0012 spec 首句) | INSERTED | `## MH – Specification` + "mh.xpt, Medical History — Events. One record per medical history event per subject, Tabulation." (CM/AE 先例位置) | 171 |
| 3 | :19 | R3 N-4 (ig34_p0172_a0018) | INSERTED | 2b 补漏句 "The modified term is listed in MHMODIFY." | 172 |
| 4 | :21 | KB 扩写 (2d) | REPLACED (D2 删扩写, 删除清单 D-1) | 删 "It is expected that this variable will be populated." — PDF p173 2d 无此句; 来自 AE assumption (p138), 跨域串入; 规范性语句, 非解释性 → 不适用 D6 | 173 |
| 5 | :26 | R3 N-5 (ig34_p0173_a0006) | REPLACED | 3a.i "Medical Medical History" → "Medical History" | 173 |
| 6 | :31 | R3 N-6 (ig34_p0173_a0010) | INSERTED | 4a 补 ", respectively" | 173 |
| 7 | :36 | R3 N-7 (ig34_p0174_a0001 TABLE_HEADER; unparseable 表) | REPLACED | 4d 表头 MHPRESP/MHOCCUR/MHSTAT → "Value of MHPRESP / Value of MHOCCUR / Value of MHSTAT"; 4 数据行对渲染图逐格一致, 未动 | 174 |
| 8 | :51 | ig34_p0174_a0012 (6b) | REPLACED (PDF_TYPO T-1) | 第二处 MHENDTYP → MHEVDTYP | 174 |
| 9 | :53 | KB 自写注 | REPLACED (D6) | `> **Note:**` → `> KB note (not in SDTMIG):`, 正文保留 (中文, 见主控决定项) | — |
| 10 | MH/examples.md:7 | R3 N-8 (ig34_p0175_a0004) | REPLACED (D2 删改写, D-2) | Ex1 Rows 1-3: "MHSCAT displays the body systems specified on the CRF" → PDF "MHSCAT indicates the body system for which the event was collected"; "Ongoing at Study Start" → "Ongoing" (旧词来自 Ex2 叙述) | 175 |
| 11 | :9 | R3 N-9 (ig34_p0175_a0005) | REPLACED (D2 删串入句, D-3) | Ex1 Rows 4-5: 删 KB 串入句 "MHSTDTC was populated with the date and time at which the event occurred." (属 Ex2 Row 4); "start dates with" → "start dates of" | 175 |
| 12 | :13-14 | census:13 HEADER (MHEVDTYP) | TABLE_REBUILT | 表头 MHDECOD 后加 MHEVDTYP 列 (PDF 列序); 分隔线同步 | 175 |
| 13 | :15-17 | census:13 r1-r3 MHSTDTC/MHENTPT (×6) | REPLACED | 2004-09-18 从 MHSTDTC 移到 MHENTPT (MHSTDTC 空) | 175 |
| 14 | :18-19 | census:13 r4/r5 MHEVDTYP (×2) | REPLACED | 新列值 SYMPTOM ONSET / DIAGNOSIS; r1-r3 MHEVDTYP 空 | 175 |
| 15 | :31 | R3 N-10 (ig34_p0176_a0001) | INSERTED | Ex2 Rows 1-3 句尾补 "on using --STRF and --ENRF" | 176 |
| 16 | :39-40 | census:39 HEADER (MHBODSYS 位置) | TABLE_REBUILT | 列序改为 PDF: MHSCAT, MHPRESP, MHOCCUR, MHBODSYS; 分隔线同步 | 176 |
| 17 | :41-48 | census:39 r1-r3 MHBODSYS (×6) + r4-r8 随列序同步 | TABLE_REBUILT | 8 行全部按新列序重排 (值按列名不变; r5-r8 的 Y/Y、Y/N 仍在 MHPRESP/MHOCCUR, census 未列但已对渲染图核) | 176 |
| 18 | :65 | census:60 r4 MHREASND/VISITNUM (×2) | REPLACED | "1" 从 MHREASND 移回 VISITNUM | 177 |
| 19 | :69 | census:60 r8 MHOCCUR | REPLACED | N → Y | 177 |
| 20 | :85 | census:83 r1 MHOCCUR | REPLACED | 空 → Y | 177 |
| 21 | :88 | census:83 r4 MHOCCUR | REPLACED | 空 → Y | 177 |
| 22 | :106 | census:104 r1 MHDTC | SKIPPED_PDF_TYPO (T-2) | KB 2019-11-02 保留; PDF 印 "2019-011-02" | 178 |
| 23 | :109 | census:104 r4 MHENRTPT/MHENTPT (×2) | REPLACED | BEFORE / 2019-12-08 → 空 / 空 (PDF r4 两格空; KB 疑从 r3 复制) | 178 |

- atoms 覆盖率自查: atoms 0 → 无 atom 行. census 24 diff 全在 #12-14/#16-23 (writer.jsonl 38 行 = 24 census + 14 项 R3/D2/D6/PDF_TYPO).

### census 表处理

| census ref (before 行号) | 处理 | 结果 (after) |
|---|---|---|
| examples:13 Ex1 (9 = HEADER 1 + CELL 8) | #12-14 | OK |
| examples:39 Ex2 (7 = HEADER 1 + CELL 6) | #16-17 | OK |
| examples:60 Ex3 (3) | #18-19 | OK |
| examples:83 Ex4 (2) | #20-21 | OK |
| examples:104 Ex5 (3) | #22 T-2 / #23 | DIFF 1 残留 (T-2, 预期) |
| assumptions:30 (现 :36) 4d 表 UNPARSEABLE | #7 表头; 数据行人工逐格对 p174 渲染 | 不可机检 → reviewer 须人工逐格 |

- 汇总: before `DIFF 5 / UNPARSEABLE 1, cells 444, diffs 24` → after `OK 4 / DIFF 1 / UNPARSEABLE 1, cells 449, diffs 1` (= T-2). RESULT RED 来自 manifest 外 PDF_ONLY 334 张, 改前改后相同.

```
S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/7fe38595-6d99-4b86-881d-0dfb0d270167/scratchpad/t2_B-MH_writer
python3 -I -c "import json;J=json.load(open('.work/10_tier_b_repair/work/t2_batches/B-MH.json'));json.dump([{k:r[k] for k in ('file','src','lo','hi')} for r in J['pdf_ranges']],open('$S/manifest.json','w'))"
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json     # before: 改前跑 (或 --kb-root $S/before_root/knowledge_base)
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl                                          # before: fp_before.jsonl 改前跑
python3 -I $S/fp_mh.py $S/fp_after.jsonl
python3 -I $S/prose_scan.py ; python3 -I $S/prose_scan.py $S/before_root/knowledge_base
python3 tools/check_links.py | tail -1    # live docs: 42 (基线 42)
```

### fp_match (改前 vs 改后, 全量)
- hit_target 3803 → 3820. 新命中 18: p0171_a0012, p0172_a0018, p0173_a0006, p0173_a0010, p0174_a0001, p0175_a0004/a0005/a0007-a0012, p0176_a0001/a0005, p0177_a0006/a0015/a0018.
- **回归 1 (预期, PDF_TYPO 修正引起)**: ig34_p0174_a0012 (6b, 原子按 PDF 含 "MHENDTYP"; KB 改为 MHEVDTYP, T-1).
- MH 改后仍未命中: p0171_a0013-p0172_a0013 (spec 表行/脚注, 属 spec.md, 不在本批白名单, ledger 多为 INTENTIONAL_EXCLUDE); p0173_a0007 (T-3 引号内多余空格, 预期); p0178_a0005 (Ex5 r1 "2019-011-02", T-2, 预期).
- **预期 fp 回归清单**: p0174_a0012 (T-1); 持续不命中 p0173_a0007 (T-3)、p0178_a0005 (T-2).

### 双向全扫 (含表格原子; p171 §6.2.6 起 至 p178 §6.2.7 前)
- PDF→KB (pdf_atoms 非表格原子, 归一后子串): 改前 12 未命中 → 改后 4: p0172_a0013 (spec 脚注, 属 spec.md), p0173_a0007 (T-3), p0174_a0012 (T-1), p0175_a0001 HEADING "MH – Examples" (KB 文件 H1 `# MH — Examples` 为结构标题, 不改锚点).
- KB→PDF (KB 逐句在 layout 文本归一后子串): 改前 10 → 改后 5: assumptions :27 (T-3), :51 (T-1), :53 ×2 (D6 KB note), :55 (item 7 — 仅 layout 文本 "--\nSMIE" 跨行致脚本误报, 对渲染图一致).
- 表格原子: assumptions 4d 表 + examples 5 张 mh.xpt 全部对 110dpi 渲染图逐格人工核, 表头 / 列序 / 列数 / Row 列与 PDF 一致 (除 T-2). `**mh.xpt**` / `## Example N` 对应 PDF.
- 已核非问题 (仅格式, 同 B-EG/B-OE 口径未改): PDF 弯引号/弯撇号 (sponsor’s, “Ongoing”, “no medical history”), 7. 中 "‑‑SDTH" 非断字连字符, PDF 普通文本的 "2. MH description and coding" 等在 KB 加粗 (Markdown 语法).
- KB_AUTHORED / D6: :53 中文注 (D6 标注, 见主控决定项); 无其他 KB 自写解释内容. 标题 `# MH — Assumptions` / `# MH — Examples` 为纯导航.

### 新增 atom 清单 (R3)
- N-1 ig34_p0171_a0009, N-2 p0171_a0011, N-3 p0171_a0012, N-4 p0172_a0018, N-5 p0173_a0006, N-6 p0173_a0010, N-7 p0174_a0001, N-8 p0175_a0004, N-9 p0175_a0005, N-10 p0176_a0001.

### 删除清单 (reviewer 逐条确认)

| # | 原位置 (base 行号) | 改后 | 原因 | 保留副本 |
|---|---|---|---|---|
| D-1 | assumptions:15 句尾 "It is expected that this variable will be populated." | :21 删 | D2 删扩写: PDF p173 2d 无; 原文属 AE assumption 2d (p138), 跨域串入; v3.4 MHBODSYS 为 Perm, 规范性语句不能按 D6 保留 | AE/assumptions.md:19 (AE 本有) |
| D-2 | examples:7 "MHSCAT displays the body systems specified on the CRF" / "Ongoing at Study Start" | :7 PDF 原文 | R2 改写 (实为 Ex2 叙述串入); 该行只承载 p0175_a0004 (改前未命中) → 换 PDF 原文 | Ex2 :31 (PDF Ex2 原有) |
| D-3 | examples:9 "MHSTDTC was populated with the date and time at which the event occurred." + "with MHEVDTYP" | :9 删句 + "of" | KB 串入句 (PDF Ex2 Row 4 原句), 与 Ex1 (日期为症状起始/诊断日期) 不符 → D2 删; 该行只承载 p0175_a0005 | Ex2 :33 (PDF Ex2 原有) |
| D-4 | assumptions:20, :47 (`**Note:**` 前缀), examples 表格旧值 | 同行 | VALUE_DIFF / 表头跟 PDF 的旧值替换 (#5, #7-9, #12-23) | — |

### PDF_TYPO 清单

| T | 位置 | PDF | KB | 依据 / 处理 |
|---|---|---|---|---|
| T-1 | assumptions:51 (6b) | "…date of diagnosis and MHENDTYP = "DIAGNOSIS"" | MHEVDTYP | 正确值由 PDF 自身确定: 同句前半 "MHEVDTYP = "SYMPTOMS""、6a 定义、spec p171 MHEVDTYP 行, MHENDTYP 非 spec 变量 → KB 写正确值并登记. fp 回归 p0174_a0012 预期 |
| T-2 | examples:106 Ex5 r1 MHDTC | 2019-011-02 | 2019-11-02 (未改) | 非法 ISO 8601; "011" 可读作 11 或 01, PDF 自身不能唯一确定 → **T4 用户裁定项**. 注意: 补充口径对"不能确定"者要求"照录 PDF", 本处按 writer 规则 2 保留 KB 合理值 (未写入非法日期), 请主控二选一 |
| T-3 | assumptions:27 (3a.ii) | “Allergy Medical History, “ (逗号后多空格且引号方向错) | "Allergy Medical History," | 印刷标点错, KB 保留规范写法; p0173_a0007 持续不命中, 预期 |

### 需要主控决定
- **M-1 :53 中文 KB note**: 英文 KB 中的中文注 (原 `**Note:**`, 已按 D6 改前缀, 正文未动). 6b 已改正为 MHEVDTYP 后该注仍准确 (说明 PDF 原印 MHENDTYP). 选项: 保留 / 改译为英文 / 删除 — 未擅自改写.
- **M-2 T-2** (见上): 保留 KB 2019-11-02 还是照录 PDF 2019-011-02.

### 范围外发现 (主控决定)
- **O-MH-1 `knowledge_base/domains/MH/spec.md`**: p171-172 spec 表行 (p0171_a0013-p0172_a0012) 与脚注 (p0172_a0013) fp 未命中, 属 spec.md, 不在本批白名单, 未查未动.

### 触碰过的 unparseable 表
- **MH/assumptions.md:36** (base :30) 4d Situation 表: 改表头 3 格 (加 "Value of"); 4 数据行对 p174 渲染图逐格一致未动. census 不可机检 → reviewer 须对渲染图人工逐格.

### git diff --stat
```
 knowledge_base/domains/MH/assumptions.md | 20 ++++++++-----
 knowledge_base/domains/MH/examples.md    | 48 ++++++++++++++++----------------
 2 files changed, 37 insertions(+), 31 deletions(-)
```
- 只改本批 2 文件; 工作树其他 M/?? 为他批既有改动, 未触碰. 未 commit. check_links live docs 42 (基线 42).

## attempt 1 续 (主控裁定 M-1 / M-2, 2026-11-26)

- **M-1**: assumptions.md:53 的中文 KB note 已译成英文，仍放在 `> KB note (not in SDTMIG):` 下。原有说法逐项核对，均与 PDF 不矛盾：PDF p174 6b 印的是 MHENDTYP；6a 定义和 PDF p171 spec 行都是 MHEVDTYP；KB MH/spec.md:95 有 MHEVDTYP，没有 MHENDTYP；FA/SM 的 examples 用的都是 MHEVDTYP。按 D6 保留。
- **M-2**: T-2 按 keep-correct 处理。正确值能由 PDF 自身确定：同表其他日期都是 YYYY-MM-DD 格式，"011" 唯一合法的读法是 11。KB 保留 2019-11-02，不再是 T4 项。
- md5 assumptions.md: d693e9d9f52459d2898d543919af54f1 → `c4469c2749e81dd20d713d7bd04d6e8a` (行数 55 不变); examples.md 不变 `d7642d4811cca46e92979906328848a2`.
- 复跑 (`python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after2.jsonl`): hit_target 3820，相对改前的回归只有 p0174_a0012 (T-1，预期)，新命中 18，与 attempt 1 相同。check_links live docs 42，基线 42。prose_scan KB→PDF 中 :53 的 3 行属 D6 KB note，是预期的。

## attempt 1 续 2 (reviewer F-1 + 主控改判 T-2, 2026-11-26)

- **T-2 改判**: "2019-011-02" 有两种读法，可读作 2019-11-02 (多了前导 0)，也可读作 2019-01-02 (多了一个 1)，PDF 自身无法确定是哪种。因此 examples.md:106 Ex5 r1 的 MHDTC 照录 PDF 原值 `2019-011-02`，登记为「照录 + T4 用户裁定」。这一条取代「attempt 1 续」里 M-2 的 keep-correct 登记。
- md5 examples.md: d7642d4811cca46e92979906328848a2 → `216c920a870d40a08430b12f2a0d3e77`；assumptions.md 不变 (`c4469c2749e81dd20d713d7bd04d6e8a`)。
- 复跑: census MH 结果为 `OK 5 / UNPARSEABLE 1, cells 449, diffs 0`。fp hit_target 3818，ig34_p0178_a0005 现在命中，MH 新命中 19 条；MH 唯一的回归是 p0174_a0012 (T-1，预期)。另有 3 条回归 p0370_a021 / p0373_a013 / p0374_a011，属 FA – Examples，来自工作树里 B-FA 未提交的改动，不是本批造成的。check_links live docs 42，基线 42。
