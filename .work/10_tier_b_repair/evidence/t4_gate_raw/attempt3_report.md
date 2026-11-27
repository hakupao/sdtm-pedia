# T4.1 总闸 attempt 3 — 审查者报告原文

<!-- chain: E (plans) -->
> 审查者 `feature-dev:code-reviewer` (opus) 新实例, 只读, 无 Bash; brief `subagent_prompts/t4_gate_reviewer_v3.0.md`; 对象 HEAD `4a5dd1d` (预跑日志 `work/t4/gate_prerun.log` 在 `a88a585` 上生成). 派发 / 返回时间见 `trace.jsonl` 的 `T4.1` attempt 3 行. 下面是审查者回复正文, 由脚本从会话记录里原样取出 (主控未改一字; 规则 D).

---

**总结论：CONDITIONAL**

T4.1 总闸 attempt 3 不通过。G-TB1 到 G-TB9 没有一条判 NOT_MET；78 条改标我挑了 10 条核，全部成立；样本交集是 0。挡住 PASS 的只有一件事：第三轮审查查出 4 条 PDF_TYPO 多标（`ig34_p0412_a006` / `a007` / `a008`、`ig34_p0413_a010`），我用文本层逐条复核，确认它们自己的 PDF 原文没有笔误，KB 与 PDF 逐字一致，应为 EXACT。这 4 条现在仍是 PDF_TYPO，挂的登记 `S-TDM TD T-1` / `T-4` 描述的是相邻原子或另一张表。按 brief 的判定口径，任一样本 NOT_HOLD 就不能 PASS，而它们是第三轮全检样本里的条目。主人对问题 A 只回了「继续」，没有选。另外，M-9、问题 B 以及几处过期数字都不挡闸，单列在后面。

---

### 1. G-TB 逐条

| 闸 | 判定 | 依据 | 条件 / 缺口 |
|---|---|---|---|
| G-TB1 | MET_WITH_CONDITION | 日志第 18 行：`§5.0 scope sections=174 residual_gap=0 G-TB1 pass=174/174` [读日志]。PDF_TYPO 174 行登记都非空（`"registry": []` 0 条）[自算 Grep]。ack 来源合计 122+22+19+6+4+1=174，`(未归因)` 0 条（`t4_ack_lists.md:13`）[自算]。 | 4 条 TD 原子的 "登记" 实际描述的是邻近原子，ack 是 U-5 整类代裁（`t4_ack_lists.md:376-380`），所以 "每条有登记" 在实质上对这 4 条不成立。没判 NOT_MET，是因为它们落在终态类里、残留为 0、正确标签 EXACT 也是终态类；但按判定口径这 4 条挡 PASS。问题 B 那 1 条另列。 |
| G-TB2 | MET（U-3 范围内口径） | 日志第 18 行：范围内 174/174，字面口径 157/174 [读日志] | 取决于 U-3 A。第一轮记录已确认，见 C 项。 |
| G-TB3 | MET_WITH_CONDITION | U-1 B 9860/9933 = 99.2651% ≥ 06 基线 99.0192%；strict 95.5301%；mapped 99.3509%；内容 90.6188%（日志 23-27 行）[读日志]。这些值等于预演值（`t4_relabel_pending.md:4`；`t4_owner_decisions_round2.md:123`）。 | 按 PLAN 字面 "06 口径 ≥99.02%"，strict 不达标，过闸完全依赖 U-1 B（PLAN:112 口径注）。U-1 B 现值比主人确认时的 99.2690 低了 0.0039 个百分点，但第二轮那一页给主人看过新值，见 C 项。 |
| G-TB4 | MET_WITH_CONDITION | HEAD census：497 张表 / OK 309 / DIFF 38 / diffs 148 / UNPARSEABLE 146 / PDF_ONLY 0（日志 61 行）[读日志]，与 `t4_c3_closeout.md:29` 一致。C3 60 张 = 49 + 4 + 7 已逐表结案（:235），verifier 审过（:258-283）。 | census 原始输出是 RED，靠 "PDF_TYPO 登记例外" 过闸。148 处差异的基数沿用 T2 分诊 [采信]；新增的 4 处我只核了 DS:292（`B-DS U-1`，PDF p165:3 是 SCREEN，KB DS:294/298 是 SCRN）。 |
| G-TB5 | MET_WITH_CONDITION | R2L 的 auditor：N=33，seed 20261134，结果 33/33（`t4_round2_ledger_audit.md:5-8`）。`audit_matrix.md:97-114` 已补齐 T3 / T4 各行。 | 规格 `t4_round2_ledger_spec_v1.0.md` 里没写 N。"事先定" 的证据只有派发时的 trace 行（trace 476，09:12:07Z，早于完成时刻 09:18:34Z）和 auditor 自述。33 大于 PLAN §5.3 的公式值 16，是从严，但不是写在计划里的。`audit_matrix.md:7` 有过期字样，见 D 项。 |
| G-TB6 | MET（U-4 A / M-6） | 日志 135-138 行：新增 5414 行全部溯源，比例 100%；UNEXPLAINED 0；NOTE_EXEMPT 5 条，每条命中 1 次 [读日志] | C 层是抽样过闸（U-4）；5 条 Note 豁免是 M-6，已在第一轮记录中追认。 |
| G-TB7 | MET | 日志第 13 行：`live docs: 42` ≤ 42 [读日志] | 我没有复跑。 |
| G-TB8 | MET | trace 473-482：T4.R2L 的 writer 是 `oh-my-claudecode:executor`，reviewer 是 `oh-my-claudecode:code-reviewer`，auditor 是 `oh-my-claudecode:verifier`，三种不同 [自算 Read]。reviewer 在隔离副本里从改前台账整链跑了两遍（runA/B），delta 复审又跑了两遍（runC/D），md5 都是 `16024ac0…`（`t4_round2_ledger_review.md:9,40,68`），与日志第 2 行和第 282 行一致。 | 能证明到这一步：台账等于脚本整链的输出。脚本输入 `t4_r2l_relabel.json` 是一次性脚本生成的，生成人未写明；它的内容与主人选的清单逐条一致（日志第 148 行）。主控那一行（trace 483）只动了脚本和文档。上一任会话的时间戳问题依旧（未决项 8）。 |
| G-TB9 | MET_WITH_CONDITION | t3_mutation：M0 / M2 / M7 绿，M1 / M3-M6 红，真 KB md5 前后不变（日志 66-85 行）。t0_mutation_head：13/13 变异施加，EXPECT 8/8，M4 7/7，三次复原都绿，`ALL MATCH`（日志 92-127 行）[读日志]。M4a 换靶（M-8）主人第二轮问题 5 已追认（`t4_user_decisions.md:57`）。 | `t4_t0_refresh.md` §6 的基线重建没有送独立审查（:96）。预跑日志也是主控跑的，我只能读。脚本和用例没改，风险低。 |

### 2. 样本层

**交集 [自算 Grep]**
- 78 条改标和 5 条只改指针的行，与以下样本的交集都是 0：总闸样本 `gate_sample.jsonl` 84 条、T4.2 预筛 `human_sample.jsonl` 42 条、主人抽查 6 条。这三份样本全部沿用 attempt 1 / 2 的判定。
- 我的 Grep 命中过 3 个相近的 id（`sv20_p0047_a003`、`sv20_p0051_a016`、`sv20_p0046_a005`），都不在改动集里。
- 补检 / Q9 / 第二轮 / 第三轮这几份样本本身就是 78 条改标的来源（日志 154-241 行），原判定就是 "旧标签不成立"。我从中挑了下表的 10 条重判。

**我挑的改标原子（四组都有）**

| # | atom_id | 组 | 新标签 | 判定 | 依据 |
|---|---|---|---|---|---|
| 1 | sv20_p0052_a012 | R1-row | IE | HOLDS | PDF `sv20_p0052.txt:29-31`：TA STUDYID 行有 C83082 和 Definition 列。KB `model/05_study_level_data.md:55` 是 5 列精简版，这 5 格与 PDF 一致。符合 R1（`t1_user_ack.md:4`）。 |
| 2 | sv20_p0058_a005 | R1-row | IE | HOLDS | PDF `sv20_p0058.txt:15-16`：MIDSTYPE 有 Notes 和 Examples。KB `05:188` 5 列一致，Notes 未收。 |
| 3 | sv20_p0069_a001 | R1-row（原 EXACT） | IE | HOLDS | PDF `sv20_p0069.txt:6-10`：§6.6 APID 行有 Notes。KB `06_relationship_datasets.md:151` 只有 5 列。旧 EXACT 是配到了 `04:39`（另一张表），不成立。 |
| 4 | sv20_p0003_a011 | v2.0-TOC | IE | HOLDS | PDF `sv20_p0003.txt:18` 是 "9 APPENDICES"。v2.0 的附录在 KB 里没有，`knowledge_base` 里只有 SDTMIG 的 `ch10:422` Appendix F，属于另一份文档。 |
| 5 | ig34_p0043_a010 | registered-typo | PDF_TYPO | HOLDS（仅文本层） | PDF `ig34_p0043.txt:13` 印 `"ONGOING"',`，多一个撇号。KB `ch04:932` 写 `"ONGOING",`。登记 S-CH4 T-8。渲染页没看。 |
| 6 | ig34_p0278_a015 | registered-typo | PDF_TYPO | HOLDS | PDF `ig34_p0278.txt:15`：第 13 行 RDOMAIN 印 PC，同行 IDVAR 是 PPGRPID。KB `PC/examples.md:103` 写 PP。登记 B-PCPP T-2。原子 verbatim 写的是 PP（抽取时已改对）。 |
| 7 | ig34_p0147_a025 | registered-typo | PDF_TYPO | HOLDS | PDF `ig34_p0147.txt:30`：BSREFID 印 298B1-1R0；同页 :15 / :42 是 298R1-1R0。KB `BE/examples.md:124` 写 298R1-1R0。登记 B-BE T-3。 |
| 8 | ig34_p0083_a020 | typo-oos | PDF_TYPO | HOLDS | PDF `ig34_p0083.txt:39` 表头印 BIRTHDTC。KB `SE/examples.md:79` 写 BRTHDTC。登记 S-SPREL SE T-1，其 span_lines 含 79。 |
| 9 | ig34_p0304_a026 | typo-oos | PDF_TYPO | HOLDS | PDF `ig34_p0304.txt:29` 印 OCCULAR。KB `OE/examples.md:142` 写 OCULAR COMFORT，与 suppoe `:153` 一致。登记 B-OE T-2。 |
| 10 | ig34_p0316_a023 | typo-oos | PDF_TYPO | HOLDS | PDF `ig34_p0316.txt:46` 印 laterallity。KB `PE/spec.md:174` 写 laterality。登记 S-FND PE T-1。 |

- 计数：HOLDS 10 / NOT_HOLD 0 / UNVERIFIABLE 0。
- 需要说明：第 4、6-10 号这 6 条也在 R2L auditor 的 33 条里，所以真正独立于 auditor 的只有第 1、2、3、5 号 4 条。

**样本里仍未处理的 NOT_HOLD / UNVERIFIABLE（与上表分开）**

| atom_id | 现标签 | 我的判定 | 依据 |
|---|---|---|---|
| ig34_p0412_a006 / a007 / a008 | PDF_TYPO | **NOT_HOLD**（应为 EXACT） | PDF `ig34_p0412.txt:14-16` 三句本身无误；登记的 "assessments.." 在 :17，是下一个原子。KB `TD/examples.md:40` 逐字承载这三句。[自算] |
| ig34_p0413_a010 | PDF_TYPO | **NOT_HOLD**（应为 EXACT） | PDF p413:21 印 TDTGTPAI，是对的；笔误 TDTGPAI 在 p414:29。KB `TD:102` 写 TDTGTPAI，与 PDF 一致。[自算] |
| ig34_p0293_a038 | PDF_TYPO | UNVERIFIABLE | 折行处有没有空格，文本层判不了（`t4_round3_raw/pack_9.md:28`；登记自己也注了 "折行歧义"）。我没能做字符级解析。KB 两种情况下都对。[采信] |

### 3. C 项：裁定来源

1. **上一轮四件事**（`t4_owner_confirmation.md` 第一节）
   - 作 G-TB1 的 "用户 ack"：**足够**。主人勾选的 "委托代裁全部" 选项附了原文说明（:18），委托覆盖 U-5；ack 按来源分开记。
   - 作 G-TB3 U-1 B 口径的 "用户认可"：**足够**。选项原文写明了 U-1 B 的内容和 strict 并列报告（:15）。另外，第二轮那一页明确以 U-1 B 为过闸口径（`round2.md:19`），并给出改后数字 99.2651 / 95.5301（:67、:123），主人用 "是，都按建议" 作了肯定回答。这是一次正面回答，不是沉默。
   - T4.2 hard 闸改口径并关闭：**足够**，但带已公开的局限。主人有权改口径；PLAN:82 / :134 已修订，并写明 6/6 零错的 95% 上界约 39%。
   - 这三条判断都不依赖 "邀请后未提异议"（`round2.md:151` 那句）。只看记录本身、协调方的佐证（转达）和第二轮的正面回答，结论不变。
   - 局限照实保留：上一任会话记录、一个词加多选勾选、没有截图。
2. **第二轮三条原话**
   - 「是，都按建议」是对一个逐项列出的追问的直接回答（`owner_confirmation:37,43`），足以支撑 78 条改标和问题 1-9 的登记：**足够**。
   - 「继续」没有回答问题 A / B，主控也没有替主人选（:73-76），处理得当。
   - M-9（落地机制）不在主人的选择范围内：**需主人追认**，不挡闸。
3. **人工判定来源可核性**（attempt 2 判 "不足"）：现在**足够（带局限）**。
   - 第二轮由现任主控逐字记录、附收到时间、走直接聊天渠道。
   - 第一轮有记录，有协调方原文留档（`t4_coordinator_note_20261127.md`），时间线可对。
   - 仍然没有截图或会话原文，无法从仓库外独立核对。

### 4. D 项：attempt 2 "仍开 / 部分关" 各项的现状

| 项 | 现状 | 依据 |
|---|---|---|
| C3 逐表结案清单 | 已关 | `t4_c3_closeout.md` §5 共 60 行。我抽核了 #1（`c3_closeout.json` n=1 → KB `EX:15` 表头一致，reviewer 指针 `t2_S-INT_review.md:79` 有逐格记录）和 #16（`t2_S-CH4_review.md:33`）。 |
| census 变化逐表说明 | 已关 | 同文件 §3 / §4：三个时点逐表配对，并含只有配对元数据变化的 26 张；verifier 独立配对 53/53。 |
| t0_mutation 在现 KB 重证 | 已关 | 日志 ALL MATCH；M-8 已追认；§6 基线重建未独立审（见 E）。 |
| pre_existing 58 单独核 | 已关 | 补检 58 条：HOLDS 26 / HOLDS_AS_EQUIV 30 / NOT_HOLD 2，这 2 条已由 R2L 改为 IE（`supp_fullcheck:28,57-58`）。现在是 52 条：reviewer 实测 58→52（`ledger_review:21`），日志第 54 行也是 52。 |
| FIG 11 逐条核 | 已关 | 11/11 HOLDS，对渲染页核（`supp_fullcheck:29,41`）[采信] |
| "规则 0 抽中" 各类 | 已关 | 9 个非空层 145 条全部通过（:129）[采信] |
| ATOM_ERR / PDF_TYPO 补抽 | 部分关 | PDF_TYPO 174 条全部有人看过（:119），但留下 4 条 NOT_HOLD 和 1 条 UNVERIFIABLE。ATOM_ERR 看过的是 C7 38 + triage 74 + K4 2 + 总闸 4（:102），S1-R1 157 条里约 83 条没被单独看过 [采信 / 推算]。 |
| PLAN 修订 | 已关 | PLAN:93（FIG 11）、:82 / :134（T4.2）、:112-116（口径注） |
| audit_matrix 缺行 | 已关（有过期字样） | :97-114 已补；但 :7 仍写 "M-8 待追认"，已过期。 |
| user_decisions 与 human_verdicts 的矛盾 | 已关 | `t4_user_decisions.md:2` 状态行已分层写明；`t4_human_verdicts.md:3` 不再与之冲突。 |
| 新发现的过期 / 矛盾（都是 LOW，主控改） | 仍开 | ① `_progress.json:232-233` 的 steps.T4.1 / T4.2 还停在 attempt 1 / "待用户判定"。② `audit_matrix.md:7` "M-8 待追认"。③ `t4_supp_fullcheck.md:12` 的复跑注释 "pre_existing 58"，现在跑出来是 52。④ 同文件 :98 "PDF_TYPO 149" 没有时点说明（:119 有）。⑤ `HANDOFF.md:50` "M-8 待追认" 在下午那一节，那一节标题没有像 :21 那样标 "(历史)"。现值 99.2651 / 95.5301 / 174 / 274 / `16024ac0…` 在 PLAN:116、HANDOFF:62、`_progress.json:237-239` 都一致。 |

### 5. E 项：未审项与未决项的处置

| 项 | 挡闸? | 理由 | 由谁补 |
|---|---|---|---|
| 问题 A（4 条多标） | **挡闸** | 台账里留着已证实不成立的标签，登记指向别的原子，G-TB1 "每条有登记" 对这 4 条不成立。数字上不影响 U-1 B，strict 会 +4。 | 主人选 A1 / A2。若选 A1：writer → reviewer 改台账，按 HANDOFF:66 改断言，重建 T0 基线，再做一次 delta 闸审。 |
| 问题 B（p0293_a038） | 不挡，记已知局限 | KB 两种情况都对，判不了的只是标签 | 主人（B1 / B2），可以之后再定 |
| M-9 | 不挡，需主人 | 这是机制选择；结果与主人选的清单逐条一致，reviewer、auditor 都 PASS | 主人追认 |
| M-7 里 p0362_a010 那处更正 | 不挡 | 只是把 ack 来源归到 M-4（M-4 本身在已追认范围内），标签没变 | — |
| 第一节的局限 / 第二轮三句话 | 不挡 | 见 C 项 | — |
| 99.2690 → 99.2651 | 不挡 | 第二轮那一页给主人看过新值，主人肯定回答 | — |
| 只抽样的几类（2207 抽 215、标题 71/316、宽筛 169/142、范围外 146） | 不挡，记已知局限 | 主人选了 4d=A、7a=C；215 条 0 错，95% 上界约 1.4% | — |
| 约 80 条标签级别项、O68-O71 | 不挡，记已知局限 | 内容成立，KB 冻结 | 留后续 |
| trace 里的整点时间戳 | 不挡，记已知局限 | 无法还原，R2L 各行用的是真实时钟 | — |
| 第二轮一页第 3 稿未审 | 不挡 | 主人已经答了；我核了关键数字（:67、:123），与日志一致 | — |
| T0 §6 基线重建未审 | 不挡 | 脚本和用例没改，日志 ALL MATCH，13/13 施加 | 可选：独立复跑一次 |
| 改过的 `t4_supp_report.py` 与两份汇总 | 不挡 | 发现两处过期（D 项 ③ ④） | 主控改字 |
| `t4_r2l_sample_overlap.py` / `t4_gate_prerun.sh` | 不挡 | 我用 Grep 独立核了交集（0），日志结构完整 | — |
| HANDOFF / PLAN / _progress / audit_matrix 的更新 | 不挡 | 见 D 项的过期项 | 主控 |

**需主人但不挡闸（供主控转给主人）**：M-9 追认；问题 B 怎么记。

### 6. 我核过的数字和位置

- **[自算 Grep]**
  - 台账各标签计数：EXACT 4706 / EQUIVALENT 3949 / IE 2559 / ATOM_ERR 197 / PDF_TYPO 174 / FIG 11 / PARTIAL+MISPLACED+ERROR 896。
  - PDF_TYPO 登记为空的 0 条；`T4-R2L-owner-IE` 53 条；`T4 R2L owner` basis 25 条；登记表 274 行。
  - ack 来源加总 174。
  - 78 条改标 + 5 条指针行与 gate / human 样本交集 0。
  - 上面 10 条改标、4 条多标原子、DS:292、C3 #1 / #16 对应的 PDF 行与 KB 行。
- **[读日志]** live docs 42；节数 174 / 157；覆盖率四个数；direct_hit GREEN 与 pre_existing 52；census 497 / 38 / 148；t3 / t0 变异结果；反向溯源 5414 / 5414；各文件 md5。
- **[采信]** census 148 处差异的基数；补检 / Q9 / 第三轮各层的计数；auditor 33 条用了渲染页；`ig34_p0293_a038` 判不了；协调方消息原文。
- **我没能核的**：
  - 所有渲染页，包括 p43 的字形。
  - 各命令我都没有复跑（没有 Bash）。
  - 第一轮主人原话的会话原文。
  - 148 处 census 差异逐条对登记。
  - ATOM_ERR S1-R1 剩下的约 83 条。
