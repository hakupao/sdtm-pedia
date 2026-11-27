# T4.1 总闸独立审 — attempt 1 / 2 / 3 (本文件按 attempt 追加; 正文开头是 attempt 1)

<!-- chain: E (plans) -->
> **最新状态: T4.1 总闸 = PASS (2026-11-27; attempt 3 + delta 合并)** — 见文末 "§attempt 3 delta" (attempt 3 = CONDITIONAL, 唯一挡闸项 = 问题 A → 主人答 A1 → R3L 改 4 条 → delta 闸审 PASS). attempt 2 = CONDITIONAL 见 "§attempt 2". 以下到 "§attempt 2" 之前是 attempt 1 的原文 (历史, 不改).
> attempt 1 状态: **不通过 — CONDITIONAL (证据层齐, 等用户裁定)** (2026-11-27).
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

---

# §attempt 3 (2026-11-27) — **不通过 (CONDITIONAL)**

> 审查: `feature-dev:code-reviewer` (opus) 新实例, 只读, brief `subagent_prompts/t4_gate_reviewer_v3.0.md`; 对象 HEAD `4a5dd1d` (KB 树 `63f857774a42cfaa71798705ad40ab51bc5e378a`, 台账 md5 `16024ac09721cb3f8519cd68fa455196`). 审查者实例**无 Bash**: 复跑输出由主控事先在 `a88a585` 上跑好 (`work/t4/gate_prerun.log`), 审查者的数字标 [自算 Grep] / [读日志] / [采信].
> **报告原文** (脚本从会话记录原样取出, 主控未改一字): `evidence/t4_gate_raw/attempt3_report.md`. 下面是主控的要点誊录, 不改判 (规则 D); 与原文有出入以原文为准. 规则 B 指针: `evidence/failures/step_T4.1_attempt_3.md`.

## 结论: CONDITIONAL
- G-TB1 ~ G-TB9 **没有一条 NOT_MET**; 审查者从 78 条改标里自挑 10 条 (四组都有) 重判 **10 / 10 HOLDS**; 78 条改标 + 5 条指针行与总闸样本 84、T4.2 预筛 42、主人抽查 6 的交集都是 0 (三份样本沿用 attempt 1 / 2 的判定).
- **挡住 PASS 的只有一件事 = 问题 A**: 第三轮查出的 4 条多标 PDF_TYPO (`ig34_p0412_a006` / `a007` / `a008`、`ig34_p0413_a010`). 审查者自己用文本层逐条复核: 它们自己的 PDF 原文没有笔误, KB 与 PDF 逐字一致, 应为 EXACT; 挂的登记 `S-TDM TD T-1` / `T-4` 描述的是相邻原子 / 另一张表. 按写死的口径 "任一样本 NOT_HOLD → 不 PASS". 主人对问题 A 只回了「继续」, 没有选.
- M-9、问题 B、几处过期数字都**不挡闸**, 单列.

## G-TB 表 (誊录)
| 闸 | 判定 | 要点 | 条件 / 缺口 |
|---|---|---|---|
| G-TB1 | MET_WITH_CONDITION | 范围内 174 节残留 0; PDF_TYPO 174 条登记都非空; ack 来源 122 + 22 + 19 + 6 + 4 + 1 = 174, "(未归因)" 0 | 4 条 TD 原子的登记实际描述的是邻近原子, "每条有登记" 在实质上对这 4 条不成立 → 挡 PASS; 问题 B 那 1 条另列 |
| G-TB2 | MET (U-3 范围内口径) | 范围内 174/174; 字面 157/174 | 取决于 U-3 A |
| G-TB3 | MET_WITH_CONDITION | U-1 B 9860/9933 = 99.2651% ≥ 99.0192%; strict 95.5301%; mapped 99.3509%; 内容 90.6188%; 等于预演值 | 按 PLAN 字面 strict 不达标, 过闸完全依赖 U-1 B; 现值比主人上一轮确认时低 0.0039 个百分点, 但第二轮那一页给主人看过新值 |
| G-TB4 | MET_WITH_CONDITION | census 497 表 / OK 309 / DIFF 38 / diffs 148; C3 60 张 = 49 + 4 + 7 已逐表结案, verifier 审过; 审查者抽核 #1、#16 与 DS:292 | census 原始输出是 RED, 靠 "PDF_TYPO 登记例外" 过闸; 148 处差异的基数沿用 T2 分诊 [采信] |
| G-TB5 | MET_WITH_CONDITION | R2L auditor N=33 (seed 20261134) 33/33; `audit_matrix.md` 已补齐 T3 / T4 行 | N 没写在规格里, "事先定" 的证据只有派发时的 trace 行与 auditor 自述 (33 > PLAN §5.3 公式值 16, 是从严) |
| G-TB6 | MET (U-4 A / M-6) | 新增 5414 行全部溯源, UNEXPLAINED 0, NOTE_EXEMPT 5 条各命中 1 次 | C 层抽样过闸 (U-4) |
| G-TB7 | MET | live docs 42 | 审查者未复跑 |
| G-TB8 | MET | R2L writer `oh-my-claudecode:executor` / reviewer `oh-my-claudecode:code-reviewer` / auditor `oh-my-claudecode:verifier` 三种不同; reviewer 在隔离副本里整链跑了四遍, md5 都是 `16024ac0…` | `t4_r2l_relabel.json` 由一次性脚本生成, 生成人未写明 (内容与主人选的清单逐条一致); 上一任会话的时间戳问题依旧 |
| G-TB9 | MET_WITH_CONDITION | t3_mutation M0 / M2 / M7 绿、M1 / M3-M6 红, 真 KB md5 不变; t0_mutation_head 13/13 施加, EXPECT 8/8, M4 7/7, ALL MATCH; M-8 主人第二轮已追认 | `t4_t0_refresh.md` §6 的基线重建没有送独立审查 (脚本与用例未改, 风险低) |

## 样本层 (誊录)
- 自挑 10 条: `sv20_p0052_a012`、`sv20_p0058_a005`、`sv20_p0069_a001` (R1-row); `sv20_p0003_a011` (v2.0-TOC); `ig34_p0043_a010` (仅文本层, 渲染页没看)、`ig34_p0278_a015`、`ig34_p0147_a025` (registered-typo); `ig34_p0083_a020`、`ig34_p0304_a026`、`ig34_p0316_a023` (范围外) — 全部 HOLDS. 审查者说明: 其中 6 条也在 R2L auditor 的 33 条里, 真正独立于 auditor 的是 4 条.
- 仍未处理: `ig34_p0412_a006` / `a007` / `a008`、`ig34_p0413_a010` = **NOT_HOLD** (应为 EXACT; PDF `ig34_p0412.txt:14-16` 三句本身无误, 登记的 "assessments.." 在 :17; p413:21 印 TDTGTPAI 是对的, 笔误在 p414:29); `ig34_p0293_a038` = UNVERIFIABLE (折行处有没有空格文本层判不了; KB 两种情况下都对).

## C 项 (裁定来源; 誊录)
1. 上一轮四件事: 作 G-TB1 "用户 ack" **足够**; 作 G-TB3 U-1 B 口径认可 **足够** (第二轮那一页明确以 U-1 B 为过闸口径并给出改后数字, 主人作了正面回答); T4.2 改口径并关闭 **足够, 带已公开的局限**. 局限照实保留: 上一任会话记录、一个词加多选勾选、没有截图.
2. 第二轮三条原话: 「是，都按建议」是对逐项列出的追问的直接回答, 支撑 78 条改标与问题 1-9 的登记 **足够**; 「继续」没有回答问题 A / B, 主控没有替主人选, 处理得当; M-9 **需主人追认**, 不挡闸.
3. 人工判定来源可核性 (attempt 2 判 "不足"): 现在 **足够 (带局限)** — 仍然没有截图或会话原文, 无法从仓库外独立核对.

## D 项 (attempt 2 缺口现状; 誊录)
已关: C3 逐表结案清单; census 变化逐表说明; t0_mutation 在现 KB 重证; pre_existing 58 单独核 (现 52); FIG 11 逐条核; "规则 0 抽中" 各类; PLAN 修订; audit_matrix 缺行; `t4_user_decisions.md` 与 `t4_human_verdicts.md` 的矛盾. **部分关**: ATOM_ERR / PDF_TYPO 补抽 — PDF_TYPO 174 条全部有人看过但留下 4 条 NOT_HOLD + 1 条 UNVERIFIABLE; ATOM_ERR 的 S1-R1 157 条里约 83 条没被单独看过 [审查者采信 / 推算]. **仍开 (LOW, 主控改)**: 5 处过期文字 — `_progress.json` steps.T4.1 / T4.2; `audit_matrix.md:7` "M-8 待追认"; `t4_supp_fullcheck.md:12` 复跑注释 "pre_existing 58"; 同文件 :98 "PDF_TYPO 149" 无时点说明; `HANDOFF.md` 下午那一节的 "M-8 待追认" (该节标题没标 "(历史)").

## E 项 (未审项与未决项的处置; 誊录)
| 项 | 挡闸? | 由谁补 |
|---|---|---|
| 问题 A (4 条多标) | **挡闸** | 主人选 A1 / A2. 若 A1: writer → reviewer 改台账, 改 `t4_supp_report.py` 断言, 重建 T0 基线, 再做一次 delta 闸审 |
| 问题 B (`ig34_p0293_a038`) | 不挡, 记已知局限 | 主人 (B1 / B2), 可以之后再定 |
| M-9 | 不挡, 需主人 | 主人追认 |
| M-7 里 p0362_a010 那处更正 / 第一节的局限 / 第二轮三句话 / 99.2690 → 99.2651 | 不挡 | — |
| 只抽样的几类; 约 80 条标签级别项、O68-O71; trace 整点时间戳 | 不挡, 记已知局限 | 留后续 |
| 一页第 3 稿未审; T0 §6 重建未审; 改过的 `t4_supp_report.py` 与两份汇总; 新脚本; 文档更新 | 不挡 | T0 重建可选独立复跑一次; 过期文字主控改 |

审查者没能核的 (原文 §6): 所有渲染页 (含 p43 字形); 各命令没有复跑; 第一轮主人原话的会话原文; 148 处 census 差异逐条对登记; ATOM_ERR S1-R1 剩下的约 83 条.

## 主控对 attempt 3 的处理 (2026-11-27; 不改判)
- 5 处过期文字 (D 项 LOW) 已改: `_progress.json` steps.T4.1 / T4.2; `audit_matrix.md:7`; `scripts/t4/t4_supp_report.py` 两处措辞加时点说明后重生成 `t4_supp_fullcheck.md`; `HANDOFF.md` 下午那一节标题加 "(历史)".
- 挡闸项 (问题 A) 是主人的决定, 主控**没有替他定, 台账没有再动**; 2026-11-27T09:57:27Z 在聊天里再次向主人提问 (说明这是总闸唯一的挡闸项; 提问要点记在 `t4_owner_confirmation.md` "主控的第三次提问"), 回答将逐字记入同一文件; 同时向协调方报了阻塞.
- G-TB5 的 "N 没写在规格里": 属实 — 主控是在派发 auditor 的消息里定的 N=33 与 seed, 没有写进 `subagent_prompts/t4/t4_round2_ledger_spec_v1.0.md`; 记为已知不足.
- 审查者指出的 "ATOM_ERR S1-R1 约 83 条没被单独看过" 不是本轮新开的缺口 (U-5 整类确认 + C7 38 全检 + triage 74 全检的既有状态), 记为已知局限, 留给主人 / 协调方决定是否再加一轮.
- (后续, 同日) 主人直接回答 「A1、B1、追认 M-9」 (`t4_owner_confirmation.md` 消息 4) → R3L 批把这 4 条改回 EXACT (提交 `d794fb6`; `t4_round3_ledger_W.md` / `t4_round3_ledger_review.md`) → T0 基线重建 (`t4_t0_refresh.md` §7) → 对这一处的 delta 闸审见下一节.

---

# §attempt 3 delta (2026-11-27) — **PASS** (T4.1 总闸; attempt 3 + 本次 delta 合并)

> 审查: `feature-dev:code-reviewer` (opus) **另一个新实例** (不是做 attempt 3 的那个), 只读, 无 Bash; brief `subagent_prompts/t4_gate_reviewer_v3.1.md`; 对象 HEAD `c09439c` (KB 树 `63f857774a42cfaa71798705ad40ab51bc5e378a`; 台账 md5 `438098704becc84eda01a925b80defaa`; 预跑日志 `work/t4/gate_prerun.log` 在 `b97b1da` 上生成). 范围只限 attempt 3 之后的变化.
> **报告原文** (脚本从会话记录原样取出, 主控未改一字): `evidence/t4_gate_raw/attempt3_delta_report.md`. 下面是主控的要点誊录, 不改判 (规则 D); 与原文有出入以原文为准. PASS 的含义仅限 T4.1 总闸; push、打 tag、T4.3 都不在范围内.

## 结论: PASS
- attempt 3 的唯一挡闸项 (问题 A) **已关**, A 的四问都成立: ① 主人消息 4 「A1、B1、追认 M-9」点名了选项, 是正面回答, 够用 (局限同前: 一句短话、无截图); ② 4 条原子审查者只用文本层逐条重判 **4 / 4 HOLDS** (渲染页没看), 现标签 EXACT、规则 live-hit、不再挂登记; ③ 真正有笔误的相邻原子 `ig34_p0412_a009` / `ig34_p0414_a013` 仍是 PDF_TYPO, 登记都在; ④ B1 已落实 (标签没动; "无法判定" 写在 `t4_user_decisions.md` §000c、`t4_supp_fullcheck.md`、登记表原有的 note).
- R3L 标签变化恰好 4 条 (逐字节相同是 [读日志]); 审查者自己 Grep 的计数全部吻合 (PDF_TYPO 170 / EXACT 4710 / `T4-R3L` 4 行 / PDF_TYPO 空登记 0 条 / 登记表 274 行). "由现有判定路径得出" 属实, 但要说准确: 不是事后覆盖标签, 是**有断言约束的成因层排除** (按清单把这 4 条的 K3b 触及拿掉后走现有判定) — 即 M-10 ③. 审查者没读 `decide()` 本体, "落到 live-hit 分支" 是采信 R3L reviewer.
- 没有哪条 G-TB 因 R3L 变成 NOT_MET; 没有发现新的挡闸项.

## 有变化的闸 (誊录; 其余沿用 attempt 3)
| 闸 | 现判 | 要点 |
|---|---|---|
| G-TB1 | MET_WITH_CONDITION (条件缩小) | 174/174 残留 0; PDF_TYPO 170 条每条有登记; ack 来源 118 + 22 + 19 + 6 + 4 + 1 = 170, "(未归因)" 0; attempt 3 对这 4 条的实质性缺口已消失, 剩下的条件只有 U-5 整类代裁 |
| G-TB3 | MET_WITH_CONDITION (沿用) | U-1 B 99.2651% 不变; strict 95.5301% → 95.5703% 是上升; mapped 99.3511%; 内容 90.6227% |
| G-TB5 | MET_WITH_CONDITION (新条件) | R3L 没设语义 auditor; 语义上的独立核验有三次 (第三轮 tracer、attempt 3 审查者、本次 4 / 4 文本层重判); 不挡闸 |
| G-TB8 | MET_WITH_CONDITION (新条件) | 按 PLAN 字面 "每批 3 个不同 subagent_type", R3L 在 trace 里只有 2 种 (executor / code-reviewer); 第三个不同类型的独立核验可由本次 delta 审查 (`feature-dev:code-reviewer`) 充当, 要主控补上本次的 subagent_done 行; 随 M-10 ⑥ 一起由主人追认 |
| G-TB9 | MET_WITH_CONDITION (沿用) | t3_mutation M0 / M2 / M7 绿、M1 / M3-M6 红; t0 13/13 施加, ALL MATCH; §7 的基线重建没有送独立审查 |

## 过期文字 (誊录)
attempt 3 指出的 5 处都已改 (其中两处改得不彻底 → 并入下面 LOW-1 / LOW-2). 本次新发现 8 条 LOW: LOW-1 `_progress.json` steps.T4.1 仍写 "主人未答"; LOW-2 `audit_matrix.md:7` 与 `PLAN.md` 口径注只引 `t4_t0_refresh.md` §6 没引 §7; LOW-3 `t4_supp_fullcheck.md:119` 仍写 "现共 174 条 … 待主人定"; LOW-4 `t4_user_decisions.md` §000c 引言只写到消息 3; LOW-5 `audit_matrix.md` 三行的业务判定列写 "待主人裁定 / 主人未答" 没有时点说明; LOW-6 `ig34_p0412_a006` / `a008` 已是 EXACT 但台账行还留着 06 时期的 `discrepancy` 文字与较低的 similarity; LOW-7 B1 的 "无法判定" 没写到 ack 清单的备注栏与台账那一行; LOW-8 R3L 4 行的 `ts` 早于主人决定日 (已在 M-10 ⑤ 披露).

## 处置表 (誊录)
| 项 | 挡闸? | 由谁补 |
|---|---|---|
| M-10 (R3L 的机制选择; 含 "不设 auditor") | 不挡, 需主人 | 主人追认 |
| ATOM_ERR S1-R1 约 83 条没被单独看过 | 不挡, 记已知局限, 需主人 | 主人决定是否加一轮 |
| T0 §6 / §7 基线重建未送独立审查 | 不挡 | 可选: 独立复跑一次 |
| 改过的三个脚本与两份汇总; 这次的文档更新 | 不挡 | 主控改字 (LOW-1 ~ LOW-5) |
| R3L reviewer 的 5 条 LOW 没回 writer 修 | 不挡 | — (主控的处理合理) |
| attempt 3 已判 "不挡, 记已知局限" 的各项 | 不挡, 同意 attempt 3 | — |

审查者没能核的: 渲染页; 所有命令 (没有 Bash); `decide()` 本体; 消息 4 的会话原文.

## 主控对 delta 审查的处理 (2026-11-27; 不改判)
- LOW-1 ~ LOW-5 已改 (`_progress.json`; `audit_matrix.md:7` 与三行业务判定加时点与后续; `PLAN.md` 口径注引 §7; `t4_supp_report.py` 一句措辞改后重生成 `t4_supp_fullcheck.md`; `t4_user_decisions.md` §000c 引言补消息 4).
- LOW-7: `scripts/t4/t4_ack_lists.py` 加备注表, 重生成 `t4_ack_lists.md`, `ig34_p0293_a038` 那一行末列写明 B1 与 "无法判定"; 台账那一行不动 (主控不写台账).
- LOW-6 / LOW-8 不改 (都在台账里, 改它们要再跑一批回写): 记为已知 — `discrepancy` / `similarity` 是 06 时期匹配器留下的辅助字段, 不参与任何闸; `ts` 的事已在 M-10 ⑤ 披露.
- G-TB8: 本次 delta 审查的 `subagent_done` 行已记入 `trace.jsonl` (`T4.1` attempt `3-delta`), 作为 R3L 这一批第三个不同 subagent_type 的独立核验; 是否认可随 M-10 由主人定.
- 需主人但不挡闸的两件事 (M-10 追认; ATOM_ERR 约 83 条是否加一轮): 2026-11-27T13:46:05Z 在聊天里告诉主人 (要点记在 `t4_owner_confirmation.md` "主控的第四次告知"), 并写进给协调方的完成报告 `evidence/checkpoints/t4_attempt3_report.md` §5; 主控没有替他定.
- (主控注) `evidence/checkpoints/t4_ack_lists.md` 在 delta 审查之后因 LOW-7 重生成过一次: md5 `18a2981ce5bcdb11989cfdcf6ba46a4e` → `91ad638504915b98a1fed79b40b0d719`, 唯一差别是 `ig34_p0293_a038` 那一行末列多了 B1 的备注 (`git diff` 为 1 行). `t4_round3_ledger_W.md` §7 与 R3L reviewer 原文里引的是旧值, 那两份原文不改.

---

# attempt 3 D 项 "ATOM_ERR / PDF_TYPO 补抽 = 部分关" 的后续: 加查 (2026-11-27 夜; 主控登记, **不改判**)

- 主人选了 "加查" (协调方转述; 来源如实记在 `t4_owner_confirmation.md` "第三个会话" 一节). 新会话主控 (任务 `task_5b6b27f6c68d`) 执行, 汇总 `evidence/checkpoints/t4_atomerr_fullcheck.md`.
- 确切条数: S1-R1 157 条 = 此前已逐条判过 80 (补检 74 + 总闸样本 5 + T4.2 预筛 1) + **从未逐条判过 77**. attempt 3 估的 "约 83" = 157 − 74. 本轮全检 83 = 77 (首次) + 6 (盲复检). 筛法 `scripts/t4/t4_atomerr_sample.py`.
- 审查者 `oh-my-claudecode:tracer` ×4 (新实例; 口径 `subagent_prompts/t4/t4_atomerr_s1r1_v1.0.md` 派发前提交 `bf303d8`): **成立 82 / 不成立 1 / 判不了 0**; 盲复检 6 / 6 与先前判定一致. 原始结果 `evidence/t4_atomerr_raw/pack_{1..4}.md`.
- 不成立的 1 条: `ig34_p0124_a001` (ATOM_ERR, S1-R1) — 原子与 PDF 逐格一致, 没抽错; KB 逐字承载 → 按定义应为 EXACT. 另一类型的独立审查者 (`general-purpose`) 盲复看结论相同 (`evidence/t4_atomerr_raw/second_look.md`). 台账副本实算: U-1 B 不变 (99.2651%), strict +1 条 (95.5804%).
- **另有 8 条取决于口径, 未裁**: 登记 `B-CE T-2` 那组 (E18-E25) 原子与 PDF 只差 USUBJID 里的一个空格; 两位审查者都判成立, 其中一位写明 "若代码值内部的空格算空白归一则 ① 不成立". 这是 brief 两句话之间的缺口 (主控写的 brief), 列为问题 D (`t4_atomerr_fullcheck.md` §5a; D2 = 改 EXACT 时 strict 再 +8 条, U-1 B 不变).
- **台账没改** (md5 `438098704becc84eda01a925b80defaa`), KB 没改. 改不改 = 问题 C / 问题 D, 等主人直接定. 按写死条款本轮记 "不通过", 归档 `evidence/failures/step_T4.AE_attempt_1.md`.
- 这一项的现状事实: ATOM_ERR 197 条与 PDF_TYPO 170 条现在每一条在各轮独立审查的原始结果里都有自己的判定行 (`scripts/t4/t4_atomerr_coverage.py` 扫结果表: 197 / 197、170 / 170); ATOM_ERR 里有 1 条已判不成立而标签未改. **"部分关" 改成什么状态由总闸角色 (`feature-dev:code-reviewer` 新实例) 或协调方判, 主控不判** (规则 D). 主人选 C1 并改完后, 可与那一处的 delta 闸审一并判.
- 对已通过的 T4.1 总闸的影响, 主控只陈述事实不下结论: 这 1 条与 attempt 3 当时挡闸的 4 条多标 PDF_TYPO 是同一种情况 (已证实不成立的标签留在台账里), 方向同样是改回 EXACT、同样不影响过闸口径数字. 是否影响 PASS 的有效性, 同样由总闸角色 / 协调方判.

---

# 加查与 R4L 之后的 delta 闸审 (2026-11-27 夜; 誊录; 原文 `evidence/t4_gate_raw/attempt3_delta2_report.md`)

> 审查者 `feature-dev:code-reviewer` (opus) **另一个新实例**, 只读, 无 Bash; brief `subagent_prompts/t4_gate_reviewer_v3.2.md` (判定口径派发前写死); 对象 HEAD `6d89fb9` (预跑日志 `work/t4/gate_prerun.log` 在 `2c61ea5` 上生成). 下面是主控的誊录与计数, 结论以原文为准; 主控不改判.

## 结论: PASS (仅指 T4.1 总闸; attempt 3 + delta + 本次合并看)
- A (`ig34_p0124_a001`): 主人消息 5 足以作为改标依据; 审查者按列对齐重判 = HOLDS (原子没抽错, KB `ML/examples.md:42` 逐字承载, EXACT 成立); 标签由现有 `live-hit` 路径判出, 是带断言的成因层撤销, 不是事后覆盖.
- B: R4L 清单外变化 0 (恰好 1 条改标 + 4 行只改 `registry`); 4 条补的登记指针在登记表里都存在且对得上; writer / reviewer 类型不同; reviewer 的 LOW 与主控的处理判 "合理".
- C: 没有哪条 G-TB 变成 NOT_MET. G-TB3 现值 U-1 B 99.2651% (不变) / strict 95.5804% (上升). **G-TB8**: R3L 那一批的字面条件已由 M-10 追认关闭; R4L 这一批 trace 里只有 executor / code-reviewer 两种类型, 第三种由本次审查充当 (须补 trace 行), 且 R4L 的机制选择尚未登记 → 按 R3L 先例判不挡闸.
- **D ("ATOM_ERR / PDF_TYPO 补抽", attempt 3 判 "部分关"): 现状态 = 已关 (带局限)**. 筛法与 157 = 74 + 6 + 77 对账成立; 口径确在派发之前提交; 审查者类型独立; 盲复检 6 条一致; 审查者自己抽核 12 条 (含 `B-CE T-2` 2 条、涉登记 2 条、表格行与非表格行) + 另 4 条, 与加查审查者**全部一致**. 局限: 渲染页没看; S1-R1 以外各条的 "判成立" 采信前几轮记录; 加查汇总没有送独立审查; "每条都有判定行" 证明的是每条都被看过, 不等于每条都判成立.
- E (问题 D 的处理): 足够. D1 口径与标签定义、与登记 `B-CE T-2`、与两位审查者当时的判定自洽; 登记位置与写法够用. 两处缺口 (不挡闸): 上级 brief `t4_supp_fullcheck_v1.0.md` 那两句话仍没写先后 (LOW-7); D1 没说 "值内空格恰好落在折行处" 时哪条优先 (建议主人以后补一句).
- F (M-10): 主人的追认足以关掉 delta 报告里 G-TB8 的字面条件 (对 R3L); 不覆盖 R4L.
- H / I: 各未审项都判 "不挡闸, 记已知局限"; 前两份报告判 "不挡闸" 的各项同意, 现状未变.
- **push 之前须处理的事项** (原文): ① 在最终 HEAD 上重跑 `scripts/t4/t4_prepush_check.sh` 并补 `t4_prepush_check.md` "§3 最终一次"; ② 把本报告原样存档并在 trace 补 `subagent_done` 行 (兼作 R4L 批第三个不同类型的独立核验记录); ③ 在 `t4_user_decisions.md` §000b 登记 M-11 (R4L 的机制选择). 都是文字 / 记录类.
- 需主人但不挡闸: M-11 追认 (可事后告知); D1 的折行边界.
- LOW 9 处 (过期 / 小矛盾), 见下.

## 主控对这次审查的处理 (不改判)
- ② 报告已原样存档 (`evidence/t4_gate_raw/attempt3_delta2_report.md`); `trace.jsonl` 已补 `T4.1` attempt `3-delta2` 的 `subagent_done` 行, 注明兼作 R4L 批第三个不同 subagent_type 的独立核验.
- ③ M-11 已登记在 `t4_user_decisions.md` §000b (待主人追认; 不挡闸; 在聊天里告知主人, 记录在 `t4_owner_confirmation.md`).
- ① 推送前检查在最终 HEAD 上重跑, 输出记在 `t4_prepush_check.md` §3 "最终一次".
- LOW-1 (`_progress.json` G-TB8 / G-TB9)、LOW-2 (`audit_matrix.md:7` 补 §8)、LOW-3 (`HANDOFF.md` 上一节标题改标 "历史")、LOW-4 (`t4_user_decisions.md` §000c 引言补消息 5)、LOW-5 (`t4_atomerr_fullcheck.md` 补 "有判定行 ≠ 判成立; 现 196 是那 197 的子集")、LOW-7 (`subagent_prompts/t4/t4_supp_fullcheck_v1.0.md` 文末加指向 D1 的补注, 正文不改)、LOW-9 (`PLAN.md` 状态行压短): 已改.
- LOW-6 (`evidence/t4_atomerr_raw/second_look.md:21` 把 su.xpt 写成 19 列, 实际 18 列): 那是审查者原文, 不改; 在这里更正, 不影响判定.
- LOW-8 (消息 5 的收到时间与提交 `cd24cc2` 只差约 1 秒): 事实是 — 收到消息后的第一条命令先取时钟, 同一条命令接着写记录并提交, 所以两个时间挨着; 本环境里时钟走得比实际耗时慢 (同一会话里审查者耗时十几分钟的调用, 前后 `date -u` 只差一两分钟). 记录里 "收到后立即取的时钟" 指的就是这个取法. 记为记录形式的已知局限, 不改原记录.
- D1 的折行边界: 记为后续项 (`HANDOFF.md` 最后一节), 等主人以后补一句; 现有台账里只有 `ig34_p0293_a038` 一条碰到这个边界, 它已按主人 B1 单独处理.
