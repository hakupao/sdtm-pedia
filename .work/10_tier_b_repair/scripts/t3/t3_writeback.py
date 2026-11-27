#!/usr/bin/env python3
"""T3.1 ledger write-back (working copy only) -> work/coverage_ledger.wc.jsonl.
Input is always the frozen backup work/coverage_ledger.wc.pre_t3.jsonl (created on first run), so re-runs are idempotent.
Allowed set = triage_merged.json atoms ∪ work/t3_t2s_atoms.jsonl ∪ t3_errata keys (主控 C2). Per atom, first rule:
  1 S1 errata (work/t3_errata.json atom_err)           -> ATOM_ERR (R1) / PDF_TYPO (R2)
  2 triage FIGURE                                      -> FIGURE_DEFERRED
  2b T4 R2L list work/t4_r2l_relabel.json, to = IE    -> INTENTIONAL_EXCLUDE (VERSION_MISMATCH; 主人 2026-11-27 问题 1 / 2 = A;
     before K3b / live-hit). Its registry_ptr only appends registry ids to the evidence of atoms that stay PDF_TYPO.
  3 pending_user concluded '残留'                       -> residual (verdict kept)
  4 norm(verbatim) ⊂ norm(target KB file) right now    -> EXACT, also over triage IE (主控 C5; original IE ack kept in evidence)
    (targets: fp_match targets ∪ triage kb_loc/target ∪ S1 remap ∪ writer kb_file)
  5 triage IE (must be listed in t1_ie_final.md)       -> INTENTIONAL_EXCLUDE
  5b work/t3_c1_manual.json (主控 C1; cited KB line asserted ⊂ PDF page)  -> EQUIVALENT
  6 writer row note/SKIPPED_PDF_TYPO names T-n found in the PDF_TYPO registry -> PDF_TYPO (registry '照录' -> ATOM_ERR)
  7 triage PRESENT/REWRITE_OK agreed by two agents (reviewed or ruling src) AND the T1-judged kb_loc line (302ec4c) still
    exists in HEAD, or was reworked by a PASS batch's fix row in the same HEAD table block -> EQUIVALENT
    or writer fix row (INSERTED/REPLACED/TABLE_REBUILT/MOVED/RELOCATE/R3_RESTORED) + review PASS + audit PASS -> EQUIVALENT
    (主控 C3: a review that ended CONDITIONAL with no reviewer re-review PASS is not accepted -> residual-review-CONDITIONAL)
  8 else residual (verdict kept, listed)
T4 R3L (主人 2026-11-27 问题 A = A1): work/t4_r3l_relabel.json lists atoms whose K3b touch the reviewers rejected; that touch
(exactly the listed registry ids) is dropped after the K3b scan, the atoms join the allowed set and must end live-hit EXACT.
T4 R4L (主人 2026-11-27 问题 C = C1): work/t4_r4l_relabel.json `relabel` atoms had their errata ATOM_ERR revoked by
t3_errata_build.py (t3_errata.json r4l_revoked); they join the allowed set and must end live-hit EXACT. Its `registry_ptr`
only appends registry ids to the evidence of atoms that stay ATOM_ERR via S1-R1 (label / rule / batch unchanged).
Only rows whose verdict changes are rewritten (every row of a duplicated id; T4 R3L / R4L rows always). The 4 in-scope triage atoms that have no
ledger row are appended. Asserts (exit 1): changed/appended ids ⊆ allowed; untouched lines byte-identical to backup;
every changed row matched_by.phase == 'TB'; IE flips ⊆ t1_ie_final.md (except rule T4-R2L-owner-IE);
every T4 R2L listed atom ends on its listed label.
Usage: python3 -I .work/10_tier_b_repair/scripts/t3/t3_writeback.py [--ts 2026-11-26T00:00:00Z]
"""
import argparse, collections, difflib, hashlib, json, os, re, shutil, subprocess, sys
from datetime import datetime, timezone
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from t3_common import ROOT, TB, W, CK, FIX_ACTIONS, INDEX_FILES, valid_hits, lj, norm, norm_pdf, kb_norm, atom_order, expand_ref, writer_rows, verdict_ptr, batch_commits

ap = argparse.ArgumentParser()
ap.add_argument("--ts", default=datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"))
a = ap.parse_args()
LEDGER, BAK = f"{W}/coverage_ledger.wc.jsonl", f"{W}/coverage_ledger.wc.pre_t3.jsonl"
md5 = lambda p: hashlib.md5(open(p, "rb").read()).hexdigest()
if not os.path.exists(BAK):
    shutil.copyfile(LEDGER, BAK)
print("backup", os.path.relpath(BAK, ROOT), md5(BAK), "| ledger before", md5(LEDGER))

A = {x["atom_id"]: x for x in lj(f"{W}/pdf_atoms.jsonl")}
T = {t["atom_id"]: t for t in json.load(open(f"{W}/triage_merged.json"))}
S2S = collections.defaultdict(list)
for r in lj(f"{W}/t3_t2s_atoms.jsonl"):
    S2S[r["atom_id"]].append(r)
ER = json.load(open(f"{W}/t3_errata.json"))
REG = lj(f"{W}/t2_pdf_typo_registry.jsonl")
IE_FINAL = set(re.findall(r"\b(?:ig34|sv20)_p\d+_a\d+\b", open(f"{CK}/t1_ie_final.md", encoding="utf-8").read()))
md_file = {m["atom_id"]: m.get("file", "") for m in lj(f"{W}/md_atoms.jsonl")}
sec_t = {(r["source"], r["section_key"]): r.get("md_target_files") or [] for r in lj(f"{W}/section_coverage.wc.baseline.jsonl")}  # frozen T0 copy (== pre-T3 wc)
raw = open(BAK, encoding="utf-8").read().splitlines(keepends=True)
rows = [json.loads(l) for l in raw]
led = {}
for r in rows:
    led[r["pdf_atom_id"]] = r  # last row wins (t3_recompute semantics)
# 主控 C2: allowed set = triage ∪ T2S ∪ t3_errata per-atom keys (atom_err ∪ target_remap)
ALLOWED = (set(T) | set(S2S) | set(ER["atom_err"]) | set(ER["target_remap"])) & set(A)
# T4 第二轮改台账 R2L (主人 2026-11-27 问题 1 = A / 2 = A): data list work/t4_r2l_relabel.json (scripts/t4/t4_r2l_build.py);
# the 53 INTENTIONAL_EXCLUDE entries join the allowed set (the 25 PDF_TYPO ones come in as t3_errata atom_err R2)
R2L_ALL = json.load(open(f"{W}/t4_r2l_relabel.json"))
R2L = R2L_ALL["relabel"]
R2L_IE = {i: e for i, e in R2L.items() if e["to"] == "INTENTIONAL_EXCLUDE"}
assert set(R2L_IE) <= set(A) and not set(R2L_IE) & set(ER["atom_err"]), sorted(set(R2L_IE) & set(ER["atom_err"]))
ALLOWED |= set(R2L_IE)
# T4 问题 C 改台账 R4L: the revoked errata atoms (must equal t3_errata.json r4l_revoked) join the allowed set
R4L_ALL = json.load(open(f"{W}/t4_r4l_relabel.json"))
R4L = R4L_ALL["relabel"]
assert set(R4L) <= set(A) and set(R4L) == set(ER.get("r4l_revoked", {})) and not set(R4L) & (set(ER["atom_err"]) | set(R2L)), \
    ("T4 R4L list != t3_errata r4l_revoked / still in atom_err / in R2L", sorted(R4L), sorted(ER.get("r4l_revoked", {})))
# reviewer M-1: the revoke must exist and the list must equal the add-on check's NOT_HOLD atoms (second data source)
R4L_NH = {i for i, v in json.load(open(f"{W}/t4/atomerr/verdicts.json", encoding="utf-8")).items() if v["verdict"] == "NOT_HOLD"}
assert ER.get("r4l_revoked") and set(R4L) == R4L_NH, \
    ("T4 R4L: r4l_revoked empty or relabel ids != verdicts.json NOT_HOLD", sorted(R4L), sorted(ER.get("r4l_revoked", {})), sorted(R4L_NH))
ALLOWED |= set(R4L)
C1 = {k: v for k, v in json.load(open(f"{W}/t3_c1_manual.json")).items() if not k.startswith("_")}
order, idx = atom_order()
WR = collections.defaultdict(list)
for b, wf, n, r in writer_rows():
    for i in expand_ref(str(r["ref"]), idx, order)[0]:
        WR[i].append(dict(batch=b, action=r["action"], kb_file=r["kb_file"], ptr=f"{wf}:{n}", note=str(r.get("note", "")),
                          ref=str(r["ref"])))
COMMIT = batch_commits()
DELTA = f"{CK}/t3_delta_rereview.md"
DELTA_PASS = {}  # 主控 C7: batch -> file:line of its '## B-XX — PASS' delta re-review verdict
if os.path.exists(DELTA):
    for n, l in enumerate(open(DELTA, encoding="utf-8"), 1):
        m = re.match(r"^## ((?:B|S)-\S+) — PASS\s*$", l)
        if m:
            DELTA_PASS[m.group(1)] = f"{os.path.relpath(DELTA, ROOT)}:{n}"
TN = re.compile(r"\bT-(\d+)")
VP = {}
def vp(b):
    """(review_ptr, audit_ptr, review_status); status PASS | DELTA_REREVIEW_PASS (主控 C7, accepted) | CONDITIONAL. Review files of the first batches (B-PCPP/B-LB/B-CP) end at
    'verdict: CONDITIONAL … 其余全部通过' and trace.jsonl has no later code-reviewer PASS (only verifier PASS):
    status 'CONDITIONAL' is returned and, per 主控 C3, NOT accepted as review evidence."""
    if b not in VP:
        rv, st = verdict_ptr(b, "review"), "PASS"
        if not rv:
            p = f"{CK}/t2_{b}_review.md"
            n = next((n for n, l in enumerate(open(p, encoding="utf-8"), 1) if re.search(r"verdict: CONDITIONAL", l, re.I)), None) \
                if os.path.exists(p) else None
            rv, st = (f"{os.path.relpath(p, ROOT)}:{n}", "CONDITIONAL") if n else (None, None)
            if st == "CONDITIONAL" and b in DELTA_PASS:  # 主控 C7: delta re-review PASS lifts the CONDITIONAL
                rv, st = DELTA_PASS[b], "DELTA_REREVIEW_PASS"
        VP[b] = (rv, verdict_ptr(b, "audit"), st)
    return VP[b]

def reg_find(batch, tn):
    return [r for r in REG if r["batch"] == batch and re.match(rf"{re.escape(batch)}( \w+)? T-{tn}(?!\d)", r["id"])]

def targets(i):
    """attempt 2 / 审计 K1: ordered candidates. Tier 1 = the atom's own targets (ledger md_atom_ids files, S1 remap,
    triage kb_loc / ruling target, writer fix-row kb_file); tier 2 = section md_target_files (fallback only).
    Index files (VARIABLE_INDEX / INDEX / ROUTING) are never targets."""
    e = led.get(i, {})
    src = A[i]["atom_id"].split("_")[0]
    tg = collections.OrderedDict()
    for f in sorted({md_file.get(m, "") for m in e.get("md_atom_ids", [])} - {""}):
        tg.setdefault(f, "tier1: ledger md_atom_ids file")
    t = T.get(i, {})
    if t.get("kb_loc") and str(t["kb_loc"]).startswith("knowledge_base/"):
        tg.setdefault(t["kb_loc"].split(":")[0], f"tier1: triage kb_loc {t['kb_loc']}")
    if t.get("target"):
        tg.setdefault(t["target"], "tier1: triage target (ruling)")
    if i in ER["target_remap"]:
        tg.setdefault(ER["target_remap"][i]["target"], f"tier1: S1 remap ({ER['target_remap'][i]['source']})")
    for w in WR.get(i, []):
        if w["action"] in FIX_ACTIONS:
            tg.setdefault(w["kb_file"], f"tier1: writer {w['ptr']} {w['action']}")
    for f in sorted(sec_t.get((src, A[i]["parent_section"]), [])):
        tg.setdefault(f, "tier2: section md_target_files")
    dom = atom_domain(i)  # attempt 3 (审计 A2-5.3 / 主控 C5): the atom's own domain spec.md (spec footnotes / rows)
    if dom and os.path.exists(f"{ROOT}/knowledge_base/domains/{dom}/spec.md"):
        tg.setdefault(f"knowledge_base/domains/{dom}/spec.md", f"tier2: own-domain spec.md ({dom})")
    for f in INDEX_FILES:
        tg.pop(f, None)
    return tg

_lines = {}
def lines(rev, f):
    if (rev, f) not in _lines:
        _lines[(rev, f)] = (subprocess.run(["git", "-C", ROOT, "show", f"{rev}:{f}"], capture_output=True, text=True).stdout.splitlines()
                            if rev else open(f"{ROOT}/{f}", encoding="utf-8").read().splitlines())
    return _lines[(rev, f)]
WR_FILE = collections.defaultdict(list)
for b, wf, n, r in writer_rows():
    if r["action"] in FIX_ACTIONS and str(r.get("kb_line_after", "")).isdigit():
        WR_FILE[r["kb_file"]].append(dict(batch=b, action=r["action"], line=int(r["kb_line_after"]), ptr=f"{wf}:{n}", ref=str(r["ref"])))

def t1_still_valid(t):
    """T1 two-agent agreement was judged on the pre-T2 KB (302ec4c). Valid now only if the kb_loc line text still exists
    in the HEAD file ('unchanged'), or the line was reworked by a T2 fix row of a PASS batch that lies in the same HEAD
    table block / within 3 lines of the best-matching HEAD line ('reworked-by-T2'); else 'stale'."""
    kl = t.get("kb_loc") or ""
    m = re.match(r"(knowledge_base/\S+?):(\d+)$", kl)
    if not m:
        return dict(status="stale", why=f"kb_loc without line: {kl!r}")
    f, n = m.group(1), int(m.group(2))
    base, head = lines("302ec4c", f), lines(None, f)
    if n > len(base):
        return dict(status="stale", why="kb_loc line beyond 302ec4c file")
    bl = base[n - 1]
    if bl in head:
        return dict(status="unchanged", base_line=f"302ec4c:{f}:{n}", head_line=f"{f}:{head.index(bl) + 1}")
    hn = max(range(len(head)), key=lambda k: difflib.SequenceMatcher(None, norm(bl), norm(head[k]), autojunk=False).ratio()) + 1
    lo = hi = hn
    if head[hn - 1].lstrip().startswith("|"):
        while lo > 1 and head[lo - 2].lstrip().startswith("|"):
            lo -= 1
        while hi < len(head) and head[hi].lstrip().startswith("|"):
            hi += 1
    lo, hi = lo - 3, hi + 3
    for w in WR_FILE.get(f, []):
        rv, au, stt = vp(w["batch"])
        if lo <= w["line"] <= hi and rv and au and stt in ("PASS", "DELTA_REREVIEW_PASS"):
            return dict(status="reworked-by-T2", base_line=f"302ec4c:{f}:{n}", head_line=f"{f}:{hn}", block=[lo + 3, hi - 3],
                        batch=w["batch"], fix_row=w["ptr"], fix_ref=w["ref"], review=rv, review_status=stt, audit=au,
                        commit=COMMIT.get(w["batch"]))
    return dict(status="stale", base_line=f"302ec4c:{f}:{n}", head_line_best=f"{f}:{hn}", why="no T2 fix row in HEAD block")

def c1_check(i):
    """C1 evidence must hold now: cited KB line (minus list marker / bold) ⊂ norm_pdf(PDF p-1..p+1 joined by ' ')."""
    f, n = C1[i]["kb"].rsplit(":", 1)
    l = open(f"{ROOT}/{f}", encoding="utf-8").read().splitlines()[int(n) - 1]
    l = norm(re.sub(r"^\s*(?:[-*+]|\d+[.)])\s+", "", l).replace("**", ""))
    pg = C1[i]["pdf_page"]
    pdf = " ".join(norm_pdf(open(f"{W}/pdf_pages/ig34_p{q:04d}.txt", encoding="utf-8").read()) for q in (pg - 1, pg, pg + 1))
    return bool(l) and l in pdf

def atom_domain(i):
    """domain code from '(XX)' in the section title, else from the triage kb_loc 'domains/XX/' path."""
    m = re.search(r"\(([A-Z]{2,8})\)", A[i]["parent_section"])
    if m:
        return m.group(1)
    m = re.search(r"knowledge_base/domains/([A-Z]+)/", str(T.get(i, {}).get("kb_loc") or ""))
    return m.group(1) if m else None

def find_hit(i, tg, v):
    """first target (tier order) with a word-bounded, section-anchored occurrence; S1 remap target tried first."""
    # attempt 3 (审计 A2-5.2): remap > triage kb_loc / ruling target > writer fix row > ledger md_atom_ids > tier2
    rank = lambda f: 0 if "remap" in tg[f] else 1 if "triage" in tg[f] else 2 if "writer" in tg[f] else 3 if tg[f].startswith("tier1") else 4
    order_ = sorted(tg, key=rank)
    rejected, first, allv = {}, None, []
    for f in order_:
        ok, rej = valid_hits(f, v, i, A[i]["parent_section"])
        if ok:
            allv += [(f, x[0]) for x in ok]
            if not first:
                kl = re.match(r"(knowledge_base/\S+?):(\d+)$", str(T.get(i, {}).get("kb_loc") or ""))
                if kl and kl.group(1) == f:  # several valid lines: the one nearest the triage kb_loc first (pointer only)
                    ok = sorted(ok, key=lambda x: abs(x[0] - int(kl.group(2))))
                first = (f, [x[0] for x in ok])
                HITWHY[i] = ok[0][1]
        if rej and not first:
            rejected[f] = rej[:5]
    ALLV[i] = allv
    return (first[0], first[1], rejected) if first else (None, [], rejected)
ALLV = {}  # atom -> every valid (file, line) across its targets (K11 counting)
HITWHY = {}  # atom -> anchor reason of the chosen hit (attempt 3 risk register)

C7_ATOM_ERR = {  # 主控 C7 + K4: delta re-review found the atom verbatim wrong while KB = PDF (checked: atom ∉ PDF window)
    "ig34_p0196_a006": "t3_delta_rereview.md:58 (原子写 'Operationally defined', PDF/KB 'Operationally derived')",
    "ig34_p0247_a021": "t3_delta_rereview.md:51,59 (原子写 'PtFtv / 1999-05-15', PDF/KB 'PrThr / 1999-06-19T04:00')",
}
def pdf_window(i):
    src, p = i.split("_")[0], A[i]["page"]
    return " ".join(norm_pdf(open(f, encoding="utf-8").read()) for q in (p - 1, p, p + 1)
                    for f in [f"{W}/pdf_pages/{src}_p{q:04d}.txt"] if os.path.exists(f))

def _clean(x):
    x = re.sub(r"\([^)]*[\u4e00-\u9fff][^)]*\)", " ", str(x))          # drop Chinese annotations '(两个右引号)'
    return [norm(y) for y in x.split(" / ") if len(norm(y)) >= 2]

def tn_applies(i, w, r):
    """A registered T-n explains this atom's non-hit only if (a) PDF-side and KB-side values differ after norm()
    (quote/dash-only typos are invisible to norm) and (b) for a multi-atom writer row, the PDF-side value occurs in
    this atom (single-atom rows are tied to the atom by the writer)."""
    pv, kv = _clean(r["pdf_value"]), norm(r["kb_text_span"])
    if pv and all(x == kv for x in pv):
        return False
    single = expand_ref(w["ref"], idx, order)[0] == [i]
    va = norm(A[i]["verbatim"])
    return single or any(x in va and x != kv for x in pv)

def decide(i, no_exact=False):
    """-> (verdict|None for residual, rule, batch_id, evidence dict, extra fields). no_exact: K11 surplus re-decision."""
    t, v = T.get(i), norm(A[i]["verbatim"])
    tg = targets(i)
    hit, hit_lines, rejected = find_hit(i, tg, v)
    if no_exact:
        hit, hit_lines = None, []
    ev = dict(hit_file=hit, hit_lines=hit_lines, hit_target_src=tg.get(hit), targets=list(tg), rejected_hits=rejected,
              triage=None, writer=[], t2s=S2S.get(i, []), k11_surplus=no_exact)
    if t:
        ev["triage"] = {k: t.get(k) for k in ("final_class", "src", "reviewed", "lane", "pack_id", "kb_loc", "ie_cat", "pdf_typo_suspect")}
    fixes = [w for w in WR.get(i, []) if w["action"] in FIX_ACTIONS]
    ev["writer"] = [{k: w[k] for k in ("batch", "action", "ptr")} for w in WR.get(i, [])]
    if i in ER["atom_err"]:
        x = ER["atom_err"][i]
        ev.update(errata=f"work/t3_errata.json#atom_err/{i}", registry=x["registry"], checkpoint=x["checkpoint"], basis=x["basis"][:200])
        rb = x["registry"][0].split(" ")[0] if x["registry"] else None
        if rb in DELTA_PASS:  # 主控 C7 / 审计 K7: registry of a CONDITIONAL batch, accepted via the delta re-review
            ev["c7_delta_rereview"] = DELTA_PASS[rb]
        return x["terminal"], f"S1-{x['cls']}", (x["registry"][0].split(" ")[0] if x["registry"] else "T1/T2-errata"), ev, {}
    if t and t["final_class"] == "FIGURE":
        return "FIGURE_DEFERRED", "FIGURE", f"T1:{t['pack_id']}", ev, {}
    if i in R2L_IE:  # T4 R2L (主人 2026-11-27 问题 1 = A / 2 = A): before K3b / live-hit (an R1-row / TOC atom may still hit KB)
        e = R2L_IE[i]
        why = "R1-row: KB 精简列一致, PDF 其它列未收" if e["group"] == "R1-row" else "v2.0 目录条目, 对应章节 KB 未收"
        ev.update(t4_r2l=dict(group=e["group"], decision=e["decision"], raw=e["raw"], spec="subagent_prompts/t4/t4_round2_ledger_spec_v1.0.md §1"))
        return "INTENTIONAL_EXCLUDE", "T4-R2L-owner-IE", "T4-R2L", ev, dict(
            category="VERSION_MISMATCH", exclusion_reason=f"Tier B T4 round-2 IE (VERSION_MISMATCH; {why})", approved_by=e["decision"])
    if i in K3B:  # attempt 3 / 审计 K3b: registered deviation touches this atom -> PDF_TYPO (before live-hit / IE)
        ev.update(registry=sorted(set(K3B[i])), k3b=K3B_WHY.get(i))
        rb = K3B[i][0].split(" ")[0]
        if rb in DELTA_PASS:
            ev["c7_delta_rereview"] = DELTA_PASS[rb]
        return "PDF_TYPO", "K3b-registry", rb, ev, {}
    pu = ER["pending_user"].get(i)
    if pu and "残留" in pu["conclusion"]:
        ev["pending_user"] = pu["conclusion"]
        return None, "pending_user-residual", None, ev, {}
    ack = "evidence/checkpoints/t1_user_ack.md R4 (+R1 for VERSION_MISMATCH); list evidence/checkpoints/t1_ie_final.md"
    if hit:  # 主控 C5: a live hit on the target beats IE
        b = next((w["batch"] for w in fixes if w["kb_file"] == hit), None) or \
            (f"T1:{t['pack_id']}" if t else (S2S[i][0]["batch"] if i in S2S else "T3-errata-key"))
        if t and t["final_class"] == "IE":
            assert i in IE_FINAL, f"IE atom {i} not in t1_ie_final.md"
            ev["ie_ack_original"] = dict(ie_cat=t.get("ie_cat"), src=t["src"], ack=ack, note="主控 C5: 当场命中 → EXACT 优先于 IE")
            return "EXACT", "live-hit(was-IE-ack)", b, ev, {}
        return "EXACT", "live-hit", b, ev, {}
    if t and t["final_class"] == "IE":
        assert i in IE_FINAL, f"IE atom {i} not in t1_ie_final.md"
        return "INTENTIONAL_EXCLUDE", "IE-ack", f"T1:{t['pack_id']}", ev, dict(
            category=t.get("ie_cat"), exclusion_reason=f"Tier B T1 IE ({t.get('ie_cat')}; {t['src']})", approved_by=f"user: {ack}")
    if i in C1:  # 主控 C1: manual PDF + KB check, asserted below
        f, n = C1[i]["kb"].rsplit(":", 1)
        ev.update(c1_manual=C1[i], c1_check=c1_check(i))
        return C1[i]["verdict"], "C1-manual-PDF+KB", "T3-C1", ev, {}
    if i in C7_ATOM_ERR:
        assert norm(A[i]["verbatim"]) not in pdf_window(i), f"C7 ATOM_ERR but atom on PDF page: {i}"
        ev.update(c7=C7_ATOM_ERR[i], atom_in_pdf=False)
        return "ATOM_ERR", "C7-K4-rereview", "T3-C7", ev, {}
    for w in WR.get(i, []):  # 审计 K3: T-n from note AND ref
        for tn in TN.findall(w["note"] + " " + w["ref"]):
            regs = [r for r in reg_find(w["batch"], tn) if tn_applies(i, w, r)]
            if regs:
                ev.update(registry=[r["id"] for r in regs], writer_row=w["ptr"], registry_handling=regs[0]["handling"])
                if w["batch"] in DELTA_PASS:
                    ev["c7_delta_rereview"] = DELTA_PASS[w["batch"]]
                term = "ATOM_ERR" if regs[0]["handling"].startswith("照录") else "PDF_TYPO"
                return term, "writer-Tn-registry", w["batch"], ev, {}
    if t and t["final_class"] in ("PRESENT", "REWRITE_OK") and (t["reviewed"] or str(t["src"]).startswith("ruling:")):
        st = t1_still_valid(t)
        ev["t1_kb_loc_check"] = st
        if st["status"] == "unchanged":
            return "EQUIVALENT", "T1-two-agent", f"T1:{t['pack_id']}", ev, {}
        if st["status"] == "reworked-by-T2":
            return "EQUIVALENT", "T1-two-agent+T2-rework", st["batch"], ev, {}
        # T1 judged pre-T2 text that no longer exists and no T2 row covers it -> fall through (T2 fix rows / residual)
    for w in fixes:
        rv, au, st = vp(w["batch"])
        if rv and au and st == "CONDITIONAL":  # 主控 C3: CONDITIONAL with no reviewer re-review PASS -> not accepted
            ev.setdefault("rejected_conditional", []).append(dict(batch=w["batch"], fix_row=w["ptr"], review=rv, audit=au))
            continue
        if rv and au:
            ck = next((x["checkpoint"] for x in S2S.get(i, []) if x["batch"] == w["batch"] and x["checkpoint"]), None)
            if not ck:
                p = f"{CK}/t2_{w['batch']}.md"
                tail = i.split("_", 1)[1]
                ck = next((f"{os.path.relpath(p, ROOT)}:{n}" for n, l in enumerate(open(p, encoding="utf-8"), 1) if tail in l), None) \
                    if os.path.exists(p) else None
            ev.update(fix_row=w["ptr"], checkpoint=ck or os.path.relpath(f"{CK}/t2_{w['batch']}.md", ROOT),
                      review=rv, review_status=st, audit=au, commit=COMMIT.get(w["batch"]))
            if st == "DELTA_REREVIEW_PASS" and norm(A[i]["verbatim"]) not in pdf_window(i):
                # 主控 attempt 3 C7 口径: atom ∉ PDF window while KB = PDF (census + delta re-review) -> ATOM_ERR (as K4)
                ev["atom_in_pdf"] = False
                return "ATOM_ERR", "C7-atom-not-in-PDF", w["batch"], ev, {}
            return "EQUIVALENT", "T2-fix+PASS" if st == "PASS" else "T2-fix+deltaRereviewPASS+auditPASS", w["batch"], ev, {}
    if ev.get("rejected_conditional"):
        return None, "residual-review-CONDITIONAL", None, ev, {}
    return None, "residual-no-evidence", None, ev, {}

# 审计 K3 全量: atoms named by any writer row whose note/ref carries a registered T-n join the allowed set
K3_ATOMS = {i for i, ws in WR.items() if i in A and any(reg_find(w["batch"], tn) for w in ws for tn in TN.findall(w["note"] + " " + w["ref"]))}
K3_EXTRA = K3_ATOMS - ALLOWED
ALLOWED |= K3_ATOMS
# ── attempt 3 / 审计 K3b: registry-driven. For every 'KB 写正确值' deviation in t2_pdf_typo_registry.jsonl:
#   P = PDF-side value(s), K = KB-side span (kb_text_span) + kb_value; aligned token diff (difflib, interior only)
#   gives pd (PDF-only tokens) and kd (KB-only tokens), length >= 3.
#   An atom is touched when its PDF window (p..p+1) holds the registry page, the registry kb_file is one of its targets,
#   and (a) it carries a pd token that the KB file no longer has (atom = PDF, KB corrected) or
#       (b) it carries a kd token that the registry PDF page does not have (extractor already corrected; KB = atom), or
#       (c) it carries a kd token and its word-bounded KB hit is on the registry's kb_line_now (the deviating line itself).
#   Touched atoms -> PDF_TYPO, before live-hit EXACT / IE (only S1 errata and FIGURE come first).
LOCATOR = re.compile(r"^(row|rows|r\d+(/r\d+)?|ex\d+[a-z]?|asm|\d{1,2}|[a-z]{2,8}\.xpt|relrec|supp[a-z]*|spec|notes)$")
STOP = {"the", "and", "that", "with", "for", "this", "are", "was", "were", "from", "not", "has", "have", "been", "which", "when", "into", "its"}
PUNCT_ONLY = []
TOK = lambda x: re.findall(r"[a-z0-9][a-z0-9/._+-]*[a-z0-9+]|[a-z0-9]", x)
CJK = re.compile(r"[\u4e00-\u9fff]")
def reg_diff(r):
    pv = " ".join(CJK.sub(" ", x) for x in _clean(r["pdf_value"])).strip()   # 'Ex3 表头 LBSTRNHI' -> 'ex3 lbstrnhi'
    kv = " ".join([norm(r["kb_text_span"])] + [x for x in _clean(r["kb_value"]) if not CJK.search(x)][:1])
    if not pv:
        return None
    P = [t for t in TOK(pv) if not LOCATOR.match(t)]   # drop locators of descriptive pdf_value ('Row 5', 'Ex3', 'asm 7')
    K = TOK(norm(r["kb_text_span"]))
    if not P or re.search(r"句号|句点|逗号|句末", str(r["kb_value"]) + str(r["pdf_value"])):
        if r["id"] not in PUNCT_ONLY:
            PUNCT_ONLY.append(r["id"])  # e.g. 'Row 5 句末无句点': punctuation-only, not tokenizable
        return "PUNCT"
    if not K:
        K = TOK(kv)
    ops = difflib.SequenceMatcher(None, P, K, autojunk=False).get_opcodes()
    pd, kd = set(), set()
    for n, (tag, i1, i2, j1, j2) in enumerate(ops):
        if tag == "equal":
            continue
        edge = n in (0, len(ops) - 1) and tag in ("insert", "delete")
        if edge and len(ops) > 1:
            continue  # span extent, not the deviation
        pd |= set(P[i1:i2]); kd |= set(K[j1:j2])
    pd, kd = {t for t in pd - kd if len(t) >= 3 and t not in STOP}, {t for t in kd - pd if len(t) >= 3 and t not in STOP}
    CTX[r["id"]] = (P, K)
    spacing = re.sub(r"\s", "", " ".join(P)) == re.sub(r"\s", "", " ".join(K)) or bool(re.search(r"空格", str(r["kb_value"])))
    if spacing:  # spacing-only typo ('CMSTRF.Some'): only an atom carrying the PDF-joined form is touched
        kd = set()
    return (pd, kd) if (pd or kd) else None
_pt = {}
def page_tokens(src, pg):
    if (src, pg) not in _pt:
        f = f"{W}/pdf_pages/{src}_p{pg:04d}.txt"
        _pt[(src, pg)] = set(TOK(norm_pdf(open(f, encoding="utf-8").read()))) if os.path.exists(f) else set()
    return _pt[(src, pg)]
_kt = {}
def kb_tokens(f):
    if f not in _kt:
        _kt[f] = set(TOK(kb_norm(f)))
    return _kt[f]
CTX = {}
def distinctive(t):
    """attempt 4 (审计 A3-5.2: n-gram context was too strict for table cells): a diff token with a digit, a non-letter
    character or >= 6 letters (variable names like BESDTC / TESTCD / MonoSub / SUENTTP) needs no neighbour."""
    return len(t) >= 6 or not t.isalpha()

def ctx_ok(v, toks, side, allow_distinctive=True):
    """the atom must carry the diff token with a same-side neighbour (n-gram) when the side has more than one token,
    unless the token is distinctive (rules a/b only; rule c keeps the strict n-gram)."""
    if len(side) <= 1 or (allow_distinctive and any(distinctive(t) for t in toks)):
        return True
    for t in toks:
        for k, x in enumerate(side):
            if x == t and any(" ".join(side[a:b]) in v for a, b in ((k - 1, k + 1), (k, k + 2)) if a >= 0 and b <= len(side)):
                return True
    return False
K3B_UNUSABLE = [r["id"] for r in REG if r["handling"].startswith("KB 写正确值") and reg_diff(r) is None]

K3B = collections.defaultdict(list)
K3B_WHY = {}
K3B_A_EXCLUDED = []  # (atom, registry) pairs dropped by rule (a)'s own-tier1-file exclusion (审计 A4-5.2)
K3B_DEBUG = set(os.environ.get("K3B_DEBUG", "").split(",")) - {""}
by_page = collections.defaultdict(list)
for x in A.values():
    by_page[(x["atom_id"].split("_")[0], x["page"])].append(x["atom_id"])
for r in REG:
    if not r["handling"].startswith("KB 写正确值"):
        continue
    d = reg_diff(r)
    if d == "PUNCT":  # punctuation-only deviation: the atom whose KB hit is the registered line itself is touched
        src = "sv20" if r["kb_file"].startswith("knowledge_base/model/") else "ig34"
        for pg in (r["pdf_page"] - 1, r["pdf_page"]):
            for i in by_page.get((src, pg), []):
                if A[i]["atom_type"] == "HEADING" or r["kb_file"] not in targets(i):
                    continue
                if int(r.get("kb_line_now") or -1) in [ln for ln, _ in valid_hits(r["kb_file"], norm(A[i]["verbatim"]), i, A[i]["parent_section"])[0]]:
                    K3B[i].append(r["id"])
                    K3B_WHY.setdefault(i, []).append(f"{r['id']}:c'(punctuation-only, on registered line)")
        continue
    if not d:
        continue
    pd, kd = d
    src = "sv20" if r["kb_file"].startswith("knowledge_base/model/") else "ig34"
    pd_live0 = {t for t in pd if t not in kb_tokens(r["kb_file"])}
    for pg in (r["pdf_page"] - 1, r["pdf_page"]):
        for i in by_page.get((src, pg), []):
            if A[i]["atom_type"] == "HEADING":
                continue
            v = norm(A[i]["verbatim"])
            at = set(TOK(v))
            if i in K3B_DEBUG:
                print("K3B_DEBUG", i, r["id"], "kb_file in targets:", r["kb_file"] in targets(i), "pd:", sorted(pd), "kd:", sorted(kd),
                      "at∩pd:", sorted(at & pd), "at∩kd:", sorted(at & kd), "pd_live0:", sorted(pd_live0), "P,K:", CTX[r["id"]])
            if r["kb_file"] not in targets(i) or not (at & (pd | kd)):
                continue
            # (c) the atom sits on the registered deviation line itself (kb_line_now) and carries a KB-side token
            win = page_tokens(src, A[i]["page"]) | page_tokens(src, A[i]["page"] + 1)
            P_, K_ = CTX[r["id"]]
            # (b) only for non-row atoms: table-row text layers wrap cells, so "not in window" is no evidence there
            kd_live = {t for t in at & kd if t not in win} if A[i]["atom_type"] != "TABLE_ROW" else set()
            # attempt 4: the PDF-side token must also be gone from the atom's own (tier1) KB files — MB atoms whose MB file
            # still (correctly) carries MBREFID are not touched by the MS supp deviation B-MS T-3
            own = [f for f, tag in targets(i).items() if tag.startswith("tier1")]
            pd_own = {t for t in at & pd_live0 if not any(t in kb_tokens(f) for f in own if f != r["kb_file"])}
            if (at & pd_live0) - pd_own:
                K3B_A_EXCLUDED.append(f"{i}|{r['id']}|{sorted((at & pd_live0) - pd_own)}")
            pd_live = pd_own if ctx_ok(v, pd_own, P_) else set()
            if not ctx_ok(v, kd_live, K_):
                kd_live = set()
            on_line = bool(at & kd) and ctx_ok(v, at & kd, K_, allow_distinctive=False) and int(r.get("kb_line_now") or -1) in [ln for ln, _ in valid_hits(r["kb_file"], v, i, A[i]["parent_section"])[0]]
            why = "a:pdf-side" if at & pd_live else "b:kb-side-not-in-window" if kd_live else "c:on-registered-line" if on_line else None
            if why:
                K3B[i].append(r["id"])
                K3B_WHY.setdefault(i, []).append(f"{r['id']}:{why}:{sorted((at & pd_live) or kd_live or (at & kd))[:3]}")
# attempt 4 / 主控 第 2 项: manual PDF + KB + atom comparison for the 2 audit 待人工 atoms
K3B_MANUAL = {k: v for k, v in json.load(open(f"{W}/t3_k3b_manual.json")).items() if not k.startswith("_")}
for i, m in K3B_MANUAL.items():
    K3B[i].append(m["registry"])
    K3B_WHY.setdefault(i, []).append(f"{m['registry']}:manual:{m['kb']}")
# attempt 4 / 主控 第 3 项: K3b adds to the allowed set only §5.0-scope atoms (+ keep_k3b entries of the keep list)
SCOPE = {(r["source"], r["section_key"]) for r in lj(f"{TB}/inventory.jsonl")} | {("ig34", "§6.3.5.9.3 Relating PP Records to PC Records")}
in_scope = lambda i: (i.split("_")[0], A[i]["parent_section"]) in SCOPE
# attempt 4 可复现性修复 (审计 A4-5.1): out-of-§5.0 K3b handling comes ONLY from the explicit data list
# work/t3_k3b_out_of_scope_keep.json (action keep_k3b: keep the K3b PDF_TYPO; t4_only: list, do not change).
# Every entry is re-asserted at run time: its pdf.token ⊂ norm(PDF line) and kb.token ⊂ norm(KB line).
KEEP = {k: v for k, v in json.load(open(f"{W}/t3_k3b_out_of_scope_keep.json")).items() if not k.startswith("_")}
KEEP_BAD = []
for i, k in KEEP.items():
    pg, ln = k["pdf"]["line"].split(":")
    pl = open(f"{W}/pdf_pages/{pg}.txt", encoding="utf-8").read().splitlines()[int(ln) - 1]
    kf, kn = k["kb"]["line"].rsplit(":", 1)
    kl = open(f"{ROOT}/{kf}", encoding="utf-8").read().splitlines()[int(kn) - 1]
    if k["pdf"]["token"] not in norm_pdf(pl) or k["kb"]["token"] not in norm(kl):
        KEEP_BAD.append(i)
K3B_KEEP_A3 = sorted(i for i, k in KEEP.items() if k["action"] == "keep_k3b")
# T4 问题 A 改台账 R3L (主人 2026-11-27 问题 A = A1): data list work/t4_r3l_relabel.json (scripts/t4/t4_r3l_build.py).
# The reviewers found the registered deviation is not in these atoms (it is in a neighbour atom / another table): their K3b
# touch must be exactly the listed registry ids and is dropped; the atoms join the allowed set and are decided by the
# existing branches (asserted below: live-hit EXACT). Their keep-list entries carry action t4_r3l_drop.
R3L = json.load(open(f"{W}/t4_r3l_relabel.json"))["relabel"]
assert set(R3L) <= set(A) and not set(R3L) & (set(ER["atom_err"]) | set(R2L)), sorted(set(R3L) & (set(ER["atom_err"]) | set(R2L)))
assert not set(R3L) & set(R4L), sorted(set(R3L) & set(R4L))
assert {i for i, k in KEEP.items() if k["action"] == "t4_r3l_drop"} == set(R3L), sorted(i for i, k in KEEP.items() if k["action"] == "t4_r3l_drop")
K3B_R3L = {}
for i, e in R3L.items():
    assert sorted(set(K3B.get(i, []))) == e["k3b_drop"], ("T4 R3L K3b touch != listed", i, sorted(set(K3B.get(i, []))), e["k3b_drop"])
    K3B_R3L[i] = dict(registry=sorted(set(K3B.pop(i))), why=K3B_WHY.pop(i, None))
ALLOWED |= set(R3L)
K3B_OUT = {i: K3B.pop(i) for i in [i for i in K3B if (KEEP.get(i, {}).get("action") == "t4_only")
                                     or (not in_scope(i) and i not in ALLOWED and KEEP.get(i, {}).get("action") != "keep_k3b")]}
K3B_EXTRA = set(K3B) - ALLOWED
ALLOWED |= set(K3B)
decided = {i: decide(i) for i in sorted(ALLOWED)}
# 审计 K11: n EXACT atoms with the same section + normalized text need >= n valid occurrences in their hit files
grp = collections.defaultdict(list)
for i, (verdict, rule, batch, ev, extra) in decided.items():
    if verdict == "EXACT":
        grp[(A[i]["atom_id"].split("_")[0], A[i]["parent_section"], norm(A[i]["verbatim"]))].append(i)
K11 = {}
for k, ids in grp.items():
    if len(ids) < 2:
        continue
    occ = {x for i in ids for x in ALLV.get(i, [])}
    if len(occ) < len(ids):
        surplus = sorted(ids)[len(occ):]
        K11["|".join(k[1:])[:120]] = dict(atoms=sorted(ids), occurrences=sorted(occ), surplus=surplus)
        for i in surplus:
            decided[i] = decide(i, no_exact=True)
# T4 R2L §2 item 3 (pointer only): registry ids the reviewers found missing from the evidence of atoms that stay PDF_TYPO
REG_IDS = {r["id"] for r in REG}
for i, p in R2L_ALL["registry_ptr"].items():
    assert i in decided and decided[i][0] == "PDF_TYPO" and all(r in REG_IDS for r in p["add"]), (i, decided.get(i, [None])[0])
    ev = decided[i][3]
    ev["registry"] = list(ev.get("registry") or []) + [r for r in p["add"] if r not in (ev.get("registry") or [])]
    ev["t4_r2l_registry_ptr"] = dict(add=p["add"], raw=p["raw"], note="T4 R2L §2.3: 只补登记指针, 标签与规则不变")
# T4 R4L registry_ptr (pointer only; t4_atomerr_fullcheck.md §5b): the atom must stay ATOM_ERR via S1-R1; only evidence.registry
# changes (provenance stays in work/t4_r4l_relabel.json, so no other evidence key is added)
for i, p in R4L_ALL["registry_ptr"].items():
    assert all(r in REG_IDS for r in p["add"]), ("T4 R4L registry_ptr: registry id not in t2_pdf_typo_registry.jsonl", i,
                                                 [r for r in p["add"] if r not in REG_IDS])
    assert i in decided and decided[i][:2] == ("ATOM_ERR", "S1-R1"), \
        ("T4 R4L registry_ptr atom not ATOM_ERR via S1-R1", i, decided.get(i, [None, None])[:2])
    ev = decided[i][3]
    ev["registry"] = list(ev.get("registry") or []) + [r for r in p["add"] if r not in (ev.get("registry") or [])]
# T4 R4L: decision source + reviewer pointers; batch T4-R4L (the live-hit fallback would say T3-errata-key)
for i, e in R4L.items():
    verdict, rule, batch, ev, extra = decided[i]
    ev["t4_r4l"] = dict(group=e["group"], decision=e["decision"], raw=e["raw"], before="ATOM_ERR (S1-R1, t1_errata t3_atom_err)",
                        errata_revoked=f"work/t3_errata.json#r4l_revoked/{i}", spec=e["spec"])
    decided[i] = (verdict, rule, "T4-R4L", ev, extra)
# T4 R3L: decision source + reviewer pointer on the evidence; batch T4-R3L (the live-hit fallback would say T3-errata-key)
for i, e in R3L.items():
    verdict, rule, batch, ev, extra = decided[i]
    ev["t4_r3l"] = dict(group=e["group"], decision=e["decision"], raw=e["raw"], before="PDF_TYPO (K3b-registry, keep_k3b)",
                        k3b_dropped=K3B_R3L[i]["registry"], k3b_why_dropped=K3B_R3L[i]["why"],
                        spec="subagent_prompts/t4/t4_round3_ledger_spec_v1.0.md §1")
    decided[i] = (verdict, rule, "T4-R3L", ev, extra)
decisions, new_rows = {}, {}
for i in sorted(ALLOWED):
    verdict, rule, batch, ev, extra = decided[i]
    old = led.get(i, {}).get("verdict", "NO_LEDGER_ROW")
    decisions[i] = dict(old=old, new=verdict or old, rule=rule, batch=batch, in_triage=i in T, in_t2s=i in S2S,
                        short_verbatim=len(norm(A[i]["verbatim"])) < 25, evidence=ev)
    if verdict and (verdict != old or i in R3L or i in R4L):  # T4 R3L / R4L rows are rewritten as TB rows even when equal to pre_t3 (direct_hit checks TB rows)
        mb = dict(phase="TB", subagent_type="script/t3_writeback", batch_id=batch, rule=rule, prev_verdict=old,
                  evidence=ev, prompt_version="t3_writer_v1.0", ts=a.ts)
        new_rows[i] = (verdict, mb, extra)

out_lines, changed_ids, appended = [], collections.Counter(), []
for l, r in zip(raw, rows):
    i = r["pdf_atom_id"]
    if i in new_rows:
        verdict, mb, extra = new_rows[i]
        nr = dict(r, verdict=verdict, matched_by=mb)
        for k, v in extra.items():
            nr[k] = v
        out_lines.append(json.dumps(nr, ensure_ascii=False) + "\n")
        changed_ids[i] += 1
    else:
        out_lines.append(l)
for i in sorted(new_rows):
    if i not in led:
        verdict, mb, extra = new_rows[i]
        nr = dict(pdf_atom_id=i, md_atom_ids=[], verdict=verdict, similarity_score=None, discrepancy=None,
                  exclusion_reason=extra.get("exclusion_reason"), category=extra.get("category"),
                  approved_by=extra.get("approved_by"), matched_by=dict(mb, appended_row=True))
        out_lines.append(json.dumps(nr, ensure_ascii=False) + "\n")
        appended.append(i)
with open(LEDGER, "w", encoding="utf-8") as f:
    f.writelines(out_lines)

# ── assertions
bad = []
chk = open(LEDGER, encoding="utf-8").read().splitlines(keepends=True)
if len(chk) != len(raw) + len(appended):
    bad.append(f"line count {len(chk)} != {len(raw)}+{len(appended)}")
for n, (l0, l1) in enumerate(zip(raw, chk)):
    r1 = json.loads(l1)
    if r1["pdf_atom_id"] not in new_rows and l0 != l1:
        bad.append(f"untouched line {n + 1} differs")
    if l0 != l1:
        if r1["pdf_atom_id"] not in ALLOWED:
            bad.append(f"changed id outside allowed set: {r1['pdf_atom_id']}")
        if r1["matched_by"].get("phase") != "TB":
            bad.append(f"changed row without phase TB: {r1['pdf_atom_id']}")
for l1 in chk[len(raw):]:
    r1 = json.loads(l1)
    if r1["pdf_atom_id"] not in ALLOWED or r1["pdf_atom_id"] in led or r1["matched_by"].get("phase") != "TB":
        bad.append(f"bad appended row {r1['pdf_atom_id']}")
for i, (v, mb, _) in new_rows.items():
    if v == "INTENTIONAL_EXCLUDE" and i not in IE_FINAL and not (i in R2L_IE and mb["rule"] == "T4-R2L-owner-IE"):
        bad.append(f"IE flip not in t1_ie_final: {i}")
    if mb["rule"] == "C1-manual-PDF+KB" and not mb["evidence"]["c1_check"]:
        bad.append(f"C1 evidence fails: {i}")
    if v == "EXACT" and not (mb["evidence"]["hit_file"] and valid_hits(mb["evidence"]["hit_file"], norm(A[i]["verbatim"]), i, A[i]["parent_section"])[0]):
        bad.append(f"EXACT without word-bounded anchored hit: {i}")
    if v == "EXACT" and mb["evidence"]["hit_file"] in INDEX_FILES:
        bad.append(f"EXACT on index file: {i}")
    if v == "EXACT" and i in K3B:
        bad.append(f"EXACT atom touched by registered deviation (K3b): {i} {K3B[i]}")
    if v == "ATOM_ERR" and norm(A[i]["verbatim"]) in pdf_window(i):
        bad.append(f"ATOM_ERR but atom on PDF page (K4): {i}")

# attempt 4 / 主控 第 3 项: no §5.0-scope EXACT/EQUIVALENT row of the FINAL ledger (TB or stock) may be touched by a
# registered deviation (scan above covers every atom, not only TB rows)
final = {}
for l1 in chk:
    r1 = json.loads(l1)
    final[r1["pdf_atom_id"]] = r1["verdict"]
K3B_ASSERT_HITS = sorted(i for i in K3B if final.get(i) in ("EXACT", "EQUIVALENT"))
for i in KEEP_BAD:
    bad.append(f"keep-list entry no longer holds (pdf/kb line token): {i}")
for i, k in KEEP.items():
    if k["action"] == "keep_k3b" and final.get(i) != "PDF_TYPO":
        bad.append(f"keep_k3b entry not PDF_TYPO in final ledger: {i}")
    if k["action"] == "keep_k3b" and i not in K3B:
        bad.append(f"keep_k3b entry no longer touched by K3b rules: {i}")
# T4 R2L: every listed atom ends on its listed label; the IE ones are not claimed by an earlier decide() branch
R2L_UNDECIDED = sorted(set(R2L) - set(decided))  # reviewer (R2L): a listed atom outside the allowed set is reported, not a KeyError
for i in R2L_UNDECIDED:
    bad.append(f"T4 R2L atom not in allowed set / not decided: {i}")
for i, e in ((i, e) for i, e in R2L.items() if i in decided):
    if final.get(i) != e["to"]:
        bad.append(f"T4 R2L atom not at listed label: {i} {final.get(i)} != {e['to']}")
    if i in R2L_IE and (i in K3B or (T.get(i) or {}).get("final_class") == "FIGURE" or decided[i][1] != "T4-R2L-owner-IE"):
        bad.append(f"T4 R2L IE atom decided by another branch: {i} {decided[i][1]}")
    if i not in R2L_IE and decided[i][1] != "S1-R2":
        bad.append(f"T4 R2L PDF_TYPO atom not via S1-R2: {i} {decided[i][1]}")
for i, e in R3L.items():  # T4 R3L: the listed label must come from the existing live-hit path, not be assigned
    if final.get(i) != e["to"] or decided[i][1] != "live-hit" or i in K3B or i not in new_rows:
        bad.append(f"T4 R3L atom not live-hit {e['to']}: {i} {final.get(i)} {decided[i][1]} in_k3b={i in K3B}")
for i, e in R4L.items():  # T4 R4L: EXACT must come from the existing live-hit path (pre_t3 is already EXACT: check the rule)
    if final.get(i) != e["to"] or decided[i][1] != "live-hit" or i in K3B or i not in new_rows:
        bad.append(f"T4 R4L atom not live-hit {e['to']}: {i} {final.get(i)} {decided[i][1]} in_k3b={i in K3B}")
for i in K3B_ASSERT_HITS:
    bad.append(f"§5.0 EXACT/EQUIVALENT touched by registered deviation (final ledger): {i} {K3B[i]}")
open(f"{W}/t3_t4_k3b_out_of_scope.txt", "w").write("".join(f"{i}\t{final.get(i)}\t{';'.join(sorted(set(v)))}\n" for i, v in sorted(K3B_OUT.items())))

# ── report
C = collections.Counter
flips = C((d["old"], d["new"]) for i, d in decisions.items() if i in new_rows)
print(f"allowed={len(ALLOWED)} (triage∩atoms={len(set(T) & set(A))}, t2s={len(S2S)}) flipped_atoms={len(new_rows)} "
      f"rewritten_rows={sum(changed_ids.values())} (dup ids rewritten: {[i for i, n in changed_ids.items() if n > 1]}) appended={appended}")
print("flips by new verdict:", dict(C(v for v, _, _ in new_rows.values())))
print("flips by rule:", dict(C(d["rule"] for i, d in decisions.items() if i in new_rows)))
print("flips old->new:", dict(flips))
res = {i: d for i, d in decisions.items() if d["rule"].startswith("residual") or d["rule"] == "pending_user-residual"}
json.dump(dict(K3_extra=sorted(K3_EXTRA), K11=K11, K3b={i: sorted(set(v)) for i, v in sorted(K3B.items())}, K3b_why=K3B_WHY,
               K3b_extra=sorted(K3B_EXTRA), K3b_unusable_registry=K3B_UNUSABLE, K3b_punct_only=PUNCT_ONLY,
               K3b_out_of_scope={i: sorted(set(v)) for i, v in sorted(K3B_OUT.items())}, K3b_manual=sorted(K3B_MANUAL),
               K3b_keep_list=K3B_KEEP_A3, K3b_a_excluded=dict(count=len(K3B_A_EXCLUDED), pairs=K3B_A_EXCLUDED),
               K3b_t4_r3l_dropped=K3B_R3L),
          open(f"{W}/t3_rules.json", "w"), ensure_ascii=False, indent=1)
AL = {"atom section has no number", "file numbering is the other PDF", "no governing numbered heading"}
anchorless = sorted(i for i, d in decisions.items() if d["new"] == "EXACT" and HITWHY.get(i) in AL)
open(f"{W}/t3_t4_risk_anchorless.txt", "w").write("".join(f"{i}\t{HITWHY[i]}\t{decisions[i]['evidence']['hit_file']}:{decisions[i]['evidence']['hit_lines'][0]}\n" for i in anchorless))
print("K3b punctuation-only registry rows (matched by registered line only):", len(PUNCT_ONLY), PUNCT_ONLY)
print("K3b out of §5.0 (T4 list work/t3_t4_k3b_out_of_scope.txt, not changed):", len(K3B_OUT), sorted(K3B_OUT))
print("K3b keep list:", len(KEEP), "entries, failing pdf/kb re-check:", KEEP_BAD, "| rule (a) own-file exclusions:", len(K3B_A_EXCLUDED))
print("K3b extended assertion over final ledger §5.0 EXACT/EQUIVALENT: hits =", len(K3B_ASSERT_HITS))
print("K3b: atoms", len(K3B), "extra (not otherwise allowed)", len(K3B_EXTRA), "| registry rows not machine-usable", len(K3B_UNUSABLE))
print("anchorless EXACT (T4 risk list work/t3_t4_risk_anchorless.txt):", len(anchorless))
print("K3 allowed-set extension (writer T-n atoms not otherwise allowed):", len(K3_EXTRA), sorted(K3_EXTRA))
print("T4 R2L:", len(R2L), "listed; final label as listed:", sum(final.get(i) == e["to"] for i, e in R2L.items()), "| IE", len(R2L_IE))
print("T4 R3L:", len(R3L), "listed; K3b touches dropped:", {i: x["registry"] for i, x in K3B_R3L.items()},
      "| final label as listed via live-hit:", sum(final.get(i) == e["to"] and decided[i][1] == "live-hit" for i, e in R3L.items()))
print("T4 R4L:", len(R4L), "listed (errata revoked) | final label as listed via live-hit:",
      sum(final.get(i) == e["to"] and decided[i][1] == "live-hit" for i, e in R4L.items()),
      "| registry_ptr:", {i: decided[i][3]["registry"] for i in R4L_ALL["registry_ptr"]})
print("K11 groups short of occurrences:", json.dumps(K11, ensure_ascii=False))
print("T1 kb_loc check:", dict(C((d["evidence"].get("t1_kb_loc_check") or {}).get("status") for d in decisions.values() if d["evidence"].get("t1_kb_loc_check"))))
print("residual (allowed, verdict kept):", len(res), dict(C((d["old"], d["in_triage"]) for d in res.values())))
for i, d in res.items():
    print("  RESIDUAL", i, d["old"], d["rule"], "triage" if d["in_triage"] else "t2s-only", (d["evidence"].get("triage") or {}).get("final_class"))
unchanged_same = [i for i, d in decisions.items() if i not in new_rows and d["rule"] not in res and i not in res]
print("allowed, decided but verdict already equal (no write):", len([i for i in decisions if i not in new_rows and i not in res]))
print("triage MANUAL ids (not atoms, not written):", sorted(set(T) - set(A)))
json.dump(decisions, open(f"{W}/t3_writeback_decisions.json", "w", encoding="utf-8"), ensure_ascii=False, indent=0)
print("ledger after", md5(LEDGER), "| decisions -> work/t3_writeback_decisions.json")
print("ASSERT:", "FAIL " + str(bad[:20]) if bad else "OK")
sys.exit(1 if bad else 0)
