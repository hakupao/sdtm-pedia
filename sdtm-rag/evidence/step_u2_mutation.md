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

⇒ **8 条断言全部至少被一条变异证伪过, 无装饰断言残留。**

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
