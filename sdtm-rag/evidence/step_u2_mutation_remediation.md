# U2 — 抽检方 B 放行条件的实现 + 生产开关翻转

> 状态: **已完成** (2026-08-13) — 21/21 变异 KILLED, 全量 1181 → **1189 passed, 0 failed**
> 输入: 抽检方 B 的独立变异复跑 (57 条: 33 KILLED / 24 SURVIVED, 判定「有条件 PASS」)
> 本文件不重新论证缺口, 只记录**做了什么**与**每条新断言的变异复验**。

---

## 0. 变异纪律 (三条硬约束的执行形态)

| 约束 | 执行形态 |
|------|----------|
| 变异只在私有子目录 | harness + spec + 结果 JSON 全在 session scratchpad (`u2mut/`), **不进 git**; 仓库里只落本文件 |
| 锚点恰好命中一次 | 每条变异先 `text.count(old)`, `!= 1` 即 ANCHOR_ERROR 跳过并复原。**27 个锚点全部 1 hit** |
| 收尾 sha256 复原 | 每条变异 `try/finally` 写回原文并 `assert sha256(after) == sha256(before)`; 21 条全过 |

变异靶文件里 `server/main.py` 与 `eval/run_eval.py` **本单元一个字都没改** —— 它们只被变异过再复原,
收尾 sha256 与开工前逐位相同 (`e4fbace…` / `45240ec…`), 可用 `git status` 交叉核对 (两者不在 M 列表里)。

每条变异都跑**全量套件** (不是子集), 单条约 35s。基线 = 1189 passed / 0 failed。

---

## 1. `eval/judge_controls.py` 的 9 条装饰断言 (最重)

69 行文件存在的全部意义是让一个数字可解读, 而「用的是哪把尺子 / 抽了几题 / 均值怎么算」
三件事此前**零断言** —— 11 条测试里 7 条 main() 测试全部 `monkeypatch(jc, "check_fact_recall_judge")`。

新增 5 条测试 + 强化 3 条既有测试的断言:

| ID | 变异 (锚点 → 改成) | 结果 | 杀手 |
|----|--------------------|------|------|
| **X2** | `from eval.run_eval import … check_fact_recall_judge` → 删掉 import, 模块内自带一个假 judge | KILLED 1188/1 | `test_the_judged_ruler_is_the_one_run_eval_uses` |
| **I** | `--judge-model` default `DEFAULT_JUDGE_MODEL` → `"vendor/some-other-model"` | KILLED 1188/1 | `test_default_judge_model_is_run_evals_default` |
| **K** | `avg = … if ok else 0.0` → `else 1.0` | KILLED 1188/1 | `test_total_parse_failure_reads_as_zero_never_as_a_perfect_score` |
| **J** | `--n` default `6` → `3` | KILLED 1188/1 | `test_sample_size_defaults_to_six_and_follows_the_flag` |
| **U1** | `sample_ids(list(qs), a.n)` → `sample_ids(list(qs), 3)` | KILLED 1188/1 | 同上 |
| **U6a** | 逐题回执 → 写死 `recall=1.0 parse_ok=True` | KILLED 1188/1 | `test_screen_receipt_reports_the_real_numbers` |
| **U6b** | 汇总回执 → 写死 `parse_ok={len(rows)} avg=1.0000` | KILLED 1188/1 | 同上 |
| **L** | `if n <= 0 or n > len(ids)` → `if n < 0 …` | KILLED 1188/1 | `test_sample_ids_rejects_impossible_n` (补的下界断言) |
| **N** | judge 第三槽 `q["expected_facts"]` → `[]` | KILLED 1188/1 | `test_main_puts_question_and_answer_in_their_own_slots` (补的 `c["facts"] == _FACTS[qid]`) |
| **S1** | `rows.append({"id": qid, …})` → `{"id": "q01", …}` | KILLED 1188/1 | `test_main_keeps_unparseable_verdicts_out_of_the_average` (补的 id 列断言) |

设计要点:

- **X2 不取 `harness` fixture** —— 取了就是在被打桩后的模块上断身份, 什么也证明不了。
- **I / J** 都断到**来源**而不是常量 (`run_eval.DEFAULT_JUDGE_MODEL` / `sample_ids(list(_FACTS), 6)`),
  这样 run_eval 换默认 judge 时对照跟着走, 而"脱钩"仍然红。
- **U6** 让三题取三种不同结局 (0.5 命中 / 解析失败 / 满分), 使"写死常量"与"如实转述"逐字可分;
  均值 0.7500 = 1.5/2 一并把 K/B5 的口径 (不可解析不进均值) 再钉一次。

## 2. 第五条对调型: 规则文本两类来源的**定义**互换

`server/study_corpus.py` 的 `_DOC_CORPUS_RULES` 是 spec §4.2 的交付物本身 (Task 8 双臂差值的解释
完全建立在「答题方分得清来源」上)。原断言是**成员形状** (`in`), 对**配对**结构上不可见。

改成断**名字与其定义相连的整句**:

| ID | 变异 | 结果 | 杀手 |
|----|------|------|------|
| **P1** | 卡片与章節的**定义互换** (卡片说成「手順・計画文書の節」, 章節说成「入力項目の定義」) | KILLED 1188/1 | `test_system_prompt_names_both_source_kinds_and_keeps_section_numbers` |
| **X1** | 節番号规则的主语从章節改挂到卡片上 | KILLED 1188/1 | 同上 |

## 3. 共错型: 日志 / 回执读**兄弟引擎**的 count

根因是 fixture —— 两台 FakeEngine 的 `count()` 同为 137, 于是"读错引擎"逐位不可分。
改成按 `collection_name` 分派: cards 959 / docs 137。

| ID | 变异 | 结果 | 杀手 |
|----|------|------|------|
| **C** | `main.py` ready 日志 `chunks=rag_docs.…count()` → `rag_study.…count()` | KILLED 1188/1 | `test_seats_and_collection_are_reported_in_the_ready_log` |
| **LOW** | `run_eval.py` 屏幕回执 `docs_rag.…count()` → `study_rag.…count()` | KILLED 1188/1 | `test_docs_channel_receipt_reports_the_docs_collection_not_its_sibling` (新增) |

抽检方 B 把 eval 侧标为 LOW; 一并做了 —— 同一种共错, fixture 已经改好, 增量只有一条断言。

## 4. lever 取值: prod 侧此前一条断言都没有

生产侧全是 cards↔docs **自比**, 跨路径又只比 6 个 STRUCTURAL 键 ⇒ 两台一起改照绿。
补 `settings.*` 取值断言 + 给 `embedding_model` / `chroma_dir` 补方向钉。

| ID | 变异 | 结果 | 杀手 |
|----|------|------|------|
| **Q** | 生产两台 study 引擎 `hybrid_alpha` 一起 → `0.99` | KILLED 1188/1 | `test_prod_docs_engine_carries_every_lever_its_cards_engine_carries` |
| **S2** | **四台** study 引擎 `embedding_model` 一起 → `"bogus-embed"` | KILLED 1186/3 | prod + eval 两条同源测试 + `test_docs_engine_shares_every_lever_with_the_cards_engine` |
| **S2b** | **四台** study 引擎 `chroma_dir` 一起指到别处 | KILLED 1185/4 | 同上 + `test_validate_study_endpoint::test_create_app_boots_through_lifespan` |

取值断言对着**本次 boot 真正用的那个 `Settings`** (`prod_boot.settings`), 不对着模块级单例再抄一份常量
—— 断的是"生产把 settings 传下去了", 故 `.env` 覆盖任一 lever 时这条跟着走而不会伪红。

## 5. `or` 回落型: 空臂实验的正确性直接依赖它

per-call **负数**有闸有断言, **0 没有** = 单边守卫; 而 0 正是空臂那一臂唯一的表达方式。

| ID | 变异 | 结果 | 杀手 |
|----|------|------|------|
| **E** | `study_corpus.py` `seats = self.doc_seats if doc_seats is None else doc_seats` → `doc_seats or self.doc_seats` | KILLED 1188/1 | `test_per_call_doc_seats_zero_turns_the_channel_off_for_that_call` (新增) |
| **F** | `run_eval.py` `args.doc_seats if … is not None else …` → `args.doc_seats or …` | KILLED 1188/1 | `test_doc_seats_zero_is_honoured_not_silently_defaulted` (新增) |

F 的测试把 `settings.study_docs_seats` monkeypatch 成 9 (≠ 出厂 8), 才能把"回落"与"恰好等于默认"分开。

## 6. 环境隔离: `test_settings_study_docs_defaults` 读的是环境不只是代码默认

`config.py:17` import 期 `load_dotenv`, `Settings` 用 `env_prefix="SDTM_RAG_"` ⇒ 该测试量的是**本机配置**。
修法: 断言前 `monkeypatch.delenv` 掉全部 `SDTM_RAG_*`, 再构造 `Settings()`。

| 检查 | 命令 | 结果 |
|------|------|------|
| **ENV 变异** (去掉 delenv + 敌意环境) | harness, env=`SDTM_RAG_STUDY_DOCS_SEATS=5 SDTM_RAG_STUDY_DOCS_ENABLED=false` | KILLED 1188/1 (`test_settings_study_docs_defaults`) — 原缺陷复现 |
| **A 对照** (保留 delenv, 同一敌意环境) | 下方命令 A | **9 passed, 0 failed** — 修好了 |

```bash
cd sdtm-rag
# A: 敌意环境 + 现有隔离 ⇒ 应全绿
SDTM_RAG_STUDY_DOCS_SEATS=5 SDTM_RAG_STUDY_DOCS_ENABLED=false \
  ./.venv/bin/python -m pytest -q scripts/tests/test_main_study_docs_wiring.py
```

同类的 `test_docs_engine_parity.py` 的 `assert prod["top_k"] != settings.top_k` **已删除**
(方向由「cards 拿全局 top_k、docs 拿席位」这条同源比对承担)。删除前后对照:

```bash
SDTM_RAG_TOP_K=7 ./.venv/bin/python -m pytest -q scripts/tests/test_docs_engine_parity.py
```

| 树 | 结果 |
|----|------|
| 把 `!= settings.top_k` 加回去 | **2 failed** (`…identical_structural_kwargs` + `…prod_docs_engine_carries_every_lever…`) |
| 当前树 (已删) | **1 failed** (只剩下面那条残余) |

### ⚠ 已知残余 (本单元**未**修, 新发现)

`SDTM_RAG_TOP_K` 被设成**恰好等于测试用的席位数** (7 或 5) 时, 两条同源测试的差集断言
`{k for k in docs if cards[k] != docs[k]} == {"collection_name", "top_k"}` 会伪红 —— 因为 cards 与 docs
的 `top_k` 撞成同一个值, 差集塌成 `{"collection_name"}`。

与已删的那条不同, **这条差集断言本身是正确的结构性主张**, 伪红来自 fixture 选的席位常量 (7/5) 可能
与环境撞值。修它要改动 fixture 的席位常量体系 (多处 `--doc-seats 7` / `docs["top_k"] == 7` 联动),
超出抽检方 B 点名的范围, 故**留给下一轮裁定**。复跑命令即上面那条。

## 7. 生产开关翻转 (用户 2026-08-13 裁定)

`server/config.py`: `study_docs_enabled: bool = False` → **`True`** (`study_docs_seats` 保持 8)。

依据 (逐字照抄裁定口径, 不得美化):

- 收益侧: doc 侧答题 0.0333 → 0.9517, doc 侧检索 0 → 1.0。
- 代价侧: 卡片侧代价**未被建立** —— ON-ON 对照显示驱动条款 3 的 `q23r` 不复现, ON 臂自身噪声
  +2.78pt 已达声称效应量, 四种 OFF×ON 组合跨 −4.17 到 +0.00pt。
- ⇒ **spec §6 自毁条款 3 是触发状态, 由用户 2026-08-13 裁定豁免后翻转。**
  不是「未触发」, 也不是「验收通过」。回退杠杆: `SDTM_RAG_STUDY_DOCS_ENABLED=false`。

这句话同时写进 `config.py` 的字段注释与 `test_settings_study_docs_defaults` 的 docstring。

| ID | 变异 | 结果 | 杀手 |
|----|------|------|------|
| **FLIP** | 默认翻回 `False` | KILLED 1188/1 | `test_settings_study_docs_defaults` |

### 翻转的连带修改 (非可选)

`test_main_study_lookup_wiring.py` 两条测试解包 `cdisc, study = boot(s).engines` —— 默认翻 True 后
lifespan 多造一台 docs 引擎, 两条 ValueError。修法是**把无关开关显式钉住**
(`Settings(study_lookup_enabled=…, study_docs_enabled=False)`), 因为这两条量的是 S2 挂在哪台引擎上,
二台引擎的世界最直白。**没有**改它们的任何断言。

## 8. 死代码删除 (按抽检方 B: 删除, 不补断言)

**(a) `judge_controls.py` 的撞位回落分支** —— 原 `if len(idx) != n: idx = list(range(n))`。
不可达的证明可复跑:

```bash
cd sdtm-rag && ./.venv/bin/python -c "
bad=[(L,n) for L in range(1,300) for n in range(1,L+1) if len({(k*L)//(n+1) for k in range(1,n+1)})!=n]
print('collisions:', len(bad), bad[:5])"
# → collisions: 0 []
```

闭式论证 (写进代码注释, 比枚举更强): 闸已保证 `n <= L`; `n == L` 时 `(k*L)//(L+1) = k-1` (k=1..L)
两两不同, `n < L` 时步长更大 ⇒ 恒得 n 个位置。

**(b) `study_corpus.py` 的 `CARD_FILE_TYPE`** —— 全仓无引用, 删除。原地留一行注释说明卡片侧
**故意**没有对应常量 (分组用反选 `!= DOC_FILE_TYPE`; 改成正选会让未知 file_type 的 chunk 静默消失),
防止有人把它加回来。

---

## 9. 总账

```bash
cd sdtm-rag && ./.venv/bin/python -m pytest -q
# 本机 pytest 不打最终汇总行, 计数走 junit-xml:
#   ./.venv/bin/python -m pytest -q --junit-xml=/tmp/j.xml && \
#   python -c "import xml.etree.ElementTree as ET;t=ET.parse('/tmp/j.xml').getroot()[0];print(t.attrib)"
```

| 项 | 值 |
|----|----|
| 全量 | 1181 (开工) → **1189 passed, 0 failed, 0 errors** |
| 新增测试函数 | 8 条 (judge_controls 5 / study_corpus 1 / run_eval_doc_channel 2) |
| 强化既有测试断言 | 5 条 (L / N / S1 / P1+X1 / C, 及 parity 的 Q+S2 方向钉) |
| 变异复验 | **21/21 KILLED**, 全部由本轮新增/强化的那条断言点名 |
| ruff | 5 findings, 与 HEAD **逐条相同** (全部先于本单元存在), 零新增 |
| 生产代码净改动 | `config.py` 1 个默认值 + `judge_controls.py` 删 2 行 + `study_corpus.py` 删 1 行 |
| equivalent mutant | **0 条** (本轮 21 条无一存活, 故无需单独归类) |
