import json
from pathlib import Path
from scripts import build_kg_viewer as V

def test_build_data_includes_implicit(tmp_path, monkeypatch):
    fake = {"meta": {"domains": ["PR","TR"]},
            "edges": [{"source":"PR","target":"TR","kind":"data_flow","directed":True,
                       "relation":"x","confidence":0.8,"verified":True,
                       "evidence":{"quote":"q","source_file":"f","line":1}}]}
    p = V.ROOT / "data" / "meta" / "implicit_relations.json"
    existed = p.exists(); backup = p.read_text() if existed else None
    p.write_text(json.dumps(fake), encoding="utf-8")
    try:
        data = V.build_data()
        assert data["implicit"]["edges"][0]["kind"] == "data_flow"
    finally:
        if existed: p.write_text(backup)
        elif p.exists(): p.unlink()
