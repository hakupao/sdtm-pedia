# 独立 delta 复审 C — 第二轮补检 / 待改清单 / 给主人一页第 2 稿 (原文誊录)

<!-- chain: E (plans) -->
> 审查者: `oh-my-claudecode:code-reviewer` (opus, 新实例), 只读; 对象 HEAD `1b30197`; 主控登记其返回的时刻 = trace `T4.GAP.REVIEW_C` 的 `subagent_done` 行 (2026-11-27T06:09:23Z). 主控原样誊录 (只做了 Markdown 转义还原), 不改判.
> 主控对各条的处理见 `evidence/checkpoints/t4_supp_fullcheck.md` 文末 "delta 复审 C 的处理". **处理后的第 3 稿没有再送审** (如实); 留给总闸 attempt 3 一并看.

# 独立 delta 复审：T4 第二轮补检、待改清单与给主人一页第 2 稿（HEAD `1b30197`）

**整体结论：CONDITIONAL，要求修改。HIGH 4 条（都已用证据核过）、MEDIUM 5 条、LOW 13 条。**

数字层面这一轮可信：
- 175 条第二轮判定和 `verdicts.json` 逐条对上，0 不一致。
- 三个总体、72 条待改清单、9 行各选法数字全部独立复现。
- 给主人一页里列的数字全部对上。

问题出在三处：
- **给主人一页有事实错**：说标题类原子 "不在任何一道闸的范围内"；问题 6 选项 A 的理由不成立；问题 8 的现状说错了。
- **范围外漏了一类**：与 U-8 同类、应改标 PDF_TYPO 的范围外原子，这次没有筛也没有报给主人。
- **转述不全**：第二轮审查者写明 "交主控酌定 / 留主控决定" 的几条附注，汇总里没有转述。

范围内我没找到应改标却漏掉的原子，但我的筛法覆盖有限，所以这一项写成待核，不写 PASS。

## 各项结论

| 项 | 结论 | 依据 |
|---|---|---|
| A 上次 16 条的处理 | CONDITIONAL | #1、#2、#4、#5、#7、#9、#10、#11、#12、#14、#15 已处理到位。#3：给主人一页第 134 行与 `t4_user_decisions.md` 状态行 ③ 的每一句，都能在协调方留档或 `t4_owner_confirmation.md` 里找到依据，没有超出。唯一的局限是该留档是写作者自己誊录的。#6 只做了一半：范围内 sv20 标题类 EQUIVALENT 共 5 条，只审了 3 条，另 2 条没交代。#13 这一轮的新附注又没转述全（见 M1）。#16 改出了新的数字错（见 H3）。 |
| B 第二轮汇总是否忠实 | CONDITIONAL | 计数全部吻合：XDOC 24/3；TYPO_SIB 10/53；TYPO_SIB2 5/35；PDF_TYPO 45。"样本外发现" 基本转述了，但标签级别的附注缺了 5 个包里的条目（M1）。 |
| C 取法有没有漏 | CONDITIONAL（ii 待核） | (i) 范围内 57 条（EQUIVALENT 55 / EXACT 2），已审 30、本轮 27；范围外 146 条（PARTIAL 113 / EQUIVALENT 21 / EXACT 12），p74 14 条。全部复现，与 `round2_population.json` 一致。(iii) PDF_TYPO 149 条、未审 144 条（S1-R2 52 / writer-Tn 33 / K3b 59），按 seed 20261132 重抽得到的样本与文件完全相同。(ii) 范围内没找到反例；范围外确认漏了 6 条（H4）。筛法本身有盲区（M5）。 |
| D 待改 72 条 | PASS | 72 行的现标签与台账一致；原始结果文件:行都含该 atom，判定也对得上。17 个登记 id 都存在，与问题 3 的清单不多不少。9 行数字逐一复现：三组都改 = 9860/9933 = 99.2651%；strict 95.5905%；内容 90.6247%；"+ p74 14 条" = 9846/9919；"+ 146 条" = 9714/9787。只有一处 LOW：L3。 |
| E 给主人一页第 2 稿 | FAIL | 数字全对：570、72、9+10、8 行表、65/16/81、4.5/4.0/1.4%、45+5、6.4%、99、316、11→8+3、146/113/21/12/14、99.2640%、99.2541%。但事实陈述有错：H1、H2、H3；还缺一类应问主人的事：H4。 |
| F 未确认写成已确认 | PASS（附 LOW） | M-8、72 条改标、各处抽查、问题 6-9 都写成 "待主人"。M-1 ~ M-7 "按记录已追认" 与 `t4_owner_confirmation.md` 一致；M-5 = "M3 换靶"，在该记录列的例子里。问题 1 的 R1 对得上 `t1_user_ack.md:4`。问题 2 的 a009 / a010 都是 IE，`approved_by = user-ack-2026-05-12-P6-T2`。U-8 确实是改了标签的。U-10④ 在登记表里写作 "补登记"。小问题见 L6、L12。 |
| G 其它一致性 | CONDITIONAL | 72、19、51、2、570、175、27、103、45、146、14 在 HANDOFF、`_progress.json`、PLAN、`audit_matrix.md`、失败归档里一致。没有 Markdown 链接；没有 "t4_owner_pending" 或 "(待写)"。但有一处改编号后遗留的旧指针（L1）。`audit_matrix.md` 里审查 A 的 "MEDIUM 1 / LOW 11" 属实。 |

## 发现清单

### HIGH

**H1　标题类原子其实在 G-TB3 的范围内**
- **位置**：`t4_owner_decisions_round2.md:92`、`:73`
- **问题**：问题 6 写 "标题类原子不在任何一道闸的范围内"；问题 4c 写 "闸的定义本来就不含标题"，选项 A 的理由是 "(闸定义不含标题)"。这两句都不对。
- **依据**：G-TB3 按整本台账算，不筛原子类型（`t4_coverage_decomp.py` 没有 atom_type 过滤；`PLAN.md:103`）。台账里标题类原子的现标签是 EXACT 367 / EQUIVALENT 275 / PARTIAL 77 / MISPLACED 35 / IE 121，全部计入 U-1 B 的分子分母。只有 G-TB1 明确是 "非 HEADING"（`PLAN.md:101`）。
- **建议改法**：改成 "不在 G-TB1（节级残留）范围内，但计入 G-TB3"。问题 6 若从严，补上会动 G-TB3 的说明和数字；问题 4c 选项 A 的理由也照此改。

**H2　问题 6 选项 A 的理由不成立**
- **位置**：`t4_owner_decisions_round2.md:96`
- **问题**：括注 "节号在各节的小标题里已有" 不成立。
- **依据**：
  - XDOC 审查者原文写了 SE 三个文件都没有带 5.3 的标题、OI 三个文件都没有 9.2（`pack_xdoc.md` R2、R24）。
  - 我用 `grep -n "5\.3\|9\.2"` 查 `SE/*.md` 和 `OI/*.md`，0 命中，非标题行里也没有。
  - 我对每个域目录用 `grep -h "^#"` 检查 "标题里有没有任何 `N.N` 节号"：64 个目录里有 44 个完全没有。
- **建议改法**：删掉这句。照实写 "多数域文件里任何标题都不带 PDF 节号"。

**H3　问题 8 有两处事实错，还漏了同类的一行**
- **位置**：`t4_owner_decisions_round2.md:112`、`:116`；`t4_supp_fullcheck.md:117`
- **问题与依据**：
  - 第 116 行说 "已知有 19 条原子因此只算 '等价' 而不是 '逐字'"。台账里这 19 条（p191 的 HOLDS_AS_EQUIV）现标签全部是 EXACT；审查者认为应降为 EQUIVALENT，但主控决定不改（§2.2 "其余 26 条…不改"）。
  - fullcheck 说 "这 26 行在残余清单里归类 `table_elision`"。实际残余清单里 EG 只有 25 行（62、64-87；63 是表格分隔线），第 26 行是 `RE/examples.md:15`。这一行同样是表头用 `...` 表示省略列，问题 8 没有提到它。
- **建议改法**：
  - 第 116 行改为 "这 19 条现标 '逐字'，按定义应为 '等价'，记标签级别后续项"。
  - 数字改为 "EG 25 行 + RE 1 行"。
  - 问题 8 把 RE:15 并进来，或者单列。

**H4　漏报范围外的已登记笔误同类原子（U-8 同类）**
- **位置**：`t4_owner_decisions_round2.md` 问题 7（:99-108）；`t4_supp_fullcheck.md:96-97`、`:103`
- **问题**：TYPO_SIB / TYPO_SIB2 只取了范围内。范围外同类原子既没有筛，也没有报给主人。可是上一轮 U-8 正是把范围外的 4 条已登记笔误改成了 PDF_TYPO（`t4_user_decisions.md:20`、`:39`）。
- **依据**：我在文本层加登记表上确认了 6 条（没看渲染页）：
  - `ig34_p0083_a020`（EXACT）：原子文字就是 PDF 的 `BIRTHDTC`；KB `SE/examples.md:79` 写 `BRTHDTC`；登记 S-SPREL SE T-1 写的是 "p82-84"。它的姊妹原子 `p0082_a025` 在 U-8 里已经改了标签。
  - `ig34_p0304_a026`、`a027`、`a028`、`a029`（EQUIVALENT）：PDF p304 第 29、32、35、38 行印 `OCCULAR`；KB `OE/examples.md:142-145` 写 `OCULAR COMFORT`；登记 B-OE T-2 "×4"。
  - `ig34_p0316_a023`（EQUIVALENT）：PDF p316:46 印 `laterallity`；KB PE spec 写 `laterality`；登记 S-FND PE T-1。
  - 用写作者的 TYPO_SIB 筛法去掉范围限制后重跑，范围外得到 TYPO_SIB 类候选 36 条（EXACT 18 / EQUIVALENT 18），外加 TYPO_SIB2 类 36 条。其中 `p0083_a020` 和 `p0316_a023` 这个筛法本身就筛不出来。
- **建议改法**：对范围外按同一口径和本条的补充启发式各跑一遍，交独立审查确认。确认后在给主人一页里与问题 7 并列成一问（引 U-8 先例），并给出各选法的数字。

### MEDIUM

**M1　第二轮的标签级别附注没有转述全**
- **位置**：`t4_supp_fullcheck.md:132`
- **问题**：只列了 `pack_sib_2` 的 8 条，下列附注都缺：
  - `pack_sib_1`：R34、R43、R50
  - `pack_sib2_1`：S8、S10、S15、S17、S19（审查者原话 "S8…交主控酌定"）
  - `pack_sib2_2`：S21、S22、S23、S27（审查者原话 "留主控决定是否进入标签级别后续项"）
  - `pack_sib_3`：`p0147_a024` / `a025` 原子抽错
  - 我另外发现一条：`ig34_p0280_a045`（EQUIVALENT，未审）原子写 `DYIDRGX_A`，PDF p280:59 和 KB `PC/examples.md:293` 都是 `DY1DRGX_A`，属于原子抽错、KB 正确。
- **影响**：给主人一页 `:135` 写的 "约 60 条" 也会跟着变。
- **建议改法**：补全，或者写明 "另见各原始结果文件的附注段"，再重算 "约 60"。

**M2　问题 9 第 1 处 "KB 都是照 PDF 原样录的" 不准确**
- **位置**：`t4_owner_decisions_round2.md:121`
- **问题**：KB 的 §6.6 表没有 Notes 列，p69 那句话 KB 根本没收；KB 只有 p50 版本，在 04:42。
- **依据**：`t4_q9_raw/pack_5.md:16`、`:44`、`:62`。审查者还提醒过："若后续给 §6.6 表补 Notes，需先定此处口径"。
- **为什么定 MEDIUM**：措辞不准，但不改变选项的含义。
- **建议改法**：改为 "p69 这句 KB 没收（§6.6 表只有 5 列），p50 那句 KB 照录"，并注明问题 1 选 B 时要先定这里的口径。

**M3　问题 6 没给数字影响和涉及条数**
- **位置**：`t4_owner_decisions_round2.md:89-97`
- **问题**：协调方要求每个选项都写出对数字的影响（`t4_coordinator_note_20261127.md:22`）。XDOC 审查者写了 "台账里约几十条标 EQUIVALENT，按本层口径都会判 NOT_HOLD"，这一页既没给条数，也没算从严之后 G-TB3 怎么动。
- **建议改法**：数出同类标题原子，并按从严情形实算 G-TB3。

**M4　问题 7 的区间和 "上限情形" 默认了配错的都记 IE**
- **位置**：`t4_owner_decisions_round2.md:106`；`t4_relabel_pending.md:29`、`:34`
- **问题**："介于 99.2651% 与 99.2541% 之间" 和 "上限情形" 都假定配错的原子改记 IE。如果自己那份文档的 KB 里也没有这段内容，又不被认可为 IE，就该记未覆盖；反过来，内容也可能其实在 `model/` 里，只需修指针、标签不变。这两种情形都在区间之外，第一种还会比 99.2541% 更低。
- **依据**：146 条里有 113 条 PARTIAL；只看过 p74 这 14 条。
- **建议改法**：写明 "按都认 IE 计"，或者另给一个 "改记未覆盖" 的情形数字。

**M5　C(ii) 范围内的筛法有盲区，结论只能算待核**
- **位置**：`t4_round2_sample.py` / `t4_round2b_sample.py` 的 TYPO 筛法；`t4_supp_fullcheck.md:96-97`
- **问题**：
  - 只取登记的第一个页号 ±1，而有 13 条登记是区段或多页（如 S-SPREL SE T-1 写 "p82-84"）。
  - 与 KB 行比重合度时只用登记给的行号；PE 那条只有 `kb_line_now` 174 一行，所以漏掉了。
  - TYPO_SIB2 不收 EXACT。
- **我的核法**：用 "PDF 笔误写法 token、且该 token 在全 KB 里不存在" 做全量扫描，加同页定位，结果没有找到范围内漏掉的原子。但 195 条 "KB 写正确值" 登记里，有 73 条抽不出可用的 token（多是空格或标点类笔误），我没法测。
- **建议改法**：在 fullcheck §4 写明这几处盲区。对那 73 条按人工或字符级 diff 补查。

### LOW

| # | 位置 | 问题 | 建议改法 |
|--:|---|---|---|
| L1 | `t4_t0_refresh.md:6` | 还写 "提问在 … 问题 4"，第 2 稿里 M-8 已是问题 5。我 grep 了所有改过的文件，只有这一处是旧编号。 | 改成 "问题 5"。 |
| L2 | `t4_supp_fullcheck.md:128` | "两条 EXACT 按定义成立" 是主控自己的判断；`a023` 没经任何审查。审查者提过 "影响相邻原子" 的口径（`pack_sib_1` 附注 1）。T-10d 的 `a019` / `a020` 同理。 | 写成 "主控按空白归一判定；a023 / a020 未审"。 |
| L3 | `t4_relabel_pending.md:107-108` | 写的候选是 "B-PCPP T-2 / T-3"，原始结果已经确认 a015 = T-2、a028 = T-3（`pack_sib_3.md:23-24`）。 | 写成确定的 id。 |
| L4 | `t4_owner_decisions_round2.md:72` | "剩下 99 条" 里有 `ig34_p0169_a0024` 在人工样本里；45 条抽样里也含人工样本的 `ig34_p0010_a002`。实际看过的是 51 条，不是 50 条。 | 加注说明。 |
| L5 | `t4_owner_decisions_round2.md:30-37`、`:45-48` | 未建议的选项后面带了评价括注："（与事实不符…）"、"（与…定义不符）"，有诱导之嫌。 | 把评价移到 "建议" 里，标成主控判断。 |
| L6 | `t4_owner_decisions_round2.md:12` | "按您上一轮确认的 U-1 B 口径" 没带 "按记录" 的限定，与第 134 行的写法不一致。 | 加 "按 `t4_owner_confirmation.md` 的记录"。 |
| L7 | `t4_owner_decisions_round2.md:80-82` | 只说 M4a 换了位置，没提 M4d0 的断言改了、M4d 删的份数从 2 变成 1。这两处是事先预告过的维护，但主人读这一句会以为只有 M4a 有变化。 | 加半句说明。 |
| L8 | `t4_supp_fullcheck.md:122` | "ig34 p278 Method B：叙述说…" 这段叙述其实在 p277:32，表在 p278。确认是同一处，已登记 B-PCPP T-4。 | 页号改成 "p277 叙述 / p278 表"。 |
| L9 | `t4_supp_fullcheck.md:95` | XDOC 层的 "共 57 条" 和第 1 稿里的 "57 条旧标签" 同数，容易混。 | 换个说法，或加注。 |
| L10 | `audit_matrix.md` 第二轮那一行 | "同页同行" 不准确，实际是 ±1 页、且与登记所在 KB 行的重合度 ≥ 0.8。 | 照实写。 |
| L11 | fullcheck 文末 #6 的处理 | 范围内 sv20 标题类 EQUIVALENT 共 5 条，有 2 条既没审也没交代。 | 补查，或写明没查。 |
| L12 | `t4_user_decisions.md:56`（M-7） | M-7 的内容在主人那次确认之后又被接手主控改过一次（U-7 23 → 22），"M-1 ~ M-7 已追认" 是否覆盖这次改动，属于待核。 | 注明这处改动发生在确认之后。 |
| L13 | `t4_coordinator_note_20261127.md` | 这份 "原文逐字" 是写作者自己誊录的，仓里无法独立核对（只有消息 id）。#3 的依据成立，但带着这个局限。 | 状态行写明这个局限。 |

## 我写的核对脚本

全部在 `/private/tmp/claude-501/-Volumes-DevSSD-Project-sdtm-pedia/4fbae0a7-da27-4851-8814-ac846216a212/scratchpad/review_c/`，用 `python3 -I` 运行，只读仓库，没有 import 仓内任何脚本。

- **`common.py`**：自己读取台账、原子、决策表、登记表、`md_atoms`、inventory；按原定义重写了 `in_scope`；汇总已审集合（gate / supp / q9 / u5_c7 / round2 / round2b / human）。
- **`b_parse.py`**：解析 8 个原始结果文件里的 R / S 行，与 `verdicts.json` 的 `round2` 逐条比对 num / verdict / layer / raw。输出：raw 175，json 175，mismatch 0；样本 175 条与原始结果一一对应。计数为 PDF_TYPO HOLDS 45 / TYPO_SIB 10 + 53 / TYPO_SIB2 5 + 35 / XDOC 24 + 3。
- **`c1_xdoc.py`**：
  - 范围内 57 条（EQUIVALENT 55 / EXACT 2），已审 30、剩 27；与 `round2_population.json` 的范围内、范围外两份清单完全相同。
  - 范围外 146 条（PARTIAL 113 / EQUIVALENT 21 / EXACT 12），p74 14 条，主要在 v2.0 第 11、71、5、6、74 页。
  - 27 条的类型：IG 非标题 16 条（TABLE_ROW 13 / LIST_ITEM 2 / SENTENCE 1），IG 标题 8 条，sv20 标题 3 条。
  - 范围内 stock 标题类 EXACT 149 / EQUIVALENT 167（ig34 162 / sv20 5）。非标题类 EXACT 1739 + 14 = 1753，EQUIVALENT 2207 + 127。
  - 指针混指两份文档的原子 0 条；完全没有 md 指针的 EXACT / EQUIVALENT 有 547 条（这些 XDOC 筛法看不到）。
- **`c3_pt.py`**：PDF_TYPO 149 条，未审 144 条 {S1-R2 52, writer-Tn 33, K3b 59}；按 seed 重抽与原样本相同。人工样本里的 2 条 PDF_TYPO，1 条在 45 条抽样内，1 条（`p0169_a0024`）在剩下的 99 条里。
- **`c2_sib.py` / `c2c.py` / `c2e.py` / `c2f.py`**：用笔误写法 token 反查原子，分同页定位和全 KB 全量两种做法；再用写作者的筛法去掉范围限制重跑。
  - 范围内没有确认的新反例：命中的 `p0280_a045` 是原子抽错，不是笔误漏标。
  - 范围外确认 6 条（H4）；写作者筛法下范围外候选为 36 + 36 条。
  - 195 条 "KB 写正确值" 登记里有 73 条没法用 token 测。
- **`d_check.py` / `d_nums.py`**：解析 `t4_relabel_pending.md` §3 的 72 行，核对现标签、原始结果文件:行、判定、登记 id。0 处不符（脚本输出里的 `REG MISSING` 是我解析时带上了 "PDF 笔误 " 前缀，直接查表后 3 个 id 都在）。按 `t4_coverage_decomp.py` 的公式逐行在内存里改标（台账有 11 个 id 重复出现，都不涉及这 72 条和 146 条），9 行数字全部与 `scenarios.json` 及 §2 表一致。
- **`e_check.py`**：
  - 72 条里只有 `ig34_p0064_a012` 在决策表里（T3 live-hit，PARTIAL → EXACT）；72 条都没进过 gate / human 样本。
  - 316 条标题类里 305 条没人审过。
  - EG p191 那 19 条全部是 EXACT。
  - 残余清单 1091 行 = kb_nav 685 / body 235 / heading 144 / table_elision 26（EG 25 + RE 1）/ kb_note 1。
- **另用 shell 核对的几处**：
  - 57 / 64 用审查者的正则复现了；不在 57 之列的 7 个域是 CO、FA、FT、MH、PE、TA、TU。
  - p69:22-23 写 "subject or pool identified in RDEVID"，p50:36 写 "device"，两处确实不同。
  - p277:32 的叙述就是 B-PCPP T-4 那处矛盾。
  - `model/` 里没有任何 Appendix 标题。
  - v2.0 变量表共 12 列（p52 表头）。

## 收尾命令输出

```
$ git status --short
 M .work/10_tier_b_repair/trace.jsonl
?? .work/10_tier_b_repair/work/t4/gate_prerun.log
$ git rev-parse HEAD:knowledge_base
63f857774a42cfaa71798705ad40ab51bc5e378a
$ md5 -q .work/10_tier_b_repair/work/coverage_ledger.wc.jsonl
60729f7b64b7c1dfaf2174e394f6dd9c
```

`git status` 里这两处不是我造成的：我只在上面那个 scratchpad 目录里写过文件，没有改过任何已跟踪文件。按 brief，这两处是写作者在审查期间追加 trace 行和生成预跑日志。KB 树和工作台账 md5 都与预期一致。
