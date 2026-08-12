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
