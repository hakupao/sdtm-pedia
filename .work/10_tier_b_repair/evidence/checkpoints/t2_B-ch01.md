# T2 B-ch01 writer checkpoint

## attempt 1 (2026-11-26, oh-my-claudecode:executor / opus)

- base HEAD: `fb62af2fa96e830e90bc5dae9b6e232f99ae1379`
- md5 ch01 before `ea035b1480368746ca32c7b0b5eeba67` → after `9464e10913f83fa0e1a9e3a6aed5e819`
- kb_files: 仅 `knowledge_base/chapters/ch01_introduction.md`. scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/7fe38595-6d99-4b86-881d-0dfb0d270167/scratchpad/t2_Bch01_writer/` (ch01_before.md, p-007..010.png 90dpi, fp_before_all/fp_after_all.jsonl, rev.py)
- 真值: chapter 1 = SDTMIG p7-p10 (p11 起 §2, 已核 `ig34_p0011.txt` 首行 "2 Fundamentals of the SDTM"). p8/p9/p10 渲染逐项目视 (列表层级、逗号、em-dash).
- 编辑方式 (仿 B-ch02 先例): 全章按 PDF 顺序逐字重写. 先补 PDF 原文, 再按 D2 删去被逐字覆盖的旧改写 / KB 摘要表. 3 张 KB 表 (§1.2 :15、Related IG :53、§1.4.1 :80; 均为 census unparseable) 是 PDF 列表的 KB 摘要 → 按规则 3 "跟 PDF 走" 改为 PDF 列表结构.
- 标题: `##`/`###` 文字层级全部不变, 唯一变化 = 删除 KB 自写 `### Related Implementation Guides` (PDF 无此标题; 全仓 grep `related-implementation-guides` 0 入链).
- 排版: 合并折行 (`study-\nspecific`, `controlled-\nterminology`, `-\n-LNKID`); p9 Type 项双空格归一为单空格; 直引号照 PDF 文本层; Core 项 em-dash 照录.

### 变更清单 (行号 = 改后)

| # | kb_file:line | ref | action | before → after 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 1 | ch01:109 | ig34_p0010_a025 | REPLACED | 截短的 "will be clarified in a future release" → PDF 原句全文 (含 other identification variables / examples reviewed) | 10 |
| 2 | ch01:58 | ig34_p0009_a003 | REPLACED | 第4条改写 → 逐字, 补 "See the implementation examples for each domain …" | 9 |
| 3 | ch01:59 | ig34_p0009_a004 | REPLACED | 第5条 → 逐字, 补 "to understand the fundamentals … typical protocols" | 9 |
| 4 | ch01:60 | ig34_p0009_a005 | REPLACED | 第6条 → 逐字, 补 "to learn advanced concepts …" | 9 |
| 5 | ch01:61 | ig34_p0009_a006 | REPLACED | 第7条 → 逐字, 补 "to learn about occasions …" | 9 |
| 6 | ch01:80 | ig34_p0009_a023 | TABLE_REBUILT | Type 行 → PDF bullet, 补 "These values are taken directly from the SDTM." | 9 |
| 7 | ch01:83 | ig34_p0009_a026 | TABLE_REBUILT | 补 "As noted in the table note" (R2) | 9 |
| 8 | ch01:97 | ig34_p0010_a014 | TABLE_REBUILT | CDISC Notes "population rules" → PDF 子项 "Rules for when or how …" | 10 |
| 9 | ch01:99 | ig34_p0010_a016 | TABLE_REBUILT | Core 行 → PDF 原文, 补 "explained further in Section 4.1.5, SDTM Core Designations" | 10 |
| 10 | ch01:109 | ig34_p0010_a023 | REPLACED | 2 条箭头 bullet → PDF 原句 (补 "when setting up a relationship in RELREC") | 10 |
| R | ch01:92 | t2_recheck ig34_p0010_a009 | TABLE_REBUILT (副作用) | §1.4.1 重建后 "Format:" 子项逐字存在; recheck 判定归 reviewer, writer 不声明 | 10 |

atoms 覆盖率: 10/10 (表中 #1-#10).

### batch notes 必补项

| ref | 改后位置 | 状态 |
|---|---|---|
| p7 §1.2 引导句 + 10 条章节 bullet (a010-a020) | ch01:15-26 | INSERTED, 表删 (D-1) |
| p9 guides 句 a008 (补 "and should be consulted when needed") + a009 URL 句 + 3 bullet a010-a012 | ch01:64-68 | INSERTED |
| p9-10 §1.4.1 全部 7 列层级 (Variable Name / Label / Type / Controlled Terms, Codelist, or Format > Controlled Terms > asterisk > 3 子项, external code system; Codelist 3 项; Format / Role / CDISC Notes 4 项 / Core) | ch01:74-99 | TABLE_REBUILT, 层级对 p9/p10 渲染 |
| ig34_p0009_a009 / a020 / a021, ig34_p0010_a004 | :64 / :77 / :78 / :87 | 现 hit_target = ch01 |

### 其它恢复 (R3 新增, 不在 atoms)
- §1.1 :9 补 "(SDTM, available at https://www.cdisc.org/standards/foundational/sdtm)" (p7 a006, URL 丢失).
- §1.3 恢复 PDF 顺序: 引导句 → 14 bullet → "A detailed list …" → Version 3.1 段; 14 条 bullet 全部补回 "See Section …" 交叉引用 + 被压缩的措辞 (p8 a001-a014, 如 "in preparation for its eventual retirement", "(i.e., …)", "for these domains").
- §1.4 "Recommended reading order:" (KB 自写标签) → PDF 句 "The following guidelines may be helpful in reading this document:" (p8 a023); 第1/2/8条补 "First," / "Next, … of this document … to regulatory authorities" / "Finally,".
- §1.4.1 引导句补 "for a domain" (p9 a014); Variable Name 两子项 (a018/a019); Codelist 3 项全逐字 (a006-a008); Role 全句 (a010); CDISC Notes 4 子项 (a011-a015).
- §1.5 DRVFL 段补 "of the SDTMIG and/or Model document" (p10 a020); LNKID 首句补 "that" / "the definition of" (a022); a024 补 "in this version of" / "between --LNKID and --LNKGRP".
- 页码行 :3 Pages 7-12 → 7-10.
- fp 新命中 hit_target=ch01 共 65: p7 a006 a010-a020 / p8 a001-a014 a023 a024 / p9 a001-a011 a014 a018-a021 a023 a026 / p10 a001 a002 a004 a006-a016 a020 a022-a025.

### 删除清单 (D2)

| # | 原 ch01 行 (base) | 内容 | 原因 | 保留 / 替代位置 |
|---|---|---|---|---|
| D-1 | :15-26 | §1.2 三列摘要表 (Section/Title/Description, 10 行) | KB 摘要, 被 p7 10 bullet 逐字覆盖 | ch01:15-26 |
| D-2 | :30 后半 + :32 | §1.3 改写段 (顺序被调换) | 原句逐字移回 PDF 顺序, 无内容删除 | ch01:30, :47, :49 |
| D-3 | :34-49 | 14 条压缩 bullet | 被 p8 逐字 bullet 覆盖 | ch01:30-45 |
| D-4 | :51-57 | `### Related Implementation Guides` + 3 行表 | KB 自写标题/表, 放错节 (§1.3 下), 内容与 p9 guides bullet 重复; 0 入链 | ch01:64-68 |
| D-5 | :63-72 | "Recommended reading order:" + 8 条改写 | 被 p8-9 逐字 8 条覆盖 | ch01:53-62 |
| D-6 | :74 | guides 改写段 ("See the SDTMIG for Associated Persons …") | 被 p9 a008 + 3 bullet 逐字覆盖 | ch01:64-68 |
| D-7 | :78 | §1.4.1 引导段 (缺 "for a domain") | 原地换成 PDF 原文 | ch01:72 |
| D-8 | :80-88 | §1.4.1 Column/Description 表 (7 行) | KB 摘要表, 被 PDF 嵌套列表逐字覆盖; triage kb_loc :84-88 映射原子 (p9 a023 a026, p10 a001-a016) 改后全部 hit_target=ch01 (a002 照录 PDF) | ch01:74-99 |
| D-9 | :94 | DRVFL 段 (截短) | 原地换成 PDF 全句 | ch01:105 |
| D-10 | :98-102 | LNKID 改写段 + 2 条箭头 bullet + 截短末句 | 被 p10 a022-a025 原文段覆盖 | ch01:109 |

删除前核: triage_merged.json 中 kb_loc 指向 ch01 的 22 条原子改后全部 hit_target=ch01 (仅 a024 atom 自身缺逗号除外, 不在 kb_loc 映射中).

### PDF_TYPO / 待主控 (T4)
- **T-1** (p10 a002): PDF 渲染为 "for which a codelist not yet been developed" (缺 "has"). 无法由 PDF 自身确定正确词 → 照录 PDF (原 KB 写 "has not yet been"), 登记 T4. 照录使 a002 fp 命中.
- **T-2** (p10 a023): PDF 中 RELTYPE = ONE 与 = MANY 两分句都写 "--LNKID (and not --LNKGRP)", 疑 MANY 应为 --LNKGRP. 渲染确认 PDF 即如此 → 照录, 登记 T4 (原 KB 箭头 bullet 同样两行皆 --LNKID).
- atom 误差 (非 KB 问题): ig34_p0009_a024 verbatim "Controlled Terms, Codelist or Format" 缺逗号; 渲染与文本层均为 "Codelist, or Format" → KB 按渲染, 该 atom fp 预期不命中 (SKIPPED_ATOM_ERR 仅指 atom 本身).

### 触碰过的 unparseable 表 (reviewer 须人工)
- ch01:15 (base) §1.2 表 → 已转 PDF bullet 列表.
- ch01:53 (base) Related IG 表 → 删除 (D-4).
- ch01:80 (base) §1.4.1 表 → 已转 PDF 嵌套列表 (3-4 级), 层级须对 p9/p10 渲染核.

### 范围外发现
- 无 KB 他文件改动. ch02:7 交叉引用 (`[Chapter 1](ch01_introduction.md)`) 所列 §1.2/§1.4/§1.4.1 现在 ch01 均完整承载, 链接仍有效.

### 验证 (命令可复跑, repo 根; S = 上述 scratch)
```
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --scope all --out $S/fp_before_all.jsonl     # 改前, live KB
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --scope all --out $S/fp_after_all.jsonl --baseline $S/fp_before_all.jsonl --regress-out $S/fp_regress.jsonl
  → regressions=0 new_hits=65 RESULT: GREEN; p7-10 全部原子 hit_target=ch01, 唯一例外 ig34_p0009_a024 (atom 缺逗号)
python3 -I $S/rev.py knowledge_base/chapters/ch01_introduction.md   # KB 每句 (去标题/Source 行) 按 norm ∈ norm_pdf(p7..p10)
  → reverse misses 0
diff <(grep '^#' $S/ch01_before.md) <(grep '^#' knowledge_base/chapters/ch01_introduction.md)
  → 仅 "< ### Related Implementation Guides"
python3 tools/check_links.py | grep 'live docs'   → broken relative links: 18668 (live docs: 42) = 基线
git diff --stat -- knowledge_base/chapters/ch01_introduction.md   → 1 file changed, 75 insertions(+), 68 deletions(-)
```
注: fp 前后两次均跑在 live KB 上 (工作树含其它批未提交改动, 两次之间仅 ch01 变化); reviewer 宜用隔离副本复核.

## attempt 1 续 (主控改判 T-1/T-2, reviewer 旁证)

- md5 ch01 → `e7c39a7ae829e3abe67a7e49808c584e`. 仅改 ch01:85 与 ch01:109 各一处.
- **T-1 → keep-correct**: ch01:85 "a codelist not yet been developed" → "a codelist has not yet been developed". 依据: PDF 自身 p49 (RELMIDS) 同一短语为 "has not yet been developed"; 缺词处唯一合语法补法.
- **T-2 → keep-correct**: ch01:109 MANY 分句 "IDVAR of --LNKID (and not --LNKGRP)" → "IDVAR of --LNKGRP (and not --LNKID)". 依据: 同段前句 (p10) LNKGRP "used to identify a group of records" + p31 §4 定义 (--LNKGRP 识别一组记录, many-to-one); ONE↔LNKID / MANY↔LNKGRP 对称, 只换一个变量名则括号自相矛盾, 故唯一自洽改法是两变量名对调. 注: a023 曾为 T1.4 用户维持 REAL_GAP 的原子 ("in RELREC" 已补, 未受影响).
- 因改正不再命中 (预期): ig34_p0010_a002, ig34_p0010_a023 (+ 原有 ig34_p0009_a024 atom 缺逗号).
- 复验 (隔离副本; kbA = 现 KB 但 ch01 换回 base, kbB = 现 KB):
```
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --scope all --kb-root $S/kbA --out $S/fpA.jsonl
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --scope all --kb-root $S/kbB --out $S/fpB.jsonl --baseline $S/fpA.jsonl --regress-out $S/fp_regB.jsonl
  → regressions=0 new_hits=63 RESULT: GREEN; p7-10 不命中 ch01 = p9_a024, p10_a002, p10_a023
python3 tools/check_links.py | grep 'live docs'  → 18668 (live docs: 42)
```
