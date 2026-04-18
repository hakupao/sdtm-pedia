#!/usr/bin/env python3
"""Codelist scorer for SDTM Phase 6.5 v2 batch 4 (top 200) + batch 5 (rank 201-500).

Computes a per-codelist utility score and ranks all CDISC codelists found
in knowledge_base/terminology/ for the v2 expansion plan (see PLAN_V2.md
§4 / design doc §2.5).

Scoring formula (strict per spec):

    score = 0.5 * normalize(domain_ref_count)   # referenced by domain specs
          + 0.3 * sigmoid_term(term_count)      # codelist body term count
          + 0.2 * (50 if name in T_codelist_hits else 0)

Signals:
    - domain_ref_count: number of occurrences of the codelist's CDISC
      C-code (e.g. C66742) in knowledge_base/domains/*/spec.md. Domain
      specs link to codelists by `(C-code)` in their Controlled Terms
      references, so the C-code is the stable reference key.
    - term_count: number of table body rows inside the codelist section,
      counted by the regex `^\\| C\\d+` (every real CDISC term row starts
      with a code like `C12345`).
    - T_codelist_hits: known high-impact codelists from the v1 baseline
      test set. We match by CDISC short name (NY, AERELN, FREQ,
      PROBLEM_TYPE). Only NY (C66742) and FREQ (C71113) exist in this
      knowledge_base; AERELN and PROBLEM_TYPE are listed for forward
      compatibility and simply yield no bonus if absent.

Why sigmoid_term is shaped this way (center=30, two-sided decay):
    We want to favor codelists with a moderately-sized controlled term
    list. Codelists with <3 terms carry almost no information beyond what
    the domain spec already states (useless for RAG grounding). Codelists
    with >500 terms (e.g. Anatomical Location, MedDRA) blow the token
    budget and are better linked than inlined. The sweet spot for
    "educational, fits in a budget, covers real clinical ambiguity" is
    around 20-50 terms (e.g. Frequency, Severity, Route, Outcome). We
    encode this with a log-distance decay centered at log10(30):

        f(n) = 1 / (1 + |log10(n+1) - log10(30)|)   if n > 0 else 0

    This is a symmetric hat in log space: peaks at n=30 (≈1.0), decays
    smoothly toward 0 for very small (n=1 → 0.4) or very large
    (n=1000 → 0.37) codelists. No tunable hyperparameters beyond the
    hard-coded center of 30, which is the median "useful" size observed
    in the CDISC CT corpus.

Min-max normalization (domain_ref_count):
    domain_ref_count has a long tail: most codelists are referenced 0-2
    times, a handful 20+ times. Min-max keeps the weighted sum
    interpretable and scale-free. If max == min (degenerate, all zero),
    we yield 0.0 for every codelist rather than a NaN.

Usage:
    cd <repo root>
    python3 ai_platforms/claude_projects/scripts_v2/score_codelists.py

Read-only: reads only knowledge_base/; writes nothing to disk. All
output goes to stdout (three sections: top 200, rank 201-500, stats).
"""
from __future__ import annotations

import math
import re
import sys
from pathlib import Path

# --- Configuration (hardcoded per spec) -------------------------------------

# Short names from v1 T-test baseline that should receive the fixed bonus.
# Map: short_name -> C-code. Only codelists that actually exist in the
# knowledge_base contribute to the bonus; missing ones are benign (no-op).
T_CODELIST_HITS: dict[str, str] = {
    "NY": "C66742",        # No Yes Response
    "AERELN": "",          # Not present in this knowledge_base
    "FREQ": "C71113",      # Frequency
    "PROBLEM_TYPE": "",    # Not present in this knowledge_base
}

# Sigmoid_term center (median "useful" codelist size).
SIGMOID_CENTER_N = 30

# Batch cutoffs (spec).
TOP_N_BATCH4 = 200
RANK_START_BATCH5 = 201
RANK_END_BATCH5 = 500

# Token-per-term heuristic for capacity estimation (spec simplification).
TOKENS_PER_TERM = 30

# --- Paths ------------------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parents[3]
TERMINOLOGY_DIR = REPO_ROOT / "knowledge_base" / "terminology"
DOMAINS_DIR = REPO_ROOT / "knowledge_base" / "domains"

# Codelist heading: `## Full Name (Cnnnnn)` — captures name and C-code.
CODELIST_HEADING_RE = re.compile(r"^##\s+(.+?)\s+\((C\d+)\)\s*$")
# Term row: markdown table body line starting with `| C<digits>`.
TERM_ROW_RE = re.compile(r"^\|\s*C\d+\s*\|")


# --- Parsing ----------------------------------------------------------------


def parse_codelists(term_dir: Path) -> list[tuple[str, str, int]]:
    """Walk terminology/ and yield (c_code, full_name, term_count).

    Deduplication: the same codelist can be split across multiple files
    (e.g. general_part1.md, general_part2.md) or repeat in multiple files
    (e.g. eg_part1.md and eg_part3.md both contain ATRIAL BIGEMINY rows).
    We aggregate by C-code: sum term_counts across all files that host
    a `## ... (Cnnnnn)` section for the same code.
    """
    # c_code -> [full_name, accumulated_term_count]
    agg: dict[str, list] = {}

    for md_path in sorted(term_dir.rglob("*.md")):
        lines = md_path.read_text(encoding="utf-8", errors="strict").splitlines()
        i = 0
        n = len(lines)
        while i < n:
            m = CODELIST_HEADING_RE.match(lines[i])
            if not m:
                i += 1
                continue
            name, c_code = m.group(1).strip(), m.group(2)
            # Count term rows until next `## ` heading or EOF.
            j = i + 1
            term_count = 0
            while j < n and not lines[j].startswith("## "):
                if TERM_ROW_RE.match(lines[j]):
                    term_count += 1
                j += 1
            if c_code in agg:
                agg[c_code][1] += term_count
            else:
                agg[c_code] = [name, term_count]
            i = j  # resume at next heading or EOF

    return sorted(
        ((c, v[0], v[1]) for c, v in agg.items()),
        key=lambda t: t[0],
    )


def count_domain_refs(c_codes: list[str]) -> dict[str, int]:
    """Count occurrences of each C-code across all domains/*/spec.md.

    Domain specs reference codelists via markdown links like
    `(C66742)](../../terminology/core/general_part4.md)`. Counting raw
    `Cnnnnn` occurrences is the simplest stable signal.
    """
    # Build the full concatenated spec text once; grep all codes against it.
    spec_files = sorted(DOMAINS_DIR.rglob("spec.md"))
    combined = "\n".join(
        p.read_text(encoding="utf-8", errors="strict") for p in spec_files
    )
    out: dict[str, int] = {}
    for c in c_codes:
        pattern = re.compile(rf"\b{re.escape(c)}\b")
        out[c] = len(pattern.findall(combined))
    return out


# --- Scoring ----------------------------------------------------------------


def sigmoid_term(n: int) -> float:
    """Log-distance hat centered at n=30; returns value in (0, 1], or 0 at n=0.

    See module docstring for rationale.
    """
    if n <= 0:
        return 0.0
    return 1.0 / (1.0 + abs(math.log10(n + 1) - math.log10(SIGMOID_CENTER_N)))


def min_max_normalize(values: dict[str, int]) -> dict[str, float]:
    """Min-max normalize {key: int} -> {key: float in [0, 1]}.

    Returns all-zero when max == min (degenerate).
    """
    if not values:
        return {}
    vs = list(values.values())
    lo, hi = min(vs), max(vs)
    if hi == lo:
        return {k: 0.0 for k in values}
    span = hi - lo
    return {k: (v - lo) / span for k, v in values.items()}


def is_t_hit(c_code: str, full_name: str) -> bool:
    """Return True if codelist matches any entry in T_CODELIST_HITS.

    Match is by C-code (the mapping we hardcode at top). Short-name
    strings like NY / FREQ don't appear literally in the .md headings,
    so name-based matching isn't possible; we rely on the curated map.
    """
    hit_c_codes = {v for v in T_CODELIST_HITS.values() if v}
    return c_code in hit_c_codes


def compute_scores(
    codelists: list[tuple[str, str, int]],
    domain_refs: dict[str, int],
) -> dict[str, float]:
    """Apply scoring formula, return {c_code: score}."""
    norm_refs = min_max_normalize(domain_refs)
    scores: dict[str, float] = {}
    for c_code, full_name, term_count in codelists:
        hit_bonus = 0.2 * (50 if is_t_hit(c_code, full_name) else 0)
        scores[c_code] = (
            0.5 * norm_refs.get(c_code, 0.0)
            + 0.3 * sigmoid_term(term_count)
            + hit_bonus
        )
    return scores


# --- Main -------------------------------------------------------------------


def main() -> int:
    if not TERMINOLOGY_DIR.is_dir():
        print(f"error: terminology/ not found at {TERMINOLOGY_DIR}", file=sys.stderr)
        return 2
    if not DOMAINS_DIR.is_dir():
        print(f"error: domains/ not found at {DOMAINS_DIR}", file=sys.stderr)
        return 2

    codelists = parse_codelists(TERMINOLOGY_DIR)
    c_codes = [c for c, _, _ in codelists]
    term_counts = {c: t for c, _, t in codelists}
    names = {c: n for c, n, _ in codelists}

    domain_refs = count_domain_refs(c_codes)
    scores = compute_scores(codelists, domain_refs)

    # Stable sort: score desc, then c_code asc (idempotent tiebreak).
    ranked = sorted(scores.items(), key=lambda kv: (-kv[1], kv[0]))

    # --- Section 1: batch 4 top 200 -----------------------------------------
    print(f"# 批 4 top {TOP_N_BATCH4} (按 score 降序)")
    batch4 = ranked[:TOP_N_BATCH4]
    for c, s in batch4:
        label = f"{c} / {names[c]}"
        print(f"{label}: {s:.3f}")
    print()

    # --- Section 2: batch 5 rank 201-500 ------------------------------------
    print(f"# 批 5 rank {RANK_START_BATCH5}-{RANK_END_BATCH5} (按 score 降序)")
    batch5 = ranked[RANK_START_BATCH5 - 1 : RANK_END_BATCH5]
    for c, s in batch5:
        label = f"{c} / {names[c]}"
        print(f"{label}: {s:.3f}")
    print()

    # --- Section 3: stats ---------------------------------------------------
    total = len(ranked)
    batch4_tokens = sum(term_counts[c] * TOKENS_PER_TERM for c, _ in batch4)
    batch5_tokens = sum(term_counts[c] * TOKENS_PER_TERM for c, _ in batch5)

    print("# 统计")
    print(f"Total codelists: {total}")
    print(
        f"Top {TOP_N_BATCH4} coverage: {len(batch4)} codelists, "
        f"估 {batch4_tokens:,} tokens (term_count * {TOKENS_PER_TERM})"
    )
    print(
        f"Rank {RANK_START_BATCH5}-{RANK_END_BATCH5} coverage: "
        f"{len(batch5)} codelists, 估 {batch5_tokens:,} tokens"
    )

    # T_codelist_hits audit: which known hits landed in top 200?
    hit_c_codes = {v: k for k, v in T_CODELIST_HITS.items() if v}
    print()
    print("# T_codelist_hits 审计")
    rank_of = {c: idx + 1 for idx, (c, _) in enumerate(ranked)}
    for short_name, c_code in T_CODELIST_HITS.items():
        if not c_code:
            print(f"{short_name}: (not mapped / not in knowledge_base)")
            continue
        rank = rank_of.get(c_code)
        if rank is None:
            print(f"{short_name} ({c_code}): NOT FOUND in knowledge_base")
        else:
            print(f"{short_name} ({c_code}): rank {rank}, score {scores[c_code]:.3f}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
