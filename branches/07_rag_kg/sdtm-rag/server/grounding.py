"""Deterministic counting grounding gate (SP2 Phase 1).

apply_counting_gate(answer, facts) checks every CheckableCount in facts against
the integers stated in the LLM answer.  It is NON-DESTRUCTIVE: when a contradiction
is found (a different explicit number stated for the subject) the original answer
text is left intact and an authoritative correction block is APPENDED.  A missing
number is NOT a violation — the facts block injected upstream already supplied it.

Design points
-------------
- Pure function: no app / IO / global state.  Safe to call from router.py and
  eval scripts identically.
- Conservative scoping: _stated_numbers_near() only inspects sentences that
  CONTAIN the subject (case-insensitive).  An unrelated number in a different
  sentence never triggers a false positive.
- Numbers-as-words (e.g. "forty-three") are intentionally NOT matched — the gate
  only catches explicit digit strings, which is the common failure mode (LLM
  writes a wrong digit count).
"""
from __future__ import annotations

import re

from server.structured_answer import StructuredFacts

# Split into sentences on ". ", "! ", "? " or end-of-string, keeping the delimiter.
_SENT_RE = re.compile(r"(?<=[.!?])\s+")

# Extract integers (digit sequences) from a string.
_INT_RE = re.compile(r"\b(\d+)\b")

_CORRECTION_HEADER = "**Authoritative correction (SDTM metadata):**"


def _sentences(text: str) -> list[str]:
    """Split *text* into sentences (best-effort; adequate for LLM prose)."""
    return _SENT_RE.split(text)


def _stated_numbers_near(answer: str, subject: str) -> list[int]:
    """Return all integers found in sentences that mention *subject* (case-insensitive).

    Only sentences containing the subject are examined, so an unrelated number
    elsewhere in the answer never triggers a false violation.
    """
    subject_lower = subject.lower()
    numbers: list[int] = []
    for sent in _sentences(answer):
        if subject_lower in sent.lower():
            numbers.extend(int(m) for m in _INT_RE.findall(sent))
    return numbers


def apply_counting_gate(
    answer: str,
    facts: StructuredFacts | None,
) -> tuple[str, list[dict]]:
    """Gate the answer against deterministic counts from *facts*.

    Parameters
    ----------
    answer:
        The raw LLM answer string.
    facts:
        StructuredFacts produced by StructuredAnswerer.resolve(), or None.

    Returns
    -------
    (possibly_appended_answer, violations)
        *violations* is a list of dicts with keys subject/kind/expected/stated.
        If no violations, the original *answer* is returned unchanged and
        *violations* is [].
    """
    if facts is None or not facts.checkable_counts:
        return answer, []

    violations: list[dict] = []

    for cc in facts.checkable_counts:
        stated_numbers = _stated_numbers_near(answer, cc.subject)
        if not stated_numbers:
            # No explicit number stated for this subject — not a contradiction.
            continue
        # A contradiction exists if ANY stated number differs from the expected value.
        for num in stated_numbers:
            if num != cc.value:
                violations.append(
                    {
                        "subject": cc.subject,
                        "kind": cc.kind,
                        "expected": cc.value,
                        "stated": num,
                    }
                )
                break  # one violation record per CheckableCount is sufficient

    if not violations:
        return answer, []

    # Build one correction block for ALL violations (non-destructive append).
    correction_lines = [
        f"- {v['subject']} appears in exactly {v['expected']} {v['kind']}."
        for v in violations
    ]
    correction_block = (
        "\n\n---\n\n"
        + _CORRECTION_HEADER
        + "\n"
        + "\n".join(correction_lines)
    )
    return answer + correction_block, violations
