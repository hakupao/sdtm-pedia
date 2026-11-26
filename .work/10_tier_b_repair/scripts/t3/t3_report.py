#!/usr/bin/env python3
"""T3 summary numbers for evidence/checkpoints/t3_recompute.md + reviewer sampling sets (work/t3_audit_sets/).
Reads: work/section_coverage.wc.jsonl (post-T3), work/scratch/t3/section_coverage.pre_t3.jsonl (pre-T3 recompute),
work/t3_writeback_decisions.json. Writes work/t3_audit_sets/<rule>__<new_verdict>.txt (one atom id per line).
Usage: python3 -I .work/10_tier_b_repair/scripts/t3/t3_report.py
"""
import collections, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from t3_common import W, lj, norm

POST = lj(f"{W}/section_coverage.wc.jsonl")
PRE = lj(f"{W}/scratch/t3/section_coverage.pre_t3.jsonl")
D = json.load(open(f"{W}/t3_writeback_decisions.json"))
C = collections.Counter

for lab, S in (("pre-T3", PRE), ("post-T3", POST)):
    sc = [e for e in S if e["tb_in_scope"]]
    print(f"[{lab}] §5.0 sections={len(sc)} residual={sum(e['tb_residual_gap'] for e in sc)} "
          f"G-TB1 pass={sum(e['tb_g1_pass'] for e in sc)} G-TB2 pass={sum(e['tb_g2_pass'] for e in sc)} | "
          f"stock aggregate_verdict (all 399): {dict(C(e['aggregate_verdict'] for e in S))}")

# G-TB1 residual by section / class (post)
print("\nG-TB1 residual atoms (post):")
for e in POST:
    if e["tb_in_scope"] and e["tb_residual_gap"]:
        print(f"  {e['source']} {e['section_key'][:70]} residual={e['tb_residual_gap']} "
              f"{ {k: v for k, v in e['tb_verdict_counts'].items() if v} }")
res = {i: d for i, d in D.items() if d["rule"].startswith("residual") or d["rule"] == "pending_user-residual"}
print("  residual atoms:", {i: (d["old"], (d["evidence"].get("triage") or {}).get("final_class"), d["rule"]) for i, d in res.items()})

# G-TB2 scope-restricted variant: structural section passes iff all IN-SCOPE direct children pass (recursively)
num = lambda k: (re.match(r"^§([0-9.]+)", k) or [None, None])[1]
by = {(e["source"], num(e["section_key"])): e for e in POST if num(e["section_key"])}
kids = lambda e: [v for (s, m), v in by.items() if s == e["source"] and m and num(e["section_key"]) and
                  m.startswith(num(e["section_key"]) + ".") and "." not in m[len(num(e["section_key"])) + 1:]]
memo = {}
def g2s(e):
    k = (e["source"], e["section_key"])
    if k not in memo:
        if e["tb_density_excl_ie"] is not None:
            memo[k] = e["tb_density_excl_ie"] == 1.0
        else:
            memo[k] = all(g2s(c) for c in kids(e) if c["tb_in_scope"])
    return memo[k]
sc = [e for e in POST if e["tb_in_scope"]]
fail_strict = [e for e in sc if not e["tb_g2_pass"]]
fail_scoped = [e for e in sc if not g2s(e)]
print(f"\nG-TB2 [参考列] strict (stock tb_g2_pass, children anywhere): {len(sc) - len(fail_strict)}/{len(sc)}; "
      f"[闸 C4] scope-restricted (structural parents judged on in-scope children only): {len(sc) - len(fail_scoped)}/{len(sc)}")
print("  strict-only failures (structural parents failing solely via out-of-§5.0 children):",
      [f"{e['source']} {e['section_key'][:40]}" for e in fail_strict if e not in fail_scoped])
print("  scoped failures:", [f"{e['source']} {e['section_key'][:50]} dens={e['tb_density_excl_ie']}" for e in fail_scoped])

# write-back flip stats + audit sets
fl = {i: d for i, d in D.items() if d["new"] != d["old"]}
in_scope_ids = {i for i, d in D.items() if d["in_triage"]}
print(f"\nwrite-back: allowed={len(D)} flipped={len(fl)} flip rate={len(fl) / len(D) * 100:.1f}% "
      f"(triage flipped {sum(d['in_triage'] for d in fl.values())}/{len(in_scope_ids)}; t2s-only flipped "
      f"{sum(not d['in_triage'] for d in fl.values())})")
print("  by new verdict:", dict(C(d["new"] for d in fl.values())))
print("  by rule x new:", dict(C((d["rule"], d["new"]) for d in fl.values())))
print("  triage class -> new:", dict(C(((d["evidence"].get("triage") or {}).get("final_class", "T2S-only"), d["new"]) for d in fl.values())))
print("  EXACT with short verbatim (<25 chars, sample these):", sum(d["new"] == "EXACT" and d["short_verbatim"] for d in fl.values()))
ie_hit = [i for i, d in D.items() if d["new"] == "INTENTIONAL_EXCLUDE" and d["evidence"].get("hit_file")]
print("  triage IE whose verbatim now hits KB (kept IE, T4 note):", len(ie_hit))
r4b = [i for i, d in D.items() if (d["evidence"].get("triage") or {}).get("src") == "ruling:R4-blocked"]
print("  R4-blocked IE (kept IE; t1_ie_final says 待用户):", r4b)
od = os.path.join(W, "t3_audit_sets")
os.makedirs(od, exist_ok=True)
groups = collections.defaultdict(list)
for i, d in fl.items():
    groups[f"{d['rule']}__{d['new']}"].append(i)
groups["IE_now_hits_KB"] = ie_hit
groups["EXACT_short_verbatim"] = [i for i, d in fl.items() if d["new"] == "EXACT" and d["short_verbatim"]]
groups["residual"] = sorted(res)
for g, ids in groups.items():
    open(f"{od}/{g}.txt", "w").write("\n".join(sorted(ids)) + "\n")
print("  audit sets:", {g: len(v) for g, v in sorted(groups.items())})
