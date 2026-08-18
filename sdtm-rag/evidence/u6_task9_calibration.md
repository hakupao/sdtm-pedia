# U6 Task 9 — 可见集标定 (legacy 181 + dev 12; 词表/正则)

> 日期: 2026-08-18 (标定 R0/R1); 2026-08-18 终值 (G1 后复跑)
> 执行目录: `sdtm-rag/` (以下命令逐字可复跑, 全部 `./.venv/bin/python`)
> git rev: R0/R1 于 `v1.4-company-release-504-g4e252bb`; **终值**于 `8dcb622` (G1 已合入, 工作树干净)
> 参照物: Task 6 冻结基线 `data/study/st01/eval/runs/u6_baseline_run_1.json` (gitignored)
> **零 LLM 调用** (标定是离线模拟); 红线: 本文件只记题号 / 组名 / 计数 / 命令 / rc —— 零题面。
> 可见集纪律 (spec §5.2): 全程只读 `legacy` + `dev`; held-out / distractor / ambiguous /
> u1_doc / final 五组**一次都没有被读过** (仪器在读入处就丢弃, 见 §1)。

---

## 0. 一句话结论 (终值)

**三条预登记规则全过, 标定收口, 信号层定义冻结** (`rc=0`, `accepted = True`):

| 规则 | 判定 | 终值 |
|---|---|---|
| (a) legacy exact 不降 | ✅ PASS | 179 → **179** (Δ0) |
| (b) dev exact 降 ≤1 | ✅ PASS | 12 → **12** (drop 0) |
| (c) 双信号活 (detect 读法, controller 裁定) | ✅ PASS | study_sig **9** / cdisc_sig **104** |

双读法数字并列 (引用 (c) 必须连读法一起写, 见 §4):

| 读法 | study_sig | cdisc_sig | 含义 |
|---|---|---|---|
| **widen** (拓宽真的发生, 可见集) | **0** | **0** | 可见集上信号层一次都没改判 —— 这正是 (a)(b) 要的"零害", 但同时意味着**可见集不提供任何"信号真的会 fire"的正面证据** |
| **detect** (探针命中, 可见集) | **9** (legacy 8 + dev 1) | **104** (legacy 104 + dev 0) | 两个信号都不是死代码 |

⚠ **`study_sig` 的真实活性由 Task 10 after 批的逐题 `widened_by` 字段回答**, 不由本文件回答:
可见集上它 widen 0 次 (按构造, 见 §4 —— 可见集里每道单库题都已判对, 任何 widen 都是纯损失),
所以"它在真实欠账题上会不会 fire"在这里**结构上不可测**。同理 `cdisc_sig`。

### 0-1 到达终值的经过 (不省略失败)

1. **R0** (Task 8 起点词表): legacy 179 → 167, (a) ⛔。误触 12 题 = study 侧 6 + cdisc 侧 6。
2. **R1** (词表标定, 本 task 旋钮内): cdisc 侧误触 6 → 0, legacy 179 → 173, (a) 仍 ⛔。
   当时结论 = **BLOCKED**: 余下 6 分全部来自 `study_sig`, 其判据 `StudyLookup.resolve`
   与本 task 三个旋钮无数据依赖 ⇒ 再标定多少轮都恒等。
3. **G1** (controller 裁定后的**代码**改动, commit `8dcb622`, 非词表轮次): study 信号判据由
   「`resolve` 任意命中」收紧为 `StudyLookup.strong_hit()` (①label / ②a 多 token 交集 / ③别名),
   排除弱通道 ②b (单个大写 token 撞 OID 段)。
4. **终值** (G1 后复跑本标定台): 6 题误触全消, legacy 回到 179, 三条全过。

R1 的 BLOCKED 报告里给出的可见集反事实预测 (widen 0 次 / study_sig 探针 legacy 8 + dev 1 /
三条全过) 与 G1 后的实测**逐数字相符**, 见 §5-1。

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

## 3. 轮次表 (词表轮 ≤5; 实际用 2 轮 + 1 次裁定后的代码改动)

| 轮 | 性质 | 改动 | (a) legacy exact | (b) dev drop | (c) widen 读法 | (c) detect 读法 | widen fire (study_sig / cdisc_sig) | accepted |
|---|---|---|---|---|---|---|---|---|
| R0 | 词表轮 | 起点 (Task 8 词表, `[A-Z]{4,8}`) | ⛔ 179 → **167** (−12) | PASS 0 | PASS 6/6 | PASS 16/117 | legacy 6 / legacy 6 | ✗ |
| R1 | 词表轮 | `_DOMAIN_VAR_RE` 锚定到 KB 派生的域码+词根+单独变量 | ⛔ 179 → **173** (−6) | PASS 0 | ⛔ 6/0 | PASS 16/104 | legacy 6 / **0** | ✗ |
| **G1** | **代码改动 (controller 裁定后; 非词表轮次)** | `_study_signal` 由 `resolve()` 任意命中 → `StudyLookup.strong_hit()` (排除弱通道 ②b); 词表**一字未动** | ✅ 179 → **179** (Δ0) | ✅ PASS 0 | ⛔ 0/0 | ✅ PASS 9/104 | **0 / 0** | **✓** |

- R0 → R1 的差: cdisc 侧误触 6 题 (`st_st01_v11_q07 / q11 / q16 / q19 / q20 / q22`) 全部消除,
  legacy 回补 6 分; study 侧那 6 题 (`q19 / q43 / s01 / q91 / q107 / q123`) **逐题不变**。
- R1 → G1 的差: study 侧那 6 题**全部消除**, legacy 回到 179。G1 由 controller 在收到 R1 的
  BLOCKED 报告后裁定并另行实现 (commit `8dcb622`, 含 `resolve()` 8127 条差分逐位不变的证据),
  **不计入本 task 的 ≤5 轮词表迭代预算** —— 它改的是信号层判据代码, 不是词表。
- G1 后 `detector fire study_sig legacy` 由 15 降为 8: 掉的正是那 6 道纯标准题, 外加
  `st_st01_v11_q16` (它此前也只有弱通道命中)。`cdisc_sig` 侧一格未动 (104), 因为 G1 不碰 cdisc 半边。

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

### 3-3 终值 stdout (逐字, G1 合入后 — 词表与 R1 逐字相同)

跑批命令与 §1 复跑命令一字不差; 代码状态 = commit `8dcb622`, 工作树干净。

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
  study_sig  legacy   n=  8  ['st_st01_v11_q01', 'st_st01_v11_q03', 'st_st01_v11_q08', 'st_st01_v11_q14', 'st_st01_v11_q17', 'st_st01_v11_q19', 'st_st01_v11_q20', 'st_st01_v11_q21']
  study_sig  dev      n=  1  ['u3_doc_03']
  cdisc_sig  legacy   n=104   (逐题同 R1)
  cdisc_sig  dev      n=  0  []

a_legacy_exact_not_lower         PASS  {"base": 179, "sim": 179}
b_dev_exact_drop_le_1            PASS  {"base": 12, "sim": 12, "drop": 0}
c_both_signals_alive_widen       ⛔ 未达标  {"counts": {"study_sig": 0, "cdisc_sig": 0}}  (仅报告)
c_both_signals_alive_detect      PASS  {"counts": {"study_sig": 9, "cdisc_sig": 104}}  ← 操作性读法
accepted = True  (c 读法: detect)
rc=0
```

(`cdisc_sig legacy` 那行的 104 个题号与 §3-2 逐题相同, 此处压缩为计数; 完整清单跑一次
复跑命令即得。)

**读这张表最容易读错的一格**: `widen fire` 四格全 0 **不是**"信号层没装上", 而是
"可见集上没有一道题需要它" —— 这正是 (a)(b) 要的零害。信号层是否装上由 `accepted=True`
之外的另一组证据看住: `detector fire` 两侧非零 (探针活着) + Task 8 的方向/契约单测 +
Task 10 after 批的 `meta.signal_layer=on` 与逐题 `widened_by` 字段。

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

### 5-1 反事实 G1 → 已实现并实测证实

R1 期 (BLOCKED 报告里) 用旁路脚本量的**预测**:

```
G1 下 study_sig widen (可见集): {'legacy': (0, []), 'dev': (0, [])}
G1 下 study_sig 探针 fire      : {'legacy': 8, 'dev': 1}
```

G1 实现并过 scoped 审查后 (commit `8dcb622`), 用**本标定台**复跑的实测 (§3-3):

| 量 | R1 期预测 | G1 后实测 | 相符 |
|---|---|---|---|
| study_sig widen (legacy / dev) | 0 / 0 | 0 / 0 | ✓ |
| study_sig 探针 fire (legacy / dev) | 8 / 1 | 8 / 1 | ✓ |
| (a) legacy exact | 179 (Δ0) | 179 (Δ0) | ✓ |
| (b) dev drop | 0 | 0 | ✓ |
| (c)-detect | 两信号均活 | 9 / 104 | ✓ |

预测与实测逐数字相符, 无偏差可记。注意两者是**两条独立实现路径**得到的同一批数字:
预测用的是旁路脚本自己拼的通道判据 (raw label 子串 + cap 过滤后的交集 + 别名),
实测走的是 G1 落地的 `StudyLookup.strong_hit()` (三条通道**全部**取 cap 过滤后的命中)。
两者在 label 通道的 cap 处理上并不完全等价, 而可见集上读数相同 —— 说明可见集里没有
"label 命中但超 cap" 的题, 不说明两种写法一般等价。

备选 G2 (只排除「命中 token 本身就是 SDTM 标准 token」的那种撞车): 按上表只能消掉 6 题中的 2 题,
legacy 仍 175 < 178, **不足以解阻**; 未采纳。

---

## 6. 冻结声明 — **信号层定义 (代码 + 常量) 自此冻结**

Task 10 全闸跑批之前, 下表每一项**一字不许再动**。改动其中任何一项 ⇒ 本标定作废, 须重跑。

| 冻结物 | 位置 | 现状 |
|---|---|---|
| 拓宽理由白名单 `WIDEN_REASONS` | `server/routing_signals.py` | `("study_sig", "cdisc_sig")` (Task 8 起未动) |
| 方向表 `WIDEN_REASON_BY_CORPUS` | 同上 | `{"cdisc": "study_sig", "study": "cdisc_sig"}` (Task 8 起未动) |
| `CDISC_STRUCT_TERMS` | 同上 | 8 条, 本 task **未改动** |
| `_CT_CODE_RE` | 同上 | 未改动 (可见集 0 次 fire, 无害) |
| `_DOMAIN_VAR_RE` + `_SDTM_DOMAIN_CODES` (60) / `_SDTM_VAR_ROOTS` (200) / `_SDTM_STANDALONE_VARS` (98) | 同上 | R1 冻结版 (§2 可逐字复算) |
| `_study_signal` 判据 | 同上 | **G1 版**: `StudyLookup.strong_hit()` (①label / ②a 交集 / ③别名; 排除弱通道 ②b) |
| `strong_hit` / `_channel_hits` | `server/study_lookup.py` | G1 新增只读方法; `resolve()` 逐位不变 (差分 8127 条 IDENTICAL, 见 `evidence/step_u6_g1_strong_channel.md`) |
| `decide_corpus` 的 widen 契约 (白名单闸 / 方向闸 / 异常旁路) | `server/federation.py` | Task 7/8 版, 本 task 未动 |

参照物 (Task 10 的 `--baseline`): `data/study/st01/eval/runs/u6_baseline_run_{1,2,3}.json`
(Task 6 冻结, gitignored)。标定终值产自 commit `8dcb622`, 工作树干净。

本文件**宣称**: 预登记三条规则在可见集上全部达标 (§0 终值表), 且 (c) 的读法与双数字
已按 controller 裁定并列写明。本文件**不宣称**信号层能修好那 9 条 fatal 欠账 —— 见 §7。

---

## 7. 已知限制 (逐条注明"看不见什么 / 不能证明什么")

1. **封存组完全不可见**: 本标定没有、也不允许有任何 held-out / distractor / ambiguous /
   u1_doc / final 的读数。故**不能**声称本信号层对那 9 条 fatal 欠账有效或无效 —— 那是 Task 10 的事。
2. **可见集上两个信号 widen 各 0 次** (§3-3)。这意味着本标定证明的是**零害**, 完全没有证明
   **有效**: "信号真的会把某道题拓宽成 both" 这件事在可见集上**结构上不可测**
   (按 §4 的推证, 可见集里每道单库题都已判对, 任何 widen 都是纯损失 —— 换言之, 可见集
   本来就不该有 widen)。
   ⇒ **`study_sig` 与 `cdisc_sig` 的真实活性, 由 Task 10 after 批的逐题 `widened_by` 字段回答**
   (run json `detail` + `meta.signal_layer=on`), 不由本文件回答。引用本文件的 (c) 结论时,
   必须连"这是 detect 读法 / widen 读法为 0"一起写。
3. **两次"只窄不宽"的方向性代价**:
   (i) R1 词表是 R0 的**真子集** (§2) ⇒ 封存组上只可能少 fire;
   (ii) G1 的强通道判据是"resolve 任意命中"的**真子集** ⇒ 同样只可能少 fire。
   若某道 distractor/ambiguous 题原本靠"任意 4–8 位大写"或靠弱通道 ②b 才被拓宽, 这两步会把它丢掉。
   这是预登记规则 (a) 逼出来的取舍, 已如实记账 —— 修法收窄到"零害"的代价就是修法面也变窄。
4. **基线单份**: 标定用 `u6_baseline_run_1.json` 一份 (三遍 254/254 逐题一致, Task 6 §4),
   故单份与三遍等价; 但若将来基线不再全稳, 本结论须重算。
5. **离线模拟 ≠ 真跑**: 本标定假设 router 在 after 批会给出与冻结基线**逐题相同**的判定
   (基线三遍全稳支持这个假设, 但它是假设)。若 after 批某题判定漂移, 该题的 widen 结论随之作废。
   Task 10 的三遍 + `clause6_unstable` 是这条假设的检验处。

---

## 8. 回归 / 静态检查 / 泄漏自检

终值状态 (commit `8dcb622`, 工作树干净) 实测:

```
$ ./.venv/bin/python -m pytest -q                 # 全量
1641 passed (0 failed; rc=0)     # Task 9 前 1586 + 标定台 42 + G1 新增 13
$ ./.venv/bin/ruff check server/routing_signals.py server/study_lookup.py \
      eval/u6_calibrate_signals.py scripts/tests/test_u6_calibrate_signals.py \
      scripts/tests/test_routing_signals.py scripts/tests/test_study_lookup.py
All checks passed!
$ ./.venv/bin/mypy server/routing_signals.py eval/u6_calibrate_signals.py server/study_lookup.py
Success: no issues found in 3 source files
```

(R1 期同口径读数为 `1628 passed`; 差的 13 条是 G1 commit 带进来的 study_lookup/信号层测试。
ruff 全目录扫 `server/ eval/` 另有 36 条**既有**告警, 全部落在本单元未触碰的文件
`cap_recall_sweep.py` / `error_test_set.py` / `u3_task8_verdict.py` 等; 本单元触碰的 6 个文件
逐个扫过为 `All checks passed!` —— 引用"绿"时必须连这条范围限定一起写。)

(Task 8 的方向/大小写/白名单三组测试逐条仍绿 —— `test_routing_signals.py` **42 passed**
(G1 后由 38 增至 42), 其中 `AESEV` / 全角 `ＡＥＳＥＶ` / 受控术语英文词条 / `Sdtm` 四条命中
用例与 `CRF` / 纯数字 / 无拉丁形态三条沉默用例都在冻结版正则下重跑通过。)

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
| (a) 可否达标 | 派出时假设"剪词表即可" | **否** —— 损失有一半在旋钮外 (study 侧) | ✗ 与预期不符, 已按实情上报 BLOCKED |
| 轮数 | ≤5 | 2 (第 3 轮起为结构性无效, 见 §3) | 提前收敛 |
| G1 后 (a)(b)(c) | R1 期反事实预测: 三条全过, widen 0, 探针 8+1 | 实测逐数字相符 (§5-1) | ✓ 预测被证实 |
| LLM 调用 (终值复跑) | 0 | 0 | ✓ |
| LLM 调用 | 0 | 0 | ✓ |
