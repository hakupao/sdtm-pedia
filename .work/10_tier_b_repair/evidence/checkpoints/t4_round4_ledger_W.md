# T4 问题 C 改台账 (R4L) — writer checkpoint
<!-- chain: E (plans) -->
> 状态: writer 已完成 (2026-11-27, `oh-my-claudecode:executor`, attempt 1). 等 reviewer 复跑逐行核 (规则 D). 本文不给自己判 PASS.
> 规格: `subagent_prompts/t4/t4_round4_ledger_spec_v1.0.md`. 依据: 主人 2026-11-27 直接回答 "C1" (`evidence/checkpoints/t4_owner_confirmation.md` 消息 5). 语义依据: 两位互不知情的独立审查者 `evidence/t4_atomerr_raw/pack_1.md:29` (E12, `oh-my-claudecode:tracer`) 与 `evidence/t4_atomerr_raw/second_look.md:20` (E12, `general-purpose`), 都判 NOT_HOLD.
> 结果: 台账 md5 `438098704becc84eda01a925b80defaa` → **`eef9bb14e5afab7e68a231ddd18cfa1c`**. 改输入后从源头跑了四遍整链: runA / runB 用第一版 `t3_errata_build.py`, runC / runD 用终版 (§2 末小修); 两两比较 (A vs B、C vs D) 7 个产物 md5 都一致, 四遍台账 md5 都相同. 终版代码的 "两遍一致" 证据是 runC vs runD. 标签变化恰好 1 条 (`ig34_p0124_a001` ATOM_ERR → EXACT, 由现有 `live-hit` 规则判出). 清单外标签变化 0; 非标签字段变化 4 行, 都是规格里那 4 条 ATOM_ERR 补登记指针, 只动了 `matched_by.evidence.registry`.
> 未动: `knowledge_base/` (`HEAD:knowledge_base` = `63f857774a42cfaa71798705ad40ab51bc5e378a`, 工作树无改动, 真 KB 内容 md5 `b71a466d…` 变异前后一致); `archive/`、`releases/`、`web/`; `work/t1_errata.json` (只读; md5 与改前副本相同); 登记表 `work/t2_pdf_typo_registry.jsonl`; `B-CE T-2` 那 8 条 (仍为 ATOM_ERR); `ig34_p0293_a038` (仍为 PDF_TYPO). 没有 git add / commit / push. 没跑 `t0_mutation_head.sh` / `t4_gate_prerun.sh` / `t4_supp_report.py` / `t4_sample.py` / `t4_render.py` / `t4_atomerr_sample.py`, 也没重跑 `t3_build_keep.py`.
> scratch (gitignored): `work/scratch/t4/r4l/` (`run_chain.sh` = R3L 同名脚本原样复制; `rdiff.py` = R3L 版只把清单换成 `t4_r4l_relabel.json`; `mut.sh` = 新断言的变异; run0 / runA / runB / runC / runD 日志; `before/` 改前副本; `coverage_pre.log`; 变异日志 `mut*.log`、`mut.out`、`mut5_dh.log`).

## 0. 命令 (仓库根目录; T=.work/10_tier_b_repair, R=$T/work/scratch/t4/r4l)
```bash
cp $T/work/coverage_ledger.wc.jsonl $T/work/coverage_ledger.wc.pre_r4l.jsonl      # 规则 B 备份 (入库), md5 43809870…
python3 -I $T/scripts/t4/t4_r3l_build.py            # HANDOFF "坑": 整链前先跑 (幂等; keep md5 前后都是 1e99f101…)
python3 -I $T/scripts/t4/t4_atomerr_coverage.py > $R/coverage_pre.log   # 改台账之前留底 (输出见 §3)
bash $R/run_chain.sh $R/run0                         # 改任何输入之前先跑整链: 台账仍为 43809870…, 7 个产物 md5 与 R3L runD 相同
python3 -I $T/scripts/t4/t4_r4l_build.py             # 一次性: 生成 work/t4_r4l_relabel.json (跑两次 md5 相同)
#   改 t3_errata_build.py / t3_writeback.py (见 §2) → 单跑 errata + writeback + rdiff (中间态 s1): 恰好 1 行标签变化 + 4 行只改 registry
bash $R/run_chain.sh $R/runA; bash $R/run_chain.sh $R/runB; diff $R/runA/md5.txt $R/runB/md5.txt   # 空
python3 -I $T/scripts/t4/t4_ack_lists.py; python3 -I $T/scripts/t4/t4_coverage_decomp.py; python3 tools/check_links.py 2>&1 | grep "live docs"
bash $T/scripts/t3/t3_mutation.sh > $T/work/t4/t4_mutation_r4l.log 2>&1
#   小修 t3_errata_build.py (撤销挪到允许集标记之后, 见 §2 末) → bash $R/run_chain.sh $R/runC; diff $R/runB/md5.txt $R/runC/md5.txt
bash $R/mut.sh                                       # 新断言的变异 ①-④ (§3 末); ⑤ 见 §3 末
bash $R/run_chain.sh $R/runD; diff $R/runC/md5.txt $R/runD/md5.txt                                  # 空
python3 $R/rdiff.py $T/work/coverage_ledger.wc.pre_r4l.jsonl $T/work/coverage_ledger.wc.jsonl $T/work/t4/r4l_ledger_diff.txt
python3 -I $T/scripts/t4/t4_ack_lists.py
python3 -I $T/scripts/t3_recompute.py --ledger $T/work/coverage_ledger.wc.pre_r4l.jsonl --out $R/sc_pre_r4l.jsonl   # 只用于节级对照
git status --short knowledge_base archive releases web; git rev-parse HEAD:knowledge_base; git diff --quiet HEAD -- knowledge_base
```
- `--ts 2026-11-26T12:00:00Z` 不变, 所以没改判的行与备份逐字节相同.

## 1. 成因 (改之前查清, 自己核过)
| 环节 | 事实 |
|---|---|
| 出处 | `evidence/checkpoints/t2_B-ML_review.md:70` 是 "范围外 (沿用 writer)" 一节的一句顺带话: "原子错 … p0124_a001 (MIDSDTC 截断) 供 ledger 修正参考". 没有逐格核对记录 |
| 登记 | `work/t1_errata.json` 的 `t3_atom_err` 有 `"ig34_p0124_a001": "B-ML review: 原子 verbatim MIDSDTC 截断; KB 与 PDF 一致"` (第 109 行). 这是它进入 errata 的唯一来源: 不在 `t3_fp_expected_regressions.jsonl`、不在 triage (无 triage 行)、不在 `t3_t2s_atoms.jsonl`、不在 R2L 清单、无 remap / pending_user |
| 展开 | `scripts/t3/t3_errata_build.py` (1) 把它写成 `atom_err` 条目: `classify()` 没找到 T-n、也没有 "照录" → R1 → 终态 ATOM_ERR, `registry` = [] |
| K4 没挡住 | K4 只在 `norm(原子) ⊂ norm_pdf(p-1..p+1)` 时才撤 R1. PDF 文本层 `work/pdf_pages/ig34_p0124.txt:1-5` 是逐格折行的表格 (`XYZ-001-` / `001`, `2015-09-` / `03T17:00`, `LAST` / `MEAL` / `PRIOR` / `TO`), 整行子串测不出来, 所以 `atom_in_pdf` = false, 条目留下 |
| 判定 | `scripts/t3/t3_writeback.py` 的 `decide()` 第一条分支就是 S1 errata, 优先于 live-hit → `S1-R1` ATOM_ERR. 台账这一行自己带着 `hit_file` = `knowledge_base/domains/ML/examples.md`, `hit_lines` = [42], `prev_verdict` = EXACT |
| 实际 | 原子 (`work/pdf_atoms.jsonl`) 最后一格是完整的 `2015-09-03T17:00`, 没截断; 原子 `prompt_version` 带 `OptionE_p124_rerun` (第二位审查者也指出, 登记时可能看的是重抽前的版本; 我没去核旧版). KB `ML/examples.md:42` 与原子逐格相同 (`| 2 | XYZ | ML | XYZ-001-001 | … | HYPO2 | 2015-09-03T17:00 |`) |

- 原子在 §5.0 范围内 (`§6.1.4 [Meal Data (ML)]`), K3b 没有触及它 (`t3_rules.json` 的 `K3b` / `K3b_out_of_scope` 里都没有).
- 原子进允许集的唯一途径就是这条 errata. 只删 errata 的话, 它会退回 pre_t3 的 stock 行 (EXACT, 但不是 `decide()` 判出来的, 行上也没有决定来源). 所以照 R3L 的做法让它进允许集, 并强制重写成 TB 行.

## 2. 改法 (从成因下手; 数据与规则分开)
| 项 | 做法 | 改的文件 |
|---|---|---|
| 数据清单 | `scripts/t4/t4_r4l_build.py` (一次性, 幂等, 路径按 `__file__` 推算) 从加查的机读清单 `work/t4/atomerr/verdicts.json` 取 NOT_HOLD 的条目 (断言恰好 1 条 = `ig34_p0124_a001`), 写 `relabel`: group `atomerr-not-hold` / now ATOM_ERR / to EXACT / raw = [`pack_1.md:29`, `second_look.md:20`] (断言文件:行存在, 第二行含 NOT_HOLD) / decision "owner 2026-11-27 问题 C = C1 (evidence/checkpoints/t4_owner_confirmation.md 消息 5)" / revoke `t1_errata.t3_atom_err` / spec. 另写 `registry_ptr` 4 条 (见下). 之后 JSON 是运行时唯一来源, t3 脚本里没写 id. 注意: 4 条指针的 原子 → 登记 id 对照是写在 `t4_r4l_build.py` 里的字面表 `PTR` (取自 `t4_atomerr_fullcheck.md` §5b), 由脚本对 `verdicts.json` 的审查者原话与登记表交叉断言 | 新增 `scripts/t4/t4_r4l_build.py`、`work/t4_r4l_relabel.json` (md5 `c33abbe7…`) |
| errata: 撤销 | 新段 (6): 在 K4、remap、pending、允许集标记都做完之后, `json.dump` 之前, 读清单, 逐条断言 "只因这条 errata 才是 ATOM_ERR": 在 `atom_err` 里; `source` = `t1_errata.t3_atom_err` = 清单 `revoke`; `cls` = R1; `registry` 为空; 在 `t1_errata.t3_atom_err` 里; 不是 fp 清单的 R1/R2; triage 不是 ATOM_ERR; 不在 R2L; 清单 now/to = ATOM_ERR/EXACT. 然后从 `atom_err` 拿掉, 原样存进新键 `r4l_revoked` (附 decision / raw / spec). `work/t1_errata.json` 不改 | `scripts/t3/t3_errata_build.py` |
| writeback: 允许集 | R2L 之后读清单; 断言 清单 ⊂ 原子表、清单 = `t3_errata.json` 的 `r4l_revoked` 键集、不在 `atom_err`、不在 R2L; 并入允许集 (在 K3b 与 `K3B_OUT` 之前). R3L 段加一句断言 R3L ∩ R4L = ∅. 这些都是写台账之前的模块级 assert | `scripts/t3/t3_writeback.py` |
| writeback: 判定 | 不新增判定分支. 原子走现有 `decide()`, 落到 `live-hit` (命中 `ML/examples.md:42`). 之后给 evidence 加 `t4_r4l` (group / decision / raw / before / errata_revoked / spec), batch_id 改为 `T4-R4L` (live-hit 的兜底值是 `T3-errata-key`, 不真实) | 同上 |
| writeback: 强制重写 | pre_t3 就是 EXACT, 按 "只重写 verdict 有变化的行" 会退回 stock 行. 条件改为 `verdict != old or i in R3L or i in R4L` | 同上 |
| writeback: 断言 | 写台账之后: 终态 = 清单 `to` (EXACT)、规则 = `live-hit`、不在 K3B、已重写. **查的是规则, 不只是标签** — 只查标签的话, 判不出 EXACT 的原子退回 stock EXACT 也能过 (变异 ② 证明了这一点). 不满足 → `ASSERT: FAIL`, rc=1 | 同上 |
| 4 条登记指针 | 照 R2L 的 `registry_ptr` 机制, 但只动 `evidence.registry`: 在 decide 与 K11 之后, 断言该原子 `decided` = (ATOM_ERR, S1-R1)、登记 id 存在, 然后把 id 追加到 `ev["registry"]`. 没写进 `atom_err[i]["registry"]` — 那样 `decide()` 会从 `registry[0]` 改 `batch_id` (T1/T2-errata → B-DS 等), 还可能加 `c7_delta_rereview`, 超出 "只补指针". 与 R2L 不同, 行上**没加**出处键 (R2L 加了 `t4_r2l_registry_ptr`); 出处留在 `work/t4_r4l_relabel.json` 的 `registry_ptr` (raw / decision / spec) | 同上 |
| ack 清单 | 只改状态行文字 (R4L 重生成, 上一次为 R3L). 分类逻辑没改 | `scripts/t4/t4_ack_lists.py`, 重生成 `evidence/checkpoints/t4_ack_lists.md` |

- 4 条登记指针 (依据 `evidence/checkpoints/t4_atomerr_fullcheck.md` §5b; build 脚本断言: 审查结果 = HOLDS 且 registry_note = true, 审查者原话里有这个登记号, 登记 handling = "KB 写正确值", 登记页与原子页相差不超过 1):

| 原子 | 补的登记 id | 审查者原始结果 |
|---|---|---|
| `ig34_p0161_a0012` | `B-DS T-4` | `evidence/t4_atomerr_raw/pack_2.md:18` |
| `ig34_p0337_a003` | `B-RS T-3` (登记页 336; 原子标 p337, 内容在 p336) | `evidence/t4_atomerr_raw/pack_4.md:14` |
| `ig34_p0339_a001` | `B-RS T-6 (RS 副本)` | `evidence/t4_atomerr_raw/pack_4.md:21` |
| `ig34_p0361_a016` | `B-FA T-2` | `evidence/t4_atomerr_raw/pack_4.md:29` |

  规格写的是 `B-RS T-6`; 登记表里没有这个裸 id, 只有 `B-RS T-6 (RS 副本)` (p339, `RS/assumptions.md:128`) / `(FT 副本)` (p323) / `(QS 副本)` (p328). 与审查者核的位置 (`RS/assumptions.md:128`) 对应的是 `(RS 副本)`, 所以用了它. 请 reviewer 确认.
- 小修 (runB 之后): 第一版把撤销放在 K4 之后、允许集标记之前, 结果 `r4l_revoked` 里存的条目 `in_allowed_set` = false (原条目是 true; 原因是 `put()` 时允许集还只有 triage ∪ t2s). 改成在标记之后撤, 存下的条目与改前 `atom_err` 条目逐字段相同 (python 核对为 True). 台账、rules、decisions md5 不变, 只有 `t3_errata.json` 由 `8a69d98a…` 变为 `76535530…`. 之后 runC / runD 都是新版.

## 3. 验收 (规格 §2; 输出摘自 `$R/runD/` 日志与命令回显; runB / runC 同)
| 项 | 命令 | 输出 | 判定 |
|---|---|---|---|
| 备份 | `cp` + `md5 -q` | `work/coverage_ledger.wc.pre_r4l.jsonl` = `438098704becc84eda01a925b80defaa` | 符合 |
| 基线可复现 | `run_chain.sh run0` | 台账 `438098704becc84eda01a925b80defaa`; 7 个产物 md5 与 `work/scratch/t4/r3l/runD/md5.txt` 相同; 日志除 writeback 第 1 行的 "ledger before" 外与 R3L runD 逐字相同; `ASSERT: OK`, direct_hit GREEN | 符合 |
| 逐行 diff | `rdiff.py` (§0) | `rows 12492 / 12492; identical 12487; label-changed 1; other-changed 4`; `listed atoms not changed: []`; `label ('atomerr-not-hold', 'ATOM_ERR', 'EXACT', True): 1`, 该行 `OK rule=live-hit`; `fields-only [registry]: 4` (只有 `matched_by.evidence.registry`: [] → [登记 id]) | 符合 |
| 行数 | `wc -l` | 12492 | 符合 |
| 多遍 md5 | `diff runA/md5.txt runB/md5.txt`; `diff runC/md5.txt runD/md5.txt` | 都为空. ledger `eef9bb14e5afab7e68a231ddd18cfa1c` (runA-D 都是); errata `76535530…` (runC/D; runA/B 为 `8a69d98a…`, 见 §2 小修); t2s `33ef2fe0…` / fp_expected `e7df6ce0…` / keep `1e99f101…` / rules `1096bec2…` 不变; decisions `8aa949c1…` | 符合 |
| 终态计数 | python 计数 | ATOM_ERR 197 → **196**, EXACT 4710 → **4711**; PDF_TYPO 170 / EQUIVALENT 3949 / IE 2559 / FIGURE 11 / PARTIAL 637 / MISPLACED 197 / ERROR 62 不变 | 符合 |
| 覆盖率四个数 | `t4_coverage_decomp.py` | strict `9494/9933 = 95.5804%`; mapped `9494/9556 = 99.3512%`; U-1 B `9860/9933 = 99.2651%`; content `8660/9556 = 90.6237%` | 与改前留底的 `C1` 行逐字相同 (见下) |
| s0_classify | runD `04_s0.log` | `not in t3 list (NEW): []`; `BAD []`; `R4 = 0` | 符合 (日志与 run0 逐字相同) |
| t3_direct_hit | runD `08_direct_hit.log` | `TB(all)=1034 stock(§5.0 scope)=1748`; tb_exact_miss / k11_short / anchor_lost / expected_regression / errata / unexplained 全为 0; pre_existing 52; `RESULT: GREEN` | 符合. TB 1033 → 1034 (+1 = 这条), stock 与 pre_existing 不变 |
| t3_recompute | runD `09_recompute.log` | `§5.0 scope sections=174 residual_gap=0 G-TB1 pass=174/174 G-TB2 pass=157/174` | 符合 (日志与 run0 逐字相同) |
| writeback ASSERT | runD `07_writeback.log` | `T4 R4L: 1 listed (errata revoked) \| final label as listed via live-hit: 1 \| registry_ptr: {'ig34_p0161_a0012': ['B-DS T-4'], 'ig34_p0337_a003': ['B-RS T-3'], 'ig34_p0339_a001': ['B-RS T-6 (RS 副本)'], 'ig34_p0361_a016': ['B-FA T-2']}`; R3L 4 / R2L 78 照旧; `ASSERT: OK` | 符合 |
| ack 清单 | `t4_ack_lists.py` | `{'ATOM_ERR': 196, 'PDF_TYPO': 170, 'FIGURE_DEFERRED': 11}`; 来源 U-5 324 / U-7 22 / U-8 4 / U-2 1 / M-4 1 / 第二轮 3 = A 19 / 7b = A 6; "(未归因)" 断言通过. md5 `04e72e75…` | 符合 (U-5 325 → 324 = 这条原属 U-5) |
| live docs | `check_links.py` (本 checkpoint 写好之后重跑) | `broken relative links: 18668 (live docs: 42)` | 符合 |
| t3_mutation | `work/t4/t4_mutation_r4l.log` (在 runB 状态下跑; 当时台账 md5 = 终态 `eef9bb14…`; 变异只读台账) | M0 GREEN; M1 RED (tb_exact_miss `ig34_p0133_a021`); M2 GREEN; M3 RED (anchor_lost `ig34_p0064_a001`); M4 RED (tb_exact_miss 4); M5 RED (anchor_lost `ig34_p0295_a020`); M6 RED; M7 GREEN; `real KB md5 before/after b71a466d6e618f995c493a82de3e3eb7`, `real KB unchanged: OK` | 符合. 没有靶子失效; 日志 md5 `502f7f5d…` 与 R3L 的 `t4_mutation_r3l.log` 相同 |
| KB / 冻结区 | `git status --short knowledge_base archive releases web` / `git rev-parse HEAD:knowledge_base` / `git diff --quiet HEAD -- knowledge_base` | 空 / `63f857774a42cfaa71798705ad40ab51bc5e378a` / 无改动 | 符合 |

改台账之前的留底 (`python3 -I .work/10_tier_b_repair/scripts/t4/t4_atomerr_coverage.py`, 原样; 改台账之后这个脚本按设计会在 `assert … L[i]["verdict"] == "ATOM_ERR" for i in C1` 处失败, 没再跑):
```
ATOM_ERR 197: with a verdict row 197, without 0 []; first source {'t4_atomerr_raw': 77, 't4_supp_raw': 76, 't4_gate_raw': 7, 'checkpoints': 37}
PDF_TYPO 170: with a verdict row 170, without 0 []; first source {'t4_round2_raw': 60, 't4_round3_raw': 101, 't4_gate_raw': 5, 't4_supp_raw': 4}
now                       : U-1 B 9860/9933 = 99.2651% | strict 9493/9933 = 95.5703% | mapped 9493/9555 = 99.3511% | content 8659/9555 = 90.6227% | EXACT 4710 ATOM_ERR 197 PDF_TYPO 170
C1 (1 -> EXACT)           : U-1 B 9860/9933 = 99.2651% | strict 9494/9933 = 95.5804% | mapped 9494/9556 = 99.3512% | content 8660/9556 = 90.6237% | EXACT 4711 ATOM_ERR 196 PDF_TYPO 170
B-CE 8 -> EXACT           : U-1 B 9860/9933 = 99.2651% | strict 9501/9933 = 95.6509% | mapped 9501/9563 = 99.3517% | content 8667/9563 = 90.6306% | EXACT 4718 ATOM_ERR 189 PDF_TYPO 170
B-CE 8 -> PDF_TYPO        : U-1 B 9860/9933 = 99.2651% | strict 9493/9933 = 95.5703% | mapped 9493/9555 = 99.3511% | content 8659/9555 = 90.6227% | EXACT 4710 ATOM_ERR 189 PDF_TYPO 178
C1 + B-CE 8 -> EXACT      : U-1 B 9860/9933 = 99.2651% | strict 9502/9933 = 95.6609% | mapped 9502/9564 = 99.3517% | content 8668/9564 = 90.6315% | EXACT 4719 ATOM_ERR 188 PDF_TYPO 170
B-CE atoms: ['ig34_p0153_a0034', 'ig34_p0154_a0002', 'ig34_p0154_a0013', 'ig34_p0154_a0014', 'ig34_p0154_a0015', 'ig34_p0154_a0029', 'ig34_p0154_a0030', 'ig34_p0155_a0002']
ledger md5 (unchanged): 438098704becc84eda01a925b80defaa
```

新断言的变异 (规则 5; `$R/mut.sh`, 每次改完输入后跑, 之后从 `$R/orig/` 还原; 输出 `$R/mut.out`):
- ① 清单 `relabel` 加一个不在 `atom_err` 的 id (`ig34_p0133_a021`, 一条 live-hit EXACT 原子). `errata rc=1`, `AssertionError: ('T4 R4L revoke: not an errata-only ATOM_ERR', 'ig34_p0133_a021', None)`; `t3_errata.json` md5 未变 (断言在写文件之前).
- ①b 加一个在 `atom_err` 里、但来源是 triage 的 id (`ig34_p0149_a009`). `errata rc=1`, 同一断言, 附该条目 (`source: triage_merged.json`).
- ② 加一个撤掉后得不出 EXACT 的 id: `ig34_p0122_a017` (同样只来自 t1 errata 的 S1-R1, pre_t3 也是 EXACT, KB 与原子不一致). 撤销断言通过, `errata rc=0`; writeback `rc=1`, `ASSERT: FAIL ['T4 R4L atom not live-hit EXACT: ig34_p0122_a017 EXACT residual-no-evidence in_k3b=False']`. 台账里这一行退回了 stock 行 (`EXACT None None`, 即 verdict EXACT、无 phase / rule) — 只查标签的话这一条会被放过, 所以断言查规则. writeback 是先写后断言, 所以随后整套还原并重跑了 runD.
- ③ writeback 用改前的 `t3_errata.json` (a001 仍在 `atom_err`, 无 `r4l_revoked`). `writeback rc=1`, `AssertionError: ('T4 R4L list != t3_errata r4l_revoked / still in atom_err / in R2L', ['ig34_p0124_a001'], [])`; 台账 md5 未变 (写之前).
- ④ `registry_ptr` 加一个不是 S1-R1 ATOM_ERR 的原子 (`ig34_p0412_a009`, PDF_TYPO). `writeback rc=1`, `AssertionError: ('T4 R4L registry_ptr atom not ATOM_ERR via S1-R1', 'ig34_p0412_a009', ('PDF_TYPO', 'writer-Tn-registry'))`; 台账 md5 未变.
- ⑤ direct_hit 对这条的独立检查: 在 `$R/kb_mut/` (`git archive HEAD knowledge_base` 副本, 不是真 KB) 里把 `ML/examples.md:42` 最后一格 `2015-09-03T17:00` 改成 `17:01`. `t3_direct_hit.py --kb-root` 该副本: `tb_exact_miss: 1 ['ig34_p0124_a001']`, `RESULT: RED`, rc=1. 副本已删; 真 KB `git status` 为空.
- 还原后: 台账 `eef9bb14…`、errata `76535530…`、清单 `c33abbe7…`. 之后从源头跑 runD, 7 个产物 md5 与 runC 逐一相同, 11 个日志与 runC 逐字相同.

## 4. 逐行 diff 汇总 (清单: `work/t4/r4l_ledger_diff.txt`, md5 `d9a4bc91…`)
| 类 | 条数 |
|---|--:|
| atomerr-not-hold ATOM_ERR → EXACT (规则 live-hit) | 1 |
| 只改非标签字段 (`matched_by.evidence.registry`, 4 条登记指针) | 4 |
| 逐字节相同 | 12487 |

- `ig34_p0124_a001` 新行 (第 3280 行): verdict EXACT, phase TB, batch_id `T4-R4L`, rule `live-hit`, prev_verdict EXACT (writeback 一向以 pre_t3 备份为基准), `hit_file` `knowledge_base/domains/ML/examples.md`, `hit_lines` [42]; evidence 去掉了 `errata` / `registry` / `checkpoint` / `basis` (这些是 S1 分支才写的键), 加了 `t4_r4l` (decision = "owner 2026-11-27 问题 C = C1 (evidence/checkpoints/t4_owner_confirmation.md 消息 5)", raw = 两位审查者的结果行, before = "ATOM_ERR (S1-R1, t1_errata t3_atom_err)", errata_revoked = `work/t3_errata.json#r4l_revoked/ig34_p0124_a001`, spec). 其余字段 (md_atom_ids / similarity_score / ts / prompt_version) 不变.
- 4 条指针行: 标签 ATOM_ERR、规则 S1-R1、batch_id T1/T2-errata 都不变, 只有 `evidence.registry`.

其它派生文件的变化 (改前副本 `$R/before/`):
- `t3_errata.json`: `atom_err` 235 → 234 (少这一条, 其余条目逐字相同); 新键 `r4l_revoked` (1 条, 原条目原样); `target_remap` / `pending_user` / `k4` / `_note` 不变.
- `t3_rules.json`: md5 不变 (`1096bec2…`).
- `t3_writeback_decisions.json`: 键集合不变 (2055); 只有 5 键变化: a001 (new ATOM_ERR → EXACT, rule S1-R1 → live-hit, batch → T4-R4L, evidence 同上) 与 4 条指针 (只有 evidence.registry).
- `t3_t4_risk_anchorless.txt`: 511 → 512, 加了这一条 (原因 "no governing numbered heading", `ML/examples.md:42`). 见 §6 第 2 条.
- `t3_t4_k3b_out_of_scope.txt`: 不变.
- `t3_audit_sets/`: 只有 `S1-R1__ATOM_ERR.txt` 少这 1 行. `live-hit__EXACT.txt` 不变 — `t3_report.py` 按 old ≠ new 统计 flip, 这条 old = 基线 EXACT, 所以 report 的 flipped 2009 → 2008、live-hit EXACT 仍为 1012; direct_hit 的 TB 计数 1034 含这一条.
- `section_coverage.wc.jsonl`: 含 ts. 用 `t3_recompute.py --ledger pre_r4l` 重算改前状态, 按位置对齐比较 (忽略 ts): 399 节里只有 §6.1.4 [Meal Data (ML)] 1 节变化 (matched 49 → 50, density 0.5269 → 0.5376, tb_verdict_counts), aggregate_verdict 不变; 全书分布不变.
- `t4_ack_lists.md`: ATOM_ERR 节去掉这一行, 后面的行重新编号; 汇总行 197 → 196、S1-R1 157 → 156、U-5 196 → 195; 4 条指针行的 "依据 / 登记" 列多了 `[登记 id]`, "决定来源" 列仍为 U-5 (按行逐字核过, 其余行只有编号变化); 状态行文字.
- runD 日志相对 run0 有变化的: `01_fp_head` (按台账标签统计的命中分布, EXACT 2306 → 2307 / ATOM_ERR 1 → 0)、`06_errata`、`07_writeback`、`08_direct_hit`、`10_report`、`11_global` (strict 9493 → 9494 等) — 都只差这一条; 其余日志逐字相同.

## 5. 没做 / 撤回的项
- 没有撤回的项: 4 条登记指针都补了, 没有引起标签或允许集变化 (这 4 条本来就在允许集里, 规则仍为 S1-R1).
- 指针行上没加出处键 (与 R2L 不同), 理由见 §2; 如要比照 R2L 在行上加 `t4_r4l_registry_ptr`, 只需在 writeback 那一段加一行, 由主控定.
- 没动 `B-CE T-2` 8 条 (问题 D = D1), 没动 `ig34_p0293_a038`.
- 没去查别的 S1-R1 原子是不是同一成因 (顺带话 + 折行表格让 K4 测不出). 本批只按主人 C1 处理这一条.

## 6. 已知局限 / 需主控定
1. **同一成因可能还有别的原子**. K4 的整行子串复核对逐格折行的表格行测不出来, 只要 t1 errata 里有一句不准的 "原子错", 就会留成 S1-R1. 相关事实见 `evidence/checkpoints/t4_atomerr_fullcheck.md` (那 83 条加查: 成立 82 / 不成立 1; 其余 S1-R1 原子此前由别的轮次逐条判过; `B-CE T-2` 8 条取决于口径). 我没有另做全量排查, 也没改 K4 机制.
2. 这条新 EXACT 进了 `t3_t4_risk_anchorless.txt` (无编号标题锚点). direct_hit 用 `valid_hits` 独立核过 (变异 ⑤ 证明它会变 RED). 锚点弱是 `ML/examples.md` 文件结构造成的, 与改标无关.
3. 这一行的 verdict 与 pre_t3 基线相同, 按旧口径本不重写. 这次强制重写成 TB 行, 所以 report 的 flip 计数反而少 1 (2009 → 2008), direct_hit 的 TB 计数加 1.
4. 新行 `matched_by` 的 `ts` 是 2026-11-26T12:00:00Z、`prompt_version` 是 t3_writer_v1.0, 早于主人的决定日. 这是沿用固定 ts 的结果 (同 R2L / R3L). 决定日期写在 `evidence.t4_r4l.decision` 里.
5. `scripts/t4/t4_atomerr_coverage.py` 改台账之后按设计会断言失败 (它的 C1 清单要求这一条仍为 ATOM_ERR); `t4_atomerr_sample.py` 断言旧台账 md5, 同样会失败. 两个都没改, 是否要改由主控定.
6. `scripts/t4/t4_gate_prerun.sh` (只读, 没跑) 的 md5 清单不含本批新增的 `coverage_ledger.wc.pre_r4l.jsonl` / `t4_r4l_relabel.json`. 是否补进去由主控定. 改台账后 `t0_mutation_head.sh --make-baseline` 要由主控重建.
7. 登记 id 用了 `B-RS T-6 (RS 副本)` 而不是规格写的 `B-RS T-6` (登记表里没有裸 id), 见 §2.
8. **从清单里删掉条目不会报错**: 若把 `ig34_p0124_a001` 从 `work/t4_r4l_relabel.json` 的 `relabel` 里删掉, errata 不再撤销, 它会悄悄回到 S1-R1 ATOM_ERR, writeback 仍 `ASSERT: OK`. R3L 有 keep 清单 `t4_r3l_drop` 集合 = 清单的交叉断言, 能抓到删除; R4L 没有对应的第二处数据可以对照 (`t1_errata.json` 只读不改). 本批没加代码, 需要的话由主控定.

## 7. md5 (终态)
| 文件 | md5 |
|---|---|
| `work/coverage_ledger.wc.jsonl` | `eef9bb14e5afab7e68a231ddd18cfa1c` |
| `work/coverage_ledger.wc.pre_r4l.jsonl` (备份) | `438098704becc84eda01a925b80defaa` |
| `work/t4_r4l_relabel.json` | `c33abbe7893160a020044b0d27d60d51` |
| `work/t3_errata.json` | `765355300d3c473fad601dd44b1492a5` |
| `work/t3_rules.json` (不变) / `t3_writeback_decisions.json` | `1096bec29fa25711b250d70711093002` / `8aa949c10f0aaa51178b1d372cecbc5f` |
| `work/t3_k3b_out_of_scope_keep.json` / `t3_t2s_atoms.jsonl` / `t3_fp_expected_regressions.jsonl` (都不变) | `1e99f101…` / `33ef2fe0…` / `e7df6ce0…` |
| `evidence/checkpoints/t4_ack_lists.md` | `04e72e7537f0508af496997dd21613f0` |
| `work/t4/r4l_ledger_diff.txt` | `d9a4bc918e7d9e09e23991f5eb87eedc` |
| `work/t4/t4_mutation_r4l.log` | `502f7f5d7a100aa4c69a8b68a8549e72` |
| `scripts/t3/t3_errata_build.py` / `scripts/t3/t3_writeback.py` | `0e3911c6e4c97cd5eb777dd19e41bb04` / `5db98492fe5c717cf48240c8a067e3f5` |

## 8. 小修 (reviewer M-1 / L-1 / L-3)
> 2026-11-28, 同一 writer (`oh-my-claudecode:executor`). 依据: `evidence/checkpoints/t4_round4_ledger_review.md` §2 (M-1 / L-1 / L-3); 主控只要求这三处 (L-2 / L-4 / L-5 主控登记为已知). 只改了两份脚本; 数据、台账、KB 都没改. 改前脚本副本: `work/scratch/t4/r4l/before_fix/`.

| 项 | 改的位置 (小修后行号) | 做法 |
|---|---|---|
| M-1 | `scripts/t3/t3_errata_build.py:243-245` | 段 (6) 读清单后断言 `set(relabel)` = `work/t4/atomerr/verdicts.json` 里判定为 NOT_HOLD 的 id 集合, 且后者非空 (第二个数据源). 在 `json.dump` 之前 |
| M-1 | `scripts/t3/t3_writeback.py:74-77` | 读清单后断言 `t3_errata.json` 的 `r4l_revoked` 非空, 且 `set(relabel)` = verdicts.json 的 NOT_HOLD 集合. 模块级, 在写台账之前 (原有的 "清单 = r4l_revoked 键集" 断言保留) |
| L-1 | `scripts/t3/t3_writeback.py:542-546` | 原来的一条 assert 拆成两条: 先 `登记 id ∈ REG_IDS` (报文 "registry id not in t2_pdf_typo_registry.jsonl", 列出不存在的 id), 再 `decided = (ATOM_ERR, S1-R1)` (报文不变) |
| L-3 | `scripts/t3/t3_errata_build.py:248-249` | 撤销循环第一句断言 `i not in t1_errata.pending_user` (放在 errata-only 断言之前, 让变异 ④ 能单独打到它) |

两遍整链 (`bash $R/run_chain.sh $R/runG`; `… $R/runH`; 小修中途另跑过 runE / runF, 那时 L-3 断言还在 errata-only 断言之后, 结果相同):
- `diff runD/md5.txt runG/md5.txt`、`diff runG/md5.txt runH/md5.txt` 都为空. 7 个产物 md5 与小修前 (runD) 相同: ledger `eef9bb14e5afab7e68a231ddd18cfa1c`; errata `765355300d3c473fad601dd44b1492a5`; t2s `33ef2fe0f125ca57cef568d33cfc01ae`; fp_expected `e7df6ce0e92abd6c002ded3da534ffc0`; keep `1e99f1010ff402f738fc57b2884d1954`; rules `1096bec29fa25711b250d70711093002`; decisions `8aa949c10f0aaa51178b1d372cecbc5f`.
- runH 的 11 个日志与 runD 逐字相同 (`ASSERT: OK`, direct_hit GREEN). `rdiff.py` 仍为 `identical 12487; label-changed 1; other-changed 4`. ack 清单重生成 md5 仍为 `04e72e75…`.
- 脚本新 md5: `t3_errata_build.py` `acc7e86f2bcf79df47b82e2b83325d20`; `t3_writeback.py` `890055907034255da717d5c34b63c3d7` (§7 表里的是小修前的值).

变异 (`$R/mut_fix.sh`, 输出 `$R/mut_fix.out`; 每个都照整链的顺序先跑 errata 再跑 writeback, 之后从 `$R/orig_fix/` 还原):
- ① `relabel` 置空: errata `rc=1`, `AssertionError: ('T4 R4L relabel ids != NOT_HOLD ids of work/t4/atomerr/verdicts.json', [], ['ig34_p0124_a001'])`, errata 文件未写; writeback `rc=1`, `('T4 R4L list != t3_errata r4l_revoked / still in atom_err / in R2L', [], ['ig34_p0124_a001'])`, 台账未写.
- ①b 同上, 再把 `t3_errata.json` 换成改前副本 (没有 `r4l_revoked`, 即 errata 那道断言被绕过的情况): writeback `rc=1`, 新断言 `('T4 R4L: r4l_revoked empty or relabel ids != verdicts.json NOT_HOLD', [], [], ['ig34_p0124_a001'])`, 台账未写.
- ② `relabel` 多放 `ig34_p0122_a017` (verdicts.json 判 HOLDS): errata `rc=1`, `('T4 R4L relabel ids != NOT_HOLD ids …', ['ig34_p0122_a017', 'ig34_p0124_a001'], ['ig34_p0124_a001'])`, errata 文件未写; writeback `rc=1` (清单 ≠ r4l_revoked), 台账未写.
- ③ 指针 `ig34_p0339_a001` 改成裸 `B-RS T-6`: errata `rc=0`; writeback `rc=1`, `('T4 R4L registry_ptr: registry id not in t2_pdf_typo_registry.jsonl', 'ig34_p0339_a001', ['B-RS T-6'])` — 报文说的是登记 id 不存在; 台账未写.
- ④ `relabel` 多放 pending_user 里的 `ig34_p0011_a020`, 并且在 verdicts.json 副本里把它也标成 NOT_HOLD (否则 M-1 断言先报): errata `rc=1`, `('T4 R4L revoke: atom is in t1_errata pending_user', 'ig34_p0011_a020')`, errata 文件未写; writeback `rc=1` (清单 ≠ r4l_revoked), 台账未写. verdicts.json 已还原 (md5 `7f1f5e3e…`).
- 所有报错都在写台账之前 (writeback 的这几条都是模块级 assert; errata 的在 `json.dump` 之前). 还原后: ledger `eef9bb14…`、errata `76535530…`、清单 `c33abbe7…`、verdicts `7f1f5e3e…`; 之后跑的 runG / runH 见上.
- §6 第 8 条 (清单删空不报错) 由本节的 M-1 断言补上; 剩下的前提是 `verdicts.json` 本身不被同时改动.

收尾检查: `git status --short knowledge_base archive releases web` 为空; `git rev-parse HEAD:knowledge_base` = `63f857774a42cfaa71798705ad40ab51bc5e378a`; `python3 tools/check_links.py 2>&1 | grep "live docs"` = `broken relative links: 18668 (live docs: 42)`.
