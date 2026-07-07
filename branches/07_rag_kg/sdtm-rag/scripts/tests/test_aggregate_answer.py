# scripts/tests/test_aggregate_answer.py
import pytest

from server.aggregate_answer import AggregateAnswerer, detect_aggregate_intents
from server.config import settings
from server.graph_engine import GraphEngine
from server.meta_store import MetaStore

# ── detection: must-fire, 每个语言形状家族 ≥3 例 ──────────────────────────────


def test_threshold_prefix_strict_fires():
    assert "threshold" in detect_aggregate_intents(
        "Which variables appear in more than 30 domains?")
    assert "threshold" in detect_aggregate_intents(
        "List the variables found in greater than 10 SDTM domains.")
    assert "threshold" in detect_aggregate_intents(
        "Are there variables used in over 20 domains?")
    assert "threshold" in detect_aggregate_intents(
        "Which variables exceed 15 domains in terms of variable usage?")


def test_threshold_prefix_inclusive_fires():
    assert "threshold" in detect_aggregate_intents(
        "Which variables appear in at least 40 domains?")
    assert "threshold" in detect_aggregate_intents(
        "Show the variables present in a minimum of 5 domains.")
    assert "threshold" in detect_aggregate_intents(
        "Which variables occur in no fewer than 8 domains?")


def test_threshold_postfix_inclusive_fires():
    assert "threshold" in detect_aggregate_intents(
        "Which variables show up in 3 or more domains?")
    assert "threshold" in detect_aggregate_intents(
        "Any variables used across 40+ domains?")
    assert "threshold" in detect_aggregate_intents(
        "Which variables span 10 or greater domains?")


def test_superlative_fires():
    assert "superlative" in detect_aggregate_intents(
        "What is the most shared codelist?")
    assert "superlative" in detect_aggregate_intents(
        "Which codelist is most widely used across domains?")
    assert "superlative" in detect_aggregate_intents(
        "What's the most reused controlled terminology?")
    assert "superlative" in detect_aggregate_intents(
        "Which code list is used by the largest number of variables?")


# ── detection: must-not-fire ─────────────────────────────────────────────────


def test_upper_bound_must_not_fire():
    # 引擎只有 >= 语义; 上界触发会注入方向错误的事实
    assert detect_aggregate_intents("Which variables appear in fewer than 5 domains?") == set()
    assert detect_aggregate_intents("Which variables are in at most 3 domains?") == set()
    assert detect_aggregate_intents("Variables in no more than 10 domains?") == set()
    assert detect_aggregate_intents("Which variables appear in 5 or fewer domains?") == set()
    assert detect_aggregate_intents("Variables in not more than 6 domains?") == set()
    assert detect_aggregate_intents("Which variables occur in no greater than 10 domains?") == set()
    assert detect_aggregate_intents("Are there variables not over 20 domains?") == set()
    assert detect_aggregate_intents("Which variables do not exceed 15 domains?") == set()


def test_version_number_postfix_must_not_fire():
    # "SDTM 3.2+" is a version reference, not a domain-count threshold
    assert detect_aggregate_intents(
        "Which variables in SDTM 3.2+ domains are required?") == set()


def test_sp2_territory_must_not_fire():
    assert detect_aggregate_intents("How many domains include TAETORD?") == set()
    assert detect_aggregate_intents("Which domains use the VISITNUM variable?") == set()


def test_prose_superlative_without_codelist_cue_must_not_fire():
    assert detect_aggregate_intents("What are the most common adverse events?") == set()
    assert detect_aggregate_intents("Which domain is most frequently used in trials?") == set()


def test_threshold_without_number_or_context_must_not_fire():
    assert detect_aggregate_intents("Which variables appear in many domains?") == set()
    # 有数字有 variable 但无 "domain" → 不触发 (沿用 SP3 双词共现门语义)
    assert detect_aggregate_intents("How many variables are in more than 5 records?") == set()


# ── resolve() battery ────────────────────────────────────────────────────────


@pytest.fixture(scope="module")
def agg() -> AggregateAnswerer:
    return AggregateAnswerer(GraphEngine(MetaStore(settings.meta_path)))


def test_threshold_strict_excludes_exact_boundary(agg):
    # "more than 40" 严格 (>40): 恰好 40 域的变量必须不出现
    facts = agg.resolve("Which variables appear in more than 40 domains?")
    assert facts is not None
    exact40 = [v for v, c in agg.engine.variables_in_min_domains(40) if c == 40]
    for v in exact40:
        assert v not in facts.text_block


def test_threshold_inclusive_includes_exact_boundary(agg):
    facts = agg.resolve("Which variables appear in at least 40 domains?")
    assert facts is not None
    exact40 = [v for v, c in agg.engine.variables_in_min_domains(40) if c == 40]
    if exact40:
        assert any(v in facts.text_block for v in exact40)


def test_threshold_n_from_expression_not_first_digit(agg):
    # 旧 graph_answer 抓 query 里第一个裸数字 (此例会错抓 5); 新装配必须从阈值表达取数
    facts = agg.resolve("List 5 variables that appear in more than 40 domains.")
    assert facts is not None
    n_gt40 = len(agg.engine.variables_in_min_domains(41))
    assert f"**{n_gt40}**" in facts.text_block
    assert ">40" in facts.text_block


def test_postfix_threshold_resolves(agg):
    facts = agg.resolve("Which variables show up in 30 or more domains?")
    assert facts is not None
    n = len(agg.engine.variables_in_min_domains(30))
    assert f"**{n}**" in facts.text_block
    assert "≥30" in facts.text_block


def test_superlative_top5_matches_engine(agg):
    facts = agg.resolve("What is the most shared codelist?")
    assert facts is not None
    for t in agg.engine.most_shared_codelists(5):
        assert t["code"] in facts.text_block


def test_no_counts_no_advisory(agg):
    facts = agg.resolve("Which variables appear in at least 30 domains?")
    assert facts is not None
    assert facts.checkable_counts == []
    assert facts.advisory_block == ""


def test_resolve_none_when_no_intent(agg):
    assert agg.resolve("How many domains include TAETORD?") is None
    assert agg.resolve("What are the most common adverse events?") is None


# ── golden: 注入行文与 SP3 遗留格式逐字相同 (kgval 已证有效, 格式不许漂移) ──────


def test_golden_threshold_line_format(agg):
    res = agg.engine.variables_in_min_domains(41)
    listed = ", ".join(f"{v} ({c})" for v, c in res[:50])
    expected = f"- **{len(res)}** variables appear in >40 domains: {listed}."
    facts = agg.resolve("Which variables appear in more than 40 domains?")
    assert facts.text_block == expected


def test_golden_most_shared_line_format(agg):
    top = agg.engine.most_shared_codelists(5)
    listed = ", ".join(f"{t['code']} ({t['name']}, {t['n_variables']} vars)" for t in top)
    expected = f"- Most-shared codelists: {listed}."
    facts = agg.resolve("What is the most shared codelist?")
    assert facts.text_block == expected


# ── wiring: maybe_build_answerer 按 flag 注册 AGG ─────────────────────────────


def test_maybe_build_answerer_includes_agg():
    from server.config import Settings
    from server.main import maybe_build_answerer
    a = maybe_build_answerer(Settings(structured_answer_enabled=False,
                                      graph_answer_enabled=False,
                                      aggregate_answer_enabled=True))
    assert a is not None
    assert a.resolve("Which variables appear in at least 30 domains?") is not None
    assert a.resolve("How many domains include TAETORD?") is None  # SP2 off → AGG 静默
    assert maybe_build_answerer(Settings(structured_answer_enabled=False,
                                         graph_answer_enabled=False,
                                         aggregate_answer_enabled=False)) is None


def test_maybe_build_answerer_full_composite():
    from server.config import Settings
    from server.main import maybe_build_answerer
    from server.structured_answer import CompositeAnswerer
    a = maybe_build_answerer(Settings(structured_answer_enabled=True,
                                      graph_answer_enabled=True,
                                      aggregate_answer_enabled=True))
    assert isinstance(a, CompositeAnswerer)
    # 三通道各自的代表 query 都能出事实
    assert a.resolve("How many domains include TAETORD?") is not None      # SP2
    assert a.resolve("Which variables appear in 3 or more domains?") is not None  # AGG
    assert a.resolve("What is affected if codelist C66742 changes?") is not None  # SP3
