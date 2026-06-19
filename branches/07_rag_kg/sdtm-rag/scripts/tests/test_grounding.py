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

High-precision v2 regression net (must-NOT-fire — the 36 eval false-positives):
 18. correct value present via pronoun / next-sentence (C66742 / 41 domains)
 19. char-limit "8 characters" near subject must not fire when correct value absent
     ... actually correct value IS present via kind-word path → no violation
 20. char-limit "200 characters" near IE — correct value (18) present → no fire
 21. implausible number + kind-word absent — correct value present → no fire
 22. bilingual correct: "36 个 SDTM 域" present → no fire
 23. table-row index near subject — correct value present elsewhere → no fire

Must-FIRE (genuine contradiction — wrong count + kind-word adjacent + correct absent):
 24. English: wrong domain count stated, correct absent
 25. Bilingual: wrong domain count in Chinese, correct absent
 26. Variables: wrong variable count stated, correct absent
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


# ===========================================================================
# High-precision v2 regression net — must-NOT-fire (the 36 eval false-positives)
# ===========================================================================

# ---------------------------------------------------------------------------
# case 18: correct value present via pronoun / next-sentence reference
# Real failure shape from q34: "包含 4 个值...被 41 个 SDTM 域使用"
# The gate must see 41 (correct) is present → no violation, even though 4
# is also present in the same answer near the subject.
# ---------------------------------------------------------------------------

def test_correct_value_in_next_sentence_pronoun_no_violation():
    """C66742 answer: term-count 4 in one sentence, correct domain-count 41 elsewhere."""
    answer = (
        "No Yes Response (C66742) 包含 4 个值：N、NA、U、Y。"
        "该 codelist 被 41 个 SDTM 域使用。"
    )
    facts = _facts("C66742", "domains", 41)
    out_answer, violations = apply_counting_gate(answer, facts)
    assert violations == [], (
        f"False positive: correct value 41 is present, gate must not fire. "
        f"Got violations: {violations}\nAnswer: {answer}"
    )
    assert out_answer == answer


# ---------------------------------------------------------------------------
# case 19: char-limit "8 characters" near TESTCD subject — correct value is 1
# Real failure shape from q21/q22/q26/q61/q62: "不超过 8 个字符"
# Correct value (1) is present as the domain-count for LBTESTCD.
# ---------------------------------------------------------------------------

def test_char_limit_near_testcd_no_violation():
    """LBTESTCD appears in 1 domain; '8 characters' limit must not trigger gate."""
    answer = (
        "LBTESTCD 是 LB 域的主题变量。"
        "LBTESTCD 的值不能超过 8 个字符，也不能以数字开头。"
        "LBTESTCD 出现在 1 个 SDTM 域中：LB。"
    )
    facts = _facts("LBTESTCD", "domains", 1)
    out_answer, violations = apply_counting_gate(answer, facts)
    assert violations == [], (
        f"False positive on char-limit: got {violations}\nAnswer: {answer}"
    )
    assert out_answer == answer


# ---------------------------------------------------------------------------
# case 20: char-limit "200 characters" near IE/IETEST — correct values present
# Real failure shape from q27.
# ---------------------------------------------------------------------------

def test_char_limit_200_near_ie_no_violation():
    """IE domain has 18 variables; '200 characters' limit must not trigger gate."""
    answer = (
        "IE 域共包含 18 个变量。"
        "IETEST 不能超过 200 个字符。如果文本超过 200 个字符，应在 IETEST 中放入有意义的文本。"
    )
    facts_ie = _facts("IE", "variables", 18)
    out_answer, violations = apply_counting_gate(answer, facts_ie)
    assert violations == [], (
        f"False positive on 200-char-limit for IE: got {violations}"
    )
    assert out_answer == answer


# ---------------------------------------------------------------------------
# case 21: implausible number (>300) near subject, correct value absent —
# must NOT fire because 830 > _SDTM_MAX_VARIABLES plausibility bound.
# ---------------------------------------------------------------------------

def test_implausible_number_no_violation():
    """830 is implausible for domain-count (>63) → no violation even if correct absent."""
    answer = "C71620 contains 830 terms in the codelist."
    # correct value 32 is NOT present, but 830 is implausible for domains
    facts = _facts("C71620", "domains", 32)
    out_answer, violations = apply_counting_gate(answer, facts)
    # 830 > 63 (max domains), plus "terms" is not a kind-word → no fire
    assert violations == [], (
        f"Implausible number should not fire: got {violations}"
    )
    assert out_answer == answer


# ---------------------------------------------------------------------------
# case 22: bilingual correct count present → no violation
# Real pattern: "VISITDY 出现在 36 个 SDTM 域中"
# ---------------------------------------------------------------------------

def test_bilingual_correct_count_no_violation():
    """Correct count stated in Chinese → absence check sees 36 → no violation."""
    answer = "VISITDY 出现在 36 个 SDTM 域中，包括 LB、VS、EG 等。"
    facts = _facts("VISITDY", "domains", 36)
    out_answer, violations = apply_counting_gate(answer, facts)
    assert violations == [], (
        f"Bilingual correct answer must not fire: got {violations}"
    )
    assert out_answer == answer


# ---------------------------------------------------------------------------
# case 23: table-row index near subject — correct value present elsewhere
# Real failure shape from q32/q58: "| 4 | VISIT |" or "| 5 | TSPARMCD |"
# ---------------------------------------------------------------------------

def test_table_row_index_near_subject_no_violation():
    """Row index '4' in a markdown table must not trigger when correct value 36 is present."""
    answer = (
        "| 4 | VISIT | Visit Name | Char | Timing | Perm |\n"
        "VISIT 出现在 36 个 SDTM 域中。"
    )
    facts = _facts("VISIT", "domains", 36)
    out_answer, violations = apply_counting_gate(answer, facts)
    assert violations == [], (
        f"Table-row index must not fire when correct value present: got {violations}"
    )
    assert out_answer == answer


# ===========================================================================
# Must-FIRE cases — genuine contradiction (correct value absent, wrong count
# stated WITH kind-word adjacent, plausible, subject-scoped)
# ===========================================================================

# ---------------------------------------------------------------------------
# case 24: English — wrong domain count stated, correct value absent
# ---------------------------------------------------------------------------

def test_genuine_wrong_domain_count_english_fires():
    """TAETORD in 41 domains stated, correct is 43 and absent → violation fires."""
    answer = "TAETORD appears in 41 domains."
    facts = _facts("TAETORD", "domains", 43)
    out_answer, violations = apply_counting_gate(answer, facts)
    assert len(violations) == 1, f"Expected 1 violation, got {violations}"
    assert violations[0]["subject"] == "TAETORD"
    assert violations[0]["expected"] == 43
    assert violations[0]["stated"] == 41
    assert "appears in exactly 43 SDTM domains" in out_answer
    assert out_answer.startswith(answer)


# ---------------------------------------------------------------------------
# case 25: Bilingual — wrong domain count in Chinese, correct absent
# ---------------------------------------------------------------------------

def test_genuine_wrong_domain_count_bilingual_fires():
    """TAETORD 出现在 41 个域 — 41 stated in Chinese, correct 43 absent → fires."""
    answer = "TAETORD 出现在 41 个域。"
    facts = _facts("TAETORD", "domains", 43)
    out_answer, violations = apply_counting_gate(answer, facts)
    assert len(violations) == 1, f"Expected 1 violation, got {violations}"
    assert violations[0]["expected"] == 43
    assert violations[0]["stated"] == 41
    assert "43" in out_answer


# ---------------------------------------------------------------------------
# case 26: Variables — wrong variable count stated, correct absent
# ---------------------------------------------------------------------------

def test_genuine_wrong_variable_count_fires():
    """AE contains 55 variables stated, correct is 60 and absent → violation fires."""
    answer = "The AE domain contains 55 variables."
    facts = _facts("AE", "variables", 60)
    out_answer, violations = apply_counting_gate(answer, facts)
    assert len(violations) == 1, f"Expected 1 violation, got {violations}"
    assert violations[0]["subject"] == "AE"
    assert violations[0]["expected"] == 60
    assert violations[0]["stated"] == 55
    assert "contains exactly 60 variables" in out_answer


# ===========================================================================
# codelist_variables kind — must-FIRE and must-NOT-fire
# ===========================================================================

# ---------------------------------------------------------------------------
# case 27: codelist variable-count contradiction → gate FIRES
# This is the q67 hallucination shape: model says 106, truth is 123.
# ---------------------------------------------------------------------------

def test_codelist_variable_count_wrong_fires():
    """C66742 used by 123 variables; model states 106 → gate fires, appends correction."""
    answer = "C66742 is used by 106 variables across SDTM domains."
    facts = StructuredFacts(
        text_block="- **C66742** — codelist. Used by 123 variables across 41 domains.",
        checkable_counts=[
            CheckableCount(subject="C66742", kind="codelist_variables", value=123),
        ],
    )
    out_answer, violations = apply_counting_gate(answer, facts)
    assert len(violations) == 1, f"Expected 1 violation, got {violations}"
    v = violations[0]
    assert v["subject"] == "C66742"
    assert v["kind"] == "codelist_variables"
    assert v["expected"] == 123
    assert v["stated"] == 106
    # Correction uses "used by" wording (not "contains")
    assert "used by exactly 123 variables" in out_answer, (
        f"Expected 'used by exactly 123 variables' in correction, got:\n{out_answer}"
    )
    assert out_answer.startswith(answer)


# ---------------------------------------------------------------------------
# case 28: correct variable count present → must NOT fire
# ---------------------------------------------------------------------------

def test_codelist_variable_count_correct_no_fire():
    """C66742 answer states 123 variables (correct) → no violation."""
    answer = "C66742 is used by 123 variables across SDTM."
    facts = StructuredFacts(
        text_block="- **C66742** — codelist. Used by 123 variables across 41 domains.",
        checkable_counts=[
            CheckableCount(subject="C66742", kind="codelist_variables", value=123),
        ],
    )
    out_answer, violations = apply_counting_gate(answer, facts)
    assert violations == [], f"Correct count present; must not fire. Got: {violations}"
    assert out_answer == answer


# ---------------------------------------------------------------------------
# case 29: correction wording for codelist_variables uses "used by" (not "contains")
# ---------------------------------------------------------------------------

def test_correction_wording_codelist_variables():
    """kind=codelist_variables correction must say 'used by exactly N variables.'"""
    answer = "C99999 is used by 5 variables."
    facts = StructuredFacts(
        text_block="- C99999 used by 50 variables.",
        checkable_counts=[CheckableCount(subject="C99999", kind="codelist_variables", value=50)],
    )
    out_answer, violations = apply_counting_gate(answer, facts)
    assert len(violations) == 1
    assert "used by exactly 50 variables" in out_answer, (
        f"Expected 'used by exactly 50 variables' in:\n{out_answer}"
    )
    # Must NOT use "contains" wording (that's for domain→variable counts)
    assert "contains exactly 50" not in out_answer
