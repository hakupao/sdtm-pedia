# T2 B-ch08 reviewer

## attempt 1 (2026-11-26, oh-my-claudecode:code-reviewer / opus)

**verdict: CONDITIONAL** (1 项修正: T-8 须照录 PDF; 其余全部通过)

- 范围: `knowledge_base/chapters/ch08_relationships.md` (md5 `756f95e1a1eee42498f1359a44402a28` = writer 报告改后值), `git diff bdb54fe -- knowledge_base/chapters/ch08_relationships.md` (+89/−88). 工作区其他 KB 改动属他批, 未审.
- 真值: `work/pdf_pages/ig34_p0427..0441.txt` + `pdftotext -raw/-layout` + 渲染 p431/p436/p437/p440 (`pdftoppm -r 110`, `source/cdisc/SDTMIG v3.4 (no header footer).pdf`, 页码偏移 0 已核: p427 首行 = "8 Representing Relationships and Data").
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/7fe38595-6d99-4b86-881d-0dfb0d270167/scratchpad/t2_B-ch08_reviewer/` (bin/scan.py 反向, bin/fwdline.py 正向; 均为独立实现, 未用 writer 脚本)

### 命令与结果 (可复跑; S = 上述 scratch)
```
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json
  → KB tables 15; {'OK': 10, 'UNPARSEABLE': 5}; cells 442; diffs 0; exit 1 仅因全局 PDF_ONLY 329 (p427-440 内 0 条), pdf_unparsed 仅 p274/p342 (非本批)
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --out $S/fp_after.jsonl --baseline .work/10_tier_b_repair/work/fp_baseline.jsonl --regress-out $S/fp_regress.jsonl
  → regressions=44 RESULT RED; 44 条页码全在 p118/215/218/254-263/363-364/396 (他批 MS/FA/CP/TA 工作区改动), p427-440 及 ch08 目标 0 条
  → p427-440 原子 83: hit_any 80 (baseline 69); atoms[] a010/a018/a019 hit_target = ch08 ✓
python3 -I $S/bin/fwdline.py $S/bin   # PDF p427-440 每行 (raw) norm 后 ⊂ KB
  → ok 692 miss 12: 全部可归类 (章标题 1, T-2 ×2 行, T-3, T-4, T-6, T-8, 表头上标 "Format1" ×2, 脚注 "1In" ×2, T-7)
python3 -I $S/bin/scan.py              # KB 每句 / 每表格单元 ⊂ PDF p427-440 (raw+layout)
  → 38 条未命中: 全部为 导航 (文件标题/Source/"xx.xpt:"/"**Example n:**"/"Example 1:"), 脚注 "^1^ In", T-1/T-2/T-3/T-4/T-5/T-6/T-7/T-8, D6 note + Mermaid 代码行; 无自造词句
python3 tools/check_links.py | grep 'live docs' → broken relative links: 18668 (live docs: 42) ≤ 42 ✓
grep -rnoE 'ch08_relationships(\.md)?#[A-Za-z0-9_-]+' --exclude-dir={archive,releases,node_modules,.git} . | wc -l → 0 (标题改名无断链)
```

### 问题表
| ref | 检查项 | 问题 | 证据 |
|---|---|---|---|
| ch08:315 / ig34_p0436_a016 (T-8) | PDF_TYPO 取舍规则 | **FIX**: writer 自认 "无法由 PDF 他处确定" 却保留 KB 改写 "represent an event". PDF 内两种读法都有先例 ("data probably represent a finding" p436 / "may be represented as a finding" p436), 不唯一 → 规则要求照录 | p436: "help determine whether the data represent as an event or a finding" |
| ch08:432 (T-7) | PDF_TYPO | 接受 (LOW): "is"→"it" 单字母拼写级, 同 T-4 "llustrate" 先例; 若主控要求与 T-8 同口径严格, 也可改照录+T4 | p440: "therefore is does not require" |
| ch08:100/156/226 vs 117/131 | 一致性 | LOW (不阻断): Ex2/Ex3 改为独立 "**Example 2**" 行, Ex1 仍为行内 "**Example 1:**"; 均为导航标签 | p430 "Example 1" / "Example 2" 均独立行 |
| ch08:78/82 vs 339/345 | 一致性 | LOW (预存, 非本批改动): RELREC 用粗体标签, RELSUB/RELSPEC 用 ### 标题 | — |

### 修正清单 (writer attempt 2)
1. ch08:315 "whether the data represent an event or a finding" → 照录 PDF "whether the data represent as an event or a finding"; checkpoint T-8 改为 "照录 PDF, T4 用户裁定项" (不再列入 "KB 写正确值" 表).
   delta 仅此一行; 回 reviewer 复审 delta 即可 (无需重跑全扫, 需重跑 fp ch08 回归 = 0).

### 核查清单 (逐项结论)
- (1) atoms 3/3 REAL_GAP (a010 ch08:14, a018 :20, a019 :21) 逐句 = PDF p427 ✓. R3 44 条恢复: fwdline 正向逐行全命中 (除登记 PDF_TYPO) ✓. 5 处标题恢复 = PDF: §8.1 "…Using the --GRPID Variable" (p428), §8.3 "Relating Datasets" (p430), §8.4.3 "SUPP-- Examples" (p433), §8.6 全称 (p435), RELSUB/RELSPEC "— Specification/Assumptions/Examples" (p438-440; PDF 用 en dash, KB em dash 同 RELREC 先例) ✓. "### Key Rules" = KB 自写伪标题, 删除正确; 4 段还原为 PDF p433 段落 (含 "the key variables") ✓. §8.4.2 重复段: PDF p433 §8.4.2 以 "…dataset name SQAPFAMH." 结束, 无 "See Section 4.5.3" 段; 该段仅在 §8.4.1 后 (p433 顶) 出现一次 → 删除正确, ch08:214 保留 ✓. "**Note:**" 标签删除 (p439 无标签) ✓. 粗体: p431 渲染 NO/IS 粗体, "ONE and ONE." 非粗体 ✓; "attributions" 非粗体 ✓.
- (2) 表格 (人工逐格, 见下表) ✓. Question 表 `<br>` + •/◦: **接受** — 保留 PDF 一级/二级 bullet 层次 (p436 "Data collected at an initial visit" 为缩进 ◦ 子项), "; " 会丢层次; GFM 单元格内 `<br>` 可渲染.
- (3) T-1 (p439 relsub Row 4/6 + CT) / T-2 (表头 CMGRPID) / T-3 (句内开括号) / T-4 (拼写) / T-5 (Example 1 后连续编号) / T-6 (无对应开括号) ✓; T-7 接受 (见问题表); **T-8 不合规 → FIX**. PDF 自相矛盾照录: "COMBO 1" (p430 正文) vs "COMBO1" (表 Row 2) ✓; 图 SPC-003 "(Brain)" vs relspec Row 5 "TISSUE" ✓ (均不可由 PDF 确定). RELSUB assumption 7 PDF 无句号, KB 加句号 (同列表其余项均有句号, 可确定) ✓.
- (4) Source 行 427-440: p440 = §8.8 RELSPEC 例表结束, p441 首行 "9 Study References" ✓.
- (5) D6 note 位于 Mermaid 上方, 前缀 `> KB note (not in SDTMIG):`, 含 "KB rendering of the PDF figure" ✓. Mermaid vs p440 图: SPC-001→A, SPC-001→B, B→B-1, SPC-003→003-A; 类型 Tissue/Tissue/Tissue/DNA/Brain/RNA; 层级 1/2/2/3/1/2 = 图行标题 ✓. RELSUB Description/Overview (p437) 在 Specification (p438) 之前, 2 段逐句 = PDF ✓; relsub.xpt 首句 = p438 ✓.
- (6) 全扫双向 (含表格原子) 完成, 见命令段; 除 T-8 外无缺失、无自造.
- (7) fp ch08 回归 0; census 0 diff; check_links 42.

### 人工逐格表 (渲染 / layout 对照)
| KB 表 (改后行) | PDF | 结果 |
|---|---|---|
| cm.xpt ch08:46-59 (12×12) | p428 | 全格一致; CMDECOD Row1-12 = Generic Med A…L (Row 9 "Generic Med I") |
| RELREC spec ch08:86-94 (7×7) + 脚注 :96 | p429 | 一致 (未触碰) |
| SUPP-- spec ch08:195-206 (10×7) + 脚注 :208 | p432 | 一致 (未触碰) |
| Question 表 ch08:317-324 (6 行×2) | p436-437 渲染 | 一致: 行1 2 bullet; 行2 2 bullet + 1 ◦; 行3 3 bullet; 行4 2 bullet (第 2 条为 p437 续页, 归属正确), 仅 T-6; 行5 2 bullet; 行6 3 bullet (URL 一致) |
| RELSUB spec ch08:349-355 (5×7) + 脚注 :357 | p438 | 一致: label "Subject Relationship"、CT "(RELSUB)"、Role/Notes/Core 逐格 = PDF |
| RELSPEC spec ch08:418-425 (6×7) + 脚注 :427 | p439 | 一致; SPEC CT "(SPECTYPE)(GENSMP)" |
| relrec Ex1/2/3, relrec 8.3.1, suppae, suppqs, dm, relsub, relspec 例表 | p430-440 | census OK (10 张) + fwdline 行级命中 |

### R2 recheck
`t2_recheck[]` 为空 — 无.

### G-TB6 结构行签字
Source 行 (页码改 427-440, 已核 p441 = §9) ✓; 标题 ×9 (8.1 / 8.3 / 8.4.3 / 8.6 / RELSUB Description/Overview (新增) / RELSUB Specification / Assumptions / Examples / RELSPEC Specification / Assumptions / Examples 中改名者) ✓; RELSUB 表头+分隔线 (7 列 = PDF) ✓; "**Example 2**" "**Example 3**" 标签行 ✓; 3 处脚注 `^1^` 行 (PDF 上标 1) ✓; D6 note 行 ✓; 删除 "### Key Rules" ✓.

### attempt 1 补充 (同一 reviewer, 交付前补证; 以本节为准, 覆盖上文冲突处)
**补渲染**: `pdftoppm -f N -l N -r 110` p428/p429/p432/p438/p439 (另有 p431/p436/p437/p440), 逐页 Read 图核对. 上文 "人工逐格表" 改为以下逐行结论 (每行 = KB 行 vs 渲染同行全部 7 列):

| KB 行 | PDF 渲染 | 结论 |
|---|---|---|
| cm.xpt :48-59 Row 1-12 | p428 | 12 行 × 12 列一致; CMDECOD A-H, "Generic Med I" (Row 9 单行), J-L |
| RELREC spec :88 STUDYID / :89 RDOMAIN (DOMAIN) / :90 USUBJID / :91 IDVAR * / :92 IDVARVAL / :93 RELTYPE (RELTYPE) Record Qualifier / :94 RELID Record Qualifier | p429 | 7 行逐格一致 (Type/CT/Role/Notes/Core) |
| SUPP-- spec :197-206 (STUDYID…QEVAL; QNAM * Topic; QLABEL Synonym Qualifier; QVAL Result Qualifier; QORIG/QEVAL Record Qualifier; QEVAL (EVAL) Exp) | p432 | 10 行逐格一致 |
| Question 表 :319-324 | p436/p437 | 见上文 (一致, 仅 T-6) |
| RELSUB spec :351 STUDYID Req / :352 USUBJID Exp / :353 POOLID Perm / :354 RSUBJID Req / :355 SREL "Subject Relationship" (RELSUB) Record Qualifier Req | p438 | 5 行 × 7 列一致 (表头 7 列 = PDF) |
| RELSPEC spec :420-425 (REFID Req; SPEC (SPECTYPE)(GENSMP) Variable Qualifier Perm; PARENT Exp; LEVEL Num Variable Qualifier Req) | p439 | 6 行逐格一致 |
| 3 脚注 :96/:208/:357/:427 | p429/p432/p438/p439 | 文字一致 (上标 1 → `^1^`) |
格式: p432 "attributions" 非粗体 ✓; p439 RELSPEC 框注无 "Note:" 标签 ✓; p439 "Row 1:" 等为粗体标签 ✓.
另 (LOW, 预存, 非本批改动): p428 "This example illustrates how CMGRPID…" 在 PDF 为独立段, KB :34 并入前段 (仅分段).

**T-8 证据** (不截断): `for f in ig34_p04{27..40}.txt; do tr '\n' ' ' < $f | grep -oE '.{30}(represent(s|ed)? (as )?(an|a) (event|finding)).{20}'; done` →
p435 "whether an observation represents an event, an intervention, or a finding"; p436 "data represent as an event or a finding"; p436 "represented as a finding about the event"; p436 "data probably represent a finding".
p435/p436 "represent a finding" 支持删 "as", 但 p436 "represented as a finding" 同样支持 "are represented as an event" → 两种修法均有 PDF 内先例, **不唯一确定** → 照录 + T4 (维持 FIX).

**T-7 改判**: "therefore is does not" 也有两种修法 (is→it / 删 "is"), 与 T-8 同型, PDF 内无证据定一 → **一并改为照录 + T4** (撤回上文 "接受").

**fp 回归措辞更正**: 44 条回归页码均非 ch08 页 (p118/215/218/254-264/363-364/396), 不归因具体他批; ch08 (p427-440) 回归 0.
**结构行计数更正**: 标题签字为 11 处 (8.1 / 8.3 / 8.4.3 / 8.6 / RELSUB Description/Overview (新增) / RELSUB Specification / Assumptions / Examples / RELSPEC Specification / Assumptions / Examples).

**最终修正清单 (writer attempt 2)**:
1. ch08:315 "whether the data represent an event or a finding" → "whether the data represent as an event or a finding" (照录 p436); checkpoint T-8 移出 "KB 写正确值" 表, 标 "照录 + T4".
2. ch08:432 "therefore it does not require" → "therefore is does not require" (照录 p440); checkpoint T-7 同上处理.
delta 仅 2 行; 回 reviewer 复审 delta + fp ch08 回归 = 0 即可.
**verdict 维持 CONDITIONAL.**

## 续 签字 (delta 复审, 2026-11-26, oh-my-claudecode:code-reviewer)
**verdict: PASS**. ch08 md5 `154743c22e466e03124bdd18a7b34b95`. 对比本人 attempt 1 保存的 diff (`$S/diff.txt` vs `$S/diff2.txt`, 只比 +/- 行): 实质变化仅 3 处, 其余为 diff 对齐噪声.
- :317 "whether the data represent as an event or a finding" = p436 原文 ✓ (T-8 照录 + T4)
- :434 "therefore is does not require" = p440 原文 ✓ (T-7 照录 + T4)
- :100 "**Example 1**" 独立标签行 + 原段文字不变 = p430 版面 ✓ (与 Ex2/Ex3 一致)
- fwdline.py 重跑: ok 694 / miss 10 (T-7/T-8 两行已命中, 余为已登记项); fp_match: 全局 regressions=48 RED, p427-440/ch08 回归 0; check_links live docs 42 ✓
