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
