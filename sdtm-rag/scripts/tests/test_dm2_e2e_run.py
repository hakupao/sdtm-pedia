"""dm2_e2e_run 跑批脚本对研读包答案闸的记录 (grounding / regenerate). 零网络: requests.post 打桩.
⛔ 只用虚构 OID。"""
from __future__ import annotations

import importlib.util
import json
from pathlib import Path

_PATH = Path(__file__).resolve().parents[2] / "eval" / "prod_wirein" / "dm2_e2e_run.py"
_spec = importlib.util.spec_from_file_location("dm2_e2e_run", _PATH)
run = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(run)

G = {"final": {"ok": True, "unknown_oids": [], "lang_expected": "zh", "lang_observed": "zh",
               "reasons": []},
     "first": {"ok": False, "unknown_oids": ["ITEM_Z9"], "lang_expected": "zh",
               "lang_observed": "zh", "reasons": ["x"]},
     "regenerated": True}


class _Resp:
    status_code = 200

    def __init__(self, frames):
        self._b = "".join(frames).encode("utf-8")

    def iter_content(self, chunk_size=None):
        yield self._b

    def __enter__(self):
        return self

    def __exit__(self, *a):
        return False


def _frame(ev, data):
    return f"event: {ev}\ndata: {json.dumps(data, ensure_ascii=False)}\n\n"


def test_one_call_keeps_only_final_round_as_answer(monkeypatch):
    frames = [_frame("sources", {"dossier": {"attached": True}}),
              _frame("token", {"text": "首轮"}),
              _frame("grounding", G["first"]),
              _frame("regenerate", {"reasons": ["x"], "grounding": G["first"]}),
              _frame("token", {"text": "第二轮"}),
              _frame("grounding", G["final"]),
              _frame("done", {"grounding": G, "dossier": {"attached": True}})]
    monkeypatch.setattr(run.requests, "post", lambda *a, **k: _Resp(frames))
    rec = run._one_call("http://x", "q", "m")
    assert rec["ok"] and rec["answer"] == "第二轮" and rec["first_answer"] == "首轮"
    assert len(rec["grounding_events"]) == 2 and len(rec["regenerate_events"]) == 1
    assert rec["done_event"]["grounding"] == G


def test_one_call_without_gate_has_no_first_answer(monkeypatch):
    frames = [_frame("token", {"text": "a"}), _frame("done", {})]
    monkeypatch.setattr(run.requests, "post", lambda *a, **k: _Resp(frames))
    rec = run._one_call("http://x", "q", "m")
    assert rec["answer"] == "a" and rec["first_answer"] is None


def test_summary_line_reports_grounding():
    line = run._summary_line("dm01", "opus-5", {"done_event": {"grounding": G}, "answer": "a"})
    assert "grounding_ok=True" in line and "regenerated=True" in line
    line = run._summary_line("dm01", "opus-5", {"done_event": {}, "answer": "a"})
    assert "grounding_ok=None" in line and "regenerated=None" in line


def test_judge_pack_carries_grounding(tmp_path, monkeypatch):
    monkeypatch.setattr(run, "_item_list_text", lambda: "## B.")
    monkeypatch.setattr(run, "_first_paragraph", lambda md: "def")
    q = {"dm01": {"question": "q", "domain": "DS", "expected_sources": ["cards/x.md"]}}
    rec = {"answer": "a", "done_event": {"grounding": G, "dossier": {"attached": True}}}
    run._write_judge_pack(tmp_path, [("dm01", "opus-5", rec)], q)
    pack = json.loads((tmp_path / "judge_pack.json").read_text(encoding="utf-8"))
    assert pack["runs"][0]["grounding"] == G


def test_gate_fails_when_dossier_attached_but_grounding_missing(tmp_path, capsys):
    ok = {"n_attempts": 1, "done_event": {"dossier": {"attached": True}, "grounding": G}}
    miss = {"n_attempts": 1, "done_event": {"dossier": {"attached": True}, "grounding": None}}
    assert run._gate([("dm01", "opus-5", ok)], tmp_path) == 0
    assert run._gate([("dm01", "opus-5", ok), ("dm02", "opus-5", miss)], tmp_path) == 1
    assert "dm02/opus-5" in capsys.readouterr().out
