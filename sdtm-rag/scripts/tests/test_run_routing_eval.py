"""Plan B Phase 1 闸 1: 路由打分逻辑. LLM 调用不进单测 (真实三遍在 eval 执行)."""
import pytest

from eval import run_routing_eval
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


# ── 日语补充 gold 的合并加载 (Task 5b) ──────────────────────────────
_CDISC_YML = """
- id: c1
  question: Which domain holds adverse events?
  expected_sources: [ae.md]
"""
_STUDY_YML = """
- id: s1
  question: dummy study question
  expected_sources: [st01__X]
- id: s2
  question: dummy out-of-scope question
  out_of_scope: true
"""
_JA_YML = """
- id: ja_supp_01
  question: dummy japanese standard question
  gold: cdisc
"""


def _wire(tmp_path, monkeypatch, *, ja: str | None = _JA_YML):
    cd = tmp_path / "cdisc.yml"
    cd.write_text(_CDISC_YML, encoding="utf-8")
    st = tmp_path / "study.yml"
    st.write_text(_STUDY_YML, encoding="utf-8")
    ja_path = tmp_path / "ja.yml"
    if ja is not None:
        ja_path.write_text(ja, encoding="utf-8")
    monkeypatch.setattr(run_routing_eval, "CDISC_SET", cd)
    monkeypatch.setattr(run_routing_eval, "STUDY_SET", st)
    monkeypatch.setattr(run_routing_eval, "JA_SUPP_SET", ja_path)


def test_load_gold_merges_ja_supplement(tmp_path, monkeypatch):
    _wire(tmp_path, monkeypatch)
    gold = run_routing_eval.load_gold()
    # cdisc 1 + study 1 (out_of_scope 被剔除) + ja 补充 1
    assert [(g["id"], g["gold"]) for g in gold] == [
        ("c1", "cdisc"), ("st_s1", "study"), ("ja_supp_01", "cdisc")]


def test_missing_ja_supplement_raises(tmp_path, monkeypatch):
    # 补充 gold 是本次提交的一部分, 缺失即闸口失效 —— 必须 fail loud
    _wire(tmp_path, monkeypatch, ja=None)
    with pytest.raises(FileNotFoundError):
        run_routing_eval.load_gold()


def test_ja_supplement_rejects_bad_label(tmp_path, monkeypatch):
    _wire(tmp_path, monkeypatch, ja="- id: ja_bad\n  question: q\n  gold: cdics\n")
    with pytest.raises(ValueError):
        run_routing_eval.load_gold()


def test_duplicate_id_across_sets_raises(tmp_path, monkeypatch):
    # 同 id 会在 predictions dict 里互相覆盖 → 静默改变计分, 必须拦
    _wire(tmp_path, monkeypatch, ja="- id: c1\n  question: q\n  gold: cdisc\n")
    with pytest.raises(ValueError):
        run_routing_eval.load_gold()
