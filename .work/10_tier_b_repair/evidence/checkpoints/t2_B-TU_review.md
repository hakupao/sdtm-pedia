# T2 B-TU review

## attempt 1 (2026-11-26, oh-my-claudecode:code-reviewer / opus)

**verdict: PASS**

### 命令 (可复跑; scratch = /private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/7fe38595-6d99-4b86-881d-0dfb0d270167/scratchpad/t2_B-TU_reviewer)
```
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json   # exit 1: RED 仅来自全局 PDF_ONLY
  → B-TU 表: OK 5 (examples:21/33/53/68/90) / UNPARSEABLE 6 (assumptions:38/56/80/88/98/109) / DIFF 0
  → 页 344-358 内 PDF_ONLY: p344 ss.xpt (SS), p355-358 tr.xpt×2 + relrec.xpt×2 (TR/examples.md, B-TU manifest 外) → 非本批
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl   # exit 1, 48 regress 全局
  → 过滤 p340-360: 0 条 (TU 隔离回归 0; 其余为他批 p118-p364)
pdftoppm -r 110 p344-349,353,354,356; -r 160/170 p349,353,354,356 (表格逐格)
python3 tools/check_links.py | grep "live docs"   # live docs: 42 (≤42)
git diff f22fe60 -- knowledge_base/domains/TU/    # = git diff HEAD (TU 无中间 commit); 只 2 白名单文件
```

### 问题表
| ref | 检查项 | 问题 | 证据 |
|---|---|---|---|
| — | — | 无阻断项 | — |

### (1) VALUE_DIFF + census 触碰表 (独立对渲染逐格)
| ref | KB after | PDF | 结论 |
|---|---|---|---|
| a015 examples:24 TUTESTCD | VSLIDENT | p353 r2 "VSLIDENT" | 一致 |
| a016 examples:25 TUTEST | Limb Lesion Identification | p353 r3 "Limb Lesion Identification" | 一致 |
| a018 examples:27 TUTESTCD | VSLIDENT | p353 r5 "VSLIDENT" | 一致 |
| a005 examples:36 QNAM | TUPAGA | p354 supptu r2 "TUPAGA" | 一致 |
| Ex1 tu.xpt 5 行×17 列 | 全格 | p353 | 一致 |
| Ex1 supptu 5×11 | 全格 | p354 | 一致 |
| Ex2 tu 8×19 / supptu 5×9 (未改) | 全格 | p354 | 一致 |
| Ex3 tu.xpt 表头 | …TUDTC, TUDY (20 列) | p356 列序同 | 一致 |
| Ex3 TUDY r1-r7 | -2/-3/-3/-3/-2/48/88 | p356 同 | 一致 |
| Ex3 r5 TULAT | RIGHT | p356 R1-NT02 RIGHT | 一致 |
| Ex3 其余格 7×19 | 全格 (r7 TULAT LEFT) | p356 | 一致 |

### (2) 人工逐格 — 触碰的 UNPARSEABLE 表 (p349 160dpi 渲染)
METIND 表 assumptions:88-92 (8 列):
| 行 | TULNKID | TUTESTCD | TUTEST | TUORRES | TUSTAT | TULOC | TUMETHOD | VISIT | 结论 |
|---|---|---|---|---|---|---|---|---|---|
| 表头 | | | | | | | | | 8 列名/顺序一致 |
| r1 | 空 | METIND | Metastatic Tumor Site Indicator | Y | 空 | LIVER | CT SCAN | BASELINE | 一致 |
| r2 | 空 | METIND | 同 | N | 空 | BRAIN | MRI | BASELINE | 一致 |
| r3 | 空 | METIND | 同 | 空 | NOT DONE | PLEURAL CAVITY | 空 | BASELINE | 一致 (NOT DONE 在 TUSTAT 列) |

Disease recurrence 表 assumptions:98-105 (8 列):
| 行 | TUREFID | TULNKID | TUTESTCD | TUTEST | TUORRES | TULOC | TULAT | TUMETHOD | 结论 |
|---|---|---|---|---|---|---|---|---|---|
| 表头 | | | | | | | | | 一致 |
| r1 | IMG-00007 | LOC01 | DRCRLTLC | Disease Recurrence Relative Location | LOCAL | BREAST | LEFT | CT SCAN | 一致 |
| r2 | IMG-00007 | REG01 | DRCRLTLC | 同 | REGIONAL | INTERNAL MAMMARY LYMPH NODE | 空 | CT SCAN | 一致 |
| r3 | IMG-00007 | REG02 | DRCRLTLC | 同 | REGIONAL | INFRACLAVICULAR LYMPH NODE | 空 | CT SCAN | 一致 (PDF 折行 INFRACLAVIC/ULAR) |
| r4 | IMG-00007 | DIS01 | DRCRLTLC | 同 | DISTANT | LIVER | 空 | CT SCAN | 一致 |
| r5 | IMG-00007 | DIS02 | DRCRLTLC | 同 | DISTANT | COLON | 空 | CT SCAN | 一致 |
| r6 | IMG-00007 | CON01 | DRCRLTLC | 同 | CONTRALATERAL | BREAST | RIGHT | CT SCAN | 一致 (PDF 折行 CONTRALATE/RAL) |
- 独立方法交叉: pdf_pages/ig34_p0349.txt layout 文本 :8 "NOT DONE" 位于 TUSTAT 列位, :25-45 六处 "DRCRLTLC".
- 未触碰 UNPARSEABLE 表 (split 9 行 p347, location-of-interest 4 行 p347, NTIND 3 行 p348, QNAM 2 行 p349): 顺带对渲染逐格, 全部一致.

### (3) R3 恢复 12 项 (逐字 / 位置)
| N | KB | PDF | 结论 |
|---|---|---|---|
| N-1 | examples:3 `## §6.3.12.3 Tumor Identification/Tumor Results Examples` | p353 标题 | 一致; 写法同 MB/examples.md:3 先例 |
| N-2 | assumptions:5 引言 3 句 | p344 §6.3.12 段 | 逐字一致 (含 "Disease Response and Clin Classification" PDF 原样链接文本) |
| N-3 | assumptions:7 `## 6.3.12.1 Tumor/Lesion Identification (TU)` | p344 | 一致, 位于 Description 前 |
| N-4/5 | assumptions:21-23 `## TU – Specification` + spec 首句 | p345 | 逐字一致; 位置 Description 与 Assumptions 间 (CM/IS 口径) |
| N-6 | assumptions:25 `## TU – Assumptions` | p346 | 一致, item 1 前 |
| N-7 | assumptions:34 | p347 | 见 (4) |
| N-8 | assumptions:52-54 | p347 "This example represents tumors assessed by location of interest." | 逐字; PDF 亦为第二段 |
| N-9 | assumptions:70 6c "new tumor/lesion, its" | p348 6c | 一致 |
| N-10 | METIND r3 NOT DONE→TUSTAT | p349 | 一致 |
| N-11 | DRCRLTLC ×6 | p349 | 一致 |
| N-12 | CONTRALATERAL | p349 | 一致 (单元格折行) |

### (4) D-1 / 并段 / T-1
- D-1: p347 "During the course of a trial, a tumor/lesion might split into…" — 无 "identified at baseline" → 删除正确.
- D-2 并段: p347 "…controlled-terminology. During the course of a trial…" 同一段内接续 → 合并正确, 无文字丢失.
- T-1: p353 Rows 1-2 印 "aorta-iliac vessel"; 同页叙述 "aorto-iliac vessel (L01-1)" 与表 r2 "AORTO-ILIAC PERIPHERAL ARTERY" → PDF 自身可定正确值, KB 保留 aorto-iliac 并登记, 符合 PDF_TYPO 口径.

### (5) 双向全扫 (p344 §6.3.12 起 - p349, p353-354, p356 TU 部分; 对渲染逐句 + 表格原子)
- PDF→KB: 引言 / 6.3.12.1 / Description 2 段 + 5 bullet / Specification 首句 / Assumptions 1(a-c)-13 全部句子、4 张假设内表 + 2 张 p349 表、Ex1-Ex3 叙述 + Rows 说明 + 5 张 TU 表 → KB 全部有, 位置同节. 缺失 0.
  (spec 表行 + 脚注 p345-346 属 TU/spec.md, 白名单外; writer 已列 O-TU-1.) TR 叙述/表 (p350-352, p354 下, p355-358) 属 TR, 不入 TU.
- KB→PDF: 全文件逐句均可在 PDF 找到; 唯一 KB 自写 = examples:5 "Note: TU and TR share examples. See also `[TR Examples](../TR/examples.md)`." 纯导航、不矛盾, 按 D6 范围不标注, 认可.
- KB 标题 vs PDF: `## 6.3.12 Tumor/Lesion Domains` / `## 6.3.12.1 …` / `## TU – Description/Overview` / `## TU – Specification` / `## TU – Assumptions` / `## §6.3.12.3 …` 与 PDF 措辞一致; `## Example 1-3` 对 PDF "Example N"; `# TU — Assumptions/Examples` 文件结构标题.
- 仅格式差异 (不改, 同前批口径): 6b 弯引号, assumption 2 "Tumor Split”" 引号不配对, `**Rows N:**` 加粗; PDF "is used identify" (assumption 10) KB 照录.
- PDF 自身交叉引用不一致 (assumption 2 "see assumption 3 for details on splitting") KB 照录, 正确.

### G-TB6 结构行签字
新增结构行: assumptions:7 (6.3.12.1 标题), :21 (TU – Specification), :25 (TU – Assumptions); examples:3 (§6.3.12.3 标题); examples:90-91 Ex3 表头+分隔线 (加 TUDY). 全部有 PDF 出处, 签字. 新增/改动内容行 ~30, 无出处 0.

### (6) 无副作用
- KB diff 只含 TU/assumptions.md + TU/examples.md (其余 KB 改动为他批 commit/工作树, 非本批); 无清单外删除; 已有标题/锚点未变.
- fp 隔离回归 (p340-360) 0; check_links live docs 42 (≤42).
- t2_recheck 0 项, 无 R2 判定.
