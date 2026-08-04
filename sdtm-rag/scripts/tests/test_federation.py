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
