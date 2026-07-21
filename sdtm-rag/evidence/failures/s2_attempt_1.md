# S2 attempt 1 — failed levers (archived per Rule B, do not delete)

Context: pushing v2 (102q, retrieval-only) cross 76% + concept 92% → ≥95%.
Final shipped config = `--structured-lookup --hybrid` (RRF, pool=30). This file
records the levers that were tried and rejected, with the data that rejected them.

## Failure 1 — BM25 hybrid pool depth >30 (deeper pool to rescue q73)

- Input: `--structured-lookup --hybrid --hybrid-pool {50,75,100}` on v2.
- Hypothesis: q73 gold `model/06_relationship_datasets.md` sits at BM25 rank ~18 /
  dense rank ~81; a deeper fusion pool would let its several page chunks
  accumulate enough RRF mass to reach top-15.
- Result (technical):
  - pool=30 → misses {q73}            (concept 100%, cross 96%) ← BEST
  - pool=50 → misses {q38, q73}       (concept 94%) — q38 broke
  - pool=75 → misses {q38, q73}       (concept 94%) — q38 broke
  - pool=100 → misses {q08, q38}      (concept 96%) — q73 fixed but q08 + q38 broke
- Business judgment: REJECT. Deepening the pool re-floats BM25 tail noise that
  displaces already-found golds (q08 DM/spec, q38 ch02). Every depth >30 traded
  ≥1 regression for at most one marginal gain (q73). Not robust → kept pool=30.
- Next-attempt input: q73 is NOT a pool problem. Its gold is a *model page*
  reached by neither dense nor BM25 well; the clean fix is a deterministic S1-style
  route (RDOMAIN / relationship-dataset query → model/06), deferred to S4.

## Failure 2 — weighted (min-max normalized) fusion instead of RRF

- Input: `--structured-lookup --hybrid --hybrid-fusion weighted --hybrid-alpha {0.5,0.6,0.7}`.
- Hypothesis: a dense-leaning weighted blend might beat parameter-free RRF.
- Result (technical): identical across all three alphas —
  concept 96%, cross 96%, mixed 100%, single 100%; misses {q39, q73}. Overall 98.0%.
  RRF: concept 100%, cross 96%; misses {q73}. Overall 99.0%.
- Business judgment: REJECT weighted. RRF strictly dominates (rescues q39 that
  weighted loses) AND is parameter-free (zero overfit risk). Min-max
  normalization flattens q39's BM25 signal; rank-based RRF preserves it. alpha is
  not even a useful lever here (flat 0.5→0.7). Shipped RRF.

## Net outcome (config that shipped)
`--structured-lookup --hybrid` (RRF, pool=30): single 100% / mixed 100% /
cross 96% / concept 100%; overall 99.0%. Sole remaining miss: q73 (→ S4).
