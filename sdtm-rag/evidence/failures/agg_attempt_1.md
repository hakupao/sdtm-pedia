# AGG attempt 1 — held-out fire-rate gate FAILED (archived per Rule B, do not delete)

Context: Task 6 fire-rate gate. Gate = AGG fired >= 13/16 (81%) on the blind
held-out set `eval/test_set_agg_heldout.yml` (16 questions, gold independently
verified in Tasks 1-5). Probe: `eval/prod_wirein/agg_fire_probe.py`.

## Result (technical)

AGG fired **4/16** (25%) — well below the 13/16 gate.

| category               | n | SP2 fired | AGG fired | SP3 fired |
|------------------------|---|-----------|-----------|-----------|
| aggregate_threshold    | 8 | 3/8       | 3/8       | 0/8       |
| aggregate_superlative  | 8 | 1/8       | 1/8       | 0/8       |
| **ALL**                | 16| 4/16      | **4/16**  | 0/16      |

Fired: ah05, ah06, ah07 (threshold), as05 (superlative).
Silent (12): ah01, ah02, ah03, ah04, ah08, as01, as02, as03, as04, as06, as07, as08.

Reference regression (kgval, Step 3, not a gate): AGG fired **10/10** on the
`aggregate` family of `test_set_kg_value.yml` — exceeds the ≥8/10 expectation
noted in the brief and far above the legacy SP3 cue set's 2/10. The channel
works fine on the phrasings it was tuned against; the held-out set exposes a
narrower recognized surface than assumed.

## Business judgment

REJECT as passing. This is exactly the held-out-generalization failure mode
the gate exists to catch: `detect_aggregate_intents()` in
`server/aggregate_answer.py` recognizes a narrower set of English shapes than
natural blind phrasing produces. Per plan, no per-question pattern patch is
authorized from this seat — that would be fitting the regex to the 16 specific
sentences rather than fixing the shape class, and the held-out set is burned
(cannot be reused as the gate once its wording has been inspected to fix code).

## Per-silent-question shape analysis

Verified directly against the compiled regexes (`_THRESH_STRICT_RE`,
`_THRESH_INCL_PRE_RE`, `_THRESH_INCL_POST_RE`, `_SUPERLATIVE_RE`) — every
silent question below matches **zero** of the four regexes; none are borderline.

### Threshold family (`aggregate_threshold`, 5/8 silent)

| id | question | shape gap |
|----|----------|-----------|
| ah01 | "...show up in **two or more** different domains?" | spelled-out number word ("two"); `_THRESH_INCL_POST_RE` requires a digit (`\d{1,3}`), not a number word |
| ah02 | "...as many as **six** separate domains, **or even more**" | spelled-out number word ("six") *and* an inserted word ("even") breaks the required digit-adjacent-to-"or more" match |
| ah03 | "...turn up in **nine or more** different SDTM domains" | spelled-out number word ("nine") |
| ah04 | "...shared across **a dozen or more** SDTM domains" | non-numeric quantity word ("a dozen") — no digit at all |
| ah08 | "...span **38 domains or more**" | digit present (38) but the noun "domains" sits between the number and "or more"; `_THRESH_INCL_POST_RE` requires the digit directly adjacent to "or more" (only optional whitespace, no intervening word) |

Common theme: the shipped regex family only recognizes **digit-adjacent**
threshold phrasing ("at least 18", "25 or more", "a minimum of 30"). Any of
(a) spelled-out number words, or (b) a noun/modifier inserted between the
number and its bound-word ("N domains or more" vs "N or more"), falls outside
the recognized shape. The 3/8 threshold questions that *did* fire — ah05 ("at
least 18"), ah06 ("25 or more domains" — "or more" directly adjacent to the
digit), ah07 ("a minimum of 30") — all use digit-adjacent phrasing, confirming
the pattern.

### Superlative family (`aggregate_superlative`, 7/8 silent)

All 7 silent questions correctly pass the codelist-context cue gate (the
word "codelist" or "controlled terminology" is present in every one) — the
gap is entirely in `_SUPERLATIVE_RE`, not the cue co-occurrence check.

| id | question | shape gap |
|----|----------|-----------|
| as01 | "...**attached to more variables than any other**?" | comparative "more X than any other" construction — no "most X" or "largest/highest/greatest/biggest number of" token present at all |
| as02 | "...reused across the **widest range of** SDTM domains?" | "widest range of" is a superlative not in the (largest\|highest\|greatest\|biggest) + "number of" list |
| as03 | "...gets shared between variables **the most**?" | postposed "the most" (verb ... the most) instead of the recognized preposed "most + verb" order |
| as04 | "...codelists that **the most variables** draw on?" | "most" quantifies "variables" (the object), not the shared/used/reused verb — inverted semantic framing ("most variables per codelist" vs "most shared codelist") |
| as06 | "...codelists that get reused **by the most variables**?" | same inversion as as04 — "most" attaches to "variables", not to "reused" |
| as07 | "...tied to **more variables than any other**?" | same comparative-than-any-other construction as as01 |
| as08 | "...single **most-used** codelist..." | hyphenated compound "most-used"; `_SUPERLATIVE_RE` requires whitespace (`\s+`) between "most" and "used" — the hyphen breaks the match |

Common theme: the shipped regex only recognizes **preposed "most + verb"**
("most shared", "most used") or **"largest/highest/greatest/biggest number
of"**. Three distinct alternative shapes are missing: (1) comparative
"more/greater X than any other" (as01, as07), (2) postposed or
inverted-subject "most" (as03, as04, as06), (3) alternative superlative
adjectives not in the (largest|highest|greatest|biggest) list, e.g. "widest
range of" (as02), and (4) hyphenated "most-X" compounds (as08).

## Next-attempt input (for whoever owns the remedy)

Per plan, only shape-class-level pattern fixes are authorized, and a fresh
blind held-out set must be authored afterward (this set is burned — its
exact wording is now visible in this file). Candidate shape classes to add,
purely as observations from this failure (not a prescribed fix):
- number-word → digit normalization (or a small closed number-word regex)
  for the threshold family, and relaxing the strict digit-adjacency
  requirement in `_THRESH_INCL_POST_RE` to tolerate an intervening noun.
- broadening `_SUPERLATIVE_RE` to cover comparative ("more/greater ... than
  any other"), postposed/inverted "most", additional superlative adjectives,
  and hyphenated "most-X" compounds.

This is a controller-level decision, not made here.
