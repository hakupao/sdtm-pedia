# 独立审查 B — 补检汇总 / 待改清单 / 给主人的一页 / 文档一致性 (原文誊录)

<!-- chain: E (plans) -->
> 审查者: `oh-my-claudecode:code-reviewer` (opus), 只读; 对象 HEAD `1df9f60`; 返回时间 2026-11-27 约 14:38 JST. 主控原样誊录 (只做了 Markdown 转义还原), 不改判. 审查者没有 Write 权限, 所以由主控落盘.
> 主控对各条的处理见 `evidence/checkpoints/t4_supp_fullcheck.md` 文末 "独立审查 B 的处理".
> 说明 (#3): 审查者认为 "协调方说明您当时回过 '可以, 我去发'" 是多写的 — 那两点在协调方消息原文里有, 是主控给审查者的 brief 里漏了; 原文已留档 `evidence/checkpoints/t4_coordinator_note_20261127.md`.

## 结论：CONDITIONAL，有 4 项 HIGH

数字层面这一轮基本可信。16 份原始结果和 `verdicts.json` 逐条对上，57 条改标和所有改后数字都复现了，工作台账 md5 没变。问题出在两处：一是总体口径和置信度的写法有缺口、有说过头的地方，二是给主人的一页里有几处与事实不符，并且多写了我拿到的确认来源事实之外的内容。另外还漏报了一条和那 4 条已登记笔误同类的原子。

## 各项结论

| 项 | 结论 | 依据 |
|---|---|---|
| A 汇总是否忠实 | CONDITIONAL | 395 条判定和计数全对，各层分列一致，原始结果行号指针 57/57 都对。但审查者写的几处 "需复议 / owner 定口径" 汇总没有转述（#8、#13）。 |
| B 总体与漏层 | CONDITIONAL | 11 层总体、扣掉 gate 2 条、C7 扣 0 都对；规则计数变化表属实。PDF_TYPO 类这一轮没覆盖，也没写明（#7）。 |
| C Q9 方案与表述 | FAIL | 置信上界合并了 gate 8 条，没有按 brief 报 65 条单独的上界（#5）。"全量指纹复验" 没说明不含 HEADING，也没说明跨 PDF 命中会自动放行（#6）。分层抽样的种子写死、池排过序，可复现，没问题。 |
| D 待改 57 条 | CONDITIONAL | 每条的指针、判定、分组、登记 id 都对，改后数字全部复现。但同一笔误 B-BE T-3 下还有一条 EXACT 原子漏列（#1）。 |
| E 给主人的一页 | FAIL | 数字全对。问题 5 条数和说法有误（#2），问题 3 的理由不成立（#4），确认来源的描述多了内容（#3），两份文档的选项不一致（#10）。 |
| F 未确认写成已确认 | CONDITIONAL | M-8、57 条改标、Q9 抽样都写成 "待主人"，没写成已定。问题在于多写了来源（#3），以及 M-4 被写成 "待追认"，和确认记录不一致（#9）。PLAN 口径注与 §000 原文一致，只省略了 U-4 的 "HEADING 21 全量"。 |
| G 其它一致性 | CONDITIONAL | `t4_ack_lists.md` 只改了 2 行，符合说明；没有 Markdown 链接，没有 TODO（"(待审)" 除外）。"其余 10 层" 算错了（#11），`relabel_pending` §2 G-TB2 一行标注错了（#12）。 |
| H 规则 B 与后果条款 | CONDITIONAL | 规则 B 归档五要素齐。后果条款没有被放宽，NOT_HOLD_R1 那条反而从 "直接改 IE" 收紧成问主人，但没写明和 brief 不同（#14）。置信上界的报法偏离了 brief（#5）。输入写的 HEAD 不准（#15）。 |

## 发现清单

| # | 严重度 | 位置 | 问题 | 依据 | 建议改法 |
|--:|---|---|---|---|---|
| 1 | HIGH | `t4_relabel_pending.md` §3；`t4_owner_decisions_round2.md:34` | 漏报同类项：`ig34_p0147_a026`（BE 例子 bs 表第 4 行，台账是 stock EXACT）也受已登记笔误 B-BE T-3 影响，KB 和 PDF 不一样，却不在 57 条里。问题 2 说 "同类的其它原子早就标成 PDF 笔误"，对 B-BE T-3 不成立：p147 没有任何 PDF_TYPO 原子。 | `ig34_p0147.txt:31` PDF 印 `298B1-1R0`；`BE/examples.md:125` KB 是 `298R1-1R0`。登记 B-BE T-3 的说明写 "bs r3-4, 2 格"。这条不在 pre_existing 里，因为原子抽出来的文字本来就和 KB 一样，指纹检查会通过。 | 补进清单（变成 58 条），重算数字。另外说明 PRE_EXISTING 这一层的取法看不见 "原子文字 = KB 修正值 ≠ PDF" 的情况，建议按 "KB 写正确值" 的登记逐条反查同页的 EXACT/EQUIV 原子。 |
| 2 | HIGH | `t4_owner_decisions_round2.md:85-89` | 问题 5 说 "第 74 页的 3 条"，台账里 sv20_p0074 共 14 条都配到了 SDTMIG `ch10`：a001 是 PARTIAL，a002–a013 是 EXACT，a014 是 EQUIVALENT。同一段先说 "不影响任何一道闸"，下一句又给出 99.2651→99.2649 的变化，自相矛盾，因为 G-TB3 是按整本台账算的。U-8 被说成 "同类问题"，但 U-8 是范围外的已登记笔误，不是跨文档错配。 | 脚本 c_pop.py / c_xdoc.py 列出了这 14 条；`t4_coverage_decomp.py` 的分子分母是全台账。 | 改成 14 条，重算（14 条都改 IE 时 U-1 B = 9846/9919 = 99.2640%，在 1A2A 基础上算）。删掉 "不影响任何一道闸"，改写成 "不在 G-TB1/2 范围内，但会进 G-TB3 的分子分母"。"同类" 改为 "上一轮范围外的 4 条也改了标签"。 |
| 3 | HIGH | `t4_owner_decisions_round2.md:107`；`t4_user_decisions.md:2` 状态行 ③ | 描述上一轮确认来源时多写了内容："协调方说明您当时回过 '可以, 我去发'，时间线吻合" / "依据 = 时间线 + 主人对协调方说过 '可以, 我去发'"。我拿到的协调方说明里没有这两点。其余几点（发在上一任主控会话聊天里、记录人、别处没再看到原文、以记录为准往下走、局限保留、由下一次总闸判断）一致。 | 和本次任务里 "关于确认来源的事实" 逐句对照。 | 删掉这两处，或者先请协调方确认原话再写。确认之前算待核，不能写成事实。 |
| 4 | HIGH（把握中等） | `t4_owner_decisions_round2.md:62`；`t4_supp_fullcheck.md:84` | 问题 3 说 "SDTMIG 这边没有 v2.0 那种结构性原因"，不成立。范围内的 stock SDTMIG 旧 EQUIVALENT 里有 16 条非 HEADING 原子，台账只指向 v2.0 的 `model/` 文件，这正是这次查出的跨文档 / 跨表错配类型，而且 65 条样本一条都没抽到。例子：`ig34_p0195_a020/22/24`、`p0196_a001/2/9/10`（LB 通用规格）→ `model/02`；`ig34_p0364_a014-16`（FA）→ `model/02`；`p0079_a016`、`p0080_a003/a009` → `model/02/03`；`p0441_a004/5` → `model/05`。 | 脚本 c_xdoc 片段（见下）。 | 删掉这句。把这 16 条单列成一层全检（约 1 个审查实例），并写进问题 3 的选项。 |
| 5 | MEDIUM | `t4_supp_fullcheck.md:84`；round2 `:60-67` | Q9 brief 第 33 行写死的是报 "65 抽 0 错及其置信上界"。实际报的是合并 gate 对照层 8 条后的 73 条 → 4.0%。65 条单独算是 4.5%。那 8 条来自另一个抽样框（gate 对照层），分层也不按比例；fullcheck 写了 "假设简单随机"，给主人的一页没写这个前提。 | 1−0.05^(1/65) = 0.04504；1−0.05^(1/73) = 0.0402；1−0.05^(1/223) = 0.0133。 | 两个上界都报，并在给主人的一页加上 "近似：按简单随机计；分层抽样，且合并了不同来源的样本"。 |
| 6 | MEDIUM | `t4_supp_fullcheck.md:74-76`；round2 `:58`；PLAN §9 Q9 | 总体都不含 HEADING，但没写明：范围内 stock HEADING 有 EXACT 149、EQUIVALENT 167（ig34 162 / sv20 5），既不在指纹复验里，也不在 Q9 里。sv20 的 5 条里有 3 条指向 SDTMIG `ch01/ch02`。`t3_direct_hit.py`（`anchor_ok`）遇到 "另一份 PDF 的文件" 会自动放行，所以 "全量指纹复验" 不检查文字落在哪份文档里（这一点 Q9 包 2 的审查者已经点出）。另外 fullcheck 写 1753，给主人的一页写 1758（指纹脚本的 n_stock 多算了 5 条在决策表里的），两处没解释为什么不同。 | c_pop / c_exact 的输出；`t3_direct_hit.py` 中 `x["atom_type"]=="HEADING"` 被跳过；`t3_common.py:176-177`。G-TB1 的定义本身就是 "非 HEADING"，所以排除是有依据的，但必须写出来。 | 三处都写明 "不含 HEADING（G-TB1 定义如此）；指纹复验只查文字和本文档内的节锚点，跨 PDF 的命中不判对错"。1753 和 1758 统一，或注明差别来源。sv20 那 5 条 HEADING EQUIV 建议补查。 |
| 7 | MEDIUM | 本轮所有文档都没提 | attempt 1 §5 点名的 "ATOM_ERR/PDF_TYPO 合计补抽到 ≥30" 和 attempt 2 D 项写的 "部分关（仅 C7 38）"：ATOM_ERR 这一轮查得很多（C7 38、triage 74、K4 2），但 PDF_TYPO 149 条里只有 gate 5 条 + 人工样本 2 条，142 条一条没查，而且 PDF_TYPO 在 U-1 B 口径下算覆盖。round2 `:9` 的 "这次把它们全部查了一遍" 容易被理解成这一项也补完了。 | 脚本 b_pop 的输出：`PDF_TYPO 149 in gate 5 … unchecked 142`。 | 在 fullcheck 和 HANDOFF 里明写这一项仍开着，或者另做一次 PDF_TYPO 分层补抽（K3b 61 / S1-R2 53 / writer-Tn 35）。 |
| 8 | MEDIUM | `t4_supp_fullcheck.md` §5 | 审查者提出的 "需复议" 汇总没转述：Q9 包 1:50（Q19–Q26 标题加了域代码后缀；按 brief 的 TOC 规则 "标题文字不同 → NOT_HOLD"，若从严这 8 条要复议，可以引 U-10① 的先例）；补检包 2:58（§6.4 RELSUB / §6.5 DR 的五列表 "需要 owner 定口径"）。 | 原始结果的对应行。 | §5 补上这两条，并写明处理依据（U-10①；§6.4/§6.5 在范围外）。 |
| 9 | MEDIUM | `t4_ack_lists.md` 第 119 行、`t4_ack_lists.py` MAIN_CTRL；`t4_user_decisions.md` §000b 标题 | M-4 被写成 "待主人追认"，但 `t4_owner_confirmation.md` 记的是追认了 M-1..M-7，给主人的一页 `:76` 也说 M-5 "按记录已追认"。§000b 标题还写着 "待主人追认"，对 M-1..M-7 已经过时。 | 三处文字互相矛盾。 | 改成 "M-4（按 `t4_owner_confirmation.md` 记录已追认）"。§000b 标题注明 M-1..M-7 已按记录追认，只有 M-8 待追认。 |
| 10 | MEDIUM | round2 `:26-30` 与 relabel_pending `:11-14` | 选项不一致：给主人的一页里问题 1 的 C 是 "只改 51 条、2 条另议"，清单里的 C 是 "其它"。问题 1 把 51 条 R1 类和 2 条目录条目捆在一起，但选项 A 的理由（与 R1 一致）只适用于那 51 条。问题 2 选项 B 的 "总闸会再点名" 是预测，带诱导。"未单独算"（问题 1=C、2=A 那一行）其实可以算出来：strict 95.7423%、内容 90.6413%。 | 文档对照；脚本 d_recalc 的输出。 | 两份文档的选项统一；目录条目单独成一问；把预测性的话删掉或另起一句标成 "主控判断"；补上算好的数字。 |
| 11 | LOW | fail 文件 `:8`；HANDOFF 新节；audit_matrix 补检行 | "其余 10 个非空层 / 10 层通过" 错了，应为 9 层（FIG、ATOM_ERR、RELOCATE、6 条规则；LOCATE 那层是空的）。fullcheck §4 的 145 条 / 9 类是对的。 | 层表。 | 改成 9。 |
| 12 | LOW | `t4_relabel_pending.md:24` | 这一行标的是 "G-TB2 (范围内)"，但给的 `157/174` 是字面口径；范围内口径是 174/174（`_progress.json` 和给主人的一页都这么写）。 | 文档对照。 | 改标注，或两个值并列。 |
| 13 | LOW | fullcheck §5 | 标签级别（原子抽错、KB 对）只列了补检 #3/#4，实际 PRE_EXISTING 的 HOLDS 里还有 #12–16、#19–21 等多条。另有几条审查者的观察没有转述：补检包 3:54（p69、p77 原子）、Q9 包 3:61（`sv20_p0053_a018` 列错位）、补检包 4:59（CE/HO 规格附加 NCI C-code，没有 KB note）。 | 原始结果。 | 补全，或写 "另见原始结果某某行"。 |
| 14 | LOW | relabel_pending `:5`；round2 问题 1 | Q9 brief 写死的后果是 "NOT_HOLD_R1 → 台账改 IE（R1 是用户已 ack 的类别）"，实际改成了请主人定，这是收紧不是放宽，但没写明和 brief 不一样。引用的 "PLAN §3.1 B5" 本义是域规格表行（452 条），不是一般 IE 的规定。 | brief `:31`；PLAN `:46`。 | 加一句说明为什么偏离 brief，并改正引用。 |
| 15 | LOW | fail 文件 `:6` | 输入写 "HEAD `d46f8af`"，但补检 04:52Z 派发时 HEAD 已经是 `c555bd8`（13:47 JST）。KB 树和台账 md5 相同，结论不受影响。 | trace.jsonl；`git show c555bd8`。 | 改成 `c555bd8`。 |
| 16 | LOW（待核） | round2 `:109` | 说 "EG 例 3 … U-9(c) 已定接受现状"：U-9(c) 原文是 "残余 230 行"，现在残余文件有 1091 行；EG 第 62–87 行的类型是 `table_elision`（共 26 行），无法确认当时接受的 230 行里包括它们。另外 `t4_supp_fullcheck.md:29` 说 LOCATE 是 "在 T2 已全部定位"，实际是 28 条 `ruling:LOCATE-LB` 在分批时转成了 REAL_GAP。 | 残余文件统计；`t2_batch_table.md:18`。 | 先核 230 行指的是哪些行再下结论；LOCATE 的原因改成照实写。 |

## 我写的核对脚本

全部在 `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/4fbae0a7-da27-4851-8814-ac846216a212/scratchpad/review_b/`，只读仓库，都用 `python3 -I` 在 `.work/10_tier_b_repair` 下运行。

- **`a_parse.py`**：直接解析 16 份原始结果的表格（兼容各文件列的差异、"同上" 层名、"HOLDS (TOC)" 写法），和 `verdicts.json`、两份样本逐条比对。
  - 输出：补检 203 = HOLDS 171 / HOLDS_AS_EQUIV 30 / NOT_HOLD 2；Q9 192 = HOLDS 141 / NOT_HOLD_R1 49 / NOT_HOLD 2；不匹配 0，样本缺漏 0，层名差异 0。
- **`d_recalc.py`**：按 `t4_coverage_decomp.py` 的同一公式自己实现，在内存里改标。
  - 现状：strict 9567/9986 = 95.8041；mapped 99.3561；U-1 B 9913/9986 = 99.2690；内容 90.6948。
  - 问题 1=A、2=A：strict 9510/9933 = 95.7415；mapped 99.3523；U-1 B 9860/9933 = 99.2651；内容 90.6394。
  - 问题 1=A、2=B：95.7817 / 99.2651 / 90.6433。问题 1=C、2=A：95.7423 / 9862/9935 = 99.2652 / 90.6413。只做问题 2=A：95.7641 / 99.2690 / 90.6909。在 1A2A 基础上加 p74 那 3 条：99.2649。
  - 57 条的分组、现标签和原始结果行号全部对上。
- **`c_pop.py` / `c_exact.py`**：重算 stock 总体。不含 HEADING 时 4968 = EXACT 1753 / EQUIVALENT 2334 / IE 881，EQUIVALENT = sv20 127 + ig34 2207，分型和脚本一致。含 HEADING 时 5430，其中 HEADING 462。指纹脚本的 n_stock = 1758。
- **`c_xdoc.py`**：找跨文档指针（得到 #2 的 14 条、#4 的 16 条、#6 的 sv20 HEADING 3 条）。
- **`b_pop.py`**：独立重算补检各层总体（与 `supp_population` 一致，合计 203）；规则计数用 `git show 3a24a1c` 的决策表比对，T1-two-agent→+T2-rework 14 条、IE-ack→live-hit 1 条，属实；PDF_TYPO 149 条里有 142 条没查过。
- **`d_typo_sib.py`**：按登记表反查同页的 EXACT/EQUIV 原子，这是粗筛，人工确认后得到 #1 的 `ig34_p0147_a026`。

## 收尾状态

```
$ git status --short
 M .work/10_tier_b_repair/trace.jsonl
?? .work/10_tier_b_repair/scripts/t4/t4_gate_prerun.sh
$ git rev-parse HEAD:knowledge_base
63f857774a42cfaa71798705ad40ab51bc5e378a
$ md5 -q .work/10_tier_b_repair/work/coverage_ledger.wc.jsonl
60729f7b64b7c1dfaf2174e394f6dd9c
```

`git status` 里那两处改动不是我做的：我只在 scratchpad 里写过文件，没改过任何已跟踪文件。会话开始时 git status 是干净的，所以这两处是审查期间别处写进来的，需要协调方确认来源。KB 树和工作台账 md5 都和预期一致。

(主控注: 那两处是主控在审查期间自己做的 — 追加 trace 行、新写预跑脚本.)
