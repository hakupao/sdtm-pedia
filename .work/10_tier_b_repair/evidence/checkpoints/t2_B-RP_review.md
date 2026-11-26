# T2 B-RP reviewer

## attempt 1 (2026-11-26, oh-my-claudecode:code-reviewer / opus)

**verdict: PASS**

- base f22fe60; 审 `git diff f22fe60 -- knowledge_base/domains/RP/` (assumptions.md +4, examples.md +7/-7). 整 KB diff 其余文件 (ch01/EC/EX/REL*/TA) 属并行他批, 不在本批; 本批未触 RP 以外文件.
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/7fe38595-6d99-4b86-881d-0dfb0d270167/scratchpad/t2_B-RP_reviewer/`

### 命令与结果 (S=上面 scratch, cwd=repo 根)
```
python3 -I -c "...B-RP.json pdf_ranges -> $S/manifest.json"
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json
  # exit 1 (仅因全局 PDF_ONLY); KB tables 1, status {'OK': 1}, cells 399, diffs 0
  # pdf_only 页 305-307: 只有 p305 OE Ex4 suppoe.xpt / ae.xpt (属 OE, 非 RP); pdf_unparsed 无 p305-307
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl
  # exit 1 RESULT RED: 全局 regress 48 条, grep -cE 'p030[5-7]|RP/' = 0 (均他批 §6.4.2 等)
  # ig34_p0305_a013 hit_target = knowledge_base/domains/RP/assumptions.md
python3 tools/check_links.py | grep 'live docs'   # broken relative links: 18668 (live docs: 42)
pdftoppm -f 307 -l 307 -r 110 -png "source/cdisc/SDTMIG v3.4 (no header footer).pdf" $S/p ; 同 p305
```
- p305-307 fp 未命中 target 的非排除原子 2 条, 均非本批回归 (baseline 同态):
  - ig34_p0306_a022 (spec 脚注 "1In this column, an asterisk (*)…") 属 spec.md; 全 KB domains/*/spec.md 0 份含该脚注 → 全域性缺口, 交 O15/O16 (范围外).
  - ig34_p0307_a008 (Ex1 r1 TABLE_ROW): 原子文本 RPSTRESN 空, 而 PDF 渲染 r1 RPSTRESN=1 → 原子抽取错, KB 正确.

### G-TB4 表格 — Ex1 rp.xpt 独立方法人工逐格 (p307 110dpi 渲染 + pdftotext -layout, 非 bbox)
| Row | 结果 |
|---|---|
| 1-7 (P0001 SCREENING, RPDTC 2008-03-09, RPDY -10) | 一致 (含 RPSTRESN 1/2/3/空/10/空/空, RPDUR r6 P3Y, RPBLFL Y) |
| 8-9 (Day 1, 2008-03-19, 1) | 一致 |
| 10 (Day 29, 2008-04-16, 29) | 一致 |
| 11 (Day 29, **2008-04-16**, 29) | 一致 (writer 修 2008-04-29→04-16 正确) |
| 12-13 (**2009-03-09**, -10) | 一致 (修 2009-03-10→03-09 正确) |
| 14-15 (2009-03-09) | 一致 (未改格) |
| 16-19 (**2009-03-09**, -10) | 一致 (修正确); r16 MENOAGE 55 YEARS, r17 MENARAGE 11, r18 DIAPHRAGM P3Y, r19 N |
| 20 (Day 1, 2009-03-19, 1) | 一致 |
| 21 (Day 29, 2009-04-16, 29) | 一致 |
- 表头 19 列 / 列序 / 21 行 / Row 列 与渲染一致. 7 格修正全对, 其余 392 格无改坏.

### 新增节 a013 核
- `RP/assumptions.md:3` `## RP – Description/Overview` (en dash, 与 PDF p305 标题同) + `:5` 原句; 归一化子串核 = 逐字 (PDF: "A findings domain that contains physiological and morphological findings related to the male…").
- 位置: H1 后、`## RP – Specification` 前 = PDF p305 顺序 (Description/Overview → Specification), 与 CM/IS 先例一致.

### 双向全扫 (p305 "6.3.7.6" 至 p307 页末, 含表格原子)
- PDF→KB: Description/Overview 句 (assumptions:5) / spec 首句 (:9) / Assumptions 1, 2, 3, 3a (含 URL), 4 (:13-20) / "Example 1" + 引导句 + "rp.xpt" + 表 21 行 — 全在. Spec 表 (p305-306) + 脚注属 spec.md (白名单外, 本批未扫格; 脚注全域缺见上).
- KB→PDF: assumptions.md 20 行、examples.md 31 行逐行均有出处; 无 KB 自写解释 / D6 / 伪节号. 微差: :13 "subject's" 直引号 vs PDF 弯引号 (主控口径不改).

### G-TB6 结构行签字
| 行 | 类型 | 判 |
|---|---|---|
| assumptions.md:3 `## RP – Description/Overview` | 新增节标题 (PDF p305 同名) | 签 |
| assumptions.md:4,6 空行 | 结构 | 签 |
| examples.md:21-23,26-29 | 改动表行 (非结构), 已逐格核 | 签 |
- 新增/改动内容行 8 (1 句 + 7 表行), 无出处 0.

### 问题表
| ref | 检查项 | 问题 | 证据 |
|---|---|---|---|
| — | — | 无阻断问题 | — |
| ig34_p0306_a022 | 范围外 | RP/spec.md 缺 spec 脚注 (全域 0/64) | p306 "1In this column, an asterisk (*) indicates…" |

### R2 recheck
- t2_recheck 0 条, 无.
