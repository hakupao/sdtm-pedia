#!/usr/bin/env python3
"""Add-on check the owner chose on 2026-11-27 ("加查"): final ATOM_ERR atoms of rule S1-R1 that no independent
reviewer has judged one by one. Full check, no sampling.

Population (exact, not the gate's estimate of ~83):
  S1R1   = ledger rows with verdict ATOM_ERR and matched_by.rule == "S1-R1"
  JUDGED = S1R1 atoms that have their own verdict row in the raw output of a T4 independent review
           (files in RAW below; a table row whose 2nd cell is the atom id)
  NEW    = S1R1 - JUDGED                      -> checked here for the first time
  RECHK  = JUDGED atoms not judged by the supp full check (gate sample / T4.2 prescreen)
           -> checked again, blind (same layer name, interleaved by page), as a consistency control
  The gate's "~83" = |S1R1| - |supp TRIAGE_ATOM_ERR layer|; NEW + RECHK is exactly that set.
Not counted as "judged" (disclosed, atoms stay in NEW): the T2 batch reviewer / auditor line a ledger `basis` points at
(that line is the origin of the label, i.e. the claim under test) and one-line ticks of the T3 auditor
(evidence/step_T3_audit.md).
Same builders / renderer as the gate packs (definition parts exec-ed; t4_sample.py / t4_render.py never re-run).
Writes only under work/t4/atomerr/. Usage (repo root): python3 -I .work/10_tier_b_repair/scripts/t4/t4_atomerr_sample.py
"""
import collections, glob, hashlib, json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
TB = os.path.dirname(os.path.dirname(HERE))
OUT = f"{TB}/work/t4/atomerr"
LEDGER_MD5 = "438098704becc84eda01a925b80defaa"
LAYER, PACK = "ae:S1R1_ATOM_ERR", 21
RAW = ["evidence/t4_gate_raw/pack[1-4].md", "evidence/t4_supp_raw/pack_*.md", "evidence/t4_q9_raw/pack_*.md",
       "evidence/t4_round2_raw/pack_*.md", "evidence/t4_round3_raw/pack_*.md", "evidence/t4_gate_raw/attempt3_report.md",
       "evidence/t4_gate_raw/attempt3_delta_report.md", "evidence/checkpoints/t4_human_prescreen.md",
       "evidence/checkpoints/t4_human_prescreen_postthaw.md", "evidence/checkpoints/t4_human_verdicts.md",
       "evidence/checkpoints/t4_u5_c7_fullcheck.md", "evidence/checkpoints/t4_u7_rowcheck.md",
       "evidence/checkpoints/t4_round2_ledger_audit.md"]
VERDICTS = ("HOLDS_AS_EQUIV", "NOT_HOLD", "HOLDS", "UNVERIFIABLE", "内容正确", "内容错误", "看不出")
os.makedirs(OUT, exist_ok=True)
md5 = lambda p: hashlib.md5(open(p, "rb").read()).hexdigest()
assert md5(f"{TB}/work/coverage_ledger.wc.jsonl") == LEDGER_MD5, "ledger changed: re-derive the population on purpose"


def defs_only(path, marker):
    src = open(path, encoding="utf-8").read()
    assert src.count(marker) == 1, (path, marker)
    return src.split(marker)[0]


S = {"__file__": f"{HERE}/t4_sample.py", "__name__": "t4_sample_defs"}
exec(compile(defs_only(f"{HERE}/t4_sample.py", "\ncls = lambda c:"), f"{HERE}/t4_sample.py", "exec"), S)
R = {"__name__": "t4_render_defs"}
exec(compile(defs_only(f"{HERE}/t4_render.py", '\ngate = lj(f"{TB}/work/t4/gate_sample.jsonl")'), f"{HERE}/t4_render.py", "exec"), R)
L = S["L"]

key = lambda i: (i[:4], int(i.split("_p")[1].split("_a")[0]), int(i.split("_a")[1]))
s1r1 = sorted((i for i, r in L.items() if r["verdict"] == "ATOM_ERR" and r["matched_by"].get("rule") == "S1-R1"), key=key)
all_ae = [i for i, r in L.items() if r["verdict"] == "ATOM_ERR"]

judged = collections.defaultdict(list)  # atom -> [(file, line, verdict)]
for pat in RAW:
    files = sorted(glob.glob(f"{TB}/{pat}"))
    assert files, pat
    for f in files:
        for n, line in enumerate(open(f, encoding="utf-8"), 1):
            cells = [c.strip().strip("`") for c in line.split("|")]
            if len(cells) < 5 or cells[2] not in L:
                continue
            v = next((v for c in cells[3:7] for v in VERDICTS if c.replace("*", "") == v), None)
            if v and L[cells[2]]["verdict"] == "ATOM_ERR" and L[cells[2]]["matched_by"].get("rule") == "S1-R1":
                judged[cells[2]].append((os.path.relpath(f, TB), n, v))

src = lambda i: sorted({f.split("/")[1] if f.startswith("evidence/t4_") else f.split("/")[-1] for f, _, _ in judged[i]})
by_src = collections.Counter(tuple(src(i)) for i in judged)
supp = {i for i in judged if "t4_supp_raw" in src(i)}
rechk = sorted(set(judged) - supp, key=key)
new = [i for i in s1r1 if i not in judged]
assert not (set(judged) - set(s1r1)) and len(set(new) | set(judged)) == len(s1r1)
bad_prior = {i: v for i, v in judged.items() if any(x[2] not in ("HOLDS", "内容正确") for x in v)}

t3 = open(f"{TB}/evidence/step_T3_audit.md", encoding="utf-8").read().splitlines()
t3_cells = [[c.strip().strip("`") for c in l.split("|")] for l in t3 if l.startswith("|") and "✓" in l]
t3_tick = sorted({c[2] for c in t3_cells if len(c) > 3 and c[2] in set(new)}, key=key)
chk = lambda i: (L[i]["matched_by"]["evidence"].get("checkpoint") or "").split(":")[0].split("/")[-1]
basis_src = collections.Counter(chk(i) for i in new)

checked = sorted(new + rechk, key=key)
rows = [S["refine_human"](S["row"](i, LAYER)) for i in checked]
with open(f"{OUT}/atomerr_sample.jsonl", "w", encoding="utf-8") as fh:
    for x in rows:
        fh.write(json.dumps(x, ensure_ascii=False) + "\n")
pop = dict(ledger_md5=LEDGER_MD5, atom_err_total=len(all_ae), s1r1=len(s1r1),
           judged_before=len(judged), judged_by_source={" + ".join(k): v for k, v in sorted(by_src.items())},
           judged_before_not_holds=bad_prior, new=new, recheck=rechk,
           recheck_prior={i: [dict(file=f, line=n, verdict=v) for f, n, v in judged[i]] for i in rechk},
           new_with_t3_auditor_tick=t3_tick, new_basis_checkpoint_file=dict(sorted(basis_src.items())),
           new_by_atom_type=dict(collections.Counter(x["atom_type"] for x in rows if x["atom_id"] in set(new))),
           new_by_prev_verdict=dict(collections.Counter(L[i]["matched_by"].get("prev_verdict") for i in new)),
           checked=checked)
json.dump(pop, open(f"{OUT}/atomerr_population.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)

n = k = 0
for lo in range(0, len(rows), PACK):
    k += 1
    part = rows[lo:lo + PACK]
    out = [f"# T4 加查包 {k} — ATOM_ERR (S1-R1) ({len(part)} 条, 全检; 编号 E{n + 1}-E{n + len(part)})", "",
           "> 由 `scripts/t4/t4_atomerr_sample.py` 生成 (KB = HEAD 内容). 只读材料. 编号全局连续 (前缀 E).", ""]
    for x in part:
        n += 1
        out += R["block"](x, f"E{n}")
    open(f"{OUT}/atomerr_pack_{k}.md", "w", encoding="utf-8").write("\n".join(out) + "\n")
assert n == len(rows) == len(new) + len(rechk)

print(f"ATOM_ERR {len(all_ae)}; S1-R1 {len(s1r1)}")
print(f"judged one by one before: {len(judged)}  {dict(pop['judged_by_source'])}; prior verdict not HOLDS: {len(bad_prior)}")
print(f"NEW (never judged one by one) {len(new)}; RECHECK (gate / prescreen, blind) {len(rechk)}; checked here {len(rows)}; packs {k}")
print(f"reconcile: {len(s1r1)} = supp {len(supp)} + gate/prescreen {len(rechk)} + new {len(new)}; gate estimate = {len(s1r1)} - {len(supp)} = {len(s1r1) - len(supp)}")
print(f"NEW with a one-line tick of the T3 auditor (kept in NEW): {len(t3_tick)} {t3_tick}")
print(f"NEW by atom type {pop['new_by_atom_type']}; by pre-T3 verdict {pop['new_by_prev_verdict']}")
print(f"atomerr_sample.jsonl md5 {md5(f'{OUT}/atomerr_sample.jsonl')}; atomerr_population.json md5 {md5(f'{OUT}/atomerr_population.json')}")
for x in rows:
    if x["pdf"]["score"] < 0.8 or x["kb"]["src"] == "none":
        print("weak:", x["atom_id"], "pdf", x["pdf"]["score"], "kb", x["kb"]["src"])
