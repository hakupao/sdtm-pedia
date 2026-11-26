# T2 B-SU reviewer

## attempt 1 (oh-my-claudecode:code-reviewer / opus)

**verdict: PASS**

- 范围: base = HEAD (`beaefa9`; 437c2ad..HEAD 无 SU 文件改动), `git diff HEAD -- knowledge_base/domains/SU/` = assumptions.md +10 行纯插入; examples.md md5 `d5b3e9a8…` = HEAD; spec.md 未动. 工作树中其他 KB 改动属别批 (CE/CO/DI/DV/IE/ML/SV/TI/TV), 不计本批.
- 节页范围: 独立核 p129 (6.1.6 节首, Description/Overview, spec 首句, spec 表) → p130-131 (spec 续; p131 SU – Assumptions 1-4) → p132 (5; Examples Ex1 叙述) → p133 (su.xpt; 其后 6.2). 完整 = **p129-133**; batch json hi=132 漏 p133 (同意 writer F-1). 本域无节引言 NOTE.
- 授权: Description/Overview + spec 首句 + PDF 原有小标题 `SU – Assumptions` 均在通用 brief 授权内; 无授权外改动.

### 命令与关键输出 (scratch = `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-SU_reviewer`)
```
S=<scratch>; echo '[{"file":"knowledge_base/domains/SU/examples.md","src":"ig34","lo":129,"hi":133}]' > $S/manifest.json   # hi 修正为 133
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json
  -> KB tables: 1; status: {'OK': 1}; cells compared: 126; diffs: 0; exit 1 仅因全局 PDF_ONLY (p129-133 内 pdf_only = [] , pdf_unparsed 仅 p274/p342)
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl
  -> RESULT: RED (全局 60 条回归, grep -cE 'ig34_p01(29|3[0-3])_' fp_regress.jsonl = 0, 均为他批页码)
python3 -I -c "...from fp_match import norm; norm(verbatim) in norm(open('knowledge_base/domains/SU/assumptions.md').read())"
  -> ig34_p0129_a003 True; ig34_p0129_a005 (spec 首句) True
python3 tools/check_links.py 2>&1 | grep "live docs"   -> live docs: 42
```

### 问题表
| ref | 检查项 | 问题 | 证据 |
|---|---|---|---|
| — | — | 无阻塞问题 | — |
| ig34_p0132_a014 (fp 未命中) | T-1 PDF_TYPO | 预期: PDF "SUENTTP" 笔误, KB examples.md:19 写 SUENTPT. 依据 PDF 自身: spec 变量名 SUENTPT (p130 L52, p131 L6), 同页 Row 3 "SUENTPT and SUENRTPT are not populated", p133 表头 SUENTPT. 取舍符合口径 (PDF 自身可定 → 正确值). 注: writer 报告引用行号 examples.md:23 实为 Row 3 行, Row 1 在 :19 (报告笔误, 不影响 KB) | p132 "(SUENTTP = "2006-01-01", SUENRTPT = "ONGOING")" |
| ig34_p0133_a003 (fp hit None) | 原子质量 | 原子 verbatim 本身串列 (21 格, 多出 "2006-01-01"), in_pdf_page=false; 渲染图核 KB Row 1 正确, 非 KB 问题 | p133 渲染图 |
| ig34_p0131_a001 PARTIAL hit spec.md | 范围外 | spec 表行, 属 spec.md (O15), 非本批 | — |

### 人工逐格 (su.xpt, p133 130dpi 渲染图 vs examples.md:35-43, 独立于 census)
| Row | 结果 |
|---|---|
| header 18 列 | 一致 (Row…SUENRTPT 顺序一致) |
| 1 | 一致: CIGARETTES/TOBACCO, SUSTAT/SUREASND 空, 2/PACK/QD, SUSTDTC/SUENDTC 空, SUSTTPT 2006-01-01, BEFORE, SUENTPT 2006-01-01, ONGOING |
| 2 | 一致: COFFEE/CAFFEINE, 3/CUP/QD, SUSTDTC=SUENDTC=2006-01-01, 相对时间 4 列空 |
| 3 | 一致: CIGARETTES/TOBACCO, 1/PACK/QD, SUSTDTC 空, SUENDTC 2003, SUSTTPT 2006-03-15, BEFORE, SUENTPT/SUENRTPT 空 |
| 4 | 一致: TEA/CAFFEINE, 1/CUP/QD, 2006-03-15 ×2 |
| 5 | 一致: COFFEE/CAFFEINE, 2/CUP/QD, 2006-03-15 ×2 |
| 6 | 一致: CIGARETTES/TOBACCO, NOT DONE, "Subject left office before CRF was completed", 其余空 |
| 7 | 一致: CAFFEINE/CAFFEINE, NOT DONE, 同 SUREASND, 其余空 |

### 双向全扫 (p129-133, 含表格原子)
- PDF→KB: p129 Description 句 → assumptions.md:5 逐字; spec 首句 → :9 逐字 (em dash 同 PDF); p131-132 Assumptions 1.a-b / 2.a-c / 3.a-b / 4.a-b / 5 → :13-30 逐字 (弯→直引号, "--\nMOOD" 折行 → "--MOOD", 全局惯例); "see Section 4.2.6, Grouping Variables and Categorization" 交叉引用在 :24. p132 Examples 引言/7 条 bullet/SUCAT 段/Not shown/Row 1-7 → examples.md:5-31 逐字 (唯一差 T-1); "See Section 4.4.7, Use of Relative Timing Variables" 在 :19. p133 `su.xpt` 标题 + 表 → :33-43 (逐格见上). spec 表 (p129-131) 归 spec.md, 范围外. fp_match: p131_a005-a017, p132_a001, a004-a020 (除 a014=T-1) 均 EXACT 命中 SU 文件.
- KB→PDF: assumptions.md 30 行、examples.md 43 行逐行均有 PDF 出处; 无 KB 自写解释性内容 (无 D6 项), 无伪节号.

### G-TB6 结构行签字
- assumptions.md:3 `## SU – Description/Overview` = PDF p129 小标题 ✔
- assumptions.md:7 `## SU – Specification` = PDF p129 小标题 ✔
- assumptions.md:11 `## SU – Assumptions` = PDF p131 小标题 ✔
- 空行 :2/:4/:6/:8/:10/:12 ✔; 格式与 CM/CE 先例 (assumptions.md 头 11 行) 一致 ✔
- 新增内容行 :5 / :9 → PDF p129 逐字 ✔; 无出处行 0.

### R2 recheck
- t2_recheck = [] (无).

### 结论
atoms 1/1 处理 (INSERTED, 目标命中); census 1 表 OK 0 diff + 人工逐格 7×18 0 差; G-TB6 新增 5 非空行 (3 结构 + 2 内容, 无出处 0); 无白名单外改动; live docs 42. PASS.
