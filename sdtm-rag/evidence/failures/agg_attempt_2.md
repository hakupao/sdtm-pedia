# AGG attempt 2 — fresh blind held-out (r2) fire-rate gate FAILED (archived per Rule B, do not delete)

Context: after the round 1-3 shape-class fixes (commits 0866b66 / d37d86e / 2468c4f),
a FRESH blind held-out set was authored (r1 set burned, moved to
`eval/test_set_agg_heldout_burned_r1.yml`; new r2 set now at
`eval/test_set_agg_heldout.yml`, 16 questions). Gate = AGG fired >= 13/16.
Probe: `eval/prod_wirein/agg_fire_probe.py`.

## Result (technical)

AGG fired **12/16** (75%) — below the 13/16 gate.

| category               | n | SP2 fired | AGG fired | SP3 fired |
|------------------------|---|-----------|-----------|-----------|
| aggregate_threshold    | 8 | 4/8       | 7/8       | 0/8       |
| aggregate_superlative  | 8 | 1/8       | 5/8       | 0/8       |
| **ALL**                | 16| 5/16      | **12/16** | 0/16      |

Fired: ah01-ah06, ah08 (threshold), as01, as02, as03, as06, as07 (superlative).
Silent (4): ah07, as04, as05, as08.

Full per-question fire record: `eval/prod_wirein/agg_fire_test_set_agg_heldout.json`
(r2 wordings in `eval/test_set_agg_heldout.yml`).

## Business judgment

REJECT as passing (12 < 13). The round 1-3 shape classes generalized well
(4/16 -> 12/16 on a fully fresh blind set), but two further legitimate English
shape classes exist that the patterns do not cover, plus one metaphoric shape
that is out of regex reach. Remedy authorized at shape-class level only
(round 4); this r2 set is now burned in turn — its wordings are visible below,
so a future gate needs a fresh blind set again.

## Per-silent-question shape analysis

| id | question | shape gap |
|----|----------|-----------|
| ah07 | "I'm looking for variables that are used in **30-plus** domains — which ones are those?" | numeric "plus"-word postfix: digit + hyphen/space + the word "plus" ("30-plus", "30 plus"). The postfix family only knows the symbol `+` ("30+") and the word-bound phrases ("or more" / "or greater" / "and above") — the word "plus" is not in the alternation. |
| as04 | "Could you **rank** the codelists by how many variables reference each one and **give me the top few**?" | top-N ranking-request shape: "the top few" (quantifier after "top"). No superlative token at all — the request is framed as a ranking with a cutoff, not as "most X". |
| as05 | "What are **the top three codelists** in terms of how many variables reference them?" | same top-N ranking shape, with a spelled-out N ("top three"). `_normalize_numbers` already yields "top 3", but no pattern consumes "top + quantifier". |
| as08 | "Out of all the codelists, which one is **the clear champion** when it comes to variable usage?" | metaphoric superlative ("the clear champion", cf. r1's "real workhorse" — which only fired because it ALSO contained "more variables than any other"; this one has no literal quantity/superlative token anywhere). NOT fixable at pattern level without a metaphor lexicon — deliberately NOT patched. |

## Known-limit classes (documented, no pattern fix)

Alongside r1's ah02 ("as many as six separate domains, or even more" — adverb
inserted inside the bound phrase), as08 establishes a second permanent
known-limit class:

- **KL-1 (r1 ah02)**: bound-phrase-internal adverb insertion ("or even more").
- **KL-2 (r2 as08)**: metaphoric superlative with zero quantity token ("the
  clear champion", "the undisputed king", ...). A regex fix would require an
  open-ended metaphor lexicon — per-idiom patching, exactly the overfitting
  the gate exists to prevent. Accepted silent; the LLM answer path still
  handles these questions without injected facts.

## Next-attempt input (for round 4)

Two shape classes authorized (pattern-level, zero q-id/wording hardcoding):

1. **Shape class 7 — numeric "plus" postfix**: `(\d{1,3})[\s-]*plus\b`
   (inclusive, n from the digit), keeping the version-number guard `(?<!\.)`
   ("SDTM 3.2-plus" must not fire).
2. **Shape class 8 — top-N ranking request**: `\btop\s+(?:\d{1,3}|few|several|couple)\b`
   on the number-normalized text ("top three" -> "top 3"), gated by the
   existing codelist-cue co-occurrence check.

Expected post-fix fire on this (now burned) r2 set: 15/16, silent only as08 (KL-2).
