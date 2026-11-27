# T4.1 总闸独立审 — attempt 1

<!-- chain: E (plans) -->
> 状态: **不通过 — CONDITIONAL (证据层齐, 等用户裁定)** (2026-11-27).
> 审查角色: `feature-dev:code-reviewer` (opus) × 5 个独立实例, 本项目其它环节未用过 (trace.jsonl 0 次; 证据层审查 §4 核过). 4 个审 84 条样本, 1 个审闸门证据层.
> 主控只做三件事: 抽样 (脚本)、派发、誊录 + 机械计数. 审查回复原样存于 `evidence/t4_gate_raw/pack{1,2,3,4}.md` 与 `evidence/t4_gate_raw/evidence_layer.md`; 本文件不改判 (规则 D).
> brief: `subagent_prompts/t4_gate_reviewer_v1.0.md`. 判定口径派发前已定: 任一样本 NOT_HOLD → 不 PASS; UNVERIFIABLE 不算 PASS.
> 规则 B: 本次是 CONDITIONAL (等用户裁定), 不是证据不成立的失败, 不按失败归档; 指针 `evidence/failures/step_T4.1_attempt_1.md`.
> KB 未改: 审查期间 KB = 00a2e93 内容, 真 KB md5 `b3a040150c53a4256ea0dde645bd7d07` (t3 口径) 前后一致.

## 0. 结论

- **样本层: 84/84 HOLDS**, NOT_HOLD 0, UNVERIFIABLE 0 (PLAN 正式 72 条 + 主控加的补充层 12 条).
- **证据层: 判 "不能 PASS", 最多 CONDITIONAL.** 原因 (按 PLAN 字面): G-TB1 NOT_MET (残留 1 条 + 三类登记无用户 ack)、G-TB2 NOT_MET (170/174, 字面严格口径 155/174)、G-TB3 字面 NOT_MET (06 公式照套 = strict 96.07%; mapped 99.36% 过, 但 mapped 口径无用户认可记录).
- 所以 **T4.1 总闸 = 不通过 (CONDITIONAL)**. 这些缺口都要用户裁定才能关闭, 不是再修 KB 能解决的; 清单见 §5 和 `t4_user_decisions.md` §00.

## 1. 抽样设计 (复跑)

```bash
python3 -I .work/10_tier_b_repair/scripts/t4/t4_sample.py   # -> work/t4/{gate,human}_sample.jsonl
python3 -I .work/10_tier_b_repair/scripts/t4/t4_render.py   # -> work/t4/gate_pack_{1..4}.md + evidence/checkpoints/t4_human_sample.md
```
- seed 20261127; 每个总体先排序再 `random.Random(seed).sample`. 连跑两次 md5 一致 (命令: 上面两行连跑两遍后 `md5 -q .work/10_tier_b_repair/work/t4/gate_sample.jsonl .work/10_tier_b_repair/work/t4/human_sample.jsonl`): gate_sample `67b1013f496096df483eb300a66150d6` (= 审查者所看版本; 之后只改了人工层, `git diff` 总闸包为空) / human_sample `5b4212ee6b5deb873ab29d7f13e17232` (人工层按总闸指针偏移教训补了定位: 多处命中全列、近似定位加警告、IE 按变量名定位、PDF_TYPO 登记内联).
- 正式 72 = triage `final_class` PRESENT / REWRITE_OK / REAL_GAP / VALUE_DIFF / IE 各 12 (按 triage 类抽, 不按终态过滤) + 对照层 12 (§5.0 SCOPE 内、非 HEADING、T3 前后都是 EXACT/EQUIV、不在 `t3_writeback_decisions.json`; 总体 4119).
- 补充层 12 (PLAN 外, 主控加): T3 允许集中不在 triage 的 480 个原子 (T2S / 勘误新定终态, ATOM_ERR / PDF_TYPO 主要来源), 终态 ATOM_ERR / PDF_TYPO / EXACT 各 4.
- 总体排除: `MANUAL_01/02` (无 ledger 行)、残留 `ig34_p0056_a006` (另交用户).
- 样本包里 "PDF 原文" 取自 `work/pdf_pages/*.txt` 自动定位, 不取原子 verbatim; KB 指针由脚本给, 审查者都自己重新 Grep 过 (报告的指针偏移: #46 #50 #54 #60 #84, 不影响判定).

## 2. 样本层结果 (誊录)

| 包 | 行 | 层 | HOLDS | NOT_HOLD | UNVERIFIABLE | 原文 |
|---|---|---|--:|--:|--:|---|
| 1 | 1-21 | PRESENT 12 + REWRITE_OK 9 | 21 | 0 | 0 | `evidence/t4_gate_raw/pack1.md` |
| 2 | 22-42 | REWRITE_OK 3 + REAL_GAP 12 + VALUE_DIFF 6 | 21 | 0 | 0 | `evidence/t4_gate_raw/pack2.md` |
| 3 | 43-63 | VALUE_DIFF 6 + IE 12 + CONTROL 3 | 21 | 0 | 0 | `evidence/t4_gate_raw/pack3.md` |
| 4 | 64-84 | CONTROL 9 + SUPP_ATOM_ERR 4 + SUPP_PDF_TYPO 4 + SUPP_EXACT 4 | 21 | 0 | 0 | `evidence/t4_gate_raw/pack4.md` |
| **合计** | 84 | 正式 72 + 补充 12 | **84** | **0** | **0** | |

对照层 12/12 HOLDS → PLAN Q9 的 "发现错 → 扩为全量指纹复验" 未触发.

审查者顺带指出的标签口径问题 (不是 NOT_HOLD, 交用户 / 后续):
- pack2 #37/#41、pack3 #52/#62: 原子 verbatim 抽错, 但终态标 EXACT/EQUIV/IE 而不是 ATOM_ERR (KB 与 PDF 一致, 终态按定义成立; 同类在别处标 ATOM_ERR, 口径不统一).
- pack3 #61-63: 对照层 3 条 stock EQUIVALENT 实为逐字 → 覆盖低报, 是否统一改 EXACT 待定.
- pack3 表后 1: `t1_ie_final.md` 没有 SPEC_TABLE_HEADER 的类别定义, 审查者自定口径判 HOLDS, 建议补正式定义.
- pack4 #84: KB 标题比 PDF 多后缀 "(TE)", 按 EXACT 容差判 HOLDS; 追加后缀算 EXACT 还是 EQUIV 待定.

## 3. 证据层结果 (誊录摘要; 全文 `evidence/t4_gate_raw/evidence_layer.md`)

| 闸 | 判定 | 要点 |
|---|---|---|
| G-TB1 | **NOT_MET** | 残留 `ig34_p0056_a006` (PARTIAL); ATOM_ERR 197 / PDF_TYPO 122 / FIG 11 无用户 ack; PLAN §5.0 写 FIGURE 12, 实际 11 |
| G-TB2 | **NOT_MET** | 范围内口径 170/174, 字面严格 155/174; 未过 4 节全由 p0056_a006 一条造成; "范围内" 口径是主控 C4 定的, 未经用户 |
| G-TB3 | **字面 NOT_MET; mapped 过** | 见 §4 |
| G-TB4 | MET_WITH_CONDITION | S-CT/S-TYPO 后没在 HEAD 重跑全量 census; C3 剩余表无结案清单 |
| G-TB5 | MET | 3 个 FAIL 批都重做 + 归档; 小问题: B-AE 0/9 < N=10, "业务判定"列全为"待主控", T0.4 行写"待跑" |
| G-TB6 | MET_WITH_CONDITION | C 层 1370 行 (MERMAID 322 / TABLE_TOKENS 680 等) 只靠抽样, 字面 100% 不成立 |
| G-TB7 | MET_WITH_CONDITION | 要当前输出 |
| G-TB8 | MET (字面) | 82 批 3 角色齐; trace 有事后回填行, 不能独立证明主会话没写 KB |
| G-TB9 | MET | 建议 HEAD 上重跑变异 |

主控按证据层要求补的当前输出 (只读运行, KB 不变):

```bash
python3 tools/check_links.py 2>&1 | grep "live docs"
# broken relative links: 18668 (live docs: 42)          → G-TB7 ≤ 42 成立 (含本次新增 T4 文件)
bash .work/10_tier_b_repair/scripts/t3/t3_mutation.sh > .work/10_tier_b_repair/work/t4/t4_mutation_head.log 2>&1
# M0 GREEN / M1 RED / M2 GREEN / M3 RED / M4 RED / M5 RED / M6 RED / M7 GREEN; real KB md5 after b3a040150c53a4256ea0dde645bd7d07, unchanged OK  → 与 T3 一致
# 注: 跑的是 T3 变异脚本 (覆盖 fp_match + t3 直接命中); 审查者建议的 T0 变异脚本 t0_mutation.sh 本次未在 HEAD 重跑
python3 -I .work/10_tier_b_repair/scripts/table_census.py --manifest .work/10_tier_b_repair/work/census_full_manifest.json --out .work/10_tier_b_repair/work/t4/census_full_head.json
# KB tables 500; {'UNPARSEABLE': 148, 'OK': 311, 'DIFF': 37, 'NO_PDF': 4}; PDF_ONLY 0; cells compared 35129; diffs 144
```
- census: 与 T2 收尾 (`50c3958`, 即 60 批 T2 之后、22 个 T2S 批之前; `evidence/t2_census_global_triage.md` §1: KB 表 501 / OK 311 / DIFF 37 / diffs 144 / UNPARSEABLE 149 / PDF_ONLY 1) 相比, 汇总计数 OK / DIFF / diffs 相同, 但 KB 表 501→500、UNPARSEABLE 149→148、PDF_ONLY 1→0 有变. **合计相同不等于差异集相同**: 未逐表比对 (旧 json 已清; 可用 `git archive 50c3958 knowledge_base` + `--kb-root` 重跑后逐表比), 所以不能据此断言 T2S 各批没有引入表格差异. C3 逐表结案清单仍缺 (G-TB4 条件未关).

## 4. 覆盖率: 两个口径并排

复跑: `python3 -I .work/10_tier_b_repair/scripts/t4/t4_coverage_decomp.py` (按行比 pre_t3 与终态 ledger; 06 按行计).

| 口径 | 公式 | 值 | 对 99.02% |
|---|---|--:|---|
| T3 前 (= 06 终态) | (EXACT+EQUIV+PARTIAL+MISPLACED) / (行 − IE) | 10298/10400 = **99.0192%** | 基线 |
| **strict** | 同 06 公式; 新三类 (ATOM_ERR/PDF_TYPO/FIG) 留在分母、不进分子 | 9593/9985 = **96.0741%** | **低于** 99.02% |
| **mapped** | 新三类与 IE 一样从分母去掉 | 9593/9655 = **99.3578%** | 高于 |
| 参考: 新三类中 ATOM_ERR/PDF_TYPO 算覆盖、FIG 算未覆盖 | — | 99.27% (证据层审查者推导) | 高于 |
| 参考: 严格内容 (EXACT+EQUIV)/mapped 分母 | — | T3 前 76.76% → 现 90.70% (审查者自算) | — |

下降分解 (strict 99.02% → 96.07%):
- **几乎全部来自 319 行 "已覆盖 → 新三类"** (ATOM_ERR 194 / PDF_TYPO 121 / FIG 4): 分子 −319、分母不变, 约 −3.19 个百分点. 这 319 行在 06 里算覆盖 (多为 PARTIAL/EQUIV/EXACT/MISPLACED). 若仍算覆盖: 9912/9985 = 99.2689%.
- 其余: 已覆盖 → IE 494 (用户 R4 已 ack, 约 −0.05pp)、IE → 已覆盖 72、未覆盖 → 已覆盖 32、未覆盖 → 新三类 8、末尾新增 5.
- 不管哪个口径, 范围外仍有 PARTIAL 638 / MISPLACED 197 算作 "已覆盖"; 唯一的未覆盖是 ERROR 62.

用哪个口径过闸 (证据层审查者意见 + 主控说明, 交用户定):
- 按公式字面, strict 才与 06 同口径; 但 ATOM_ERR (原子抽错, KB 按 PDF) 和 PDF_TYPO (PDF 笔误, KB 按登记) 的定义都是 "KB 承载了 PDF 内容", strict 把它们算未覆盖, 与 06 的本意相反. 所以两者都不是严格同口径.
- mapped 与 strict 的差距完全来自分母定义 (330 行); mapped 高于 99.02% 的部分来自未覆盖从 102 降到 62 (真修回 32 + 改归新三类 8).
- 审查者建议: 用 mapped (或 99.27%) 过闸, 同时并列报告 strict 96.07% 和内容指标 90.70%, 写明范围外 PARTIAL/MISPLACED. **mapped 口径目前没有用户认可记录** (`t1_user_ack.md` / `t2_post_user_ack.md` 无; `t3_recompute.md:515` 仍写 "需要确认采用 mapped").
- 另: mapped 依赖的 ATOM_ERR / PDF_TYPO 标签中, C7 的 38 条 "原子不在 PDF 窗内" 并非逐条证明 (`t3_recompute.md:127-128`); 本次补充层只抽了 ATOM_ERR 4 + PDF_TYPO 4 (全 HOLDS, 但 0 错时 95% 上限约 31%).

## 5. 关闭 T4.1 需要的事

**用户裁定** (已汇总到 `t4_user_decisions.md` §00):
1. 残留 `ig34_p0056_a006` 的处理 (G-TB1 / G-TB2).
2. ATOM_ERR 197 / PDF_TYPO 122 / FIG 11 确认 (`t4_ack_lists.md`), 以及 A1-A6 / A5 / B 组逐条 (G-TB1).
3. G-TB3 采用哪个口径, 是否同意并列报告 strict 与内容指标.
4. G-TB2 结构父节用 "范围内" (170) 还是字面严格 (155).
5. G-TB6 C 层是否接受按抽样过.

**主控可补 / 建议 (本次未做)**:
- C3 剩余 UNPARSEABLE 表的逐表结案清单 (G-TB4); census 500/148/0 差异原因.
- 抽样补强 (证据层审查者建议): T3 direct_hit 的 pre_existing 58 条单独成层或全检; ATOM_ERR/PDF_TYPO 补抽到合计 ≥30 (重点 C7-atom-not-in-PDF 38 条); FIGURE_DEFERRED 11 条及 triage ATOM_ERR/RELOCATE/LOCATE 88 条、`T1-two-agent+T2-rework` / `T2-fix+deltaRereviewPASS+auditPASS` / `live-hit(was-IE-ack)` / `C1-manual` / `C7-K4-rereview` 规则 0 抽中.
- 文档状态行过期: `step_T3_audit.md:4` 顶部仍写 FAIL (终审 PASS 在 :479)、`t3_recompute.md:4` 状态行是 writer 时期的、`audit_matrix.md` T0.4 行 "待跑".

**KB 观察项 (KB 冻结, 只记录; 已列入 `t4_user_decisions.md` §00 U-9)**:
- `knowledge_base/model/05_study_level_data.md:29/45` 等: 5.1.x 标题加了 PDF 没有的域代码后缀 "(TE)" "(TA)" …, 无 KB note (与 A5-1 / A5-11 标题口径同类).
- `knowledge_base/domains/CE/examples.md:43-46` CRF 用 `( )`, FA CRF 用 `○`, 两处不统一 (CRF ○□ 口径的具体实例).
- `knowledge_base/domains/CE/examples.md:39` CRF 标题 "CE Example 2 — Clinical Events with Severity" 为 KB 自拟, PDF p152 只有 "CRF", 无 KB note.
- `knowledge_base/chapters/ch02_fundamentals.md:158` / `:167` KB 自拟标题无 D6 标注.
- PDF p354 叙述 "Lymph Nodes State" vs p355 表 "Lymph Node State", KB 分别照录, 未登记.

---

# §attempt 2 (2026-11-27) — **不通过 (CONDITIONAL)**

> 审查: `feature-dev:code-reviewer` (opus) 新实例, 只读, brief `subagent_prompts/t4_gate_reviewer_v2.0.md`; 对象 HEAD `d3f2ea9` (含解冻轮 `a59c2d3`). 主控誊录要点, 不改判 (规则 D). 规则 B: 不是证据失败, 是缺主人层面的确认 + 若干仍开缺口; 指针 `evidence/failures/step_T4.1_attempt_2.md`.
> 审查者实例**无 Bash**: 数字标 [自算 Grep] / [读日志] / [采信]; 其要求的复跑由主控在下方 "主控补跑" 给出当前输出 (与 attempt 1 §3 同做法).

## 结论: CONDITIONAL
- G-TB1-9 无 NOT_MET (6 条 MET_WITH_CONDITION); 样本层无 NOT_HOLD.
- C(3) 人工判定来源可核性 **不足**; C(1) 中 G-TB3 口径与 C(2) T4.2 口径 **需主人确认** → 上限 CONDITIONAL.
- 另缺: 有 Bash 的复跑 (主控已补, 见下); G-TB9 table_census / fp_match 在现 KB 上无变异再证明 (t0_mutation MISMATCH); G-TB4 C3 逐表结案清单.

## G-TB 表 (誊录)
| 闸 | 判定 | 要点 | 条件 / 缺口 |
|---|---|---|---|
| G-TB1 | MET_WITH_CONDITION | ledger 12492 行 EXACT 4718 / EQUIV 4015 / IE 2506 / PARTIAL 637 / MISPLACED 197 / ATOM_ERR 197 / PDF_TYPO 149 / FIG 11 / ERROR 62; p0056_a006 = ATOM_ERR; 范围内 174 节残留 0; PDF_TYPO 149/149 带 registry | ack 靠委托代裁; p0362_a010 改标是主控决定 (不在 §000 委托内) 却记在 U-7 名下; PLAN §5.0 FIG 12 实为 11 未更正 |
| G-TB2 | MET (U-3 范围内口径) | 范围内 174/174; 字面严格 157/174 (17 个结构父节仅因范围外子节) | 取决于 U-3 代裁 |
| G-TB3 | MET_WITH_CONDITION (U-1 B 口径) | B 9913/9986 = 99.2690% ≥ 99.0192%; strict 95.8041% (attempt 1 96.07%, 再降); mapped 99.3561%; 内容 90.6948% | 按 PLAN 字面不达标, 过闸完全依赖代裁 B 口径; 代裁时 PDF_TYPO 122, 现 149 |
| G-TB4 | MET_WITH_CONDITION | census DIFF 37→38, diffs 144→148 = DS SCRN ×2 + PP h ×2 (均登记 KB 写正确值, PDF_TYPO 例外); 删 3 表对得上 A5-8/A5-10 | 逐表配对只有 W3 做过; **C3 结案清单仍缺** |
| G-TB5 | MET | auditor 30/30 + 15/15 | audit_matrix 缺 T3 / U-5 / 解冻轮行 |
| G-TB6 | MET_WITH_CONDITION | 5414 行未溯源 0, NOTE_EXEMPT 5 | 5 条豁免是主控决定; C 层抽样 (U-4) |
| G-TB7 | MET_WITH_CONDITION | 日志 live docs 42 | 审查者未复跑 (主控补跑见下) |
| G-TB8 | MET (字面) 带局限 | 解冻轮 writer executor / reviewer code-reviewer / auditor verifier | trace 时间戳事后回填 (W1 03:02Z 早于 U-5/U-7 的 06:00Z; review/audit 整点 12:00Z), 证明不了先后; W3 中途 5 项主控决定超出委托 |
| G-TB9 | MET_WITH_CONDITION | t3_mutation M0 绿 / M1 红 / M2 绿 / M3 红 / M4-6 红 / M7 绿, 真 KB md5 不变 | t0_mutation 在现 KB MISMATCH (变异断言未施加, HEAD 副本同格局, 既有) → table_census / fp_match 在现 KB 无 "变红再复原" 证明; M3 换靶是主控决定; CE p153 14 原子只块级核 |

## 样本层延续性
- 解冻后有变化 4 条 (#22 ig34_p0151_a0013、#23 p0153_a0009、#24 p0153_a0019、#84 sv20_p0051_a016) + 相邻变化 1 条 (#65 p0152_a0003): 渲染页 p151-153 / model/05 重判 **全部 HOLDS**; 其余 79 条沿用 attempt 1 (指针不在改动 hunk 内; #3/#25/#26/#28 长行 Grep 截断未逐字核, 所在行不在任何 hunk).
- 审查者另记: auditor kb.diff 为 25 个文件, KB reviewer 写 "26 个", 交主控核.

## C 项 (裁定来源)
1. 委托代裁作 G-TB1 用户 ack: **足够** (委托明确覆盖 §00 选择题, U-6 排除, ack 按来源分登). 作 G-TB3 口径认可: **需主人确认** (U-1 实为改闸口径, strict 95.80%, 过闸全靠该口径). 委托**未覆盖**主控在 W3 的 5 项决定 (p0362 改标 / registry 事实修正 / Note 豁免 / M3 换靶 / ack 来源归属) → 需主人追认或在 §000 单列为主控决定.
2. "AI 预筛 42 + 主人抽查 6" 关闭 T4.2 hard 闸: **需主人确认** —— 主人有权改口径, 但 PLAN:82/127 未修订、Changelog 无记录; 6/6 零错 95% 上界约 39% vs 30/30 约 9.5%; AI 预筛不是独立人工证据; `t4_user_decisions.md` 状态与 `t4_human_verdicts.md` 自相矛盾.
3. 人工判定来源可核性: **不足** —— 委托原话与 "6 条都对" 都经协调方转达, 仓内无独立凭证; 需主人直接确认或在仓内留可核原话 / 截图 (委托原话、T4.2 口径变更、6 条判定).

## D 项 (attempt 1 缺口现状)
已关: 残留 p0056_a006; C7 38 全检; 文档状态行 (t3_recompute:4、audit_matrix:7; 另 step_T3_audit:4). 部分关: census 汇总变化原因 (解冻轮已归因, 500/148/0 vs T2 收尾仍未逐表); ATOM_ERR/PDF_TYPO 补抽 (仅 C7 38). **仍开**: C3 逐表结案清单; pre_existing 58 条单独核; FIG 11 条逐条核; 规则 0 抽中 5 类及 88 条; PLAN FIG 12→11; audit_matrix 缺 T3/T4 行. t0_mutation 已跑 = MISMATCH.

## 主控补跑 (HEAD `d3f2ea9`, 只读; 审查者无 Bash 时的当前输出)
```bash
python3 tools/check_links.py 2>&1 | grep "live docs"
# broken relative links: 18668 (live docs: 42)
bash .work/10_tier_b_repair/scripts/t3/t3_mutation.sh > .work/10_tier_b_repair/work/t4/t4_mutation_gate2.log 2>&1
# RESULT 依次: GREEN RED GREEN RED RED RED RED GREEN (M0..M7); real KB md5 before/after b71a466d6e618f995c493a82de3e3eb7, unchanged OK
python3 -I .work/10_tier_b_repair/scripts/t4/t4_coverage_decomp.py
# final strict 9567/9986 = 95.8041% / mapped 9567/9629 = 99.3561% / U-1 B 9913/9986 = 99.2690% / content 8733/9629 = 90.6948%
git status --short   # 补跑后仅本节新增文件 (日志 + brief v2.0), 无 tracked 改动
```
- t0_mutation 未重新跑 (W3 已在解冻后 KB 与 HEAD 副本各跑一次, 日志 `work/t4/t0_mutation_thaw.log` / `t0_mutation_kbhead.log`, 同格局 MISMATCH); 要恢复 G-TB9 对 table_census / fp_match 的证明需刷新 T0 baseline, 属后续项.
- 文件数: `git show --stat --format= a59c2d3 -- knowledge_base` → `25 files changed, 118 insertions(+), 179 deletions(-)`; KB reviewer 写的 "26 个" 不准, 以 25 为准.
