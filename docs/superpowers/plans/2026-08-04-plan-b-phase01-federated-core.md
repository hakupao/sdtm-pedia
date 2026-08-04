# Plan B Phase 0+1: 联邦路由核心 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 把 `study_st01` (959 卡) 接入服务：eval 判据先下沉到 section 粒度 (Phase 0)，然后 LLM 判库 + 配额合并 + 引用标识 + 前端切换 (Phase 1)，全部 eval 闸过绿后默认启用。

**Architecture:** 新增 `server/federation.py`，`FederatedEngine` **组合**两个现有 `RAGEngine`（不改造为多 collection）。LLM 路由 (light/Haiku, temperature 0, 严格 JSON) 判 `cdisc|study|both`，任何异常降级 `both`。both 模式按库配额 `ceil(k/2)` 合并，不做跨库分数排序。spec: `docs/superpowers/specs/2026-08-04-plan-b-federated-routing-design.md`。

**Tech Stack:** Python 3.14 / FastAPI / chromadb / LiteLLM Router / bm25s (+CJK bigram) / pytest。无新依赖。

## Global Constraints

- 工作目录一律 `sdtm-pedia/sdtm-rag/`；测试命令 `python -m pytest`（venv `.venv` 已配好；若 python 不对则 `./.venv/bin/python`）。
- 测试基线 **669 passed** 只增不减；每个 task 结束跑全量。
- 基线数字（不得回归）：study 25 计分题 source recall **≥88.5%**（hybrid+CJK bigram）；CDISC 140 题 **≥81.1%**（retrieval-only+hybrid+structured-lookup）。
- 路由闸：165 题（140 cdisc + 25 study 计分题）exact 准确率 **≥95%**，跑 **3 遍**；**错成对侧单库的题数必须为 0**（both 是唯一可容错向）。
- 红线：任何提交文件不得含真实研究名/字段 OID/项目标签/单元格值。含题目文本的 run 产物只写 `data/study/st01/eval/runs/`（gitignored）。提交前用 `data/study/studies.local.yaml` 里的真名 grep 暂存 diff。
- TDD：每个功能先写失败测试。commit 信息中文，格式仿 `git log` 现有风格。
- eval 全程 `federation_enabled` 与服务无关（eval 自建引擎）；golden 评测不开联网搜索（本 plan 无搜索内容）。

---

### Task 1: eval 判据下沉 section 粒度 (Phase 0)

**Files:**
- Modify: `eval/run_eval.py:73-111`（`check_source_recall`）、`run_evaluation` 内调用处（~line 250）
- Test: `scripts/tests/test_source_recall_section.py`（新建）

**Interfaces:**
- Produces: `check_source_recall(retrieved_sources, expected_sources, any_of=None, retrieved_sections=None)` — 期望串含 `#` 时按 `路径#节` 双条件匹配：`path` 子串匹配 source **且** `sec` 子串匹配同一条目的 section。`retrieved_sections` 与 `retrieved_sources` 等长对齐（元素可 None）。纯路径写法行为逐字节不变（向后兼容）。
- 题集语法：`expected_sources: ["chapters/ch04.md#4.1"]`（`#` 后为 section 子串）。

- [ ] **Step 1: 写失败测试**

```python
# scripts/tests/test_source_recall_section.py
"""Phase 0: check_source_recall 的 file#section 粒度判据 (spec §2 Phase 0).

动机: CDISC 侧存在 222-chunk 单文件, 纯路径子串判别力≈0 (study_golden_v1.md 血的教训:
"文件含答案"≠"被召回的 chunk 含答案")。
"""
import pytest

from eval.run_eval import check_source_recall

SOURCES = ["chapters/ch04.md", "chapters/ch04.md", "domains/AE/spec.md"]
SECTIONS = ["4.1 Timing", "4.2 Duration", None]


def test_plain_path_behavior_unchanged():
    recall, hits, misses = check_source_recall(SOURCES, ["domains/AE/spec.md"])
    assert recall == 1.0 and hits == ["domains/AE/spec.md"] and misses == []


def test_section_gold_hit_requires_same_entry():
    # 路径命中但 section 在另一条目上 → 不算命中
    recall, _, misses = check_source_recall(
        SOURCES, ["chapters/ch04.md#4.9"], retrieved_sections=SECTIONS)
    assert recall == 0.0 and misses == ["chapters/ch04.md#4.9"]


def test_section_gold_hit():
    recall, hits, _ = check_source_recall(
        SOURCES, ["chapters/ch04.md#4.2"], retrieved_sections=SECTIONS)
    assert recall == 1.0 and hits == ["chapters/ch04.md#4.2"]


def test_section_gold_none_section_never_matches():
    recall, _, _ = check_source_recall(
        SOURCES, ["domains/AE/spec.md#1"], retrieved_sections=SECTIONS)
    assert recall == 0.0


def test_section_gold_without_sections_fails_loud():
    # 判据要求 section 但调用方没给 → fail loud, 不静默降级为路径匹配
    with pytest.raises(ValueError, match="retrieved_sections"):
        check_source_recall(SOURCES, ["chapters/ch04.md#4.1"])


def test_any_of_group_supports_section_syntax():
    recall, hits, _ = check_source_recall(
        SOURCES, [], any_of=["nope.md", "chapters/ch04.md#4.1"],
        retrieved_sections=SECTIONS)
    assert recall == 1.0 and "chapters/ch04.md#4.1" in hits


def test_length_mismatch_fails_loud():
    with pytest.raises(ValueError):
        check_source_recall(SOURCES, ["chapters/ch04.md#4.1"],
                            retrieved_sections=["only-one"])
```

- [ ] **Step 2: 跑测试确认失败**

Run: `python -m pytest scripts/tests/test_source_recall_section.py -v`
Expected: FAIL（`retrieved_sections` 参数不存在 / section 语法未实现）

- [ ] **Step 3: 实现**

在 `check_source_recall` 加第四参数并抽出匹配器（docstring 保留原有"血的教训"段，追加 section 语法说明）：

```python
def check_source_recall(
    retrieved_sources: list[str],
    expected_sources: list[str],
    any_of: list[str] | None = None,
    retrieved_sections: list[str | None] | None = None,
) -> tuple[float, list[str], list[str]]:
```

```python
    def _matches(exp: str) -> bool:
        if "#" in exp:
            if retrieved_sections is None:
                raise ValueError(
                    f"section-level gold {exp!r} requires retrieved_sections "
                    "(caller must pass [c.section for c in chunks])"
                )
            if len(retrieved_sections) != len(retrieved_sources):
                raise ValueError("retrieved_sections length mismatch")
            path, sec = exp.split("#", 1)
            return any(
                path in src and sec in (s or "")
                for src, s in zip(retrieved_sources, retrieved_sections)
            )
        return any(exp in src for src in retrieved_sources)
```

原 `found = any(exp in src ...)` 与 any_of 组的 `any(e in src ...)` 全部改为 `_matches(exp)` / `_matches(e)`；hits/misses append 语义不变。

`run_evaluation` 中调用处（`chunks = rag.retrieve(...)` 之后）：

```python
        src_recall, src_hits, src_misses = check_source_recall(
            retrieved_sources,
            q.get("expected_sources", []),
            any_of=q.get("expected_sources_any"),
            retrieved_sections=[c.section for c in chunks],
        )
```

- [ ] **Step 4: 跑新测试 + 既有 eval 测试**

Run: `python -m pytest scripts/tests/test_source_recall_section.py scripts/tests/test_run_eval_flags.py scripts/tests/test_run_eval_judge.py -v`
Expected: 全 PASS（向后兼容闸）

- [ ] **Step 5: 全量测试**

Run: `python -m pytest -q`
Expected: ≥669+7 passed

- [ ] **Step 6: Commit**

```bash
git add eval/run_eval.py scripts/tests/test_source_recall_section.py
git commit -m "feat(eval): source 判据下沉 section 粒度 (Plan B Phase 0)"
```

---

### Task 2: server/federation.py — 路由 + 联邦引擎

**Files:**
- Modify: `server/rag.py:19-30`（`RetrievedChunk` 加 `corpus` 字段）
- Create: `server/federation.py`
- Test: `scripts/tests/test_federation.py`（新建）

**Interfaces:**
- Consumes: `RAGEngine.retrieve(query, *, domain=None, file_type=None, top_k=None) -> list[RetrievedChunk]`、`RAGEngine.format_context(chunks) -> str`、`RAGEngine.build_messages(question, context, history=None) -> list[dict]`、`RAGEngine.system_prompt` property。llm_router: LiteLLM Router，`completion(model="light", messages=..., temperature=0)`。
- Produces（Task 3/5/6 依赖，签名务必一致）:
  - `RetrievedChunk.corpus: str = ""`（dataclass 新末位字段，默认空串保证既有构造不破）
  - `federation.route_corpus(llm_router, question: str) -> tuple[str, bool]`（corpus, fallback_used）
  - `federation.FederatedEngine(cdisc, study, llm_router, top_k=15)`，方法：
    - `.retrieve(question, *, corpus="auto", top_k=None, domain=None, file_type=None) -> tuple[list[RetrievedChunk], str]`（chunks, routed_corpus；domain/file_type 只透传给 cdisc 引擎）
    - `.format_context(chunks) -> str`（按 corpus 分组，组头 `# 【標準 CDISC】` / `# 【本研究 (study)】`）
    - `.build_messages(question, context, history=None, *, corpus) -> list[dict]`
  - `federation.VALID_CORPORA = ("cdisc", "study", "both")`

- [ ] **Step 1: RetrievedChunk 加字段（无需独立测试，全量套件即回归闸）**

`server/rag.py` dataclass 末尾加：

```python
    corpus: str = ""  # Plan B federation: "cdisc" | "study"; 空串 = 未标注 (单库路径)
```

- [ ] **Step 2: 写失败测试**

```python
# scripts/tests/test_federation.py
"""Plan B Phase 1: route_corpus + FederatedEngine (spec §1.1-1.3).

路由是全计划唯一非确定性组件 — 测试全部用 fake llm_router 钉死行为边界:
合法 JSON 三值 / 包噪声 JSON / 非法值 / 异常 → 兜底 both (宁可多查)。
引擎侧用 stub (duck-typed), 不碰 chroma。
"""
from types import SimpleNamespace

import pytest

from server.federation import VALID_CORPORA, FederatedEngine, route_corpus
from server.rag import RetrievedChunk


def _resp(text):
    return SimpleNamespace(choices=[SimpleNamespace(message=SimpleNamespace(content=text))])


class _FakeLLM:
    def __init__(self, text=None, exc=None):
        self.text, self.exc, self.calls = text, exc, []

    def completion(self, model, messages, **kw):
        self.calls.append({"model": model, **kw})
        if self.exc:
            raise self.exc
        return _resp(self.text)


class _StubEngine:
    def __init__(self, name, n=20):
        self.name = name
        self.system_prompt = f"SYS-{name}"
        self._chunks = [
            RetrievedChunk(chunk_id=f"{name}-{i}", source=f"{name}/f{i}.md",
                           domain=None, file_type=None, section=None,
                           similarity=0.9 - i * 0.01, text=f"t{i}")
            for i in range(n)
        ]
        self.retrieve_kwargs = None

    def retrieve(self, q, *, domain=None, file_type=None, top_k=None):
        self.retrieve_kwargs = {"domain": domain, "file_type": file_type, "top_k": top_k}
        return self._chunks[: (top_k or 15)]

    def format_context(self, chunks):
        return f"CTX-{self.name}({len(chunks)})"

    def build_messages(self, q, ctx, history=None):
        return [{"role": "system", "content": self.system_prompt},
                {"role": "user", "content": f"{ctx}\n{q}"}]


# ── route_corpus ──

@pytest.mark.parametrize("corpus", VALID_CORPORA)
def test_route_valid_json(corpus):
    got, fallback = route_corpus(_FakeLLM(f'{{"corpus": "{corpus}"}}'), "q")
    assert got == corpus and fallback is False


def test_route_json_embedded_in_prose():
    got, fallback = route_corpus(_FakeLLM('Sure! {"corpus": "study"} hope that helps'), "q")
    assert got == "study" and fallback is False


@pytest.mark.parametrize("bad", ['{"corpus": "everything"}', "not json", ""])
def test_route_bad_output_falls_back_both(bad):
    got, fallback = route_corpus(_FakeLLM(bad), "q")
    assert got == "both" and fallback is True


def test_route_exception_falls_back_both():
    got, fallback = route_corpus(_FakeLLM(exc=RuntimeError("timeout")), "q")
    assert got == "both" and fallback is True


def test_route_uses_light_model_temperature_zero():
    llm = _FakeLLM('{"corpus": "cdisc"}')
    route_corpus(llm, "q")
    assert llm.calls[0]["model"] == "light" and llm.calls[0]["temperature"] == 0


# ── FederatedEngine ──

def _fed(llm_text='{"corpus": "cdisc"}'):
    cd, st = _StubEngine("cdisc"), _StubEngine("study")
    return FederatedEngine(cd, st, _FakeLLM(llm_text), top_k=15), cd, st


def test_explicit_corpus_skips_llm():
    fed, cd, st = _fed()
    fed.llm_router = _FakeLLM(exc=RuntimeError("must not be called"))
    chunks, routed = fed.retrieve("q", corpus="study")
    assert routed == "study" and all(c.corpus == "study" for c in chunks)
    assert len(chunks) == 15 and cd.retrieve_kwargs is None


def test_auto_routes_via_llm():
    fed, cd, st = _fed('{"corpus": "cdisc"}')
    chunks, routed = fed.retrieve("q", corpus="auto")
    assert routed == "cdisc" and all(c.corpus == "cdisc" for c in chunks)
    assert st.retrieve_kwargs is None


def test_both_quota_ceil_half_each_no_score_sort():
    fed, cd, st = _fed()
    chunks, routed = fed.retrieve("q", corpus="both", top_k=15)
    assert routed == "both"
    assert [c.corpus for c in chunks] == ["cdisc"] * 8 + ["study"] * 8  # ceil(15/2)=8, 分组不混排
    assert cd.retrieve_kwargs["top_k"] == 8 and st.retrieve_kwargs["top_k"] == 8


def test_domain_filter_forwarded_to_cdisc_only():
    fed, cd, st = _fed()
    fed.retrieve("q", corpus="both", domain="AE")
    assert cd.retrieve_kwargs["domain"] == "AE"
    assert st.retrieve_kwargs["domain"] is None


def test_invalid_corpus_rejected():
    fed, _, _ = _fed()
    with pytest.raises(ValueError):
        fed.retrieve("q", corpus="everything")


def test_format_context_groups_by_corpus():
    fed, _, _ = _fed()
    chunks, _ = fed.retrieve("q", corpus="both", top_k=4)
    ctx = fed.format_context(chunks)
    assert "【標準 CDISC】" in ctx and "【本研究 (study)】" in ctx
    assert "CTX-cdisc(2)" in ctx and "CTX-study(2)" in ctx
    assert ctx.index("CDISC") < ctx.index("本研究")


def test_build_messages_system_per_corpus():
    fed, _, _ = _fed()
    single = fed.build_messages("q", "CTX", corpus="study")
    assert single[0]["role"] == "system"
    assert "SYS-study" in single[0]["content"] and "SYS-cdisc" not in single[0]["content"]
    both = fed.build_messages("q", "CTX", corpus="both")
    assert "SYS-cdisc" in both[0]["content"] and "SYS-study" in both[0]["content"]
    # 联邦规则恒在 (标源库 + 跨库推理性标注)
    for msgs in (single, both):
        assert "Federation rules" in msgs[0]["content"]
```

- [ ] **Step 3: 跑测试确认失败**

Run: `python -m pytest scripts/tests/test_federation.py -v`
Expected: FAIL（`server.federation` 不存在）

- [ ] **Step 4: 实现 server/federation.py**

```python
"""Plan B 联邦路由: 双库组合 + LLM 判库 + 配额合并 (spec 2026-08-04 §1).

设计要点:
- 组合而非改造: 两个 RAGEngine 各自保留 BM25 索引 (study 侧天然 CJK bigram) 与直查通道。
- LLM 路由是全计划唯一非确定性组件: temperature 0 + 严格 JSON + 任何异常降级 "both"
  (兜底方向 = 宁可多查不可漏查; 路由准确率由 eval/run_routing_eval.py 三遍闸把守)。
- both 合并不做跨库分数排序 —— 两库相似度分布不可比, 按库配额 ceil(k/2) 分组拼接。
"""
from __future__ import annotations

import json
import math

import structlog

log = structlog.get_logger()

VALID_CORPORA = ("cdisc", "study", "both")

_ROUTER_SYSTEM = """You are a corpus router for a clinical-data Q&A service. Two corpora exist:
- "cdisc": the public CDISC SDTM standard — domains (DM, AE, VS, ...), variables, controlled \
terminology, implementation-guide chapters. English content.
- "study": ONE specific clinical study's EDC field cards — forms/screens, field labels, item \
groups, display conditions, units. Japanese EDC vocabulary.
Decide which corpus the question needs. Use "both" when it maps study fields to the SDTM \
standard, touches both, or you are unsure.
Respond with ONLY this JSON, nothing else: {"corpus": "cdisc"} or {"corpus": "study"} or {"corpus": "both"}"""

_FEDERATION_RULES = (
    "\n\n## Federation rules\n"
    "- Retrieved context may come from two corpora: 【標準 CDISC】 (public SDTM standard) and "
    "【本研究 (study)】 (this study's EDC field cards). Always state which corpus each claim "
    "comes from.\n"
    "- EDC↔SDTM mapping questions: NO mapping document exists in either corpus — any mapping "
    "you state is inference. Label it explicitly (推測/inference), never present it as documented "
    "fact.\n"
)


def route_corpus(llm_router, question: str) -> tuple[str, bool]:
    """判库. 返回 (corpus, fallback_used). 任何异常 → ("both", True)."""
    try:
        resp = llm_router.completion(
            model="light",
            messages=[
                {"role": "system", "content": _ROUTER_SYSTEM},
                {"role": "user", "content": question},
            ],
            temperature=0,
        )
        raw = (resp.choices[0].message.content or "").strip()
        start, end = raw.find("{"), raw.rfind("}")
        if start < 0 or end <= start:
            raise ValueError(f"no JSON object in router output: {raw!r}")
        corpus = json.loads(raw[start : end + 1])["corpus"]
        if corpus not in VALID_CORPORA:
            raise ValueError(f"invalid corpus {corpus!r}")
        return corpus, False
    except Exception:
        log.warning("route_corpus_fallback_both", exc_info=True)
        return "both", True


class FederatedEngine:
    def __init__(self, cdisc, study, llm_router, top_k: int = 15):
        self.cdisc = cdisc
        self.study = study
        self.llm_router = llm_router
        self.top_k = top_k

    def retrieve(
        self,
        question: str,
        *,
        corpus: str = "auto",
        top_k: int | None = None,
        domain: str | None = None,
        file_type: str | None = None,
    ):
        """返回 (chunks, routed_corpus). domain/file_type 是 CDISC 侧概念, 只透传 cdisc 引擎."""
        if corpus not in ("auto", *VALID_CORPORA):
            raise ValueError(f"corpus must be auto|cdisc|study|both, got {corpus!r}")
        k = top_k or self.top_k
        routed = corpus
        if corpus == "auto":
            routed, fallback = route_corpus(self.llm_router, question)
            log.info("federation_routed", corpus=routed, fallback=fallback)
        if routed == "cdisc":
            chunks = self.cdisc.retrieve(question, domain=domain, file_type=file_type, top_k=k)
            for c in chunks:
                c.corpus = "cdisc"
            return chunks, routed
        if routed == "study":
            chunks = self.study.retrieve(question, top_k=k)
            for c in chunks:
                c.corpus = "study"
            return chunks, routed
        # both: 按库配额, 分组拼接 (cdisc 先), 不做跨库分数排序
        k_each = math.ceil(k / 2)
        cd = self.cdisc.retrieve(question, domain=domain, file_type=file_type, top_k=k_each)
        st = self.study.retrieve(question, top_k=k_each)
        for c in cd:
            c.corpus = "cdisc"
        for c in st:
            c.corpus = "study"
        return cd + st, "both"

    def format_context(self, chunks) -> str:
        cd = [c for c in chunks if c.corpus == "cdisc"]
        st = [c for c in chunks if c.corpus == "study"]
        parts = []
        if cd:
            parts.append("# 【標準 CDISC】\n" + self.cdisc.format_context(cd))
        if st:
            parts.append("# 【本研究 (study)】\n" + self.study.format_context(st))
        return "\n\n".join(parts)

    def build_messages(self, question, context, history=None, *, corpus: str):
        # 委托 cdisc 引擎产出消息结构 (user 消息格式与单库路径逐字节一致), 只替换 system
        msgs = self.cdisc.build_messages(question, context, history)
        msgs[0] = {"role": "system", "content": self._system_for(corpus)}
        return msgs

    def _system_for(self, corpus: str) -> str:
        if corpus == "cdisc":
            base = self.cdisc.system_prompt
        elif corpus == "study":
            base = self.study.system_prompt
        else:
            base = self.cdisc.system_prompt + "\n\n" + self.study.system_prompt
        return base + _FEDERATION_RULES
```

注意: `build_messages` 假设 `RAGEngine.build_messages` 返回的 `msgs[0]` 是 system 消息——实现前先看 `server/rag.py:698` 确认（现状是 `messages[0] = {"role": "system", ...}`，若不符按实际调整并改测试）。

- [ ] **Step 5: 跑测试确认通过**

Run: `python -m pytest scripts/tests/test_federation.py -v`
Expected: 全 PASS

- [ ] **Step 6: 全量 + mypy**

Run: `python -m pytest -q && python -m mypy server/federation.py`
Expected: passed 只增；mypy clean（项目有 mypy 就跑，没有配置则跳过）

- [ ] **Step 7: Commit**

```bash
git add server/rag.py server/federation.py scripts/tests/test_federation.py
git commit -m "feat(federation): LLM 判库 + FederatedEngine 配额合并 (Plan B Phase 1)"
```

---

### Task 3: Settings + 服务接线 + API corpus 参数

**Files:**
- Modify: `server/config.py`（~line 33 `collection_name` 附近加三字段）
- Modify: `server/main.py`（lifespan，`app.state.rag = RAGEngine(...)` 之后）
- Modify: `server/router.py`（`AskRequest`/`AskStreamRequest`/`SourceItem`/`AskResponse`；`ask`/`ask_stream` 主体；`/api/info`）
- Test: `scripts/tests/test_federation_api.py`（新建）

**Interfaces:**
- Consumes: Task 2 的 `FederatedEngine` 全部签名。
- Produces:
  - Settings: `federation_enabled: bool = False`（本 task 默认关，Task 7 过闸后翻 True）、`study_collection_name: str = "study_st01"`、`study_kb_root: Path`（默认 `data/study/st01`，写法仿 `kb_root` 现有默认值的构造方式）
  - `app.state.federation: FederatedEngine | None`
  - API: 请求字段 `corpus: Literal["auto","cdisc","study","both"] = "auto"`；`SourceItem.corpus: str | None = None`；`AskResponse.routed_corpus: str | None = None`；ask_stream 的 `sources` 事件 data 加 `"routed_corpus"` 键；`/api/info` 加 `"federation": bool`

- [ ] **Step 1: 写失败测试**

```python
# scripts/tests/test_federation_api.py
"""Plan B Phase 1: API 层联邦接线. Fake FederatedEngine, 不碰 chroma/LLM.

关键边界: federation 关闭 (app.state.federation=None) 时行为与现状逐字节一致;
routed=study 时跳过 CDISC 专用 structured answerer。
"""
from types import SimpleNamespace

from fastapi import FastAPI
from fastapi.testclient import TestClient

from server.config import Settings
from server.router import api_router


def _chunk(corpus):
    return SimpleNamespace(chunk_id=f"{corpus}-1", source=f"{corpus}/f.md", domain=None,
                           file_type=None, section=None, similarity=0.9,
                           text="x" * 400, corpus=corpus)


class _FakeFed:
    def __init__(self, routed="study"):
        self.routed = routed
        self.calls = []

    def retrieve(self, q, *, corpus="auto", top_k=None, domain=None, file_type=None):
        self.calls.append(corpus)
        return [_chunk("study"), _chunk("cdisc")], self.routed

    def format_context(self, chunks):
        return "FED-CTX"

    def build_messages(self, q, ctx, history=None, *, corpus):
        return [{"role": "system", "content": f"S-{corpus}"},
                {"role": "user", "content": q}]


class _FakeLLM:
    def completion(self, model, messages, **kw):
        return SimpleNamespace(
            choices=[SimpleNamespace(message=SimpleNamespace(content="ANS"))],
            model="m", usage=None)


class _Answerer:
    def __init__(self):
        self.called = False

    def resolve(self, q):
        self.called = True
        return None


def _client(fed=None, answerer=None):
    app = FastAPI()
    app.include_router(api_router)
    app.state.rag = None  # federation 路径不得触碰单库引擎
    app.state.llm_router = _FakeLLM()
    app.state.settings = Settings()
    app.state.federation = fed
    if answerer is not None:
        app.state.answerer = answerer
    return TestClient(app)


def test_ask_federated_returns_corpus_and_routed():
    r = _client(fed=_FakeFed(routed="study")).post(
        "/api/ask", json={"question": "画面の項目は?", "corpus": "auto"})
    assert r.status_code == 200
    body = r.json()
    assert body["routed_corpus"] == "study"
    assert {s["corpus"] for s in body["sources"]} == {"study", "cdisc"}


def test_ask_corpus_passthrough():
    fed = _FakeFed()
    _client(fed=fed).post("/api/ask", json={"question": "q", "corpus": "both"})
    assert fed.calls == ["both"]


def test_ask_invalid_corpus_422():
    r = _client(fed=_FakeFed()).post("/api/ask", json={"question": "q", "corpus": "all"})
    assert r.status_code == 422


def test_ask_routed_study_skips_cdisc_answerer():
    ans = _Answerer()
    _client(fed=_FakeFed(routed="study"), answerer=ans).post(
        "/api/ask", json={"question": "q"})
    assert ans.called is False


def test_ask_routed_cdisc_keeps_answerer():
    ans = _Answerer()
    _client(fed=_FakeFed(routed="cdisc"), answerer=ans).post(
        "/api/ask", json={"question": "q"})
    assert ans.called is True


def test_ask_stream_sources_event_carries_routed_corpus():
    # ask_stream 用 async llm; 复用 test_ask_stream.py 的 _FakeRouter 形态
    from scripts.tests.test_ask_stream import _FakeRouter
    app = FastAPI()
    app.include_router(api_router)
    app.state.rag = None
    app.state.llm_router = _FakeRouter()
    app.state.settings = Settings()
    app.state.federation = _FakeFed(routed="both")
    r = TestClient(app).post("/api/ask_stream", json={"question": "q", "corpus": "auto"})
    assert r.status_code == 200
    assert '"routed_corpus": "both"' in r.text
    assert '"corpus": "study"' in r.text
```

（若 `scripts.tests.test_ask_stream` 不可 import——无 `__init__`——则把 `_FakeRouter` 复制进本文件，勿改动原文件。）

- [ ] **Step 2: 跑测试确认失败**

Run: `python -m pytest scripts/tests/test_federation_api.py -v`
Expected: FAIL

- [ ] **Step 3: 实现 config.py**

`collection_name` 字段附近：

```python
    # ── Plan B 联邦路由 (spec docs/superpowers/specs/2026-08-04-plan-b-federated-routing-design.md) ──
    # 默认关; Phase 1 全部 eval 闸过绿后翻 True (含义: 服务启动时构建 study 引擎 + 联邦层)。
    federation_enabled: bool = False
    study_collection_name: str = "study_st01"
    study_kb_root: Path = ...  # 仿 kb_root 默认值写法, 指向 data/study/st01 (含 ROUTING.md/INDEX.md/cards)
```

（`...` 处按 `kb_root` 现有默认值的相同构造方式写，指向 `data/study/st01`。）

- [ ] **Step 4: 实现 main.py lifespan 接线**

`app.state.rag = RAGEngine(...)` 块之后：

```python
    app.state.federation = None
    if s.federation_enabled:
        # study 引擎: S1 结构化直查是 CDISC 专用故恒关 (先例: run_eval --collection 同此);
        # hybrid 沿用生产开关 (study 侧经 ja_tokenize 天然获得 CJK bigram)。
        # 配置错误 (collection 不存在/ROUTING.md 缺失) 一律 fail loud — 显式开着 federation
        # 却静默退化成单库, 比启动失败更危险。
        rag_study = RAGEngine(
            chroma_dir=s.chroma_dir,
            kb_root=s.study_kb_root,
            collection_name=s.study_collection_name,
            embedding_model=s.embedding_model,
            top_k=s.top_k,
            structured_lookup_enabled=False,
            hybrid_enabled=s.hybrid_enabled,
            hybrid_fusion=s.hybrid_fusion,
            hybrid_alpha=s.hybrid_alpha,
            hybrid_pool=s.hybrid_pool,
            prompt_guardrail_enabled=s.prompt_guardrail_enabled,
        )
        from server.federation import FederatedEngine
        app.state.federation = FederatedEngine(
            app.state.rag, rag_study, app.state.llm_router, top_k=s.top_k
        )
        log.info("federation", study_collection=s.study_collection_name)
```

（注意顺序：必须在 `app.state.llm_router = create_router(s)` 之后。若现状 rag 先于 llm_router 构建，把 federation 块放在 llm_router 行之后。）

- [ ] **Step 5: 实现 router.py**

模型字段（`Literal` 已 import）：

```python
class AskRequest(BaseModel):
    ...
    corpus: Literal["auto", "cdisc", "study", "both"] = "auto"
```

`AskStreamRequest` 同样加。`SourceItem` 加 `corpus: str | None = None`；`AskResponse` 加 `routed_corpus: str | None = None`。

`ask()` 检索段改为：

```python
    fed = getattr(request.app.state, "federation", None)
    routed: str | None = None
    try:
        if fed is not None:
            chunks, routed = fed.retrieve(
                body.question, corpus=body.corpus, top_k=body.top_k,
                domain=body.domain, file_type=body.file_type,
            )
        else:
            chunks = rag.retrieve(
                body.question, domain=body.domain,
                file_type=body.file_type, top_k=body.top_k,
            )
    except Exception as e:
        log.error("retrieve_failed", error=str(e), exc_info=True)
        raise HTTPException(status_code=502, detail="Retrieval service temporarily unavailable.") from e
```

answerer 段（S1/CompositeAnswerer 是 CDISC 专用）：

```python
    answerer = getattr(request.app.state, "answerer", None)
    if routed == "study":
        answerer = None  # CDISC 专用事实通道, study 单库路由下必须静默跳过
```

context/messages 段：

```python
    engine = fed if fed is not None else rag
    context = engine.format_context(chunks)
    ...
    if fed is not None:
        messages = fed.build_messages(body.question, context, history_dicts or None,
                                      corpus=routed or body.corpus)
    else:
        messages = rag.build_messages(body.question, context, history_dicts or None)
```

sources 构造加 `corpus=c.corpus or None`（`getattr(c, "corpus", None) or None` 更稳）；`AskResponse(..., routed_corpus=routed)`。

`ask_stream()` 同构改造；sources 事件：

```python
    yield sse("sources", {"sources": sources, "routed_corpus": routed})
```

`/api/info`（现有 handler 内）响应加 `"federation": request.app.state.federation is not None`。

- [ ] **Step 6: 跑新测试 + 既有 API 测试**

Run: `python -m pytest scripts/tests/test_federation_api.py scripts/tests/test_ask_stream.py scripts/tests/test_router_structured.py scripts/tests/test_phase3_security.py -v`
Expected: 全 PASS（federation=None 回归闸靠既有测试）

- [ ] **Step 7: 全量测试**

Run: `python -m pytest -q`
Expected: passed 只增

- [ ] **Step 8: Commit**

```bash
git add server/config.py server/main.py server/router.py scripts/tests/test_federation_api.py
git commit -m "feat(api): 联邦路由接线 — corpus 参数 + routed_corpus + study 引擎构建 (默认关)"
```

---

### Task 4: webchat 前端 — 库选择 + 来源徽章

**Files:**
- Modify: `webchat/index.html`（30 行；topbar 加 select）
- Modify: `webchat/app.js`（~line 199 请求体；sources 渲染处；topbar /api/info 处 ~line 338）
- Modify: `webchat/style.css`（徽章样式）

**Interfaces:**
- Consumes: Task 3 的 API（请求 `corpus` 字段；sources 事件的 `routed_corpus` + 每条 source 的 `corpus`；`/api/info` 的 `federation`）。

无 JS 测试基建——本 task 以 Playwright 手动冒烟验收（Step 4）。

- [ ] **Step 1: index.html topbar 加选择器**

```html
<select id="corpus" title="検索対象コーパス">
  <option value="auto" selected>自動</option>
  <option value="cdisc">標準 (CDISC)</option>
  <option value="study">本研究</option>
  <option value="both">両方</option>
</select>
```

`/api/info` 返回 `federation: false` 时隐藏该控件（app.js 里 `document.getElementById("corpus").hidden = !info.federation`）。

- [ ] **Step 2: app.js 请求体 + 渲染**

fetch 体（line ~199）：

```js
body: JSON.stringify({ question, history, corpus: document.getElementById("corpus").value }),
```

sources 事件处理处：每条 source 渲染前缀徽章，`src.corpus === "study"` → `本研究`，`"cdisc"` → `標準`，空/无字段 → 不显示徽章（联邦关闭时零变化）。`routed_corpus` 显示在答案元信息行（现有 model 显示旁）：`判定: 標準/本研究/両方`。

```js
const CORPUS_LABEL = { cdisc: "標準", study: "本研究", both: "両方" };
```

- [ ] **Step 3: style.css 徽章**

```css
.corpus-badge { font-size: 11px; padding: 0 4px; border-radius: 3px; margin-right: 4px;
  background: var(--badge-bg, #e0e7ff); }
.corpus-badge.study { background: var(--badge-study-bg, #ffe4e6); }
```

- [ ] **Step 4: 冒烟（federation 默认还是关的——用临时 env 开）**

```bash
SDTM_RAG_FEDERATION_ENABLED=true python -m uvicorn server.main:app --port 8010
```

（pydantic-settings env 前缀按 `server/config.py` 现有约定拼；若前缀不同以实际为准。）
用 playwright/浏览器打开 `http://127.0.0.1:8010`：① 下拉可见且默认 自動；② 选 本研究 问一题日文 EDC 问题 → 来源全部带 本研究 徽章；③ 选 標準 问 "AE domain の必須変数は?" → 標準 徽章；④ 判定行显示 routed corpus。停掉临时服务。

- [ ] **Step 5: Commit**

```bash
git add webchat/
git commit -m "feat(webchat): corpus 切换下拉 + 来源库徽章 + 判定显示"
```

---

### Task 5: 路由准确率闸 — run_routing_eval.py + 三遍执行

**Files:**
- Create: `eval/run_routing_eval.py`
- Test: `scripts/tests/test_run_routing_eval.py`（新建）

**Interfaces:**
- Consumes: `federation.route_corpus`；`eval.run_eval.load_test_set`；`server.llm_config.create_router`；gold 文件 `eval/test_set_v3.yml`（140 题，label=cdisc）+ `data/study/st01/eval/test_set_study_v1_1.yml`（27 题，剔除 `out_of_scope: true` 后 25 题，label=study）。
- Produces: CLI `python -m eval.run_routing_eval --runs 3`。逐题明细（含题目文本）只写 `data/study/st01/eval/runs/routing_run_N.json`；stdout 只打统计。退出码: 全闸过 0，否则 1。

**闸定义（写死在代码里）**: exact = predicted==gold；fatal = predicted 是单库且 != gold（cdisc→study 或 study→cdisc，双向都致命——错的单库=该题 recall 归零）；both 计入 non-exact 但非 fatal。PASS 条件：**每一遍** exact_acc ≥ 0.95 且 fatal == 0。另报三遍间逐题一致率（稳定性观测值，不设闸）。

- [ ] **Step 1: 写失败测试（纯打分逻辑，不碰 LLM）**

```python
# scripts/tests/test_run_routing_eval.py
"""Plan B Phase 1 闸 1: 路由打分逻辑. LLM 调用不进单测 (真实三遍在 eval 执行)."""
from eval.run_routing_eval import score_run

GOLD = [{"id": "q1", "gold": "cdisc"}, {"id": "q2", "gold": "study"},
        {"id": "q3", "gold": "study"}, {"id": "q4", "gold": "cdisc"}]


def test_all_exact():
    s = score_run(GOLD, {"q1": "cdisc", "q2": "study", "q3": "study", "q4": "cdisc"})
    assert s["exact_acc"] == 1.0 and s["fatal"] == 0 and s["passed"] is True


def test_both_is_nonfatal_but_not_exact():
    s = score_run(GOLD, {"q1": "cdisc", "q2": "both", "q3": "study", "q4": "cdisc"})
    assert s["exact_acc"] == 0.75 and s["fatal"] == 0
    assert s["passed"] is False  # 0.75 < 0.95


def test_wrong_single_corpus_is_fatal_both_directions():
    s = score_run(GOLD, {"q1": "study", "q2": "cdisc", "q3": "study", "q4": "cdisc"})
    assert s["fatal"] == 2 and s["passed"] is False
    assert {f["id"] for f in s["fatal_items"]} == {"q1", "q2"}


def test_missing_prediction_counts_fatal():
    # 断题 (LLM 全挂被 route_corpus 兜成 both 之外的缺失) 不许静默
    s = score_run(GOLD, {"q1": "cdisc", "q2": "study", "q3": "study"})
    assert s["fatal"] >= 1
```

- [ ] **Step 2: 跑测试确认失败**

Run: `python -m pytest scripts/tests/test_run_routing_eval.py -v`
Expected: FAIL（模块不存在）

- [ ] **Step 3: 实现**

```python
"""Plan B Phase 1 闸 1: 路由准确率三遍评测.

红线: 逐题明细 (含题目文本) 只写 data/study/st01/eval/runs/ (gitignored);
stdout 只打统计, 不打题目文本。
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from eval.run_eval import load_test_set
from server.config import settings
from server.federation import route_corpus
from server.llm_config import create_router

CDISC_SET = Path("eval/test_set_v3.yml")
STUDY_SET = Path("data/study/st01/eval/test_set_study_v1_1.yml")
RUNS_DIR = Path("data/study/st01/eval/runs")
EXACT_THRESHOLD = 0.95


def load_gold() -> list[dict]:
    items = [{"id": q["id"], "question": q["question"], "gold": "cdisc"}
             for q in load_test_set(str(CDISC_SET))]
    items += [{"id": f"st_{q['id']}", "question": q["question"], "gold": "study"}
              for q in load_test_set(str(STUDY_SET)) if not q.get("out_of_scope")]
    return items


def score_run(gold: list[dict], predictions: dict[str, str]) -> dict:
    exact = 0
    fatal_items = []
    for g in gold:
        pred = predictions.get(g["id"])
        if pred == g["gold"]:
            exact += 1
        elif pred != "both":  # 错的单库 or 缺失: 该题 recall 归零, 致命
            fatal_items.append({"id": g["id"], "gold": g["gold"], "pred": pred})
    acc = exact / len(gold)
    return {"n": len(gold), "exact": exact, "exact_acc": round(acc, 4),
            "fatal": len(fatal_items), "fatal_items": fatal_items,
            "passed": acc >= EXACT_THRESHOLD and not fatal_items}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--runs", type=int, default=3)
    args = parser.parse_args(argv)
    gold = load_gold()
    llm = create_router(settings)
    RUNS_DIR.mkdir(parents=True, exist_ok=True)

    all_passed = True
    per_run_preds: list[dict[str, str]] = []
    for run_i in range(1, args.runs + 1):
        preds: dict[str, str] = {}
        n_fallback = 0
        for g in gold:
            corpus, fallback = route_corpus(llm, g["question"])
            preds[g["id"]] = corpus
            n_fallback += fallback
        s = score_run(gold, preds)
        per_run_preds.append(preds)
        detail = [{**g, "pred": preds[g["id"]]} for g in gold]
        (RUNS_DIR / f"routing_run_{run_i}.json").write_text(
            json.dumps({"summary": {k: v for k, v in s.items() if k != "fatal_items"},
                        "detail": detail}, ensure_ascii=False, indent=1))
        print(f"run {run_i}: exact {s['exact']}/{s['n']} = {s['exact_acc']:.1%}  "
              f"fatal={s['fatal']}  fallback={n_fallback}  "
              f"{'PASS' if s['passed'] else 'FAIL'}")
        all_passed &= s["passed"]

    stable = sum(
        1 for g in gold
        if len({p[g["id"]] for p in per_run_preds}) == 1
    )
    print(f"stability: {stable}/{len(gold)} 题三遍判定一致")
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 4: 单测通过 + 全量**

Run: `python -m pytest scripts/tests/test_run_routing_eval.py -v && python -m pytest -q`
Expected: 全 PASS

- [ ] **Step 5: 真实三遍执行（闸 1）**

Run: `python -m eval.run_routing_eval --runs 3`
Expected: 三遍全部 `PASS`（exact ≥95%、fatal=0）、退出码 0。

若 FAIL：不改阈值、不改 gold。调 `_ROUTER_SYSTEM` 措辞（描述加细/加 few-shot），改完**重跑三遍**。fatal 题逐题看 `routing_run_N.json` 明细。prompt 迭代超过 3 轮仍 FAIL → 停下向用户报告（可能需要改路由方案，属 spec 变更）。

- [ ] **Step 6: 确认 runs 产物未被 git 追踪 + Commit**

```bash
git status --short data/study/  # 必须空
git add eval/run_routing_eval.py scripts/tests/test_run_routing_eval.py
git commit -m "feat(eval): 路由准确率三遍闸 — exact≥95% 且致命错向=0 (Plan B 闸 1)"
```

---

### Task 6: 端到端联邦 eval — run_eval --federated + 闸 2/3

**Files:**
- Modify: `eval/run_eval.py`（argparse + main 内引擎构建段 ~line 620-640）
- Test: `scripts/tests/test_run_eval_federated.py`（新建）

**Interfaces:**
- Consumes: `FederatedEngine`；Task 1 的 section 判据（已并入 run_evaluation）。
- Produces: `--federated` flag：自建 cdisc 引擎（`settings.collection_name`/`settings.kb_root`）+ study 引擎（`settings.study_collection_name`/`settings.study_kb_root`，S1 恒关）+ `FederatedEngine`，corpus="auto" 走全联邦路径。与 `--collection`/`--kb-root` 互斥（argparse error）。retrieval lever flags（--hybrid 等）同时作用于两个引擎。

- [ ] **Step 1: 写失败测试**

```python
# scripts/tests/test_run_eval_federated.py
"""--federated 的 adapter 与互斥闸. 引擎用 stub, 不碰 chroma."""
import pytest

from eval.run_eval import _FederatedAdapter, main
from server.rag import RetrievedChunk


class _FakeFed:
    def retrieve(self, q, *, corpus="auto", top_k=None, domain=None, file_type=None):
        assert corpus == "auto"
        c = RetrievedChunk(chunk_id="s-1", source="study/f.md", domain=None,
                           file_type=None, section="§2", similarity=0.9,
                           text="t", corpus="study")
        return [c], "study"


def test_adapter_unwraps_tuple_and_records_route():
    a = _FederatedAdapter(_FakeFed())
    chunks = a.retrieve("q", top_k=5)
    assert [c.source for c in chunks] == ["study/f.md"]
    assert a.routed == ["study"]


def test_federated_mutually_exclusive_with_collection(tmp_path, capsys):
    ts = tmp_path / "t.yml"
    ts.write_text("- id: q1\n  category: c\n  question: x\n  expected_sources: [a.md]\n")
    with pytest.raises(SystemExit):
        main([str(ts), "--retrieval-only", "--federated", "--collection", "study_st01"])
```

- [ ] **Step 2: 跑测试确认失败**

Run: `python -m pytest scripts/tests/test_run_eval_federated.py -v`
Expected: FAIL

- [ ] **Step 3: 实现**

argparse：

```python
    parser.add_argument(
        "--federated", action="store_true",
        help="Plan B: cdisc+study 双引擎 + LLM 路由 (corpus=auto) 走全联邦检索路径。"
             "与 --collection/--kb-root 互斥。study 引擎 S1 恒关。",
    )
```

main 内（`--collection` 处理段附近）：

```python
    if args.federated and (args.collection or args.kb_root):
        parser.error("--federated 与 --collection/--kb-root 互斥 (联邦模式引擎路径取自 settings)")
```

module 级 adapter（run_evaluation 的 `rag.retrieve(q, top_k=...)` 契约不变）：

```python
class _FederatedAdapter:
    """FederatedEngine → run_evaluation 的 rag 形状 (retrieve 返回 list, 记录判库)."""

    def __init__(self, fed):
        self.fed = fed
        self.routed: list[str] = []

    def retrieve(self, q, top_k=None):
        chunks, routed = self.fed.retrieve(q, corpus="auto", top_k=top_k)
        self.routed.append(routed)
        return chunks

    def format_context(self, chunks):
        return self.fed.format_context(chunks)

    def build_messages(self, q, context, history=None):
        return self.fed.build_messages(q, context, history, corpus="both")
```

引擎构建段：`--federated` 时构建两个 RAGEngine（cdisc 沿用现有构建参数含 `structured_lookup_enabled=structured_lookup`；study 用 `settings.study_collection_name`/`settings.study_kb_root` 且 `structured_lookup_enabled=False`，其余 lever 同 cdisc），包 `FederatedEngine(cdisc, study, create_router(settings), top_k=args.top_k)` 再包 `_FederatedAdapter`。评测结束在 summary 后打印判库分布：

```python
        from collections import Counter
        print(f"routing: {dict(Counter(rag.routed))}")
```

- [ ] **Step 4: 单测 + 全量通过**

Run: `python -m pytest scripts/tests/test_run_eval_federated.py -v && python -m pytest -q`
Expected: 全 PASS

- [ ] **Step 5: 控制组复现（基线钉死，两条都要）**

```bash
python -m eval.run_eval eval/test_set_v3.yml --retrieval-only --hybrid --structured-lookup \
  --output data/study/st01/eval/runs/planb_ctrl_cdisc.json
python -m eval.run_eval data/study/st01/eval/test_set_study_v1_1.yml --retrieval-only --hybrid \
  --collection study_st01 --kb-root data/study/st01 \
  --output data/study/st01/eval/runs/planb_ctrl_study.json
```

Expected: CDISC avg source recall = **81.1%**（±0，同索引同参必须复现；若不符，先查索引新鲜度 `python -m scripts.check_index_freshness`，勿继续）；study = **88.5%**。若命令旗标与基线记录有出入，以 `evidence/checkpoints/s4_full_eval_closure.md` 与 `study_golden_v1.md` §3.1b 记录的原始命令为准。

- [ ] **Step 6: 联邦组执行（闸 2/3）**

```bash
python -m eval.run_eval eval/test_set_v3.yml --retrieval-only --hybrid --structured-lookup \
  --federated --output data/study/st01/eval/runs/planb_fed_cdisc.json
python -m eval.run_eval data/study/st01/eval/test_set_study_v1_1.yml --retrieval-only --hybrid \
  --federated --output data/study/st01/eval/runs/planb_fed_study.json
```

Expected（闸）: 联邦路径下 CDISC **≥81.1%**、study **≥88.5%**。

若 study 侧跌破且 miss 集中在被路由为 both 的题（配额 8 < 15 深度损失）：预案 = both 模式配额从 `ceil(k/2)` 提为每库 k（`test_federation.py` 配额断言同步改），重跑本 step 两条 + Task 5 三遍闸。这是 spec 预留的有界升级，不算 spec 变更；改完在 commit 信息里写明。其他形态的回归 → 停下向用户报告。

- [ ] **Step 7: Commit**

```bash
git status --short data/study/  # 必须空
git add eval/run_eval.py scripts/tests/test_run_eval_federated.py
git commit -m "feat(eval): --federated 全联邦检索评测通道; 闸 2/3 过绿 (cdisc ≥81.1 / study ≥88.5)"
```

---

### Task 7: 默认启用 + 部署 + 证据归档 + 收尾

**Files:**
- Modify: `server/config.py`（`federation_enabled` 默认 True）
- Create: `sdtm-rag/evidence/checkpoints/planb_phase1_federation.md`
- Modify: `.work/meta/worklog/phase_07_rag_kg.md`、`docs/PROGRESS.md`、`CLAUDE.md`（Key Paths 一行）

**Interfaces:** 无新代码接口；本 task 是 rollout + 记录。

- [ ] **Step 1: 翻默认值**

```python
    federation_enabled: bool = True
```

Run: `python -m pytest -q` — Expected: 全 PASS（测试构造 Settings() 处若受影响，显式传 False 的 fake 已隔离；有挂的按测试意图修）。

- [ ] **Step 2: 重启服务 + 冒烟**

按 `sdtm-rag/deploy/` runbook 重启 `com.sdtmrag.api`（launchd）。然后：

```bash
curl -s http://127.0.0.1:8000/api/info | python -m json.tool   # federation: true, 索引新鲜度绿
curl -s http://127.0.0.1:8000/api/ask -H 'Content-Type: application/json' \
  -d '{"question": "AE domain の必須変数は?", "corpus": "auto"}' | python -m json.tool
```

Expected: 第二条 `routed_corpus` 为 `cdisc`，sources 全 cdisc。再问一条日文 EDC 画面问题（题目从 `data/study/st01/eval/` 题集里挑，**别写进本文档或 commit**），expected `routed_corpus: study`。浏览器过一遍 Task 4 的四点冒烟。

- [ ] **Step 3: 证据 checkpoint**

`evidence/checkpoints/planb_phase1_federation.md`，只含统计（红线同前）：三闸结果表（路由三遍 exact/fatal/fallback/稳定性；控制组 vs 联邦组两库数字）、both 配额最终值（8 或升级后的 k 及原因）、决策日志引用（spec D1-D7）、known limits（LLM 路由非确定性边界、跨库 best-effort 不进验收）。

- [ ] **Step 4: 收尾索引（按 CLAUDE.md wrap-up 清单）**

- `worklog/phase_07_rag_kg.md` append 本轮记录；
- `docs/PROGRESS.md` Phase 7 状态更新（Plan B Phase 0+1 DONE, 指向 checkpoint）；
- `CLAUDE.md` Key Paths 加一行（≤80 字符）: `| Plan B 联邦路由 Phase1 | server/federation.py + evidence planb_phase1_federation.md |`；
- 扫 CLAUDE.md 剪过期状态（"下一步 Plan B 联邦路由" 改为指向 Phase 2/3/4）。

- [ ] **Step 5: 真名扫描 + Commit + push**

```bash
REAL=$(python -c "import yaml,sys; r=yaml.safe_load(open('data/study/studies.local.yaml')); print(' '.join(str(v) for e in r.values() for v in e.values()))")
git add -A ':!data/study'
git diff --cached | grep -iF "$REAL" && echo LEAK || echo clean   # 必须 clean
git commit -m "feat(federation): Plan B Phase 0+1 收官 — 联邦路由默认启用, 三闸全绿"
git push
```

（真名扫描逻辑如与既有收尾脚本重复，用既有的。）

- [ ] **Step 6: 独立复审（规则 D）**

merge/收尾后按项目惯例发起独立复审（不同 subagent_type，非本 session 自审），范围：Task 1-6 的 diff + 三闸数字。复审 FAIL 项按严重度处理后才算 Phase 1 关闭。

---

## Self-Review 记录

- Spec 覆盖：Phase 0 → Task 1；§1.1-1.5 → Task 2/3/4；闸 1 → Task 5；闸 2/3 + hybrid 复核（联邦组即 hybrid 接线后重测）→ Task 6；rollout/安全决策记录 → Task 7。Phase 2/3/4 明确不在本 plan（各自独立成 plan）。
- 类型一致性：`retrieve` 返回 `tuple[list[RetrievedChunk], str]` 贯穿 Task 2/3/6；`corpus` 字段名全程一致；`_FederatedAdapter.routed` 命名在 Task 6 测试与实现一致。
- 已知留白（刻意，不是 placeholder）：`study_kb_root` 默认值构造与 env 前缀"仿现有写法"——这两处依赖 config.py 现场形态，执行者按同文件先例写，测试会兜住。
