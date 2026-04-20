#!/usr/bin/env python3
"""Domain scorer for SDTM Phase 6.5 v2 batch 2 (high-frequency domains).

Computes a per-domain utility score and recommends a merge set of 25-28
domains for batch 2 of the v2 expansion plan (see PLAN_V2.md §4,
design doc §2.3).

Scoring formula (strict per spec):
    score = 0.4 * normalize(cross_ref_count)
          + 0.4 * normalize(examples_tokens)
          + 0.2 * (20 if domain in T_test_hits else 0)

Signals:
    - cross_ref_count: number of word-boundary matches of the domain
      abbreviation (e.g. \\bAE\\b) in knowledge_base/VARIABLE_INDEX.md.
      Captures both cross-domain variable lists and per-domain sections.
    - examples_tokens: tiktoken cl100k_base token count of
      knowledge_base/domains/<DOMAIN>/examples.md (0 if file missing).
    - T_test_hits: domains that actually hit the baseline test set
      (from v1 T1-T8 audit); given a fixed boost.

Why min-max normalization:
    We need each signal bounded to [0, 1] so the weighted sum is
    interpretable and independent of the raw scale (cross-ref counts are
    typically <30 while examples token counts can exceed 10k). Min-max is
    simple, deterministic, and robust enough for a ranked top-N cut.
    Z-score would need a distribution assumption we don't have, and
    log-scaling would obscure the flat region where most mid-tier domains
    live. We want lossless ordering, not statistical inference.

Usage:
    cd <repo root>
    python3 ai_platforms/claude_projects/scripts_v2/score_domains.py

Read-only: only reads knowledge_base/; writes nothing.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import tiktoken

# --- Configuration (hardcoded per spec) -------------------------------------

ENCODING_NAME = "cl100k_base"

# Full list of SDTM domains (63, matches knowledge_base/domains/).
ALL_DOMAINS: list[str] = [
    "AE", "AG", "BE", "BS", "CE", "CM", "CO", "CP", "CV", "DA",
    "DD", "DM", "DS", "DV", "EC", "EG", "EX", "FA", "FT", "GF",
    "HO", "IE", "IS", "LB", "MB", "MH", "MI", "MK", "ML", "MS",
    "NV", "OE", "OI", "PC", "PE", "PP", "PR", "QS", "RE", "RELREC",
    "RELSPEC", "RELSUB", "RP", "RS", "SC", "SE", "SM", "SR", "SS", "SU",
    "SUPPQUAL", "SV", "TA", "TD", "TE", "TI", "TM", "TR", "TS", "TU",
    "TV", "UR", "VS",
]

# User-selected must-include domains (batch 1 + design choice).
USER_MUST: list[str] = [
    "DM", "SE", "DS", "BS", "BE", "MI", "GF", "PR", "CM", "EX",
    "TU", "TR", "RS", "SS", "DD", "LB", "FA", "CE", "MH", "SU",
]

# Domains that hit the baseline T1-T8 tests; fixed bonus term.
T_TEST_HITS: list[str] = ["AE", "PC", "PP", "EX", "MH", "LB"]

# Merge-list size target (inclusive).
MERGE_MIN = 25
MERGE_MAX = 28

# --- Paths ------------------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parents[3]
VAR_INDEX = REPO_ROOT / "knowledge_base" / "VARIABLE_INDEX.md"
DOMAINS_DIR = REPO_ROOT / "knowledge_base" / "domains"


# --- Signal extraction ------------------------------------------------------


def count_cross_refs(index_text: str, domain: str) -> int:
    """Count word-boundary occurrences of DOMAIN in VARIABLE_INDEX.md text."""
    pattern = re.compile(rf"\b{re.escape(domain)}\b")
    return len(pattern.findall(index_text))


def count_examples_tokens(encoder: "tiktoken.Encoding", domain: str) -> int:
    """Return tiktoken cl100k_base token count of domains/<domain>/examples.md.

    Returns 0 if the file does not exist (not an error).
    """
    path = DOMAINS_DIR / domain / "examples.md"
    if not path.is_file():
        return 0
    return len(encoder.encode(path.read_text(encoding="utf-8", errors="strict")))


# --- Scoring ----------------------------------------------------------------


def min_max_normalize(values: dict[str, int]) -> dict[str, float]:
    """Min-max normalize a {key: int} map to {key: float in [0, 1]}.

    If max == min (degenerate), return 0.0 for every key.
    """
    if not values:
        return {}
    vs = list(values.values())
    lo, hi = min(vs), max(vs)
    if hi == lo:
        return {k: 0.0 for k in values}
    span = hi - lo
    return {k: (v - lo) / span for k, v in values.items()}


def compute_scores(
    cross_refs: dict[str, int],
    examples_tokens: dict[str, int],
) -> dict[str, float]:
    """Apply scoring formula, return {domain: score} (floats).

    Note: spec formula has `0.2 * (20 if hit else 0)` — the 20 is a flat
    bonus (= 4.0 contribution) on top of the normalized signals. We
    implement it verbatim.
    """
    norm_refs = min_max_normalize(cross_refs)
    norm_toks = min_max_normalize(examples_tokens)
    out: dict[str, float] = {}
    for d in sorted(cross_refs):
        hit_bonus = 0.2 * (20 if d in T_TEST_HITS else 0)
        out[d] = 0.4 * norm_refs[d] + 0.4 * norm_toks[d] + hit_bonus
    return out


# --- Main -------------------------------------------------------------------


def main() -> int:
    if not VAR_INDEX.is_file():
        print(f"error: VARIABLE_INDEX.md not found at {VAR_INDEX}", file=sys.stderr)
        return 2
    if not DOMAINS_DIR.is_dir():
        print(f"error: domains/ not found at {DOMAINS_DIR}", file=sys.stderr)
        return 2

    encoder = tiktoken.get_encoding(ENCODING_NAME)
    index_text = VAR_INDEX.read_text(encoding="utf-8", errors="strict")

    domains = sorted(ALL_DOMAINS)

    cross_refs = {d: count_cross_refs(index_text, d) for d in domains}
    examples_tokens = {d: count_examples_tokens(encoder, d) for d in domains}
    scores = compute_scores(cross_refs, examples_tokens)

    # Must-include set: user picks + T_test_hits, dedup, deterministic order.
    must_set = sorted(set(USER_MUST) | set(T_TEST_HITS))

    # Section 1: must-include list.
    print("# 必选域 (用户清单 + T_test_hits, 去重)")
    for d in sorted(USER_MUST):
        print(f"{d}: must (user)")
    extra_from_tests = sorted(set(T_TEST_HITS) - set(USER_MUST))
    for d in extra_from_tests:
        print(f"{d}: must (T_test_hits)")
    print()

    # Section 2: scored ranking (excluding must-set), top 20.
    print("# 打分排序 (除必选外, top 20)")
    scored = [(d, s) for d, s in scores.items() if d not in must_set]
    # Primary key: score desc; tiebreak: domain asc — stable & idempotent.
    scored.sort(key=lambda kv: (-kv[1], kv[0]))
    top_ranked = scored[:20]
    for d, s in top_ranked:
        print(f"{d}: {s:.2f}")
    print()

    # Section 3: recommended merge set — must + top-N until size in [25, 28].
    # Greedy: keep adding from ranked list; stop at MERGE_MAX; must already
    # gives us len(must_set) entries (24-26 for this config).
    target = MERGE_MAX  # fill to the ceiling, then verify floor.
    remaining_slots = max(0, target - len(must_set))
    add_from_rank = [d for d, _ in scored[:remaining_slots]]
    merge_set = sorted(set(must_set) | set(add_from_rank))
    # Clamp down if somehow > MERGE_MAX (shouldn't happen with our math).
    if len(merge_set) > MERGE_MAX:
        # Drop lowest-scored non-must domains.
        non_must_sorted = sorted(
            (d for d in merge_set if d not in must_set),
            key=lambda x: (scores.get(x, 0.0), x),
        )
        while len(merge_set) > MERGE_MAX and non_must_sorted:
            merge_set.remove(non_must_sorted.pop(0))
        merge_set = sorted(merge_set)

    print(f"# 推荐合并清单 (必选 + top N 直至总数 {MERGE_MIN}-{MERGE_MAX}):")
    print(f"[{', '.join(merge_set)}]  # 共 {len(merge_set)} 域")

    # Post-condition check (defensive): verify size constraint.
    if not (MERGE_MIN <= len(merge_set) <= MERGE_MAX):
        print(
            f"warning: merge set size {len(merge_set)} outside [{MERGE_MIN}, {MERGE_MAX}]",
            file=sys.stderr,
        )
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
