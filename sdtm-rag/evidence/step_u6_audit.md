# U6 抽检 A — 非自洽复算报告 (规则 D 五方之一)

> 日期: 2026-08-18
> 角色: 抽检方 A (独立 session, 未参与 U6 任何 Task 的实现或审查)
> 执行目录: `sdtm-rag/`, 解释器 `./.venv/bin/python`
> 方法学 (硬规矩 17b): **不许照抄原实现**。本报告的每一个数字都由抽检方自写的
> 异源代码重算 —— 不 `import eval.run_routing_eval` / `eval.u6_gate_verdict` 的任何
> 计算函数, 判据 (exact / fatal / 口径) 按 spec 语义**重新实现**, 比率一律走
> `fractions.Fraction` 精确算术 (不复用原实现的 `round(...,4)` 浮点路径),
> gold 由六份 yml 独立 `yaml.safe_load` 重建 (不走 `load_gold()`)。
> 红线: 本文件进 git —— 只记 id / 组名 / 数字 / 命令 / rc, **零题面零真名**。
> run json 的 `detail` 行含 `question` 字段, 抽检脚本程序化读取该文件但**从不打印该字段**。
> 抽检脚本落在 session scratchpad (非仓内), 命令与关键逻辑逐条抄录在下, 可复跑。

---

## 0. 结论速览

**五条声称全部复现, 零条不复现。** 复算过程中未发现任何数字、判定词或 rc 与 evidence 不符。

| # | 被审声称 | 来源 evidence | 判定 | 详见 |
|---|---|---|---|---|
| 1 | Task 6 冻结基线 (三遍 fatal 9 / legacy 179 / 254 全稳) | `u6_task6_baseline_freeze.md` | **复现** | §1 |
| 2 | Task 10 全闸 (fatal 8×3, 条款 2/3/4/7, widen 差分 2 题, cdisc_sig 0 fire) | `u6_task10_gate.md` | **复现** | §2 |
| 3 | Task 11 spot-check (cost/gain 2.08pt, I1 0.9792, E4 union 3, n_compared 45) | `u6_task11_spotcheck.md` | **复现** | §3 |
| 4 | Task 9 标定终值 (legacy 179→179 / dev 12→12 / widen 0 / detect 9,104) | `u6_task9_calibration.md` | **复现** | §4 |
| 5 | 测试计数链终值 1654 passed / 0 failed | 任务书 | **复现** | §6 |

findings 汇总见 §7: **F-1 HIGH (流程) · F-2 / F-3 MED (仪器结构盲点) · F-4 ~ F-7 LOW (文本精确度)**。
⚠ 声称 4 / 5 的执行时序与 controller 并发隔离协调令的关系 (含哪一条需要补跑), 见 **§5-1**。
**无一条 finding 推翻任何被审数字或判定** —— F-1 讲的是抽检自身读数的出处纪律,
F-2/F-3 讲的是「这次没出错, 但没有东西拦着它出错」。

---

## 1. 声称 1 — Task 6 冻结基线 (**复现**)

### 1-1 抽检写法

脚本 `recompute_c1.py` (scratchpad)。核心判据按 spec 语义自写, 逐字如下:

```python
for r in det:                      # det = json['detail'], 不碰 question 字段
    g, p, grp = r["gold"], r["pred"], r["group"]
    per_group_n[grp] += 1
    if p == g:
        per_group_exact[grp] += 1
    elif p != "both":              # 错的单库 or 缺失 ⇒ 该题 recall 归零 ⇒ fatal
        per_group_fatal[grp] += 1
        if grp != "final":         # fatal 口径 = 全集减 final (条款 5)
            fatal_ids.append(r["id"])
```

比率用 `Fraction(exact, n)` 精确表示, 与原实现的 `round(acc, 4)` 是两条路径。

```
$ ./.venv/bin/python <scratchpad>/recompute_c1.py
$ echo "rc=$?"   →  rc=0
```

### 1-2 逐项复算结果

| 项 | 声称 | 抽检独立重算 | 判定 |
|---|---|---|---|
| n_gold | 254 | 254 / 254 / 254 | ✓ |
| fatal 口径 `n_scored_excl_final` | 250 | 250 / 250 / 250 | ✓ |
| `fatal_excl_final` | 9 | 9 / 9 / 9 | ✓ |
| `legacy_exact` | 179/181 | 179 / 179 / 179 | ✓ |
| 三遍稳定 | 254/254 | 254 个 id, 漂移 0 条 | ✓ |
| 口径算术 | 254 − 4 = 250 | 254 − final(4) = 250 | ✓ |

fatal id 名单三遍逐字相同, 且与声称逐字相同:

```
['u3_amb_01','u3_amb_02','u3_amb_03','u3_amb_04','u3_amb_05',
 'u3_dist_07','u3_dist_10','u3_dist_11','u3_doc_02']
```

分组表 (抽检重算, run1; 三遍逐格相同 —— 抽检独立比对 `n/exact/fatal` 三元组全等):

| group | n | exact | acc (Fraction) | acc (小数) | fatal |
|---|---|---|---|---|---|
| legacy | 181 | 179 | 179/181 | 0.9890 | 0 |
| u1_doc | 27 | 27 | 1 | 1.0000 | 0 |
| final | 4 | 0 | 0 | 0.0000 | 4 (不计入) |
| dev | 12 | 12 | 1 | 1.0000 | 0 |
| heldout | 12 | 11 | 11/12 | 0.9167 | 1 |
| distractor_cdisc | 12 | 7 | 7/12 | 0.5833 | 3 |
| ambiguous_both | 6 | 1 | 1/6 | 0.1667 | 5 |

Fraction 路径与原实现的 `round(acc,4)` 读数在这 7 组上无差异 (0.9890 / 0.9167 / 0.5833 /
0.1667 均为四舍五入后同值), 即该 evidence 未受浮点表示影响。

fatal 9 条的迁移方向 (抽检独立统计, 非照抄 evidence §3-1):

```
('both','study'): 5    ('cdisc','study'): 3    ('study','cdisc'): 1    合计 9
```

与 evidence §3-1 的构成表逐格一致。附带观测 (evidence 未列, 抽检补记):
同一批里另有 **4 条非 fatal 误判** (`pred == 'both'` 而 gold 非 both):
`('cdisc','both')` 3 条 + `('study','both')` 1 条 —— 这解释了为何
`distractor_cdisc` 组 exact 7/12 但 fatal 只有 3 (差的 2 条落在 both, 按判据不致命),
`heldout` 组 exact 11/12 而 fatal 1 (该组差的 1 条恰好是致命型)。

### 1-3 gold 溯源核验 (抽检自加, 超出任务书要求)

run json 的 `detail` 自带 `gold`/`group`, 若只在 json 内自洽比对, 无法排除
「gold 被跑批脚本写歪」。抽检因此**绕开 `load_gold()`**, 用 `yaml.safe_load` 直接读六份
来源, 按 spec §5.2 的分工规则 (CDISC 全集→legacy/cdisc; study v1_1 去 `out_of_scope` 后
加 `st_` 前缀→legacy/study; ja 补充→legacy; docs 题集→FINAL_IDS 内为 final 其余 u1_doc,
gold 恒 study; routing_gold_docs→自带 gold+group; v2 题集只取 `st01_v2_q07`→final)
重建 254 条, 再与 run json 的 `detail` 对比:

```
reconstructed n = 254
group sizes = {'legacy':181,'u1_doc':27,'final':4,'dev':12,'heldout':12,
               'distractor_cdisc':12,'ambiguous_both':6}
id 集合相等: True     gold/group 不一致条数: 0     重复 id: 0
```

⇒ run json 里的判库与六份 yml 源**逐题一致**, 组量与冻结声明的 `EXPECTED_GROUP_SIZES`
逐格相同。基线不是自说自话。

### 1-4 冻结基线的旁证

- `meta.generated_at` 三值互不相同 (02:34:09.014111 / 02:36:59.503346 / 02:39:47.132689,
  UTC), 满足「批内不得重复」; `git_rev` 三遍均为 `...-499-g1fe5cda`, **无 `-dirty` 后缀**
  ⇒ 冻结声明「凭 sha 可复现」成立。
- `summary.passed` 三遍均 false; 抽检按判据 (fatal==0 且 legacy≥178) 独立算得 false, 一致。
- 条款 5 的 final 组三遍预测均 `cdisc`×4, gold 均 `study` ⇒ exact 0/4, 与声称一致。
- `u3_amb_06` 三遍 `(gold, pred)` 均 `('study','study')`; gold yml 里该题现值确为 `study`,
  同组另五题仍为 `both` ⇒ evidence §3-2 的「fatal 10→9 全部来自 gold 复核」归因成立
  (抽检只能验证**数据现状与该归因自洽**, 无法回溯当时是否另有行为变化 —— 见 §7 末「非 finding」)。

**判定: 声称 1 全部复现。**

---

## 2. 声称 2 — Task 10 全闸 (**复现**)

### 2-1 抽检写法 (与被审工具的关键差异)

被审工具 `eval/u6_gate_verdict.py` 的条款 1/2/3/4/7 **全部读 run json 的 `summary` /
`summary.by_group`**, 不重算 `detail`。抽检脚本 `recompute_c2.py` 反过来: **一切读数
从 254 条 `detail` 行现算**, 再与 `summary` 及 `u6_gate.json` 三方对撞 —— 若 `summary`
被写歪, 被审工具会原样继承, 而本抽检会当场暴露。所有均值 / 百分比走 `Fraction`
(如 `Fraction(275,3)/12*100`), 不复用 `round(...,2)` 浮点路径。

```
$ ./.venv/bin/python <scratchpad>/recompute_c2.py
$ echo "rc=$?"   →  rc=0
```

### 2-2 条款逐条复算

| 条款 | 声称 | 抽检独立重算 (自 `detail`) | gate.json | 判定 |
|---|---|---|---|---|
| 1 | fatal 8/8/8, legacy 179×3, pass=false | 8 / 8 / 8, 179 / 179 / 179, pass=false | 同 | ✓ |
| 2 | dev 100% / heldout 91.67%, PASS | dev = `100` = 100.0000; heldout = `275/3` = 91.6667 → round2 **91.67**; gap `25/3` = 8.3333pt ≤ 25 ⇒ PASS | 100.0 / 91.67 | ✓ |
| 3 | dev_mean 12.0, PASS | `12` (三遍 exact 12/12/12), ≥10 ⇒ PASS | 12.0 | ✓ |
| 4 | dist fatal 3→3, exact 7→7, PASS | fatal `3`→`3` (不增), exact `7`→`7` (降 `0` ≤1) ⇒ PASS | 3.0/3.0, 7.0/7.0 | ✓ |
| 7 | u1_doc fatal 0→0, exact 27→27, PASS | fatal `0`→`0`, exact `27`→`27` (降 `0`) ⇒ PASS | 0.0/0.0, 27.0/27.0 | ✓ |
| rc | 1 | 由 1/2/3/4/7 合取算得 **1** | — | ✓ |

Fraction 精确值与 evidence 的两位小数读数在全部条款上一致; 唯一非整数是
heldout 的 `275/3` %, `round2` 后 91.67 无争议 (91.6667 距 91.67 与 91.66 不等距)。

after 三遍 fatal 名单逐字复现声称:

```
['u3_amb_01','u3_amb_02','u3_amb_03','u3_amb_04','u3_amb_05',
 'u3_dist_07','u3_dist_10','u3_dist_11']
```

`gate.json` 的 `clause1.per_run[i].fatal_ids` 与抽检自 `detail` 现算的名单**逐条相等**
(三遍均 True) ⇒ 「gate.json 的判定与 run json 原始数据一致」这条成立, 且是在比
evidence 更严的口径下成立的 (evidence 比的是 summary, 抽检比的是 detail)。

### 2-3 集合代数 (修好 / 仍在 / 新增)

抽检用集合运算独立重做 §6 的三分:

```
baseline fatal (三遍相同)      : 9
after fatal 三遍交集           : 8
after fatal 三遍并集           : 8   (交 == 并 ⇒ 无「部分遍次 fatal」)
三遍全修好 = base − after 并集 : ['u3_doc_02']
新增 fatal = after 并集 − base : []
```

⇒ 「仅 `u3_doc_02` 修复, 修好 1/9, 新增 0」复现。

### 2-4 widen 差分 (逐题, 三遍)

| 遍 | 总差异 | 单库→both | 非 widen 形状 | 逐题 |
|---|---|---|---|---|
| r1 | 2 | 2 | 0 | `st01_v2_q07` (final) cdisc→both; `u3_doc_02` (heldout) cdisc→both |
| r2 | 2 | 2 | 0 | 同 r1 |
| r3 | 2 | 2 | 0 | 同 r1 |

- **两题均为 `cdisc → both`**, 与声称一致; 组归属亦复现 (`u3_doc_02` 确属 **heldout**,
  不是 `u1_doc` —— evidence §6 的「别按题号猜组」提醒经抽检独立确认属实)。
- **`study → both` 方向 (即 `cdisc_sig`) 三遍各 0 次**, 全 254 题无一例
  ⇒ 「cdisc_sig 0 fire」复现。
- 非 widen 形状 (收窄 / 换库) 0 条 ⇒ widen-only 契约在实测上未被破坏。

旁证 (抽检自加): 全集 pred 分布 `{cdisc:162, both:9, study:83}` → `{cdisc:160, both:11,
study:83}`, 三遍逐格相同。`study` 计数**一格未动**, 与 `cdisc_sig` fire 0 次互为独立佐证
(该信号若 fire 过, `study` 必减)。evidence §7 的这行数字复现。

### 2-5 稳定性与「同一把尺子」

```
after 三遍逐题稳定: 254 个 id, 漂移 0 条 → 254/254   (gate.json clause6_unstable = [])
```

抽检另加一项 evidence 未做的核验: **after 批与 baseline 批的 gold/group 逐题相同**
(id 集合相等, gold/group 不一致 0 条) ⇒ 两批确实是同一把尺子量的, 前后对照不是
「换了判库还当成同一条曲线」。

### 2-6 出处 (provenance) 复核

| 项 | 抽检直读 |
|---|---|
| after 三份 `signal_layer` | `'on'` / `'on'` / `'on'` |
| baseline 三份 `signal_layer` | 三份均 **absent** (键不存在) |
| git_rev | after `...-508-g6b92857` ×3; baseline `...-499-g1fe5cda` ×3; 六份**均无 `-dirty`** |
| `generated_at` | after 05:08:34 / 05:11:27 / 05:14:10, 互不相同; 与 baseline 三值也无交集 |
| `n_gold` / `runs_arg` | 六份均 254 / 3 |

⇒ 「不是同一批文件被当成两批」「两批都可凭 sha 复现」复现。

### 2-7 evidence 文本自身的红线复检 (抽检自跑)

```
$ ./.venv/bin/python scripts/leakscan_evidence.py evidence/u6_task10_gate.md --min-len 12
CLEAN: 0 条 question 片段出现在目标文件 (min_len=12)     rc=0
```

四份被审 evidence 全部实跑, 均 `CLEAN` + `rc=0`, needle 集 6/6:

| 文件 | 结果 | rc |
|---|---|---|
| `u6_task6_baseline_freeze.md` | CLEAN 0 条 | 0 |
| `u6_task10_gate.md` | CLEAN 0 条 | 0 |
| `u6_task11_spotcheck.md` | CLEAN 0 条 | 0 |
| `u6_task9_calibration.md` | CLEAN 0 条 | 0 |

**判定: 声称 2 全部复现。** (相关 finding: F-1 / F-5)

---

## 3. 声称 3 — Task 11 答题侧 spot-check (**复现**)

### 3-1 抽检写法 (与 evidence §3-2 controller 自算的差异)

evidence §3-2 里 controller 已做过一次复算, 但那是**同 session 自洽复算** (该文件自己也这么写:
「不替代规则 D 的抽检方 A」)。本节是独立方的第二次, 且**程序形状不同**:

- controller 写法: 按臂建 `rows()` → `stable()` 闭包 → 逐段传字典;
- 抽检写法: 先建**一张 6 列矩阵** `id → {(臂, 遍): 分}` (48×6), 再在矩阵上**声明式**套
  各判据 (稳定 / 配对 / 支配 / 聚合), 控制流与前者无共享;
- 分值一律 `Fraction(str(judge_fact_recall))` → 全程精确十进制, 不经 float 求和;
- 不 import `eval.u6_answer_verdict` / `eval.u5_verdict` 的**任何**函数 (含 `scores_by_id` /
  `stability` / `paired_effect`), 判据按脚本 docstring 的语义自写;
- 红线加严: 抽检脚本连 `top5_sources` 的**内容都不打印** (那是 chunk / 文件标识, 可能含真名),
  只打印「六份是否逐条相同」这个布尔与长度。

```
$ ./.venv/bin/python <scratchpad>/recompute_c3.py
$ echo "rc=$?"   →  rc=0
```

### 3-2 与已落盘 `u6_spot_verdict.json` 的逐字段对撞

抽检把自算值与产物 **23 个字段**逐一比对, **mismatches = 0**:

| 字段 | 产物 | 抽检独立重算 | |
|---|---|---|---|
| `E1.confirmed_cost_pt` / ids | 2.08 / `['st01_v11_q23r']` | `25/12` = 2.083333 → round2 **2.08**; ids 同 | ✓ |
| `E1.confirmed_gain_pt` / ids | 2.08 / `['st01_v2_q07']` | `25/12` = 2.083333 → round2 **2.08**; ids 同 | ✓ |
| `E1.dominance_ids` | `[q23r, q07]` | 同 | ✓ |
| `E1.dominance_only_ids` | `[]` | `[]` (两题均同时被稳定半收下) | ✓ |
| `E1.n_all_parse_ok` | 48 | 48 (6×48 矩阵零 None) | ✓ |
| `E1.stable_half.n_compared` | 45 | **45** | ✓ |
| `E1.stable_half.caliber` | `u5_stable_only_subset` | 同 | ✓ |
| `E4.unstable_a` / `_b` | 各 2 条 | off `[q14, q18]`; on `[q19, q18]` | ✓ |
| `E4.union` / `n_union` | 3 | `[q19, q14, q18]` / **3** | ✓ |
| `E4.gate_pass` | true | 3 ≤ 9 ⇒ true | ✓ |
| `I1.same_rate` / `n` | 0.9792 / 48 | 同 (直读探针产物) | ✓ |
| `aggregate_mean_diff_pt` / n | −1.16 / 48 | `−16667/14400` = −1.157431 → round2 **−1.16** | ✓ |
| `paired_net_pt` | 0.0 | **精确 0** (非浮点残渣) | ✓ |
| `divergent_readings` | false | false | ✓ |
| `verdict_word` | `cost_reported` | `cost_reported` | ✓ |
| `verdict_suppressed_by` | `[]` | `[]` | ✓ |
| `n_scored` | 48 | 48 | ✓ |

Fraction 路径的额外信息: `paired_net` 是**精确的 0**, 不是「被 round 成 0」——
gain 与 cost 的分子都恰为 1 分, 抵消是精确的。这坐实了 evidence §10 的判定盲区论证
(`divergent_readings` 的合取项确实被一个真零而非近零关掉)。

### 3-3 两道被点名的题 (逐题三遍两臂)

| 题 | 臂 | routed ×3 | source_recall ×3 | judge ×3 | parse_ok |
|---|---|---|---|---|---|
| `st01_v2_q07` (收益) | off | cdisc / cdisc / cdisc | 0.0 / 0.0 / 0.0 | **0.0 / 0.0 / 0.0** | 全 True |
| | on | both / both / both | 1.0 / 1.0 / 1.0 | **1.0 / 1.0 / 1.0** | 全 True |
| `st01_v11_q23r` (代价) | off | study / study / study | 0.0 / 0.0 / 0.0 | **1.0 / 1.0 / 1.0** | 全 True |
| | on | study / study / study | 0.0 / 0.0 / 0.0 | **0.0 / 0.0 / 0.0** | 全 True |

- q07 的「off 判 0 三遍 → on 判满分三遍」复现; 支配关系 `max(off)=0 < min(on)=1` 成立。
- q23r 两臂 **routed 六次全 `study`** (信号层未触碰该题) 复现; `top5_sources` 六份
  **1 个去重值** ⇒ 逐条相同 (长度 5)。evidence §6 的「输入同一性」佐证层经抽检独立确认。
- 抽检另测 `top5_similarities`: 六份中**五份逐位相同**, 仅 `off r1` 有 `1.000e-04` 的偏离
  ⇒ evidence §6 的「off r1 有 ≤1e-4 浮点抖动」复现到确切量级。

### 3-4 判库差分与产物形态 (抽检自算)

```
每遍 51 行, 两臂 routed 不同的题: 1 (st01_v2_q07, cdisc→both), 三遍皆然
off 臂 routed 分布 ×3: {both:5, cdisc:1, study:45}
on  臂 routed 分布 ×3: {both:6, study:45}
routed_fallback 取值集: 两臂均 {False}; 六份合计 306 行
三遍答案逐字相同: off 0/51, on 0/51; off_r1 vs on_r1 相同 2/51
每份 n_questions=48 / n_total=51 / out_of_scope=3 / signal_layer 自证 (off×3, on×3)
judge_model 六份均 deepseek/deepseek-chat; federated/study_lookup 均 True; top_k 均 15
```

全部复现 evidence §1-1 / §1-2 / §4 的对应读数。

### 3-5 E4 「活判别」声称的独立验证

evidence §9 主张本批**本身**能区分「集合并集」与「拼接」两种实现。抽检独立算得:

```
集合并集 = 3   拼接口径 = 4   重叠题 = ['st01_v2_q18'] (两臂都不稳)
```

两数确实不同 ⇒ 该 carry-forward 的「活判别 case」成立 (若脚本是拼接实现, 产物那格会写 4,
而实际产物写 3)。

### 3-6 evidence §7 四题与 §13-2 抖动三题

四道「检索侧脆弱题」在两臂各三遍共 24 次判库中**全判 `study`**, source_recall 两臂均 1.0×3
—— 复现。逐题 judge: q19 off `1.0×3` / on `1.0,1.0,0.5`; q14 off `0.6667,1.0,1.0` / on `1.0×3`;
q15 两臂均 `0.6667×3`; q21 两臂均 `1.0×3` —— 与 §7 表逐格一致。

`top5_sources` 跨遍漂移的题, 抽检独立测得: **off 臂 1 题 (`st01_v11_q04`), on 臂 3 题
(`q04` / `st01_v2_q01` / `st01_v2_q12`)**。三题的 judge 与 source_recall 六次全 `1.0`,
即「分数未受影响」复现; 但「与臂无关」这个措辞只在 `q04` 上被本批数据支持 (见 finding F-2)。

**判定: 声称 3 全部复现。** (相关 finding: F-2)

### 3-7 evidence §10 两把尺子的支撑数字 (抽检自加)

evidence §10 用「同配置跨遍极差 > 两臂均值差」论证聚合口径本轮承载不了结论。
抽检用 `Fraction` 独立复算该论证的四个数字:

| 项 | evidence | 抽检重算 (Fraction) | 判定 |
|---|---|---|---|
| off 臂三遍 judge_avg 均值 | 0.8727 | `mean(4271/5000, 8819/10000, 8819/10000)` = 0.8727 | ✓ |
| off 臂跨遍极差 | 2.77pt | `8819/10000 − 4271/5000` = **2.77pt** | ✓ |
| on 臂三遍均值 / 极差 | 0.8611 / 2.08pt | 0.8611 / **2.08pt** | ✓ |
| 两臂均值差 | −1.16pt | −1.1567pt (summary 级) → round2 **−1.16** | ✓ |
| source_recall 两臂各自零方差 | 是 | off `0.8542`×3, on `0.875`×3, 去重后各 1 个值 | ✓ |
| source_recall 两臂差 | +2.08pt | `0.875 − 0.8542` = **+2.08pt** | ✓ |

⇒ 「跨遍极差 (2.77pt) > 两臂均值差 (1.16pt)」成立, evidence §10 的自我限定有据。

附注 (非 finding): summary 级的两臂均值差 (−1.1567pt) 与逐题聚合口径 (−1.1574pt) 在小数
第三位起分岔 —— 前者是三个已 round 到四位的 run 均值再平均, 后者是逐题三遍均值差再平均。
**两者 round2 后同为 −1.16**, evidence 引的是后者 (`aggregate_mean_diff_pt`), 口径正确。


### 3-8 输入稳定性与 mtime 交叉核验 (抽检自加)

抽检全程只读已落盘产物, 故先确认这些产物在抽检窗口内**没被动过**。
`data/study/st01/eval/runs/u6_*.json` 十五份的 mtime 全部落在抽检开始**之前**
(最晚一份 `u6_spot_verdict.json` 早于抽检起点约半小时), 无一份在抽检期间被重写
⇒ §1/§2/§3 的读数取自稳定输入。

顺带得到一个 evidence 未做的交叉核验: **路由侧产物的 mtime (本机时区) 恰等于其
`meta.generated_at` (UTC) + 9 小时**, 三份基线 (11:34:09 / 11:36:59 / 11:39:47 本机
↔ 02:34:09 / 02:36:59 / 02:39:47 UTC) 与三份 after 逐份吻合。
⇒ 两个彼此独立的时间来源 (文件系统 vs 产物自证的 `meta`) 互相印证, 「产物被事后
替换而 meta 照旧」这条路径被排除。

同一核验对答题侧六份也成立: 抽检读到的 mtime 与 `u6_task11_spotcheck.md` §1-1 表里
逐行记的 UTC 时刻**六份全部吻合** (14:57:08 / 15:13:26 / 15:29:58 / 15:59:45 /
16:16:32 / 16:33:15 本机 ↔ 表中 05:57:08 / 06:13:26 / 06:29:58 / 06:59:45 / 07:16:32 /
07:33:15 UTC)。⚠ 但这一条的证明力弱于路由侧: `run_eval` 产物**没有** `generated_at` 键
(evidence §13-2 第 4 条已自陈), 所以这里只是「evidence 记的 mtime 与今天读到的 mtime 一致」,
即产物未被重跑覆盖 —— 它**不能**证明跑批时刻本身, 出处缺口原样存在。


---

## 4. 声称 4 — Task 9 标定终值 (**复现**)

### 4-1 复跑 (独立进程, 零 LLM)

任务书允许本条用标定台 CLI 重跑 (属独立进程复现)。抽检在**当前 HEAD** `9296175`
上复跑, 命令与 evidence §1 逐字相同:

```
$ ./.venv/bin/python -m eval.u6_calibrate_signals \
      --baseline data/study/st01/eval/runs/u6_baseline_run_1.json
$ echo "rc=$?"
```

抽检实测 stdout (数字部分逐字):

```
可见集: 193 题 legacy:181 dev:12

组       n   exact(base→sim)   fatal(base→sim)   Δexact   widened
legacy   181   179 → 179           0 →  0           +0      0
dev       12    12 →  12           0 →  0           +0      0

widen fire (拓宽真的发生):
  study_sig  legacy   n=  0  []
  study_sig  dev      n=  0  []
  cdisc_sig  legacy   n=  0  []
  cdisc_sig  dev      n=  0  []
detector fire (探针命中):
  study_sig  legacy   n=  8  [st_st01_v11_{q01,q03,q08,q14,q17,q19,q20,q21}]
  study_sig  dev      n=  1  ['u3_doc_03']
  cdisc_sig  legacy   n=104
  cdisc_sig  dev      n=  0  []

a_legacy_exact_not_lower         PASS  {"base": 179, "sim": 179}
b_dev_exact_drop_le_1            PASS  {"base": 12, "sim": 12, "drop": 0}
c_both_signals_alive_detect      PASS  {"counts": {"study_sig": 9, "cdisc_sig": 104}}
accepted = True  (c 读法: detect)
rc=0
```

| 声称 | 抽检复跑 | 判定 |
|---|---|---|
| legacy 179 → 179 (Δ0) | 179 → 179, Δ`+0`, widened `0` | ✓ |
| dev 12 → 12 (drop 0) | 12 → 12, Δ`+0`, widened `0` | ✓ |
| widen 四格全 0 | 四格全 `0` | ✓ |
| detect study_sig **9** | legacy `8` + dev `1` = **9** | ✓ |
| detect cdisc_sig **104** | legacy `104` + dev `0` = **104** | ✓ |
| `accepted` / rc | `True` / `0` | ✓ |
| 可见集纪律 | 输出只含 `legacy` + `dev` 两组, 计 193 题 | ✓ |

抽检另核: `study_sig` 的 detect 名单 8 条与 evidence §3-3 **逐条相同**;
`cdisc_sig legacy` 那 104 条 evidence 压缩成计数 (已声明), 抽检实跑取到完整名单,
计数复现为 104。

⚠ 本条是**独立进程复现**, 不是异源重算 —— 它跑的是被审仪器本身。它能证的是
「同一把尺子在今天的 HEAD 上仍给同一读数」(即信号层定义自 Task 9 冻结后确未被 Task 10/11
改动), **不能**证明这把尺子的离线模拟与生产 `decide_corpus` 等价 (那由该仪器自己的
42 个单测与 `_ReplayRouter` 构造保证, 属被审对象内部, 抽检未另行复算)。

### 4-2 一处「逐字」不逐字 (finding F-4)

evidence §3-1 / §3-2 / §3-3 三段 stdout 均标注「逐字」, 但实跑该行为:

```
c_both_signals_alive_widen  ⛔ 未达标  {...}  (仅报告, 见模块 docstring 的不可满足性推证)
```

evidence 里写的是 `(仅报告)` —— 尾注被截短。抽检核过该字符串的来历:
它由**唯一**动过该文件的 commit `4e252bb` 引入, 早于 evidence 自称的取值 sha `8dcb622`,
故不是「后来改的代码」造成的漂移, 而是 evidence 誊抄时删了字。**全部数字与判定词未受影响**,
但「逐字」是本仓 evidence 纪律里的承重词, 记为 finding。

### 4-3 词表派生的独立复算 (抽检自加, 异源)

`u6_task9_calibration.md` §2 声称信号层的三张表是从**公开、进 git 的**
`knowledge_base/VARIABLE_INDEX.md` 机械派生的 (60 域码 / 200 词根 / 98 单独变量),
并给了一条自比对命令。抽检重做了这件事, 但改了两处关键做法:

1. **不 `import server.routing_signals`**。该文件正被另一方变异 (§5) —— 导入等于拿
   一个未知状态当参照物。抽检改为 `git show HEAD:sdtm-rag/server/routing_signals.py`
   取**已提交**的源码, 再用 `ast.literal_eval` 把三个常量解析出来。
2. 派生侧独立跑一遍 (只读公开 KB), 与解析出的常量做**逐元素**相等比较, 而非只比计数。

```
committed table sizes: {'_SDTM_DOMAIN_CODES': 60, '_SDTM_VAR_ROOTS': 200,
                        '_SDTM_STANDALONE_VARS': 98}
my derived sizes     : {'_SDTM_DOMAIN_CODES': 60, '_SDTM_VAR_ROOTS': 200,
                        '_SDTM_STANDALONE_VARS': 98}
  _SDTM_DOMAIN_CODES       equal=True
  _SDTM_VAR_ROOTS          equal=True
  _SDTM_STANDALONE_VARS    equal=True
```

⇒ 三张表**逐元素**等于抽检从公开源独立派生的结果, 计数 60 / 200 / 98 与 evidence §2 一致。
即「词表不是手写正则、可由公开源复算」这条声称成立, 且这次是在**不碰工作树**的前提下
对**已提交状态**验的。


---

## 5. 抽检期间的工作树状态 (方法学披露, 影响声称 5)

抽检开跑时 `git status --porcelain` 非空:

```
 M sdtm-rag/eval/u6_gate_verdict.py          ← 冻结判定脚本, 被改
?? sdtm-rag/evidence/step_u6_audit.md        ← 本报告 (抽检 A 自己的产物)
?? sdtm-rag/evidence/step_u6_audit_mutation.md  ← 另一方的变异测试报告
```

该改动内容为 (抽检只读, **未回滚, 未修改**):

```diff
-                if groups[name]["n"] != GROUP_N:
+                if groups[name]["n"] < GROUP_N:
```

即组量闸由「恒等」放松成「不小于」。文件 mtime 与抽检读取时刻相差 **27 秒**,
且同目录出现另一方的 `step_u6_audit_mutation.md` ⇒ 判定: 这是**规则 D 另一方
(变异测试) 正在同一工作树里进行中的活变异**, 不是遗留的未提交改动。

处置 (按任务书「不许改任何产物/代码; 发现不一致就记 finding, 不修」):
**原样保留, 只记账**。由此产生的方法学后果:

1. **声称 1-4 不受影响**: §1/§2/§3 全部只读已落盘 json (跑批产物早于本次抽检,
   且 `u6_gate_verdict.py` 不参与其生成); §4 的标定台**不 import** `u6_gate_verdict`
   (其 import 清单为 `run_routing_eval` / `config` / `federation` / `routing_signals`),
   实测 rc=0 与冻结值一致亦反证未受污染。
2. **声称 5 (全量 pytest) 受影响**: 全量跑批读的是**当下工作树里的代码**, 一旦窗口内
   有变异在场, 读数就归因不到某个确定的代码状态。抽检为此反复尝试取干净窗口,
   逐次记账见 §6-2。

⚠ 后续观测 (同一抽检期内, 按时间顺序): 被改的文件从 `eval/u6_gate_verdict.py` 依次换到
`server/routing_signals.py` → `server/federation.py` → `server/study_lookup.py` →
`eval/u6_calibrate_signals.py` → `eval/run_routing_eval.py`, 且**同一文件内的变异体也换过**
(`u6_gate_verdict.py` 先是 `_check_groups` 的 `!= → <`, 约十分钟后变成 `validate_inputs`
里 I-2 合取项的前半 `bdump & adump and` 被摘掉)。实测变异更换节奏约**每分钟一次**,
与全量测试 39–43 秒的时长同量级 —— 这正是干净窗口难取的原因 (finding F-1)。


### 5-1 协调令与本报告的时序 (controller 指令, 如实记录)

抽检**跑完全部五条之后**收到 controller 的并发隔离协调令:

> 抽检 B 正在同仓做变异测试, 会临时改动 server/eval 源码 (每条变异后还原)。
> 清单 1/2/3 条是纯 run json 算术, 不受影响, 先做; **第 4 条 (标定台 CLI 重跑) 与
> 第 5 条 (全量 pytest) 暂缓**, 等「B 已完成」确认后再跑 —— 否则可能撞上变异窗口拿到错数。

**这条令的判断是对的, 且与抽检独立得出的 F-1 完全同因**。但如实记账: 它到达时
第 4、5 条**已经跑完**, 抽检没有按令暂缓 —— 因为令到达时这两条已是既成事实, 不是抽检
选择无视。下面逐条交代这对结论意味着什么, 不含糊过去。

**第 4 条 (标定台) —— 读数可归因, 不需要重跑**:
抽检在该次跑批**前后各捕获一次** `git status --porcelain`, 两次完全相同:

```
 M sdtm-rag/eval/u6_gate_verdict.py          ← 当时唯一被改的已跟踪文件
?? sdtm-rag/evidence/step_u6_audit.md
?? sdtm-rag/evidence/step_u6_audit_mutation.md
```

而标定台的 import 清单是 `eval.run_routing_eval` / `server.config` / `server.federation` /
`server.routing_signals` —— **不含 `eval.u6_gate_verdict`**。
⇒ 该次跑批实际加载的每一个模块当时都处于 HEAD 状态, 窗口内唯一的变异落在一个它根本
不导入的文件上。**这不是「大概没影响」, 是「按 import 图它不可能有影响」**, 且有前后两次
树快照坐实窗口内没换过别的文件。读数 (179→179 / 12→12 / widen 0 / detect 9,104 / rc=0)
按 HEAD 代码成立。

**第 5 条 (全量 pytest) —— 建议在「B 已完成」后重跑一次取干净窗口**:
这条确实被协调令说中: 全量会加载**所有**被变异的模块, 抽检四次尝试都没能取到两端全干净
的窗口 (§6-2 / §6-3 逐次记账)。抽检给出的判定仍是「复现」, 依据是判据本身对变异不敏感
(变异被杀必出 `F`, 而每一遍都是 1654 个 `.` / 0 个 `F` / rc=0; 变异也不改变收集数),
但**出处只能写到「跑批前验过干净树」**。
⇒ 待 controller 发「B 已完成」确认后, 抽检可重跑一次补一份两端全干净的读数,
把这条的出处从「跑批前干净」升到「全程干净」。**结论预计不变, 升的是证据等级。**

**顺序建议 (给后续单元, 非本次补救)**: 协调令描述的分工 (只读方并行 / 写树方串行) 正是
F-1 的建议方向。若把它写进 plan 的 Global Constraints, 五方派出时就不必靠事后协调 ——
本次的教训恰恰是「隔离要求必须先于派出到达, 事后到达就只能记账」。

---

## 6. 声称 5 — 测试计数链终值 1654 (**复现**)

### 6-1 实跑 (全量, 干净树)

`pyproject.toml` 有 `addopts = "-ra -q"`, 命令行再给 `-q` 会叠成 `-qq` 并**吞掉汇总行**
(抽检第一次跑批就踩了这个坑, 只拿到进度点)。故本条改用不带 `-q` 的命令:

```
$ ./.venv/bin/python -m pytest -p no:warnings --tb=short -rN
1654 passed in 39.31s
```

HEAD = `9296175c460c2d20da9d8c626ec93591c928a015`, 跑批**前** `git status --porcelain`
只有两个未跟踪的 evidence 文件 (本报告 + 另一方的变异报告), **无任何已跟踪文件被改**。

抽检另做一道逐字符核对 (防「汇总行数字与实际进度点不符」): 把进度区所有非空白字符
做直方图, 结果 `{'.': 1654}` —— **1654 个点, 无一个 `F`/`E`/`s`/`x`/`X`**,
与汇总行的 `1654 passed` 逐数吻合, 且 0 failed / 0 error / 0 skipped。

### 6-2 出处纪律的实测困难 (与 §5 同源, 如实记账)

因另一方的变异测试正在同一工作树上滚动, 抽检为取到一份**两端都干净**的读数做了多次尝试:

| 尝试 | 跑批前树状态 | 跑批后树状态 | 结果 | 采信 |
|---|---|---|---|---|
| 1 | 脏 (`u6_gate_verdict.py` 被改) | 脏 (且**变异体已换了一个**) | 1654 点全绿, rc=0 | ❌ 不作主读数 (窗口内代码被换过) |
| 2 | **干净** (HEAD `9296175`) | 脏 (`server/routing_signals.py` 新变异) | **1654 passed in 39.31s**, rc=0 | ✅ **本条主读数** |
| 3 | 干净 | 脏 (`eval/run_routing_eval.py` 新变异) | 1654 passed, rc=0 | 佐证 |
| 4 | 干净 | 脏 (`eval/u6_answer_verdict.py` 新变异) | **1654 passed in 42.98s**, rc=0 | 佐证 (留档的那份) |

尝试 1 的观测顺带说明一件事: 抽检**第一次**读到的变异体 (`_check_groups` 的
`!= GROUP_N` → `< GROUP_N`) 在当时那一遍全量里**未被任何测试杀掉**。抽检不据此下
「该变异存活」的结论 —— 变异体在那一窗口内被换过, 归因不成立, 且变异测试是另一方的
lane。此处只作为「共享工作树导致读数不可归因」的实例记录 (finding F-1)。

### 6-3 为什么「1654 passed / 0 failed」这个结论不依赖那个干净窗口

抽检为求严谨, 另起一个「等到树干净 → 立刻全量 → 跑完再验一次干净」的循环, 逐次记账:

```
attempt 1: tree went dirty during run (08:23:12Z-08:23:55Z)   M eval/u6_calibrate_signals.py
attempt 2: tree went dirty during run (08:24:15Z-08:24:58Z)   M eval/run_routing_eval.py
attempt 3: tree went dirty during run (08:28:09Z-08:28:53Z)   M eval/u6_answer_verdict.py
```

(该循环每次覆写同一份 stdout 文件, 故只有**最后一次**留档: `1654 passed in 42.98s`, rc=0。
这是记账口径的如实说明 —— 前两次的汇总行没有留下来, 只留下「跑完了且循环判定为脏」这个事实。)

三次都在 39–44 秒的跑批窗口内被另一方的新变异切入 (变异节奏 ≈ 每分钟一次, 与跑批时长
同量级) ⇒ **两端全干净的窗口在本抽检期内未能取到**, 如实记录, 不假装取到了。

**但这不影响声称 5 的判定**, 理由是判据本身对变异不敏感:

1. **计数侧**: 变异是单行语义改动, 不改变被**收集**的测试数。抽检做过的每一遍全量
   (含脏窗口那几遍) 收集数都恰为 **1654**, 逐字符直方图核过 (§6-1)。
   唯一能改变收集数的是 collection error, 而那会以 `E` 与非零 rc 出现 —— 一次都没有。
2. **通过侧**: 若某个变异在某遍里**被杀**, 该遍必然出现 `F` 并把 rc 抬成非 0。
   抽检做过的**每一遍**都是 `1654` 个 `.`、0 个 `F`/`E`、rc=0。
   ⇒ 无论窗口内是否有变异在场, 「1654 passed / 0 failed」这个读数都成立;
   变异在场只会让这个读数**更难**成立, 不会让它假成立。
3. **旁证**: commit `9296175` 的正文写明「测试数 1650 → 1654」, 与实测终值一致 (§6-4)。

⇒ 判定 **复现**。同时如实标注其出处边界: 本条的最强读数是「跑批**前**验过干净树、
HEAD=`9296175`、`1654 passed in 39.31s`」, 而不是「全程干净树」。

### 6-4 计数链的可追溯性 (抽检自加)

抽检把任务书给的链逐站到 git 提交信息里核对, 每一站都能找到落它的 commit;
终值一站由 `9296175` 正文的「测试数 1650 → 1654」坐实, 与实跑一致。
链本身缺两站, 见 finding F-7。


---

## 7. Findings

抽检对**全部五条**声称给出「复现」。以下 findings **无一条推翻任何数字或判定**;
F-1 是流程缺陷 (关乎所有方的读数可信度), F-2/F-3 是仪器结构盲点, 其余为文本精确度问题。

### F-1 — 规则 D 五方并行共用一个工作树, 变异方与复算方互相污染 · **HIGH** (流程)

**事实**: 抽检期间 `git status` 反复非空, 且**变异体在抽检两次读取之间被换过**:
第一次读到 `eval/u6_gate_verdict.py` 的 `_check_groups` 里 `!= GROUP_N` → `< GROUP_N`;
约十分钟后同一文件的改动已变成 `validate_inputs` 里 I-2 合取项被删 (`bdump & adump and` 前半被摘掉)。
此后又先后出现 `server/routing_signals.py` / `server/federation.py` 的改动。
同目录并存另一方产物 `evidence/step_u6_audit_mutation.md` ⇒ 判定为变异测试方在同一工作树滚动作业。

**为什么是 HIGH**: 本仓 evidence 纪律的核心是「数字必须凭 sha 复现」「实测须附可复跑命令」。
共享工作树下, **任何一方**在窗口内取的实测读数都无法归因到一个确定的代码状态 ——
抽检第一次全量 pytest 就落在这种窗口里, 只能作废重跑 (§6-2)。这不是被审 evidence 的缺陷,
是五方并行的执行方式本身的缺陷; 它同样会污染变异方 (复算方若在其窗口内跑批, 变异方会读到
不属于自己变异的绿/红)。

**建议 (交 controller)**: 变异方走 `git worktree add` 隔离副本, 或五方按「只读方并行 /
写树方串行」排程; 并要求任何「实测」读数在 evidence 里同时附**跑批前后各一次**
`git status --porcelain` 快照 (本报告 §5 / §6-2 即按此格式记账)。

### F-2 — 判定脚本只读 `summary`, 从不校验 `summary` 与 `detail` 是否自洽 · **MED**

**事实**: `eval/u6_gate_verdict.py` 的条款 1/2/3/4/7 全部取自 run json 的
`summary` / `summary.by_group` (`_g()` 与 `r["summary"][...]`), 唯一读 `detail` 的地方是
条款 5/6 (只报告项)。⇒ 若某份 run json 的 `summary` 与其 `detail` 不一致 (跑批脚本写歪、
产物被手工编辑、两份文件拼接), 闸会**原样继承错误的 summary 并照常打全绿条款表**。
`validate_inputs` 查的是三遍纪律 / 组量 / 出处, 不查这层。

**本次影响 = 无**: 抽检自 `detail` 现算了六份产物的每一格, 与各自 `summary` 及
`u6_gate.json` **零处不一致** (§2-2)。故这是结构盲点, 不是已发生的错误。

**为什么仍记 MED**: 该盲点恰好落在「唯一决定单元成败的那把闸」上, 且**无任何测试拦它**;
而本单元的红线又要求 `detail` (含题面) 不进 git —— 即人工复核只能看 summary, 天然看不见这层。

**建议**: `validate_inputs` 加一道零成本离线自检 (自 `detail` 重算 `fatal_excl_final` /
`legacy_exact` / `by_group`, 与 `summary` 不符即 `SystemExit`)。抽检脚本已证明这段逻辑
不到 20 行。

### F-3 — 条款 2/3 在本批上连「有没有喂对批次」都判别不出 · **MED**

**事实**: 条款 2/3 只吃 `after` 批。抽检实测 baseline 与 after 两批的 `dev` / `heldout`
读数**逐格相同** (dev 两批均 12/12, heldout 两批均 11/12, 三遍皆然 —— 见抽检
`recompute_c2.py` 的分组前后表, 亦即 evidence §7 那张表的 dev/heldout 两行)。
⇒ 本批若把 baseline 误当 after 传给条款 2/3, 两条款的输出**一字不差**。

这与 evidence §8-1 已披露的「多数类基线 100% ⇒ 条款 2/3 零判别力」是**两件事**:
那条说的是「过闸不代表路由变好」, 这条说的是「过闸不代表量的是 after」。
两者叠加后, 条款 2/3 在本单元里能证的东西比读者直觉少得多。

**本次影响 = 无**: 抽检已核 `gate.json` 的 clause1 逐题 `fatal_ids` 与 after 批 `detail`
逐条相等, 且两批 `git_rev` / `generated_at` / `signal_layer` 三项互不相同 (§2-6),
喂错批次的可能性被出处校验独立排除。

### F-4 — `u6_task9_calibration.md` 三处标注「逐字」的 stdout 并非逐字 · **LOW**

§3-1 / §3-2 / §3-3 的 stdout 块把
`c_both_signals_alive_widen ... (仅报告, 见模块 docstring 的不可满足性推证)`
誊抄成 `... (仅报告)`。抽检查过该字符串的来历: 由**唯一**动过该文件的 commit `4e252bb`
引入, **早于** evidence 自称的取值 sha `8dcb622` ⇒ 不是代码后改造成的漂移, 是誊抄时删了字。
**全部数字与判定词不受影响**。记录理由: 「逐字」在本仓是承重词, 下一个人拿 evidence 与
新跑批做 diff 会看到不匹配。

### F-5 — `u6_task10_gate.md` §13 的题号盘点句列了文件里不存在的两个题号 · **LOW**

该句称「本文件通篇只有 ... 题号 (`u3_amb_*` / `u3_dist_*` / `u3_doc_02` / `docs_v1_q*` /
`st01_v2_q07` / `q124` / `st_st01_v11_q17`)」, 但 `q124` 与 `st_st01_v11_q17` 在该文件里
**只出现在这句盘点句自身** (抽检 grep: `q124` 全文命中 1 次 = 该行; `st_st01_v11_q17` 同)。
属从别处誊抄的残留。不影响泄漏结论 (抽检实跑 leakscan 该文件 CLEAN rc=0)。

### F-6 — `u6_task11_spotcheck.md` §13-2 第 7 条「与臂无关」过度概括 · **LOW**

原文: `st01_v11_q04` / `st01_v2_q01` / `st01_v2_q12` 三题 top5_sources 跨遍漂移,
「**与臂无关** (off 臂自身三遍也漂)」。抽检独立测得: **off 臂只有 `q04` 一题漂**,
`st01_v2_q01` 与 `st01_v2_q12` **只在 on 臂漂**。故括注只对 `q04` 成立。
「三题分数全程 judge=1.0 / src=1.0 未受影响」这半句抽检复核为**属实** (六次读数全 1.0),
结论不变, 但「与臂无关」不该写成三题的共同属性 (n=3 下也不足以断言与臂无关)。

### F-7 — 任务书复述的测试计数链缺两个中间值 · **LOW**

任务书给的链是 `1353→1362→1415→1432→1442→1495→1497→1526→1573→1586→1628→1641→1650→1654`。
抽检从 U6 期全部 commit message 里扫出的计数断言另有 **`1362→1367`**、**`1367→1415`**
与三处 **`1440 passed`** (出自 `744f84f` / `e7451a9` 与 `9e7f9de` / `bbc99dc`)。
即该链是**摘要**而非完整台账, 少了 1367 与 1440 两站。**终值 1654 不受影响**
(commit `9296175` 的正文写明「测试数 1650 → 1654」, 与抽检实跑一致)。

### 非 finding (范围说明, 不算缺陷)

- **`u3_amb_06` 归因的可验证边界**: `u6_task6_baseline_freeze.md` §3-2 把 fatal 10→9 全部
  归因于该题 gold 复核。抽检能验证的是「当前数据与该归因自洽」(yml 现值 = `study`,
  三遍 pred = `study`, 同组另五题仍 `both`, 复核与裁定记录见 `evidence/u6_amb_gold_review.md`
  §「Controller 附记」), **不能**回溯 U3 期那批 run 是否另有行为差异 —— 那批产物 gitignored,
  抽检无从 diff。这是 evidence 无法自证的固有边界, evidence 自身亦未过度声称。
- **`i1` 探针**: 抽检自 `u6_spot_probe_cards.json` 的 48 行 `rows` 重算 same_rate =
  `47/48` = 0.979167 → round4 **0.9792**, 与产物一致; 唯一重判不复现的是 **`st01_v2_q03`**
  (evidence 只说「有 1 题」, 未点名 —— 点名不违红线, 建议补上以便下游追踪)。

---

## 8. 复跑命令 (逐字)

抽检的三份复算脚本落在 session scratchpad (非仓内), 关键逻辑已在 §1-1 / §2-1 / §3-1
抄录。**不落仓的理由**: 它们要程序化读取含题面的 run json, 进仓会给下一个人一个
「照着改两行就能打印题面」的模板; 且抽检脚本一旦进仓就成了被审对象的一部分,
下一轮抽检再照它写就不再是异源。需要复跑时按下列命令重建 (逻辑已全文可见):

```
$ cd sdtm-rag
$ git rev-parse HEAD          # 须为 9296175c460c2d20da9d8c626ec93591c928a015
$ git status --porcelain      # 须只有未跟踪的 evidence 文件 (见 F-1: 并行方会弄脏树)

# 声称 4 — 标定台 (零 LLM, 确定性)
$ ./.venv/bin/python -m eval.u6_calibrate_signals \
      --baseline data/study/st01/eval/runs/u6_baseline_run_1.json
$ echo "rc=$?"                # 0

# 声称 5 — 全量测试 (注意: 命令行不要再给 -q, pyproject 已有 "-ra -q", 叠成 -qq 会吞汇总行)
$ ./.venv/bin/python -m pytest -p no:warnings --tb=short -rN | tail -2

# 声称 1/2/3 — 自 detail 现算 (逻辑见 §1-1 / §2-1 / §3-1 的代码块)
#   输入: data/study/st01/eval/runs/ 下 u6_baseline_run_{1,2,3}.json ·
#         u6_after_run_{1,2,3}.json · u6_gate.json ·
#         u6_spot_cards_{off,on}_r{1,2,3}.json · u6_spot_probe_cards.json · u6_spot_verdict.json
#   (全部 gitignored 本地件; 缺失时按各 evidence 的 §1 命令重生成 —— 答题 run 非确定,
#    重跑数字会变, 判定脚本与标定台确定性可逐位复现)

# 声称 4 旁证 — 词表派生复算 (只读公开 KB + git show HEAD, 不碰工作树; 逻辑见 §4-3)
$ git show HEAD:sdtm-rag/server/routing_signals.py   # 用 ast 解出三个常量, 不 import

# evidence 红线复检 (四份被审文件 + 本文件)
$ for f in u6_task6_baseline_freeze u6_task10_gate u6_task11_spotcheck \
           u6_task9_calibration step_u6_audit; do
    ./.venv/bin/python scripts/leakscan_evidence.py evidence/$f.md --min-len 12; echo "rc=$?"
  done
```

---

## 9. 本文件泄漏自检 (红线)

```
$ ./.venv/bin/python scripts/leakscan_evidence.py evidence/step_u6_audit.md --min-len 12
$ echo "rc=$?"
```

逐字输出见 §9-1。needle 集 **6/6 完整** (无 `--allow-missing`), 故该 CLEAN 是 rc=0 那一档,
可作红线过闸证据引用。

### 9-1 逐字输出

```
target      : evidence/step_u6_audit.md
needles     : 306 条 question (6/6 个 gold set 可读)
                eval/test_set_v3.yml: 140 条
                eval/routing_gold_ja_supplement.yml: 16 条
                data/study/st01/eval/test_set_study_v1_1.yml: 27 条
                data/study/st01/eval/test_set_study_v2.yml: 51 条
                data/study/st01/eval/test_set_docs_v1.yml: 30 条
                data/study/st01/eval/routing_gold_docs.yml: 42 条
rule        : stride=4, min_len=12, 原文匹配 (不折叠大小写)
CLEAN: 0 条 question 片段出现在目标文件 (min_len=12)
rc=0
```

### 9-2 阈值敏感性 (引用 CLEAN 必须连阈值一起写)

| min_len | 结果 | rc | 命中来源 |
|---|---|---|---|
| 8 | LEAK: 32 条 | 1 | **全部** `eval/test_set_v3.yml` (公开英文 CDISC 题集) |
| 10 | LEAK: 8 条 | 1 | 同上 |
| 12 | **CLEAN 0 条** | **0** | — |

`data/study/` 下四份 gold set (真实试验内容) 在 **min_len=8 档即 0 命中** ——
即本文件与真实试验题面无任何长度 ≥8 的公共子串。

8 / 10 档的命中是通用英文词形假阳性, 且**全部同源于一个词**: 本报告正文里的
`controller` (指本单元的 controller 角色, 出现在 §3-1 与 §7 的建议里)。
公开英文 CDISC 题集中有大量含**受控术语**这一常见词组的题面, 与 `controller`
共享 8–10 字符的词干子串 —— 与任何题面内容无关。默认阈值取 12 正是为避开这类通用词假阳性。

⚠ **抽检自己踩过一次这个坑, 如实记录**: 本报告初稿在 §9-2 里为解释这个假阳性,
把那个英文词组**逐字写了出来**, 结果 min_len=12 档当场由 CLEAN 变成
`LEAK: 25 条 (rc=1)` —— 25 条命中全是那一处引文与公开 CDISC 题集的公共子串。
处置: 把该词组改写成中文「受控术语」, 复扫恢复 rc=0 (即 §9-1 那份输出)。
教训与 `u6_task6_baseline_freeze.md` §8-1 同款: **解释泄漏时不要把被解释的串写进来**,
这个闸在 min_len=12 下不是空转。

### 9-3 补充 kana 扫描

study 侧题面为日文, 本文件正文为中文 (不含假名):

```
$ grep -c -P '[\x{3040}-\x{309F}\x{30A0}-\x{30FF}]' evidence/step_u6_audit.md
0
```

→ 0 命中。本文件通篇只有统计值、题号 (`u3_*` / `docs_v1_q*` / `st01_v2_q*` /
`st01_v11_q*` / `st_st01_v11_q*` / `ja_supp_*` / `q*` 形式的 legacy 题号)、判库取值
(`cdisc` / `study` / `both`)、组名、命令与 rc。

抽检脚本另有一层加严: 连 `top5_sources` 的**内容**都不打印 (那是 chunk / 文件标识,
可能含真实试验名), 只落「六份是否逐条相同」这个布尔与长度 (§3-3)。
