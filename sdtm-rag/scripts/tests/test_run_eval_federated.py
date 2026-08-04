"""--federated 的 adapter 与互斥闸. 引擎用 stub, 不碰 chroma."""
import pytest

from eval.run_eval import _FederatedAdapter, main
from server.rag import RetrievedChunk


class _FakeFed:
    def __init__(self):
        self.calls = []

    def retrieve(self, q, *, corpus="auto", top_k=None, domain=None, file_type=None):
        assert corpus == "auto"
        self.calls.append({"q": q, "top_k": top_k})
        c = RetrievedChunk(chunk_id="s-1", source="study/f.md", domain=None,
                           file_type=None, section="§2", similarity=0.9,
                           text="t", corpus="study")
        return [c], "study"

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


def test_adapter_delegates_format_context_and_build_messages():
    a = _FederatedAdapter(_FakeFed())
    assert a.format_context([1, 2]) == "CTX(2)"
    msgs = a.build_messages("q", "ctx")
    # 联邦答题走双库 system prompt (corpus="both"), 与检索判库无关
    assert msgs[0]["content"] == "SYS-both"
    assert msgs[1]["content"] == "ctx\nq"


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
