"""--federated 的 adapter 与互斥闸. 引擎用 stub, 不碰 chroma."""
import json

import pytest

from eval import run_eval
from eval.run_eval import _FederatedAdapter, attach_routing_fields, main
from server.rag import RetrievedChunk


class _FakeFed:
    def __init__(self, routes=None):
        self.calls = []
        # 每次 retrieve 依次吐一个判库; 耗尽后固定复用最后一个
        self.routes = list(routes or ["study"])

    def retrieve(self, q, *, corpus="auto", top_k=None, domain=None, file_type=None):
        assert corpus == "auto"
        self.calls.append({"q": q, "top_k": top_k})
        routed = self.routes.pop(0) if len(self.routes) > 1 else self.routes[0]
        c = RetrievedChunk(chunk_id="s-1", source="study/f.md", domain=None,
                           file_type=None, section="§2", similarity=0.9,
                           text="t", corpus=routed)
        return [c], routed

    def format_context(self, chunks):
        return f"CTX({len(chunks)})"

    def build_messages(self, q, context, history=None, *, corpus):
        return [{"role": "system", "content": f"SYS-{corpus}"},
                {"role": "user", "content": f"{context}\n{q}"}]


def test_adapter_unwraps_tuple_and_records_route():
    a = _FederatedAdapter(_FakeFed())
    chunks = a.retrieve("q", top_k=5)
    assert [c.source for c in chunks] == ["study/f.md"]
    assert a.routed == ["study"]


def test_adapter_passes_top_k_through():
    fed = _FakeFed()
    a = _FederatedAdapter(fed)
    a.retrieve("q", top_k=15)
    a.retrieve("q2")
    assert [c["top_k"] for c in fed.calls] == [15, None]
    assert a.routed == ["study", "study"]


def test_adapter_delegates_format_context():
    a = _FederatedAdapter(_FakeFed())
    assert a.format_context([1, 2]) == "CTX(2)"


def test_build_messages_uses_the_route_of_the_question_just_retrieved():
    """答题 system prompt 必须跟着本题判库走 — 硬编码 both 会让单库题拿到双库 prompt,
    与生产 router.py (corpus=routed) 不一致, 使联邦答题闸测的不是生产行为."""
    a = _FederatedAdapter(_FakeFed(["study"]))
    a.retrieve("q")
    msgs = a.build_messages("q", "ctx")
    assert msgs[0]["content"] == "SYS-study"
    assert msgs[1]["content"] == "ctx\nq"


def test_build_messages_tracks_route_changing_across_questions():
    a = _FederatedAdapter(_FakeFed(["study", "cdisc", "both"]))
    seen = []
    for q in ("q1", "q2", "q3"):
        a.retrieve(q)
        seen.append(a.build_messages(q, "ctx")[0]["content"])
    assert seen == ["SYS-study", "SYS-cdisc", "SYS-both"]


def test_build_messages_before_any_retrieve_fails_loud():
    """无判库时静默回落 both 正是本 bug 的形状 — 报错而不是猜."""
    a = _FederatedAdapter(_FakeFed())
    with pytest.raises(RuntimeError, match="retrieve"):
        a.build_messages("q", "ctx")


def _write_ts(tmp_path):
    ts = tmp_path / "t.yml"
    ts.write_text("- id: q1\n  category: c\n  question: x\n  expected_sources: [a.md]\n")
    return str(ts)


def test_federated_mutually_exclusive_with_collection(tmp_path, capsys):
    ts = _write_ts(tmp_path)
    with pytest.raises(SystemExit):
        main([ts, "--retrieval-only", "--federated", "--collection", "study_st01"])


def test_federated_mutually_exclusive_with_kb_root(tmp_path, capsys):
    ts = _write_ts(tmp_path)
    with pytest.raises(SystemExit):
        main([ts, "--retrieval-only", "--federated", "--kb-root", "data/study/st01/cards"])


# ── U5: 逐题判库观测字段 ──

def test_adapter_records_fallback_flag_per_question():
    fed = _FakeFed()
    fed.last_route_fallback = False
    a = _FederatedAdapter(fed)
    a.retrieve("q")
    fed.last_route_fallback = True
    a.retrieve("q2")
    assert a.routed_fallback == [False, True]


def test_adapter_fallback_defaults_none_when_engine_lacks_attr():
    a = _FederatedAdapter(_FakeFed())
    a.retrieve("q")
    assert a.routed_fallback == [None]


def test_attach_routing_fields_writes_per_question_observations():
    results = [{"id": "a"}, {"id": "b"}]
    a = _FederatedAdapter(_FakeFed(["study", "both"]))
    a.retrieve("q1")
    a.retrieve("q2")
    attach_routing_fields(results, a)
    assert [r["routed"] for r in results] == ["study", "both"]
    assert results[0]["routed_fallback"] is None


def test_attach_routing_fields_fails_loud_on_length_mismatch():
    a = _FederatedAdapter(_FakeFed())
    a.retrieve("q")
    with pytest.raises(RuntimeError):
        attach_routing_fields([], a)


# ── U5 审查修复: attach 主线接线 (I1) 与 fallback 值传递 (I2) ──

class _FallbackFed(_FakeFed):
    """逐题带不同 `last_route_fallback` 的引擎 (真 FederatedEngine 的形状: auto 档才有值).

    原有 _FakeFed 根本没有该属性, 于是断言 `routed_fallback is None` 恒真 ——
    实现把 fallback 硬写成 None 也全绿, 值传递零覆盖。
    """

    def __init__(self, routes=None, flags=None):
        super().__init__(routes)
        self._flags = list(flags or [None])
        self.last_route_fallback = None

    def retrieve(self, q, **kw):
        self.last_route_fallback = (
            self._flags.pop(0) if len(self._flags) > 1 else self._flags[0]
        )
        return super().retrieve(q, **kw)


def test_attach_routing_fields_carries_non_none_fallback_values():
    """恒写 None / 全写最后一次 的实现必须红 —— fallback 值传递的杀手 (审查 I2)."""
    results = [{"id": "a"}, {"id": "b"}]
    a = _FederatedAdapter(_FallbackFed(["study", "both"], [False, True]))
    a.retrieve("q1")
    a.retrieve("q2")
    attach_routing_fields(results, a)
    assert [r["routed_fallback"] for r in results] == [False, True]


def _run_main_federated(tmp_path, monkeypatch, fed):
    """真跑 `main() + --federated + --output`, 只桩重引擎.

    run_evaluation 若桩成 `[]`, attach 走 `0 == 0` 退化路径、一个字段都不写也全绿 ——
    删掉主线那行调用测试照样绿 (审查 I1)。所以这里让 run_evaluation / print_summary /
    attach 全走真码, 逐题真过 adapter, 只把 chroma 引擎与 router 换成假货。
    """
    ts = tmp_path / "t.yml"
    ts.write_text(
        "- id: q1\n  category: c\n  question: x1\n  expected_sources: [study/f.md]\n"
        "- id: q2\n  category: c\n  question: x2\n  expected_sources: [study/f.md]\n",
        encoding="utf-8",
    )
    out = tmp_path / "out.json"

    class FakeCollection:
        def count(self):
            return 0

    class FakeEngine:
        def __init__(self, **kwargs):
            self.collection = FakeCollection()
            for k, v in kwargs.items():
                setattr(self, k, v)

    monkeypatch.setattr(run_eval, "RAGEngine", FakeEngine)
    monkeypatch.setattr(run_eval, "FederatedEngine", lambda *a, **k: fed)
    monkeypatch.setattr(run_eval, "create_router", lambda *a, **k: None)
    main([str(ts), "--retrieval-only", "--federated", "--output", str(out)])
    return json.loads(out.read_text(encoding="utf-8"))["results"]


def test_attach_routing_fields_fails_loud_when_the_two_evidence_lists_desync():
    """长度闸只比 routed 与 results; routed 与 routed_fallback 之间的错位靠 zip(strict=True).
    去掉 strict 后 zip 会静默截断, 尾部若干题一个字段都不写却不报错 (抽检方 B 变异 C03)."""
    a = _FederatedAdapter(_FallbackFed(["study", "both"], [False, True]))
    a.retrieve("q1")
    a.retrieve("q2")
    a.routed_fallback.pop()
    with pytest.raises(ValueError):
        attach_routing_fields([{"id": "a"}, {"id": "b"}], a)


def test_main_federated_writes_routing_fields_into_output_json(tmp_path, monkeypatch):
    """主线接线断言: 产物每行都要有本题的 routed / routed_fallback (审查 I1)."""
    rows = _run_main_federated(
        tmp_path, monkeypatch, _FallbackFed(["study", "both"], [False, True])
    )
    assert [r["id"] for r in rows] == ["q1", "q2"]
    assert [r["routed"] for r in rows] == ["study", "both"]
    assert [r["routed_fallback"] for r in rows] == [False, True]


# ---- U6 Task 11: --signal-layer 透传 (答题侧 off/on 双臂的唯一开关) ----
# 接线失效是静默的: on 臂没通电 ⇒ 两臂逐位相同 ⇒ 判定读出"信号层无代价无收益",
# 而那批数字的文件名与 evidence 都写着 on。所以"开着确实传了"和"关着一定是 None"
# 两个方向都要锁, 且必须锁在 FederatedEngine 的构造实参上 (生产同一个入口)。


@pytest.fixture
def captured_fed_kwargs(tmp_path, monkeypatch):
    """跑 main(--federated), 收下 FederatedEngine 的构造 kwargs。"""
    ts = tmp_path / "t.yml"
    ts.write_text(
        "- id: q1\n  category: c\n  question: x1\n  expected_sources: [study/f.md]\n",
        encoding="utf-8",
    )
    kw: dict = {}

    class FakeCollection:
        def count(self):
            return 0

    class FakeEngine:
        def __init__(self, **kwargs):
            self.collection = FakeCollection()
            for k, v in kwargs.items():
                setattr(self, k, v)

    class _AnyCorpusFed(_FakeFed):
        """`_FakeFed` 钉死 corpus=="auto"; 本 fixture 也要跑强制档, 故放开这一条。"""

        def retrieve(self, q, *, corpus="auto", top_k=None, domain=None, file_type=None):
            self.calls.append({"q": q, "corpus": corpus, "top_k": top_k})
            routed = self.routes[0] if corpus == "auto" else corpus
            c = RetrievedChunk(chunk_id="s-1", source="study/f.md", domain=None,
                               file_type=None, section="§2", similarity=0.9,
                               text="t", corpus=routed)
            return [c], routed

    def _fake_fed(*a, **k):
        kw.update(k)
        return _AnyCorpusFed()

    monkeypatch.setattr(run_eval, "RAGEngine", FakeEngine)
    monkeypatch.setattr(run_eval, "FederatedEngine", _fake_fed)
    monkeypatch.setattr(run_eval, "create_router", lambda *a, **k: None)

    def _run(extra: list[str], out: str | None = None) -> dict:
        args = [str(ts), "--retrieval-only", "--federated", *extra]
        if out:
            args += ["--output", out]
        main(args)
        return kw

    return _run


@pytest.fixture
def spy_build_signals(monkeypatch):
    """把 build_signals 换成哨兵工厂; recorded 空 = 根本没被调用。"""
    from server import routing_signals as rs_mod

    sentinel = object()
    recorded: dict = {}

    def _fake(settings_arg, study_lookup=None):
        recorded["settings"] = settings_arg
        recorded["study_lookup"] = study_lookup
        return sentinel

    monkeypatch.setattr(rs_mod, "build_signals", _fake)
    return sentinel, recorded


def test_signal_layer_defaults_to_off(captured_fed_kwargs, spy_build_signals):
    """默认路径必须与加 flag 之前逐位相同: signals=None 且工厂根本没被调用。"""
    _, recorded = spy_build_signals
    kw = captured_fed_kwargs([])
    assert kw["signals"] is None
    assert recorded == {}, "off 臂却调了 build_signals — 默认路径被污染"


def test_signal_layer_on_passes_the_production_factory_object(
    captured_fed_kwargs, spy_build_signals
):
    sentinel, recorded = spy_build_signals
    kw = captured_fed_kwargs(["--signal-layer", "on"])
    assert kw["signals"] is sentinel
    from server.config import settings
    assert recorded["settings"] is settings      # 硬编码路径会绕开 settings override


def test_signal_layer_off_explicitly_is_still_none(captured_fed_kwargs, spy_build_signals):
    _, recorded = spy_build_signals
    kw = captured_fed_kwargs(["--signal-layer", "off"])
    assert kw["signals"] is None
    assert recorded == {}


def test_signal_layer_on_reuses_the_s2_lookup(captured_fed_kwargs, spy_build_signals,
                                              monkeypatch):
    """生产 lifespan 复用同一份 S2 (main.py 注释: 不造第二份 —— 两份可以来自不同文件)。
    eval 侧另造一份 ⇒ 尺子量的信号层与线上跑的不是同一个数据源。"""
    from server import study_lookup as sl_mod

    class _FakeLookup:
        def stats(self):
            return "7 items/0 aliases"

    lookup = _FakeLookup()
    monkeypatch.setattr(sl_mod.StudyLookup, "from_paths", staticmethod(lambda c, a: lookup))
    _, recorded = spy_build_signals
    captured_fed_kwargs(["--signal-layer", "on", "--study-lookup"])
    assert recorded["study_lookup"] is lookup


def test_signal_layer_requires_federated(tmp_path, monkeypatch):
    """裸给 --signal-layer on 会静默无效 (信号层只挂在联邦判库上) → usage error。"""
    ts = tmp_path / "t.yml"
    ts.write_text(
        "- id: q1\n  category: c\n  question: x1\n  expected_sources: [study/f.md]\n",
        encoding="utf-8",
    )
    with pytest.raises(SystemExit) as ei:
        main([str(ts), "--retrieval-only", "--signal-layer", "on"])
    assert ei.value.code == 2


def test_signal_layer_on_refuses_a_none_factory_result(captured_fed_kwargs, monkeypatch):
    """工厂返回 None = 悄悄跑成 off, 而产物 summary 仍写 "on" —— 那批数字会被当成
    「信号层开着」的证据引用 (run_routing_eval 同款闸)。"""
    from server import routing_signals as rs_mod

    monkeypatch.setattr(rs_mod, "build_signals", lambda *a, **k: None)
    with pytest.raises(SystemExit):
        captured_fed_kwargs(["--signal-layer", "on"])


def test_summary_records_signal_layer(captured_fed_kwargs, spy_build_signals, tmp_path):
    """两臂产物除文件名外必须能自证 off/on, 否则事后无法判断哪份是哪臂。"""
    out = tmp_path / "sig_on.json"
    captured_fed_kwargs(["--signal-layer", "on"], out=str(out))
    assert json.loads(out.read_text(encoding="utf-8"))["summary"]["signal_layer"] == "on"


def test_summary_records_signal_layer_off(captured_fed_kwargs, tmp_path):
    out = tmp_path / "sig_off.json"
    captured_fed_kwargs([], out=str(out))
    assert json.loads(out.read_text(encoding="utf-8"))["summary"]["signal_layer"] == "off"


def test_federated_receipt_prints_signal_layer(captured_fed_kwargs, spy_build_signals,
                                               capsys):
    """屏幕回执: 不给 --output 时 summary 看不到, 人肉跑必须看得出这一臂开没开。"""
    captured_fed_kwargs(["--signal-layer", "on"])
    assert "signal_layer=on" in capsys.readouterr().out


def test_signal_layer_on_rejects_a_forced_corpus(tmp_path, monkeypatch):
    """强制判库不走 `decide_corpus`, 信号层整层惰性 —— 但 summary 与回执照样写 `on`。
    那是**假标签面**: 一批信号层从未通电的数字, 事后看与真 on 臂一字不差。"""
    ts = tmp_path / "t.yml"
    ts.write_text(
        "- id: q1\n  category: c\n  question: x1\n  expected_sources: [study/f.md]\n",
        encoding="utf-8",
    )
    for forced in ("study", "both", "cdisc"):
        with pytest.raises(SystemExit) as ei:
            main([str(ts), "--retrieval-only", "--federated",
                  "--corpus", forced, "--signal-layer", "on"])
        assert ei.value.code == 2


def test_signal_layer_off_still_allows_a_forced_corpus(captured_fed_kwargs):
    """U5 的强制档矩阵 (--corpus study/both) 必须原样跑得动 —— 闸只拦 on。"""
    kw = captured_fed_kwargs(["--corpus", "study"])
    assert kw["signals"] is None


def test_federated_receipt_prints_the_real_corpus(captured_fed_kwargs, capsys):
    """回执曾把 corpus 硬编码成 auto: 强制档跑批的屏幕/日志因此自称 auto,
    而那正是 U5 用来拆分「判库损耗 vs 接线损耗」的那个开关。"""
    captured_fed_kwargs(["--corpus", "study"])
    out = capsys.readouterr().out
    assert "corpus=study" in out
    assert "corpus=auto" not in out


@pytest.mark.parametrize("corpus,word", [("auto", "LLM(light)"), ("study", "forced"),
                                         ("both", "forced"), ("cdisc", "forced")])
def test_federated_receipt_routing_word_follows_the_corpus(captured_fed_kwargs, capsys,
                                                           corpus, word):
    """同一行里的 `corpus=` 与 `signal_layer=` 两格各有专测, 而 `routing=` 判词没有 ——
    同一类缺陷、同一行, 只修了一半 (finding F-10)。判词写死成 LLM(light) 后, 强制档
    跑批的回执会再次自称走了 LLM 路由, 而强制档根本不经 `decide_corpus`。
    """
    captured_fed_kwargs(["--corpus", corpus])
    assert f"routing={word}(corpus={corpus})" in capsys.readouterr().out


def test_explicit_corpus_auto_with_signal_layer_on_is_accepted(captured_fed_kwargs,
                                                               spy_build_signals):
    """Task 11 双臂跑批命令逐字写的是 `--corpus auto --signal-layer on` ——
    新加的强制档闸不许把它一起拦掉 (那会让 evidence §15 的复跑命令失效)。"""
    sentinel, _ = spy_build_signals
    kw = captured_fed_kwargs(["--corpus", "auto", "--signal-layer", "on"])
    assert kw["signals"] is sentinel
