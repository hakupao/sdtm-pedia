# T2 B-DD reviewer

## attempt 1 (审 writer attempt 1+2 终态; oh-my-claudecode:code-reviewer / opus)

**verdict: PASS**

- base = HEAD (d84a225); 本批 diff `git diff HEAD -- knowledge_base/domains/DD/` = assumptions.md 13+/1-; examples.md / spec.md 未动 (md5 e890adec… / 8f80011d…); assumptions.md md5 = 78b98f31dca3afc892e57033dc255b01 (= writer attempt 2 报告值).
- 页范围: DD 节 p183 顶 (6.3.2) → p185 中 (6.3.3 EG 前); p182 无 DD 内容。与 writer 一致。
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-DD_reviewer/`

### 命令与结果 (可复跑)
```
S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-DD_reviewer
# manifest = batch pdf_ranges (examples.md 183-185) + 追加 assumptions.md 183-185
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json
  -> KB tables 5, status OK 5, cells 147, diffs 0; exit 1 仅因全局 PDF_ONLY (p183-185 内 pdf_only = 0, pdf_unparsed 无本批页)
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl
  -> RESULT: RED, regress 51 条; grep -E 'p018[3-5]|DD/' fp_regress.jsonl = 0 (全为他批, 如 p0363 §6.4.2)
python3 -I $S/cmp.py "source/cdisc/SDTMIG v3.4 (no header footer).pdf"   # KB assumptions.md 每行 (去 #/编号/**) vs p183-185 pdftotext 归一化
python3 tools/check_links.py 2>&1 | grep "live docs"   -> live docs: 42
```

### 检查结果
| 项 | 结论 |
|---|---|
| 1 完整 | atoms 2 (p183_a003/a004) 均 INSERTED, fp hit_target = DD/assumptions.md; t2_recheck 0; census diff 0 / pdf_only 0 / unparseable 0 |
| 2 G-TB4 | examples.md 5 表 census OK (dd p184 70 格, ae 13, dd p185 10, ds 30, relrec 24, 0 diff); 另对渲染图 p184/p185 (110dpi) 人工逐格: 表头/列序/每格/relrec RELTYPE 空列 全部一致 |
| 3 G-TB6 反向 | assumptions.md 新增 12 行 + 改 1 行逐条在 PDF 命中 (见下签字); 无自造句 |
| 4 位置 | Description/Overview + Specification 首句在文件标题与 Assumptions 之间, 与 CV/RE 先例同构; PDF 顺序 Description→Specification→Assumptions 一致 |
| 5 无副作用 | DD 目录仅 assumptions.md 变动; 无删除 (唯一 - 行为 codeable→codetable 旧值替换); 原列表 1-3、5 未动 |
| 6 R2 recheck | 无条目 |
| 粗体 | p183 渲染 (150dpi) 确认第 1、2 个 "not" 为粗体, 第 3 个 ("is not already") 非粗体; KB 恰为 `**not**` ×2 + 普通 not ×1 ✓ |
| codetable | p184 assumption 4 原文 "described in the DD codetable"; KB:21 已改, cmp.py HIT ✓ (主控授权) |
| 字符 | 标题 en dash U+2013 ×3 与 PDF 一致; spec 首句 em dash U+2014 与 PDF 一致 |

### G-TB6 新增/改动行签字 (DD/assumptions.md, 行号 = 改后)
| 行 | 内容 | PDF 出处 | 结论 |
|---|---|---|---|
| 3 | `## DD – Description/Overview` | p183 节小标题 | 结构行, 签字 |
| 5 | "A findings domain that contains the diagnosis of the cause of death for a subject." | p183 | 逐字 HIT |
| 7 | "The domain is designed to hold supplemental data …previously did not have a clearly defined home." (4 句) | p183 | 逐字 HIT (去 ** 后) |
| 9 | `## DD – Specification` | p183 节小标题 | 结构行, 签字 |
| 11 | "dd.xpt, Death Details — Findings. One record per finding per subject, Tabulation." | p183 | 逐字 HIT |
| 13 | `## DD – Assumptions` | p184 原标题 "DD – Assumptions" | 结构行, 签字 (PDF 原标题 ✓) |
| 21 | assumption 4 "...DD codetable (available at https://www.cdisc.org/standards/terminology/controlled-terminology)." | p184 | 逐字 HIT |

### 双向全扫 (p183-185, 含表格原子)
- PDF→KB: p183 叙述 3 段 (a003/a004/a006) 命中 assumptions.md; p183 spec 表 a007-a019 + 脚注 a020 属 spec.md (白名单外, writer F-3 → O15; spec.md 已有 DDRESCAT/DDDY 等节, 非本批). p184 assumptions 1-5 全命中 (5 因 PDF 折行 "-- SPEC" 归一化 MISS, 人工核 KB "--SPEC" 正确, 未改动行); Ex1/Ex2 叙述、Rows 标签、5 个 xpt 标签、5 表全部命中 examples.md. p185 a020+ 属 EG.
- KB→PDF: assumptions.md 除文件标题 `# DD — Assumptions` (导航) 外全部命中; examples.md 全部行有 PDF 对应 (`## Example 1/2`、`**Rows …:**` 为结构). 无 KB 自写解释内容 (D6 无), 无伪节号.

### 问题表 (均非阻断)
| ref | 检查项 | 问题 | 证据 | 严重度 / 置信 |
|---|---|---|---|---|
| examples.md:5 | 字符 | PDF p184 "subject’s" 弯撇号, KB 直撇号 | p184 Ex1 首句 | LOW / HIGH — 全库直引号惯例, writer F-2 已登记, 不改 |
| examples.md:1 | 标题 | PDF 小标题 "DD – Examples" (en dash), KB 文件标题 `# DD — Examples` (em dash) | p184 | LOW / HIGH — 文件级导航标题, 全库同构, 不在本批改动范围, 不改 |
| writer 报告 F-1 | 文档 | attempt 1 行号 ":19" 实为插入前旧行号 | writer attempt 2 已自行更正 | 信息 |

### 人工逐格表 (渲染 p184/p185 110dpi)
| 表 | 行数 | 结果 |
|---|---|---|
| Ex1 dd.xpt (p184) | 7 | 一致 (含 Row 6 CHF / CONGESTIVE HEART FAILURE, Row 7 MEMORIAL HOSPITAL / HOSPITAL) |
| Ex2 ae.xpt (p184) | 1 | 一致 (13 列, AEOUT FATAL, AESER Y, AESDTH Y) |
| Ex2 dd.xpt (p185) | 1 | 一致 |
| Ex2 ds.xpt (p185) | 3 | 一致 (DSDTC/DSSTDTC 列序一致) |
| Ex2 relrec.xpt (p185) | 3 | 一致 (RELTYPE 空, RELID 1) |
