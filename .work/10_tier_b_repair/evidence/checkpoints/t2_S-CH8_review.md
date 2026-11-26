# T2S S-CH8 reviewer checkpoint

## attempt 1 (2026-11-26, oh-my-claudecode:code-reviewer / opus)

**Verdict: PASS** (无 CRITICAL/HIGH/MEDIUM; 5 条 LOW 观察, 均归 S-TYPO 或主控已裁, 不阻断)

- 对象: `git diff HEAD -- knowledge_base/chapters/ch08_relationships.md` (numstat +17/−6; md5 `b093dd3e029e566d66dfac63ec89dce4` = writer 更正段). 工作树另有 ch04 / ch10 / model/02 改动 = S-CH4 / S-CH10 / S-MOD2 并行批, 不计. narrow_files 空; 未动 domains/.
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/d6800696-3318-4d1d-9806-05c60470220c/scratchpad/t2s_S-CH8_reviewer/` (自写 `rscan.py` p2k/k2p、`chk.py`; 未复用 writer 脚本). 渲染实际打开: p429 / p432 / p436 / p437 / p438 / p439 / p440 (110dpi).

### 命令与结果 (可复跑; S = 上述 scratch)
```
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest $S/manifest.json --out $S/census_after.json   # exit 1 (仅全局 PDF_ONLY 329); KB 表 15: OK 10 / UNPARSEABLE 5; cells 442; diffs 0; pdf_only 落 p427-440 = 0; pdf_unparsed = p274/p342 非本批
git show HEAD:knowledge_base/chapters/ch08_relationships.md > $S/ch08_base.md   # kbA = 当前 KB 副本 + ch08 HEAD; kbB = 当前 KB 副本
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --kb-root $S/kbA --out $S/fpA.jsonl
python3 -I .work/10_tier_b_repair/scripts/fp_match.py --kb-root $S/kbB --out $S/fpB.jsonl --baseline $S/fpA.jsonl --regress-out $S/fp_regress.jsonl   # regressions=0 new_hits=1 GREEN (exit 0)
python3 -I $S/rscan.py $S p2k knowledge_base/chapters/ch08_relationships.md   # PDF→KB: 540 句段, miss 99 (逐条定性见下)
python3 -I $S/rscan.py $S k2p knowledge_base/chapters/ch08_relationships.md   # KB→PDF: 905 句段/表格, miss 39 (逐条定性见下)
python3 -I -c "import re;n=lambda s:re.sub(r'[^A-Za-z0-9]','',s);print(n(open('$S/ch08_base.md').read())==n(open('knowledge_base/chapters/ch08_relationships.md').read()))"   # True (区分大小写)
# 非字母数字字符差: +8 '*' (RELSUB/RELSPEC Ex1 标签加粗) / −4 ':' (4 处标签冒号); 其余为空白 (空行 + em dash 两侧空格)
python3 tools/check_links.py 2>&1 | grep "live docs"   # broken relative links: 18668 (live docs: 42)
```
- **writer "字母数字层零增删" 独立证实**: 区分大小写字母数字序列相等; 标点差仅 +8 `*` −4 `:`; 与 writer 8 处 (版式 6 + 破折号空格 2 行) 完全对应.

### 页范围复核 (O20)
同意 p427-440: p426 末为 §7 TD 列表; p427 首行 "8 Representing Relationships and Data"; p440 末为 relspec.xpt Row 6; p441 首行 "9 Study References".

### 双向全扫 — 逐页 (reviewer 自己的计数; rscan: raw+layout, 去连字符折行, 去非字母数字后子串匹配)
| 页 | PDF→KB 句段 / miss | miss 定性 | 结论 |
|---|---|---|---|
| 427 | 28 / 2 | 章标题与首句拼段 (分拆核两者均命中); "TWIN, DIZOGOTIC" = T-1 | 一致; 章引言首段 + 8 bullet + IDVAR 段 + 3 bullet 全命中 |
| 428 | 26 / 7 | GMGRPID ×2 = T-2; "Again, … COMBO THPY 2 …" 与表头拼段 (单独核命中); 4 段 cm.xpt 列串 (census OK) | 一致 |
| 429 | 42 / 11 | RELREC spec 表列串 → 渲染逐格 (下) | 一致 |
| 430 | 31 / 18 | 3 张 relrec 表列串 (census OK); 2 句与表头拼段 (单独核命中) | 一致 |
| 431 | 32 / 0 | — | 一致 |
| 432 | 86 / 6 | SUPP-- spec 表列串 → 渲染逐格 | 一致 |
| 433 | 34 / 6 | §8.4.3 标题+"llustrate" (T-4); suppae 表列串 (census OK); "Example" 无编号 (T-5) | 一致 |
| 434 | 42 / 10 | suppqs 表列串 (census OK) | 一致 |
| 435 | 30 / 0 | — | 一致 (含 #9 两处 em dash 无空格, PDF L435:26-27) |
| 436 | 37 / 2 | Question 表两列串行 → 渲染逐格 | 一致 |
| 437 | 30 / 3 | 同上 | 一致 |
| 438 | 52 / 6 | RELSUB spec 列串 → 渲染逐格 | 一致 |
| 439 | 50 / 21 | dm/relsub 表列串 (census OK); RELSPEC spec 列串 → 渲染逐格; "Rows 2-3:" / "…to each other." 与表名拼段 (单独核命中) | 一致 |
| 440 | 20 / 7 | relspec 表列串 (census OK); 图后句与表名拼段 (单独核命中) | 一致 |
- **原子级补核** (`work/pdf_atoms.jsonl` p427-440 全部 392 原子, 去 `•`/`o` 前缀后字母数字子串查 ch08): SENTENCE 179/180、LIST_ITEM 52/55、NOTE 5/6、HEADING 38/38、CODE_LITERAL 13/13 命中; 未命中 = a011/a006/a008/a019 (T-1/T-2/T-2/T-4 keep-correct)、p440_a009 图 NOTE (Mermaid D6)、TABLE_ROW 40 + TABLE_HEADER 3 (原子串带 "Row n" 前缀/列串, 由 census OK + 渲染逐格覆盖).
- **KB→PDF miss 39 定性**: :1 H1 / :3 Source 行 (导航); :40 CMGRPID (T-2); :91-94 / :358-361 / :434-436 spec 表 Notes 格 (PDF 文本列串, 渲染逐格一致); :228 illustrate (T-4); :241 "Example 2:" 标签 (T-5, 主控裁定 a 保持行内); :325-330 Question 表格 (渲染一致); :454-461 D6 KB note + Mermaid. **无自造句、无扩写.**

### census_items 渲染逐格 (5 张 UNPARSEABLE)
| 表 (改后行号) | 页 | 逐格结果 |
|---|---|---|
| RELREC spec :86-94 + 脚注 :96 | p429 | 7 行 × 7 列一致: STUDYID Req; RDOMAIN (DOMAIN) Req; USUBJID Exp; IDVAR `*` Req (Notes "Examples: --SEQ, --GRPID."); IDVARVAL Exp ("value of --SEQ would be entered here", PDF 折行 "--"); RELTYPE (RELTYPE) Record Qualifier Exp (含 "as described in Section 8.3, Relating Datasets"); RELID Record Qualifier Req. 脚注文字一致 |
| SUPP-- spec :199-212 | p432 | 10 行 × 7 列一致: IDVAR `*` Exp; IDVARVAL Exp; QNAM `*` Topic Req; QLABEL Synonym Qualifier Req; QVAL Result Qualifier Req; QORIG Record Qualifier Req (含 "See Section 4.1.8, Origin Metadata."); QEVAL (EVAL) Record Qualifier Exp |
| Question 表 :323-330 | p436-437 | 6 行 × 2 列一致; 行 2 子项 PDF `o` → KB `◦`; 行 4 第 2 bullet 跨 p437 归属正确; 行 6 URL 一致; 仅差 T-6 ("coded)." 多余括号, keep-correct) |
| RELSUB spec :355-363 | p438 | 5 行 × 7 列一致: USUBJID Exp; POOLID Perm; RSUBJID "Related Subject or Pool Identifier" Req; SREL (RELSUB) Record Qualifier Req |
| RELSPEC spec :429-438 | p439 | 6 行 × 7 列一致: STUDYID / USUBJID / REFID Req; SPEC (SPECTYPE)(GENSMP) Variable Qualifier Perm; PARENT Identifier Exp; LEVEL Num Variable Qualifier Req |

### 覆盖矩阵 §8.x PARTIAL 逐条定性 (`work/scratch/t2/global/t2_coverage_matrix.S-CH8.json`)
| 原子 | 节 | KB 行 | 判定 |
|---|---|---|---|
| ig34_p0427_a011 | §8 | :15 | 假阳: 仅 DIZOGOTIC→DIZYGOTIC (T-1, PDF relsub 表自证) |
| ig34_p0428_a006 / a008 | §8.1.1 | :36 / :40 | 假阳: GMGRPID→CMGRPID (T-2) |
| ig34_p0433_a017 | §8.4.2 | :224 | 假阳: 字母数字全句命中, 差 ")" (T-3) |
| ig34_p0433_a019 | §8.4.3 | :228 | 假阳: llustrate→illustrate (T-4) |
| ig34_p0434_a010-a013 (4) | §8.4.4 | :258-261 | 假阳: 原子带 "•      " 前缀; 去前缀后各自在所在行字母数字全句命中 (in_line=True) |
| ig34_p0436_a010-a015 (6) + p0437_a011-a012 (2) | §8.6.3 | :314-319 / :338-339 | 假阳: 同上 bullet 前缀; 8 条均 in_line=True |
- **R2 缺短语 0 条**; 无 CONDITIONAL 修正项.

### D7 / 结构 / 删除 / D6 签字
- D7: §8.2/§8.3 (RELREC)、§8.4 (SUPPQUAL)、§8.7 (RELSUB)、§8.8 (RELSPEC) 两边保留; 12 个域文件顶部 `> Source text: SDTMIG v3.4 §8.x (also in chapters/ch08_relationships.md)` 均在 (grep 全量). ch08 侧本批全扫逐字一致, 依据成立.
- 变更 #1-#4 (Example 1 标签独立行): PDF p431:2 / p433:30 / p439:2 / p440:9 均为独立行 "Example 1" — 签字. #5/#6 (Row 标签行间空行): PDF p439:6-7 / :15-17 各自独立行 — 签字. #9 (em dash 去空格): PDF L433:46-47 "questionnaires—" "(ADAS-Cog)—for", L435:26-27 "events—including" "them—may" — 签字.
- 删除清单 D-1 (标签冒号 ×4)、D-2 (dash 空格 ×4): 均为 KB 版式, PDF 无 — 签字. 结构改动无 (标题/锚点未变; 入站 `ch08_relationships.md#` 锚点链接 0).
- D6: :454 Mermaid KB note 既有; 对 p440 渲染: SPC-001→001-A/001-B, 001-B→001-B-1 (DNA), SPC-003 (Brain)→003-A (RNA), Level 1/2/3 一致, 不矛盾 — 签字.

### 问题表 (LOW, 不阻断)
| ref | 检查项 | 问题 | 处理 |
|---|---|---|---|
| ch08:241 | 排版字符 | PDF "Assessment Scale–Cognitive" (en dash), KB 连字符 | U1 → S-TYPO |
| ch08:191 | 排版字符 | PDF "STUDYID…QNAM" 省略号, KB "..." | U1 → S-TYPO |
| ch08 4 张 spec 表头 / 脚注 | 格式 | 表头缺上标 ¹; 脚注 `^1^` | 主控裁定 (b) → S-TYPO (O59) |
| ch08:241/:294 | 范围 | #9 dash 去空格在裁定 (b) "本批不扩" 之前已做; 结果与 PDF 一致, 不要求回退. SUPPQUAL/examples.md 同句仍带空格 | 留 S-TYPO (O59) 统一 |
| ch08:241 | 版式 | Example 2 仍为行内标签 (PDF T-5 无编号) | 主控裁定 (a), 不改 |

### Positive
- writer 更正段自承 trace note 过时与 "三批→两批" 措辞更正, 证据可复跑; 变异测试与 census 实验均附命令.
