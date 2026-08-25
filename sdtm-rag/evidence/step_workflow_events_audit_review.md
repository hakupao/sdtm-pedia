# Task 6 对抗性复核 (规则 D 审查方)

> 日期: 2026-08-26 · 分支 `feat/study-workflow-events` · 复核范围 `0b0dbfa..e71a2a1`
> 角色: 规则 D 三方核验之**审查方** (与实现方 impl-t6、抽检方 audit-t6 均不同 subagent)
> 红线: 全文零真实 OID / label / 题面, 一律用题号 (`ev_qNN`) + 计数 + 形态指代
> 分工: **不复算闸 A/B/C 的数字** (抽检方职责); 本文质疑设计、结论强度与措辞诚实度

---

## 总判定

- **Spec compliance: ❌**
- **Task quality: Issues found** — 1 Critical · 4 Important · 3 Minor

**一句话**: 代码本身干净、测试真实、类型 6 那段结论的自我限定写得比多数轮次都诚实;
但本单元有一条**控制方已经写死的裁定 (Ruling P2) 没有实现、没有披露**, 而该裁定当初
就预言了不实现的后果 —— 收口证据把那个后果原样写成了"结构性、与实现无关", 方向正好
是裁定预言的误读再往前一步。另有 6 条被点名"进 T6 收口证据"的 ruling/教训整批缺席,
闸 D 记录的验证方法是一条**结构上不可能失败的空闸**。

---

## Issues

### Critical-1 — Ruling P2 未实现且未披露; 其可预见后果被写成"结构性、非 bug"

`.superpowers/sdd/2026-08-25-study-workflow-events/progress.md:50-60`
(裁定原文) ↔ `sdtm-rag/server/study_lookup.py:100-129` (未实现)
↔ `sdtm-rag/evidence/checkpoints/study_workflow_events.md:57-64` 与 `:148-151` (错误归因)

控制方在派发前的跨 Task 接口扫描里已写死:

> **P2 (跨 Task 接口不闭合)**: …T6 的 `_event_index` 只索引 events 与 activities,
> `resolve_events` **永远不可能返回 assignment: 目标** ⇒ 那类题必然全灭, 且会被
> **误读成"事件通道效果差"**。
> **Ruling P2**: T6 的 `_event_index` 追加索引 assignments — 以 `form_oid` 为键指向
> `assignment:{event_oid}/{activity_oid}/{form_oid}`。…**T6 须相应增加一个测试。**

实现里没有任何 `form_oid → assignment:` 索引。`assignment:` 目标**只有一条产生路径**
(item OID 子串 → `collect_scope` 减法), 事件/活动索引段永远产不出。

**这不是理论风险 —— 我实测了它的代价**(只读复跑, 命令见 §复跑):

| 题 | 类别 | 返回件数 | gold 的 event 目标已返回? | gold 的 activity 目标已返回? |
|---|---|---|---|---|
| `ev_q06` | event_form_assignment | 2 | **是** | **是** |
| `ev_q09` | event_form_assignment | 2 | **是** | **是** |
| `ev_q10` | event_form_assignment | 2 | **是** | 否 |
| `ev_q12` | repeating_rule | 1 | 否 | **是** |
| `ev_q14` | repeating_rule | 1 | 否 | **是** |
| `ev_q15` | repeating_rule | 1 | 否 | **是** |

`ev_q06`/`ev_q09` 上, 通道**已经把 gold 的 (event, activity) 两级都查出来了**, 只因
gold 落在 `assignment:` 粒度而判 miss。`ev_q12`/`ev_q14`/`ev_q15` 已查出 gold 的
activity。从已命中的 activity 反查 `self._assignments_by_form_activity` 换算成
`assignment:` 目标, 是一次确定性 join, 数据已在内存里 (`self._assignments`), **零 LLM,
不越 spec §2 范围** —— 正是 Ruling P2 要求的东西。

而收口证据对这 10 题 (event_form_assignment 5 + repeating_rule 5) 的归因是:

> 答案…从不出现在题面里, 需要"生成"而非"查表"。这类问法**结构上不在 `resolve_events`
> 子串匹配的能力范围内, 与实现是否有 bug 无关**  (`:62-64`)
> …要答这类题**需要生成式能力 (LLM 读三池数据后组织语言)**  (§4-4, `:150-151`)

**对至少 5 题 (`ev_q06`/`ev_q09`/`ev_q12`/`ev_q14`/`ev_q15`) 这是与实测相反的陈述**:
对象就写在题面里, 通道也确实查到了, 差的是一次 join 而不是"生成式能力"。

**责任归属要说清楚**: task-6-brief.md 从头到尾没有转达 Ruling P2 —— Step 3 给的示例
代码只有 events/activities 两段, Step 8 的已知限制清单三条里也没有它。实现者是**照
brief 字面交付的**, 这条主要是**派发缺陷**, 不是实现者失职。但归因段是实现者自己写的,
在没有做过"改一下能不能命中"这个检验的情况下, 把 miss 断言成"与实现无关 / 需要 LLM",
超出了证据能支撑的范围。

**要求**: (a) 实现 Ruling P2 或由控制方正式撤销它并记账; (b) 无论 (a) 走哪条,
§2.1 与 §4-4 的"结构上不在能力范围内 / 需要生成式能力"必须改写 —— 至少把
event_form_assignment 与 repeating_rule 两类从"结构性不可答"里摘出来, 改成"当前
实现未接 assignment 粒度输出 (Ruling P2 未落地), 非题面所致"。

> 附注 (给 (a) 的决策留一句): 若按 P2 扇出 assignment 目标, 会把"一个 activity 下
> 全部表单"一次性吐出, 而本轮尺子对 precision 零惩罚 —— 那正是 §11-1 点名的盲区。
> **这是一个真实的设计取舍, 值得写下来**; 但它是"我们选择不做, 因为会薅尺子的漏洞",
> 不是"物理上做不到"。前者诚实, 后者是现在写的那个。

---

### Important-1 — 闸 D 记录的验证方法是空闸 (`git status` 查一个 gitignored 目录)

`sdtm-rag/evidence/checkpoints/study_workflow_events.md:24` · 同句另见
`.superpowers/sdd/2026-08-25-study-workflow-events/task-6-report.md:38` 与 `:184-185`

> 本会话未重渲染任何卡片 (`git status` 确认 `data/study/st01/cards/` 零改动)

`sdtm-rag/.gitignore:10` 是 `data/study/`。实测 `git check-ignore -v data/study/st01/cards/`
命中该行, `git status --porcelain data/study/st01/cards/` **恒为空** —— 卡片改没改都一样。
task-1-review.md:137 早就点过同一件事 ("`data/study/` 被 `sdtm-rag/.gitignore:10` 忽略,
diff 里一张卡都没有")。这是本仓写在裁定里的最坏形态: **"不实的'已设闸'记录比缺闸更害人"**
(progress.md:205-206)。

**但结论本身是对的 —— 我用能证伪的方法独立证实了**: 拿控制方建的指纹清单
`cards_post_t1.sha256.json` 逐文件重算 SHA256:

```
manifest entries: 961   current cards: 961
identical=961  changed=0  missing=0  extra=0
```

**961/961 逐字节相同**, 卡片确实自 T1 之后零改动。所以这是**方法记错、结论无害**:
现成的能证伪的工具就在 workspace 里没被用。请把 §1 闸 D 那格换成上面的 sha256 结果
(或 study golden v2 Δ0 这条真实旁证), 删掉 `git status` 那句。

---

### Important-2 — 6 条被点名"进 T6 收口证据"的裁定/教训整批缺席

我把 progress.md 里所有写明"进/写进 T6 收口证据"的条目对着 checkpoint 逐条查, **命中 0 条**
(`grep -n 'RedactedCatalog|占位符|中间产物|对照语料|回归锁|减法未生效|showlocals|教训'` → 无输出):

| # | 出处 | 内容 | 在 checkpoint? |
|---|---|---|---|
| 1 | progress.md:213-215 | **闸 C 的 `61` 属回归锁而非独立参照物**, 判别力来自双向互证, 完全不依赖 61 —— "此点应写进 T6 收口证据的已知限制" | ❌ |
| 2 | progress.md:220-222, 236-241 | fixture repr 泄漏教训 + 其定量边界 (`--tb=short` 不打印 / `-q` 不抑制 / `--showlocals` 仍泄漏 / 整体 dict 比较绕开 `__repr__`) | ❌ |
| 3 | progress.md:250 | 报告类中间产物也要过红线扫描, 不能只扫 git 追踪面 | ❌ |
| 4 | progress.md:272 | 红线扫描的对照语料必须覆盖**源**的全部区段, 否则"尚未解析进产物的那部分源"是天然盲区 | ❌ |
| 5 | progress.md:295 | 红线洗白必须用**可区分**占位符 | ❌ |
| 6 | progress.md:312-317 | Task 4 减法的数据自洽佐证 ("有 hidden 但减法未生效 = 0" 等) —— "**它比任何测试绿灯更能说明推导正确**" | ❌ |

第 1 条正是团队 lead 在本次复核任务里点名要查的那条: checkpoint §1 闸 C 那格写的是
"**61/61, PASS**", 不带任何限定; §4-2 提到闸 C 时把它当"看守"用, 也没说 61 不是独立参照物。
**该写没写。**

第 6 条的缺席代价最大, 而且是双重的: 它是**唯一一份能在 33 题之外独立支撑"减法有效"的
证据**。yml 拘束条件明文禁止拿类型 6 那 5 题当"减法有效"的证据 —— 那么合规的做法就是
搬出这条数据自洽佐证。checkpoint 两边都没做: 既没搬佐证, 又拿那 5 题走到了 "5/5 精确"
的措辞边缘 (见 §答2)。

同样地, brief 也没转达其中任何一条 —— 这批缺席**主要仍是派发缺陷**。但收口证据是本单元
留给后人的唯一入口, 缺了就是缺了。

---

### Important-3 — `_MAX_EVENTS_TOTAL = 8` 的截断在本轮真的触发了, 全文零披露

`sdtm-rag/server/study_lookup.py:39` · `:222` (`return out[:_MAX_EVENTS_TOTAL]`)

实测 33 题里 **`ev_q02` 未截断前返回 14 条, 被砍到 8 条**。checkpoint 全文没有"截断"
二字, §2.1 把 `ev_q02` 归进"题面不含答案锚点所以答不出"那一类 —— 而它实际上是**命中了
题面里一个 4 字符 item OID、扇出 14 条、再被 cap 砍掉一半**。机制与写的完全不同。

两点必须进已知限制:

1. **截断顺序 = `dict` 插入序 (即 catalog 里 events/activities/items 的原始行序), 不是
   相关性序**。`resolve_events` 先跑事件/活动段再跑 item 段, 所以事件名的巧合命中**天然
   优先于** `collect_scope` 算出的结构化目标 —— 噪声排在信号前面。
2. 本轮**侥幸无害**: 我逐题验过, 没有任何一题的 gold 是"在未截断集合里、被 cap 砍掉的"
   (`gold lost purely to cap: []`)。但 `ev_q02` 已经贴到 cap, `ev_q28` 恰好等于 8 —— 余量
   为 0。若按 Critical-1 补上 assignment 扇出, 这个 cap **一定**会开始咬人。

---

### Important-4 — 45.45% 没有参照物; 而参照物就在隔壁且对本单元有利

`sdtm-rag/evidence/checkpoints/study_workflow_events.md:8-15` (§0 一句话结论) · §2

checkpoint 把 15/33 = 45.45% 当主结果报出, 但**没给任何对照基线**, 读者无从判断这是好是坏。
实现者报告 §顾虑 2 也只说"15/33 是一个偏低的总分"。

基线是现成的 —— Task 5 的 `EVENTS_V1_NOTES.md §11-6` 对**同一批 33 题**测过旧通道:
卡片侧 3/33 (9.1%) · doc 侧 7/33 (21.2%) · 并集 9/33 (27.3%, 自动化原始值);
**语义核验后真阳性并集 3/33 ≈ 9.1%**。

对着这个看, 本单元不是"偏低", 是把旧通道答不出的一大片答出来了。**不写基线, 等于让本
单元自己吃了个哑巴亏**, 同时也让 §6 S4 的价值论证在收口处断了线 (S4 在 T5 判过未触发,
但 T6 收口证据一个字没接)。

**但补的时候必须带一句口径警告**: §11-6 那组数用的是 **fact-recall** (检索正文里子串
存在性), Task 6 这组用的是 **expected_sources 交集非空**。两把尺子不同, 直接相减是
不成立的。正确写法是并排列出并注明口径不可比, 而不是算一个 "+6" 的差。

---

### Minor-1 — "老 catalog 静默降级"的保证宽于测试, 实际会 `KeyError`

`sdtm-rag/scripts/tests/test_study_lookup_events.py:40-43` ·
`sdtm-rag/scripts/study/collect_scope.py:35-40` (`item["raw"]`)

`test_resolve_events_missing_pools_degrades_quietly` 的 docstring 写"**老 catalog (无三池)
不许炸**"。但该用例的 query 不含 fixture 里那个 item OID, **item 段整段没被执行** —— 它只
证明了事件/活动索引那一半会降级。实测 items 缺 `raw` 键时:

```
RAISED: KeyError 'raw'
```

危害当前为零 (`build_catalog.py` 用 `asdict()` 出 items, `raw` 恒在; `resolve_events`
目前无任何非测试调用方)。但 `test_study_lookup.py` 里已有十几处不带 `raw` 的手搭 fixture
—— 哪天有人给其中之一喂进 `resolve_events`, 就会炸在一句写着"不许炸"的保证下面。
建议 `item.get("raw") or {}`, 或把 docstring 的保证范围收窄到它真正测到的那一半。

### Minor-2 — `_item_oid_index` 的键未过 `_norm`, 与 `_event_index` 不对称

`sdtm-rag/server/study_lookup.py:119-122` vs `:100-113`

事件/活动索引键一律 `_norm(...)`, item OID 索引键用**裸 oid**, 而查找端比的是
`_norm(query)`。当前无害 (item OID 全 ASCII, `_norm` 只做 NFKC + 去空白, 不改大小写),
但这是一条**没写下来也没测到的隐含不变量**。同文件同方法里两套键规范, 后人改 `_norm`
时很容易只顾一半。

### Minor-3 — §2.2 标题与正文自相矛盾 ("单列不进总分" vs "未被抽出另算")

`sdtm-rag/evidence/checkpoints/study_workflow_events.md:72` (标题) vs `:90-93` (正文)

标题写 "**单列不进总分**", 正文写 "它们各自落在…类别桶里, **未被抽出另算**"。后者是实情:
`ev_q28`/`ev_q30` 两个命中确实计入了 15/33。标题那句是**假的**。
量级上不重大 —— 我算过, 剔除三题后是 **13/30 = 43.33%** (vs 45.45%), 挪 2.1 个点。
所以这是措辞缺陷不是注水, 但既然 yml 明文要求"単独列挙し, 総分に混ぜて終わらせない",
把净额那一行写出来是两分钟的事。

---

## 团队 lead 六问 · 逐条结论

### 答 1 — 「15/33」被怎么用: **是, "结构性"确实在替一个真实的能力缺口挡枪**

分两半判:

- **`event_timing` 5 题 + `conditional_event` 3 题 miss**: 归因**成立**。实测这 8 题里 7 题
  返回 0 条 (`ev_q02` 是例外, 见 Important-3), 题面确实没有可索引的锚点, 且 §4-1 已说明
  Scheduling 字段本研究全空 —— 这类确实不是子串通道能答的。
- **`event_form_assignment` 5 题 + `repeating_rule` 5 题 miss**: 归因**不成立**。见
  Critical-1 的实测表 —— 5 题的 gold event/activity **已经被通道查出来了**, 只差一次
  确定性 join。把它写成"需要生成式能力 (LLM)"是与实测相反的陈述。

**"够不够 spec §2 声称的能力范围"**: 按控制方自己在 Ruling P2 里给出的解释 ——
"用户选定范围是'事件表可查', '某事件下收集哪些表单'正属该范围 (spec §2 In scope 1)"
—— **不够**。一个只能"给名字找记录"的通道, 在本单元宣称的范围里本来就该能回答
"这个事件下分配了哪些表单", 数据也全在 catalog 里。

**证据文件有没有说清楚**: 没有。§2.1 用"结构性原因 (不是逐题巧合, 是三个类别的题面设计
使然)"一句把三类一起收走, 三个字盖过去了。而且它还多走了一步 —— 把 0/15 说成
"**Task 5 白送分修复的直接代价**"。这个因果讲反了: 修复前那些命中是**白送分**, 本来就
不是能力的证据。正确的说法是"通道从来没有这个能力, Task 5 只是不再替它遮着"。写成"代价"
,读起来像尺子变苛刻了, 而不是尺子变诚实了。

### 答 2 — 类型 6 的结论强度: **并列呈现, 未塞进已知限制; 但标题与结论句仍踩线**

先给公道: 这一段是本份 checkpoint 里写得最好的部分。

- 拘束条件 (`§11-1`: 引用这 5 题必须併記返却件数) —— **照做了**, §3 表格逐题给出总返回数 /
  `assignment:` 类型条目数 / tp / fp / 其他类型噪声 / gold 集合大小。我复算过表里的形态,
  与实测一致 (`ev_q27` 7/7 · `ev_q28` 8 条含 1 tp · `ev_q29` 2/2 · `ev_q30` 4 条含 1 tp ·
  `ev_q31` 1/1)。
- 盲区**不在**已知限制里而已 —— 它在 §3 的**同一段落、同一句的后半句**, 用"但…**依然
  成立**"连着, 而且明写"不代表评分方法本身的这个盲区被堵上了, 换一批题或换一个不同实现
  完全可能触发它"。这是并列, 不是"结论 + 附注"。§4-5 是**再**记一遍, 不是唯一出处。

所以团队 lead 担心的形态 (前者写成结论、后者塞进已知限制) **没有发生**。

**但两处仍踩线, 该改**:

1. §3 的**标题**是"减法**是否真的有效**", 结论句是加粗的 "5/5 题的答案都是 **是**"。
   yml file header 的拘束原文是「この5題の結果を『減法が効いている証拠』として引用する
   ことは**禁止**」—— 併記返却件数是**附加**要求, 不是解禁条件。现在的写法是"限定后的
   有效结论", 而拘束禁的是"有效结论"本身。**改法很便宜**: 把标题改成中性的"类型 6 返回
   件数与 precision 实测", 结论句改成"目标 item 自身的减法与 gold 逐条相等 (5/5), 但按
   §11-1 拘束, 本节不作为'减法有效'的证据"。
2. 更值得做的是 **Important-2 第 6 条**: 搬出 Task 4 那份数据自洽佐证 ("有 hidden 但减法
   未生效 = 0" 等)。那份证据**不受本拘束约束**, 且控制方原话就是"比任何测试绿灯更能说明
   推导正确"。有它在, §3 根本不需要往结论边缘蹭。

**一个额外的、没人提过的循环风险 (Cannot verify, 见下)**: "5/5 逐条集合相等"这个数,
取决于类型 6 的 `expected_sources` 当初是怎么产生的。若 gold 是拿同一条减法规则算出来的,
那 5/5 就只是代码与 gold 同源自洽, 不构成验证。我没能确认 gold 的产生方式。

### 答 3 — 三题归因是否真落实: **报通道 ✅ · 单列不混总分 ❌ · 机制论证成立但避重就轻**

yml 对 `ev_q08`/`ev_q28`/`ev_q30` 写死两条:

**(i) 必须同时报出实际命中通道** — **落实了**。§2.2 表格两列: 事件通道 (本次实测) /
卡片·doc 侧 (引 NOTES §10-6), 且注明了出处。我复核了事件通道那一列, 与实测吻合:
`ev_q08` 返回 0 条 (真的没命中); `ev_q28` 8 条含 1 条 gold; `ev_q30` 4 条含 1 条 gold。

**(ii) 算增益时单独列出、不混总分** — **没落实**。见 Minor-3: 标题声称"不进总分",
实际两个命中都在 15 里, 且 checkpoint **从头到尾没有算过任何"事件层增益"** —— 连
Important-4 说的那个对照基线都没摆。所以严格讲这一条是双重未做: 既没单列净额,
也没做增益计算。

**(iii) "机制是结构化推导, 与文本共现型泄漏是两种性质, 不应混为一谈" 成不成立?**

**成立, 而且实测支持**: `ev_q28`/`ev_q30` 的 gold 命中类型都是 `assignment:`,
只能由 item OID → `collect_scope` 减法这一条路径产生 (事件/活动索引段结构上产不出
`assignment:`)。所以确实不是文本共现。

**但这是在为一个不需要辩护的地方辩护, 反而绕开了更强也更简单的事实**: yml 的原始担忧
是**归因混淆** ——「若事件通道在这三题上赢了, 有可能是 doc 通道在做功而非事件层」。
而 Task 6 Step 6 的实测**只调用 `lk.resolve_events(...)`, 卡片/doc 引擎根本不在回路里**。
归因混淆在这个测量里**不可能发生**, 一句话就完了。checkpoint 却花了一整段去论证"机制
性质不同", 语气是防守式的。**建议直接改成那一句**, 更硬也更短。

所以: 不是开脱 (论证本身是真的), 是**用了一个较弱的辩护, 同时漏掉了 (ii)**。

### 答 4 — brief 扩展的正当性: **合理补齐, 不是 scope creep; "可单独回退"基本属实, 有一处半真**

**正当性: 站得住。** 三条理由:

1. M5 的原文要求就是让 `collect_scope` 有真实消费方; brief 的示例代码若逐字照抄, M5 落不了地
   —— 实现者在报告 §顾虑 1 主动点名了这个偏离, 没有偷偷加。
2. 它落在 spec §2 In scope 3 (item 真实采集范围) 内, 不越界。
3. 事后看, 它是类型 6 拿到 5/5 的**唯一**原因 —— 没有它, 33 题里另有 5 题归零, 总分从
   15/33 掉到 10/33。

**而且有个反讽值得记一笔**: 这段"超出 brief"的扩展, 恰恰是 Ruling P2 精神的**一半**实现
(它确实让通道能产出 `assignment:` 目标了), 只是键选了 item OID 而不是裁定写的 form OID。
实现者在没看到 P2 的情况下自己摸到了同一处缺口的一半 —— 派发漏了 P2, 反倒是实现者的
主动扩展补回了其中一块。

**"边界清楚、可单独回退": 技术上真, 语义上半真。**

- 真: `resolve_events` 的 item 段 (`server/study_lookup.py:115-129` 的索引 + `:216-221`
  的第二个循环) 是自包含的, 删掉不影响事件/活动索引那一半, 事件段的 4 个测试照过。
- 半真: 回退它会让 `scripts/study/collect_scope.py` **重新变成零非渲染消费方** ——
  也就是 M5 当初点名的"死代码住错了家"原地复活。所以"单独回退不影响别的"只在**代码**层面
  成立, 在**遗留项闭合**层面不成立: 退了这段, M4/M5 一起退回未闭合。这一句该补进证据。

### 答 5 — 已知限制是否完整: **五条中四条在, 一条缺; 另有 5 条该写没写**

控制方点名的五条:

| # | 要求 | 位置 | 判定 |
|---|---|---|---|
| 1 | Scheduling 全空 | §4-1 | ✅ |
| 2 | 脚注启发式 | §4-2 | ✅ |
| 3 | `resolve_events` 与 `resolve()` 不同源、未做挤占分析 | §4-3 | ✅ |
| 4 | **闸 C 的 61 是回归锁非独立参照物** | — | ❌ **缺** (见 Important-2 第 1 条; §1 那格还写着无限定的 "61/61, PASS") |
| 5 | 类型 6 盲区 + 三题归因 | §4-5 / §4-6 | ✅ |

**该写而没写的 (按严重度排):**

1. **Ruling P2 未落地** (Critical-1) —— 这条其实不该进"已知限制", 该是**未完成项**。
2. **`_MAX_EVENTS_TOTAL=8` 截断已触发** + 截断顺序是插入序不是相关性序 (Important-3)。
3. **无对照基线 / 与 §11-6 口径不可比** (Important-4)。
4. **闸 D 的 `git status` 方法无效** (Important-1) —— 与其说是限制, 不如说是要改的错记录。
5. **另外 5 条被点名进 T6 收口证据的教训** (Important-2 第 2-6 条)。
6. `item["raw"]` KeyError (Minor-1)。

顺带: §4-9 (未接入生产查询路由) **是主动写的、准确的、且对读者最有用的一条** —— 我
`grep -rn 'resolve_events' --include='*.py'` 复核过, 除测试外零调用方, 与所写完全一致。
这条给实现者记一功。

### 答 6 — 措辞诚实度: **禁用词零命中; 但有 1 处不实陈述、1 处自相矛盾、1 处因果讲反**

`grep -n '验收通过|已支持|已证明|有效|证明|PASS|成立|坐实'` 全文过了一遍:

- 「验收通过」「已支持」「已证明」: **0 处**。
- 「PASS」3 处, 全在 §1 闸 A/B/C, 均由具名测试兜底 —— 撑得住 (数字本身归抽检方)。
  唯一的问题是闸 C 那格该带 Important-2 第 1 条的限定。
- 「证明」4 处, **全部是否定式**("不能证明该盲区已被堵上"/"测试只能证明…不能让调用方
  分辨") —— 用法正确, 是在收紧不是在放大。
- 「有效」3 处, 全部带引号或带否定限定 —— 除了 §3 的**标题**, 见 §答 2 第 1 点。
- §5「引用纪律自查」: 搜"SDTM 映射已支持"/"TA/TE/TV/SV" 得 0 处。技术上合规, 但这是**搜
  违禁字符串本身**, 属自动通过的检查。我另外实读了全文, 确认**没有任何形式的 SDTM 映射
  声明** —— 引用纪律**实质合规**, 不只是字面合规。

**撑不住的三处** (按本仓"不实的'已设闸'记录比缺闸更害人"这条标准排):

1. **不实陈述** — §1 闸 D 的 `git status` 验证法 (Important-1)。这是唯一一处"记录了一条
   实际上不存在的闸"。**最该先修的就是它。**
2. **自相矛盾** — §2.2 标题"单列不进总分" (Minor-3)。
3. **因果讲反** — §2.1 把 0/15 说成"Task 5 白送分修复的**直接代价**" (答 1 末段)。

另外, **实现者报告的诚实度值得单独肯定**: §顾虑 1-4 主动点名了超出 brief 的扩展、
15/33 偏低、类型 6 结论的限定条件、规则 D 未做; §Step 8 还主动披露了 `leakscan` 的一处
假阳性并说明为何不改。§Step 3 明写"未遇到落地困难, 未提前示警"。Step 9 按 kickoff 硬规矩
17 如实点名"核验报告尚未落盘, 不视为已完成" —— 没有一处把未做说成已做。**本单元的问题
集中在"该转达的没转达"与"归因超出证据", 不在于虚报。**

---

## ⚠️ Cannot verify

1. **类型 6 的 `expected_sources` 是怎么产生的** —— 若 gold 当初是用同一条
   "form 分配 − 隐藏清单" 规则算出来的, 那 §3 的 "5/5 逐条集合相等" 就是代码与 gold
   同源自洽, 不构成对减法的验证 (循环论证)。题集与 NOTES 均未记载 gold 的产生方式,
   我无法从 gitignored 的题集反推。**建议控制方直接向 Task 5 实现方确认。** 这条若成立,
   会实质削弱 §3 的全部结论强度。
2. **闸 A/B/C 的具体数字** (110 / 21 / 109 / 1 / 61 / 四条差集为 0) —— 按分工归抽检方,
   本文未复算。
3. **`tests=1772 failures=0 errors=0 skipped=0`** —— 按指示未重跑全量。
4. **§2.2 表格右列 (卡片/doc 侧已知泄漏)** —— 引自 `EVENTS_V1_NOTES.md §10-6/§11-6` 的
   既往实测, 本次未重跑 doc/卡片引擎复核。出处已在 checkpoint 标注, 属合规引用。
5. **Ruling P2 若实现, 那 10 题会不会真的转命中** —— 我只证明了 gold 的 event/activity
   已被查出、join 数据在内存里; 没有改代码实测 (审查方不改文件)。

---

## 复跑命令 (本文全部实测均可复现)

```bash
cd /Users/bojiangzhang/MyProject/sdtm-pedia/sdtm-rag

# (1) 闸 D 的真实验证法 —— 逐卡 SHA256 对指纹清单 (输出 961/961 identical)
.venv/bin/python - <<'PY'
import json, hashlib, pathlib
man = json.loads(pathlib.Path('../.superpowers/sdd/2026-08-25-study-workflow-events/cards_post_t1.sha256.json').read_text())
root = pathlib.Path('data/study/st01/cards')
cur = {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in root.glob('*.md')}
k = {pathlib.Path(a).name: b for a, b in man.items()}
print(f"identical={sum(1 for a,b in k.items() if cur.get(a)==b)} changed={sum(1 for a,b in k.items() if a in cur and cur[a]!=b)} "
      f"missing={sum(1 for a in k if a not in cur)} extra={sum(1 for a in cur if a not in k)} (n={len(k)})")
PY

# (2) 闸 D 记录的方法为何是空闸
git check-ignore -v data/study/st01/cards/            # 命中 .gitignore:10
git status --porcelain data/study/st01/cards/         # 恒空, 与卡片是否改动无关

# (3) Critical-1 的实测 (逐题命中 / 返回件数 / gold 粒度) 与 Important-3 的截断实测
#     脚本: scratchpad/probe.py · probe2.py · probe3.py (只读, 只打印题号+计数+目标类型前缀)
#     probe3 关键输出: ev_q06/ev_q09 gold 的 event 与 activity 目标均已返回;
#                      ev_q12/ev_q14/ev_q15 gold 的 activity 目标已返回
#     probe2 关键输出: ev_q02 uncapped=14 → capped=8 (截断); "gold lost purely to cap: []"

# (4) Minor-1 的 KeyError 实测
.venv/bin/python -c "
from server.study_lookup import StudyLookup
lk=StudyLookup({'study':'stx','items':[{'form_oid':'F','item_oid':'ABCD','label':'zzzz'}],
                'assignments':[{'event_oid':'E','activity_oid':'A','form_oid':'F'}]})
try: print(lk.resolve_events('ABCD'))
except Exception as e: print('RAISED:', type(e).__name__, e)"        # → RAISED: KeyError 'raw'

# (5) resolve_events 零非测试调用方 (§4-9 属实)
grep -rn 'resolve_events' --include='*.py' . | grep -v '\.venv'

# (6) Important-2 的缺席复核
grep -n 'RedactedCatalog\|占位符\|中间产物\|对照语料\|回归锁\|减法未生效\|showlocals\|教训' \
     evidence/checkpoints/study_workflow_events.md                   # → 无输出
```

---

## 建议处置顺序

1. **闸 D 的 `git status` 那句** (Important-1) —— 改一行, 且是唯一一处不实的"已设闸"记录。
2. **Critical-1** —— 控制方裁决: 实现 Ruling P2, 或正式撤销并记账。无论哪条, §2.1/§4-4
   的归因措辞都要改。
3. **Important-2** —— 6 条裁定/教训补进 checkpoint (第 1 条与第 6 条优先: 一条是 lead
   点名的已知限制, 一条能把 §3 从拘束边缘救下来)。
4. Important-3 / Important-4 / Minor-3 —— 补披露与补基线, 都是加段落, 不动代码。
5. Minor-1 / Minor-2 —— 各一行代码或一行 docstring。

**代码本身没有需要回退的东西。** 本轮的问题在收口证据的记录与归因, 不在实现。
