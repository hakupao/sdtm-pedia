import json,sys,re
R="/Volumes/DevSSD/Project/sdtm-pedia"
B=R+"/.work/10_tier_b_repair/work"
atoms={}
for l in open(B+"/pdf_atoms.jsonl"):
    a=json.loads(l); atoms[a["atom_id"]]=a
rows={json.loads(l)["atom_id"]:json.loads(l) for l in open(B+"/triage/lane_B.jsonl")}
plan=json.load(open(B+"/triage/review_lane_B.plan.json"))
packs={}
import glob
for f in glob.glob(B+"/t1_packs/pack_01[0-7].json"):
    for a in json.load(open(f))["atoms"]: packs[a["atom_id"]]=a
def norm(s): return re.sub(r"[^a-z0-9]+"," ",s.lower()).strip()
def pdf_lines(aid,txt):
    a=atoms.get(aid)
    pg=a["page"] if a else rows[aid]["evidence"]["pdf_page"]
    src="ig34" if aid.startswith("ig34") else "sv20"
    try: lines=open(f"{B}/pdf_pages/{src}_p{pg:04d}.txt").read().splitlines()
    except Exception as e: return [f"nopage {e}"]
    toks=[t for t in norm(txt).split() if len(t)>2][:8]
    best=[]
    for i,l in enumerate(lines):
        n=norm(l); sc=sum(t in n for t in toks)
        best.append((sc,i))
    best.sort(reverse=True)
    out=[]
    for sc,i in best[:1]:
        for j in range(max(0,i-1),min(len(lines),i+2)): out.append(f"  P{pg}:{j+1}: {lines[j][:220]}")
    return out
def kb(loc,ctx=1):
    if not loc: return []
    m=re.match(r"(.*?):(\d+)(?:-(\d+))?",loc)
    if not m: return [f"  badloc {loc}"]
    f,s,e=m.group(1),int(m.group(2)),int(m.group(3) or m.group(2))
    if not f.startswith("knowledge_base"): f="knowledge_base/"+f
    try: L=open(R+"/"+f).read().splitlines()
    except Exception as ex: return [f"  NOFILE {f}"]
    return [f"  K{j+1}: {L[j][:260]}" for j in range(max(0,s-1-ctx),min(len(L),e+ctx))]
ids=sys.argv[1:]
for aid in ids:
    r=rows[aid]; a=atoms.get(aid,{}); p=packs.get(aid,{})
    ev=r["evidence"]
    print(f"=== {aid} [{a.get('atom_type')}] {a.get('parent_section','')[:50]} W={r['class']}/{r['confidence']} pre={p.get('prefilter_class')} spec={p.get('spec_row')}")
    print("  ATOM:",a.get("verbatim","")[:300])
    print("  Q:",ev["pdf_quote_short"][:200]); print("  LOC:",ev["kb_loc"],"| R:",ev["reason"][:400])
    for x in pdf_lines(aid,a.get("verbatim") or ev["pdf_quote_short"]): print(x)
    for x in kb(ev["kb_loc"]): print(x)
