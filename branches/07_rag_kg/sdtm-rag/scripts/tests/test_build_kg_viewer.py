import json
from scripts import build_kg_viewer as V


def test_build_data_includes_implicit(tmp_path, monkeypatch):
    fake = {"meta": {"domains": ["PR", "TR"]},
            "edges": [{"source": "PR", "target": "TR", "kind": "data_flow", "directed": True,
                       "relation": "x", "confidence": 0.8, "verified": True,
                       "evidence": {"quote": "q", "source_file": "f", "line": 1}}]}
    impl_path = tmp_path / "impl.json"
    impl_path.write_text(json.dumps(fake), encoding="utf-8")
    monkeypatch.setattr(V, "IMPL_PATH", impl_path)

    data = V.build_data()
    assert data["implicit"]["edges"][0]["kind"] == "data_flow"


def test_build_data_implicit_none_when_missing(tmp_path, monkeypatch):
    monkeypatch.setattr(V, "IMPL_PATH", tmp_path / "does_not_exist.json")

    data = V.build_data()
    assert data["implicit"] is None
