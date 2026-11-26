#!/usr/bin/env python3
"""One-off fixation (attempt 4 可复现性修复): write work/t3_k3b_out_of_scope_keep.json from work/t3_rules.json
(K3b_keep_a3 = 21 out-of-§5.0 K3b atoms decided in attempt 3 and audited; T4_ONLY = 3 atoms the audit named).
Each entry carries atom_id / action / registry / rule / pdf (page:line + token) / kb (file:line + token).
t3_writeback.py then reads only this JSON (no attempt-3 output, no hard-coded ids) and re-asserts pdf/kb lines.
Run once; afterwards the JSON is the source. Usage: python3 -I .work/10_tier_b_repair/scripts/t3/t3_build_keep.py
"""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from t3_common import ROOT, W, lj, norm, norm_pdf
R = json.load(open(f"{W}/t3_rules.json"))
A = {x["atom_id"]: x for x in lj(f"{W}/pdf_atoms.jsonl")}
REG = {r["id"]: r for r in lj(f"{W}/t2_pdf_typo_registry.jsonl")}
CJK = re.compile(r"[一-鿿×]")
def pdf_lines(src, p):
    f = f"{W}/pdf_pages/{src}_p{p:04d}.txt"
    return [norm_pdf(l) for l in open(f, encoding="utf-8").read().splitlines()] if os.path.exists(f) else []
def kb_line_text(f, n):
    L = open(f"{ROOT}/{f}", encoding="utf-8").read().splitlines()
    return norm(L[n - 1]) if 0 < n <= len(L) else ""
out = {"_note": "attempt 4 可复现性修复 (审计 A4-5.1): 范围外 K3b 保留 21 条 (action=keep_k3b) + 审计点名仅登记 3 条 (action=t4_only). "
                "t3_writeback.py 只读本清单; 每条运行时断言 pdf.token ⊂ norm(PDF 行) 且 kb.token ⊂ norm(KB 行). 生成: scripts/t3/t3_build_keep.py (一次性)."}
T4_ONLY = ["ig34_p0082_a025", "ig34_p0342_a006", "ig34_p0342_a007"]
PDF_VALUE = {"B-OE T-1": ["idvaral"], "B-RS T-2": ["will contained"], "B-RS T-1": ["repsonse"], "B-SR T-1 (examples)": ["bau ml"],
             "B-SC T-1": ["20-17-04-01"], "B-MK T-2": ["replacement/"], "B-PCPP T-5": ["123-1001 ppseq 1"]}
for i, action in [(i, "keep_k3b") for i in R["K3b_keep_a3"]] + [(i, "t4_only") for i in T4_ONLY]:
    why = (R["K3b_why"].get(i) or [""])
    regs = sorted({w.split(":")[0] for w in why} | set(R["K3b_out_of_scope"].get(i, [])))
    r = REG[regs[0]]
    rule = why[0].split(":")[1].split("(")[0] if why[0] else "a"
    src = i.split("_")[0]
    # KB side: registry kb_text_span on (or nearest to) kb_line_now
    kt = norm(r["kb_text_span"]).strip(" |")
    L = open(f"{ROOT}/{r['kb_file']}", encoding="utf-8").read().splitlines()
    cand = [n for n, l in enumerate(L, 1) if kt and kt in norm(l)]
    kn = min(cand, key=lambda n: abs(n - int(r["kb_line_now"]))) if cand else int(r["kb_line_now"])
    # PDF side: a PDF-side token of the registry (pdf_value minus Chinese/locators) on the registry page, else atom words
    toks = [t for t in re.findall(r"[a-z0-9][a-z0-9/._+-]*[a-z0-9]", norm(CJK.sub(" ", r["pdf_value"]))) if len(t) >= 4]
    # prefer the deviating PDF-side value: the rule-(a) token, the explicit PDF value, then other pdf_value tokens
    wt = re.findall(r"\['([^']+)'", why[0]) if rule == "a" else []
    toks = wt + PDF_VALUE.get(regs[0], []) + [t for t in toks if t not in kt] + toks
    pt, pl = None, None
    for t in toks + [" ".join(norm(A[i]["verbatim"]).split()[:3])]:
        for pg in (r["pdf_page"], A[i]["page"], A[i]["page"] + 1):
            for n, l in enumerate(pdf_lines(src, pg), 1):
                if t and t in l:
                    pt, pl = t, f"{src}_p{pg:04d}:{n}"
                    break
            if pt: break
        if pt: break
    out[i] = dict(action=action, registry=regs, rule=rule, why=why,
                  pdf=dict(line=pl, token=pt), kb=dict(line=f"{r['kb_file']}:{kn}", token=kt or None))
json.dump(out, open(f"{W}/t3_k3b_out_of_scope_keep.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
miss = [i for i, v in out.items() if not i.startswith("_") and (not v["pdf"]["line"] or not v["kb"]["token"] or v["kb"]["token"] not in kb_line_text(*[v["kb"]["line"].rsplit(":", 1)[0], int(v["kb"]["line"].rsplit(":", 1)[1])]))]
print("entries:", len(out) - 1, "incomplete:", miss)
