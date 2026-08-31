# 联网通道语义抽检 (规则 A)

> 联网答案不可复算, **不进 gold set** —— 本表是它唯一的质量证据。
> ⚠ 机检只能查形状; **人判两列必须人眼逐条判**, 不得由脚本判 PASS。
> ⚠ **本表 (v3, 2026-08-31) 三条限定, 阅读前先看**:
> 1. **样本量 n=2** —— 任何一行「零码」的观察 (第 1/2 题) 都只是这次运行的证据, 不构成 Rule 9(b) 在统计意义上的有效性证明。
> 2. 第 3 题两个 ⛔ 码见下方附录「已结构性排除」标注: 该轮 `搜索次数=0`, 判定依据是结构性的 (没联网就没有网页内容能进 context), 不是靠「最近引用标记」那条弱启发式。
> 3. 机检目前只查过 `Cxxxxx` 硬编码; **`机检: Web句含硬事实词` 这一列是 v4 (代码审查后) 才加的新机检, 本表三行都是 v3 产出、未采集这项, 一律标 `n/a`, 不代表零命中** —— Rule 9(b) 禁的 class/category 归属、Core/Role/Type 三样, 这三行事实上从未被机检检查过。

| # | 问题 | 机检: CT 码 | web_status | web_searches_ok | 搜索次数 | 机检: [Web:] 数 | 机检: [Source:] 数 | 机检: Web句含硬事实词 | 人判: 标注是否规矩 | 人判: 借鉴是否标推测 |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | How do other teams handle EDC fields that don't map to any s | ✅ 无 | ok | 2 | 2 | 6 | 23 | n/a (本轮未采集) | ⬜ 待判 | ⬜ 待判 |
| 2 | What do practitioners say about overusing SUPPQUAL versus cr | ✅ 无 | ok | 2 | 2 | 5 | 12 | n/a (本轮未采集) | ⬜ 待判 | ⬜ 待判 |
| 3 | How is Findings About (FA) used in practice versus a custom  | ⛔ C101833,C101832 | ok | 0 | 0 | 0 | 22 | n/a (本轮未采集) | ⬜ 待判 | ⬜ 待判 |

## 判读规则

- **CT 码列出现任何码 = 立即查**: Rule 9(b) 禁止从网页产出 `Cxxxxx`、class/category 归属、Core/Role/Type。
  码若能在 `knowledge_base/` 找到且答案标的是 `[Source:]`, 属正常 (KB 来源);
  标 `[Web:]` 却带码 = **红线破**。
- **`搜索次数` 列 = 0 时优先看它, 比「最近引用标记」这条弱启发式更硬**: 该轮没有触发任何工具调用 ⇒ context 内不可能混入任何网页内容 ⇒ Rule 9(b) 的触发条件从未成立——这一行任何 CT 码命中都只能来自 KB, 可直接判非红线破 (第 3 题即此情形, 见下方附录), 不需要再去核对最近引用标记。
- **`web_status`/`web_searches_ok` 直接给出联网是否真的发生** —— 比『`[Web:]` 数为 0 ⇒ 可能没真联网』这种间接推断可靠: `web_searches_ok` > 0 才是真的搜到了结果; `web_status` 应为 `ok`, 非 `ok` (如 `partial`/`disabled`/`quota_exceeded`/`failed`/`off`) 说明联网本身有问题或不完整 (`partial` = 有成有败, 不是全灭)。
- **`机检: Web句含硬事实词` 只是形状扫描, 不是判定**: 命中不等于红线破, 只是提示该句混着 Core/Role/Class 一类硬事实词汇又带 `[Web:` 引用, 值得人多看一眼。本表三行此列均为 `n/a` (v3 产出, 该项检查 v4 才加, 见上方限定 3), 不代表这三题的答案里没有这类词——**没查过**和**查过没有**是两回事。
- 人判两列必须逐条看答案原文, 不看就填 = 抽检失效 (规则 A 的意义就在这)。

## 附录: CT 码标注上下文 (机器只定位, 不判读)

> ⚠ **「最近引用标记」是启发式定位, 不是来源判定。** 绝对字符距离只能告诉你「这个码附近最近的标记是什么」, **推不出**「这个码来自那个来源」 —— 同一段落可能引了多个来源, 物理最近的标记未必是这个码的事实依据所在。红线判定必须**读原文片段**确认该码的事实依据来自哪一边, 不能只看这一列的标签。`搜索次数==0` 的行不适用这条弱路径, 见下方「已结构性排除」标注。

### 第 3 题: How is Findings About (FA) used in practice versus a custom findings domain?

- **已结构性排除**: 本轮零工具调用 (`搜索次数=0`, `web_searches_ok=0`) ⇒ context 内无任何网页内容 ⇒ Rule 9(b) 适用前提未成立, 下面两个码只可能来自 KB。(不依赖下面的「最近引用」这条启发式, 那条只是交叉验证。)
- **`C101833`** @ char 5626 — 最近引用标记是 `[Source:...]` (距 `C101833` 101 字符): `[Source: domains/FA/assumptions.md]`
  > …ise be added. [Source: domains/FA/assumptions.md] - `FATEST` — Label "Findings About Test Name", Char, Synonym Qualifier, **Req**, Controlled Terms **C101833**, value ≤ 40 characters; CT lives in a general FATEST codelist plus several therapeutic-area-specific codelists. `FATESTCD` uses **C101832**. [Sourc…
- **`C101832`** @ char 5766 — 最近引用标记是 `[Source:...]` (距 `C101832` 11 字符): `[Source: domains/FA/spec.md]`
  > …d Terms **C101833**, value ≤ 40 characters; CT lives in a general FATEST codelist plus several therapeutic-area-specific codelists. `FATESTCD` uses **C101832**. [Source: domains/FA/spec.md] [Source: VARIABLE_INDEX.md] - `FACAT` (Label "Category for Findings About", Char, Grouping Qualifier, **Perm**, no CT…

## 附录: [Web:] 句子里的 Core/Role/Class 等硬事实关键词 (机器只定位, 不判读)

(本轮 v3 未实现此项机检, `n/a` —— 见上方限定 3。不代表本轮三题的答案里没有这类词, 只是没查过, 见 `eval/web_channel_spotcheck.py` v4 起补的 `_hard_fact_keyword_hits()`。)
