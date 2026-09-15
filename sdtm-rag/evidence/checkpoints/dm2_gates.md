# DM2 T8 — L2 零 LLM 闸 (触发扫描 + 零回归) (2026-09-15)

> 判据: `cdisc140` 必须 `0/140` (纯 CDISC 题不该整本喂). `study48` 触发数不设下限, 记 N 与
> 题号即可。检索层 (retrieval-only 逐题 source recall) 不应有任何变化: 研读包走的是新增的
> dossier 通道, 不经 `eval/run_eval.py` (它跑的是 `--structured-lookup`/`--study-lookup` 的裸
> 检索, 与 dossier 无关), 所以两集 diff 必须 `worse=[] better=[]`。
>
> `mapping8` — **预登记: 映射 8/8 → 实测 7/8 (dm08 长名前缀不识别, D1 已知限制) → 按预登记
> 判据 FAIL, 接受豁免** (裁定人: controller, 2026-09-15; 重审触发条件: D1 长名前缀识别扩展时)。
> 即: 门槛没有被改成 7/8, 是预登记的 8/8 没达到而被显式豁免 —— 事后移门柱与显式豁免是两回事,
> 后者留得住"这条闸其实没过"这个事实。dm08 (RS via 长名前缀 "Disease Response") 需手动
> `dossier: on` 兜底。

## Attempt 1 (FAIL, 已归档)

首次跑 `eval/prod_wirein/dm2_trigger_sweep.py` 时 `cdisc140` 实测 `1/140` (q29 误触),
未过 gate。归档: `evidence/failures/dm2_task8_attempt_1.md`。

根因: `_SCOPE_RE` 的英文分支 `our study|this study|our trial|this trial` 缺 `\b` 词边界,
"How do the **f<our Trial>** Design domains TA (Trial Arms), TE..." 里 "four" 词尾 "our" +
空格 + "Trial" 被跨词边匹配成 "our trial"。q29 domains 非空 (TA/TE/TV/TI 四码), scope 误命中,
两条件同时满足 → 误触发。

## Fix (attempt 2, 本次)

Controller 裁定: 给英文分支加 `\b` 词边界 (CJK 分支与 `本 ?study` 保持不加, `\b` 在 CJK
字符边界上行为不可靠)。`server/dossier_trigger.py::_SCOPE_RE`:

```python
_SCOPE_RE = re.compile(
    r"本研究|本試験|当試験|当研究|この試験|この研究|本 ?study"
    r"|\bour study\b|\bthis study\b|\bour trial\b|\bthis trial\b"
    r"|\bin (?:our|this) (?:study|trial|research)\b",
    re.IGNORECASE,
)
```

负例测试 (`scripts/tests/test_dossier_trigger.py::test_auto_quiet_without_scope`) 新增:
`"How do the four Trial Design domains TA, TE, TV and TI work together?"` (公开 CDISC 内容,
可引用原句) — 断言不触发 (`_qd_hit` 域命中但 scope 不命中 → `auto:no_match`)。

`docs/superpowers/plans/2026-09-15-study-dossier.md` Task 3 代码块与
`docs/superpowers/specs/2026-09-15-study-dossier-design.md` §4 scope-word 行同步为上述正则。

### 单元测试

```bash
cd sdtm-rag
.venv/bin/python -m pytest -p no:cacheprovider scripts/tests/test_dossier_trigger.py
```

```
..............                                                           [100%]
14 passed in 0.02s
```

**Commit 1** (先提交修复): `a00d63c` — `fix(rag): DM2 T8 范围词英文分支加 \b (q29 "four Trial" 误触); 负例测试 + spec/plan 同步`
文件: `server/dossier_trigger.py`, `scripts/tests/test_dossier_trigger.py`,
`docs/superpowers/plans/2026-09-15-study-dossier.md`, `docs/superpowers/specs/2026-09-15-study-dossier-design.md`。

## Step 2 复跑: 触发扫描

命令 (从 `sdtm-rag/`):

```bash
.venv/bin/python eval/prod_wirein/dm2_trigger_sweep.py
```

三行数字:

```
cdisc140: 0/140 fired  []
study48: 0/51 fired  []
mapping8: 7/8 fired  ['dm01', 'dm02', 'dm03', 'dm04', 'dm05', 'dm06', 'dm07']
```

- `cdisc140: 0/140` — 过闸 (attempt 1 的 q29 误触已修)。
- `mapping8: 7/8` — 缺 `dm08` (domain=RS, 长名前缀 "Disease Response" 未被 D1 长名识别表覆盖)。
  **未达预登记的 8/8, 按判据 FAIL, controller 显式豁免** (见本文件顶部判据段), 不在本 task 修
  (需手动 `dossier: on`), 不阻断单元收口。
- `study48: 0/51` (51 = 48 计分 + 3 `out_of_scope`) — 全部 51 题都未同时命中"域码非空"与
  "范围词"两个条件。Controller 裁定可接受, 记录数字即可。

## Step 2b: gold 卡 part B 穷尽闸 (终审 I2 补测, 2026-09-15)

spec §7 一直断言「研读包 part B 穷尽全部 EDC 項目」, 但这条断言此前从未被跑过 (终审 I2)。
现由同一个 sweep 脚本实测: 取 `test_set_domain_mapping_v1.yml` 全部 `expected_sources` 中
`st01__<FORM>__<ITEM>.md` 形状的 gold 卡, 逐条查 part B 是否存在同时含 ` <FORM>] ` 与
` (<ITEM>) ` 的行。

命令 (从 `sdtm-rag/`, 与触发扫描同一条):

```bash
.venv/bin/python eval/prod_wirein/dm2_trigger_sweep.py
```

```
gold_cards_in_partB: 32/32
unique: 24/24
```

32 = 8 题 × 4 张 gold 卡 (dm01-dm03 同为 DS 域, 卡有重叠 → 去重 24 张)。**32/32 过闸**:
映射题的每一张 gold 卡都确实在一览里, part B 穷尽性不是空口断言。

与之配套的运行期闸 (终审 I1): `server/main.py::maybe_build_dossier` 在构建后拿
`data/study/st01/catalog.json` 的 `items` 条数交叉核验 `n_items`, 不一致即 `RuntimeError`
拒启动 (`cards/` 是 gitignored 生成物, 漏卡本来一行报错都没有)。启动日志加 `cards_md`。

## Step 3: 零回归复跑

命令 (从 `sdtm-rag/`):

```bash
.venv/bin/python -m eval.run_eval eval/test_set_v3.yml --retrieval-only --hybrid --structured-lookup --output eval/runs/dm2_cdisc_after.json
.venv/bin/python -m eval.run_eval data/study/st01/eval/test_set_study_v2.yml --retrieval-only --hybrid --study-lookup --collection study_st01 --kb-root data/study/st01/cards --output data/study/st01/eval/runs/dm2_study_after.json
```

结果摘要 (verbatim `EVAL SUMMARY` 关键行):

```
# cdisc140
Questions: 140
Source recall (avg): 99.2%
Threshold: 85%  ->  PASS (retrieval-only)

# study48
Questions: 48
Source recall (avg): 87.5%
out_of_scope (未计分): 3
Threshold: 85%  ->  PASS (retrieval-only)
```

逐题 diff (对 DM1 收官时的 `dm1_*_after.json`, key = `summary.source_recall_avg`):

```python
import json
for name,b,a in [("cdisc140","eval/runs/dm1_cdisc_after.json","eval/runs/dm2_cdisc_after.json"),
                 ("study48","data/study/st01/eval/runs/dm1_study_after.json","data/study/st01/eval/runs/dm2_study_after.json")]:
    B={r["id"]:r for r in json.load(open(b))["results"]}; A={r["id"]:r for r in json.load(open(a))["results"]}
    key=next(k for k in next(iter(B.values())) if "recall" in k and "source" in k)
    print(name, json.load(open(b))["summary"]["source_recall_avg"], "->", json.load(open(a))["summary"]["source_recall_avg"],
          "worse:", [q for q in B if A[q][key]<B[q][key]], "better:", [q for q in B if A[q][key]>B[q][key]])
```

verbatim 输出:

```
cdisc140 0.9917 -> 0.9917 worse: [] better: []
study48 0.875 -> 0.875 worse: [] better: []
```

**检索层零回归确认: 两集 `worse=[] better=[]`, 数字逐位不变** — 研读包 (dossier) 通道未经
`eval/run_eval.py`, 触发器修复只改 `_SCOPE_RE` 的判定表达式本身, 不碰检索/embedding/排序任何一处。

## 复跑 (整体)

```bash
cd sdtm-rag
.venv/bin/python -m pytest -p no:cacheprovider scripts/tests/test_dossier_trigger.py
.venv/bin/python eval/prod_wirein/dm2_trigger_sweep.py
.venv/bin/python -m eval.run_eval eval/test_set_v3.yml --retrieval-only --hybrid --structured-lookup --output eval/runs/dm2_cdisc_after.json
.venv/bin/python -m eval.run_eval data/study/st01/eval/test_set_study_v2.yml --retrieval-only --hybrid --study-lookup --collection study_st01 --kb-root data/study/st01/cards --output data/study/st01/eval/runs/dm2_study_after.json
# 逐题 diff: 见本文件 Step 3 脚本 (path 换成 dm1_*_after.json vs dm2_*_after.json)
```

**Commit 2** (本次 task 收口): `eval/prod_wirein/dm2_trigger_sweep.py`,
`evidence/failures/dm2_task8_attempt_1.md`, `evidence/checkpoints/dm2_gates.md`,
`eval/runs/dm2_cdisc_after.json` — `feat(rag): DM2 T8 L2 闸: 140q 零触发, 映射 7/8 触发 (dm08 known limit), 检索层零回归`
