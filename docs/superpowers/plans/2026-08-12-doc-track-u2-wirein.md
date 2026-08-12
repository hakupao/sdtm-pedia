# doc 轨 U2 接线 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 把 st01 的 114 个手順書章节 chunk (collection `study_st01_docs`) 接进检索侧, 并在 U1 已落盘的两把尺子上量出接线损耗与答题侧席位挤占。

**Architecture:** 新建组合器 `StudyCorpusEngine` 包住既有 study cards 引擎 + 一台新的 docs 引擎, 对 `FederatedEngine` 保持同一鸭子接口 (`retrieve` / `format_context` / `system_prompt` / `build_messages`)。cards 的 15 席原样不动, doc **追加** N 席 (加席不抢席), 不做跨库分数排序。router 的 study 语料描述改准并重跑路由闸。

**Tech Stack:** Python 3.12 · FastAPI · chromadb (PersistentClient) · pytest (`testpaths = scripts/tests`, `addopts = -ra -q`) · litellm router (Bedrock jp. profile)

## Global Constraints

以下每条来自 spec `docs/superpowers/specs/2026-08-12-doc-track-u2-wirein-design.md`, 逐字生效于**每个** task:

1. **数据红线**: 进 git 的任何文件**零真名零正文** —— 不含 catalog 的 item OID / label 值、PDF 真名、≥12 字的语料 CJK 串。题集、语料、逐题明细只写 `data/study/`(gitignored)。
2. **自毁条款不许改阈值** (spec §6 六条)。触发 = 当场停下, 写 `evidence/failures/`, 上报用户, **不许调参把数字调上去再报**。
3. **写「实测」必附可复跑命令** (U1 §8 硬约束 5)。没跑过的不许用实测语气写。
4. **必须开 `--judge`** 跑任何答题侧数字 (U1 §8 硬约束 2)。裸子串对 12–82 字整句 fact 恒接近零, 与检索质量无关。
5. **两把尺子都要报** (U1 §8 硬约束 1): N=15 生产档 + N=5 判别力档。
6. **失分不得默认归因到检索质量** (U1 §8 硬约束 3): 先分清「判库损耗」「PRT 有而 EDC 结构上没有」「检索没找到」。
7. **新加的取证输出当场补断言** (硬规矩 18) 并做**物理变异测试**证明它会红。
8. **关键数字用非自洽写法复算** (硬规矩 17b)。
9. 引用 U1 上界时必须写「100% **触发了**自毁条款, **用户豁免**」, 不得写成「一次过」。
10. 基线: `1119 passed` · `sdtm_kb_v1` 4329 / `study_st01` 959 / `study_st01_docs` 114 · 卡片侧 87.50% 逐题 Δ0 vs `runs/v2_baseline_s2on.json` · 路由 178/181 fatal=0。
11. **变异跑批必须用私有子目录 + 复原核验** (2026-08-12 Task 3 事故立): 并发 agent 覆写了
    共享 scratchpad 根目录的脚本, 变异跑批被超时 SIGTERM, `finally` 未执行, **`eval/run_eval.py`
    被留在变异态**。实现方靠快照 diff 发现并复原, controller 独立复核了 diff 确认无残留。
    ⇒ 变异脚本一律放 `<scratchpad>/<task 名>/` 私有子目录; 每轮带子超时; 收尾必须打印
    `RESTORED True` 之类的**可核验**复原证据。被留在变异态的生产文件会静默污染其后全部数字。
12. **两个搜索方向都要做** (Task 1 审查方实证): ①「从断言出发找能杀死它的变异」——
    上界 = 已有断言集合, **结构上发现不了无人守的代码行**; ②「**从代码行出发问这行改坏了谁会红**」。
    只做① 的自证式变异测试会得到"全部断言都被证伪过"的真结论, 同时漏掉整块零覆盖代码
    (Task 3 实测: 删光 27 行装配块, 计划的 4 条断言一条不红)。

---

## File Structure

| 文件 | 职责 |
|---|---|
| `server/study_corpus.py` (**新**) | `StudyCorpusEngine` 组合器 (cards + docs), 唯一新增运行时组件 |
| `server/config.py` (改) | 三个新 setting: `study_docs_enabled` / `study_docs_collection_name` / `study_docs_seats` |
| `server/main.py` (改) | lifespan 里构造 docs 引擎并包成 `StudyCorpusEngine`; 响亮失败与告警留声 |
| `server/federation.py` (改) | `_ROUTER_SYSTEM` 中 study 的语料描述改准 (只改事实描述, 不动规则优先级) |
| `eval/run_eval.py` (改) | 新 flag `--study-docs` / `--doc-seats` / `--corpus` |
| `eval/judge_controls.py` (**新**) | 阳性/阴性对照 harness (U1 一次性跑的那两条, 变成可复跑脚本) |
| `scripts/tests/test_study_corpus.py` (**新**) | 组合器单测 (stub 引擎, 不碰 chroma) |
| `scripts/tests/test_main_study_docs_wiring.py` (**新**) | 生产 lifespan 接线锁 |
| `scripts/tests/test_run_eval_doc_channel.py` (**新**) | eval flag 接线锁 |
| `scripts/tests/test_judge_controls.py` (**新**) | 对照 harness 单测 |
| `evidence/checkpoints/doc_track_u2_wirein.md` (**新**) | 收口证据 |

---

### Task 1: `StudyCorpusEngine` 组合器

**Files:**
- Create: `server/study_corpus.py`
- Test: `scripts/tests/test_study_corpus.py`

**Interfaces:**
- Consumes: `server.rag.RetrievedChunk` (字段 `chunk_id / source / domain / file_type / section / similarity / text / rerank_score / via_lookup / corpus`)
- Produces: `StudyCorpusEngine(cards, docs, *, doc_seats: int)`, 方法 `retrieve(question, *, top_k=None, doc_seats=None) -> list[RetrievedChunk]` · `format_context(chunks) -> str` · 属性 `system_prompt: str` · 常量 `DOC_FILE_TYPE = "protocol_section"` / `CARD_FILE_TYPE = "field_card"`

> **修订 (2026-08-12, Task 1 审查后)**: 原 Interfaces 还列了 `build_messages`。独立审查方实证
> 它在生产路径上**不可达** (联邦答题走 `FederatedEngine.build_messages` → `cdisc.build_messages`
> + `_system_for`, 后者只读 `study.system_prompt`), 且删掉整个方法后 8 条测试全绿 = 零覆盖。
> **裁定: 删掉**, 不补钉子 —— 留着是"零测试守护的死代码", 删了则未来真有人调它会
> AttributeError 响亮失败。
>
> **补入 (spec §7 的 `both` 模式席位, 原计划漏分配)**: Task 1 需补一条测试断言
> `retrieve(q, top_k=8)` (= `ceil(15/2)`, both 档 cards 拿到的值) 下 **docs 仍拿满 N 席不缩**。
> spec §4.2 逐字禁止在 both 下缩 doc 席位; 这条测试是该禁令唯一的守卫。

- [ ] **Step 1: 写失败测试 (核心行为四条)**

```python
"""U2: StudyCorpusEngine — cards + 手順書章节 的组合器 (spec §4.1-4.2)。

引擎侧全用 stub (duck-typed), 不碰 chroma / 不发 embedding。
"""
from server.rag import RetrievedChunk
from server.study_corpus import StudyCorpusEngine


def _chunk(cid, file_type, sim=0.5):
    return RetrievedChunk(chunk_id=cid, source=f"{cid}.md", domain=None,
                          file_type=file_type, section=None, similarity=sim, text=f"t-{cid}")


class _Stub:
    def __init__(self, name, file_type, n=20):
        self.name, self.system_prompt = name, f"SYS-{name}"
        self._chunks = [_chunk(f"{name}-{i}", file_type, 0.9 - i * 0.01) for i in range(n)]
        self.calls = []

    def retrieve(self, q, *, top_k=None, **kw):
        self.calls.append(top_k)
        return self._chunks[: (top_k or 15)]

    def format_context(self, chunks):
        return f"CTX-{self.name}({len(chunks)})"

    def build_messages(self, q, ctx, history=None):
        return [{"role": "system", "content": self.system_prompt},
                {"role": "user", "content": f"{ctx}\n{q}"}]


def _engine(doc_seats=5, n_cards=20, n_docs=20):
    cards = _Stub("card", "field_card", n_cards)
    docs = _Stub("doc", "protocol_section", n_docs)
    return StudyCorpusEngine(cards, docs, doc_seats=doc_seats), cards, docs


def test_cards_keep_full_top_k_and_docs_are_appended():
    """doc 是加席不是抢席: cards 拿满 top_k, doc 追加在后, 总长 = top_k + seats。"""
    eng, cards, docs = _engine(doc_seats=5)
    got = eng.retrieve("q", top_k=15)
    assert cards.calls == [15]          # cards 的 top_k 原样传下去, 一席不减
    assert docs.calls == [5]
    assert len(got) == 20
    assert [c.file_type for c in got[:15]] == ["field_card"] * 15
    assert [c.file_type for c in got[15:]] == ["protocol_section"] * 5


def test_doc_seats_zero_means_channel_off():
    """seats=0 时 docs 引擎一次都不该被打 (零开销回落, 与通道 OFF 逐位相同)。"""
    eng, cards, docs = _engine(doc_seats=0)
    got = eng.retrieve("q", top_k=15)
    assert docs.calls == []
    assert len(got) == 15


def test_per_call_doc_seats_overrides_default():
    eng, _, docs = _engine(doc_seats=5)
    eng.retrieve("q", top_k=15, doc_seats=8)
    assert docs.calls == [8]


def test_duplicate_chunk_ids_are_deduped_cards_win():
    cards = _Stub("x", "field_card", 3)
    docs = _Stub("x", "protocol_section", 3)   # 同名 chunk_id
    eng = StudyCorpusEngine(cards, docs, doc_seats=3)
    got = eng.retrieve("q", top_k=3)
    assert [c.chunk_id for c in got] == ["x-0", "x-1", "x-2"]
    assert all(c.file_type == "field_card" for c in got)


def test_format_context_groups_the_two_source_kinds():
    eng, _, _ = _engine(doc_seats=2)
    ctx = eng.format_context(eng.retrieve("q", top_k=3))
    assert "CTX-card(3)" in ctx and "CTX-doc(2)" in ctx
    assert ctx.index("CTX-card(3)") < ctx.index("CTX-doc(2)")


def test_format_context_omits_absent_group():
    """只有卡片时不许打出空的手順書小节 (空标题会让答题方以为检索过而没找到)。"""
    eng, _, _ = _engine(doc_seats=0)
    ctx = eng.format_context(eng.retrieve("q", top_k=3))
    assert "CTX-doc" not in ctx


def test_system_prompt_comes_from_cards_engine_never_docs():
    """docs 引擎的 kb_root 指的是 cards/ ⇒ 它的 system_prompt 描述的是卡片库, 用了就是错的。"""
    eng, _, docs = _engine()
    docs.system_prompt = "POISON-must-never-be-read"
    assert "POISON" not in eng.system_prompt
    assert "SYS-card" in eng.system_prompt


def test_negative_doc_seats_fails_loud():
    import pytest
    with pytest.raises(ValueError, match="doc_seats"):
        _engine(doc_seats=-1)
```

- [ ] **Step 2: 跑测试确认失败**

Run: `cd sdtm-rag && ./.venv/bin/python -m pytest scripts/tests/test_study_corpus.py -p no:warnings`
Expected: FAIL — `ModuleNotFoundError: No module named 'server.study_corpus'`

- [ ] **Step 3: 实现组合器**

```python
"""U2: study 侧语料组合器 — field cards + 手順書章节 chunk (spec 2026-08-12 §4)。

设计要点:
- **加席不抢席**: cards 引擎的 top_k 原样传下去, doc 另取 seats 席追加在后。C1 实测
  同库混装会让长篇章节在向量相似度上压过卡片 (87.50% → 78.1%, 6 题回归), 所以这里
  既不同库也不共享席位 —— cards 的召回在结构上不可能被 doc 改变。
- **不做跨库分数排序**: 沿用联邦既有纪律 (两库相似度分布不可比)。
- **system_prompt 只来自 cards 引擎**: docs 引擎的 kb_root 指向 cards/ (RAGEngine 硬要求
  ROUTING.md/INDEX.md, docs/ 没有), 它自己的 system_prompt 描述的是卡片库, 读了就是错的。
"""
from __future__ import annotations

CARD_FILE_TYPE = "field_card"
DOC_FILE_TYPE = "protocol_section"

_DOC_CORPUS_RULES = (
    "\n\n## Study document rules\n"
    "- 本研究のコンテキストには 2 種類ある: 【EDC 項目カード】 (入力項目の定義) と "
    "【手順書章節】 (本研究自身の手順・計画文書の節)。どちらに基づく記述かを必ず示すこと。\n"
    "- 手順書章節は節番号を伴う。引用時は節番号を保持すること。\n"
)


class StudyCorpusEngine:
    """cards 引擎 + docs 引擎の組合せ。FederatedEngine から見た鴨型は RAGEngine と同じ。"""

    def __init__(self, cards, docs, *, doc_seats: int):
        if doc_seats < 0:
            raise ValueError(f"doc_seats must be >= 0, got {doc_seats}")
        self.cards = cards
        self.docs = docs
        self.doc_seats = doc_seats

    @property
    def system_prompt(self) -> str:
        return self.cards.system_prompt + _DOC_CORPUS_RULES

    def retrieve(self, question: str, *, top_k=None, doc_seats=None, **kw):
        seats = self.doc_seats if doc_seats is None else doc_seats
        chunks = list(self.cards.retrieve(question, top_k=top_k))
        if seats <= 0:
            return chunks
        seen = {c.chunk_id for c in chunks}
        for d in self.docs.retrieve(question, top_k=seats):
            if d.chunk_id in seen:
                continue
            seen.add(d.chunk_id)
            chunks.append(d)
        return chunks

    def format_context(self, chunks) -> str:
        cards = [c for c in chunks if c.file_type != DOC_FILE_TYPE]
        docs = [c for c in chunks if c.file_type == DOC_FILE_TYPE]
        parts = []
        if cards:
            parts.append("## 【EDC 項目カード】\n" + self.cards.format_context(cards))
        if docs:
            parts.append("## 【手順書章節】\n" + self.docs.format_context(docs))
        return "\n\n".join(parts)

    def build_messages(self, question, context, history=None):
        msgs = self.cards.build_messages(question, context, history)
        msgs[0] = {"role": "system", "content": self.system_prompt}
        return msgs
```

- [ ] **Step 4: 跑测试确认通过**

Run: `cd sdtm-rag && ./.venv/bin/python -m pytest scripts/tests/test_study_corpus.py -p no:warnings`
Expected: PASS (8 passed)

- [ ] **Step 5: 物理变异测试 (Global Constraint 7)**

逐条做, 每条改完跑全量 `./.venv/bin/python -m pytest -p no:warnings`, 记录 failed 条数, **改回**:

| 变异 | 期望 |
|---|---|
| `retrieve` 里 `if seats <= 0: return chunks` 改成 `return chunks` (恒不取 doc) | ≥1 failed |
| `retrieve` 改成 `chunks = list(self.cards.retrieve(question, top_k=seats))` (抢席) | ≥1 failed |
| `system_prompt` 改成 `return self.docs.system_prompt + _DOC_CORPUS_RULES` | ≥1 failed |
| `format_context` 去掉 `if docs:` 守卫 (恒打空小节) | ≥1 failed |

四条都必须变红。**任何一条变异后全绿 = 该断言是装饰品, 当场补断言再复验。**
把四条的实测 failed 数写进 `evidence/step_u2_mutation.md`。

- [ ] **Step 6: 提交**

```bash
cd sdtm-rag && git add server/study_corpus.py scripts/tests/test_study_corpus.py ../evidence/step_u2_mutation.md 2>/dev/null; \
cd /Users/bojiangzhang/MyProject/sdtm-pedia && git add sdtm-rag/server/study_corpus.py sdtm-rag/scripts/tests/test_study_corpus.py sdtm-rag/evidence/step_u2_mutation.md && \
git commit -m "feat(doc-track): U2 Task 1 — StudyCorpusEngine 组合器 (加席不抢席) + 四条变异实证"
```

---

### Task 2: 生产接线 (config + main lifespan)

**Files:**
- Modify: `server/config.py` (在 `study_lookup_enabled` 一族后)
- Modify: `server/main.py:112-153` (federation 分支内)
- Test: `scripts/tests/test_main_study_docs_wiring.py`

**Interfaces:**
- Consumes: Task 1 的 `StudyCorpusEngine`
- Produces: `settings.study_docs_enabled: bool` / `settings.study_docs_collection_name: str` / `settings.study_docs_seats: int`; `app.state.federation.study` 在开关开时是 `StudyCorpusEngine` 实例

> **修订 (2026-08-12, Task 2 执行后 —— 两处计划缺陷, 逐字记账)**:
> 1. 下面 fixture 的 `structlog.configure(processors=[lambda _l, m, ed: ...])` **是错的**:
>    structlog processor 签名是 `(logger, method_name, event_dict)`, `m` 绑的是 `"info"`/
>    `"warning"` 这个**方法名**, 事件名在 `ed["event"]` ⇒ 照抄则后两条测试**在任何实现下
>    都不可能通过**。实际实现改用 `structlog.testing.capture_logs()` (顺带避免裸
>    `configure` 把处理器永久留在全局配置里泄漏给后续测试)。
> 2. Step 2 写的预期失败形态 (`Settings 没有 study_docs_enabled`) **不成立**:
>    pydantic-settings 对构造函数里的未知字段**静默忽略**, `Settings(study_docs_enabled=True)`
>    在字段还不存在时也不报错 ⇒ 失败以断言形式出现。**推论 (给 Task 9 抽检方)**: 任何
>    `boot(study_doc_seats=7)` 这类拼错的 override 都会静默走默认值而测试照绿, setting
>    名拼写值得专门验一次。

- [ ] **Step 1: 写失败测试**

```python
"""U2: 生产 lifespan 上的 doc 通道接线锁 (spec §4.5)。

接线漏在这里是完全静默的 —— 服务照常起, study 侧只是回到纯卡片。所以三个方向都要锁:
开着一定包成 StudyCorpusEngine / 关着一定不包 / 开着但联邦关着要留声。
仿 test_main_study_lookup_wiring.py 的 stub 编制, 不碰 chroma。
"""
from __future__ import annotations

import asyncio
from types import SimpleNamespace

import pytest
import structlog
from fastapi import FastAPI

from server import main as main_mod
from server.config import Settings
from server.study_corpus import StudyCorpusEngine


@pytest.fixture
def boot(monkeypatch):
    engines: list[dict] = []

    class FakeCollection:
        def count(self):
            return 0

    class FakeEngine:
        def __init__(self, **kwargs):
            engines.append(kwargs)
            self.collection = FakeCollection()
            self.system_prompt = "SYS"

        def _vi_section_map(self):
            return {}

    monkeypatch.setattr(main_mod, "RAGEngine", FakeEngine)
    monkeypatch.setattr(main_mod, "create_router", lambda s: SimpleNamespace(model_list=[]))
    monkeypatch.setattr(main_mod, "SpecLoader",
                        lambda root: SimpleNamespace(domains=[], codelists=[]))

    def _run(**overrides):
        s = Settings(**overrides)
        app = FastAPI()
        app.state.settings = s
        events: list[tuple] = []
        structlog.configure(processors=[lambda _l, m, ed: events.append((m, ed)) or ""])
        async def go():
            async with main_mod.lifespan(app):
                pass
        asyncio.run(go())
        return app, engines, events

    return _run


def test_docs_engine_is_built_and_wrapped_when_enabled(boot):
    app, engines, _ = boot(federation_enabled=True, study_docs_enabled=True, study_docs_seats=5)
    built = [e["collection_name"] for e in engines]
    assert "study_st01_docs" in built
    assert isinstance(app.state.federation.study, StudyCorpusEngine)
    assert app.state.federation.study.doc_seats == 5


def test_docs_engine_absent_when_disabled(boot):
    app, engines, _ = boot(federation_enabled=True, study_docs_enabled=False)
    assert "study_st01_docs" not in [e["collection_name"] for e in engines]
    assert not isinstance(app.state.federation.study, StudyCorpusEngine)


def test_docs_enabled_without_federation_logs_ignored(boot):
    _, engines, events = boot(federation_enabled=False, study_docs_enabled=True)
    assert "study_st01_docs" not in [e["collection_name"] for e in engines]
    assert any(m == "study_docs_ignored" for m, _ in events)


def test_seats_and_collection_are_reported_in_the_ready_log(boot):
    """条数/库名进日志: 席位写死成常量或库名指错时, 唯一的现场线索就是这一行。"""
    _, _, events = boot(federation_enabled=True, study_docs_enabled=True, study_docs_seats=7)
    hit = [ed for m, ed in events if m == "study_docs"]
    assert hit and hit[0]["seats"] == 7 and hit[0]["collection"] == "study_st01_docs"
```

- [ ] **Step 2: 跑测试确认失败**

Run: `cd sdtm-rag && ./.venv/bin/python -m pytest scripts/tests/test_main_study_docs_wiring.py -p no:warnings`
Expected: FAIL — `Settings` 没有 `study_docs_enabled`

- [ ] **Step 3: 加三个 setting**

在 `server/config.py` 的 `study_aliases_path` 之后加:

```python
    # U2 doc 通道 (spec 2026-08-12 §4.5): study 侧除 959 张卡片外, 还有 114 个手順書章节
    # chunk 在独立 collection 里。加席不抢席 —— cards 的 top_k 不动, doc 另取 seats 席。
    # collection 不存在而开关开着 = 配置错误, 启动响亮失败 (见 main.py), 不静默降级。
    study_docs_enabled: bool = False
    study_docs_collection_name: str = "study_st01_docs"
    study_docs_seats: int = 5
```

> `study_docs_enabled` 的**生产默认值**由 Task 8 的双臂结果 + spec §6 自毁条款 3 决定;
> 本 task 先落 `False`, 证据齐了再在 Task 9 改。**不许在证据之前改成 True。**

- [ ] **Step 4: 接进 lifespan**

`server/main.py` federation 分支里, 构造完 `rag_study` 之后、构造 `FederatedEngine` 之前:

```python
        study_engine = rag_study
        if s.study_docs_enabled:
            # collection 缺失 = 配置错误, 响亮失败 (与 federation 同纪律): 显式开着 doc 通道
            # 却静默退化成纯卡片, 比启动失败更危险 —— 它表现为"接了线但一条 doc 都不出现"。
            rag_docs = RAGEngine(
                chroma_dir=s.chroma_dir,
                # docs/ 没有 ROUTING.md/INDEX.md, 而 kb_root 只进 system prompt 不参与检索;
                # 这里与 U1 测上界时逐字同一条路径, 数字因此可比。system_prompt 不被读 ——
                # StudyCorpusEngine 只用 cards 引擎那份 (test_study_corpus 已钉死)。
                kb_root=s.study_kb_root,
                collection_name=s.study_docs_collection_name,
                embedding_model=s.embedding_model,
                top_k=s.study_docs_seats,
                structured_lookup_enabled=False,
                hybrid_enabled=s.hybrid_enabled,
                hybrid_fusion=s.hybrid_fusion,
                hybrid_alpha=s.hybrid_alpha,
                hybrid_pool=s.hybrid_pool,
                prompt_guardrail_enabled=s.prompt_guardrail_enabled,
            )
            from server.study_corpus import StudyCorpusEngine
            study_engine = StudyCorpusEngine(rag_study, rag_docs, doc_seats=s.study_docs_seats)
            log.info("study_docs", collection=s.study_docs_collection_name,
                     seats=s.study_docs_seats, chunks=rag_docs.collection.count())
```

`FederatedEngine(app.state.rag, study_engine, ...)` —— 把第二个实参从 `rag_study` 换成 `study_engine`。

再在 `elif s.study_lookup_enabled:` 那族旁边补一条同形告警:

```python
    if s.study_docs_enabled and not s.federation_enabled:
        log.warning(
            "study_docs_ignored",
            note="study_docs_enabled=true 但 federation_enabled=false; doc 通道只挂在联邦的 "
                 "study 引擎上, 本次启动未加载",
        )
```

- [ ] **Step 5: 跑测试**

Run: `cd sdtm-rag && ./.venv/bin/python -m pytest scripts/tests/test_main_study_docs_wiring.py -p no:warnings && ./.venv/bin/python -m pytest -p no:warnings`
Expected: 新测试 4 passed; 全量 ≥ 1131 passed, 0 failed

- [ ] **Step 6: 变异测试**

| 变异 | 期望 |
|---|---|
| lifespan 里 `study_engine = StudyCorpusEngine(...)` 那行删掉 (只建不包) | ≥1 failed |
| `doc_seats=s.study_docs_seats` 改成 `doc_seats=5` 常量 | ≥1 failed |
| `study_docs_ignored` 告警删掉 | ≥1 failed |

追加进 `evidence/step_u2_mutation.md`。

- [ ] **Step 7: 提交**

```bash
cd /Users/bojiangzhang/MyProject/sdtm-pedia && \
git add sdtm-rag/server/config.py sdtm-rag/server/main.py sdtm-rag/scripts/tests/test_main_study_docs_wiring.py sdtm-rag/evidence/step_u2_mutation.md && \
git commit -m "feat(doc-track): U2 Task 2 — doc 通道生产接线 (默认 OFF, 响亮失败 + 留声)"
```

---

### Task 3: eval 接线 (`--study-docs` / `--doc-seats` / `--corpus`)

**Files:**
- Modify: `eval/run_eval.py:705-760` (argparse) 与 `:815-857` (federated 分支) 与 `_FederatedAdapter:552-572`
- Test: `scripts/tests/test_run_eval_doc_channel.py`

**Interfaces:**
- Consumes: Task 1 `StudyCorpusEngine`
- Produces: CLI `--study-docs` (bool) / `--doc-seats N` (int, 默认取 `settings.study_docs_seats`) / `--corpus {auto,cdisc,study,both}` (默认 `auto`); `_FederatedAdapter.__init__(fed, corpus="auto")`

> **修订 (2026-08-12, Task 3 执行后)**:
> 1. ⛔ **下面这 4 条断言经实证是装饰品**。把 `main()` 里整个 doc 通道装配块**删光**
>    (变异 B9) 首测 **1142 passed / 0 failed** —— 4 条没有一条进入 federated 装配分支,
>    新增的 27 行零覆盖。实际实现**保留这 4 条逐字不动**, 另加 6 条 (3 条 stderr 判别 +
>    3 条装配锁, `RAGEngine`/`create_router`/`FederatedEngine`/`run_evaluation` 全 stub,
>    零 chroma 零 LLM), 22 条变异补强后 22/22 全红。
> 2. Step 2 写的预期失败 (`unrecognized arguments: --study-docs`) **不成立**: argparse 对
>    未知 flag 抛的**同样是 `SystemExit`** ⇒ `pytest.raises(SystemExit)` 在"闸拒绝"与
>    "flag 压根没实现"两种情形下一样绿, 那条测试在实现之前就已 PASS。**教训: 用
>    `SystemExit` 断 argparse 闸时, 必须同时判 stderr 内容, 否则闸与缺失不可分。**
> 3. `settings.study_docs_seats` 出厂值恰为 **5**, 与计划里"写死 5"的变异撞号 ⇒
>    照那条变异跑必须先把 settings 改成别的值, 否则变异是 no-op 会被误读成装饰断言。

- [ ] **Step 1: 写失败测试**

```python
"""U2: run_eval 的 doc 通道与强制判库 flag (spec §4.6)。

只测 argparse 与装配, 不跑真检索 (RAGEngine/create_router 全 stub)。
"""
from types import SimpleNamespace

import pytest

from eval import run_eval as m


def test_study_docs_requires_federated():
    with pytest.raises(SystemExit):
        m.main(["x.yml", "--study-docs"])


def test_corpus_default_is_auto_and_adapter_passes_it_through():
    fed = SimpleNamespace(retrieve=lambda q, corpus, top_k: ([], corpus))
    ad = m._FederatedAdapter(fed)
    ad.retrieve("q")
    assert ad.routed == ["auto"]


def test_corpus_forced_study_is_passed_to_federation():
    """强制判库是把「判库损耗」与「接线损耗」拆开的唯一手段 —— 传丢了两个数就合并了。"""
    seen = {}

    def _retrieve(q, corpus, top_k):
        seen["corpus"] = corpus
        return [], corpus

    ad = m._FederatedAdapter(SimpleNamespace(retrieve=_retrieve), corpus="study")
    ad.retrieve("q")
    assert seen["corpus"] == "study"


def test_invalid_corpus_rejected():
    with pytest.raises(SystemExit):
        m.main(["x.yml", "--federated", "--corpus", "nope"])
```

- [ ] **Step 2: 跑测试确认失败**

Run: `cd sdtm-rag && ./.venv/bin/python -m pytest scripts/tests/test_run_eval_doc_channel.py -p no:warnings`
Expected: FAIL — `unrecognized arguments: --study-docs`

- [ ] **Step 3: 实现**

argparse 里加 (紧跟 `--study-lookup`):

```python
    parser.add_argument(
        "--study-docs", action="store_true",
        help="U2: study 侧 doc 通道 (手順書章节 chunk 追加 N 席)。需 --federated",
    )
    parser.add_argument(
        "--doc-seats", type=int, default=None,
        help="doc 追加席位数 N (默认取 settings.study_docs_seats)。加席不抢席: "
             "cards 的 top_k 不受影响",
    )
    parser.add_argument(
        "--corpus", default="auto", choices=["auto", "cdisc", "study", "both"],
        help="强制判库 (默认 auto = 走 LLM 路由, 与生产逐字相同)。强制 study 用于把"
             "判库损耗与接线损耗拆开",
    )
```

flag 闸 (紧跟现有两条):

```python
    if args.study_docs and not args.federated:
        parser.error("--study-docs 需要 --federated (doc 通道挂在联邦的 study 引擎上)")
    if args.corpus != "auto" and not args.federated:
        parser.error("--corpus 只在 --federated 下有意义")
```

federated 分支里, 构造完 `study_rag` 后:

```python
        study_engine = study_rag
        if args.study_docs:
            doc_seats = (
                args.doc_seats if args.doc_seats is not None else settings.study_docs_seats
            )
            docs_rag = RAGEngine(
                chroma_dir=settings.chroma_dir,
                kb_root=settings.study_kb_root,      # 与 U1 上界口径逐字相同
                collection_name=settings.study_docs_collection_name,
                embedding_model=settings.embedding_model,
                top_k=doc_seats,
                structured_lookup_enabled=False,
                hybrid_enabled=args.hybrid,
                hybrid_fusion=args.hybrid_fusion or settings.hybrid_fusion,
                hybrid_alpha=(
                    args.hybrid_alpha if args.hybrid_alpha is not None else settings.hybrid_alpha
                ),
                hybrid_pool=(
                    args.hybrid_pool if args.hybrid_pool is not None else settings.hybrid_pool
                ),
                prompt_guardrail_enabled=args.guardrail,
            )
            from server.study_corpus import StudyCorpusEngine
            study_engine = StudyCorpusEngine(study_rag, docs_rag, doc_seats=doc_seats)
            print(f"Study docs channel: {docs_rag.collection.count()} chunks, "
                  f"collection={settings.study_docs_collection_name}, seats={doc_seats}")
        retriever = _FederatedAdapter(
            FederatedEngine(rag, study_engine, create_router(settings), top_k=args.top_k),
            corpus=args.corpus,
        )
```

`_FederatedAdapter` 加 corpus:

```python
    def __init__(self, fed, corpus: str = "auto"):
        self.fed = fed
        self.corpus = corpus
        self.routed: list[str] = []

    def retrieve(self, q, top_k=None):
        chunks, routed = self.fed.retrieve(q, corpus=self.corpus, top_k=top_k)
        self.routed.append(routed)
        return chunks
```

> ⚠ `FederatedEngine.retrieve` 在 `corpus != "auto"` 时把入参原样当 routed 返回,
> 故 `self.routed` 记的仍是本题实际用的库, `build_messages` 的 system prompt 口径不变。

- [ ] **Step 4: 跑测试**

Run: `cd sdtm-rag && ./.venv/bin/python -m pytest scripts/tests/test_run_eval_doc_channel.py scripts/tests/test_run_eval_federated.py -p no:warnings`
Expected: PASS, 既有联邦测试零回归

- [ ] **Step 5: 回归闸 — 不加新 flag 时行为逐字不变**

Run:
```bash
cd sdtm-rag && ./.venv/bin/python -m eval.run_eval data/study/st01/eval/test_set_study_v2.yml \
  --retrieval-only --hybrid --study-lookup \
  --collection study_st01 --kb-root data/study/st01/cards --output /tmp/u2_t3_regress.json
./.venv/bin/python -c "
import json
a=json.load(open('/tmp/u2_t3_regress.json')); b=json.load(open('data/study/st01/eval/runs/v2_baseline_s2on.json'))
pa={r['id']:r['source_recall'] for r in a['results']}; pb={r['id']:r['source_recall'] for r in b['results']}
d={k:(pa[k],pb[k]) for k in pa if pa[k]!=pb[k]}
print('avg', a['summary']['source_recall_avg'], '| per-q diffs:', d)"
```
Expected: `avg 0.875 | per-q diffs: {}`

- [ ] **Step 6: 提交**

```bash
cd /Users/bojiangzhang/MyProject/sdtm-pedia && \
git add sdtm-rag/eval/run_eval.py sdtm-rag/scripts/tests/test_run_eval_doc_channel.py && \
git commit -m "feat(doc-track): U2 Task 3 — eval 侧 --study-docs/--doc-seats/--corpus"
```

---

### Task 3b: docs 引擎构造去重 (新增 — 两方独立提出的漂移风险)

**为什么必须在 Task 4 之前做**: docs 引擎现在被**两条独立代码路径各造一次** ——
`server/main.py` 的 lifespan (生产) 与 `eval/run_eval.py` 的 `--study-docs` 分支 (尺子)。
两处各抄了一份参数清单, **没有任何东西钉它们相等**。漂移的表现是: **尺子全绿而生产是另一台
引擎, 且不会有任何报错** —— 这直接抽掉本单元全部数字的效力。

两方独立提出: Task 2 审查方 (问题 2③「跨路径漂移才是本条真正的风险」) 与 Task 3 实现方
(风险 3: eval 侧 docs 引擎**少了 `rerank_*` / `query_expansion` 三个 lever**, 吃默认值,
而 cards/cdisc 两台都从 `args` 取 ⇒ 一旦有人跑 `--rerank` 或 `--query-expansion`, 三台引擎
口径不一致而数字看不出来)。

**Files:**
- Modify: `server/study_corpus.py` (加模块级工厂)
- Modify: `server/main.py` (lifespan 改调工厂) · `eval/run_eval.py` (federated 分支改调工厂)
- Test: `scripts/tests/test_study_corpus.py` (工厂单测) · `scripts/tests/test_docs_engine_parity.py` (新, 两路径同源闸)

**Interfaces:**
- Produces: `make_docs_engine(rag_cls, *, chroma_dir, kb_root, collection_name, embedding_model, seats, levers: dict)` → RAGEngine 实例; `DOCS_ENGINE_FIXED_KWARGS` (常量 dict, 记录 doc 引擎恒定的那几个: `structured_lookup_enabled=False`, `study_lookup` 不传)

- [ ] **Step 1: 写失败测试 — 两路径同源闸**

断言两件事 (第二件是本 task 的核心):
1. 工厂产出的 kwargs 里 `structured_lookup_enabled is False` 且不含 `study_lookup`;
2. **`main.py` 与 `run_eval.py` 两条路径在同一组 lever 值下, 构造 docs 引擎所用的 kwargs
   逐键相同** —— 用同一个 `FakeRAG` 记录 kwargs, 分别跑 lifespan 与 `run_eval.main()`
   (两侧都 stub 掉真引擎/路由/评测), 比对两个 dict。

- [ ] **Step 2: 跑测试确认失败** (工厂不存在 / 两侧 kwargs 不等)

- [ ] **Step 3: 实现工厂并让两处都调它**

工厂只负责"把参数装配成 RAGEngine", **不读 settings 也不读 args** —— 两侧各自解析自己的
配置来源后把**解析结果**传进来, 这样 eval 的 `--hybrid` 覆盖与生产的 settings 取值都保留,
被钉住的是**装配方式**而不是取值来源。

同时补齐 eval 侧缺的三个 lever (`rerank_enabled` / `rerank_model` / `rerank_candidates` /
`query_expansion` 一族), 使 docs 引擎与同一次运行里的 cards 引擎 lever 一致。

- [ ] **Step 4: 跑测试确认通过 + 全量 pytest**

- [ ] **Step 5: 回归闸 — 重跑 Task 3 Step 5 的不变性检查**

```bash
cd sdtm-rag && ./.venv/bin/python -m eval.run_eval data/study/st01/eval/test_set_study_v2.yml \
  --retrieval-only --hybrid --study-lookup \
  --collection study_st01 --kb-root data/study/st01/cards --output /tmp/u2_t3b_regress.json
```
Expected: `avg 0.875`, 逐题 diffs `{}` (重构不许动数字)

- [ ] **Step 6: 变异测试 (两个方向, 见 Global Constraint 12)**

至少含: 工厂里 `structured_lookup_enabled` 改 `True` · 两路径之一绕过工厂直接 `RAGEngine(...)` ·
lever 传参漏一个 —— 三条都必须变红。

- [ ] **Step 7: 提交**

```bash
cd /Users/bojiangzhang/MyProject/sdtm-pedia && \
git add sdtm-rag/server/study_corpus.py sdtm-rag/server/main.py sdtm-rag/eval/run_eval.py \
        sdtm-rag/scripts/tests/test_study_corpus.py sdtm-rag/scripts/tests/test_docs_engine_parity.py && \
git commit -m "refactor(doc-track): U2 Task 3b — docs 引擎构造去重 + 两路径同源闸"
```

---

### Task 4: N sweep (零 LLM) + 与 U1 k 曲线对照

**Files:**
- 无代码改动 (纯跑批 + 记录)
- Create: `evidence/step_u2_sweep.md` (进 git, 只写数字)
- 产物: `data/study/st01/eval/runs/u2_docs_N{0,3,5,8,10,15}.json` (gitignored)

**Interfaces:**
- Consumes: Task 3 的 CLI
- Produces: 生产 N 的取值与**选择理由**, 供 Task 5-8 使用

- [ ] **Step 1: 跑 sweep (强制 corpus=study, 隔离判库变量)**

```bash
cd sdtm-rag
P=data/study/st01/eval/test_set_docs_v1.yml
for N in 0 3 5 8 10 15; do
  ./.venv/bin/python -m eval.run_eval $P --retrieval-only --hybrid --study-lookup \
    --federated --corpus study --study-docs --doc-seats $N \
    --output data/study/st01/eval/runs/u2_docs_N$N.json
done
```

- [ ] **Step 2: 算 recall**

```bash
cd sdtm-rag && ./.venv/bin/python -c "
import json
for N in [0,3,5,8,10,15]:
    d=json.load(open(f'data/study/st01/eval/runs/u2_docs_N{N}.json'))
    rs=d['results']
    print(N, d['summary']['source_recall_avg'],
          'full=', sum(1 for r in rs if r['source_recall']==1.0), '/', len(rs))
"
```

- [ ] **Step 3: 算 context 成本 (run 输出里没有正文, 必须另量)**

`run_eval` 的 `top5_sources` 只有文件名 (`eval/run_eval.py:343`), **不带正文** ⇒ 成本要直接从
引擎量。写到 `data/study/st01/eval/` (gitignored), 只把汇总数字带进证据:

```bash
cd sdtm-rag && ./.venv/bin/python -c "
import json, yaml
from server.config import settings
from server.rag import RAGEngine
from server.study_corpus import StudyCorpusEngine
from server.study_lookup import StudyLookup

qs = yaml.safe_load(open('data/study/st01/eval/test_set_docs_v1.yml'))
common = dict(chroma_dir=settings.chroma_dir, embedding_model=settings.embedding_model,
              hybrid_enabled=True, hybrid_fusion=settings.hybrid_fusion,
              hybrid_alpha=settings.hybrid_alpha, hybrid_pool=settings.hybrid_pool,
              structured_lookup_enabled=False)
cards = RAGEngine(kb_root=settings.study_kb_root, collection_name=settings.study_collection_name,
                  top_k=15, study_lookup=StudyLookup.from_paths(
                      settings.study_catalog_path, settings.study_aliases_path), **common)
docs = RAGEngine(kb_root=settings.study_kb_root,
                 collection_name=settings.study_docs_collection_name, top_k=15, **common)
out = {}
for N in [0, 3, 5, 8, 10, 15]:
    eng = StudyCorpusEngine(cards, docs, doc_seats=N)
    sizes = [len(eng.format_context(eng.retrieve(q['question'], top_k=15))) for q in qs]
    out[N] = {'median': sorted(sizes)[len(sizes)//2], 'max': max(sizes),
              'mean': round(sum(sizes)/len(sizes))}
    print(N, out[N], flush=True)
json.dump(out, open('data/study/st01/eval/runs/u2_ctx_cost.json','w'), indent=2)"
```

⚠ 这一步**多打一遍 embedding** (每题每档一次检索), 但零 LLM 生成。若与 Step 1 的召回数
对不上 (同 N 下 gold 命中集不同), **先查口径** (Global Constraint 8) 再下结论。

- [ ] **Step 4: 与 U1 k 曲线逐档比 (参照物在本单元之外)**

| N | U1 doc-only 预测 | U2 实测 | 差 = 接线损耗 |
|---|---|---|---|
| 3 | 0.8667 | | |
| 5 | 0.8833 | | |
| 8 | 1.0000 | | |
| 15 | 1.0000 | | |

- [ ] **Step 5: 检查自毁条款 2**

`N=15` 实测 **< 90.0%** ⇒ **停**, 写 `evidence/failures/u2_wirein_upper_gap.md`, 上报用户, 不许继续调参。

- [ ] **Step 6: 定生产 N 并写理由**

`evidence/step_u2_sweep.md` 必须同时写: 每档 recall · 每档 context 字符量 · 选中的 N ·
**为什么不选更大的 N** (成本) 与 **为什么不选更小的 N** (召回)。只写结论 = 不合格。

- [ ] **Step 7: 提交**

```bash
cd /Users/bojiangzhang/MyProject/sdtm-pedia && git add sdtm-rag/evidence/step_u2_sweep.md && \
git commit -m "evidence(doc-track): U2 Task 4 — N sweep 与 U1 k 曲线逐档对照"
```

---

### Task 5: router 描述改准 + 路由闸

**Files:**
- Modify: `server/federation.py:20-55` (`_ROUTER_SYSTEM` 规则 2 的语料描述)
- Test: `scripts/tests/test_federation.py` (补一条 prompt 内容断言)

**Interfaces:**
- Consumes: 无
- Produces: 新 `_ROUTER_SYSTEM`; 路由闸结果 `data/study/st01/eval/runs/routing_u2_*.json`

- [ ] **Step 1: 记录基线 (改之前)**

```bash
cd sdtm-rag && ./.venv/bin/python -m eval.run_routing_eval --runs 3 2>&1 | tail -8
```
Expected: `exact` ≈ 178/181, `fatal=0`。**把三遍的逐题预测存下来**供逐题比。

- [ ] **Step 2: 写失败测试**

```python
def test_router_prompt_describes_the_study_document_corpus():
    """C1 之后 study 库里除了卡片还有 114 个手順書章节 chunk。prompt 若仍只写 field cards,
    偏"标准味"的手順問題会被判给 cdisc (实测 30 题里 5 题如此), 而 CDISC 库结构上答不出。"""
    from server.federation import _ROUTER_SYSTEM
    assert "field cards" in _ROUTER_SYSTEM
    assert "protocol" in _ROUTER_SYSTEM.lower()
```

- [ ] **Step 3: 改 prompt (只改事实描述, 不动规则优先级)**

`_ROUTER_SYSTEM` 里 study 语料那一行:

```
- "study": ONE specific clinical study's own artifacts — its EDC field cards \
(forms/screens, field labels, item groups, display conditions, units) AND that study's own \
protocol / procedure document sections (手順・計画文書の節: eligibility, treatment schedule, \
assessments, statistical plan). Japanese content.
```

规则 1/2/3 的正文与优先级**一个字不改**。

- [ ] **Step 4: 跑路由闸三遍**

```bash
cd sdtm-rag && ./.venv/bin/python -m eval.run_routing_eval --runs 3 2>&1 | tail -8
```

判据 (spec §5.4): `exact ≥ 178/181` 且 `fatal = 0`。**新增 fatal 逐题列名。**
不达标 ⇒ 自毁条款 5: **回滚 prompt**, 并在证据里写明 doc 侧天花板被压到 25/30 = 83.3%。

- [ ] **Step 5: 单独测 30 道 doc 题的判库 (不并入 181)**

```bash
cd sdtm-rag && ./.venv/bin/python -c "
import yaml, collections, sys
sys.path.insert(0, '.')
from server.config import settings
from server.federation import route_corpus
from server.llm_config import create_router
qs = yaml.safe_load(open('data/study/st01/eval/test_set_docs_v1.yml'))
r = create_router(settings)
out = [(q['id'], route_corpus(r, q['question'])[0]) for q in qs]
print(collections.Counter(c for _, c in out))
print('non-study:', [i for i, c in out if c != 'study'])"
```
基线 (改之前, 2026-08-12 实测): `study 25 / cdisc 5`, non-study = `q05 q15 q17 q53 q55`。

- [ ] **Step 6: 全量测试 + 提交**

```bash
cd sdtm-rag && ./.venv/bin/python -m pytest -p no:warnings
cd /Users/bojiangzhang/MyProject/sdtm-pedia && \
git add sdtm-rag/server/federation.py sdtm-rag/scripts/tests/test_federation.py && \
git commit -m "fix(doc-track): U2 Task 5 — router 的 study 语料描述补上手順書章节"
```

---

### Task 6: 三把尺子 + 卡片侧不回归 (retrieval-only, 零 LLM)

**Files:**
- 无代码改动
- Create: `evidence/step_u2_rulers.md`

- [ ] **Step 1: 尺子① 接线损耗档 (强制 study, N=15)**

```bash
cd sdtm-rag && ./.venv/bin/python -m eval.run_eval data/study/st01/eval/test_set_docs_v1.yml \
  --retrieval-only --hybrid --study-lookup --federated --corpus study \
  --study-docs --doc-seats 15 --output data/study/st01/eval/runs/u2_ruler1_N15.json
```
对照 U1 上界 **100.0%** (⛔ 该值触发了自毁条款, 用户豁免 —— 引用时必须原样写)。

- [ ] **Step 2: 尺子② 判别力档 (强制 study, N=5)**

同上换 `--doc-seats 5`, 输出 `u2_ruler2_N5.json`。对照 U1 **88.33%**。

- [ ] **Step 3: 尺子③ 生产档 (corpus=auto, 生产 N)**

```bash
cd sdtm-rag && ./.venv/bin/python -m eval.run_eval data/study/st01/eval/test_set_docs_v1.yml \
  --retrieval-only --hybrid --study-lookup --federated --study-docs \
  --output data/study/st01/eval/runs/u2_ruler3_prod.json
```
**①③之差 = 判库损耗, 单列, 不许并进接线损耗** (Global Constraint 6)。

- [ ] **Step 4: 卡片侧 48 题逐题 Δ0 (自毁条款 1)**

```bash
cd sdtm-rag && ./.venv/bin/python -m eval.run_eval data/study/st01/eval/test_set_study_v2.yml \
  --retrieval-only --hybrid --study-lookup --federated --corpus study --study-docs \
  --output data/study/st01/eval/runs/u2_cards_docon.json
./.venv/bin/python -c "
import json
a=json.load(open('data/study/st01/eval/runs/u2_cards_docon.json'))
b=json.load(open('data/study/st01/eval/runs/v2_baseline_s2on.json'))
pa={r['id']:r['source_recall'] for r in a['results']}; pb={r['id']:r['source_recall'] for r in b['results']}
print('avg', a['summary']['source_recall_avg'])
print('diffs', {k:(pa[k],pb[k]) for k in pa if pa[k]!=pb[k]})"
```
Expected: `avg 0.875` · `diffs {}`。**非 Δ0 ⇒ 自毁条款 1, 方案作废退回设计。**

- [ ] **Step 5: 写 `evidence/step_u2_rulers.md`**

必须同写 (硬规矩 19): 卡片侧 Δ0 **由构造保证 ⇒ 判别力低, 该绿灯不可证伪**。

- [ ] **Step 6: 提交**

```bash
cd /Users/bojiangzhang/MyProject/sdtm-pedia && git add sdtm-rag/evidence/step_u2_rulers.md && \
git commit -m "evidence(doc-track): U2 Task 6 — 三把尺子 + 卡片侧逐题 Δ0"
```

---

### Task 7: 对照 harness (`eval/judge_controls.py`)

**Files:**
- Create: `eval/judge_controls.py`
- Test: `scripts/tests/test_judge_controls.py`

**Interfaces:**
- Consumes: `eval.run_eval.check_fact_recall_judge(answer, expected_facts, judge_model=..., temperature=...)`
- Produces: CLI `python -m eval.judge_controls <test_set.yml> --mode {positive,negative} --n 6`; 函数 `sample_ids(ids: list[str], n: int) -> list[str]`

- [ ] **Step 1: 写失败测试 (抽样规则是重点 — 它必须与分数无关)**

```python
"""U2: 阳性/阴性对照 harness (spec §5.3)。

U1 Task 9 是一次性跑的; 这里变成可复跑脚本 —— 没有对照, 双臂数字不可解读。
抽样规则先写死, 事后不许换 (与分数无关是它唯一的价值)。
"""
from eval.judge_controls import sample_ids, positive_answer


def test_sample_ids_is_deterministic_and_spread():
    ids = [f"q{i:02d}" for i in range(30)]
    got = sample_ids(ids, 6)
    assert got == sample_ids(ids, 6)                    # 确定性
    assert len(got) == len(set(got)) == 6
    assert got[0] != ids[0]                             # 不取首题 (仿 U1)
    assert got == [ids[i] for i in (4, 8, 12, 17, 21, 25)]


def test_sample_ids_sorts_before_indexing():
    """入参顺序不该影响抽样 —— 否则"抽样规则"会随文件里的题序漂移。"""
    ids = [f"q{i:02d}" for i in range(30)]
    assert sample_ids(list(reversed(ids)), 6) == sample_ids(ids, 6)


def test_sample_ids_rejects_impossible_n():
    import pytest
    with pytest.raises(ValueError):
        sample_ids(["a", "b"], 6)


def test_positive_answer_is_the_gold_facts_joined():
    q = {"expected_facts": ["fact one", "fact two"]}
    a = positive_answer(q)
    assert "fact one" in a and "fact two" in a
```

- [ ] **Step 2: 跑测试确认失败**

Run: `cd sdtm-rag && ./.venv/bin/python -m pytest scripts/tests/test_judge_controls.py -p no:warnings`
Expected: FAIL — `No module named 'eval.judge_controls'`

- [ ] **Step 3: 实现**

```python
"""U2 阳性/阴性对照 (spec §5.3)。

为什么必须有: judge 分数只有在"喂对答案会得高分、喂空会得低分"两侧都成立时才可解读。
U1 实测过一次 (卡片库 0.0 ×6 + 阳性 1.00 ×6), 但那是一次性脚本 —— 本单元把它固化,
否则下一个人无法复跑 (U1 §8 硬约束 5)。

抽样规则 (spec §5.3, 读数据前写死): id 升序后取 idx = ⌊k*n/7⌋, k=1..6。与分数无关。
"""
from __future__ import annotations

import argparse
import json

import yaml

from eval.run_eval import DEFAULT_JUDGE_MODEL, check_fact_recall_judge


def sample_ids(ids: list[str], n: int) -> list[str]:
    if n <= 0 or n > len(ids):
        raise ValueError(f"n={n} out of range for {len(ids)} ids")
    ordered = sorted(ids)
    idx = sorted({(k * len(ordered)) // (n + 1) for k in range(1, n + 1)})
    if len(idx) != n:  # 小池子撞位: 退化成前 n 个不重复位置, 仍与分数无关
        idx = list(range(n))
    return [ordered[i] for i in idx]


def positive_answer(q: dict) -> str:
    """阳性对照答案 = gold facts 原句拼接。judge 若给不出 ≈1.0, 说明尺子本身坏了。"""
    return "\n".join(q["expected_facts"])


def main(argv=None) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("test_set")
    p.add_argument("--mode", choices=["positive", "negative"], required=True)
    p.add_argument("--n", type=int, default=6)
    p.add_argument("--judge-model", default=DEFAULT_JUDGE_MODEL)
    p.add_argument("--output")
    a = p.parse_args(argv)

    qs = {q["id"]: q for q in yaml.safe_load(open(a.test_set, encoding="utf-8"))}
    picked = sample_ids(list(qs), a.n)
    rows = []
    for qid in picked:
        q = qs[qid]
        answer = positive_answer(q) if a.mode == "positive" else "情報が見つかりませんでした。"
        # 签名核对过 (eval/run_eval.py:254): (question, answer, expected_facts, judge_model,
        # temperature=0.0) -> (recall, hits, misses) | None; None = judge 回复不可解析。
        verdict = check_fact_recall_judge(
            q["question"], answer, q["expected_facts"],
            judge_model=a.judge_model, temperature=0.0,
        )
        recall = verdict[0] if verdict else None
        rows.append({"id": qid, "recall": recall, "parse_ok": verdict is not None})
        print(f"[{a.mode}] {qid} recall={recall} parse_ok={verdict is not None}", flush=True)

    ok = [r["recall"] for r in rows if r["recall"] is not None]
    avg = sum(ok) / len(ok) if ok else 0.0
    print(f"[{a.mode}] n={len(rows)} parse_ok={sum(r['parse_ok'] for r in rows)} avg={avg:.4f}")
    if a.output:
        json.dump({"mode": a.mode, "avg": avg, "rows": rows},
                  open(a.output, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

> `DEFAULT_JUDGE_MODEL = "deepseek/deepseek-chat"` (`eval/run_eval.py:211`)。judge 的重试与
> 限流退避在 `check_fact_recall_judge` 内部, 本脚本不重复实现。

- [ ] **Step 4: 跑测试**

Run: `cd sdtm-rag && ./.venv/bin/python -m pytest scripts/tests/test_judge_controls.py -p no:warnings`
Expected: PASS (4 passed)

- [ ] **Step 5: 变异测试**

`sample_ids` 里去掉 `sorted(ids)` ⇒ 期望 ≥1 failed; `positive_answer` 返回 `""` ⇒ ≥1 failed。追加进 `evidence/step_u2_mutation.md`。

- [ ] **Step 6: 提交**

```bash
cd /Users/bojiangzhang/MyProject/sdtm-pedia && \
git add sdtm-rag/eval/judge_controls.py sdtm-rag/scripts/tests/test_judge_controls.py sdtm-rag/evidence/step_u2_mutation.md && \
git commit -m "feat(doc-track): U2 Task 7 — 阳性/阴性对照 harness (抽样规则先写死)"
```

---

### Task 8: 答题侧双臂 (kickoff 硬验收第 3 条)

**Files:**
- 无代码改动
- Create: `evidence/step_u2_answerside.md`

**先跑对照, 对照不成立就停 —— 自毁条款 4。**

- [ ] **Step 1: 阳性/阴性对照 (两组各 6)**

```bash
cd sdtm-rag
for M in positive negative; do
  ./.venv/bin/python -m eval.judge_controls data/study/st01/eval/test_set_docs_v1.yml \
    --mode $M --n 6 --output data/study/st01/eval/runs/u2_ctrl_docs_$M.json
  ./.venv/bin/python -m eval.judge_controls data/study/st01/eval/test_set_study_v2.yml \
    --mode $M --n 6 --output data/study/st01/eval/runs/u2_ctrl_cards_$M.json
done
```
判据: 阳性 **≥ 0.80**, 阴性 **≤ 0.20**。不满足 ⇒ **停, 不许解读任何双臂数字**。

- [ ] **Step 2: 卡片 48 题双臂**

```bash
cd sdtm-rag
# OFF 臂
./.venv/bin/python -m eval.run_eval data/study/st01/eval/test_set_study_v2.yml \
  --hybrid --study-lookup --federated --corpus study --judge --temperature 0 \
  --output data/study/st01/eval/runs/u2_ans_cards_off.json
# ON 臂 (只多 --study-docs, 其余逐字相同)
./.venv/bin/python -m eval.run_eval data/study/st01/eval/test_set_study_v2.yml \
  --hybrid --study-lookup --federated --corpus study --study-docs --judge --temperature 0 \
  --output data/study/st01/eval/runs/u2_ans_cards_on.json
```

- [ ] **Step 3: doc 30 题双臂**

同上换题集 `test_set_docs_v1.yml`, 输出 `u2_ans_docs_{off,on}.json`。

- [ ] **Step 4: 逐题比 + 判 parse 失败**

```bash
cd sdtm-rag && ./.venv/bin/python -c "
import json
for tag in ['cards','docs']:
    off=json.load(open(f'data/study/st01/eval/runs/u2_ans_{tag}_off.json'))
    on =json.load(open(f'data/study/st01/eval/runs/u2_ans_{tag}_on.json'))
    po={r['id']:r for r in off['results']}; pn={r['id']:r for r in on['results']}
    bad=[i for i,r in list(po.items())+list(pn.items()) if not r.get('judge_parse_ok', True)]
    down=[(i, po[i]['judge_fact_recall'], pn[i]['judge_fact_recall'])
          for i in po if pn[i]['judge_fact_recall'] < po[i]['judge_fact_recall']]
    up  =[i for i in po if pn[i]['judge_fact_recall'] > po[i]['judge_fact_recall']]
    ao=sum(po[i]['judge_fact_recall'] for i in po)/len(po)
    an=sum(pn[i]['judge_fact_recall'] for i in pn)/len(pn)
    print(tag, 'off', round(ao,4), 'on', round(an,4), 'down', len(down), 'up', len(up))
    print('  parse_fail:', bad); print('  down detail:', down)"
```

- [ ] **Step 5: 判自毁条款 3 与 6**

- 卡片组 down **≥ 3 题** 或均值降 **> 2.0pt** ⇒ `study_docs_enabled` 生产**默认 OFF**, 本轮不上生产。
- doc 组 ON 臂均值 **< 0.50** ⇒ **停下诊断** ("检索到了但答不出"), 不许拿 retrieval 数字当交付。

- [ ] **Step 6: 写 `evidence/step_u2_answerside.md` + 提交**

必须同写: 单模型单温度 ⇒ 换模型可能翻转 (U1 `q57` 先例); `parse_ok=False` 的题单列。

```bash
cd /Users/bojiangzhang/MyProject/sdtm-pedia && git add sdtm-rag/evidence/step_u2_answerside.md && \
git commit -m "evidence(doc-track): U2 Task 8 — 答题侧双臂 + 阳阴对照"
```

---

### Task 9: 规则 D 三方核验 + 生产默认值裁定

**Files:**
- Create: `evidence/step_u2_audit.md` (抽检方 A) · `evidence/step_u2_audit_mutation.md` (抽检方 B)
- Modify: `server/config.py` (仅当 Task 8 判据全过时把 `study_docs_enabled` 改 `True`)

- [ ] **Step 1: 派抽检方 A (与实现方不同 subagent_type / 不同 session)**

任务: 独立复算 Task 4/6 的关键数字, **参照物自建** (不 import `server.study_corpus`),
判据三条: ① 三把尺子的数字能独立复现 ② 卡片侧 Δ0 属实 ③ N sweep 的 context 成本数字属实。
**开工/收工各记一次 `data/study/st01/eval/runs/` 的 sha256**, 证明产物未被并发改动。

- [ ] **Step 2: 派抽检方 B (再换一个 subagent_type)**

任务: 对 Task 1/2/3/7 的**每一条新断言**做物理变异, 独立于实现方自己那轮。
点名任何"打了但没断言"的输出 (U1 抓到过两条)。

- [ ] **Step 3: controller 非自洽复算 (硬规矩 17b)**

用**不同代码路径**复算至少三个关键数字 (例: 不走 run_eval 的 summary, 直接从逐题 JSON 重算均值;
context 字符量用 chroma 原文重算而非 run 输出)。

- [ ] **Step 4: 裁定生产默认值**

Task 8 判据全过 ⇒ `study_docs_enabled: bool = True` + 全量测试 + 跑一次生产冒烟:

```bash
cd sdtm-rag && ./.venv/bin/python -m pytest -p no:warnings
```
未过 ⇒ 保持 `False`, 并在收口证据里写明**为什么关着**与**开它需要什么证据**。

- [ ] **Step 5: 提交**

```bash
cd /Users/bojiangzhang/MyProject/sdtm-pedia && \
git add sdtm-rag/evidence/step_u2_audit.md sdtm-rag/evidence/step_u2_audit_mutation.md sdtm-rag/server/config.py && \
git commit -m "test(doc-track): U2 Task 9 — 规则 D 三方核验 + 生产默认值裁定"
```

---

### Task 10: 收口

**Files:**
- Create: `evidence/checkpoints/doc_track_u2_wirein.md`
- Modify: `milestones/07_rag_kg/DOC_TRACK_KICKOFF.md` (U2 段改状态) · `docs/PROGRESS.md` · `.work/meta/worklog/phase_07_rag_kg.md` · `CLAUDE.md` Key Paths (仅当需要新指针)

- [ ] **Step 1: 写收口证据**

必含: 一句话结论 · 三把尺子的数 + 判库损耗单列 · 卡片侧 Δ0 (并注明构造保证) · 答题侧双臂 + 对照 ·
路由闸前后 · **已知限制逐条注明它看不见什么** (spec §8 六条起步) · **本单元不能证明什么** ·
复跑命令逐字 · 给下一单元 (L1 卷首 / C2) 的硬约束。

- [ ] **Step 2: 红线程序化复扫**

```bash
cd sdtm-rag && ./.venv/bin/python -c "
import json, subprocess, pathlib
cat=json.load(open('data/study/st01/catalog.json'))
# ⚠ 长度下限对 item_oid 也必须设 (Task 1 实现方实测): catalog 里有 CT / AGE 这类 2-3 字符
# OID, 不设下限会把 RAGEngine 里的 'AGE'、stub 里的 'CTX' 全报成泄漏 —— 真泄漏会被噪声淹掉。
# 加 >=4 后 1417 个值对 Task 1 的三个新文件零命中。
vals={it['item_oid'] for it in cat['items'] if len(it['item_oid'])>=4} \
     | {it['label'] for it in cat['items'] if len(it['label'])>=4}
files=subprocess.run(['git','ls-files'],capture_output=True,text=True,cwd='..').stdout.split()
hits=[]
for f in files:
    p=pathlib.Path('..')/f
    try: t=p.read_text(encoding='utf-8')
    except Exception: continue
    for v in vals:
        if v and v in t: hits.append((f,v))
print('hits:', len(hits)); print(hits[:20])"
```
本单元新增文件必须**零命中**。存量命中如实记录不修。

- [ ] **Step 3: 全量测试 + 三条自检**

```bash
cd sdtm-rag && ./.venv/bin/python -m pytest -p no:warnings --tb=short
```

- [ ] **Step 4: Chain B 更新 + 提交** (worklog → PROGRESS → kickoff 状态)

```bash
cd /Users/bojiangzhang/MyProject/sdtm-pedia && git add -A && \
git commit -m "feat(doc-track): U2 CLOSED — doc chunk 接线 + 三把尺子 + 答题侧双臂"
```

---

## Self-Review

**Spec coverage**: §4.1→Task 1 · §4.2→Task 1 · §4.3→Task 4 · §4.4→Task 5 · §4.5→Task 2 · §4.6→Task 3+7 · §5.1→Task 6 · §5.2→Task 6 Step 4 · §5.3→Task 7+8 · §5.4→Task 5 · §6 自毁条款 1→T6S4 / 2→T4S4 / 3→T8S5 / 4→T8S1 / 5→T5S4 / 6→T8S5 · §7→各 task 的变异步 + Task 9 Step 2 · §8→Task 10 Step 1 · §10→Task 9。

**签名核对过的三处** (写计划时实读源码, 非照记忆写): `check_fact_recall_judge` 的参数序
(`eval/run_eval.py:254`) · `DEFAULT_JUDGE_MODEL` (`:211`) · `top5_sources` 只存文件名不存正文
(`:343` —— 故 context 成本另用 Task 4 Step 3 的脚本量, 不从 run 输出里凑)。

**不许即兴**: 本计划不留"当场设计"的口子。遇到与源码不符的地方, **停下改计划再执行**,
不要就地换写法 —— U1 的教训正是照 plan 字面跑会产出装饰闸 (判据② 与闸 D 两次)。
