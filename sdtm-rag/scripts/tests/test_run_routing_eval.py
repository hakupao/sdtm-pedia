"""Plan B Phase 1 闸 1: 路由打分逻辑. LLM 调用不进单测 (真实三遍在 eval 执行)."""
import json

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


GOLD_BOTH = GOLD + [{"id": "q5", "gold": "both"}]
_EXACT_4 = {"q1": "cdisc", "q2": "study", "q3": "study", "q4": "cdisc"}


def test_gold_both_exact_when_predicted_both():
    s = score_run(GOLD_BOTH, {**_EXACT_4, "q5": "both"})
    assert s["exact"] == 5 and s["fatal"] == 0 and s["passed"] is True


def test_gold_both_is_fatal_when_predicted_single_corpus():
    # 映射题被判成任一单库 = 另一半证据永远取不到, 与错向单库同级致命
    for single in ("cdisc", "study"):
        s = score_run(GOLD_BOTH, {**_EXACT_4, "q5": single})
        assert s["fatal"] == 1, single
        assert s["fatal_items"][0]["id"] == "q5"
        assert s["passed"] is False


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
    # U3 后 load_gold 还会并入 doc 题, 故只断言 legacy 这一段的构成与顺序
    _wire_u3(tmp_path, monkeypatch)
    gold = run_routing_eval.load_gold()
    # cdisc 1 + study 1 (out_of_scope 被剔除) + ja 补充 1
    assert [(g["id"], g["gold"]) for g in gold if g["group"] == "legacy"] == [
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


@pytest.mark.parametrize("body", ["", "# 只剩注释, 题全被删了\n"])
def test_empty_ja_supplement_raises(tmp_path, monkeypatch, body):
    # 空文件/只剩注释 → 静默返回 [] 等于闸悄悄变松, 必须 fail loud
    _wire(tmp_path, monkeypatch, ja=body)
    with pytest.raises(ValueError):
        run_routing_eval.load_gold()


def test_duplicate_id_across_sets_raises(tmp_path, monkeypatch):
    # 同 id 会在 predictions dict 里互相覆盖 → 静默改变计分, 必须拦
    # 重名检查在全部题集并完之后才跑, 故 doc 题集也要接上, 否则先撞上缺文件
    _wire_u3(tmp_path, monkeypatch, ja="- id: c1\n  question: q\n  gold: cdisc\n")
    with pytest.raises(ValueError):
        run_routing_eval.load_gold()


# ── U3: 手順書 gold + 分组计分 (spec 2026-08-13 §5/§7) ──────────────
from eval.run_routing_eval import gate_verdict, score_by_group  # noqa: E402

_DOCS_QUESTION_YML = """
- id: docs_v1_q15
  question: dummy doc question 15
  expected_sources: [st01_doc_a]
- id: docs_v1_q17
  question: dummy doc question 17
  expected_sources: [st01_doc_b]
- id: docs_v1_q53
  question: dummy doc question 53
  expected_sources: [st01_doc_c]
- id: docs_v1_q01
  question: dummy doc question 01
  expected_sources: [st01_doc_d]
"""
_DOCS_ROUTING_YML = """
- id: u3_dev_01
  question: dummy authored doc-routing question
  gold: study
  group: dev
- id: u3_hold_01
  question: dummy held-out doc-routing question
  gold: study
  group: heldout
- id: u3_dist_01
  question: dummy cdisc distractor
  gold: cdisc
  group: distractor_cdisc
- id: u3_amb_01
  question: dummy genuinely ambiguous question
  gold: both
  group: ambiguous_both
"""


def _wire_u3(tmp_path, monkeypatch, *, docs_q=_DOCS_QUESTION_YML, docs_r=_DOCS_ROUTING_YML,
             ja=_JA_YML):
    _wire(tmp_path, monkeypatch, ja=ja)
    dq = tmp_path / "docs_q.yml"
    dq.write_text(docs_q, encoding="utf-8")
    dr = tmp_path / "docs_r.yml"
    dr.write_text(docs_r, encoding="utf-8")
    monkeypatch.setattr(run_routing_eval, "DOCS_QUESTION_SET", dq)
    monkeypatch.setattr(run_routing_eval, "DOCS_ROUTING_SET", dr)
    return dq, dr


def test_load_gold_tags_every_item_with_a_group(tmp_path, monkeypatch):
    _wire_u3(tmp_path, monkeypatch)
    gold = run_routing_eval.load_gold()
    assert all(g["group"] in run_routing_eval.GROUPS for g in gold)
    by = {g["id"]: g["group"] for g in gold}
    assert by["c1"] == "legacy" and by["st_s1"] == "legacy" and by["ja_supp_01"] == "legacy"
    assert by["docs_v1_q15"] == "final" and by["docs_v1_q01"] == "u1_doc"
    assert by["u3_dev_01"] == "dev" and by["u3_hold_01"] == "heldout"


def test_u1_doc_questions_are_all_gold_study(tmp_path, monkeypatch):
    # spec §5.2: 统一标签消掉「标签被结果反向塑造」这个作弊面
    _wire_u3(tmp_path, monkeypatch)
    gold = run_routing_eval.load_gold()
    docs = [g for g in gold if g["group"] in ("final", "u1_doc")]
    assert len(docs) == 4 and {g["gold"] for g in docs} == {"study"}


def test_missing_final_id_raises(tmp_path, monkeypatch):
    # 三题被改名/删掉而闸照跑 = 条款 5 的报告对象静默消失
    _wire_u3(tmp_path, monkeypatch,
             docs_q="- id: docs_v1_q01\n  question: q\n  expected_sources: [x]\n")
    with pytest.raises(ValueError, match="FINAL_IDS"):
        run_routing_eval.load_gold()


def test_docs_routing_gold_rejects_bad_group(tmp_path, monkeypatch):
    _wire_u3(tmp_path, monkeypatch,
             docs_r="- id: u3_x\n  question: q\n  gold: study\n  group: devv\n")
    with pytest.raises(ValueError):
        run_routing_eval.load_gold()


def test_docs_routing_gold_rejects_legacy_group(tmp_path, monkeypatch):
    # 新题自称 legacy 会污染回归条款 1 的参照物
    _wire_u3(tmp_path, monkeypatch,
             docs_r="- id: u3_x\n  question: q\n  gold: study\n  group: legacy\n")
    with pytest.raises(ValueError):
        run_routing_eval.load_gold()


@pytest.mark.parametrize("body", ["", "# 题全被删了\n"])
def test_empty_docs_routing_gold_raises(tmp_path, monkeypatch, body):
    _wire_u3(tmp_path, monkeypatch, docs_r=body)
    with pytest.raises(ValueError):
        run_routing_eval.load_gold()


def test_missing_docs_routing_gold_raises(tmp_path, monkeypatch):
    _wire_u3(tmp_path, monkeypatch)
    monkeypatch.setattr(run_routing_eval, "DOCS_ROUTING_SET", tmp_path / "nope.yml")
    with pytest.raises(FileNotFoundError):
        run_routing_eval.load_gold()


_G = [{"id": "L1", "gold": "cdisc", "group": "legacy"},
      {"id": "L2", "gold": "study", "group": "legacy"},
      {"id": "F1", "gold": "study", "group": "final"},
      {"id": "D1", "gold": "study", "group": "dev"},
      {"id": "H1", "gold": "study", "group": "heldout"}]


def test_score_by_group_slices_independently():
    preds = {"L1": "cdisc", "L2": "study", "F1": "cdisc", "D1": "study", "H1": "cdisc"}
    by = score_by_group(_G, preds)
    assert by["legacy"]["exact"] == 2 and by["legacy"]["fatal"] == 0
    assert by["dev"]["exact"] == 1
    assert by["heldout"]["exact"] == 0 and by["heldout"]["fatal"] == 1


def test_score_by_group_rejects_unknown_group():
    with pytest.raises(ValueError, match="未知 group"):
        score_by_group([{"id": "X", "gold": "cdisc", "group": "mystery"}], {"X": "cdisc"})


def test_gate_verdict_excludes_final_from_fatal(monkeypatch):
    # spec §7: 条款 1 与条款 5 会互相打架, 口径写死 = 全集减 final 组
    monkeypatch.setattr(run_routing_eval, "LEGACY_EXACT_FLOOR", 2)
    preds = {"L1": "cdisc", "L2": "study", "F1": "cdisc", "D1": "study", "H1": "study"}
    v = gate_verdict(_G, preds)
    assert v["fatal_excl_final"] == 0          # F1 判错但不计入
    assert v["by_group"]["final"]["fatal"] == 1  # 仍然如实报告
    assert v["passed"] is True


def test_gate_verdict_counts_non_final_fatal(monkeypatch):
    monkeypatch.setattr(run_routing_eval, "LEGACY_EXACT_FLOOR", 2)
    preds = {"L1": "cdisc", "L2": "study", "F1": "study", "D1": "cdisc", "H1": "study"}
    v = gate_verdict(_G, preds)
    assert v["fatal_excl_final"] == 1 and v["passed"] is False


def test_gate_verdict_fails_when_legacy_below_floor(monkeypatch):
    monkeypatch.setattr(run_routing_eval, "LEGACY_EXACT_FLOOR", 2)
    preds = {"L1": "both", "L2": "study", "F1": "study", "D1": "study", "H1": "study"}
    v = gate_verdict(_G, preds)          # L1 判 both: 非 fatal 但不 exact
    assert v["fatal_excl_final"] == 0 and v["legacy_exact"] == 1
    assert v["passed"] is False


def test_gate_verdict_raises_without_legacy_subset():
    # 回归条款 1 没有参照物时必须拒绝给结论, 而不是默认放行
    with pytest.raises(ValueError, match="legacy"):
        gate_verdict([{"id": "D1", "gold": "study", "group": "dev"}], {"D1": "study"})


def test_gate_verdict_does_not_print_question_text(tmp_path, monkeypatch, capsys):
    # 红线: stdout 只许出现 id 与数字
    _wire_u3(tmp_path, monkeypatch)
    gold = run_routing_eval.load_gold()
    v = gate_verdict(gold, {g["id"]: g["gold"] for g in gold})
    assert "dummy" not in json.dumps(v, ensure_ascii=False)


def test_policy_constants_match_spec():
    # 变异验证发现的缺口: floor 与豁免名单是**策略值**, 而上面每条 gate 测试都
    # monkeypatch 掉了 LEGACY_EXACT_FLOOR —— 源码里把 178 悄悄改小 (spec §7 明写"不许下调")
    # 或给 FINAL_IDS 增删一题, 原测试集合无一条会红。这条钉的就是那个盲区。
    assert run_routing_eval.LEGACY_EXACT_FLOOR == 178
    assert run_routing_eval.FINAL_IDS == ("docs_v1_q15", "docs_v1_q17", "docs_v1_q53")
    assert run_routing_eval.GROUPS == (
        "legacy", "u1_doc", "final", "dev", "heldout", "distractor_cdisc", "ambiguous_both")
