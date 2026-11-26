# T2 B-SUPPQUAL — writer checkpoint

## attempt 1 (2026-11-26, oh-my-claudecode:executor / opus)

- base HEAD: `beaefa9cbea4bdd86deffb7091650174ca411c83` (SUPPQUAL 改前工作树 clean)
- 依据: D7 (t1_user_ack.md, 两边都留按 PDF 逐字修 + 顶部 Source 行; 格式照 B-REL); 主控授权 SUPPQUAL 三文件全扫可按 PDF 逐字修.
- 节页范围 (O20): §8.4 = p431 (节标题 + 前 2 段) → p432 (attributions / 唯一性 / --GRPID 段 + §8.4.1 spec 首句 + spec 表) → p433 (表后 4 段 + §8.4.2 + §8.4.3 Ex1 + Ex2 引言) → p434 (suppqs 表 + Additional examples + §8.4.4; 其后 §8.5). batch pdf_ranges 430-432 / pdf_pages 433 **不全**, 实扫 p431-434.
- 渲染: p432-434 110dpi 目视 (scratch).
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-SUPPQUAL_writer/` (*.before.md, p432-434 png, xcheck.py, manifest.json, census_after.json, fp_after.jsonl, fp_regress.jsonl)

### md5 (before → after)
| file | before | after |
|---|---|---|
| SUPPQUAL/assumptions.md | 1453d2816e7bd34d9450707bf47d37ef | 5d545905416b92f9790c6983d90fcb3a |
| SUPPQUAL/examples.md | 21c81fb731e481e6347f11dedc4f326b | 1e7a0ecb20783b72542d797f6e4ab79c |
| SUPPQUAL/spec.md | 51ae042888a4bbbc9479732ced7e555c | 7272860ac4d11ce54e389f4a085a18de |

### 变更清单 (行号 = 改后)
| # | kb_file:line | ref | action | before → after 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 1 | assumptions.md:3, examples.md:3, spec.md:3 | D7 | INSERTED | `> Source text: SDTMIG v3.4 §… (also in chapters/ch08_relationships.md).` (assumptions §8.4, §8.4.1, §8.4.2, §8.4.4; examples §8.4.3; spec §8.4.1) | 431-434 |
| 2 | assumptions.md:13 | R3 scan:p0432:grpid-para | INSERTED | 补 "Just as use of the optional grouping identifier variable (--GRPID) …" 整段 (KB 缺) | 432 |
| 3 | assumptions.md:15-17 | R3 scan:p0432:8.4.1-title + spec 首句 | INSERTED | 新增 `## Supplemental Qualifiers (SUPP--)` (PDF §8.4.1 标题, 同文件 ## 无编号) + "supp--.xpt, Supplemental Qualifiers for [domain name] — Relationship. …" | 432 |
| 4 | assumptions.md:23 | R3 scan:p0433:see-4.5.3 | INSERTED | 补 "See Section 4.5.3, Text Strings that Exceed … 200 characters in length." | 433 |
| 5 | assumptions.md:25 | R3 scan:p0433:see-C1 | INSERTED | 补 "See Appendix C1, Supplemental Qualifiers Name Codes, … CDISC Notes for QVAL." | 433 |
| 6 | assumptions.md:29 | R3 scan:p0433:8.4.2-AP | INSERTED | §8.4.2 段尾补 3 句 (associated persons / SUPPAPFAMH too long / "SUPP"→"SQ", SQAPFAMH) | 433 |
| 7 | assumptions.md:37 | R3 scan:p0434:8.4.4-b3 | REPLACED | "within a parent domain" → PDF "within a parent dataset" | 434 |
| 8 | examples.md:9 | O2 | REPLACED | "(AEOSP and AETRTEM)" → "(AESOSP and AETRTEM)" | 433 |
| 9 | examples.md:15 | census:examples.md:13:1:QNAM / :QLABEL (O2) | REPLACED | AEOSP → AESOSP; "Clinically Medically Important SAE" → "Other Medically Important SAE" | 433 |
| 10 | examples.md:16 | census:examples.md:14:2:QNAM (O2) | REPLACED | AETRTEMA → AETRTEM | 433 |
| 11 | examples.md:20 | R3 scan:p0433:ex2-intro | REPLACED | "(ADAS-COG)" → PDF "(ADAS-Cog)" (正文; 表内 IDVARVAL 仍为 PDF 的 ADAS-COG) | 433 |
| 12 | examples.md:31 | R3 scan:p0434:additional-examples | REPLACED | "domain examples such as Section 5.2, Demographics" → PDF "domain examples, such as in Section 5.2 Demographics" | 434 |
| 13 | spec.md 全 10 变量 | scan:p0432 spec 表 | VERIFIED | Order/Label/Type/Role/Core/CDISC Notes 逐变量 = PDF (脚本对已审 ch08 表 9/9 + QEVAL 目视); Structure 行 = PDF 首句; CT C66734=(DOMAIN), C78735=(EVAL) 映射正确 | 432 |
| 14 | examples.md:24-29 suppqs 4×11 | census:examples.md:22 NO_PDF | VERIFIED | census NO_PDF (p434 不在 pdf_ranges + PDF 例标题缺编号); 对 p434 渲染逐格人工核 44 格全一致, 未改 | 434 |

- 覆盖率自查: atoms 0; census DIFF 2 表 = #9-10 (3 CELL, 改后 census OK 0 diff) + #14 (NO_PDF 人工核); O2 = #8-10; R3 新增 = #2-7, #11-12.

### census 表处理
| census ref | 处理 | 改后 |
|---|---|---|
| examples.md:11 (改后 :13) Ex1 suppae.xpt DIFF 3 CELL | #9-10 | OK, cells 22, diffs 0 |
| examples.md:22 (改后 :24) Ex2 suppqs.xpt NO_PDF | #14 人工逐格 (p434 渲染) | NO_PDF (预期; 内容一致) |

### PDF_TYPO 清单 (KB 写正确值, 依据 = PDF 自身)
- T-1 p433 §8.4.3 引言 "llustrate" → KB 保留 "illustrate" (拼写错; ch08 同).
- T-2 p433 Ex2 标题仅 "Example" 缺编号 → KB 保留 `## Example 2` (前为 Example 1, 文末 PDF 例序; 标题/锚点不改).
- T-3 p433 §8.4.2 末句 "(e.g., resulting in the dataset name SQAPFAMH." 缺右括号 → KB 补 ")" (括号配对; ch08 同).

### 排版字符 (沿用 ch08 / B-REL 已裁口径, 未改)
- PDF 弯引号 (’ “ ”: Ex1 "variables’", Ex2 "subject’s", §8.4.2 “SUPP”/“SQ”, §8.4.4 “INTP”) → KB 直引号 (B-REL 续节 (c) 裁定: 与 ch08 一致, 引号归 O40).
- PDF "STUDYID…QNAM" (单字符省略号) → KB "..."; PDF "Scale–Cognitive" (en dash) → KB 连字符 "-". 与 ch08 现状一致; 如主控要求逐字符, 需与 ch08 同步 (列需主控定 #1).

### 删除清单
| # | 位置 (before) | 改后 | 原因 | 保留副本 |
|---|---|---|---|---|
| D-1 | examples.md:7/:13/:14 旧值 AEOSP / "Clinically Medically Important SAE" / AETRTEMA | 同行 | VALUE_DIFF (O2) | — |
| D-2 | assumptions.md:25 "domain" (1 词) | :37 | 词替换型改写恢复 PDF "dataset" (行不承载其他原子) | — |
| D-3 | examples.md:18 "COG" / :29 "such as Section 5.2," | :20 / :31 | 短语级偏差恢复 PDF 原文 | — |

### 双向全扫 (含表格原子)
- PDF→KB: p431-434 §8.4 全文规范化 (引号/dash/省略号/粗体/空白) 逐句查 SUPPQUAL 三文件拼接文本; 未命中仅 = 节标题粘连行、spec 表版面串列 (由 #13 逐变量核覆盖)、T-3 句 (KB 多 ")")、例标题后粘连表名. 叙述 0 缺. 两张例表对渲染逐格 0 差.
- KB→PDF: 三文件逐句/逐格查 PDF; 未命中仅 = H1 / Source 行 / `## Example 2` (T-2) / "illustrate" (T-1) / T-3 句 / spec 字段块标签 (`**Order:**` 等格式行, 内容由 #13 核) / spec Cross References 导航段 (全库统一格式) / 表格内跨行折行格 (渲染核一致). 无 KB 自写解释性内容 (D6 无), 无伪节号.
- KB_AUTHORED 保留 (纯导航): H1、`## Example 1/2`、`**suppae.xpt**`/`**suppqs.xpt**`、assumptions 的 `## Submitting…` / `## When Not to Use…` (PDF 标题去编号, 锚点不动)、spec `> Class: … | Structure: …` 与 Cross References.
- ch08 §8.4 (:181-256) 对 PDF: 内容一致, 无需主控修内容; 仅排版差 (同上直引号/省略号/en dash; Ex2 em dash 两侧有空格 "questionnaires — Brief", PDF 无空格).

### 范围外发现 / 需主控定
1. (需主控定) 排版字符 …/– 是否逐字符恢复 (SUPPQUAL 与 ch08 需同步); 引号已归 O40.
2. spec.md 记法 (IDVAR/QNAM CT 列 PDF "*" → KB 空; CT 列 C-code 代 codelist 名; 无脚注 ¹) — 全库格式, 同 B-REL O24 → O15, 未改.
3. batch json pdf_ranges (430-432) 偏移, 实际 §8.4 = p431-434 (O20).
4. fp_match: p431-434 改后 EXACT 31 / EQUIVALENT 4 / PARTIAL 7; PARTIAL 7 (p0433_a021-a024, a033-a035) target = ch08, baseline 同为 PARTIAL, 非本批回归.

### 触碰的 unparseable 表
- 无.

### git diff --stat
```
 knowledge_base/domains/SUPPQUAL/assumptions.md | 16 ++++++++++++++--
 knowledge_base/domains/SUPPQUAL/examples.md    | 12 +++++++-----
 knowledge_base/domains/SUPPQUAL/spec.md        |  2 ++
 3 files changed, 23 insertions(+), 7 deletions(-)
```

### 复跑命令
```
S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-SUPPQUAL_writer
python3 -I -c "import json;J=json.load(open('.work/10_tier_b_repair/work/t2_batches/B-SUPPQUAL.json'));json.dump([{k:r[k] for k in ('file','src','lo','hi')} for r in J['pdf_ranges']],open('$S/manifest.json','w'))"
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json   # suppae OK diffs 0; suppqs NO_PDF
python3 -I $S/xcheck.py    # 双向句/格扫描 (p431-434 vs SUPPQUAL 三文件)
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl
grep -cE 'p043[1-4]|SUPPQUAL' $S/fp_regress.jsonl   # 0 (全局 RED 60 条为他批在途)
python3 tools/check_links.py 2>&1 | grep "live docs"   # live docs: 42
```
