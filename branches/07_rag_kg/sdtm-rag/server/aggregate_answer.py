"""AGG channel: aggregate metadata queries (variables-in-min-domains / most-shared
codelists) as an independent deterministic answerer.

Split out of SP3 graph_answer (KG value eval 2026-06-21: aggregate was SP3's only
positive niche, +11~17pp when fired, but the legacy cue set fired on just 2/10 natural
phrasings). Detection is pattern-level over English quantity-threshold and superlative
shapes — zero hardcoded q-ids, no phrases lifted from any eval set.

Safety model matches SP2/SP3: a misfire injects at worst recall-additive TRUE facts.
Lower-bound thresholds only: the engine exposes variables_in_min_domains (>= semantics);
upper-bound phrasings ("fewer than", "at most", "no more than", "or fewer") MUST NOT
fire — they would inject facts answering the wrong direction.
"""
from __future__ import annotations

import re

from server.graph_engine import GraphEngine
from server.structured_answer import _CODELIST_CUES, StructuredFacts

# Lower-bound threshold shapes. Strict (exclusive) -> engine threshold n+1; inclusive
# -> n. Fixed-width lookbehinds keep negated forms ("no more than 5", "not over 20",
# "do not exceed 15" — upper bounds) out of the strict family; the postfix `(?<!\.)`
# keeps version numbers like "SDTM 3.2+" out. Group 1 is always the number.
_THRESH_STRICT_RE = re.compile(
    r"\b(?<!no )(?<!not )(?:more than|greater than|over|exceeds?|exceeding)\s+(\d{1,3})\b",
    re.IGNORECASE)
_THRESH_INCL_PRE_RE = re.compile(
    r"\b(?:at least|a minimum of|no fewer than|no less than)\s+(\d{1,3})\b",
    re.IGNORECASE)
_THRESH_INCL_POST_RE = re.compile(
    r"\b(?<!\.)(\d{1,3})\s*(?:or more|or greater|and above|\+)",
    re.IGNORECASE)

# Superlative shapes for most-shared codelists: "most shared/used/reused/common ...",
# optionally with an -ly adverb ("most widely used"), plus "largest number of" style.
_SUPERLATIVE_RE = re.compile(
    r"\bmost\s+(?:\w+ly\s+)?(?:shared|used|reused|common\w*|frequent\w*|prevalent|popular)\b"
    r"|\b(?:largest|highest|greatest|biggest)\s+number\s+of\b",
    re.IGNORECASE)


def detect_aggregate_intents(query: str) -> set[str]:
    ql = query.lower()
    intents: set[str] = set()
    # threshold: a lower-bound quantity shape AND both context words (co-occurrence
    # gate, carried over from the SP3 semantics)
    if ("variable" in ql and "domain" in ql and (
            _THRESH_STRICT_RE.search(query)
            or _THRESH_INCL_PRE_RE.search(query)
            or _THRESH_INCL_POST_RE.search(query))):
        intents.add("threshold")
    # superlative: a superlative shape AND a codelist context cue (blocks prose like
    # "most common adverse events")
    if _SUPERLATIVE_RE.search(query) and any(c in ql for c in _CODELIST_CUES):
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
            # legacy branch had that bug).
            m = _THRESH_STRICT_RE.search(query)
            if m:
                n = int(m.group(1))
                threshold, wording = n + 1, f">{n}"
            else:
                m = _THRESH_INCL_PRE_RE.search(query) or _THRESH_INCL_POST_RE.search(query)
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
