# 联网通道语义抽检 (规则 A)

> 联网答案不可复算, **不进 gold set** —— 本表是它唯一的质量证据。
> ⚠ 机检只能查形状; **人判两列必须人眼逐条判**, 不得由脚本判 PASS。

| # | 问题 | 机检: CT 码 | web_status | web_searches_ok | 搜索次数 | 机检: [Web:] 数 | 机检: [Source:] 数 | 人判: 标注是否规矩 | 人判: 借鉴是否标推测 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | How do other teams handle EDC fields that don't map to any s | ✅ 无 | ok | 2 | 2 | 6 | 23 | ⬜ 待判 | ⬜ 待判 |
| 2 | What do practitioners say about overusing SUPPQUAL versus cr | ✅ 无 | ok | 2 | 2 | 5 | 12 | ⬜ 待判 | ⬜ 待判 |
| 3 | How is Findings About (FA) used in practice versus a custom  | ⛔ C101833,C101832 | ok | 0 | 0 | 0 | 22 | ⬜ 待判 | ⬜ 待判 |

## 判读规则

- **CT 码列出现任何码 = 立即查**: Rule 9(b) 禁止从网页产出 `Cxxxxx`。
  码若能在 `knowledge_base/` 找到且答案标的是 `[Source:]`, 属正常 (KB 来源);
  标 `[Web:]` 却带码 = **红线破**。
- **`web_status`/`web_searches_ok` 直接给出联网是否真的发生** —— 比『`[Web:]` 数为 0 ⇒ 可能没真联网』这种间接推断可靠: `web_searches_ok` > 0 才是真的搜到了结果; `web_status` 应为 `ok`, 非 `ok` (如 `disabled`/`quota_exceeded`/`failed`/`off`) 说明联网本身有问题。
- 人判两列必须逐条看答案原文, 不看就填 = 抽检失效 (规则 A 的意义就在这)。

## 附录: CT 码标注上下文 (机器只定位, 不判读)

> ⚠ **"最近引用标记"是启发式定位, 不是来源判定。** 绝对字符距离只能告诉你"这个码附近最近的标记是什么", **推不出**"这个码来自那个来源" —— 同一段落可能引了多个来源, 物理最近的标记未必是这个码的事实依据所在。红线判定必须**读原文片段**确认该码的事实依据来自哪一边, 不能只看这一列的标签。

### 第 3 题: How is Findings About (FA) used in practice versus a custom findings domain?

- **`C101833`** @ char 5626 — 最近引用标记是 `[Source:...]` (距 `C101833` 101 字符): `[Source: domains/FA/assumptions.md]`
  > …ise be added. [Source: domains/FA/assumptions.md] - `FATEST` — Label "Findings About Test Name", Char, Synonym Qualifier, **Req**, Controlled Terms **C101833**, value ≤ 40 characters; CT lives in a general FATEST codelist plus several therapeutic-area-specific codelists. `FATESTCD` uses **C101832**. [Sourc…
- **`C101832`** @ char 5766 — 最近引用标记是 `[Source:...]` (距 `C101832` 11 字符): `[Source: domains/FA/spec.md]`
  > …d Terms **C101833**, value ≤ 40 characters; CT lives in a general FATEST codelist plus several therapeutic-area-specific codelists. `FATESTCD` uses **C101832**. [Source: domains/FA/spec.md] [Source: VARIABLE_INDEX.md] - `FACAT` (Label "Category for Findings About", Char, Grouping Qualifier, **Perm**, no CT…

