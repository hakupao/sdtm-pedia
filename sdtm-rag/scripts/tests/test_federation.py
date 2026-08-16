"""Plan B Phase 1: route_corpus + FederatedEngine (spec §1.1-1.3).

路由是全计划唯一非确定性组件 — 测试全部用 fake llm_router 钉死行为边界:
合法 JSON 三值 / 包噪声 JSON / 非法值 / 异常 → 兜底 both (宁可多查)。
引擎侧用 stub (duck-typed), 不碰 chroma。
"""
from types import SimpleNamespace

import pytest

from server.federation import _ROUTER_SYSTEM, VALID_CORPORA, FederatedEngine, route_corpus
from server.rag import RetrievedChunk


def _resp(text):
    return SimpleNamespace(choices=[SimpleNamespace(message=SimpleNamespace(content=text))])


class _FakeLLM:
    def __init__(self, text=None, exc=None):
        self.text, self.exc, self.calls = text, exc, []

    def completion(self, model, messages, **kw):
        self.calls.append({"model": model, "messages": messages, **kw})
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


# ── _ROUTER_SYSTEM 事实描述 ──

def test_router_prompt_describes_the_study_document_corpus():
    """C1 之后 study 库里除了 EDC 卡片还有本研究自己的手順/計画文書章节 chunk。

    判库 prompt 里 study 的语料描述若仍只写 field cards, 偏"标准味"的手順問題会被判给
    cdisc, 而 CDISC 库结构上答不出本研究的手順 (该题 recall 归零)。

    ⚠ 断言范围只取 study 那一条 bullet, 不是整段 prompt: 规则 1 的正文里早就有
    "our protocol" 这个词 (第一人称叙事的例子), 所以 `"protocol" in _ROUTER_SYSTEM.lower()`
    这种整段断言在改动**之前**就是绿的 = 装饰品, 不能用。
    """
    study_bullet = _ROUTER_SYSTEM.split("Decide which corpus")[0].split('- "study":')[1]
    assert "field cards" in study_bullet, "study 语料描述必须仍包含 EDC 卡片"
    low = study_bullet.lower()
    assert "protocol" in low and "section" in low, (
        "study 语料描述必须写明本研究自己的手順/計画文書章节 (protocol/procedure document sections)"
    )


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


def test_route_actually_sends_the_router_prompt_and_the_question():
    """上一条只钉 prompt 常量的**内容**; 这条钉它确实被**送出去**。

    变异实证 (2026-08-12, U2 Task 5): 把 route_corpus 送出的 system 换成空串、或把用户问题
    换成空串, 全量 1155 条测试**一条都不红** —— 判库整个 prompt 通道此前零覆盖, 只有跑 181
    题的 run_routing_eval (LLM, 不在 pytest 里) 才看得见。
    """
    llm = _FakeLLM('{"corpus": "cdisc"}')
    route_corpus(llm, "どの項目ですか")
    msgs = llm.calls[0]["messages"]
    assert msgs[0] == {"role": "system", "content": _ROUTER_SYSTEM}
    assert msgs[1] == {"role": "user", "content": "どの項目ですか"}


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


# ── U5: 逐题判库 fallback 观测属性 ──

class _U5StubEngine:
    def retrieve(self, question, *, top_k=None, **kw):
        return []


def _u5_fed():
    from server.federation import FederatedEngine
    return FederatedEngine(cdisc=_U5StubEngine(), study=_U5StubEngine(), llm_router=object())


def test_last_route_fallback_exists_before_any_retrieve():
    """观测属性得在构造期就存在: 只靠 retrieve 里赋值的话, 首次 retrieve 之前读到的是
    AttributeError, 而 eval 侧的 getattr 兜底会把它读成 None —— 缺属性伪装成"没回落"."""
    assert _u5_fed().last_route_fallback is None


def test_last_route_fallback_none_on_forced_corpus():
    fed = _u5_fed()
    fed.retrieve("q", corpus="study")
    assert fed.last_route_fallback is None


def test_last_route_fallback_records_auto_and_clears_on_forced(monkeypatch):
    fed = _u5_fed()
    monkeypatch.setattr("server.federation.route_corpus", lambda r, q: ("study", True))
    fed.retrieve("q", corpus="auto")
    assert fed.last_route_fallback is True
    fed.retrieve("q", corpus="both")  # 强制档必须清掉上一题的标志, 否则串题
    assert fed.last_route_fallback is None
