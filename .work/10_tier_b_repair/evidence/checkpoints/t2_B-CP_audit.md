# T2 B-CP auditor (Rule A 独立抽检)

## attempt 1 (2026-11-26, oh-my-claudecode:verifier / opus)

范围: `git diff 97e1895 -- knowledge_base/domains/CP/` (examples.md + assumptions.md; 97e1895..HEAD 无 CP 提交). 先独立判, 判完才对照 writer/reviewer.
Scratch: `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/7fe38595-6d99-4b86-881d-0dfb0d270167/scratchpad/t2_B-CP_auditor/` (下称 $S).

### 抽样 (可复跑)
- 主样本: `t2_auditor_v1.0.md` 抽样脚本原样 (b="B-CP", seed=20261126), 输出 `$S/sample.json` → **C=25, P=100, N=10** (C 抽 5 + P−C 对照 5).
- 补抽 (主控要求 "新增 + 删除都抽"; 同 seed, `random.Random(20261126)`, 先抽新增后抽删除, 输出 `$S/supp.json`):
  新增 atom 清单 24 条中抽 6; 删除清单 D-1..D-20 中抽 6.
- 全量反扫 (超出抽样, 加强): `$S/faith.py` = examples.md 每条非表格行按句 norm 后 ∈ PDF p207-221 拼接文本; `fp_match.py` 隔离跑 (base=git archive 97e1895, cur=base+现 CP 两文件) 看 p208-220 全部 prose 原子是否命中.

### 主样本 (N=10)
| # | atom_id | PDF 页:行 + 摘要 | KB file:line | 丢失? | 忠实? | 位置? | 说明 |
|---|---|---|---|---|---|---|---|
| 1 | ig34_p0213_a004 | 213:15 rows 7-9 数据用于 rows 10-11, CPGRPID 标组 | CP/examples.md:121 | 否 | 是 | 是 (Ex3) | verbatim |
| 2 | ig34_p0213_a003 | 213:12 Rows 10-11 单核细胞子系占总单核%, "Monocytes Sub", CPSBMRKS 区分 | examples.md:119 | 否 | 是 | 是 (Ex3) | verbatim |
| 3 | ig34_p0209_a001 | 209:1 (续 p208) CD45+ 纳入 CPMRKSTR 后可省; Row 3 比例; "/" 分隔分子分母 | examples.md:15 | 否 | 是 | 是 (Ex1a) | verbatim |
| 4 | ig34_p0215_a013 | 215:24 复杂表型检测 → CPSPTSTD 提供更完整描述, 非 CT 管理 | examples.md:192 | 否 | 是 | 是 (Ex6 引言) | verbatim |
| 5 | ig34_p0215_a015 | 215:35 Rows 7-10 CPSPTSTD 前置细胞状态 marker (CD83+), rows 9-10 表达 | examples.md:196 | 否 | 是 | 是 (Ex6) | verbatim |
| 6 | ig34_p0208_a010 | 208:23 各新变量用法在 ≥1 个例子中展示 | examples.md:5 | 否 | 是 | 是 (引言) | verbatim |
| 7 | ig34_p0211_a009 | 211:26 row 11 比值不用 CPCELSTA, 预协调入 CPTEST, 去 "Sub", CPGRPID 分组 | examples.md:81 | 否 | 是 | 是 (Ex2) | 唯一差异 = 补闭括号 ")" (T-1, 已登记, PDF 自身可定) |
| 8 | ig34_p0212_a011 | 212:33 CPTEST 填最细命名群 + "Sub"; CPSBMRKS 只放额外 marker; TLym Help 2 例 | examples.md:107 | 否 | 是 | 是 (Ex3 引言) | verbatim |
| 9 | ig34_p0218_a018 | 218:29 Rows 7-8 同型对照背景结合; CPBDAGNT / CPMRKSTR 标示 | examples.md:273 | 否 | 是 | 是 (Ex8) | verbatim |
| 10 | ig34_p0210_a020 | 210:38 (Ex1b) Row 1 白细胞总数, FSC/SSC 排碎片, CPGATDEF 可空 | examples.md:52 | 否 | 是 | 是 (Ex1b) | verbatim |

### 补抽 A: 新增 atom (6/24)
| # | atom_id | PDF 页:行 + 摘要 | KB file:line | 丢失? | 忠实? | 位置? | 说明 |
|---|---|---|---|---|---|---|---|
| A1 | ig34_p0218_a016 | 218:22 Rows 1-3 CPTEST/CPMRKSTR/CPBDAGNT/CPREPNUM/CPCOLSRT; "mean extent of CDxx bound" | examples.md:269 | 否 | 是 | 是 (Ex8) | verbatim; 旧改写 "mean of CDxx" 已删 (D-10) |
| A2 | ig34_p0218_a015 | 218:20 CPSPTSTD / CPTSTPNL 有助识别细胞群 | examples.md:267 | 否 | 是 | 是 (Ex8 引言, 在 Rows 1-3 前, 与 PDF 序一致) | verbatim |
| A3 | ig34_p0209_a003 | 209:18 Rows 6-7 T 淋巴系 marker 正负表达; 顺序同 rows 4-5 | examples.md:19 | 否 | 是 | 是 (Ex1a) | verbatim |
| A4 | ig34_p0219_a018 | 219:68 全套检测: 游离/总/背景/特异结合; HA5/2D4; MESF; CPTSTCND; RO 计算 | examples.md:301 | 否 | 是 | 是 (Ex9, Row 1 前) | verbatim |
| A5 | ig34_p0210_a021 | 210:41 Rows 2-3 淋巴细胞绝对数/占白细胞%; FSC/SSC 亚门; ", where they are used to distinguish…lineages" | examples.md:54 | 否 | 是 | 是 (Ex1b) | verbatim (含原缺分句) |
| A6 | ig34_p0217_a016 | 217:52 Row 2 同 row 1 但报最终门; CDxx 前置; CPBDAGNT/CPTSTPNL | examples.md:249 | 否 | 是 | 是 (Ex7) | verbatim (3 句全); 附录矛盾版 (D-20) 已删 |

### 补抽 B: 删除项 (6/20)
| # | 删除项 | 核对 | 丢失? | 说明 |
|---|---|---|---|---|
| B1 | D-11 Ex9 Row 1 "…CPGATDEF contains the gate definition." | base 有 2 处 / cur 0; 同行保留 PDF p219:73→p220:1 原句 "…CPGATEDEF contains the gate definition/gating strategy." | 否 | 删的是改写; PDF 原句信息更全 |
| B2 | D-8 "3 new variables that qualify CPTEST have been added…" (独立句) | cur 该短语仅存在于 PDF 原句 "To accommodate the need for further subsetting, 3 new variables…" (p212:28) | 否 | |
| B3 | D-10 "…the mean of CDxx bound…" | cur 0; :269 为 PDF "mean extent of CDxx bound" | 否 | |
| B4 | D-4 "…viability marker 7AAD-." | cur 0; :71 为 PDF "7AAD to exclude cells…(7AAD+)" (p211:13) | 否 | 改写句信息被 PDF 原句覆盖 |
| B5 | D-14 Ex5 占位句 `*(cp.xpt table contains 8 rows …)*` | KB 自写; :175-187 真表 8 数据行在 | 否 | |
| B6 | D-6 "…for the apoptotic lymphocyte subpopulation, both as a cell count…" | :75 为 PDF p211:18-20 原两句 (apoptotic cell state / The sponsor is reporting…) | 否 | 被删 "(i.e., apoptotic, being defined)" 为 KB 改写, PDF 为 "(i.e., apoptotic) being measured" |
- 附带全量: base assumptions.md 附录 11 条 `[atom]` 段逐句 ∈ 现 examples.md → 9 条全命中; 未命中 2 条 = D-20 (与 PDF 矛盾的 ", as in row 1"/CPGATEDEF 版) 与 a001 附录改写 ("is not part", PDF "it is not part") — 均为预期, PDF 原文在 examples.md:249 / :303.

### 全量反扫 (加强证据)
- 忠实度 (`python3 $S/faith.py`): examples.md 全部非表格行按句 ∈ PDF p207-221 → 不命中 5 句 = :81 (T-1)、:200 (T-3)、:202 (T-2)、:271 (T-4)、:303 (跨页 p219 末 + p220 首, 拼接后逐字存在, 已 grep 核). 无自造/扩写句.
- 丢失 (fp_cur p208-220 prose): 98 条中 hit_target 90 (CP/examples 85, CP/assumptions 2 = p208 假设 9/10, GF 3 = p220 GF 节); 未命中 8 = T-1/T-2/T-3/T-4 四条 + p0212_a009/p0215_a012/p0220_a002/p0220_a003 (原子文本自身错: 未命中子句经 norm_pdf 检 p 与 p+1 页均不存在于 PDF; KB 与 PDF 一致).
- **fp 回退 (隔离 CP)**: `fp_match.py --kb-root $S/cur/knowledge_base --baseline $S/fp_base.jsonl` → regressions=1 = **{ig34_p0215_a018}** (T-2 CPCSMRKR→CPCSMRKS), new_hits=63. 与要求集合完全相等 ✓.

### 表格 15 随机格 (Ex2–Ex9; seed 20261126; `$S/cells.json`) vs 渲染 PDF (220dpi 裁切 `$S/img/c_*.png`) + bbox 独立读
| # | Ex/行/列 | KB | PDF | 一致 |
|---|---|---|---|---|
| 1 | Ex8 r5 CPTPTNUM | 1 | 1 (p219) | ✓ |
| 2 | Ex8 r1 CPDTC | 2020-07-24T09:00 | 2020-07- / 24T09:00 (目视) | ✓ |
| 3 | Ex2 r6 CPORRESU | % | % (p212) | ✓ |
| 4 | Ex3 r4 CPSBMRKS | (空) | 空 (目视 p213) | ✓ |
| 5 | Ex6 r11 CPTSTPNL | mDC AND pDC SUBSETS | 3 行折行同值 (目视) | ✓ |
| 6 | Ex6 r17 USUBJID | ABCD-001-001 | ABCD- / 001-001 | ✓ |
| 7 | Ex5 r8 CPRESSCL | QUANTITATIVE | QUANTITATIVE (目视 p215) | ✓ |
| 8 | Ex6 r12 CPSEQ | 12 | 12 | ✓ |
| 9 | Ex3 r8 CPTEST | Mono Sub | Mono Sub (目视) | ✓ |
| 10 | Ex6 r30 CPRESSCL | QUANTITATIVE | QUANTITATIVE (目视 p217) | ✓ |
| 11 | Ex6 r20 CPMRKSTR | CD45+CD3-CD19-CD20-CD56-HLADR+CD123+CD1c- | 同 (目视 p216) | ✓ |
| 12 | Ex6 r4 CPTEST | Dendritic Cells | Dendritic Cells | ✓ |
| 13 | Ex9 r4 CPORRES | 4798 | 4798 (目视 p220) | ✓ |
| 14 | Ex3 r12 CPCSMRKS | ANXV+ | ANXV+ (目视) | ✓ |
| 15 | Ex9 r3 CPCAT | TARGET ENGAGEMENT | TARGET ENGAGEMENT (目视) | ✓ |
- 15/15 一致. (目视附带看到 Ex6 CPGATDEF PDF `SSCmid|CD45LIN-|…`, KB `CD45+LIN-` = T-9 已登记.)

### USUBJID 渲染复核
- Ex2 (p211 5 行 + p212 6 行) 全部 `0005`/`00542` 两行; Ex9 (p220) 14 行全部 `0001`/`00001` (bbox 计数 nA=nB). 目视 c_212_6 / c_220_* 均为首行 4 位、次行 5 位.
- 宽度: p212 列起点到下一列起点 27.8pt, "0005"+"00542" = 24.9pt (≈2.77pt/位); p220 21.6pt vs 17.3pt (≈1.73pt/位). 扣单元格左右内边距后 9/10 位串放不下一行, 若无空格则字符级断行应把首行塞满 (≈7-8 位), 不会恰好 4|5 且每行一致 → 断点为空格. KB `0005 00542` (11 处) / `0001 00001` (14 处) 判定 **成立**.

### 独立判后对照 writer/reviewer
- 与 writer 续/续2 与 reviewer 结论一致; reviewer CONDITIONAL 的 p0208_a009 (:5 "Gate Name"→"Gate") 已由续2 修, fp_cur 命中 ✓.
- D6: 主控口径 assumptions.md:98 标题 / :100 交叉引用为导航 → 不需 KB note; 本审认可 (examples.md 无 KB 自写解释性内容残留, faith.py 0 未登记句).

### 观察 (不计 FAIL, 交主控)
- O-1 PDF_TYPO 口径一致性: T-2 把 CPCSMRKR 改为 CPCSMRKS, 但 PDF 系统性写 `CPGATEDEF` (p211/212/213/217/218/220 叙述, KB :71/:109/:117/:247/:267/:303 照录), 正确变量名 CPGATDEF 可由 spec/表头确定. D-11 还删了 KB 原用正确名 CPGATDEF 的改写句. 不是丢失/忠实错 (与 PDF 逐字一致), 但按 "补充口径" 取舍规则应改正或至少登记为 T 项; 建议主控裁 (改则需同步接受 fp 回退).

### 汇总
- 主样本 10: 独有丢失 **0**, 忠实度错 **0**, 位置错 0. 补抽新增 6 / 删除 6: 丢失 0, 忠实错 0. 表格 15 格 0 错. fp 回退 = {ig34_p0215_a018} ✓.
- G-TB8: trace 有 B-CP writer `oh-my-claudecode:executor` subagent_done ×3 (01:09:50 / 01:16:56 / 01:40:51) 与 reviewer `oh-my-claudecode:code-reviewer` subagent_done (01:25:07, CONDITIONAL → 续2 已处理); `agent: main` 记录中无 B-CP 写 KB ✓.
- **判定: PASS** (attempt 1).
