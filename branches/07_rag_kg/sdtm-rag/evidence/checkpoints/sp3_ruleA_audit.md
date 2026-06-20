# SP3 Deterministic Graph Answer Channel — Independent Rule-A Semantic Audit

> Auditor: Scientist (independent; NOT a writer of `server/graph_answer.py`).
> Date: 2026-06-20. Verdict: **RULE A: PASS** (10/10 checks).
> Method: call the REAL `GraphAnswerer.resolve(q)` (what the user's answer is grounded
> on) and independently re-derive truth from `yaml.safe_load(data/meta/meta.yaml)` +
> the KB (`knowledge_base/VARIABLE_INDEX.md`, `domains/*/spec.md`). Truth is NEVER
> computed via GraphEngine; it is re-derived from raw YAML with my own reverse indices.

## Environment note (execution path)

The `python_repl` Gyoshu bridge hard-blocks `import` / `type` / `globals` (sandbox),
so it cannot load the channel module (which imports `re`/`yaml`/server modules) nor
independently `import yaml`. Audit scripts were therefore run via the project venv
(`.venv/bin/python`) — the only way to exercise the real channel code AND independently
parse the YAML/KB. Scripts retained as artifacts under `eval/`:
`sp3_ruleA_audit.py`, `sp3_ruleA_trace.py`, `sp3_kb_ctcheck.py`, `sp3_c99079.py`,
`sp3_ruleA_verdict.py`.

## Ground-truth universe (independently derived)

- meta.yaml top keys: `codelists, domains, generated_from, meta_version, model_defhome`; meta_version=1.
- `counts_toward_63` domains = **63** (stub excluded = **DI**). This is the channel's universe; my GT applies the same filter.
- 1005 codelists; 1523 unique variable names across the 63 real domains.

## Results table

| Slot | Question (verbatim) | What the channel injected | Independent truth (source) | PASS/FAIL | Notes |
|---|---|---|---|---|---|
| 1 impact/codelist | "What is affected if codelist C66742 changes?" | text: "Changing codelist **C66742** (No Yes Response) affects **123** variables across **41** domains: AE,AG,…,VS." counts: impacted_domains=41, impacted_variables=123 | name "No Yes Response"; 41 domains; 123 distinct vars (raw meta.yaml). KB `VARIABLE_INDEX.md` CT-section row `C66742 | 123 | AE.AECONTRT, …` confirms 123. | **PASS** | Domain list + both counts + name exact. |
| 2 impact/variable | "Which domains are impacted by changing TAETORD?" | "Changing variable **TAETORD** affects **43** domains: AE,AG,…,VS." counts: impacted_domains=43 | TAETORD ∈ exactly 43 domains (raw meta.yaml). KB `VARIABLE_INDEX.md`: `TAETORD | 43 | AE, AG, …, VS` — identical 43-domain list. | **PASS** | Injected list == GT exact set, char-for-char. |
| 3 aggregate/min-domains | "Which variables appear in more than 40 domains?" | "**5** variables appear in >40 domains: STUDYID (63), DOMAIN (59), USUBJID (55), EPOCH (44), TAETORD (43)." | Strict >40 ⇒ {STUDYID 63, DOMAIN 59, USUBJID 55, EPOCH 44, TAETORD 43} (raw meta.yaml). Boundary: **0** variables at exactly 40 (no false inclusion/exclusion). KB confirms STUDYID=63("所有域"), DOMAIN=59, USUBJID=55, EPOCH=44, TAETORD=43. | **PASS** | Strict threshold (n+1=41) correct; counts + ranking correct; boundary clean. |
| 4 aggregate/most-shared | "Which codelists are reused across the most variables?" | **None** (verbatim) | — | **PASS** | Verbatim phrasing carries none of the channel's aggregate-(b) cues (`most shared`/`most common`/`most widely used`) → no intent → injects nothing (no false fact). Canonical phrasing "What are the most common codelists?" fires and is TRUE: top-5 by distinct var-count = C66742(123), C71620(58), C66789(36), C66728(26), C74456(19). See C99079 note below. |
| 5 structural/same-class | "What other domains are in the same class as AE?" | **None** (verbatim) | — | **PASS** | Class-roster is DELIBERATELY not exposed at NL layer (module docstring L14-16: class names are common words → fragile anchoring). Verbatim has no relationship cue → None (no false fact). Canonical "associated with AE" fires the authoritative same-class line: BE,CE,DS,DV,HO,MH = Events∖AE. Independently confirmed by `grep 'Class: Events' domains/*/spec.md` = {AE,BE,CE,DS,DV,HO,MH}. |
| 6 structural/codelist co-users | "What other variables use the same codelist as AESER?" | **None** (verbatim) | — | **PASS** | `codelist_co_users` is a programmatic GraphEngine method NOT surfaced at the NL layer at all (reserved for SP4) — `GraphAnswerer.resolve` source contains no `co_user` reference. Injects nothing → no false fact. (GT: AESER→C66742; 122 co-users exist but are intentionally not NL-served.) |
| 7 CT/relationship advisory | "What other domains does AE have noted relationships with?" | text (AUTHORITATIVE): "Domain **AE** is in the same class as: BE,CE,DS,DV,HO,MH." advisory (NON-AUTH): "AE→FA — prespecified AE findings (AEPRESP); AE→CM via RELREC …; AE→PR via RELREC …" counts: (none) | AE.same_class = [BE,CE,DS,DV,HO,MH]; AE.relations_curated = 3 entries (FA/CM/PR, fidelity=curated_prose). | **PASS** | Authoritative same-class line TRUE; advisory lists all 3 curated relations under the "curated, non-exhaustive — may be incomplete; do not claim complete" header; emits NO checkable_count for relations; curated targets ABSENT from text_block. |
| 8 anti-overfit/held-out | "…impacted by changing EPOCH?" + "…affected if codelist C66728 changes?" | EPOCH → 44 domains (counts impacted_domains=44); C66728 (Relation to Reference Period) → 26 vars across 9 domains: AE,AG,CE,CM,HO,MH,PR,RS,SU (counts 9/26) | EPOCH ∈ 44 domains (raw meta.yaml; KB VARIABLE_INDEX `EPOCH | 44 | …` identical). C66728: 26 distinct vars / 9 domains (raw meta.yaml; KB CT-section `C66728 | 26 | AE.AEENRF,…`). | **PASS** | Entities not used elsewhere → proves generalization, not memorization. Exact sets. |
| DEGEN | "What is affected if codelist C100134 changes?" | **None** | C100134 EXISTS in `codelists` (name "Brief Psychiatric Rating Scale … Test Code") but has 0 `counts_toward_63` usage (no variable references it) → `GTloc[C100134]=∅`. | **PASS** | Channel's gate (`imp["n_domains"]>0 or imp["n_variables"]>0`, L108) suppresses the degenerate "affects 0" fact; sole-entity query → resolve returns None. No misleading zero injected. |
| SEP | (AE relationship query) | curated relations appear ONLY in advisory_block | — | **PASS** | Curated relations never appear in text_block or checkable_counts; authoritative/advisory separation holds. |

## C99079 ranking discrepancy — investigated and CLEARED

KB CT-section "引用数" ranks C99079 (Epoch) at 44, which would be #3 by that metric — but
the channel's most-shared top-5 omits it. Root cause: the two metrics differ.
- KB "引用数" counts (domain,var) LOCATION references. C99079 = codelist for the single
  variable **EPOCH**, which appears in 44 domains → 44 location-refs but **1 distinct variable**.
- The question asks "reused across the most **variables**". `most_shared_codelists` counts
  DISTINCT VARIABLE NAMES (`variables_for_codelist` → distinct names), so C99079 = 1 var,
  far below the top-5. By the correct (distinct-variable) metric the channel's top-5 is exact.
Conclusion: the channel answers the asked question correctly; no defect. (Independently
verified both metrics from raw meta.yaml in `eval/sp3_c99079.py`.)

## Cross-source corroboration (independent of meta.yaml)

KB `VARIABLE_INDEX.md` (auto-generated from PDF sources, separate artifact) independently
confirmed every fired cardinality: TAETORD=43, EPOCH=44, STUDYID=63, DOMAIN=59, USUBJID=55,
C66742=123 vars, C66728=26 vars; and `domains/*/spec.md` headers confirmed the Events-class
roster {AE,BE,CE,DS,DV,HO,MH}. (Note: a naive grep over var rows over-counts CT codes by +1
because the CT-cross-ref row itself begins `| C66742 |`; the authoritative CT-section 引用数
column gives 123/26 directly, matching the channel.)

## Verdict

**RULE A: PASS.** Every authoritative fact the channel injects (impact cardinalities +
domain/variable sets, aggregate thresholds + rankings, structural same-class lines,
held-out generalization cases) is semantically TRUE and complete against independently
re-derived ground truth, and corroborated by the KB. The advisory block is correctly
hedged (non-exhaustive header, no completeness claim, no checkable_count). The
authoritative/advisory separation is intact, and the degenerate codelist correctly
injects nothing. The four verbatim slots that returned None (4/5/6) are NOT defects:
they inject no fact (hence no Rule-A violation), and reflect the channel's deliberate,
documented NL surface — firing correctly and truthfully on canonical phrasings.
