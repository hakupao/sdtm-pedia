# T2S S-CH8 auditor checkpoint (Rule A)

## attempt 1 (2026-11-26, oh-my-claudecode:verifier / opus)

**Verdict: PASS** — 独有信息丢失 0, 忠实度错误 0 (N=30, seed 20261126).

- 对象: `git diff HEAD -- knowledge_base/chapters/ch08_relationships.md` (+17/−6): 4 处 Example 标签改独立行 (p431/p433/p439/p440), RELSUB 2 组 Row 标签间加空行 (p439), em dash 去空格 ×4 (:241 / :294, 与 PDF 一致). 文字信息无增删. 其他工作树改动 (ch04/ch10/model02) 属并行批, 不计.
- 先独立判 (样本 + 反扫 + 渲染) 后才读 `t2_S-CH8.md` / `t2_S-CH8_review.md`; 结论一致.
- scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/d6800696-3318-4d1d-9806-05c60470220c/scratchpad/t2s_S-CH8_auditor/` (`sample.py`, `rev.py`, p428/430/432/439/440 渲染 110dpi).

### 抽样 (可复跑: `python3 -I $S/sample.py`, 在 repo 根)
- P = `work/pdf_atoms.jsonl` 中 ig34, atom_type ∈ SENTENCE/LIST_ITEM/NOTE/CROSS_REF/TABLE_ROW, 页 427-440, parent_section 以 "§8" 开头或为 RELREC/RELSUB/RELSPEC 子标题 (§8.2.1/§8.7/§8.8 下属; p427-440 全属 §8, 无边界别节原子), 去 ledger INTENTIONAL_EXCLUDE (25) → |P| = 301. intros 无.
- C (writer 改动页 = writer.jsonl 中 action≠VERIFIED 的页 431/433/435/439/440) = 120.
- N = min(30, max(20, ceil(30.1)), 301) = 30; C 抽 ceil(N/3)=10, P−C 抽 20. `random.Random(20261126)`.

| # | atom_id | PDF 页 + 摘要 | KB ch08:line | 丢失? | 忠实? | 位置? | 说明 |
|---|---|---|---|---|---|---|---|
| 1 | ig34_p0431_a009 | p431 operational DB 可能分开或单一数据集 | :169 | 否 | 是 | §8.3.1 | 逐字 |
| 2 | ig34_p0431_a015 | p431 RELTYPE 允许值 ONE/MANY | :171 | 否 | 是 | §8.3.1 | 逐字 |
| 3 | ig34_p0433_a012 | p433 SUPP-- 命名 ("--" 源域) | :224 | 否 | 是 | §8.4.2 | 逐字 (引号排版归 S-TYPO) |
| 4 | ig34_p0433_a016 | p433 SUPPAPFAMH 过长 | :224 | 否 | 是 | §8.4.2 | 逐字 |
| 5 | ig34_p0435_a001 | p435 单条评论只能关联 1 域 | :280 | 否 | 是 | §8.5 | 逐字 |
| 6 | ig34_p0435_a007 | p435 判定 event/intervention/finding | :290 | 否 | 是 | §8.6.1 | 逐字 |
| 7 | ig34_p0435_a027 | p435 单一结构适用多类数据 | :302 | 否 | 是 | §8.6.2 | 逐字 |
| 8 | ig34_p0435_a029 | p435 urinalysis 归 LB, LBSPEC | :302 | 否 | 是 | §8.6.2 | 逐字 含 §6.3.5.6 引用 |
| 9 | ig34_p0435_a033 | p435 PC topic (跨页句) | :304 | 否 | 是 | §8.6.2 | 跨页续句完整 |
| 10 | ig34_p0440_a008 | p440 Figure 标题 | :452 | 否 | 是 | RELSPEC Ex | 逐字; 下方 Mermaid 有 D6, 对渲染图分支/层级一致 |
| 11 | ig34_p0428_a017 | p428 cm.xpt Row 6 (TABLE_ROW) | :53 | 否 | 是 | §8.1.1 | 渲染逐格 12/12 一致 |
| 12 | ig34_p0429_a010 | p429 --GRPID 作 IDVAR | :69 | 否 | 是 | §8.2 | 逐字 |
| 13 | ig34_p0429_a011 | p429 IDVARVAL 含义 | :69 | 否 | 是 | §8.2 | 逐字 |
| 14 | ig34_p0430_a010 | p430 RELREC Ex1 Row 2 (TABLE_ROW) | :113 | 否 | 是 | §8.2.2 | 渲染逐格 8/8 (RELTYPE 空) |
| 15 | ig34_p0431_a024 | p431 SDTM 不允许新增变量 | :185 | 否 | 是 | §8.4 | 逐字 |
| 16 | ig34_p0432_a003 | p432 多种 attribution | :189 | 否 | 是 | §8.4 | 逐字 |
| 17 | ig34_p0432_a009 | p432 2 评估者各用 QNAM | :191 | 否 | 是 | §8.4 | 逐字 |
| 18 | ig34_p0432_a016 | p432 SUPP-- spec STUDYID 行 (TABLE_ROW) | :201 | 否 | 是 | §8.4.1 | 渲染逐格 7/7 |
| 19 | ig34_p0433_a017 | p433 SUPP→SQ, SQAPFAMH | :224 | 否 | 是 | §8.4.2 | KB 补 ")" = 已登记 T-3 (括号配对) |
| 20 | ig34_p0434_a017 | p434 评论可关联主体/域/记录 | :267 | 否 | 是 | §8.5 | 逐字 |
| 21 | ig34_p0434_a021 | p434 RDOMAIN/IDVAR/IDVARVAL 填法引句 | :269 | 否 | 是 | §8.5 | 逐字 |
| 22 | ig34_p0435_a002 | p435 跨多域评论需重复 | :280 | 否 | 是 | §8.5 | 逐字 |
| 23 | ig34_p0435_a006 | p435 Section 2.6 引用 | :290 | 否 | 是 | §8.6.1 | 逐字 |
| 24 | ig34_p0435_a018 | p435 medical events 多方面 (em dash) | :294 | 否 | 是 | §8.6.1 | 逐字, dash 无空格同 PDF (本批改动) |
| 25 | ig34_p0435_a020 | p435 Findings 定义 | :296 | 否 | 是 | §8.6.1 | 逐字 |
| 26 | ig34_p0435_a025 | p435 单/多 topic 不清 | :300 | 否 | 是 | §8.6.2 | 逐字 |
| 27 | ig34_p0435_a026 | p435 IG 两种都有示例 | :300 | 否 | 是 | §8.6.2 | 逐字 |
| 28 | ig34_p0438_a015 | p438 RELSUB asm 3 POOLID | :369 | 否 | 是 | RELSUB Asm | 逐字 |
| 29 | ig34_p0439_a023 | p439 relsub.xpt Row 6 (TABLE_ROW) | :413 | 否 | 是 | RELSUB Ex | 渲染逐格 5/5 |
| 30 | ig34_p0440_a003 | p440 RELSPEC asm 2 | :443 | 否 | 是 | RELSPEC Asm | 逐字 (PDF "is does" 照录) |

独有信息丢失 = 0; 忠实度错误 = 0.

### 另查
- gaps / intros / footnote_moves: 本批均空 (json), 无需落地核.
- 反向 KB→PDF 全文件扫 (`python3 -I $S/rev.py`, 去排版字符归一后对 p427-440 文本): 叙述未命中仅 :1 H1 / :3 Source 行 / `*.xpt:` 表名标签 (导航, U8) ; :15 DIZYGOTIC (T-1) ; :40 CMGRPID (T-2) ; :224 ")" (T-3) ; :228 illustrate (T-4) ; :241 Example 2 标签 (PDF 无编号 T-5) ; :169 / :373 跨行断句与句末 "." (T-9) ; :454-461 D6 块. 表格未命中均为 pdftotext 串列, 4 张样本表渲染逐格一致. 无 PDF 出处且未 D6 的解释性内容 = 0.
- 位置: 全部样本在 PDF 所属节对应 KB 节下.
- 授权范围: `git diff HEAD --stat -- knowledge_base/chapters/ch08_relationships.md` 只有本文件; narrow_files 空.
- G-TB8: trace 有 T2S.S-CH8 writer (`oh-my-claudecode:executor`, 07:58:04Z) + reviewer (`oh-my-claudecode:code-reviewer`, PASS, 08:08:09Z) subagent_done; `agent: main` 记录 0.
- `python3 tools/check_links.py 2>&1 | grep "live docs"` → `broken relative links: 18668 (live docs: 42)` (= 基线 42).
- 与 writer/reviewer 对照 (判完后读): 改动清单、T-1~T-5/T-9 登记、census 5 表 VERIFIED 与本审一致; 无分歧.
