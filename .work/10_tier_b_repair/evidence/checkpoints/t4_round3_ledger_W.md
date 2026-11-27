# T4 问题 A 改台账 (R3L) — writer checkpoint
<!-- chain: E (plans) -->
> 状态: writer 已完成 (2026-11-27, `oh-my-claudecode:executor`, attempt 1). 等 reviewer 复跑逐行核 (规则 D). 本文不给自己判 PASS.
> 规格: `subagent_prompts/t4/t4_round3_ledger_spec_v1.0.md`. 依据: 主人 2026-11-27 直接回答 "A1" (`evidence/checkpoints/t4_owner_confirmation.md` 消息 4). 语义依据: 第三轮审查者 `evidence/t4_round3_raw/pack_10.md:29-32` (T237-T240 NOT_HOLD), 总闸 attempt 3 审查者 `evidence/t4_gate_raw/attempt3_report.md:57-58`.
> 结果: 台账 md5 `16024ac09721cb3f8519cd68fa455196` → **`438098704becc84eda01a925b80defaa`**. 源头整链跑了四遍 (runA / runB / runC / runD), 台账 / rules / decisions 等产物 md5 一致 (keep 清单在 runC 之后因 `_note` 生成方式小修换过一次 md5, 见 §3 末). 标签变化恰好 4 条, 都是 PDF_TYPO → EXACT, 都由现有 `live-hit` 规则判出. 清单外标签变化 0, 非标签字段变化 0.
> 未动: `knowledge_base/` (`HEAD:knowledge_base` = `63f857774a42cfaa71798705ad40ab51bc5e378a`, 工作树无改动, 真 KB 内容 md5 `b71a466d…` 变异前后一致); `archive/`、`releases/`; 登记表 `work/t2_pdf_typo_registry.jsonl` (md5 仍为 `e6f86b49…`); `ig34_p0293_a038` (仍为 PDF_TYPO). 未 git add / commit / push. 没跑 `t0_mutation_head.sh` / `t4_gate_prerun.sh` / `t4_supp_report.py` / `t4_c3_report.py` / `t4_sample.py` / `t4_render.py`.
> scratch (gitignored): `work/scratch/t4/r3l/` (`run_chain.sh` = R2L 同名脚本原样复制; `rdiff.py` = R2L 版只把清单换成 `t4_r3l_relabel.json`; run0 / runA / runB / runC / runD 日志; `before/` 改前副本; 变异日志 `mut1_wb.log` / `mut2_wb.log` / `mut3_dh.log` / `mut4_wb.log`).

## 0. 命令 (仓库根目录; T=.work/10_tier_b_repair, R=$T/work/scratch/t4/r3l)
```bash
cp $T/work/coverage_ledger.wc.jsonl $T/work/coverage_ledger.wc.pre_r3l.jsonl     # 规则 B 备份 (入库), md5 16024ac0…
bash $R/run_chain.sh $R/run0                       # 改任何输入之前先跑整链: 台账仍为 16024ac0… (基线可复现)
python3 -I $T/scripts/t4/t4_r3l_build.py           # 一次性: 生成 work/t4_r3l_relabel.json, 改 keep 清单 4 条 (幂等, 跑两次结果相同)
#   改 t3_writeback.py (见 §2) → 单跑 writeback + rdiff (中间态 s1): 恰好 4 行标签变化
bash $R/run_chain.sh $R/runA; bash $R/run_chain.sh $R/runB; diff $R/runA/md5.txt $R/runB/md5.txt   # 空 = 一致
python3 $R/rdiff.py $T/work/coverage_ledger.wc.pre_r3l.jsonl $T/work/coverage_ledger.wc.jsonl $T/work/t4/r3l_ledger_diff.txt
python3 -I $T/scripts/t4/t4_ack_lists.py
python3 -I $T/scripts/t4/t4_coverage_decomp.py; python3 tools/check_links.py 2>&1 | grep "live docs"
bash $T/scripts/t3/t3_mutation.sh > $T/work/t4/t4_mutation_r3l.log 2>&1
python3 -I $T/scripts/t3_recompute.py --ledger $T/work/coverage_ledger.wc.pre_r3l.jsonl --out $R/sc_pre_r3l.jsonl   # 只用于节级对照
#   新断言的变异 (§3 末), 之后从源头再跑一遍: bash $R/run_chain.sh $R/runC; diff $R/runB/md5.txt $R/runC/md5.txt
#   小修 keep _note 生成方式 (§3 末) 后: cp $R/before/t3_k3b_out_of_scope_keep.json $T/work/; t4_r3l_build.py ×2; 变异 ④; bash $R/run_chain.sh $R/runD
git status --short knowledge_base archive releases; git rev-parse HEAD:knowledge_base; git diff --quiet HEAD -- knowledge_base
```
- `--ts 2026-11-26T12:00:00Z` 不变, 所以没改判的行与备份逐字节相同.

## 1. 成因 (改之前查清)
4 条都由 `t3_writeback.py` 的 **K3b 登记扫描**判成 PDF_TYPO (规则 `K3b-registry`). 它们都在 §5.0 范围外 (§7.3.2 TD – Examples), 能留在 PDF_TYPO 只因为 `work/t3_k3b_out_of_scope_keep.json` 里有它们的 `keep_k3b` 条目 (attempt 4 / A4-5.1 生成). 没有 triage / t2s / errata 条目, 允许集也只靠这一条进来.

| 原子 | K3b 子规则 | 登记 | 误触及的原因 | 真正有笔误的原子 |
|---|---|---|---|---|
| `ig34_p0412_a006` / `a007` / `a008` | c' (只有标点的笔误: 原子在 KB 上的命中行 = 登记的 `kb_line_now`) | `S-TDM TD T-1` ("assessments..", KB 第 40 行) | KB `TD/examples.md:40` 是把 PDF 4 句合成的一段. c' 只看命中行, 所以命中这一行的原子全被触及 | `ig34_p0412_a009` (仍为 PDF_TYPO, 规则 `writer-Tn-registry`, 不受影响) |
| `ig34_p0413_a010` | c (原子带 KB 侧 token `tdtgtpai`, 且命中行含登记的 `kb_line_now` 167) | `S-TDM TD T-4` (Ex3 表头 TDTGPAI) | 本原子是 Ex2 表头. 三个例子的表头文字相同, 它在 KB 上命中 50 / 102 / 167 三行, 其中含 167 | `ig34_p0414_a013` (仍为 PDF_TYPO, `K3b-registry` 规则 b) |

- 成因的模式: c' 会触及所有命中同一 KB 合并行的原子; c 会触及文字与登记行相同的其它表头行. 两种都是 "命中行相同, 但笔误不在本原子".
- 登记表 T-1 / T-4 两行没有 "受影响原子" 字段 (T-4 的 `span_lines_in_file` [50, 102, 167] 是 KB 行号, 说的是 token 在 KB 中出现的位置, 本身不错), 所以没有登记字段要更正, 登记表没改.

## 2. 改法 (从成因下手; 数据与规则分开)
| 项 | 做法 | 改的文件 |
|---|---|---|
| 数据清单 | `scripts/t4/t4_r3l_build.py` (一次性, 幂等) 从 `work/t4/supp/relabel_pending.json` 取 `group` = `typo-overlabel` 的 4 条, 写 `work/t4_r3l_relabel.json`. 每条有 group / now / to / raw / why / decision ("owner 2026-11-27 问题 A = A1 (`evidence/checkpoints/t4_owner_confirmation.md` 消息 4)") / `k3b_drop` (被否定的 K3b 触及, 取自该原子 keep 条目的 `registry`) / `k3b_rule`. 生成时断言 4 条、now/to、`raw` 的 文件:行 存在、登记 id 存在. 之后 JSON 是运行时唯一来源, 脚本里没写 id | 新增 `scripts/t4/t4_r3l_build.py`、`work/t4_r3l_relabel.json` (md5 `1dcefad3…`) |
| keep 清单 | 同一脚本把这 4 条的 `action` 由 `keep_k3b` 改为 `t4_r3l_drop`, 加字段 `t4_r3l_fix` (before → after、decision、raw、spec、basis); `_note` 追加一句 (句中 id 与计数由 `rel` / `keep` 生成, 脚本里不写 id). 条目不删. 没跑 `t3_build_keep.py` | `work/t3_k3b_out_of_scope_keep.json` (md5 `9053d986…` → `27d477c3…`) |
| writeback: 剔除触及 | 在 K3b 扫描 + K3B_MANUAL + keep 清单加载之后、`K3B_OUT` 之前: 读清单; 断言 (a) 清单原子 ⊂ 原子表、不在 errata atom_err、不在 R2L 清单; (b) keep 清单里 `t4_r3l_drop` 的集合 = 清单; (c) **每条原子当前的 K3b 触及恰好等于 `k3b_drop`** (多一条或少一条登记都报错). 然后把它从 `K3B` / `K3B_WHY` 里拿掉, 记进 `t3_rules.json` 新键 `K3b_t4_r3l_dropped`, 原子并入允许集. 这些是模块级 assert, 发生在写台账之前 | `scripts/t3/t3_writeback.py` |
| writeback: 判定 | 不新增判定分支. 原子走现有 `decide()`, 4 条都落到 `live-hit` (KB 逐字命中; 命中行 a006-a008 = `TD/examples.md:40`, a010 = `:50/102/167`). 之后给 evidence 加 `t4_r3l` (group / decision / raw / before / k3b_dropped / k3b_why_dropped / spec), batch_id 改为 `T4-R3L` (live-hit 的兜底值是 `T3-errata-key`, 不真实) | 同上 |
| writeback: 强制重写 | a007 / a010 在 pre_t3 基线里就是 EXACT, 按 "只重写 verdict 有变化的行" 会退回 stock 行; stock 行在 §5.0 范围外不进 `t3_direct_hit.py` 的检查, 行上也不会有决定来源. 所以清单原子即使 verdict = 基线也重写成 TB 行 (`if verdict and (verdict != old or i in R3L)`) | 同上 |
| writeback: 断言 | 终态必须 = 清单 `to` (EXACT)、规则必须是 `live-hit`、不在 K3B、已重写. 不满足 → `ASSERT: FAIL`, rc=1. docstring 同步 (加 R3L 说明, 写明 R3L 行总是重写) | 同上 |
| ack 清单 | 只改状态行文字 (R3L 重生成, 上一次为 R2L). 分类逻辑没改: 4 条不再是 PDF_TYPO, 自然从清单里消失 | `scripts/t4/t4_ack_lists.py`, 重生成 `evidence/checkpoints/t4_ack_lists.md` |

## 3. 验收 (规格 §2; 输出摘自 `$R/runB/` 日志与命令回显; runC 结果相同)
| 项 | 命令 | 输出 | 判定 |
|---|---|---|---|
| 备份 | `cp` + `md5 -q` | `work/coverage_ledger.wc.pre_r3l.jsonl` = `16024ac09721cb3f8519cd68fa455196` | 符合 |
| 逐行 diff | `rdiff.py` (见 §0) | `rows 12492 / 12492; identical 12488; label-changed 4; other-changed 0`; `listed atoms not changed: []`; `label ('typo-overlabel', 'PDF_TYPO', 'EXACT', True): 4`; 4 行都是 `OK rule=live-hit` | 符合 |
| 行数 | `wc -l` | 12492 | 符合 |
| 两遍 md5 | `diff runA/md5.txt runB/md5.txt` (另 runB vs runC) | 都为空. ledger `438098704becc84eda01a925b80defaa`; errata `b6065206…` / t2s `33ef2fe0…` / fp_expected `e7df6ce0…` 不变; keep `1e99f101…` (runD; runA-runC 时为 `27d477c3…`, 差别只在 `_note`); rules `1096bec2…`; decisions `10a925c9…` | 符合 |
| 终态计数 | python 计数 | PDF_TYPO 174 → **170**, EXACT 4706 → **4710**; 其余 (IE 2559 / EQUIVALENT 3949 / PARTIAL 637 / ATOM_ERR 197 / MISPLACED 197 / ERROR 62 / FIGURE 11) 不变 | 符合 |
| 覆盖率四个数 | `t4_coverage_decomp.py` | strict `9493/9933 = 95.5703%`; mapped `9493/9555 = 99.3511%`; U-1 B `9860/9933 = 99.2651%`; content `8659/9555 = 90.6227%` | 与 `scenarios.json` 最后一项 ("主人已定的全部 + 4 条多标的 PDF 笔误 → 逐字": n 82, u1b 9860/9933 = 99.2651%, strict 9493/9933 = 95.5703%, mapped 9493/9555 = 99.3511%, content 8659/9555 = 90.6227%) 逐字相同 |
| s0_classify | runB `04_s0.log` | `not in t3 list (NEW): []`; `BAD []`; `Counter({'R3': 47, 'R2': 42, 'R1': 32}) R4 = 0` | 符合 (日志与 run0 逐字相同) |
| t3_direct_hit | runB `08_direct_hit.log` | `TB(all)=1033 stock(§5.0 scope)=1748`; tb_exact_miss / k11_short / anchor_lost / unexplained 全为 0; pre_existing 52; `RESULT: GREEN` | 符合. TB 1029 → 1033 (+4 = 这 4 条), stock 与 pre_existing 不变 |
| t3_recompute | runB `09_recompute.log` | `§5.0 scope sections=174 residual_gap=0 G-TB1 pass=174/174 G-TB2 pass=157/174` | 符合 |
| writeback ASSERT | runB `07_writeback.log` | `T4 R3L: 4 listed; K3b touches dropped: {a006/a007/a008: ['S-TDM TD T-1'], a010: ['S-TDM TD T-4']} \| final label as listed via live-hit: 4`; `T4 R2L: 78 listed; final label as listed: 78`; keep 25 条复核失败 []; K3b 扩展断言 0; K11 `{}`; `ASSERT: OK` | 符合 |
| ack 清单 | `t4_ack_lists.py` | `{'ATOM_ERR': 197, 'PDF_TYPO': 170, 'FIGURE_DEFERRED': 11}`; 来源 U-5 325 / U-7 22 / U-8 4 / U-2 1 / M-4 1 / 第二轮 3 = A 19 / 7b = A 6; "(未归因)" 断言通过. md5 `18a2981c…` | 符合 (U-5 329 → 325 = 这 4 条原属 U-5) |
| live docs | `check_links.py` | `broken relative links: 18668 (live docs: 42)` | 符合 |
| t3_mutation | `work/t4/t4_mutation_r3l.log` | M0 GREEN; M1 RED (tb_exact_miss `ig34_p0133_a021`); M2 GREEN; M3 RED (anchor_lost `ig34_p0064_a001`); M4 RED (tb_exact_miss 4); M5 RED (anchor_lost `ig34_p0295_a020`); M6 RED; M7 GREEN; `real KB md5 before/after b71a466d6e618f995c493a82de3e3eb7`, `real KB unchanged: OK` | 符合. 没有靶子失效 |
| KB / 冻结区 | `git status --short knowledge_base archive releases` / `git rev-parse HEAD:knowledge_base` / `git diff --quiet HEAD -- knowledge_base` | 空 / `63f857774a42cfaa71798705ad40ab51bc5e378a` / 无改动 | 符合 |

新断言的变异 (规则 5; 每次先确认改动已写入, 再跑, 之后 `cp` 还原; 日志在 `$R/`):
- ① 清单里 `ig34_p0413_a010` 的 `k3b_drop` 改成 `S-TDM TD T-1` (确认 `S-TDM TD T-4` 出现 0 次). `writeback rc=1`, `AssertionError: ('T4 R3L K3b touch != listed', 'ig34_p0413_a010', ['S-TDM TD T-4'], ['S-TDM TD T-1'])`.
- ② 从清单删掉 `ig34_p0412_a006` (确认出现 0 次). `writeback rc=1`, `AssertionError: ['ig34_p0412_a006', 'ig34_p0412_a007', 'ig34_p0412_a008', 'ig34_p0413_a010']` (keep 清单 `t4_r3l_drop` 集合 ≠ 清单).
- 两次台账 md5 都保持 `43809870…`、rules `1096bec2…` (断言在写文件之前). 还原后清单 md5 = `1dcefad3…`.
- ③ direct_hit 对这 4 条的独立检查: 在 `$R/kb_mut/` (`git archive HEAD knowledge_base` 副本, 不是真 KB) 里删掉 `TD/examples.md` 中 a008 那句, 并把三处 `| TDTGTPAI |` 改成 `| TDTGXXXX |`. `t3_direct_hit.py --kb-root` 该副本: `tb_exact_miss: 2 ['ig34_p0412_a008', 'ig34_p0413_a010']`, `RESULT: RED`, rc=1. 副本已删.
- ④ 写台账之后的那条断言 (只改数据即可构造): 在 `work/t3_errata.json` 的 `pending_user` 加 `ig34_p0413_a010` (conclusion 含 "残留"), 让 `decide()` 在 live-hit 之前落到 residual 分支. 选 a010 是因为它的基线本来就是 EXACT, 能证明断言查的是规则而不只是标签. 结果 `writeback rc=1`, `ASSERT: FAIL ['T4 R3L atom not live-hit EXACT: ig34_p0413_a010 EXACT pending_user-residual in_k3b=False']` (`final label as listed via live-hit: 3`). 这一处 writeback 先写台账后断言, 所以还原 errata (md5 `b6065206…`) 后从源头重跑了 runD.
- 变异 ①-③ 之后从源头再跑 runC, 7 个产物 md5 与 runB 逐一相同.
- 小修 (advisor 意见): `t4_r3l_build.py` 原来把 4 个 id 和 21 / 4 / 0 计数直接写在 keep `_note` 的字符串里, 改为由 `rel` / `keep` 生成. 先把 keep 清单还原为改前副本 (md5 `9053d986…`), 再跑两遍 build (幂等), keep md5 `27d477c3…` → `1e99f101…` (只差 `_note`). 之后做变异 ④, 再从源头跑 runD: 台账 `43809870…`、errata / t2s / fp_expected / rules / decisions md5 与 runC 逐一相同, 只有 keep 为新值; writeback `ASSERT: OK`, direct_hit GREEN. ack 重生成 md5 仍为 `18a2981c…`.

## 4. 逐行 diff 汇总 (清单: `work/t4/r3l_ledger_diff.txt`, md5 `dd4225c1…`)
| 类 | 条数 |
|---|--:|
| typo-overlabel PDF_TYPO → EXACT (规则 live-hit) | 4 |
| 只改非标签字段 | 0 |
| 逐字节相同 | 12488 |

- a006 / a008: 新行 `prev_verdict` = EQUIVALENT; a007 / a010: `prev_verdict` = EXACT. writeback 一向以 pre_t3 备份为基准, 不是改前台账的 PDF_TYPO. 改前状态写在 `evidence.t4_r3l.before`.
- 4 行都是 TB 行, evidence 带 `t4_r3l`, 没有 `registry` / `k3b` 键. 逐行打印 (runD 后, 从 `work/coverage_ledger.wc.jsonl` 读 verdict / phase / batch_id / rule / prev_verdict / hit_file / hit_lines / 有无 registry / 有无 k3b / t4_r3l.raw):

| 原子 | verdict | phase | batch_id | rule | prev_verdict | hit | registry / k3b | t4_r3l.raw |
|---|---|---|---|---|---|---|---|---|
| `ig34_p0412_a006` | EXACT | TB | T4-R3L | live-hit | EQUIVALENT | `TD/examples.md` [40] | 无 / 无 | `pack_10.md:29` |
| `ig34_p0412_a007` | EXACT | TB | T4-R3L | live-hit | EXACT | `TD/examples.md` [40] | 无 / 无 | `pack_10.md:30` |
| `ig34_p0412_a008` | EXACT | TB | T4-R3L | live-hit | EQUIVALENT | `TD/examples.md` [40] | 无 / 无 | `pack_10.md:31` |
| `ig34_p0413_a010` | EXACT | TB | T4-R3L | live-hit | EXACT | `TD/examples.md` [50, 102, 167] | 无 / 无 | `pack_10.md:32` |

  4 行的 `t4_r3l` 都是: decision = "owner 2026-11-27 问题 A = A1 (evidence/checkpoints/t4_owner_confirmation.md 消息 4)", before = "PDF_TYPO (K3b-registry, keep_k3b)", k3b_dropped = a006-a008 `S-TDM TD T-1` / a010 `S-TDM TD T-4`, spec = 规格 §1.

其它派生文件的变化 (改前副本 `$R/before/`):
- `t3_rules.json`: `K3b` / `K3b_why` / `K3b_extra` / `K3b_keep_list` 各少这 4 条; 新键 `K3b_t4_r3l_dropped` (4 条, 记被剔除的登记与原 why). K11 仍为 `{}`, 其它键不变.
- `t3_writeback_decisions.json`: 只有这 4 键变化 (new = EXACT, rule = live-hit, batch = T4-R3L).
- `t3_t4_risk_anchorless.txt`: 507 → 511, 加了这 4 条 (命中原因 "no governing numbered heading": `TD/examples.md` 没有带编号的标题). 见 §6 第 2 条.
- `t3_t4_k3b_out_of_scope.txt`: 不变.
- `t3_audit_sets/`: `K3b-registry__PDF_TYPO.txt` 少 4 行, `live-hit__EXACT.txt` 多 2 行. 后者只多 2 行, 因为 `t3_report.py` 按 old ≠ new 统计 "flip" (a007 / a010 的 old = 基线 EXACT), 所以 report 的 flipped 是 2011 → 2009, live-hit EXACT 1010 → 1012. direct_hit 的 TB 计数是 1033 (含全部 4 条).
- `section_coverage.wc.jsonl`: 含 ts. 用 `t3_recompute.py --ledger pre_r3l` 重算改前状态, 按位置对齐比较 (忽略 ts): 只有 2 节的 aggregate_verdict 变了, 都在 §5.0 范围外. §7.3.2 TD – Examples CONTENT_TRUNCATED → MOSTLY_COMPLETE (matched 31 → 35, density 0.7949 → 0.8974); §7.3 [SCHEDULE FOR ASSESSMENTS] SIBLING_DROPPED → MOSTLY_COMPLETE. 全书分布: SIBLING_DROPPED 41 → 40, CONTENT_TRUNCATED 57 → 56, MOSTLY_COMPLETE 65 → 67.
- `t4_ack_lists.md`: PDF_TYPO 节去掉这 4 行, 后面的行重新编号; 汇总行 174 → 170、K3b-registry 61 → 57; 状态行文字.

## 5. 没做 / 撤回的项
- 没有撤回的项: 没有一项改动引起清单外标签变化.
- 没改 K3b 规则 c / c' 本身. 改规则可能牵动其它 PDF_TYPO 原子, 守则 3 不允许. 我也没去查其它原子是不是同一模式.
- 没改登记表: T-1 / T-4 没有 "受影响原子" 字段, 见 §1.
- 没删 keep 清单条目, 改的是 action, 留了 before → after 记录.

## 6. 已知局限 / 需主控定
1. **同一模式可能还有别的原子, 本批没查, 也没修**. c' 和 c 只认命中行, 所以别的合并行、相同表头上也可能有同类多标. 本批只按主人 A1 处理了这 4 条. 要不要全量排查, 请主控定.
2. 4 条新 EXACT 进了 `t3_t4_risk_anchorless.txt` (无编号标题锚点). direct_hit 用 `valid_hits` 独立核过, KB 也有逐字命中. 锚点弱是 `TD/examples.md` 文件结构造成的, 与改标无关.
3. a007 / a010 的 verdict 与 pre_t3 基线相同, 按旧口径本不重写. 这次强制重写成 TB 行 (理由见 §2), 所以 report 的 "flip" 计数只加 2, direct_hit 的 TB 计数加 4.
4. 4 行新 `matched_by` 的 `ts` 是 2026-11-26T12:00:00Z、`prompt_version` 是 t3_writer_v1.0, 早于主人的决定日. 这是沿用固定 ts 的结果 (同 R2L §5 第 6 条). 决定日期写在 `evidence.t4_r3l.decision` 里.
6. `scripts/t4/t4_gate_prerun.sh` (只读, 没跑) 第 48 行的 md5 清单含 `coverage_ledger.wc.pre_r2l.jsonl` / `t4_r2l_relabel.json`, 不含本批新增的 `coverage_ledger.wc.pre_r3l.jsonl` / `t4_r3l_relabel.json` / keep 清单. 是否补进去由主控定. `t3_attempt_diff.py` 读 `t3_rules.json` 的 K3b 键, 不写死计数. `t3_rules.json` 的数从这批起变了: K3b-registry PDF_TYPO 61 → 57、`K3b_keep_list` 25 → 21, 另有新键 `K3b_t4_r3l_dropped`.
5. 机制选择请主控认可: 数据新建 `work/t4_r3l_relabel.json`, 不并入 `t4_r2l_relabel.json` (R2L 的断言要求非 IE 条目走 S1-R2); keep action 用了新值 `t4_r3l_drop`, 没复用 `t4_only` (复用会让它们进 `t3_t4_k3b_out_of_scope.txt`, 看起来像 "仍被触及").

## 7. md5 (终态)
| 文件 | md5 |
|---|---|
| `work/coverage_ledger.wc.jsonl` | `438098704becc84eda01a925b80defaa` |
| `work/coverage_ledger.wc.pre_r3l.jsonl` (备份) | `16024ac09721cb3f8519cd68fa455196` |
| `work/t4_r3l_relabel.json` | `1dcefad3463c4814f42fb68eb6343e0c` |
| `work/t3_k3b_out_of_scope_keep.json` | `1e99f1010ff402f738fc57b2884d1954` |
| `work/t3_rules.json` / `t3_writeback_decisions.json` | `1096bec29fa25711b250d70711093002` / `10a925c9e44c75c6d2ce9551d56156d1` |
| `work/t3_errata.json` / `t2_pdf_typo_registry.jsonl` / `t4_r2l_relabel.json` (都不变) | `b6065206…` / `e6f86b49…` / `3e7e6eba…` |
| `evidence/checkpoints/t4_ack_lists.md` | `18a2981ce5bcdb11989cfdcf6ba46a4e` |
| `work/t4/r3l_ledger_diff.txt` | `dd4225c189d58d32834ff98ac9f5da4f` |
| `work/t4/t4_mutation_r3l.log` | `502f7f5d7a100aa4c69a8b68a8549e72` |
