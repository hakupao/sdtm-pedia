# T2 B-FT reviewer

## attempt 1 (2026-11-26, oh-my-claudecode:code-reviewer / opus)

**verdict: PASS**

- base = HEAD (d84a225); 本批 diff: `git diff HEAD -- knowledge_base/domains/FT/` = FT/assumptions.md +23/-0 (纯插入); examples.md / spec.md 未动 (md5 cdd1cfcc… / 9b283c65…); assumptions.md md5 fab7d333c95400865cdd1657933b2542 与 writer 报告一致. QS/RS 无本批改动.
- scratch: /private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-FT_reviewer/

### 命令 (可复跑) 与关键输出
```
S=/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-FT_reviewer
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json
#  -> KB tables: 2; status: {'OK': 2}; cells compared: 113; diffs: 0 ; exit 0
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl
#  -> RESULT: RED; fp_regress.jsonl 51 条全文已读, 无 p318-324 / FT 原子 (均为他批页 p118-p396)
#  p318_a015-a021 hit_target = FT/assumptions.md (a017/a018 的 "PARTIAL" 是 ledger 旧标签, 非匹配结果)
python3 -I $S/cmp.py <PDF 段> <KB 段> <quote_norm>   # 词级 difflib, 见下
python3 tools/check_links.py 2>&1 | grep "live docs"   # live docs: 42 (基线 42)
```
- 直接 norm(verbatim) in norm(target) 检查 (fp_match.norm): p318 a014-a021 全 True; p319 a002/a003/a004/a006 True; p321-323 原子仅 4 条 False, 全部有解释:
  p322_a009 (T-5 "an resolution"), p323_a006 (T-6 --STRNC), p323_a008 (T-1, examples.md), p322_a013 (原子抽取漏 "see Section 4 of the QRS supplement"; PDF p322 与 KB:66 都有该短语 → 原子错, KB 对). p319_a001 heading 见 L-1.

### 双向全扫 p318-324 (含表格原子)
| 段 | PDF→KB | KB→PDF |
|---|---|---|
| p318 §6.3.9 标题 + 3 段 + 2 bullet + 末段 | 词级 diff 仅 `§` 前缀与 Markdown `-` (结构) | assumptions.md:3-14 每词有出处 |
| p319 Description/Overview + spec 首句 | 逐字 (:18, :22) | 同 |
| p319-320 spec 表 + 脚注 | 属 spec.md, 不在本批白名单 (writer F-2 → O15) | — |
| p321 FT – Assumptions 1-2 | 逐字 (:26-30) | 同 |
| p321-323 QRS Shared 1-10 | 引号归一后仅 2 差: 6a "an"→"a" (T-5), 10 "--STRNC"→"--STNRC" (T-6), 均沿用 B-RS 依据; 弯/直引号 9 处 (“standardized responses”×5, “total”, instrument’s×5 含 CT 一处) → O40/T4, 不计本批 | 同 |
| p323 FT – Examples 引言 | 仅差 "qrs)." (T-1) | examples.md:3 |
| p323 Example 1 / 标题 / 叙述 | 逐字 | :5-9 |
| p323 ft.xpt 6 行 × 17 列 | census OK + 渲染图人工逐格一致 (见下) | :13-20 |
| p324 suppft 引言 + 1 行 × 11 列 | 逐字 / 逐格一致 | :22-28 |
| p324 6.3.9.2 QS 之后 | 属 QS 批 | — |

### PDF_TYPO 核依据
- T-1 (p323): 渲染图确认 "(at https://www.cdisc.org/standards/foundational/qrs Additional FT examples" 无右括号与句点; 平行句 p328 "…foundational/qrs). Additional QS examples" → PDF 自身可定, KB "qrs). Additional" 正确. 成立.
- T-5 / T-6: 沿用 B-RS 登记 (冠词语法 / --STNRC 为 CT 变量名), KB 与 RS 副本一致. 成立.

### G-TB4 人工逐格 (p323 渲染 110dpi vs FT/examples.md)
| Row | 结果 |
|---|---|
| 表头 17 列 | 一致 (列序 Row…FTDTC) |
| 1 | 一致 (FTTEST "SIXMW1-Distance at 1 Minute" 单数, 与 PDF 同) |
| 2-6 | 一致 (Minutes; 201/299/396/493/597 ×3 列; m; Y; 1; 2014-03-10) |
| suppft 表头 11 列 + Row 1 | 一致 (p324 pdftotext 单行, FTGRPID/1/FTASSTDV/Assistance Device/CANE/CRF/INVESTIGATOR) |

### G-TB6 新增行反向溯源 (diff 23 行)
| KB 行 | 出处 / 签字 |
|---|---|
| :3 `## §6.3.9 Questionnaires, Ratings, and Scales (QRS) Domains (FT, QS, RS)` | 结构行 (PDF p318 标题, NV/LB `§` 先例) — 签字 |
| :5 | p318 首段 3 句 逐字 (a015+a016) |
| :7 | p318 a017 逐字 |
| :9 | p318 a018 逐字 |
| :11-12 | p318 bullet a019/a020 逐字 (含 URL 与句点) |
| :14 | p318 a021 逐字 |
| :16 `## FT – Description/Overview` | 结构行 (p319 原小标题) — 签字 |
| :18 | p319 a003 逐字 |
| :20 `## FT – Specification` | 结构行 (p319 原小标题) — 签字 |
| :22 | p319 a006 逐字 |
| :24 `## FT – Assumptions` | 结构行 (p321 原小标题) — 签字 |
| 空行 ×12 | 结构 |
无出处词句: 0. KB_AUTHORED / D6: 无.

### 检查项结论
1. 完整: atoms 2 (a017/a018) 均 INSERTED 且命中; t2_recheck 0; census DIFF/pdf_only/unparsed 0. R3 新增 (a014-a016, a019-a021) 均核.
2. G-TB4: 2 表 OK, 人工逐格一致.
3. G-TB6: 23 新增行全有出处, 4 条结构行签字.
4. 位置: §6.3.9 父节引言放 FT/assumptions.md 顶部 (主控认可; NV §6.3.7 / LB §6.3.5 先例), 位于 FT Description 之前, 顺序同 PDF p318→p319→p321. FT assumptions 原列表现挂在 `## FT – Assumptions` 下 (修正了原本会挂到 Specification 下的问题).
5. 无副作用: 本批只动 FT/assumptions.md (授权: Description/Overview、spec 首句、节引言、PDF 原小标题); 无删除/改写; 原有 `# FT — Assumptions` / `## QRS Shared Assumptions` 未变. 全 KB 其余 diff (CE/DA/DD/TS/model06 等) 属他批.
6. R2 recheck: 无条目.

### 问题表 (均非阻断)
| ref | 检查项 | 问题 | 证据 |
|---|---|---|---|
| L-1 ig34_p0319_a001 | 结构/导航 | PDF 子节标题 "6.3.9.1 Functional Tests (FT)" 未落 KB; 现 `## §6.3.9` 后直接 `## FT – Description/Overview`, 同级标题. 内容不缺 (FT – 前缀消歧), MH/PE/TU 有域自身节号标题先例, CM/RS 无 → 可选. 建议 (主控定): 在 :15 后插 `## §6.3.9.1 Functional Tests (FT)`. | p319 首行 "6.3.9.1 Functional Tests (FT)" |
| L-2 QRS Shared 引号 | 逐词 | 直 vs 弯引号 9 处, 已登记 O40 → T4; 文字逐词一致 (除 T-5/T-6) | p321-322 “standardized responses” / instrument’s |
| L-3 p322_a013 | 原子质量 | pdf_atoms 原子漏 "see Section 4 of the QRS supplement." (PDF/KB 都有); 仅影响 fp 匹配, 非 KB 问题 | p322 7. "…study metadata; see Section 4 of the QRS supplement." |

无 CONDITIONAL 修正项.

## attempt 2 (delta 复审, L-1 采纳)

**verdict: PASS**

- `git diff HEAD -- knowledge_base/domains/FT` 全量看: 仍只动 assumptions.md, 纯插入 (+25/-0); examples.md / spec.md md5 未变 (cdd1cfcc… / 9b283c65…).
- assumptions.md md5 0cd5c84b1a7f7976d5e3c7a37d622cad. 去掉 :16-17 后 (`sed '16,17d'`) md5 = fab7d333c95400865cdd1657933b2542 = attempt 1 审过的终态 → delta 只有这 2 行.
- :16 `## §6.3.9.1 Functional Tests (FT)` 与 p319 首行 "6.3.9.1 Functional Tests (FT)" 逐字一致 (`§` 前缀沿用 :3 / NV / LB 节号标题惯例); :17 空行. 结构行签字. 位置在 §6.3.9 引言 (:14) 之后、`## FT – Description/Overview` (:18) 之前, 顺序与 PDF p318→p319 一致. 原子 ig34_p0319_a001 (HEADING) 现已命中.
- live docs: 42 (基线 42).
