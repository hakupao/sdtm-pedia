#!/usr/bin/env python3
"""T0 inventory (read-only): Tier B section list + atom-level fingerprint probe vs CURRENT KB.
Usage: python3 -I .work/10_tier_b_repair/scripts/t0_inventory.py <orig_p4b_section_coverage.jsonl>
  orig file = `git show f024a3f:branches/06_deep_verification/section_coverage.jsonl`
Writes .work/10_tier_b_repair/inventory.jsonl + prints summary. Never writes archive/ or knowledge_base/.
"""
import json, re, sys, glob, collections, unicodedata, os
ROOT = "/Volumes/DevSSD/Project/sdtm-pedia"
DV = f"{ROOT}/archive/deep_verification"
OUT = f"{ROOT}/.work/10_tier_b_repair/inventory.jsonl"
TIERB = {"SIBLING_DROPPED", "CONTENT_TRUNCATED"}

def lj(p): return [json.loads(l) for l in open(p, encoding="utf-8")]
def norm(s):
    s = unicodedata.normalize("NFKC", s)
    s = s.translate(str.maketrans({"‘": "'", "’": "'", "“": '"', "”": '"', "–": "-", "—": "-"}))
    s = re.sub(r"[*_`|>#\\]", " ", s)
    return re.sub(r"\s+", " ", s).strip().lower()

# NB: section_id is NOT unique (308 ids / 399 rows); key by (source, section_key)
K = lambda r: (r["source"], r["section_key"])
orig = {K(r): r for r in lj(sys.argv[1])}
cur = {K(r): r for r in lj(f"{DV}/section_coverage.jsonl")}
ledger = {e["pdf_atom_id"]: e for e in lj(f"{DV}/coverage_ledger.jsonl")}
atoms = collections.defaultdict(list)
for a in lj(f"{DV}/pdf_atoms.jsonl"):
    src = a["atom_id"].split("_")[0]
    atoms[(src, a["parent_section"])].append(a)

kb_files = {p[len(ROOT)+1:]: norm(open(p, encoding="utf-8").read()) for p in glob.glob(f"{ROOT}/knowledge_base/**/*.md", recursive=True)}
kb_all = "\n".join(kb_files.values())

ids = sorted(i for i in set(orig) | set(cur)
             if orig.get(i, {}).get("aggregate_verdict") in TIERB or cur.get(i, {}).get("aggregate_verdict") in TIERB)
rows = []
for sid in ids:  # sid = (source, section_key)
    o, c = orig.get(sid, {}), cur.get(sid, {})
    ref = c or o
    content = [a for a in atoms[(ref["source"], ref["section_key"])] if a["atom_type"] != "HEADING"]
    vc = collections.Counter((ledger.get(a["atom_id"]) or {}).get("verdict", "MISSING") for a in content)
    gap = [a for a in content if (ledger.get(a["atom_id"]) or {}).get("verdict", "MISSING") not in ("EXACT", "EQUIVALENT", "INTENTIONAL_EXCLUDE")]
    tgt = ref.get("md_target_files") or []
    hit_t = hit_any = 0; by_type = collections.Counter(); absent = []
    for a in gap:
        v = norm(a["verbatim"]); by_type[a["atom_type"]] += 1
        in_t = any(v and v in kb_files.get(f, "") for f in tgt)
        in_any = in_t or (v and v in kb_all)
        hit_t += in_t; hit_any += bool(in_any)
        if not in_any: absent.append(a["atom_id"])
    denom_noie = len(content) - vc["INTENTIONAL_EXCLUDE"]
    rows.append({
        "tb_id": None, "section_id": ref["section_id"], "source": ref["source"], "section_key": ref["section_key"],
        "pdf_page_range": ref["pdf_page_range"],
        "verdict_p4b_orig": o.get("aggregate_verdict"), "verdict_current": c.get("aggregate_verdict"),
        "patterns_current": c.get("failure_patterns", []),
        "md_target_files": tgt, "n_content_atoms": len(content), "ledger_verdicts": dict(vc),
        "density_current": c.get("coverage_density"),
        "density_excl_ie": round((vc["EXACT"] + vc["EQUIVALENT"]) / denom_noie, 4) if denom_noie else None,
        "n_gap_atoms": len(gap), "gap_by_type": dict(by_type),
        "probe_verbatim_in_target": hit_t, "probe_verbatim_anywhere": hit_any,
        "probe_absent": len(gap) - hit_any, "probe_absent_atom_ids": absent,
        "child_sections": c.get("child_sections", {}),
    })
for i, r in enumerate(rows, 1): r["tb_id"] = f"TB-{i:03d}"
with open(OUT, "w", encoding="utf-8") as f:
    for r in rows: f.write(json.dumps(r, ensure_ascii=False) + "\n")

C = collections.Counter
print("sections in union:", len(rows))
print("orig verdict:", C(r["verdict_p4b_orig"] for r in rows))
print("current verdict:", C(r["verdict_current"] for r in rows))
print("transitions:", C((r["verdict_p4b_orig"], r["verdict_current"]) for r in rows).most_common())
cb = [r for r in rows if r["verdict_current"] in TIERB]
print("current TierB sections:", len(cb), "content atoms:", sum(r["n_content_atoms"] for r in cb),
      "gap atoms:", sum(r["n_gap_atoms"] for r in cb),
      "probe hit in target:", sum(r["probe_verbatim_in_target"] for r in cb),
      "probe hit anywhere:", sum(r["probe_verbatim_anywhere"] for r in cb),
      "probe absent:", sum(r["probe_absent"] for r in cb))
gv = C()
for r in cb: gv.update({k: v for k, v in r["ledger_verdicts"].items() if k not in ("EXACT", "EQUIVALENT", "INTENTIONAL_EXCLUDE")})
print("gap atoms by ledger verdict:", gv)
gt = C()
for r in cb: gt.update(r["gap_by_type"])
print("gap atoms by type:", gt)
bf = C(); bfa = C()
for r in cb:
    for f in (r["md_target_files"] or ["<none>"]): bf[f] += 1
    k = (r["md_target_files"] or ["<none>"])[0]; bfa[k] += r["probe_absent"]
print("sections per target file (top 40):", bf.most_common(40))
print("probe_absent by primary file (top 30):", bfa.most_common(30))
print("files touched:", len(bf))
print("no target file:", sum(1 for r in cb if not r["md_target_files"]))
print("density_excl_ie >= 0.80 among current TierB:", sum(1 for r in cb if (r["density_excl_ie"] or 0) >= 0.8))

# ── render section table (inventory_table.md) ──
SPEC_CORE = ("Req", "Exp", "Perm")
A = {}
for lst in atoms.values():
    for a in lst: A[a["atom_id"]] = a
def kind(a):
    v = a["verbatim"].strip().strip("|").strip(); cells = [x.strip() for x in v.split("|")]
    if (a["atom_type"] == "TABLE_HEADER" and "Variable Label" in v) or (a["atom_type"] == "TABLE_ROW" and cells and cells[-1] in SPEC_CORE):
        return "spec"
    return "prose" if a["atom_type"] in ("SENTENCE", "LIST_ITEM", "NOTE") else "other"
with open(OUT.replace("inventory.jsonl", "inventory_table.md"), "w", encoding="utf-8") as f:
    f.write("# Tier B 节清单 (自动生成, 勿手改)\n\n> 生成: `python3 -I .work/10_tier_b_repair/scripts/t0_inventory.py <orig_p4b.jsonl>`\n"
            "> 列: 现 verdict / 原 verdict / 内容原子 / gap 原子 (ledger 非 EXACT/EQUIV/IE) / probe 缺 (spec·prose·other) / IE 外密度 / 主目标文件\n\n"
            "| TB | src | 节 | 现 | 原 | 原子 | gap | 缺 s/p/o | 密度(去IE) | 主目标文件 |\n|---|---|---|---|---|--:|--:|---|--:|---|\n")
    ab = {"SIBLING_DROPPED": "SD", "CONTENT_TRUNCATED": "CT", "FULL_COVERAGE": "FULL", "MOSTLY_COMPLETE": "MOST", "SKELETON_ONLY": "SKEL", None: "-"}
    for r in sorted(rows, key=lambda r: ((r["md_target_files"] or ["~"])[0], r["source"], r["section_key"])):
        k = collections.Counter(kind(A[i]) for i in r["probe_absent_atom_ids"])
        sk = r["section_key"].replace("|", "/")[:70]
        tgt = (r["md_target_files"] or ["(无)"])[0].replace("knowledge_base/", "")
        f.write(f"| {r['tb_id']} | {r['source']} | {sk} | {ab[r['verdict_current']]} | {ab[r['verdict_p4b_orig']]} | {r['n_content_atoms']} | {r['n_gap_atoms']} | "
                f"{k['spec']}/{k['prose']}/{k['other']} | {r['density_excl_ie'] if r['density_excl_ie'] is not None else '-'} | {tgt} |\n")
print("wrote inventory_table.md")
