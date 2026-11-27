# T4.1 总闸 — 加查与 R4L 之后的 delta 闸审 — 审查者报告原文

<!-- chain: E (plans) -->
> 审查者 `feature-dev:code-reviewer` (opus) 新实例, 只读, 无 Bash; brief `subagent_prompts/t4_gate_reviewer_v3.2.md`; 对象 HEAD `6d89fb9` (预跑日志 `work/t4/gate_prerun.log` 在 `2c61ea5` 上生成). 派发 / 返回时间见 `trace.jsonl` 的 `T4.1` attempt `3-delta2` 行. 下面是审查者回复正文, 由脚本 `scripts/t4/t4_extract_reply.py` 从会话记录里原样取出 (主控未改一字; 规则 D).

---

## T4.1 总闸 delta 闸审（加查与 R4L 之后）— 审查者报告

审查者：`feature-dev:code-reviewer` 新实例，只读，无 Bash。brief `subagent_prompts/t4_gate_reviewer_v3.2.md`。对象 HEAD `6d89fb9`（预跑日志在 `2c61ea5` 上生成）。路径省略前缀 `.work/10_tier_b_repair/`，KB 路径除外。

### 1. 总结论：**PASS**（仅指 T4.1 总闸，由 attempt 3、delta 与本次三者合并得出）

- **A 项三问都成立。** 我按列对齐重判 `ig34_p0124_a001`，结果是 HOLDS：原子没抽错，KB 逐字承载，EXACT 成立。这个标签由现有的 live-hit 路径判出，是有断言约束的成因层撤销，不是事后覆盖标签。
- **R4L 没有清单外的变化。** 恰好 1 条改标，另有 4 行只改了 `registry`。
- **没有哪条 G-TB 变成 NOT_MET。**
- **加查抽核：** 我抽核了 12 条，与审查者全部一致，没有 "应改而未改" 的 NOT_HOLD。D 项判 **已关（带局限）**。
- **新的条件（不挡闸）：** R4L 这一批的 G-TB8 字面条件，和 R3L 当时一样只有 2 种 subagent_type。M-10 的追认只覆盖 R3L，R4L 的机制选择也没有登记（没有 M-11）。这一点按 R3L 的先例处理，见 C、H。
- 另有 LOW 9 处，主控改字即可。

**push 之前须处理的事项：**
- ① 在最终 HEAD 上重跑 `scripts/t4/t4_prepush_check.sh`，并补 `t4_prepush_check.md` "§3 最终一次"（目前是空的）。
- ② 把本报告原样存档，并在 trace 补本次的 `subagent_done` 行，兼作 R4L 批第三个不同类型的独立核验记录。
- ③ 在 `t4_user_decisions.md` §000b 登记 M-11（R4L 的机制选择）。

这三项都是文字或记录类，不改判。

**需主人但不挡闸：**
- M-11 追认，可事后告知。
- 以后若遇到 "值内空格恰好落在折行处"，D1 未说明哪条优先（见 E）。

### 2. A 项（`ig34_p0124_a001`）

**(1) 主人的回答足以作为改标依据。**
- 第六次、第七次提问（`t4_owner_confirmation.md:121, :135`）列出了 C1 / C2 的选项，C1 的含义是 "改回 EXACT，只改台账 1 条，不动 KB"。
- 消息 5「C1、D1、追认 M-10」（:142）点名了选项，是正面回答。
- 局限同前：一句短话，没有截图。另外：
  - 记录写的收到时间是 14:41:14Z，标注 "收到后立即取的时钟"。
  - 但写入原话与 D1 口径的提交 `cd24cc2`，在 reflog 里的时间约为 14:41:15Z（我手算换算 UTC）。
  - 1 秒内不可能写完这些文件，所以那个时钟不是收到时立即取的。这属于记录形式的局限，见 LOW-8。

**(2) 台账这一行，以及我自己的重判。**
- 台账第 3280 行现在是：`verdict` EXACT / `rule` live-hit / `batch_id` T4-R4L / `hit_file` `ML/examples.md`，`hit_lines` [42]。`evidence.t4_r4l` 指向消息 5、`pack_1.md:29` 与 `second_look.md:20`。
- 改前备份同一行是 ATOM_ERR / S1-R1，basis 为 "MIDSDTC 截断"。
- 列对齐：我按字符列号把 `ig34_p0124.txt` 第 1 行表头与第 2-5 行对齐：
  - MLDOSE 8 / MLDOSU oz 在第 97 / 104 列。
  - MLDTC 空；第 117 列的 "2015-09-" + "03T08:30" 属于 MLSTDTC。
  - MLENDTC、MLEVLINT 空。
  - 第 163 列的 "LAST / MEAL / PRIOR / TO" 属于 RELMIDS。
  - 第 173 列是 MIDS = HYPO2；第 179 列是 MIDSDTC = "2015-09-" + "03T17:00"。
- 原子 `pdf_atoms.jsonl:3280` 的 18 格与上面逐格一致，MIDSDTC 完整，没有截断。
- KB `ML/examples.md:42` 的 18 格与 PDF 逐格一致，表头在 :39。
- 我的判定：**HOLDS**，EXACT 成立。原子带 `OptionE_p124_rerun`，"截断" 这个说法很可能针对的是重抽之前的版本 [推断]。

**(3) "由现有判定路径得出" 属实，需要说准确。**
- `t3_errata_build.py:242-255`：先断言清单等于 `verdicts.json` 的 NOT_HOLD 集合，且这条原子只因一条 t1_errata R1 注记而是 ATOM_ERR（不涉及 registry、triage、R2L、pending_user）。然后把它从 `atom_err` 移到 `r4l_revoked`。
- `t3_writeback.py:69-78`：再次断言清单 = `r4l_revoked` = NOT_HOLD 集合，然后把它并入允许集。
- `decide()`（:249-295）在 atom_err、FIGURE、R2L_IE、K3B、pending_user 这几支都不命中，落到 `hit` → `("EXACT","live-hit")`。
- 后处理 :549-553 只改 `batch_id` 和 `evidence`，不改 verdict。
- 断言段：:618-619 要求 EXACT 必须有词界锚定的命中；:622 要求不在 K3B；:655-657 要求规则 = live-hit。
- 结论：不是事后覆盖标签，是成因层撤销后由原判定路径判出。`find_hit` / `valid_hits` 的函数体我没读 [采信 R4L reviewer]。

### 3. B 项

- **改动范围：**
  - 日志第 152 行："label changed 1 … other-fields-only [4] == R4L registry_ptr list: True | all other rows byte-identical: True" [读日志]。
  - `r4l_ledger_diff.txt`：identical 12487 / label-changed 1 / other-changed 4，4 行都是 `registry: [] → [...]`。
- **我用 Grep 核的计数：**
  - 工作台账：ATOM_ERR 196 / EXACT 4711 / PDF_TYPO 170；EQUIVALENT + IE + FIG = 6519（3949 + 2559 + 11）。
  - S1-R1 的 ATOM_ERR 156；`T4-R4L` 1 行。
  - 改前备份：ATOM_ERR 197 / EXACT 4710。
  - 以上都与日志第 42 行和 brief G 一致。
- **4 条补的登记指针**（台账 4187 / 8478 / 8507 / 9039 行；在登记表里都存在，内容对得上）：

| 原子 | 登记 | 登记表行 | 登记内容 | 与原子 / KB 的对照 |
|---|---|---|---|---|
| `ig34_p0161_a0012` | `B-DS T-4` | 51 | p161 "epocch" → epoch | 与 DS:120 一致 |
| `ig34_p0337_a003` | `B-RS T-3` | 154 | pdf_page 336 "uses a a source value" | 原子挂在 p337，但内容实际在 p336，登记页号是对的；与 RS:81 一致 |
| `ig34_p0339_a001` | `B-RS T-6 (RS 副本)` | 85 | "--STRNC" → "--STNRC" | KB RS:128 |
| `ig34_p0361_a016` | `B-FA T-2` | 74 | "Section 6.4.4.," | 我核了 `ig34_p0361.txt:37` 与 FA:15 |

- **写者与审者分离：** trace 512-518 行，writer 是 `oh-my-claudecode:executor`，reviewer 是 `oh-my-claudecode:code-reviewer`，类型不同。提交 `65d6a0f`（约 15:22:27Z）晚于 reviewer 的 delta PASS（15:22:13Z）。
- **reviewer 的 LOW 与主控的处理：合理。**
  - M-1 / L-1 / L-3 回 writer 小修，同一 reviewer 做了 delta 复审。
  - L-2 / L-5 是沿用的既有做法。
  - L-4：这条原子进入 anchorless 清单，原因是所属节 "§6.1.4 [Meal Data (ML)]" 不带节号，属实。
  - DL-1 的耦合（R4L 清单靠审查者判定文件来钉）已登记为已知。
  - DL-3 见 H 项。

### 4. C 项：有变化的闸

| 闸 | 现判 | 新依据 |
|---|---|---|
| G-TB1 | MET_WITH_CONDITION，沿用 | 174/174，残留 0（日志第 18 行）[读日志]。ATOM_ERR 196 = U-5 195 + U-2 1（日志第 280 行）[读日志]。条件仍只有 U-5 整类代裁。 |
| G-TB3 | MET_WITH_CONDITION，沿用 | U-1 B 99.2651% 不变；strict 95.5703 → 95.5804，是上升；mapped 99.3512；内容 90.6237（日志 23-27 行）[读日志]。 |
| G-TB5 | MET_WITH_CONDITION，沿用 | R4L 没改 KB prose。这 1 条的语义核验有三次：tracer、general-purpose 互不知情各判一次，加上我本次重判。 |
| G-TB8 | MET_WITH_CONDITION（R3L 的条件已关；R4L 有新条件） | R3L 那一批的字面条件已由 M-10 追认关闭（F 项）。R4L 在 trace 里只有 executor 和 code-reviewer 两种类型，第三种由本次审查充当，须补 trace 行。R4L 的机制选择（撤销 errata、强制重写为 TB 行、固定 ts、不设 auditor、`verdicts.json` 耦合）还没有登记。按 R3L 的先例判不挡闸。 |
| G-TB9 | MET_WITH_CONDITION，沿用 | t3_mutation：M0 / M2 / M7 绿，M1 / M3-M6 红，真 KB md5 前后不变。t0_mutation_head：13/13 施加，ALL MATCH（日志 66-127 行）[读日志]。§8 的基线重建没有送独立审查。 |
| direct_hit | 无变化 | GREEN；TB 1034（= 1033 + 1），stock 1748，pre_existing 52 [读日志] |
| G-TB2 / 4 / 6 / 7 | 沿用 | 174/174 与字面 157/174；census 497 / 309 / 38 / 148；反向溯源 5414/5414、UNEXPLAINED 0；live docs 42 [读日志] |

### 5. D 项（"ATOM_ERR / PDF_TYPO 补抽"）

**做法核对：**
- **筛法与对账 157 = 74 + 6 + 77：成立。**
  - `atomerr_population.json`：judged_before 80 = 补检 74 + 总闸样本 5 + T4.2 预筛 1；`judged_before_not_holds` 为空。
  - `new` 77 条、`checked` 83 条，我逐行数过。
  - 日志第 284-287 行：NEW 77 = 76 HOLDS / 1 NOT_HOLD，RECHECK 6 = 6 HOLDS [读日志]。
- **口径是否在派发之前提交：是。**
  - reflog 顺序是 `bf303d8`（brief + 包 + 筛法）→ `251b2de`（审查者原始结果）。
  - 各审查者文件头的 `date -u` 在 14:10:11Z 到 14:11:59Z 之间。
  - `bf303d8` 我手算约为 14:09:19Z，早于 trace 里的派发时间 14:09:59Z。
  - brief 文末的 "v1.0 之后的口径补注" 是事后加的，但写明了是事后加的，也没有用它改任何一条判定。
- **审查者独立性：** 包 1-4 是 tracer ×4，复看是 general-purpose，类型不同。`second_look.md:12` 自述没读包 1-4 的结果 [采信]。
- **盲复检 6 条：与原判一致。**
  - 样本包里不给先前结论（我看了 E6 那一条确认）。
  - 新判 E6 / E30 / E35 / E37 / E42 / E80 全部 HOLDS [自算 Grep]，与 `recheck_prior` 记的原判（HOLDS / 内容正确）一致。
- **"每条都有逐条判定行" 的说法：**
  - `t4_atomerr_coverage.py` 核的是 "有判定行"，判定词是任意的，包括 NOT_HOLD。它证明 "每条都被看过"，不等于 "每条都判成立"。
  - 日志第 293 行的 "ATOM_ERR 197" 是按改前台账算的；现在的 196 条是那 197 条的子集，所以仍然成立。
  - S1-R1 以外各条的 "判成立" 依赖前几轮的记录 [采信]；`ig34_p0293_a038` 仍是已知的 UNVERIFIABLE（按 B1 处理）。

**我抽核的 12 条**（"先" = 我先用文本层与 KB 自判，再看审查者的判定行；"后" = 看过审查者的判定行之后才核）：

| 编号 | atom_id | 审查者判定 | 我的判定 | 依据 |
|---|---|---|---|---|
| E22（先） | ig34_p0154_a0015 | HOLDS | HOLDS | `p0154:24-25` USUBJID "ABC -US-" + "701-002"，原子没有空格（按 D1 算真实差异）；其余格一致；KB CE:125 = PDF（B-CE T-2） |
| E25（先） | ig34_p0155_a0002 | HOLDS | HOLDS | `p0155:2` 同上；KB CE:150 = PDF（B-CE T-2） |
| E26（先） | ig34_p0161_a0012 | HOLDS | HOLDS | 原子写 DSCAT，PDF `:19` 是 DSSCAT；KB DS:120 = PDF，只有 epocch → epoch 一处差异（B-DS T-4） |
| E50（先） | ig34_p0274_a019 | HOLDS | HOLDS | 原子第 7 行多 "Collected"，PDF `:35` 那一格空；KB PP:74 = PDF |
| E60（先） | ig34_p0307_a008 | HOLDS | HOLDS | 列号对齐后 RPSTRESN 在第 132 列，值为 "1"，原子是空的；KB RP:11 = PDF |
| E36（先） | ig34_p0238_a005 | HOLDS | HOLDS | 原子 ISSEQ 3，PDF `:7` 是 1；KB IS:162 = PDF |
| E54（先） | ig34_p0301_a017 | HOLDS | HOLDS | 原子漏 ', using OETESTCD="INTP"'，多出 OEDTC 串；KB OE:7 = PDF |
| E61（先） | ig34_p0322_a013 | HOLDS | HOLDS | 原子漏 "see Section 4 of the QRS supplement. See"；KB FT:68 = PDF |
| E10（后） | ig34_p0122_a017 | HOLDS | HOLDS | 原子第二句多 "not"（`:37`）；KB ML:13 = PDF |
| E13（后） | ig34_p0133_a003 | HOLDS | HOLDS | PDF 18 列（`:2`，列号对齐），原子 21 格串列；KB SU:37 18 格 = PDF |
| E64（后） | ig34_p0337_a003 | HOLDS | HOLDS | 原子 ">-3" / "RSORRESRU"，PDF `p0336:34-35` 是 ">3" / "RSORRESU"；KB RS:81 只差登记的 "a a"（B-RS T-3） |
| E75（后） | ig34_p0360_a021 | HOLDS | HOLDS | 列号对齐后 VSDY = 1，VSTPT = "BASELINE" + 第 36 行的 "1"；原子 VSDY 空、VSTPT 只到 BASELINE；KB VS:17 = PDF |

- 另外按文本层核了 E71、E79、E83、E12，都是 HOLDS（E12 即 A 项那条，我的判定是 ①不成立，与审查者相同）。
- 与审查者不一致的判定：**无**。描述层面有一处出入：`second_look.md` 写 E13 的 su.xpt 有 "19 列"，实际是 18 列，不影响判定（LOW-6）。
- **这一项的现状态：已关（带局限）。**
  - 原来的缺口（S1-R1 里约 83 条没被单独逐条看过）已经补上：157 条都有独立审查者的逐条判定。
  - 查出的 1 条 NOT_HOLD 已由 R4L 改掉；取决于口径的 8 条已由 D1 定下。
  - 局限：渲染页我没看；S1-R1 以外各条的 "判成立" 是采信前几轮记录；加查汇总本身没有送独立审查（见 H）。

### 6. E / F 项

**E（问题 D 的处理）：足够，有一处缺口。**
- **与标签定义自洽。** v1.0 brief :15 对 ATOM_ERR 的定义是 "原子与 PDF 不符，而 KB 按 PDF 写对了"。KB 照录了 PDF 里的空格，符合这个定义。
- **与登记 `B-CE T-2` 自洽。** 登记的 handling 是 "照录+T4"，依据写 "PDF 8 处一致带空格"。8 行台账都挂着这条登记的指针（3972 / 3974 / 3985-3987 / 4001 / 4002 / 4004 行）。
- **与两位审查者当时的判定自洽。** 他们都按 "值类一个字符都要对" 判 HOLDS（`pack_1.md:35-38`、`pack_2.md:14, :47`）。
- **登记位置与写法：** `t4_user_decisions.md:84`、加查 brief :46-49、`PLAN.md:117` 写法明确，以后的审查者可以照此执行。
- **缺口一：** 上级 brief `t4_supp_fullcheck_v1.0.md:14, :35` 里那两句话仍然没有写先后，也没有指向 D1，以后复用会再撞上（LOW-7）。
- **缺口二：** D1 把 "折行处的空白" 列为可归一的空白，但没有说值内空格恰好落在折行处时哪条优先。`ig34_p0293_a038` 这类情况会碰到这个边界，建议主人以后补一句。不挡闸。
- **8 条维持 ATOM_ERR 没有留下矛盾。** 登记依据里提到 USUBJID 惯例不含空格，这只是 D3 的理由，主人选了 D1。

**F（M-10）：足以关掉。**
- 第四次、第五次、第七次提问都写明了 M-10 ⑥ "只有两类审查角色"（:100、:109、:135）。消息 5 明文写了 "追认 M-10"。
- 所以 delta 报告里 G-TB8 的那个字面条件对 R3L 已关。
- 它不覆盖 R4L，见 C 项。

### 7. G 项：过期与矛盾（都是 LOW，主控改）

- **现值一致的位置：** `PLAN.md:117`、`HANDOFF.md:92`、`_progress.json:239, :241`、`t4_atomerr_fullcheck.md:157`、`docs/PROGRESS.md:22`（99.27 / 95.58 是取整）、`t4_ack_lists.md` 头部（日志 272-280 行）都与现值一致。
- **LOW-1** `_progress.json:247` 的 G-TB9 仍写 "R3L 后 … §7"，没有 §8；`:246` 的 G-TB8 仍写 "MET 字面 (attempt 2)"，没有反映 R3L / R4L 的情况。
- **LOW-2** `audit_matrix.md:7` 只引到 §6 / §7，缺 §8。
- **LOW-3** `HANDOFF.md:69` 那一节的标题标着 "仍有效"，但其中 :72 的现数字（95.5703 / EXACT 4710 / ATOM_ERR 197）和 :74 的 "M-10 待追认" 都已过期。标题只说 "仍开 ①②" 看最后一节，数字没有包括进去。
- **LOW-4** `t4_user_decisions.md:63` 的 §000c 引言只写到消息 4，没提消息 5（:83-85 的表行有）。
- **LOW-5** `t4_atomerr_fullcheck.md:58` 与日志第 293 行写的是 "197 / 197 都有判定行"：应补一句说明 "有判定行 ≠ 判成立"，以及现在的 196 是那 197 的子集。
- **LOW-6** `second_look.md:21` 写 E13 "19 列"，实际是 18 列。
- **LOW-7** 见 E 项（上级 brief 两句话没有写先后）。
- **LOW-8** 消息 5 的 "收到后立即取的时钟" 与 `cd24cc2` 的提交时间只差约 1 秒，见 A(1)。
- **LOW-9** `PLAN.md:4` 状态行很长，括号里还留着 "问题 A / B 未答"；有时点链条，不算错，但可以压短。

### 8. H / I 项处置表

| 项 | 挡闸? | 理由 | 由谁补 |
|---|---|---|---|
| 主控写的加查汇总 | 不挡，记已知局限 | 我核了 §1 的数字、§3 的计数、§5a / §5b 的事实与 §8 的现值，问题只有 LOW-5 | 主控改字 |
| R4L 之后的 T0 基线重建（§8） | 不挡 | 日志 13/13 施加、ALL MATCH，与 §7 的日志逐行相同 [读日志]；我没有复跑 | 可选：独立复跑一次 |
| 主控改的 5 份脚本与重生成的 2 份汇总 | 不挡 | 只对照了日志输出，没读脚本 diff。日志的计数与我 Grep 的一致；两份汇总已带 R4L 字样 [抽查 Grep] | 可选：独立审 diff |
| 推送前检查的口径（不含用户名的机器路径由协调方放行） | 不挡 T4.1；push 前须重跑 | 决定人是协调方，不在闸的范围内；预跑在 `734b91e` 上做，"最终一次" 一节还是空的 | 主控（push 前）；主人若有异议，经协调方转达 |
| R4L 没设语义 auditor | 不挡 | 语义有三次独立核验（tracer、general-purpose、本次）；作为 M-11 的一部分 | 主控登记 M-11；主人追认（可事后告知） |
| 加查审查者没看的东西 | 不挡 | 各文件头都自述看了渲染页；包 3 只读 grep 过台账（这批标签都是 ATOM_ERR，无诱导）；`t4_extract_reply.py` 是主控写的取原文工具，没有经过审查 | 记已知 |
| 记录时间（LOW-8） | 不挡，记已知局限 | 与既有的记录形式局限同类 | 协调方可佐证 |
| I：抽样而非全检的几类、约 80 条标签级别项、O68-O71、trace 整点时间戳、记录形式的局限 | 不挡，同意前两份报告 | 现状没变；R4L 新行的 ts 2026-11-26 属于同类（reviewer L-5） | — |

### 9. 我核过的数字与位置

- **[自算 Grep / Read]**
  - 台账计数：ATOM_ERR 196 / EXACT 4711 / PDF_TYPO 170 / EQUIVALENT + IE + FIG 6519 / S1-R1 的 ATOM_ERR 156 / `T4-R4L` 1 行；改前备份 197 / 4710。
  - 台账第 3280 行改前与改后；4 条指针所在的 4187 / 8478 / 8507 / 9039 行；B-CE T-2 的 8 行指针。
  - 登记表 274 行，以及第 19 / 51 / 74 / 85 / 154 行。
  - 两份 t3 脚本的 R4L 段；`decide()` 的 :249-298。
  - population.json 的各项计数；trace 499-521 行。
  - 本地 reflog 的提交顺序（时间是我手算换算的 UTC）。
  - 上表 12 条加上 E71 / E79 / E83 的文本层与 KB 行。
  - 第 7 节列出的各文档行。
- **[读日志]** live docs 42；节数 174 / 157；覆盖率四个数；direct_hit；census；t3 / t0 变异；反向溯源；R4L 单批的逐字节比较；各文件 md5（台账 `eef9bb14…`，KB 树 `63f85777…`）；ack 来源；83 行的解析结果。
- **[采信]** 渲染页上的空格与字形；`find_hit` / `valid_hits` 的函数体；S1-R1 以外各条 "判成立"；复看者没读包 1-4 的结果；U-7 A1-7 的来源。
- **没能核的：**
  - 所有渲染页；所有命令（我没有 Bash）。
  - 5 份脚本的 diff。
  - 消息 5 的会话原文，以及 `cd24cc2` 里那段文字是否早于消息就写好了。
  - `ig34_p0293_a038` 的字符级情况。
