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
  sentence never triggers a false violation.
- Subject matching uses whole-token boundary (\\b) so short subjects like ARM,
  AGE, SEX, AE never match as substrings of longer words (alarm, usage, sexual).
- Numbers-as-words (e.g. "forty-three") are intentionally NOT matched — the gate
  only catches explicit digit strings, which is the common failure mode (LLM
  writes a wrong digit count).
- Decimal fragments (e.g. "3.5") and CT codes (e.g. "C66742") are NOT matched
  as standalone integers, preventing stray-digit false positives.
"""
from __future__ import annotations

import re

from server.structured_answer import StructuredFacts

# Split on ". ", "! ", "? " (sentence-ending punctuation + whitespace) OR on
# one-or-more newlines so that line-per-fact layouts are split correctly.
_SENT_RE = re.compile(r"(?<=[.!?])\s+|\n+")

# Match a standalone integer that is NOT:
#   - preceded by a word-char or dot  (rules out "C66742" → 66742, "3.5" → 3 or 5)
#   - followed by a word-char or dot  (rules out "43rd" → 43)
# This pattern intentionally avoids \b because \b treats "." as a boundary
# and would still extract the stray digit from "3.5".
_INT_RE = re.compile(r"(?<![\w.])\d+(?![\w.])")

_CORRECTION_HEADER = "**Authoritative correction (SDTM metadata):**"


def _sentences(text: str) -> list[str]:
    """Split *text* into sentences (best-effort; adequate for LLM prose)."""
    return _SENT_RE.split(text)


def _stated_numbers_near(answer: str, subject: str) -> list[int]:
    """Return all integers found in sentences that mention *subject* (whole-token).

    Uses whole-token boundary matching so that a short subject like "ARM" does
    not match inside "alarm", "AGE" inside "usage"/"Page", etc.  Only sentences
    containing the subject as a distinct token are examined.
    """
    subject_pattern = re.compile(
        rf"\b{re.escape(subject)}\b", re.IGNORECASE
    )
    numbers: list[int] = []
    for sent in _sentences(answer):
        if subject_pattern.search(sent):
            numbers.extend(int(m) for m in _INT_RE.findall(sent))
    return numbers


def _correction_line(v: dict) -> str:
    """Render a single correction line with kind-aware wording.

    kind == "domains"   → "<subject> appears in exactly <n> SDTM domains."
    kind == "variables" → "<subject> contains exactly <n> variables."
    anything else       → generic "<subject> has exactly <n> <kind>."
    """
    subject = v["subject"]
    kind = v["kind"]
    n = v["expected"]
    if kind == "domains":
        return f"- {subject} appears in exactly {n} SDTM domains."
    if kind == "variables":
        return f"- {subject} contains exactly {n} variables."
    return f"- {subject} has exactly {n} {kind}."


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
    correction_lines = [_correction_line(v) for v in violations]
    correction_block = (
        "\n\n---\n\n"
        + _CORRECTION_HEADER
        + "\n"
        + "\n".join(correction_lines)
    )
    return answer + correction_block, violations
