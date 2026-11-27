# T4 解冻轮 (唯一一次 KB 修改) — 改动规格 v1.0
<!-- chain: E (plans) -->
> 主控 2026-11-27. 裁定来源: `evidence/checkpoints/t4_user_decisions.md` §000 (**委托代裁**, 非主人逐条裁定). 本规格只列 "改什么 + 依据指针", 不是 KB 内容; KB 由 writer 改, reviewer / auditor 独立复核 (规则 D).
> 流程: W1 (本规格 §1 值与排版) → W2 (§2 结构 / 标题 / D6) → reviewer (KB 全部 diff) → W3 (§3 台账回写 + 重算) → reviewer-L → auditor (全部). 失败按规则 B 归档 `evidence/failures/step_T4_thaw_attempt_N.md`.
> 共同禁区: 不碰 `archive/`、`releases/`、sdtm-rag 仓; 不改 spec.md 的 `- **Controlled Terms:**` 单元格格式; 不重排 model 文件的变量编号 (`#` 列); 不 git stash/checkout/reset; 不 commit; 不跑 `scripts/t4/t4_render.py` / `t4_sample.py` (会覆盖人工抽样包).
> 改标题 / 锚点前: `grep -rn "<file>#" knowledge_base web/src tools docs` 核入站链接; 有入站链接 → 同步改链接或保留旧标题并记录.
> 冻结前基线: KB 索引 md5 `29eaa90f82530add622432f9987e2850` (`git ls-files -s knowledge_base | md5 -q`, HEAD 3a24a1c); census `work/t4/census_full_head.json`; rag 映射 `work/t4/defhome_pre_thaw.txt` (R4 new 72).

## §1 W1: 值 / 措辞 / 排版字符
1. **U-7 维持 B 的 21 行** (A1-A3): 按 `evidence/checkpoints/t4_u7_rowcheck.md` 每行 "精确改法" 改, 含其 §"草拟位置漏了副本" 列出的全部副本 (A2-2 :285, A2-5 :48/:50, A2-15 :300, A2-16 :334 等). A2-16 用审查者更正值 ("PC records with PCGRPID"), 不用草拟 PPGRPID. **改回 A 的 5 行 (A2-12, A3-24, A3-28, A3-31, A3-32) 与草拟为 A 的行不改.** 行号以当前文件为准, 先 Grep 定位旧串, 对不上就停下报告.
2. **A6-1 / A6-2**: B-IS T-6 (IS/examples.md, 全部副本) 与 B-TA T-4 (TA/examples.md:351) 的 hyphen → PDF 的 en dash (U1 排版照 PDF). B-MK T-1 **不改** (代裁 Q3, 记后续).
3. **U-9(a) CRF 符号 口径 A**: 按 `evidence/checkpoints/t2_S-TYPO.md` "CRF 符号: 给 T4 用户裁定的候选口径" 的口径 A: CE/examples.md p152 `( )`→○ 18, p153 `( )`→○ 15 / `[ ]`→□ 6; ch04 p32/p33 `[ ]`→○ 16 + p32 Wingdings 坏字形处 `[ ]`→○ 3. **控制总数 CE 39 + ch04 19 = 58**, 不等就停. ML 保持 `[X]`/`[ ]`; FA / AE / DM Mermaid 不动. 用 `scripts/t2s/typo_plan.py` 生成计划 + `typo_assert.py --plan` 断言 (S-TYPO 同机制; 计划存 `work/t2_batches/T4-THAW.typo.plan.jsonl`).
4. **registry 同步** (`work/t2_pdf_typo_registry.jsonl`): §1.1/§1.2 涉及的登记行 handling `照录` → `KB 写正确值` (A6 行改 kb_text_span 为 en dash 写法), `kb_text_span` / `kb_value` / `kb_line_now` 改为改后值; A2-16 行 note 写 "草拟候选值 PPGRPID 有误, 由 U-7 审查者按同页 relrec 更正 (t4_u7_rowcheck.md)"; 每改一行加字段 `"t4_decision": "U-7 B (委托代裁 2026-11-27)"` 等. 新增登记: U-10④ `p354 "Lymph Nodes State"` vs `p355 "Lymph Node State"` (handling 照录, cat obs); U-10① model/05 5.1.x 标题 "(XX)" 后缀 = S-MOD3 主控规则保留的检索导航 (cat obs, 不改 KB).
5. **断言**: `typo_assert.py --plan` PASS; `ct_assert.py` PASS (C-code note 59 不变); `python3 tools/check_links.py 2>&1 | grep "live docs"` ≤ 42.

## §2 W2: 结构 / 标题 / D6 (`t4_user_decisions.md` §1 A5 表各行 "候选 (B)" + "依据")
1. **A5-1**: `model/05` 既有标题补 PDF 节号 + 原名 (sv20 页), 5.1.1.1-2 / 5.1.3.1-2 / 5.1.4.1-3 七个四级节改 `####`; 原有 "(XX)" 域代码后缀按 S-MOD3 规则保留在 PDF 标题后.
2. **A5-2**: `model/05` TT/TP 表列名 `Notes` → `Usage Restrictions`, 同步改表上方 KB note 的措辞 (须属实).
3. **A5-3** (代裁 Q1 = 照做): `model/05` TS 表加第 6 列 `Usage Restrictions`, TSVALCD/TSVCDREF/TSVCDVER 三行填 PDF 值 ("Not in nonclinical trials", 以 sv20 渲染页为准), 其余行空; 表上方加/改 KB note 与 TT/TP 同式. 不改 `#` 编号.
4. **A5-4**: `model/05`、`model/06` Role 列括注统一为 `Role (Variable(s) Qualified)` 写法 (S-MOD2 已用的写法); 只改括注文字, 不增删列.
5. **A5-5**: `model/06` 6.1-6.7 标题 / H1 改 PDF 原标题 (sv20).
6. **A5-6**: `model/06` RELREC USUBJID/POOLID 的 KB 自写 Notes → 加 `> KB note (not in SDTM v2.0):` 标注 (选 "加 D6", **不清空格子**).
7. **A5-7**: `model/06` RELREC APID Notes 补全 PDF 句 (POOLDEF 句).
8. **A5-8**: `model/06` "RELTYPE Combinations" KB 自写表 → 改为一行指向 ch08 相应节的交叉引用 (与 SDTMIG ch08 数据集级 3 种组合一致); Summary 表 SUPP-- "Yes" 改为准确说法 (依据 ch08 / sv20).
9. **A5-9**: `domains/TI/assumptions.md` §7.4 标题 → PDF "7.4 Trial Eligibility and Summary (TI and TS)".
10. **A5-10**: `domains/PP/examples.md` "RELREC Method Quick Reference (PP-side view)" 整节 → 一行交叉引用到 `PC/examples.md` 相应节.
11. **A5-11**: TA §7.1/§7.2 自拟标题 (X-4)、FA `## §6.4.4 FA – Description/Overview` 合并标题、MB H2 "and"、SS `#####` 层级 → 统一改 PDF 原标题 / 层级 (先核 0 入站链接).
12. **A5-13**: `domains/RELREC/assumptions.md:5` D6 行改措辞, 消除 "not in SDTMIG" 与 "from SDTMIG §8" 的字面矛盾.
13. **A5-14** (按主控意见): 全库 `> KB note (not in SDTMIG):` / `(not in SDTM v2.0):` 逐条分类 —— **只说明来源 / 位置** (如 "以下来自 §x"、"本节对应 PDF 第 n 页"、"表在 PDF 中位于…") 的改前缀为 `> Note:`; KB 自写内容 (解释、补充值、C-code 说明、KB 自写表/图/列说明) **保留原前缀**. 拿不准的保留原前缀. 输出全量分类清单 (文件:行 / 类别 / 改否), 写在 checkpoint.
14. **A5-12 / A5-15 = A**: 不改.
15. **U-10 ②③**: `domains/CE/examples.md:39` CRF 标题 (KB 自拟) 与 `chapters/ch02_fundamentals.md:158/:167` KB 自拟标题: PDF 同位置有标签 / 标题 → 改为 PDF 原文 (先核入站链接); PDF 无对应 → 保留并登记 (out_of_scope_findings 追加 O 号), 不加 D6 (标题属导航).
16. **U-11**: Mermaid 不需改 (解冻前 42/42 渲染 OK); 若本轮改动触及 Mermaid 块, 改后跑 `bash scripts/t4/t4_mermaid_render.sh <scratch>` 须 0 FAIL.
17. **断言**: 同 §1.5; 另报 `git diff --stat -- knowledge_base`.

## §3 W3: 台账回写 + 重算 (KB 改完、reviewer PASS 之后)
1. **U-2**: `ig34_p0056_a006` → ATOM_ERR (依据 `t4_user_decisions.md` U-2 行; PDF p56:37-40 vs 原子漏 "to improve readability").
2. **U-8**: `ig34_p0026_a037` / `ig34_p0082_a025` / `ig34_p0342_a006` / `ig34_p0342_a007` → PDF_TYPO (登记 B-ch04 T-7 / S-SPREL SE T-1 / B-SC T-1).
3. 必须改在 `t3_writeback.py` 的**输入**里 (`work/t3_errata.json` / `work/t3_k3b_out_of_scope_keep.json` / registry 等, 按脚本现有读法), 再按 `evidence/checkpoints/t3_recompute.md` §A4.5 命令在新 KB 上整套重跑 (fp_match → s0_classify → t3_t2s_atoms → t3_errata_build → t3_writeback → t3_direct_hit → t3_recompute → t3_report → t3_global_coverage); 不得手改 ledger 行 (下次重跑会被冲掉). 新 KB 下 fp 回归 / 标签变化逐条列出原因 (预期: §1 改为正确值的原子可能 EXACT → PDF_TYPO 或反之).
4. 重算覆盖: `scripts/t4/t4_coverage_decomp.py` 并列报 strict / mapped / **U-1 B 口径 (ATOM_ERR+PDF_TYPO 算覆盖, FIG 算未覆盖)** / 内容指标 (EXACT+EQUIV); 重跑 `scripts/t4/t4_ack_lists.py` (清单状态行改 "委托代裁整类确认, 见 t4_user_decisions §000").
5. 其它: `table_census.py` 在新 KB 上重跑, 与 `work/t4/census_full_head.json` **逐表** diff (不是只比合计), 每个变化表说明原因; `bash scripts/t3/t3_mutation.sh` 与 `bash scripts/t0_mutation.sh` 在新 HEAD 重跑; `t4_heading_diff.py kb-2026.11.25 HEAD` 与 `00a2e93 HEAD` 各跑一次; `check_links` ≤ 42.
