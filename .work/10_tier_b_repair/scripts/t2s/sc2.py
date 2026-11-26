# usage: sc2.py SCRATCH DOM p1[:hdrIdx],p2,...   (bbox per-column compare; hdrIdx picks which header on page, default last)
import re,sys,html,unicodedata
S=sys.argv[1]; dom=sys.argv[2]; specs=sys.argv[3].split(',')
R='/Volumes/DevSSD/Project/sdtm-pedia/knowledge_base/domains/%s/spec.md'%dom
def norm(s):
    s=unicodedata.normalize('NFKC',s)
    for a,b in [('‘',"'"),('’',"'"),('“','"'),('”','"'),('–','-'),('—','-'),('‑','-')]: s=s.replace(a,b)
    return re.sub(r'\s+',' ',s).strip()
order=['name','label','type','ct','role','notes','core']
rows=[];foot={}
for sp in specs:
    p,_,hi=sp.partition(':'); p=int(p)
    W=[(float(m[1]),float(m[2]),float(m[3]),html.unescape(m[5])) for m in re.finditer(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">(.*?)</word>',open(f'{S}/bb_{p}.html').read())]
    lines={}
    for w in W: lines.setdefault(round(w[1]),[]).append(w)
    hdrs=sorted({round(w[1]) for w in W if w[3]=='Variable' and w[0]<80})
    hdrs=[h for h in hdrs if any(x[3]=='Label' for x in W if abs(x[1]-h)<2)]
    if not hdrs: hy=-20; print('NOTE p%d no header, reuse prev column x'%p)
    else:
     hy=hdrs[int(hi)] if hi else hdrs[-1]
     H=[w for w in W if abs(w[1]-hy)<2]
     def hx(t): return [w[0] for w in H if w[3]==t]
     xs={'name':hx('Variable')[0],'label':hx('Variable')[1],'type':hx('Type')[0],'ct':hx('Controlled')[0],'role':hx('Role')[0],'notes':hx('CDISC')[0],'core':hx('Core')[0]}
    bounds=[xs[k]-3 for k in order]
    # stop: footnote line (starts '1In' / 'In this column'), heading line 'XX –', next header, copyright
    stops=[]
    for y,L in lines.items():
        L=sorted(L); t=' '.join(w[3] for w in L)
        if y<=hy+5: continue
        if L[0][0]<80 and (re.match(r'^1? ?In this column',t) or re.match(r'^[A-Z]{2} – ',t) or t.startswith('©') or (t.startswith('Variable') and 'Label' in t)): stops.append(y)
        if re.match(r'^\d+(\.\d+)+ ',t) and L[0][0]<80: stops.append(y)
    ylim=min(stops+[9999])-1
    for y,L in lines.items():
        t=' '.join(w[3] for w in sorted(L))
        if y>hy and re.match(r'^1? ?In this column',t): foot[p]=t
    body=[w for w in W if w[1]>hy+15 and w[1]<ylim]
    def col(w):
        c=0
        for i,b in enumerate(bounds):
            if w[0]>=b: c=i
        return order[c]
    starts=sorted([w for w in body if col(w)=='name' and re.match(r'^[A-Z][A-Z0-9]+$',w[3])],key=lambda w:w[1])
    for i,s in enumerate(starts):
        y0=s[1]-1; y1=starts[i+1][1]-1 if i+1<len(starts) else 9999
        r={k:[] for k in order}
        for w in sorted([w for w in body if y0<=w[1]<y1],key=lambda w:(round(w[1]),w[0])): r[col(w)].append(w[3])
        rows.append({k:' '.join(v) for k,v in r.items()}|{'page':p})
kb=open(R).read()
blocks=re.findall(r'### (\S+)\n(.*?)(?=\n### |\n---)',kb,re.S)
K={}
for n,b in blocks:
    d={}
    for m in re.finditer(r'- \*\*(.+?):\*\* ?(.*)',b): d[m[1]]=m[2]
    K[n]=d
pn=[r['name'] for r in rows]; kn=list(K)
print('pdf vars',len(rows),'kb vars',len(K),'order same:',pn==kn)
if pn!=kn: print('PDF',pn); print('KB ',kn)
ordbad=[n for n in kn if K[n].get('Order','')!=str(kn.index(n)+1)]
print('KB Order field mismatches:',ordbad)
for r in rows:
    k=K.get(r['name'],{}); out=[]
    for f,kf in [('label','Label'),('type','Type'),('ct','Controlled Terms'),('role','Role'),('core','Core'),('notes','CDISC Notes')]:
        a=re.sub(r'\s','',norm(r[f])); b=re.sub(r'\s','',norm(k.get(kf,'')))
        if a!=b: out.append(f'{f}: PDF[{norm(r[f])}] KB[{norm(k.get(kf,""))}]')
    print(r['page'],r['name'],'OK' if not out else ' || '.join(out))
print('FOOT',foot)
