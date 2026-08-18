# U6 Task 10 — 全闸三遍判定 (七条款; 结果预登记)

> 日期: 2026-08-18
> 执行目录: `sdtm-rag/` (以下命令逐字可复跑, 全部用 `./.venv/bin/python`)
> git rev (after 批跑批时): `v1.4-company-release-508-g6b92857` — 工作树**干净**, 无 `-dirty` 后缀,
> 即这批数字可凭 sha `6b92857` 复现。
> 参照物 (baseline): Task 6 冻结基线, 产自 sha `1fe5cda`, 同样干净工作树。
> 性质: 本单元的**决定性闸**。结果先于跑批预登记 (plan Global Constraints, 2026-08-17)。
> 红线: 本文件进 git, 只记统计值 / 题号 / 判库取值 (`cdisc` / `study` / `both`) / 命令 / rc
> —— 零题面, 零真实试验标识符。

---

## 0. 一句话结论

**`rc=1`, 条款 1 触发, 单元按预登记转 FAIL 形态。** 条款 2/3/4/7 全 PASS —— 即
**信号层零害, 但没有修掉欠账**: 9 条 fatal 只修掉 1 条 (`u3_doc_02`), 余 8 条三遍原样仍在。

| 条款 | 判定 | 关键数字 |
|---|---|---|
| 1 (主闸: 每遍 fatal=0 且 legacy exact ≥178) | ⛔ **触发** | fatal 8 / 8 / 8 (要求 0); legacy 179 / 179 / 179 (floor 178, 达标) |
| 2 (held-out 与 dev 差 ≤25pt) | ✅ PASS | dev 100.0% / heldout 91.67% (差 8.33pt) |
| 3 (dev exact ≥10/12) | ✅ PASS | dev_mean 12.0 |
| 4 (distractor_cdisc 双列双闸) | ✅ PASS | fatal 3.0→3.0 (不增); exact 7.0→7.0 (降 0 ≤1) |
| 5 (final 组只报告, 不作判据) | (只报告) | 见 §4 |
| 6 (三遍稳定性, 只报告不进 rc) | (只报告) | `clause6_unstable: []` —— 254/254 全稳 |
| 7 (u1_doc 双列双闸) | ✅ PASS | fatal 0.0→0.0 (不增); exact 27.0→27.0 (降 0 ≤1) |

`rc=1` 仅由条款 1 决定 (rc 取 1/2/3/4/7 的合取)。判定脚本**正常退出**并打全条款表,
不是崩溃 —— 崩溃与 `rc=1` 是两回事, 后者是判据说话。

---

## 1. after 三遍跑批

```
$ ./.venv/bin/python -m eval.run_routing_eval --runs 3 --out-prefix u6_after_run --signal-layer on
```

完整 stdout (逐字):

```
run 1: legacy 179/181 (floor 178)  fatal_excl_final=8  fallback=0  FAIL(条款1)
         groups: legacy:179/181  u1_doc:27/27  final:0/4  dev:12/12  heldout:11/12  distractor_cdisc:7/12  ambiguous_both:1/6
         fatal ids: ['u3_amb_01', 'u3_amb_02', 'u3_amb_03', 'u3_amb_04', 'u3_amb_05', 'u3_dist_07', 'u3_dist_10', 'u3_dist_11']
run 2: legacy 179/181 (floor 178)  fatal_excl_final=8  fallback=0  FAIL(条款1)
         groups: legacy:179/181  u1_doc:27/27  final:0/4  dev:12/12  heldout:11/12  distractor_cdisc:7/12  ambiguous_both:1/6
         fatal ids: ['u3_amb_01', 'u3_amb_02', 'u3_amb_03', 'u3_amb_04', 'u3_amb_05', 'u3_dist_07', 'u3_dist_10', 'u3_dist_11']
run 3: legacy 179/181 (floor 178)  fatal_excl_final=8  fallback=0  FAIL(条款1)
         groups: legacy:179/181  u1_doc:27/27  final:0/4  dev:12/12  heldout:11/12  distractor_cdisc:7/12  ambiguous_both:1/6
         fatal ids: ['u3_amb_01', 'u3_amb_02', 'u3_amb_03', 'u3_amb_04', 'u3_amb_05', 'u3_dist_07', 'u3_dist_10', 'u3_dist_11']
stability: 254/254 题三遍判定一致
```

stderr: 空。产物 (gitignored): `data/study/st01/eval/runs/u6_after_run_{1,2,3}.json`。

用时: 三遍合计约 9 分 (每遍约 2 分 50 秒; 254×3 次 Bedrock light 路由调用)。`fallback=0` 三遍
—— 无一题走判库兜底, 故本批 `both` 全部是判库或信号层的**主动**结果, 不含兜底打空。

⚠ **本条命令的 rc 未捕获** (如实记账): 跑批时用 `... | tee ...; echo "EXIT_RC=${PIPESTATUS[0]}"`
包裹, 而 zsh 的管道状态数组是 `$pipestatus` (1-based), `${PIPESTATUS[0]}` 在 zsh 下取空,
故回执里 `EXIT_RC=` 是空串, **不是 0**。三行 `FAIL(条款1)` 已逐字在上, 但"这条命令的 rc"
本文件不作断言。**这不影响判定**: 本单元的判据 rc 出自 `u6_gate_verdict` (§3), 不是这条跑批命令。

---

## 2. 出处核验 (provenance; 只读 meta 键, 不读 detail 行)

`u6_gate_verdict` 的 `validate_inputs` **不检查** `meta.signal_layer` (Task 7 结转 ③),
故这一格由本 task 手工核验:

```
$ ./.venv/bin/python -c "
import json
for i in (1,2,3):
    m=json.load(open(f'data/study/st01/eval/runs/u6_after_run_{i}.json'))['meta']
    print(f'  r{i}:', json.dumps(m, ensure_ascii=False))
for i in (1,2,3):
    m=json.load(open(f'data/study/st01/eval/runs/u6_baseline_run_{i}.json'))['meta']
    print(f'  r{i}: signal_layer=', repr(m.get('signal_layer','<absent>')), '| git_rev=', m['git_rev'], '| generated_at=', m['generated_at'])
"
```

after 批 (逐字):

```
  r1: {"generated_at": "2026-08-18T05:08:34.376613+00:00", "git_rev": "v1.4-company-release-508-g6b92857", "runs_arg": 3, "run_index": 1, "n_gold": 254, "out_prefix": "u6_after_run", "signal_layer": "on"}
  r2: {"generated_at": "2026-08-18T05:11:27.408475+00:00", "git_rev": "v1.4-company-release-508-g6b92857", "runs_arg": 3, "run_index": 2, "n_gold": 254, "out_prefix": "u6_after_run", "signal_layer": "on"}
  r3: {"generated_at": "2026-08-18T05:14:10.276372+00:00", "git_rev": "v1.4-company-release-508-g6b92857", "runs_arg": 3, "run_index": 3, "n_gold": 254, "out_prefix": "u6_after_run", "signal_layer": "on"}
```

baseline 批 (逐字):

```
  r1: signal_layer= '<absent>' | git_rev= v1.4-company-release-499-g1fe5cda | generated_at= 2026-08-18T02:34:09.014111+00:00
  r2: signal_layer= '<absent>' | git_rev= v1.4-company-release-499-g1fe5cda | generated_at= 2026-08-18T02:36:59.503346+00:00
  r3: signal_layer= '<absent>' | git_rev= v1.4-company-release-499-g1fe5cda | generated_at= 2026-08-18T02:39:47.132689+00:00
```

逐条核验:

| 核验项 | 结果 |
|---|---|
| after 三份 `signal_layer` | 全为 `"on"` ⇒ 这批确实是信号层开着跑的 |
| baseline 三份 `signal_layer` | 全为 **absent** (Task 6 跑批早于该键落地) ⇒ 等价于 off, 与"基线无信号层"相符 |
| 两批 `git_rev` 尾段 sha | after `6b92857` ≠ baseline `1fe5cda` ⇒ 不是同一批文件被当成两批 |
| `-dirty` 后缀 | 两批六份**均无** ⇒ 两批都可凭 sha 复现 |
| 批内 `generated_at` | 各批三个互不相同 (after 05:08:34 / 05:11:27 / 05:14:10; baseline 02:34:09 / 02:36:59 / 02:39:47) ⇒ 三遍纪律不是同一份喂三遍 |
| `n_gold` / `runs_arg` | 六份均为 254 / 3 ⇒ 同一把尺子 |

工作树状态 (after 批跑批前后各验一次, 均干净):

```
$ git status --porcelain     # 空输出
$ git rev-parse HEAD
6b9285709b8eadd100d522adc2855ae2e9ad7695
```

`u6_gate_verdict` 自身的 `_warn_provenance` **未打印任何 ⚠ 行** —— 既无脏树告警, 也无
"两批共用 git_rev 尾段"告警, 与上表一致。

信号层定义按 Task 9 §6 冻结, 本 task **零代码改动**。旁证 (同 sha 复跑冻结件测试):

```
$ ./.venv/bin/python -m pytest scripts/tests/test_routing_signals.py -q
..........................................                               [100%]
```

42 passed, 与 Task 9 §8 记的 42 一致 ⇒ 信号层未被本 task 动过。

---

## 3. 判定 (七条款)

```
$ ./.venv/bin/python -m eval.u6_gate_verdict \
    --baseline data/study/st01/eval/runs/u6_baseline_run_1.json \
               data/study/st01/eval/runs/u6_baseline_run_2.json \
               data/study/st01/eval/runs/u6_baseline_run_3.json \
    --after    data/study/st01/eval/runs/u6_after_run_1.json \
               data/study/st01/eval/runs/u6_after_run_2.json \
               data/study/st01/eval/runs/u6_after_run_3.json \
    --output   data/study/st01/eval/runs/u6_gate.json
$ echo "rc=$?"
```

完整 stdout (逐字):

```
clause1 ⛔ 触发 {}
  r1: fatal=8  legacy=179 (floor 178)  fatal_ids=['u3_amb_01', 'u3_amb_02', 'u3_amb_03', 'u3_amb_04', 'u3_amb_05', 'u3_dist_07', 'u3_dist_10', 'u3_dist_11']
  r2: fatal=8  legacy=179 (floor 178)  fatal_ids=['u3_amb_01', 'u3_amb_02', 'u3_amb_03', 'u3_amb_04', 'u3_amb_05', 'u3_dist_07', 'u3_dist_10', 'u3_dist_11']
  r3: fatal=8  legacy=179 (floor 178)  fatal_ids=['u3_amb_01', 'u3_amb_02', 'u3_amb_03', 'u3_amb_04', 'u3_amb_05', 'u3_dist_07', 'u3_dist_10', 'u3_dist_11']
clause2 PASS {"dev_pct": 100.0, "heldout_pct": 91.67, "majority_note": "dev/heldout 多数类基线 100%, 不得单独引用 (U3 §7.1)"}
clause3 PASS {"dev_mean": 12.0}
clause4 PASS {"group": "distractor_cdisc", "fatal": {"base": 3.0, "after": 3.0}, "exact": {"base": 7.0, "after": 7.0}, "note": "widen-only 机制下 fatal 半由构造保证, 判别力在 exact 半 (spec §4.2)"}
clause7 PASS {"group": "u1_doc", "fatal": {"base": 0.0, "after": 0.0}, "exact": {"base": 27.0, "after": 27.0}, "note": "widen-only 机制下 fatal 半由构造保证, 判别力在 exact 半 (spec §4.2)"}
clause5 (只报告): [{'docs_v1_q15': 'cdisc', 'docs_v1_q17': 'cdisc', 'docs_v1_q53': 'cdisc', 'st01_v2_q07': 'both'}, {'docs_v1_q15': 'cdisc', 'docs_v1_q17': 'cdisc', 'docs_v1_q53': 'cdisc', 'st01_v2_q07': 'both'}, {'docs_v1_q15': 'cdisc', 'docs_v1_q17': 'cdisc', 'docs_v1_q53': 'cdisc', 'st01_v2_q07': 'both'}]
clause6 unstable: []
rc=1
```

```
rc=1
```

产物: `data/study/st01/eval/runs/u6_gate.json` (gitignored, 与 run json 同在 `data/study/` 下)。

### 3-1 条款 4 / 7 的双列 (两列都列, 缺一不可)

| 条款 | 组 | n | fatal base → after | exact base → after | 闸 | 判定 |
|---|---|---|---|---|---|---|
| 4 | `distractor_cdisc` | 12 | 3.0 → 3.0 | 7.0 → 7.0 | fatal 不增 AND exact 降 ≤1 | ✅ PASS |
| 7 | `u1_doc` | 27 | 0.0 → 0.0 | 27.0 → 27.0 | fatal 不增 AND exact 降 ≤1 | ✅ PASS |

(数字为三遍均值; 因三遍逐题全稳, 均值等于每一遍的值。)

---

## 4. 条款 5 (final 组, 只报告不作判据)

三遍逐字相同:

| id | gold | baseline pred | after pred | 变化 |
|---|---|---|---|---|
| `docs_v1_q15` | study | cdisc | cdisc | — |
| `docs_v1_q17` | study | cdisc | cdisc | — |
| `docs_v1_q53` | study | cdisc | cdisc | — |
| `st01_v2_q07` | study | cdisc | **both** | 信号层拓宽 |

final 组 fatal 由 4 降到 3 (§6 表), 唯一的差是 `st01_v2_q07` 被拓宽后不再算 fatal
(`score_run`: pred 为 `both` 时非 exact 也非 fatal)。**该组不进 rc, 不得用来支持任何过闸结论。**

spec §5.4 的顶层指标 (auto 相对强制 study 的 docs 侧 `source_recall` 差, −10pt → 0)
是**答题侧**读数, 本 task 未测 —— 按 plan 自查表并入 Task 11 Step 3 判读。本文件只提供
其动机题 (`q15/q17/q53/q07`) 的判库读数, 即上表。

---

## 5. widen fire 统计 (逐题 pred 差分; 零题面)

### 5-1 口径说明 (为什么用 pred 差分)

Task 9 §7-2 预期"由 Task 10 after 批的逐题 `widened_by` 字段回答"。**实际 run json 的
`detail` 行没有这个字段** —— `run_routing_eval` 写的 detail 键为 `id / group / gold / pred / question`
(`decide_corpus` 第三个返回值 `widened_by` 在 eval 侧被丢弃, 只有生产 `retrieve` 留观测字段)。
故 widen 计数改由**基线↔after 的逐题 pred 差分**得出, 并如实标注其口径边界:

- widen-only 契约下信号层只产生 单库 → `both` 一种形状, 所以"base ∈ {cdisc, study} 且 after = `both`"
  是信号层 fire 的**必要形状**;
- 但 pred 差分**不能在原理上排除**"判库自身漂移恰好产生同一形状"。本批两侧各自
  254/254 三遍全稳 (§5-2), 漂移的可能性极低, 但这是**观测**而非构造保证。
- 反向漏计: 若某题判库本来就判 `both`, 信号层按契约沉默 (`both` 已最宽), 这类"信号想 fire
  但无处可 fire"不在计数内 —— 本口径量的是**改判**, 不是探针命中 (即 Task 9 §4 的 `widen` 读法,
  非 `detect` 读法)。

命令 (脚本只搬 id / group / gold / pred / 数字, 不打印 `question`):

```
$ ./.venv/bin/python - <<'PY'   # 全文见本节各表的产出; 核心为逐题 pred 比对
import json
RUNS="data/study/st01/eval/runs"
load=lambda p:[json.load(open(f"{RUNS}/{p}_run_{i}.json",encoding="utf-8")) for i in (1,2,3)]
base,after=load("u6_baseline"),load("u6_after")
preds=lambda rs:[{d["id"]:d["pred"] for d in r["detail"]} for r in rs]
meta={d["id"]:d["group"] for d in base[0]["detail"]}
bp,ap=preds(base),preds(after)
for i in range(3):
    diffs=[(k,bp[i][k],ap[i][k]) for k in bp[i] if bp[i][k]!=ap[i].get(k)]
    widen=[d for d in diffs if d[1] in ("cdisc","study") and d[2]=="both"]
    print(f"r{i+1}: 差异 {len(diffs)} 题 (widen {len(widen)}; 非 widen {len(diffs)-len(widen)})")
PY
```

### 5-2 三遍稳定性 (两批)

```
baseline: 254/254 题三遍一致; unstable=[]
after   : 254/254 题三遍一致; unstable=[]
```

与判定脚本的 `clause6 unstable: []` 一致 (两处独立算法同结论)。

### 5-3 差异总量 (逐遍配对 r_i vs r_i)

```
r1: 差异 2 题 (widen 单库→both 2; 非 widen 0)
r2: 差异 2 题 (widen 单库→both 2; 非 widen 0)
r3: 差异 2 题 (widen 单库→both 2; 非 widen 0)
```

**非 widen 差异 0 条** —— 全部改判都符合 widen-only 形状, 没有出现收窄或换库。

### 5-4 按组的 fire 计数

| group | n | r1 | r2 | r3 | 三遍恒定 fire | 题号 | 方向 |
|---|---|---|---|---|---|---|---|
| legacy | 181 | 0 | 0 | 0 | 0 | — | — |
| u1_doc | 27 | 0 | 0 | 0 | 0 | — | — |
| dev | 12 | 0 | 0 | 0 | 0 | — | — |
| heldout | 12 | 1 | 1 | 1 | 1 | `u3_doc_02` | cdisc→both |
| distractor_cdisc | 12 | 0 | 0 | 0 | 0 | — | — |
| ambiguous_both | 6 | 0 | 0 | 0 | 0 | — | — |
| final | 4 | 1 | 1 | 1 | 1 | `st01_v2_q07` | cdisc→both |
| **TOTAL** | **254** | **2** | **2** | **2** | **2** | | |

### 5-5 两个信号的真实活性 (Task 9 §7-2 留给本 task 的问题, 现在有答案)

| 信号 | 方向 | 本批 widen fire 次数 | 读数 |
|---|---|---|---|
| `study_sig` | cdisc → both | **2** (每遍) | 在封存组上**确实会 fire**; Task 9 可见集上的 0 次是可见集构造所致, 不是死信号 |
| `cdisc_sig` | study → both | **0** (每遍) | 在**全部 254 题**上一次都没改判 —— 含它本该发力的 8 条欠账题 |

这条不对称正是条款 1 失守的直接原因: 余下 8 条 fatal 的 baseline pred **全是 `study`**,
要修好必须由 `cdisc_sig` 触发 study→both, 而它 fire 0 次 (§6)。

⚠ 引用限制: 上表是 **widen 读法**的计数 (改判次数)。`detect` 读法 (探针命中但未改判)
本批未测 —— run json 不落 `widened_by`, 亦不落探针命中。Task 9 §0 的 detect 数字
(study_sig 9 / cdisc_sig 104) 只在**可见集**上, 与本表不是同一批题, **两者不可相加也不可互证**。

---

## 6. baseline 9 条 fatal 的前后对照 (修好 vs 仍在)

```
baseline fatal (9): ['u3_amb_01', 'u3_amb_02', 'u3_amb_03', 'u3_amb_04', 'u3_amb_05', 'u3_dist_07', 'u3_dist_10', 'u3_dist_11', 'u3_doc_02']
after r1 fatal (8): ['u3_amb_01', 'u3_amb_02', 'u3_amb_03', 'u3_amb_04', 'u3_amb_05', 'u3_dist_07', 'u3_dist_10', 'u3_dist_11']
after r2 fatal (8): 同 r1 (逐字)
after r3 fatal (8): 同 r1 (逐字)
三遍全修好 (1): ['u3_doc_02']
三遍仍 fatal (8): ['u3_amb_01', 'u3_amb_02', 'u3_amb_03', 'u3_amb_04', 'u3_amb_05', 'u3_dist_07', 'u3_dist_10', 'u3_dist_11']
部分遍次修好 (0): []
新增 fatal (基线无) (0): []
```

**修好 1 / 9, 仍在 8 / 9, 新增 0。**

逐条 (组 / gold / baseline pred / after 三遍 pred):

| id | group | gold | base pred | after pred ×3 | 修法所需方向 | 结果 |
|---|---|---|---|---|---|---|
| `u3_amb_01` | ambiguous_both | both | study | study / study / study | study→both (`cdisc_sig`) | 仍 fatal |
| `u3_amb_02` | ambiguous_both | both | study | study / study / study | study→both (`cdisc_sig`) | 仍 fatal |
| `u3_amb_03` | ambiguous_both | both | study | study / study / study | study→both (`cdisc_sig`) | 仍 fatal |
| `u3_amb_04` | ambiguous_both | both | study | study / study / study | study→both (`cdisc_sig`) | 仍 fatal |
| `u3_amb_05` | ambiguous_both | both | study | study / study / study | study→both (`cdisc_sig`) | 仍 fatal |
| `u3_dist_07` | distractor_cdisc | cdisc | study | study / study / study | study→both (`cdisc_sig`) | 仍 fatal |
| `u3_dist_10` | distractor_cdisc | cdisc | study | study / study / study | study→both (`cdisc_sig`) | 仍 fatal |
| `u3_dist_11` | distractor_cdisc | cdisc | study | study / study / study | study→both (`cdisc_sig`) | 仍 fatal |
| `u3_doc_02` | **heldout** | study | cdisc | **both / both / both** | cdisc→both (`study_sig`) | ✅ 修好 |

注: `u3_doc_02` 属 **heldout** 组 (题号前缀 `u3_doc_` 与组名 `u1_doc` 不是一回事 —— 别按题号猜组)。
它被拓宽后 gold=`study` 而 pred=`both`, 故**不再 fatal, 但也不算 exact**; heldout 组 exact
因此仍是 11/12 (§7 表), fatal 由 1 降到 0。

### 6-1 为什么 8 条没修好 (机制层面, 不是猜测)

全部 8 条的 baseline pred 都是 `study`。按方向表 `WIDEN_REASON_BY_CORPUS`,
`study` 判定只接受 `cdisc_sig` 作拓宽依据; 而 `cdisc_sig` 在本批 254 题上 fire 0 次 (§5-4/5-5)。
即: 修法在这 8 条上**根本没有触发**, 不是触发了但方向/闸拦下了。

这与 Task 9 §7-3 预登记的"只窄不宽的方向性代价"吻合: R1 词表剪枝 (真子集) 与 G1 强通道收紧
(真子集) 两步为换取可见集零害, 把修法面同步收窄; 封存组上"收窄到不再命中欠账题"这个风险
当时已记账为**不可测**, 现在实测为**已发生**。

---

## 7. 各组 exact / fatal 前后 (summary 直读, 三遍均值)

```
group                n  exact_b  exact_a  fatal_b  fatal_a
legacy             181   179.00   179.00     0.00     0.00
u1_doc              27    27.00    27.00     0.00     0.00
dev                 12    12.00    12.00     0.00     0.00
heldout             12    11.00    11.00     1.00     0.00
distractor_cdisc    12     7.00     7.00     3.00     3.00
ambiguous_both       6     1.00     1.00     5.00     5.00
final                4     0.00     0.00     4.00     3.00
```

**没有任何一组的 exact 下降** (七组逐格相等), fatal 只在 heldout (1→0) 与 final (4→3) 下降。
全集 pred 分布由 `{cdisc:162, both:9, study:83}` 变为 `{cdisc:160, both:11, study:83}`
—— `study` 计数一格未动, 是 `cdisc_sig` fire 0 次的另一处独立佐证。

---

## 8. 引用纪律 (逐条, 引用本文件任何数字时必须一起写)

1. **条款 2/3 不得单独引用**: `dev` / `heldout` 两组 gold **全部是 `study`** (各 12 题),
   多数类基线 = 100%。一个恒答 `study` 的平凡判器在这两组上就是满分, 故条款 2/3 单独看
   **零判别力** (U3 §7.1 / 抽检 A-2)。本次 dev 100.0% / heldout 91.67% 的 PASS 不构成
   "路由变好"的任何证据。
2. **条款 4/7 的 fatal 半由构造保证**: 本单元机制是 widen-only, 加宽只会把错的单库判定变成
   `both`, 而 `score_run` 里 pred=`both` 永不计 fatal ⇒ **fatal 半在本机制下不可能变坏**,
   它的"不增"是构造结论不是实测结论。条款 4/7 的**判别力在 exact 半** (spec §4.2 预登记声明)。
   本次 exact 半读数为 7.0→7.0 与 27.0→27.0, 那才是这两条闸真正说了话的地方。
3. **`ambiguous_both` 组 gold 已混合**: 该组 6 题的 gold 现为 **5 条 `both` + 1 条 `study`**
   (`u3_amb_06` 经 Task 3/4 出题侧复核改判为 `study`, 见 `evidence/u6_amb_gold_review.md`)。
   故该组读数 (exact 1/6, fatal 5) **不得按"纯 both 组"解读** —— 那 1 分 exact 来自
   `u3_amb_06` 这条 gold=`study` 的题, 不是任何一条 both 题被判对。
4. **本批 `fallback=0`**: 三遍无一题走判库兜底, 故本文件的 `both` 读数不含"兜底打空"成分。
   (引用他处 `both` 数字时若来自 fallback 非 0 的批次, 该限定不成立。)

---

## 9. 已知限制 (看不见什么 / 不能证明什么)

1. **widen 计数是 pred 差分, 不是仪器直读** (§5-1): run json 无 `widened_by` 字段。
   本文件的 2 次/遍是"改判计数", 在原理上不能排除判库漂移伪装成同形状 —— 只有两批各
   254/254 全稳这一**观测**支撑, 没有构造保证。想要构造保证需要 eval 侧落 `widened_by`,
   那是代码改动, 本 task 明令零代码改动, 故留作已知限制。
2. **detect 读法本批未测**: 只知道 `cdisc_sig` 改判 0 次, **不知道**它的探针在这 254 题上
   命中过几次。"fire 0 次"因此只在 widen 读法下成立; "`cdisc_sig` 是死代码"这个更强的说法
   **本文件不支持** (Task 9 可见集上它 detect 命中 104 次, 说明它在别的题面上活着)。
3. **只测判库侧**: 本文件全部读数是 corpus 判定的对错, **不含任何答题质量读数**。
   信号层把 `u3_doc_02` / `st01_v2_q07` 拓宽成 `both` 之后答得更好还是更差, 本文件
   **不能回答** —— 那是 Task 11 (答题侧 spot-check) 的事。"fatal 少了 1 条"是判库口径的改善,
   不等于用户看到的答案变好。
4. **spec §5.4 的顶层指标未测** (§4): docs 侧 `source_recall` 差属答题侧, 并入 Task 11。
5. **三遍即全部**: 按纪律只跑三遍, 未重跑追数字。三遍逐题全稳使得"再跑一遍会不同"的
   可能性低, 但样本就是 3。
6. **8 条未修的原因是"没触发", 不是"触发了但判错"** (§6-1): 这是从方向表 + fire 计数
   推出的机制结论。至于**为什么** `cdisc_sig` 在这 8 条题面上不命中 (词表缺哪类词形),
   需要读题面才能回答, 本 task 红线禁止, 故不作诊断。

---

## 10. 预登记执行 (本 task 只做 evidence + 上报, 不代执行后果)

plan Global Constraints (2026-08-17, **先于结果**登记):

> Task 10 全闸任一条款触发 ⇒ Phase 1 代码 commit 全部 revert, Phase 0 仪器与基线存续,
> 失败归档 `evidence/failures/u6_task10_attempt_1.md` (规则 B), 上报用户;
> **不许改阈值不许删题, 没有第二轮标定后重闸** (要重启须新单元)。

条款 1 触发 ⇒ 该预登记生效。本 task 按 controller 指派**只**做两件事:

1. 本 evidence 文件落盘并单独 commit;
2. 上报 controller。

**未做**(交 controller 执行, 本 task 无授权): revert Task 7/8/9 代码 commit ·
`evidence/failures/u6_task10_attempt_1.md` 归档 · 上报用户 · 单元转 FAIL 形态收口。

**未做**(纪律禁止): 重跑追数字 · 调阈值 · 改 gold · 改信号层词表。三遍就是三遍。

---

## 11. 观测 vs 派出前预期

| 项 | 派出前预期 | 实测 | 判定 |
|---|---|---|---|
| 条款 1 fatal | 需 0 才过 | 8 / 8 / 8 | ⛔ 触发 (预登记 rc=1 分支) |
| legacy exact | ≥178 | 179 ×3 | ✓ 达标 (条款 1 的另一半) |
| 条款 4 exact 半 | 降 ≤1 | 降 0 | ✓ 优于闸 |
| 条款 7 exact 半 | 降 ≤1 | 降 0 | ✓ 优于闸 |
| `study_sig` 真实活性 | Task 9 未知 (可见集不可测) | widen 2 次/遍 (heldout 1 + final 1) | **新信息**: 活的 |
| `cdisc_sig` 真实活性 | Task 9 未知 (可见集不可测) | widen 0 次/遍 | **新信息**: 在封存组上不触发 |
| 修好的 fatal 条数 | 未预登记具体数 (条款 1 要求 9/9) | 1/9 | ⛔ 差 8 条 |
| 新增 fatal | widen-only 构造上应为 0 | 0 | ✓ 构造被实测印证 |
| 三遍稳定 | (未预登记) | 254/254 两批皆是 | 全稳 |
| 非 widen 形状的改判 | 应为 0 | 0 | ✓ |
| 判定脚本行为 | 打全条款表并返回 rc | 正常退出, rc=1 | ✓ 非崩溃 |

一处与预期不符已如实记账: 跑批命令的 rc 未捕获 (§1 的 zsh `$pipestatus` 说明), 不影响判据。

---

## 12. 复跑命令 (逐字)

```
$ cd sdtm-rag
$ git rev-parse HEAD        # 须为 6b9285709b8eadd100d522adc2855ae2e9ad7695, 且 git status 干净
$ ./.venv/bin/python -m eval.run_routing_eval --runs 3 --out-prefix u6_after_run --signal-layer on
$ ./.venv/bin/python -m eval.u6_gate_verdict \
    --baseline data/study/st01/eval/runs/u6_baseline_run_1.json \
               data/study/st01/eval/runs/u6_baseline_run_2.json \
               data/study/st01/eval/runs/u6_baseline_run_3.json \
    --after    data/study/st01/eval/runs/u6_after_run_1.json \
               data/study/st01/eval/runs/u6_after_run_2.json \
               data/study/st01/eval/runs/u6_after_run_3.json \
    --output   data/study/st01/eval/runs/u6_gate.json
$ echo "rc=$?"          # 1
```

⚠ 复跑会**覆盖** `u6_after_run_{1,2,3}.json` (同 out-prefix)。基线三份不受影响。
⚠ 第一条命令走 Bedrock, 约 9 分钟 / 762 次 light 路由调用; 判定脚本零 LLM, 秒级。

---

## 13. 本文件泄漏自检

```
$ ./.venv/bin/python scripts/leakscan_evidence.py evidence/u6_task10_gate.md --min-len 12
$ echo "rc=$?"
```

逐字输出见 §13-1。补充 kana 扫描:

```
$ grep -nP '[\x{3040}-\x{309F}\x{30A0}-\x{30FF}]' evidence/u6_task10_gate.md
```

→ 无输出 (0 命中)。本文件通篇只有统计值、题号 (`u3_amb_*` / `u3_dist_*` / `u3_doc_02` /
`docs_v1_q*` / `st01_v2_q07` / `q124` / `st_st01_v11_q17`)、判库取值、命令与 rc。

### 13-1 泄漏扫描逐字输出

```
target      : evidence/u6_task10_gate.md
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

needle 集 **6/6 完整** (无 `--allow-missing`), 故这个 CLEAN 是 rc=0 那一档, 可作红线过闸证据引用。

### 13-2 阈值敏感性 (引用 CLEAN 必须连阈值一起写)

上面的 CLEAN 是 `min_len=12` 这把尺子下的结论。更短的窗会把通用英文词组
(判库取值 / 命令片段 / 组名) 扫成假阳性 —— Task 9 §8-2 已实测过一次这种假阳性并留档。
本文件为此刻意不复述任何题面用词, 只用题号与判库取值。
