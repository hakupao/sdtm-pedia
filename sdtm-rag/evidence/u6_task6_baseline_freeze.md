# U6 Task 6 — 新基线三遍冻结 (Phase 0 收口硬闸)

> 日期: 2026-08-18
> 执行目录: `sdtm-rag/` (以下命令逐字可复跑, 全部用 `./.venv/bin/python`)
> git rev (跑批时): `v1.4-company-release-499-g1fe5cda` — 工作树**干净**, 无 `-dirty` 后缀,
> 即这批数字可凭 sha `1fe5cda` 复现。
> 性质: Phase 0 收口的**冻结基线**。Phase 1 一切对比的参照物。
> 红线: 本文件进 git, 只记统计值 / 题号 / 命令 / rc —— 零题面, 零真实试验标识符。

---

## 1. 基线三遍跑批

```
$ ./.venv/bin/python -m eval.run_routing_eval --runs 3 --out-prefix u6_baseline_run
$ echo "rc=$?"
```

完整 stdout (逐字):

```
run 1: legacy 179/181 (floor 178)  fatal_excl_final=9  fallback=0  FAIL(条款1)
         groups: legacy:179/181  u1_doc:27/27  final:0/4  dev:12/12  heldout:11/12  distractor_cdisc:7/12  ambiguous_both:1/6
         fatal ids: ['u3_amb_01', 'u3_amb_02', 'u3_amb_03', 'u3_amb_04', 'u3_amb_05', 'u3_dist_07', 'u3_dist_10', 'u3_dist_11', 'u3_doc_02']
run 2: legacy 179/181 (floor 178)  fatal_excl_final=9  fallback=0  FAIL(条款1)
         groups: legacy:179/181  u1_doc:27/27  final:0/4  dev:12/12  heldout:11/12  distractor_cdisc:7/12  ambiguous_both:1/6
         fatal ids: ['u3_amb_01', 'u3_amb_02', 'u3_amb_03', 'u3_amb_04', 'u3_amb_05', 'u3_dist_07', 'u3_dist_10', 'u3_dist_11', 'u3_doc_02']
run 3: legacy 179/181 (floor 178)  fatal_excl_final=9  fallback=0  FAIL(条款1)
         groups: legacy:179/181  u1_doc:27/27  final:0/4  dev:12/12  heldout:11/12  distractor_cdisc:7/12  ambiguous_both:1/6
         fatal ids: ['u3_amb_01', 'u3_amb_02', 'u3_amb_03', 'u3_amb_04', 'u3_amb_05', 'u3_dist_07', 'u3_dist_10', 'u3_dist_11', 'u3_doc_02']
stability: 254/254 题三遍判定一致
```

```
rc=1
```

stderr: 空。

**rc=1 是预期**, 不是跑批失败: 条款 1 要求「每遍 fatal_excl_final=0 且 legacy_exact ≥ 178」,
其中 fatal 分量未达标。这 9 条正是本单元 (判库欠账重启修法) 存在的理由。

产物 (gitignored): `data/study/st01/eval/runs/u6_baseline_run_{1,2,3}.json`

用时: 三遍合计约 8 分 30 秒 (每遍约 2 分 50 秒; 254×3 次 Bedrock light 路由调用)。
逐遍 `meta.generated_at` (UTC): run1 `02:34:09.014111` / run2 `02:36:59.503346` /
run3 `02:39:47.132689` —— 三个时间戳互不相同, 满足 `u6_gate_verdict.validate_inputs`
的「批内不得重复」校验。

---

## 2. 逐遍数字 (meta / summary 直读)

```
$ ./.venv/bin/python -c "
import json
for i in (1,2,3):
    d=json.load(open(f'data/study/st01/eval/runs/u6_baseline_run_{i}.json'))
    m,s=d['meta'],d['summary']
    print(m['run_index'], m['n_gold'], m['git_rev'], s['n_scored_excl_final'],
          s['fatal_excl_final'], s['legacy_exact'], s['legacy_floor'], s['passed'])
    print(json.dumps(s['by_group'], ensure_ascii=False))
"
```

### 2-1 顶层 (三遍)

| run | n_gold | fatal 口径 `n_scored_excl_final` | `fatal_excl_final` | `legacy_exact` | floor | `passed` |
|---|---|---|---|---|---|---|
| 1 | 254 | 250 | 9 | 179/181 | 178 | false |
| 2 | 254 | 250 | 9 | 179/181 | 178 | false |
| 3 | 254 | 250 | 9 | 179/181 | 178 | false |

fatal 口径 250 = 全集 254 − final 组 4 (spec §7 条款 5: final 组只报告不作判据)。

### 2-2 分组 exact / fatal (三遍逐格相同, 故列一张表)

| group | n | exact | exact_acc | fatal |
|---|---|---|---|---|
| legacy | 181 | 179 | 0.9890 | 0 |
| u1_doc | 27 | 27 | 1.0000 | 0 |
| final | 4 | 0 | 0.0000 | 4 (不计入判据) |
| dev | 12 | 12 | 1.0000 | 0 |
| heldout | 12 | 11 | 0.9167 | 1 |
| distractor_cdisc | 12 | 7 | 0.5833 | 3 |
| ambiguous_both | 6 | 1 | 0.1667 | 5 |

三遍完全一致 (run1 = run2 = run3 逐格相同)。

### 2-3 条款 5 组 (只报告, 不作判据) 逐遍预测

```
$ ./.venv/bin/python -c "
import json
for i in (1,2,3):
    d=json.load(open(f'data/study/st01/eval/runs/u6_baseline_run_{i}.json'))
    print(i, {x['id']:x['pred'] for x in d['detail'] if x['group']=='final'})
"
```

三遍均为: `{'docs_v1_q15': 'cdisc', 'docs_v1_q17': 'cdisc', 'docs_v1_q53': 'cdisc', 'st01_v2_q07': 'cdisc'}`
(gold 均 study ⇒ final 组 exact 0/4; 按条款 5 不进 fatal 口径。)

---

## 3. fatal 9 条的欠账构成, 及与 U3 期 fatal=10 的差异归因

### 3-1 构成

```
both  → study : 5   (u3_amb_01 .. u3_amb_05)
cdisc → study : 3   (u3_dist_07, u3_dist_10, u3_dist_11)
study → cdisc : 1   (u3_doc_02)
                --
                 9
```

### 3-2 与 U3 期基线的差异 (**不是**「与 U3 基线一致」)

U3 期 / 本单元 Task 0 预跑读到的是 **fatal = 10**, 名单里比现在多一条 `u3_amb_06`。
本次为 **fatal = 9**。这个差异**不是**路由行为变好, 也**不是**测量噪声, 而是**判库 (gold) 本身改了**:

- `u3_amb_06` 的 gold 由 `both` 改为 `study`, 依据是出题侧隔离方的独立盲判复核
  + 用户裁定 (2026-08-18), 记录在 `evidence/u6_amb_gold_review.md`
  (含 Controller 附记的裁定行)。同批复核维持 `u3_amb_01` / `u3_amb_04` 的 `both`。
- 路由器在该题上三遍仍预测 `study`。改 gold 前这是 `both→study` 的 fatal;
  改 gold 后**同一个预测**就是正确答案。实测: 三遍 `u3_amb_06` 的
  `(gold, pred)` 均为 `('study', 'study')`。
- 连带的组内读数变化: `ambiguous_both` 由 U3 期 `0/6` 变为 `1/6` —— 多出的那 1 分
  全部来自 `u3_amb_06` 的重新标注, 其余五题读数未动。

```
$ ./.venv/bin/python -c "
import json
for i in (1,2,3):
    d=json.load(open(f'data/study/st01/eval/runs/u6_baseline_run_{i}.json'))
    print(i, [(x['gold'],x['pred']) for x in d['detail'] if x['id']=='u3_amb_06'])
"
1 [('study', 'study')]
2 [('study', 'study')]
3 [('study', 'study')]
```

gold 现状复核 (只读 id / gold / group 三项, 不读题面):

```
$ ./.venv/bin/python -c "
import yaml, collections
items = yaml.safe_load(open('data/study/st01/eval/routing_gold_docs.yml',encoding='utf-8'))
print(len(items), dict(collections.Counter(q['group'] for q in items)))
print([(q['id'], q['gold']) for q in items if q['group']=='ambiguous_both'])
"
42 {'dev': 12, 'heldout': 12, 'distractor_cdisc': 12, 'ambiguous_both': 6}
[('u3_amb_01', 'both'), ('u3_amb_02', 'both'), ('u3_amb_03', 'both'), ('u3_amb_04', 'both'), ('u3_amb_05', 'both'), ('u3_amb_06', 'study')]
```

### 3-3 另一处与 U3 期的差异: 全集 253 → 254

Task 3 把 `st01_v2_q07` 收编进条款 5 的 final 组 (`FINAL_IDS` 由 3 个增至 4 个),
故全集由 253 变 254、final 组由 `0/3` 变 `0/4`、fatal 口径由 250 保持 250
(253−3 = 250, 254−4 = 250 —— 分母恰好不变, 但两侧各加了一题, 引用时不要误读成「没动过」)。
稳定性分母同步由 253 变 254。

⇒ **一句话**: 本基线的 fatal=9 与 U3 期的 fatal=10 之间, 唯一的差是
`u3_amb_06` 的 gold 复核结果, 与路由器行为无关。

---

## 4. 三遍稳定性

```
stability: 254/254 题三遍判定一致
```

全集 254 题, 三遍预测逐题相同, 无一题漂移。fatal 名单三遍逐字相同 (见 §1 stdout)。

---

## 5. 判定脚本负例自检 (I-2 同内容拒收)

按 controller 裁定, 本步只做负例自检 —— 「以 Task 0 的 `routing_run_*` 作 after」那条
演示命令**取消**: 那批 run 产于 Task 1 仪器修缮之前, 没有 `meta` 键,
`validate_inputs` 会按设计拒收, 属 plan 自身的时序矛盾; 条款表演示由 Task 10 的
真实 after 免费获得, 不为演示多花 3×254 次 LLM 调用。

同一组 baseline 文件同时喂给 `--baseline` 与 `--after`, 脚本必须拒绝:

```
$ ./.venv/bin/python -m eval.u6_gate_verdict \
    --baseline data/study/st01/eval/runs/u6_baseline_run_1.json \
               data/study/st01/eval/runs/u6_baseline_run_2.json \
               data/study/st01/eval/runs/u6_baseline_run_3.json \
    --after    data/study/st01/eval/runs/u6_baseline_run_1.json \
               data/study/st01/eval/runs/u6_baseline_run_2.json \
               data/study/st01/eval/runs/u6_baseline_run_3.json
$ echo "rc=$?"
```

stdout: 空 (**一行条款表都没打** —— 拒收发生在任何判定之前)。

stderr (逐字):

```
baseline 与 after 内容相同 (含同 meta) — 疑似拷贝错文件 (审查 I-2)
```

```
rc=1
```

判定: 校验活着 ✓。这条负例证明 `validate_inputs` 的 I-2 分支
(summary 逐字相同 **且** `meta.generated_at` 集合相交 ⇒ 同一批文件被当成两批)
不是死代码。注意它是 `SystemExit` 而非返回值 —— 脚本在拿到任何条款结论之前就退出,
所以「拷贝错文件」这种情形不可能产出一张全绿的条款表。

---

## 6. 冻结声明

**冻结自此生效: 此后阈值/gold/判据一字不许改。**

冻结的三件物与其现值:

| 冻结物 | 现值 / 位置 |
|---|---|
| 阈值 | `LEGACY_EXACT_FLOOR = 178` (`eval/run_routing_eval.py`), `LEGACY_FLOOR = 178` / `C2_GAP_PT = 25.0` / `C3_DEV_MIN = 10.0` / `GROUP_N = 12` (`eval/u6_gate_verdict.py`) |
| gold | 六个 gold set 的现内容; 组量 `EXPECTED_GROUP_SIZES` = legacy 181 / u1_doc 27 / final 4 / dev 12 / heldout 12 / distractor_cdisc 12 / ambiguous_both 6; `FINAL_IDS` 4 个 |
| 判据 | `eval/u6_gate_verdict.py` 的条款 1/2/3/4/7 (条款 4/7 双列双闸), fatal 口径 = 全集减 final = 250 |

参照物: `data/study/st01/eval/runs/u6_baseline_run_{1,2,3}.json` (gitignored),
产自 sha `1fe5cda`, 干净工作树。Phase 1 的一切 after 跑批都以这三份作 `--baseline`。

---

## 7. 观测 vs 派出前预期

| 项 | 预期 (ledger 登记) | 实测 (三遍) | 判定 |
|---|---|---|---|
| fatal_excl_final | ≈ 9 | 9 / 9 / 9 | ✓ |
| fatal ids | amb_01..05 + dist_07/10/11 + doc_02 | 逐字相同 | ✓ |
| legacy_exact | ≈ 179/181 | 179 / 179 / 179 | ✓ |
| 全集 | 254 | 254 | ✓ |
| fatal 口径 | 250 | 250 | ✓ |
| final 组 | 4 题 (含 st01_v2_q07) | n=4, exact 0/4 | ✓ |
| 三遍稳定 | (未预登记具体数) | 254/254 | 全稳 |
| rc | 1 (欠账未修) | 1 | ✓ |
| 负例自检 | 须拒收 | rc=1 + I-2 拒收消息 | ✓ |

无一项偏离预期, 无需触发「如实记录偏差」条款。

---

## 8. 本文件泄漏自检

```
$ ./.venv/bin/python scripts/leakscan_evidence.py evidence/u6_task6_baseline_freeze.md --min-len 12
$ echo "rc=$?"
```

```
target      : evidence/u6_task6_baseline_freeze.md
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

needle 集 **6/6 完整** (无 `--allow-missing`), 故这个 CLEAN 是 rc=0 那一档,
可作红线过闸证据引用。

### 8-1 一次真实的假阳性及其处置 (如实记录, 不是事后美化)

本文件**初稿**在 min_len=12 下扫出 `LEAK: 1 条 (rc=1)`。命中片段是一个 12 字符的
**通用英文词片段**, 来源是初稿 §3-2 里那条复核命令自己写的 Python import 行,
与 `eval/test_set_v3.yml` (CDISC 侧英文题面) 共享的常见单词 —— **不是** study 侧题面泄漏
(study 侧题面为日文, 见下面的 kana 扫描 0 命中)。

处置: 把该复核命令改写成等价的另一种 import 写法 (`import yaml, collections` +
`collections.Counter`), **并重新实跑该命令取真实输出**回填 §3-2, 而不是只改文字。
改写后复扫 rc=0 (即上面那份输出)。

记录这一段的理由: 「扫描器报了一次又变绿」如果不写下来, 下一个人会以为本文件一次就干净,
从而低估这个闸的实际作用; 而这次命中恰好证明它在 min_len=12 下**不是空转**。

### 8-2 阈值敏感性 (引用 CLEAN 必须连阈值一起写)

```
$ for n in 8 10 12; do ./.venv/bin/python scripts/leakscan_evidence.py \
      evidence/u6_task6_baseline_freeze.md --min-len $n; echo "rc=$?"; done
```

| min_len | 结果 | rc |
|---|---|---|
| 8 | LEAK: 26 条 | 1 |
| 10 | LEAK: 7 条 | 1 |
| 12 | CLEAN: 0 条 | 0 |

(三档读数均在本文件**定稿内容**上测得。注意 8/10 档的计数对本文件自身正文长度敏感 ——
本节文字本身也含通用英文词, 初稿时 8 档读数为 24; 12 档恒为 0, 与正文增删无关。)

8 / 10 档的命中**全部**来自 `eval/test_set_v3.yml` 一侧, 是本文件正文与命令里的通用英文词
(受控术语类名词、`summary` 这类字段名、上面那条 import 行的模块名) 与 CDISC 英文题面
共享的短子串, 逐条可判读为非题面泄漏。默认阈值取 12 即为避开这类通用词假阳性。

### 8-3 补充 kana 扫描

study 侧题面为日文, 本文件正文为中文 (不含假名):

```
$ grep -nP '[\x{3040}-\x{309F}\x{30A0}-\x{30FF}]' evidence/u6_task6_baseline_freeze.md
```

→ 无输出 (0 命中)。

本文件通篇只有统计值、题号 (`u3_*` / `docs_v1_q*` / `st01_v2_q07`)、命令与 rc。
