# T2S S-CH8 writer checkpoint (扫描批: chapters/ch08_relationships.md, §8 p427-440)

## attempt 1 (2026-11-26, oh-my-claudecode:executor / opus)

- base HEAD `669405f` (S-SPREL 已提交); ch08 改前 = HEAD (`git status` 干净, md5 `154743c22e466e03124bdd18a7b34b95` = B-ch08 终态) → 改后 md5 `0334def914a5992c1fcd987268535e6a` (464→475 行). **仅版式改动, 文字零增删** (改前/改后全文去非字母数字后逐字相等, 命令见验证).
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/d6800696-3318-4d1d-9806-05c60470220c/scratchpad/t2s_S-CH8_writer/` (ch08_base.md = `git show HEAD:`; scan.py / strict.py / pagelog.py / speccmp_ch.py / qtab.py / apply.py; bb_429/432/436/437/438/439.html = `pdftotext -bbox`; p427-p440 110dpi 渲染; census_before/after.json; kbA/kbB + fpA/fpB.jsonl).
- 历史: `t2_B-ch08.md` (+review/audit PASS) 的 T-1~T-8 继续有效; T-9 (RELSUB asm 7 句号, B-REL 命名) 同样适用于 ch08:373.
- D2/D7 归属 (已读 `t2_B-REL.md` / `t2_B-SUPPQUAL.md` / `t2_S-SPREL.md` 全文): §8.2/§8.3 (RELREC)、§8.4 (SUPPQUAL)、§8.7 (RELSUB)、§8.8 (RELSPEC) 按 **D7 两边都留、都按 PDF 逐字**, ch08 不去重、不改交叉引用; 三批结论 "ch08 与域文件无内容冲突" (B-REL 范围外 #3, B-SUPPQUAL 末段), 本批全扫复核同. 未动任何 domains/ 文件.

### 完整节页范围 (O20 复核)
| 单元 | 节 | json lo-hi | 复核结果 | 依据 |
|---|---|---|---|---|
| chapters/ch08_relationships.md | §8 (含 §8 章引言 + §8.1-§8.8) | 427-441 | **427-440** | p427 首行 `8 Representing Relationships and Data` (章引言首段 + 8 bullet + IDVAR 段 + 3 bullet 全在 p427, 主控已裁归 ch08); p440 relspec.xpt Row 6 为 §8 末; p441 首行 `9 Study References` → p441 无 §8 内容 (同 B-ch08 / S-SPREL 复核) |

### 双向全扫 — 逐页日志
方法: PDF→KB = 该页 layout 文本按句/bullet 切分, 去非字母数字后在 ch08 全文查 (`pagelog.py`, 计数为改后); KB→PDF = ch08 每行按句/表格单元切分, 引号/破折号/空白归一但**保留标点**后查 p427-440 layout 拼接文本 (`strict.py`) + 去非字母数字版 (`scan.py`); spec 表 = `speccmp_ch.py` (bbox 词框按表头 x 分列, 逐变量 Label/Type/CT/Role/Notes/Core + 变量顺序; 变异测试: 改 IDVARVAL Notes 1 词 + QLABEL Role → 2 处均报); §8.6.3 Question 表 = `qtab.py` (bbox 左右两列分拼, 去 `o` 子项符; 变异测试: 删 "and interventions" + "FT," → 均报); 例表 = `table_census.py` + 渲染. 渲染实际打开: p428 / p429 / p432 / p433 / p436 / p437 / p438 / p439 / p440 (110dpi); p427 / p430 / p431 / p434 / p435 未打开 (纯叙述 + census OK 例表, 以 layout 文本为准; B-ch08 reviewer 已渲染 p431).

| 页 | 节 | PDF→KB: 句/列表/表行 数, 命中, 缺→已补 | KB→PDF: 对应 KB 段, 无出处行→处理 | 表 (逐格/census) | 备注 |
|---|---|---|---|---|---|
| 427 | §8 章引言 / IDVAR 段 | 27 / 25 / 0 | ch08:5-22; 无出处: :1 H1、:3 Source 行、:5 `## Overview` (导航) | 无表 | 未命中 2 = 章标题与首段拼接 (KB H1 等价)、"DIZOGOTIC" (T-1 keep-correct). 章引言首段 + 8 bullet 与 KB :7-16 逐句一致 (strict.py 带标点通过) |
| 428 | §8.1 / §8.1.1 | 18 / 15 / 0 | ch08:26-59 一致 | cm.xpt census OK (12×12) + 渲染 | 未命中 3 = "GMGRPID" ×2 (T-2) + Rows 10-12 句与 "cm.xpt" 表头拼接; "This example illustrates how CMGRPID…" PDF 独立段, KB 并入 :34 (S-FND 口径: 仅分段, 不改) |
| 429 | §8.2 / §8.2.1 RELREC Desc + Spec | 32 / 21 / 0 | ch08:63-96 一致 | **census item ch08:86** RELREC spec 7 变量 speccmp 全 OK + 渲染逐格 (下表) | 未命中 11 = spec 表 layout 串列 + 脚注 "1In" (上标 1) |
| 430 | §8.2.2 Ex1-3 / §8.3 | 10 / 10 / 0 | ch08:98-154 一致 | relrec Ex1/2/3 census OK | "COMBO 1" vs 表 "COMBO1" = PDF 自相矛盾, 照录 (B-ch08 已登记) |
| 431 | §8.3.1 / §8.4 首 | 25 / 25 / 0 | ch08:156-189 一致 | relrec census OK | PDF "Example 1" 独立行 → KB :158 改独立标签 (变更 #1) |
| 432 | §8.4 续 / §8.4.1 spec | 38 / 23 / 0 | ch08:189-212 一致 | **census item ch08:197→199** SUPP-- spec 10 变量 speccmp 全 OK + 渲染逐格 | 未命中 15 = spec 表 layout 串列 + 脚注 "1 In" |
| 433 | §8.4.1 尾 / §8.4.2 / §8.4.3 Ex1 / Ex2 叙述 | 26 / 24 / 0 | ch08:214-241 一致 | suppae census OK | 未命中 2 = "llustrate" (T-4) 与标题拼接、Ex1 末句与 "suppae.xpt" 表头拼接; "SQAPFAMH." 缺右括号 (T-3); Ex2 PDF 标签 "Example" 无编号 (T-5); Ex1 标签改独立行 (#2) |
| 434 | §8.4.3 suppqs / §8.4.4 / §8.5 | 25 / 25 / 0 | ch08:243-280 一致 | suppqs census OK | |
| 435 | §8.5 尾 / §8.6 / §8.6.1 / §8.6.2 | 30 / 30 / 0 | ch08:280-304 一致 | 无表 | :294 "medical events — including … them — may" 破折号两侧空格 (PDF 无空格, 见需主控定 #1) |
| 436 | §8.6.2 尾 / §8.6.3 / Question 表 行1-4 | 36 / 31 / 0 | ch08:304-328 一致 | **census item ch08:319→323** Question 表 qtab.py 左右列 True/True + 渲染逐格 (下表) | 未命中 5 = Question 表两列 layout 串行; "represent as an event" 照录 (T-8 T4); "may also be coded)." 多余右括号 (T-6 keep-correct) |
| 437 | Question 表 行4 续-6 / §8.6.3 尾 / §8.7 RELSUB Desc | 29 / 25 / 0 | ch08:328-349 一致 | 同上 | 未命中 4 = Question 表两列串行 |
| 438 | RELSUB Spec / spec / Assumptions | 36 / 30 / 0 | ch08:351-374 一致 | **census item ch08:351→355** RELSUB spec 5 变量 speccmp 全 OK + 渲染逐格 | 未命中 6 = spec 串列 + 脚注; asm 7 句末 PDF 无句号, KB 有 (T-9 keep-correct) |
| 439 | RELSUB Examples / §8.8 框注 / RELSPEC Desc + Spec | 21 / 15 / 0 | ch08:376-438 一致 | dm / relsub census OK; **census item ch08:420→429** RELSPEC spec: speccmp 5/5 OK, STUDYID bbox 漏读 → 渲染 p439 核一致 | 未命中 6 = spec 串列 + 脚注; Example 1 标签改独立行 (#3); Row 标签行间补空行 (#5/#6, PDF 各自独立行) |
| 440 | RELSPEC Assumptions / Examples / 图 / relspec | 10 / 9 / 0 | ch08:440-475 一致; 无出处: :454 D6 KB note + Mermaid (既有, 复核不矛盾) | relspec census OK | 未命中 1 = 图题与图后句拼接; "is does not" 照录 (T-7 T4); Example 1 标签改独立行 (#4); Mermaid vs 渲染: SPC-001→A/B, B→B-1, SPC-003→003-A, 类型/层级一致 |

合计: PDF→KB 叙述/列表/表行缺口 0 (已补 0); 全部未命中 = 表格 layout 串列 (由 speccmp/qtab/census + 渲染覆盖)、标题/表名拼接、脚注上标 "1"、已登记 PDF_TYPO. KB→PDF (`strict.py` 带标点, 改后输出全量): 无出处仅 :1 H1、:3 Source 行、`xx.xpt:` 表前标签、`^1^` 脚注前缀、:15 DIZYGOTIC (T-1)、:40 CMGRPID (T-2)、:224 "SQAPFAMH)." (T-3)、:228 "illustrate" (T-4)、:241 "Example 2:" (T-5)、:373 句末句号 (T-9)、:454-462 D6 note + Mermaid. 无自造句, 无未登记差异.

### census_items 逐格 (渲染 110dpi + bbox; 行号 HEAD→改后)
| 表 | 页 | 逐行结果 |
|---|---|---|
| RELREC spec ch08:86 (未移位) + 脚注 :96 | p429 | STUDYID / RDOMAIN (DOMAIN) / USUBJID Exp / IDVAR `*` Req / IDVARVAL Exp / RELTYPE (RELTYPE) Record Qualifier Exp / RELID Record Qualifier Req: 7 行 × 7 列一致; 脚注文字一致 |
| SUPP-- spec ch08:197→199 + 脚注 :212 | p432 | STUDYID…QEVAL 10 行 × 7 列一致 (IDVAR `*` Exp; QNAM `*` Topic Req; QLABEL Synonym Qualifier; QVAL Result Qualifier; QORIG Record Qualifier Req; QEVAL (EVAL) Record Qualifier Exp) |
| Question 表 ch08:319→323 | p436-437 | 6 行 × 2 列一致: 行1 2 bullet; 行2 2 bullet + 1 子项 (PDF `o` → KB `◦`); 行3 3 bullet; 行4 2 bullet (第 2 条在 p437 续页, 归属正确); 行5 2 bullet; 行6 3 bullet (URL 一致). 差异仅 T-6 (KB 去 "coded)" 多余括号) |
| RELSUB spec ch08:351→355 + 脚注 :363 | p438 | STUDYID Req / USUBJID Exp / POOLID Perm / RSUBJID Req / SREL "Subject Relationship" (RELSUB) Record Qualifier Req: 5 行 × 7 列一致 |
| RELSPEC spec ch08:420→429 + 脚注 :438 | p439 | STUDYID Req (渲染) / USUBJID Req / REFID Req / SPEC (SPECTYPE)(GENSMP) Variable Qualifier Perm / PARENT Identifier Exp / LEVEL Num Variable Qualifier Req: 6 行 × 7 列一致 |
- table_census.py (manifest = ch08 × p427-440): before = after `KB 表 15: OK 10 / UNPARSEABLE 5, cells 442, diffs 0`; PDF_ONLY 落在 p427-440 的 0 张 (从 census json `pdf_only[].pages` 过滤, 非 tail 摘要); pdf_unparsed 无本批页.

### 变更清单 (行号 = 改后)
| # | kb_file:line | ref | action | before → after 摘要 | PDF 页 |
|---|---|---|---|---|---|
| 1 | ch08:158-160 | pdf:p431:§8.3.1 "Example 1" 标签 | REPLACED (版式) | 行内 `**Example 1:** This example…` → 独立行 `**Example 1**` + 空行 + 原段 (同文件 :100/:119/:133 先例; PDF 独立行) | 431 |
| 2 | ch08:230-232 | pdf:p433:§8.4.3 Ex1 标签 | REPLACED (版式) | 同上 | 433 |
| 3 | ch08:378-380 | pdf:p439:RELSUB Ex1 标签 | REPLACED (版式) | `Example 1: The following data…` → `**Example 1**` + 空行 + 原段 | 439 |
| 4 | ch08:448-450 | pdf:p440:RELSPEC Ex1 标签 | REPLACED (版式) | `Example 1: This example uses…` → 同上 | 440 |
| 5 | ch08:384-386 | pdf:p439:Row 1 / Rows 2-3 | INSERTED (空行) | 两标签行间补空行 (原相邻行在 Markdown 渲染时合并为一段; PDF 为两行) | 439 |
| 6 | ch08:398-402 | pdf:p439:Rows 1-2 / 3,5 / 4,6 | INSERTED (空行) | 三标签行间补 2 个空行 (同上) | 439 |
| 7 | ch08:86/199/323/355/429 | census items ×5 | VERIFIED | 逐格一致 (见上表), 未改 | 429/432/436-437/438/439 |
| 8 | ch08:241 | pdf:p433:§8.4.3 Ex2 标签 | VERIFIED (保留行内) | 曾改独立行 `**Example 2**`, census 因 PDF 标签无编号 (T-5) 把 suppqs 配到 Ex1 → KB ex=2 失配成 NO_PDF / PDF_ONLY+1; 已撤回, 保留原行内 `**Example 2:**` (见需主控定 #2) | 433 |
- 文字改动 0 (改前/改后全文去非字母数字逐字相等); 实改 6 处版式. 新增 atom 0.

### 结构改动清单
无 (无标题增删改、无整段挪位; #1-#6 仅标签行拆行 / 空行).

### 删除清单
无内容删除. (#1-#4 删去的仅为 KB 自加的标签冒号 ":" — 导航标签格式.)

### D6 标注清单
无新增. 既有 1 处: ch08:454 Mermaid KB note (复核与 p440 图一致, 不矛盾). KB 自写导航保留不标: :1 H1、:3 Source 行、:5 `## Overview` (PDF 章标题后无小标题)、`xx.xpt:` 标签、`**Rows n-m:**` / `**Example n**` 标签、`### RELSUB/RELSPEC — …` (em dash, 文件惯例; 规则 6 不动).

### PDF_TYPO 清单
无新增; 沿用 (复核成立): T-1 p427 DIZOGOTIC→KB DIZYGOTIC (:15); T-2 p428 GMGRPID ×2→CMGRPID (:36/:40); T-3 p433 SQAPFAMH 缺 ")" →KB 补 (:224); T-4 p433 llustrate→illustrate (:228); T-5 p433 "Example" 无编号→KB "Example 2" (:241); T-6 p436 "coded)."→"coded." (:328); T-7 p440 "is does not" 照录 + T4 (:443); T-8 p436 "represent as an event" 照录 + T4 (:321); T-9 p438 asm 7 句末句号 KB 补 (:373). PDF 自相矛盾照录: p430 "COMBO 1" vs 表 COMBO1; p440 图 "(Brain)" vs relspec Row 5 TISSUE.

### 范围外发现
无 KB 错. (domains/RELREC/RELSUB/RELSPEC/SUPPQUAL 与 ch08 同节文字已由 B-REL / B-SUPPQUAL / S-SPREL 修对, 本批对照未见冲突.)

### 需主控定
1. **破折号两侧空格** (U1 之外): ch08:241 "questionnaires — Brief … (ADAS-Cog) — for"、:294 "medical events — including … them — may": PDF 为无空格 em dash ("questionnaires—Brief", "events—including"). S-TYPO 若只做字符替换不会去空格; 是否由 S-TYPO 一并去空格 (SUPPQUAL/examples.md 同句同问题, B-SUPPQUAL 已提). 本批未改.
2. **§8.4.3 Example 2 标签**: 为与 :100/:119/:133/:158/:230 统一应改独立行 `**Example 2**`, 但 census 会因 PDF T-5 失配 (实测 OK 10→9, NO_PDF 1, PDF_ONLY +1). 现保留行内; 若主控接受 census 侧豁免, 可再改.
3. (观察, 不改) 4 张 spec 表表头 "Controlled Terms, Codelist or Format" 缺 PDF 上标 ¹; 脚注用 `^1^` (GFM 不渲染为上标; domains 的 U2 格式为 `> ¹…`) — 均为 B-ch08 已审格式, 若需全库统一请归 S-TYPO / 格式批. RELREC 用粗体标签、RELSUB/RELSPEC 用 `###` 标题 (预存, 规则 6 不动).

### 验证 (repo 根; S = 上述 scratch; 输出未截断)
```
python3 -I -c "import re;n=lambda s:re.sub(r'[^a-z0-9]','',s.lower());print(n(open('$S/ch08_base.md').read())==n(open('knowledge_base/chapters/ch08_relationships.md').read()))"   → True
python3 -I $S/strict.py knowledge_base/chapters/ch08_relationships.md      # KB→PDF 带标点; 残留见上 "合计"
python3 -I $S/pagelog.py knowledge_base/chapters/ch08_relationships.md     # 逐页 PDF→KB 计数 (日志表)
K=knowledge_base/chapters/ch08_relationships.md; python3 -I $S/speccmp_ch.py $S X 429 $K 86; python3 -I $S/speccmp_ch.py $S X 432 $K 199; python3 -I $S/speccmp_ch.py $S X 438 $K 355; python3 -I $S/speccmp_ch.py $S X 439 $K 429   → 7/10/5/5 OK (p439 STUDYID bbox 漏读, 渲染核)
python3 -I $S/qtab.py $S knowledge_base/chapters/ch08_relationships.md   → left eq True / right eq True
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json   → OK 10 / UNPARSEABLE 5, diffs 0 (RESULT RED 仅因全局 PDF_ONLY 329, p427-440 内 0)
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --kb-root $S/kbA --out $S/fpA.jsonl   (kbA = 当前工作区 knowledge_base 副本 + ch08_base)
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --kb-root $S/kbB --out $S/fpB.jsonl --baseline $S/fpA.jsonl --regress-out $S/fp_regress.jsonl   → regressions=0 new_hits=0 GREEN
grep -rnoE 'ch08_relationships(\.md)?#[A-Za-z0-9_-]+' --exclude-dir={archive,releases,node_modules,.git} . | wc -l   → 0
python3 tools/check_links.py 2>&1 | grep "live docs"   → broken relative links: 18668 (live docs: 42)
```

### git diff --stat
```
 knowledge_base/chapters/ch08_relationships.md | 19 +++++++++++++++----
 1 file changed, 15 insertions(+), 4 deletions(-)
```
- writer.jsonl: `work/t2_batches/S-CH8.writer.jsonl`.

### 更正 (同 attempt, 自查后追加; 与上文冲突处以本段为准)
- **新增变更 #9 (破折号空格)**: 覆盖矩阵 (`MATRIX_TAG=S-CH8`) 显示 §8.6.1 原子 ig34_p0435_a018 = NONE, 成因即上文需主控定 #1 的 " — " 两侧空格 (S-TYPO 只换字符, 不会去空格, 缺口永不闭合). 已按 PDF 修: ch08:241 "questionnaires—Brief" / "(ADAS-Cog)—for" (p433), ch08:294 "medical events—including" / "treat them—may be" (p435); 字符本为 U+2014, 仅删两侧空格. 改后矩阵 §8.6.1 = 18/0/0, fp new_hits 3. **需主控定 #1 撤回** (改为已修); SUPPQUAL/examples.md 同句同问题属已提交域文件, 本批不改 (登记供 S-TYPO / 主控).
- **改后 md5 = `b093dd3e029e566d66dfac63ec89dce4`** (475 行; 上文 `0334def9…` 作废). `git diff --stat`: 1 file, +17/−6. 实改合计 **8 处** (版式 6 + 破折号空格 2 行/4 处); 文字 (字母数字) 零增删, 命令同验证块第 1 条 → True.
- **验证块已在终版上全量重跑** (上文验证块写于 Example 2 撤回前, spec 行号以本段为准): `strict.py` 全量输出存 `$S/strict_final.txt` (29 行, 全部为上文 "合计" 所列导航/脚注前缀/T-n/D6, 无其他); `speccmp_ch.py` 429:86 / 432:199 / 438:355 / 439:429 → 7 / 10 / 5 / 5 OK; `qtab.py` → True / True; `table_census.py` → OK 10 / UNPARSEABLE 5, diffs 0; fp_match (kbB 重建为终版) → regressions=0 new_hits=3 GREEN; check_links → live docs 42.
- **变异测试命令** (原文称实测, 补命令): `sed -e '92s/would be entered/would be put/' -e '205s/Synonym Qualifier/Record Qualifier/' $S/ch08_base.md > $S/mut.md; python3 -I $S/speccmp_ch.py $S X 429 $S/mut.md 86; python3 -I $S/speccmp_ch.py $S X 432 $S/mut.md 197` → IDVARVAL notes / QLABEL role 两处 DIFF; `sed -e '322s/past events and interventions/past events/' -e '326s/(QS, FT, or RS)/(QS or RS)/' <改后 Example 1 拆行前副本> > $S/mut.md; python3 -I $S/qtab.py $S $S/mut.md` → right eq False, 两处 delete 均报. (行号为当时文件; 复跑需按内容定位.)
- **Example 2 census 实验命令**: 将 ch08:241 改为 `**Example 2**` + 空行 + 原段后跑 `python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json` → `OK 9 / UNPARSEABLE 5 / NO_PDF 1, PDF_ONLY 330` (suppqs KB ex=2 vs PDF ex=1, 因 T-5); 撤回后恢复 OK 10 / PDF_ONLY 329.
- **qtab.py 局限**: 只比小写字母数字, Question 表的标点/大小写以 p436/p437 渲染目视为准 (逐格表已列; 差异仅 T-6 与引号样式).
- **版式改动与 S-FND 口径**: S-FND 裁定 "仅段落拆分/合并不同 → 不改", 故 p428 段落合并未动; #1-#4 依据是本文件 B-ch08 续 #3 先例 (:100 Example 1 改独立行, reviewer PASS) 的同文件统一, #5/#6 是 Markdown 渲染问题 (相邻标签行会被合并成一段, 与 PDF 逐行版面不符), 不属分段口径.
- **删除清单补行**: | D-1 | ch08:158/:230/:378/:448 (改前 :158/:228/:374/:439) | 标签冒号 ":" ×4 (KB 自加, PDF 标签无冒号) | 版式, 标签改独立行 | — | ; | D-2 | ch08:241/:294 em dash 两侧空格 ×4 | PDF 无空格 | — |.
- **D2/D7 依据措辞更正**: 已读 `t2_B-REL.md` 与 `t2_B-SUPPQUAL.md` 全文 (`t2_S-SPREL.md` 全文); "三批结论" 更正为 **两批**: B-REL 范围外 #3 ("ch08 差异: 无内容冲突") 与 B-SUPPQUAL 末段 ("ch08 §8.4 对 PDF: 内容一致, 仅排版差"). S-SPREL 只扫域文件, 未对 ch08 下结论.
- **覆盖矩阵** (输出 `work/scratch/t2/global/t2_coverage_matrix.S-CH8.md`, 全量 grep 未截断): ch08 宿主的 §8 / §8.1 / §8.1.1 / §8.3 / §8.4.1-§8.4.4 / §8.5 / §8.6.1-§8.6.3 全为 `ch08:F/in`; §8 18/1/0 (PARTIAL = a011 T-1 DIZOGOTIC)、§8.1.1 6/2/0 (T-2 ×2)、§8.4.3 0/1/0 (T-4 llustrate)、§8.4.4 1/4/0 与 §8.6.3 15/8/0 (原子带 "•" 前缀的 PARTIAL, 文本已逐句核一致). §8.2.1 / §8.2.2 / §8.3.1 / §8.6 行 0 原子 (域宿主或无正文原子), 非缺口. 另 §6.3.7.1 行列出 `ch08:96 F/out`: 原子 ig34_p0286_a014 是通用 CT 星号脚注 (NV 通用规格表), 与 ch08:96 RELREC 表脚注 (p429) 同文, 属文本巧合命中, 非 ch08 承载 §6.3.7.1 内容 (ch08 不改).
- trace 行 note 写于 #9 之前 ("6 layout-only edits"), 未追加第二行; 实际改动以本段为准 (8 处).
