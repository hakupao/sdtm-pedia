"""T1.4 package generator (scratch helper). Writes evidence/checkpoints/t1_ie_candidates.md + t1_batch_draft.md.
IDs / locations / counts only, no PDF text. Run from repo root: python3 -I .work/10_tier_b_repair/scripts/helpers/t14_pkg.py"""
import collections, glob, json, re
TB = "/Volumes/DevSSD/Project/sdtm-pedia/.work/10_tier_b_repair"
M = json.load(open(f"{TB}/work/triage_merged.json"))
PRE = {json.loads(l)["atom_id"]: json.loads(l) for l in open(f"{TB}/work/triage_prefilter.jsonl")}
PK = {json.load(open(f))["pack_id"]: json.load(open(f)) for f in glob.glob(f"{TB}/work/t1_packs/pack_*.json")}
CEN = json.load(open(f"{TB}/work/census_full.json"))
MAN = json.load(open(f"{TB}/work/census_full_manifest.json"))
E = json.load(open(f"{TB}/work/t1_errata.json"))
EXTRA = {r["atom_id"] for r in json.load(open(f"{TB}/work/t1_extra_review_set.json"))}
KB = "knowledge_base/"

def unit_of(path):
    p = path.split(":")[0]
    m = re.match(r"knowledge_base/domains/([^/]+)", p)
    return f"domains/{m.group(1)}" if m else p[len(KB):]

# ── 1. IE candidates ───────────────────────────────────────────────────────────────────────────────────
ie = [r for r in M if r["final_class"] == "IE_CAND"]
by = collections.defaultdict(list)
for r in ie:
    cat = r["ie_cat"] or ("SPEC_TABLE_HEADER" if r["atom_id"] == "ig34_p0195_a008" else "UNSET")
    by[cat].append(r)
L = ["# T1.4 IE 候选清单 (IE_CAND) — 待用户逐类 ack", "",
     "<!-- chain: E (plans) -->",
     "> 状态: 待用户 ack (T1.4 hard checkpoint); 生成: `scripts/helpers/t14_pkg.py` (2026-11-26) 读 `work/triage_merged.json`",
     "> (`python3 -I .work/10_tier_b_repair/scripts/t1_merge.py` 复跑后与复跑前逐字节相同). 只列 ID / 节 / KB 位置, 不含 PDF 原文.",
     "",
     f"总计 **{len(ie)}** 条. 列: `det` = 确定性支撑 (SPEC_MATCH + section_domain 比对一致); `rev` = T1.3 reviewer 已复核;",
     "`extra` = 在 `t1_extra_review_set.json` (非确定性支撑且未复核, 追加 100% 复核中); `src` = writer / reviewer (覆盖) / pending_user.",
     "",
     "| ie_cat | 条数 | det | rev | extra |", "|---|--:|--:|--:|--:|"]
for c, rs in sorted(by.items(), key=lambda x: -len(x[1])):
    L.append(f"| {c} | {len(rs)} | {sum(r['det_backed'] for r in rs)} | {sum(r['reviewed'] for r in rs)} | {sum(r['atom_id'] in EXTRA for r in rs)} |")
L += ["", "待裁定 (T1.4, 不在本文件内裁): VERSION_MISMATCH 口径 — lane A 23 条 sv20 §1 / lane C 24 条 sv20 (model/05/06 收了 5 列版本) /",
      "lane D pack_032 SE/SJ 23 表行 vs pack_027 口径相反; 不认 → 对应条转 REAL_GAP 或 LOCATE (见 `t1_lane_notes.md`).",
      "`ig34_p0195_a008` reviewer 覆盖 LOCATE→IE_CAND, merge 未取到 ie_cat, 按 reviewer 说明归 SPEC_TABLE_HEADER.", ""]
for c, rs in sorted(by.items(), key=lambda x: -len(x[1])):
    L += [f"## {c} ({len(rs)})", "", "| atom_id | 节 | kb_loc | det | rev | extra | src |", "|---|---|---|:-:|:-:|:-:|---|"]
    for r in sorted(rs, key=lambda r: r["atom_id"]):
        sec = (PRE.get(r["atom_id"], {}).get("section_key") or "").replace("|", "/")
        L.append(f"| {r['atom_id']} | {sec} | {r['kb_loc'] or ''} | {'Y' if r['det_backed'] else ''} | {'Y' if r['reviewed'] else ''} | "
                 f"{'Y' if r['atom_id'] in EXTRA else ''} | {r['src']} |")
    L.append("")
open(f"{TB}/evidence/checkpoints/t1_ie_candidates.md", "w").write("\n".join(L))

# ── 2. batch draft ─────────────────────────────────────────────────────────────────────────────────────
FIX = ("REAL_GAP", "VALUE_DIFF", "RELOCATE", "LOCATE")
U = collections.defaultdict(lambda: {"atoms": collections.Counter(), "files": collections.Counter(), "nolock": 0, "cen_tab": 0,
                                     "cen_rows": 0, "cen_cells": 0, "overlap": 0, "pdf_only": [], "unparse": 0, "unparse_rows": 0, "O": [], "in_pdf_only": 0})
cen_rows = collections.defaultdict(set)     # file -> set of KB line numbers with a cell diff
cen_spans = collections.defaultdict(list)   # file -> [(start, end)] of DIFF tables
for t in CEN["tables"]:
    u = unit_of(t["file"])
    if t["status"] == "UNPARSEABLE":
        U[u]["unparse"] += 1; U[u]["unparse_rows"] += t["n_rows"]
    if t["status"] in ("DIFF", "NO_PDF"):
        U[u]["cen_tab"] += 1
        rows = {x["kb_line"] for x in t.get("diffs", []) if x.get("kb_line")}
        U[u]["cen_rows"] += len(rows); U[u]["cen_cells"] += sum(x["type"] == "CELL" for x in t.get("diffs", []))
        cen_rows[t["file"]] |= rows; cen_spans[t["file"]].append((t["line"], t["line"] + t["n_rows"] + 1))
        U[u]["files"][t["file"][len(KB):]] += 0
dom_rng = [(m["file"], m["lo"], m["hi"]) for m in MAN if m["file"].endswith("examples.md") and m["src"] == "ig34"]
# PDF_ONLY table -> unit of the KB examples.md tables paired with PDF tables within +-1 page (else page range)
for p in CEN["pdf_only"]:
    pg = p["pages"][0]
    near = collections.Counter(unit_of(t["file"]) for t in CEN["tables"] if t.get("pdf_pages") and
                               min(abs(x - pg) for x in t["pdf_pages"]) <= 1 and t["file"].endswith("examples.md"))
    hit = [f for f, lo, hi in dom_rng if lo <= pg <= hi]
    tgt = near.most_common(1)[0][0] if near else (unit_of(hit[-1]) if hit else "(未定)")
    U[tgt]["pdf_only"].append(f"p{pg} Ex{p['ex']} {p['ds']} ({p['n_rows']}行)")
for r in M:
    if r["final_class"] not in FIX:
        continue
    pre = PRE.get(r["atom_id"], {})
    if r["kb_loc"]:
        f = r["kb_loc"].split(":")[0]; src = "kb_loc"
    elif pre.get("primary_unit"):
        f = pre["primary_unit"]; src = "unit"
    else:
        f = (PK[r["pack_id"]]["kb_owned_files"] or ["(未定)"])[0]; src = "pack"
    u = unit_of(f)
    U[u]["atoms"][r["final_class"]] += 1
    if not r["kb_loc"] and pre.get("atom_type") in ("TABLE_ROW", "TABLE_HEADER") and \
            any(str(pre.get("pdf_page")) in map(str, p["pages"]) for p in CEN["pdf_only"]):
        U[u]["in_pdf_only"] += 1      # row/header of a whole-missing PDF table: already counted as PDF_ONLY rows
    if src != "kb_loc":
        U[u]["nolock"] += 1
    else:
        U[u]["files"][f[len(KB):]] += 1
        try:
            ln = int(r["kb_loc"].split(":")[1].split("-")[0])
        except (IndexError, ValueError):
            ln = None
        if r["final_class"] == "VALUE_DIFF" and ln and any(a <= ln <= b for a, b in cen_spans.get(f, [])):
            U[u]["overlap"] += 1
O = {"O1": ["domains/PC", "domains/PP"], "O2": ["domains/SUPPQUAL"], "O3": ["chapters/ch04_general_assumptions.md"],
     "O4": ["domains/ML", "domains/CE", "domains/TA"], "O5": ["chapters/ch03_submitting_data.md"], "O6": ["domains/EG"],
     "O7": ["domains/IS"], "O8": ["domains/AE"], "O9": ["domains/MB"],
     "O10": ["domains/EX", "domains/FA", "domains/TA", "domains/CE", "domains/CP"], "O11": ["domains/AE"],
     "O12": ["chapters/ch04_general_assumptions.md"]}
for o, us in O.items():
    for u in us:
        U[u]["O"].append(o)
rows = []
for u, v in U.items():
    n_at = sum(v["atoms"].values())
    work = n_at + v["cen_rows"] - v["overlap"] - v["in_pdf_only"] + sum(int(re.search(r"\((\d+)行\)", x).group(1)) for x in v["pdf_only"])
    if not (n_at or v["cen_rows"] or v["pdf_only"] or v["O"]):
        continue
    rows.append((u, v, n_at, work))
rows.sort(key=lambda x: -x[3])
B = ["# T1.4 T2 批次表草案 (draft, 待用户定)", "", "<!-- chain: E (plans) -->",
     "> 状态: 草案 (2026-11-26), T1.4 hard checkpoint 时与用户定稿; 生成: `scripts/helpers/t14_pkg.py`.",
     "> 输入: `work/triage_merged.json` (REAL_GAP/VALUE_DIFF/RELOCATE/LOCATE) + `work/census_full.json` (v2 全量 census) + `work/out_of_scope_findings.md` O1-O12.",
     "> 只列位置与计数, 不含 PDF 原文.", "",
     "## 1. 按 KB 单元汇总 (单元 = 域目录或单个 chapter/model 文件; 一批 = 一个单元, 同单元串行)", "",
     "列: 分诊 = REAL_GAP/VALUE_DIFF/RELOCATE/LOCATE 原子数 (无 kb_loc 者按 prefilter `primary_unit`, 再退 pack `kb_owned_files`, 计入 `无loc`);",
     "census = v2 DIFF/NO_PDF 表数 / 有 diff 的 KB 行数 (与落在同表的 VALUE_DIFF 原子去重 = `重叠`); PDF_ONLY = KB 缺整表;",
     "不可机检 = 该单元 UNPARSEABLE 表数 (行数) — 本批触碰到才须 reviewer 人工逐格 (G-TB4);",
     "工作量 = 分诊 + census 行 − 重叠 (VALUE_DIFF 落在 census DIFF 表内) − 分诊已含 (无 kb_loc 的表行/表头原子落在 PDF_ONLY 表页) + PDF_ONLY 行.", "",
     "| # | 单元 | 分诊 (RG/VD/RL/LC) | 无loc | census 表/行/格 | 重叠 | PDF_ONLY (其中分诊已含) | 不可机检 | O# | 工作量 |",
     "|--:|---|---|--:|---|--:|---|---|---|--:|"]
T = collections.Counter()
for i, (u, v, n_at, w) in enumerate(rows, 1):
    a = v["atoms"]
    B.append(f"| {i} | {u} | {n_at} ({a['REAL_GAP']}/{a['VALUE_DIFF']}/{a['RELOCATE']}/{a['LOCATE']}) | {v['nolock']} | "
             f"{v['cen_tab']}/{v['cen_rows']}/{v['cen_cells']} | {v['overlap']} | {'; '.join(v['pdf_only'])}{' (−' + str(v['in_pdf_only']) + ')' if v['in_pdf_only'] else ''} | "
             f"{v['unparse']} ({v['unparse_rows']}) | {','.join(v['O'])} | {w} |")
    T["atoms"] += n_at; T["cen_rows"] += v["cen_rows"]; T["overlap"] += v["overlap"]; T["work"] += w; T["units"] += 1
    T["cen_cells"] += v["cen_cells"]; T["pdf_only_rows"] += w - n_at - v["cen_rows"] + v["overlap"] + v["in_pdf_only"]
    T["in_pdf_only"] += v["in_pdf_only"]
json.dump(dict(T), open(f"{TB}/work/scratch/census_fix/batch_totals.json", "w"))
B += ["", f"合计: 单元 {T['units']}; 分诊原子 {T['atoms']}; census 有 diff 行 {T['cen_rows']} (格 {T['cen_cells']}); 重叠 {T['overlap']}; "
      f"PDF_ONLY 行 {T['pdf_only_rows']} (其中 {T['in_pdf_only']} 行已作分诊原子计入, 已扣); 工作量 {T['work']}.", ""]
B.append("## 2. 单元内文件分布 (有 kb_loc 的分诊原子 / census DIFF 表所在文件)")
B.append("")
for u, v, n_at, w in rows:
    fs = ", ".join(f"{f} ({c})" for f, c in sorted(v["files"].items()))
    if fs:
        B.append(f"- **{u}**: {fs}")
import os
tail = f"{TB}/work/scratch/census_fix/batch_tail.md"     # hand-written §3-§5 (numbers refer to §1 as of 2026-11-26)
open(f"{TB}/evidence/checkpoints/t1_batch_draft.md", "w").write("\n".join(B) + "\n" + (open(tail).read() if os.path.exists(tail) else ""))
print(dict(T))
