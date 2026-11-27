<!-- 原样誊录: feature-dev:code-reviewer (opus) T4.1 闸门证据层审查回复, 2026-11-27. 主控未改动内容 (仅把 HTML 转义 (&gt; &amp;) 还原为原字符; $T = .work/10_tier_b_repair). -->

# T4.1 总闸证据层审查 (feature-dev:code-reviewer, 只读)

**结论: T4.1 现在不能判 PASS。** 就算样本全部 HOLDS 也不行: G-TB1 和 G-TB2 按 PLAN 字面没过; G-TB3 按 06 公式字面算是 96.07%, 也没过; G-TB1 要求的用户 ack 还一条都没有。

我没有 Bash, 下面的核对分两类:
- **[G] 我用 Grep/Read 亲自核过**: ledger 各 verdict 计数、`"phase": "TB"` 计数、triage 各类计数、样本的层/终态/规则分布、trace 里每批的角色。
- **[转] 转述证据文件, 我没复跑**: md5、live docs、变异结果、170/174、主控给的逐行转移表。

我做过的一致性检查: 主控列的 23 类转移合计 1890 行, 加末尾新增 5 行 = 1895。ledger 中 `"phase": "TB"` 的计数也是 1895 [G], 和 `step_T3_audit.md:456` 一致。

## 1. G-TB1..9

| 闸 | PLAN 阈值 | 实测值与证据 | 判定 | 条件 / 缺口 |
|---|---|---|---|---|
| G-TB1 | §5.0 内残留 PARTIAL/MISSING/ERROR/MISPLACED/LOCATE = 0; ATOM_ERR/PDF_TYPO/FIG 每条有登记 + 用户 ack | 残留 1 条 `ig34_p0056_a006`。ledger 第 1737 行仍是 PARTIAL [G]; `t3_writeback_decisions.json:7835-7859` 的 rule 是 `pending_user-residual`, triage 结论 REAL_GAP (依据 R2-ack)。三份登记清单都在 `work/t3_audit_sets/` [G]。用户 ack 没有: `t4_user_decisions.md:2` 写着"草拟, 待主控审后交用户" | **NOT_MET** | ① 残留 1 条要用户裁定。R2 规定"补回原文", 但 KB 正冻结, 两者冲突; ② 197 / 122 / 11 三类清单都要用户 ack; ③ PLAN §5.0 写 FIGURE 12 条, triage 和 ledger 实际都是 11 条 [G], 要说明 |
| G-TB2 | 有内容的节密度 = 1.00; 结构父节要"所有子节达标" | 按"只看范围内子节"口径是 170/174, 按字面严格口径是 155/174 (`t3_recompute.md:49`) [转]。未过的是 §4.5.3.2 (密度 0.963) 和它的父节 §4 / §4.5 / §4.5.3, 都是 p0056_a006 一条造成的 | **NOT_MET** | PLAN 原文是"所有子节", 没限定"范围内"。按字面应取 155。改用"范围内"口径是主控在 C4 定的, 不是用户。需要用户确认采用哪个口径 |
| G-TB3 | 06 口径 ≥ 99.02% 且不下降 | strict 96.0741% / mapped 99.3578%, 我按转移分解复核过 (见 §2) | **字面 NOT_MET; mapped 过** | 06 公式照字面套就是 strict。mapped 等于新加了一个 06 没有的排除类, 没有用户 ack 记录 |
| G-TB4 | 本项目碰过的表不一致 = 0 (登记的 PDF_TYPO 例外) | 各批 reviewer 在 trace 里都留了 census 结论 (如 trace:45/52/55/63)。全局 census 只在 `50c3958` 跑过一次 (`t2_census_global_triage.md:3,9-13`): OK 311 / DIFF 37 / UNPARSEABLE 149。其中 C1 3 张后来补登记了 (SE T-1、TD T-4); C3 60 张当时"状态未知"。之后 S-CH4 人工核了 ch04 的 C3 表 (`t2_S-CH4.md:70-88`), S-CH10 的 8 张也是人工核 (`t2_S-CH10_review.md:25`) | **MET_WITH_CONDITION** | ① S-CT / S-TYPO 之后没在 HEAD 上重跑过全量 census (我搜了 t2_S-CT/TYPO*、t2_coverage_matrix、trace, 都没找到); ② C3 剩下的表 (model/02 15、EX 8、model/03 7、model/04 1、TR 1) 我没找到结案证据, 要补一份 C3 逐表结案清单 |
| G-TB5 | 抽检独有丢失 0, 忠实度错 0; 1 条错 → 该批重做 | `audit_matrix.md` 各批最终都是 PASS。3 个 FAIL 都重做过: B-ch04 :15→:23、B-ch02 :18→:19、B-TA :36→:38, 失败也都归档在 `evidence/failures/` | **MET** | 小问题: B-AE 只核了 0/9, 按字面不足 N=10 (:21); "业务判定"列全是"待主控"; T0.4 行还写"待跑" (:7); 表里没有 T3 / T4 的行 |
| G-TB6 | 新增 KB 行能在 PDF 找到 (子串, 或 reviewer 签字的结构行) 100% | 5336 行未溯源 0 (`t3_recompute.md:461-470`) [转]。但 C 层 1370 行是 writer 自己定义的类, 只抽了 30 行 + HEADING 21 行全量 (`step_T3_audit.md:147-164`)。MERMAID 322 行 T3 没有独立证据 (:157), TABLE_TOKENS 680 行是宽口径 | **MET_WITH_CONDITION** | C 层既不是"子串", 也不是"逐行签字"。字面 100% 不成立, 只靠抽样接受, 要总闸或用户明确接受这个口径 |
| G-TB7 | live docs ≤ 42 | T3 时是 42 (`t3_recompute.md:51,454`; `step_T3_audit.md:460`) [转] | **MET_WITH_CONDITION** | 之后新增了 T4 未跟踪文件 (t4_human_sample.md、work/t4/、evidence/t4_gate_raw/)。evidence 文件以前就让计数变过 (`audit_matrix.md:23` 有 45 的先例)。要主控贴一次当前的 `python3 tools/check_links.py 2>&1 \| grep "live docs"` 输出 |
| G-TB8 | 每批 3 种不同 subagent_type 的 subagent_done; 主会话无写 KB 记录 | 批次表 59 批 (`t2_batch_table.md:24-82`) + B-REL (D7 新开) = 60 个 B 批, 加 22 个 S 批, 每批 executor / code-reviewer / verifier 都齐 (trace:43-405) [G]。`agent: main` 只有 user_ack / step_note 6 行 (trace:3,12,26,38,42,48) [G] | **MET** (字面) | trace 本身不能独立证明"主会话没写 KB": ① 有"回填 (主控)"行 (trace:147/155/156), 而且顺序排在 verifier 之后。我核过 :147 对应的改动已被 :144 的 delta 复审覆盖; ② T3 只有 3 行 (:406-408), 时间戳是整点, 属于事后回填; ③ U1-U8 不在 trace 里。要更强的证据, 得拿各 KB commit 的改动文件和批次文件清单对一遍 |
| G-TB9 | 3/3 变红, 复原后变绿 | M1 / M2 / M3 都红, RESTORE 绿 (`t0_mutation.md:39-50`); 预期表 exit 0 (:115-123); census v2 的变异 (:171-182); 用户 ack 在 trace:12; T3 补测 M1、M3-M6 红 [转] | **MET** | T0 的变异跑的是 T0 时的脚本版本。fp_match / t3_common 之后改过, 建议收尾时在 HEAD 上重跑一次 `t0_mutation.sh` |

## 2. 覆盖率口径 (B)

**我自己核过的数字** [G]:
- 现 ledger: PARTIAL 639; ATOM_ERR + PDF_TYPO + FIG = 330; IE 2507; MISPLACED + ERROR = 259 (即 197 + 62)。
- 06 报告 (`p6_t5_nonprose_update_report.md:28-32`): 分子 Covered = EXACT + EQUIV + PARTIAL + MISPLACED = 10298, 分母 = 10400 (行数减 IE), 得 99.02%。

**转移分解** (按主控给的转移表, 分子和分母都对上了):

| 组 | 行数 | 对分子 | 对 strict 分母 | 对 mapped 分母 |
|---|--:|--:|--:|--:|
| 已覆盖 → 已覆盖 (P/E/M→EXACT/EQUIV) | 963 | 0 | 0 | 0 |
| 已覆盖 → IE (PARTIAL 490 + MISPLACED 4) | 494 | −494 | −494 | −494 |
| **已覆盖 → 新三类** (ATOM_ERR 194 / PDF_TYPO 121 / FIG 4) | **319** | −319 | 0 | −319 |
| IE → 已覆盖 | 72 | +72 | +72 | +72 |
| IE → ATOM_ERR | 2 | 0 | +2 | 0 |
| 未覆盖 → 已覆盖 (ERROR 30 + MISSING 2) | 32 | +32 | 0 | 0 |
| 未覆盖 → 新三类 (MISSING→FIG 7 + ERROR→ATOM_ERR 1) | 8 | 0 | 0 | −8 |
| 末尾新增 (4 条已覆盖 + 1 条 PDF_TYPO) | 5 | +4 | +5 | +4 |
| **结果** | 1895 | 9593 | 9985 → 96.07% | 9655 → 99.36% |

**(1) 哪个口径与 06 同口径?**
- 按公式字面, strict 才是同口径: 06 只排除 IE, 新三类既不在分子里, 也不是 IE。
- 但按定义, ATOM_ERR 和 PDF_TYPO 都是"KB 承载了 PDF 内容" (前者是原子抽错, 后者是 PDF 笔误)。这 319 条在 06 里本来就算分子。strict 把它们算成未覆盖, 违背了 06 的本意。
- 所以两个口径都不是严格的同口径。

**(2) 99.02% → 96.07% 的下降来自哪里?**
- 几乎全部来自那 319 条"已覆盖 → 新三类": 它们让分子少了 319, 分母不变, 正好 −3.19 个百分点。
- 如果把这 319 条仍算覆盖, 结果是 9912/9985 = 99.27%。
- 其余几组的影响都很小。494 条转 IE 只拉低约 0.05 个百分点 (从覆盖项里拿走), 这批 IE 用户已在 R4 ack。

**(3) mapped 过闸只是因为分母定义变了吗?**
- strict 和 mapped 的差距完全来自定义: 分母差了 330 行。
- 但 mapped 比 99.02% 高出的那部分是真实的: 未覆盖从 102 降到 62。其中 32 条是真修回来的, 8 条是改归 FIG / ATOM_ERR。
- 把覆盖项移进排除类, 只会让 mapped 变低, 不会抬高它。mapped 现在等于 1 − 62(ERROR)/9655。

**(4) 剩下的 PARTIAL / MISPLACED / ERROR 意味着什么?**
- PARTIAL 639 条里, 638 条在 §5.0 范围外, 1 条是 p0056_a006 (这个拆分是转述 T3 的残留数, 不是我核的)。MISPLACED 197 条也在范围外。
- 这些行在每个口径里都算"已覆盖"。所以不管是 99.36% 还是 96.07%, 意思都只是"KB 里有对应内容, 可能不完整或放错了位置", 不是"逐字或等价"。
- ERROR 62 条是所有口径下唯一的未覆盖项。
- 建议同时报一个严格内容指标 (EXACT + EQUIV) / mapped 分母: T3 前 7983/10400 = 76.76%, 现在 8757/9655 = 90.70%。这是审查者自算的, 没用脚本跑。

**(5) 建议怎么过闸**
- 用 mapped 过闸, 或者用"ATOM_ERR / PDF_TYPO 算覆盖、FIG 算未覆盖"的 99.27% (审查者推导值)。
- 同时必须并列报告 strict 96.07% 和内容指标 90.70%, 并写明范围外还有 PARTIAL 638 / MISPLACED 197。
- **没有任何用户认可 mapped 的记录**: `t1_user_ack.md` 和 `t2_post_user_ack.md` 里都没有 G-TB3 / mapped / strict 相关内容 [G]。`t3_recompute.md:515` 仍写着"需要确认采用 mapped"; 各 attempt 的"[闸, mapped]"标注只是主控在 C4 的裁定。
- 另外, mapped 用到的 ATOM_ERR / PDF_TYPO 标签里有一部分没逐条证明过。`t3_recompute.md:127-128` 自己写明: C7 的 38 条"原子不在 PDF 窗内"判 ATOM_ERR 并非逐条证明; S-TDM TD T-1 有 2 条可能多标。

## 3. 抽样设计 (C)

- **N=72 的分层**: 符合 PLAN 字面, 即 5 个 triage 类各 12 条加对照 12 条 (gate_sample 第 1-72 行) [G]。种子 20261127 已记录, 抽样前先排序, 结果可复现。分层按 triage 类、不按终态, 这一点也和 PLAN 一致。
- **对照层取法**: 符合 Q9 原意 (§5.0 范围内、非 HEADING、不在 D 中、T3 前后都是 EXACT/EQUIV)。有两处欠缺:
  - T3 的 direct_hit 已经查出 58 条 pre_existing, 即"P4a 标的 EXACT 在 T2 前的 KB 上也不命中", 正是 Q9 要找的那种问题。随机从约 1700 条里抽 12 条, 期望只能抽到不到 1 条。建议这 58 条单独成层或全检。
  - stock EQUIVALENT 无法用指纹复验, 而 Q9 写的升级路径是"扩为全量指纹复验", 对 EQUIV 不适用, 需要另定。
- **补充层 SUPP**: 方向是对的, 它正好对着 mapped 排除掉的那批原子。但力度太弱: ATOM_ERR 4 条 + PDF_TYPO 4 条, 0 错时 95% 置信上限约 31%, 撑不起 3.2 个百分点的口径决定。另外它只抽 triage 之外的原子, 也没有 EQUIV / IE 层。建议 ATOM_ERR / PDF_TYPO 合计扩到 30 条以上, 重点放 C7-atom-not-in-PDF 38 条和 c′ 类。
- **完全没被抽到的**:
  - 终态 FIGURE_DEFERRED 11 条, gate 和 human 都是 0 条。
  - triage 类 ATOM_ERR / RELOCATE / LOCATE (77 条) 和 FIGURE (11 条), 共 88 条, 不在任何一层 [G]。
  - 按规则看, 抽中 0 条的有: `T1-two-agent+T2-rework` 13 条、`T2-fix+deltaRereviewPASS+auditPASS` (即原 CONDITIONAL 三批)、`live-hit(was-IE-ack)` 18 条、`C1-manual` 3 条、`C7-K4-rereview` 2 条 [G, 按 gate 的 rule 字段]。
- **人工 30 + 风险 12**:
  - 互斥是对的 (通过 `used` 集合实现)。PLAN 写的是"VALUE_DIFF+IE 10", 拆成 5+5 是主控的解释, 要写进 checkpoint。
  - 加上风险层后人工总数是 42, 不是 PLAN 的 30, 要在 T4.2 的 hard checkpoint 上告知用户。
  - 风险层按 8:4 抽, 而总体是 442:66, 偏重"原子节无编号"那一类。可以接受, 但要注明。
- **排除项**: MANUAL_01/02 没有 ledger 行, 排除合理; p0056_a006 作为单独的用户项排除, 也合理。小问题: ledger 有 11 个重复 id, 用 dict 读取时取最后一行, 如果重复行的 verdict 不同, 样本终态可能不准。

## 4. 审查角色 (D)

在 `$T` 全目录 grep `feature-dev` [G]: **trace.jsonl 里出现 0 次。** 只出现在 PLAN:147、HANDOFF:21、_progress:8、本 brief, 以及 T4.1 自己的 `evidence/t4_gate_raw/pack{1,2}.md`。结论: 本项目其它环节没用过这个角色。

## 5. T4.1 能否在样本全部 HOLDS 时判 PASS

**不能。** 样本全部 HOLDS 只能说明"已抽样的终态成立"。最多可以判"CONDITIONAL: 证据层齐, 等用户裁定"。转 PASS 之前必须做完下面这些:

**要用户裁定的:**
1. `ig34_p0056_a006`: 补回原文 (要解冻 KB)、接受成 EQUIVALENT, 还是转为登记例外。这一条关系到 G-TB1 和 G-TB2。
2. ATOM_ERR 197 / PDF_TYPO 122 / FIG 11 三份清单的 ack, 以及 `t4_user_decisions.md` 里 A1-A6 的 A/B 选择和 B 组 keep-correct 的知悉 (G-TB1)。
3. G-TB3 用哪个口径 (mapped / 99.27% / strict), 并同意并列报告 strict 和内容指标。
4. G-TB2 结构父节用"范围内"还是字面严格口径 (170 vs 155)。
5. G-TB6 的 C 层 (MERMAID 322 / TABLE_TOKENS 680) 是否接受按抽样过。

**主控要补的证据:**
- HEAD 上重跑全量 census, 附 C3 结案清单 (G-TB4)。
- 当前的 live docs 输出 (G-TB7)。
- HEAD 上重跑 `t0_mutation.sh` (G-TB9, 建议)。

**文档要更新的:**
- `step_T3_audit.md:4` 顶部状态还写着 FAIL, 实际终审是 PASS (:479)。
- `t3_recompute.md:4` 的状态行还是 writer 时期的。
- `audit_matrix.md` 的 T0.4 行还写"待跑", 也缺 T3 / T4 的行。

**样本外顺手发现的 KB 问题 (低优先级, 不修):** `chapters/ch02_fundamentals.md:158`、`:167` 是 KB 自拟的标题, 但没有 D6 标注 (来源 `step_T3_audit.md:162`)。
