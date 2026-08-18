"""Plan B Phase 1: route_corpus + FederatedEngine (spec §1.1-1.3).

路由是全计划唯一非确定性组件 — 测试全部用 fake llm_router 钉死行为边界:
合法 JSON 三值 / 包噪声 JSON / 非法值 / 异常 → 兜底 both (宁可多查)。
引擎侧用 stub (duck-typed), 不碰 chroma。
"""
import logging
from types import SimpleNamespace

import pytest
import structlog

from server import federation
from server.federation import (
    _ROUTER_SYSTEM,
    VALID_CORPORA,
    FederatedEngine,
    decide_corpus,
    route_corpus,
)
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


# ── U6 T7: decide_corpus (判库 + 确定性信号纠偏挂点; 生产与 eval 同源) ──

class _SigStub:
    """signals 契约桩: widen_reason(routed, question) -> "study_sig" | "cdisc_sig" | None."""

    def __init__(self, reason=None):
        self.reason, self.calls = reason, []

    def widen_reason(self, routed, question):
        self.calls.append((routed, question))
        return self.reason


class _SigBoom:
    """一被问就炸 —— 用来钉「这条路径**不许**碰信号层」, 而不是事后数调用次数."""

    def widen_reason(self, routed, question):
        raise AssertionError("这条路径不该询问信号层")


def _route_stub(result, seen=None):
    def _route(llm_router, question):
        if seen is not None:
            seen.append((llm_router, question))
        return result
    return _route


@pytest.mark.parametrize("text", ['{"corpus": "cdisc"}', '{"corpus": "study"}',
                                  '{"corpus": "both"}', '{"corpus": "everything"}',
                                  "not json", ""])
def test_decide_corpus_without_signals_is_route_corpus_verbatim(text):
    """本 task 的行为不变承诺: signals 缺省时三元组前两位逐位等于裸 route_corpus (含兜底路径).

    对照物是**真跑一遍 route_corpus**, 不是另抄一份期望值 —— 抄的那份会跟着 route_corpus
    一起被改动, 证不了「同一条判库」。
    """
    expected = route_corpus(_FakeLLM(text), "q")
    assert decide_corpus(_FakeLLM(text), "q") == (*expected, None)          # 默认实参
    assert decide_corpus(_FakeLLM(text), "q", None) == (*expected, None)    # 显式 None


def test_decide_corpus_forwards_router_and_question_untouched(monkeypatch):
    """判库入参必须原样透传: 送错 router / 送空问题时上面那些断言照样全绿。"""
    seen = []
    monkeypatch.setattr(federation, "route_corpus", _route_stub(("cdisc", False), seen))
    llm = object()
    decide_corpus(llm, "どの項目ですか")
    assert seen == [(llm, "どの項目ですか")]


@pytest.mark.parametrize("routed,reason", [("cdisc", "study_sig"), ("study", "cdisc_sig")])
def test_decide_corpus_widens_single_corpus_to_both(monkeypatch, routed, reason):
    monkeypatch.setattr(federation, "route_corpus", _route_stub((routed, False)))
    sig = _SigStub(reason)
    assert decide_corpus(object(), "q", sig) == ("both", False, reason)
    assert sig.calls == [(routed, "q")], "信号层拿到的必须是**判库结果**与原问题"


@pytest.mark.parametrize("routed", ["cdisc", "study"])
def test_decide_corpus_keeps_corpus_when_no_signal_fires(monkeypatch, routed):
    monkeypatch.setattr(federation, "route_corpus", _route_stub((routed, False)))
    assert decide_corpus(object(), "q", _SigStub(None)) == (routed, False, None)


def test_decide_corpus_never_consults_signals_on_both(monkeypatch):
    """widen-only: both 已是最宽, 再问信号层只可能带来收窄/换库 —— 本设计明令禁止的方向."""
    monkeypatch.setattr(federation, "route_corpus", _route_stub(("both", False)))
    assert decide_corpus(object(), "q", _SigBoom()) == ("both", False, None)


def test_decide_corpus_keeps_fallback_flag_on_router_failure():
    """判库整个挂掉 → ("both", True): fallback 标志必须原样带出 (逐题取证靠它),
    且兜底出来的 both 同样不问信号层."""
    got = decide_corpus(_FakeLLM(exc=RuntimeError("timeout")), "q", _SigBoom())
    assert got == ("both", True, None)


def _sig_fed(signals=None):
    return FederatedEngine(cdisc=_U5StubEngine(), study=_U5StubEngine(),
                           llm_router=object(), signals=signals)


def test_signals_default_to_none_and_widened_attr_exists_before_any_retrieve():
    """默认不挂信号层 (Task 8 才接线); 观测属性得在构造期就存在 —— 理由同
    last_route_fallback: eval 侧的 getattr 兜底会把「缺属性」读成「没被拓宽」."""
    fed = _sig_fed()
    assert fed.signals is None and fed.last_signal_widened is None


def test_engine_auto_widens_and_records_the_reason(monkeypatch):
    monkeypatch.setattr(federation, "route_corpus", _route_stub(("cdisc", False)))
    sig = _SigStub("study_sig")
    fed = _sig_fed(sig)
    _, routed = fed.retrieve("q", corpus="auto")
    assert routed == "both", "信号 fire 后必须真的按 both 去检索, 不能只记个标志"
    assert fed.last_signal_widened == "study_sig"
    assert sig.calls == [("cdisc", "q")]


def test_engine_auto_goes_through_the_shared_decide_corpus(monkeypatch):
    """同源闸: 引擎里把「route_corpus + widen」再抄一份, 上面那些断言照样全绿 ——
    而 eval 侧调的是 decide_corpus, 两份实现从此各自漂移且无人看得见 (make_docs_engine 先例)."""
    calls = []
    real = federation.decide_corpus

    def _spy(llm_router, question, signals=None):
        calls.append((question, signals))
        return real(llm_router, question, signals)

    monkeypatch.setattr(federation, "decide_corpus", _spy)
    monkeypatch.setattr(federation, "route_corpus", _route_stub(("study", False)))
    sig = _SigStub(None)
    _sig_fed(sig).retrieve("q", corpus="auto")
    assert calls == [("q", sig)], "auto 档必须经 decide_corpus, 且把引擎自己的 signals 交出去"


@pytest.mark.parametrize("corpus", list(VALID_CORPORA))
def test_forced_corpus_never_consults_signals(corpus):
    fed = FederatedEngine(cdisc=_U5StubEngine(), study=_U5StubEngine(),
                          llm_router=_FakeLLM(exc=RuntimeError("must not be called")),
                          signals=_SigBoom())
    fed.retrieve("q", corpus=corpus)
    assert fed.last_signal_widened is None


def test_last_signal_widened_clears_on_the_next_forced_call(monkeypatch):
    monkeypatch.setattr(federation, "route_corpus", _route_stub(("study", False)))
    fed = _sig_fed(_SigStub("cdisc_sig"))
    fed.retrieve("q", corpus="auto")
    assert fed.last_signal_widened == "cdisc_sig"
    fed.retrieve("q", corpus="cdisc")  # 强制档必须清掉上一题的理由, 否则串题
    assert fed.last_signal_widened is None


class _LogSpy:
    def __init__(self):
        self.calls = []

    def info(self, event, **kw):
        self.calls.append((event, kw))

    def warning(self, *a, **kw):
        pass


def test_routed_log_line_carries_the_widen_reason_and_no_question_text(monkeypatch):
    """判库日志是「这题为什么查了两库」的唯一现场线索; 少 widened= 就只能看到一个无来由的 both.

    红线同时钉住: 该行不许带题面 (日志会进服务端 stdout / 排障贴文)。
    """
    spy = _LogSpy()
    monkeypatch.setattr(federation, "log", spy)
    monkeypatch.setattr(federation, "route_corpus", _route_stub(("cdisc", False)))
    _sig_fed(_SigStub("study_sig")).retrieve("どの項目ですか", corpus="auto")
    assert spy.calls == [("federation_routed",
                          {"corpus": "both", "fallback": False, "widened": "study_sig"})]
    assert "どの項目" not in repr(spy.calls)


# ── U6 T8: 信号层是**旁路**, 不是判库的必经之路 (控制器裁定 1/2) ──
#
# 信号层挂在生产 retrieve 上之后, 它每一种失效方式都必须收敛成「本题不拓宽」:
# 一个坏掉的信号层可以让判库退回 Task 6 冻结基线, 但绝不许让 /api/ask 返回 500。
# 反向的代价也已记账: 信号层若整条静默死掉, 条款 1 (fatal=0) 会在 Task 10 响亮地
# 不通过 —— 所以这里吞异常不会让"死掉的信号层"混过本单元。

class _SigRaises:
    def __init__(self, exc):
        self.exc = exc

    def widen_reason(self, routed, question):
        raise self.exc


class _SigBadValue:
    """返回白名单外的字符串 —— 契约违反, 与抛异常同路处理。"""

    def __init__(self, value):
        self.value = value

    def widen_reason(self, routed, question):
        return self.value


def _signal_warnings(logs):
    return [e for e in logs if e["event"] == "signal_layer_error"]


@pytest.mark.parametrize("exc", [RuntimeError("boom"), ValueError("bad"), KeyError("k")])
def test_decide_corpus_treats_a_raising_signal_layer_as_no_widen(monkeypatch, exc):
    monkeypatch.setattr(federation, "route_corpus", _route_stub(("cdisc", False)))
    with structlog.testing.capture_logs() as logs:
        assert decide_corpus(object(), "q", _SigRaises(exc)) == ("cdisc", False, None)
    warn = _signal_warnings(logs)
    assert warn and warn[0]["log_level"] == "warning", "静默吞掉 = 信号层死了也没人知道"
    assert warn[0]["kind"] == "raised"
    assert warn[0]["error"] == type(exc).__name__


@pytest.mark.parametrize("text", ['{"corpus": "cdisc"}', '{"corpus": "study"}',
                                  '{"corpus": "both"}', "not json"])
def test_decide_corpus_without_signals_is_silent_too(text):
    """「signals=None 时逐位等于裸 route_corpus」这条承诺的**日志面**。

    丢掉 `signals is not None` 那半合取后返回值逐位不变 —— `None.widen_reason(...)` 抛
    AttributeError, 被下面那道旁路原样吞掉 —— 但每一道题都会多出一条 signal_layer_error
    warning (finding F-15)。返回值面上一条已经钉住了, 缺的是这一面。
    """
    with structlog.testing.capture_logs() as logs:
        decide_corpus(_FakeLLM(text), "q")
        decide_corpus(_FakeLLM(text), "q", None)
    assert _signal_warnings(logs) == []


@pytest.mark.parametrize("bad", ["widen", "study", "both", "STUDY_SIG", "", 1, True])
def test_decide_corpus_rejects_reasons_outside_the_whitelist(monkeypatch, bad):
    """白名单是 widen-only 的最后一道结构闸: 信号层返回 "study" 之类的库名时,
    不设闸的实现会照样拓宽并把库名写进逐题观测字段, 让下游读成一次合法拓宽。

    kind 必须是 not_whitelisted 而非 wrong_direction: 方向闸恰好也会拦下所有表外取值,
    两条闸因此在"拦没拦住"这一层不可分 —— 只有现场报出破的是哪条契约, 白名单这条闸
    才是活的 (去掉它, 本断言立刻红)。
    """
    monkeypatch.setattr(federation, "route_corpus", _route_stub(("study", False)))
    with structlog.testing.capture_logs() as logs:
        assert decide_corpus(object(), "q", _SigBadValue(bad)) == ("study", False, None)
    assert _signal_warnings(logs)[0]["kind"] == "not_whitelisted"


@pytest.mark.parametrize("routed,same_side", [("cdisc", "cdisc_sig"), ("study", "study_sig")])
def test_decide_corpus_rejects_a_reason_that_contradicts_the_routed_corpus(
    monkeypatch, routed, same_side
):
    """方向闸 (修复环 1 I-1): 拓宽的依据只能是**对侧**信号。同侧理由 (cdisc 判定 +
    cdisc_sig) 是白名单内的合法取值, 却对每道判对的单库题都成立 —— 认它等于把 auto
    档整体推成 both, 而白名单闸对此完全看不见。"""
    monkeypatch.setattr(federation, "route_corpus", _route_stub((routed, False)))
    with structlog.testing.capture_logs() as logs:
        assert decide_corpus(object(), "q", _SigStub(same_side)) == (routed, False, None)
    assert _signal_warnings(logs)[0]["kind"] == "wrong_direction"


@pytest.mark.parametrize("sig_factory", [
    _SigBadValue,                                  # 把题面当 reason 返回
    lambda q: _SigRaises(RuntimeError(q)),         # 把题面写进异常 message
])
def test_signal_layer_warning_never_carries_question_text(sig_factory):
    """红线: warning 行会进 logs/api.launchd.log 与排障贴文。题面有两条渗漏路径 ——
    信号层返回的原值, 与它抛出的异常 message (`exc_info=True` 更狠: 本服务的 structlog
    走默认 rich traceback, 连帧 locals 一起打, `question` 就在 locals 里)。
    故 warning 只带受控字段: kind (固定哨兵) + error (异常类名)。
    """
    q = "この項目はどの変数に対応しますか"
    with structlog.testing.capture_logs() as logs:
        decide_corpus(_FakeLLM('{"corpus": "study"}'), q, sig_factory(q))
    assert _signal_warnings(logs), "先确认这条路径真的走到了 warning"
    assert q not in repr(logs)
    assert "この項目" not in repr(logs)


def test_rendered_warning_has_no_question_text(capsys):
    """上一条看的是事件字典, 而题面渗漏发生在**渲染层**: `capture_logs` 把 exc_info 存成
    一个布尔就完事, 真渲染器 (本服务只配 wrapper_class ⇒ 默认 ConsoleRenderer + rich
    traceback) 却会把整条栈连同帧局部变量打出来, `question` 就在里面。
    故这条按生产配置真渲染一次, 读 stdout —— 落地的正是 logs/api.launchd.log 那份内容。
    """
    q = "この項目はどの変数に対応しますか"
    structlog.reset_defaults()
    try:
        structlog.configure(
            wrapper_class=structlog.make_filtering_bound_logger(logging.WARNING))
        decide_corpus(_FakeLLM('{"corpus": "study"}'), q,
                      _SigRaises(RuntimeError(q)))
    finally:
        structlog.reset_defaults()
    out = capsys.readouterr().out
    assert "signal_layer_error" in out, "先确认真的渲染出了这条 warning"
    assert q not in out and "この項目" not in out


@pytest.mark.parametrize("routed,reason", [("cdisc", "study_sig"), ("study", "cdisc_sig")])
def test_decide_corpus_accepts_every_whitelisted_reason(monkeypatch, routed, reason):
    """白名单的另一向: 闸不许把合法理由也一起挡掉 (那等于信号层从未接通)。"""
    monkeypatch.setattr(federation, "route_corpus", _route_stub((routed, False)))
    assert decide_corpus(object(), "q", _SigStub(reason)) == ("both", False, reason)


def test_whitelist_is_the_one_in_routing_signals():
    """两处各写一份白名单 = Task 9 加理由时改一处漏一处, 且症状是"新理由被当成非法"。"""
    from server.routing_signals import WIDEN_REASONS
    assert federation.WIDEN_REASONS is WIDEN_REASONS


def test_retrieve_survives_a_dead_signal_layer(monkeypatch):
    """生产路径的锁: 信号层炸了, retrieve 照常返回未拓宽的判库结果, 不向上抛。"""
    monkeypatch.setattr(federation, "route_corpus", _route_stub(("study", False)))
    fed = _sig_fed(_SigRaises(RuntimeError("boom")))
    with structlog.testing.capture_logs() as logs:
        chunks, routed = fed.retrieve("q", corpus="auto")
    assert (chunks, routed) == ([], "study")
    assert fed.last_signal_widened is None
    assert [e for e in logs if e["event"] == "signal_layer_error"]
