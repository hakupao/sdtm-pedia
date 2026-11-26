"""T1.4 apply → T2 package. Reads work/triage_merged.json (after t1_rulings.json) + work/census_full.json; writes
  evidence/checkpoints/t1_ie_final.md, t1_r1_r4_resolution.md, t1_r2_scan.md, t2_batch_table.md, work/t2_batches/<batch>.json.
IDs / locations / counts only, no PDF text. t14_pkg.py (T1.4 package) is NOT rerun: it would overwrite the acked T1.4 files.
Run from repo root: python3 -I .work/10_tier_b_repair/scripts/helpers/t2_pkg.py"""
import collections, glob, json, os, re
TB = "/Volumes/DevSSD/Project/sdtm-pedia/.work/10_tier_b_repair"
K = "knowledge_base/"
M = json.load(open(f"{TB}/work/triage_merged.json"))
MB = {r["atom_id"]: r for r in M}
PRE = {json.loads(l)["atom_id"]: json.loads(l) for l in open(f"{TB}/work/triage_prefilter.jsonl")}
PRE0 = {r["atom_id"]: r for r in json.load(open(f"{TB}/work/scratch/t14_apply/triage_merged.pre_rulings.json"))}
A = {json.loads(l)["atom_id"]: json.loads(l) for l in open(f"{TB}/work/pdf_atoms.jsonl")}
PK = {json.load(open(f))["pack_id"]: json.load(open(f)) for f in glob.glob(f"{TB}/work/t1_packs/pack_*.json")}
RU = json.load(open(f"{TB}/work/t1_rulings.json"))["atoms"]
CEN = json.load(open(f"{TB}/work/census_full.json"))
MAN = json.load(open(f"{TB}/work/census_full_manifest.json"))
W = {}
for L in "ABCD":
    for l in open(f"{TB}/work/triage/lane_{L}.jsonl"):
        r = json.loads(l); W[r["atom_id"]] = r
CK = f"{TB}/evidence/checkpoints"
HDR = ["<!-- chain: E (plans) -->", "> 生成: `scripts/helpers/t2_pkg.py` (2026-11-26) 读 `work/triage_merged.json` (含 `work/t1_rulings.json`); 只列 ID / 位置 / 计数, 不含 PDF 原文.", ""]

def page(a):
    return (A.get(a) or {}).get("page") or W[a]["evidence"].get("pdf_page")
def sec(a):
    return (PRE.get(a, {}).get("section_key") or (A.get(a) or {}).get("parent_section") or "").replace("|", "/")
def unit_of(path):
    p = path.split(":")[0]
    m = re.match(r"knowledge_base/domains/([^/]+)", p)
    return f"domains/{m.group(1)}" if m else p[len(K):]

# ── 1. final IE list ───────────────────────────────────────────────────────────────────────────────────
ie = [r for r in M if r["final_class"] == "IE"]
by = collections.defaultdict(list)
for r in ie:
    by[r["ie_cat"]].append(r)
L = ["# T1 最终 IE 清单 (用户 ack: t1_user_ack.md R1/R4)", ""] + HDR + [
    f"总计 **{len(ie)}** 条 (T1.4 前 IE_CAND 587 − R1 转 REAL_GAP 25 − R4 转 PRESENT 49). 标签按 whitelist 先例统一 (见 `t1_r1_r4_resolution.md` §3).",
    "`R4-blocked` = 用户裁 PRESENT 但非逐字, 暂留 IE 待用户 (见 `t1_r1_r4_resolution.md` §2).", "",
    "| ie_cat | 条数 |", "|---|--:|"] + [f"| {c} | {len(v)} |" for c, v in sorted(by.items(), key=lambda x: -len(x[1]))] + [""]
for c, rs in sorted(by.items(), key=lambda x: -len(x[1])):
    L += [f"## {c} ({len(rs)})", "", "| atom_id | 节 | kb_loc | ruling |", "|---|---|---|---|"]
    for r in sorted(rs, key=lambda r: r["atom_id"]):
        L.append(f"| {r['atom_id']} | {sec(r['atom_id'])} | {r['kb_loc'] or ''} | {r['src'].replace('ruling:', '') if r['src'].startswith('ruling:') else ''} |")
    L.append("")
open(f"{CK}/t1_ie_final.md", "w").write("\n".join(L))

# ── 2. R1 / R4 resolution list ─────────────────────────────────────────────────────────────────────────
def rows(rule_prefix):
    return sorted(a for a, e in RU.items() if e["rule"].startswith(rule_prefix))
L = ["# T1.4 裁定落地: R1 / R4 逐条", ""] + HDR + [
    "## 1. R1 — VERSION_MISMATCH 70 条", "",
    "规则: sv20 变量表行且 model/ 有 5 列精简版 (#/name/label/type/role 与 PDF 一致, 脚本逐行断言) → IE; sv20 §1 Introduction 句 → REAL_GAP (补进 model/01, 在 §2 前新增 §1);",
    "TD 句 (sv20 §5.1.4.2) → REAL_GAP (按归属补进 model/05 TD 节). 70 = 表行 45 + §1 22 + TD 3; 零散条目 (TOC / 列头) 不在这 70 条内, 按 §3 的先例归类.",
    "ack 里写的 '§1 17 条 / TD 2 句' 是 T1.3b 追加复核子集的数, 全集为 §1 22 / TD 3 (同一规则).", "",
    "| atom_id | 节 | 原 kb_loc | 裁定 | 修复目标 |", "|---|---|---|---|---|"]
for a in rows("R1"):
    e = RU[a]
    L.append(f"| {a} | {sec(a)} | {PRE0[a]['kb_loc'] or ''} | {e['to']} ({e['rule']}) | {e.get('target', '')} |")
sv_sib = sorted(a for a, r in MB.items() if a.startswith("sv20") and r["final_class"] in ("PRESENT", "REAL_GAP", "REWRITE_OK", "VALUE_DIFF"))
L += ["", f"### 1b. 反向口径兄弟 (lane notes: pack_027 sv20 §2 / sv20 §6.6) — {len(sv_sib)} 条, **0 条改类**", "",
      "判据: 是变量表行且 5 列版在 model/ → IE; 是 prose → 保持分诊类. 这些全是 prose (脚本断言: 非 IE 的 sv20 原子无 TABLE_ROW/TABLE_HEADER);",
      "§6.6 的表行 sv20_p0068_a023 已在上表 (IE). 只给 null kb_loc 的补了修复目标 (TARGET).", "",
      "| atom_id | 节 | atom_type | 类 | 目标 |", "|---|---|---|---|---|"]
for a in sv_sib:
    L.append(f"| {a} | {sec(a)} | {A[a]['atom_type']} | {MB[a]['final_class']} | {MB[a].get('target') or MB[a]['kb_loc'] or ''} |")
L += ["", "另: 06 whitelist 里 sv20 §1 的 `sv20_p0004_a016` 已是 IE (VERSION_MISMATCH, 不在本项目范围), 按 R1 它也属 §1 引言 → **待用户**: 是否一并补进 model/01.", "",
      "## 2. R4 — IE 整体 ack; 逐字在 KB 的转 PRESENT", "",
      "判据: `fp_match.norm(verbatim)` 是 kb_loc **整个文件** `norm()` 的子串 (同 T3.2 指纹复验口径).",
      "- R4-present 40: §3.2.1 xpt 文件名 (ch03 Location 格), T1.3b 追加复核所列;",
      "- R4-present-sibling 9: 同表同型的 xpt 文件名, T1.3 已复核故不在 44 内; 同口径一并转 (统一标签);",
      "- **R4-blocked 5**: 4 条数据集标题行 (T1.3b 说逐字一致) + 同型 AE 1 条. 实际 KB spec.md 顶部为 `> Class: … | Structure: …`, 缺 'xx.xpt,' 与 ', Tabulation' →",
      "  非逐字, PRESENT 过不了 T3.2 指纹复验; **暂留 IE (REDUNDANT_WITH_SPEC), 待用户** (同型 ML 标题行 ig34_p0121_a005 现为 REWRITE_OK, 已标 t2_recheck).", "",
      "| atom_id | kb_loc | 裁定 |", "|---|---|---|"]
for a in rows("R4-present") + rows("R4-blocked"):
    L.append(f"| {a} | {PRE0[a]['kb_loc'] or ''} | {RU[a]['to']} ({RU[a]['rule']}) |")
L += ["", "## 3. IE 标签统一 (whitelist 先例)", "",
      "- CT 星号脚注 → REDUNDANT_WITH_SPEC (whitelist 同文 REDUNDANT_WITH_SPEC 13 : EDITORIAL_META 5, 取多数);",
      "- sv20 目录条目 → VERSION_MISMATCH (同页 sv20_p0002_a001/a004/a006/a010/a021 先例);",
      "- sv20 变量表列头 → VERSION_MISMATCH (whitelist sv20 TABLE_HEADER: VERSION_MISMATCH 13 + sdtm_v2_superseded 4; 'structural' 6 为结构标题非列头);",
      "- ig34_p0195_a008 无 ie_cat → SPEC_TABLE_HEADER (reviewer 说明).", "",
      "| atom_id | 原 → 新 |", "|---|---|"]
for a in rows("R4-relabel"):
    L.append(f"| {a} | {RU[a]['note'].split(' (')[0]} |")
L += ["", "## 4. 修复目标补全 (kb_loc 为空 / ledger 目标错; 依据 lane notes, T1.3 已核)", "",
      "| atom_id | 类 | 目标 | 依据 |", "|---|---|---|---|"]
for a in rows("TARGET") + rows("LOCATE"):
    L.append(f"| {a} | {RU[a]['to']} | {RU[a]['target']} | {RU[a]['note']} |")
L.append("")
open(f"{CK}/t1_r1_r4_resolution.md", "w").write("\n".join(L))

# ── 3. R2 scan of all final REWRITE_OK (pre-ruling) ────────────────────────────────────────────────────
KEEP = {"ig34_p0010_a002": "KB 多一个 'has' (增词非丢失, 意同)", "ig34_p0010_a015": "URL 前加 'the NCI website' (增词)",
        "sv20_p0005_a004": "T1.3 reviewer: 信息点全在 model/01:102", "ig34_p0042_a026": "本原子在; :879 值差另记 O12"}
L = ["# T1.4 R2 扫描: 全部 REWRITE_OK 是否属 '丢短语但别处有'", ""] + HDR + [
    "R2 (用户): 改写丢失短语, 即使同节上下文 / 同表行已有 → **REAL_GAP, 补回原文**.",
    "判据: writer/reviewer 理由**承认** kb_loc 处缺某片段, 并用另一行 / 另一处 / 隐含 / 约定来开脱 →",
    "片段是内容 (限定词 / 计数 / 术语 / 交叉引用) → FLIP (REAL_GAP); 只是标签、结构或 C02 型多行映射 → RECHECK (`t2_recheck=true`, T2 reviewer 回 PDF 定);",
    "理由逐信息点给到 KB 行、未承认缺失 → KEEP. 97 条逐条人工判 (关键词 grep 只作辅助).",
    "**注**: 标定集 C02 自身 (ig34_p0043_a012) 用 :894 覆盖 :898 缺的 'observation', 与 R2 有张力 → 列 RECHECK, 不在此裁; 请用户确认 C02 是否仍作 REWRITE_OK 标杆.", "",
    "| # | atom_id | kb_loc | 判 | 理由 |", "|--:|---|---|---|---|"]
rw = sorted([a for a, r in PRE0.items() if r["final_class"] == "REWRITE_OK"])
cnt = collections.Counter()
for i, a in enumerate(rw, 1):
    e = RU.get(a)
    call = "FLIP" if e and e["rule"] == "R2-flip" else "RECHECK" if e and e["rule"] == "R2-recheck" else "KEEP"
    cnt[call] += 1
    why = e["note"] if e else KEEP.get(a, "信息点逐一映射到 KB 行, 未承认缺失" if not re.search(r"CRF|合并", W[a]["evidence"]["reason"])
                                        else "CRF / 表格多行合并为单行, 各值与对应关系在")
    L.append(f"| {i} | {a} | {PRE0[a]['kb_loc'] or ''} | {call} | {why} |")
L += ["", f"合计: {len(rw)} 条 → FLIP {cnt['FLIP']} / RECHECK {cnt['RECHECK']} / KEEP {cnt['KEEP']}. 另 4 条 pending_user (ig34_p0010_a023 / p0011_a020 / p0012_a005 / p0056_a006) 按 R2 定为 REAL_GAP (R2-ack).", ""]
open(f"{CK}/t1_r2_scan.md", "w").write("\n".join(L))

# ── 4. batches ─────────────────────────────────────────────────────────────────────────────────────────
FIX = ("REAL_GAP", "VALUE_DIFF", "RELOCATE")
U = collections.defaultdict(lambda: {"atoms": [], "recheck": [], "diff_tables": [], "pdf_only": [], "pdf_unparsed": [], "unparseable": [],
                                     "O": [], "overlap": 0, "in_pdf_only": 0, "pages": set(), "files": set()})
cen_spans = collections.defaultdict(list)
for t in CEN["tables"]:
    u = unit_of(t["file"]); U[u]["files"].add(t["file"])
    if t["status"] == "UNPARSEABLE":
        U[u]["unparseable"].append({"file": t["file"], "line": t["line"], "n_rows": t["n_rows"], "ex": t["ex"], "ds": t["ds"]})
    if t["status"] in ("DIFF", "NO_PDF"):
        d = t.get("diffs", [])
        U[u]["diff_tables"].append({"file": t["file"], "line": t["line"], "status": t["status"], "ex": t["ex"], "ds": t["ds"],
                                    "pdf_pages": t.get("pdf_pages"), "pdf_ex": t.get("pdf_ex"), "kb_duplicate": t.get("kb_duplicate"),
                                    "n_diffs": len(d), "n_cell": sum(x["type"] == "CELL" for x in d),
                                    "diff_types": dict(collections.Counter(x["type"] for x in d)),
                                    "kb_lines_with_diff": sorted({x["kb_line"] for x in d if x.get("kb_line")})})
        U[u]["pages"] |= set(t.get("pdf_pages") or [])
        cen_spans[t["file"]].append((t["line"], t["line"] + t["n_rows"] + 1))
dom_rng = [(m["file"], m["lo"], m["hi"]) for m in MAN if m["file"].endswith("examples.md") and m["src"] == "ig34"]
for p in CEN["pdf_only"]:                       # same heuristic as t14_pkg (draft reviewed at T1.4)
    pg = p["pages"][0]
    near = collections.Counter(unit_of(t["file"]) for t in CEN["tables"] if t.get("pdf_pages") and
                               min(abs(x - pg) for x in t["pdf_pages"]) <= 1 and t["file"].endswith("examples.md"))
    hit = [f for f, lo, hi in dom_rng if lo <= pg <= hi]
    tgt = near.most_common(1)[0][0] if near else unit_of(hit[-1])
    U[tgt]["pdf_only"].append(p); U[tgt]["pages"] |= set(p["pages"])
for p in CEN["pdf_unparsed"]:
    u = f"domains/{p['ds'].split('.')[0].upper()}"
    assert os.path.isdir(f"/Volumes/DevSSD/Project/sdtm-pedia/{K}{u}"), u
    U[u]["pdf_unparsed"].append(p); U[u]["pages"] |= set(p["pages"])
pdf_only_pages = {str(x) for p in CEN["pdf_only"] for x in p["pages"]}
for r in M:
    a = r["atom_id"]
    if r["final_class"] not in FIX and not r.get("t2_recheck"):
        continue
    pre = PRE.get(a, {})
    f = r.get("target") or r["kb_loc"] or pre.get("primary_unit") or (PK[r["pack_id"]]["kb_owned_files"] or ["?"])[0]
    u = unit_of(f)
    if a.startswith("sv20"):
        assert u.startswith("model/"), (a, u)
    elif r["final_class"] != "RELOCATE":
        assert not u.startswith("model/"), (a, u)
    item = {"atom_id": a, "class": r["final_class"], "page": page(a), "src": a.split("_")[0] if a.startswith(("ig34", "sv20")) else "ig34",
            "atom_type": (A.get(a) or {}).get("atom_type", "MANUAL"), "section": sec(a), "kb_loc": r["kb_loc"], "target": r.get("target"),
            "pdf_typo_suspect": r["pdf_typo_suspect"], "triage_src": r["src"],
            "triage_ref": f"work/triage/lane_{r['lane']}.jsonl (+ review_lane_{r['lane']}.jsonl; gitignored, 本地读)"}
    if r.get("ruling_note"): item["ruling_note"] = r["ruling_note"]
    U[u]["pages"].add(page(a))
    if r.get("t2_recheck") and r["final_class"] not in FIX:
        U[u]["recheck"].append(item); continue
    U[u]["atoms"].append(item)
    if not (r.get("target") or r["kb_loc"]) and item["atom_type"] in ("TABLE_ROW", "TABLE_HEADER") and str(pre.get("pdf_page")) in pdf_only_pages:
        U[u]["in_pdf_only"] += 1
    if r["final_class"] == "VALUE_DIFF" and r["kb_loc"]:
        try:
            ln = int(r["kb_loc"].split(":")[1].split("-")[0])
        except (IndexError, ValueError):
            ln = None
        if ln and any(x <= ln <= y for x, y in cen_spans.get(r["kb_loc"].split(":")[0], [])):
            U[u]["overlap"] += 1
OM = {"O1": ["domains/PC", "domains/PP"], "O2": ["domains/SUPPQUAL"], "O3": ["chapters/ch04_general_assumptions.md"],
      "O4": ["domains/ML", "domains/CE", "domains/TA"], "O5": ["chapters/ch03_submitting_data.md"], "O6": ["domains/EG"],
      "O7": ["domains/IS"], "O8": ["domains/AE"], "O9": ["domains/MB"],
      "O10": ["domains/EX", "domains/FA", "domains/TA", "domains/CE", "domains/CP"], "O11": ["domains/AE"],
      "O12": ["chapters/ch04_general_assumptions.md"]}
for o, us in OM.items():
    for u in us:
        U[u]["O"].append(o)
NOTE = {
    "domains/PC": ["Issue 5 主节 §6.3.5.9.3; PC Ex1 整表缺 (p270-271 PDF_ONLY)", "p277 PP 表两份副本 (PP/examples.md:112 与 PC/assumptions.md:86): 两份都按 PDF 修, 都不删 (去重未裁, 待用户)",
                   "MANUAL_02: PDF p277 文字与 p278 表自相矛盾 → PDF_TYPO 候选, KB 不改, 登记"],
    "domains/PP": ["MANUAL_01: PP Ex1 用了 Ex3 数据 → 按 p273 重建 Ex1 表", "p274 Ex2 pp.xpt 垂直居中, census 不可机检 → reviewer 人工逐格并留表"],
    "domains/CP": ["Ex2-8 七张 cp.xpt KB 只占位 (PDF_ONLY)", "Ex1a 行 2/4/6 PRESENT 的前提是 KB 已重排改名的列; 修表头 ig34_p0210_a002 时整表 (表头 + 全部行) 同步重排, 不能只改表头", "Ex1b 行 1 列错位 (O10)"],
    "domains/MB": ["MB/examples.md 两份 Ex1-3 (行 1-170 / 171-400) 各有不同错 (O9): 两份都按 PDF 修, 都不删 (去重未裁, 待用户)",
                   "Ex3 di.xpt + relrec.xpt 缺 (PDF_ONLY p263): 补在 MB/examples.md Ex3 下 (DI 无 examples.md)"],
    "domains/TR": ["Ex2 PDF 跳 Row 12 → 行号 diff 是 PDF_TYPO 候选 (不改 KB 行号, 登记); 但其中 9 条另有真 KB 错 (VISIT/TRDTC 列错位, 多填日期, TRREASND) 必须修", "Ex3 TRMETHOD/TRNAM 列互换"],
    "domains/LB": ["§6.3.5.1 (28 原子, 原 LOCATE) → LB/assumptions.md 顶部 (标题行后) 新增 '## §6.3.5.1 …' 节, 结构仿 NV/assumptions.md §6.3.7.1;",
                   "通用规格表 p195-196 整表补 (含不在分诊里的 ledger EQUIVALENT/MISPLACED 行, 否则表不完整; 这些行按 G-TB6 逐行指到 PDF 页)", "ig34_p0195_a008 (该表列头) 是 IE, 但插表需要表头 = 结构行"],
    "domains/FA": ["RELOCATE 3: 本批独占; ch02_fundamentals.md:219,227 与 model/02_observation_classes.md:188-190 **只允许删除这些行** (移到 FA/assumptions.md:62 / :64);",
                   "本批与 B-ch02 / B-model02 串行 (同文件)"],
    "chapters/ch04_general_assumptions.md": ["一个文件一批 (PLAN 原拆 ch04a/ch04b 串行, 现合并; 若 writer 上下文不够再按 §4.1-4.3 / §4.4-4.5 拆)", "33 张不可机检表: 触碰才人工逐格"],
    "model/01_concepts_and_terms.md": ["R1: sv20 §1 Introduction 22 句 → 在 '## 2.1' 前新增 §1 (PDF 原标题与子标题), 逐字"],
    "model/05_study_level_data.md": ["R1: TD 3 句 → '### Trial Disease Assessments (TD)' 节"],
    "model/06_relationship_datasets.md": ["§6.6 APRELSUB 3 句 → :129 节"],
    "domains/AE": ["O11: AE/assumptions.md:39 KB 把 '…/etc.' 扩写成 6 项 (超出 PDF): 报告, 不删 (删除需用户裁)"],
    "domains/SC": ["p342 Ex2 sc.xpt 垂直居中 (PDF_UNPARSED) + SC/examples.md:34 NO_PDF → 人工逐格"],
}
SERIAL = {"domains/FA": ["chapters/ch02_fundamentals.md", "model/02_observation_classes.md"]}
units = []
for u, v in U.items():
    pdf_only_rows = sum(p["n_rows"] for p in v["pdf_only"])
    cen_rows = sum(len(t["kb_lines_with_diff"]) for t in v["diff_tables"])
    work = len(v["atoms"]) + cen_rows - v["overlap"] - v["in_pdf_only"] + pdf_only_rows
    if not (v["atoms"] or v["recheck"] or cen_rows or v["pdf_only"] or v["pdf_unparsed"] or v["O"]
            or any(t["status"] == "NO_PDF" for t in v["diff_tables"])):
        continue
    units.append((u, v, work, cen_rows, pdf_only_rows))
def bid(u):
    return {"domains/PC": "B-PCPP", "domains/PP": "B-PCPP"}.get(u) or "B-" + (u.split("/")[1] if u.startswith("domains/") else
            re.sub(r"_.*", "", u.split("/")[1]) if u.startswith("chapters/") else "model" + u.split("/")[1][:2])
B = collections.OrderedDict()
for u, v, w, cr, pr in units:
    B.setdefault(bid(u), []).append((u, v, w, cr, pr))
order = ["B-PCPP"] + sorted([b for b in B if b != "B-PCPP"], key=lambda b: -sum(x[2] for x in B[b]))
os.makedirs(f"{TB}/work/t2_batches", exist_ok=True)
for f in glob.glob(f"{TB}/work/t2_batches/*.json"):
    os.remove(f)
unit_bid = {u: b for b, xs in B.items() for u, *_ in xs}
T = collections.Counter(); TL = []; DET = []
for i, b in enumerate(order, 1):
    xs = B[b]
    kb_files = sorted({f for u, v, *_ in xs for f in v["files"]} | {(a["target"] or a["kb_loc"] or "").split(":")[0] for u, v, *_ in xs for a in v["atoms"] + v["recheck"]} - {""})
    for u, *_ in xs:
        if u.endswith(".md"):
            kb_files = sorted(set(kb_files) | {K + u})
    atoms = [a for u, v, *_ in xs for a in v["atoms"]]
    rech = [a for u, v, *_ in xs for a in v["recheck"]]
    srcdel = []
    if any(u == "domains/FA" for u, *_ in xs):
        def anc(f, ln):     # first 6 words of the KB line (KB text, not PDF) so the writer can re-locate after other batches shift lines
            return " ".join(open(f"/Volumes/DevSSD/Project/sdtm-pedia/{f}").read().split("\n")[ln - 1].split()[:6])
        srcdel = [{"file": K + "chapters/ch02_fundamentals.md", "lines_at_base": [219, 227], "atoms": ["ig34_p0363_a014", "ig34_p0364_a003"]},
                  {"file": K + "model/02_observation_classes.md", "lines_at_base": [188, 189, 190], "atoms": ["ig34_p0364_a011"]}]
        for x in srcdel:
            x["anchors"] = [anc(x["file"], n) for n in x["lines_at_base"]]
            x["line_basis"] = "行号 = 本 JSON 生成时 (base dfa9eee + 未改 KB); 若同文件的批已先跑, 按 anchors 内容重新定位; 只删这些行"
    serial = sorted({unit_bid[s] for u, *_ in xs for s in SERIAL.get(u, []) if s in unit_bid} |
                    {"B-FA" for u, *_ in xs if u in SERIAL.get("domains/FA", []) and "domains/FA" in unit_bid})
    cls = collections.Counter(a["class"] for a in atoms)
    w = sum(x[2] for x in xs)
    pages = sorted({p for u, v, *_ in xs for p in v["pages"] if p}, key=int)
    rng = sorted({(m["file"], m["src"], m["lo"], m["hi"]) for m in MAN if m["file"] in kb_files})
    J = {"batch_id": b, "order": i, "units": [u for u, *_ in xs], "kb_files": kb_files, "delete_only_source_lines": srcdel, "serial_with": serial,
         "workload": w, "counts": {"fix_atoms": len(atoms), **cls, "t2_recheck": len(rech),
                                   "census_diff_tables": sum(len(v["diff_tables"]) for u, v, *_ in xs),
                                   "census_kb_rows": sum(x[3] for x in xs), "pdf_only_tables": sum(len(v["pdf_only"]) for u, v, *_ in xs),
                                   "pdf_only_rows": sum(x[4] for x in xs), "unparseable_tables": sum(len(v["unparseable"]) for u, v, *_ in xs)},
         "pdf_pages": pages, "pdf_ranges": [{"file": f, "src": s, "lo": lo, "hi": hi} for f, s, lo, hi in rng],
         "atoms": sorted(atoms, key=lambda a: (a["kb_loc"] or a["target"] or "", a["atom_id"])), "t2_recheck": rech,
         "census": {"source": "work/census_full.json (v2)", "diff_tables": [t for u, v, *_ in xs for t in v["diff_tables"]],
                    "pdf_only": [p for u, v, *_ in xs for p in v["pdf_only"]], "pdf_unparsed": [p for u, v, *_ in xs for p in v["pdf_unparsed"]],
                    "unparseable_kb_tables_hand_check_if_touched": [t for u, v, *_ in xs for t in v["unparseable"]]},
         "out_of_scope": sorted({o for u, v, *_ in xs for o in v["O"]}, key=lambda o: int(o[1:])),
         "notes": [n for u, *_ in xs for n in NOTE.get(u, [])]}
    json.dump(J, open(f"{TB}/work/t2_batches/{b}.json", "w"), ensure_ascii=False, indent=1)
    T["batches"] += 1; T["work"] += w; T["atoms"] += len(atoms); T["recheck"] += len(rech)
    T["cen_rows"] += J["counts"]["census_kb_rows"]; T["pdf_only_rows"] += J["counts"]["pdf_only_rows"]
    po = "; ".join("p%s Ex%s %s (%s行)" % (p["pages"][0], p["ex"], p["ds"], p["n_rows"]) for p in J["census"]["pdf_only"])
    pu = "; ".join("p%s %s" % (p["pages"][0], p["ds"]) for p in J["census"]["pdf_unparsed"])
    DET.append(f"### {i}. {b}\n- 原子: " + (", ".join(f"{a['atom_id']}({a['class'][:2]})" for a in J["atoms"]) or "—") +
               ("\n- t2_recheck: " + ", ".join(a["atom_id"] for a in rech) if rech else "") +
               "\n- census DIFF/NO_PDF 表: " + (", ".join(f"{t['file'][len(K):]}:{t['line']}" for t in J["census"]["diff_tables"]) or "—") +
               "\n- 不可机检 (触碰才人工): " + (", ".join(f"{t['file'][len(K):]}:{t['line']}" for t in J["census"]["unparseable_kb_tables_hand_check_if_touched"]) or "—") +
               f"\n- PDF 页: {', '.join(map(str, pages)) or '—'}")
    TL.append(f"| {i} | {b} | {', '.join(J['units'])} | {len(atoms)} ({cls['REAL_GAP']}/{cls['VALUE_DIFF']}/{cls['RELOCATE']}) | {len(rech)} | "
              f"{J['counts']['census_diff_tables']}/{J['counts']['census_kb_rows']} | "
              f"{po} | {pu} | "
              f"{J['counts']['unparseable_tables']} | {','.join(J['out_of_scope'])} | {', '.join(J['serial_with'])} | {w} |")
tot_fix = sum(1 for r in M if r["final_class"] in FIX)
assert T["atoms"] == tot_fix, (T["atoms"], tot_fix)
L = ["# T2 批次表 v1.0", ""] + HDR + [
    "> 状态: **v1.0** (2026-11-26, T1.4 裁定落地后). 机器可读: `work/t2_batches/<batch>.json` (含原子清单 / census 引用 / 页码 / 串行约束).",
    "> 规则: 一批 = 一个 KB 单元 (域目录或单个 chapter/model 文件); 例外 B-PCPP = domains/PC + domains/PP (Issue 5, PLAN §6 首批 hard).",
    "> 排序: B-PCPP 第一, 其余按工作量降序. 同文件绝不并行; `串行` 列 = 因 RELOCATE 跨单元必须与之串行的批.", "",
    "列: 分诊 = REAL_GAP/VALUE_DIFF/RELOCATE 原子 (RG/VD/RL); recheck = R2 待 T2 reviewer 回 PDF 定的 REWRITE_OK; census = DIFF/NO_PDF 表数 / 有 diff 的 KB 行数;",
    "PDF_ONLY = KB 缺整表; PDF_UNPARSED = PDF 侧不可机检 (人工逐格); 不可机检 = KB 侧 UNPARSEABLE 表数 (触碰才人工, G-TB4);",
    "工作量 = 分诊 + census 行 − 重叠 (VALUE_DIFF 落在 census DIFF 表) − 分诊已含 (无 loc 表行落在 PDF_ONLY 页) + PDF_ONLY 行.", "",
    "## LOCATE §6.3.5.1 (28) 的决定",
    "", "判据: (1) `ls knowledge_base/domains/` 无 §6.3.5.1 的通用文件 (C11); (2) IG 通用规格节的先例宿主 = 该组代表域的 assumptions.md 顶部 (NV/assumptions.md 承载 §6.3.7 概述 + §6.3.7.1);",
    "(3) §6.3.5.1 名为 'Generic Specimen-based **Lab** Findings', LB 是该组通用实验室域, T1.3 reviewer 已把同节列头 ig34_p0195_a008 定位到 LB/assumptions.md:1 →",
    "**目标 = `domains/LB/assumptions.md` 顶部新增 §6.3.5.1 节**; 28 条 LOCATE 转 REAL_GAP (rule LOCATE-LB), 归 B-LB. NV 先例只有 prose, 本节 21 条是通用规格表行 → 整张通用表一并补.", "",
    "## 批次", "",
    "| # | 批 | 单元 | 分诊 (RG/VD/RL) | recheck | census 表/行 | PDF_ONLY | PDF_UNPARSED | 不可机检 | O# | 串行 | 工作量 |",
    "|--:|---|---|---|--:|---|---|---|--:|---|---|--:|"] + TL + [
    "", f"合计: **{T['batches']} 批**; 分诊原子 {T['atoms']} (= 全部 REAL_GAP+VALUE_DIFF+RELOCATE); recheck {T['recheck']}; census 有 diff 行 {T['cen_rows']}; PDF_ONLY 行 {T['pdf_only_rows']}; 工作量 {T['work']}.",
    "", "## 每批明细 (ID / 位置; 完整字段见 JSON)", ""] + DET + [
    "", "## 待用户",
    f"- 批数 {T['batches']} (一单元一批) 远多于 PLAN §6/§7 的 16-17 批: 每批 3 次 subagent 调用 → ~{3 * T['batches']} 次 (PLAN v1.1 估 48-51). 建议: 工作量 < 10 的小域按 ≤8 目录装箱合批 (PLAN §6 原规则), 需用户定.",
    "- 重复副本 (MB 两份 Ex1-3; p277 PP 表两份): 本表默认两份都修、都不删; 是否去重需用户裁.",
    "- R4-blocked 5 条标题行 + ML 标题行 recheck: 见 `t1_r1_r4_resolution.md` §2.", ""]
open(f"{CK}/t2_batch_table.md", "w").write("\n".join(L))
print(dict(T), "fix", tot_fix)
print(collections.Counter(r["final_class"] for r in M))
