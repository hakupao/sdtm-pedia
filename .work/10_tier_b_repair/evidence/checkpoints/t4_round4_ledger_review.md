# T4 问题 C 改台账 (R4L) — 独立 reviewer (结构审查)

<!-- chain: E (plans) -->
> 状态: **PASS** (HIGH 0 / MEDIUM 1 / LOW 5; 2026-11-27) → 小修后 **delta PASS** (HIGH 0 / MEDIUM 0 / LOW 3; 见文末 "delta 复审"). 审查者 `oh-my-claudecode:code-reviewer` (opus), 对仓库工作树只读, 在隔离副本里复跑; 对象 = 工作树里 writer 改后的台账 (md5 `eef9bb14e5afab7e68a231ddd18cfa1c`). 下面是审查者回复正文, 由脚本 `scripts/t4/t4_extract_reply.py` 从会话记录里原样取出 (主控未改一字; 规则 D). 派发 / 返回时间见 `trace.jsonl` 的 `T4.R4L.REVIEW` 行. MEDIUM / LOW 的处理见文末 "主控的处理" (主控追加, 不属于审查者原文).

---

## R4L 改台账批 独立结构审查 (reviewer: `oh-my-claudecode:code-reviewer`)

### 1. 结论: **PASS**

没有 HIGH。有 1 条 MEDIUM (writer 已自报，不阻塞)，另有 5 条 LOW。

台账逐行变化恰好是规格要求的 1 条改标加 4 条指针。改标由现有 live-hit 规则判出，没有在回写之后覆盖标签。在隔离副本里从改前备份复跑整链三遍，md5 都等于工作树台账。我自己设计的 8 个变异里，7 个按预期拦下；第 8 个用来确认 writer 自报的缺口，结果属实。

### 2. 问题清单

**HIGH**: 无

**MEDIUM**
- **M-1** `.work/10_tier_b_repair/scripts/t3/t3_errata_build.py:242-250`：撤销清单被删空时不报错 (writer checkpoint §6.8 已自报，我已实测确认)。
  - 实测：把 `work/t4_r4l_relabel.json` 的 `relabel` 置空 (变异 R7)，errata rc=0，writeback rc=0，输出 `ASSERT: OK`。`ig34_p0124_a001` 悄悄退回 `ATOM_ERR / S1-R1`，台账 md5 变为 `9fa4c8fa…`。
  - 后果：主人 C1 的决定只靠这一份 JSON 承载。JSON 被误删或回退时，整链仍判通过。R3L 有 keep 清单交叉断言，R4L 没有。
  - 建议修法：在 `t3_errata_build.py` 段 (6) 加一句交叉断言，要求 `set(R4L)` 等于 `work/t4/atomerr/verdicts.json` 中 NOT_HOLD 的集合 (这是第二个数据源)。或者在 writeback 里断言 `r4l_revoked` 非空，且与 verdicts.json 一致。

**LOW**
- **L-1** `scripts/t3/t3_writeback.py:538-539`：指针断言把两件事合成一条，报错文字会误导。
  - 实测：把指针改成裸 id `B-RS T-6` (变异 R2)，正确报错 rc=1，但报错文字是 `'T4 R4L registry_ptr atom not ATOM_ERR via S1-R1', 'ig34_p0339_a001', ('ATOM_ERR', 'S1-R1')`。实际原因是登记 id 不存在，报文却说"不是 S1-R1"。
  - 修法：把 `r in REG_IDS` 拆成一条单独的 assert，带自己的报文。
- **L-2** `scripts/t3/t3_writeback.py` 先写台账后断言 (已有设计，本批沿用)。
  - 实测：变异 R4 断言失败后，副本台账已被改成 `f1e41ed0…`，rc=1。不影响本批，但失败后必须从备份还原 (HANDOFF "坑" 已写)。
- **L-3** `scripts/t3/t3_errata_build.py:242`：撤销放在 pending_user 结论生成之后。
  - 以后清单里若放进一个同时在 `t1_errata.pending_user` 里的原子，它的 pending 结论仍会写"终态 ATOM_ERR (S1 atom_err)"，与撤销矛盾。
  - 本批的 a001 不在 pending_user 里 (实测 False)，所以不触发。建议在段 (6) 的断言里加 `i not in E1["pending_user"]`。
- **L-4** `work/t3_t4_risk_anchorless.txt` 从 511 行变为 512 行，新增的就是 a001。
  - `scripts/t4/t4_sample.py:34` 读取这个文件，`t4_human_header.md:25` 里写着 508 这个层规模。以后若重跑抽样，层规模会变。按要求我没有跑 t4_sample.py，这一条交主控登记即可。
- **L-5** 新行 `matched_by.ts` 是 `2026-11-26T12:00:00Z`，早于主人的决定日 (固定 ts 的沿用做法，writer §6.4 已自报)。决定日期写在 `evidence.t4_r4l.decision` 里，可追溯。

### 3. A-J 逐项

**A. 逐行比较** (实测)
- 我自己写的 python 按位置对齐，逐行断言 `pdf_atom_id` 相同，再展平嵌套字段比较。
- 结果：两份台账都是 12492 行，尾部换行一致。
  - 标签变化恰好 1 行：第 3280 行 `ig34_p0124_a001` ATOM_ERR → EXACT。
  - 另有 4 行变化，且只变了 `matched_by.evidence.registry`，都是 `[]` → `[id]`：
    - 第 4187 行 `ig34_p0161_a0012` → `B-DS T-4`
    - 第 8478 行 `ig34_p0337_a003` → `B-RS T-3`
    - 第 8507 行 `ig34_p0339_a001` → `B-RS T-6 (RS 副本)`
    - 第 9039 行 `ig34_p0361_a016` → `B-FA T-2`
  - 字节级核对：把旧行里的 `"registry": []` 替换成新值后，与新行逐字节相等 (4/4 True)，说明键序和其它字节都没动。其余 12487 行逐字节相同。
  - 这 5 个 id 在台账里各只有 1 行，不涉及重复 id 的多行问题。
- 登记表 `work/t2_pdf_typo_registry.jsonl` 核对：4 个 id 都恰好命中 1 条，handling 都是"KB 写正确值"，KB 文件:行处都含 kb_value，PDF 页文本都含 pdf_value。
  - `B-DS T-4`：p161，`DS/examples.md`
  - `B-RS T-3`：登记页 p336，原子标 p337，相差 1，writer 已说明；`RS/assumptions.md:81`
  - `B-RS T-6 (RS 副本)`：p339，`RS/assumptions.md:128`
  - `B-FA T-2`：p361，`FA/assumptions.md:15`
- 关于 `B-RS T-6`：登记表里**没有**裸 id `B-RS T-6`，只有 `(RS 副本)` p339、`(FT 副本)`、`(QS 副本)` 三条。原子在 p339，审查者核的位置是 `RS/assumptions.md:128`，所以 **writer 用全名 `B-RS T-6 (RS 副本)` 是正确的**。按规格字面写裸 id 会挂到不存在的登记，变异 R2 已证实会被拦下。
- 判定：符合。

**B. `ig34_p0124_a001` 新行** (实测；只看了文本层，**没看渲染页**)
- 新行内容：rule `live-hit`，batch `T4-R4L`，`hit_file` `knowledge_base/domains/ML/examples.md`，`hit_lines` [42]。S1 分支专有的 errata / registry / checkpoint / basis 四个键已去掉，新增 `t4_r4l` 出处。
- 读 `decide()` (`t3_writeback.py:245-291`)：本批没有在 decide 里加任何 R4L 分支。原子从 `atom_err` 撤掉后，自然落到原有的 `if hit: return "EXACT", "live-hit"`。之后只改了 batch 名和 evidence，没改 verdict 和 rule。
- 反证 (变异 R4)：在副本里把 KB 第 42 行末格改成 `17:01`，writeback 报 `ASSERT: FAIL ['T4 R4L atom not live-hit EXACT: ig34_p0124_a001 EXACT residual-no-evidence …']`，rc=1。说明 EXACT 依赖逐字命中，不是硬写的。
- 三方对照：
  - 原子用 `split('|')` 拆格后是 18 格，`ML/examples.md:42` 也是 18 格，逐格相等 (True)。表头第 39 行也是 18 列，格与列逐一对应。
  - PDF 文本层 `work/pdf_pages/ig34_p0124.txt` 按列起点核对：
    - `2015-09-` / `03T08:30` 在第 117 列，即表头 MLSTDTC，所以 MLDTC (第 111 列) 为空。
    - `LAST MEAL PRIOR TO` 在第 163 列，即 RELMIDS。
    - `HYPO2` 在第 173 列，即 MIDS。
    - `2015-09-` / `03T17:00` 在第 179 列，即 MIDSDTC。
  - 原子、PDF、KB 三者一致。MIDSDTC 没有截断，t1 errata 里"MIDSDTC 截断"的说法不成立。
- 判定：符合。

**C. 改法是否从成因下手** (实测：通读 diff 和新文件，并跑了 build)
- errata 侧：撤销做在 `t3_errata_build.py` 段 (6) (errata 源头)，在写 `t3_errata.json` 之前，原条目原样存进 `r4l_revoked`。
  - 实测 `r4l_revoked[a001].entry` 与 HEAD 版本的 `atom_err[a001]` 相等 (True)。
  - writeback 之后没有覆盖标签：R4L 后处理只改 batch 和 evidence。`work/t1_errata.json` 用 `git diff --quiet HEAD` 核过，未改。
- 新断言拦得住吗 (变异见 E)：
  - 清单 id 不在 atom_err：R8 拦下。
  - 撤掉后得不出 EXACT：R4 拦下。
  - 指针挂到非 S1-R1 原子：R3 拦下。
  - D1 防护：把 B-CE 原子放进清单 (R1)，被 `registry` 非空 (`B-CE T-2`) 和 `X.class == R1` 两个条件拦下。
- 对这 5 条之外原子的影响：
  - 新增的改写条件 `or i in R4L` 只对清单内原子生效。
  - registry_ptr 循环只遍历清单。
  - errata 的 pop 只作用于清单。
  - `ev["registry"]` 用 `list(...) + [...]` 新建列表，不会改到 ER 原条目里共享的 list。
  - 实测清单外标签变化为 0。`t3_writeback_decisions.json` 只有这 5 键变化 (见 H)。
  - 以后重跑的隐患见 M-1 和 L-3。
- `scripts/t4/t4_r4l_build.py` 在副本里跑了两遍，输出都是 `c33abbe7893160a020044b0d27d60d51`，与工作树的 JSON 相同，幂等。
- 判定：符合 (隐患见 M-1、L-3)。

**D. 整链复跑** (实测)
- 副本做法：rsync 整个仓库 (去掉 `web/` 和 `work/scratch/`，补拷 `work/scratch/t3`)；48 个 .py/.sh 里写死的仓库路径全部改成指向副本，grep 确认剩余 0 处；整链脚本从 `work/scratch/t4/r3l/run_chain.sh` 复制并把 `cd` 改到副本。
- 每遍之前把副本的 `coverage_ledger.wc.jsonl` 置为 `coverage_ledger.wc.pre_r4l.jsonl` (`43809870…`)，第一遍还先把派生文件 checkout 回 HEAD。
- 结果：run1、run2 和变异还原后的 run3，台账都是 **`eef9bb14e5afab7e68a231ddd18cfa1c`**，等于工作树。run2 与 run3 的 7 个产物 md5 一致，11 个日志逐字一致。
  - 其他产物 md5：errata `76535530…`，decisions `8aa949c1…`，rules `1096bec2…`，t2s / fp_expected / keep 都不变。
  - 副本里的 `t3_errata.json`、`t3_writeback_decisions.json`、`t3_rules.json`、`t3_t4_risk_anchorless.txt`、`t3_t4_k3b_out_of_scope.txt`、`t3_audit_sets/` 全部与工作树逐字节相同。`section_coverage.wc.jsonl` 去掉 ts 后 399 行全同。
- 说明：
  - writeback 永远以 `coverage_ledger.wc.pre_t3.jsonl` 为输入，所以起始台账只影响 `01_fp_head` 日志里一行命中统计和 writeback 日志首行的 "ledger before"。我的 run2 与 writer 的 runD 日志在路径归一后，只差这两处。
  - `fp_head` / `fp_all` rc=1 (RESULT: RED) 是已有状态，R3L runD 也一样，与本批无关。
- 判定：符合。

**E. 变异** (实测，在隔离副本里，全部我自己设计)

| # | 变异 | 结果 |
|---|---|---|
| R1 | relabel 加入 B-CE T-2 原子 `ig34_p0153_a0034` (D1 防护) | errata rc=1，`T4 R4L revoke: not an errata-only ATOM_ERR` (拦下它的是 registry 非空、X.class=R1 两个条件) |
| R2 | 指针改成规格字面的裸 id `B-RS T-6` | writeback rc=1，台账未写 (报文误导，见 L-1) |
| R3 | 指针挂到 C7 规则的 ATOM_ERR 原子 `ig34_p0196_a006` | writeback rc=1，`('ATOM_ERR', 'C7-K4-rereview')`，台账未写 |
| R4 | 副本 KB `ML/examples.md:42` 末格改为 `17:01` | writeback rc=1，`ASSERT: FAIL … residual-no-evidence` |
| R5 | relabel 的 `to` 改为 EQUIVALENT | errata rc=1 |
| R6 | errata 已撤销 a001，但手工删掉 `r4l_revoked` | writeback rc=1，`T4 R4L list != t3_errata r4l_revoked …` |
| R8 | relabel 加入 R3L 原子 `ig34_p0412_a006` (不在 atom_err) | errata rc=1，`…, None)`，`t3_errata.json` 未写 |
| R7 | relabel 置空 (确认已知缺口) | rc 全 0，`ASSERT: OK`，a001 退回 ATOM_ERR (见 M-1) |

- 还原核对：还原后 relabel `c33abbe7…`、errata `76535530…`，副本 KB 文件 md5 与原仓库相同，副本 `git status knowledge_base` 为空。之后跑 run3，md5 与 run2 一致。
- 判定：符合 (R7 是已知缺口)。

**F. 闸数字** (实测，在副本里跑；副本台账 = `eef9bb14…`)
- `t4_coverage_decomp.py`：
  - strict 9494/9933 = 95.5804%
  - mapped 9494/9556 = 99.3512%
  - U-1 B 9860/9933 = 99.2651%
  - 内容 8660/9556 = 90.6237%
- 终态计数：EXACT 4711 / EQUIVALENT 3949 / IE 2559 / PDF_TYPO 170 / ATOM_ERR 196 / FIG 11 (另有 PARTIAL 637 / MISPLACED 197 / ERROR 62)。
- B-CE 8 条仍是 ATOM_ERR / S1-R1，`ig34_p0293_a038` 仍是 PDF_TYPO。
- `t3_direct_hit.py`：TB(all)=1034 (writer 的 run0 是 1033，加 1 就是这一条)，stock 1748，tb_exact_miss 0，unexplained 0，`RESULT: GREEN`。
- `t3_recompute.py`：`§5.0 scope sections=174 residual_gap=0 G-TB1 pass=174/174 G-TB2 pass=157/174`。
- writeback：`T4 R4L: 1 listed … via live-hit: 1`，`ASSERT: OK`。
- report：flipped 2009 → 2008，S1-R1 ATOM_ERR 157 → 156，与 writer 说法一致。
- 判定：符合。

**G. `t4_ack_lists.md`** (实测)
- 在副本里重生成，与工作树逐字节相同 (`04e72e75…`)。
- 和 HEAD 比较 (行内容多重集，忽略编号) 只有这些变化：
  - 状态行文字
  - 汇总行 197 → 196、S1-R1 157 → 156、U-5 196 → 195
  - 节标题 197 → 196
  - a001 行删除
  - 4 条指针行的依据列末尾加上 `[登记 id]`，决定来源仍是 U-5
- ATOM_ERR 196，"(未归因)" 不出现。
- 判定：符合。

**H. 其它重新生成的文件** (实测)
- `t3_errata.json`：顶层只多了 `r4l_revoked`；`atom_err` 只少了 a001；其余键不变。
- `t3_writeback_decisions.json`：键集合不变，只有这 5 键变化。
  - a001：new / rule / batch / evidence 变化。
  - 4 条指针原子：只有 `evidence.registry` 变化，old / new / rule / batch 不变。
- `t3_audit_sets/S1-R1__ATOM_ERR.txt`：只删了 a001。
- `t3_t4_risk_anchorless.txt`：只加了 a001 (见 L-4)。
- `section_coverage.wc.jsonl`：去掉 ts 后只有 `ig34_§6.1.4` 一节变化 (matched 49 → 50，ATOM_ERR 7 → 6，EXACT 47 → 48，density 0.5269 → 0.5376)。
- `trace.jsonl`：只追加了 3 行 (dispatch / done / 本次 reviewer dispatch)。
- 副本 vs 原仓库的 `git status` 文件清单：除了副本里改过写死路径的脚本，两边完全一致；没有只在一侧变化的文件。
- 判定：所有变化都能由这 5 条解释，没有解释不了的变化。

**I. writer 说法核对** (实测)
- 以下都与我的实测一致：新旧 md5、逐行 diff 汇总、终态计数、四个覆盖率数、direct_hit 1033 → 1034、flip 2009 → 2008、derived 文件变化描述、`B-RS T-6 (RS 副本)` 的理由、§6 已知局限 (包括 §6.8，即 M-1)。
- `work/scratch/t4/r4l/run0/md5.txt` 与 `r3l/runD/md5.txt` 相同 (只读核过)，支持 writer "基线可复现"的说法。
- `t4_mutation_r4l.log` 的 md5 `502f7f5d…` 与 R3L 的 `t4_mutation_r3l.log` 相同，属实。
- 没发现夸大或过期数字。
- 隐私核查：对 checkpoint、`t4_r4l_build.py`、`t4_r4l_relabel.json`、`r4l_ledger_diff.txt`、`t4_mutation_r4l.log`、`t4_ack_lists.md`，以及 scripts / trace 的新增行，grep 本机用户目录、用户名、邮箱、`/Volumes/`、`/private/`、`/tmp/`，命中 0。
- 这些新文件都没有被 gitignore，会入库。`t4_r4l_build.py` 的路径按 `__file__` 推算，没有写死。
- 判定：符合。

**J. KB 冻结** (实测；最后在原仓库上又核了一遍)
- `git status --short knowledge_base archive releases web` 为空。
- `git rev-parse HEAD:knowledge_base` = `63f857774a42cfaa71798705ad40ab51bc5e378a`。
- 原仓库 `git status --short` 仍是开始时那 17 项，台账 md5 仍是 `eef9bb14…`。我没有写原仓库。
- 判定：符合。

### 4. 没能核的东西
- 渲染页 p124 没看，只核了文本层的列位置。
- `tools/check_links.py` 的 live docs = 42：副本里没有 `web/`，结果会不同，所以没跑，采信 writer。
- `scripts/t3/t3_mutation.sh` 的 M0-M7：没跑，采信 writer 日志，其 md5 与 R3L 那份相同。
- writer 的 run0 基线：没在改动前状态下独立重跑，只读核了 run0 的 md5 与 R3L runD 相同。
- 按要求没跑以下脚本，所以对它们的影响只做了 grep 级判断：`t0_mutation_head.sh`、`t4_gate_prerun.sh`、`t4_supp_report.py`、`t4_sample.py`、`t4_render.py`、`t4_atomerr_sample.py`。
  - `t4_sample.py` 读取 `t3_t4_risk_anchorless.txt`，以及行级和 errata 的 registry (见 L-4)。
  - `t4_atomerr_coverage.py` 改台账后按设计会断言失败 (writer §6.5 已报)。
  - `t4_gate_prerun.sh` 的 md5 清单还没纳入本批的 `coverage_ledger.wc.pre_r4l.jsonl` 和 `t4_r4l_relabel.json` (writer §6.6 已报)。
  - 这三项交主控处理。
- a001 在 t1 登记时是否看的是重抽前的原子 (`OptionE_p124_rerun`)：没去核旧版原子。

---

# delta 复审 (writer 按 M-1 / L-1 / L-3 小修之后; 同一 reviewer 实例; 原文, 同样由脚本原样取出)

## R4L delta 复审 (M-1 / L-1 / L-3 小修; reviewer `oh-my-claudecode:code-reviewer`, 同一实例)

### 结论: **PASS**

我上次报的 M-1、L-1、L-3 三处都已关闭。小修只改了两份脚本里的断言，没有改任何判定路径。在隔离副本里从改前备份台账重跑整链，台账 md5 仍是 `eef9bb14e5afab7e68a231ddd18cfa1c`，7 个产物 md5 和 11 个日志都与上次逐字相同。我自己设计的 7 个变异全部在写台账之前报错，台账一次都没被改写。这次没有 HIGH 或 MEDIUM 问题。

### 问题清单
- **HIGH**: 无
- **MEDIUM**: 无
- **LOW**
  - **DL-1** `scripts/t3/t3_errata_build.py:245`、`scripts/t3/t3_writeback.py:76`：`work/t4/atomerr/verdicts.json` 现在成了整链的输入，但还没登记为输入。
    - 已实测的行为：
      - 文件不存在：两份脚本都抛 FileNotFoundError，rc=1，不写任何文件，结果偏安全。
      - 文件被 `scripts/t4/t4_atomerr_report.py:40` 重新生成后多出一条 NOT_HOLD：整链报错，必须先更新清单才能跑通 (变异 D4)。这属于"响亮失败"，可以接受。
    - 风险：审查者判出 NOT_HOLD 和主人决定改标是两回事。现在用前者去钉后者，以后若出现主人还没裁决的新 NOT_HOLD，整链会一直红到主人裁决为止。另外 `t4_gate_prerun.sh` 的 md5 清单里还没有这份文件。
    - 建议：把它补进 gate_prerun 的 md5 清单，并在 HANDOFF "坑" 一节写一句：重跑 `t4_atomerr_report.py` 会影响 R4L。
  - **DL-2** `scripts/t3/t3_errata_build.py:245`：报错文字有一处不准，只影响措辞，不影响拦截。
    - 清单和 verdicts.json 的 NOT_HOLD 两边都为空时 (变异 D5)，真正触发的是 `R4L_NH` 非空这个条件，报文却写 `relabel ids != NOT_HOLD ids`，并附 `[] []`。
    - 修法：把非空检查拆成单独一条 assert，或在报文里写明 "or empty"。
  - **DL-3** 工作树里多了一个新的未跟踪文件 `scripts/t4/t4_extract_reply.py`，writer 第 8 节没有列它。
    - 从内容看是主控用来"原样抽取 subagent 回复"的工具，与本批判定链无关，也没有 import 关系。
    - 我 grep 过，里面没有本机用户目录、用户名或 `/Volumes/` 路径。
    - 请主控确认它是主控自己的产物，并在提交说明里写上。

### 1-5 逐项

**1. 变化范围** (实测)
- 做法：以我的隔离副本为基准 (上次审完时的状态)，对比路径归一后的工作树，并核对 md5。
- 结果：
  - 脚本只有 `scripts/t3/t3_errata_build.py` 和 `scripts/t3/t3_writeback.py` 两份有变化，新 md5 分别是 `acc7e86f…` / `89005590…`，与 writer 所报一致。
  - `trace.jsonl` 只追加了 3 行。
  - checkpoint 只新增了第 8 节。
  - 新增未跟踪文件 2 个：`evidence/checkpoints/t4_round4_ledger_review.md` (存档的我上次报告) 和 `scripts/t4/t4_extract_reply.py` (见 DL-3)。
- 以下文件与上次逐字节相同：
  - `work/coverage_ledger.wc.jsonl` `eef9bb14…`
  - `work/t3_errata.json` `76535530…`
  - `work/t3_writeback_decisions.json` `8aa949c1…`
  - `work/t3_rules.json` `1096bec2…`
  - `evidence/checkpoints/t4_ack_lists.md` `04e72e75…`
  - `work/t4_r4l_relabel.json` `c33abbe7…`
  - `work/t3_t4_risk_anchorless.txt`、`work/t3_t4_k3b_out_of_scope.txt`、`work/t3_audit_sets/`
  - `work/t4/r4l_ledger_diff.txt`、`work/t4/t4_mutation_r4l.log`、`scripts/t4/t4_r4l_build.py`、`scripts/t4/t4_ack_lists.py`
  - 输入文件 `verdicts.json` `7f1f5e3e…`、`t1_errata.json`、两份备份台账
- 例外：`work/section_coverage.wc.jsonl` 字节有变化。原因是 writer 在工作树里重跑了整链，内嵌的 ts 变成 `2026-11-27T15:17:54Z`。递归去掉 ts 后，399 行与上次全同。
- 判定：符合。只有 section_coverage 的时间戳变了，这在预期之内。

**2. 读两份脚本的 delta** (实测)

`t3_errata_build.py`
- `:243-245`：段 (6) 读入清单后，立刻断言 NOT_HOLD 集合非空，且等于 `set(relabel)`。这一步在撤销循环和 `json.dump` 之前，变异时 errata 文件确实都没被写。
- `:248-249`：撤销循环的第一句断言该原子不在 `E1["pending_user"]` 里。`E1` 就是 `t1_errata.json` (`:21`)。

`t3_writeback.py`
- `:74-77`：模块级断言，要求 `r4l_revoked` 非空，且清单等于 NOT_HOLD 集合。它在 decide 和写台账之前执行。原有的 "清单 = r4l_revoked 键集" 断言保留。
- `:542-546`：指针断言拆成两条。先查登记 id 是否在 `REG_IDS` 里，报文列出不存在的 id；再查是否为 `(ATOM_ERR, S1-R1)`。

总体判断
- 这些都是纯断言，没有改 decide、改写条件或任何数据。条件只收紧、没有放宽，所以不会影响这 5 条之外的原子。实测 7 个产物 md5 不变也印证了这一点。
- 对 `verdicts.json` 的依赖见 DL-1。

判定：符合。

**3. 整链复跑** (实测)
- 做法：先把两份新脚本同步进隔离副本 (路径改指副本，grep 确认剩余 0 处)，并核对副本的输入文件与工作树相同。再把副本台账置为 `coverage_ledger.wc.pre_r4l.jsonl`，跑整链 (run4)。
- 结果：
  - 台账 `eef9bb14e5afab7e68a231ddd18cfa1c`。
  - `md5.txt` 的 7 项与上次 run2 相同，11 个日志逐字节相同：`ASSERT: OK`，direct_hit GREEN，recompute 174 节残留 0。
  - `fp_head` / `fp_all` 仍是 RED，与上次相同，属于已有状态。
- 判定：符合。

**4. 变异** (实测，在副本里；每项都先跑 errata，再跑 writeback，并记录前后 md5)

| # | 变异 | errata 结果 | writeback 结果 | 台账 / errata 是否被写 |
|---|---|---|---|---|
| D1 (上次 R7) | relabel 置空 | rc=1，`relabel ids != NOT_HOLD ids …, [], ['ig34_p0124_a001']` | rc=1，`list != t3_errata r4l_revoked …` | 都未写 |
| D2 (上次 R2) | 指针改成裸 id `B-RS T-6` | rc=0 | rc=1，`registry_ptr: registry id not in t2_pdf_typo_registry.jsonl', 'ig34_p0339_a001', ['B-RS T-6']`，报文现在准确 | 未写 |
| D3 | 把 verdicts.json 移走 | rc=1，FileNotFoundError | rc=1，FileNotFoundError | 都未写 |
| D4 | verdicts.json 里多标一条 NOT_HOLD (`ig34_p0122_a017`) | rc=1 | rc=1，新断言 `r4l_revoked empty or relabel ids != verdicts.json NOT_HOLD` | 都未写 |
| D5 | verdicts 的 NOT_HOLD 和 relabel 同时置空 | rc=1 (报文见 DL-2) | rc=1 | 都未写 |
| D6 | 绕过 errata 侧：用 HEAD 版 `t3_errata.json` (没有 `r4l_revoked`) 加空 relabel，只跑 writeback | 不跑 | rc=1，新断言命中 | 台账未写 |
| D7 (查 L-3) | relabel 和 verdicts 同时加入 pending_user 原子 `ig34_p0056_a006` | rc=1，`revoke: atom is in t1_errata pending_user` | 不跑 | errata 未写 |

- 还原后：relabel `c33abbe7…`，verdicts `7f1f5e3e…`，errata `76535530…`，台账 `eef9bb14…`，副本 `git status knowledge_base` 为空。
- 判定：符合。所有拦截都发生在写文件之前。

**5. KB 冻结** (实测，在原仓库上只读)
- `git status --short knowledge_base archive releases web` 为空。
- `git rev-parse HEAD:knowledge_base` = `63f857774a42cfaa71798705ad40ab51bc5e378a`。
- 工作树台账 md5 `eef9bb14…`。`git status --short` 共 19 项，即上次的 17 项加上 review 存档和 `t4_extract_reply.py`。
- 判定：符合。

### 上次问题的关闭情况
- **M-1 已关**。清单被删空或改动后，现在会在 errata 和 writeback 两侧都报错 (D1、D4、D5、D6)。剩下的前提是 `verdicts.json` 不被同时篡改，这一点见 DL-1。
- **L-1 已关**。裸 id 的报文现在准确说明是登记 id 不存在 (D2)。
- **L-3 已关**。pending_user 原子会被拦下 (D7)。

### 没能核的东西
- 按约定没在副本里重跑 `tools/check_links.py` (live docs = 42) 和 `scripts/t3/t3_mutation.sh`，两项都采信 writer 第 8 节。
- writer 的 runE、runF、runG、runH 和 `mut_fix.sh` 没有逐个复核。我用自己的 run4 和 D1-D7 代替。
- `t4_round4_ledger_review.md` 是否与我上次的回复逐字一致没有核，这不在本次 delta 范围内。

---

# 主控的处理 (主控追加, 不属于审查者原文; 不改判)

- 第一次审查的 M-1 / L-1 / L-3: 回 writer 小修 → 同一 reviewer delta 复审 PASS (上面). L-2 (回写脚本先写台账后断言) 是既有设计, 已写在 `HANDOFF.md` "坑"; L-4 (`work/t3_t4_risk_anchorless.txt` 511 → 512 行, 多的就是这条; `t4_sample.py` 不再重跑, 层规模数字 508 是当时的值) 与 L-5 (新行 `ts` 沿用固定值, 决定日期在 `evidence.t4_r4l.decision`) 记为已知, 不改.
- DL-1: `work/t4/atomerr/verdicts.json` 已补进 `scripts/t4/t4_gate_prerun.sh` 的 md5 清单 (连同 `coverage_ledger.wc.pre_r4l.jsonl`、`t4_r4l_relabel.json`); `HANDOFF.md` "坑" 加了一句 (重跑 `t4_atomerr_report.py` 若使 NOT_HOLD 集合变化, 整链会报错, 须先更新清单). 审查者指出的 "用审查者判定去钉主人决定" 的耦合记为已知: 现在两者恰好一致 (主人 C1 = 唯一的 NOT_HOLD).
- DL-2 (两边都空时报文措辞不准): 不改, 记已知 (只影响措辞, 拦得住).
- DL-3: `scripts/t4/t4_extract_reply.py` 是主控本会话写的工具 (把 subagent 的最后一条回复从会话记录里原样取出存档), 与判定链无关.
- 审查者没看渲染页 p124: 这一条的渲染页已由加查的两位审查者各自看过 (`evidence/t4_atomerr_raw/pack_1.md` E12、`second_look.md` E12).
- writer 指出规格里的登记号 `B-RS T-6` 写得不全 (登记表里的 id 是 `B-RS T-6 (RS 副本)`): 是主控规格的笔误, writer 用全名, reviewer 判正确; 规格文件不回改 (留痕), 在这里更正.
