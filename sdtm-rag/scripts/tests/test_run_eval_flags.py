"""Unit tests for eval/run_eval.py --collection / --kb-root wiring.

RAGEngine / run_evaluation / print_summary are stubbed, so no chroma dir is
opened and no API is called. The point is the construction kwargs: the default
path must stay byte-identical to pre-flag behaviour, and --collection must
force structured-lookup off (the S1 gold map is CDISC-specific).
"""
from __future__ import annotations

from pathlib import Path

import pytest

from eval import run_eval
from server.config import settings


@pytest.fixture
def captured(tmp_path, monkeypatch):
    """Run main() with all heavy collaborators stubbed; return RAGEngine kwargs."""
    test_set = tmp_path / "ts.yml"
    # gold 非空: load_test_set 现在拒绝无 gold 的计分题 (空 gold 会白得满分)
    test_set.write_text(
        "- id: q1\n  question: hi\n  expected_facts: []\n"
        "  expected_sources: ['stub.md']\n",
        encoding="utf-8",
    )
    calls: dict = {}

    class FakeCollection:
        def count(self):
            return 0

    class FakeEngine:
        def __init__(self, **kwargs):
            calls.update(kwargs)
            self.collection = FakeCollection()
            self.rerank_model = kwargs["rerank_model"]
            self.rerank_candidates = kwargs["rerank_candidates"]
            self.query_expansion = kwargs["query_expansion"]
            self.expansion_model = kwargs["expansion_model"]
            self.expansion_n_queries = kwargs["expansion_n_queries"]
            self.hybrid_fusion = kwargs["hybrid_fusion"]
            self.hybrid_alpha = kwargs["hybrid_alpha"]

    monkeypatch.setattr(run_eval, "RAGEngine", FakeEngine)
    monkeypatch.setattr(run_eval, "run_evaluation", lambda *a, **k: [])
    monkeypatch.setattr(
        run_eval, "print_summary", lambda *a, **k: {"verdict": "PASS"}
    )

    def _run(extra_args: list[str]) -> dict:
        run_eval.main([str(test_set), "--retrieval-only", *extra_args])
        return calls

    return _run


def test_default_path_uses_settings(captured):
    kwargs = captured([])
    assert kwargs["collection_name"] == settings.collection_name
    assert kwargs["kb_root"] == settings.kb_root
    assert kwargs["structured_lookup_enabled"] is False
    assert kwargs["chroma_dir"] == settings.chroma_dir


def test_default_path_keeps_structured_lookup_flag(captured):
    kwargs = captured(["--structured-lookup"])
    assert kwargs["collection_name"] == settings.collection_name
    assert kwargs["structured_lookup_enabled"] is True


def test_collection_override_forces_structured_lookup_off(captured):
    kwargs = captured(["--collection", "study_st01", "--structured-lookup"])
    assert kwargs["collection_name"] == "study_st01"
    assert kwargs["structured_lookup_enabled"] is False
    # kb_root untouched when only --collection is given
    assert kwargs["kb_root"] == settings.kb_root


def test_kb_root_override(captured):
    kwargs = captured(["--kb-root", "data/study/st01/cards"])
    assert kwargs["kb_root"] == Path("data/study/st01/cards")
    assert kwargs["collection_name"] == settings.collection_name


def test_kb_root_alone_does_not_disable_structured_lookup(captured):
    kwargs = captured(["--kb-root", "data/study/st01/cards", "--structured-lookup"])
    assert kwargs["structured_lookup_enabled"] is True


def test_collection_without_kb_root_warns(captured, capsys):
    captured(["--collection", "study_st01"])
    out = capsys.readouterr().out
    assert "warning" in out.lower()
    assert "--kb-root" in out


def test_collection_with_kb_root_no_warning(captured, capsys):
    captured(["--collection", "study_st01", "--kb-root", "data/study/st01/cards"])
    out = capsys.readouterr().out
    assert "warning: --collection" not in out


# ---- P2 (M-2): 空串拒绝 / P3 (T12): 报告层断言 ----

def test_empty_collection_rejected(captured):
    with pytest.raises(SystemExit) as ei:
        captured(["--collection", ""])
    assert ei.value.code == 2      # argparse usage error, 而非静默回落默认库


def test_empty_kb_root_rejected(captured):
    with pytest.raises(SystemExit) as ei:
        captured(["--kb-root", ""])
    assert ei.value.code == 2


def test_summary_records_collection(captured, tmp_path):
    """报告层: --collection 必须落进 output JSON 的 summary (评测可溯源)."""
    import json
    out_file = tmp_path / "out.json"
    captured(["--collection", "study_st01",
              "--kb-root", "data/study/st01/cards", "--output", str(out_file)])
    saved = json.loads(out_file.read_text(encoding="utf-8"))
    assert saved["summary"]["collection"] == "study_st01"
    assert saved["summary"]["top_k"] == 15


def test_collection_whitespace_stripped(captured):
    kwargs = captured(["--collection", "  study_st01  ",
                       "--kb-root", "data/study/st01/cards"])
    assert kwargs["collection_name"] == "study_st01"


# ---- golden set v1.1: out_of_scope 题不计入 recall 统计 ----

def _mk_result(qid, cat, recall, **extra):
    return {"id": qid, "category": cat, "question": "q", "source_recall": recall,
            "source_hits": [], "source_misses": [], "top5_sources": [],
            "top5_similarities": [], **extra}


def test_out_of_scope_excluded_from_average(capsys):
    """out_of_scope 题在 harness 里无判别力 (无答案可判), 必须排除出平均值."""
    from eval.run_eval import print_summary
    results = [
        _mk_result("a", "field_lookup", 1.0),
        _mk_result("b", "field_lookup", 0.0),
        _mk_result("z", "negative", 1.0, out_of_scope=True),
    ]
    summary = print_summary(results, retrieval_only=True)
    assert summary["n_scored"] == 2
    assert summary["source_recall_avg"] == 0.5   # 不是 (1+0+1)/3 = 0.667
    assert summary["n_out_of_scope"] == 1


def test_out_of_scope_listed_separately(capsys):
    from eval.run_eval import print_summary
    print_summary([
        _mk_result("a", "field_lookup", 1.0),
        _mk_result("z", "negative", 1.0, out_of_scope=True),
    ], retrieval_only=True)
    out = capsys.readouterr().out
    assert "out_of_scope" in out and "z" in out


def test_no_out_of_scope_keeps_old_behaviour(capsys):
    from eval.run_eval import print_summary
    summary = print_summary([
        _mk_result("a", "field_lookup", 1.0),
        _mk_result("b", "field_lookup", 0.0),
    ], retrieval_only=True)
    assert summary["source_recall_avg"] == 0.5
    assert summary["n_scored"] == 2
    assert summary.get("n_out_of_scope", 0) == 0


def test_run_evaluation_propagates_out_of_scope():
    """yml 的 out_of_scope 必须原样带进 result, 否则 print_summary 看不到."""
    from eval.run_eval import run_evaluation

    class _Chunk:
        source, similarity = "st01__X__Y.md", 0.5

    class _Rag:
        def retrieve(self, q, top_k=None):
            return [_Chunk()]

    res = run_evaluation(
        [{"id": "z", "category": "negative", "question": "q",
          "expected_sources": [], "out_of_scope": True}],
        _Rag(), retrieval_only=True,
    )
    assert res[0]["out_of_scope"] is True


def test_summary_reports_total_and_scored_separately():
    """n_questions 在 out_of_scope 过滤后语义已变 → 必须同时给出总题数, 否则读者被误导."""
    from eval.run_eval import print_summary
    summary = print_summary([
        _mk_result("a", "field_lookup", 1.0),
        _mk_result("z", "negative", 1.0, out_of_scope=True),
    ], retrieval_only=True)
    assert summary["n_scored"] == 1
    assert summary["n_total"] == 2


def test_all_out_of_scope_does_not_divide_by_zero():
    from eval.run_eval import print_summary
    summary = print_summary([
        _mk_result("z", "negative", 1.0, out_of_scope=True),
    ], retrieval_only=True)
    assert summary["n_scored"] == 0
    assert summary["source_recall_avg"] == 0.0


# ---- expected_sources_any: "任一来源即可" 语义 ----
# 既有 expected_sources 是 AND (每条都要命中)。但常见真相是"这几个来源里任一个都能
# 完整回答" —— 用 AND 表达会把正确检索记成部分失败 (实测 q43: 两源皆有效, 却只得 0.5)。

def test_sources_any_full_credit_when_one_hit():
    from eval.run_eval import check_source_recall
    r, hits, misses = check_source_recall(
        ["VARIABLE_INDEX.md"], [], any_of=["domains/DM/spec.md", "VARIABLE_INDEX.md"])
    assert r == 1.0 and hits == ["VARIABLE_INDEX.md"] and misses == []


def test_sources_any_zero_when_none_hit():
    from eval.run_eval import check_source_recall
    r, hits, misses = check_source_recall(
        ["chapters/ch01.md"], [], any_of=["domains/DM/spec.md", "VARIABLE_INDEX.md"])
    assert r == 0.0 and hits == []
    assert misses == ["domains/DM/spec.md", "VARIABLE_INDEX.md"]


def test_sources_and_semantics_unchanged():
    """既有 AND 行为必须逐字节不变 (139/140 题依赖它)."""
    from eval.run_eval import check_source_recall
    r, hits, misses = check_source_recall(
        ["a.md"], ["a.md", "b.md"])
    assert r == 0.5 and hits == ["a.md"] and misses == ["b.md"]


def test_sources_and_plus_any_combine():
    """两者并用: AND 组全中 + ANY 组命中一个 → 满分."""
    from eval.run_eval import check_source_recall
    r, _, _ = check_source_recall(
        ["a.md", "v.md"], ["a.md"], any_of=["v.md", "w.md"])
    assert r == 1.0


def test_run_evaluation_reads_sources_any_from_testset():
    from eval.run_eval import run_evaluation

    class _Chunk:
        source, similarity = "chapters/ch01.md", 0.9      # any_of 里都没有

    class _Rag:
        def retrieve(self, q, top_k=None):
            return [_Chunk()]

    # 若 run_evaluation 不读 expected_sources_any, 空 expected_sources 会恒得 1.0 (假绿),
    # 故用"全不命中"形态: 只有真读了 any_of 才会是 0.0
    res = run_evaluation(
        [{"id": "x", "category": "mixed", "question": "q",
          "expected_sources_any": ["domains/DM/spec.md", "VARIABLE_INDEX.md"]}],
        _Rag(), retrieval_only=True,
    )
    assert res[0]["source_recall"] == 0.0


# ---- 题集 schema 校验: 空 gold 静默送分是单向朝上的计分地雷 ----
# check_source_recall 对空 expected 返回 1.0。若键名写错 (expected_source_any) 或
# 两个 gold 键都空, 该题白得满分且分数朝上、幅度小, 不会被任何闸拦住。

def test_load_test_set_rejects_question_without_any_gold(tmp_path):
    from eval.run_eval import load_test_set
    p = tmp_path / "ts.yml"
    p.write_text("- id: q1\n  category: c\n  question: hi\n", encoding="utf-8")
    with pytest.raises(ValueError, match="q1"):
        load_test_set(str(p))


def test_load_test_set_rejects_unknown_expected_key(tmp_path):
    """键名拼错 (expected_source_any) 必须响亮失败, 而非静默当作无 gold."""
    from eval.run_eval import load_test_set
    p = tmp_path / "ts.yml"
    p.write_text(
        "- id: q1\n  category: c\n  question: hi\n"
        "  expected_sources: ['a.md']\n  expected_source_any: ['b.md']\n",
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match="expected_source_any"):
        load_test_set(str(p))


def test_load_test_set_allows_out_of_scope_without_gold(tmp_path):
    from eval.run_eval import load_test_set
    p = tmp_path / "ts.yml"
    p.write_text(
        "- id: z\n  category: negative\n  question: hi\n"
        "  out_of_scope: true\n  expected_sources: []\n",
        encoding="utf-8",
    )
    assert len(load_test_set(str(p))) == 1


def test_load_test_set_accepts_sources_any(tmp_path):
    from eval.run_eval import load_test_set
    p = tmp_path / "ts.yml"
    p.write_text(
        "- id: q1\n  category: c\n  question: hi\n"
        "  expected_sources_any: ['a.md', 'b.md']\n", encoding="utf-8")
    assert len(load_test_set(str(p))) == 1


def test_real_cdisc_test_set_passes_schema():
    """回归钉: 生产题集 140 题必须全部有非空 gold."""
    from eval.run_eval import load_test_set
    assert len(load_test_set("eval/test_set_v3.yml")) == 140


# ---- S2 study 结构化直查接线 (Plan B Phase 2 Task 5) ----
# 接线失效是静默的: S2 不通电 → 指标退回基线, 没有任何异常。所以"开关开着确实注入了"
# 和"开关关着一定不注入"两个方向都要有锁, 且注入必须落在 study 引擎而非 cdisc 引擎。


class _FakeLookup:
    """条数刻意用不寻常的值: 回执行若把条数写死成常量, 断言立刻对不上。"""

    def __init__(self, n_items: int = 7, n_aliases: int = 0):
        self.n_items = n_items
        self.n_aliases = n_aliases

    def stats(self) -> str:
        return f"{self.n_items} items/{self.n_aliases} aliases"


@pytest.fixture
def fake_lookup(monkeypatch):
    """把 StudyLookup.from_paths 换成假货工厂 (不碰真 catalog)。

    返回 (lookup, recorded): recorded 空 = from_paths 根本没被调用。
    """
    from server import study_lookup as sl_mod

    recorded: dict = {}
    lookup = _FakeLookup()

    def _fake(catalog_path, aliases_path):
        recorded["catalog"] = catalog_path
        recorded["aliases"] = aliases_path
        return lookup

    monkeypatch.setattr(sl_mod.StudyLookup, "from_paths", staticmethod(_fake))
    return lookup, recorded


@pytest.fixture
def captured_federated(tmp_path, monkeypatch):
    """--federated 模式: 按构造顺序收下两台引擎的 kwargs (cdisc, study)."""
    test_set = tmp_path / "ts.yml"
    test_set.write_text(
        "- id: q1\n  question: hi\n  expected_facts: []\n"
        "  expected_sources: ['stub.md']\n",
        encoding="utf-8",
    )
    calls: list[dict] = []

    class FakeCollection:
        def count(self):
            return 0

    class FakeEngine:
        def __init__(self, **kwargs):
            calls.append(kwargs)
            self.collection = FakeCollection()
            for k in ("rerank_model", "rerank_candidates", "query_expansion",
                      "expansion_model", "expansion_n_queries", "hybrid_fusion",
                      "hybrid_alpha"):
                setattr(self, k, kwargs[k])

    monkeypatch.setattr(run_eval, "RAGEngine", FakeEngine)
    monkeypatch.setattr(run_eval, "FederatedEngine", lambda *a, **k: object())
    monkeypatch.setattr(run_eval, "create_router", lambda *a, **k: None)
    monkeypatch.setattr(run_eval, "run_evaluation", lambda *a, **k: [])
    monkeypatch.setattr(
        run_eval, "print_summary", lambda *a, **k: {"verdict": "PASS"}
    )

    def _run(extra_args: list[str]) -> list[dict]:
        run_eval.main(
            [str(test_set), "--retrieval-only", "--federated", *extra_args]
        )
        assert len(calls) == 2, "联邦模式必须构造 cdisc + study 两台引擎"
        return calls

    return _run


def test_study_lookup_requires_collection_or_federated(captured):
    """裸给 --study-lookup 会挂到 CDISC 库上 (S2 是 study 专属) → 必须 usage error."""
    with pytest.raises(SystemExit) as ei:
        captured(["--study-lookup"])
    assert ei.value.code == 2


def test_settings_study_lookup_defaults():
    from server.config import Settings
    s = Settings()
    assert s.study_lookup_enabled is False       # Task 8 验收全绿后才翻 True
    assert s.study_catalog_path.name == "catalog.json"
    assert s.study_aliases_path.name == "lookup_aliases.yml"
    # 两个文件同属一个 study 数据目录; 指到别处 = 配置写错
    assert s.study_catalog_path.parent == s.study_aliases_path.parent


def test_collection_mode_injects_study_lookup(captured, fake_lookup):
    lookup, recorded = fake_lookup
    kwargs = captured(["--collection", "study_st01",
                       "--kb-root", "data/study/st01/cards", "--study-lookup"])
    assert kwargs["study_lookup"] is lookup
    # 路径取自 settings (不是硬编码), 否则 Task 8 翻开关时改 settings 不生效
    assert recorded["catalog"] == settings.study_catalog_path
    assert recorded["aliases"] == settings.study_aliases_path
    # S1 被 --collection 强制关 → 不触发 RAGEngine 的 S1/S2 互斥闸
    assert kwargs["structured_lookup_enabled"] is False


def test_collection_mode_without_flag_injects_nothing(captured, fake_lookup):
    _, recorded = fake_lookup
    kwargs = captured(["--collection", "study_st01",
                       "--kb-root", "data/study/st01/cards"])
    assert kwargs.get("study_lookup") is None
    assert recorded == {}, "没给 --study-lookup 却读了 catalog = 默认路径被污染"


def test_federated_injects_study_lookup_into_study_engine_only(
    captured_federated, fake_lookup
):
    lookup, _ = fake_lookup
    cdisc, study = captured_federated(["--study-lookup"])
    assert study["study_lookup"] is lookup
    # S2 挂到 cdisc 引擎 = 错线 (且 S1 开着时会撞互斥闸炸启动)
    assert cdisc.get("study_lookup") is None


def test_federated_without_flag_injects_nothing(captured_federated, fake_lookup):
    _, recorded = fake_lookup
    cdisc, study = captured_federated([])
    assert study.get("study_lookup") is None
    assert cdisc.get("study_lookup") is None
    assert recorded == {}


def test_federated_print_reports_study_lookup_on(
    captured_federated, fake_lookup, capsys
):
    """ON 不够: 别名 0 条时通道③ 完全没通电, 而屏幕上与加载成功一模一样。条数必须打出来."""
    captured_federated(["--study-lookup"])
    assert "study_lookup=ON(7 items/0 aliases)" in capsys.readouterr().out


def test_federated_print_counts_track_the_lookup(captured_federated, monkeypatch, capsys):
    """换个规模, 打印数字必须跟着变 (不是写死的字符串)."""
    from server import study_lookup as sl_mod
    monkeypatch.setattr(
        sl_mod.StudyLookup, "from_paths",
        staticmethod(lambda c, a: _FakeLookup(n_items=41, n_aliases=5)),
    )
    captured_federated(["--study-lookup"])
    assert "study_lookup=ON(41 items/5 aliases)" in capsys.readouterr().out


def test_collection_mode_prints_study_lookup_receipt(captured, fake_lookup, capsys):
    """不给 --output 时 summary JSON 看不到, 屏幕必须能看出 S2 开没开、别名几条."""
    captured(["--collection", "study_st01",
              "--kb-root", "data/study/st01/cards", "--study-lookup"])
    assert "study_lookup=ON(7 items/0 aliases)" in capsys.readouterr().out


def test_collection_mode_receipt_counts_track_the_lookup(captured, monkeypatch, capsys):
    """联邦回执有多尺度锁, collection 回执没有 —— 条数写死成常量时这一行不会报警."""
    from server import study_lookup as sl_mod
    monkeypatch.setattr(
        sl_mod.StudyLookup, "from_paths",
        staticmethod(lambda c, a: _FakeLookup(n_items=41, n_aliases=5)),
    )
    captured(["--collection", "study_st01", "--kb-root", "data/study/st01/cards",
              "--study-lookup"])
    assert "study_lookup=ON(41 items/5 aliases)" in capsys.readouterr().out


def test_collection_mode_receipt_absent_without_flag(captured, capsys):
    captured(["--collection", "study_st01", "--kb-root", "data/study/st01/cards"])
    assert "study_lookup" not in capsys.readouterr().out


def test_federated_print_reports_study_lookup_off(captured_federated, capsys):
    captured_federated([])
    assert "study_lookup=OFF" in capsys.readouterr().out


def test_summary_records_study_lookup(captured, fake_lookup, tmp_path):
    """报告层: 跑没跑 S2 必须落进 output JSON, 否则两轮评测结果无法区分."""
    import json
    out_file = tmp_path / "out_s2.json"
    captured(["--collection", "study_st01", "--kb-root", "data/study/st01/cards",
              "--study-lookup", "--output", str(out_file)])
    saved = json.loads(out_file.read_text(encoding="utf-8"))
    assert saved["summary"]["study_lookup"] is True


def test_summary_omits_study_lookup_when_off(captured, tmp_path):
    import json
    out_file = tmp_path / "out_no_s2.json"
    captured(["--collection", "study_st01", "--kb-root", "data/study/st01/cards",
              "--output", str(out_file)])
    saved = json.loads(out_file.read_text(encoding="utf-8"))
    assert "study_lookup" not in saved["summary"]
