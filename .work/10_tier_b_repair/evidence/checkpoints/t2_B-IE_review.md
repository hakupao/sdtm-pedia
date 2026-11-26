# T2 B-IE reviewer checkpoint

## attempt 1 (oh-my-claudecode:code-reviewer / opus)

**Verdict: PASS**

- base = HEAD; 本批 diff: `git diff HEAD -- knowledge_base/domains/IE/` → 仅 IE/assumptions.md +10 行 (9→19); examples.md / spec.md 未动.
- md5 (复核): assumptions.md `52184de0d2ce3bb54509155501fbec67`, examples.md `2c90e887fa81855d646b031280c29aba`, spec.md `54c1d1e0916b34d7473a1e449a795c4b` — 与 writer 报告一致.
- 节范围核 (O20): §6.3.4 起于 p193 首行, p194 "6.3.5 Specimen-based Findings Domains" 止; batch lo/hi 193-194 完整覆盖.
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-IE_reviewer/`

### 命令与关键输出 (可复跑, S=上述 scratch)
```
python3 -I -c "...pdf_ranges→$S/manifest.json"
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json
  → KB tables: 1; status: {'OK': 1}; cells compared: 64; diffs: 0   (exit 1 仅因全局 PDF_ONLY 338, 页码均不在 193-194 之外的本批)
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl
  → RESULT: RED (全局 60 条回归, 均为他批页码如 p262/p263); grep -cE 'ig34_p019[34]' $S/fp_regress.jsonl → 0
fp_after: ig34_p0193_a003 hit_target = IE/assumptions.md (基线 hit_target=null); p194 a002-a005/a008-a016 hit_target 均为 IE 文件
直接查目标: python3 -I (fp_match.norm) → Description 句 / spec 首句 in assumptions.md: True (norm) + True (逐字)
python3 tools/check_links.py 2>&1 | grep "live docs" → live docs: 42
pdftoppm -f 193 -l 194 -r 110 -png "source/cdisc/SDTMIG v3.4 (no header footer).pdf" $S/p
```

### 问题表
| ref | 检查项 | 问题 | 证据 |
|---|---|---|---|
| — | — | 无本批问题 | — |

### 1. 完整
- atoms 1 条 (ig34_p0193_a003 REAL_GAP) → writer INSERTED assumptions.md:5, 命中. t2_recheck 0, census DIFF 0, pdf_only (本批页) 0, unparseable 0.

### 2. G-TB4 表格 — ie.xpt (examples.md:13-18) 对 p194 渲染图人工逐格 (独立于 census)
| Row | 结果 |
|---|---|
| 表头 16 列 (Row…IEDY) | 一致, 列序一致 |
| 1 | 一致 (XYZ-0007 / 17 / EXCL17 / Ventricular Rate / EXCLUSION / Y / Y / 1 / WEEK -8 / -56 / 1999-01-10 / -58) |
| 2 | 一致 (XYZ-0007 / 2 / 3 / INCL03 / Acceptable mammogram from local radiologist? / INCLUSION / N / N / … / -58) |
| 3 | 一致 (XYZ-0047 / 1 / 3 / … / 1999-01-12 / -56) |
| 4 | 一致 (XYZ-0096 / 1 / 3 / … / 1999-01-13 / -55) |
- 折行 (XYZ-/0007, WEEK -/8, 1999-01-/10) 按渲染图合并, KB 正确. 0 差.

### 3. G-TB6 反向溯源 (diff 新增 10 行)
| 行 | 类别 | 出处 / 签字 |
|---|---|---|
| 3 `## IE – Description/Overview` | 结构行 (PDF 原小标题, U+2013) | p193 小标题, 签字 |
| 5 Description 句 | 内容 | p193 逐字 "A findings domain that contains those criteria…" |
| 7 `## IE – Specification` | 结构行 (PDF 原小标题) | p193 小标题, 签字 |
| 9 spec 首句 | 内容 | p193 逐字 "ie.xpt, Inclusion/Exclusion Criteria Not Met — Findings…" (U+2014) |
| 11 `## IE – Assumptions` | 结构行 (PDF 原小标题) | p194 首行 "IE – Assumptions", 渲染图确认, 签字 |
| 2/4/6/8/10 空行 | 格式 | 签字 |
- 无出处词句: 0. 结构与 CM/assumptions.md (HEAD) 先例完全同形.

### 4. 位置
- Description/Specification 置于 `# IE — Assumptions` 下、Assumptions 列表前, 与 PDF 顺序 (p193 Description → Specification → p194 Assumptions) 一致; 符合 dispatch notes 域 spec 首句口径.

### 5. 无副作用
- IE 目录仅 assumptions.md 改动; 原 assumptions 1-4 未改 (diff 仅 + 行); 原标题 `# IE — Assumptions` 未变. 工作树中其他 M 文件属他批, 不计.
- 授权范围: Description/Overview + spec 首句 + PDF 原小标题 — 均在 t2_writer_common_brief 授权内.

### 6. R2 recheck
- t2_recheck 为空, 无.

### 双向全扫 (p193-194, 含表格原子)
- PDF→KB: p193 节标题 (KB 用 `# IE — …` 导航标题, 各域先例); Description ✓; Specification 小标题+首句 ✓; spec 表 22 变量 → spec.md (本批范围外, 未动); 脚注 "1In this column, an asterisk (*)…" spec.md 缺 → writer F-1 已登记, 归 O15 (fp p0193_a025 hit_target null, 与 F-1 一致). p194 Assumptions 小标题 ✓, 1-4 逐句 ✓ (item 4 "--\nSTRESU"/"--\nLOBXFL" 为折行, 渲染确认 `--STRESU`/`--LOBXFL`); "IE – Examples" (KB `# IE — Examples` 导航) / Example 1 / 引言句 / Rows 1-2 / Rows 3-4 / ie.xpt / 表 5 行 ✓.
- KB→PDF: assumptions.md 19 行、examples.md 全行均有 PDF 出处或为导航/格式; 无 D6 解释性内容; 无伪节号.
- 观察 (非本批问题): Description 句与 terminology/core/general_part4.md C61536 定义、spec 首句与 ch03 表行信息重叠 — 属不同 PDF/CT 出处, 与 CM 先例同, 不构成 D2 重复.

### 范围外 (沿用 writer)
- F-1 spec.md 缺 p193 脚注 (O15). F-2 IESCAT Notes "or for to categorize as a major or minor exceptions" 与 PDF 一致 (PDF 自身语病), 照录 OK.
