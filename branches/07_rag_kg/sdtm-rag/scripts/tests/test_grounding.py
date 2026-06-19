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
 11. short subject (ARM) must NOT match as substring of longer word (alarm)
 12. subject AGE must NOT match inside "usage" or "Page"
 13. 2-letter domain subject (AE) must NOT match inside unrelated words
 14. newline-separated lines: number on different line must not contaminate
 15. decimal "3.5" near subject must not cause false violation
 16. correction wording: kind=variables → "contains exactly N variables."
 17. correction wording: kind=domains  → "appears in exactly N SDTM domains."
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


# ---------------------------------------------------------------------------
# case 11: short subject ARM must NOT match as substring of "alarm"
# Fix 1 regression: token-boundary subject match
# ---------------------------------------------------------------------------

def test_arm_not_matched_inside_alarm():
    # "alarm" contains "arm" as a substring — must NOT trigger a violation.
    # The only sentence mentioning ARM as a standalone token states 3 (correct).
    answer = "ARM appears in 3 domains. A safety alarm triggered 12 times."
    facts = _facts("ARM", "domains", 3)
    out_answer, violations = apply_counting_gate(answer, facts)
    assert violations == [], f"Expected no violations but got: {violations}"
    assert out_answer == answer, "Answer must not be modified on correct count"


# ---------------------------------------------------------------------------
# case 12: subject AGE must NOT match inside "usage" or "Page"
# Fix 1 regression: token-boundary subject match
# ---------------------------------------------------------------------------

def test_age_not_matched_inside_usage_or_page():
    # "usage" and "Page" both contain "age" — the 99/7 must not be attributed to AGE.
    answer = "AGE appears in 5 domains. Check usage of the variable on Page 99 with 7 items."
    facts = _facts("AGE", "domains", 5)
    out_answer, violations = apply_counting_gate(answer, facts)
    assert violations == [], f"Expected no violations but got: {violations}"
    assert out_answer == answer


# ---------------------------------------------------------------------------
# case 13: 2-letter domain subject AE must NOT match inside unrelated words
# Fix 1 regression: short-code false positive
# ---------------------------------------------------------------------------

def test_ae_not_matched_inside_unrelated_word():
    # "adverse" contains "ae" as a substring — 42 must not be attributed to AE.
    answer = "AE contains 10 variables. Adverse events happened 42 times."
    facts = _facts("AE", "variables", 10)
    out_answer, violations = apply_counting_gate(answer, facts)
    assert violations == [], f"Expected no violations but got: {violations}"
    assert out_answer == answer


# ---------------------------------------------------------------------------
# case 14: newline-separated lines — number on a different line must not bleed
# Fix 2 regression: sentence splitter must handle newlines
# ---------------------------------------------------------------------------

def test_newline_separated_no_contamination():
    # TAETORD correct (43); VISITDY's 36 is on its own line and must not contaminate.
    answer = "TAETORD appears in 43 domains\nVISITDY appears in 36 domains"
    facts = _facts("TAETORD", "domains", 43)
    out_answer, violations = apply_counting_gate(answer, facts)
    assert violations == [], f"Expected no violations but got: {violations}"
    assert out_answer == answer


# ---------------------------------------------------------------------------
# case 15: decimal "3.5" near subject must NOT cause a false violation
# Fix 3 regression: decimal-safe integer regex
# ---------------------------------------------------------------------------

def test_decimal_near_subject_no_false_violation():
    # The correct count is 4; "3.5" near the subject must not extract stray 3 or 5.
    answer = "RATIO has a mean of 3.5 and RATIO appears in 4 domains."
    facts = _facts("RATIO", "domains", 4)
    out_answer, violations = apply_counting_gate(answer, facts)
    assert violations == [], f"Expected no violations but got: {violations}"
    assert out_answer == answer


# ---------------------------------------------------------------------------
# case 16 & 17: correction wording is kind-aware
# Fix 4: kind=variables → "contains exactly N variables."
#         kind=domains  → "appears in exactly N SDTM domains."
# ---------------------------------------------------------------------------

def test_correction_wording_variables():
    # A domain that "contains" variables — correction must say "contains exactly N variables."
    answer = "AE contains 99 variables."
    facts = _facts("AE", "variables", 10)
    out_answer, violations = apply_counting_gate(answer, facts)
    assert len(violations) == 1
    assert "contains exactly 10 variables" in out_answer, (
        f"Expected 'contains exactly 10 variables' in correction block, got:\n{out_answer}"
    )
    # Must NOT use the "appears in" wording for variables
    assert "appears in exactly 10 variables" not in out_answer


def test_correction_wording_domains():
    # A variable that "appears in" domains — correction must say "appears in exactly N SDTM domains."
    answer = "TAETORD appears in 5 domains."
    facts = _facts("TAETORD", "domains", 43)
    out_answer, violations = apply_counting_gate(answer, facts)
    assert len(violations) == 1
    assert "appears in exactly 43 SDTM domains" in out_answer, (
        f"Expected 'appears in exactly 43 SDTM domains' in correction block, got:\n{out_answer}"
    )
