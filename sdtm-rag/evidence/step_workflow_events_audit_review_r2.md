# Task 6 修复轮1 对抗性复核 (规则 D 第 2 轮 · 审查方)

> 日期: 2026-08-26 · 分支 `feat/study-workflow-events` · 复核范围 `e71a2a1..6b54d6c`
> 角色: 规则 D 第 2 轮之**审查方** (与实现方、首轮抽检方/审查方均不同 subagent)
> 红线: 全文零真实 OID / label / 题面 — 一律用题号 (`ev_qNN`) + 计数 + 形态 (`<OID len=N>`)
> 未改动任何文件 (本报告除外), 未派 subagent, 未重跑全量测试 (按派发指示)

---

## 总判定

- **首轮 10 条发现的落实: 10/10 ADDRESSED** —— 逐条查过, 没有一条是"只写了个标题"的
  打折写法; 新增的两条闸测试与两处代码修复都是带真实断言的实件, 我独立复算过其中
  全部可复算的数字, 无一处对不上。
- **但本轮**新引入** 1 Critical + 3 Important**。Critical 与首轮 Critical-1 是**同一类
  错误的复发**: 修复只做了缺口的一半 (form OID → assignment), 然后在标题写着"归因纪律
  (修复轮1教训, 不能再犯)"的那一节里, 对剩下那一半又写了一次"题面本身没有锚点"的归因
  —— 对 4 题**与实测相反**。
- 红线: 本轮改动面 (8 个文件 + diff 全文) **零真名**, 含闸自身看不见的短名形态 (我补扫了
  68 个 len 2-3 的真实名称, 0 命中)。实现者自述的草稿手滑**没有漏网**。

---

## 第一部分 · 首轮 10 条逐条判定

> 派发信写"9 条", 逐项列出来是 10 条 (Critical 1 + Important 4 + 审查方 Minor 3 +
> 抽检方 Minor 2); 抽检方实际是 3 条 Minor (checkpoint §9 记作 a/b/c), 我按 11 条全查。

| # | 首轮发现 | 判定 | 证据 |
|---|---|---|---|
| Critical-1 | Ruling P2 未落地 | **ADDRESSED**(实现层) | `server/study_lookup.py` 新增 `_form_assignment_index` (form_oid → 该 form 全部 assignment) + 三层拼接; 实测 `repeating_rule` 0/5→5/5、`event_form_assignment` 0/5→1/5, 总分 15/33→21/33。⚠ **配套归因是本轮新 Critical, 见第三部分** |
| Important-1 | 闸 D 是空闸 (`git status` 查 gitignored 目录) | **ADDRESSED** | §1 闸 D 那格把旧方法**划了删除线**并写明"是**空闸**, 卡片改没改都一样"; 改用 sha256 对 `cards_post_t1.sha256.json`。我独立重算: `identical=961 changed=0 missing=0 extra=0 (n=961)`。§8 M5 那段的同一句也一并改了 |
| Important-2 | 6 条被点名"进 T6 收口证据"的裁定/教训整批缺席 | **ADDRESSED (6/6, 有实质内容)** | ①闸 C 的 61 是回归锁 → §1 闸 C 行的 ⚠ 段, 明写"判别力来自 `set(fwd)==set(bwd)` 与 `mismatched==[]` 两处独立导出的互证, 61/82 只是稳定性快照"; ②fixture repr 泄漏定量边界 → §6-10 (`--tb=short`/`-q`/`--showlocals`/整体 dict 比较 四种情形逐一写明); ③中间产物红线扫描 → §6-11(a); ④对照语料覆盖面盲区 → §6-11(b); ⑤占位符可区分 → §6-12; ⑥Task 4 减法数据自洽 → §6-13。**⑥我独立复算过**: 带 `Hidden in activity` 的 item = **231** (声称 231), "减法未生效"= **0** (声称 0) |
| Important-3 | `_MAX_EVENTS_TOTAL=8` 截断已真实触发, 全文零披露 | **ADDRESSED** (但新写的证明句过宽, 见第三部分) | §2-1 写明首轮实测 `ev_q02` 未截断 14 条被砍到 8; §2-4 重新论证 cap 语义并把取值改为 50; §9 逐条对照里也记了。cap 现在**仍在咬**: `ev_q06` 未截断 60 → 截断 50 (我复算一致) |
| Important-4 | 45.45% 无参照物 | **ADDRESSED** | §5 新增旧通道基线 (卡片 3/33 · doc 7/33 · 并集 9/33 · 语义核验后真阳性并集 3/33), 并带**口径警告**: 旧数是 fact-recall、本轮是 source-recall, 明写"不能直接相减或换算成'增益 X 个百分点'", 还点名禁止"好 6 倍"这种表述 |
| Minor-1 | `item["raw"]` KeyError; docstring 保证宽于测试 | **ADDRESSED** | `collect_scope.py` 改 `(item.get("raw") or {})`; 旧用例 docstring 加 ⚠ 明写"只证明了事件/活动索引那一半"; 新增 `test_resolve_events_item_scope_missing_raw_degrades_quietly` + `test_collect_scope_missing_raw_key_treated_as_no_hidden` 补对称覆盖 |
| Minor-2 | `_item_oid_index` 键未过 `_norm`, 与其余索引不对称 | **ADDRESSED** | 改为 `self._item_oid_index[_norm(oid)]`, 注释写明"无行为变化的加固" |
| Minor-3 | §2.2 标题"单列不进总分" vs 正文自相矛盾 | **ADDRESSED** | §3.2 加 ⚠ 口径更正段, 如实写"确实计入了 21/33", 并给出净额 **19/30 = 63.33%**。我复算: 21 − (`ev_q28`/`ev_q30` 两个命中) = 19, 33 − 3 = 30 ✓ |
| 抽检方 (a) | 闸 C 升级 form 感知严格转置 | **ADDRESSED** | 新增 `test_gate_c_transpose_consistency_form_aware`, 按 (activity, form) 二元键, 断言 `键集对称差=0` / `键数==82` / `mismatched==0`。我独立复算带 `Hidden items` 的 assignment 行 = **82** ✓ |
| 抽检方 (b) | 闸 B activity OID 全局唯一无测试看守 | **ADDRESSED** | 新增 `test_activity_oid_globally_unique`, 断言 `n_total == n_unique == 77`; docstring 写清了"为什么 gate B 三条差集不需要这条前提也能过" |
| 抽检方 (c) | 覆盖面缺口未量化 | **ADDRESSED** | §6-8。我独立复算全部三个数: item OID <3 的 item = **10**/959 ✓ · assignment 目标总数 = **110** ✓ · Tier 2 不可达 = **11** ✓ · 去掉长度下限后不可达 = **0** ✓ |

三个本轮改动的测试文件实跑: `25 passed` (events 12 / collect_scope 4 / workflow_pools 9)。
两条新闸测试都是真断言, 不是占位。

---

## 第二部分 · 三件重点

### A. Tier 1b 避让逻辑的边界 —— **有两条真实遗漏, 其中一条会丢正确结果**

避让逻辑本体 (`server/study_lookup.py` 的 `covered_forms`): Tier 2 每算出一个**非空**减法
结果就把该 item 的 form 记进 `covered_forms`; Tier 1b 遍历时跳过 `covered_forms` 里的 form。

**派发信点名的四种边界, 逐个构造实测 (合成 fixture 全部用 `偽`/`GI` 前缀伪值):**

| 边界 | 结论 |
|---|---|
| 题面点名 item 但**不**点名 form | **无遗漏**。Tier 1b 要 form OID 自己有界命中才 fire, 不命中就不存在"要不要让"的问题。真实数据里 form/item/event/activity 四类 OID **零个**含 `[A-Za-z0-9_]` 之外的字符, 所以不会出现"item OID 内部夹一个连字符, 把 form OID 露成一个有界 token"这种间接触发 |
| 题面点名**多个** form | **无遗漏**。逐 form 独立判定, 我构造"点名 formA+formB+formA 的一个 item"实测: formA 让位、**formB 的原始清单完整保留** |
| 点名的 item 属于**多个** form | **有边界, 当前无害**。真实数据 959 个 item_oid **全局唯一** (0 个跨 form 复用), 所以不发生; 但代码里 `_item_oid_index` 的值是 list, 合成实测确认: 一个 OID 落在两个 form 时, **两个 form 会一起进 `covered_forms`**, 于是"用户明确点名的那个 form"也可能因为另一个 form 里有个同名 item 而被连坐 |
| item 的减法结果为**空** | **非单调, 未记录**。`if scope:` 才进 `covered_forms` ⇒ 一个"在所有活动里都被隐藏"的 item 反而**不触发避让**, Tier 1b 原样吐出未减法全集。真实数据 0 例 (我复算: scope 为空的 item = 0/959), 属理论边界 |

**真正的问题是第五种 —— 派发信问的"会不会误把正确的 Tier 1b 结果也让掉": 会, 而且可复现。**

Tier 2 的结果按定义是 Tier 1b 的**子集** (`collect_scope` = 该 form 的分配 − 该 item 的隐藏
清单)。只要隐藏清单非空, 这个子集就是**真**子集 —— 让位掉的那部分**没有任何其他层会补回来**。

- 真实数据规模: **231/959** 个 item 的减法结果是所属 form 全量的真子集 (涉及 7/21 个 form);
  单个 item 触发的避让最多吃掉 **39** 条目标。
- 端到端复现 (走 `resolve_events`, 非纸面推演):

  | query 形态 | 返回条数 |
  |---|---|
  | 只点名一个 `<OID len=3>` form | **40** 条 (该 form 全量) |
  | 同一 form + 该 form 下一个 `<OID len=10>` item | **1** 条 |

  差集: 只在前者出现的 **39** 条, 全部是 `assignment:` 型, 全部因避让消失。

- **触发器本身是不可靠的**: 避让的触发条件只是"某个 item OID 有界命中题面", 而 §6-6 是
  checkpoint 自己刚写进已知限制的一条 —— 短 OID 会跟研究领域通用词撞字面。我量化了这个
  交叉风险: 3-4 字符的 item OID 共 **66** 个, 其中 **33** 个一旦被通用词巧合触发, 就会把
  所属 form 的 Tier 1b 清单压掉并真的丢目标 (单次最多 39 条)。**即: 一次巧合的 Tier 2
  命中, 可以吃掉一次被明确点名的 Tier 1b 请求。**

**因此 §2-2 与 `resolve_events` docstring 里那句"命中不丢 (两层都含 gold)"作为一般陈述
是假的** —— 它只在 `gold ⊆ Tier 2` 时成立, 也就是只在"题面问的是 item 采集范围"时成立;
对 form 级问法 (`event_form_assignment`/`repeating_rule`, 正是 Ruling P2 要服务的那两类)
恰恰不成立。

**本轮 33 题不受影响 (已逐题验证)**: 避让实际触发 5 题 (全部是类型 6), 共压掉 66 条目标,
**因避让丢掉 gold 的题数 = 0**。所以这是设计缺陷而非当下的分数问题, 但它埋在"Ruling P2
服务的那两类问法"正下方。

**建议**: 避让改成"逐条相减"而不是"整 form 让位" —— Tier 1b 只跳过**已经在 Tier 2 出现过
的那些具体 target**, 其余照常输出。这样 precision 收益一样拿到 (重复条目不会重复出现),
但不会连带删掉"被这个 item 隐藏、却仍然是该 form 真实分配"的条目。

---

### B. cap 三层优先级 —— **优先级本身真的生效 (我构造了触发用例证实); 但 §2 的证明不充分, 且标题的全称断言有反例**

**(1) 原证明的充分性: 不够。** "33/33 题在有 cap / 无 cap 两种口径下命中判定完全一致"
我复算属实 (唯一真截断的是 `ev_q06`, 60 → 50, 两种口径下都 miss)。但这个证明有两处结构性
盲区: ①33 题里只有 1 题触发 cap, "全部不触发"本来就无法证明设计正确 (这正是派发信的原话);
②判定是**二值**的, 只看 `gold ∩ 返回 ≠ ∅`, 对"相关目标被砍掉但本来也不算命中"完全不敏感。

**(2) 我构造的触发用例: 优先级确实生效。**

| 构造 | uncapped | capped | 结果 |
|---|---|---|---|
| 两个大 form (Tier 1b) + 一个第三 form 的 item (Tier 2) | 70 | 50 | Tier 2 的 **12 条全部保留**; 被砍的 20 条全是 Tier 1b |
| 同上再加 3 个名称索引键 (Tier 3) | 74 | 50 | Tier 3 的 4 条 **全部被砍 (保留 0)**; Tier 2 仍 12/12 保留 |

即"结构化目标不被名称子串挤掉"这个 Ruling 的**字面目标是达到了**。测试侧也已有一条真正
触发 cap 的用例 (`test_resolve_events_structured_not_squeezed_by_name_substring`, 造了 60 个
同名 Tier 3 目标 > cap 50, 断言 Tier 1a 存活) —— 那条是实件, 不是纸面; 但它的 query 里没有
item OID, 所以**没有测到 Tier 2 在 cap 下的存活**, 上表第一行补上了这一半。

**(3) 但 §2 的加粗标题「验证: cap 从未挤掉结构化目标」有反例, 撑不住。**

`ev_q06` (未命中题, 首轮 Critical-1 表格里的第一行):

| | 未截断 (60 条) | 截断后 (50 条) |
|---|---|---|
| gold 的 `event:` 目标在不在 | **在** | **不在** |
| gold 的 `activity:` 目标在不在 | **在** | **不在** |

被 cap 砍掉的 10 条里, 有 **2 条是 `event:`/`activity:` 型** —— 恰好就是 gold 自己那一对。
顶掉它们的, 是 50 条来自"短 form OID 撞通用词"(§6-6 自己记的那条已知限制) 的 Tier 1b 原始
清单。**噪声排在信号前面, 只是位置从 Tier 3 下移到了 Tier 1b。** 判定没变 (gold 是
`assignment:` 粒度, 两种口径下都 miss), 所以"33/33 判定一致"这个证明**结构上看不见它**。

**(4) 另一条未披露的层内行为**: Tier 1b 层**内部**的截断顺序是 `_form_assignment_index`
的 dict 插入序 (= catalog 里 assignments 的原始行序), 不是相关性序。实测: 两个大 form 同框
时 uncapped 58 → capped 50, 被砍的 8 条**全部落在其中一个 form**, 另一个 0 条 —— 谁被砍
只取决于谁在 catalog 里排后面。首轮 Important-3 点名的"截断顺序是插入序不是相关性序"这条,
在 Tier 之间被修好了, 在 Tier **之内**原样存在, 全文未提。

**建议措辞**: 把标题改成"33 题上 cap 未改变任何题的命中判定" (这句我复算属实), 并把
`ev_q06` 那两条被砍的相关目标 + Tier 1b 层内插入序截断补进 §6。

---

### C. 同源自洽风险的表述 —— **② 已落地; ① 只写了禁令没写定性, 判 PARTIALLY ADDRESSED**

**② (支撑"减法有效"的是 Task 4 数据自洽佐证): ADDRESSED, 且写得好。**
§4 开头的 ⚠ 段直接把读者引过去: "真正独立于这 5 题、能佐证减法机制本身的证据是 Task 4
数据自洽复算, 见 §6-13"; §6-13 正文完整 (231 个带隐藏清单的 item, 0 个"减法什么都没减掉"),
并说明了这是**双重缺口**的两侧 (Task 4 侧此前未做, 本单元补上)。我独立复算: **231 ✓ / 0 ✓**。

**① (类型 6 的 5/5 是循环证据、不得单独引用): 禁令 ADDRESSED, 定性 NOT ADDRESSED。**

- **禁令部分写得很硬, 挑不出打折**: §4 标题已改成中性的"返回件数与 precision 实测";
  开头写明"本节**不作为**'类型6 减法有效'的证据"; 结论段再写一遍"**不是**对减法规则本身
  '是否有效'的独立验证"; 结尾还加粗了"引用本节时必须完整带出返回件数与 tp/fp 拆解,
  **且**明确本节不构成'减法有效'的证据——两条都要满足, 缺一不可"。这不是含糊提一句。
- **但"循环"这个定性没有被写死**。§9 末段把它写成**审查方的一条待确认顾虑**:
  用的是"**若**当初是用同一条规则独立算出来的…**存在**同源自洽风险"的条件句;
  接着引 `EVENTS_V1_NOTES` §6 做了**半条反驳** ("这确实是一次独立实现");
  结论是"**本单元无法自行解决**——需要 team lead 直接向 Task 5 实现方确认", 并明写
  "**未擅自判定这条顾虑是否成立**"。
- 控制方现已查证裁定: 类型 6 的 gold 判据与 `collect_scope()` **逐字同构 (已读源码确认)**
  ⇒ 循环**成立**, 不是"若…则"。因此 §9 那段现在是**过期且方向相反**的: 它给后人留了一个
  "这条顾虑可能不成立"的口子, 还留了一条现在已经站不住的反驳。写这段时控制方尚未裁定,
  所以这不是当时的过错; 但**现在必须定稿改写**, 否则下一个引用者读到的是"悬而未决"。

**要求 (定稿一次即可)**: §9 那段改成陈述句 —— "控制方已查证: 类型 6 gold 判据与
`collect_scope()` 逐字同构, **5/5 精确属循环证据**, 不得单独引用为'减法有效'的证据;
支撑该结论的独立材料是 §6-13 的 Task 4 数据自洽复算"; 删掉"独立实现"那半条反驳与
"未擅自判定 / 需 lead 确认"的悬置措辞。§4 结论里那句括注 (指向 §9 的"顾虑") 一并同步。

---

## 第三部分 · 本轮新引入的破坏

### 🔴 Critical (新) — §3.1 / §6-4 的新归因对 4 题与实测相反, 是首轮 Critical-1 的同类复发

§3.1 新增了一段"归因纪律 (修复轮1教训, 不能再犯)", 声称对剩余 12 题**逐题跑过反事实核验**,
并给出结论:

> **`event_timing` 5 题 + `event_form_assignment` 剩余 4 题**: 逐题核验, gold 的全部锚点
> (event OID / activity OID / activity 名 / form OID, 视题而定) **均不在**题面里
> (9 题 × 各 2-3 个锚点, **全部 False**)。

我用同一判据独立逐题复核 (OID 走 `_bounded_contains`, 名称走 `_norm` 子串, 与代码同款):

| 题 | gold 粒度 | 命中的 gold 锚点 (形态) | §3.1 说法 |
|---|---|---|---|
| `ev_q01`–`ev_q05` | activity / assignment | **无** | ✅ 成立 |
| `ev_q06` | assignment | **活动名 `<NAME len=3>` + 事件名 `<NAME len=3>`**, 两者都 ≥ 索引阈值 | ❌ 不成立 |
| `ev_q07` | assignment | 事件名 `<NAME len=2>` (在题面里, 被 `_MIN_EVENT_NAME_LEN=3` 挡在索引外) | ❌ 不成立 |
| `ev_q08` | assignment | 事件名 `<NAME len=2>` (同上) | ❌ 不成立 |
| `ev_q09` | assignment | **活动名 `<NAME len=4>` + 事件名 `<NAME len=4>`**, 两者都 ≥ 阈值 | ❌ 不成立 |
| `ev_q16` / `ev_q20b` | event | **无** | ✅ 成立 |
| `ev_q17` | event | 事件名 `<NAME len=2>`, 阈值裁剪 | ✅ §3.1 已单独划出 |

**而且不止"锚点在题面里"—— 通道已经把它们查出来了:**

| 题 | 通道是否已返回 gold 自己的 `event:` | 是否已返回 gold 自己的 `activity:` |
|---|---|---|
| `ev_q09` | **是** | **是** |
| `ev_q06` | **是** (未截断口径; 截断后被砍掉, 见 B-3) | **是** (同上) |

所以这 4 题的真实成因**不是**"题面本身不含可索引的标识符", 而是 **Tier 3 (名称索引)
到 `assignment:` 粒度这条路径不存在** —— `_name_index` 结构上只产 `event:`/`activity:`
两种目标。这与 Ruling P2 修的是**同一个缺口**, 只是入口从 form OID 换成了可读名。
Ruling P2 只补了一半, 而 §3.1 把没补的那一半又写成了"问法本身超出精确匹配的能力范围"。

两处连带的假陈述:

- §3.1: "这不是索引维度缺失 (Ruling P2 已补齐 form 维度), 是问法本身超出精确匹配的能力
  范围" —— 对 `ev_q06`/`ev_q09` 是反的。
- §6-4: "Ruling P2 补齐了 form 维度后, 这批题里**'题面点名了 gold 标识符却仍答不出'的
  情形已经消除**" —— **未消除**, 4 题仍是这个形态 (2 题名称已被索引并已返回, 2 题名称
  被 2 字符阈值挡掉)。

补充一条方法层面的问题: §3.1 自己列的锚点清单是 "event OID / activity OID / activity 名 /
form OID" —— **漏了 event 名**。`ev_q07`/`ev_q08` 恰好就栽在这个漏项上; 而 `ev_q06`/
`ev_q09` 连清单里已有的 "activity 名" 都判成了 False, 说明那次"逐题反事实核验"本身没有
正确执行。同时 §3.1 专门为 `ev_q17` 划出了"**阈值裁剪掉了一个真实存在的锚点**, 与'题面本就
没有锚点'是两种不同性质"这条区分 —— 判断是对的, 但 `ev_q07`/`ev_q08` 是**同一形态**, 没有
一并划出。

**这条的严重性不在分数** (这 4 题在任何口径下都还是 miss), 而在于: 首轮 Critical-1 的表格
第一行第二行写的就是 `ev_q06`/`ev_q09` "gold 的 event 与 activity 两级都已返回", 本轮却在
"不能再犯"的标题下把同样两题重新归因成"题面没锚点"。**这正是首轮点名的错误方向: 把可用
确定性手段闭合的工程缺口, 记成不可修复的结构性限制。**

**要求**: (a) §3.1 把 `ev_q06`/`ev_q09` 从"无锚点"里摘出来, 如实写"gold 的事件名与活动名
都在题面里、通道也已返回对应的 `event:`/`activity:` 目标, 未命中的原因是名称索引产不出
`assignment:` 粒度"; (b) `ev_q07`/`ev_q08` 并入 `ev_q17` 那条"阈值裁剪"; (c) §6-4 删掉
"已经消除"那句, 改成"form OID 这一入口已补齐, **名称 → assignment 粒度这条入口仍缺**",
并明确这是一个**未完成项**, 不是结构性限制。

### 🟠 Important-新-1 — `ev_q06` 的输出质量净退步, 全文零披露

首轮审查方实测该题返回 **2** 条, 且那 2 条正是 gold 的 event 与 activity。本轮返回 **50**
条, 那 2 条被 cap 砍掉 (见 B-3), 顶替它们的是短 form OID 撞词带来的原始清单。分数不变
(两轮都 miss), 但对下游消费方 (这条通道的输出是要 union-add 进检索的) 是明确的退步。
§9 的逐条对照里只写了修复带来的增益, 没有任何一处写这个回退。

### 🟠 Important-新-2 — 聚合噪声量未披露, 只披露了类型 6 那 5 题

checkpoint 对返回件数的披露纪律只覆盖 §4 的 5 题 (yml 拘束要求的那批) + §6-6 的 2 个案例。
我算了本轮的全局形态:

- 33 题**共返回 259 条**目标, 其中与 gold 有交集的只有 **28** 条 ⇒ 全局 precision **10.81%**
- 12 个未命中题共返回 **157 条纯噪声**; 其中 **10/12** 由修复前的"返回空"变成"返回非空"
- 返回 ≥10 条的题有 **10** 个

Ruling P2 让 6 题转命中, 同时让这条通道在**大多数答不出的题上从"沉默"变成"自信地给一堆
错东西"**。§6-6 记了机制、举了 2 个案例, 但没有任何一处给出这个总量。以本仓对"引用必须
併記返却件数"的纪律标准, 只给类型 6 那 5 题是不够的。

### 🟡 Minor-新-1 — §9 的测试条数分解有一格与实测不符

§9 写 "`test_study_lookup_events.py` 从 7 条增至 **13** 条"。实测
(`pytest --collect-only`): **12** 条。总数 `1764 → 1780` (+16) 仍然成立
(12 + 4 + 2 − 2 = 16), 是分解那一格写错, 不影响总数。

---

## 红线扫描结果

| 扫描面 | 工具 | 结果 |
|---|---|---|
| 本轮改动的 8 个文件 + 首轮两份报告 | `scripts/oidscan_evidence.py` | **CLEAN (0 处)** |
| 本轮 diff 全文 `review-e71a2a1..6b54d6c.diff` | 同上 | **CLEAN (0 处)** |
| 上述全部文件 + diff, **补扫闸的盲区** | 自写 (needle = 68 个 len 2-3 的真实 event/activity/form/item 名称) | **0 处命中** |

**为什么要补扫**: `oidscan_evidence.py` 的 label/name 池**剔除 len < 4 的取值** (见其
docstring 的"判定规则"段), 而真实数据里有 3 个 `<NAME len=2>` 事件名、2 个 `<NAME len=2>`
活动名等共 68 个短名 —— 一个 2 字符真实事件名写进正文, 闸是抓不到的。本轮改动面恰恰反复
讨论"2 字符事件名被阈值挡住"这个话题, 是最容易手滑的位置。补扫 0 命中 ⇒ **实现者自述的
"草稿里手滑写进过 2-3 处真名, 已自查改掉"经独立复核属实, 没有漏网**, 含闸看不见的形态。

**唯一 LEAK, 不在实现者的改动面**: 控制方自己的 `.superpowers/.../progress.md`
(**gitignored**, 不进 git) 被闸报 **12 处**, 集中在 4 行 —— 那几行正是控制方在讨论"哪些
撞车词要进 allowlist"的段落, 形态是 `<OID len=2>`/`<OID len=3>`/`<OID len=5>` 的短
form/item OID。不进 git, 危害受限; 但按 §6-11(a) 本轮刚写进已知限制的那条纪律 ("报告类
中间产物也要过红线扫描, 不能只扫 git 追踪面"), 这是那条纪律自身的第一个反例, 建议控制方
自行处置 (或按闸的 ALLOWLIST 机制正式记账, 而不是靠"在扫描面外"侥幸清白)。

**本报告自扫** (按派发要求):

```
$ .venv/bin/python scripts/oidscan_evidence.py evidence/step_workflow_events_audit_review_r2.md
CLEAN: 0 处未在 allowlist 的 OID/label 命中 (1 个文件)
```
(自写短名补扫同样 0 命中 —— 结果附在下方复跑命令 (7))

---

## 措辞诚实度扫描

全文过 `验收通过|已支持|已证明|有效|证明|坐实|保证`:

- **「验收通过」「已支持」: 0 处。**
- **「已证明」1 处** (§9: "已证明 33/33 题在有 cap/无 cap 两种口径下命中判定完全一致")
  —— 该陈述**属实**, 我独立复现 (仅 `ev_q06` 真截断, 判定不变)。撑得住。
- **「有效」全部在引用/否定语境** (§4 反复写"不作为'减法有效'的证据"), 合规。
- **「证明」其余各处均为否定式** ("不能证明该盲区已被堵上"/"测试只能证明…不能让调用方
  分辨"), 是在收紧不是在放大。

**撑不住的 2 处**:

1. §2 加粗标题 **「验证: cap 从未挤掉结构化目标」** —— "从未"是全称断言, 支撑它的证据
   (33 题二值判定一致) 结构上看不见相关性损失, 而反例已经存在 (`ev_q06`, 见 B-3)。
2. §3.1 「9 题 × 各 2-3 个锚点, **全部 False**」与 §6-4 「'题面点名了 gold 标识符却仍答
   不出'的情形**已经消除**」 —— 见第三部分 Critical, 对 4 题与实测相反。

**值得肯定的三处** (与首轮相比是实打实的进步):

- §1 闸 D 那格没有把旧方法悄悄删掉, 而是**划着删除线保留 + 写明"是空闸"** —— 让后人看得见
  这里曾经错过, 比直接换掉更诚实。
- §4 对 yml 拘束的处理**比首轮建议的还严**: 标题改中性、两处独立写明不得引用、结尾把
  "併記件数"与"不构成证据"两条并列为必须同时满足, 堵死了"多报几个数字就解禁"的读法。
- §6-6 是**主动**把 Ruling P2 自己引入的新噪声源写成已知限制, 不是被指出后才补的。

---

## ⚠️ Cannot verify

1. **全量 `tests=1780 failures=0 errors=0`** —— 按派发指示未重跑; 只实跑了本轮改动的
   3 个测试文件 (25 passed)。
2. **`ev_q06` 首轮返回 2 条**这一点引自首轮审查方报告的实测表, 我未 checkout 父提交复现;
   但"那 2 条在当前 uncapped 输出里仍然存在、且被 cap 砍掉"是我本轮实测的。
3. **§5 的旧通道基线数字** (卡片 3/33 · doc 7/33 · 并集 9/33 · 语义核验后 3/33) 引自
   `EVENTS_V1_NOTES.md §11-6`, 本次未重跑 doc/卡片引擎复核; 出处已在 checkpoint 标注。
4. **闸 A 的四数与 ledger +209** —— 属抽检方分工, 本文未复算 (我复算的是闸 B 的 77、
   闸 C 的 82、闸 D 的 961、§6-8 的 10/110/11/0、§6-13 的 231/0)。
5. **类型 6 gold 与 `collect_scope()` 逐字同构** —— 采信控制方的裁定 (派发信写明"已读
   源码确认"), 本文未自行读 Task 5 的出题脚本复核。

---

## 复跑命令 (本文全部实测均可复现)

```bash
cd /Users/bojiangzhang/MyProject/sdtm-pedia/sdtm-rag

# (1) 闸 D sha256 961/961
.venv/bin/python - <<'PY'
import json, hashlib, pathlib
man = json.loads(pathlib.Path('../.superpowers/sdd/2026-08-25-study-workflow-events/cards_post_t1.sha256.json').read_text())
cur = {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in pathlib.Path('data/study/st01/cards').glob('*.md')}
k = {pathlib.Path(a).name: b for a, b in man.items()}
print(f"identical={sum(1 for a,b in k.items() if cur.get(a)==b)} changed={sum(1 for a,b in k.items() if a in cur and cur[a]!=b)} n={len(k)}")
PY

# (2) 本轮改动的三个测试文件 (25 passed) 与条数
.venv/bin/python -m pytest scripts/tests/test_study_lookup_events.py \
  scripts/tests/test_collect_scope.py scripts/tests/test_catalog_workflow_pools.py -p no:warnings -q
.venv/bin/python -m pytest <同上三文件> -q --collect-only | tail -4    # events=12 (§9 写 13)

# (3) A: 避让丢目标的规模与端到端复现   —— scratchpad/r2/p2.py · p3.py
#     p2 输出: 231/959 个 item 的 Tier2 是 Tier1b 的真子集, 涉 7/21 form, 单次最多丢 39 条
#     p3 输出: 只点名 form → 40 条; form + 同 form 一个 item → 1 条; 差集 39 条全是 assignment:

# (4) A: 四种边界的合成 fixture 实测        —— scratchpad/r2/p6.py (全部伪值)
#     多 form 独立避让 ✓ / 只点 item 不 fire Tier1b ✓ / 同 OID 跨 form 连坐 ✓ / scope 空不避让 ✓

# (5) B: 构造触发 cap 的输入验证优先级      —— scratchpad/r2/p8.py
#     uncapped 70 → capped 50, Tier2 12/12 保留, 被砍全是 Tier1b/Tier3
#     加 Tier3 后 uncapped 74 → Tier3 4 条保留 0 条, Tier2 仍 12/12
#     两大 form 同框 58 → 50, 被砍 8 条全落在一个 form (层内插入序截断)

# (6) B/Critical: 逐题拆层 + ev_q06 的 cap 相关性损失  —— scratchpad/r2/p4.py · p14-p17.py
#     p4  : 21/33; 避让触发 5 题共压 66 条; 因避让丢 gold 的题 = 0; cap 截断 1 题, 判定一致
#     p14 : 12 个未命中题的 gold 锚点核验 → q06/q07/q08/q09 各有 gold 名称锚点在题面里
#     p16 : q09 已返回 gold 的 event: 与 activity:; q06 同样 (未截断口径)
#     p17 : ev_q06 uncapped=60 capped=50, gold 的 event:/activity: 在 uncapped 里 True、capped 里 False

# (7) 红线: 官方闸 + 短名补扫
.venv/bin/python scripts/oidscan_evidence.py \
  evidence/checkpoints/study_workflow_events.md server/study_lookup.py \
  scripts/study/collect_scope.py scripts/tests/test_study_lookup_events.py \
  scripts/tests/test_collect_scope.py scripts/tests/test_catalog_workflow_pools.py \
  ../.superpowers/sdd/2026-08-25-study-workflow-events/task-6-report.md \
  "../.superpowers/sdd/2026-08-25-study-workflow-events/review-e71a2a1..6b54d6c.diff"   # CLEAN
.venv/bin/python scripts/oidscan_evidence.py evidence/step_workflow_events_audit_review_r2.md  # CLEAN
#     短名补扫 (68 个 len 2-3 真实名称当 needle) —— scratchpad/r2/p12.py → 0 命中

# (8) checkpoint 数字复算 —— scratchpad/r2/p13.py
#     §6-13: 231 / 0 ✓   §6-8: 10 / 110 / 11 / 0 ✓   §2: 单 form 40 / 单 item 40 ✓   闸C: 82 ✓
```

---

## 建议处置顺序

1. **Critical (新)** —— §3.1 的 4 题归因 + §6-4 的"已经消除"必须改 (第三部分给了逐条改法)。
   这是唯一一条"证据文件对后人说了假话"的问题。
2. **C-①** —— §9 的同源自洽段按控制方裁定定稿, 删掉悬置与已失效的反驳。改一段。
3. **A 的避让缺陷** —— 至少把"命中不丢"这句的适用范围写进 §6 (对 form 级问法不成立);
   代码改成"逐条相减"是更好的解, 但属新一轮工作, 由控制方决定是否本轮做。
4. **B 的措辞与披露** —— §2 标题的"从未"改成有界陈述 + 补 `ev_q06` 的相关性损失 + 补
   Tier 1b 层内插入序截断。
5. **Important-新-2** —— 补一段全局返回量 (259 / 28 / 10.81% / 12 题 157 条噪声)。
6. **Minor-新-1** —— §9 的 "13 条" 改 "12 条"。

**代码没有需要回退的东西。** 本轮的实现修复 (Ruling P2 + 三层优先级 + 有界匹配 + cap 重定义
+ 两条新闸 + 两处 Minor 修复) 全部是真做的、可复算的、带测试的; 问题集中在**新写的归因段落
超出了证据**, 以及**修复只做了缺口的一半却按"已经消除"结账**。
