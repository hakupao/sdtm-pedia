# U5 收口 — 抽检方 A 独立复算报告 (规则 D)

> 状态: **完成**
> 角色: 抽检方 A (独立 session, 独立代码, 只读产物)
> 日期: 2026-08-16
> 分支: `doc-track-u5`
> 输入: `data/study/st01/eval/runs/` 下 24 份产物 —
> 12 矩阵 run `u5_{cards,docs}_{study,both}_r{1,2,3}.json` · 2 probe · 4 control ·
> 6 auto run · 被验对象 `u5_verdict.json`
>
> **独立性声明 (硬规矩 17b)**: 未读、未 import `eval/u5_verdict.py`; 未读
> `evidence/checkpoints/` 与 `evidence/failures/` 下任何 U5 既有判定文档。全部数字由本报告
> §9 贴出的独立脚本从 run json 的 `results` 数组逐题重算, **不采信 `summary` 顶层字段**
> (`summary` 仅作为被比对方出现在 §5 / §6 / §7)。判据口径 (稳定 / scored / 配对 / pt 分母)
> 由我从产物结构自行定义后再与 verdict 对齐, 不抄脚本写法。
>
> **零题面声明**: 复算脚本在 load 阶段即丢弃 `question` / `answer` / `answer_preview` 三键;
> 本报告只出现题号与数字, 不含任何题面文字、任何知识库真名、任何源文件名 (含其双下划线前缀)。

## 结论速览

| 分块 | 声称条数 | 复现 | 不复现 |
|---|---|---|---|
| §1 I2 逐配置稳定集 (4 计数 + 4 清单) | 8 | 8 | 0 |
| §2 E1 配对代价/收益 + E4 (2 语料 ×5 + 2) | 12 | 12 | 0 |
| §3 I1 probe (6) + I3 control (4) | 10 | 10 | 0 |
| §4 E3 脆弱 4 题 (每题 4 字段) | 4 | 4 | 0 |
| §5 12 个 judge_avg | 12 | 12 | 0 |
| §6 auto 分布 + fallback + 脆弱路由 | 8 | 8 | 0 |
| §7 12 run 参数交叉一致性 + routing 单键 | 5 | 5 | 0 |
| §8 三闸 pass + advisory_only + E2 判词 | 5 | 5 | 0 |
| **合计** | **64** | **64** | **0** |

U5 判定 json 的**每一个数字都复现, 无一处算错**。

新增 finding **7 条** (§10), 全部属「数字对但判据设计有问题」一类, 其中 **HIGH 2 条**:

- **F-1 (HIGH)**: `confirmed_cost_pt = 0.00` 不是「both 档没有代价」, 而是**过滤规则把 100%
  的代价题censored 掉了**。换一把**不做任何稳定性假设的最坏界尺子** (`max(both 三遍) <
  min(study 三遍)` 才算确认代价), 代价 = **2.08pt / 2 题**, 而收益一分不变仍是 2.78pt / 同 2 题。
  即: 该过滤对收益侧零损耗, 对代价侧全清零 —— 方向性偏置。
- **F-2 (HIGH)**: auto 档有 **4 题被路由到 cdisc 且 source_recall = 0.0** (三遍全同),
  而同题强制 study/both 档为 1.0; `routed_fallback` 在这 4 题上**一次都没触发**。
  「fallback 243 全 False」这句在 Task 6 里读作健康信号, 实际含义是**兜底机制在 4 处确认的
  路由打空上完全失灵**, docs 语料 3/30 = 10% 的题在 auto 档拿不到任何 gold 证据。

---

## 0. 复算口径 — 我自己的定义 (先定义, 后对齐)

我不看被验脚本, 先从产物结构自定 4 个口径, 再拿去和 verdict 对:

| 口径 | 我的定义 | 产物依据 |
|---|---|---|
| scored 行 | `results[]` 中 `out_of_scope == False` 的行 | cards 51 行 → 48; docs 30 行 → 30 |
| 稳定 (I2) | 同一题三遍 `judge_fact_recall` 三值全等 **且** 三遍 `judge_parse_ok` 全 True | 两条件缺一即入不稳定清单 |
| 配对 (E1) | study 侧与 both 侧**双双稳定**的题才进比较; 差 = both − study | 不稳定题一律进 E4 |
| pt 分母 | cards 48 / docs 30 (scored 全集, 非 n_compared) | 见 §2 反推验证 |

前置断言 (三条全过):

- cards 六份 run 的 scored id 集合完全相同 (48 题); docs 六份完全相同 (30 题)。
- cards 每份 run 总行 51 (48 scored + 3 out_of_scope); docs 每份 30 (无 out_of_scope)。
- gold 侧核对: `test_set_study_v2.yml` 共 51 个 id, `test_set_docs_v1.yml` 共 30 个 id ——
  **两个语料都是跑了 gold 全集, 无子集挑选**, 无 cherry-pick 空间。

浮点处理: 全部差值/均值用 `fractions.Fraction(str(v))` 精确累加后再 `round(...,2/4)`,
避免二进制浮点尾差伪造不一致。

---

## 1. I2 — 逐配置稳定集与不稳定清单

**我的算法**: 对每配置的 48/30 道 scored 题, 取三遍 `judge_fact_recall` 与 `judge_parse_ok`,
三分全等且三个 parse_ok 全 True 记稳定, 否则入不稳定清单; 清单排序后与 verdict 逐 id 比。

| 配置 | 我的不稳定数 | verdict `I2.counts` | 相等 | 清单逐 id 相等 |
|---|---|---|---|---|
| cards_study | 5 | 5 | 是 | 是 |
| cards_both | 4 | 4 | 是 | 是 |
| docs_study | 1 | 1 | 是 | 是 |
| docs_both | 0 | 0 | 是 | 是 |

我复算出的清单 (与 verdict `I2.unstable` 逐 id 完全一致):

- cards_study: `st01_v11_q23r, st01_v2_q06, st01_v2_q14, st01_v2_q18, st01_v2_q21`
- cards_both: `st01_v11_q23r, st01_v2_q03, st01_v2_q18, st01_v2_q22`
- docs_study: `docs_v1_q41`
- docs_both: (空)

**8/8 复现。** 补充事实: 12 份矩阵 run 共 468 条 scored 行, `judge_parse_ok == False` 的行
**0 条**, 12 份 `summary.judge_parse_failures` 亦全为 0 —— 即 I2 的不稳定**全部来自分值漂移,
没有一条来自 parse 失败**, 两个条件里只有第一个真正起作用 (见 §10 F-5)。

---

## 2. E1 — 配对代价/收益 + E4 未决集

**我的算法**: 取 study 侧稳定集 ∩ both 侧稳定集为配对集; 逐题 `d = both − study`;
`d < 0` 入代价清单, `d > 0` 入收益清单; `pt = Σ|d| × 100 / 分母`, 分母取 scored 全集 (48/30)。

| 项 | 我的数 | verdict | 相等 |
|---|---|---|---|
| cards `n_compared` | 41 | 41 | 是 |
| cards `confirmed_cost_ids` | (空) | (空) | 是 |
| cards `confirmed_cost_pt` | 0.00 | 0.0 | 是 |
| cards `confirmed_gain_ids` | `st01_v2_q08, st01_v2_q19` | 同 | 是 |
| cards `confirmed_gain_pt` | 2.78 | 2.78 | 是 |
| docs `n_compared` | 29 | 29 | 是 |
| docs `confirmed_cost_ids` / `_pt` | (空) / 0.00 | (空) / 0.0 | 是 |
| docs `confirmed_gain_ids` / `_pt` | (空) / 0.00 | (空) / 0.0 | 是 |
| cards `E4_undecidable` (7 题) | 两侧不稳定并集 | 同 | 是 |
| docs `E4_undecidable` (1 题) | `docs_v1_q41` | 同 | 是 |

分母反推验证 (确认分母是 48 不是 41): 收益两题逐题差 —

| 题号 | study (三遍同) | both (三遍同) | 差 |
|---|---|---|---|
| `st01_v2_q08` | 0.0 | 1.0 | +1.0000 |
| `st01_v2_q19` | 0.6667 | 1.0 | +0.3333 |

Σ差 = 1.3333 → ×100/48 = **2.78** (吻合); 若分母取 n_compared=41 则为 3.25 (不吻合)。
故 verdict 的分母确为 scored 全集 48 —— 与 §0 我的独立定义一致。

`n_compared` 反推: 48 − |{cards_study 不稳定 5} ∪ {cards_both 不稳定 4}| = 48 − 7 = 41 ✓;
30 − 1 = 29 ✓。E4 集合正是这两个并集。

**12/12 复现。** 但 `confirmed_cost_pt = 0.00` 的**成因**有严重问题, 见 §10 F-1。

---

## 3. I1 probe 与 I3 control — 从 rows 重数 (不信顶层)

**我的算法 (I1)**: 不读 `same_rate` / `n_same` 顶层字段, 也不信行内 `same` 布尔, 直接对
`rows[]` 逐行比 `orig == rejudged` 重新判同, 再 `n_same / len(rows)`。

| 项 | 我的数 (逐行重判) | 行内 `same` 布尔计数 | 顶层字段 | verdict | 相等 |
|---|---|---|---|---|---|
| probe_cards `n` | 48 | — | 48 | 48 | 是 |
| probe_cards `same_rate` | 1.0 | 48 | 1.0 | 1.0 | 是 |
| probe_cards `n_orig_parse_fail` | 0 | — | 0 | 0 | 是 |
| probe_docs `n` | 30 | — | 30 | 30 | 是 |
| probe_docs `same_rate` | 1.0 | 30 | 1.0 | 1.0 | 是 |
| probe_docs `n_orig_parse_fail` | 0 | — | 0 | 0 | 是 |

三路一致 (逐行重判 = 行内布尔 = 顶层字段), 无顶层字段与 rows 脱节的情况。

**我的算法 (I3)**: 对每个 control 文件的 `rows[]` 用 Fraction 精确求 `recall` 均值, 再与
`avg` 顶层及 verdict 比。

| control | n | 我的 avg | 顶层 `avg` | verdict `I3.avg` | 相等 | 全 parse_ok |
|---|---|---|---|---|---|---|
| docs_positive | 6 | 1.0 | 1.0 | 1.0 | 是 | 是 |
| docs_negative | 6 | 0.0 | 0.0 | 0.0 | 是 | 是 |
| cards_positive | 6 | 1.0 | 1.0 | 1.0 | 是 | 是 |
| cards_negative | 6 | 0.0 | 0.0 | 0.0 | 是 | 是 |

**10/10 复现。** probe 的判据强度问题见 §10 F-3, control 的覆盖盲区见 §10 F-4。

---

## 4. E3 — 脆弱 4 题逐题三遍原始分

**我的算法**: 直接从 6 份 cards 矩阵 run 抠这 4 题的 `judge_fact_recall` 原始三元组, 自行判
稳定, 稳定则取该值、不稳定则记 null, 再与 `E3_fragile` 四字段比。

| 题号 | study 三遍原始 | both 三遍原始 | 我的 (study, both) | 我的 (stable_s, stable_b) | verdict | 相等 |
|---|---|---|---|---|---|---|
| `st01_v11_q19` | 1.0 / 1.0 / 1.0 | 1.0 / 1.0 / 1.0 | (1.0, 1.0) | (True, True) | 同 | 是 |
| `st01_v2_q14` | **0.6667 / 1.0 / 1.0** | 0.3333 / 0.3333 / 0.3333 | (null, 0.3333) | (False, True) | 同 | 是 |
| `st01_v2_q15` | 0.6667 / 0.6667 / 0.6667 | 0.6667 / 0.6667 / 0.6667 | (0.6667, 0.6667) | (True, True) | 同 | 是 |
| `st01_v2_q21` | **0.6667 / 1.0 / 1.0** | 0.0 / 0.0 / 0.0 | (null, 0.0) | (False, True) | 同 | 是 |

**4/4 复现。** 但请注意粗体两行的形状: `q21` 的 both 侧**三遍钉死 0.0**, study 侧**三遍最低
0.6667**; `q14` 的 both 侧三遍钉死 0.3333, study 侧三遍最低 0.6667。这两题被判「未决」,
是 §10 F-1 的直接来源 —— 它们其实是本次数据里**唯二无需任何假设即可确认的回归**。

---

## 5. Task 5 的 12 个 judge_avg — 从 scored 行重算

**我的算法**: 对每份 run 取 scored 行, `Fraction` 精确求 `judge_fact_recall` 均值, `round(4)`;
既与 Task 5 声称值比, 也与该 run `summary.judge_fact_recall_avg` 比 (双向)。

| 配置 | 我的 r1/r2/r3 (逐行重算) | 该 run summary 顶层 | Task 5 声称 | 三方相等 |
|---|---|---|---|---|
| cards_study | 0.8681 / 0.9028 / 0.8819 | 同 | 0.8681 / 0.9028 / 0.8819 | 是 |
| cards_both | 0.8681 / 0.8958 / 0.8681 | 同 | 0.8681 / 0.8958 / 0.8681 | 是 |
| docs_study | 0.9583 / 0.9417 / 0.9583 | 同 | 0.9583 / 0.9417 / 0.9583 | 是 |
| docs_both | 0.9583 / 0.9583 / 0.9583 | 同 | 0.9583 / 0.9583 / 0.9583 | 是 |

**12/12 复现。** 分母核实: 均值分母 = scored 行数 (48/30), 未把 3 条 out_of_scope 掺进去
(掺进去 cards_study r1 会变 0.8170, 与声称不符 → 反证分母口径正确)。

副产品事实 (§10 F-6 用): cards 两档三遍均值 study = 0.8843 平均 vs both = 0.8773 平均,
**both 档在总均值上其实略低于 study 档**, 与 E1「只有收益没有代价」的方向相反。

---

## 6. Task 6 — auto 档三项主张, 从 6 份 auto 产物直接重数

**我的算法**: 不读 `summary.routing`, 直接对 `results[]` 逐行 `Counter(row["routed"])`;
`routed_fallback` 逐行数 True; 脆弱 4 题从三份 cards auto run 抠 `routed`。

| auto run | 我逐行数出的 routed | 该 run `summary.routing` | 相等 | fallback True |
|---|---|---|---|---|
| cards r1 / r2 / r3 | study 45, both 5, cdisc 1 (三遍全同) | 同 | 是 | 0 / 0 / 0 |
| docs r1 / r2 / r3 | study 27, cdisc 3 (三遍全同) | 同 | 是 | 0 / 0 / 0 |

- 分布主张 **45/5/1 ×3 · 27/0/3 ×3**: 复现 (docs 的 both = 0, 与声称的「27/0/3」对上)。
- 总行数: 3×51 + 3×30 = **243**, `routed_fallback == True` 计数 = **0** → 「243 全 False」复现。
- 脆弱 4 题: 3 轮 × 4 题 = **12 行, `routed` 全为 `study`** (取值域 = {study} 单元素) → 复现。

**8/8 复现。** 但这三条主张的**风险含义被漏报**, 见 §10 F-2。

---

## 7. 交叉一致性 — 12 矩阵 run 同参数前提

**我的算法**: 把 12 份 run 的 `summary` 指定字段 JSON 规范化后放进桶, 数桶数; 桶数 = 1 即全同。

| 字段 | 我数出的取值桶数 | 取值 | 12 run 全同 |
|---|---|---|---|
| `hybrid` | 1 | `{"fusion":"rrf","alpha":null}` | 是 |
| `study_lookup` | 1 | `true` | 是 |
| `top_k` | 1 | `15` | 是 |
| `judge_model` | 1 | `deepseek/deepseek-chat` | 是 |
| (加验) `federated` | 1 | `true` | 是 |
| (加验) `threshold` | 1 | `0.85` | 是 |

**4/4 声称字段复现** (另 2 个我主动加验的字段也全同)。

routing 单键核验 (声称: 强制档下 routing 应为单键):

| run | `summary.routing` | 我逐行数出 | 单键且 = 强制档 |
|---|---|---|---|
| cards_study ×3 | `{study: 51}` | `{study: 51}` | 是 |
| cards_both ×3 | `{both: 51}` | `{both: 51}` | 是 |
| docs_study ×3 | `{study: 30}` | `{study: 30}` | 是 |
| docs_both ×3 | `{both: 30}` | `{both: 30}` | 是 |

12 份矩阵 run `routed_fallback == True` 计数亦全为 0 (强制档下兜底不应触发, 一致)。
**5/5 复现。**

注: 矩阵 run 的 routing 计数是 51/30 (含 3 条 out_of_scope), 而 judge 均值分母是 48/30
(不含) —— 两处分母口径不同但各自自洽, 不构成错误, 仅记录以免后人误读。

---

## 8. 三闸判定与 E2 判词复算

| 项 | 我按 `thresholds` 重算 | verdict | 相等 |
|---|---|---|---|
| I1 pass (阈 ≥0.95) | True (1.0 / 1.0) | True | 是 |
| I2 pass (阈 cards ≤7, docs ≤4) | True (5,4 ≤7; 1,0 ≤4) | True | 是 |
| I3 pass (阈 pos ≥0.8, neg ≤0.2) | True (1.0/1.0; 0.0/0.0) | True | 是 |
| `advisory_only` | False (三闸全过 → 非 advisory) | False | 是 |
| `E2_verdict` | 与「cost 0 / gain 2.78 & 0」自洽 | `cheap_on_this_ruler` | 是 |

**5/5 复现。** 注意 `E2_verdict` 的字面 —— **"on this ruler"** 这个限定词本身是诚实的,
§10 的 finding 正是在说这把尺子测不到什么。

---

## 9. 复算脚本 (独立实现, 未 import 被验脚本)

脚本置于 session scratchpad, **不进仓**:
`<scratchpad>/recalc_a.py` (§0-§8) + 4 段内联 `python3 - <<EOF` 探针 (§10 敏感性分析)。

核心写法与被验对象的差异点 (硬规矩 17b 要求异源):

1. 精确算术: 全程 `Fraction(str(v))` 累加, 只在最后一步 `round`; 不用 float 累加。
2. 顶层字段一律不采信: `same_rate` / `avg` / `routing` / `judge_fact_recall_avg` 全部从
   `rows[]` / `results[]` 重数后**反向**去比顶层, 顶层只作被比对方。
3. 口径先自定后对齐: §0 四个口径在打开 verdict 之前就定死, 再做比对。
4. load 阶段剥离 `question` / `answer` / `answer_preview`, 从物理上杜绝题面进入计算与报告。
5. 额外加了 3 个前置断言 (id 集跨 run 一致 / 行数 / gold 全集), 被验对象未必有。

---

## 10. 新增 Finding (7 条)

### F-1 (HIGH) — `confirmed_cost_pt = 0.00` 是过滤造出来的, 换尺子代价 = 2.08pt

E1 要求「两侧三遍都完全稳定」才计入比较。问题是: **两档分值不同的题, 天然更容易在档内也不稳定**
—— 这个过滤精准地删掉了信号本身。用两把不同的替代尺子量同一批数据:

| 尺子 | 假设强度 | cards 代价 | cards 收益 | cards 净 |
|---|---|---|---|---|
| verdict 现用 (双侧三遍全同才算) | 最强 | **0.00pt / 0 题** | 2.78pt / 2 题 | +2.78 |
| 三遍均值 (全 48 题都算) | 中 | 4.63pt / 5 题 | 3.94pt / 4 题 | **−0.69** |
| **最坏界** (`max(both3) < min(study3)` 才算确认代价, 反之算收益) | **最弱, 不做任何稳定性假设** | **2.08pt / 2 题** | 2.78pt / 2 题 | +0.69 |

三点必须说清:

1. **最坏界尺子零假设**。它只问「both 的三遍最好成绩, 是否仍不如 study 的三遍最差成绩」。
   `st01_v2_q21` (both 三遍 0.0 vs study 三遍最低 0.6667) 与 `st01_v2_q14`
   (both 三遍 0.3333 vs study 三遍最低 0.6667) 满足该条件, 即**无论抽哪一遍作代表, 这两题
   both 都输**。把它们叫「未决 (undecidable)」在数据上站不住。
2. **过滤是方向性的**。均值口径下 5 道题净负、4 道题净正; 5 道净负题 (`q03/q06/q14/q18/q21`)
   **全部 5/5 落在被删的 7 题里**, 4 道净正题只有 2 道被删 (`q23r/q22`)。
   即该过滤**清掉 100% 的代价、只清掉 50% 的收益**。
3. **对收益侧零损耗**。最坏界尺子下收益仍是 2.78pt / 同样 2 题 —— 换尺子没让收益变多。
   所以「cost 0 / gain 2.78」这组数的不对称, 来自尺子而非来自系统。

**建议**: `confirmed_cost_pt` 至少并列给出最坏界口径的值 (cards 2.08pt), 或把 E4 里满足
`max(both3) < min(study3)` 的题从「未决」移到「确认代价」。当前写法会让读者读成
「both 档零代价」, 而数据支持的结论是「both 档在最保守口径下仍有 2 题确认回归」。

### F-2 (HIGH) — auto 档 4 题路由打空且 source_recall = 0.0, fallback 一次未触发

Task 6 三条主张数字全对, 但「fallback 243 全 False」被当健康信号读, 方向反了。逐行核出:

| 题号 | auto `routed` | auto `source_recall` | 同题 study 档 | 同题 both 档 | `routed_fallback` |
|---|---|---|---|---|---|
| `st01_v2_q07` | cdisc | **0.0** (三遍) | 1.0 | 1.0 | False (三遍) |
| `docs_v1_q15` | cdisc | **0.0** (三遍) | 1.0 | 1.0 | False (三遍) |
| `docs_v1_q17` | cdisc | **0.0** (三遍) | 1.0 | 1.0 | False (三遍) |
| `docs_v1_q53` | cdisc | **0.0** (三遍) | 1.0 | 1.0 | False (三遍) |

- 这不是「召回略低」, 是 **gold 源一条都没命中**, 三遍稳定复现 (检索侧确定性)。
- docs 语料 **3/30 = 10%** 的题在 auto 档拿不到任何证据; cards 1/48。
- 整体检索均值也随之被拖: docs `source_recall_avg` auto **0.900** vs study/both **1.000**;
  cards auto **0.8542** vs study **0.8750**。auto 档在两个语料上检索都劣于强制 study。
- `routed_fallback` 恒 False 说明**兜底逻辑在这 4 个本该兜底的场景里没有任何动作**。

**建议**: 「fallback 243 全 False」这句在收口文档里必须补一句限定 ——
「其中含 4 例路由至 cdisc 且 gold 全空, 兜底未触发」, 否则该句会被读成兜底健康。
另建议把「auto 档 source_recall 相对强制 study 的差」列为 U5 的显式指标。

### F-3 (MED) — I1 probe 只覆盖 6 份答案集里的 1 份, 且天花板效应稀释判据强度

- 我按逐题分值反查 probe 的来源答案集: `probe_cards` 与 **`cards_both_r1` 48/48 逐题精确吻合**,
  与其余 5 份 cards run 均不吻合 (最高 45/48)。即 cards 的 judge 确定性只在
  **6 份答案集中的 1 份**上验过。`probe_docs` 与 4 份 docs run 吻合 (docs 侧答案更收敛)。
- 天花板: cards probe 的 48 个原分里 **39 个 = 1.0**; docs 30 个里 **27 个 = 1.0**。
  一个「永远给 1.0」的退化 judge 在 cards 上也能拿到 39/48 = 81% 的 same_rate。
  真正有判别力的是那 9 个非满分项 (0.0×4 / 0.3333×2 / 0.6667×3), 它们确实精确复现 —— 这是
  真信息, 但**有效样本是 9 不是 48**, 而阈值 0.95 是按 48 定的 (允许错 2 个)。
- 缓解事实 (对 U5 有利, 应写进结论): 我核过 12 份矩阵 run 的答案文本, cards 四配置
  **三遍逐题答案 0/48 相同**, docs 也仅 1/30 相同 —— 即三遍是**真实重采样**, 不是缓存重放。
  结合 I1 (同答案重判 100% 同分), 可推 I2 的不稳定**全部来自生成侧而非 judge 侧**。这条推论
  成立且重要, 但它依赖 I1 的外推 (1 份答案集 → 6 份), 应显式写明是外推。

**建议**: probe 换成跨 run 抽样 (每份 run 抽若干题) 而非单份全量, 并在结论里报「非满分项
same_rate」这个去天花板后的数。

### F-4 (MED) — I3 control 只验 0/1 两个端点, 而 E1 的信号大半在中间分值区

- 4 个 control 各 n=6, positive 全 1.0 / negative 全 0.0, 完美分离。这证明 judge 能区分
  「喂 gold」与「喂错答案」两个极端, 但**没有任何 control 落在 0.3333 / 0.5 / 0.6667 / 0.75**
  这些中间分值上。
- 而 E1 的结论正建在中间分值上: 收益题 `st01_v2_q19` 是 0.6667 → 1.0; §10 F-1 里的两道确认
  代价题是 0.6667 vs 0.3333 与 0.6667 vs 0.0。**只有 `st01_v2_q08` (0.0 → 1.0) 落在 control
  覆盖的端点区**。按 pt 拆: 收益 2.78pt 中 2.08pt 在覆盖区、0.69pt 在未覆盖区。
- 换句话说: 尺子的**刻度线**验过了, **刻度间的等距性**没验过。

**建议**: 补 1-2 组中间分值 control (人工构造 1/3、2/3 命中的答案), 或在结论里声明 E1 的
partial-credit 部分未受 I3 保护。

### F-5 (LOW) — I2 的「全 parse_ok」条件在本次数据里是空条件

468 条 scored 行 `judge_parse_ok` 全 True, 12 份 `judge_parse_failures` 全 0。因此
「三遍全同 **且** 全 parse_ok」这个复合条件里, 第二个合取项**一次都没起作用**, I2 实际等价于
「三遍全同」。这不是错误 (条件写着是对的), 但收口文档若把 parse_ok 作为一道独立防线陈述,
属于未经触发的防线, 应标注「本次未触发」。

### F-6 (LOW) — 总均值方向与 E1 结论相反, 收口文档应并列

按 §5 复算, cards 三遍总均值 study 平均 **0.8843** vs both 平均 **0.8773** —— both 档整体
略低。E1 因过滤只报出「+2.78pt 收益、零代价」, 两个数放一起会让读者困惑。这不是矛盾
(总均值含不稳定题, E1 不含), 但**方向相反的两个数只报一个**是选择性呈现。

**建议**: E 段并列「配对口径 +2.78pt (n=41)」与「全集三遍均值口径 −0.69pt (n=48)」, 并解释
差异来自过滤。

### F-7 (LOW) — pt 分母 (48/30) 与比较集 (41/29) 不同源

`confirmed_gain_pt` 的分子只在 41 题上产生, 分母却是 48。这是保守方向 (同时压小收益与代价,
本次代价为 0 故不改变判定), 但口径上把两个不同规模的集合混在一个比值里。跨单元比较 pt 时
若比较集大小不同 (如 U6 过滤更严导致 n_compared 降到 30), pt 会因分母不变而失真。

**建议**: pt 旁边固定附 `n_compared`, 或改报 `Σ差 / n_compared` 并注明口径切换。

---

## 11. 抽检方 A 结论

- **64 项声称, 64 项复现, 0 项不一致。** U5 判定 json 在算术层面完全可信, 且我主动加验的
  6 个交叉一致性维度 (id 集、行数、gold 全集、参数桶、fallback、parse) 也全部自洽。
- **但算术正确 ≠ 判据正确。** 两条 HIGH finding 都不是「算错了」, 而是「这把尺子的形状让
  结论偏向一侧」: F-1 的过滤规则单向清除代价证据 (换零假设尺子后代价 2.08pt 现形),
  F-2 的健康信号掩盖了 4 例确认的路由打空 + 兜底失灵。
- **对收口的建议**: E 段与 Task 6 结论句需按 F-1 / F-2 补限定语后再收口; 若维持现判词
  `cheap_on_this_ruler`, 必须在同一段落写明「这把尺子对 2 道最坏界确认的回归不敏感」。
