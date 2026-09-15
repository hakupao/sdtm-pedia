"""Unit tests for eval/run_eval.py --collection / --kb-root wiring.

RAGEngine / run_evaluation / print_summary are stubbed, so no chroma dir is
opened and no API is called. The point is the construction kwargs: the default
path must stay byte-identical to pre-flag behaviour, and --collection must
force structured-lookup off (the S1 gold map is CDISC-specific).
"""
from __future__ import annotations

import re
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
            self.web_search_enabled = kwargs["web_search_enabled"]
            self.prompt_guardrail_enabled = kwargs["prompt_guardrail_enabled"]
            # summary["retrieval_levers"] 读引擎实收值 (V-1), 替身必须照搬真引擎的这几个
            self.top_k = kwargs["top_k"]
            self.structured_lookup_enabled = kwargs["structured_lookup_enabled"]
            self.hybrid_enabled = kwargs["hybrid_enabled"]
            self.rerank_enabled = kwargs["rerank_enabled"]
            # study 引擎不传这个 kwarg (S1 关着, 通道不可达), 故照搬真引擎的签名默认值
            self.domain_definition_seat = kwargs.get("domain_definition_seat", True)
            # T5: 屏幕回执与 summary 都读引擎实收的这一项 (V-1 同纪律)
            self.domain_expander = kwargs.get("domain_expander")

    class FakeRouter:
        model_list: list = []

    monkeypatch.setattr(run_eval, "RAGEngine", FakeEngine)
    monkeypatch.setattr(run_eval, "run_evaluation", lambda *a, **k: [])
    monkeypatch.setattr(
        run_eval, "print_summary", lambda *a, **k: {"verdict": "PASS"}
    )
    # 非 retrieval-only 分支会真建 Router (B6 的闸要跑那个方向), 桩掉。
    # retrieval-only 时根本不调用它, 对既有用例是无操作。
    monkeypatch.setattr(run_eval, "create_router", lambda *a, **k: FakeRouter())

    def _run(extra_args: list[str], *, retrieval_only: bool = True) -> dict:
        mode = ["--retrieval-only"] if retrieval_only else []
        run_eval.main([str(test_set), *mode, *extra_args])
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
                      "hybrid_alpha", "web_search_enabled",
                      "prompt_guardrail_enabled",
                      # summary["retrieval_levers"] 读引擎实收值 (V-1)
                      "top_k", "structured_lookup_enabled", "hybrid_enabled",
                      "rerank_enabled"):
                setattr(self, k, kwargs[k])
            # study 引擎不传这个 kwarg (S1 关着, 通道不可达), 故照搬真引擎的签名默认值
            self.domain_definition_seat = kwargs.get("domain_definition_seat", True)
            # T5: 屏幕回执与 summary 都读引擎实收的这一项 (V-1 同纪律)
            self.domain_expander = kwargs.get("domain_expander")

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
    assert s.study_lookup_enabled is True        # Task 8 验收全绿后翻开 (2026-08-06)
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


# ---- B3': --web-search lever (联网参考通道 spec §10.1 B3'/B3) ----
# 生产每次请求都带 Rule 9 (与请求级 `web` 真假无关), 而 eval 曾把 web_search_enabled 写死
# False ⇒ 140q / study 48q 的数字描述的是一个**生产不跑的构型**。终审变异实测: 两处 False
# 改 True, 1862 条全绿 —— 值漂无人响。所以两个方向 + 两个注入点都要钉:
#   · 只钉 ON: 把值写死成常量 True 照样绿;
#   · 只钉 cdisc: 联邦 study_levers 那处漏改照样绿 —— 这正是 B3' 得以存活的形状。
# ⚠ 本 lever 只复现 system prompt 构型, eval 不会真去联网 (工具循环只在 /api/ask_stream)。

def _engine_receipt_line(stdout: str) -> str:
    """只取 `RAG engine:` 那一行再断言。

    两个理由: (1) tmp_path 目录名含测试函数名, 整段 stdout 自带 "web_search" 字样;
    (2) 回执若哪天被挪到别的 print, 扫全文照绿而屏幕上那行已经没有它了。
    """
    lines = [ln for ln in stdout.splitlines() if ln.startswith("RAG engine:")]
    assert len(lines) == 1, f"期望恰好一行 RAG engine 回执, 实得 {len(lines)}"
    return lines[0]


def test_web_search_flag_reaches_cdisc_engine(captured):
    assert captured(["--web-search"])["web_search_enabled"] is True


def test_web_search_default_off_on_cdisc_engine(captured):
    """反方向: 缺了它, 把 lever 写死成 True 也能全绿 (终审刚在 I-B 上踩过同款)."""
    assert captured([])["web_search_enabled"] is False


def test_web_search_flag_reaches_both_federated_engines(captured_federated):
    """联邦两臂共用一个 args ⇒ 两台引擎的 prompt 构型必须同时翻。"""
    cdisc, study = captured_federated(["--web-search"])
    assert cdisc["web_search_enabled"] is True
    assert study["web_search_enabled"] is True


def test_web_search_default_off_on_both_federated_engines(captured_federated):
    cdisc, study = captured_federated([])
    assert cdisc["web_search_enabled"] is False
    assert study["web_search_enabled"] is False


def test_web_search_receipt_says_it_does_not_search(captured, capsys):
    """不给 --output 时 summary JSON 看不到, 屏幕必须能看出开没开;

    且回执要写死"不联网" —— 一行 `web_search=ON` 会被读成"这轮是联网评测", 而它只是
    prompt 构型。本分支反复栽的正是这类"看起来在做、实际不做"。
    """
    captured(["--web-search"])
    engine_line = _engine_receipt_line(capsys.readouterr().out)
    assert "web_search=ON" in engine_line
    assert "no live search" in engine_line


def test_web_search_receipt_absent_without_flag(captured, capsys):
    captured([])
    assert "web_search" not in _engine_receipt_line(capsys.readouterr().out)


def test_web_search_help_states_the_prompt_only_boundary(capsys, monkeypatch):
    """flag 名读起来像"eval 会联网"。help 一旦丢掉这条边界, 下一个人就会拿它当联网评测,
    而 eval 走非流式路径, 工具循环只存在于 /api/ask_stream (spec §10.0)。

    ⚠ 断言必须落在 `--web-search` **自己那一块** help 上。对整份 --help 裸 `in` 是假闸:
    `"--web-search" in help_text` 光 usage 行的 `[--web-search]` 就满足; `/api/ask_stream`
    出现在**任何别的 flag** 的 help 里也算 —— 实测把边界句从本 flag 删光、把该 token 塞进
    `--full-answers`, 九条全绿而渲染出来的 help 一句"eval 不联网"都没有。
    """
    # 钉住宽度: argparse 按 COLUMNS 折行, 且折平**不修复断词** ⇒ W<=21 时 `/api/ask_stream`
    # 被 textwrap 拆开会伪红 (实测阈值 W=21 红 / W=22 绿)。钉死后该依赖整体消失。
    monkeypatch.setenv("COLUMNS", "100")
    with pytest.raises(SystemExit) as ei:
        run_eval.main(["--help"])
    assert ei.value.code == 0
    help_text = capsys.readouterr().out

    # 抽取端先自证: 抽不到就红, 否则下面全是永真式 (空 block 里什么都 `in` 不到 → 会红,
    # 但错因会指成"文案没写", 掩盖"选项整个没了")
    m = re.search(r"^ {2}--web-search\b(.*?)(?=^ {2}-|\Z)", help_text, re.S | re.M)
    assert m, "--help 里没有 `--web-search` 选项块 (抽取端失效)"
    # argparse 按终端宽度折行并缩进 24 空格, 还会在连字符处断词 ⇒ 先折平, 断言才不随
    # COLUMNS 飘 (两个待断言的串本身不含连字符, 折平后即可稳定匹配)
    block = " ".join(m.group(1).split())
    assert len(block.split()) >= 20, f"help 块只剩 {len(block.split())} 词, 已被抠空"

    # 结论句 (边界本身) 与原因锚点各钉一条 —— 只钉原因时, 把"eval 不联网"整句删掉
    # 而留着 /api/ask_stream 仍会绿
    assert "does not search the web" in block.lower()
    assert "/api/ask_stream" in block


def test_summary_records_web_search(captured, tmp_path):
    """报告层: 两轮评测事后只靠文件名认构型是没有取证价值的."""
    import json
    out_file = tmp_path / "out_web.json"
    captured(["--web-search", "--output", str(out_file)])
    saved = json.loads(out_file.read_text(encoding="utf-8"))
    assert saved["summary"]["web_search"] is True


def test_summary_records_web_search_off(captured, tmp_path):
    import json
    out_file = tmp_path / "out_no_web.json"
    captured(["--output", str(out_file)])
    saved = json.loads(out_file.read_text(encoding="utf-8"))
    assert saved["summary"]["web_search"] is False


# ---- R3: --guardrail 取值接线 (与上面 --web-search 同款病, 同一文件隔 8 行) ----
# 复审变异实测 (2026-09-01): 把 cdisc 那处 prompt_guardrail_enabled 钉成常量, **True 和
# False 两个方向各 1874 条全绿** —— 只有 study_levers 那处被 docs_engine_parity 闸捎带钉住
# (且仅 ON 方向), cdisc 主引擎两个方向都没人管。叠加当时回执与 summary 都读 args, 就能跑出
# 一批**标着 guardrail=ON、实际全程 OFF 的 140q 数字**, 而 guardrail A/B 成对评测正是
# evidence/checkpoints/guardrail_v2_summary.md 那批结论的来源。
# 现回执 (:872) 与 summary (:1055) 已改读 rag.prompt_guardrail_enabled, 这里补取值断言。

def test_guardrail_flag_reaches_cdisc_engine(captured):
    assert captured(["--guardrail"])["prompt_guardrail_enabled"] is True


def test_guardrail_default_off_on_cdisc_engine(captured):
    """反方向: 缺了它, 把 lever 钉成常量 True 也能全绿 (复审 Mut-G1 实测)."""
    assert captured([])["prompt_guardrail_enabled"] is False


def test_guardrail_flag_reaches_both_federated_engines(captured_federated):
    cdisc, study = captured_federated(["--guardrail"])
    assert cdisc["prompt_guardrail_enabled"] is True
    assert study["prompt_guardrail_enabled"] is True


def test_guardrail_default_off_on_both_federated_engines(captured_federated):
    """parity 闸只钉住 study_levers 的 ON 方向 ⇒ OFF 方向此前两处都裸着."""
    cdisc, study = captured_federated([])
    assert cdisc["prompt_guardrail_enabled"] is False
    assert study["prompt_guardrail_enabled"] is False


def test_guardrail_receipt_tracks_the_engine_not_the_flag(captured, capsys):
    """回执读引擎实收值: 注入点漏改时屏幕上的 guardrail=ON 就是假标签."""
    captured(["--guardrail"])
    assert "guardrail=ON" in _engine_receipt_line(capsys.readouterr().out)


def test_guardrail_receipt_absent_without_flag(captured, capsys):
    captured([])
    assert "guardrail" not in _engine_receipt_line(capsys.readouterr().out)


def test_summary_records_guardrail_both_directions(captured, tmp_path):
    """落盘的是引擎实收值 —— 事后拿两份 JSON 对臂时, 标签必须与引擎一致."""
    import json

    on_file, off_file = tmp_path / "g_on.json", tmp_path / "g_off.json"
    captured(["--guardrail", "--output", str(on_file)])
    captured(["--output", str(off_file)])
    assert json.loads(on_file.read_text(encoding="utf-8"))["summary"]["prompt_guardrail"] is True
    assert json.loads(off_file.read_text(encoding="utf-8"))["summary"]["prompt_guardrail"] is False

# ---------------------------------------------------------------------------
# B6 — retrieval-only 下答题侧 lever 空转, 而产物无法自证 (spec §10.1)
#
# `--retrieval-only` 一次 LLM 调用都不发 (run_eval.py:4 帮助文本 + 答题分支的
# `if not retrieval_only ...`), 所以 prompt_guardrail / web_search 这两个**答题侧**
# lever 完全空转 —— 但屏幕照打 `guardrail=ON`, summary 照落 `prompt_guardrail: true`。
# 门面上的 7 个数字全部出自 retrieval-only 跑法, 而 spec §10.1 的 B3′ 当初被写成
# 「140q 数字描述生产不跑的构型」, 多半正是因为产物自己分不清这两类 run。
# ---------------------------------------------------------------------------


def test_summary_records_retrieval_only_both_directions():
    """两个方向都钉 —— 只钉 True 那侧, 把这个键写死成常量 True 也全绿。"""
    from eval.run_eval import print_summary
    src_only = print_summary([_mk_result("a", "field_lookup", 1.0)], retrieval_only=True)
    full = print_summary(
        [_mk_result("a", "field_lookup", 1.0, fact_recall=1.0, answer_preview="ans")],
        retrieval_only=False,
    )
    assert src_only["retrieval_only"] is True
    assert full["retrieval_only"] is False
    # 类型不许漂: 既有消费方按 bool 读 prompt_guardrail / web_search, 新键同口径
    assert isinstance(src_only["retrieval_only"], bool)
    # 空转的那两个键本身仍是 bool, 语义由上面这个键限定, 不改类型
    assert isinstance(full["retrieval_only"], bool)


def test_retrieval_only_flag_reaches_print_summary_both_directions(captured, monkeypatch):
    """落盘的 retrieval_only 必须跟命令行同步 —— 接线断了, 上面那条直测照样全绿。"""
    seen: list[bool] = []

    def _spy(results, **kw):
        seen.append(kw["retrieval_only"])
        return {"verdict": "PASS"}

    monkeypatch.setattr(run_eval, "print_summary", _spy)
    captured([])
    captured([], retrieval_only=False)
    assert seen == [True, False]


def test_summary_n_answered_records_the_fact_not_the_flag():
    """n_answered 记**事实**: 「模式 = full」不蕴含「真的答了题」。

    答题分支除了 `not retrieval_only` 还有 `router is not None or direct_model is not
    None` 一层; 那层不满足时一题不答, 而 retrieval_only 仍是 False。只钉 retrieval_only
    的闸对这种情况是瞎的 —— 落盘的 `prompt_guardrail: true` 照样是个空标签。"""
    from eval.run_eval import print_summary
    answered = print_summary([
        _mk_result("a", "field_lookup", 1.0, answer_preview="ans"),
        _mk_result("b", "field_lookup", 1.0, answer_preview="ans"),
    ], retrieval_only=False)
    assert answered["n_answered"] == 2

    silent = print_summary([
        _mk_result("a", "field_lookup", 1.0),
        _mk_result("b", "field_lookup", 1.0),
    ], retrieval_only=False)
    assert silent["retrieval_only"] is False and silent["n_answered"] == 0

    src_only = print_summary([_mk_result("a", "field_lookup", 1.0)], retrieval_only=True)
    assert src_only["n_answered"] == 0


def test_summary_n_answered_counts_out_of_scope_rows_too():
    """out_of_scope 题同样走答题分支。n_answered 问的是"发生过多少次答题",
    用计分集 (已剔除 out_of_scope) 去数会低报。"""
    from eval.run_eval import print_summary
    s = print_summary([
        _mk_result("a", "field_lookup", 1.0, answer_preview="ans"),
        _mk_result("z", "negative", 1.0, answer_preview="ans", out_of_scope=True),
    ], retrieval_only=False)
    assert s["n_answered"] == 2
    assert s["n_scored"] == 1          # 对照: 计分集确实只有 1 题


def test_run_evaluation_marks_answered_rows_so_summary_can_count_them():
    """端到端 (真 run_evaluation + 真 print_summary): 答题分支真的跑过时 n_answered 才涨。

    上面几条喂的是手搓 row, 挡不住"答题分支被改坏"—— 例如把它的 `or` 写成 `and`,
    没给 --model 时就一题不答, 而 retrieval_only 仍是 False。这条能。"""
    from eval.run_eval import print_summary, run_evaluation

    class _Chunk:
        source, similarity, section = "a.md", 0.5, None

    class _Rag:
        def retrieve(self, q, top_k=None):
            return [_Chunk()]

        def format_context(self, chunks):
            return "ctx"

        def build_messages(self, q, ctx):
            return [{"role": "user", "content": q}]

    class _Resp:
        usage, model = None, "fake"
        choices = [type("C", (), {"message": type("M", (), {"content": "ans"})()})()]

    class _Router:
        def completion(self, model=None, **kw):
            return _Resp()

    res = run_evaluation(
        [{"id": "a", "category": "field_lookup", "question": "q",
          "expected_sources": ["a.md"], "expected_facts": []}],
        _Rag(), _Router(), retrieval_only=False,
    )
    assert "answer_preview" in res[0]
    assert print_summary(res, retrieval_only=False)["n_answered"] == 1


def _lever_segment(line: str, lever: str) -> str:
    """取回执行里属于某个 lever 的那一段 (到下一个 `, <字段>=` 为止)。

    不能简单用逗号切: web_search 的文案自带逗号 (`(prompt-only, no live search)`)。
    下一段的起点是"逗号+空格后面紧跟 `标识符=`"。"""
    m = re.search(rf"\b{re.escape(lever)}=ON", line)
    assert m, f"回执里没有 {lever}=ON: {line}"
    rest = line[m.end():]
    nxt = re.search(r",\s(?=[a-z_]+=)", rest)
    return rest[:nxt.start()] if nxt else rest


@pytest.mark.parametrize("flag,lever", [("--guardrail", "guardrail"),
                                        ("--web-search", "web_search")])
def test_retrieval_only_receipt_marks_answer_levers_inert(captured, capsys, flag, lever):
    """空转标记必须**紧贴**它标注的那个 lever, 不能只是同一行里出现过。

    单独开一个 lever 跑: 标记恰好一个, 且落在那个 lever 自己的段里。「扫全行有没有
    INERT」那种闸挡不住标记被挪到行尾 —— 读者扫到 `guardrail=ON` 时就看不到它了。"""
    captured([flag])
    line = _engine_receipt_line(capsys.readouterr().out)
    assert line.count(run_eval.INERT_LEVER_MARK) == 1, line
    assert run_eval.INERT_LEVER_MARK in _lever_segment(line, lever), line


def test_retrieval_only_receipt_marks_each_answer_lever_separately(captured, capsys):
    """两个都开时**各标各的** —— 只在行尾打一个总标记, 上面的参数化用例照样绿。"""
    captured(["--guardrail", "--web-search"])
    line = _engine_receipt_line(capsys.readouterr().out)
    assert line.count(run_eval.INERT_LEVER_MARK) == 2, line
    for lever in ("guardrail", "web_search"):
        assert run_eval.INERT_LEVER_MARK in _lever_segment(line, lever), line


def test_full_run_receipt_does_not_mark_levers_inert(captured, capsys):
    """反方向: 真发 LLM 调用时不许打空转标记, 否则标记恒在 = 无信息。"""
    captured(["--guardrail", "--web-search"], retrieval_only=False)
    line = _engine_receipt_line(capsys.readouterr().out)
    assert "guardrail=ON" in line and "web_search=ON" in line
    assert run_eval.INERT_LEVER_MARK not in line
    assert "INERT" not in line
