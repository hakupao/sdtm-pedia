"""Tests for server/grounding.py — apply_counting_gate().

TDD: write tests first, implement gate, confirm all green.

Cases:
  1. correct count in answer → no change, no violations
  2. wrong count in answer   → correction block appended, violation returned
  3. no number stated for subject → no violation (missing ≠ contradiction)
  4. None facts              → passthrough unchanged
  5. empty checkable_counts  → passthrough unchanged
  6. multi-digit number handling (43, 36)
  7. unrelated number in a different sentence → no false positive
  8. multiple violations     → all appended in one correction block
  9. subject appears multiple times in same sentence (still correct)
 10. subject case-insensitive match
"""
from __future__ import annotations

from server.grounding import apply_counting_gate
from server.structured_answer import CheckableCount, StructuredFacts

# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------

def _facts(subject: str, kind: str, value: int) -> StructuredFacts:
    return StructuredFacts(
        text_block=f"- {subject} appears in exactly {value} {kind}.",
        checkable_counts=[CheckableCount(subject=subject, kind=kind, value=value)],
    )


# ---------------------------------------------------------------------------
# case 1: answer states the CORRECT count → no change, no violations
# ---------------------------------------------------------------------------

def test_correct_count_no_violation():
    answer = "TAETORD appears in 43 domains across SDTM."
    facts = _facts("TAETORD", "domains", 43)
    out_answer, violations = apply_counting_gate(answer, facts)
    assert out_answer == answer, "answer must not be modified on correct count"
    assert violations == []


# ---------------------------------------------------------------------------
# case 2: answer states WRONG count → correction block appended, violation returned
# ---------------------------------------------------------------------------

def test_wrong_count_correction_appended():
    answer = "TAETORD appears in 10 domains."
    facts = _facts("TAETORD", "domains", 43)
    out_answer, violations = apply_counting_gate(answer, facts)
    assert "TAETORD" in out_answer
    assert "43" in out_answer
    assert "Authoritative correction" in out_answer
    assert out_answer.startswith(answer), "original answer text must be preserved at front"
    assert len(violations) == 1
    v = violations[0]
    assert v["subject"] == "TAETORD"
    assert v["kind"] == "domains"
    assert v["expected"] == 43
    assert v["stated"] == 10


# ---------------------------------------------------------------------------
# case 3: answer mentions subject but states NO number → no violation
# (missing number is not a contradiction; facts block already supplied it)
# ---------------------------------------------------------------------------

def test_no_number_stated_no_violation():
    answer = "TAETORD is a variable that appears in many domains."
    facts = _facts("TAETORD", "domains", 43)
    out_answer, violations = apply_counting_gate(answer, facts)
    assert out_answer == answer
    assert violations == []


# ---------------------------------------------------------------------------
# case 4: facts is None → passthrough
# ---------------------------------------------------------------------------

def test_none_facts_passthrough():
    answer = "Some answer about TAETORD in 10 domains."
    out_answer, violations = apply_counting_gate(answer, None)
    assert out_answer == answer
    assert violations == []


# ---------------------------------------------------------------------------
# case 5: empty checkable_counts → passthrough
# ---------------------------------------------------------------------------

def test_empty_checkable_counts_passthrough():
    answer = "TAETORD appears in 10 domains."
    facts = StructuredFacts(text_block="some facts", checkable_counts=[])
    out_answer, violations = apply_counting_gate(answer, facts)
    assert out_answer == answer
    assert violations == []


# ---------------------------------------------------------------------------
# case 6: multi-digit numbers (43, 36) handled correctly
# ---------------------------------------------------------------------------

def test_multi_digit_correct():
    answer = "VISITDY appears in 36 domains."
    facts = _facts("VISITDY", "domains", 36)
    out_answer, violations = apply_counting_gate(answer, facts)
    assert out_answer == answer
    assert violations == []


def test_multi_digit_wrong():
    answer = "VISITDY appears in 99 domains."
    facts = _facts("VISITDY", "domains", 36)
    _, violations = apply_counting_gate(answer, facts)
    assert len(violations) == 1
    assert violations[0]["expected"] == 36
    assert violations[0]["stated"] == 99


# ---------------------------------------------------------------------------
# case 7: unrelated number in a DIFFERENT sentence → no false positive
# The number 100 belongs to a sentence that does NOT mention the subject.
# ---------------------------------------------------------------------------

def test_unrelated_number_different_sentence_no_false_positive():
    answer = (
        "There are 100 total variables in SDTM. "
        "TAETORD is used across multiple SDTM domains."
    )
    facts = _facts("TAETORD", "domains", 43)
    out_answer, violations = apply_counting_gate(answer, facts)
    assert out_answer == answer, "no correction should be appended"
    assert violations == []


# ---------------------------------------------------------------------------
# case 8: multiple violations → all captured, one correction block
# ---------------------------------------------------------------------------

def test_multiple_violations():
    answer = "TAETORD appears in 10 domains. VISITDY appears in 5 domains."
    facts = StructuredFacts(
        text_block="facts",
        checkable_counts=[
            CheckableCount("TAETORD", "domains", 43),
            CheckableCount("VISITDY", "domains", 36),
        ],
    )
    out_answer, violations = apply_counting_gate(answer, facts)
    assert len(violations) == 2
    assert "TAETORD" in out_answer and "43" in out_answer
    assert "VISITDY" in out_answer and "36" in out_answer
    # Only ONE correction block appended
    assert out_answer.count("Authoritative correction") == 1


# ---------------------------------------------------------------------------
# case 9: subject appears multiple times in the same sentence (still correct)
# ---------------------------------------------------------------------------

def test_subject_multiple_times_same_sentence_correct():
    answer = "TAETORD, or TAETORD variable, appears in 43 domains."
    facts = _facts("TAETORD", "domains", 43)
    out_answer, violations = apply_counting_gate(answer, facts)
    assert out_answer == answer
    assert violations == []


# ---------------------------------------------------------------------------
# case 10: case-insensitive subject matching
# ---------------------------------------------------------------------------

def test_subject_case_insensitive():
    # Answer uses lowercase subject name — gate should still find the stated number
    answer = "taetord appears in 10 domains."
    facts = _facts("TAETORD", "domains", 43)
    _, violations = apply_counting_gate(answer, facts)
    assert len(violations) == 1
    assert violations[0]["stated"] == 10
