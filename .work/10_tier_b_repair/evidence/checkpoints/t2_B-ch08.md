# T2 B-ch08 writer checkpoint

## attempt 1 (2026-11-26, oh-my-claudecode:executor / opus)

- batch: `B-ch08` (kb_files = `knowledge_base/chapters/ch08_relationships.md` only; **no ch03 in this batch → lane C ch03 Keys / CO–CODTC / O5 not handled here**)
- base HEAD: `bdb54fe1b9cf2c30872eaae5786197be676a3652`
- md5 ch08 before `d85ed592f46e302ae2fe129318820fbb` → after `756f95e1a1eee42498f1359a44402a28`; `git diff --stat`: 1 file, +89/−88
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/7fe38595-6d99-4b86-881d-0dfb0d270167/scratchpad/t2_B-ch08_writer/` (ch08_before.md, p427-p440 90dpi renders, fwd.py / rev.py / order.py / spec_cells.py / qtab.py, kbA/kbB, fpA/fpB, census_before/after.json)
- 真值: `work/pdf_pages/ig34_p0427-0440` + bbox + renders. Batch pdf_ranges = p427-440 (§8 ends p440; §9 starts p441).

### 扫描方法 (全扫, 含表格类原子; 可复跑, S = scratch)
```
python3 -I $S/fwd.py <kb>        # forward: ALL pdf_atoms p427-440 (SENTENCE/LIST_ITEM/HEADING/NOTE/TABLE_ROW/TABLE_HEADER/CODE_LITERAL/FIGURE) norm-substring vs ch08
python3 -I $S/rev.py <kb>        # reverse: every ch08 prose sentence + every table cell (whole file) vs p427-440 layout text
python3 -I $S/order.py <kb>      # ordered word-level diff of ch08 prose vs p427-440 (catches order/dup/punctuation that substring scans miss)
python3 -I $S/spec_cells.py <kb> <kb_line> <page> <y0> <y1>   # column-aware cell compare from pdftotext -bbox (mutation-tested: 2 injected diffs both caught)
python3 -I $S/qtab.py <kb> $S 186                             # §8.6.3 Question table, 2-col bbox compare p436-437
```
fwd 计数 (`grep -c '^MISS' / '^WS'`): before MISS 98 / WS 4 → after MISS 53 / WS 2; MISS→hit 45, WS→hit 2, 新 MISS 0. 剩余全部可归类 (见「剩余未命中归类」).

### 变更清单 (行号 = 改后)
| # | kb_file:line | ref | action | before → after 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 1 | ch08:14 | ig34_p0427_a010 | REPLACED (R2) | §8.6 bullet "— the concept of related datasets and where to place additional data" → PDF full bullet (separate domain vs supplemental qualifier; modeling findings data …) | 427 |
| 2 | ch08:20 | ig34_p0427_a018 | REPLACED (R2) | --SEQ bullet: + "The variable --SEQ …" + "For example, if a subject has 25 adverse events … 25 unique AESEQ values …" | 427 |
| 3 | ch08:21 | ig34_p0427_a019 | REPLACED (R2) | --REFID bullet: + "such as an identifier provided in an electronic data transfer. Some examples are …"; "Values for --REFID are sponsor-defined and can be any alphanumeric strings …" | 427 |
| 4 | ch08:9-13,15-16 | 新增 atom p427_a005-a009, a011, a012 | REPLACED (R2) | 7 条 §8.x overview bullets: KB "— representing …" 改写 → PDF "…, describes …" 原文; 恢复丢失短语 "the demographics domain (DM) / general observation-class domain record (or records)", "(see also Section 5.1, Comments)", "such as a comment recorded in association with an adverse event", "For example:" | 427 |
| 5 | ch08:18 | 新增 p427 sentence order | MOVED (文件内) | "The specific set of identifiers … following sections." 从列表后 (旧:24) 移回 "The following are examples …" 之前 (PDF 顺序) | 427 |
| 6 | ch08:22 | 新增 ig34_p0427_a020 | INSERTED | "Section 8.1" 后补 ", Relating Groups of Records Within a Domain Using the --GRPID Variable" | 427 |
| 7 | ch08:26 | 新增 ig34_p0427_a021 | REPLACED (标题) | "Using --GRPID" → "Using the --GRPID Variable" (= PDF) | 428 |
| 8 | ch08:48-59 | census ch08:48 cm.xpt CMDECOD ×11 | REPLACED | "Generic Med" → "Generic Med A…H, J, K, L" (Row 9 本已为 "Generic Med I") | 428 |
| 9 | ch08:117-119 | 新增 ig34_p0430_a016/a017 | REPLACED (R2) | "Same scenario as Example 1, but in this case" → "Example 2 is the same scenario as Example 1. In this case, however, …"; 标签改独立行 "**Example 2**" | 430 |
| 10 | ch08:131-133 | 新增 ig34_p0430_a026/a027 | REPLACED (R2) | 同上 Example 3 ("Example 3 is the same scenario as Example 2. However, …") | 430 |
| 11 | ch08:148 | 标题 | REPLACED | "## 8.3 Relating Datasets Using RELREC" → "## 8.3 Relating Datasets" | 430 |
| 12 | ch08:185 | 格式 | REPLACED | "**attributions**" 去 KB 加粗 (PDF 非粗体, p432 渲染) | 432 |
| 13 | ch08:210-216 | 新增 ig34_p0433_a002/a005/a008 | REPLACED | 删 KB 自写小标题 "### Key Rules"; 4 条 bullet 还原为 PDF 4 段; 恢复 "the key variables" + 各段句末句号 | 433 |
| 14 | ch08:220 | 新增 ig34_p0433_a011/a015 | REPLACED | "SDTMIGv3.1" → "SDTMIG v3.1"; 去 KB 加粗 "**deprecated**"; 恢复 URL "https://www.cdisc.org/standards/foundational/sdtmig/" | 433 |
| 15 | 旧 ch08:219 | D2 去重 | DELETED | §8.4.2 末 "See Section 4.5.3, Text Strings …" 段是 §8.4.1 段 (ch08:214) 的复制, PDF §8.4.2 无 | 433 |
| 16 | ch08:222 | 新增 ig34_p0433_a018 | REPLACED (标题) | "### 8.4.3 Examples" → "### 8.4.3 SUPP-- Examples" | 433 |
| 17 | ch08:246 | 新增 ig34_p0434_a007 | REPLACED (R2) | "domain examples such as Section 5.2" → "domain examples, such as in Section 5.2" | 434 |
| 18 | ch08:253-255 | 新增 ig34_p0434_a011/a012/a013 | INSERTED | 3 条 bullet 补句末句号 (PDF 有; 第 1 条 PDF 无句号, 不动) | 434 |
| 19 | ch08:274 | 新增 ig34_p0434_a028 | INSERTED (R2) | 补 ", for example a comment that applies to a group of concomitant medications, perhaps taken as a combination therapy" | 434 |
| 20 | ch08:280 | 新增 ig34_p0435_a004 | REPLACED (标题) | "## 8.6 Where Data Belong" → "## 8.6 How to Determine Where Data Belong in SDTM-Compliant Data Tabulations" | 435 |
| 21 | ch08:294-298 | 格式 | REPLACED | §8.6.2 KB 把 3 段拆成 10 个单句段 → 恢复 PDF 3 段 (文字未改) | 435-436 |
| 22 | ch08:317-324 | 新增 ig34_p0436_a019-a023, p0437_a001-a003 | TABLE_REBUILT | Question 表 (UNPARSEABLE): 单元格改为 PDF 逐条 bullet (`• …<br>• …`, 子项 `◦`); 补缺失 bullet "A "No" answer is inconclusive. This does not rule out …" (p437 顶) | 436-437 |
| 23 | ch08:339-343 | 新增 ig34_p0437_a014-a018 | INSERTED | 新增 "### RELSUB — Description/Overview" + 1 句定义 + 1 段 (3 句) | 437 |
| 24 | ch08:345-357 | 新增 ig34_p0438_a001-a011 | TABLE_REBUILT | "### Specification" → "### RELSUB — Specification"; 补 relsub.xpt 首句; KB 4 列简表 → PDF 7 列 (含 CT/Role/CDISC Notes); SREL label "Subject Relationship to Related Subject/Pool" → "Subject Relationship"; 补脚注 ^1^ | 438 |
| 25 | ch08:359 | 新增 ig34_p0438_a012 | REPLACED (标题) | "### Assumptions" → "### RELSUB — Assumptions" | 438 |
| 26 | ch08:364 | 新增 ig34_p0438_a016 | REPLACED | "If the study" → "If a study" | 438 |
| 27 | ch08:367 | 新增 ig34_p0438_a019 | REPLACED | "2 directional representations" → "2 directional relationships" | 438 |
| 28 | ch08:370 | 新增 ig34_p0439_a001 | REPLACED (标题) | "### Example" → "### RELSUB — Examples" | 439 |
| 29 | ch08:408 | 格式 | REPLACED | 去 KB 标签 "**Note:**" (PDF 为无标签框注, p439 渲染); 引用块保留 | 439 |
| 30 | ch08:414 / 429 / 435 | 新增 ig34_p0439_a028, p0440_a001, a005 | REPLACED (标题) | "### Specification/Assumptions/Example" → "### RELSPEC — Specification / — Assumptions / — Examples" | 439-440 |
| 31 | ch08:427 | 新增 ig34_p0439_a039 | INSERTED | RELSPEC 规格表后补脚注 ^1^ (PDF 有, KB 缺) | 439 |
| 32 | ch08:441 | D6 / Mermaid | INSERTED | Mermaid 上方加 `> KB note (not in SDTMIG): … KB rendering of the PDF figure (Figure. Sample Specimen Relationship) …`; 图逻辑 = p440 图 (SPC-001→A,B; B→B-1; SPC-003→003-A; 节点类型/层级一致) | 440 |
| 34 | ch08:169-173 | 格式 (p431 渲染) | REPLACED | §8.3 三条编号项: 去 KB 加粗 "**ONE and ONE.**" 等标签 (PDF 非粗体); PDF 粗体 "NO" / "IS" 改为 **NO** / **IS** | 431 |
| 33 | ch08:3 | KB_AUTHORED 元数据 | REPLACED | "Source: … (Pages 427-446)" → "(Pages 427-440)" (§9 起于 p441, ch10 Source 写 444 起; 446 与 PDF 矛盾) | 427-441 |

atoms[] 覆盖: 3/3 (a010 #1, a018 #2, a019 #3), 均 REPLACED (R2: KB 改写行只承载本原子, 换成 PDF 全文 = 超集, fp 无回归).
census: DIFF 表 1 张 (ch08:48 cm.xpt, 11 格) 全部处理 (#8); pdf_only 0; pdf_unparsed 0.

### 新增 atom 清单 (R3; 由 fwd_before/fwd_after 机器生成: before 未命中 → after 命中, 去掉 atoms[] 的 a010/a018/a019)
ig34_p0427_a005 a006 a007 a008 a009 a012 a020 a021 / p0430_a016 a017 a026 a027 / p0432_a001 (WS) / p0433_a002 a005 a008 a011 (WS) a015 a018 / p0434_a007 a011 a012 a013 a028 / p0435_a004 / p0437_a014 a015 a016 a017 a018 / p0438_a001 a003 a004 a007 a008 a009 a010 a012 a016 a019 / p0439_a001 a028 / p0440_a001 a005 (共 44).
另有改动但原子仍不命中 (原子格式/PDF_TYPO, 见下): p0427_a011 (T-1), p0436_a020/a022 + p0437_a001 (Question 表, bbox 核一致), p0438_a005/a011 + p0439_a039 (脚注/表头上标).

### 删除 / 替换清单 (reviewer 逐条确认)
| 位置 (改前) | 删除/替换内容 | 原因 | 保留副本 |
|---|---|---|---|
| ch08:9-16 | 8 条 overview bullet 的 KB 改写 (含 "DM or a GOC domain record") | R2 + 补充口径 (旧改写只承载本 bullet 原子) → 换 PDF 原文 | — |
| ch08:20-22 | 3 条 IDVAR bullet 改写 | 同上 (a018/a019/a020) | — |
| ch08:24 | "The specific set of identifiers …" 段 | 移到 :18 (PDF 顺序), 非删除 | ch08:18 |
| ch08:119 / :131 | "Same scenario as Example n, but …" | 词替换型改写, 换 PDF 原句 | — |
| ch08:208 | "### Key Rules" 小标题 | KB 自写伪小标题, PDF 无 | — |
| ch08:219 | "See Section 4.5.3, Text Strings …" (§8.4.2 内) | D2 去重: 与 §8.4.1 段重复, PDF §8.4.2 无此段 | ch08:214 |
| ch08:354-360 | RELSUB 4 列 KB 简表 (含错 label "Subject Relationship to Related Subject/Pool") | 规则 3 表跟 PDF → 7 列重建 | ch08:347-355 |
| ch08:411 | "**Note:**" 标签 | PDF 无此标签 (ch04 L12 先例) | — |

### PDF_TYPO 清单 (KB 写正确值, 未照录)
| T | PDF 位置 | PDF 原文 | KB | 依据 |
|---|---|---|---|---|
| T-1 | p427 §8.7 bullet (a011) | "TWIN, DIZOGOTIC" | "TWIN, DIZYGOTIC" | 同 PDF p439 relsub.xpt Row 4/6 "TWIN, DIZYGOTIC" |
| T-2 | p428 Rows 1-3 / Rows 7-9 (a006/a008) | "GMGRPID" ×2 | "CMGRPID" | 同段其余处与表头均为 CMGRPID |
| T-3 | p433 §8.4.2 末句 (a017) | "SQAPFAMH." (括号未闭合) | "SQAPFAMH)." | 同句 "(e.g., resulting in …" 开括号 |
| T-4 | p433 §8.4.3 首句 (a019) | "llustrate" | "illustrate" | 拼写 |
| T-5 | p433 §8.4.3 第二例标签 | "Example" (无编号) | "**Example 2:**" | 前一例为 "Example 1", 例序 |
| T-6 | p436 Question 表 "Is verbatim…" 格 (a022) | "may also be coded)." (多余右括号) | "may also be coded." | 句中无对应开括号 |
| T-7 | p440 RELSPEC assumption 2 (a003) | "therefore is does not" | "therefore it does not" | 语法 (主语缺失) |
| T-8 | p436 §8.6.3 (a016) | "whether the data represent as an event or a finding" | "represent an event" (KB 原文, 未改) | 语法; 无法由 PDF 他处确定 → **T4 用户裁定项** (KB 保留无 "as") |

### PDF 内部不一致 (照录 PDF, 不改, 登记供 T4)
- p430 Example 3 文字 CMGRPID = "COMBO 1" vs 表 Row 2 IDVARVAL "COMBO1": KB 两处均照录.
- p440 图 SPC-003 标 "(Brain)" vs relspec.xpt Row 5 SPEC "TISSUE": KB Mermaid 照图, 表照表.
- p438 RELSUB assumption 7 末无句号 (KB 保留句号, 纯标点).

### KB_AUTHORED 保留 (纯导航, 不加 D6)
ch08:1 文件标题; ch08:3 Source 行 (已更正页码); ch08:5 "## Overview" (PDF 为 §8 首段无小标题); 各表前 "cm.xpt:" 等冒号; "**Rows n-m:**" / "**Example n:**" 粗体标签; "### RELSUB/RELSPEC — …" 用 em dash (同文件 RELREC 先例; PDF 为 en dash/hyphen 混用).

### 触碰 / 人工核过的 unparseable 表 (全部 5 张, reviewer 须对渲染逐格)
| 改后行 | 表 | 触碰 | 核法 | 结果 |
|---|---|---|---|---|
| ch08:86 | RELREC spec (p429) | 否 | spec_cells.py bbox 逐格 + p429 渲染 | 7×7 一致 |
| ch08:195 | SUPP-- spec (p432) | 否 | 同上 + p432 渲染 | 10×7 一致 |
| ch08:317 | §8.6.3 Question 表 (p436-437) | **是 (重建)** | qtab.py 2 列 bbox 顺序比 + p436/p437 渲染 | 一致 (仅 T-6) |
| ch08:349 | RELSUB spec (p438) | **是 (4→7 列重建)** | spec_cells.py + p438 渲染 | 5×7 一致 |
| ch08:418 | RELSPEC spec (p439) | 否 (表后补脚注) | spec_cells.py + p439 渲染 | 6×7 一致 |
spec_cells.py 变异测试: 改 RSUBJID 注释 1 词 + PARENT Role → 2 处均报 DIFF.

### 验证 (命令输出不截断)
```
fp_match --kb-root $S/kbA (base ch08) --out $S/fpA.jsonl
fp_match --kb-root $S/kbB (after)     --out $S/fpB.jsonl --baseline $S/fpA.jsonl --regress-out $S/fp_regress.jsonl
  → regressions=0 new_hits=12  RESULT: GREEN  (fp_regress.jsonl 0 行; kbA/kbB 均取自同一时刻工作区, 只差 ch08 — 先前一次 kbA 早于他批写入, 出现 TA p396 假回归, 已重建)
table_census --pages ig34:427-440 --kb $S/kbA/chapters/ch08_relationships.md → DIFF 1 (cm.xpt 11 格) RED
table_census --pages ig34:427-440 --kb $S/kbB/chapters/ch08_relationships.md → {'OK': 10, 'UNPARSEABLE': 5}; PDF_ONLY 0; cells 442; diffs 0  GREEN
python3 tools/check_links.py | grep 'live docs' → broken relative links: 18668 (live docs: 42) = 基线
grep -rnoE 'ch08_relationships(\.md)?#[A-Za-z0-9_-]+' --exclude-dir={archive,releases,node_modules,.git} . → 0 条 (标题改名无断链)
order.py (改后) → 非表格 prose 有序比对仅剩: KB 文件标题/Source/Overview (导航), T-1/T-2/T-4/T-7/T-8, "Example 2" 标签 (T-5), 脚注 "1 In" 版面位置
```

### 剩余 fwd 未命中归类 (改后)
- 原子格式假阴: p428_a012-a023 / p429_a023-a029 / p430_a009-a033 (原子带 "Row n |" 前缀或 "| |" 空格, spec 表 PDF 无 Row 列) — 表格已由 census / spec_cells 逐格核一致.
- 脚注 / 表头 "Format1" / "1In this column" (p429_a030, p432_a015/a026, p438_a005/a011, p439_a032/a039): 上标 1 版面; KB 用 `^1^` (同文件先例).
- p427_a001 章标题: KB 文件标题 "# SDTMIG v3.4 — Chapter 8: Representing Relationships and Data" 带 "Chapter 8:" 前缀, norm 后 "8:" 使子串不命中 (导航标题, 不改).
- PDF_TYPO: p427_a011 (T-1), p428_a006/a008 (T-2), p433_a017 (T-3), p433_a019 (T-4), p436_a016 (T-8), p440_a003 (T-7).
- Question 表原子 p436_a020/a022, p437_a001: 原子把 bullet "•" 与 "(continued)" 写进文本 / T-6; qtab.py bbox 比对一致.
- p440_a009 FIGURE 描述原子 (由 Mermaid + D6 承载).
- WS (仅空白/连字符差): p433_a034 / p435_a018 (KB 破折号两侧有空格). overview bullet 的 "**Section 8.x**" KB 粗体已去 (PDF 非粗体), 7 条转为精确命中.

### 格式说明
- Question 表单元格内多条 bullet 用 `• …<br>• …`、子项 `<br>◦ …`; KB 其他表格无 `<br>` 先例 (grep `knowledge_base` 表格行 `<br>` = 0, 仅 RELSPEC/examples.md Mermaid 用 `<br/>`), 属本批新格式, 请 reviewer 确认可接受 (备选: 单元格内 "; " 连接).
- §8.4.4 "should **not** be submitted" 粗体 = PDF (p434 渲染), 保留.

### 范围外发现 (未改, 交主控)
- **跨文件重复 (D2 候选)**: `knowledge_base/domains/RELREC/`, `RELSUB/`, `RELSPEC/` (各 spec/assumptions/examples.md) 与 `SUPPQUAL/` 承载 ch08 §8.2.1/§8.7/§8.8/§8.4.1 同一 PDF 内容 (例: RELSUB/spec.md:43 "Label: Subject Relationship", RELSPEC/examples.md Mermaid). 归属按 PDF 章节号为 ch08; 只有 B-SUPPQUAL 有批次, RELREC/RELSUB/RELSPEC 无批 → 主控决定是否去重 / 另开批.
- 已修缺陷的全库复查 (`grep -rnE 'Subject Relationship to Related Subject/Pool|\| Generic Med \||SDTMIGv3\.1|Relating Datasets Using RELREC|directional representations' knowledge_base --include='*.md'` → 0 条, 不截断).
- O5 / ch03 不属本批.

## attempt 1 续 (2026-11-26, reviewer CONDITIONAL 修正 + 用户 D7)
- delta (3 处; md5 756f95e1… → `154743c22e466e03124bdd18a7b34b95`; diff vs base +94/−91):
  1. ch08:317 "whether the data represent an event" → "represent as an event" (照录 p436). **T-8 改为: 照录 PDF + T4 用户裁定** (两种修法 PDF 内均有先例, 不唯一).
  2. ch08:434 "therefore it does not" → "therefore is does not" (照录 p440). **T-7 改为: 照录 PDF + T4 用户裁定** (is→it / 删 is 两解).
  3. LOW: ch08:100 §8.2.2 Example 1 标签改为独立行 "**Example 1**" (与 Ex2/Ex3 统一; p430 "Example 1" 为独立行).
- PDF_TYPO 表更正: T-7 / T-8 移出「KB 写正确值」, 归「照录 + T4」. 其余 T-1~T-6 不变.
- D7 (用户): domains/RELREC/RELSUB/RELSPEC/SUPPQUAL 与 ch08 两边都留, 由后续 B-REL / B-SUPPQUAL 批按本 ch08 修对; 本批不动. 上文「范围外发现」第 1 条据此关闭.
- 验证 (kbA2 = 当前工作区 + ch08_before, kbB2 = 当前工作区):
  `fp_match --kb-root $S/kbB2 --baseline $S/fpA2.jsonl` → regressions=0 new_hits=12 GREEN; fwd p436_a016 / p440_a003 现命中.
  `python3 tools/check_links.py | grep 'live docs'` → broken relative links: 18668 (live docs: 42) = 基线.
