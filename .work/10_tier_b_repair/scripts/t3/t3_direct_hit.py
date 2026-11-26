#!/usr/bin/env python3
"""T3.2 direct-hit recheck, attempt 2 (审计 K2: independent — never reads matched_by.evidence.hit_file).
For every EXACT ledger row (TB rows anywhere, stock rows inside §5.0) the targets are rebuilt from primary sources:
ledger md_atom_ids files, t3_errata remap, triage kb_loc / target, writer-log fix rows (kb_file), section md_target_files,
the atom's own domain spec.md (attempt 3);
index files (VARIABLE_INDEX / INDEX / ROUTING) excluded. A hit must be word-bounded and section-anchored
(t3_common.valid_hits) and, per 审计 K11, a group of n EXACT atoms with the same section + text needs >= n distinct hits.
Anchor checks for terminal non-EXACT rows (so deleting their KB support turns RED too):
  TB EQUIVALENT rule 'T1-two-agent'  -> the T1-judged kb_loc line (302ec4c text) must still exist in the KB file;
  INTENTIONAL_EXCLUDE with a spec.md kb_loc -> the '### VAR' block heading above that kb_loc (302ec4c) must still exist.
Buckets: tb_exact_miss / k11_short / anchor_lost (RED); expected_regression / errata / pre_existing (explained); unexplained (RED).
Usage: python3 -I .work/10_tier_b_repair/scripts/t3/t3_direct_hit.py [--kb-root DIR] [--base-kb-root DIR] [--out JSON]
"""
import argparse, collections, json, os, re, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from t3_common import ROOT, TB, W, INDEX_FILES, lj, norm, valid_hits, atom_order, expand_ref, writer_rows, FIX_ACTIONS

ap = argparse.ArgumentParser()
ap.add_argument("--kb-root", default=f"{ROOT}/knowledge_base")
ap.add_argument("--base-kb-root", default=f"{W}/scratch/t3/kb_t2base/knowledge_base", help="KB at 302ec4c (pre-T2)")
ap.add_argument("--ledger", default=f"{W}/coverage_ledger.wc.jsonl")
ap.add_argument("--out")
a = ap.parse_args()
kb_root, base_root = os.path.abspath(a.kb_root), os.path.abspath(a.base_kb_root)
A = {x["atom_id"]: x for x in lj(f"{W}/pdf_atoms.jsonl")}
T = {t["atom_id"]: t for t in json.load(open(f"{W}/triage_merged.json"))}
scope = {(r["source"], r["section_key"]) for r in lj(f"{TB}/inventory.jsonl")} | {("ig34", "§6.3.5.9.3 Relating PP Records to PC Records")}
md_file = {m["atom_id"]: m.get("file", "") for m in lj(f"{W}/md_atoms.jsonl")}
sec_t = {(r["source"], r["section_key"]): r.get("md_target_files") or [] for r in lj(f"{W}/section_coverage.wc.baseline.jsonl")}
ER = json.load(open(f"{W}/t3_errata.json"))
EXP = {r["atom_id"] for r in lj(f"{W}/t3_fp_expected_regressions.jsonl")}
order, idx = atom_order()
WRF = collections.defaultdict(set)
for b, wf, n, r in writer_rows():
    if r["action"] in FIX_ACTIONS:
        for i in expand_ref(str(r["ref"]), idx, order)[0]:
            WRF[i].add(r["kb_file"])
led = {}
for e in lj(a.ledger):
    led[e["pdf_atom_id"]] = e

def targets(i, e):
    tg = {md_file.get(m, "") for m in e.get("md_atom_ids", [])} - {""}
    if i in ER["target_remap"]:
        tg.add(ER["target_remap"][i]["target"])
    t = T.get(i, {})
    for x in (t.get("kb_loc"), t.get("target")):
        if x and str(x).startswith("knowledge_base/"):
            tg.add(x.split(":")[0])
    tg |= WRF.get(i, set()) | set(sec_t.get((i.split("_")[0], A[i]["parent_section"]), []))
    m = re.search(r"\(([A-Z]{2,8})\)", A[i]["parent_section"]) or re.search(r"knowledge_base/domains/([A-Z]+)/", str(t.get("kb_loc") or ""))
    if m and os.path.exists(f"{ROOT}/knowledge_base/domains/{m.group(1)}/spec.md"):
        tg.add(f"knowledge_base/domains/{m.group(1)}/spec.md")  # attempt 3 / C5: the atom's own domain spec.md
    return sorted(tg - INDEX_FILES)

_base = {}
def base_lines(f):
    if f not in _base:
        _base[f] = subprocess.run(["git", "-C", ROOT, "show", f"302ec4c:{f}"], capture_output=True, text=True).stdout.splitlines()
    return _base[f]
def kb_raw(f):
    p = os.path.join(kb_root, f[len("knowledge_base/"):])
    return open(p, encoding="utf-8").read().splitlines() if os.path.exists(p) else []

B = collections.defaultdict(list)
n_tb = n_stock = n_anchor = 0
hits, groups = {}, collections.defaultdict(list)
for i, e in led.items():
    x = A.get(i)
    if not x:
        continue
    tb = e.get("matched_by", {}).get("phase") == "TB"
    rule = e.get("matched_by", {}).get("rule", "")
    # ---- anchor checks for non-EXACT terminal rows
    if tb and e["verdict"] == "EQUIVALENT" and rule == "T1-two-agent":
        n_anchor += 1
        f, ln = T[i]["kb_loc"].rsplit(":", 1)
        bl = base_lines(f)[int(ln) - 1]
        if bl not in kb_raw(f):
            B["anchor_lost"].append(f"{i} T1 kb_loc line {T[i]['kb_loc']}")
        continue
    if e["verdict"] == "INTENTIONAL_EXCLUDE" and i in T and re.match(r"knowledge_base/\S+/spec\.md:\d+$", T[i].get("kb_loc") or ""):
        n_anchor += 1
        f, ln = T[i]["kb_loc"].rsplit(":", 1)
        bl = base_lines(f)
        head = next((bl[k] for k in range(int(ln) - 1, -1, -1) if bl[k].startswith("### ")), None)
        if head and head not in kb_raw(f):
            B["anchor_lost"].append(f"{i} IE spec block '{head}' ({T[i]['kb_loc']})")
        continue
    if e["verdict"] != "EXACT" or (not tb and (x["atom_type"] == "HEADING" or (i.split("_")[0], x["parent_section"]) not in scope)):
        continue
    v = norm(x["verbatim"])
    tg = targets(i, e)
    found = [(f, ln) for f in tg for ln, _ in valid_hits(f, v, i, x["parent_section"], kb_root)[0]]
    if tb:
        n_tb += 1
        hits[i] = found
        groups[(i.split("_")[0], x["parent_section"], v)].append(i)
        if not found:
            B["tb_exact_miss"].append(i)
        continue
    n_stock += 1
    if found:
        continue
    if i in EXP:
        B["expected_regression"].append(i)
    elif i in ER["atom_err"]:
        B["errata"].append(i)
    elif not any(valid_hits(f, v, i, x["parent_section"], base_root)[0] for f in tg):  # no valid hit pre-T2 either
        B["pre_existing"].append(i)
    else:
        B["unexplained"].append(i)
for k, ids in groups.items():
    occ = {h for i in ids for h in hits[i]}
    if len(ids) > 1 and len(occ) < len(ids) and not any(i in B["tb_exact_miss"] for i in ids):
        B["k11_short"].append(f"{ids} occ={len(occ)}")
print(f"kb_root={kb_root}\nEXACT checked (independent targets): TB(all)={n_tb} stock(§5.0 scope)={n_stock}; anchor-checked non-EXACT rows={n_anchor}")
for k in ("tb_exact_miss", "k11_short", "anchor_lost", "expected_regression", "errata", "pre_existing", "unexplained"):
    print(f"  {k}: {len(B[k])}", B[k][:8])
if a.out:
    json.dump(B, open(a.out, "w"), indent=1, ensure_ascii=False)
rc = 1 if (B["tb_exact_miss"] or B["k11_short"] or B["anchor_lost"] or B["unexplained"]) else 0
print("RESULT:", "RED" if rc else "GREEN")
sys.exit(rc)
