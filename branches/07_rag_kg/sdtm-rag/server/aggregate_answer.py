"""AGG channel: aggregate metadata queries (variables-in-min-domains / most-shared
codelists) as an independent deterministic answerer.

Split out of SP3 graph_answer (KG value eval 2026-06-21: aggregate was SP3's only
positive niche, +11~17pp when fired, but the legacy cue set fired on just 2/10 natural
phrasings). Detection is pattern-level over English quantity-threshold and superlative
shapes — zero hardcoded q-ids, no phrases lifted from any eval set.

Held-out gate remedy (agg_attempt_1, fired 4/16): threshold matching now normalizes
spelled-out number words ("nine", "a dozen") to digits before matching, and tolerates
one noun between the number and a word-bound phrase ("38 domains or more"). Superlative
matching adds comparative ("more X than any other"), postposed "the most" (determiner
and adverbial forms), extra spread-noun adjectives (widest/broadest range/variety), and
hyphenated "most-X" compounds — all still gated by the codelist-cue co-occurrence check.
Round 4 (agg_attempt_2, fresh blind set fired 12/16): adds the numeric "plus" postfix
("30-plus domains") to the threshold family and the top-N ranking request ("the top
three codelists", "the top few") to the superlative family; metaphoric superlatives
("the clear champion") are a documented known limit, not patched.

Safety model matches SP2/SP3: a misfire injects at worst recall-additive TRUE facts.
Lower-bound thresholds only: the engine exposes variables_in_min_domains (>= semantics);
upper-bound phrasings ("fewer than", "at most", "no more than", "or fewer") MUST NOT
fire — they would inject facts answering the wrong direction.
"""
from __future__ import annotations

import re

from server.graph_engine import GraphEngine
from server.structured_answer import _CODELIST_CUES, StructuredFacts

# Spelled-out number words -> digits, for threshold matching only. Word-boundary,
# case-insensitive; the negative lookaround excludes hyphenated compounds ("twenty-one")
# so they pass through untouched rather than being partially normalized.
_NUMBER_WORDS = {
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7,
    "eight": 8, "nine": 9, "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13,
    "fourteen": 14, "fifteen": 15, "sixteen": 16, "seventeen": 17, "eighteen": 18,
    "nineteen": 19, "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60,
}
_NUMBER_WORD_RE = re.compile(
    r"(?<![\w-])(" + "|".join(_NUMBER_WORDS) + r")(?![\w-])", re.IGNORECASE)
# Dozen resolution is ALLOWLIST-only (round 3): exactly "a dozen"/"a-dozen" -> 12,
# blocked when preceded by "half "/"half-". Every other dozen form (bare "dozen",
# "couple dozen", "several dozen", "two dozen", "2 dozen", odd spacing) stays a
# word — no digit appears, so the threshold regexes cannot fire. A wrong-magnitude
# fire is worse than silence: anything multiplied or ambiguous FAILS CLOSED.
_A_DOZEN_RE = re.compile(r"\b(?<!half )(?<!half-)a[\s-]dozen\b", re.IGNORECASE)


def _normalize_numbers(text: str) -> str:
    """Replace standalone spelled-out number words (one..twenty, thirty, forty, fifty,
    sixty) and the exact allowlisted phrase "a dozen"/"a-dozen" with digits, so
    threshold regexes (which only match `\\d{1,3}`) can see them. Hyphenated number
    compounds are left untouched; any multiplied/ambiguous dozen ("two dozen", "half
    a dozen", "several dozen", bare "dozen") is deliberately NOT resolved — fail
    closed rather than fire with the wrong magnitude."""
    text = _NUMBER_WORD_RE.sub(lambda m: str(_NUMBER_WORDS[m.group(1).lower()]), text)
    return _A_DOZEN_RE.sub("12", text)


# Lower-bound threshold shapes. Strict (exclusive) -> engine threshold n+1; inclusive
# -> n. Fixed-width lookbehinds keep negated forms ("no more than 5", "not over 20",
# "do not exceed 15" — upper bounds) out of the strict family; the postfix `(?<!\.)`
# keeps version numbers like "SDTM 3.2+" / "SDTM 3.2-plus" out. Group 1 is always
# the number. The word-bound alternatives tolerate ONE optional noun/modifier between
# the number and the bound phrase ("38 domains or more"); the symbol `+` and the word
# "plus" ("30-plus", "30 plus" — round 4 shape class 7) stay adjacent to the digit.
# The gap word must not be "dozen": a multiplier there means the digit is NOT the
# real quantity ("2 dozen or more" would fire n=2) — fail closed instead.
_THRESH_STRICT_RE = re.compile(
    r"\b(?<!no )(?<!not )(?:more than|greater than|over|exceeds?|exceeding)\s+(\d{1,3})\b",
    re.IGNORECASE)
_THRESH_INCL_PRE_RE = re.compile(
    r"\b(?:at least|a minimum of|no fewer than|no less than)\s+(\d{1,3})\b",
    re.IGNORECASE)
_THRESH_INCL_POST_RE = re.compile(
    r"\b(?<!\.)(\d{1,3})\s*(?:(?:(?!dozen\b)[A-Za-z]+\s+)?(?:or more|or greater|and above)"
    r"|\+|[\s-]*plus\b)",
    re.IGNORECASE)

# Superlative shapes for most-shared codelists:
# - preposed "most (adverb) shared/used/..." (spaces or hyphens: "most-used", "most
#   widely-used"); comparative "more X than any other"; postposed "the most", either
#   as a bare determiner ("the most variables") or an adverbial usage-verb-then-"the
#   most" construction ("gets shared ... the most"); superlative adjective + spread
#   noun ("largest number of", "widest range of", "broadest variety of").
# The adverbial form covers present-tense verbs too ("sponsors reference the most",
# "recycles the most") and is clause-bound: the verb-to-"the most" gap excludes
# , ; : and em/en dashes and is capped at 40 chars, so a usage verb in one clause
# cannot link to "the most" in an unrelated one.
_SUPERLATIVE_RE = re.compile(
    r"\bmost[\s-]+(?:\w+ly[\s-]+)?(?:shared|used|reused|common\w*|frequent\w*|prevalent|popular)\b"
    r"|\b(?:largest|highest|greatest|biggest|widest|broadest)\s+(?:number|count|range|spread|variety)\s+of\b"
    r"|\bmore\s+\w+\s+than\s+any\s+other\b"
    r"|\bthe\s+most\s+variables\b"
    r"|\b(?:share[ds]?|used?|uses|reuse[ds]?|drawn|draws?|reference[ds]?|recycle[ds]?)\b"
    r"[^.?!,;:—–]{0,40}\bthe\s+most\b",
    re.IGNORECASE)

# Top-N ranking request (round 4 shape class 8): "the top three codelists", "give me
# the top few" — a ranking with a cutoff is a most-shared query even with no
# superlative token. Matched on the number-normalized text ("top three" -> "top 3");
# requires a quantifier right after "top" (digit or few/several/couple), so "on top
# of" / "top priority" stay out. Same codelist-cue co-occurrence gate as above.
_TOP_N_RE = re.compile(r"\btop\s+(?:\d{1,3}|few|several|couple)\b", re.IGNORECASE)


def detect_aggregate_intents(query: str) -> set[str]:
    ql = query.lower()
    norm = _normalize_numbers(query)
    intents: set[str] = set()
    # threshold: a lower-bound quantity shape AND both context words (co-occurrence
    # gate, carried over from the SP3 semantics); matched on the number-normalized text
    if ("variable" in ql and "domain" in ql and (
            _THRESH_STRICT_RE.search(norm)
            or _THRESH_INCL_PRE_RE.search(norm)
            or _THRESH_INCL_POST_RE.search(norm))):
        intents.add("threshold")
    # superlative: a superlative shape (raw text) or a top-N ranking request
    # (normalized text), AND a codelist context cue (blocks prose like "most common
    # adverse events" / "top three products")
    if ((_SUPERLATIVE_RE.search(query) or _TOP_N_RE.search(norm))
            and any(c in ql for c in _CODELIST_CUES)):
        intents.add("superlative")
    return intents


class AggregateAnswerer:
    """Deterministic aggregate answerer over GraphEngine (read-only, stateless)."""

    def __init__(self, engine: GraphEngine):
        self.engine = engine

    def resolve(self, query: str) -> StructuredFacts | None:
        intents = detect_aggregate_intents(query)
        if not intents:
            return None
        lines: list[str] = []

        if "threshold" in intents:
            # Strict beats inclusive when both shapes appear; n comes from the matched
            # threshold expression itself (NOT the first bare digit in the query — the
            # legacy branch had that bug). Matched on number-normalized text so spelled-
            # out number words ("nine or more") resolve to the right n.
            norm = _normalize_numbers(query)
            m = _THRESH_STRICT_RE.search(norm)
            if m:
                n = int(m.group(1))
                threshold, wording = n + 1, f">{n}"
            else:
                m = _THRESH_INCL_PRE_RE.search(norm) or _THRESH_INCL_POST_RE.search(norm)
                # Invariant: detect_aggregate_intents() only sets "threshold" when one of
                # the three regexes matches this SAME normalized query; if STRICT didn't
                # match above, one of PRE/POST must (mypy can't see across functions).
                assert m is not None, "threshold intent detected but no threshold regex matched"
                n = int(m.group(1))
                threshold, wording = n, f"≥{n}"
            res = self.engine.variables_in_min_domains(threshold)
            if res:
                listed = ", ".join(f"{v} ({c})" for v, c in res[:50])
                lines.append(
                    f"- **{len(res)}** variables appear in {wording} domains: {listed}."
                )

        if "superlative" in intents:
            top = self.engine.most_shared_codelists(5)
            listed = ", ".join(
                f"{t['code']} ({t['name']}, {t['n_variables']} vars)" for t in top)
            lines.append(f"- Most-shared codelists: {listed}.")

        if not lines:
            return None
        return StructuredFacts(text_block="\n".join(lines), checkable_counts=[])
