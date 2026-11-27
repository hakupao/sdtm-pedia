# T4 解冻轮 W3 (规格 §3: 台账回写 + 重算) — writer checkpoint
<!-- chain: E (plans) -->
> 状态: **未通过, 已停下等主控决定** (2026-11-27, writer oh-my-claudecode:executor, attempt 1). 本文不给自己判 PASS.
> - U-2 和 U-8 已经落到输入里, 整套重跑后结果稳定, writeback 的 ASSERT 为 OK.
> - 但新 KB 上有两个现有断言失败: `s0_classify` 报 NEW 27 条; `t3_direct_hit` 为 RED, 有 2 条 unexplained.
> - 另有 16 个原子的 stock 标签已经失效, 现有规则改不到它们 (§3).
> - 要消掉这些失败, 必须选一种打标机制. 按规格这属于改判定规则, 交主控决定; 本轮未自行改规则.
> 规格 / 依据: `subagent_prompts/t4/t4_thaw_spec_v1.0.md` §3; `t4_user_decisions.md` §000 (U-1=B, U-2=A, U-8=A×4); `t4_thaw_review.md` 问题 #4.
> 写入范围: `scripts/t3/t3_errata_build.py`、`t3_reverse_trace.py`; `scripts/t4/t4_coverage_decomp.py`、`t4_ack_lists.py`、`t4_heading_diff.py`; `work/t3_k3b_out_of_scope_keep.json`; 重跑产物 (`work/` ledger / errata / rules / decisions / section_coverage / audit_sets / t4 census + 日志); `evidence/checkpoints/t4_ack_lists.md`.
> 未动: `knowledge_base/` (真 KB 内容 md5 `b71a466d6e618f995c493a82de3e3eb7`, 两个变异脚本跑前跑后一致; 索引 md5 `29eaa90f…` = HEAD). 未 commit / stash / checkout. 没跑 t4_render / t4_sample.
> scratch: `work/scratch/t4/W3_writer/` (`run_chain.sh`、run1/run2/run3 日志、`ldiff.py`、`attr.py`、`rows23.py`、`census_diff.py`、`kb_head/` = HEAD KB 副本).

## 0. 命令 (仓库根目录)
```bash
T=.work/10_tier_b_repair; S=$T/work/scratch/t4/W3_writer
bash $S/run_chain.sh $S/run1     # §A4.5 整套 (先隐藏 t3_attempt1-3, trap 放回), 新 KB + 旧输入 → ledger 50bdd08b…
#   (之后改 U-2 / U-8 输入, 见 §1)
bash $S/run_chain.sh $S/run2; bash $S/run_chain.sh $S/run3   # 新 KB + 新输入, 跑两遍; diff run2/md5.txt run3/md5.txt 为空
python3 $S/ldiff.py HEAD:$T/work/coverage_ledger.wc.jsonl $T/work/coverage_ledger.wc.jsonl   # 逐原子 diff
python3 -I $T/scripts/t4/t4_coverage_decomp.py [$S/head_ledger.jsonl]; python3 -I $T/scripts/t4/t4_ack_lists.py
python3 -I $T/scripts/fp_match.py --scope all --sections $T/work/section_coverage.wc.baseline.jsonl --ledger $T/work/coverage_ledger.wc.pre_t3.jsonl --kb-root $S/kb_head/knowledge_base --out $S/fp_all_kbhead.jsonl
python3 -I $T/scripts/fp_match.py --scope all --sections $T/work/section_coverage.wc.baseline.jsonl --ledger $T/work/coverage_ledger.wc.pre_t3.jsonl --out $S/fp_all_now.jsonl --baseline $S/fp_all_kbhead.jsonl --regress-out $S/regress_thaw.jsonl   # 解冻本身的回归 = 32
python3 -I $T/scripts/t3/t3_reverse_trace.py --out $S/reverse_trace_head.json; python3 -I $T/scripts/t3/t3_reverse_trace.py --rev WORKTREE --out $S/reverse_trace_thaw.json
python3 -I $T/scripts/table_census.py --manifest $T/work/census_full_manifest.json --out $T/work/t4/census_full_thaw.json; python3 $S/census_diff.py
bash $T/scripts/t3/t3_mutation.sh > $T/work/t4/t4_mutation_thaw.log 2>&1; bash $T/scripts/t0_mutation.sh > $T/work/t4/t0_mutation_thaw.log 2>&1
bash $S/t0_mutation_on_kbhead.sh > $S/t0_mutation_kbhead.log 2>&1   # 同一脚本只把 KB 源换成 HEAD 副本, 用来对照
python3 -I $T/scripts/t4/t4_heading_diff.py kb-2026.11.25 WORKTREE > $T/work/t4/kb_heading_diff_kb-2026.11.25_WORKTREE.txt
python3 -I $T/scripts/t4/t4_heading_diff.py 00a2e93 WORKTREE > $T/work/t4/kb_heading_diff_00a2e93_WORKTREE.txt
python3 tools/check_links.py 2>&1 | grep "live docs"
```
- `--ts 2026-11-26T12:00:00Z` 固定不变, 所以未改判的行与 HEAD **逐字节相同**.
- 行 diff 就等于改判集合: HEAD 与终态 12492 行中 12459 行相同, 不同的 33 行全部列在 §2.

## 1. U-2 / U-8 改在输入里 (未手改 ledger)
| 项 | 改动 | 跑出的结果 |
|---|---|---|
| U-2 | `t3_errata_build.py` 新增第 (4) 段: `put("ig34_p0056_a006", "R1", …, source "T4 U-2 (t4_user_decisions.md §000)")`. 写法与该脚本已有的逐原子特例相同; 不改 `t1_errata.json` (按约定只读). K4 段会复核原子 ∉ PDF 窗, 已通过. 同时改 pending_user 结论文字, 避免出现 "T2 改判" | `PARTIAL → ATOM_ERR (S1-R1)`. 残留 1 → **0** |
| U-8 | `work/t3_k3b_out_of_scope_keep.json`: 3 条 `t4_only → keep_k3b`, 加 `t4_decision` 字段; 新增 `ig34_p0026_a037` (keep_k3b, pdf `ig34_p0026:55` "vistnum", kb `ch04:200` "visitnum, mktestcd"); 同步改 `_note`. 现在 keep_k3b 25 条, t4_only 0 条 | ① `p0026_a037` PARTIAL → PDF_TYPO; ② `p0082_a025` EXACT → PDF_TYPO; ③④ `p0342_a006/a007` EQUIVALENT → PDF_TYPO. 规则都是 K3b-registry. keep 清单复核 25/25 成立. 范围外清单 `t3_t4_k3b_out_of_scope.txt` 由 4 行变为 **0** 行 |

新旧 `t3_errata.json` 逐键比较: 只有 `atom_err` 和 `pending_user` 下的 `ig34_p0056_a006` 两处不同.

稳定性: run2 与 run3 的 md5 完全一致.
- ledger `da4eb10064387c046e8760bd1139773e`, t3_errata `84dc1ba9a2f5a7edf558bf40e93bcb7e`, t3_rules `8945d2886796abf140acd3d23e8ffa87`, decisions `d1dfe7a25f8d3b5140da0884d43cca9b`, keep `9053d98642b9b4aad2b1c8b3c336268a`.
- t2s_atoms `33ef2fe0…` 和 fp_expected `78b22b1c…` 与 T3 相同.
- fp 输出在两次运行之间只有 `verdict` 回显字段不同: 第一次 fp_match 读的是当时的 ledger, 命中结果相同.

## 2. 逐原子标签变化 (HEAD → 终态, 共 33 行; 先单独跑 run1, 才能把变化拆到各归因)
| # | 原子 | HEAD → 终态 (规则) | 归因 |
|--:|---|---|---|
| 1 | ig34_p0056_a006 | PARTIAL → ATOM_ERR (S1-R1) | **U-2** |
| 2-5 | ig34_p0026_a037 / p0082_a025 / p0342_a006 / p0342_a007 | PARTIAL / EXACT / EQUIV / EQUIV → PDF_TYPO (K3b) | **U-8** ①②③④ |
| 6 | ig34_p0016_a019 | EXACT → PDF_TYPO (writer-Tn-registry, B-ch02 T-1) | **U-7 A2-11** ("Trials Sets" → "Trial Sets") |
| 7 | ig34_p0041_a038 | EQUIV → PDF_TYPO (K3b, B-ch04 N-1) | **U-7 A3-34** (foreword → forward) |
| 8 | ig34_p0085_a010 | EXACT → PDF_TYPO (K3b, B-SM O32) | **U-7 A2-8** (SMDY → SMSTDY) |
| 9 | ig34_p0190_a017 | EQUIV → PDF_TYPO (K3b, B-EG T-3) | **U-7 A3-5** (investigation → investigator) |
| 10 | ig34_p0363_a009 | EXACT → PDF_TYPO (K3b, B-FA T-6) | **U-7 A3-8** (may provided → provide) |
| 11 | ig34_p0419_a017 | EXACT → PDF_TYPO (K3b, B-TS T-4) | **U-7 A2-6** (OUTMSPR → OUTMSPRI) |
| 12 | sv20_p0064_a020 | IE → EXACT (live-hit(was-IE-ack), model/06:40) | **A5-7**: APID Notes 补上 PDF 句后, 原子在 §6.1 内逐字命中. HEAD 时只在 §6.2 有命中, 被节锚拒掉 |
| 13-26 | ig34_p0153_a0006/7/8/9/11/12/13/16/18/19/22/23/24/25 (14 条) | EQUIV 不变; 规则 T1-two-agent → T1-two-agent+T2-rework | **CRF** (U-9a, CE p153 `[ ]`→□). T1 判定时的 kb_loc 行 (CE:81 等) 文本已变, 现在要靠 B-CE fix row 的同块规则才成立. 规则名里的 "T2-rework" 其实是 T4 CRF 改动, 标签不受影响. 后果见 §5 M3 |
| 27 | ig34_p0362_a010 | ATOM_ERR 不变; 新增 hit_file FA/assumptions.md | **U-7 A3-7**. 依据已失效, 见 §3 末行 |
| 28-33 | ig34_p0366_a014, sv20_p0061_a006, p0062_a002, p0068_a012/a019/a020 | 只有 hit_lines 变了 | 指针变化: A5-11 (FA 标题加 1 行)、A5-1 / A5-5 (model/05、06 标题和行号变化) |

- 无法归因的: **0** 条.
- A5-n 和 A6 没有引起标签变化. A6 的 en dash 经 norm 后看不出差别; A5 只引起上表 #12 和指针变化.
- 风险清单 `t3_t4_risk_anchorless.txt` 仍为 508 条, 只有 FA 的 8 个行号 +1 (A5-11).
- ack 清单: ATOM_ERR 198 / PDF_TYPO 132 / FIG 11. U-5 裁定时是 197 / 122 / 11, 多出的 11 条 = #1-#11.
- 状态行已按要求改写, 并注明这 11 条不在 U-5 裁定范围内. md5 `37e568d0…`.

## 3. 断言失败与失效标签 (阻塞项, 等主控决定)
### 3.1 fp 回归 (s0_classify `NEW` 27, exit 1) 和 解冻本身的回归 (以 HEAD KB 为基线, scope=all: 丢命中 32 条)
in-scope 回归 72 → 99, scope=all 82 → 109, 两处都多出这 27 条. `s0_classify` 断言要求 NEW 为空, 现在不满足.
| 组 | 原子 | 原因 | 现标签 |
|---|---|---|---|
| A5-10 (19) | ig34_p0275_a019, p0277_a020/a023/a024, p0278_a002/a033-a041/a054, p0281_a034/a049, p0282_a035, p0283_a012 | PP/examples "RELREC Method Quick Reference" 整节换成一行交叉引用. 这些原子的靶文件 PP/examples 不再含原文, 但原文仍在 PC/examples.md (`hit_any` = PC) | 不变 (stock EQUIV 15 / live-hit EXACT 4, 后者命中 PC). 标签成立, 只是 fp 期望清单里没有这些条目 |
| U-7 (8) | p0085_a010 (A2-8)、p0190_a017 (A3-5)、p0298_a001 (A3-15)、p0372_a013 (A3-9)、p0419_a006 / a011 / a013 (A2-5)、p0419_a017 (A2-6) | KB 已改成正确值, 原子 = PDF 原错 | 3 条已转 PDF_TYPO (#8 #9 #11), **5 条仍是旧标签** (见 3.2) |
| (另 5 条) | p0016_a019、p0041_a038、p0160_a0026、p0165_a0007、p0425_a024 | 同为 U-7, 只在 HEAD 基线的 scope=all 回归里出现 | 前 2 条已转 PDF_TYPO; 后 3 条见 3.2 |
`ig34_p0278_a051` "不再回归" 是 T3 以前就有的情况: 该条目注明 "baseline 即未命中", 与本轮无关.

### 3.2 失效的 stock 标签 (16 条; 其中 13 条在 §5.0 范围内): KB 已不含原子原文, 标签仍是 EXACT/EQUIVALENT
| 原子 | 标签 | §5.0 | 对应 U-7 行 | 现有规则没改到它的原因 |
|---|---|---|---|---|
| ig34_p0419_a011 / a013 | **EXACT** | 在 | A2-5 B-TS T-3 (DOSFREQ → DOSFRQ) | registry pdf_value 写成 "DOSFREQ vs Ex4 DOSFRQ", reg_diff 把差异当成边缘操作丢掉 → 不可用. 这是 **direct_hit unexplained 2** 的来源 |
| ig34_p0160_a0026 | **EXACT** | 外 | A3-2 B-DS U-4 (删 in) | 差异 token < 3 字符 → 不可用 |
| ig34_p0165_a0007 | **EXACT** | 外 | A1-9 B-DS U-1 (SCREEN → SCRN) | span 与原子对不齐: pd 算出 'etcd', 原子不含该 token |
| ig34_p0419_a006 | EQUIV | 在 | A2-5 (+A2-4, 'Dose' 的大小写差异经 norm 后看不出) | 同 A2-5 |
| ig34_p0425_a024 | EQUIV | 在 | A2-7 B-TS T-6 (MAXAGE → AGEMAX) | registry 不可用 |
| ig34_p0372_a013 | EQUIV | 在 | A3-9 B-FA T-8 (populated → populate) | 规则 (a) 要求 PDF 侧 token 从整个文件消失, 但 'populated' 在该文件里还出现 3 次 |
| ig34_p0298_a001 | EQUIV | 在 | A3-15 B-NV N-2 (删 the) | ① 差异 token 'the' 属停用词 → 不可用; ② registry 页号 297, 原子在 p298. K3b 只扫 registry 页及前一页, 扫不到 p298 |
| ig34_p0285_a015 | EQUIV | 外 | A3-14 B-NV N-1 (may included → include) | registry 页号 294 (W1 已注明实为 p285). K3b 只扫 p293-294, 扫不到 p285 |
| ig34_p0280_a036 | EQUIV | 在 | A2-3 B-PCPP T-8b | registry kb_file (PC/examples) 不在原子靶内 (原子靶 = PP 侧) |
| ig34_p0280_a039 / a040 | EQUIV | 在 | A2-2 B-PCPP T-8 | 同上 |
| ig34_p0281_a002 / a003 | EQUIV | 在 | A2-15 S-SPC2 N-1 | 同上 |
| ig34_p0281_a031 / a032 | EQUIV | 在 | A2-16 S-SPC2 N-2 | 同上 |
| ig34_p0362_a010 (反向) | ATOM_ERR | 在 | A3-7 B-FA T-4 (补 to) | 原来的依据是 "KB = PDF, 原子抽错". 现在 KB = 原子 ≠ PDF, 依据不再成立; 按 K3b (b) 的定义应为 PDF_TYPO. 因 errata 规则优先, 标签停在 ATOM_ERR |
- W1 预报的 `reg_diff` 丢 < 3 字符差异, 实际只是上表原因之一.
- 另外三类原因: pdf_value 写成描述句; 规则 (a) 要求 token 从整个文件消失、靶文件不含 registry 文件; registry 页号错 (B-NV N-1 / N-2).
- 页号核对: 17 条逐条比较了 原子页 与 registry 页. 只有 B-NV 两条不在 K3b 扫描窗内, 其余 15 条都在.
- 单靠调阈值, 两个红灯一个也消不掉, 而且会波及全部 KB-写正确值 行, 所以**没有改脚本**.
- 另外 3 行 registry 本身不可用 (B-PCPP T-7 PPSTRESU h、B-IS T-6、B-TA T-4). 它们没有原子受影响: norm 后看不出差别, 或原子本来就不命中.

**需要主控选一种**:
- (i) **推荐**, 但有附加要求. 沿用现有的逐原子数据机制: 在 `s0_classify.py` 里加 "T4 解冻" 条目, 每条带 registry id 和 KB/PDF token 断言. 本轮未试跑.
  - U-7 的 16 条记为 R2 → PDF_TYPO.
  - 其中 8 条的 registry id 不是 `T-n` 形式 (B-DS U-1/U-4、B-NV N-1/N-2、S-SPC2 N-1/N-2). `t3_errata_build.classify()` 只认 `T-(\d+)`, 遇到这 8 条会报 "R2 without registry id", exit 1. 因此还要照现有 `p0240_a004` 的做法, 在 errata_build 里给这 8 条逐个指定 registry.
  - **`p0362_a010` 不能走 S0**. 它现在命中 FA/assumptions:39, 不是回归; S0 对非 R3 条目命中靶文件会报 `unexpected-hit`. 它已是 errata R1, 需要单独决定: 改 R2 → PDF_TYPO, 或维持 ATOM_ERR 并更新依据.
  - A5-10 的 19 条记为 R3, 新靶 PC/examples.md, 断言原文在新靶中. 这样它们会进入允许集. 预计其中 15 条 stock EQUIV 会变成 live-hit EXACT, **但这只是推测, 未验证**: 过不了节锚或 K11 计数的会落到 `residual-no-evidence`, G-TB1 残留会上升.
  - 条目数定值 `== 83` 也要改成新值.
  - 做完以上几项, 预计两个红灯都能消掉, 不改任何判定规则.
- (ii) 改 K3b 规则: reg_diff 阈值 / 描述型 pdf_value / 规则 (a) 的整文件条件 / 靶判断. 属于规则改动, 会影响全部 registry 行.
- (iii) 修正 registry 本身: 描述型 pdf_value (B-TS T-3 等)、页号 (B-NV N-1 → p285, N-2 → p298). 只能救一部分, 救不了 PC 靶外、停用词和规则 (a) 这几类.

方案 (i) 的影响 (改判 16 条, 加上 p0362_a010 若改 PDF_TYPO; 不含 A5-10 的 R3):
| 口径 | 现在 | 实施后 |
|---|---|---|
| strict | 95.9644% | 95.8041% (9567/9986) |
| mapped | 99.3572% | 99.3561% |
| U-1 B | 99.2690% | 不变 |
| 内容指标 | 90.7102% | 90.6948% |

## 4. 各闸数值 (终态; 带 † 的会随 §3 的决定变化)
| 闸 | T3 / HEAD | 终态 |
|---|---|---|
| G-TB1 残留 | 1 (`p0056_a006`) | **0**. 174/174 节通过† (有 13 条范围内失效标签, 因为算作通过而未计入) |
| G-TB2 [闸, 范围内] / [参考列, 严格] | 170/174 / 155/174 | **174/174** / 157/174 (只因范围外子节不过的结构父节 17 个) |
| G-TB3 strict | 96.0741% (9593/9985) | **95.9644%** (9583/9986)† |
| G-TB3 mapped | 99.3578% (9593/9655) | **99.3572%** (9583/9645)† |
| **U-1 B 口径** (ATOM_ERR+PDF_TYPO 算覆盖, FIG 不算) | 99.2689% (9912/9985) | **99.2690%** (9913/9986). §3 的处理不影响这一项 |
| 内容指标 EXACT+EQUIV / mapped 分母 | 90.6991% (8757/9655) | **90.7102%** (8749/9645)† |
| G-TB6 反向溯源 (base 302ec4c) | 新增 5336 行, 未溯源 0 | 新增 5414 行, **未溯源 5** = review #4 列出的 5 行 `> Note:` (EX:5 / MS:3 / PC:3 / PP:3 / RELREC:5), 原因是失去了 KB_NOTE 豁免. 其余变化逐类见 §6 |
| direct_hit | GREEN | **RED**: unexplained 2 = p0419_a011/a013 (§3.2); tb_exact_miss / anchor_lost / k11 均为 0 |
| G-TB7 live docs | 42 | **42** |

- 覆盖率脚本 `t4_coverage_decomp.py` 新加了 U-1 B 行和内容指标行, 并可用 argv 指定要读的 ledger.
- 用它读 HEAD ledger, 得到 96.0741 / 99.3578 / 99.2689 / 90.6991, 与 T3 / 总闸数值一致.

## 5. 变异测试 (日志在 `work/t4/`)
| 脚本 | 结果 | 说明 |
|---|---|---|
| `t3_mutation.sh` → `t4_mutation_thaw.log` | 真 KB 跑前跑后一致 OK (`b71a466d…`). M1 tb_exact_miss 1、M4 tb_exact_miss 4、M5 anchor_lost 1, 信号都在 | ① 基线本身是 RED (p0419 unexplained 2), 所以 M0/M2/M7 不再是 GREEN, 测试失去区分力 (§3 处理后应能恢复). ② **M3 已失效**: 删除模式 `  \[ \] Surgery` 0 次替换, 因为 CRF 改成了 `□ Surgery`. 我在 scratch 里改用 `□ Surgery` 删掉 1 处, direct_hit 仍不报错: CE 这 14 条已不是 T1-two-agent 规则, direct_hit 不再按 kb_loc 行核它们. 所以只改模式恢复不了 M3, 需要主控决定 (换靶或补核) |
| `t0_mutation.sh` → `t0_mutation_thaw.log` | MISMATCH (exit 1): M0-M3 / RESTORE 全为 [1 1 1]; M4a/M4d 的 assert 失配; M4b/M4c OK. 真 KB 前后一致 (`e2d862e2…`, 该脚本按文件逐个算 md5) | **T3 以前就有**: 我用同一脚本跑 HEAD 副本 (`t0_mutation_kbhead.log`), 失配格局完全相同. 原因是 baseline (fp_baseline / census_BPCPP.v2 / section_coverage baseline) 生成于 T0 KB. 解冻带来的只是数量变化: M0 的 fp 回归 55 → 82 (+27, 即 §3.1), PC/PP census 表 24 → 22 (A5-10) |

## 6. census 逐表 (`census_full_thaw.json` vs `census_full_head.json`; 按 文件 + 最近标题 + 标题下序号 配对, 不按行号)
- 汇总: KB 表 500 → 497; OK 311 → 309; DIFF 37 → 38; UNPARSEABLE 148 → 146; NO_PDF 4; diffs 144 → 148.
- 配对结果: 487 张不变, 5 张有变化, 另有 5 对是同一张表只换了标题, 另 3 张被删除.
| 表 | 变化 | 原因 |
|---|---|---|
| DS/examples.md:292 Ex10 se.xpt | diffs 1 → 3 (+ETCD `SCRN` vs PDF `SCREEN`, 第 1/5 行) | U-7 A1-9 (KB 写正确值, 预期的 DIFF) |
| PP/examples.md:14 Ex1 pp.xpt | OK → DIFF (+PPSTRESU `h` vs PDF `H`, 第 1/4 行) | U-7 A1-21 |
| model/05:99 TT、:119 TP | 表头 Notes → Usage Restrictions | A5-2 |
| model/05:215→217 TS | 表头加第 6 列 Usage Restrictions | A5-3 |
| model/06 6.3-6.7 五张 (行 101/118/136/155/173 → 94/111/129/148/166) | 只换了标题, 其余字段逐字相同 | A5-5 |
| 删除: PP:120 Method label mapping (UNPARSEABLE)、PP:152 Method C relrec (OK) | — | A5-10 |
| 删除: model/06:50 RELTYPE Combinations (UNPARSEABLE) | — | A5-8 |
- CRF (CE / ch04) 的表在 census 中没有变化, 都是 UNPARSEABLE 或单元格比较结果不变.

## 7. G-TB6 逐类变化 (以 HEAD 为基线 → 工作树; 两次都用当前 registry)
| 类 | HEAD → 终态 | 原因 |
|---|---|---|
| PDF_TYPO | +29 | 都是 U-7 / A6 改动行 (W1 改了 15 个文件, 涉及 29 行): PC 7、TS 5、DS 3、IS 3、FA 3 等 |
| TABLE_TOKENS | +36 −8 | CRF 行 (ch04 +19, CE ±4); A5-2 / A5-3 (model/05 +11 −3); A5-4 / A5-7 (model/06 +2 −1) |
| HEADING_PDF | 216 → 224 | A5-9 / A5-11 等标题改成 PDF 原题 |
| HEADING_NOT_IN_PDF | +12 −7 | model/05 五个 `###` → `####`, 文字照旧带 "(XX)" (U-10①); model/06 6.1-6.7 新标题带 "(XX)" 检索后缀; PP 两个 KB 标题随 A5-10 删除 |
| KB_NOTE / KB_NOTE_SCOPE | −5 / −1 | 5 行前缀改成 `> Note:` (A5-14); A5-8 / A5-10 删掉 D6; A5-2 / A5-3 / A5-6 改写或新增 D6 |
| XREF_D2 | +2 | A5-8 / A5-10 新增的交叉引用行 |
| UNEXPLAINED | +5 | review #4 列出的 5 行 `> Note:` (属预期, 不算回归; 是否给 `> Note:` 加豁免由主控定) |
- 脚本改动: `t3_reverse_trace.py` 新增 `--rev WORKTREE`. 默认 HEAD 模式输出仍为 5336 行、未溯源 0.

## 8. 标题 diff (`t4_heading_diff.py` 新增 NEW=WORKTREE, 因为本轮改动未提交; HEAD 模式的输出与已存文件逐字相同)
| 对比 | 改了标题的文件 | 删 | 增 |
|---|--:|--:|--:|
| kb-2026.11.25 → HEAD | 77 | 85 | 226 |
| kb-2026.11.25 → WORKTREE | 79 | 104 | 239 |
| 00a2e93 → WORKTREE (= HEAD → WORKTREE) | 8 | 28 | 22 |
- 输出文件: `work/t4/kb_heading_diff_kb-2026.11.25_WORKTREE.txt`、`work/t4/kb_heading_diff_00a2e93_WORKTREE.txt`.
- 00a2e93 → WORKTREE 的 8 个文件全是 W2 的改动: FA / MB / PP / SS / TA / TI / model05 / model06, 对应 A5-1 / 5 / 8 / 9 / 10 / 11.

## 9. md5 (终态)
- ledger: `da4eb10064387c046e8760bd1139773e`; run1 (只换新 KB、未改输入) 为 `50bdd08b25469e929a0e1788ccf74e5f`, HEAD 为 `a8011432…`.
- t3_errata `84dc1ba9…`; t3_rules `8945d288…`; decisions `d1dfe7a2…`; keep `9053d986…`; section_coverage `fdb85821…` (含 ts).
- census_full_thaw `dc1c846c…`; registry `46fad482…` (本轮未改).
- 真 KB 内容 `b71a466d…`, 索引 `29eaa90f…`.

## attempt 1 续 (主控决定后)
> 2026-11-27. 依据: 主控对上文 §3 五项的决定: (i)+(iii), 否决 (ii); p0362_a010 → PDF_TYPO; M3 换靶; `> Note:` 显式豁免; ack 标注来源.
> 结果: s0_classify NEW **0**; direct_hit **GREEN**; t3_mutation 基线 GREEN, M1/M3-M6 RED, M0/M2/M7 GREEN; ledger 跑两遍 md5 一致; G-TB1 残留 **0**; live docs 42. 真 KB 未动 (`b71a466d…`).
> 未改 K3b 判定规则. 没有无法归因的变化.

### C1. (iii) registry 事实修正 (`work/t2_pdf_typo_registry.jsonl`, 6 行; 每行加字段 `t4_w3_fix` 记 before→after 和依据, 原描述型 pdf_value 也写在该字段里)
| 登记 | before → after | 依据 |
|---|---|---|
| B-NV N-1 | pdf_page 294 → **285** | `pdf_pages/ig34_p0285.txt:32` "may included" |
| B-NV N-2 | pdf_page 297 → **298** | `ig34_p0298.txt:1` "links the" (下一行接 each) |
| B-TS T-2 | pdf_value `正文 "Dose" vs 表 DOSE` → `TSPARMCD = "Dose"` | `ig34_p0419.txt:17` |
| B-TS T-3 | `DOSFREQ vs Ex4 DOSFRQ` → `DOSFREQ` | `ig34_p0419.txt:17,22,24` |
| B-TS T-4 | `OUTMSPR vs Ex1 OUTMSPRI` → `TSPARM = "OUTMSPR"` | `ig34_p0419.txt:38` |
| B-TS T-6 | `MAXAGE vs 参数 AGEMAX` → `MAXAGE case` | `ig34_p0425.txt:30` |
- 修正范围: 只改了 "KB 写正确值" 行里写成 "X vs Y" 的 4 行. 照录行里的 "vs" 描述不参与 K3b 判定, 没有改.
- 单独跑一遍 (run4; 与 run2 相比只差 registry): K3b 新触及 4 条 → PDF_TYPO: p0419_a006 / a011 / a013 (B-TS T-3)、p0425_a024 (B-TS T-6). 其余行逐字节不变. 这一步之后 direct_hit 已转 GREEN.
- 两条 NV 的页号改对后, K3b 仍然没有触及: N-2 的差异词 'the' 是停用词; N-1 的原子不满足规则 (a). 这两条改由 (i) 处理.

### C2. (i) s0 逐原子条目 + errata 指定 registry
- `scripts/t3/s0_classify.py` 新增 "T4 解冻" 段:
  - R2 共 19 条. 主控定的 16 条之外, 加了 p0085_a010 / p0190_a017 / p0419_a017 三条. 它们是 U-7 原子, 已由 K3b 转为 PDF_TYPO, 但也在 fp 回归里, 不登记就做不到 NEW = 0. 登记后终态仍是 PDF_TYPO, 只是规则名从 K3b-registry 变为 S1-R2.
  - R3 共 19 条 (A5-10), 新靶 PC/examples.md, 断言原文在新靶中.
  - 每条 R2 都带 KB token 和 PDF token 断言, 结果 BAD = [].
  - 条目数定值 `== 83` 改为 **121** (= 83 + 19 + 19), 注释写明来源.
- `scripts/t3/t3_errata_build.py`:
  - 新增 `T4_U7_REG` 表, 给 19 条逐个指定 registry, 做法同 p0240_a004. 覆盖 8 条非 T-n 的 id; B-PCPP T-8 与 T-8b 分开. 运行时断言 registry id 存在.
  - p0362_a010 改为 R2 / PDF_TYPO / registry B-FA T-4, basis 以 "T4 U-7 后依据变更" 开头, 后接原 basis.
  - errata 构建结果: "R2 without registry id" 为 []; 指针缺失 0.

### C3. 标签变化 (run4 → 终态; 也就是 attempt 1 末尾的 33 行之后, 又多出的变化)
| 类 | 原子 | 变化 | 归因 |
|---|---|---|---|
| R2 新转 PDF_TYPO (12) | p0160_a0026, p0165_a0007, p0280_a036/a039/a040, p0281_a002/a003/a031/a032, p0285_a015, p0298_a001, p0372_a013 | EXACT 2 / EQUIV 10 → PDF_TYPO (S1-R2) | 对应的 U-7 行 (§3.2 表) |
| p0362_a010 | — | ATOM_ERR (S1-R1) → PDF_TYPO (S1-R2, B-FA T-4) | 主控决定 2 / U-7 A3-7 |
| (iii) K3b 触及 (4) | p0419_a006/a011/a013, p0425_a024 | EQUIV / EXACT / EXACT / EQUIV → PDF_TYPO (先 K3b, 终态规则 S1-R2) | (iii) + U-7 A2-5 / A2-7 |
| 只改规则名 (3) | p0085_a010, p0190_a017, p0419_a017 | PDF_TYPO 不变, 规则 K3b → S1-R2 | (i) 的另 3 条 |
| R3 → live-hit (15) | p0275_a019, p0277_a020/a023/a024, p0278_a002/a033-a041/a054 | EQUIV → EXACT (命中 PC/examples.md) | A5-10. **15/15 都在 PC 节锚内命中, K11 计数也够, 没有一条落到残留** |
| R3 本已 EXACT (4) | p0281_a034/a049, p0282_a035, p0283_a012 | 不变 | A5-10 |
| 只有 checkpoint 指针变 (14) | p0160_a0028、p0199_a020 等 | `t3_fp_expected_regressions.jsonl` 新增 38 条后行号后移 | 指针 |
- HEAD → 终态合计: 58 行改了标签或规则, 20 行只改指针; 12492 行中 12414 行逐字节相同. 逐行清单: `work/scratch/t4/W3_writer/ldiff_head_final.txt`.
- 终态计数: ATOM_ERR 197 / PDF_TYPO 149 / FIG 11.

### C4. M3 换靶 + CE p153 核查
- **M3 新靶**: `DM/spec.md:219` ARMCD 的 CDISC Notes 行, 即 `ig34_p0064_a001` 的 T1 kb_loc 行.
  - 理由: 该原子是 PRESENT, 规则 T1-two-agent, kb_loc 行在文件中唯一, direct_hit 仍逐行核它.
  - 变异做法: 删掉句子 "It is not subject to the character restrictions that apply to TESTCD.". 该句在 DM/spec 出现 2 次, 两处都删 (另一处是 ACTARMCD 的同一句).
  - 结果: anchor_lost `ig34_p0064_a001` → **RED**.
  - 原 CE 模式保留在脚本中并注明已停用; 脚本头部写明换靶理由.
- **CE p153 的 14 条** (`scripts/t4/t4_ce_p153_check.py`, 输出 `work/t4/t4_ce_p153_check.txt`): **14/14 OK**.
  - 每条原子的全部字母数字 token 都在 B-CE 同块 (CE/examples.md:72-83, fix row B-CE.writer.jsonl:8, review PASS) 中出现.
  - 抽取器把 CRF 选项符号写成独立字母 'o', 这个 token 改为检查 "块内含 ○/□"; 14 条均满足.
  - 局限: 这是块级 token 核查, 不是逐格对位.

### C5. `> Note:` 显式豁免
- 清单 `work/t4_note_exempt.json`: 5 条, 按 "文件 + 整行文本" 锚定, 来源注明 A5-14 (委托代裁 U-11).
- `t3_reverse_trace.py` 读该清单, 命中的行归为新类 NOTE_EXEMPT, 计入 "added buckets". 在 WORKTREE 模式下断言每条恰好命中 1 行.
- 结果: 新增 5414 行, 全部溯源 (100.00%), UNEXPLAINED 0, NOTE_EXEMPT 5. HEAD 模式仍为 5336 行、未溯源 0.

### C6. ack 来源标注
- `t4_ack_lists.py` 新增 "决定来源" 列, 汇总表按来源计数. 状态行写明: U-5 之后进入这三类的原子按来源标注, 不归入 U-5.
- 判定办法: 拿 3a24a1c 的 ledger (U-5 裁定时的状态) 与当前比. 标签相同的记为 U-5; 不同的按以下顺序找来源: errata 的 source 为 T4 U-2 → U-2; keep 清单有 t4_decision → U-8; registry 有 t4_decision → U-7 (写出所在行). 找不到来源就断言失败.
- 结果: U-5 329 / U-2 1 / U-8 4 / U-7 23. 合计 357 = 197 + 149 + 11, 未归因 0.
- 说明: 3a24a1c 时有 330 条, 其中 p0362_a010 改标后归入 U-7, 所以 U-5 剩 329.

### C7. 终值
| 项 | 值 |
|---|---|
| s0_classify | NEW [] / BAD [] / R1 32 · R2 42 · R3 47 / R4 = 0, exit 0 |
| writeback | ASSERT OK; 允许集 1978; extended assertion 0; keep 25/25; 范围外 0 |
| direct_hit | GREEN (TB EXACT 1030, stock 1758; miss / anchor / unexplained 全为 0) |
| ledger md5 (run5 = run6) | `60729f7b64b7c1dfaf2174e394f6dd9c`; errata `f355a637…`, fp_expected `e7df6ce0…`, rules `fff771cf…`, decisions `5fd0a673…`, section_coverage `2b5b70f8…` (含 ts), registry `905f89e9…` |
| G-TB1 | 残留 **0**; 174/174 |
| G-TB2 | 范围内 **174/174**; [严格] 157/174 |
| strict / mapped | **95.8041%** (9567/9986) / **99.3561%** (9567/9629) |
| U-1 B | **99.2690%** (9913/9986) |
| 内容指标 EXACT+EQUIV | **90.6948%** (8733/9629) |
| G-TB6 | 5414 行全部溯源, 未溯源 0 |
| t3_mutation (`work/t4/t4_mutation_thaw2.log`) | M0 绿 / M1 红 / M2 绿 / M3 红 (新靶) / M4 红 / M5 红 / M6 红 / M7 绿; 真 KB 前后一致 |
| t0_mutation | MISMATCH 是既有问题 (HEAD 副本格局相同, 见 §5). 本轮 KB 未变, 未重跑, 也不修 |
| census | KB 未变, 沿用 §6 (`census_full_thaw.json`) |
| ack | ATOM_ERR 197 / PDF_TYPO 149 / FIG 11; 来源 U-5 329 / U-2 1 / U-8 4 / U-7 23. md5 `92cbe845…` |
| live docs | 42 |
