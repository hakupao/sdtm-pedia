# T4 问题 A 改台账 (R3L) — 独立 reviewer (结构审查)

<!-- chain: E (plans) -->
> 状态: **PASS** (2026-11-27). 审查者 `oh-my-claudecode:code-reviewer` (opus), 对仓库工作树只读, 在隔离副本里复跑; 对象 = 工作树里 writer 改后的台账 (md5 `438098704becc84eda01a925b80defaa`). 下面是审查者回复正文, 由脚本从会话记录里原样取出 (主控未改一字; 规则 D). 派发 / 返回时间见 `trace.jsonl` 的 `T4.R3L.REVIEW` 行. 审查者提到的临时目录在会话 scratchpad 下, 不入库.

---

**R3L 结构审查结论: PASS**

这批改动里没有 HIGH,也没有 MEDIUM,只有 5 条 LOW 和 1 条提示,见第 2 节。A-H 每一项都是我自己在隔离副本里跑出来的,没有用 writer 的数字。

隔离副本在 `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/4fbae0a7-da27-4851-8814-ac846216a212/scratchpad/review_r3l/repo`。它是用 rsync 复制的整个仓库,去掉了 `web/` 和 `work/scratch/`,之后补拷了 `work/scratch/t3`。副本里有 48 个脚本把仓库绝对路径写死在代码里,我先全部改成指向副本,改完后 grep 剩余 0 处,确认链条不会写回原目录。

## 1. A-H 逐项

| 项 | 结果 | 依据 / 命令 / 关键输出 |
|---|---|---|
| **A 改动集** | PASS | 用我自己写的 `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/4fbae0a7-da27-4851-8814-ac846216a212/scratchpad/review_r3l/cmp.py` 按字节逐行比较。两边各 12492 行,`pdf_atom_id` 序列完全相同。标签变化恰好 4 行,都是 PDF_TYPO → EXACT:第 10132 行 a006、10133 行 a007、10134 行 a008、10153 行 a010。这 4 行只变了 `verdict` 和 `matched_by` 两个键,其它行 0 变化。`ig34_p0293_a038` 仍是 PDF_TYPO(规则 K3b-registry,登记 B-MK T-2)。备份 md5 = `16024ac09721cb3f8519cd68fa455196`,与 `git show HEAD:` 的台账 md5 相同。 |
| **B 可复现** | PASS | 准备:在副本里把所有派生文件、keep 清单 `git checkout HEAD`,删掉 `t4_r3l_relabel.json`,然后跑两次 `t4_r3l_build.py`。两次都得到 relabel `1dcefad3…`、keep `1e99f101…`,和工作树一致,说明这一步幂等。<br>整链(writer 的 `run_chain.sh`,只把路径换成副本)跑了 runA / runB / runC 三遍,三遍的 `md5.txt` 完全相同:台账 `438098704becc84eda01a925b80defaa`、errata `b6065206…`、t2s `33ef2fe0…`、fp_expected `e7df6ce0…`、keep `1e99f101…`、rules `1096bec2…`、decisions `10a925c9…`。<br>和工作树比:rules、decisions、`t3_audit_sets/` 全部文件、anchorless、`t3_t4_k3b_out_of_scope.txt`、errata、keep、relabel,以及重生成的 `t4_ack_lists.md`(`18a2981c…`)的 md5 都相同。`section_coverage.wc.jsonl` 的 md5 不同,但 399 行里不同的只有 `aggregated_by.ts`(运行时间戳),其它字段一致。 |
| **C 机制** | PASS | 读的是 `git diff scripts/` 和 `t3_writeback.py:486-541, 623-625`。<br>① 脚本里搜 `p041` / `a006` / `TD T-` 等,没有这 4 个 id,只命中第 213 行一个无关的 `p0196_a006`;清单只来自 `work/t4_r3l_relabel.json`。<br>② 第 495 行在 `K3B.pop` 之前断言该原子当前的 K3b 触及等于 `k3b_drop`;第 492 行断言 keep 清单里 `t4_r3l_drop` 的集合等于清单。<br>③ diff 里没有删除或修改任何原有 assert / `bad.append`。唯一改动的条件是第 538 行 `verdict != old or i in R3L`:它只会让清单原子被强制重写,第 573 行"未触及行逐字节相同"的检查仍以 `new_rows` 为准,没有被放宽。<br>④ 相邻原子标签不变:a009 仍是 PDF_TYPO(writer-Tn-registry,登记 S-TDM TD T-1),a013 仍是 PDF_TYPO(K3b-registry,登记 S-TDM TD T-4,原因 `b:kb-side-not-in-window`),改前改后一样。<br>⑤ `git diff` 登记表为空,md5 = `e6f86b49…`。<br>判定路径:这 4 条走现有 `decide()`,K3b 分支(第 264 行)之后落到第 282 行的 `live-hit`。第 624 行断言规则必须是 `live-hit`、终态等于 `to`、原子不在 K3B、已被重写。 |
| **D 4 条 EXACT 成立** | PASS | 从 `pdf_atoms.jsonl` 取 verbatim,空白归一后,4 条都逐字出现在 `knowledge_base/domains/TD/examples.md`:a006-a008 在第 40 行,a010 在第 50 / 102 / 167 行。<br>PDF 文本层:a006-a008 对应 `ig34_p0412.txt:14-15`;a010 对应 `ig34_p0413.txt:21`(Ex2 表头,`TDTGTPAI` 拼写正确),去掉表格竖线后匹配。<br>登记的两处笔误都不在这 4 条里:"assessments.." 出现在 `ig34_p0412.txt:17`,即 a009;"TDTGPAI" 出现在 `ig34_p0414.txt:29`,即 Ex3 表头 a013。4 条的文本里两个 token 都是 False。 |
| **E 验收数字** | PASS | 终态计数 PDF_TYPO 174 → 170,EXACT 4706 → 4710。其余类别不变:ATOM_ERR 197、EQUIVALENT 3949、ERROR 62、FIGURE 11、IE 2559、MISPLACED 197、PARTIAL 637。<br>`t4_coverage_decomp.py`(在副本里跑):strict 9493/9933 = 95.5703%,mapped 9493/9555 = 99.3511%,U-1 B 9860/9933 = 99.2651%,内容 8659/9555 = 90.6227%,与 `scenarios.json` 最后一项逐字相同。<br>recompute:范围内 174 节残留 0,G-TB1 174/174,G-TB2 157/174。<br>direct_hit:TB(all) = 1033,stock = 1748,pre_existing 52,miss / k11 / anchor / unexplained 全为 0,结果 GREEN。<br>s0:NEW [],BAD [],R4 = 0。<br>ack 清单:PDF_TYPO 节 170 行,决定来源合计 118 + 22 + 19 + 6 + 4 + 1 = 170;"未归因" 出现 0 次;这 4 个 id 在文件里出现 0 次。<br>`check_links.py` live docs = 42。 |
| **F 新断言有效** | PASS | 共做了 7 个变异,全部在副本里:<br>① a010 的 `k3b_drop` 改成 T-1:rc=1,AssertionError "touch != listed"。<br>② 从清单删掉 a006:rc=1,第 492 行断言触发。<br>③ 在单独解出的 KB 副本 `kbm/` 里改掉 a008 那句:direct_hit rc=1,`tb_exact_miss ['ig34_p0412_a008']`,RED。<br>③b 再把三处表头改成 `TDTGXXXX`:miss 变为 a008 和 a010,RED。<br>④ 改副本 KB 里 a008 那句后跑 writeback:rc=1。K3b c' 已经不再触及这条,于是第 495 行断言先报错。<br>⑤ `k3b_drop` 改成多一个登记(超集):rc=1。<br>⑥ 在 errata 的 `pending_user` 里加 a010:rc=1,`ASSERT: FAIL ['T4 R3L atom not live-hit EXACT: ig34_p0413_a010 EXACT pending_user-residual …']`。这说明第 624 行查的是规则,不只是标签。<br>每次变异后都还原并复跑。runC 与 runB 的 md5 相同;做完 ⑥ 再还原跑一次 writeback,台账、errata、relabel、rules、decisions 的 md5 都回到原值。 |
| **G checkpoint 与实际一致** | PASS(有 1 条 LOW) | checkpoint 里的 md5、计数、diff 行数、anchorless 507 → 511(新增的正是这 4 条)、audit_sets(K3b-registry -4、live-hit +2)、两节 aggregate 变化(§7.3 和 §7.3.2 都变为 MOSTLY_COMPLETE)都与我核到的一致。没有 TODO / 占位,没有 `](` 形式的 Markdown 链接。小问题是 §6 编号顺序乱了(L-4)。 |
| **H 冻结区** | PASS | `git status --short knowledge_base archive releases` 为空;`HEAD:knowledge_base` = `63f857774a42cfaa71798705ad40ab51bc5e378a`;`git diff --quiet HEAD -- knowledge_base` 通过。 |

## 2. 发现清单

都不阻塞 PASS。

- **L-1** `t3_writeback.py:563-568`:writeback 先写台账再做最后的断言。第 624 行那条 R3L 断言失败时,改过的台账已经落盘(变异 ⑥ 实测)。这是 R2L 之前就有的设计,不是本批引入的,但新断言同样受影响。建议:先写到临时文件,断言通过后再 rename。
- **L-2** `t3_writeback.py:528`:`before="PDF_TYPO (K3b-registry, keep_k3b)"` 是写死的字符串,没有从改前台账或 keep 条目取值核对。对这 4 条是对的,以后复用这段代码时可能失真。
- **L-3** `t3_writeback.py:491-495`:新守卫用的是 Python `assert`,在 `-O` 下会失效。这和既有代码风格一致,链条也是用 `-I` 跑的,实际风险低。另外,如果 `k3b_drop=[]` 且原子没有被触及,第 496 行 `K3B.pop` 会报 KeyError:退出码仍非 0,但报错信息不直观。
- **L-4** checkpoint §6 的条目编号是 1, 2, 3, 4, 6, 5。
- **L-5 提示** `t3_build_keep.py` 如果被重跑,会抹掉 `t4_r3l_drop` 标记。好在第 492 行断言会让 writeback 直接失败,不会悄悄回退。`t4_gate_prerun.sh` 的 md5 清单里还没有本批新增的文件,writer 在 §6 第 6 条已经提出,由主控决定。
- **提示** 整链里 fp_head / fp_all 的 rc=1(RED)。writer 改动前的基线 run0 里也是同样的 RED,日志与 writer 的逐字一致,是以前就有的,不是本批造成的。

## 3. 收尾检查

- KB 树哈希 `git rev-parse HEAD:knowledge_base` = `63f857774a42cfaa71798705ad40ab51bc5e378a`,`git diff --quiet` 通过。
- 工作树台账 md5 = `438098704becc84eda01a925b80defaa`。
- `git status --short` 与审查开始时的快照 diff 为空:文件集合没有因我而变。我没有在原目录跑任何会写文件的脚本,只跑了只读的 `check_links.py`。所有临时文件都在 `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/4fbae0a7-da27-4851-8814-ac846216a212/scratchpad/review_r3l/` 下。

---

## reviewer 意见后的处理 (主控记, 不改判)

- HIGH 0 / MEDIUM 0. 5 条 LOW 与 1 条提示都不回 writer 修 (修它们要再动 `t3_writeback.py` 并重跑整链, 而结果已由 reviewer 三遍复跑钉住): L-1 (先写台账后断言) 与 L-3 (用 `assert`) 是 R2L 之前就有的设计, 记为已知局限; L-2 (写死的 `before` 字符串) 对这 4 条属实, 记为以后复用这段代码时要改; L-4 (checkpoint §6 编号 1, 2, 3, 4, 6, 5) 不改 writer 原文, 在此说明; L-5 (`t3_build_keep.py` 重跑会抹掉 `t4_r3l_drop` 标记, 但 writeback 断言会直接失败) 写进 `HANDOFF.md`.
- writer checkpoint §6 第 1 条 "同一模式可能还有别的多标原子, 本批没查": 主控注 — R2L 之前的 149 条 PDF_TYPO 已由独立审查者逐条看过 (总闸样本 5 + 第二轮 45 + 第三轮 99, 查出的就是这 4 条 + 1 条判不了的); R2L 新进入 PDF_TYPO 的 25 条本身来自审查者逐条判的 TYPO_AFFECTED. 所以现存 170 条 PDF_TYPO 每一条都被独立审查者看过, 不需要再做一次全量排查; 这是事实陈述, 不是新的判定.
- writer 提的 `t4_gate_prerun.sh` md5 清单: 主控已补 (`coverage_ledger.wc.pre_r3l.jsonl` / `t4_r3l_relabel.json` / `t3_k3b_out_of_scope_keep.json`).
- 整链里 fp_head / fp_all 的 RED 是既有状态 (reviewer 已核对改动前的基线 run0 同样为 RED), 不是本批造成的.
