#!/usr/bin/env python3
"""T3 S1: errata expansion -> work/t3_errata.json (t1_errata.json is read-only input).
atom_err: every t1_errata.t3_atom_err key + t3_fp_expected R1/R2 + triage final_class ATOM_ERR, each split
  R1 (atom extraction wrong, KB = PDF)            -> terminal ATOM_ERR
  R2 (atom = PDF, KB deliberately != PDF, T-n)    -> terminal PDF_TYPO (registry id required)
target_remap: t1 remap keys (the _B-FA group key expanded to its 23 atoms) + R3 entries of t3_fp_expected.
  + T4 R2L (主人 2026-11-27 问题 3 / 7b = A): the PDF_TYPO entries of work/t4_r2l_relabel.json -> R2 with the listed
  registry id (asserted to exist; out-of-scope entries re-assert pdf / kb line + token).
pending_user: 4 disputed atoms with the T2 outcome (live hit on target or not).
Every entry carries in_allowed_set (triage ∪ t3_t2s_atoms) and ledger_verdict_now; nothing outside the allowed
set is flipped by t3_writeback (they are reported as 'explained' only).
Usage: python3 -I .work/10_tier_b_repair/scripts/t3/t3_errata_build.py
"""
import collections, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from t3_common import ROOT, W, CK, lj, norm, norm_pdf, kb_norm, atom_order, expand_ref, writer_rows

A = {a["atom_id"]: a for a in lj(f"{W}/pdf_atoms.jsonl")}
E1 = json.load(open(f"{W}/t1_errata.json"))
T = {t["atom_id"]: t for t in json.load(open(f"{W}/triage_merged.json"))}
S = {r["atom_id"] for r in lj(f"{W}/t3_t2s_atoms.jsonl")}
L = {e["pdf_atom_id"]: e for e in lj(f"{W}/coverage_ledger.wc.pre_t3.jsonl")}  # stock (pre-T3) verdicts: never read T3 output
X = {r["atom_id"]: r for r in lj(f"{W}/t3_fp_expected_regressions.jsonl")}
REG = lj(f"{W}/t2_pdf_typo_registry.jsonl")
ALLOWED = set(T) | S  # + every t3_errata key (主控 C2), added below once the keys are known

FA23 = [f"ig34_p0363_a0{n}" for n in (11, 12, 13, 15, 16, 17, 18, 19)] + \
       [f"ig34_p0364_a00{n}" for n in range(1, 10)] + [f"ig34_p0364_a0{n}" for n in (11, 12, 13, 17, 18, 19)]
# B-FA checkpoint fp section: the authoritative list of the 23 relocated atoms
FA_CK = f"{CK}/t2_B-FA.md"


def reg_lookup(batch, tn):
    return [r["id"] for r in REG if r["batch"] == batch and re.match(rf"{re.escape(batch)}( \w+)? T-{tn}(?!\d)", r["id"])]


def classify(i, note):
    """-> (cls, registry_ids, basis_batch). Explicit fp class wins; else 照录 => R1; T-n => R2; else R1."""
    m = re.search(r"\b((?:B|S)-[A-Za-z0-9]+)(?: [A-Z]{2})? T-(\d+)", note) or \
        (re.search(r"\b((?:B|S)-[A-Za-z0-9]+)(?: [A-Z]{2})? T-(\d+)", X[i]["note"]) if i in X else None)
    regs = reg_lookup(m.group(1), m.group(2)) if m else []
    if i in X and X[i]["class"] in ("R1", "R2"):
        cls = X[i]["class"]
    elif "照录" in note:
        cls = "R1"
    elif m:
        cls = "R2"
    else:
        cls = "R1"
    return cls, regs, (m.group(1) if m else None)


def _find(p, needles):
    if not os.path.exists(p):
        return None
    for nd in needles:
        for n, l in enumerate(open(p, encoding="utf-8"), 1):
            if nd and nd in l:
                return f"{os.path.relpath(p, ROOT)}:{n}"
    return None

def errata_ptr(i, note):
    """file:line where the batch that registered this errata names the atom. Note prefixes: 'B-XX review|audit|writer',
    'B-XX T-n', 'B-XX review E-1', 'T2 global fp audit' (-> evidence/t2_fp_expected_regressions.md)."""
    tail = i.split("_", 1)[1]
    if note.startswith("T2 global fp audit"):
        return _find(f"{os.path.dirname(CK)}/t2_fp_expected_regressions.md", [i])
    m = re.match(r"((?:B|S)-[A-Za-z0-9]+)(?:\s+(review|audit|writer))?", note)
    if not m:
        return None
    b, role = m.group(1), m.group(2)
    files = {"review": [f"t2_{b}_review.md", f"t2_{b}_review_a3.md"], "audit": [f"t2_{b}_audit.md"], "writer": [f"t2_{b}.md"]}.get(role) \
        or [f"t2_{b}.md", f"t2_{b}_review.md", f"t2_{b}_audit.md"]
    tn = re.search(r"T-\d+", note)
    for fn in files + [f"t2_{b}.md", f"t2_{b}_review.md", f"t2_{b}_audit.md"]:
        r = _find(f"{CK}/{fn}", [i, tail])
        if r:
            return r
    for fn in files:
        r = _find(f"{CK}/{fn}", [tn.group(0)] if tn else [])
        if r:
            return r + " (T-n 行; 原子 id 未出现在该文件)"
    pg = re.match(r"p(\d{4})_", tail).group(1)
    for fn in files + [f"t2_{b}.md", f"t2_{b}_review.md", f"t2_{b}_audit.md"]:
        r = _find(f"{CK}/{fn}", [f"p{pg}_", f"p{int(pg)} ", f"p{int(pg)}:", f"p{int(pg)},"])
        if r:
            return r + " (页级行; 该批以范围/页号记这组原子)"
    return None

atom_err = {}
def put(i, cls, basis, source, regs, ck):
    a = A.get(i)
    atom_err[i] = dict(cls=cls, terminal="ATOM_ERR" if cls == "R1" else "PDF_TYPO", basis=basis, source=source,
                       registry=regs, checkpoint=ck, in_allowed_set=i in ALLOWED,
                       ledger_verdict_now=L.get(i, {}).get("verdict", "NO_LEDGER_ROW"),
                       triage_class=T.get(i, {}).get("final_class"), page=a["page"] if a else None)

# (1) t1_errata.t3_atom_err (100)
for i, note in E1["t3_atom_err"].items():
    cls, regs, b = classify(i, note)
    put(i, cls, note, "t1_errata.t3_atom_err", regs, errata_ptr(i, note))
# BS p0198_a012: note has no T-n; registry B-BS T-2 'part the' -> 'part of the'
if "ig34_p0198_a012" in atom_err:
    atom_err["ig34_p0198_a012"].update(cls="R2", terminal="PDF_TYPO", registry=["B-BS T-2"])
# T4 解冻 (主控决定 2026-11-27, t4_thaw_W3.md "attempt 1 续"): U-7 R2 atoms of s0_classify -> their registry rows
T4_U7_REG = {"ig34_p0160_a0026": ["B-DS U-4"], "ig34_p0165_a0007": ["B-DS U-1"], "ig34_p0419_a006": ["B-TS T-3", "B-TS T-2"],
             "ig34_p0419_a011": ["B-TS T-3"], "ig34_p0419_a013": ["B-TS T-3"], "ig34_p0425_a024": ["B-TS T-6"], "ig34_p0372_a013": ["B-FA T-8"],
             "ig34_p0298_a001": ["B-NV N-2"], "ig34_p0285_a015": ["B-NV N-1"], "ig34_p0280_a036": ["B-PCPP T-8b"],
             "ig34_p0280_a039": ["B-PCPP T-8"], "ig34_p0280_a040": ["B-PCPP T-8"], "ig34_p0281_a002": ["S-SPC2 N-1"],
             "ig34_p0281_a003": ["S-SPC2 N-1"], "ig34_p0281_a031": ["S-SPC2 N-2"], "ig34_p0281_a032": ["S-SPC2 N-2"],
             "ig34_p0085_a010": ["B-SM O32"], "ig34_p0190_a017": ["B-EG T-3"], "ig34_p0419_a017": ["B-TS T-4"]}
assert all(r in {x["id"] for x in REG} for v in T4_U7_REG.values() for r in v)
# T4 解冻 (主控决定 2): ig34_p0362_a010 was R1 (KB = PDF "thought be related"); after U-7 A3-7 KB = atom ≠ PDF -> R2 PDF_TYPO
if "ig34_p0362_a010" in atom_err:
    atom_err["ig34_p0362_a010"].update(cls="R2", terminal="PDF_TYPO", registry=["B-FA T-4"],
        basis="T4 U-7 后依据变更: KB 按 U-7 A3-7 写正确值 'thought to be related' (= 原子), PDF p362 'thought be related' → R2 PDF_TYPO "
              "(主控决定 2026-11-27). 原 basis: " + atom_err["ig34_p0362_a010"]["basis"])
# (2) t3_fp_expected R1/R2 not yet keyed (S0 additions: SE x4, CP x5, IS, PC a051)
for i, r in X.items():
    if r["class"] in ("R1", "R2") and i not in atom_err:
        cls, regs, b = classify(i, r["note"])
        if i == "ig34_p0240_a004":
            regs = ["B-IS T-4"]
        if i in T4_U7_REG:  # T4 解冻 (主控决定): registry given per atom (non T-n ids, T-8 vs T-8b)
            regs = T4_U7_REG[i]
        put(i, cls, r["note"], "t3_fp_expected_regressions.jsonl (S0)", regs, _find(f"{W}/t3_fp_expected_regressions.jsonl", [f'"atom_id": "{i}"']))
# (3) triage ATOM_ERR (T1.2 writer + T1.3 reviewer 100%)
for i, t in T.items():
    if t["final_class"] == "ATOM_ERR" and i not in atom_err:
        put(i, "R1", f"T1 triage ATOM_ERR ({t['src']}, reviewed={t['reviewed']})", "triage_merged.json",
            [], _find(f"{W}/triage_merged.json", [f'"atom_id": "{i}"']) + f" (lane {t['lane']} {t['pack_id']}; T1.3 reviewer 100%)")
# (4) T4 U-2 (委托代裁 2026-11-27, t4_user_decisions.md §000): pending_user residual -> R1. PDF p56 (ig34_p0056.txt:37-40) and
# KB ch04:1478 read "...split between words to improve readability."; the atom drops "to improve readability" (K4 below re-checks atom ∉ PDF)
put("ig34_p0056_a006", "R1", "T4 U-2 A (委托代裁): 原子第 2/3 格漏 'to improve readability' 与句点; PDF p56:37-40 与 KB ch04:1478 一致",
    "T4 U-2 (t4_user_decisions.md §000)", [], _find(f"{CK}/t4_user_decisions.md", ["| U-2 | **A**"]))
# (5) T4 第二轮改台账 R2L (主人 2026-11-27 问题 3 = A / 7b = A): 25 atoms whose KB-vs-PDF difference is a registered PDF typo
# (KB 写正确值) -> R2 PDF_TYPO bound to the given registry id. Data: work/t4_r2l_relabel.json (scripts/t4/t4_r2l_build.py);
# out-of-scope ones (7b) re-assert pdf / kb line + token like the U-8 keep list.
R2L = json.load(open(f"{W}/t4_r2l_relabel.json"))["relabel"]
R2L_BAD = []
for i, e in R2L.items():
    # reviewer (R2L): the pdf / kb re-check is mandatory for group registered-typo-oos and forbidden for every other group
    assert ("pdf" in e) == ("kb" in e) == (e["group"] == "registered-typo-oos"), (i, e["group"], sorted(e))
    if e["to"] != "PDF_TYPO":
        continue
    assert i not in atom_err and i in A, i
    assert all(r in {x["id"] for x in REG} for r in e["registry"]), (i, e["registry"])
    if e["group"] == "registered-typo-oos":
        pg, ln = e["pdf"]["line"].split(":")
        kf, kn = e["kb"]["line"].rsplit(":", 1)
        if e["pdf"]["token"] not in norm_pdf(open(f"{W}/pdf_pages/{pg}.txt", encoding="utf-8").read().splitlines()[int(ln) - 1]) or \
                e["kb"]["token"] not in norm(open(f"{ROOT}/{kf}", encoding="utf-8").read().splitlines()[int(kn) - 1]):
            R2L_BAD.append(i)
    put(i, "R2", f"T4 R2L {e['decision']}: KB 与 PDF 的差异 = 已登记 PDF 笔误 {'/'.join(e['registry'])} (KB 写正确值); 审查者原始结果 {e['raw']}",
        f"T4 R2L ({e['group']}; {e['decision']})", list(e["registry"]), f"{os.path.relpath(W, ROOT)[:-len('work')]}{e['raw']}")
assert not R2L_BAD, R2L_BAD

# ── attempt 2 / 审计 K4: an R1 (ATOM_ERR) needs norm(atom) ∉ norm_pdf(p-1..p+1). If the atom IS on the PDF page and the
# batch registered a KB deviation for it (registry row on p-1..p+1 whose pdf_value ⊂ atom) -> R2 PDF_TYPO; else drop it.
def pdf_window(src, p):
    return " ".join(norm_pdf(open(f, encoding="utf-8").read()) for q in (p - 1, p, p + 1)
                    for f in [f"{W}/pdf_pages/{src}_p{q:04d}.txt"] if os.path.exists(f))
k4 = {"to_R2": {}, "dropped": {}}
for i, v in list(atom_err.items()):
    if v["cls"] != "R1" or i not in A:
        continue
    a = A[i]
    va = norm(a["verbatim"])
    v["atom_in_pdf"] = va in pdf_window(i.split("_")[0], a["page"])
    if not v["atom_in_pdf"]:
        continue
    m = re.match(r"((?:B|S)-[A-Za-z0-9]+)", v["basis"])
    regs = [r for r in REG if (not m or r["batch"] == m.group(1)) and abs(r["pdf_page"] - a["page"]) <= 1
            and len(norm(r["pdf_value"]).split()) >= 2 and norm(r["pdf_value"]) in va]
    if regs:
        v.update(cls="R2", terminal="PDF_TYPO", registry=[r["id"] for r in regs],
                 basis=f"[K4 改判] 原子 = PDF (norm ⊂ p{a['page'] - 1}-{a['page'] + 1}); KB 有登记偏离 {regs[0]['id']}: "
                       f"PDF '{regs[0]['pdf_value']}' → KB '{regs[0]['kb_value']}'. 原 basis: {v['basis'][:120]}")
        k4["to_R2"][i] = v["registry"]
    else:
        k4["dropped"][i] = v["basis"][:160]
        del atom_err[i]

# target remap
remap = {}
for i, v in E1["t3_target_remap"].items():
    if i == "_B-FA":
        continue
    tgt = v if v.startswith("knowledge_base/") else "knowledge_base/domains/FA/assumptions.md"
    remap[i] = dict(target=tgt, basis=v[:160], source="t1_errata.t3_target_remap")
for i in FA23:
    remap.setdefault(i, dict(target="knowledge_base/domains/FA/assumptions.md",
                             basis="_B-FA 组键展开 (t2_B-FA.md fp 节 / t2_B-FA_review.md H 节 23 条)",
                             source="t1_errata._B-FA (expanded)"))
for i, r in X.items():
    if r["class"] == "R3" and i not in remap:
        tgt = "knowledge_base/" + re.search(r"new_target: (\S+)", r["note"]).group(1)
        remap[i] = dict(target=tgt, basis=r["note"][:160], source="t3_fp_expected_regressions.jsonl (S0)")
remap["ig34_p0240_a004"] = dict(target="knowledge_base/domains/IS/examples.md",
                                basis="S-SPC1 D2 删 IS/assumptions 附录副本; 现在 IS/examples.md:215 (B-IS T-4 改正值)",
                                source="S0 double key")
# 主控 C7: LB p245 footnote now lives with the LB spec table (S-SPC1 reorder; t3_delta_rereview.md LOW note)
remap["ig34_p0245_a007"] = dict(target="knowledge_base/domains/LB/spec.md",
                                basis="主控 C7: LB spec 脚注由 S-SPC1 移至 LB/spec.md:564 (t3_delta_rereview.md B-LB 节)",
                                source="主控 C7")
for i in remap:
    remap[i].update(in_allowed_set=i in ALLOWED, ledger_verdict_now=L.get(i, {}).get("verdict", "NO_LEDGER_ROW"),
                    verbatim_hits_target=bool(i in A and norm(A[i]["verbatim"]) in kb_norm(remap[i]["target"])))

# pending_user
order, idx = atom_order()
WR = collections.defaultdict(list)
for b, wf, n, r in writer_rows():
    for i in expand_ref(str(r["ref"]), idx, order)[0]:
        WR[i].append(dict(batch=b, action=r["action"], kb_file=r["kb_file"], ptr=f"{wf}:{n}", note=r["note"][:160]))
pending = {}
for i, v in E1["pending_user"].items():
    files = sorted({w["kb_file"] for w in WR[i]})
    hit = next((f for f in files if norm(A[i]["verbatim"]) in kb_norm(f)), None)
    fixed = any(w["action"] in ("INSERTED", "REPLACED", "TABLE_REBUILT") for w in WR[i])
    if i in atom_err and atom_err[i]["source"].startswith("T4 "):
        concl = f"{atom_err[i]['source']} → 终态 {atom_err[i]['terminal']} (S1 atom_err)"
    elif i in atom_err:
        concl = f"T2 改判 keep-correct ({'/'.join(atom_err[i]['registry'])}) → 终态 {atom_err[i]['terminal']} (S1 atom_err), T4 用户知悉"
    elif fixed and hit:
        concl = f"T2 实修且 target 命中 ({hit}) → 可翻 EXACT"
    else:
        concl = "T2 已改但 target 不逐字命中 → 残留 (保持原 verdict), 标 T4 待裁" if fixed else "T2 未改 → 残留, 标 T4 待裁"
    pending[i] = dict(t1=v, writer_rows=WR[i], hit=hit, fixed=fixed, conclusion=concl)

# 主控裁定 C2: allowed set = triage ∪ T2S ∪ t3_errata per-atom keys -> every errata entry is in the allowed set
ALLOWED |= set(atom_err) | set(remap)
for d in (atom_err, remap):
    for i in d:
        d[i]["in_allowed_set"] = True
out = dict(_note="T3 S1 errata (generated by scripts/t3/t3_errata_build.py; t1_errata.json untouched). "
                 "atom_err.cls R1→ATOM_ERR, R2→PDF_TYPO. since 主控 C2 every key is in the allowed set.",
           atom_err=dict(sorted(atom_err.items())), target_remap=dict(sorted(remap.items())), pending_user=pending, k4=k4)
json.dump(out, open(f"{W}/t3_errata.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)

C = collections.Counter
print("K4: R1 -> R2:", k4["to_R2"], " dropped (atom on PDF page, no registry):", list(k4["dropped"]))
bad_r1 = [i for i, v in atom_err.items() if v["cls"] == "R1" and v.get("atom_in_pdf")]
assert not bad_r1, bad_r1
print("atom_err:", len(atom_err), dict(C((v["cls"], v["source"].split(" ")[0]) for v in atom_err.values())))
print("  by terminal x allowed:", dict(C((v["terminal"], v["in_allowed_set"]) for v in atom_err.values())))
print("  outside allowed set by ledger verdict:", dict(C(v["ledger_verdict_now"] for v in atom_err.values() if not v["in_allowed_set"])))
r2_noreg = [i for i, v in atom_err.items() if v["cls"] == "R2" and not v["registry"]]
noptr = [i for i, v in atom_err.items() if not v["checkpoint"]]
print("  atom_err without file:line pointer:", len(noptr), noptr[:20])
print("  R2 without registry id:", r2_noreg)
print("target_remap:", len(remap), " not hitting target:", [i for i, v in remap.items() if not v["verbatim_hits_target"]])
print("  FA expanded present:", sum(i in remap for i in FA23), "/23")
for i, v in pending.items():
    print("pending", i, "->", v["conclusion"])
sys.exit(1 if r2_noreg else 0)
