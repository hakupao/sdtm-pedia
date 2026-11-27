#!/usr/bin/env python3
"""Parse the reviewers' raw results of the ATOM_ERR (S1-R1) add-on check and tally them. Read-only on evidence/;
writes work/t4/atomerr/verdicts.json. No verdict is changed here: the script only reads the 判定 cell of each row.
Asserts: every checked atom has exactly one row, in the pack it was dispatched in, with the number it had in the pack.
Usage (repo root): python3 -I .work/10_tier_b_repair/scripts/t4/t4_atomerr_report.py
"""
import collections, glob, hashlib, json, os, re

TB = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = f"{TB}/work/t4/atomerr"
VERDICTS = ("HOLDS", "NOT_HOLD", "UNVERIFIABLE")
pop = json.load(open(f"{OUT}/atomerr_population.json", encoding="utf-8"))
checked, new, rechk = pop["checked"], set(pop["new"]), set(pop["recheck"])
num = {i: f"E{n}" for n, i in enumerate(checked, 1)}
pack_of = {i: (n - 1) // 21 + 1 for n, i in enumerate(checked, 1)}
# the ledger the check was done on (md5 43809870…); after the R4L batch the working ledger has the NOT_HOLD atom as EXACT
ledger = {json.loads(l)["pdf_atom_id"]: json.loads(l) for l in open(f"{TB}/work/coverage_ledger.wc.pre_r4l.jsonl", encoding="utf-8")}

got = {}
for f in sorted(glob.glob(f"{TB}/evidence/t4_atomerr_raw/pack_*.md")):
    k = int(re.search(r"pack_(\d+)\.md$", f).group(1))
    for n, line in enumerate(open(f, encoding="utf-8"), 1):
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.split("|")]
        if len(cells) < 7 or not re.fullmatch(r"E\d+", cells[1].strip("`*")):
            continue
        e, i, v = cells[1].strip("`*"), cells[2].strip("`*"), cells[3].strip("`*")
        assert i in num and num[i] == e, (f, n, e, i)
        assert pack_of[i] == k, (f, n, i, "row in the wrong pack file")
        assert v in VERDICTS, (f, n, i, v)
        assert i not in got, (f, n, i, "duplicate row")
        got[i] = dict(n=e, verdict=v, file=os.path.relpath(f, TB), line=n, stratum="new" if i in new else "recheck",
                      registry_note=bool(re.search(r"涉登记", line)), half1=cells[4], half2=cells[5], note=cells[6])
missing = [i for i in checked if i not in got]
assert not missing, ("no row for", missing)
assert len(got) == len(checked) == len(new) + len(rechk)
for i in got:
    assert ledger[i]["verdict"] == "ATOM_ERR" and ledger[i]["matched_by"].get("rule") == "S1-R1"

json.dump(got, open(f"{OUT}/verdicts.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)
tally = lambda s: dict(collections.Counter(g["verdict"] for g in got.values() if g["stratum"] == s))
print(f"rows {len(got)} (= checked {len(checked)}); by pack {dict(sorted(collections.Counter(pack_of[i] for i in got).items()))}")
print(f"NEW     {len(new):3d}: {tally('new')}")
print(f"RECHECK {len(rechk):3d}: {tally('recheck')}  (prior verdicts: all HOLDS / 内容正确)")
print(f"ALL     {len(got):3d}: {dict(collections.Counter(g['verdict'] for g in got.values()))}")
for v in ("NOT_HOLD", "UNVERIFIABLE"):
    for i, g in got.items():
        if g["verdict"] == v:
            print(f"  {v} {g['n']} {i} [{g['stratum']}] {g['file']}:{g['line']}")
reg = [f"{g['n']} {i}" for i, g in got.items() if g["registry_note"]]
print(f"rows mentioning 涉登记: {len(reg)} {reg}")
print("verdicts.json md5", hashlib.md5(open(f"{OUT}/verdicts.json", "rb").read()).hexdigest())

# Second look (fixed in the brief before dispatch): every non-HOLDS atom goes to a reviewer of another type, blind —
# its block is copied verbatim from the pack together with the two blocks before and after it, with no verdicts.
bad = [i for i in checked if got[i]["verdict"] != "HOLDS"]
if bad:
    idx = sorted({j for i in bad for j in range(max(0, checked.index(i) - 2), min(len(checked), checked.index(i) + 3))})
    blocks = {}
    for f in sorted(glob.glob(f"{OUT}/atomerr_pack_[0-9]*.md")):
        for b in re.split(r"(?m)^(?=### E\d+\. )", open(f, encoding="utf-8").read())[1:]:
            blocks[re.match(r"### (E\d+)\. ", b).group(1)] = b
    out = [f"# T4 加查复看包 — ATOM_ERR (S1-R1) ({len(idx)} 条; 编号沿用原包)", "",
           "> 由 `scripts/t4/t4_atomerr_report.py` 从 `work/t4/atomerr/atomerr_pack_N.md` 原样摘出. 只读材料.", ""]
    out += [blocks[num[checked[j]]] for j in idx]
    open(f"{OUT}/atomerr_pack_second.md", "w", encoding="utf-8").write("\n".join(out))
    print("second-look pack:", [num[checked[j]] for j in idx])
