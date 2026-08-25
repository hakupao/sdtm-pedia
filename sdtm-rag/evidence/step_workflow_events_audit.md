# Task 6 抽检方复算报告 (规则 D 三方核验之一)

> 日期: 2026-08-26 · 分支 `feat/study-workflow-events` · 对象 commit `e71a2a1`
> 抽检方与实现方不同 agent / 不同 `subagent_type`, 未复用本计划的任何脚本
> 数据红线: 零真实 OID / label — 全部用题号 (`ev_qNN`) + 计数 + 形态 (`<OID len=N>`) 指代

## 0. 一句话结论

**全部 6 项数字逐位吻合, 无一处对不上。** 三池 14/77/110 与 ledger +209 用**直读 xlsx**
(自写 openpyxl 表头/脚注逻辑, 不 import `parse_config_report`) 复算成立; 闸 A/B/C 四数
与转置 61/61 复算成立; 15/33 与六类分区、§3 精度表逐格复现; 卡片侧 87.50% 三遍 Δ0 复现。

**但特别交办的三件事里, A 项归因不成立。** 实现者把 15 个 0 命中统一归因为「Task 5 把
答案词从题面拿掉了」—— 该归因对其中 **8 题成立**, 对另外 **10 题 (`ev_q06`-`ev_q15`)
不成立**。这 10 题的真实成因是 `resolve_events` **没有任何能从 event/activity/form 词汇
产出 `assignment:` 目标的索引维度**, 与题面是否含答案锚点无关: 把完整三元组词汇 (event
OID+名 / activity OID+名 / form OID+名) 全部塞进题面, 10 题 **0 题命中**; 只加一个该 form
下的 item OID, **9/10 命中**。且其中 4 题的 gold form OID (`<OID len=7~8>`) 本来就逐字在
题面里 —— 直接反证「题面不再包含答案锚点」这一说法。B 项 (类型 6 减法) 与 C 项 (brief
扩展) 结论均成立, 但各带 1-2 条实现者未披露的事实, 见 §7。

复跑口径: 本报告全部数字由 `/private/tmp/.../scratchpad/aud{1..12}*.py` 六个自写脚本产出
(临时目录, 不进 git); xlsx 侧走 `openpyxl.load_workbook` 直读, 逐题侧只调被测对象
`StudyLookup.resolve_events`, 计分/簿记全部自写, 未 import `eval.*`。

---

## 1. 三池计数 + ledger (独立复算: 直读 xlsx)

方法: 自写表头解析 (Events/Activities 三行表头自行 4 起, Forms 两行表头自行 3 起),
自写脚注判据 (ID 单元格为空或含空白 → 脚注), 不经过 `parse_config_report.py`。

| 项 | 实现者声称 | 我的独立复算 | 判定 |
|---|---|---|---|
| events | 14 | **14** (脚注 3, 非空行合计 17) | 吻合 |
| activities | 77 | **77** (脚注 3, 非空行合计 80) | 吻合 |
| assignments | 110 | **110** (脚注 2, 非空行合计 112) | 吻合 |
| ledger 增量 | +209 | **+209** | 吻合 |

ledger 加固复算 (实现者未做这一步): ledger 是全 6 个 sheet 的**逐行 1:1 台账** ——
我用 xlsx 直读逐 sheet 数非空数据行, 得 22 / 1087 / 2399 / 17 / 80 / 112 = **3717**,
与 `catalog["ledger"]` 长度 3717 逐位相等, 且按 `sheet` 字段分组的计数逐个相等。
故 workflow 三 sheet 的贡献恰为 17+80+112 = **209**, 「+209」不是估算而是恒等式。

catalog 侧读数一并核对: events 14 / activities 77 / assignments 110 / forms 21 /
items 959 — 与 xlsx 侧一致。

---

## 2. 闸 A 四数 (独立复算: 直读 xlsx, 自行 join)

| 项 | 实现者声称 | 我的独立复算 | 判定 |
|---|---|---|---|
| assignments 行数 | 110 | **110** | 吻合 |
| 唯一 form 数 | 21 | **21** | 吻合 |
| 两类 event type 下的分配数 | 109 + 1 | **sorted = [1, 109]**, 恰 2 个 type, 0 个引用不到 | 吻合 |

附带 (实现者未报): events 池自身按 event type 的分布是 **[1, 13]** —— 即那个只挂 1 条
assignment 的 type 下恰好只有 1 个 event。这条与闸 A 的 [1,109] 互证, 说明 [1,109] 不是
「多个 event 摊出来的巧合」。

---

## 3. 闸 B 引用完整性四条

| 条 | 实现者声称 | 我的独立复算 | 判定 |
|---|---|---|---|
| activities.event_oid ⊆ events | 差集 0 | **0** | 吻合 |
| assignments.event_oid ⊆ events | 差集 0 | **0** | 吻合 |
| assignments.activity ⊆ activities | 差集 0 | **0** (我用的是 (event,activity) **二元组**, 比在跑的测试更严) | 吻合 |
| assignments.form_oid ⊆ forms | 差集 0 | **0** | 吻合 |

**未披露的前提** (非缺陷, 但测试没锁): 在跑的 `test_gate_b_referential_integrity` 第 3 条
比的是**扁平 activity OID 集合**, 不是 (event, activity) 对。这只在「activity OID 全局唯一」
时才等价于我跑的严格版。我核了这个前提: 77 个 activity OID **77 个互异, 跨 event 复用 0 次**,
前提成立。但没有任何测试断言这一点 —— 换一个 activity OID 会跨 event 复用的研究, 闸 B 第 3 条
会静默变弱 (一条指向别的 event 下同名 activity 的 assignment 照样过闸)。建议把二元组版本
替换进去, 成本是改 1 行。

---

## 4. 闸 C 转置一致性 (两侧都从 xlsx 直读)

我把 items 侧也改成从 `Items and Groups` sheet 直读 (实现者的测试是从 catalog 读),
两侧都不经过 catalog 组装。

| 项 | 实现者声称 | 我的独立复算 | 判定 |
|---|---|---|---|
| fwd 键数 | 61 | **61** | 吻合 |
| bwd 键数 | — | **61** | — |
| 键集合对称差 | 0 | **0** | 吻合 |
| 逐键 item 集合不匹配数 | 0 | **0** | 吻合 |
| 隐藏清单侧 activity 去重数 | 61 | **61**, 且 61 个全部在 activities 池内 (差集 0) | 吻合 |

**「逐键完全相同」这个措辞需要限定 (实现者未披露)**: fwd 侧是把 **82 条**「Hidden items
非空」的 assignment 行**按 activity OID 并起来**压成 61 个键的。我查了这个压缩是否有损:
**15 个 activity 出现在 >1 条带隐藏清单的 assignment 行里, 而这 15 个的逐行隐藏集合
全部互不相同** (15/15)。也就是说闸 C 当前的粒度**看不出 form 级别的错配** —— 把 A 表单
那一行的隐藏 item 错记到 B 表单那一行, 并集之后闸 C 照样绿。

我补跑了一版**更严的 form 感知转置** (items 自带 `form_oid`, 所以逐 (activity, form) 对
比是做得到的, 实现者没做): 对 82 条行逐条比「该行的 Hidden items」与「该 form 下、
Hidden-in-activity 含该 activity 的 items」, **82/82 完全相等, 0 条不一致**。
所以数据本身没问题, 更强的结论也成立 —— 但这是我补出来的, 在跑的闸没有证明它。
建议把闸 C 升级到 form 粒度, 成本约 5 行。

---

## 5. 15/33 命中率 · 六类分区 · §3 精度表

自写计分器 (自己 load yml、自己算交集、自己记账), 只调被测方法。

| 项 | 实现者声称 | 我的独立复算 | 判定 |
|---|---|---|---|
| 总命中 | 15/33 = 45.45% | **15/33 = 45.45%** | 吻合 |
| event_timing | 0/5 | **0/5** | 吻合 |
| event_form_assignment | 0/5 | **0/5** | 吻合 |
| repeating_rule | 0/5 | **0/5** | 吻合 |
| conditional_event | 4/7 | **4/7** | 吻合 |
| oid_name_mapping | 6/6 | **6/6** | 吻合 |
| item_collection_scope | 5/5 | **5/5** | 吻合 |
| 未命中清单 (18 题) | q01-q10, q11-q15, q16/q17/q20b | **逐题号完全相同** | 吻合 |

§3 精度表 (总返回数 / `assignment:` 类型数 / 该类型内 tp / fp / 其他类型噪声 / gold 集大小):

| 题 | 实现者声称 | 我的独立复算 | 判定 |
|---|---|---|---|
| `ev_q27` | 7 / 7 / 7 / 0 / 0 / 7 | **7 / 7 / 7 / 0 / 0 / 7** | 吻合 |
| `ev_q28` | 8 / 8 / 1 / 7 / 0 / 1 | **8 / 8 / 1 / 7 / 0 / 1** | 吻合 |
| `ev_q29` | 2 / 2 / 2 / 0 / 0 / 2 | **2 / 2 / 2 / 0 / 0 / 2** | 吻合 |
| `ev_q30` | 4 / 1 / 1 / 0 / 3 / 1 | **4 / 1 / 1 / 0 / 3 / 1** | 吻合 |
| `ev_q31` | 1 / 1 / 1 / 0 / 0 / 1 | **1 / 1 / 1 / 0 / 0 / 1** | 吻合 |

闸 E 一并复跑: `eval.lint_gold --events-catalog` → `0 条 gold 未唯一定位`, exit=0。吻合。

---

## 6. 卡片侧不回归 + 测试数

| 项 | 实现者声称 | 我的独立复算 | 判定 |
|---|---|---|---|
| study golden v2 | 87.50% | **0.875, 三遍全部 0.875** | 吻合 |
| 逐题 Δ | Δ0 | **三遍逐题完全一致; 与冻结基线 `runs/v2_baseline_s2on.json` 48 题逐题差异 0 条** | 吻合 |
| 全量测试 | 1772 passed / 0 failed / 0 error | **tests=1772 failures=0 errors=0 skipped=0** | 吻合 |
| +10 新增 / −2 迁移 | — | **新文件 7 + 3 = 10 个 `def test_`; diff 里从 `test_build_field_cards.py` 删掉 2 个 `def test_`** | 吻合 |

「1764 基线」我没有 checkout 父提交去数, 但本 commit 只动了 3 个测试文件,
1772 − 10 + 2 = **1764** 由构造成立, 与声称一致。

---

## 7. 特别交办的三件事

### A. 「15 题 0 命中是结构性、非 bug」—— **归因不成立 (10/15 题成因被说错)**

我把 18 个未命中按 gold 的目标类型拆开验证。判据: gold 目标的每个可索引锚点
(event OID/名、activity OID/名、form OID) 是否**逐字出现在归一化后的题面里**;
以及**反事实**: 把锚点加回题面, 该题会不会命中。

**归因成立的 8 题** (gold 是 `event:` 或 `activity:` 类型):

| 题 | gold 类型 | 锚点在题面? | 加回锚点后 |
|---|---|---|---|
| `ev_q01`-`ev_q05` (event_timing 全 5 题) | `activity:` | 4 个锚点全部**不在** | **5/5 命中** |
| `ev_q16` / `ev_q20b` | `event:` | 2 个锚点全部**不在** | **2/2 命中** |
| `ev_q17` | `event:` | event OID 不在; **event 名 (`<LABEL len=2>`) 在题面里** | 命中 |

这 8 题里 7 题是干净的「题面没有锚点」。**`ev_q17` 是个例外, 实现者的措辞盖不住它**:
它的 gold event 名逐字在题面里, 未命中的原因是该名长度 2 < `_MIN_EVENT_NAME_LEN = 3`,
**根本没进索引**。这是阈值致因, 不是「答案不在题面」致因 —— 同一句话把两种机制混起来说了。

**归因不成立的 10 题** (`ev_q06`-`ev_q10` event_form_assignment + `ev_q11`-`ev_q15`
repeating_rule, gold 全部是 `assignment:` 类型):

`resolve_events` 的两段索引里, **`assignment:` 目标只在第二段 (item OID → `collect_scope`
减法) 里产出**。第一段 (`_event_index`) 我遍历了它的全部键, 它**只能产出 `event:` 与
`activity:` 两种类型**; 21 个 form OID **在两个索引里都不是键** (各 0 个)。也就是说
event / activity / form 这套词汇**在结构上无法产出 assignment 目标**, 无论题面写得多全。

三重证明:

1. **全池合成反事实**: 对全部 110 条 assignment, 我造了「event OID + event 名 + activity
   OID + activity 名 + form OID + form 名」六件套全塞进去的题面, 喂给 `resolve_events`。
   **只有 2/110 返回了对应的 assignment 目标** —— 而这 2 例是六件套里某个串恰好撞上一个
   item OID 的偶然碰撞, 不是设计路径。
2. **逐题反事实 (a)**: 这 10 题, 题面 + 完整三元组词汇 → **0/10 命中**。
3. **逐题反事实 (b)**: 这 10 题, 题面 + 一个该 gold form 下的 item OID → **9/10 命中**
   (剩 1 题 `ev_q10` 该 form 下 41 个候选 item 无一奏效)。

**更直接的反证**: `ev_q11` / `ev_q12` / `ev_q14` / `ev_q15` 四题的 gold form OID
(`<OID len=7~8>`, 不是短串巧合) **本来就逐字在题面里**。checkpoint §2.1 写的
「只能回答『问题本身已经点名了要查的对象』这一类问法」在这四题上是**被数据直接推翻的** ——
题面点名了对象, 通道照样答不出, 因为缺的是索引维度, 不是锚点。

**判定**: 这 15 个 0 **不是「代码与自身设计不符」意义上的 bug** (代码确实按写的那样跑),
但 checkpoint 给出的**成因是错的**, 且错误方向是把工程缺口说成了题集设计的必然代价。
§4-4 进一步写「要答这类题需要生成式能力, 与零 LLM 设计根本冲突」—— 对 `ev_q11`-`ev_q15`
这句**可证伪**: 一个 form OID → assignment 的索引维度 (数据齐备, `assignments` 池里就有
`repeating` 列) 能确定性地答这类题, 零 LLM。是否要加是范围决策 (brief 的 Interfaces 行
只承诺 event/activity 目标), 但**不能拿「结构性、非 bug」把它盖过去**。

附带量化: 959 个 item 里 **10 个 OID 长度 < 3, 永不进索引**; 因此 110 个 assignment 目标
里 **只有 99 个** 是 item 段有可能产出的, 另 11 个在当前实现下**不可达**。

### B. 「类型 6 减法 5/5 精确 (tp=gold, fp=0)」—— **成立, 且噪声来源报告诚实**

我做了实现者没做的**逐索引键贡献分解** (每个触发的 item OID 键各自产出了哪些目标):

| 题 | 触发的 item 键 | 各键产出 | 与 gold 逐条相等? |
|---|---|---|---|
| `ev_q27` | 1 个 `<OID len=3>` | 7 条 | **是** (tp=7 fp=0 fn=0) |
| `ev_q28` | 2 个: `<OID len=10>` / `<OID len=3>` | 1 条 / 7 条 | 目标键**是** (tp=1 fp=0); 无关键 7 条全 fp |
| `ev_q29` | 1 个 `<OID len=4>` | 2 条 | **是** (tp=2 fp=0 fn=0) |
| `ev_q30` | 1 个 `<OID len=4>` | 1 条 | **是** (tp=1 fp=0 fn=0) |
| `ev_q31` | 1 个 `<OID len=6>` | 1 条 | **是** (tp=1 fp=0 fn=0) |

`ev_q30` 的 3 条其他类型噪声我也追到源头: 事件/活动段命中了 2 个键 (`<len 4>` 与 `<len 8>`),
产出 event:1 + activity:2, 与 item 段无关 —— 与实现者 §3 的说法一致。

**噪声来源的报告是诚实的**: 两种失效机制 (短 OID 跨 item 碰撞 vs 事件名称段独立命中)
被分开说了, 没有混成一句「有噪声」; §4-5 关于「尺子无 precision 惩罚, 盲区未被堵上」的
自陈也是对的, 没有把 5/5 说成「减法通道整体精确」。

**但有 1 条未披露的脆弱性**: `ev_q28` 的原始 (未截断) 返回数**恰好是 8 = `_MAX_EVENTS_TOTAL`**,
正好压在截断线上。gold 目前排在第 1 位所以活着, 但这个排序由 `_item_oid_index` 的
**dict 插入序 (= catalog item 顺序)** 决定, 与相关性无关 —— 换个 catalog 排序, 或那个
碰撞 item 多产出 1 条, gold 就可能被 cap 截掉。§3 表里那个「8」读起来像自然结果, 实际是
边界值。

### C. 「主动扩展 brief 的示例代码 (item 采集范围索引)」—— **必要, 边界清楚, 可单独回退**

**必要性 (量化)**: 我把 brief Step 3 的示例代码**逐字**跑了一遍 (只有事件/活动索引段,
无 item 段), 用同一把尺子计分:

| 类别 | brief 字面版 | 出货版 | Δ |
|---|---|---|---|
| event_timing | 0/5 | 0/5 | 0 |
| event_form_assignment | 0/5 | 0/5 | 0 |
| repeating_rule | 0/5 | 0/5 | 0 |
| conditional_event | 4/7 | 4/7 | 0 |
| oid_name_mapping | 6/6 | 6/6 | 0 |
| **item_collection_scope** | **0/5** | **5/5** | **+5** |
| **总计** | **10/33 (30.30%)** | **15/33 (45.45%)** | **+5** |

即: 扩展贡献了全部 15 分里的 5 分, 且**恰好只落在 item_collection_scope 一类**, 对其余
五类零影响 (含零副作用 —— 没有因为多一段索引而挤掉任何原本命中的题)。同时,
`build_field_cards.py` 的生产渲染路径传 `assignments=None`, 不调 `collect_scope`; 若不加
这段扩展, `collect_scope` 在整个仓库里**没有任何生产消费方**, M5 要求的「Task 6 是
collect_scope 的第一个真实消费方」字面上无法成立。**扩展是必要的, 不是可选项。**

**契约上的一处张力 (值得记, 不影响判定)**: brief 的 Interfaces 行写的是
「返回命中的 **event/activity** 目标名」, 扩展让它也返回 `assignment:`。不过 brief 自己的
Self-Review §3 把命名空间写成 `event:` / `activity:` / `assignment:` 三种, Task 5 的 gold
也确实用了三种 (33 题的 gold 目标类型分布: assignment 22 / event 10 / activity 8)。
所以扩展与 **gold 一致**, 只与 brief 散文里的一行不一致。

**边界与可回退性**: 干净。扩展面 = `__init__` 里 3 个字段 (`_item_oid_index`、
`_assignments_by_form_activity`、`_assignments`) + `resolve_events` 里的第二段循环 +
1 行 import。`git grep` 复核: 全仓**没有任何其他地方**读这 3 个字段。`collect_scope.py`
模块本身在回退后仍然活着 (`build_field_cards.py` 独立 import 它)。回退的**唯一**代价是
item_collection_scope 那 5 分, 不牵动其余任何东西。

---

## 8. 实现者未披露的问题 (汇总)

按严重度排序:

1. **[高] 10/15 个 0 命中的成因被说错** (§7-A)。checkpoint §2.1 / §4-4 把「缺 form→assignment
   索引维度」说成了「题面不含答案锚点、需要生成式能力」。方向性问题: 把可用确定性手段闭合的
   工程缺口, 记成了不可修复的结构性限制。4 题的 gold form OID 逐字在题面里, 直接反证。
2. **[中] `_MAX_EVENTS_TOTAL = 8` 在真实数据上确实触发, 全文未提**。`ev_q02` 的原始返回是
   **14 条, 被截断到 8**。这是 33 题里唯一真截断的一题。不影响该题得分 (gold 本就不在原始
   列表里), 但 §3 表格的「总返回数」列报的是**截断后**的数, 读起来像原始规模; 9 条已知限制
   里也没有「cap 会截断」这一条。
3. **[中] `ev_q28` 压在 cap 边界上** (原始 8 = cap 8), gold 靠 dict 插入序排第 1 才活着 (§7-B)。
4. **[中] 闸 C 的粒度弱于 checkpoint 的措辞**。fwd 侧把 82 条 assignment 行按 activity 并成
   61 个键, 而 15 个 activity 的逐行隐藏集合互不相同 —— 闸 C 看不出 form 级错配 (§4)。
   我补跑的 form 感知严格版 82/82 通过, 所以**没有实际缺陷**, 但在跑的闸没证明这件事。
5. **[低] 闸 B 第 3 条的隐含前提无测试看守**: 用扁平 activity OID 集合, 只在 activity OID
   全局唯一时才等价于二元组版 (我核了: 77/77 互异, 前提成立, 但无断言) (§3)。
6. **[低] 覆盖面缺口未量化**: 10/959 个 item 的 OID 长度 < 3 永不进索引, 导致 110 个
   assignment 目标里 11 个在当前实现下不可达 (99/110) (§7-A 末)。

以上 6 条**均不改变 §1-§6 的任何数字**, 也不推翻实现者「代码按设计跑通」的结论。第 1 条
改变的是**结论的性质**: 45.45% 里那 15 分的缺口, 不全是题集设计的必然代价。

## 9. 未做 / 不在本次范围

- 未 checkout 父提交实测 1764 基线 (由构造推得, §6)。
- 未做 `_MIN_ITEM_OID_LEN` 的 4/5 字符阈值敏感性扫描 (属审查方的对抗性复核范围)。
- 未评估 `resolve_events` 与 `resolve()` 的挤占 (实现者已列为已知限制 §4-3)。
- 未改动任何文件 (本报告除外), 未派 subagent。
