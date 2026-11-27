# T4 第二轮改台账 (R2L) — writer checkpoint
<!-- chain: E (plans) -->
> 状态: writer 已完成 (2026-11-27, `oh-my-claudecode:executor`, attempt 1), 等 reviewer 复跑逐行核、verifier 审计 (规则 D). 本文不给自己判 PASS.
> 规格: `subagent_prompts/t4/t4_round2_ledger_spec_v1.0.md`. 依据: 主人 2026-11-27 直接消息 (1A / 2A / 3A / 7b-A / 9A), `evidence/checkpoints/t4_owner_confirmation.md` 第二轮.
> 结果: 台账 md5 `60729f7b64b7c1dfaf2174e394f6dd9c` → **`16024ac09721cb3f8519cd68fa455196`** (源头整链跑两遍一致). 标签变化恰好 78 条, 方向全部与清单一致. 清单外**没有**标签变化. 清单外只有 5 行非标签字段变化, 都是 §2.3 登记指针.
> §2 各项全部做了, 没有撤回: 没有一项引起标签变化.
> 未动: `knowledge_base/` (`HEAD:knowledge_base` = `63f857774a42cfaa71798705ad40ab51bc5e378a`, 工作树无改动, 真 KB 内容 md5 `b71a466d…` 变异前后一致); `archive/`、`releases/`. 未 git add / commit / push. 没跑 `t0_mutation_head.sh` / `t4_sample.py` / `t4_render.py` / `t4_supp_report.py` / `t4_c3_report.py`.
> scratch (gitignored): `work/scratch/t4/r2l/` (`run_chain.sh` = W3 同名脚本原样复制; `step.sh`、`rdiff.py`、run0 / runA / runB 日志、各步台账副本与 diff、`before/` 改前副本).

## 0. 命令 (仓库根目录; T=.work/10_tier_b_repair, R=$T/work/scratch/t4/r2l)
```bash
cp $T/work/coverage_ledger.wc.jsonl $T/work/coverage_ledger.wc.pre_r2l.jsonl          # 规则 B 备份 (入库), md5 60729f7b…
bash $R/run_chain.sh $R/run0                       # 改任何输入之前先跑一遍 §A4.5 整链: 台账仍为 60729f7b… (基线可复现)
python3 -I $T/scripts/t4/t4_r2l_build.py           # 一次性生成数据清单 work/t4_r2l_relabel.json (之后清单即源数据)
#   改 t3_errata_build.py / t3_writeback.py (见 §1) → bash $R/step.sh step1 ...   (只重跑 errata + writeback 两步)
python3 -I $T/scripts/t4/t4_r2l_registry_fix.py add basis suppqual; bash $R/step.sh s2a step1
python3 -I $T/scripts/t4/t4_r2l_registry_fix.py page;               bash $R/step.sh s2b s2a
python3 -I $T/scripts/t4/t4_r2l_registry_fix.py pdfvalue;           bash $R/step.sh s2c s2b
#   writeback 加登记指针 (§2.3 决策表部分) → bash $R/step.sh s2d s2c
bash $R/run_chain.sh $R/runA; bash $R/run_chain.sh $R/runB; diff $R/runA/md5.txt $R/runB/md5.txt   # 空 = 一致
python3 $R/rdiff.py $T/work/coverage_ledger.wc.pre_r2l.jsonl $T/work/coverage_ledger.wc.jsonl $T/work/t4/r2l_ledger_diff.txt
python3 -I $T/scripts/t4/t4_ack_lists.py
python3 $R/check_fields.py                                                  # 78 行写法逐行断言 + scenarios 那一项
python3 -I $T/scripts/t3_recompute.py --ledger $T/work/coverage_ledger.wc.pre_r2l.jsonl --out $R/sc_pre_r2l.jsonl   # 只用于节级对照
python3 -I $T/scripts/t4/t4_coverage_decomp.py; python3 tools/check_links.py 2>&1 | grep "live docs"
bash $T/scripts/t3/t3_mutation.sh > $T/work/t4/t4_mutation_r2l.log 2>&1
python3 -I $T/scripts/t3/t3_reverse_trace.py --rev WORKTREE --out $R/reverse_trace_r2l.json      # 只读对照 (不在 §3 清单里)
git status --short knowledge_base archive releases; git rev-parse HEAD:knowledge_base; git diff --quiet HEAD -- knowledge_base
```
- `--ts 2026-11-26T12:00:00Z` 不变, 所以没改判的行与备份逐字节相同.
- `rdiff.py` 做的是整行比较: 按位置对齐, 逐行断言 `pdf_atom_id` 相同 (有 11 个重复 id), 比较全部字段 (含 `category` / `exclusion_reason` / `approved_by`).

## 1. 78 条标签 (规格 §1)
| 项 | 机制 | 改的文件 |
|---|---|---|
| 数据清单 | `scripts/t4/t4_r2l_build.py` (一次性; 脚本里的 KEEP / PTR 两个字典是生成用的手写数据, 生成后的 `work/t4_r2l_relabel.json` 是运行时唯一来源, errata_build / writeback 只读该 JSON) 从 `work/t4/supp/relabel_pending.json` 取 4 组共 78 条, 写 `work/t4_r2l_relabel.json`. `typo-overlabel` 组不取. 每条带 group / now / to / raw / decision; PDF_TYPO 的带 registry. 生成时断言 78 条、`raw` 的 文件:行 存在、registry id 存在 | 新增 `scripts/t4/t4_r2l_build.py`、`work/t4_r2l_relabel.json` (md5 `3e7e6eba…`) |
| IE 53 (R1-row 51 + v2.0-TOC 2) | `t3_writeback.py` 读清单, 53 条进允许集; `decide()` 新增规则 `T4-R2L-owner-IE`, 放在 FIGURE 之后、K3b / live-hit 之前. 这 53 条原是 stock 行, 本不在允许集里; 终态 `evidence.hit_file` 53 条全为空 (`$R/check_fields.py`), 所以这个位置只是保险, 不是必需. 写 `verdict` = INTENTIONAL_EXCLUDE、`category` = VERSION_MISMATCH; `exclusion_reason` = 规格给的两种文字; `approved_by` = "owner 2026-11-27: evidence/checkpoints/t4_owner_confirmation.md 第二轮 (问题 1 = A)" / "(问题 2 = A)". `matched_by.evidence.t4_r2l` 带 group / decision / raw / 规格出处. `IE flip not in t1_ie_final` 断言只对本规则的这 53 条放行, `t1_ie_final.md` 没改 | `scripts/t3/t3_writeback.py` |
| PDF_TYPO 25 (范围内 19 + 范围外 6) | `t3_errata_build.py` 新增第 (5) 段: 读清单, `put(i, "R2", …)` 进 atom_err, 终态 PDF_TYPO, registry = 清单给的 id (运行时断言 id 在 registry 里). source = "T4 R2L (group; owner 2026-11-27 问题 3 = A / 问题 7b = A …)"; checkpoint 指针 = 该条的 `raw`. 范围外 6 条另带 U-8 keep 式的 pdf 行 + token、kb 行 + token, 运行时断言 (断言失败 exit 1). writeback 按现有 S1-R2 规则落 PDF_TYPO | `scripts/t3/t3_errata_build.py` |
| 新断言 (writeback) | 78 条终态必须 = 清单 `to`; IE 53 条必须由 `T4-R2L-owner-IE` 判出, 不能在 K3B、不能是 FIGURE; PDF_TYPO 25 条必须由 S1-R2 判出. errata 侧断言 25 条在 put 之前都不在 atom_err 里. writeback 断言 IE 53 条与 atom_err 不相交 | 同上 |

- 中间态 (只做 §1, step1): 逐行 diff 恰好 78 行不同, 其余 12414 行逐字节相同. 四个覆盖率数此时已经等于 scenarios.
- 范围内 19 条为什么不走 `s0_classify` / `T4_U7_REG` 原样:
  - 它们不是 fp 回归. 加进 s0 要改 `== 121` 条目定值.
  - 其中 5 条 EXACT 仍逐字命中 KB (终态 `hit_file` 非空; 另 4 条 EXACT 本来就没有有效命中). S0 对非 R3 条目命中会报 `unexpected-hit`.
  - 所以做成 errata 里的逐原子 registry 绑定 (与 `T4_U7_REG` 同一种做法), 数据在清单文件里, 不在脚本里写 id.
- 范围外 6 条为什么不进 keep 清单: 见 §5 第 1 条.

## 2. 登记更正 (规格 §2; `scripts/t4/t4_r2l_registry_fix.py`, 每行加字段 `t4_r2l_fix` 记 before → after 与依据; 新行带 `t4_decision`)
按 "先不进判定的、再页号、再 pdf_value、最后指针" 逐项叠加. 每项之后重跑 errata + writeback, 再与上一步做逐行 diff.

| # | 项 | 做法 | 与上一步的台账 diff | 结论 |
|---|---|---|---|---|
| 2.2 | 补两条 "PDF 自身不一致" 登记 (问题 9 = A) | 新增 `T4R2 sv20 N-1`: model/04:42; sv20 p69 §6.6 SREL 的 "subject or pool" vs p50 的 "device"; KB 只收 p50. 新增 `T4R2 RELSPEC N-1`: RELSPEC/examples.md:17; p440 图 Brain vs 表 TISSUE; KB 照录. 两条都是 batch `T4-R2L`、`handling` = 照录、`t4_decision` = "owner 2026-11-27 问题 9 = A (补登记)". `pdf_value` 写成描述句, 避免 K4 当子串匹配 | 0 行 (逐字节相同) | 做了 |
| 2.3a | `basis` 文字 (S-SPC2 N-1 / N-2、B-NV N-1 / N-2) | 去掉 "照录" 字样, 改写为 "…; KB 写正确值 (U-7 B)". `S-SPC2 N-2` 不只去掉 "照录": 原 basis "应为 PPGRPID, 照录" 里的 PPGRPID 是草稿候选值 (有误, 该行 `note` 已注明), 一并改为 "应为 PC records / PCGRPID (同页 relrec RDOMAIN=PC, IDVAR=PCGRPID)", 依据 `evidence/t4_round3_raw/pack_9.md:57` | 同上 (与 2.2 同一步 s2a) | 做了 |
| 2.3b | B-SUPPQUAL T-1 位置清单 | 新字段 `other_kb_lines` = [`knowledge_base/chapters/ch08_relationships.md:228`]. 没改 `span_lines_in_file`: 该字段只对应本行的 kb_file | 同上 | 做了 |
| 2.1 | 页号 B-IS T-6 241 → 239、B-CP T-5 211 → 212 | B-IS 依据 `ig34_p0239.txt:35,39,43`. B-CP 依据 `pack_sib2_1.md:34`, 自己又核了 `ig34_p0212.txt:2-6`: Ex2 row 6 的 CPDTC 尾段为 "16T04:20", 同表其余行为 12:20; p211:3 的 "04:20" 属上一个例子 | 0 行. 副作用只在 `t3_rules.json`: K3b 新触及 `ig34_p0212_a001` (B-CP T-5, 规则 a). 该原子本轮已由 S1-R2 定为 PDF_TYPO, S1 先于 K3b, 标签与规则名都不变 | 做了 |
| 2.3c | `pdf_value`: B-CP T-3 (实为 "(e.g.," 未闭合)、S-SPC1 CP T-16a (补 `"CD278+`) | B-CP T-3 改成 PDF 原文 "(e.g., CD40+ in rows 15-16 in addition to non-cell state, non-sublineage marker(s). Rows 17-18". T-16a 改成两处 " / " 连写 | 0 行; `t3_rules.json` 也不变 | 做了 |
| 2.3d | 决策表登记指针 | `t3_writeback.py` 在 decide 之后读清单的 `registry_ptr`, 往 `evidence.registry` 末尾追加 id, 另记 `evidence.t4_r2l_registry_ptr` (add / raw / note). 断言该原子终态 PDF_TYPO、id 存在. `registry[0]` 和 batch_id 不变. 共 5 条: `ig34_p0355_a027` + B-TR T-1; `ig34_p0356_a001` (p356 Row 27) + B-TR T-1; pack_8 的 T178 `ig34_p0198_a014` + REG BS N-1; T183 `ig34_p0206_a009` + S-SPC1 CP T-16a; T200 `ig34_p0263_a020` + B-MB T-2 | 5 行, 只改了指针字段 | 做了 |
| 2.4 | `t4_ack_lists.py` | 新分支: errata source 以 "T4 R2L" 开头 → "主人 2026-11-27 第二轮 问题 3 = A / 问题 7b = A (evidence/checkpoints/t4_owner_confirmation.md 第二轮), 非 U-5; 登记 …". 放在 "registry 有 t4_decision → U-7" 之前, 避免被误归 U-7. 状态行补一句第二轮来源; 生成标记改为 "R2L 重生成; 上一次为解冻轮 W3" | 不影响台账 | 做了, 重生成 `t4_ack_lists.md` |

registry 272 + 2 = **274** 行, 其中 9 行改了字段: 页号 2、basis 4、SUPPQUAL 1、pdf_value 2. md5 `e6f86b49…`.

## 3. 验收 (规格 §3; 输出摘自 `$R/runB/` 日志与命令回显)
| 项 | 命令 | 输出 | 判定 |
|---|---|---|---|
| 改动集 | `rdiff.py` (见 §0) | `rows 12492 / 12492; identical 12409; label-changed 78; other-changed 5`; `listed atoms not changed: []`; 78 条全部 `OK` (方向与清单一致), `NOT-IN-LIST` 0 | 符合 |
| 行数 / 重复 id | 同上 + `wc -l` | 12492; 78 条都没有重复 id, 11 个重复 id 的行不在 diff 里 | 符合 |
| 两遍 md5 | `diff runA/md5.txt runB/md5.txt` | 空. ledger `16024ac09721cb3f8519cd68fa455196`, errata `b6065206…`, rules `25b9c54b…`, decisions `a3e8c8f1…`, t2s `33ef2fe0…` (不变), fp_expected `e7df6ce0…` (不变), keep `9053d986…` (不变) | 符合 |
| s0_classify | runB `04_s0.log` | `not in t3 list (NEW): []`; `BAD []`; `Counter({'R3': 47, 'R2': 42, 'R1': 32}) R4 = 0` | 符合 (与改前相同) |
| t3_direct_hit | runB `08_direct_hit.log` | `TB(all)=1029 stock(§5.0 scope)=1748`; tb_exact_miss / k11_short / anchor_lost / unexplained 全为 0; pre_existing 52; `RESULT: GREEN` | 符合. EXACT 数的变化见表下 |
| t3_recompute | runB `09_recompute.log` | `§5.0 scope sections=174 residual_gap=0 G-TB1 pass=174/174 G-TB2 pass=157/174` | 符合 (G-TB2 字面口径 157 不变) |
| 覆盖率四个数 | `t4_coverage_decomp.py`; `check_fields.py` 末行读出 scenarios 那一项 | strict `9489/9933 = 95.5301%`; mapped `9489/9551 = 99.3509%`; U-1 B `9860/9933 = 99.2651%`; content `8655/9551 = 90.6188%` | 与 `scenarios.json` 那一项 (`n 78, u1b 9860/9933 = 99.2651%, strict 9489/9933 = 95.5301%, mapped 9489/9551 = 99.3509%, content 8655/9551 = 90.6188%, g1 174/174, g2_literal 157/174, residual 0`) 逐字相同 |
| live docs | `check_links.py` | `broken relative links: 18668 (live docs: 42)` | 符合 |
| t3_mutation | `work/t4/t4_mutation_r2l.log` | M0 GREEN; M1 RED (tb_exact_miss `ig34_p0133_a021`); M2 GREEN; M3 RED (anchor_lost `ig34_p0064_a001`); M4 RED (tb_exact_miss 4); M5 RED (anchor_lost `ig34_p0295_a020`); M6 RED; M7 GREEN; `real KB md5 before/after b71a466d6e618f995c493a82de3e3eb7`, `real KB unchanged: OK` | 符合. 没有靶子因本次改标失效 |
| KB / 冻结区 | `git status --short knowledge_base archive releases` / `git rev-parse HEAD:knowledge_base` / `git diff --quiet HEAD -- knowledge_base` | 空 / `63f857774a42cfaa71798705ad40ab51bc5e378a` / 无改动 | 符合 |
| 78 行写法 (规格 §1 写法要求) | `python3 $R/check_fields.py` | `checked 78 bad []`. 逐行断言: IE 53 条的 `category` / `exclusion_reason` / `approved_by` 按 group 等于规格原文, `evidence.t4_r2l.raw` = 清单 raw, rule = T4-R2L-owner-IE; PDF_TYPO 25 条的 `evidence.registry` = 清单, `evidence.checkpoint` 以 raw 结尾 (`basis` 有 `[:200]` 截断, 指针以 checkpoint 为准), `basis` 以决定来源开头, rule = S1-R2. hit_file 计数: 只有 registered-typo 的 5 条 EXACT 非空, 其余 73 条为空 | 符合 |
| 新断言的变异 (规则 5; 只做 errata 侧) | 把清单里 `ig34_p0316_a023` 的 pdf token 改成 `laterallityX`; 另一次把 `ig34_p0037_a002` 的 registry 改成 `B-ch04 T-999`. 每次先 `grep -c` 确认改动已写入 (1 处), 再跑 `t3_errata_build.py`, 然后 `cp` 还原 | 两次都 `errata rc=1`: `AssertionError: ['ig34_p0316_a023']` / `AssertionError: ('ig34_p0037_a002', ['B-ch04 T-999'])`. errata md5 前后都是 `b6065206…` (断言在写文件之前). 还原后清单 md5 = `3e7e6eba…` | 符合. writeback 侧的断言没做变异: 它先写台账后断言 |
| writeback ASSERT | runB `07_writeback.log` | `T4 R2L: 78 listed; final label as listed: 78 \| IE 53`; keep 25/25; K3b 扩展断言 0; 范围外 0; `ASSERT: OK` | 符合 |

direct_hit 的 EXACT 数 (改前 = run0):
- TB EXACT 1030 → 1029. 少的 1 条是 `ig34_p0064_a012`, 原为 live-hit, 现转 PDF_TYPO.
- stock (§5.0) EXACT 1758 → 1748. 少的 10 条 = R1-row 的 2 条 EXACT + registered-typo 的 8 条 stock EXACT.
- pre_existing 58 → 52. 少的 6 条是本批 EXACT 里本来就没有有效命中的原子, 现在不是 EXACT 了, 所以不再参与检查: `sv20_p0069_a001` / `a003`, 以及 `ig34_p0147_a025`、`ig34_p0262_a016` / `a017`、`ig34_p0296_a023`.
- 后 4 条的情况与 "KB 写正确值" 一致.
- 范围外那 1 条 EXACT (`ig34_p0083_a020`) 本来就不在 stock 检查范围内.

## 4. 逐行 diff 汇总 (清单: `work/t4/r2l_ledger_diff.txt`, md5 `cb8ae67a…`)
| 类 | 条数 |
|---|--:|
| R1-row EQUIVALENT → INTENTIONAL_EXCLUDE | 49 |
| R1-row EXACT → INTENTIONAL_EXCLUDE | 2 |
| v2.0-TOC EQUIVALENT → INTENTIONAL_EXCLUDE | 2 |
| registered-typo EQUIVALENT → PDF_TYPO | 10 |
| registered-typo EXACT → PDF_TYPO | 9 |
| registered-typo-oos EQUIVALENT → PDF_TYPO | 5 |
| registered-typo-oos EXACT → PDF_TYPO | 1 |
| **标签变化合计** (全部在清单内且方向一致) | **78** |
| 只改指针字段: `evidence.registry` 追加 + `evidence.t4_r2l_registry_ptr` (§2.3d) | 5 |
| 逐字节相同 | 12409 |

- 77 条原来是非 TB 行 (76 条没有 matched_by.phase, 1 条 phase = P6_T5), 现在改写成 TB 行 (`phase` = TB, `subagent_type` = script/t3_writeback).
- 另 1 条 `ig34_p0064_a012` 原来就是 TB live-hit 行. 它的 `prev_verdict` 记的是 PARTIAL: writeback 一向以 pre_t3 备份为基准, 不是改前台账的 EXACT. 方向核对以 `pre_r2l` 备份为准.

其它派生文件的变化 (改前副本 `$R/before/`):
- `t3_errata.json`: atom_err 新增 25 键, 其余不变.
- `t3_writeback_decisions.json`: 新增 77 键; `ig34_p0064_a012` 的 new / rule / evidence 变化; 5 条指针原子的 evidence 变化.
- `t3_rules.json`: K3b / K3b_why 多 `ig34_p0212_a001` (见 §2.1).
- `t3_t4_risk_anchorless.txt`: 508 → 507, 去掉 `ig34_p0064_a012`.
- `t3_audit_sets/`: 改 `S1-R2__PDF_TYPO.txt`、`live-hit__EXACT.txt`, 新增 `T4-R2L-owner-IE__INTENTIONAL_EXCLUDE.txt`.
- `section_coverage.wc.jsonl`: 含 ts; 另有 17 节的 aggregate_verdict 或 IE 计数变了. 比对方法: 用 `t3_recompute.py --ledger pre_r2l --out $R/sc_pre_r2l.jsonl` 重算改前状态, 按位置对齐比较. section_id 有重复, 不能按 id 比.
  - 转 SKELETON_ONLY 的 5 节 (35 → 40): ig34 §4.3.2; sv20 §5.1.2、§5.1.3.2、§5.1.4.3、§5.1.5.
  - 其它: ig34 §5.3 SE (范围外) FULL → MOSTLY; ig34 §5.2 DM–Examples、§6.2.2 BE MOSTLY → CONTENT_TRUNCATED; sv20 另 9 节只增加 IE 计数.
  - "current Tier B sections" 101 → 98. §5.0 闸口径 (174/174, 残留 0) 不变. scenarios 没有预报节级分布.
- ack 清单里原有的 5 行 (`ig34_p0198_a014` / `p0206_a009` / `p0263_a020` / `p0355_a027` / `p0356_a001`) 的 "依据 / 登记" 列因 §2.3d 的指针补全追加了 id; 这 5 行的决定来源未动 (仍为 U-5).
- ack: ATOM_ERR 197 / PDF_TYPO **174** (149 + 25) / FIG 11. 来源: U-5 329 / U-7 22 / U-8 4 / U-2 1 / 主控 M-4 1 / 主人第二轮 3 = A 19 / 7b = A 6. "(未归因)" 0 (断言通过). md5 `aafe246b…`.
- 只读对照 `t3_reverse_trace.py --rev WORKTREE`: 5414 行全部溯源, UNEXPLAINED 0, NOTE_EXEMPT 5/5. 与 W3 终态相比只有 1 行换类: model/04:42 由 TABLE_TOKENS 变为 PDF_TYPO, 因为新登记 `T4R2 sv20 N-1` 锚在该行.

## 5. 需主控定 / 已知局限
1. **范围外 6 条没照字面 "比照 U-8 keep 机制" 进 `t3_k3b_out_of_scope_keep.json`**.
   - 原因一: 用 `K3b` / `K3b_out_of_scope` 查过, 这 6 条都没被 K3b 触及. 写成 keep_k3b 会撞上 "keep_k3b entry no longer touched by K3b rules" 断言.
   - 原因二: `t4_ack_lists.py` 按 keep 清单的 `t4_decision` 归来源, 会把它们误归 U-8.
   - 实际做法: 走 errata R2 (与范围内 19 条相同), keep 式的 pdf / kb 行 + token 断言放在 `work/t4_r2l_relabel.json` 里, 由 errata_build 运行时核对.
   - 标签结果与字面做法应相同, 这里只是机制不同. 是否认可, 请主控定.
2. IE 53 条用的是新规则 `T4-R2L-owner-IE`, 位置在 FIGURE 之后、K3b / live-hit 之前. `IE flip not in t1_ie_final` 断言对它放行. `t1_ie_final.md` 没有加这 53 条: 它们的认可依据是主人第二轮, 不是 T1 ack.
3. B-SUPPQUAL T-1 用的是新字段 `other_kb_lines`, 不是改 `span_lines_in_file`. 审查者 (`pack_sib_3.md:67`) 还建议核对映射到 ch08:228 的 p433 原子的标签, 这超出本规格, 没做.
4. 没做 §3 清单外的检查: `t0_mutation_head.sh` 的基线按规格由主控在 reviewer 通过后重建; census 不受台账影响, 没跑.
5. 工作树里另有三个文件不是本轮改的, 开工时就已是未提交改动, 我没有碰: `evidence/checkpoints/t4_user_decisions.md`、`work/out_of_scope_findings.md`、`trace.jsonl`.
   - run0 用这棵工作树复现出 `60729f7b…`, 说明它们不影响台账.
6. 78 行新 `matched_by` 的 `ts` 是 2026-11-26T12:00:00Z、`prompt_version` 是 t3_writer_v1.0. 这两个值早于主人的决定日, 是沿用固定 ts 造成的 (这样没改判的行才能逐字节不变). 决定日期与规格出处写在 `evidence.t4_r2l` / errata basis 里.
7. 两个脚本的头部 docstring 已同步: writeback 规则表加 2b, 并写明 IE 断言的例外; errata_build 加第 (5) 段的说明. 改完重跑了 runA / runB, md5 仍一致.
8. `typo-overlabel` 4 条 (`ig34_p0412_a006` / `a007` / `a008`、`ig34_p0413_a010`) 与 `ig34_p0293_a038` 维持 PDF_TYPO, diff 里没有这几条.

## 6. md5 (终态)
| 文件 | md5 |
|---|---|
| `work/coverage_ledger.wc.jsonl` | `16024ac09721cb3f8519cd68fa455196` |
| `work/coverage_ledger.wc.pre_r2l.jsonl` (备份) | `60729f7b64b7c1dfaf2174e394f6dd9c` |
| `work/t3_errata.json` / `t3_rules.json` / `t3_writeback_decisions.json` | `b6065206…` / `25b9c54b…` / `a3e8c8f1…` |
| `work/t2_pdf_typo_registry.jsonl` | `e6f86b49f7daac2bad76625f243a1683` |
| `work/t4_r2l_relabel.json` | `3e7e6eba4b2d311b7601b54d7f007248` |
| `evidence/checkpoints/t4_ack_lists.md` | `aafe246bd44907dff30aea748d3ed084` |
| `work/t4/r2l_ledger_diff.txt` | `cb8ae67acc908e1abc82569f43b88845` |

## reviewer 意见后的小修 (2026-11-27; reviewer 判 PASS 后的 4 条, 经协调方转达)
1. **(MEDIUM) errata 范围外 token 断言改为按 group 强制** (`scripts/t3/t3_errata_build.py` 第 (5) 段循环开头, 约 :141-143). 原来的 `if "pdf" in e:` 改为:
   - 先断言 `("pdf" in e) == ("kb" in e) == (e["group"] == "registered-typo-oos")`;
   - 再按 `e["group"] == "registered-typo-oos"` 执行 pdf / kb 行 + token 核对.
   - 断言放在 `continue` 之前, IE 组带了这两个键也会报错.
   - 变异 (每次先确认改动已写入, 再跑 `t3_errata_build.py`, 之后 `cp` 还原):
     - ① 复现 reviewer 的做法: 删 `ig34_p0316_a023` 的 `pdf` 键, kb token 改为 `no-such-token-r2l`. 结果 `errata rc=1`, `AssertionError: ('ig34_p0316_a023', 'registered-typo-oos', ['decision', 'group', 'kb', 'now', 'raw', 'registry', 'to'])`.
     - ② 给 IE 组的 `sv20_p0046_a002` 加 `pdf` 键. 结果 `errata rc=1`, `AssertionError: ('sv20_p0046_a002', 'R1-row', ['decision', 'group', 'now', 'pdf', 'raw', 'to'])`.
     - 两次 errata md5 都保持 `b6065206…` (断言在写文件之前). 还原后清单 md5 = `3e7e6eba…`.
2. **(LOW) writeback R2L 断言不再 KeyError** (`scripts/t3/t3_writeback.py` 约 :592-595):
   - 先把不在 `decided` 里的清单原子收进 bad, 写成 "T4 R2L atom not in allowed set / not decided: …";
   - 循环只遍历已判定的原子.
   - 这一处没做变异: 要构造 "清单原子不在允许集" 只能改代码; writeback 又是先写台账后断言.
   - (主控注, 依 reviewer delta 复审 LOW: 上一句不准. 只改数据即可构造 — 从 `work/t3_errata.json` 的 `atom_err` 里删一条 PDF_TYPO 原子; reviewer 已在隔离副本里做了这个变异 (W1), writeback rc=1 并报出可读断言. 见 `t4_round2_ledger_review.md` 的 delta 复审一节.)
3. **(LOW) checkpoint 补写**:
   - §2 的 2.3a 行写明 `S-SPC2 N-2` 的 basis 另把 PPGRPID 改为 PC records / PCGRPID (依据 `pack_9.md:57`);
   - §4 补了 ack 中 5 行登记列追加 id 的说明;
   - §1 写明 `t4_r2l_build.py` 的 KEEP / PTR 是一次性手写数据, `work/t4_r2l_relabel.json` 是运行时唯一来源.
4. **从源头整链重跑** (`bash $R/run_chain.sh $R/runC`), 7 个产物 md5 与 runB 逐一相同:
   - ledger `16024ac09721cb3f8519cd68fa455196`;
   - errata `b606520637bc3c13b0f8f79dea6c81f6` / rules `25b9c54b67986b518669e8e5b57061e3` / decisions `a3e8c8f18d8cbdadcf5a3de4ecbd30d5`, 与改前 (`$R/md5_pre_fix.txt`) 相同;
   - t2s / fp_expected / keep 不变.
   - writeback `ASSERT: OK` (78/78); direct_hit GREEN; s0 NEW [] / BAD [].
   - `t3_attempt1-3` 已放回. ack 重生成 md5 仍为 `aafe246b…`.
   - `git status --short knowledge_base` 为空; `HEAD:knowledge_base` = `63f857774a42cfaa71798705ad40ab51bc5e378a`.
