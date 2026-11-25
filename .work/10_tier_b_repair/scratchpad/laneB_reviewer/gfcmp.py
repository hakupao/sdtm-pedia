import re,collections,sys
R="/Volumes/DevSSD/Project/sdtm-pedia"
L=open(R+"/.work/10_tier_b_repair/work/pdf_pages/ig34_p0226.txt").read().splitlines()
# find gf.xpt table start (line 8 header), rows until blank/text
start=8; rows={}; cur=None
for l in L[start:]:
    m=re.match(r"^(\d+)\s+ABC-123",l)
    if m: cur=int(m.group(1)); rows[cur]=[]
    elif cur is None: continue
    if not l.strip() or re.match(r"^[A-Za-z]{4,}\s",l) and not l.startswith(" "):
        if not m: 
            if not l.strip(): continue
    if cur: rows[cur]+=l.split()
K=open(R+"/knowledge_base/domains/GF/examples.md").read().splitlines()
for i in range(85,102):
    l=K[i]
    if not l.startswith("|"): break
    cells=[c.strip() for c in l.strip("|").split("|")]
    n=int(cells[0]); kt=collections.Counter(" ".join(cells).split())
    pt=collections.Counter(rows.get(n,[]))
    # join split tokens: compare concatenated strings
    ks="".join(sorted(" ".join(cells).split())); 
    print(n, "KB-only:",dict(kt-pt), "PDF-only:",dict(pt-kt))
