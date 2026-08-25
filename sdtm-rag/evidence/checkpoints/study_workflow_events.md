# Task 6: study_lookup 事件通道接线 — 收口证据

> 日期: 2026-08-26 (修复轮2) · 分支 `feat/study-workflow-events` · 计划:
> `.superpowers/sdd/2026-08-25-study-workflow-events/task-6-brief.md`
> 数据红线: 本文件进 git, 零真实 OID / label — 全部用题号 (`ev_qNN`) + 计数 + 形态指代
> (与 `test_catalog_workflow_pools.py` 的红线约定同款)

## 0. 一句话结论

`StudyLookup.resolve_events(query)` 四层拼接: Tier 1a (event/activity OID 精确命中) →
Tier 2 (item OID 命中 → `collect_scope` 减法, 消费 Task 4 推导, 解决 M4/M5) → Tier 1b
(form OID → 该 form 全部 assignment 原始清单, 修复轮1新增, Ruling P2) → Tier 3 (名称
子串, 最弱, 排最后)。33 题 event gold 子串口径实测 **21/33 = 63.64%** (剔除 3 题已知
泄漏题后净额 19/30 = 63.33%, 见 §3.2), 逐题清单见 §3, 12 题未命中按机制分三桶
(§3.1, 修复轮2 重新核验修正)。**全局 precision 仅 10.81%** (259 条返回里只有 28 条
对得上 gold, 见 §6-15) ——Ruling P2 让 6 题转命中的同时也让通道在大多数答不出的题上
从"沉默"变成"返回一堆错的", 这个代价必须和命中率一起引用。卡片侧 (study golden v2)
三遍复测 **87.50% 逐题 Δ0**, 无回归。测试 1764 → **1780** (净 +16), 0 failed 0 error。
**规则 D 已完成两轮核验**: 首轮 (抽检方+审查方, 1 Critical·4 Important·3 Minor, 见 §9)
驱动了 Ruling P2 等核心修复; 第二轮 (审查方, 1 Critical·3 Important·1 Minor, 报告落盘
`evidence/step_workflow_events_audit_review_r2.md`) 抓到首轮修复后归因错误同类复发
(§3.1 已按第三次核验修正)、`ev_q06` 净退步与全局噪声未披露 (§6-14/15 已补)、类型6
gold 同源关系应予定稿而非悬置 (§9 已改陈述句), 另发现 Tier 1b 避让逻辑边界与 cap 全称
断言的措辞问题 (§6-16/§2 已修)。全部已处置, 见 §9b/§10, 本文档收口。

## 1. 各闸实测值

| 闸 | 判据 | 实测 |
|---|---|---|
| A (spec §5.A 四数交叉核对) | `test_gate_a_cross_check_against_design_summary` + `test_three_pools_exist_with_expected_sizes` | assignments=110 / form_oid 去重=21 / event_type 分布 sorted=[1,109] — **全部吻合, PASS** |
| B (spec §5.B 引用完整性四条 + activity OID 全局唯一) | `test_gate_b_referential_integrity` + `test_activity_oid_globally_unique` (**修复轮1新增**) | 4 条差集长度全部 = 0; activity OID 77 个互异 (77=77) — **PASS** |
| C (spec §5.C 转置一致性) | `test_gate_c_transpose_consistency` + `test_gate_c_transpose_consistency_form_aware` (**修复轮1新增**) + `test_hidden_activities_subset_of_activities` | 按 activity 键: fwd 键数=61, 双向键集合对称差=0, 双向不匹配数=0; 按 (activity,form) 二元键 (**更严格**): 82 键, 同样双向对称差=0/不匹配数=0; 隐藏清单侧 activity 去重数=61 — **PASS**。⚠ **`61` 本身是回归锁, 不是独立判别力来源** —— 判别力来自 `set(fwd)==set(bwd)` 与 `mismatched==[]` 两处独立导出 (fwd 出自 assignments 池、bwd 出自 items 池, 两份数据分别由 Viedoc 导出) 的互证, 61/82 这两个数字只是"这次复算是否还是同一个值"的稳定性快照, 单独变了不等于闸失效, 两处独立互证若对不上才是真出问题 |
| D (卡片侧不回归) | ~~`git status` 查 `data/study/st01/cards/`~~ (**修复轮1替换** — 该目录 gitignored, `git status` 恒空, 是**空闸**, 卡片改没改都一样, 已被审查方指出); 改用 **sha256 逐文件复算** 对照 `cards_post_t1.sha256.json` (Task 1 后留在 workspace 的指纹清单) + study golden v2 三遍复测 | sha256: **961/961 文件名与哈希逐字节相同** (文件集合完全一致, 无新增无删除无改动); `source_recall_avg=0.875` 三遍逐题一致, 与冻结基线 `v2_baseline_s2on.json` 的 87.50% 相符, Δ0 — **PASS** |
| E (event gold lint) | `eval.lint_gold --events-catalog` | `0 条 gold 未唯一定位`, exit=0 |

复跑命令 (均已本会话实测, 非引用旧数字):
```bash
cd sdtm-rag
.venv/bin/python -m pytest scripts/tests/test_catalog_workflow_pools.py -p no:warnings -q   # 9 passed (7原+2新)
.venv/bin/python -m eval.lint_gold data/study/st01/eval/test_set_events_v1.yml --events-catalog data/study/st01/catalog.json   # exit=0
.venv/bin/python -m eval.run_eval data/study/st01/eval/test_set_study_v2.yml \
  --retrieval-only --hybrid --study-lookup \
  --collection study_st01 --kb-root data/study/st01/cards --output /tmp/run.json   # ×3, 逐题比对
# 闸 D sha256 复算 (示意, 实际用一次性脚本对比 cards_post_t1.sha256.json 全部 961 项):
python3 -c "
import json, hashlib, pathlib
manifest = json.loads(pathlib.Path('../.superpowers/sdd/2026-08-25-study-workflow-events/cards_post_t1.sha256.json').read_text())
current = {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in pathlib.Path('data/study/st01/cards').iterdir() if p.is_file()}
print('keyset equal:', set(manifest)==set(current))
print('identical:', sum(1 for k in manifest if current.get(k)==manifest[k]), '/', len(manifest))
"
```

## 2. Ruling P2 修复: form→assignment 索引 + 三层优先级 (修复轮1核心修复)

**问题 (审查方定位)**: 本单元最初实现只索引 event/activity 的 OID/名称, 未索引
`assignments` 池的 form_oid 维度。`event_form_assignment`/`repeating_rule` 两类问法
(10 题) 的 gold 是 `assignment:` 类型目标, 其中不少题面**逐字点名了 gold 所在的 form
OID**, 但旧实现对 form OID 视而不见, 导致这两类结构性 0/10——不是"这类问法答不出",
是索引缺了一个维度。四条反证 (审查方独立复核): 4 题的 gold form OID 本来就逐字在题面
里, 仍然答不出。

**修复**: 新增 `_form_assignment_index` (form_oid 有界匹配 → 该 form 全部 assignment
原始清单, **不做** item 级减法——"这个表单被分配到哪些活动"是表单级事实, 与 Tier 2 的
"某个具体 item 实际在哪采集"是不同判据)。真实数据 21 个 form_oid 里 7 个只有 2 字符,
用裸子串误召回风险不可接受, 改用有界匹配 (`_bounded_contains`, 两侧非 ASCII 字母/数字/
下划线)。

**连带修复 (审查方要求, 与 Ruling P2 同批做)**:

1. **三层优先级拼接**: 若不分层、按索引遍历顺序简单拼接再截断, 名称子串这类较弱信号会
   排在结构化目标**前面**抢占 cap 名额——已实测复现两个独立案例: 修复前 `ev_q30` 一题
   未截断即达 4 条, 3 条是名称索引段的巧合命中, 排在有效目标前面; 审查方独立复现的更直接
   案例——修复前 `ev_q02` 一题未截断的原始返回是 **14 条**, 被旧 cap (8) **实际截断**到
   8 条 (该题本身 gold 不在返回集合任何位置, 未改变判分, 但证明截断不是纸面风险, 真实
   数据上已经发生过)。现按 **Tier 1a (OID精确) → Tier 2 (结构化推导) → Tier 1b (form
   原始清单) → Tier 3 (名称子串)** 拼接, 同层/跨层均去重, 最后统一截断。
2. **Tier 1b 对 Tier 2 已覆盖的 form 让位**: 修复过程中新发现的连带问题——类型6的题面
   常常**同时**点名 item OID 与其所属 form OID (如 `ev_q27` 问某 item 的采集范围, 题面
   同时写出该 item 所属 form 的可读名), 若 Tier 1b 不避让, 该 form 的几十条未减法原始
   清单会把 Tier 2 的精确减法结果淹没在同一层里, precision 暴跌 (实测: 不做避让时
   `ev_q27` 从 tp=7/fp=0 退化到 tp=7/fp=25)。现记录本次查询里 Tier 2 已经算出非空减法
   结果的 form 集合, Tier 1b 对同一 form 的原始清单**整个跳过**。
   ⚠ **修复轮2 审查指出这个"整 form 让位"不是无损操作** (§6-16 详述): Tier 2 的结果按
   定义是该 form 全量的**子集**, 让掉的差集没有其他层会补回来, "命中不丢"只在 gold
   恰好落在 Tier 2 那个子集里 (即题面问的是 item 采集范围) 时成立——对 form 级问法
   (`event_form_assignment`/`repeating_rule`, 正是本轮 Ruling P2 要服务的那两类) 不
   成立。真实数据 231/959 个 item 触发此情形 (涉 7/21 个 form), 当前 33 题未因此丢过
   gold, 但这是设计上的真实缺陷, 不是"当前无害"能定性的; 更稳妥的解是"逐条相减"而非
   "整 form 让位", 本轮未做 (团队 lead 明确本轮"定稿披露, 不加新功能"), 留作后续工作。
3. **有界匹配替代裸子串**: 短 OID (2-3 字符) 裸子串在题面里误召回风险高, 且 `_norm` 去
   空白正规化会把被空格隔开的两个 token 人为拼接、扭曲边界判断 (实测案例: 某题面里一个
   3 字符 item OID 后本有半角空格再接数字, 去空白后 OID 紧贴该数字, 边界失真)。改用保留空白的
   `_norm_ws` + 双侧非 ASCII 字母/数字/下划线的正则边界, 事件/活动/form/item 四类 OID
   精确匹配统一走这条路径。
4. **cap 语义与取值重新论证**: `_MAX_EVENTS_TOTAL` 从 8 改为 **50**。旧值 8 是从
   `resolve()` 的卡片场景抄来的**诊断质量闸**语义 (匹配集合太大=不具判别力, 直接跳过整个
   匹配)——这个语义在 `resolve_events` 不成立: "一个 form 合法地对应几十条 assignment"
   是数据的正常形态, 不是匹配质量差的信号 (实测: 单个 form 最多挂 40 条 assignment, 单个
   item 的 `collect_scope` 最多算出 40 条, 均为真实值)。新 cap 定位是"防真正失控的输出
   量级"的安全阀, 不是诊断闸, 阈值覆盖到实测最大单次命中(40)之上留出余量。

**验证 (措辞已按修复轮2审查订正为有界陈述, 不再用"从未"这种全称断言)**: 对全部 33 题
分别计算"加 cap 截断"与"完全不截断"两个版本的 hit/miss 结果, **33 题上 cap 未改变
任何一题的命中判定**——这句话本身复算属实, 但**判定不变不等于"结构化目标没有被挤掉"**,
两者是不同的断言, 上一版把后者当前者的证明是过强的:

- `ev_q06` 是一个真实反例: 该题未截断 (60条) 时, gold 自己的 `event:`/`activity:` 目标
  **都在**返回集合里 (虽然粒度不够, 本就不算 source-recall 命中); 截断到 50 条后,
  这 2 条**被挤出去了**, 顶替它们的是两个与本题无关的短 form OID (§6-6 已记的撞词
  案例) 触发的 Tier 1b 原始清单。噪声排在信号前面这件事**没有被完全消除**, 只是从
  修复轮1前的"Tier 3 排在 Tier 1a/2 前面"这种**跨层**问题, 转移成了"Tier 1b 的体量
  压过 Tier 3 的正确命中"这种**层间体量**问题——三层优先级本身是生效的 (Tier 1a/2
  从未被 Tier 1b/3 挤过, 已用合成 fixture 反例证实: 两个大 form + 一个第三方 item 同框
  时, Tier 2 的命中 100% 保留, 被砍的全是 Tier 1b/3), 但优先级只保证"更精确的层不被
  更弱的层挤", 不保证"某一层内部按题目相关性排序"——若某层 (如 Tier 1b) 单次贡献的
  体量远超其他层, 它依然可以把**另一层**(Tier 3) 里真正对这道题有用的命中挤出总 cap。
- **Tier 1b 层内部的截断顺序是 `_form_assignment_index` 的 dict 插入序** (即 catalog 里
  assignments 的原始行序), **不是相关性序**: 当两个大 form 同时被命中且合计超过 cap
  时, 哪个 form 的条目被砍纯粹取决于它在 catalog 里排在前面还是后面, 与题目实际问的
  是哪个 form 无关。当前 33 题里这个现象已发生 (`ev_q06` 的两个无关 form 合计 58 条,
  截断到 50, 被砍的 8 条全部落在其中一个 form)。

**已核实、结论不变的部分**: cap=50 在当前 33 题上确实**没有改变任何一题的最终命中/
未命中判定** (`ev_q06` 本身无论截不截断都是 miss), 这个具体、有界的结论仍然成立且
已复算; 但不能引申为"cap 机制本身不会造成相关性损失"这个更强的主张。

**修复轮1前后对照**:

| | 修复轮1前 | 修复轮1后 |
|---|---|---|
| 总分 | 15/33 = 45.45% | **21/33 = 63.64%** |
| event_timing | 0/5 | 0/5 (无关: 这类问法的答案本就不在题面里, Ruling P2 不涉及) |
| event_form_assignment | 0/5 | **1/5** (仅 1 题的 gold form OID 逐字在题面里) |
| repeating_rule | 0/5 | **5/5** (全部 5 题的 gold form OID 均逐字在题面里) |
| conditional_event | 4/7 | 4/7 (不变, Ruling P2 不涉及这类) |
| oid_name_mapping | 6/6 | 6/6 (不变) |
| item_collection_scope | 5/5 | 5/5 (命中数不变, **但总返回集合的噪声增加**, 见 §4) |

## 3. Step 6 实测: 33 题 event gold 命中率 (子串口径, 非 judge — §11-5 钉死)

**总分: 21/33 = 63.64%**

| 类别 | 命中/总数 |
|---|---|
| event_timing (q01-05) | 0/5 |
| event_form_assignment (q06-10) | 1/5 |
| repeating_rule (q11-15) | 5/5 |
| conditional_event (q16-20c, 7题) | 4/7 |
| oid_name_mapping (q21-26) | 6/6 |
| item_collection_scope (q27-31) | 5/5 |

### 3.1 逐题未命中清单 (12 题)

`ev_q01 ev_q02 ev_q03 ev_q04 ev_q05` (event_timing 全 5 题) ·
`ev_q06 ev_q07 ev_q08 ev_q09` (event_form_assignment 4 题, `ev_q10` 已修复转为命中) ·
`ev_q16 ev_q17 ev_q20b` (conditional_event 3 题)

⚠ **归因纪律 (修复轮1教训, 修复轮2里同类问题复发过一次, 已改用比对方法而非手感)**:
修复轮1前的版本把 15 个未命中里 10 个笼统归因为"题面不含答案锚点", 被抽检方逐题反事实
推翻 (Critical-1)。修复轮1后我对剩余 12 题重做过一次逐题核验, 但**归因方法本身仍有缺陷,
修复轮2审查再次抓到 4 题被错误分类** (`ev_q06`/`ev_q09`/`ev_q07`/`ev_q08`)——上一版的
锚点清单漏列了"event 名"这一项, 且对已在清单里的"activity 名"两题都判成了 False (实际
是 True)。本节是第三次核验, 逐题用独立脚本对**每一类锚点** (event OID / event 名 /
activity OID / activity 名 / form OID) 分别检查是否以有界形式出现在归一化题面里, 并额外
检查通道对每题实际返回了什么, 按三种性质分桶 (而不是一句"结构性"笼统带过):

**桶 1 — 真正"题面无任何锚点"(7 题: `ev_q01`/`ev_q02`/`ev_q03`/`ev_q04`/`ev_q05`/
`ev_q16`/`ev_q20b`)**: 逐题核验, gold 的全部锚点**均不在**题面里 (7 题 × 各 2-3 个
锚点, 全部 False)。这批的题面 (Task 5 修复轮1白送分闸后) 刻意不点名可读名/OID, 只描述
"最多几个疗程"/"最远时点"这类需要**比较/聚合/枚举**才能得出答案的开放问法——
`resolve_events` 是精确匹配, 没有可以匹配的字面串, 是问法本身超出精确匹配的能力范围,
不是索引维度缺失。

**桶 2 — 锚点存在但被 `_MIN_EVENT_NAME_LEN=3` 阈值裁剪 (3 题: `ev_q07`/`ev_q08`/
`ev_q17`)**: 三题的 gold 事件**可读名均以有界形式出现在题面里**, 但均只有 2 字符,
被 `_MIN_EVENT_NAME_LEN=3` 挡在索引门外——是**阈值裁剪掉了一个真实存在的锚点**, 与桶 1
"题面本就没有锚点"是两种不同性质的未命中。未调整该阈值 (2 字符名称索引误召回风险高,
权衡后维持现状), 只做归因区分记录。

**桶 3 — 锚点存在且高于阈值, 但通道结构上产不出 gold 的目标粒度 (2 题: `ev_q06`/
`ev_q09`)**: 这两题的 gold 都是 `assignment:` 类型, 而两题的 gold 事件**名与活动名都
以有界形式出现在题面里、且长度均 ≥3** (不受阈值裁剪)。`ev_q09` 上通道确实把 gold 的
`event:`/`activity:` 目标都返回了 (只是粒度比 gold 粗一级, 判 miss); `ev_q17` 那条
"阈值裁剪"区分法不适用于这两题——它们的问题不是锚点被挡, 而是**名称索引 (Tier 3) 结构上
只产 `event:`/`activity:` 两种目标, 没有任何路径能把名称命中换算成 `assignment:` 粒度**
(这条路径与 Tier 2 的 item OID → `collect_scope` 减法不同源, 后者只在题面出现 item OID
时触发)。`ev_q06` 上情况更复杂, 通道甚至**没有**返回 gold 的 `event:`/`activity:` 目标——
机制见 §6-14 (Important-1): 题面里另外提到的两个**无关**表单 OID 触发 Tier 1b, 产出的
噪声量把本该正确的 Tier 3 命中挤出了 cap, 这是本轮修复带来的一个新退步, 单独记录。
把这两题归为"结构性无锚点"是不准确的——正确说法是"名称→`assignment:` 这条索引入口
本身缺失", 是一个**未完成项**, 不是数据/题面层面的限制 (§6-4 已同步修正)。

### 3.2 三题归因 (q08 / q28 / q30, 已知信息泄漏题, 通道命中/未命中与净额分开报)

三题的 `expected_facts` 字面陈述在 protocol 文档正文里被发现存在, 卡片/doc 通道对这三题
存在已知的部分泄漏命中。事件通道实测各自的命中情况**与卡片/doc 侧的泄漏机制完全不同源**
(修复轮1后 `ev_q08` 的返回数从 0 变为 1, 结论仍是未命中, 已重新核实并更新):

| 题 | 事件通道 (`resolve_events`) | 卡片/doc 侧已知泄漏 |
|---|---|---|
| `ev_q08` | **未命中** (返回 1 条噪声, 系一个 2 字符 form OID 恰好是 gold 所属事件 OID 的词根, Tier 1b 误召回——不是本题真正的 gold form; 事件层对这题**没有**卡片/doc 侧那条泄漏) | 卡片侧 + doc 侧均命中 (跨表单脚注 / 评估条目列表) |
| `ev_q28` | **命中** — 返回集合里含 gold, 经由 item OID 精确匹配 → `collect_scope` 减法算出 (真实结构化推导, 不是文本巧合命中); 同批还混入若干条与本题无关的噪声 (§4 详述), 但命中路径本身与卡片/doc 侧机制无关 | 仅 doc 侧命中 (章节定义正文) |
| `ev_q30` | **命中** — 返回集合里含 gold, 同样经由 item OID → `collect_scope` 算出; 另混入少量其他类型噪声条目 (§4) | 仅 doc 侧命中 (评估条目列表同段落) |

**结论**: `ev_q08` 上, 事件通道与卡片/doc 侧的已知泄漏**不同源不叠加**——事件层对这题
没有该泄漏。`ev_q28`/`ev_q30` 上, 事件通道确实命中, 且**命中机制是 collect_scope 结构化
推导**, 与卡片/doc 侧文本共现型泄漏是两种不同性质的命中路径。

⚠ **口径更正 (修复轮1, 审查方 Minor-3 指出的自相矛盾)**: 上一版此处标题写"单列不进总分",
但正文同时写"未被抽出另算"——两句自相矛盾, 且实情是后者: `ev_q28`/`ev_q30` 这 2 个命中
**确实计入了** §3 的 21/33 总分 (它们各自落在 `event_form_assignment`/`item_collection_
scope` 类别桶里, 未被抽出)。按 yml「算事件层增益时这三题单独列出、不混进总分」的要求,
正确做法是**把净额也摆出来**, 而不是声称总分"不含"它们:

- **含三题总分 (§3 headline)**: 21/33 = 63.64%
- **净额 (剔除 `ev_q08`/`ev_q28`/`ev_q30` 三题后)**: **19/30 = 63.33%**

两者相差仅 0.31 个百分点——说明这 3 题对 21/33 这个总分的贡献很小, **不是靠已知泄漏题撑
起来的**, 但净额数字本身必须摆出来供引用者核对, 不能只报一个含糊的"总分", 也不能声称
"不含"这 3 题的贡献。

## 4. 类型6 (item_collection_scope, q27-31) 返回件数与 precision 实测

⚠ **本节标题措辞已按审查方 §答2 修正**: yml file header 拘束原文是「この5題の結果を
『減法が効いている証拠』として引用することは**禁止**」——併記返却件数是**附加**要求,
不是解禁条件, 上一版标题"减法是否真的有效"与结论句"5/5 题的答案都是**是**"读起来像
"限定后的有效结论", 而拘束禁的是"有效结论"本身, 不论有没有限定。本节**不作为**"类型6
减法有效"的证据, 只报返回件数与 tp/fp 拆解 (真正独立于这 5 题、能佐证减法机制本身的
证据是 Task 4 数据自洽复算, 见 §6-13)。

**拘束条件**: 引用这 5 题证明"减法有效"必须同时报出通道实际返回件数。修复轮1的 Ruling
P2 (form 维度索引) 对这 5 题产生了**直接的连带影响**——必须一并披露, 不能只报修复轮1前
的数字:

| 题 | 总返回数 | tp | fp | gold 集合大小 | exact_set_match |
|---|---|---|---|---|---|
| `ev_q27` | 21 | 7 | 14 | 7 | 否 |
| `ev_q28` | 15 | 1 | 14 | 1 | 否 |
| `ev_q29` | 2 | 2 | 0 | 2 | **是** |
| `ev_q30` | 4 | 1 | 3 | 1 | 否 |
| `ev_q31` | 1 | 1 | 0 | 1 | **是** |

**逐题机制核查 (修复轮1后重新核实, §2 的 Tier 2 避让 Tier 1b 已生效, 但仍有残留噪声,
逐一定位来源)**:

- **目标 item 自身的 `collect_scope` 减法本身仍然精确, 5/5 不变**: 每题里真正对应题面
  所问 item 的那次减法调用, 结果与 gold 逐条集合相等 (tp=gold, fp=0)——这一点是 Tier 2
  避让 Tier 1b 生效的直接证据: 若避让失效, 目标 item 自身所在 form 的原始清单会把这个
  精确结果也弄脏, 但实测 tp 始终等于 gold 大小, 说明"目标 item 所在 form"这一维度的
  串扰已被挡住。
- **`ev_q27`/`ev_q28` 的残留 fp (各 14 条) 来自一个共同、与本题无关的 form**: 题面里
  除了目标 item 与其所属 form 外, 还**恰好**含有一个通用医学缩写词, 该词同时是 catalog
  里一个**不相关** form 的 OID (2-3 字符)。这个 form 不在 Tier 2 的"已覆盖 form"集合里
  (因为触发它的不是某个具体 item, 而是 form OID 本身的字面撞车), 所以 Tier 1b 的避让
  逻辑对它不生效, 该 form 的全部原始 assignment 原样进入结果。这与 `ev_q27`/`ev_q28`
  本身"减法是否有效"无关——是 Ruling P2 新增的 Tier 1b 索引带来的**新的、独立的**已知
  限制 (短 form OID 兼作通用词汇), 已记入 §6。
- **`ev_q30` 的残留 fp (3 条) 来源不变**: 仍是事件/活动名称索引段 (Tier 3) 对题面里另一
  个通用词的独立命中, 与 Ruling P2 无关, 修复轮1前后表现一致。
- **`ev_q29`/`ev_q31` 保持精确 (exact_set_match)**: 这两题的题面不含任何触发无关 form/
  event/activity 名称索引的通用词, 修复轮1的连带影响对它们不生效。

**结论 (中性措辞, 不作"减法有效"的证据)**: 目标 item 自身的那次 `collect_scope` 调用,
其结果与 gold 逐条集合相等 (5/5 题 tp=gold, fp=0)——修复轮1的改动 (Tier 2 避让 Tier 1b)
没有改变这一点, 若避让逻辑本身有 bug, 这里的 tp 会跌破 gold 大小, 但没有, 这是该避让逻辑
正确性的一项旁证, **不是**对减法规则本身"是否有效"的独立验证——类型6 gold 判据与
`collect_scope()` 逐字同构 (团队 lead 已查证定稿, §9), 5/5 逐条相等属循环证据。同时,
**本节的返回件数与 tp/fp 数据本身不得
被引用为"减法有效"的证据** (yml 拘束禁止, 不因为多报了几个数字就解禁): fact-recall/
source-recall 均无 precision 惩罚这个结构性盲区依然成立, 且 Ruling P2 引入的 form 级
索引又新增了一条独立的噪声来源 (短 form OID 兼通用词)。**引用本节时必须完整带出返回件数
与 tp/fp 拆解, 且明确本节不构成"减法有效"的证据——两条都要满足, 缺一不可。**

## 5. 旧通道基线对照 (Fix 4, 便于判断 21/33 是高是低)

同一批 33 题在**旧通道** (S4 卡片侧/doc侧检索探针, 语义核验后) 的表现 (记录于
`EVENTS_V1_NOTES.md` §11-6): 卡片侧 3/33 · doc 侧 7/33 · 并集 9/33 (自动化代理原始值);
**语义核验后真阳性并集 3/33 ≈ 9.1%** (仅 `ev_q08`/`ev_q28`/`ev_q30` 三题, 即 §3.2 讨论
的已知泄漏题)。

⚠ **口径警告 (必须一并声明, 不可只引数字对比)**: 旧通道那组数字是 **fact-recall**
(检索到的文本正文是否含 `expected_facts` 字面串), 本单元的 21/33 是 **source-recall**
(`resolve_events` 返回的目标标识是否与 `expected_sources` 有交集)——两者判据对象不同
(一个测"文本里有没有这句话", 一个测"是否指对了那条数据记录"), **不能直接相减或换算成
"增益 X 个百分点"**, 只能做方向性对照。在这个限定下: 21/33 (source-recall) 相对旧通道
语义核验后的 3/33 (fact-recall) 是明显更高的覆盖面, 说明这条新通道把旧通道结构性答不出
的一大片问题变成了"至少能定位到正确的数据记录"——但不能引用为"事件层比旧通道好 6 倍"
这种跨口径的换算表述。

## 6. 已知限制

1. **`Scheduling::Days/After/recurrence` 与 `Timing::*` 本研究全空**, 时点语义承载在
   `Activity name` 自由文本 —— "结构化调度"在本研究数据里不成立 (spec §2 定的能力边界
   不包含发明一个不存在的结构化字段)。
2. **脚注/隐藏清单判据是启发式** (ID 以逗号/换行分隔的自由文本列, 非强类型字段), 换
   研究/换版本可能失效, 目前只靠闸 A 的四个数字 + 闸 C 的转置一致性 (含修复轮1新增的
   form-aware 82/82 版本) 看守, 无独立第二参照物。
3. **`resolve_events` 是精确/有界键匹配, 与 `resolve()` 的四通道 (label 子串/token 段/
   交集/别名) 不同源**, 两者未做过挤占分析 (是否会互相抢卡片/抢目标名额未测)。
4. **12 题未命中按机制分三桶** (§3.1 详述, 修复轮2审查后重新核验并区分): **桶1 (7题)**
   题面确实不含任何可索引锚点, 需要生成式能力 (读数据后归纳/比较), 与 `resolve_events`
   的确定性精确匹配设计目标 (spec §2 明确"零 LLM") 根本冲突, 不是可调参修复的缺口。
   **桶2 (3题)** 锚点存在但被 `_MIN_EVENT_NAME_LEN=3` 阈值裁剪。**桶3 (2题,
   `ev_q06`/`ev_q09`) 是一个未完成项, 不是结构性限制**: Ruling P2 补齐了 form OID 这一
   入口, 但**名称 (event/activity 可读名) → `assignment:` 粒度这条入口仍然缺失**——
   Tier 3 (名称索引) 结构上只产 `event:`/`activity:` 两种目标, 没有任何路径能把名称
   命中换算成 `assignment:` 目标。这两题的 gold 事件名/活动名确实逐字在题面里 (`ev_q09`
   上通道甚至已经返回了对应的 `event:`/`activity:` 目标, 只是粒度不够), **"题面点名了
   gold 标识符却仍答不出"这个具体缺陷未被 Ruling P2 完全消除, 上一版声称"已经消除"是
   错误的**——只有 form OID 这一条入口被消除, 名称这条入口没有。⚠ **本轮刻意不实现
   这条入口**: 全局 precision 已经只有 10.81% (§6-14), 补一个新的扇出入口大概率进一步
   拉低 precision, 是否值得加需要用数据权衡, 不是"漏了就补"的反射性动作, 记为未完成项
   留给下一轮决策。
5. **类型6 (item_collection_scope) 的减法盲区** (§4 详述): fact-recall/source-recall
   均无 precision 惩罚; 本次实测目标 item 自身减法精确 (5/5), 但 Ruling P2 新增的 form
   索引对 2/5 题引入了新的、与减法本身无关的噪声来源, 不能证明"整表返回不做减法也满分"
   这个结构性盲区已被工程手段堵上。
6. **短 form OID 兼作通用医学词汇, 造成 Tier 1b 误召回** (Ruling P2 引入的**新**限制,
   §4 实测复现): form_oid 词汇表里的短值 (2-3 字符) 有一定概率与研究领域的通用缩写词
   撞字面——这类撞车不是 Ruling P2 实现的 bug, 是"用短标识符做精确匹配"这个设计本身在
   小词汇表 (21 个 form_oid) 与自然语言题面共存时的固有代价。已实测复现 2 个独立案例
   (分别影响 `ev_q08` 与 `ev_q27`/`ev_q28`), 未做进一步抑制 (抑制需要某种"这段文字更像
   在指代标识符还是在使用日常词汇"的判断, 属于生成式/语义能力, 与本通道零 LLM 的设计
   前提冲突)。
7. **三题归因风险** (§3.2): `ev_q08`/`ev_q28`/`ev_q30` 是已知的卡片/doc 侧部分泄漏题,
   事件通道对这 3 题的命中/未命中结果与卡片/doc 侧机制不同源, 已逐题交代, 不应被解读
   为"事件层复现了旁支泄漏"。
8. **item OID 覆盖面缺口: 10/959 个 item OID 长度 <3 字符, 110 个 assignment 目标中 11
   个无法通过 Tier 2 (item 精确减法) 到达** (审查方定量要求, 已量化): `_MIN_ITEM_OID_LEN
   =3` 排除了这 10 个短 OID item 作为 Tier 2 触发点, 独立复算确认: 若不设该长度下限,
   这 11 个 assignment 目标全部可达 (0 个真正意义上"没有任何 item 能产生它"的死区);
   设了下限后, 这 11 个目标**仍然可达**, 但只能经由 Ruling P2 新增的 Tier 1b (该 form
   的未减法原始清单) 到达, 不再享有 Tier 2 的减法精度——即"能查到"但"查到的是未做减法
   的全集, 不是精确的那几条"。未调整该长度下限 (维持与卡片侧 `_MIN_ITEM_OID_LEN`/
   `_MIN_SEG_LEN` 一致的既有惯例), 只作量化记录。
9. **`resolve_events` 空列表的双重诱因不可从外部区分** (M4, `collect_scope.py` 消费方
   风险): 返回 `[]` 既可能是"确实没有任何该类问题的信息" (真实空), 也可能是"query 没有
   命中任何索引键" (未查到)——两者外部表现相同。已用合成 fixture 补测试, 但测试只能证明
   函数在这两种情况下都不臆造、不报错, 不能让调用方从返回值本身分辨这两种诱因。
9a. **(已修复, 审查方 Minor-1/Minor-2) item 缺 `raw` 键会 KeyError, `_item_oid_index`
    键规范与其余三类索引不对称**: `test_resolve_events_missing_pools_degrades_quietly`
    的 docstring 曾写"老 catalog 不许炸", 但该用例的 query 不命中任何 item OID, item 段
    整段未被执行, 实际只验证了事件/活动索引那一半会降级; item 段 (`collect_scope`) 此前
    直接 `item["raw"]`, 缺该键即 KeyError, 已实测复现。**已修复**: `collect_scope.py`
    改用 `(item.get("raw") or {})`, 补 `test_collect_scope_missing_raw_key_treated_as_
    no_hidden` + `test_resolve_events_item_scope_missing_raw_degrades_quietly` 对称覆盖
    item 段的降级路径。`_item_oid_index` 的键此前是裸 `item_oid` (未过 `_norm`), 与
    `_exact_oid_index`/`_form_assignment_index` 的键规范不对称 (当前无害, item OID 全
    ASCII 且不含内部空白), 已改为 `_norm(oid)` 消除这条隐含不变量。
10. **fixture repr 泄漏教训及其定量边界** (审查方要求记录, 源自 `test_catalog_workflow_
    pools.py` 顶部 `_RedactedCatalog` 的既有说明, 本单元沿用同一红线纪律, 未新增风险面
    但复述边界供后人查阅): `--tb=short` 不打印函数实参这一行, 不需要这层防护; `-q`
    (本仓默认 `addopts`) **不会**抑制这层防护要挡的那一行; `--showlocals`/`-l` 下防护
    **完全失效** (局部变量本身是裸 OID 集合, 会被原样打出), 本仓当前不跑 `-l`, 是已知
    限制而非"以为挡住了其实没挡住"; 把 `cat` 整体与字面量 dict 比较 (`assert cat == {...}`)
    会绕开 `__repr__` 走结构化 diff, 同样泄漏——本任务的测试文件未出现这种写法。
11. **红线扫描纪律的两处补强** (审查方要求记录):
    (a) 报告类中间产物 (如本次修复过程中的调试脚本输出) 同样要过红线扫描, 不能只扫
    进 git 的文件——本轮所有调试命令的输出均只在终端会话内查看, 未写入任何持久化文件,
    故无需额外扫描动作, 但这条纪律本身需要记录以防下一个人漏掉。
    (b) 红线扫描的对照语料必须覆盖**源**的全部区段 (`oidscan_evidence.py`/
    `leakscan_evidence.py` 的对照语料是 `catalog.json` 全文 + 已生成的卡片正文), 若
    未来引入"尚未解析进 catalog.json 的原始 ConfigReport 区段", 这部分是当前两个扫描
    工具天然的盲区 (不在对照语料里的真名不会被拦下)——本轮改动未涉及新的源区段, 记录
    在案供后续单元参考。
12. **红线洗白的占位符必须可区分** (审查方要求记录): 本文件与测试文件里的伪值
    (`偽EV1`/`偽IT_A` 等) 全部带有统一前缀 `偽`, 不与真实 OID 的任何已知形态混淆, 也
    不与其他任务/文件里可能出现的占位符风格混用——沿用既有约定, 未新增占位符体系。
13. **Task 4 减法的数据自洽佐证 (审查方指出的双重缺口, 唯一独立支撑材料)**: "有 hidden
    但减法未生效=0"等数据自洽检查此前**既未在** `evidence/checkpoints/study_workflow_
    events.md` **也未在** Task 4 自己的证据里独立呈现过——而 33 题里唯一能测"减法有效"
    的类型6 5 题, yml 拘束又明文禁止单独拿它们当证据。复算 (本轮新增, 零真名): 真实数据
    231 个带 `Hidden in activity` 的 item 中, **0 个**出现"隐藏清单非空但 `collect_scope`
    减法结果与该 form 全部分配完全相同"(即减法"什么都没减掉") 的情形——231/231 减法都
    真实产生了非平凡的差集。这是**除类型6 5 题之外**、唯一一份能独立佐证"减法机制本身
    在真实数据上确实生效"的证据, 现已记录在案 (双重缺口两侧现在都有了: Task 4 侧此前
    未做, 本单元现补上)。
14. **`ev_q06` 输出质量净退步, 分数不变但真实回归** (修复轮2审查 Important-1, 已实测
    定位机制): 修复轮1前该题返回 **2** 条, 且**恰好就是 gold 的 `event:`/`activity:`
    目标本身** (粒度比 gold 粗一级, 判 miss 但输出是"准确但不够细"); 修复轮1后该题返回
    **50** 条 (触顶 cap), 那 2 条被挤出结果之外, 顶替它们的是两个**与本题无关**的
    form OID (题面里被明确点名为"排除在外"的例子) 触发 Tier 1b 产出的原始清单 (未截断
    前两个无关 form 合计 58 条)。两轮判分不变 (均 miss, 因 gold 是 `assignment:` 粒度,
    即使那 2 条没被挤掉也不算命中), 但 `resolve_events` 的设计定位是要 union-add 进
    检索的, 这 2 条"至少指对了正确 event/activity"的信息在这次修复后**从结果里消失了**,
    对下游是真实的输出质量倒退, 不是分数能体现的那种"无害"。根因与 §3.1 桶3 相同
    (名称索引产不出 `assignment:` 粒度), 但这里额外暴露了 Tier 1b 的原始清单在体量上
    可以碾压 Tier 3 的正确命中, 即便后者在优先级上排得更靠前的部分已经被保护、front
    部分未被保护 (cap 截断只保证"结构化不被名称挤", 没有反向保证"名称的正确命中不被
    体量更大的结构化条目挤")。未做修复 (需要更细的 per-tier 配额分配, 权衡与桶3 未完成
    项同性质), 记为已知限制。
15. **全局返回量与 precision 未随命中率一起披露** (修复轮2审查 Important-2, 独立复算
    确认): 33 题合计返回 **259** 条, 与对应 gold 有交集的只有 **28** 条 ⇒ **全局
    precision ≈ 10.81%**。12 个未命中题合计返回 **157** 条纯噪声 (即返回了东西但一条
    都不对); 返回 ≥10 条的题有 **10** 个。**Ruling P2 在让 6 题转命中的同时, 也让这条
    通道在大多数答不出的题上从"沉默"变成"自信地给一堆错东西"** —— 这是加 form 维度
    索引这个设计决策的直接代价, 必须和 21/33 的命中率一起引用, 不能只挑 §4 类型6那 5
    题的 precision 数字。
    ⚠ **"10/12"这个数字的口径澄清 (本单元与团队lead/审查方两次独立复核后达成一致)**:
    12 个未命中题里, 修复轮1前后 `n_returned` **有变化**的题有 **10** 个 (`ev_q01`/
    `ev_q02`/`ev_q04`/`ev_q06`/`ev_q07`/`ev_q08`/`ev_q09`/`ev_q16`/`ev_q17`/`ev_q20b`,
    只有 `ev_q03`/`ev_q05` 修复轮1前后都是 0 条未变)。这 10 题里再细分: **6 题**
    是严格意义上"从返回 0 条变成返回非 0 条"(`ev_q01`/`ev_q04`/`ev_q08`/`ev_q16`/
    `ev_q17`/`ev_q20b`); 另 **4 题** (`ev_q02`/`ev_q06`/`ev_q07`/`ev_q09`) 修复轮1前
    本来就非空 (分别为 8/2/1/2 条), 修复轮1后条数**变多**了 (16/50/3/3 条)。本单元上一版
    checkpoint 用的是"严格 0→非0"口径 (得 6), 与团队lead/审查方给出的"n_returned 有
    变化即算"口径 (得 10) 不是同一个定义, 两者独立复算数字都对, 是定义差异不是计算错误——
    已在这里把两种口径都写清楚, 避免后续引用者再对不上。

复跑命令 (本条目专用, §1 复跑命令块之外单列):
```bash
cd sdtm-rag
.venv/bin/python - <<'PY'
import json, pathlib, yaml, subprocess, sys, tempfile
from server.study_lookup import StudyLookup
cat = json.loads(pathlib.Path('data/study/st01/catalog.json').read_text())
qs = yaml.safe_load(pathlib.Path('data/study/st01/eval/test_set_events_v1.yml').read_text())
lk = StudyLookup(cat)
total = tp = ge10 = noise = 0
misses = []
for q in qs:
    got = lk.resolve_events(q["question"]); want = set(q["expected_sources"])
    total += len(got); tp += len(set(got) & want)
    if len(got) >= 10: ge10 += 1
    if not (want & set(got)):
        misses.append(q["id"]); noise += len(got)
print(f"total={total} tp={tp} precision={100*tp/total:.2f}% ge10={ge10} miss_noise={noise} n_miss={len(misses)}")
PY
# pre-fix (e71a2a1) 对照: git show e71a2a1:sdtm-rag/server/study_lookup.py 另存到隔离
# 目录 (含 scripts/study/collect_scope.py 同版本), sys.path 优先加载后重跑同一脚本,
# 逐题比较 n_returned 是否 0->非0。
```
16. **Tier 1b 的"整 form 让位"避让逻辑不是无损操作, "命中不丢"不是一般性结论**
    (修复轮2审查第二部分A, 已实测定位): §2 修复点 2 描述的避让机制 (`covered_forms`)
    只在**gold 恰好落在 Tier 2 那个减法子集里**时才不丢命中——对本轮 Ruling P2 真正
    要服务的 form 级问法 (`event_form_assignment`/`repeating_rule`), 这个前提不成立:
    Tier 2 的结果按定义是该 form 全量的**真子集** (= 分配 − 该 item 的隐藏清单), 被
    让掉的差集没有其他层会补回来。真实数据 **231/959** 个 item 的减法结果是所属 form
    全量的真子集 (涉及 **7/21** 个 form), 单个 item 触发的避让最多让掉 **39** 条目标。
    当前 33 题因这条避让**丢失 gold 的题数 = 0** (未触发, 不代表设计上不存在这个风险)。
    另外两点连带发现: ①避让的触发条件只是"某个 item OID 有界命中题面", 而 §6-6 已记的
    短 OID 撞通用词风险在这里会放大成"一次巧合的 Tier 2 命中, 吃掉一次被明确点名的
    Tier 1b 请求"——3-4 字符的 item OID 共 66 个, 其中 33 个存在这个交叉风险; ②"点名的
    item 属于多个 form"这种边界下, 两个 form 会**一起**被记入 `covered_forms` (即便
    题面只点名了其中一个), 真实数据 959 个 item_oid 全局唯一 (0 例触发), 但代码层面
    存在这条隐含耦合。更稳妥的解是把"整 form 让位"改成"逐条相减"(Tier 1b 只跳过已经在
    Tier 2 里出现过的具体 target, 其余照常输出), 本轮按团队 lead 指示"定稿披露不加
    新功能"未实现, 留作后续工作。

## 7. 引用纪律自查

全文搜索 "SDTM 映射已支持" / "TA/TE/TV/SV" 相关表述: **0 处**——TA/TE/TV/SV 映射是
spec §2 明确 out of scope, 本报告未做任何相关声明。

## 8. M4/M5 处置 (Task 4 review 遗留)

- **M5 (落位)**: `collect_scope` + `_HIDDEN_ACT_KEY` 移出 `scripts/study/build_field_cards.py`,
  新住 `scripts/study/collect_scope.py` (中性模块)。渲染器与 `server/study_lookup.py`
  各自 `import`, 依赖方向不再别扭。生产渲染路径 (`assignments=None`) 行为逐字不变——
  **修复轮1验证方法已更正**: 不再用 `git status` (该目录 gitignored, 恒空, 是空闸),
  改用 §1 闸 D 的 sha256 逐文件复算 (961/961 与 Task 1 后指纹清单逐字节相同)。
- **M4 (空集分支零测试)**: 新增 `test_collect_scope_empty_when_form_has_no_assignments`
  (合成 fixture: item 所属 form 在 assignments 池里零分配, 真实数据 0 例的这一支现在
  有测试覆盖) + `test_resolve_events_item_scope_empty_when_form_has_no_assignments`
  (消费方视角: 该情形下 `resolve_events` 不臆造任何目标, 静默返回 `[]`)。"确实哪都不
  采集"与"没查到"两种诱因在返回值层面仍不可分辨, 已作为已知限制记录 (§6-9)。

## 9. 修复轮1 (2026-08-26, 团队 lead 复审后) — 规则 D 首轮核验结果与修复记录

规则 D 三方核验首轮已由 team lead 派发并完成, 两份报告落盘:
`evidence/step_workflow_events_audit.md` (抽检方) / `evidence/step_workflow_events_
audit_review.md` (审查方, 总判定 1 Critical · 4 Important · 3 Minor)。核心发现与本轮
处置逐条对照:

- **Critical-1 (审查方) / 特别交办 A (抽检方独立复现同一根因) — Ruling P2 未落地**:
  `_event_index` 未索引 form_oid 维度, `assignment:` 类型目标**只有一条产生路径**
  (item OID → `collect_scope`), event/activity 索引段结构上永远产不出——导致
  `event_form_assignment`/`repeating_rule` 两类 10 题结构性 0 命中, 且旧版 checkpoint
  把这归因成"题面不含答案锚点/需要生成式能力", 被抽检方三重反事实 (全池合成反事实 2/110、
  逐题补锚点 0/10、逐题补 item OID 9/10) 与"4 题 gold form OID 本来就逐字在题面里仍答不出"
  直接推翻。**已修复** (§2): 新增 form→assignment 索引, 10 题里 6 题转为命中
  (`repeating_rule` 5/5 全数命中 + `event_form_assignment` 1/5)。
- **Important-3 (审查方) — `_MAX_EVENTS_TOTAL=8` 截断已真实触发, 顺序是插入序非相关性序**:
  审查方实测 `ev_q02` 未截断返回 14 条被砍到 8 条 (该题 gold 本不在集合内, 未改变判分,
  但证明截断是真实发生过的, 不是纸面风险)。**已修复** (§2): 三层优先级拼接 (精确 OID →
  结构化推导 → form 原始清单 → 名称子串) + cap 从 8 调整为 50 (语义与取值均重新论证)。
  已证明 33/33 题在有 cap/无 cap 两种口径下命中判定完全一致。
- **Important-1 (审查方) — 闸 D 验证方法是空闸**: 原用 `git status` 查 gitignored 目录,
  恒为空。审查方同时给出了可证伪的替代方法 (sha256 对指纹清单, 961/961 相同)。**已修复**
  (§1/§8): checkpoint 改用该方法, 删除 `git status` 那句。
- **Important-2 (审查方) — 6 条裁定/教训整批缺席**: 闸 C 的"61 是回归锁不是独立参照物"
  限定、fixture repr 泄漏教训边界、报告类中间产物红线扫描、红线扫描对照语料覆盖面、红线
  洗白占位符可区分性、Task 4 减法数据自洽佐证 (231/231 无"减法未生效"情形, 独立复算)。
  **已全部补入** §1/§6 (逐条见 §6-10~13 与 §1 闸 C 行的限定措辞)。
- **Important-4 (审查方) — 45.45% 无参照物**: 已补 §5 旧通道基线对照 (fact-recall
  3/33 ≈ 9.1% vs 本单元 source-recall, 附口径不可直接相减的警告)。
- **Minor-3 (审查方) — §3.2 (原§2.2) 标题"单列不进总分"与正文"未被抽出另算"自相矛盾**:
  实情是 `ev_q28`/`ev_q30` 两个命中确实计入了 21/33。**已修复** (§3.2): 改为如实陈述 +
  补净额 19/30 = 63.33% (剔除三题后)。
- **Minor-1 (审查方) — item 缺 `raw` 键会 KeyError, docstring 保证范围被夸大**;
  **Minor-2 (审查方) — `_item_oid_index` 键规范与其余索引不对称**: **均已修复** (§6-9a),
  `collect_scope.py` 改用 `item.get("raw") or {}`, `_item_oid_index` 键改过 `_norm`,
  各补 1-2 条测试。
- **抽检方 3 条 Minor**: (a) 闸 C 升级 form 感知严格转置 (82/82) ——**已实现** (§1, 新增
  `test_gate_c_transpose_consistency_form_aware`); (b) 闸 B activity OID 全局唯一无测试
  看守——**已实现** (§1, 新增 `test_activity_oid_globally_unique`); (c) item OID 覆盖面
  缺口 (10/959 <3 字符, 11/110 目标不可达 Tier 2 精确路径) ——**已量化** (§6-8)。
- **抽检方"特别交办 C" — brief 字面版 vs 出货版实测背书**: brief 字面示例代码 (仅事件/
  活动索引) 在 33 题上得 10/33, 出货版 (含 item 采集范围扩展) 得 15/33 (修复轮1前);
  +5 分全部落在类型6, 其余五类零副作用; 且 `collect_scope` 全仓无其他生产消费方——
  **扩展是必要的, 不是可选的**。抽检方同时指出一处半真: 回退该扩展在**代码**层面自包含
  (事件/活动索引段的 4 个测试照过), 但会让 `collect_scope.py` 重新变成零非渲染消费方,
  即 M5 点名的"死代码住错了家"原地复活——"单独回退不影响别的"只在代码层面成立, 在
  M4/M5 遗留项闭合层面不成立, 已在此记录。
- **答1 (审查方六问之一) — 因果讲反**: 审查方指出旧版 §2.1 把 0/15 说成"Task 5 白送分
  修复的直接代价", 因果方向讲反了 (那些命中本来就是白送分, 不是能力的证据; Task 5 只是
  不再替通道遮着, 不是通道因此"付出代价")。**已随 §3.1 重写一并修正**, 不再使用"代价"
  措辞。

**类型6 gold 与 `collect_scope()` 的同源关系 (修复轮2, team lead 已查证定稿)**: 团队
lead 已查证 `EVENTS_V1_NOTES.md:120` 明文记载类型6的 gold 判据「与 `build_field_cards.py`
的 `collect_scope()` **逐字同构 (已读源码确认)**」——**5/5 逐条集合相等属循环证据,
不得单独引用为"减法有效"的证据**; 支撑该结论的独立材料是 §6-13 的 Task 4 数据自洽复算
(231/231 无"减法未生效"情形, 该复算不依赖类型6 gold, 是真正独立的证据源)。§4 的结论
段与本节此前均按"若…则存在风险, 需 team lead 确认"的条件句悬置处理, 修复轮2 team lead
已直接查证定稿, 不再是待定项。

**本轮引入的新发现 (§2/§4/§6-6 详述, 修复过程中实测发现, 非审查方原始报告内容)**:
Ruling P2 的 form 索引与类型6的 item 索引在同一题面共同出现时会相互干扰 (Tier 2 结果被
同 form 的 Tier 1b 原始清单稀释), 已加避让逻辑修复大部分影响, 残留噪声来源已定位并记入
已知限制 (§6-6): 短 form OID 兼通用词造成的误召回, 与减法本身是否正确无关。

**本轮测试**: `1764 → 1780 passed` (净 +16: `test_study_lookup_events.py` 从 7 条增至
**12 条** [修复轮2订正: 上一版误写 13 条, `--collect-only` 实测 12 条] / `test_collect_
scope.py` 从 3 条增至 4 条 / `test_build_field_cards.py` 移出 2 条 / `test_catalog_
workflow_pools.py` 从 7 条增至 9 条), `failures=0 errors=0`。

## 9b. 修复轮2 (2026-08-26, 规则 D 第二轮核验后) — 文档/披露层定稿, 不改功能

规则 D 第二轮核验 (审查方, 报告落盘 `evidence/step_workflow_events_audit_review_r2.md`)
判定首轮 10 条发现 **10/10 ADDRESSED** (含独立复算的 961/231/0/82/10/110/11 等数字全部
吻合), 但本轮新引入 **1 Critical + 3 Important + 1 Minor**。按 team lead 明确指示
"这轮是文档与披露层面的定稿, 不加新功能", 本轮**只改文档/注释/measurement, 不改
`resolve_events`/`collect_scope` 的行为逻辑**。逐条处置:

- **Critical (新) — 归因错误同类复发**: §3.1 修复轮1版本对剩余 12 题的"无锚点"归因,
  用同一判据独立复核后发现 4 题 (`ev_q06`/`ev_q07`/`ev_q08`/`ev_q09`) 判断有误——
  `ev_q06`/`ev_q09` 的 gold 事件名与活动名均在题面里且通道已返回对应 `event:`/
  `activity:`(粒度不够而非无锚点); `ev_q07`/`ev_q08` 与 `ev_q17` 同形态 (阈值裁剪)。
  **已修复**: §3.1 改写为三桶 (真无锚点 7 题 / 阈值裁剪 3 题 / 名称→assignment 粒度
  入口缺失 2 题), §6-4 删掉"已经消除"的错误陈述, 明确标为未完成项 (不实现, 只记录)。
- **Important-新-1 — `ev_q06` 输出质量净退步未披露**: 已补 §6-14, 并定位精确机制
  (2 条正确 `event:`/`activity:` 目标在未截断输出里存在, 被 cap 挤出)。
- **Important-新-2 — 全局噪声量未披露**: 已补 §6-15 (259 返回/28 tp/10.81% precision/
  157 噪声/10 题 ≥10 条), 并解决了与 team lead 原始复审数字"10/12"的口径分歧 (定义
  差异, 非计算错误, 两个数字都对)。
- **Important-3 (同源自洽)** = team lead 消息里的定稿要求: **已修复** (§9 上文已改
  陈述句)。
- **Minor-新-1 — 测试条数分解错误**: 已修复 ("13条"→"12条")。
- **审查方补充发现 (未被 team lead 转述消息明确列出, 但同一份报告里的完整内容, 一并
  处置)**: Tier 1b"整form让位"避让逻辑不是无损操作 (231/959 items 受影响, 单次最多
  丢 39 条, 当前 33 题未触发但设计上存在) → 已补 §6-16, 并修正代码里两处过强的
  "命中不丢"注释 (`server/study_lookup.py` `__init__` 与 `resolve_events` docstring
  各一处); cap"从未挤掉结构化目标"的全称断言有反例 (`ev_q06`) → §2 已改为有界陈述,
  补充 Tier 1b 层内插入序截断这一新发现。

**红线自查**: `oidscan_evidence.py` 对本轮改动的全部文件 (含证据文件、审查方报告)
CLEAN, 详见文末。

## 10. 收口状态

规则 D 已完成两轮核验, 首轮 1 Critical/4 Important/3 Minor(+抽检方2Minor) 与第二轮
1 Critical/3 Important/1 Minor 及审查方补充发现 (Tier 1b 避让边界/cap 全称断言) **全部
已处置**。本单元遗留且明确不在本轮范围内的两个未完成项 (均已记入 §6, 不阻塞收口, 供
后续单元决策): ① 名称→`assignment:` 粒度这条索引入口仍缺 (§3.1 桶3/§6-4); ② Tier 1b
"整 form 让位"应改成"逐条相减"而非当前的整体跳过 (§6-16)。若 team lead 认为需要第三轮
复核, 建议只抽查这两处文档改写与 §6-14/15/16 三条新记录的数字是否吻合 (代码本轮零改动,
无需重新审查实现逻辑)。
