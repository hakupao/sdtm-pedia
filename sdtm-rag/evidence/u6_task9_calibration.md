# U6 Task 9 — 可见集标定 (legacy 181 + dev 12; 词表/正则)

> 日期: 2026-08-18
> 执行目录: `sdtm-rag/` (以下命令逐字可复跑, 全部 `./.venv/bin/python`)
> git rev (标定时): `v1.4-company-release-504-g4e252bb` (工作树含本轮词表改动 ⇒ 跑批时为 `-dirty`)
> 参照物: Task 6 冻结基线 `data/study/st01/eval/runs/u6_baseline_run_1.json` (gitignored)
> **零 LLM 调用** (标定是离线模拟); 红线: 本文件只记题号 / 组名 / 计数 / 命令 / rc —— 零题面。
> 可见集纪律 (spec §5.2): 全程只读 `legacy` + `dev`; held-out / distractor / ambiguous /
> u1_doc / final 五组**一次都没有被读过** (仪器在读入处就丢弃, 见 §1)。

---

## 0. 一句话结论

**BLOCKED (2 轮)**: 预登记规则 (b)(c) 达标, **(a) 不可能达标** ——
legacy 的 6 分 exact 损失**全部**来自 `study_sig` 一侧, 而该侧的判据是
`StudyLookup.resolve` (Plan B Phase 2 的既有件), **不在本 task 允许动的旋钮里**
(旋钮 = `CDISC_STRUCT_TERMS` / `_CT_CODE_RE` / `_DOMAIN_VAR_RE` 三个常量)。
本 task 能动的那半边 (cdisc 信号) 已标定到**零害**: 误触 6 题 → 0 题。

连带的硬事实: 若照现状进 Task 10, 全闸**条款 1 必不过** ——
模拟 legacy exact = 173 < `LEGACY_EXACT_FLOOR` 178, 而该阈值 Task 6 已冻结、不许下调。
即: 这次标定用零 LLM 成本, 提前买到了一个本来要烧 3×254 次调用才会撞上的失败。

处置建议 (超出本 task 旋钮, 须 controller 裁定, 见 §5): 把 study 侧信号的判据从
「`resolve` 有任何命中」收紧到「强通道命中」。该方案的可见集反事实**已实测**: widen 0 次,
(a)(b)(c) 三条全过。

---

## 1. 仪器 (`eval/u6_calibrate_signals.py`) 与 TDD 记录

先写测试 (RED) 再实现 (GREEN)。RED 证据 (逐字):

```
$ ./.venv/bin/python -m pytest scripts/tests/test_u6_calibrate_signals.py -q
...
scripts/tests/test_u6_calibrate_signals.py:22: in <module>
    from eval.u6_calibrate_signals import (
E   ModuleNotFoundError: No module named 'eval.u6_calibrate_signals'
=========================== short test summary info ============================
ERROR scripts/tests/test_u6_calibrate_signals.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
```

实现后 GREEN: `42 passed`。三件被钉死的事:

| 钉子 | 测试 | 为什么它是"错了也全绿"的形态 |
|---|---|---|
| 可见集纪律 | `visible_subset` 组集恒等断言 + `load_base_preds` 只收给定 id | 多读一组题不会让任何断言变红 |
| 零题面 | 哨兵串 `PLACEHOLDER-QUESTION-TEXT-DO-NOT-EMIT` 不得出现在 `render()` 与报告 dict | 打印题面也不会让断言变红 |
| 离线模拟 == 真跑 | 五种信号层破法 (沉默 / 双向 fire / 非白名单 / 反方向 / 抛异常) × 三种判定, 逐格与 `decide_corpus` 比对 | 自抄一份 widen 逻辑时, 白名单闸/方向闸/异常旁路会与生产不同, 而"标定按另一把尺子选词表"在数字上看不出来 |

等价性不只靠测试, 更靠构造: `simulate` 用 `_ReplayRouter` 把冻结基线 pred 喂回
**`decide_corpus` 本尊**, 没有第二份 widen 逻辑。基线 pred 非法时不兜底而是抛 ——
静默 fallback 成 `both` 在计数上与一次 widen 无法区分。

复跑:

```
$ ./.venv/bin/python -m eval.u6_calibrate_signals \
      --baseline data/study/st01/eval/runs/u6_baseline_run_1.json
$ echo "rc=$?"      # 三条规则全过为 0, 否则 1
```

---

## 2. 词表派生 (公开源, 可逐字复算)

本轮只动 `_DOMAIN_VAR_RE`。新值不是手写正则, 而是从**公开、进 git 的**
`knowledge_base/VARIABLE_INDEX.md` (1523 个变量 / 63 个域) 机械派生的三张表:

| 表 | 规则 | 条数 |
|---|---|---|
| `_SDTM_DOMAIN_CODES` | `knowledge_base/domains/` 目录名 ∪ VARIABLE_INDEX.md §2 域小节头, 取两字母者 | 60 |
| `_SDTM_VAR_ROOTS` | §2 中**以本域域码开头**的变量去掉域码后的余段 (≥3 位) | 200 |
| `_SDTM_STANDALONE_VARS` | §1/§2 全部变量里不被「域码+词根」覆盖、≥4 位、非 CT 码者 | 98 |

「归属自己域」是关键: 若按「任意两字母前缀」切, `SUBJID` 会被切成假词根 `BJID`
(SU 恰是 SU 域的域码), 于是 `AEBJID` 这类不存在的形态也会命中。

复算 (与源码逐字比对; 输出 `True` 即三张表未被手改):

```
$ ./.venv/bin/python - <<'PY'
import re
from pathlib import Path
from server.routing_signals import (_SDTM_DOMAIN_CODES, _SDTM_STANDALONE_VARS, _SDTM_VAR_ROOTS)
kb = Path("../knowledge_base")
text = (kb / "VARIABLE_INDEX.md").read_text(encoding="utf-8")
dirs = {p.name for p in (kb / "domains").iterdir() if p.is_dir()}
sec2 = text.split("## 2. Domain-Specific Variables")[1].split("## 3.")[0]
blocks = re.split(r"^### ([A-Z]{2,8}) — ", sec2, flags=re.M)[1:]
codes = sorted({c for c in dirs | set(blocks[::2]) if len(c) == 2})
roots = set()
for code, body in zip(blocks[::2], blocks[1::2], strict=True):
    vs = re.findall(r"^\| ([A-Z][A-Z0-9]{1,7}) \|", body, re.M)
    roots |= {v[len(code):] for v in vs if v.startswith(code) and len(v) - len(code) >= 3}
comp = re.compile("(?:%s)(?:%s)" % ("|".join(codes), "|".join(sorted(roots, key=len, reverse=True))))
allv = sorted(set(re.findall(r"^\| ([A-Z][A-Z0-9]{1,7}) \|", text.split("## 3.")[0], re.M)))
solo = sorted(v for v in allv if len(v) >= 4 and not comp.fullmatch(v)
              and not re.fullmatch(r"C\d{5,6}", v))
print(tuple(codes) == _SDTM_DOMAIN_CODES, tuple(sorted(roots)) == _SDTM_VAR_ROOTS,
      tuple(solo) == _SDTM_STANDALONE_VARS)
PY
True True True
```

词表纪律自检 (红线, 同 U3 §6.1):

- **零临床概念**: 三张表全部由标准变量名机械派生, 无一条是临床概念词; Task 8 的
  `test_terms_contain_no_clinical_concepts` 仍绿 (该测试看的是 `CDISC_STRUCT_TERMS`,
  **本轮未动**, 仍是 8 条)。
- **只窄不宽**: 词根 ≤6 位、单独变量 ≤8 位 ⇒ 新正则匹配的每一个 token 都是 4–8 位大写,
  即新集合 ⊆ 旧集合 (`[A-Z]{4,8}`)。故本轮改动**在任何题集上都只可能减少 fire, 不可能增加**
  —— 这条对封存组同样成立 (见 §7 已知限制)。
- 形态自检 (逐字实测): 起点版误触的 8 个形态 `SCRT / CAPOXIRI / LARS / CTCAE / IWRS /
  COVID / GRPTOX / VIII` 现在**全部不匹配**; 真变量 `AESEV / VSORRES / LBTESTCD /
  USUBJID / RFSTDTC / AEACN / EXDOSE` **全部仍匹配**。
- 正则规模 2025 字符; 单次 `search` 在 ~960 字问句上实测 0.18 ms (2000 次 0.353 s),
  对每请求一次的生产路径可忽略。

---

## 3. 轮次表 (≤5 轮; 实际用 2 轮)

| 轮 | 改动 | (a) legacy exact | (b) dev drop | (c) widen 读法 | (c) detect 读法 | widen fire (study_sig / cdisc_sig) | accepted |
|---|---|---|---|---|---|---|---|
| R0 | 起点 (Task 8 词表, `[A-Z]{4,8}`) | ⛔ 179 → **167** (−12) | PASS 0 | PASS 6/6 | PASS 16/117 | legacy 6 / legacy 6 | ✗ |
| R1 | `_DOMAIN_VAR_RE` 锚定到 KB 派生的域码+词根+单独变量 | ⛔ 179 → **173** (−6) | PASS 0 | ⛔ 6/0 | PASS 16/104 | legacy 6 / **0** | ✗ |

R0 → R1 的差: cdisc 侧误触 6 题 (`st_st01_v11_q07 / q11 / q16 / q19 / q20 / q22`) 全部消除,
legacy 回补 6 分; study 侧那 6 题 (`q19 / q43 / s01 / q91 / q107 / q123`) **逐题不变**。

**为什么止步于第 2 轮而不是跑满 5 轮**: 剩余的 6 分损失全部来自 `study_sig`,
而 `study_sig` 的判据是 `RoutingSignals._study_signal` → `StudyLookup.resolve`,
**与本 task 三个旋钮无任何数据依赖** (旋钮只进 `_cdisc_signal`)。
⇒ 任何只改这三个常量的第 3/4/5 轮, `study_sig` 的 6 次 widen 逐题恒等, legacy 恒 ≤173 < 179。
再跑三轮不是标定, 是把一个结构性结论重打三遍。R1 已是本旋钮集下的**最优点**
(cdisc 侧害 = 0, 不可能更低)。

### 3-1 R0 stdout (逐字, 起点词表 == HEAD `d3bd0e4`)

```
可见集: 193 题 legacy:181 dev:12

组       n   exact(base→sim)   fatal(base→sim)   Δexact   widened
legacy   181   179 → 167           0 →  0           -12      12
dev       12    12 →  12           0 →  0           +0      0

widen fire (拓宽真的发生):
  study_sig  legacy   n=  6  ['q19', 'q43', 's01', 'q91', 'q107', 'q123']
  study_sig  dev      n=  0  []
  cdisc_sig  legacy   n=  6  ['st_st01_v11_q07', 'st_st01_v11_q11', 'st_st01_v11_q16', 'st_st01_v11_q19', 'st_st01_v11_q20', 'st_st01_v11_q22']
  cdisc_sig  dev      n=  0  []
detector fire (探针命中):
  study_sig  legacy   n= 15  [q19, q43, s01, q91, q107, q123, st_st01_v11_{q01,q03,q08,q14,q16,q17,q19,q20,q21}]
  study_sig  dev      n=  1  ['u3_doc_03']
  cdisc_sig  legacy   n=117
  cdisc_sig  dev      n=  0  []

a_legacy_exact_not_lower         ⛔ 未达标  {"base": 179, "sim": 167}
b_dev_exact_drop_le_1            PASS  {"base": 12, "sim": 12, "drop": 0}
c_both_signals_alive_widen       PASS  {"counts": {"study_sig": 6, "cdisc_sig": 6}}  (仅报告)
c_both_signals_alive_detect      PASS  {"counts": {"study_sig": 16, "cdisc_sig": 117}}  ← 操作性读法
accepted = False  (c 读法: detect)
```

(两条 `detector fire` 行的 id 全表过长, 上面按题号族压缩/略去; 计数逐字未改,
完整清单跑一次上面的复跑命令即得 —— 全是题号, 不含题面。)

### 3-2 R1 stdout (逐字, 冻结版词表)

```
可见集: 193 题 legacy:181 dev:12

组       n   exact(base→sim)   fatal(base→sim)   Δexact   widened
legacy   181   179 → 173           0 →  0           -6      6
dev       12    12 →  12           0 →  0           +0      0

widen fire (拓宽真的发生):
  study_sig  legacy   n=  6  ['q19', 'q43', 's01', 'q91', 'q107', 'q123']
  study_sig  dev      n=  0  []
  cdisc_sig  legacy   n=  0  []
  cdisc_sig  dev      n=  0  []
detector fire (探针命中):
  study_sig  legacy   n= 15   (同 R0, 逐题相同)
  study_sig  dev      n=  1  ['u3_doc_03']
  cdisc_sig  legacy   n=104
  cdisc_sig  dev      n=  0  []

a_legacy_exact_not_lower         ⛔ 未达标  {"base": 179, "sim": 173}
b_dev_exact_drop_le_1            PASS  {"base": 12, "sim": 12, "drop": 0}
c_both_signals_alive_widen       ⛔ 未达标  {"counts": {"study_sig": 6, "cdisc_sig": 0}}  (仅报告)
c_both_signals_alive_detect      PASS  {"counts": {"study_sig": 16, "cdisc_sig": 104}}  ← 操作性读法
accepted = False  (c 读法: detect)
rc=1
```

---

## 4. 规则 (c) 的两种读法, 及 widen 读法的不可满足性

预登记条文: 「`study_sig` 与 `cdisc_sig` 各至少 fire 1 次 (无死信号)」。"fire" 有两种读法,
仪器**两种都算、都打印**, 并把操作性读法写在输出里:

- `widen` 读法 = 该信号真的把某题由单库拓宽成 `both`;
- `detect` 读法 = 该信号的探针在可见集某题上命中 (与该题判到哪库无关)。

**`widen` 读法在本可见集上与词表无关地不可满足** (推证只用 Task 6 冻结基线的聚合数字,
先于本次标定即已知, 不是看了标定数据才补的说法):

1. legacy 181 题 exact 179 且 fatal 0。按 `score_run`, 非 exact 且非 fatal ⇒ `pred == "both"`。
   故那 2 道非 exact 的 legacy 题 pred 均为 `both`; dev 12/12 全 exact。
2. ⇒ 可见集里**每一道 pred 为单库的题, 现在都恰好判对**。
3. widen-only 只做 单库→`both`, 而这些题的 gold 是单库 ⇒ 可见集上任何一次 widen 恒 −1 exact,
   不可能 +1 (能 +1 的只有 gold=`both` 且被判成单库的题, 而那种题在可见集里全是 fatal, 计数为 0)。
4. (a) ⇒ legacy 上必须 0 次 widen; (b) ⇒ dev 上至多 1 次 widen。
5. 一道题只产一个理由 (方向由判库结果定死), 故 (c) 的 widen 读法要求**至少 2 次** widen,
   且都只能落在 dev ⇒ dev 掉 2 分 > 1, 与 (b) 冲突。∎

R0 正是这条推证的实证: 该轮 (c)-widen PASS, 代价恰恰是 (a) 掉 12 分。

⇒ 操作性读法取 `detect` (它量的正是「词表被剪到永不命中」这件规则要防的事, 且不与 (a)(b)
结构性冲突)。**引用 (c) 必须连读法一起写**; 只写「(c) 达标」是无效引用。

---

## 5. 阻断诊断: study 侧那 6 次误触的通道构成 (零题面)

`StudyLookup.resolve` 三条通道: ① label 全文子串 / ②a 多 token 段交集 / ②b 单 token → OID 段 /
③ 别名 → form scope。对 6 题逐题量 (可见集内, 只打通道与计数):

| id | cards | scopes | ②b 单 token 命中 | ②a 交集 fire | ① label 命中 | 命中 token 是否本身就是 SDTM 标准 token | token 长度 |
|---|---|---|---|---|---|---|---|
| q19 | 2 | 0 | 1 | 否 | 0 | 是 | 7 |
| q43 | 1 | 0 | 1 | 否 | 0 | 否 | 3 |
| s01 | 1 | 0 | 1 | 否 | 0 | 否 | 3 |
| q91 | 2 | 0 | 1 | 否 | 0 | 是 | 7 |
| q107 | 1 | 0 | 1 | 否 | 0 | 否 | 3 |
| q123 | 1 | 0 | 1 | 否 | 0 | 否 | 6 |

⇒ **6/6 全部来自通道 ②b, 且每题只靠 1 个 token**; ①/②a/③ 一次都没参与。
机制: 本研究 EDC 的 item OID 段沿用了 SDTM 风味的命名, 于是一道**纯标准题**里出现的大写
token 会精确撞上某个 OID 段 (150 道 cdisc 判定题里撞上 6 道, 4.0%)。这不是 S2 的缺陷
—— 直查场景下 ②b 本就该宽; 缺陷在于**信号层把「resolve 有任何命中」当成了拓宽依据**。

### 5-1 反事实 G1 (已实测, 零 LLM): 若 study 信号只认强通道 ①/②a/③

```
G1 下 study_sig widen (可见集): {'legacy': (0, []), 'dev': (0, [])}
G1 下 study_sig 探针 fire      : {'legacy': 8, 'dev': 1}
```

⇒ (a) legacy 179 → 179 (Δ0, PASS)、(b) drop 0 (PASS)、(c)-detect 两信号均活 (PASS)
⇒ 三条**全过**。但这要改 `RoutingSignals._study_signal` 的判据, **不是词表/正则改动**,
超出本 task 的旋钮集, 故本 task 不动它, 交 controller 裁定 (须重走 Task 8 的审查环)。

备选 G2 (只排除「命中 token 本身就是 SDTM 标准 token」的那种撞车): 按上表只能消掉 6 题中的 2 题,
legacy 仍 175 < 178, **不足以解阻**。

---

## 6. 冻结范围声明 (诚实版)

| 物 | 状态 |
|---|---|
| `CDISC_STRUCT_TERMS` (8 条) | **未改动**, 随本 commit 冻结 |
| `_CT_CODE_RE` | **未改动** (可见集上 0 次 fire, 无害), 随本 commit 冻结 |
| `_DOMAIN_VAR_RE` + 三张派生表 | 本轮改动, 随本 commit **冻结** —— 此后不许再动 (Task 10 以此版为准) |
| `_study_signal` / `StudyLookup` | **本 task 未动**; 它是 (a) 不达标的唯一来源, 待 controller 裁定 |

⚠ 本文件**不宣称**预登记规则三条全部达标。达标的是 (b)(c-detect) 与"本 task 旋钮内的最优";
(a) 未达标, 单元状态 = **BLOCKED**, 处置在 controller。

---

## 7. 已知限制 (逐条注明"看不见什么 / 不能证明什么")

1. **封存组完全不可见**: 本标定没有、也不允许有任何 held-out / distractor / ambiguous /
   u1_doc / final 的读数。故**不能**声称本词表对那 9 条 fatal 欠账有效或无效 —— 那是 Task 10 的事。
2. **只窄不宽的方向性代价**: R1 的词表是 R0 的**真子集** (§2)。故它在封存组上**只可能少 fire**。
   若某道 distractor/ambiguous 题原本靠"任意 4-8 位大写"这条宽规则才被拓宽, 本轮会把它丢掉。
   这是预登记规则 (a) 逼出来的取舍, 已如实记账。
3. **可见集上 `cdisc_sig` 一次 widen 都没有** (R1: 0 次)。即 (c) 的 widen 读法在 cdisc 侧完全无实证,
   `cdisc_sig` 的"能拓宽"只有构造与单测背书 (Task 8 合成用例), 没有真题背书。
4. **基线单份**: 标定用 `u6_baseline_run_1.json` 一份 (三遍 254/254 逐题一致, Task 6 §4),
   故单份与三遍等价; 但若将来基线不再全稳, 本结论须重算。
5. **G1 的反事实只在可见集上成立**: 它证明"G1 在 legacy+dev 上零害且信号仍活",
   **不证明** G1 能修好那 9 条 fatal。

---

## 8. 回归 / 静态检查 / 泄漏自检

```
$ ./.venv/bin/python -m pytest -q                 # 全量
1628 passed (0 failed; rc=0)                      # 基线 1586 + 本 task 新增 42
$ ./.venv/bin/ruff check server/routing_signals.py eval/u6_calibrate_signals.py \
      scripts/tests/test_u6_calibrate_signals.py
All checks passed!
$ ./.venv/bin/mypy server/routing_signals.py eval/u6_calibrate_signals.py
Success: no issues found in 2 source files
```

(Task 8 的方向/大小写/白名单三组测试逐条仍绿 —— `test_routing_signals.py` 38 passed,
其中 `AESEV` / 全角 `ＡＥＳＥＶ` / 受控术语英文词条 / `Sdtm` 四条命中用例与
`CRF` / 纯数字 / 无拉丁形态三条沉默用例都在本轮新正则下重跑通过。)

```
$ ./.venv/bin/python scripts/leakscan_evidence.py evidence/u6_task9_calibration.md --min-len 12
$ echo "rc=$?"
```

见下方 §8-1 的逐字输出。补充 kana 扫描:

```
$ grep -nP '[\x{3040}-\x{309F}\x{30A0}-\x{30FF}]' evidence/u6_task9_calibration.md
```

→ 无输出 (0 命中)。本文件通篇只有统计值、题号 (`q*` / `s0*` / `st_st01_v11_q*` /
`ja_supp_*` / `u3_doc_03`)、标准变量名、命令与 rc。

### 8-1 泄漏扫描逐字输出

```
target      : evidence/u6_task9_calibration.md
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

### 8-2 一次真实的假阳性及其处置 (如实记录, 不是事后美化)

本文件**初稿**在 min_len=12 下扫出 `LEAK: 2 条 (rc=1)`。两条命中都是 12 字符的**通用英文**
片段 (此处刻意不复述原片段 —— 复述一遍就会把同一段字符再写进本文件, 扫描器会再次命中,
这一点初稿改完后实测过一次): 一条来自初稿 §8 引述 Task 8 某测试用例的英文名, 一条来自
初稿 §2 那句用英文写的规模说明。两处都是与 CDISC 侧**英文**题面共享的常见词,
**不是** study 题面泄漏 (study 侧题面为日文, 见上面 kana 扫描 0 命中)。

处置: 把这两处一律改写成中文表述, 复扫即 §8-1 的 rc=0。记下这一段是因为「扫描器报了一次又变绿」若不写, 下一个人会以为
本文件一次就干净, 从而低估这个闸的作用; 而这次命中恰好证明它在 min_len=12 下不是空转。

### 8-3 阈值敏感性 (引用 CLEAN 必须连阈值一起写)

| min_len | 结果 | rc |
|---|---|---|
| 8 | LEAK: 55 条 | 1 |
| 10 | LEAK: 14 条 | 1 |
| 12 | CLEAN: 0 条 | 0 |

(三档均在本文件**定稿内容**上测得。8/10 档的计数对本文件自身正文长度敏感 —— 加了 §8-2/§8-3
这两节中文说明后, 8 档由 35 升到 55、10 档由 8 升到 14, 全是本文正文里的通用英文词;
12 档恒为 0, 与正文增删无关。)

8 / 10 档命中**全部**来自 `eval/test_set_v3.yml` 一侧, 是本文件正文/命令里的通用英文词
(字段名、模块名、`variables` / `controlled` 这类词) 与 CDISC 英文题面共享的短子串,
逐条可判读为非题面泄漏。默认阈值取 12 正是为避开这类通用词假阳性。

---

## 9. 观测 vs 派出前预期

| 项 | 派出前预期 | 实测 | 判定 |
|---|---|---|---|
| 主要旋钮 | `_DOMAIN_VAR_RE` 过宽, 在 study 侧误触 | 确认: R0 误触 6 题, 全部 `_DOMAIN_VAR_RE`, terms/CT 码 0 次 | ✓ |
| 误触形态 | GRPTOX / CTCAE / IWRS / COVID / VIII 一类 | 实际撞上的是另一批同形态缩写 (3 例试验/量表/系统缩写), 机制相同 | ✓ (形态吻合, 具体 token 不同) |
| dev 侧代价 | 允许掉 ≤1 | 实测 0 | 优于预期 |
| (a) 可否达标 | 派出时假设"剪词表即可" | **否** —— 损失有一半在旋钮外 (study 侧) | ✗ 与预期不符, 已按实情上报 |
| 轮数 | ≤5 | 2 (第 3 轮起为结构性无效, 见 §3) | 提前收敛 |
| LLM 调用 | 0 | 0 | ✓ |
