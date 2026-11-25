import json
B="/Volumes/DevSSD/Project/sdtm-pedia/.work/10_tier_b_repair/work/triage"
a=[json.loads(l) for l in open(f"{B}/lane_B.v0_before_rewrite.jsonl")]
b=[json.loads(l) for l in open(f"{B}/lane_B.jsonl")]
print("order same:",[r['atom_id'] for r in a]==[r['atom_id'] for r in b])
da={r['atom_id']:r for r in a}; db={r['atom_id']:r for r in b}
print("ids only v0",set(da)-set(db),"only new",set(db)-set(da))
def flat(d,p=""):
    o={}
    for k,v in d.items():
        if isinstance(v,dict): o.update(flat(v,p+k+"."))
        else: o[p+k]=v
    return o
for i in da:
    fa,fb=flat(da[i]),flat(db[i])
    ch=[k for k in set(fa)|set(fb) if fa.get(k)!=fb.get(k)]
    if ch: print(i,sorted(ch), {k:(fa.get(k),fb.get(k)) for k in ch if k!='evidence.pdf_quote_short'})
