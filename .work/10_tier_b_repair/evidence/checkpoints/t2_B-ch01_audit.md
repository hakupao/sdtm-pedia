# T2 B-ch01 auditor (Rule A 独立抽检)

## attempt 1 (2026-11-26, oh-my-claudecode:verifier / opus)

**verdict: PASS** — 独有丢失 0, 忠实度错误 0 (18 样本: seeded 10 + §1.1-§1.3 补抽 8); G-TB8 通过.

- 审核对象: ch01 md5 `e7c39a7ae829e3abe67a7e49808c584e` (= writer 续 / reviewer 续 签字版本); base `fb62af2`, `git diff --stat` +75/-68.
- 真值: `work/pdf_pages/ig34_p0007..0010.txt` + `pdftoppm -f 9 -l 10 -r 110` 渲染 (p9/p10 目视). 先独立判, 判完才读 writer/reviewer 报告.
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/7fe38595-6d99-4b86-881d-0dfb0d270167/scratchpad/t2_B-ch01_auditor/` (S)

### 抽样 (repo 根)
```
# 主样本: t2_auditor_v1.0.md 抽样脚本原样, b="B-ch01", seed=20261126 → $S/sample.json
→ C=11 P=47 N=10 (C 抽 5 + P−C 抽 5); P 只含 p9/p10 (batch pdf_pages=[9,10])
# 补抽 (章被全量重写 >50%, 须覆盖 §1.1-§1.3 = p7/p8): p7/p8 ig34 prose 原子池 43, random.Random(20261126).sample(pool, 8) → $S/supp.json
# §1.4.1 层级: random.Random(20261126).sample(range(74,100), 10) → KB 行 [75,76,81,83,84,88,89,93,95,96]
```

### 样本判定
| # | atom_id | PDF 页:行 + 摘要 | KB file:line | 丢失? | 忠实? | 位置? | 说明 |
|---|---|---|---|---|---|---|---|
| 1 | ig34_p0010_a014 | p10:22 CDISC Notes 子项 "Rules for when or how … populated …" | ch01:97 | 无 | Y | §1.4.1 CDISC Notes L2 | 逐字 |
| 2 | ig34_p0010_a025 | p10:40-43 LNKID/LNKGRP distinction 末句 (other identification variables / examples reviewed) | ch01:109 | 无 | Y | §1.5 LNKID 小节 | 逐字 (-\n-LNKID 合并) |
| 3 | ig34_p0009_a003 | p9:4-7 第4条 Review Section 5/6 … "See the implementation examples …" | ch01:58 | 无 | Y | §1.4 #4 | 逐字 |
| 4 | ig34_p0009_a004 | p9:8-9 第5条 Read Section 7 … typical protocols | ch01:59 | 无 | Y | §1.4 #5 | 逐字 |
| 5 | ig34_p0010_a009 | p10:15-16 "Format: ISO 8601 …" | ch01:92 | 无 | Y | §1.4.1 L2 (o) | recheck → PRESENT |
| 6 | ig34_p0009_a022 | p9:40-41 Sponsors should create an appropriate label … | ch01:79 | 无 | Y | Variable Label L2 | 逐字 |
| 7 | ig34_p0009_a024 | p9:43 "Controlled Terms, Codelist, or Format" | ch01:81 | 无 | Y | L1 | atom verbatim 缺逗号 (atom 错); 渲染与文本层均有逗号, KB 按 PDF |
| 8 | ig34_p0010_a023 | p10:37-39 "This implies … RELTYPE = ONE → --LNKID; MANY → --LNKID (and not --LNKGRP)" | ch01:109 | 无 | Y* | §1.5 LNKID 小节 | *MANY 分句 KB 写 "--LNKGRP (and not --LNKID)" = T-2 keep-correct (PDF_TYPO 规则; 依据 p10 前句 + p31:7 "--LNKGRP … identify a group of records"); 已登记 t1_lane_notes:88 待 T4 知悉. "in RELREC" 已补 |
| 9 | ig34_p0009_a018 | p9:36 Variable Name 子项 "no domain prefix → taken directly from the SDTM" | ch01:75 | 无 | Y | L2 | 逐字 |
| 10 | ig34_p0009_a009 | p9:21-22 "The following guides are available at <sdtmig URL>:" | ch01:64 | 无 | Y | §1.4 guides 段 | 逐字, URL 在; batch note 必补项 |
| 11 | ig34_p0007_a005 | p7:6-7 Version 3.4 supersedes all prior versions | ch01:7 | 无 | Y | §1.1 | 逐字 |
| 12 | ig34_p0007_a008 | p7:13-14 intended for companies and individuals … | ch01:11 | 无 | Y | §1.1 | 逐字 |
| 13 | ig34_p0007_a018 | p7:32-34 Section 8 bullet (… where data belong in the SDTM) | ch01:24 | 无 | Y | §1.2 | 逐字 |
| 14 | ig34_p0007_a023 | p7:42 All updates are intended to be backward-compatible | ch01:30 | 无 | Y | §1.3 引导 | 逐字 |
| 15 | ig34_p0008_a001 | p8:1-2 DA domain bullet + See Section 6.3.1 | ch01:32 | 无 | Y | §1.3 bullet | 逐字, xref 在 |
| 16 | ig34_p0008_a009 | p8:22-24 TU/TR bullet + See Section 6.3.12 | ch01:40 | 无 | Y | §1.3 bullet | 逐字, xref 在 |
| 17 | ig34_p0008_a011 | p8:27-28 FA bullet + See Section 6.4 | ch01:42 | 无 | Y | §1.3 bullet | 逐字, xref 在 |
| 18 | ig34_p0008_a020 | p8:41-42 See Section 4.3 … Controlled Terminology | ch01:49 | 无 | Y | §1.3 Version 3.1 段末 | 逐字 |

独有丢失 0 / 18; 忠实度错误 0 / 18.

### 全章独立核 (非抽样, 兜底)
- 整章词级 diff (PDF p7-10 文本层 vs KB, 去列表符/标题#): 仅 3 处差异 — `study-\nspecific` 折行合并 (排版), `+has` (T-1, ch01:85), MANY 分句 LNKID↔LNKGRP 对调 (T-2, ch01:109). 其余逐序相等 → 无增无删.
- T-1 依据核: p49:27 "Controlled Terminology has not yet been developed" (PDF 自身平行短语); T-2 依据核: p31:7 "--LNKGRP … used to identify a group of records". 两处均已在 writer checkpoint 记录 PDF 原文 + 依据, t1_lane_notes:88 列入 T4 汇总.

### §1.4.1 层级 (4 级, 7 列) vs p9/p10 渲染 (110dpi), seeded 10 项
| KB 行 | 内容 | KB 级 | PDF 渲染 | 结果 |
|---|---|---|---|---|
| 75 | no domain prefix | L2 | o | 一致 |
| 76 | "--" placeholder | L2 | o | 一致 |
| 81 | Controlled Terms, Codelist, or Format | L1 | • | 一致 |
| 83 | As noted in the table note, asterisk | L3 | ▪ | 一致 |
| 84 | inherently sponsor-defined | L4 | • (p10 顶) | 一致 |
| 88 | Codelist | L2 | o | 一致 |
| 89 | hyperlinked codelist name in parentheses | L3 | ▪ | 一致 |
| 93 | Role | L1 | • | 一致 |
| 95 | description of what the variable means | L2 | o | 一致 |
| 96 | how this variable relates to another | L2 | o | 一致 |
- L1 共 7 项 (Variable Name / Variable Label / Type / CT,Codelist,Format / Role / CDISC Notes / Core) = PDF 7 列; 最深 L4 (:84-86) = PDF 第 4 级 •. 缩进 2 空格递增, 渲染为嵌套列表.

### batch notes 4 原子 + 隔离 fp
```
git archive HEAD knowledge_base → $S/iso_head; 同份 + 仅换现 ch01 → $S/iso_new (diff -rq 仅 ch01)
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --kb-root $S/iso_head/knowledge_base --scope all --out $S/fp_head.jsonl
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --kb-root $S/iso_new/knowledge_base --scope all --out $S/fp_new.jsonl --baseline $S/fp_head.jsonl --regress-out $S/fp_regress.jsonl
→ regressions=0 new_hits=63 RESULT: GREEN
fp_new: ig34_p0009_a009 / a020 / a021, ig34_p0010_a004 → hit_target = knowledge_base/chapters/ch01_introduction.md (4/4)
p7-10 ig34 原子 99 条 norm(verbatim) ∈ norm(ch01) 直查 → 不命中 4: p7_a001 (H1 "1 Introduction" 结构行), p9_a024 (atom 缺逗号), p10_a002 (T-1), p10_a023 (T-2) = 预期
```

### D-1..D-10 删除核
- 全章 PDF→KB 词级 diff 无 PDF 侧缺词 (仅上述 3 处) → 被删的旧表/改写段 (D-1..D-10) 中所有 PDF 支持信息均由现逐字原文承载. D-4 (`### Related Implementation Guides` + 表, PDF 无此标题) 3 条信息在 ch01:66-68; D-8 原表 Core 行的 "(Required)/(Expected)/(Permissible)" 展开为 KB 自写, PDF 无 → 删除不丢 PDF 内容. 结论: 无 PDF 支持内容丢失.

### G-TB8
- trace.jsonl T2.B-ch01: executor a1 (03:20:45) → code-reviewer PASS (03:25:18) → executor 续 (03:26:40, T-1/T-2) → code-reviewer 续 签字 PASS (03:27:50) — reviewer 签字晚于 writer 最后改动. `agent: main` 写 KB 记录 0.
- 现 ch01 md5 `e7c39a7a…` = writer 续 checkpoint 记录值 → 签字后无再改动.

### 观察 (非阻断)
- batch pdf_pages=[9,10] 使主样本总体 P 不含 p7/p8; 本次用补抽 8 覆盖 §1.1-§1.3. 建议后续全量重写批 pdf_pages 取 pdf_ranges 全页.
- T-1/T-2 keep-correct 依据为 PDF 自身旁证, 须进 T4 用户知悉清单 (已在 t1_lane_notes:88).
