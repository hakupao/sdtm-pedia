# U2 物理变异实证

> 单元: doc 轨 U2 接线 (plan `docs/superpowers/plans/2026-08-12-doc-track-u2-wirein.md`)
> 目的: 证明新加的断言不是装饰品 —— 每条改坏实现后必须有测试变红 (Global Constraint 7 / 硬规矩 18)。
> 口径: 每条变异**单独**施加, 施加后跑**全量** `./.venv/bin/python -m pytest -p no:warnings`, 记录 failed 数, 然后**改回**再做下一条。

## 复跑命令

```bash
cd /Users/bojiangzhang/MyProject/sdtm-pedia/sdtm-rag
./.venv/bin/python -m pytest -p no:warnings          # 未变异基线
# 逐条按下表改 server/study_corpus.py, 每条跑一次上面这条命令, 记 failed 数, 改回
```

## Task 1 — `server/study_corpus.py` (2026-08-12 实测)

| # | 变异 (施加于 `server/study_corpus.py`) | 期望 | 实测 failed | 变红的测试 |
|---|---|---|---|---|
| 0 | 无 (基线) | 0 failed | **0 failed / 1127 passed** | — |
| 1 | `retrieve` 里 `if seats <= 0: return chunks` 改成无条件 `return chunks` (恒不取 doc) | ≥1 | **3 failed / 1124 passed** | `test_cards_keep_full_top_k_and_docs_are_appended` · `test_per_call_doc_seats_overrides_default` · `test_format_context_groups_the_two_source_kinds` |
| 2 | `chunks = list(self.cards.retrieve(question, top_k=top_k))` 改成 `top_k=seats` (抢席) | ≥1 | **2 failed / 1125 passed** | `test_cards_keep_full_top_k_and_docs_are_appended` · `test_format_context_groups_the_two_source_kinds` |
| 3 | `system_prompt` 改成 `return self.docs.system_prompt + _DOC_CORPUS_RULES` | ≥1 | **1 failed / 1126 passed** | `test_system_prompt_comes_from_cards_engine_never_docs` |
| 4 | `format_context` 去掉 `if docs:` 守卫 (恒打空的手順書小节) | ≥1 | **1 failed / 1126 passed** | `test_format_context_omits_absent_group` |

计划指定的四条**全部变红** (无一条变异后全绿)。另见下方补做的变异 5-7。

### 变红细节 (原文摘要, 证明是被断言抓到而非 collection error)

- 变异 1: `assert docs.calls == [5]` → `assert [] == [5]`; `CTX-doc(2)` 不在 context 里。
- 变异 2: `assert cards.calls == [15]` → 实际 `[5]`; context 变成 `CTX-card(2)` (cards 席位被 doc 的 seats 数顶替)。
- 变异 3: `assert "POISON" not in eng.system_prompt` 失败 (docs 引擎的 prompt 被读进去了)。
- 变异 4: `assert "CTX-doc" not in ctx` 失败, 实际打出了 `## 【手順書章節】\nCTX-doc(0)` 空小节。

### 计划四条**没有**覆盖到的断言 → 当场补做变异 5-7

计划指定的四条变异跑完后, 8 条断言里有 3 条**从未变红过** (它们守的是另外三处代码:
`seats<=0` 早返边界、`seen` 去重、`ValueError` 闸)。按硬规矩 18 的意图 (未被证伪的断言 =
未证明的断言), 实现方当场补做三条变异, 同一口径 (单条施加 → 全量 pytest → 改回):

| # | 变异 | 期望 | 实测 failed | 变红的测试 |
|---|---|---|---|---|
| 5 | `if seats <= 0:` 改成 `if seats < 0:` (seats=0 时仍去打 docs 引擎) | ≥1 | **2 failed / 1125 passed** | `test_doc_seats_zero_means_channel_off` · `test_format_context_omits_absent_group` |
| 6 | 删掉 `if d.chunk_id in seen: continue` (不去重) | ≥1 | **1 failed / 1126 passed** | `test_duplicate_chunk_ids_are_deduped_cards_win` |
| 7 | `if doc_seats < 0: raise ValueError(...)` 改成 `doc_seats = max(doc_seats, 0)` (静默夹紧) | ≥1 | **1 failed / 1126 passed** | `test_negative_doc_seats_fails_loud` |

⇒ ~~**8 条断言全部至少被一条变异证伪过, 无装饰断言残留。**~~

> ⛔ **此结论已被独立审查方推翻 (2026-08-12), 见下方「Task 1 修复轮」。** 上面这句话说的是
> "8 条**断言**都被证伪过", 但那只证明了**断言侧**没有装饰品, 完全没有覆盖**代码侧**:
> 独立审查方从代码行出发另设计 9 条变异, **9 条全部存活**。原句保留划线不删, 作为
> "自证式变异测试会漏什么" 的样本 (规则 B: 失败数据不删)。

## 复原核验

七条变异逐条改回后:

- 全量 `pytest -p no:warnings` → **1127 passed** (= 开工基线 1119 + 本 task 新增 8)。
- `server/study_corpus.py` 与计划 §Task 1 Step 3 的代码块 **byte-identical**
  (`diff <(sed -n '166,229p' docs/superpowers/plans/2026-08-12-doc-track-u2-wirein.md) sdtm-rag/server/study_corpus.py` → 空)。
- `scripts/tests/test_study_corpus.py` 与计划 §Task 1 Step 1 的代码块同样 byte-identical。

---

## Task 2 — `server/config.py` + `server/main.py` lifespan (2026-08-12 实测)

开工基线 **1127 passed** (Task 1 收尾态); Task 2 落地后 **1131 passed** (新增 4 条测试)。
变异口径与 Task 1 相同: 单条施加 → 全量 `./.venv/bin/python -m pytest -p no:warnings` → 记 failed 数 → 改回。

新增的 4 条测试共 **10 条断言** (下表以 A1-A10 编号):

| 断言 | 出处 (`scripts/tests/test_main_study_docs_wiring.py`) | 守什么 |
|---|---|---|
| A1 | `"study_st01_docs" in built` | docs 引擎用的是 doc collection, 不是卡片 collection |
| A2 | `isinstance(...federation.study, StudyCorpusEngine)` | 建了还要**包**进联邦 |
| A3 | `...federation.study.doc_seats == 5` | 席位数进了组合器 |
| A4 | 关着时 `"study_st01_docs" not in built` | 开关关着不建 docs 引擎 |
| A5 | 关着时 `not isinstance(..., StudyCorpusEngine)` | 开关关着不包 |
| A6 | 联邦关着时 `"study_st01_docs" not in built` | 没有 study 引擎可挂时不空建 |
| A7 | `any(m == "study_docs_ignored" ...)` | 联邦关着 + doc 开着必须留声 |
| A8 | `hit` 非空 | `study_docs` 这行日志确实打了 |
| A9 | `hit[0]["seats"] == 7` | 日志里的席位数来自 settings 而非常量 |
| A10 | `hit[0]["collection"] == "study_st01_docs"` | 日志里的库名来自 doc setting 而非卡片 setting |

### 计划指定的三条

| # | 变异 (施加于 `server/main.py`) | 期望 | 实测 failed | 变红的测试 | 覆盖断言 |
|---|---|---|---|---|---|
| 0 | 无 (基线) | 0 failed | **0 failed / 1131 passed** | — | — |
| 1 | `study_engine = StudyCorpusEngine(...)` 的赋值去掉 (只建不包) | ≥1 | **1 failed / 1130 passed** | `test_docs_engine_is_built_and_wrapped_when_enabled` | A2 A3 |
| 2 | `doc_seats=s.study_docs_seats` 改成常量 `doc_seats=5` | ≥1 | ⚠ **0 failed / 1131 passed** → 补断言后 **1 failed / 1130 passed** | (补断言后) `test_seats_and_collection_are_reported_in_the_ready_log` | A3(旧,失效) → 新增断言 |
| 3 | `study_docs_ignored` 告警整块删掉 | ≥1 | **1 failed / 1130 passed** | `test_docs_enabled_without_federation_logs_ignored` | A7 |

**⚠ 变异 2 首轮全绿 = 装饰断言, 当场补断言。** 原因: 计划里唯一检查引擎席位的 A3 恰好用
`study_docs_seats=5`, 与写死的常量 `5` 逐位相同; 而用 seats=7 的那条测试只看**日志**, 不看引擎。
于是"日志报 7 席、引擎实际只拿 5 席"这类日志撒谎故障在计划的断言集下完全不可见。
补的断言 (在 seats=7 那条测试里): `assert app.state.federation.study.doc_seats == 7` ——
用非默认值把日志与引擎钉成同源。补后重跑变异 2 → **1 failed**, 装饰性解除。

### 实现方自查补做的六条 (计划三条只覆盖 A2/A3/A7, 其余 7 条断言从未变红过)

同 Task 1 的做法: 未被证伪的断言 = 未证明的断言。补做六条, 同一口径。

| # | 变异 (施加于 `server/main.py`) | 期望 | 实测 failed | 变红的测试 | 覆盖断言 |
|---|---|---|---|---|---|
| 4 | docs 引擎的 `collection_name=s.study_docs_collection_name` 改成 `s.study_collection_name` (指回卡片库) | ≥1 | **1 failed / 1130 passed** | `test_docs_engine_is_built_and_wrapped_when_enabled` | A1 |
| 5 | `if s.study_docs_enabled:` 改成 `if True:` (开关失效, 恒建恒包) | ≥1 | **3 failed / 1128 passed** | `test_docs_engine_absent_when_disabled` + `test_main_study_lookup_wiring.py::test_enabled_injects_study_lookup_into_study_engine` + `::test_disabled_injects_nothing` | A4 A5 |
| 6 | 日志 `seats=s.study_docs_seats` 改成常量 `seats=5` | ≥1 | **1 failed / 1130 passed** | `test_seats_and_collection_are_reported_in_the_ready_log` | A9 |
| 7 | 日志 `collection=s.study_docs_collection_name` 改成 `s.study_collection_name` | ≥1 | **1 failed / 1130 passed** | `test_seats_and_collection_are_reported_in_the_ready_log` | A10 |
| 8 | 整条 `log.info("study_docs", ...)` 删掉 | ≥1 | **1 failed / 1130 passed** | `test_seats_and_collection_are_reported_in_the_ready_log` | A8 |
| 9 | 在 `study_docs_ignored` 分支里也构造一台 docs `RAGEngine` (联邦关着仍空建) | ≥1 | **1 failed / 1130 passed** | `test_docs_enabled_without_federation_logs_ignored` | A6 |

⇒ **10 条断言 (含补做的第 11 条) 全部至少被一条变异证伪过, 无装饰断言残留。**

变异 5 顺带把既有的 `test_main_study_lookup_wiring.py` 两条也打红 —— 那是因为它按位置解包
`cdisc, study = boot(s).engines`, doc 引擎恒建会多出第三台。这不是搭车断言, 而是同一条 bug
的两处独立现场; 记在此以免下一个人误以为是 flaky。

### Task 2 复原核验

九条变异逐条改回后:

- `diff` 与变异前的备份 → `server/main.py` 与 `server/config.py` **完全一致** (零残留)。
- 全量 `pytest -p no:warnings` → **1131 passed** (= Task 1 收尾 1127 + 本 task 新增 4)。
- 计划 §Task 2 Step 3/Step 4 的三个代码块与落地代码 **byte-identical**:
  ```bash
  cd /Users/bojiangzhang/MyProject/sdtm-pedia
  diff <(sed -n '369,374p' docs/superpowers/plans/2026-08-12-doc-track-u2-wirein.md) <(sed -n '53,58p'   sdtm-rag/server/config.py)  # config 三个 setting
  diff <(sed -n '385,408p' docs/superpowers/plans/2026-08-12-doc-track-u2-wirein.md) <(sed -n '136,159p' sdtm-rag/server/main.py)    # lifespan 接线
  diff <(sed -n '416,421p' docs/superpowers/plans/2026-08-12-doc-track-u2-wirein.md) <(sed -n '178,183p' sdtm-rag/server/main.py)    # study_docs_ignored 告警
  ```
  三条 diff 均为空。

### 与计划的偏离 (仅测试脚手架, 断言零改写)

计划 §Task 2 Step 1 的 fixture 写的是
`structlog.configure(processors=[lambda _l, m, ed: events.append((m, ed)) or ""])`,
把元组首位当成**事件名**用。structlog 的 processor 签名实为
`(logger, method_name, event_dict)` —— `m` 绑的是 `"info"` / `"warning"` 这个**方法名**,
事件名在 `ed["event"]` 里。实测:

```bash
cd /Users/bojiangzhang/MyProject/sdtm-pedia/sdtm-rag && ./.venv/bin/python -c "
import structlog
seen=[]
structlog.configure(processors=[lambda _l, m, ed: seen.append((m, ed)) or ''])
structlog.get_logger().warning('study_docs_ignored', note='x')
print(seen)"
# → [('warning', {'note': 'x', 'event': 'study_docs_ignored'})]
```

故照原文抄时 A7/A8/A9/A10 在**任何实现下都不可能通过** (首跑即 3 failed, 其中两条是这个原因)。
修法取计划 Step 1 docstring 自己指的路 (「仿 `test_main_study_lookup_wiring.py` 的 stub 编制」):
改用 `structlog.testing.capture_logs()`, 元组首位换成 `e["event"]`。附带收益是不再往全局
structlog 配置里永久塞处理器 (裸 `configure` 会泄漏给后续测试)。**四条测试的断言一字未改。**

---

## Task 1 修复轮 — 独立审查方 REQUEST-CHANGES 后 (2026-08-12)

独立审查方 (不同 subagent_type / 不同 session) 判定: **实现逻辑无缺陷** (三路席位、去重方向、
早返、守卫全部实证正确), 问题**全在断言缺口**。它独立设计 9 条变异, **9 条全部存活 (8 tests 全绿)**。

### 方法论差异 (本轮最贵的一条, 给 Task 9 抽检方: 别重复踩)

| | 实现方首轮 | 独立审查方 |
|---|---|---|
| 搜索方向 | **从断言出发**: 找能杀死这条断言的变异 | **从代码行出发**: 问这行改坏了谁会红 |
| 覆盖到的 | 断言侧无装饰品 (7/7 变异变红) | 代码侧大片无人守 (9/9 变异存活) |
| 结构性盲区 | 只会构造"已经有人守"的变异 —— **恒不可能发现无人守的代码行** | — |

⇒ **自证式变异测试的上界 = 已有断言的集合。** 实现方跑出"变异全红"时,证明的是
"我写的断言不是装饰品",**不是**"我的代码被守住了"。这两句话在首轮被混为一谈。
Task 9 的抽检方 B 若也从断言出发, 会重现同一盲区 —— **必须从代码行 / diff 出发**。

### 本轮改了什么

| # | 改动 | 类型 |
|---|---|---|
| 1 | `format_context` 两个分组标题补字面断言 (含 `\n\n` 前导, 保证 `##` 在行首) | 补断言 |
| 2 | `retrieve` 删掉 `**kw` + 补 `TypeError` 断言 | 删代码 + 补断言 |
| 3 | **删掉 `build_messages`** (生产路径不可达的死代码) + 补 `not hasattr` 断言 | 删代码 + 补断言 |
| 4 | `_DOC_CORPUS_RULES` 补内容断言 (两类来源 + 節番号) | 补断言 |
| 5 | `file_type=None` 落进卡片组的断言 (反选 vs 正选) | 补断言 |
| 6 | both 模式席位测试 (spec §7 列为必测, 计划漏分配给任何 task) | 补断言 |
| 7 | per-call `doc_seats` 负值补 `ValueError` 闸 (与 `__init__` 同纪律) | 补代码 + 补断言 |
| 8 | docs 引擎**自身**返回重复 id 的去重断言 (原测试走不到 `seen.add` 那行) | 补断言 |
| 9 | `list()` 防御性拷贝的断言 (审查方变异 F, 本轮之前无人守) | 补断言 |

测试 8 条 → **16 条**。

### `build_messages` 删除前的调用方核验 (逐字命令 + 结果)

```bash
cd /Users/bojiangzhang/MyProject/sdtm-pedia/sdtm-rag
grep -rn "build_messages" --include="*.py" . | grep -v "\.venv/"           # [G1]
grep -rn "\.study\." --include="*.py" . | grep -v "\.venv/" | \
  grep -v "study_lookup\|study_corpus\|study_kb\|study_docs\|study_collection\|study_catalog\|study_aliases"  # [G3]
```

- **[G1]**: 全仓 `build_messages` 共 38 处。唯一在联邦路径上的是
  `server/federation.py:148` → `msgs = self.cdisc.build_messages(...)` —— 走 **cdisc** 引擎。
  其余调用方 (`server/router.py` ×5 / `eval/run_eval.py:353` / `eval/prod_wirein/forensic_*.py` /
  `eval/crowding_ab.py:509` / `eval/vi_completeness_ab.py:50`) 的接收者均为 CDISC `RAGEngine`
  (逐处核过: 三个 `eng.build_messages` 的 `eng` 都由 `settings.kb_root` + `settings.collection_name`
  构造) 或 `FederatedEngine` 本身。**无一处调用 study 引擎的 build_messages。**
- **[G3]**: 全仓对 `.study.` 的成员访问只有 5 处, 全在 `federation.py`:
  `retrieve` (:122/:129) · `format_context` (:143) · `system_prompt` (:156/:158)。
  ⇒ `StudyCorpusEngine` 的鸭子接口实际只需三件套, `build_messages` 结构上不可达。

### 变异复验 (17 条, 2026-08-12 实测)

口径变更: 本轮**不再改动工作树**。变异施加在真实源码的**副本**上, 用 conftest 把副本注入
`sys.modules['server.study_corpus']`, 跑**真实的** `scripts/tests/test_study_corpus.py`
(每次从工作树重新拷贝)。驱动器对每条变异先断言"替换确实发生了" —— 一条写错的变异会以
no-op 身份显示全绿, 被误读成"断言是装饰品"。

```bash
cd /Users/bojiangzhang/MyProject/sdtm-pedia/sdtm-rag
./.venv/bin/python <scratch>/mut2/drive.py      # 驱动器 + conftest 见报告; 不进 git
```

| # | 变异 | 结果 | 变红的测试 |
|---|---|---|---|
| BASE | 无 | 16 passed | — |
| R1-1 | 去掉 `seats<=0` 早返 (恒不取 doc) | **RED 5** | cards_keep_full_top_k · both_mode · per_call_doc_seats · format_context_groups · docs_internal_dup |
| R1-2 | cards 抢席 `top_k`→`seats` | **RED 3** | cards_keep_full_top_k · both_mode · format_context_groups |
| R1-3 | `system_prompt` 读 docs 引擎 | **RED 1** | system_prompt_comes_from_cards_engine_never_docs |
| R1-4 | `format_context` 去掉 `if docs:` 守卫 | **RED 1** | format_context_omits_absent_group |
| A | 删掉两个分组标题 | **RED 1** | format_context_groups_the_two_source_kinds |
| A2 | 只删手順書标题 | **RED 1** | format_context_groups_the_two_source_kinds |
| I | `"\n\n".join` → `"".join` (`##` 不在行首) | **RED 1** | format_context_groups_the_two_source_kinds |
| B | `_DOC_CORPUS_RULES = ""` | **RED 1** | system_prompt_names_both_source_kinds_and_keeps_section_numbers |
| C | re-add `build_messages` (弱版) | **RED 1** | engine_builds_no_messages_of_its_own |
| D | re-add `build_messages` (原版) | **RED 1** | engine_builds_no_messages_of_its_own |
| E | 去掉 `seen.add(d.chunk_id)` | **RED 1** | docs_internal_duplicates_are_deduped_too |
| G | 分组改正选 `== CARD_FILE_TYPE` | **RED 1** | unknown_file_type_is_grouped_with_cards_never_dropped |
| KW | `retrieve` 重新收 `**kw` | **RED 1** | unknown_kwarg_fails_loud_not_silently_swallowed |
| NEG | 删掉 per-call 负席位闸 | **RED 1** | negative_per_call_doc_seats_fails_loud_before_any_retrieval |
| MIN | `seats = min(seats, top_k)` (both 下缩 doc 席位) | **RED 1** | both_mode_halves_cards_but_never_shrinks_doc_seats |
| F | 去掉 `list()` 防御性拷贝 | **RED 1** (补断言前 GREEN) | retrieve_never_mutates_the_cards_engine_result |
| H | `if seats <= 0` → `if seats == 0` | **GREEN(存活)** | — 见下 |

**变异 H 存活是正确的, 不是缺口**: 修复 7 之后负席位在函数开头就 `raise`, 能走到该守卫的
`seats` 恒 `>= 0`, 故 `<= 0` 与 `== 0` **在所有可达输入下逐位等价** (equivalent mutant)。
不存在能区分二者的测试; 保留 `<=` 只是纵深防御。**不许为了让它变红去造断言。**

全量: **1149 passed** (= 修复轮开工基线 1131 + 本轮新增 8 + 并发 agent 的 Task 3 新增 10)。

### 已知限制 (本轮**不**改代码, 只记 —— Task 10 收编)

1. **`doc_seats` 是绝对常量, 不随 `top_k` 缩放。** 独立审查方实测: `top_k=3` 时得 3 张卡片 +
   5 条 doc, **doc 条数反超卡片**。而答题侧双臂只在 `top_k=15` 下量 ⇒ 双臂数字对
   "小 top_k 下 doc 占比失衡" 这个方向**看不见**。生产联邦只用 15 (study) 与 8 (both),
   故不影响本单元结论, 但任何人把 `top_k` 调小时该结论立刻失效。
2. **不许"顺手"把 seats 改成 `min(doc_seats, top_k)` 来修上一条。** 那会违反 spec §4.2
   逐字规定的"both 判库下 doc 席位不缩" (缩了则 both 题与 study 题的 doc 召回不可比)。
   唯一守卫是 `test_both_mode_halves_cards_but_never_shrinks_doc_seats` —— 它刻意取
   `N=10 > top_k=8`, 因为 `N <= top_k` 时 `min()` 不咬人, 那样的测试守不住 (变异 MIN 即为此设)。

---

## Task 2 修复轮 (2026-08-12) — 独立审查 REQUEST-CHANGES 的收口

审查方 (不同 subagent_type / 不同 session) 从**代码行**出发设计 17 条变异, **10 条存活**;
实现方上一轮从**断言**出发设计 9 条, 两套几乎不重叠 —— 两个搜索方向不等价, 这是本轮
最贵的一条方法论结论。审查方判定**实现逻辑一处不用改**, 要动的是一条错注释 + 测试侧断言。

修复轮基线: **1144 passed / 0 failed** (口径 `--ignore=scripts/tests/test_run_eval_doc_channel.py`
—— 该文件是并发 agent 的 Task 3 in-flight 产物, 不属本 task)。

### A. 两条独立实测探针 (Global Constraint 3: 声称必须可复跑)

复跑脚本已落 `scripts/` 之外的临时目录, 逐字命令如下 (零 LLM, 探针 2 打 1 次 embedding):

```bash
./.venv/bin/python -c "
from server.config import settings
from server.rag import RAGEngine
common = dict(chroma_dir=settings.chroma_dir, embedding_model=settings.embedding_model,
              structured_lookup_enabled=False, hybrid_enabled=settings.hybrid_enabled,
              hybrid_fusion=settings.hybrid_fusion, hybrid_alpha=settings.hybrid_alpha,
              hybrid_pool=settings.hybrid_pool,
              prompt_guardrail_enabled=settings.prompt_guardrail_enabled)
# 探针 1: collection 名指错 → 响亮失败?
try:
    RAGEngine(kb_root=settings.study_kb_root, collection_name='study_st01_docs_TYPO',
              top_k=5, **common)
except Exception as e:
    print('RAISED', type(e).__module__ + '.' + type(e).__name__ + ':', e)
# 探针 2: 同一 collection 换 kb_root, 召回是否逐位相同
a = RAGEngine(kb_root=settings.study_kb_root,
              collection_name=settings.study_docs_collection_name, top_k=5, **common)
b = RAGEngine(kb_root=settings.kb_root,
              collection_name=settings.study_docs_collection_name, top_k=5, **common)
ra, rb = a.retrieve('評価スケジュール', top_k=5), b.retrieve('評価スケジュール', top_k=5)
print('chunks =', a.collection.count())
print('chunk_id 逐位相同:', [c.chunk_id for c in ra] == [c.chunk_id for c in rb])
print('source   逐位相同:', [c.source for c in ra] == [c.source for c in rb])
print('source 样例:', [c.source for c in ra][:3])"
```

实测输出 (2026-08-12):

```
RAISED chromadb.errors.NotFoundError: Collection [study_st01_docs_TYPO] does not exist
chunks = 114
chunk_id 逐位相同: True
source   逐位相同: True
source 样例: ['st01__doc01__s7_6.md', 'st01__doc01__s8_2__part01.md', 'st01__doc01__s8_2__part02.md']
```

**探针 1 — 响亮失败纪律属实。** `main.py` 的注释此前**只是声称**了这条纪律, 没有任何地方
证明过。抛点是 `rag.py:93` 的 `client.get_collection` (**不是** `get_or_create`) ⇒ 开关开着
而库不在时启动即崩, 不会静默退化成纯卡片。
⚠ **刻意不为它补测试**: 生产 lifespan 的测试把 `RAGEngine` 整个 stub 掉了, FakeEngine 永远
不会抛; 让 stub 抛再断"启动失败", 断的是 stub 自己的行为 —— 构造性装饰断言。

**探针 2 — `kb_root` 对本引擎的 source 零影响。** 审查方的论断「`kb_root` 决定
`RetrievedChunk.source` ⇒ 是量尺参数」作为**一般性论断成立, 对本引擎不成立**:
`rag.py:578-581` 是 `Path(source_raw).relative_to(self.kb_root)` 包在
`try/except (ValueError, TypeError)` 里; 而 study/docs 两库的 `source` metadata 是**裸文件名**
(`st01__doc01__s10_1.md`), `relative_to` 恒抛 `ValueError` 被同处 except 接住回落原值。
故同一 docs collection 下 `kb_root` 指 `data/study/st01/cards` 与指 `knowledge_base/`,
召回的 `source` 与 `chunk_id` 逐位相同。
⇒ `main.py:139-150` 的注释按此重写。写成"kb_root 是量尺参数"会让下一个人以为 **U1 的上界
数字依赖 kb_root 取值 —— 它不依赖**。

### B. 修复清单

| # | 改了什么 | 落点 |
|---|---|---|
| 1 | 钉住两台引擎的**位置**参数 (新测试 `test_engine_positions_are_not_swapped`; FakeEngine 加 `self.kwargs`) | 测试 |
| 2 | **同源比对**断言替代逐参数抄写 (新测试 `test_docs_engine_shares_every_lever_with_the_cards_engine`) | 测试 |
| 3 | `kb_root` 注释按探针 2 重写 (区分 CDISC 侧成立 / study·docs 侧不成立) | `main.py:139-150` |
| 4 | 告警的**两条反方向**断言 (仿参照文件 `:186-188` / `:191-193`) | 测试 |
| 5 | `Settings()` 默认值断言 (体例仿 `test_run_eval_flags.py::test_settings_study_lookup_defaults`) | 测试 |
| 6 | `FakeCollection.count()` 0 → **137** (不寻常值) + 断 `chunks=` 字段 | 测试 |
| 7 | stub `StudyLookup.from_paths` (catalog 不进 git ⇒ 裸检出可跑) | 测试 |
| 8 | `top_k=s.study_docs_seats` 惰性注释 (**不加断言**, 见下) | `main.py:155-157` |

第 8 条为何不加断言: `self.top_k` 全文只被 `rag.py:263` 的 `k = top_k or self.top_k` 读, 而
`StudyCorpusEngine.retrieve` 恒显式传正整数 ⇒ `or` 右支在生产路径上永不取值。为它加断言
= 断一个不可观测的值, 构造性装饰断言。改成注释, 免得下一个人以为改它能调席位。

第 7 条的效果实测: 把 catalog/aliases 指向不存在的文件, 修前本文件 **3 failed**
(FileNotFoundError), 修后与参照文件一起 **21 passed**:

```bash
cd /Users/bojiangzhang/MyProject/sdtm-pedia/sdtm-rag && \
SDTM_RAG_STUDY_CATALOG_PATH=/nope/missing.json SDTM_RAG_STUDY_ALIASES_PATH=/nope/missing.yml \
./.venv/bin/python -m pytest scripts/tests/test_main_study_docs_wiring.py \
  scripts/tests/test_main_study_lookup_wiring.py -p no:warnings   # → 21 passed
```

### C. 变异复验 (M10-M23)

口径变更 (吸取 Task 1 实现方报的坑): **不再用整文件快照**, 改成对**当前源码**做文本替换并
断言锚点恰好命中一次 —— 快照会随源码演进悄悄变成 no-op, 写错的变异以全绿身份显示, 被
误读成"装饰断言"。跑批脚本每条: 替换 → 全量 pytest → 无条件改回。

| # | 变异 | 审查方编号 | 实测 failed | 变红的测试 |
|---|---|---|---|---|
| 0 | 无 (基线) | — | **0 / 1144 passed** | — |
| M10 | 两台引擎位置写反 `(rag_docs, rag_study)` | 09 | **1 / 1143** | `test_engine_positions_are_not_swapped` |
| M11 | docs 引擎 `kb_root` 指到 CDISC 根 | 03 | **1 / 1143** | `test_docs_engine_shares_every_lever_...` |
| M12 | docs 引擎 `top_k` 用全局 15 | 05 | **1 / 1143** | 同上 |
| M13 | docs 引擎误开 S1 | 06 | **1 / 1143** | 同上 |
| M14 | docs 引擎关掉 hybrid | 07 | **1 / 1143** | 同上 |
| M15 | docs 引擎关掉答题护栏 | 08 | **1 / 1143** | 同上 |
| M16 | docs 引擎换 embedding 模型 | 14 | **1 / 1143** | 同上 |
| M17 | docs 引擎换 chroma 目录 | 15 | **1 / 1143** | 同上 |
| M18 | 日志丢掉 `chunks` 字段 | 11 | **1 / 1143** | `test_seats_and_collection_are_reported_in_the_ready_log` |
| M19 | 告警丢掉 `and not federation_enabled` (恒报警) | 13 | **1 / 1143** | `test_no_ignored_warning_when_federation_is_on` |
| M20 | 告警并进 `study_lookup` 的 elif 链 (被前一支吃掉) | 17 | **1 / 1143** | `test_docs_enabled_without_federation_logs_ignored` |
| M21 | `study_docs_enabled` 默认偷偷翻 `True` | — | **3 / 1141** | `test_settings_study_docs_defaults` + 参照文件 2 条 |
| M22 | **cards** 引擎降到 seats 席 (抢席, 反方向) | 双方均未覆盖 | **1 / 1143** | `test_docs_engine_shares_every_lever_...` |
| M23 | 两台引擎 `top_k` **对调** (双点) | 双方均未覆盖 | ⚠ **0 / 1144 全绿** → 补断言后 **1 / 1143** | 同上 |

上一轮四条复验 (断言集改动后仍红): `M1r` 只建不包 **3 failed** · `M2r` 席位写死常量
**1 failed** · `M3r` 告警事件名打错 **1 failed** · (M22 见上表)。

**M23 是本轮唯一新发现的存活变异, 审查方 17 条与实现方前 12 条都没覆盖。**
同源比对只断"两者不同", 不断"谁大" ⇒ 把 cards 与 docs 的 `top_k` **对调**后差集一字不变,
全量 **1144 全绿**。而那正是"加席不抢席"在**接线层**的反面: 真 cards 降成 5 席去查 959 张卡,
docs 拿 15 席去查 114 条章节。补的断言把方向单独钉死:
`assert cards["top_k"] == Settings().top_k and docs["top_k"] == 7`。
补后 M22 / M23 / M12 三条 top_k 变异**全部变红**。

方法论账: 单点变异全红 ≠ 断言集完备 —— **对调型 (双点、差集不变) 变异是同源比对类断言的
系统性盲区**, 下一个用同源比对的单元必须同时钉方向。

### D. 修复轮复原核验

- 跑批脚本无条件 `finally` 改回; 收尾 `git diff` 只剩本轮**有意**的改动 (注释 + 测试)。
- 全量 (排除并发 in-flight 文件) → **1144 passed / 0 failed**。
- 本文件所在 task 的三个文件对 catalog 1417 个值 **零命中** (红线复扫)。
