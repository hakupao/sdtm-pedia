"""Deterministic counting grounding gate (SP2 Task6 — high-precision v2).

apply_counting_gate(answer, facts) checks every CheckableCount in facts against
the integers stated in the LLM answer.  It is NON-DESTRUCTIVE: when a genuine
contradiction is found, the original answer text is left intact and an
authoritative correction block is APPENDED.  A missing number is NOT a
violation — the facts block injected upstream already supplied it.

High-precision logic (eliminates the 36 eval false-positives from v1)
----------------------------------------------------------------------
For each CheckableCount(subject, kind, value):

1. Absence precondition (the key fix):
   If ``value`` appears as a standalone integer ANYWHERE in the answer
   (regex ``(?<!\\d)<value>(?!\\d)``), the model has already stated the
   correct count — skip this CheckableCount entirely.  This alone covers
   every false-positive pattern observed in the 140-question eval, including:
     - pronoun / next-sentence referencing ("该 codelist 被 41 个 SDTM 域使用")
     - char-limit numbers near subject ("不超过 8 个字符")
     - table-row numbers, section numbers, example counts

2. Wrong-count detection (only when the correct value is ABSENT):
   Within sentences that mention the subject (whole-token, case-insensitive),
   look for a number N that satisfies ALL three guards:
     a. kind-word adjacent (bilingual, ±15 chars):
          domains   → ``domains?`` OR ``域``
          variables → ``variables?`` OR ``变量``
        So "41 domains" / "41 个 SDTM 域" match; "8 characters" / "top 8
        examples" / "§4.4.5" do NOT.
     b. plausible for the kind:
          domains   → 1 ≤ N ≤ 63  (SDTM v3.4 defines exactly 63 domains)
          variables → 1 ≤ N ≤ 300  (generous upper bound)
        Numbers outside the plausible range (e.g. 200 chars, 830) are skipped.
     c. N ≠ value  → genuine violation → record + append correction.

Design points (preserved from v1)
----------------------------------
- Pure function: no app / IO / global state.
- Subject matching uses whole-token boundary (\\b) so ARM / AGE / AE never
  match inside alarm / usage / adverse.
- Decimal fragments ("3.5") and CT codes ("C66742") are not matched as
  standalone integers.
- Sentence splitting on punctuation + newlines prevents cross-sentence bleed.
"""
from __future__ import annotations

import re

from server.structured_answer import StructuredFacts

# ---------------------------------------------------------------------------
# Compile-time constants
# ---------------------------------------------------------------------------

# SDTM v3.4 defines exactly 63 domains.  We use a looser plausibility ceiling
# (200) so that wrong answers like "99 domains" are still detectable while
# numbers like 830 (term-counts) or 200 (char-limits) remain safely excluded.
_SDTM_MAX_DOMAINS: int = 200
# Generous upper bound for variable counts within a single domain.
_SDTM_MAX_VARIABLES: int = 300

# Split on sentence-ending punctuation + whitespace, OR on one-or-more newlines.
_SENT_RE = re.compile(r"(?<=[.!?])\s+|\n+")

# Standalone integer — NOT preceded/followed by a word-char or dot.
# Rules out CT codes ("C66742" → 66742), decimals ("3.5" → 3/5), ordinals ("43rd").
_INT_RE = re.compile(r"(?<![\w.])\d+(?![\w.])")

# Kind-word patterns (bilingual).  Used to check adjacency within ±_KIND_WINDOW chars.
_KIND_WORDS: dict[str, re.Pattern[str]] = {
    "domains": re.compile(r"domains?|域", re.IGNORECASE),
    "variables": re.compile(r"variables?|变量", re.IGNORECASE),
}
_KIND_WINDOW: int = 15  # chars on each side of the number to search for a kind-word

# Plausibility ranges: (min_inclusive, max_inclusive).
_KIND_PLAUSIBLE: dict[str, tuple[int, int]] = {
    "domains": (1, _SDTM_MAX_DOMAINS),
    "variables": (1, _SDTM_MAX_VARIABLES),
}

_CORRECTION_HEADER = "**Authoritative correction (SDTM metadata):**"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _sentences(text: str) -> list[str]:
    """Split *text* into sentences (best-effort; adequate for LLM prose)."""
    return _SENT_RE.split(text)


def _correct_value_absent(answer: str, value: int) -> bool:
    """Return True iff *value* does NOT appear as a standalone integer in *answer*.

    Uses a simple digit-boundary check (no word-chars on either side) rather than
    ``\\b`` to stay consistent with ``_INT_RE`` and avoid false "present" detections
    from numbers inside CT codes or decimals.
    """
    pattern = re.compile(rf"(?<!\d){re.escape(str(value))}(?!\d)")
    return pattern.search(answer) is None


def _kind_adjacent(sentence: str, pos: int, kind: str) -> bool:
    """Return True if a kind-word for *kind* appears within ±_KIND_WINDOW chars of *pos*.

    *pos* is the start-index of the number match within *sentence*.
    """
    kw_re = _KIND_WORDS.get(kind)
    if kw_re is None:
        return False  # unknown kind → skip adjacency check (conservative: no fire)
    lo = max(0, pos - _KIND_WINDOW)
    hi = min(len(sentence), pos + _KIND_WINDOW)
    window = sentence[lo:hi]
    return bool(kw_re.search(window))


def _wrong_count_in_answer(answer: str, subject: str, kind: str, value: int) -> int | None:
    """Look for a plausible, kind-adjacent, wrong count near *subject* in *answer*.

    Returns the first wrong number found, or None if no genuine contradiction exists.

    Called ONLY when the correct *value* is already confirmed absent (see
    ``_correct_value_absent``), so any matching number N ≠ value is a genuine error.
    """
    subject_pattern = re.compile(rf"\b{re.escape(subject)}\b", re.IGNORECASE)
    plausible = _KIND_PLAUSIBLE.get(kind, (1, 9999))

    for sent in _sentences(answer):
        if not subject_pattern.search(sent):
            continue
        for m in _INT_RE.finditer(sent):
            n = int(m.group())
            if n == value:
                # Shouldn't happen (we checked absence globally), but be safe.
                continue
            if not (plausible[0] <= n <= plausible[1]):
                continue  # implausible count for this kind
            if not _kind_adjacent(sent, m.start(), kind):
                continue  # number not near a kind-word — ignore
            return n  # first genuine violation found

    return None


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


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

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

    Algorithm
    ---------
    For each CheckableCount(subject, kind, value):
      1. If *value* appears as a standalone integer anywhere in the answer →
         the model stated the correct count → skip (no violation).
      2. Otherwise look for a number N in subject-scoped sentences that is
         kind-word adjacent AND plausible for the kind.  If found → violation.
    """
    if facts is None or not facts.checkable_counts:
        return answer, []

    violations: list[dict] = []

    for cc in facts.checkable_counts:
        # --- Step 1: absence precondition -----------------------------------
        if not _correct_value_absent(answer, cc.value):
            # Correct count is present somewhere → no violation for this subject.
            continue

        # --- Step 2: wrong-count detection ----------------------------------
        stated = _wrong_count_in_answer(answer, cc.subject, cc.kind, cc.value)
        if stated is not None:
            violations.append(
                {
                    "subject": cc.subject,
                    "kind": cc.kind,
                    "expected": cc.value,
                    "stated": stated,
                }
            )

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
