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


# ── detection: must-fire, held-out gate shape classes (agg_attempt_1 remedy) ──
# 每条: 1 例取自烧毁的 held-out set (回归文档), 1+ 例新写 (同形状, 未见过的措辞)。


def test_shape1_spelled_number_words_fire():
    # burned (ah01): spelled-out "two"
    assert "threshold" in detect_aggregate_intents(
        "Which SDTM variables show up in two or more different domains?")
    # burned (ah03): spelled-out "nine"
    assert "threshold" in detect_aggregate_intents(
        "Can you name the variables that turn up in nine or more different "
        "SDTM domains?")
    # burned (ah04): "a dozen"
    assert "threshold" in detect_aggregate_intents(
        "Which variables are shared across a dozen or more SDTM domains?")
    # fresh: spelled-out "eleven"
    assert "threshold" in detect_aggregate_intents(
        "Which variables occur in eleven or more domains?")
    # NOTE round 3: bare "dozen" (no leading "a") moved to the fail-closed battery —
    # dozen resolution is allowlist-only ("a dozen"/"a-dozen"), everything else silent


def test_shape2_noun_between_number_and_bound_word_fires():
    # burned (ah08): noun "domains" between number and "or more"
    assert "threshold" in detect_aggregate_intents(
        "What are the SDTM variables that span 38 domains or more?")
    # fresh: same shape, different number/adjective
    assert "threshold" in detect_aggregate_intents(
        "Which variables appear in 45 domains or greater?")


def test_shape2_noun_between_must_not_fire_for_or_fewer():
    # "or fewer" is not in the word-bound alternation regardless of the noun gap
    assert detect_aggregate_intents(
        "Which variables appear in 5 domains or fewer?") == set()


def test_shape3_comparative_as_superlative_fires():
    # burned (as01)
    assert "superlative" in detect_aggregate_intents(
        "Which single codelist is attached to more variables than any other?")
    # burned (as07)
    assert "superlative" in detect_aggregate_intents(
        "Which codelist is the real workhorse here — the one tied to more "
        "variables than any other?")
    # fresh
    assert "superlative" in detect_aggregate_intents(
        "Which controlled terminology codelist covers more variables than "
        "any other?")


def test_shape4a_postposed_the_most_determiner_fires():
    # burned (as04): "the most variables" (determiner form)
    assert "superlative" in detect_aggregate_intents(
        "Can you give me a short list of the codelists that the most "
        "variables draw on?")
    # fresh
    assert "superlative" in detect_aggregate_intents(
        "Which controlled terminology codelist do the most variables "
        "reference?")


def test_shape4b_postposed_the_most_adverbial_fires():
    # burned (as03): usage verb ("shared") ... "the most" later in sentence
    assert "superlative" in detect_aggregate_intents(
        "What controlled terminology codelist gets shared between "
        "variables the most?")
    # fresh
    assert "superlative" in detect_aggregate_intents(
        "Which codelist is referenced the most across controlled "
        "terminology domains?")
    # fresh: present-tense verb form (review round 2, folded Minor 2)
    assert "superlative" in detect_aggregate_intents(
        "Which codelist do sponsors reference the most?")
    # fresh: third-person present ("recycles") — round 3 verb-list polish
    assert "superlative" in detect_aggregate_intents(
        "Which codelist is the one SDTM recycles the most?")


def test_shape4_postposed_most_without_codelist_cue_must_not_fire():
    assert detect_aggregate_intents(
        "Which domain has the most records per subject?") == set()


def test_postposed_most_does_not_cross_clauses():
    # usage verb in one clause + "the most" in an unrelated later clause must not link up
    assert detect_aggregate_intents(
        "The DM domain is used for demographics, and separately the codelist "
        "that shows up the most across studies is C66742.") == set()


def test_postposed_most_blocked_by_dash():
    # em/en dash is a clause boundary too — the verb-to-"the most" gap must not span it
    assert detect_aggregate_intents(
        "The codelist used in DM — but the most important consideration is "
        "traceability.") == set()


def test_shape5_superlative_adjective_spread_noun_fires():
    # burned (as02): "widest range of"
    assert "superlative" in detect_aggregate_intents(
        "Which codelist is reused across the widest range of SDTM domains?")
    # fresh: "broadest variety of"
    assert "superlative" in detect_aggregate_intents(
        "Which controlled terminology codelist has the broadest variety of "
        "variables?")


def test_shape5_superlative_adjective_without_spread_noun_must_not_fire():
    assert detect_aggregate_intents(
        "What is the widest table in the database?") == set()


def test_shape6_hyphenated_compound_fires():
    # burned (as08): "most-used"
    assert "superlative" in detect_aggregate_intents(
        "What's the single most-used codelist in terms of how many "
        "variables reference it?")
    # fresh: hyphenated adverb + participle
    assert "superlative" in detect_aggregate_intents(
        "Which controlled terminology codelist is the "
        "most-frequently-used one across domains?")


# ── round 4: shape classes 7-8 (r2 held-out gate remedy, agg_attempt_2) ───────


def test_shape7_numeric_plus_postfix_fires():
    # burned (r2 ah07): digit + hyphen + word "plus"
    assert "threshold" in detect_aggregate_intents(
        "I'm looking for variables that are used in 30-plus domains — "
        "which ones are those?")
    # fresh: hyphenated and spaced variants
    assert "threshold" in detect_aggregate_intents(
        "Which variables appear in 15-plus SDTM domains?")
    assert "threshold" in detect_aggregate_intents(
        "Are there variables in 20 plus domains?")


def test_plus_word_without_digit_must_not_fire():
    # "plus" without a directly-preceding digit is not a threshold
    assert detect_aggregate_intents(
        "On the plus side, how do variables map to domains?") == set()


def test_version_number_plus_word_must_not_fire():
    # "SDTM 3.2-plus" is a version reference — the (?<!\.) guard must hold for
    # the word "plus" exactly as it does for the "+" symbol
    assert detect_aggregate_intents(
        "Which variables in SDTM 3.2-plus domains are required?") == set()


def test_shape8_top_n_ranking_fires():
    # burned (r2 as04): vague quantifier — "the top few"
    assert "superlative" in detect_aggregate_intents(
        "Could you rank the codelists by how many variables reference "
        "each one and give me the top few?")
    # burned (r2 as05): spelled-out N ("top three" -> normalized "top 3")
    assert "superlative" in detect_aggregate_intents(
        "What are the top three codelists in terms of how many variables "
        "reference them?")
    # fresh: digit N (also superlative via "most" — sets are idempotent)
    assert "superlative" in detect_aggregate_intents(
        "What are the top 5 most referenced codelists?")
    # fresh: vague quantifier + alternate codelist cue
    assert "superlative" in detect_aggregate_intents(
        "Show me the top few controlled terminology sets by reuse.")


def test_top_without_quantifier_must_not_fire():
    # "top" not followed by a quantifier is not a ranking request
    assert detect_aggregate_intents(
        "How does this sit on top of the codelist structure?") == set()
    assert detect_aggregate_intents(
        "The top priority for codelist governance is consistency — "
        "where is that documented?") == set()


def test_top_n_without_codelist_cue_must_not_fire():
    assert detect_aggregate_intents(
        "What are the top three products this quarter?") == set()


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


def test_normalized_spelled_number_upper_bound_must_not_fire():
    # "no more than six domains" normalizes to "no more than 6 domains" — normalization
    # must NOT defeat the existing upper-bound lookbehind guard
    assert detect_aggregate_intents(
        "Which variables occur in no more than six domains?") == set()


def test_quantified_dozen_fails_closed():
    # wrong-magnitude firing is worse than silence: quantified dozen must not fire
    assert detect_aggregate_intents(
        "Which variables are shared across two dozen or more SDTM domains?") == set()
    assert detect_aggregate_intents(
        "Which variables appear in half a dozen or more domains?") == set()


def test_word_multiplier_dozen_fails_closed():
    # round 3: dozen resolution is ALLOWLIST-only ("a dozen"/"a-dozen"); any word
    # multiplier, hyphenated half, digit multiplier (even with odd spacing), or bare
    # "dozen" stays a word — no digit, no fire
    assert detect_aggregate_intents(
        "Which variables show up in a couple dozen or more domains?") == set()
    assert detect_aggregate_intents(
        "Are there variables in several dozen or more SDTM domains?") == set()
    assert detect_aggregate_intents(
        "Which variables appear in half-a-dozen or more domains?") == set()
    assert detect_aggregate_intents(
        "Which variables are in 2  dozen or more domains?") == set()  # double space
    assert detect_aggregate_intents(
        "Which variables are shared across dozen or more SDTM domains?") == set()


def test_plain_a_dozen_still_fires():
    assert "threshold" in detect_aggregate_intents(
        "Which variables are shared across a dozen or more SDTM domains?")
    # hyphenated "a-dozen" is inside the allowlist (a[\s-]dozen)
    assert "threshold" in detect_aggregate_intents(
        "Which variables appear in a-dozen or more domains?")


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


def test_resolve_spelled_number_threshold_matches_engine(agg):
    # "nine or more different SDTM domains" -> normalized "9 or more" -> threshold 9
    facts = agg.resolve(
        "Can you name the variables that turn up in nine or more different "
        "SDTM domains?")
    assert facts is not None
    n = len(agg.engine.variables_in_min_domains(9))
    assert f"**{n}**" in facts.text_block
    assert "≥9" in facts.text_block


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
