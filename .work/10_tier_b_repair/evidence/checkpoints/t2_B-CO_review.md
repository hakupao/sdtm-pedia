# T2 B-CO reviewer

## attempt 1 (审 writer attempt 1+2 终态; oh-my-claudecode:code-reviewer / opus; base = HEAD, 改动未提交)

**verdict: PASS**

- 页范围: p60 (§5 章引言 + 5.1 CO Description/spec 首句/spec 表/脚注) → p61 Assumptions 1-6 + Ex1 Row 1-5 叙述 → p62 Row 6-8 + co.xpt; p62 后半 5.2 DM 属 B-DM, 未审. batch lo/hi 60-62 完整覆盖.
- 本批 KB diff 仅 2 文件 2 行: `CO/examples.md:28`, `CO/assumptions.md:5`. `git diff HEAD -- knowledge_base/domains/CO/spec.md` 0 行. 其余 KB diff (CE/CM/DV/HO/IE/MI/ML/QS) 属他批, 不计.

### 命令 (scratch = `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/855742cf-a178-484a-8229-67de708e11e7/scratchpad/t2_B-CO_reviewer/`)
```
S=<scratch>; manifest 由 B-CO.json pdf_ranges 生成 (CO/examples.md ig34 60-62)
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json
  → "KB tables: 1; status: {'OK': 1}; cells compared: 120; diffs: 0"; exit 1 (RESULT RED 仅因全局 PDF_ONLY 338, p60-62 内 PDF_ONLY 0; pdf_unparsed 2 = pp.xpt/sc.xpt Ex2, 不在本批页)
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl
  → RESULT RED (全局, 他批页 p0262/p0263 等); grep -cE 'p006[0-2]|domains/CO/' fp_regress.jsonl → 0
python3 -I -c "...from fp_match import norm; norm(<p60 第2句>) in norm(CO/assumptions.md)" → True
pdftotext -f 60 -l 62 -layout "source/cdisc/SDTMIG v3.4 (no header footer).pdf"; pdftoppm -r 110 p60-62
python3 tools/check_links.py 2>&1 | grep "live docs" → live docs: 42
```

### 问题表
| ref | 检查项 | 问题 | 证据 |
|---|---|---|---|
| — | 1-6 | 无 | — |

### G-TB4 / 人工逐格 (独立方法: p62 渲染图 110dpi + layout 列位置; 不采信 census 自比)
co.xpt 表头 15 列 Row…CODTC 顺序与 PDF 一致.
| Row | 结果 |
|---|---|
| 1 | 一致 (RDOMAIN/IDVAR/IDVARVAL/COREF 空; COVAL Comment text; CODTC 2003-11-08) |
| 2 | 一致 (PE; COREF VISIT 7; CODTC 2004-01-14) |
| 3 | 一致 (AESEQ/7/PAGE 650; COVAL/COVAL1/COVAL2 = First 200 characters / Next 200 characters / Remaining text) |
| 4 | 一致 (改后): 渲染图 "Remaining text" 位于 COVAL1 列 (与 Row 3 "Next 200 characters" 同列), COVAL2 空; COREF "PAGE 320-355" |
| 5 | 一致 (VSGRPID/VS2; COREF 空) |
| 6 | 一致 (SV; VISITNUM/4; Comment Text 大写 T 照 PDF) |
| 7 | 一致 (RDOMAIN 空; COREF VISIT 4) |
| 8 | 一致 (VISITNUM 4; CODTC 空) |
COEVAL 8 行均 PRINCIPAL INVESTIGATOR (PDF 折行). 共 120 格, 0 差. 非 PDF_TYPO: Row 4 改法与 Assumption 4 "next 200 in COVAL1" 一致.

### 双向全扫 p60-62 (含表格原子)
- PDF→KB: §5 引言 2 句 (第 2 句 attempt 2 补, 逐字); 5.1 标题; Description 1 句; spec 首句 (`CO/assumptions.md:15`); spec 脚注 (:17); Assumptions 1-6 含 3a-c 逐句一致 (6 中 "--\nREFID" 为折行); Row 1-8 叙述 (`examples.md:5-19`) 逐句一致 (含 PDF 原文 "are populated link the comment" 照录); co.xpt 见上. spec 变量表属 spec.md (不在本批范围, 未改).
- KB→PDF: assumptions.md 34 行、examples.md 32 行均有出处; 无 KB 自写解释性内容 (D6 无需), 无伪节号; `## §5 …` 标题中 "§" 为既有 KB 样式, 未改.
- R2: 本批 t2_recheck 0. 新发现缺失: 无.

### G-TB6 反向溯源 (diff 新增/改动行)
| diff 行 | 出处 | 签字 |
|---|---|---|
| `assumptions.md:5` | p60 §5 引言 2 句同段, 逐字 ("Special-purpose domains provide specific, standardized structures…") | OK |
| `examples.md:28` | p62 co.xpt Row 4 | OK |
结构行: 无新增 (无新标题/表头/分隔线/锚点). 新增 2 行 / 无出处 0.

### 授权核
- `CO/assumptions.md:5` 超 writer 通用授权字面, 由主控 M-1 授权 (writer checkpoint attempt 2 记录); 改动仅句末接续, 未动其他行. 位置: PDF 两句同段, KB 同段接续正确.
- 删除: 仅 Row 4 COVAL2 旧值 (移到 COVAL1), 无清单外删除.
