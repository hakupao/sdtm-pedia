#!/usr/bin/env python3
"""T1.2 packing: work/triage_prefilter.jsonl -> work/t1_packs/pack_NNN.json + index.md, grouped into 4 lanes.
- A pack = whole sections of one lane (~50 atoms, max 60 unless one section; a section is split only if > 80 atoms).
- Unit = prefilter primary_unit (domain dir or chapter/model file). Components = units linked by manual items
  (MANUAL_02 spans PC+PP). Lanes = components bin-packed (LPT) so lanes never share an owned KB target file.
- Non-owned target files a section also lists go to `kb_context_readonly` (read-only context, may cross lanes).
No PDF verbatim is written (atoms are referenced by id; writer reads work/pdf_atoms.jsonl + work/pdf_pages).
Usage (repo root): python3 -I .work/10_tier_b_repair/scripts/t1_pack.py
"""
import collections, glob, json, math, os, shutil

ROOT = "/Volumes/DevSSD/Project/sdtm-pedia"
TB = f"{ROOT}/.work/10_tier_b_repair"
W = f"{TB}/work"
OUT = f"{W}/t1_packs"
TARGET, SPLIT_OVER, LANES = 50, 80, ["A", "B", "C", "D"]

rows = [json.loads(l) for l in open(f"{W}/triage_prefilter.jsonl", encoding="utf-8") if l.strip()]
kb_len = {f"knowledge_base/{os.path.relpath(p, f'{ROOT}/knowledge_base')}": sum(1 for _ in open(p, encoding="utf-8"))
          for p in glob.glob(f"{ROOT}/knowledge_base/**/*.md", recursive=True)}
unit_of = lambda f: "/".join(f.split("/")[:3]) if f.split("/")[1] == "domains" else f
def unit_files(u):
    return sorted(f for f in kb_len if unit_of(f) == u) if u.startswith("knowledge_base/domains/") else [u]

# union-find over units
par = {}
def find(x):
    par.setdefault(x, x)
    while par[x] != x: par[x] = par[par[x]]; x = par[x]
    return x
for r in rows:
    find(r["primary_unit"])
    if r["manual"]:
        for t in r["targets"]: par[find(unit_of(t))] = find(r["primary_unit"])

# sections in PDF order (first atom order in prefilter = pdf_atoms order)
secs = collections.OrderedDict()
for r in rows:
    secs.setdefault((r["source"], r["section_key"], r["primary_unit"]), []).append(r)
comp = collections.defaultdict(list)
for k, rs in secs.items():
    comp[find(k[2])].append((k, rs))

# lanes: LPT over components
csize = {c: sum(len(rs) for _, rs in sl) for c, sl in comp.items()}
lane_n, lane_of = {l: 0 for l in LANES}, {}
for c in sorted(csize, key=lambda c: -csize[c]):
    l = min(LANES, key=lambda l: lane_n[l]); lane_of[c] = l; lane_n[l] += csize[c]

packs = []   # packs may mix components of the same lane (lane-disjointness is what T1/T2 need)
for lane in LANES:
    sl = [x for c in sorted(comp, key=lambda c: -csize[c]) if lane_of[c] == lane for x in comp[c]]
    cur, n, chunks = [], 0, []
    for k, rs in sl:
        if len(rs) > SPLIT_OVER:
            m = math.ceil(len(rs) / TARGET); sz = math.ceil(len(rs) / m)
            chunks += [(k, rs[i:i + sz], f"{i // sz + 1}/{m}") for i in range(0, len(rs), sz)]
        else:
            chunks.append((k, rs, None))
    for k, rs, part in chunks:
        if cur and (n + len(rs) > TARGET + 10 or part):
            packs.append((lane, cur)); cur, n = [], 0
        cur.append((k, rs, part)); n += len(rs)
        if part: packs.append((lane, cur)); cur, n = [], 0
    if cur: packs.append((lane, cur))

if os.path.isdir(OUT): shutil.rmtree(OUT)
os.makedirs(OUT)
# keep packing order (lane, component, PDF order)
lane_files = collections.defaultdict(set); lane_ctx = collections.defaultdict(set); seen = collections.Counter()
index = []
for i, (c, items) in enumerate(packs, 1):
    pid = f"pack_{i:03d}"; lane = c
    units = sorted({k[2] for k, _, _ in items})
    owned = sorted({f for u in units for f in unit_files(u)})
    sections, atoms, pages, ctx, ranges = [], [], set(), set(), collections.defaultdict(list)
    for k, rs, part in items:
        pr = sorted({r["pdf_page"] for r in rs if r["pdf_page"]})
        sections.append({"source": k[0], "section_key": k[1], "primary_unit": k[2], "part": part,
                         "n_atoms": len(rs), "pdf_pages": pr})
        for r in rs:
            seen[r["atom_id"]] += 1
            if r["pdf_page"]: pages |= {(r["source"], r["pdf_page"]), (r["source"], r["pdf_page"] + 1)}
            for t in r["targets"]:
                (ranges[t].extend(r.get("target_section_lines", {}).get(t) or [None]) if t in owned else ctx.add(t))
            a = {"atom_id": r["atom_id"], "atom_type": r["atom_type"], "pdf_page": r["pdf_page"],
                 "ledger_verdict": r.get("ledger_verdict"), "prefilter_class": r["prefilter_class"],
                 "prefilter_suggest": r["prefilter_suggest"]}
            if r["manual"]:
                a.update({"manual": True, "issue": r["issue"], "kb_loc": r["kb_loc"], "evidence": r["evidence"]})
            else:
                a.update({"fp_hit": r["fp"]["hit_target_loc"] or r["fp"]["hit_any_loc"], "fp_hit_in_section": r["fp"]["hit_in_section"],
                          "fp_v_len": r["fp"]["v_len"], "spec_row": r["spec_row"],
                          "spec_loc": (r["spec_detail"] or {}).get("spec_loc"), "census": r["census"]})
            atoms.append(a)
    kb_targets = []
    for f in owned:
        rg = sorted({tuple(x) for x in ranges.get(f, []) if x})
        if f in ranges or f.endswith("/spec.md") and any(a.get("spec_row") for a in atoms):
            kb_targets.append({"file": f, "lines": [list(x) for x in rg] or [[1, kb_len.get(f, 0)]]})
    if not kb_targets:
        kb_targets = [{"file": f, "lines": [[1, kb_len.get(f, 0)]]} for f in owned]
    lane_files[lane] |= set(owned); lane_ctx[lane] |= ctx
    pk = {"pack_id": pid, "lane": f"lane_{lane}", "units": units, "n_atoms": len(atoms), "sections": sections,
          "pdf_pages": [f"{s}_p{p:04d}" for s, p in sorted(pages)], "kb_targets": kb_targets,
          "kb_owned_files": owned, "kb_context_readonly": sorted(ctx - set(owned)), "atoms": atoms}
    json.dump(pk, open(f"{OUT}/{pid}.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    index.append(pk)

# self-checks
assert all(v == 1 for v in seen.values()) and len(seen) == len(rows), "every atom in exactly one pack"
for a in LANES:
    for b in LANES:
        if a < b: assert not (lane_files[a] & lane_files[b]), (a, b, lane_files[a] & lane_files[b])
for p in index:
    for s in p["sections"]:
        assert s["n_atoms"] <= SPLIT_OVER or s["part"], s
xlane = sum(1 for l in LANES for f in lane_ctx[l] if any(f in lane_files[m] for m in LANES if m != l))

C = collections.Counter
with open(f"{OUT}/index.md", "w", encoding="utf-8") as f:
    f.write("# T1.2 分诊包索引\n\n> 生成: `python3 -I .work/10_tier_b_repair/scripts/t1_pack.py` (输入 `work/triage_prefilter.jsonl`)\n"
            f"> 包 {len(index)} 个 / 原子 {len(rows)} (含 manual 2). 每包整节 (节 > {SPLIT_OVER} 才拆, 标 part). "
            "lane 间 owned KB 文件不相交 (脚本断言); `kb_context_readonly` 只读参考, 可跨 lane.\n"
            f"> 跨 lane 的只读参考文件引用: {xlane} 个 (T1 只读无冲突; T2 批次表在 T1.4 定).\n\n")
    f.write("| lane | 包数 | 原子 | units |\n|---|--:|--:|---|\n")
    for l in LANES:
        ps = [p for p in index if p["lane"] == f"lane_{l}"]
        us = sorted({u.replace("knowledge_base/", "") for p in ps for u in p["units"]})
        f.write(f"| lane_{l} | {len(ps)} | {sum(p['n_atoms'] for p in ps)} | {', '.join(us)} |\n")
    f.write("\n| pack | lane | 原子 | 节 (part) | PDF 页 | 预筛 suggest |\n|---|---|--:|---|---|---|\n")
    for p in index:
        secs_s = "; ".join(f"{s['section_key'][:48]}" + (f" ({s['part']})" if s["part"] else "") for s in p["sections"])
        pg = sorted({int(x.split('_p')[1]) for x in p["pdf_pages"]})
        sug = ", ".join(f"{k}:{v}" for k, v in C(a["prefilter_suggest"] or "-" for a in p["atoms"]).most_common())
        f.write(f"| {p['pack_id']} | {p['lane']} | {p['n_atoms']} | {secs_s} | {pg[0]}-{pg[-1]} | {sug} |\n")

print(f"packs: {len(index)}  atoms: {len(seen)}  sizes min/max: {min(p['n_atoms'] for p in index)}/{max(p['n_atoms'] for p in index)}")
for l in LANES:
    ps = [p for p in index if p["lane"] == f"lane_{l}"]
    print(f"lane_{l}: packs {len(ps)} atoms {sum(p['n_atoms'] for p in ps)} owned files {len(lane_files[l])}")
print(f"owned-file disjointness across lanes: OK; cross-lane read-only context refs: {xlane}")
