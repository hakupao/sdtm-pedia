# T4 第二轮改台账 (R2L) — 独立 reviewer (结构 / 机制 / 数字)

<!-- chain: E (plans) -->
> 状态: **PASS** (2026-11-27; MEDIUM 1 / LOW 4, 不挡提交; 小修由 writer 做, 见文末). 审查者 `oh-my-claudecode:code-reviewer` (opus), 只读, 在隔离副本复跑; 主控原样誊录 (只还原了转义), 不改判.
> 对象: 工作树里 writer 改后的台账与脚本 (基线 HEAD `774ebc5`).

# R2L 改台账独立复核报告（code-reviewer）

**整体结论：PASS，可以提交。** 7 项都通过。我从 HEAD 的台账出发，在隔离副本里把整链跑了两遍，得到的台账 md5 都是 `16024ac09721cb3f8519cd68fa455196`，和 writer 报的一致。下面有 5 条发现，1 条 MEDIUM、4 条 LOW，都不挡提交，建议提交前顺手补上发现 #1。

## A-G 判定

| 项 | 判定 | 依据 |
|---|---|---|
| **A 改动集** | PASS | 我自己写了 `a_diff.py`：先断言两份台账的 `pdf_atom_id` 逐位置相同，再逐行比较。行数 12492 / 12492；11 个重复 id 都没有变化。标签变了 78 行，全在清单里，方向全对，没有不符的。分组：R1-row EQUIV→IE 49 + EXACT→IE 2；v2.0-TOC 2；registered-typo EQUIV 10 + EXACT 9；oos EQUIV 5 + EXACT 1。`typo-overlabel` 4 条和 `ig34_p0293_a038` 逐字节没变。清单外没有标签变化。只改了非标签字段的有 5 行：`ig34_p0198_a014` / `p0206_a009` / `p0263_a020` / `p0355_a027` / `p0356_a001`。每行只动了 `evidence.registry`（末尾追加）和 `evidence.t4_r2l_registry_ptr.{add,note,raw}`，正好是规格 §2.3 的登记指针。终态计数：IE 2506→**2559**，PDF_TYPO 149→**174**，EXACT 4718→4706，EQUIVALENT 4015→3949，其余不变。 |
| **B 每条写法** | PASS | 用 `b_rows.py` 逐条核了全部 78 条，不是抽查。IE 53 条：`verdict`、`category` = VERSION_MISMATCH、`exclusion_reason`、`approved_by` 都与规格原文一字不差；`evidence.t4_r2l.raw` 等于清单的 `raw`；规则名 = T4-R2L-owner-IE。原始结果文件里对应那一行都写着这个 atom：R1-row 49 条判 NOT_HOLD_R1，2 条（`sv20_p0069_a001` / `a003`）判 NOT_HOLD；TOC 2 条判 NOT_HOLD。PDF_TYPO 25 条：`evidence.registry` 等于清单的 `registry`；登记 id 在登记表里都存在，`handling` 都是 "KB 写正确值"；`checkpoint` 以 `raw` 结尾；`basis` 里写了 "问题 3 = A" 或 "问题 7b = A"；规则名 = S1-R2。原始结果那一行有 21 条判 TYPO_AFFECTED，另外 4 条补检判 HOLDS_AS_EQUIV（`p0147_a025`、`p0262_a016` / `a017`、`p0296_a023`），而且都点名了同一个登记 id。errata 里 25 条全在。范围外 6 条用 `inventory.jsonl` 核过，都不在 §5.0 范围内：§5.3 SE、§6.3.7.5 OE、§6.3.8 PE。范围内的 72 条确实都在范围内。 |
| **C 机制** | PASS（有 1 条 MEDIUM） | 运行时脚本没有硬编码 atom id，都读 `work/t4_r2l_relabel.json`。"IE 必须在 `t1_ie_final.md`" 的放行条件是：该原子在 R2L 的 IE 清单里、并且规则名 = T4-R2L-owner-IE。我在副本里把规则名改掉（W2），53 条随即全部报 `IE flip not in t1_ie_final`，说明放行只限这 53 条。新断言我在副本里做了变异，都会失败：W1 从 errata 删掉一条 → rc=1（报的是 KeyError，见发现 #3）；W3 给非 PDF_TYPO 原子加登记指针 → AssertionError；W4 让 IE 清单与 atom_err 重叠 → AssertionError。原有断言只动了 IE flip 那一行，加的是上面那个窄条件，其余没有放宽。范围外 6 条没有进 keep 清单。errata 里的 PDF 行 / KB 行 + token 断言用的是同一套 `norm_pdf` / `norm`，6 个 token 我对 PDF 文本层和 KB 行逐一看过，确实成立。但这个断言写成了 `if "pdf" in e:`：数据里少了 `pdf` 键时会静默跳过。变异 E1 证实了这一点（发现 #1）。 |
| **D 登记更正** | PASS | 行数 272→274。我用 `t4_r2l_registry_fix.py` 在副本上从 HEAD 的登记表重放，得到 md5 `e6f86b49…`，与工作树一致。页号：p212 第 3 行是 row 6 续行，印 "16T04:20"，其余行是 "16T12:20"，所以 B-CP T-5 = 212 成立；p239 第 35/39/43 行有 "AUREUS–EPITOPE X"，B-IS T-6 = 239 成立。新增 `T4R2 sv20 N-1`：p69 第 21-23 行写 "subject or pool identified in RDEVID"，p50 第 36 行写 "device"；KB `model/04_associated_persons.md:42` 写 "device"，与 p50 相符。新增 `T4R2 RELSPEC N-1`：KB `RELSPEC/examples.md:17` 是 "(Brain)"，:50 是 TISSUE；p440 文本层第 26 行是 TISSUE；图里的 "Brain" 依据 `pack_6.md:25,64`。两条的 `handling` 都是 "照录"，字段与现有照录行一致。文字 / 指针更正都能在 `pack_8.md:25,28,54,58,59`、`pack_9.md:57`、`pack_10.md:57`、`pack_typo_2.md:50`、`pack_sib_3.md:67`、`pack_sib2_1.md:34,57` 找到对应。规格之外没有别的改动（`S-SPC2 N-2` 的小问题见发现 #4）。 |
| **E 数字** | PASS | 按 `t4_coverage_decomp.py` 的公式从改后台账重算：strict 9489/9933 = 95.5301%，mapped 9489/9551 = 99.3509%，U-1 B 9860/9933 = 99.2651%，内容指标 8655/9551 = 90.6188%，与 `scenarios.json` 那一项逐字相同。`t3_recompute.py --out <scratch>`：§5.0 范围 174 节，残留缺口 0，G-TB1 174/174，G-TB2 字面 157/174（改前改后都是这个数）；当前 Tier B 节数 101→98。节级比较：状态或 IE 计数变了的恰好 17 节（另有 8 个父节只是 `child_sections` 跟着变）。SKELETON_ONLY 35→40，5 节与 writer 列的一致。这 17 节不全是 IE 增加造成的：ig34 有 4 节（§4.3.2、§5.2 DM–Examples、§5.3 SE、§6.2.2 BE）来自 EXACT/EQUIV→PDF_TYPO，匹配数减少；writer 原文也没说全是 IE 造成的。§5.0 闸口径的三个数都没变。 |
| **F ack 清单** | PASS | 去掉行号后比较：新增 25 行，决定来源写成 "主人 2026-11-27 第二轮 问题 3 = A"（19 行）或 "问题 7b = A"（6 行），登记 id 也对。PDF_TYPO 149→174；没有 "(未归因)"，脚本第 76 行有这个断言。原有行除状态行和计数行外，还有 5 行的登记列追加了 id，就是 §2.3 那 5 条指针，决定来源没动。checkpoint 没提这 5 行（发现 #5）。 |
| **G checkpoint** | PASS（有 LOW） | 核过的数字全部属实：12409 / 78 / 5；77 条原是非 TB 行，其中 76 条没有 phase、1 条是 P6_T5；hit_file 非空的 5 条都是 registered-typo 的 EXACT；anchorless 508→507；decisions 新增 77 键、6 键变化；direct_hit 1030→1029、1758→1748，pre_existing 58→52；变异 M0/M2/M7 GREEN、其余 RED，真 KB md5 前后都是 `b71a466d…`；live docs 42。"全部做了，没有撤回" 属实。"需主控定" 的 5 点描述准确。没有 TODO 或占位，没有 Markdown 链接。 |

## 发现清单

| # | 严重度 | 位置 | 问题 | 依据 | 建议改法 |
|---|---|---|---|---|---|
| 1 | MEDIUM | `scripts/t3/t3_errata_build.py:146` | 范围外 6 条的 PDF / KB + token 断言只在数据里有 `pdf` 键时才执行。U-8 的 keep 清单是每条都核；这里只靠一次性的 `t4_r2l_build.py` 保证 `pdf` 键存在，以后有人改 `t4_r2l_relabel.json`，保护会悄悄失效。 | 变异 E1：删掉 `ig34_p0316_a023` 的 `pdf` 键，再把 kb token 改成不存在的值，`errata rc=0`。 | 循环里加 `assert ("pdf" in e) == (e["group"] == "registered-typo-oos"), i`，或者按 group 强制执行这项检查。 |
| 2 | LOW | `scripts/t4/t4_r2l_build.py`（KEEP / PTR 两个字典） | 一次性生成脚本里写死了 11 个 atom id 和 token。运行时脚本没有写死，规格 ① 字面上满足，但这批数据其实是在脚本里"手写的源头"。 | 读代码。 | 可以接受（与 `T4_U7_REG` 同一做法，而且数据已经进了 JSON），在 checkpoint 写明 JSON 现在是唯一源头就行。 |
| 3 | LOW | `scripts/t3/t3_writeback.py` R2L 的断言循环（`decided[i]`） | 清单里的原子不在允许集时，报 KeyError 崩掉，到不了那条有说明的断言。仍然是 rc=1，不会漏，但报错难读。 | 变异 W1：`KeyError: 'ig34_p0037_a002'`。 | 先 `bad.append` "不在 decided"，或者改用 `decided.get(i)`。 |
| 4 | LOW | `work/t2_pdf_typo_registry.jsonl` 的 `S-SPC2 N-2.basis` | 这条不只去掉了 "照录"，还把 "应为 PPGRPID" 改成了 "应为 PC records / PCGRPID"。有依据（`pack_9.md:57` 说 PPGRPID 是草稿值、有误），但 checkpoint §2.3a 写的是 "去掉照录字样"，没提内容也改了。 | 登记表逐行 diff。 | 在 checkpoint §2.3a 补一句。 |
| 5 | LOW | `evidence/checkpoints/t4_round2_ledger_W.md` §4 | ack 清单里原有 5 行的登记列有变化（追加了指针 id），checkpoint 没写。 | ack 清单去掉行号后的 diff。 | 补一行说明。 |

另外两条，不算 writer 的问题：
- 链的第一步 `fp_head` 读的是当前台账。这是原有设计，不是这次引入的。我从 HEAD 台账 `60729f7b…` 起跑仍得到 `16024ac0…`，所以结果不依赖上一轮产物。
- 审查期间工作树里出现了 `evidence/checkpoints/t4_round2_ledger_audit.md`，`trace.jsonl` 也多了 1 行。不是我写的，应该是并行的 verifier 或主控。(主控注: 是主控誊录 auditor 结果时写的.)

## 核对脚本与复跑方式

- **复跑了整链**，没有在原目录跑：`git clone --shared --no-checkout` 到临时目录，checkout `774ebc5`（KB tree 同为 `63f857…`）；用 rsync 把工作树的 `.work/10_tier_b_repair` 覆盖进去，排除 `work/scratch` 和 `t3_attempt*`；把副本脚本里写死的 `/Volumes/DevSSD/Project/sdtm-pedia` 全部换成副本路径，换完 grep 剩 0 处；每次跑之前删掉 errata / rules / decisions / audit_sets。
- **两次复跑**：runA 从 `pre_r2l` 台账起跑，得到 `16024ac0…`；runB 在 runA 的产物上再跑一遍，md5.txt 与 runA 完全相同。errata `b6065206…`、rules `25b9c54b…`、decisions `a3e8c8f1…`、anchorless `5523abd7…` 都等于工作树里的文件。`t3_audit_sets` 与工作树的 diff 为空；`section_coverage` 399 行去掉 ts 后差异为 0。
- **日志结果**：s0 NEW [] / BAD [] / R4 = 0；direct_hit GREEN（1029 / 1748 / 52）；writeback `ASSERT: OK`，T4 R2L 78/78；recompute GREEN。
- **登记表和清单也重放了**：从 HEAD 登记表跑 `t4_r2l_registry_fix.py`，得到 `e6f86b49…`；跑 `t4_r2l_build.py` 得到 `3e7e6eba…`，都与工作树一致。
- 变异测试只在副本里做（W1-W4、E1），做完已还原，再跑一次 writeback 仍得到 `16024ac0…`。没有运行规定不许跑的脚本。
- 脚本在 `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/4fbae0a7-da27-4851-8814-ac846216a212/scratchpad/review_r2l/`：`a_diff.py`、`b_rows.py`、`e_num.py`、`chain.sh`，副本在 `clone/`，日志在 `runA/`、`runB/`、`mut/`。

## 收尾命令输出 (摘)

```
$ git rev-parse HEAD:knowledge_base
63f857774a42cfaa71798705ad40ab51bc5e378a
$ md5 -q .work/10_tier_b_repair/work/coverage_ledger.wc.jsonl
16024ac09721cb3f8519cd68fa455196
```
`git status --short` 列出的是 writer 的未提交改动与主控的三个文件, `knowledge_base` / `archive` / `releases` 无改动 (`git diff --quiet HEAD -- knowledge_base` 通过).

## reviewer 意见后的处理 (主控记)

发现 #1 / #3 / #4 / #5 回给 writer 小修 (改完须重跑证明台账 md5 不变); #2 在 checkpoint 写明. 小修结果与 delta 核对见 `t4_round2_ledger_W.md` 末节与下面一行.

## 小修后的 delta 复审 (同一 reviewer 实例续; 主控誊录, 不改判)

**结论: PASS** (2026-11-27; 派发 / 返回时间见 `trace.jsonl` 的 `T4.R2L.REVIEW` 行). 5 项都通过; 只有 1 条 LOW.

| 项 | 结果 | 依据 (摘) |
|---|---|---|
| a) 脚本 diff | PASS, 没有夹带别的改动 | `scripts/t3/t3_errata_build.py` 只两处: 第 142-143 行新增断言 `("pdf" in e) == ("kb" in e) == (e["group"] == "registered-typo-oos")` (在 `if e["to"] != "PDF_TYPO": continue` 之前, IE 组也会被检查); 第 148 行 `if "pdf" in e:` 改为按 group 判. `scripts/t3/t3_writeback.py` 只第 592-595 行一处: 新增 `R2L_UNDECIDED`, 未判定的原子先收进 `bad`, 原循环体与原有断言没变 |
| b) 变异 (全在隔离副本里做, 每次还原) | PASS | E1 删 `ig34_p0316_a023` 的 `pdf` 键并改坏 kb token → errata rc=1 (上次这里 rc=0, 漏洞已堵上); E1b 只改坏 kb token → rc=1; E2 给范围内笔误组 `ig34_p0037_a002` 加 pdf / kb 键 → rc=1; E3 给 IE 组 `sv20_p0046_a002` 加 pdf / kb 键 → rc=1; E4 只删 oos 条目的 `kb` 键 → rc=1; W1 从 errata 里删掉 `ig34_p0037_a002` 后跑 writeback → rc=1, `ASSERT: FAIL ['T4 R2L atom not in allowed set / not decided: ig34_p0037_a002']` (可读断言, 不再是 KeyError) |
| c) 整链重跑 | PASS | 用新脚本从 `pre_r2l` 台账起跑两遍 (runC / runD), md5 相同且等于工作树: ledger `16024ac09721cb3f8519cd68fa455196` / errata `b606520637bc3c13b0f8f79dea6c81f6` / rules `25b9c54b67986b518669e8e5b57061e3` / decisions `a3e8c8f18d8cbdadcf5a3de4ecbd30d5`; writeback `ASSERT: OK`, T4 R2L 78/78 |
| d) 工作树 md5 | PASS, 与上次核的相同 | registry `e6f86b49f7daac2bad76625f243a1683` / `work/t4_r2l_relabel.json` `3e7e6eba4b2d311b7601b54d7f007248` / `evidence/checkpoints/t4_ack_lists.md` `aafe246bd44907dff30aea748d3ed084` |
| e) checkpoint 新补文字 | PASS (LOW 1) | §1 / §2.3a / §4 第 114 行 / 小修一节与核到的一致; 无 TODO, 无 Markdown 链接 |

**LOW**: `t4_round2_ledger_W.md` 小修第 2 点写 "这一处没做变异: 要构造 '清单原子不在允许集' 只能改代码" 不准 — 只改数据就能构造 (从 `work/t3_errata.json` 的 `atom_err` 里删一条 PDF_TYPO 原子, 即上表 W1), reviewer 已用它验证过. 处理: 主控在该句后加注 (不改 writer 原句), 不回 writer.

收尾: `git rev-parse HEAD:knowledge_base` = `63f857774a42cfaa71798705ad40ab51bc5e378a`; `git status --short knowledge_base archive releases` 为空; `git diff --quiet HEAD -- knowledge_base` 通过. reviewer 的临时副本在会话 scratchpad 的 `review_r2l/` 下 (不入库).
