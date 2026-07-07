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
