"""Plan B Phase 1 闸 1: 路由打分逻辑. LLM 调用不进单测 (真实三遍在 eval 执行)."""
import datetime
import json
import subprocess
import types

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
    # 红线的**源头**: fatal_items 是唯一逐题的容器。给它加一个 question 键今天还不泄漏
    # (gate_verdict 只取 id, by_group 又整个剔掉), 但与「by_group 不再剔除」叠加即泄漏。
    # 在源头钉键集 = 不依赖下游两道过滤器同时不出事。
    assert all(set(f) == {"id", "gold", "pred"} for f in s["fatal_items"])


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


# fixture 题集的组分布。真值 (spec §5.2 的 181/27/3/12/12/12/6) 由
# test_policy_constants_match_spec + test_real_gold_files_match_expected_sizes 钉住。
_FIXTURE_SIZES = {"legacy": 3, "u1_doc": 1, "final": 3, "dev": 1,
                  "heldout": 1, "distractor_cdisc": 1, "ambiguous_both": 1}


def _wire_u3(tmp_path, monkeypatch, *, docs_q=_DOCS_QUESTION_YML, docs_r=_DOCS_ROUTING_YML,
             ja=_JA_YML, sizes=_FIXTURE_SIZES):
    _wire(tmp_path, monkeypatch, ja=ja)
    dq = tmp_path / "docs_q.yml"
    dq.write_text(docs_q, encoding="utf-8")
    dr = tmp_path / "docs_r.yml"
    dr.write_text(docs_r, encoding="utf-8")
    monkeypatch.setattr(run_routing_eval, "DOCS_QUESTION_SET", dq)
    monkeypatch.setattr(run_routing_eval, "DOCS_ROUTING_SET", dr)
    monkeypatch.setattr(run_routing_eval, "EXPECTED_GROUP_SIZES", sizes)
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


def test_load_u1_doc_gold_itself_rejects_missing_final_id(tmp_path):
    """守卫必须钉在 load_u1_doc_gold 自己身上, 不能靠 load_gold 的恒等闸兜底.

    变异验证 (抽检方 B M04): 删掉本函数的 FINAL_IDS 守卫后, 上面那条仍全绿 —— 它的
    `match="FINAL_IDS"` 命中的是 load_gold 里「final 组 ≠ FINAL_IDS」那条消息, 即断言
    实际盯着的是**另一道闸**。而 test_real_gold_files_match_expected_sizes 直接调用
    本函数, 那条路上没有任何兜底。故按函数边界钉, 并 match 本闸独有的措辞。
    """
    p = tmp_path / "u1.yml"
    p.write_text("- id: docs_v1_q01\n  question: placeholder\n  expected_sources: [x]\n",
                 encoding="utf-8")
    with pytest.raises(ValueError, match="条款 5 无报告对象"):
        run_routing_eval.load_u1_doc_gold(p)


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
    # match 消息而非只看类型 (抽检方 B M18): 删掉 load_docs_routing_gold 的空文件闸后,
    # load_gold 的题量闸照样抛 ValueError, 裸 pytest.raises(ValueError) 分辨不出是哪道闸红的
    # ⇒ 那个守卫成了等价变异。与兄弟测试 test_empty_u1_doc_set_raises 的 match 口径对齐。
    _wire_u3(tmp_path, monkeypatch, docs_r=body)
    with pytest.raises(ValueError, match="为空"):
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


@pytest.mark.parametrize("gold", [
    [{"id": "X", "gold": "cdisc", "group": "mystery"}],
    [{"id": "X", "gold": "cdisc"}],                                  # group 键缺失 → None
    # 两者并存: sorted() 会先炸 TypeError(str 与 NoneType 不可比), 把这条消息挤掉
    [{"id": "X", "gold": "cdisc", "group": "mystery"}, {"id": "Y", "gold": "cdisc"}],
])
def test_score_by_group_rejects_unknown_group(gold):
    with pytest.raises(ValueError, match="未知 group"):
        score_by_group(gold, {"X": "cdisc", "Y": "cdisc"})


def test_gate_verdict_excludes_final_from_fatal(monkeypatch):
    # spec §7: 条款 1 与条款 5 会互相打架, 口径写死 = 全集减 final 组
    monkeypatch.setattr(run_routing_eval, "LEGACY_EXACT_FLOOR", 2)
    preds = {"L1": "cdisc", "L2": "study", "F1": "cdisc", "D1": "study", "H1": "study"}
    v = gate_verdict(_G, preds)
    assert v["fatal_excl_final"] == 0          # F1 判错但不计入
    assert v["by_group"]["final"]["fatal"] == 1  # 仍然如实报告
    assert v["passed"] is True
    # 减法**只能**是 final 一组。审查方实测: 排除项扩成 ("final","u1_doc") 或
    # ("final","heldout") 时 28 条全绿, 27 道 U1 doc / 12 道 held-out「眼睛」集体失明。
    # `!=`→`==` 那种「排除反了」会让闸明显崩掉, 「排除多了」才是悄悄放松的自然形态。
    assert v["n_scored_excl_final"] == len(_G) - 1
    # 名字说 excl_final, 内容也必须 excl_final: 从全集算会把被豁免的三题 id 打进 stdout
    assert v["fatal_ids_excl_final"] == []
    # 上报的 floor 必须是真判据用的那个, 否则 stdout 显示 178 而实判另一个数
    assert v["legacy_floor"] == run_routing_eval.LEGACY_EXACT_FLOOR
    # by_group 必须剔掉 fatal_items: 它是唯一逐题的容器, 留着就是给题面泄漏留门
    assert all("fatal_items" not in s for s in v["by_group"].values())


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


# 覆盖全部 7 组的 gold。_G 只有 4 组 (缺 u1_doc / distractor_cdisc / ambiguous_both),
# 所以「排除项扩成 ("final","u1_doc")」在 _G 上根本不改变 n —— 实测该变异在只有 _G 时存活。
_G7 = [{"id": "L1", "gold": "cdisc", "group": "legacy"},
       {"id": "L2", "gold": "study", "group": "legacy"},
       {"id": "F1", "gold": "study", "group": "final"},
       {"id": "U1", "gold": "study", "group": "u1_doc"},
       {"id": "D1", "gold": "study", "group": "dev"},
       {"id": "H1", "gold": "study", "group": "heldout"},
       {"id": "X1", "gold": "cdisc", "group": "distractor_cdisc"},
       {"id": "B1", "gold": "both", "group": "ambiguous_both"}]


@pytest.mark.parametrize("wrong_id", ["L1", "L2", "U1", "D1", "H1", "X1", "B1"])
def test_every_non_final_group_is_watched(monkeypatch, wrong_id):
    """六个非 final 组里任何一题判错都必须计入 fatal —— 逐组各来一遍。

    这是「减法被悄悄扩大」的正面防线: 排除项每多写一组, 对应那条参数就会红。
    """
    monkeypatch.setattr(run_routing_eval, "LEGACY_EXACT_FLOOR", 0)
    preds = {g["id"]: (_FLIP[g["gold"]] if g["id"] == wrong_id else g["gold"]) for g in _G7}
    v = gate_verdict(_G7, preds)
    assert v["fatal_excl_final"] == 1
    assert v["fatal_ids_excl_final"] == [wrong_id]
    assert v["n_scored_excl_final"] == len(_G7) - 1
    assert v["passed"] is False


def test_final_group_alone_escapes_fatal(monkeypatch):
    # 反向: 恰好只有 final 逃过, 且逃过不等于不被报告 (条款 5 = 只报告)
    monkeypatch.setattr(run_routing_eval, "LEGACY_EXACT_FLOOR", 0)
    preds = {g["id"]: (_FLIP[g["gold"]] if g["id"] == "F1" else g["gold"]) for g in _G7}
    v = gate_verdict(_G7, preds)
    assert v["fatal_excl_final"] == 0 and v["fatal_ids_excl_final"] == []
    assert v["passed"] is True
    assert v["by_group"]["final"]["fatal"] == 1 and v["by_group"]["final"]["n"] == 1


def test_gate_verdict_raises_without_legacy_subset():
    # 回归条款 1 没有参照物时必须拒绝给结论, 而不是默认放行
    with pytest.raises(ValueError, match="legacy"):
        gate_verdict([{"id": "D1", "gold": "study", "group": "dev"}], {"D1": "study"})


_FLIP = {"study": "cdisc", "cdisc": "study", "both": "cdisc"}


def test_gate_verdict_return_value_carries_no_question_text(tmp_path, monkeypatch):
    # 红线: gate_verdict 的返回值 (= 写进 runs json 的 summary, 也是 stdout 的唯一来源)
    # 只许带 id 与数字。**必须用带判错的预测**: fatal_items 是唯一逐题的容器, 全对预测
    # 下它恒空 ⇒ 「只有判错时才泄漏」这个形态结构上看不见 (审查方变异 V2 即此)。
    _wire_u3(tmp_path, monkeypatch)
    monkeypatch.setattr(run_routing_eval, "LEGACY_EXACT_FLOOR", 0)
    gold = run_routing_eval.load_gold()
    all_wrong = {g["id"]: _FLIP[g["gold"]] for g in gold}   # 每组都有 fatal
    v = gate_verdict(gold, all_wrong)
    assert v["fatal_excl_final"] > 0, "预测必须真的造出 fatal, 否则这条测试又瞎了"
    assert all(v["by_group"][name]["fatal"] > 0 for name in v["by_group"])
    dumped = json.dumps(v, ensure_ascii=False)
    assert "dummy" not in dumped
    for g in gold:
        assert g["question"] not in dumped


# ── main() 冒烟 (不发任何 LLM 请求) ────────────────────────────────
def _run_main(tmp_path, monkeypatch, capsys, wrong_id, argv=("--runs", "3")):
    """跑真 main(), 但把 create_router / route_corpus 换成确定性桩。

    argv 默认三遍: U6 T1 起 `--runs != 3` 会被守卫直接 SystemExit (I-1)。桩是确定性的,
    三遍与一遍的判定完全相同, 故这些 case 断言的含义未变。
    """
    _wire_u3(tmp_path, monkeypatch)
    monkeypatch.setattr(run_routing_eval, "RUNS_DIR", tmp_path / "runs")
    monkeypatch.setattr(run_routing_eval, "LEGACY_EXACT_FLOOR", 3)
    monkeypatch.setattr(run_routing_eval, "create_router", lambda settings: object())
    gold = run_routing_eval.load_gold()
    preds = {g["id"]: (_FLIP[g["gold"]] if g["id"] == wrong_id else g["gold"]) for g in gold}
    by_question = {g["question"]: preds[g["id"]] for g in gold}
    monkeypatch.setattr(run_routing_eval, "route_corpus",
                        lambda llm, question: (by_question[question], 0))
    rc = run_routing_eval.main(list(argv))
    return gold, preds, rc, capsys.readouterr().out


@pytest.mark.parametrize("wrong_id,expect_rc", [
    ("docs_v1_q15", 0),   # final 组判错: 条款 5 只报告 ⇒ 仍 rc=0 (旧全集口径会给 1)
    ("u3_dev_01", 1),     # dev 判错: 计入 fatal ⇒ rc=1
])
def test_main_rc_follows_gate_verdict(tmp_path, monkeypatch, capsys, wrong_id, expect_rc):
    # main() 此前零测试覆盖: 把 all_passed 悄悄换回 score_run 的旧全集口径,
    # 退出码含义被替换而 28 条测试全绿 (审查方变异 M29)。
    gold, preds, rc, _ = _run_main(tmp_path, monkeypatch, capsys, wrong_id)
    assert rc == expect_rc
    assert rc == (0 if gate_verdict(gold, preds)["passed"] else 1)


@pytest.mark.parametrize("wrong_id", ["docs_v1_q15", "u3_dev_01"])
def test_main_stdout_never_prints_question_text(tmp_path, monkeypatch, capsys, wrong_id):
    # 红线, 回归版: 报告里那种「把 f-string 抄进独立脚本跑一遍」证明不了 main() 将来
    # 多出来的行。审查方变异 M27 (插一行 print(detail)) / M28 (打题面而非 id) 全部存活过。
    gold, preds, _, out = _run_main(tmp_path, monkeypatch, capsys, wrong_id)
    assert "dummy" not in out
    for g in gold:
        assert g["question"] not in out


def test_main_prints_fatal_ids_not_questions(tmp_path, monkeypatch, capsys):
    gold, _, rc, out = _run_main(tmp_path, monkeypatch, capsys, "u3_dev_01")
    assert "fatal ids: ['u3_dev_01']" in out and rc == 1
    assert "groups:" in out and "legacy:3/3" in out


@pytest.mark.parametrize("wrong_id,expect", [("u3_dev_01", "FAIL(条款1)"),
                                             ("docs_v1_q15", "PASS(条款1)")])
def test_main_qualifies_the_verdict_with_the_clause_it_checks(
        tmp_path, monkeypatch, capsys, wrong_id, expect):
    """stdout 的判定词必须带「(条款1)」限定 —— 源码注释点名了裸 PASS 的后果.

    变异验证 (抽检方 B M30): 把 `PASS(条款1)`/`FAIL(条款1)` 改成裸 `PASS`/`FAIL` 后无一条测试红。
    而 `v["passed"]` 只等于 spec §7 条款 1, 裸 PASS + rc=0 正是「本单元通过」这个误读的入口,
    条款 2/3/4 会就此凭空消失。限定词是给人读的, 所以必须由断言钉住, 不能只写在注释里。
    """
    _, _, _, out = _run_main(tmp_path, monkeypatch, capsys, wrong_id)
    assert expect in out


def test_main_writes_detail_with_questions_to_runs_dir_only(tmp_path, monkeypatch, capsys):
    # 逐题明细 (含题面) 该进 gitignored 的 RUNS_DIR —— 这条同时防「为了红线把 detail 也删了」
    _run_main(tmp_path, monkeypatch, capsys, "u3_dev_01")
    written = json.loads((tmp_path / "runs" / "routing_run_1.json").read_text(encoding="utf-8"))
    assert any("dummy" in d["question"] for d in written["detail"])
    assert "dummy" not in json.dumps(written["summary"], ensure_ascii=False)


# ── C1: 条款 5 的豁免名单不许被数据文件改写 ──────────────────────────
@pytest.mark.parametrize("group", ["final", "u1_doc"])
def test_docs_routing_gold_rejects_self_declared_reserved_group(tmp_path, monkeypatch, group):
    # 自称 final = 直接脱离 fatal_excl_final。该 yml 是 gitignored ⇒ 不进 code review,
    # 等于把「哪三题被豁免」交给一个看不见的文件改写 (审查方实测: 闸 FAIL 翻 PASS)。
    _wire_u3(tmp_path, monkeypatch,
             docs_r=f"- id: u3_x\n  question: q\n  gold: study\n  group: {group}\n")
    with pytest.raises(ValueError, match="非法"):
        run_routing_eval.load_gold()


def test_final_group_must_equal_final_ids(tmp_path, monkeypatch):
    # 第二道: 任何来源 (含将来新增的第 6 个 gold 来源) 往 final 组多塞一题都要拦
    _wire_u3(tmp_path, monkeypatch)
    monkeypatch.setattr(run_routing_eval, "load_docs_routing_gold",
                        lambda path: [{"id": "u3_rogue", "question": "q",
                                       "gold": "study", "group": "final"}])
    with pytest.raises(ValueError, match="豁免名单被改写"):
        run_routing_eval.load_gold()


def test_final_group_must_not_be_short_of_final_ids(tmp_path, monkeypatch):
    """恒等而非包含: final 组**少**一题同样是改写豁免名单.

    变异验证 (抽检方 B M24): 把 `final_ids != set(FINAL_IDS)` 放宽成
    `not final_ids <= set(FINAL_IDS)` 后上面那条仍绿 —— 它只造了「多塞一题」。
    少塞的方向此前只由 load_u1_doc_gold 的守卫间接盖着 (那条又被 M04 证明自己没人盯),
    两道闸互为唯一守护 ⇒ 各自钉住各自的方向。
    """
    _wire_u3(tmp_path, monkeypatch)
    short = [{"id": i, "question": "placeholder", "gold": "study", "group": "final"}
             for i in run_routing_eval.FINAL_IDS[:-1]]
    monkeypatch.setattr(run_routing_eval, "load_u1_doc_gold", lambda path: short)
    with pytest.raises(ValueError, match="缺少"):
        run_routing_eval.load_gold()


@pytest.mark.parametrize("loader", ["load_docs_routing_gold", "load_supplement"])
def test_gold_loader_error_message_carries_no_question_text(tmp_path, loader):
    """红线的**回归守卫**: 缺键条目的异常消息只许带序号与 id, 不许带题面.

    变异验证 (抽检方 B M57): 把两个 loader 的消息改回 `f"...: {q!r}"` (Task 5 修法之前的
    写法) 后, 针对性模块 82 条全绿; 而真实畸形 gold 上三种默认 --tb 档各泄 1 条题面 ——
    即本仓最硬的那条红线, 此前没有任何断言守着, 下一个人改回去不会有任何提示。
    合成题面是无意义占位串, 不涉红线。
    """
    canary = "SYNTHETIC-QUESTION-TEXT-MUST-NOT-APPEAR"
    p = tmp_path / "gold.yml"
    p.write_text(f"- id: u3_ok\n  question: {canary}\n  gold: study\n  group: dev\n"
                 f"- question: {canary}\n  gold: study\n  group: dev\n", encoding="utf-8")
    with pytest.raises(ValueError) as exc:
        getattr(run_routing_eval, loader)(p)
    assert canary not in str(exc.value), "异常消息带出了题面 —— 红线的第 3 条路 (生产码消息) 破了"
    assert "第 1 条" in str(exc.value), "定位信息也没了: 消息必须仍能指出是哪一条"


# ── I4: 题量下限 (两个 gold 文件都 gitignored, 删题无人执行) ──────────
def test_trimmed_u1_doc_set_raises(tmp_path, monkeypatch):
    # 审查方 G1: U1 题集只剩 FINAL_IDS 三题 ⇒ u1_doc 整组消失, 闸照样 PASS
    _wire_u3(tmp_path, monkeypatch, docs_q="".join(
        f"- id: {i}\n  question: dummy {i}\n  expected_sources: [x]\n"
        for i in ("docs_v1_q15", "docs_v1_q17", "docs_v1_q53")))
    with pytest.raises(ValueError, match="题量"):
        run_routing_eval.load_gold()


def test_trimmed_docs_routing_gold_raises(tmp_path, monkeypatch):
    # 审查方 G2/G3: 新 gold 缩到 1 题 / 只剩 dev 一组 ⇒ 空组静默不进结果 dict, 闸照样 PASS
    _wire_u3(tmp_path, monkeypatch,
             docs_r="- id: u3_dev_01\n  question: q\n  gold: study\n  group: dev\n")
    with pytest.raises(ValueError, match="题量"):
        run_routing_eval.load_gold()


def test_real_gold_files_match_expected_sizes():
    """拿**真实**题集核对 EXPECTED_GROUP_SIZES —— 常量不能只跟自己对得上。

    routing_gold_docs.yml 由 Task 5 交付, 故这里只核已存在的三个 legacy 来源与 U1 题集;
    余下四组在 Task 5 之后由 load_gold() 的题量闸覆盖。
    """
    exp = run_routing_eval.EXPECTED_GROUP_SIZES
    legacy = (len(run_routing_eval.load_test_set(str(run_routing_eval.CDISC_SET)))
              + len([q for q in run_routing_eval.load_test_set(str(run_routing_eval.STUDY_SET))
                     if not q.get("out_of_scope")])
              + len(run_routing_eval.load_supplement(run_routing_eval.JA_SUPP_SET)))
    assert legacy == exp["legacy"]
    docs = run_routing_eval.load_u1_doc_gold(run_routing_eval.DOCS_QUESTION_SET)
    assert sum(1 for g in docs if g["group"] == "u1_doc") == exp["u1_doc"]
    assert sum(1 for g in docs if g["group"] == "final") == exp["final"]


# ── m5: DOCS_QUESTION_SET 侧的缺文件/空文件 (brief 只给了 ROUTING 侧两条) ──
def test_missing_u1_doc_set_raises(tmp_path, monkeypatch):
    # match 消息而非只看类型: 删掉 exists 守卫后 open() 也抛 FileNotFoundError,
    # 只断言类型的话那个守卫就是等价变异 (审查方 M25)。
    _wire_u3(tmp_path, monkeypatch)
    monkeypatch.setattr(run_routing_eval, "DOCS_QUESTION_SET", tmp_path / "nope.yml")
    with pytest.raises(FileNotFoundError, match="闸口不完整"):
        run_routing_eval.load_gold()


@pytest.mark.parametrize("body", ["", "# 题全被删了\n"])
def test_empty_u1_doc_set_raises(tmp_path, monkeypatch, body):
    _wire_u3(tmp_path, monkeypatch, docs_q=body)
    with pytest.raises(ValueError, match="为空"):
        run_routing_eval.load_gold()


def test_policy_constants_match_spec():
    # 变异验证发现的缺口: floor 与豁免名单是**策略值**, 而上面每条 gate 测试都
    # monkeypatch 掉了 LEGACY_EXACT_FLOOR —— 源码里把 178 悄悄改小 (spec §7 明写"不许下调")
    # 或给 FINAL_IDS 增删一题, 原测试集合无一条会红。这条钉的就是那个盲区。
    assert run_routing_eval.LEGACY_EXACT_FLOOR == 178
    assert run_routing_eval.FINAL_IDS == ("docs_v1_q15", "docs_v1_q17", "docs_v1_q53")
    assert run_routing_eval.GROUPS == (
        "legacy", "u1_doc", "final", "dev", "heldout", "distractor_cdisc", "ambiguous_both")
    # 数据文件有权自称的组: final / u1_doc 必须**不在**里面 (C1)
    assert run_routing_eval.AUTHORED_GROUPS == (
        "dev", "heldout", "distractor_cdisc", "ambiguous_both")
    # spec §5.2 的配比, 同样是策略值 —— _wire_u3 把它 monkeypatch 成 fixture 分布了 (I4)
    assert run_routing_eval.EXPECTED_GROUP_SIZES == {
        "legacy": 181, "u1_doc": 27, "final": 3, "dev": 12,
        "heldout": 12, "distractor_cdisc": 12, "ambiguous_both": 6}
    assert sum(run_routing_eval.EXPECTED_GROUP_SIZES.values()) == 253


# ── U6 T1: 活仪器修缮 (A-3 run 元数据 / I-1 三遍守卫 / I-4 by_group.passed) ──────
@pytest.mark.parametrize("runs", [0, 1, 2, 4])
def test_runs_guard_rejects_non_three_before_loading_gold(monkeypatch, runs):
    """I-1: `--runs != 3` 必须在**加载 gold / 建 router 之前**就 SystemExit.

    一遍跑完照样打「三遍判定一致」—— 一遍与自己比恒等于 100%, 那行读起来跟真三遍
    一字不差, 于是 `--runs 1` 的结果可以被当成三遍纪律的证据引用。
    守卫的位置也是断言的一部分: 放到 load_gold 之后, 就得先烧掉 253 题 × N 遍的 LLM 调用
    才告诉你参数不对; 故用会炸的桩钉住「这两个都不许被碰到」。
    """
    def _boom(*a, **k):
        raise AssertionError("守卫必须在 load_gold / create_router 之前就拒绝")
    monkeypatch.setattr(run_routing_eval, "load_gold", _boom)
    monkeypatch.setattr(run_routing_eval, "create_router", _boom)
    with pytest.raises(SystemExit, match="三遍纪律"):
        run_routing_eval.main(["--runs", str(runs)])


def test_default_runs_is_three_and_needs_no_flag(tmp_path, monkeypatch, capsys):
    # 守卫不许把默认路径也拦掉: 不带 --runs 就是三遍纪律本身
    _, _, rc, out = _run_main(tmp_path, monkeypatch, capsys, "docs_v1_q15", argv=())
    assert rc == 0 and "stability:" in out


def test_nonstandard_runs_flag_suppresses_stability_and_forces_nonzero_rc(
        tmp_path, monkeypatch, capsys):
    """I-1 的另一半: 调试口 `--allow-nonstandard-runs` 开着时不许打稳定性行, rc 恒非 0.

    wrong_id 选的是 final 组那题 —— 正常三遍下它 rc=0 (条款 5 只报告)。若 rc 仍是 1,
    只能是这个 flag 强制的, 不是 fatal 造成的。
    """
    _, _, rc, out = _run_main(tmp_path, monkeypatch, capsys, "docs_v1_q15",
                              argv=("--runs", "1", "--allow-nonstandard-runs"))
    assert rc == 1, "非三遍纪律运行必须非 0 退出, 否则 rc=0 会被读成闸通过"
    assert "stability:" not in out, "一遍的自我比对不是稳定性证据, 那行不许出现"
    assert "非三遍纪律" in out


def test_meta_written_and_out_prefix(tmp_path, monkeypatch, capsys):
    """A-3: 每份 run json 顶层带 meta; `--out-prefix` 让基线/改后两批不再互相覆盖.

    U3 抽检时三份 run json 里没有任何一处记着「这是哪次跑的、跑在哪个 commit 上、
    参数是什么」—— 文件 mtime 是唯一线索, 而 mtime 会被下一次跑批直接抹掉 (基线与改后
    共用 routing_run_{i}.json 这同一组文件名, 正是 --out-prefix 要解决的那个覆盖)。
    """
    _, _, rc, _ = _run_main(tmp_path, monkeypatch, capsys, "docs_v1_q15",
                            argv=("--runs", "3", "--out-prefix", "u6_x"))
    assert rc == 0
    gold_n = len(run_routing_eval.load_gold())
    for i in (1, 2, 3):
        path = tmp_path / "runs" / f"u6_x_{i}.json"
        assert path.exists(), f"--out-prefix 没生效: {path.name} 不存在"
        d = json.loads(path.read_text(encoding="utf-8"))
        m = d["meta"]
        assert set(m) >= {"generated_at", "git_rev", "runs_arg", "run_index",
                          "n_gold", "out_prefix"}
        assert m["run_index"] == i and m["runs_arg"] == 3
        assert m["out_prefix"] == "u6_x" and m["n_gold"] == gold_n
        assert m["git_rev"] and isinstance(m["git_rev"], str)
        datetime.datetime.fromisoformat(m["generated_at"])  # 必须是可解析的时间戳
        assert d["summary"] and d["detail"]  # meta 是新增, 不是替换
    # 默认前缀那批不许被这次写出来 —— 否则 --out-prefix 只是多写一份, 覆盖照旧
    assert not (tmp_path / "runs" / "routing_run_1.json").exists()


def test_meta_carries_no_question_text(tmp_path, monkeypatch, capsys):
    # 红线: meta 是新增的写盘内容, 顺手钉住它只装数字/短串 (逐题明细只许待在 detail 里)
    gold, _, _, _ = _run_main(tmp_path, monkeypatch, capsys, "u3_dev_01",
                              argv=("--runs", "3", "--out-prefix", "u6_meta"))
    meta = json.loads((tmp_path / "runs" / "u6_meta_1.json").read_text(encoding="utf-8"))["meta"]
    dumped = json.dumps(meta, ensure_ascii=False)
    assert "dummy" not in dumped
    for g in gold:
        assert g["question"] not in dumped


def _git(*args, cwd):
    subprocess.run(["git", *args], cwd=cwd, check=True, capture_output=True, timeout=30)


def test_git_rev_marks_dirty_worktree(tmp_path, monkeypatch):
    """脏树必须在 meta 里看得出来 —— 干净 sha 会被读成「checkout 它即可复现这批数字」。

    基线/改后跑批常在未提交状态下进行 (改动就躺在工作树里), 而 `rev-parse --short HEAD`
    **结构上不可能**表达这件事: 它只认 HEAD。故这条用真 git 仓验证「脏了就带得出来」,
    而不是去断言 argv 里有 "--dirty" —— 那种断言只是把实现抄一遍。
    """
    repo = tmp_path / "repo"
    repo.mkdir()
    _git("init", "-q", cwd=repo)
    (repo / "f.txt").write_text("v1\n", encoding="utf-8")
    _git("add", "f.txt", cwd=repo)
    _git("-c", "user.email=t@example.invalid", "-c", "user.name=t",
         "commit", "-q", "-m", "init", cwd=repo)
    monkeypatch.chdir(repo)

    clean = run_routing_eval._git_rev()
    assert clean and clean != "unknown" and not clean.endswith("-dirty")
    (repo / "f.txt").write_text("v2\n", encoding="utf-8")   # 工作树改动, 未提交
    assert run_routing_eval._git_rev() == f"{clean}-dirty"


def test_git_rev_passes_output_through_and_bounds_the_subprocess(monkeypatch):
    # 值原样透传 (不许把 -dirty 后缀在这里剪掉); 且 git 必须有超时 ——
    # 一次挂住的 git 会把整批三遍跑批一起挂住, 而这只是取个版本号。
    seen = {}

    def fake_run(cmd, **kw):
        seen.update(cmd=cmd, kw=kw)
        return types.SimpleNamespace(stdout="v1.4-491-gabc1234-dirty\n")

    monkeypatch.setattr(run_routing_eval.subprocess, "run", fake_run)
    assert run_routing_eval._git_rev() == "v1.4-491-gabc1234-dirty"
    assert seen["kw"].get("timeout"), "取版本号不许无限期挂住整批跑批"


@pytest.mark.parametrize("exc", [
    subprocess.TimeoutExpired(cmd="git", timeout=5),
    subprocess.CalledProcessError(returncode=128, cmd="git"),   # 非 git 仓
    FileNotFoundError("git"),                                   # 环境里没有 git
])
def test_git_rev_falls_back_to_unknown(monkeypatch, exc):
    # 记不下版本不该让整批跑批失败 —— 但也不许伪造一个看起来正常的值
    def boom(*a, **k):
        raise exc

    monkeypatch.setattr(run_routing_eval.subprocess, "run", boom)
    assert run_routing_eval._git_rev() == "unknown"


def test_by_group_has_no_passed_key(monkeypatch):
    """I-4: by_group 子项里的 `passed` 是 score_run 按 0.95 阈值算的, 而闸根本不用那个阈值.

    真判据是 gate_verdict 顶层的 `passed` (fatal_excl_final==0 且 legacy≥floor)。
    子项那个 True/False 与判定无关却长得一模一样, 读 runs json 的人会拿组级 `passed: false`
    当成「这组没过」—— 而 12 题里错 1 题 (11/12 = 0.917 < 0.95) 就足以让它是 false。
    """
    monkeypatch.setattr(run_routing_eval, "LEGACY_EXACT_FLOOR", 0)
    preds = {g["id"]: g["gold"] for g in _G7}
    v = gate_verdict(_G7, preds)
    assert v["by_group"], "空 by_group 会让下面这条断言恒真"
    assert all("passed" not in grp for grp in v["by_group"].values())
    # 顶层判据必须还在 —— 剥掉子项的 passed 不等于把结论也剥了
    assert v["passed"] is True
    # 剥掉的只有那两个键, 其余原料 (条款 2/3/4 全靠它们) 一个不能少
    assert all(set(grp) == {"n", "exact", "exact_acc", "fatal"} for grp in v["by_group"].values())
