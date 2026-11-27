#!/usr/bin/env python3
"""T4 seeded samplers (deterministic; no KB / ledger writes).
  gate   : T4.1 N=72 = triage final_class PRESENT/REWRITE_OK/REAL_GAP/VALUE_DIFF/IE x12 (no filter on final verdict)
           + control 12 (§5.0 SCOPE, non-HEADING, pre-T3 & final EXACT/EQUIV, not in t3_writeback_decisions).
  human  : T4.2 N=30 = REWRITE_OK 10 / REAL_GAP 10 / VALUE_DIFF 5 + IE 5 (disjoint from gate)
           + risk layer 12 from work/t3_t4_risk_anchorless.txt (reason 'no governing numbered heading' 8 /
             'atom section has no number' 4; disjoint from gate and human).
  Pools exclude MANUAL_01/02 (no ledger row) and the residual ig34_p0056_a006 (separate user item).
PDF text comes from work/pdf_pages/<page>.txt (pdftotext -layout), located by token overlap; the atom verbatim is
shown separately. KB text is read from the current tree (evidence.hit_file:hit_lines, else registry kb_line_now,
else live valid_hits, else fuzzy locate in candidate files).
Usage: python3 -I .work/10_tier_b_repair/scripts/t4/t4_sample.py   -> work/t4/{gate,human}_sample.jsonl
"""
import json, os, random, re, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "t3"))
from t3_common import ROOT, TB, W, lj, norm, norm_pdf, valid_hits  # noqa: E402

GATE_SEED, HUMAN_SEED, RISK_SEED = 20261127, 20261128, 20261129
EXCL = {"MANUAL_01", "MANUAL_02", "ig34_p0056_a006"}
OUT = f"{W}/t4"
os.makedirs(OUT, exist_ok=True)

A = {x["atom_id"]: x for x in lj(f"{W}/pdf_atoms.jsonl")}
T = {t["atom_id"]: t for t in json.load(open(f"{W}/triage_merged.json"))}
L = {r["pdf_atom_id"]: r for r in lj(f"{W}/coverage_ledger.wc.jsonl")}
PRE = {r["pdf_atom_id"]: r for r in lj(f"{W}/coverage_ledger.wc.pre_t3.jsonl")}
D = json.load(open(f"{W}/t3_writeback_decisions.json"))
ER = json.load(open(f"{W}/t3_errata.json"))
REG = {r["id"]: r for r in lj(f"{W}/t2_pdf_typo_registry.jsonl")}
MD = {m["atom_id"]: m for m in lj(f"{W}/md_atoms.jsonl")}
SCOPE = {(r["source"], r["section_key"]) for r in lj(f"{TB}/inventory.jsonl")} | {("ig34", "§6.3.5.9.3 Relating PP Records to PC Records")}
SEC_T = {(r["source"], r["section_key"]): r.get("md_target_files") or [] for r in lj(f"{W}/section_coverage.wc.baseline.jsonl")}
in_scope = lambda i: (i.split("_")[0], A[i]["parent_section"]) in SCOPE
RISK = [l.rstrip("\n").split("\t") for l in open(f"{W}/t3_t4_risk_anchorless.txt", encoding="utf-8") if l.strip()]
WTOK = re.compile(r"[a-z0-9]+")


def toks(s):
    return WTOK.findall(norm_pdf(s))


def locate(lines, v, maxw=14):
    """Best window (1-based start, end, score): highest token coverage, ties -> shortest window."""
    want = set(toks(v))
    if not want:
        return None
    lt = [set(toks(l)) & want for l in lines]
    best = (0.0, 0, 0, 0)  # score, -width, s, e
    for s in range(len(lines)):
        if not lt[s]:
            continue
        got = set()
        for e in range(s, min(len(lines), s + maxw)):
            got |= lt[e]
            sc = len(got) / len(want)
            if (sc, -(e - s)) > best[:2]:
                best = (sc, -(e - s), s, e)
            if sc == 1.0:
                break
    sc, _, s, e = best
    return (s + 1, e + 1, round(sc, 3)) if sc > 0 else None


def pdf_block(i):
    """Atom page first; if coverage < 0.8 also try page-1 / page+1 (atom page numbers are sometimes off by one)."""
    src, pg = i.split("_")[0], A[i]["page"]
    best = None
    for q in (pg, pg + 1, pg - 1):
        p = f"{W}/pdf_pages/{src}_p{q:04d}.txt"
        if not os.path.exists(p):
            continue
        lines = open(p, encoding="utf-8").read().splitlines()
        loc = locate(lines, A[i]["verbatim"])
        if loc and (not best or loc[2] > best[2][2] + 1e-9):
            best = (q, lines, loc)
        if best and best[2][2] >= 0.8:
            break
    if not best:
        return dict(page_txt=f".work/10_tier_b_repair/work/pdf_pages/{src}_p{pg:04d}.txt", lines=None, score=0, text="")
    q, lines, (s, e, sc) = best
    s0, e0 = max(1, s - 1), min(len(lines), e + 1)
    return dict(page_txt=f".work/10_tier_b_repair/work/pdf_pages/{src}_p{q:04d}.txt", page_used=q, lines=f"{s}-{e}",
                score=sc, text="\n".join(f"{n:>3}| {lines[n - 1].rstrip()}" for n in range(s0, e0 + 1)))


def kb_text(rel, lns, ctx=0):
    p = f"{ROOT}/{rel}"
    if not os.path.exists(p):
        return ""
    raw = open(p, encoding="utf-8").read().splitlines()
    ns = sorted({n for l in lns for n in range(max(1, l - ctx), min(len(raw), l + ctx) + 1)})
    return "\n".join(f"{n:>4}| {raw[n - 1]}" for n in ns)


def kb_block(i):
    d, r = D.get(i, {}), L[i]
    ev = d.get("evidence", {})
    if ev.get("hit_file") and ev.get("hit_lines"):
        return dict(src="decision.evidence.hit", loc=f"{ev['hit_file']}:{','.join(map(str, ev['hit_lines']))}",
                    text=kb_text(ev["hit_file"], ev["hit_lines"][:3]))
    regs = [x for x in (ER["atom_err"].get(i, {}).get("registry") or [])] + \
           [x for x in re.findall(r"[BS]-[\w-]+ (?:T|U|N)-\d+\w?", json.dumps(d, ensure_ascii=False))]
    for g in regs:
        if g in REG and REG[g].get("kb_line_now"):
            g = REG[g]
            return dict(src=f"registry {g['id']} kb_line_now", loc=f"{g['kb_file']}:{g['kb_line_now']}",
                        text=kb_text(g["kb_file"], [int(g["kb_line_now"])]))
    v = norm(A[i]["verbatim"])
    cands = list(dict.fromkeys(ev.get("targets") or []))
    cands += [MD[m]["file"] for m in r.get("md_atom_ids") or [] if m in MD]
    cands += SEC_T.get((i.split("_")[0], A[i]["parent_section"]), [])
    for f in dict.fromkeys(cands):
        hits = valid_hits(f, v, i, A[i]["parent_section"])[0]
        if hits:
            return dict(src="live valid_hits", loc=f"{f}:{','.join(str(h) for h, _ in hits[:3])}",
                        text=kb_text(f, [h for h, _ in hits[:3]]))
    kl = (T.get(i) or {}).get("kb_loc") or ""
    if ":" in kl:
        f, n = kl.rsplit(":", 1)
        p = f"{ROOT}/{f}"
        if os.path.exists(p) and n.isdigit():
            raw = open(p, encoding="utf-8").read().splitlines()
            n = int(n)
            lo = max(0, n - 16)
            loc = locate(raw[lo:n + 15], A[i]["verbatim"], maxw=6)
            if loc and loc[2] >= 0.5:
                return dict(src=f"near triage kb_loc {kl} (score {loc[2]})", loc=f"{f}:{lo + loc[0]}-{lo + loc[1]}",
                            text=kb_text(f, range(lo + loc[0], lo + loc[1] + 1)))
            return dict(src=f"triage kb_loc {kl} (T1 行号, 未定位, 显示 ±2 行)", loc=kl, text=kb_text(f, [n], ctx=2))
    best = None
    for f in dict.fromkeys(cands):
        p = f"{ROOT}/{f}"
        if not os.path.exists(p):
            continue
        loc = locate(open(p, encoding="utf-8").read().splitlines(), A[i]["verbatim"], maxw=6)
        if loc and (not best or loc[2] > best[1][2]):
            best = (f, loc)
    if best and best[1][2] >= 0.5:
        f, (s, e, sc) = best
        return dict(src=f"fuzzy locate (score {sc})", loc=f"{f}:{s}-{e}", text=kb_text(f, range(s, e + 1)))
    return dict(src="none", loc=None, text="")


def row(i, layer):
    t, r, d = T.get(i, {}), L[i], D.get(i, {})
    reg = sorted(set(re.findall(r"[BS]-[\w-]+ (?:T|U|N)-\d+\w?", json.dumps(d, ensure_ascii=False))))
    return dict(layer=layer, atom_id=i, page=A[i]["page"], atom_type=A[i]["atom_type"],
                parent_section=A[i]["parent_section"], triage_class=t.get("final_class"), ie_cat=t.get("ie_cat"),
                verdict_pre_t3=PRE.get(i, {}).get("verdict"), verdict_final=r["verdict"], rule=d.get("rule"),
                batch=d.get("batch"), exclusion_reason=r.get("exclusion_reason"),
                errata=ER["atom_err"].get(i), registry=reg, atom_verbatim=A[i]["verbatim"],
                pdf=pdf_block(i), kb=kb_block(i))


def refine_human(x):
    """Human-pack only (gate rows stay byte-identical to what the T4.1 reviewers saw): show every hit line,
    flag approximate KB pointers, locate IE spec rows by variable name, inline PDF_TYPO registry rows."""
    i, d = x["atom_id"], D.get(x["atom_id"], {})
    ev = d.get("evidence") or {}
    k = x["kb"]
    if k["src"] == "decision.evidence.hit":
        hl = ev["hit_lines"]
        k["n_hits"] = len(hl)
        k["text"] = kb_text(ev["hit_file"], hl[:8])
        if len(hl) > 1:
            k["note"] = f"同一文件共 {len(hl)} 处逐字命中 (行 {', '.join(map(str, hl))}); 请按 PDF 所在例/表判断对应的是哪一处" + \
                        (" (只显示前 8 处)" if len(hl) > 8 else "")
    if x["verdict_final"] == "INTENTIONAL_EXCLUDE":
        cells = [c.strip() for c in A[i]["verbatim"].strip().strip("|").split("|")]
        var = next((c for c in cells if re.fullmatch(r"[A-Z][A-Z0-9]{1,7}", c)), None)
        kl = ((T.get(i) or {}).get("kb_loc") or "").rsplit(":", 1)[0]
        hit = None
        if var and kl and os.path.exists(f"{ROOT}/{kl}"):
            raw = open(f"{ROOT}/{kl}", encoding="utf-8").read().splitlines()
            sec = set(toks(A[i]["parent_section"])) - {"and", "the", "of"}
            cand, head = [], ""
            for n, l in enumerate(raw, 1):
                if re.match(r"^#+\s+§?\d", l):  # numbered section heading only ('### Variables' etc. do not reset)
                    head = l
                if re.match(rf"^#+\s+{var}\s*$", l) or re.search(rf"\|\s*{var}\s*\|", l):
                    cand.append((len(sec & set(toks(head))), -n, n))
            hit = max(cand)[2] if cand else None  # the occurrence under the heading closest to the atom's section
        if hit:
            raw = open(f"{ROOT}/{kl}", encoding="utf-8").read().splitlines()
            end = hit
            if raw[hit - 1].startswith("#"):
                while end < len(raw) and not raw[end].startswith("#"):
                    end += 1
            k.update(src=f"按变量名 {var} 定位 (IE 行: KB 以 spec/model 表另一格式承载)", loc=f"{kl}:{hit}-{end}",
                     text=kb_text(kl, range(hit, min(end, hit + 9) + 1)), approx=False)
        else:
            k.update(src="IE 不进 KB, 不显示", loc=None, text="", approx=False)
    elif k["src"].startswith(("near triage", "fuzzy", "triage kb_loc")):
        k["approx"] = True
    if x["pdf"]["score"] < 0.9 or x["pdf"].get("page_used", x["page"]) != x["page"]:
        x["pdf"]["approx"] = True
    regs = list(dict.fromkeys((ev.get("registry") or []) + ((ER["atom_err"].get(i) or {}).get("registry") or []) + x["registry"]))
    rows = []
    for g in regs:
        r = REG.get(g) or next((v for kk, v in REG.items() if kk.startswith(g + " ")), None)
        if r:
            rows.append(dict(id=r["id"], pdf_value=r.get("pdf_value"), kb_value=r.get("kb_value"), handling=r.get("handling"),
                             kb=f"{r['kb_file']}:{r.get('kb_line_now')}", basis=r.get("basis")))
    if rows:
        x["registry_rows"] = rows
    return x


def pick(pool, n, seed):
    pool = sorted(pool)
    return sorted(random.Random(seed).sample(pool, min(n, len(pool))))


cls = lambda c: [i for i, t in T.items() if t["final_class"] == c and i not in EXCL and i in L and i in A]
gate = []
for c in ["PRESENT", "REWRITE_OK", "REAL_GAP", "VALUE_DIFF", "IE"]:
    gate += [row(i, f"gate:{c}") for i in pick(cls(c), 12, GATE_SEED)]
ctrl_pool = [i for i in A if i in L and i not in D and i not in EXCL and in_scope(i) and A[i]["atom_type"] != "HEADING"
             and PRE.get(i, {}).get("verdict") in ("EXACT", "EQUIVALENT") and L[i]["verdict"] in ("EXACT", "EQUIVALENT")]
gate += [row(i, "gate:CONTROL") for i in pick(ctrl_pool, 12, GATE_SEED)]
# supplementary (beyond PLAN N=72, main-controller addition): T3 allowed-set atoms outside triage (T2S / errata), the
# source of most ATOM_ERR / PDF_TYPO that the mapped G-TB3 removes from the denominator. 4 per final verdict.
nontri = [i for i in D if i not in T and i not in EXCL and i in L]
for v in ["ATOM_ERR", "PDF_TYPO", "EXACT"]:
    gate += [row(i, f"gate:SUPP_{v}") for i in pick([i for i in nontri if L[i]["verdict"] == v], 4, GATE_SEED)]
used = {g["atom_id"] for g in gate}
human = []
for c, n in [("REWRITE_OK", 10), ("REAL_GAP", 10), ("VALUE_DIFF", 5), ("IE", 5)]:
    human += [row(i, f"human:{c}") for i in pick([x for x in cls(c) if x not in used], n, HUMAN_SEED)]
used |= {h["atom_id"] for h in human}
for reason, n in [("no governing numbered heading", 8), ("atom section has no number", 4)]:
    pool = [a for a, why, *_ in RISK if why == reason and a not in used and a in L]
    human += [row(i, f"human:RISK_ANCHORLESS") for i in pick(pool, n, RISK_SEED)]
human = [refine_human(x) for x in human]
for name, rows in (("gate", gate), ("human", human)):
    with open(f"{OUT}/{name}_sample.jsonl", "w", encoding="utf-8") as fh:
        for x in rows:
            fh.write(json.dumps(x, ensure_ascii=False) + "\n")
print(f"gate {len(gate)} (control pool {len(ctrl_pool)}) | human {len(human)} | seeds {GATE_SEED}/{HUMAN_SEED}/{RISK_SEED}")
print("pools:", {c: len(cls(c)) for c in ["PRESENT", "REWRITE_OK", "REAL_GAP", "VALUE_DIFF", "IE"]},
      "risk:", {k: sum(1 for _, w, *_ in RISK if w == k) for k in {w for _, w, *_ in RISK}})
for x in gate + human:
    if x["pdf"]["score"] < 0.8 or x["kb"]["src"] == "none":
        print("weak:", x["layer"], x["atom_id"], x["verdict_final"], "pdf", x["pdf"]["score"], "kb", x["kb"]["src"])
