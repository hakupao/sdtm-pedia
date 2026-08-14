# U3 Task 9 Step 2 — 抽检方 A 独立复算报告 (规则 D)

> 状态: **完成**
> 角色: 抽检方 A (独立 session, 独立代码)
> 日期: 2026-08-14
> 输入: `data/study/st01/eval/runs/{u3_baseline_run,u3_after_run,routing_run}_{1,2,3}.json` (9 份)
> 独立性声明: 未读 `eval/u3_task8_verdict.py` (脚本与其输出), 未读 `evidence/checkpoints/` 与
> `evidence/failures/` 下任何既有判定文档; 全部数字由本报告 §8 贴出的代码从 run json 的
> `detail` 数组逐题重算, 不读 `summary` (`summary` 仅在 §7 自洽性检查中作为被比对方出现)。
> 零题面声明: 本报告不含任何 run json `question` 字段或 gold yml 题面文字; 复算代码在 load
> 阶段即丢弃 `question` 键, 章号只取 gold yml 的 `chapter` 字段。未打开
> `data/study/st01/eval/heldout_banned_terms.txt`。

## 结论速览

| 分块 | 声称条数 | 复现 | 不复现 |
|---|---|---|---|
| A 六条条款 | 6 | 6 | 0 |
| B 改动面 | 1 | 1 | 0 |
| C fatal 方向分布 | 1 | 1 | 0 |
| D 退回验证 | 1 | 1 | 0 |
| E 多数类基线 | 1 | 1 | 0 |
| **合计** | **10** | **10** | **0** |

Task 8 的**每一个数字都复现**, 无一处算错。新增 finding **7 条** (§9), 全部属于
「数字对但判据/证据设计有问题」一类, 其中 **2 条 HIGH** (条款 4 的度量对本次唯一严重回归
完全不敏感; 条款 2/3 可被零信息常量规则满足且常量规则在 heldout 上还赢过真实路由器)。

---

## 0. 复算前置 — fatal 口径源码核对

brief §判据定义 要求先读 `eval/run_routing_eval.py` 源码核对转述。

`score_run` (run_routing_eval.py:156-168) 的实际逻辑:

```python
for g in gold:
    pred = predictions.get(g["id"])
    if pred == g["gold"]:
        exact += 1
    elif pred != "both":   # 错的单库 or 缺失: 该题 recall 归零, 致命
        fatal_items.append(...)
```

逐条比对 brief 转述:

| brief 转述 | 源码 | 判定 |
|---|---|---|
| exact = `pred == gold` | `if pred == g["gold"]` | 一致 |
| gold=study 判成 cdisc → fatal | `pred != gold and pred != "both"` 覆盖 | 一致 |
| gold=cdisc 判成 study → fatal | 同上 | 一致 |
| gold=both 判成任一单库 → fatal | `pred` 为 cdisc/study 时 `pred != "both"` 成立 | 一致 |
| pred 缺失亦 fatal | `predictions.get()` 返回 `None`, `None != "both"` → fatal | 一致 |
| 判成 both 而 gold 单库 = 错但非 fatal | `elif pred != "both"` 不进 fatal 分支 | 一致 |
| 条款 1 口径 = 全 253 减 final 组 = 250 | `gate_verdict` 取 `group != "final"` 后 `score_run` | 一致 |

**结论: brief 转述与源码完全一致, 此处无 finding。** 补充两点源码事实 (转述未提, 非矛盾):

1. `pred` 若取到 `cdisc/study/both` 之外的任意值也算 fatal。实测 9 份 run 的 `pred` 取值域
   严格 ⊆ {cdisc, study, both}, 缺失 0 条 (见 §7), 故该分支未被触发。
2. `gate_verdict` 的 `passed` = `fatal == 0 and legacy_exact >= 178`, **不含** `score_run`
   内部那个 `acc >= 0.95` 阈值; 但 `summary.by_group` 各组仍各自携带一个用 0.95 算出的
   `passed` 字段 (见 §9 Finding A-7)。

---

## 1. 条款逐条复算 (A)

计算写法统一: 从 `detail` 建 `id -> {group, gold, pred}` 字典, 断言 253 题 / 分组题量等于
spec §5.2 期望 / 九份 run 的 `(id → gold, group)` 完全一致 (否则跨 run 比较无意义) —— 三个
断言全过。

### 条款 1 — fatal_excl_final = 9 三遍同; legacy exact 179/181 (基线也是 179; floor 178)

| run | n_scored_excl_final | fatal | legacy exact | legacy ≥ floor(178) |
|---|---|---|---|---|
| base 1 / 2 / 3 | 250 / 250 / 250 | **10 / 10 / 10** | 179/181 三遍同 | 是 |
| after 1 / 2 / 3 | 250 / 250 / 250 | **9 / 9 / 9** | 179/181 三遍同 | 是 |
| revert 1 / 2 / 3 | 250 / 250 / 250 | **10 / 10 / 10** | 179/181 三遍同 | 是 |

after 三遍 fatal id 名单完全相同:
`u3_amb_01, u3_amb_02, u3_amb_04, u3_amb_06, u3_dist_05, u3_dist_07, u3_dist_10, u3_dist_11, u3_doc_02`

**复现。** 附带核实两点: (a) 基线 legacy 也是 179, 与声称一致; (b) legacy 的那 2 道错题在
基线与 after 完全相同 —— `q124` (gold=cdisc, pred=both) 与 `st_st01_v11_q17` (gold=study,
pred=both), **两道都是 non-fatal 的 `both` 过判**, 即 legacy 组对 fatal 的贡献恒为 0。

### 条款 2 — dev 100% / heldout 91.67%, gap 8.33pt

| run | dev | heldout | gap |
|---|---|---|---|
| after 1/2/3 | 12/12 = 100.00% | 11/12 = 91.67% | 8.33pt |
| base 1/2/3 | 12/12 = 100.00% | 11/12 = 91.67% | 8.33pt |

**复现。** 注意基线读数与 after **完全相同** (见 Finding A-4)。

### 条款 3 — dev 12/12

after 三遍均 12/12 (100%), 基线三遍亦 12/12。**复现。**

### 条款 4 — distractor exact 基线 7/12 → after 7/12, drop 0

| run | distractor_cdisc exact | 错题 id 名单 |
|---|---|---|
| base 1/2/3 | 7/12 | `u3_dist_04, u3_dist_05, u3_dist_07, u3_dist_10, u3_dist_11` |
| after 1/2/3 | 7/12 | `u3_dist_04, u3_dist_05, u3_dist_07, u3_dist_10, u3_dist_11` |

drop = 0。**数字复现**, 且错题 id 名单前后一模一样。

⚠ 但这五题的**严重度**变了: `u3_dist_05` 由 `both` (非致命错) 变为 `study` (致命错)。
exact 口径对此完全不可见 —— 详见 Finding A-1 (HIGH)。

### 条款 5 — final 基线 0/3 → after 1/3 (q15 修好, q17/q53 仍错)

| run | final exact | docs_v1_q15 | docs_v1_q17 | docs_v1_q53 |
|---|---|---|---|---|
| base 1/2/3 | 0/3 | cdisc | cdisc | cdisc |
| after 1/2/3 | **1/3** | **study** (修好) | cdisc | cdisc |
| revert 1/2/3 | 0/3 | cdisc | cdisc | cdisc |

三题 gold 均为 study。**复现。**

### 条款 6 — 三遍 253/253 逐题一致 (unstable=0), 基线三遍亦然

用 id 对齐逐题配对比较 (`len({p1, p2, p3}) != 1` 即 unstable), 不用均值推断:

| 组 | stable | unstable | unstable ids |
|---|---|---|---|
| base | 253/253 | 0 | — |
| after | 253/253 | 0 | — |
| revert | 253/253 | 0 | — |

**复现 (就产物内容而言)。** ⚠ 但「三份文件内容一致」与「确实跑了三遍」是两件事, 从这些
产物无法区分 —— 见 Finding A-3 (MEDIUM)。

---

## 2. 改动面复算 (B)

对全 253 题逐 run 配对比较 `base[i].pred` vs `after[i].pred`:

| run | 变化题数 | 明细 (id[group] gold: base→after) |
|---|---|---|
| 1 | **4** | 见下表 |
| 2 | **4** | 同 run1 |
| 3 | **4** | 同 run1 |

三遍改动集合是否相同: **True** (三个 frozenset 去重后只剩 1 个)。

| id | group | gold | base → after | 性质 |
|---|---|---|---|---|
| `docs_v1_q15` | final | study | cdisc → study | 修好 |
| `u3_amb_03` | ambiguous_both | both | study → both | 修好 (fatal 消除) |
| `u3_amb_05` | ambiguous_both | both | study → both | 修好 (fatal 消除) |
| `u3_dist_05` | distractor_cdisc | cdisc | both → study | 仍错, **非致命错 → 致命错** |

**复现** (题数 4 / 三遍一致 / 四题 id 与方向与性质均与声称逐字相符)。

**独立收支平账 (跨 A1/B/C 三处自洽性交叉核对)**:
基线 fatal 10 − `u3_amb_03` 修好(−1) − `u3_amb_05` 修好(−1) + `u3_dist_05` 致命化(+1) = **9**
= after fatal。`docs_v1_q15` 属 final 组, 不计入 `fatal_excl_final`, 故对该数无贡献。
账平, 三处声称互相自洽。

---

## 3. fatal 方向分布复算 (C)

从 fatal 题的 `(gold, pred)` 二元组做 Counter:

| 方向 | 基线 (10) | after (9) |
|---|---|---|
| both → study | **6**: `u3_amb_01..06` | **4**: `u3_amb_01, 02, 04, 06` |
| cdisc → study | **3**: `u3_dist_07, 10, 11` | **4**: `u3_dist_05, 07, 10, 11` |
| study → cdisc | **1**: `u3_doc_02` | **1**: `u3_doc_02` |

**复现** (数量与 id 名单逐一相符)。补充: 两态下 fatal 方向都**只有三种**, 不存在
`study→both` / `cdisc→both` 之类 (按定义这类非 fatal), 也不存在 `both→cdisc`。

---

## 4. 退回验证复算 (D)

| 配对 | 逐题差异题数 | 判定 |
|---|---|---|
| `routing_run_1` vs `u3_baseline_run_1` | 0 | **EXACT MATCH** |
| `routing_run_2` vs `u3_baseline_run_2` | 0 | **EXACT MATCH** |
| `routing_run_3` vs `u3_baseline_run_3` | 0 | **EXACT MATCH** |

交叉差异矩阵 (任意 base_i × 任意 revert_j, 9 组合): 全为 0 差异。

**复现**, 且实际证据比声称更强: 三对文件 **md5 完全相同**
(`abe721322de6a68f9969502a08c3663c`), 即不只是逐题一致, 是**逐字节一致**。fatal 均为 10。

---

## 5. 多数类基线复算 (E, spec §7.1)

从 gold 分布直接算退化规则得分 (不涉及 pred):

| 集合 | gold 分布 | 多数类 | 退化规则得分 |
|---|---|---|---|
| dev (12) | study 12 | study | 「一律答 study」**12/12 = 100.0%** |
| heldout (12) | study 12 | study | 「一律答 study」**12/12 = 100.0%** |
| 新写 42 | study 24, cdisc 12, both 6 | study | **24/42 = 57.14%** |
| 全 253 | cdisc 163, study 79, both 11 | cdisc | **163/253 = 64.43%** |

**复现** (声称的 57.1% / 64.4% / 163 题 / dev·heldout 各 12/12 全部对上)。

对照实测路由器 (run 1, 三遍同):

| 集合 | 常量基线 | 实测 (base) | 实测 (after) | after − 常量 |
|---|---|---|---|---|
| 全 253 | 64.43% (一律 cdisc) | 93.28% (236/253) | 94.47% (239/253) | **+30.0pt** |
| 新写 42 | 57.14% (一律 study) | 71.43% (30/42) | 76.19% (32/42) | **+19.0pt** |
| dev 12 | **100%** (一律 study) | 100% (12/12) | 100% (12/12) | **0pt (打平)** |
| heldout 12 | **100%** (一律 study) | 91.67% (11/12) | 91.67% (11/12) | **−8.33pt (输)** |

即: 路由器在全集与新写 42 题上明显强于常量规则, 但在 dev/heldout 这两组上**打平与落后** ——
见 Finding A-2 (HIGH)。

---

## 6. 附加交付 (F)

### F1 dev 与 heldout 逐题判定表 (id 级)

两组 gold 全部为 study。`pred×3` 列三遍完全一致 (代码内有
`assert len(set(preds)) == 1` 断言, 未触发)。ch = gold yml 的 `chapter` 字段。

| id | group | ch | gold | base ×3 | after ×3 | base | after |
|---|---|---|---|---|---|---|---|
| u3_doc_01 | dev | 2 | study | study×3 | study×3 | OK | OK |
| u3_doc_03 | dev | 4 | study | study×3 | study×3 | OK | OK |
| u3_doc_05 | dev | 5 | study | study×3 | study×3 | OK | OK |
| u3_doc_07 | dev | 6 | study | study×3 | study×3 | OK | OK |
| u3_doc_09 | dev | 8 | study | study×3 | study×3 | OK | OK |
| u3_doc_11 | dev | 10 | study | study×3 | study×3 | OK | OK |
| u3_doc_13 | dev | 11 | study | study×3 | study×3 | OK | OK |
| u3_doc_15 | dev | 12 | study | study×3 | study×3 | OK | OK |
| u3_doc_17 | dev | 13 | study | study×3 | study×3 | OK | OK |
| u3_doc_19 | dev | 16 | study | study×3 | study×3 | OK | OK |
| u3_doc_21 | dev | 18 | study | study×3 | study×3 | OK | OK |
| u3_doc_23 | dev | 20 | study | study×3 | study×3 | OK | OK |
| **u3_doc_02** | **heldout** | **3** | study | **cdisc×3** | **cdisc×3** | **WRONG** | **WRONG** |
| u3_doc_04 | heldout | 4 | study | study×3 | study×3 | OK | OK |
| u3_doc_06 | heldout | 6 | study | study×3 | study×3 | OK | OK |
| u3_doc_08 | heldout | 7 | study | study×3 | study×3 | OK | OK |
| u3_doc_10 | heldout | 9 | study | study×3 | study×3 | OK | OK |
| u3_doc_12 | heldout | 10 | study | study×3 | study×3 | OK | OK |
| u3_doc_14 | heldout | 12 | study | study×3 | study×3 | OK | OK |
| u3_doc_16 | heldout | 13 | study | study×3 | study×3 | OK | OK |
| u3_doc_18 | heldout | 14 | study | study×3 | study×3 | OK | OK |
| u3_doc_20 | heldout | 17 | study | study×3 | study×3 | OK | OK |
| u3_doc_22 | heldout | 19 | study | study×3 | study×3 | OK | OK |
| u3_doc_24 | heldout | 22 | study | study×3 | study×3 | OK | OK |

dev 12/12, heldout 11/12; 基线与 after 完全相同 (无一题因 Task 7 修法改变)。
唯一错题 `u3_doc_02` (第 3 章) 判成 cdisc, 属 study→cdisc 型 fatal。

### F2 点名「dev 全对而 heldout 全错」的章

**答案: 无 (基线与 after 均为空集)。**

但这个「无」不来自泛化良好, 而来自**两组的章几乎不重叠** —— 唯一的 heldout 错题所在的
第 3 章**没有任何 dev 题**:

| 章 | dev 题数 | heldout 题数 | after dev 对 | after heldout 对 |
|---|---|---|---|---|
| 2 | 1 | 0 | 1/1 | — |
| **3** | **0** | **1** | — | **0/1** |
| 4 | 1 | 1 | 1/1 | 1/1 |
| 5 | 1 | 0 | 1/1 | — |
| 6 | 1 | 1 | 1/1 | 1/1 |
| 7 | 0 | 1 | — | 1/1 |
| 8 | 1 | 0 | 1/1 | — |
| 9 | 0 | 1 | — | 1/1 |
| 10 | 1 | 1 | 1/1 | 1/1 |
| 11 | 1 | 0 | 1/1 | — |
| 12 | 1 | 1 | 1/1 | 1/1 |
| 13 | 1 | 1 | 1/1 | 1/1 |
| 14 | 0 | 1 | — | 1/1 |
| 16 | 1 | 0 | 1/1 | — |
| 17 | 0 | 1 | — | 1/1 |
| 18 | 1 | 0 | 1/1 | — |
| 19 | 0 | 1 | — | 1/1 |
| 20 | 1 | 0 | 1/1 | — |
| 22 | 0 | 1 | — | 1/1 |

覆盖 19 章: 同时有 dev+heldout 的只有 **5 章** (4/6/10/12/13), 只有 dev 的 7 章
(2/5/8/11/16/18/20), 只有 heldout 的 7 章 (3/7/9/14/17/19/22)。基线口径同表, 结论同为「无」。
→ Finding A-5 (MEDIUM)。

### F3 legacy 组 gold=both 的 5 题

| id | gold | base ×3 | after ×3 | base | after |
|---|---|---|---|---|---|
| ja_supp_b01 | both | both×3 | both×3 | OK | OK |
| ja_supp_b02 | both | both×3 | both×3 | OK | OK |
| ja_supp_b03 | both | both×3 | both×3 | OK | OK |
| ja_supp_b04 | both | both×3 | both×3 | OK | OK |
| ja_supp_b05 | both | both×3 | both×3 | OK | OK |

**基线 5/5, after 5/5 —— 都是全对。** 题量断言 `len(both_ids) == 5` 通过 (全 253 的
gold=both 共 11 题 = legacy 5 + ambiguous_both 6, 相加平账)。

### F4 补充 — fatal 的集合归属

| 组 | 题量 | base fatal | after fatal |
|---|---|---|---|
| legacy | 181 | 0 | 0 |
| u1_doc | 27 | 0 | 0 |
| dev | 12 | 0 | 0 |
| heldout | 12 | 1 | 1 |
| distractor_cdisc | 12 | 3 | 4 |
| ambiguous_both | 6 | 6 | 4 |
| (final, 不计入) | 3 | (3) | (2) |
| **合计 excl final** | **250** | **10** | **9** |

老题 (legacy 181 + u1_doc 27 = 208 题) 在两态下 **fatal 恒为 0**; 全部 fatal 集中在新写的
42 题里。u1_doc 27/27 全对。→ Finding A-6。

---

## 7. summary 自洽性检查 (硬规矩 17b: 非自洽复算)

我的 detail 重算值 vs 产物 `summary` 自称值, 逐份逐字段比对:

| run | summary 自称 (fatal / legacy / n / passed) | 我的重算 (fatal / legacy / n) | 判定 |
|---|---|---|---|
| base 1/2/3 | 10 / 179 / 250 / False | 10 / 179 / 250 | 一致 |
| after 1/2/3 | 9 / 179 / 250 / False | 9 / 179 / 250 | 一致 |
| revert 1/2/3 | 10 / 179 / 250 / False | 10 / 179 / 250 | 一致 |

另比对了每份 run 的 `summary.by_group` 各组 `(exact, n)` 与 `summary.fatal_ids_excl_final`
名单 —— **9 份 × 7 组 全部一致, 名单也逐 id 一致**, 无任何不符 (代码在不符时会打
`FINDING`, 未打出)。

pred 值域与 schema 检查 (9 份全同):
- `pred` 取值域 ⊆ {cdisc, study, both}, **缺失 0 条**, 无越界值。
- pred 分布: base/revert = cdisc 161 / study 83 / both 9; after = cdisc 160 / study 83 / both 10。
  (对照 gold 分布 cdisc 163 / study 79 / both 11 —— 路由器 `both` 判得偏少。)
- `detail` 项 keys = `[gold, group, id, pred, question]`; `summary` keys =
  `[by_group, fatal_excl_final, fatal_ids_excl_final, legacy_exact, legacy_floor,
  n_scored_excl_final, passed]` —— **无任何 run 级元数据** (无 timestamp / run index /
  fallback 计数 / 原始响应)。→ Finding A-3。

**结论: summary 与 detail 完全自洽, 此处无 finding。** 另注: 9 份 run 的
`summary.passed` **全为 False** —— 条款 1 在基线 / after / 退回**三态下都是 FAIL**
(fatal 10 / 9 / 10 均 ≠ 0), 而 `legacy_exact >= 178` 这一半三态都满足。即卡住条款 1 的
自始至终只有 `fatal == 0`, Task 7 修法只把 fatal 从 10 降到 9, 未跨过门槛。

---

## 8. 复算代码 (可复跑)

三个脚本均放仓外路径 `/private/tmp/claude-501/.../scratchpad/`, 未写入本仓。
**代码内无任何题面字面量**; `question` 键在 load 阶段即被丢弃。

### 8.1 `audit_a.py` — 条款 A1-A6 / B / C / D / E / 自洽性

```python
"""U3 Task 9 抽检方 A — 独立复算 (只从 run json 的 detail 逐题重算)。

零题面纪律: 本脚本只从 detail 取 id/group/gold/pred, question 字段在 load 时即丢弃,
任何输出通道都不可能带出题面。
"""
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

RUNS = Path("/Users/bojiangzhang/MyProject/sdtm-pedia/sdtm-rag/data/study/st01/eval/runs")
EXPECTED_SIZES = {"legacy": 181, "u1_doc": 27, "final": 3, "dev": 12,
                  "heldout": 12, "distractor_cdisc": 12, "ambiguous_both": 6}
FINAL_IDS = {"docs_v1_q15", "docs_v1_q17", "docs_v1_q53"}


def load(name):
    """→ (rows, raw_summary)。rows: id -> {group, gold, pred}; question 在此丢弃。"""
    raw = json.loads((RUNS / f"{name}.json").read_text(encoding="utf-8"))
    rows = {}
    for d in raw["detail"]:
        assert d["id"] not in rows, f"{name}: id 重复 {d['id']}"
        rows[d["id"]] = {"group": d["group"], "gold": d["gold"], "pred": d.get("pred")}
    return rows, raw["summary"]


SETS = {
    "base": [f"u3_baseline_run_{i}" for i in (1, 2, 3)],
    "after": [f"u3_after_run_{i}" for i in (1, 2, 3)],
    "revert": [f"routing_run_{i}" for i in (1, 2, 3)],
}
DATA = {k: [load(n) for n in v] for k, v in SETS.items()}


def is_fatal(gold, pred):
    """score_run 口径: 判对不 fatal; 判错且 pred != 'both' (含缺失) 即 fatal。"""
    return pred != gold and pred != "both"


def sec(t):
    print("\n" + "=" * 72 + f"\n{t}\n" + "=" * 72)


# ---------------------------------------------------------------- 结构前置
sec("S0 结构前置 (题量 / 分组 / gold-group 稳定性)")
for tag, runs in DATA.items():
    for i, (rows, _) in enumerate(runs, 1):
        assert len(rows) == 253, f"{tag}{i}: 题量 {len(rows)} != 253"
        sizes = Counter(r["group"] for r in rows.values())
        assert dict(sizes) == EXPECTED_SIZES, f"{tag}{i}: 分组 {dict(sizes)}"
        assert sum(sizes.values()) == 253
# 九份 run 的 (id -> gold, group) 必须完全一致, 否则跨 run 比较无意义
ref = {i: (r["gold"], r["group"]) for i, r in DATA["base"][0][0].items()}
for tag, runs in DATA.items():
    for i, (rows, _) in enumerate(runs, 1):
        cur = {i2: (r["gold"], r["group"]) for i2, r in rows.items()}
        assert cur == ref, f"{tag}{i}: gold/group 与基线 run1 不一致"
assert {i for i, (_, g) in ref.items() if g == "final"} == FINAL_IDS
print("9 份 run: 各 253 题, 分组 = spec §5.2 期望, (id→gold,group) 九份完全一致")
print("group sizes:", dict(sorted(Counter(g for _, g in ref.values()).items())))
print("gold 分布 (全 253):", dict(sorted(Counter(g for g, _ in ref.values()).items())))

# ---------------------------------------------------------------- 条款 1
sec("A1 fatal_excl_final / legacy exact")
for tag in ("base", "after", "revert"):
    for i, (rows, _) in enumerate(DATA[tag], 1):
        fatal = [k for k, r in rows.items()
                 if r["group"] != "final" and is_fatal(r["gold"], r["pred"])]
        n_scored = sum(1 for r in rows.values() if r["group"] != "final")
        assert n_scored == 250, n_scored
        leg = [k for k, r in rows.items() if r["group"] == "legacy"]
        leg_exact = sum(1 for k in leg if rows[k]["pred"] == rows[k]["gold"])
        print(f"{tag}{i}: n_scored_excl_final={n_scored} fatal={len(fatal)} "
              f"legacy_exact={leg_exact}/{len(leg)} floor=178 "
              f"legacy_ok={leg_exact >= 178}")
        print(f"      fatal ids: {sorted(fatal)}")

# ---------------------------------------------------------------- 条款 2/3
sec("A2/A3 dev vs heldout")
for tag in ("base", "after"):
    for i, (rows, _) in enumerate(DATA[tag], 1):
        out = []
        for g in ("dev", "heldout"):
            sub = [k for k, r in rows.items() if r["group"] == g]
            ex = sum(1 for k in sub if rows[k]["pred"] == rows[k]["gold"])
            out.append((g, ex, len(sub), 100.0 * ex / len(sub)))
        gap = out[0][3] - out[1][3]
        print(f"{tag}{i}: dev {out[0][1]}/{out[0][2]}={out[0][3]:.2f}%  "
              f"heldout {out[1][1]}/{out[1][2]}={out[1][3]:.2f}%  gap={gap:.2f}pt")

# ---------------------------------------------------------------- 条款 4
sec("A4 distractor_cdisc exact 基线 vs after")
for tag in ("base", "after"):
    for i, (rows, _) in enumerate(DATA[tag], 1):
        sub = [k for k, r in rows.items() if r["group"] == "distractor_cdisc"]
        ex = sum(1 for k in sub if rows[k]["pred"] == rows[k]["gold"])
        wrong = sorted(k for k in sub if rows[k]["pred"] != rows[k]["gold"])
        print(f"{tag}{i}: distractor exact {ex}/{len(sub)}  错题 {wrong}")

# ---------------------------------------------------------------- 条款 5
sec("A5 final 组 (3 题) 基线 vs after")
for tag in ("base", "after", "revert"):
    for i, (rows, _) in enumerate(DATA[tag], 1):
        sub = sorted(k for k, r in rows.items() if r["group"] == "final")
        ex = sum(1 for k in sub if rows[k]["pred"] == rows[k]["gold"])
        det = {k: rows[k]["pred"] for k in sub}
        print(f"{tag}{i}: final exact {ex}/3  gold=study  pred={det}")

# ---------------------------------------------------------------- 条款 6
sec("A6 三遍逐题一致性 (id 对齐配对比较)")
for tag in ("base", "after", "revert"):
    r1, r2, r3 = (d[0] for d in DATA[tag])
    unstable = sorted(k for k in r1
                      if len({r1[k]["pred"], r2[k]["pred"], r3[k]["pred"]}) != 1)
    stable = 253 - len(unstable)
    assert stable + len(unstable) == 253
    print(f"{tag}: stable {stable}/253  unstable={len(unstable)}  ids={unstable}")

# ---------------------------------------------------------------- B 改动面
sec("B 基线→after 改动面 (全 253 题, 逐 run 配对 + 三遍一致性)")
for i in range(3):
    b, a = DATA["base"][i][0], DATA["after"][i][0]
    ch = sorted(k for k in b if b[k]["pred"] != a[k]["pred"])
    print(f"run{i+1}: 变化 {len(ch)} 题 -> "
          + "; ".join(f"{k}[{b[k]['group']}] gold={b[k]['gold']} "
                      f"{b[k]['pred']}→{a[k]['pred']} "
                      f"({'修好' if a[k]['pred'] == b[k]['gold'] else '仍错'}"
                      f"{'/致命化' if not is_fatal(b[k]['gold'], b[k]['pred']) and is_fatal(a[k]['gold'], a[k]['pred']) else ''}"
                      f")" for k in ch))
sets = [frozenset(k for k in DATA["base"][i][0]
                  if DATA["base"][i][0][k]["pred"] != DATA["after"][i][0][k]["pred"])
        for i in range(3)]
print("三遍改动集合是否相同:", len(set(sets)) == 1)

# ---------------------------------------------------------------- C fatal 方向
sec("C fatal 方向分布 (gold→pred)")
for tag in ("base", "after"):
    rows = DATA[tag][0][0]
    fat = [(k, rows[k]["gold"], rows[k]["pred"]) for k in sorted(rows)
           if rows[k]["group"] != "final" and is_fatal(rows[k]["gold"], rows[k]["pred"])]
    dist = Counter((g, p) for _, g, p in fat)
    print(f"{tag} (run1): fatal={len(fat)}")
    for (g, p), n in sorted(dist.items()):
        ids = sorted(k for k, gg, pp in fat if (gg, pp) == (g, p))
        print(f"   {g}→{p}: {n}  {ids}")

# ---------------------------------------------------------------- D 退回验证
sec("D 退回验证: routing_run_{1,2,3} vs u3_baseline_run_{1,2,3}")
for i in range(3):
    b, r = DATA["base"][i][0], DATA["revert"][i][0]
    diff = sorted(k for k in b if b[k]["pred"] != r[k]["pred"])
    print(f"run{i+1}: 逐题差异 {len(diff)} 题 {diff} -> "
          f"{'EXACT MATCH' if not diff else 'MISMATCH'}")
# 交叉矩阵: 任意 revert run 与任意 baseline run
cross = {}
for bi in range(3):
    for ri in range(3):
        b, r = DATA["base"][bi][0], DATA["revert"][ri][0]
        cross[(bi + 1, ri + 1)] = sum(1 for k in b if b[k]["pred"] != r[k]["pred"])
print("交叉差异矩阵 base_i x revert_j:", cross)

# ---------------------------------------------------------------- E 多数类
sec("E 多数类基线 (spec §7.1)")
gold_all = Counter(g for g, _ in ref.values())
print("全 253 gold 分布:", dict(sorted(gold_all.items())))
top, n = gold_all.most_common(1)[0]
print(f"全 253 多数类 = {top} {n}/253 = {100.0*n/253:.2f}%")
NEW = ("dev", "heldout", "distractor_cdisc", "ambiguous_both")
new_ids = [i for i, (_, g) in ref.items() if g in NEW]
assert len(new_ids) == 42, len(new_ids)
gold_new = Counter(ref[i][0] for i in new_ids)
tn, nn = gold_new.most_common(1)[0]
print("新写 42 gold 分布:", dict(sorted(gold_new.items())),
      f"多数类 = {tn} {nn}/42 = {100.0*nn/42:.2f}%")
for g in ("dev", "heldout"):
    sub = [i for i, (_, gg) in ref.items() if gg == g]
    gs = Counter(ref[i][0] for i in sub)
    always_study = sum(1 for i in sub if ref[i][0] == "study")
    print(f"{g}: gold 分布 {dict(gs)} -> 「一律答 study」退化规则 "
          f"{always_study}/{len(sub)} = {100.0*always_study/len(sub):.1f}%")

# ---------------------------------------------------------------- 自洽性
sec("S 自洽性: 我的 detail 重算 vs 产物 summary 自称")
for tag in ("base", "after", "revert"):
    for i, (rows, summ) in enumerate(DATA[tag], 1):
        mine_fatal = sum(1 for r in rows.values()
                         if r["group"] != "final" and is_fatal(r["gold"], r["pred"]))
        mine_leg = sum(1 for r in rows.values()
                       if r["group"] == "legacy" and r["pred"] == r["gold"])
        mine_n = sum(1 for r in rows.values() if r["group"] != "final")
        ok = (summ.get("fatal_excl_final") == mine_fatal
              and summ.get("legacy_exact") == mine_leg
              and summ.get("n_scored_excl_final") == mine_n)
        print(f"{tag}{i}: summary(fatal={summ.get('fatal_excl_final')}, "
              f"legacy={summ.get('legacy_exact')}, n={summ.get('n_scored_excl_final')}, "
              f"passed={summ.get('passed')}) | mine(fatal={mine_fatal}, "
              f"legacy={mine_leg}, n={mine_n}) -> {'一致' if ok else '不一致 FINDING'}")
        # by_group 每组 exact 也对
        for gname, gs in (summ.get("by_group") or {}).items():
            me = sum(1 for r in rows.values()
                     if r["group"] == gname and r["pred"] == r["gold"])
            mn = sum(1 for r in rows.values() if r["group"] == gname)
            if (gs.get("exact"), gs.get("n")) != (me, mn):
                print(f"      FINDING by_group {gname}: summary {gs.get('exact')}/"
                      f"{gs.get('n')} vs mine {me}/{mn}")
        # fatal_ids 名单
        mine_ids = sorted(k for k, r in rows.items()
                          if r["group"] != "final" and is_fatal(r["gold"], r["pred"]))
        if sorted(summ.get("fatal_ids_excl_final") or []) != mine_ids:
            print(f"      FINDING fatal_ids 名单不一致")
```

### 8.2 `audit_a_f.py` — 附加交付 F (逐题表 / 章聚合 / legacy both)

```python
"""U3 Task 9 抽检方 A — 附加交付 F。

零题面纪律: gold yml 只取 id / chapter / group / gold 四个键, question 立即丢弃;
输出通道只出现 id / 章号 / 标签, 不可能带出题面。
"""
from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path

import yaml

ROOT = Path("/Users/bojiangzhang/MyProject/sdtm-pedia/sdtm-rag")
RUNS = ROOT / "data/study/st01/eval/runs"
GOLD_YML = ROOT / "data/study/st01/eval/routing_gold_docs.yml"


def load(name):
    raw = json.loads((RUNS / f"{name}.json").read_text(encoding="utf-8"))
    return {d["id"]: {"group": d["group"], "gold": d["gold"], "pred": d.get("pred")}
            for d in raw["detail"]}


base = [load(f"u3_baseline_run_{i}") for i in (1, 2, 3)]
after = [load(f"u3_after_run_{i}") for i in (1, 2, 3)]

# --- 章号: 只取 id -> chapter, 不取 question
raw_gold = yaml.safe_load(GOLD_YML.read_text(encoding="utf-8")) or []
chap = {q["id"]: q.get("chapter") for q in raw_gold}
assert len(chap) == 42, len(chap)
del raw_gold  # 立即丢弃含题面的原始结构

print("=" * 72)
print("F1 dev / heldout 逐题判定表 (gold 全为 study)")
print("=" * 72)
print(f"{'id':<14}{'group':<9}{'ch':<6}{'gold':<7}{'base x3':<22}{'after x3':<22}"
      f"{'base':<6}{'after':<6}")
rows = []
for g in ("dev", "heldout"):
    ids = sorted(k for k, r in base[0].items() if r["group"] == g)
    assert len(ids) == 12, (g, len(ids))
    for k in ids:
        gold = base[0][k]["gold"]
        bp = [b[k]["pred"] for b in base]
        ap = [a[k]["pred"] for a in after]
        bok = "OK" if all(p == gold for p in bp) else "WRONG"
        aok = "OK" if all(p == gold for p in ap) else "WRONG"
        assert len(set(bp)) == 1 and len(set(ap)) == 1, k  # 三遍不一致就炸
        rows.append((k, g, chap.get(k), gold, bp, ap, bok, aok))
        print(f"{k:<14}{g:<9}{str(chap.get(k)):<6}{gold:<7}"
              f"{'/'.join(bp):<22}{'/'.join(ap):<22}{bok:<6}{aok:<6}")

print()
print("=" * 72)
print("F2 按章聚合: 是否存在「dev 全对而 heldout 全错」的章")
print("=" * 72)
bych = defaultdict(lambda: {"dev": [], "heldout": []})
for k, g, c, gold, bp, ap, bok, aok in rows:
    bych[c][g].append((k, bok, aok))
for c in sorted(bych, key=lambda x: (x is None, str(x))):
    d, h = bych[c]["dev"], bych[c]["heldout"]
    dev_all_ok_a = bool(d) and all(x[2] == "OK" for x in d)
    held_all_wrong_a = bool(h) and all(x[2] == "WRONG" for x in h)
    dev_all_ok_b = bool(d) and all(x[1] == "OK" for x in d)
    held_all_wrong_b = bool(h) and all(x[1] == "WRONG" for x in h)
    flag_a = "★命中(after)" if (dev_all_ok_a and held_all_wrong_a) else ""
    flag_b = "★命中(base)" if (dev_all_ok_b and held_all_wrong_b) else ""
    print(f"章 {str(c):<5} dev {sum(1 for x in d if x[2]=='OK')}/{len(d)} "
          f"heldout {sum(1 for x in h if x[2]=='OK')}/{len(h)} (after) | "
          f"dev {sum(1 for x in d if x[1]=='OK')}/{len(d)} "
          f"heldout {sum(1 for x in h if x[1]=='OK')}/{len(h)} (base) {flag_a}{flag_b}")
hits = [c for c in bych
        if bych[c]["dev"] and bych[c]["heldout"]
        and all(x[2] == "OK" for x in bych[c]["dev"])
        and all(x[2] == "WRONG" for x in bych[c]["heldout"])]
print("命中章 (after):", sorted(map(str, hits)) or "无")
hits_b = [c for c in bych
          if bych[c]["dev"] and bych[c]["heldout"]
          and all(x[1] == "OK" for x in bych[c]["dev"])
          and all(x[1] == "WRONG" for x in bych[c]["heldout"])]
print("命中章 (base) :", sorted(map(str, hits_b)) or "无")
print("章覆盖 (dev/heldout 各章题数):",
      {str(c): (len(bych[c]["dev"]), len(bych[c]["heldout"])) for c in sorted(bych, key=str)})

print()
print("=" * 72)
print("F3 legacy 组 gold=both 的题 (基线 / after 是否 5/5)")
print("=" * 72)
both_ids = sorted(k for k, r in base[0].items()
                  if r["group"] == "legacy" and r["gold"] == "both")
print(f"legacy gold=both 题量 = {len(both_ids)}: {both_ids}")
assert len(both_ids) == 5, len(both_ids)
nb = na = 0
for k in both_ids:
    bp = [b[k]["pred"] for b in base]
    ap = [a[k]["pred"] for a in after]
    ok_b = all(p == "both" for p in bp)
    ok_a = all(p == "both" for p in ap)
    nb += ok_b
    na += ok_a
    print(f"{k:<22} gold=both  base={'/'.join(bp):<18} after={'/'.join(ap):<18} "
          f"base={'OK' if ok_b else 'WRONG'} after={'OK' if ok_a else 'WRONG'}")
print(f"合计: 基线 {nb}/5, after {na}/5")

print()
print("=" * 72)
print("F4 legacy 组 2 道错题定位 (179/181 的另外 2 题)")
print("=" * 72)
for tag, D in (("base", base), ("after", after)):
    wrong = sorted(k for k, r in D[0].items()
                   if r["group"] == "legacy" and r["pred"] != r["gold"])
    items = [(k, D[0][k]["gold"], D[0][k]["pred"],
              "fatal" if D[0][k]["pred"] != "both" else "non-fatal") for k in wrong]
    print(tag + ": " + str(items))

print()
print("=" * 72)
print("F5 u1_doc 组 (27 题) 与 u3_doc_02 归属")
print("=" * 72)
for tag, D in (("base", base), ("after", after)):
    sub = [k for k, r in D[0].items() if r["group"] == "u1_doc"]
    ex = sum(1 for k in sub if D[0][k]["pred"] == D[0][k]["gold"])
    wrong = sorted(k for k in sub if D[0][k]["pred"] != D[0][k]["gold"])
    print(f"{tag}: u1_doc exact {ex}/{len(sub)}  错题 {wrong}")
print("u3_doc_02 的 group/gold/pred:",
      {t: (D[0]["u3_doc_02"] if "u3_doc_02" in D[0] else None)
       for t, D in (("base", base), ("after", after))})
print("u3_doc_02 章号:", chap.get("u3_doc_02"))
```

### 8.3 `audit_a_dom.py` / `audit_a_e2.py` — pred 值域 / schema / 常量基线对照

```python
# audit_a_dom.py
import json
from collections import Counter
from pathlib import Path
RUNS = Path("/Users/bojiangzhang/MyProject/sdtm-pedia/sdtm-rag/data/study/st01/eval/runs")
names = ([f"u3_baseline_run_{i}" for i in (1,2,3)] + [f"u3_after_run_{i}" for i in (1,2,3)]
         + [f"routing_run_{i}" for i in (1,2,3)])
for n in names:
    raw = json.loads((RUNS / f"{n}.json").read_text(encoding="utf-8"))
    preds = [d.get("pred") for d in raw["detail"]]
    miss = sum(1 for p in preds if p is None)
    dom = Counter(preds)
    bad = {k for k in dom if k not in ("cdisc","study","both")}
    keys = sorted({k for d in raw["detail"] for k in d})
    print(f"{n}: pred 取值 {dict(sorted(dom.items()))} 缺失={miss} 越界={bad or '无'} "
          f"| detail keys={keys} | summary keys={sorted(raw['summary'])}")

# audit_a_e2.py
import json
from collections import Counter
from pathlib import Path
RUNS = Path("/Users/bojiangzhang/MyProject/sdtm-pedia/sdtm-rag/data/study/st01/eval/runs")
def load(n):
    return {d["id"]: {"group": d["group"], "gold": d["gold"], "pred": d.get("pred")}
            for d in json.loads((RUNS / f"{n}.json").read_text(encoding="utf-8"))["detail"]}
for tag, n in (("base", "u3_baseline_run_1"), ("after", "u3_after_run_1")):
    r = load(n)
    ex = sum(1 for v in r.values() if v["pred"] == v["gold"])
    ex250 = sum(1 for v in r.values() if v["group"] != "final" and v["pred"] == v["gold"])
    maj = Counter(v["gold"] for v in r.values()).most_common(1)[0]
    print(f"{tag}: 全 253 exact {ex}/253 = {100*ex/253:.2f}%   "
          f"excl_final {ex250}/250 = {100*ex250/250:.2f}%"
          f"   |「一律答 {maj[0]}」常量基线 {maj[1]}/253 = {100*maj[1]/253:.2f}%")
    NEW = ("dev","heldout","distractor_cdisc","ambiguous_both")
    sub = [v for v in r.values() if v["group"] in NEW]
    exn = sum(1 for v in sub if v["pred"] == v["gold"])
    majn = Counter(v["gold"] for v in sub).most_common(1)[0]
    print(f"      新写 42: 实测 exact {exn}/42 = {100*exn/42:.2f}%  "
          f"vs 常量「一律答 {majn[0]}」{majn[1]}/42 = {100*majn[1]/42:.2f}%")
```

### 8.4 产物指纹 / 时间戳 (shell)

```sh
cd /Users/bojiangzhang/MyProject/sdtm-pedia/sdtm-rag/data/study/st01/eval/runs
md5 u3_baseline_run_*.json u3_after_run_*.json routing_run_{1,2,3}.json
stat -f "%Sm %N" -t "%Y-%m-%d %H:%M:%S" \
  u3_baseline_run_*.json u3_after_run_*.json routing_run_{1,2,3}.json
```

实测输出:

```
MD5 (u3_baseline_run_1.json) = abe721322de6a68f9969502a08c3663c
MD5 (u3_baseline_run_2.json) = abe721322de6a68f9969502a08c3663c
MD5 (u3_baseline_run_3.json) = abe721322de6a68f9969502a08c3663c
MD5 (u3_after_run_1.json)    = 55a0d8fa3d44d44067b6071dd615da35
MD5 (u3_after_run_2.json)    = 55a0d8fa3d44d44067b6071dd615da35
MD5 (u3_after_run_3.json)    = 55a0d8fa3d44d44067b6071dd615da35
MD5 (routing_run_1.json)     = abe721322de6a68f9969502a08c3663c
MD5 (routing_run_2.json)     = abe721322de6a68f9969502a08c3663c
MD5 (routing_run_3.json)     = abe721322de6a68f9969502a08c3663c
2026-08-14 01:26:50 u3_baseline_run_1.json
2026-08-14 01:26:50 u3_baseline_run_2.json
2026-08-14 01:26:50 u3_baseline_run_3.json
2026-08-14 15:54:41 u3_after_run_1.json
2026-08-14 15:54:41 u3_after_run_2.json
2026-08-14 15:54:41 u3_after_run_3.json
2026-08-14 16:19:19 routing_run_1.json
2026-08-14 16:22:07 routing_run_2.json
2026-08-14 16:24:59 routing_run_3.json
```

---

## 9. 新 finding 汇总 (7 条, 均非「数字算错」)

### Finding A-1 (HIGH) — 条款 4 的度量对本次修法引入的唯一严重回归完全不敏感

条款 4 用 `distractor exact` 的 drop 判「无回归」: 基线 7/12 → after 7/12, drop = 0, 判过。
但同期 `u3_dist_05` 由 `both` (非致命错) 恶化为 `study` (致命错) —— 错题 id 名单一字未变,
exact 计数一分未动, **而这是整个 Task 7 修法引入的唯一一处严重回归**。抓到它的只有条款 1
的 fatal 口径 (`cdisc→study` 从 3 涨到 4)。
建议: 条款 4 改为同时看该组 `fatal` 数 (基线 3 → after 4) 或错误方向分布, 否则「exact 不降」
可以掩盖任意规模的 non-fatal→fatal 恶化 (极端情形: 12 题全部由 `both` 变错单库, exact 仍
7/12, 条款 4 照样判过, 而该组 recall 已全线归零)。

### Finding A-2 (HIGH) — 条款 2/3 可被零信息常量规则满足, 且常量规则在 heldout 上赢过真实路由器

dev 与 heldout 两组 **gold 全部为 study** (各 12/12)。因此「一律答 study」这个不看题目的
常量规则在 dev 得 12/12 (100%)、在 heldout 得 12/12 (100%), 两条条款 (gap ≤ 25pt / dev ≥
10/12) **都被满足且余量极大**。实测路由器: dev 12/12 (与常量打平)、heldout 11/12 (**比常量
低 8.33pt**)。
即条款 2/3 对「路由器是否真的在路由」零判别力, 而唯一一次两者分道扬镳时, 路由器是**输**的
那一方。dev/heldout 的 gold 标签单一化 (统一 study) 是根因。
建议: 给 dev/heldout 各掺入 gold=cdisc 与 gold=both 的题, 使常量规则不再能满分; 或在
verdict 中并列打印常量基线, 让条款 2/3 的读数自带参照物。

### Finding A-3 (MEDIUM) — run json 无 run 级元数据, 「跑了三遍」这件事从产物不可证伪

`detail` 项 keys 只有 `[gold, group, id, pred, question]`, `summary` 只有判定字段, **无
timestamp / run index / fallback 计数 / 原始响应 / 耗时**。当 stability = 253/253 时, 三份
文件必然逐字节相同 —— 实测三组 md5 分别只有一个值。因此「一次跑复制三份」与「真跑三遍且
全一致」产生**完全相同的证据**, 条款 6 从产物层面不可证伪。
旁证: `u3_baseline_run_{1,2,3}` mtime 全为 `01:26:50` (同秒), `u3_after_run_{1,2,3}` 全为
`15:54:41` (同秒) —— 单次复制归档的签名; 而 `run_routing_eval.py` 逐 run 落盘的
`routing_run_{1,2,3}` mtime 为 `16:19:19 / 16:22:07 / 16:24:59` (间隔 2m48s / 2m52s), 才是
三遍顺序跑的签名。
说明: 这**不**指控 after/baseline 造假 —— 归档 (cp) 会抹平 mtime 是正常的; 指的是证据设计
使该声称不可独立验证。
建议: run json 加 `run_index` / `started_at` / `n_fallback` 字段, 或归档时保留原件时间戳
(`cp -p`)。

### Finding A-4 (MEDIUM) — 条款 2/3/4 在本次修法前后读数完全相同, 对该修法零判别力

dev (12/12)、heldout (11/12, 错题恒为 `u3_doc_02`)、distractor (7/12, 错题名单五个 id 完全
相同) —— 三组的 exact 读数与错题名单在基线与 after **一字不差**。本次修法只在条款 1 (fatal
10→9) 与条款 5 (final 0/3→1/3) 上产生可见变化。
即 spec §7 六条条款中有三条对本次改动没有任何信息量, 报告若并列陈述六条「均已核查」会让读者
高估验证覆盖面。

### Finding A-5 (MEDIUM) — dev 与 heldout 的章覆盖几乎不重叠, gap 度量分辨率极低

19 个章里只有 **5 章** (4/6/10/12/13) 同时有 dev 与 heldout 题; 7 章只有 dev, 7 章只有
heldout。heldout 唯一的错题 `u3_doc_02` 落在**第 3 章, 而第 3 章没有任何 dev 题**。
后果: (a) F 要求点名的「dev 全对而 heldout 全错的章」结果为**空集**, 但这个「无」是章不重叠
造成的, 不是泛化良好的证据; (b) dev−heldout gap 混淆了「章难度差异」与「是否被用于调参」,
不能当泛化差距读。
建议: 若要用 dev/heldout 度量泛化, 应按章配对抽样 (同章内 split), 而非按 id 奇偶切分。

### Finding A-6 (LOW) — 全部 fatal 集中在新写的 42 题, 老题 208 题 fatal 恒为 0

legacy 181 + u1_doc 27 = 208 题在基线与 after 均 **0 fatal**; legacy 的 2 道错题
(`q124`: cdisc→both, `st_st01_v11_q17`: study→both) 都是 non-fatal 的 `both` 过判, 前后完全
相同; u1_doc 27/27 全对。10/9 个 fatal 全部落在新写 42 题内 (ambiguous_both 6→4,
distractor 3→4, heldout 1→1)。
含义: 条款 1 的 `legacy_exact >= 178` 这半边闸三态都满足且余量 1 题, 从未是约束; 真正卡住
条款 1 的自始至终只有 `fatal == 0`, 且该 fatal 全部来自新写题集。

### Finding A-7 (LOW) — `summary.by_group.*.passed` 与条款 1 的 `passed` 不同源, 易被误读

`score_run` 返回的 `passed` 用的是 `acc >= 0.95 and not fatal_items`, 而 `gate_verdict` 顶层
的 `passed` 用的是 `fatal == 0 and legacy_exact >= 178` —— 两者判据不同。产物 `by_group` 里
每组都带着前者算出的 `passed` (after run: legacy true / u1_doc true / final false /
dev true / heldout false / distractor false / ambiguous_both false)。这些组级 `passed`
**不是 spec §7 任何一条条款**, 但字段名相同, 下游引用极易读成「该组通过闸」。
建议: 组级字段改名 (如 `subset_ok`) 或从产物中去掉。

---

## 10. 纪律自证 (零题面 / 只读 / 独立性)

### 10.1 零题面 — 机械校验 (非人工目测)

把 9 份 run json 的 `question` 与 gold yml 题面 (去重 253 条) 取出, 对本报告与四个脚本做
两级扫描: (a) 整条题面子串命中; (b) 题面去空白后切 **10 字滑窗** (共 21677 个窗口) 逐一
子串命中。脚本只打计数, 不打命中内容。

首轮结果: 整条命中 0, 但 3 条题面各有滑窗命中, **且在全部 5 个文件里都命中** —— 包括仅约
900 字符的 `audit_a_dom.py`, 指向共享词表假阳性。定性 (只显示路径/标识符类字符, 其余打码)
确认命中片段全部是 `collection` / `fromcollec` / `mcollectio` / `omcollecti` / `romcollect`,
来源是我自己代码里的 `from collections import Counter` 一行 (去空白后含 "collections"),
恰好 3 道 CDISC 题含英文单词 collection。

排除该已定性假阳性后复扫:

```
报告 evidence/step_u3_audit.md: 整条命中=0  10字滑窗命中题面数=0/253
脚本 audit_a.py:                整条命中=0  10字滑窗命中题面数=0/253
脚本 audit_a_f.py:              整条命中=0  10字滑窗命中题面数=0/253
脚本 audit_a_dom.py:            整条命中=0  10字滑窗命中题面数=0/253
脚本 audit_a_e2.py:             整条命中=0  10字滑窗命中题面数=0/253

零题面最终判定: PASS
```

未打开 `data/study/st01/eval/heldout_banned_terms.txt`。

### 10.2 只读

除本报告外未修改仓库任何文件; 全部临时脚本 (含上述校验脚本 `leak_check.py` /
`leak_class.py` / `leak_final.py`) 落在仓外路径
`/private/tmp/claude-501/-Users-bojiangzhang-MyProject-sdtm-pedia/.../scratchpad/`。

`git status --short` (在 `/Users/bojiangzhang/MyProject/sdtm-pedia` 执行):

```
?? sdtm-rag/evidence/step_u3_audit.md
```

### 10.3 独立性

未读文件清单 (独立性): `eval/u3_task8_verdict.py`、`evidence/checkpoints/**`、
`evidence/failures/**`、`data/study/st01/eval/heldout_banned_terms.txt`。
读过的仓内文件: 9 份 run json (仅取 id/group/gold/pred)、`eval/run_routing_eval.py` (源码,
brief §判据定义 明确要求)、`data/study/st01/eval/routing_gold_docs.yml` (仅取 id/chapter)。
