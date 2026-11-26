# derived from work/scratch/t2s_tools/speccmp.py: header line must contain 'Controlled'; header words removed by vocab;
# body stops at footnote ('In this column') / 'XX – Assumptions' / copyright; also checks KB Order sequence; prints full PDF text with -v
import re,sys,html,unicodedata
S=sys.argv[1]; dom=sys.argv[2]; pages=[int(x) for x in sys.argv[3].split(',')]; V='-v' in sys.argv
R='/Volumes/DevSSD/Project/sdtm-pedia/knowledge_base/domains/%s/spec.md'%dom
def norm(s):
    s=unicodedata.normalize('NFKC',s)
    for a,b in [('‘',"'"),('’',"'"),('“','"'),('”','"'),('–','-'),('—','-'),('•',' '),('▪',' ')]: s=s.replace(a,b)
    return re.sub(r'\s+',' ',s).strip()
HV={'Variable','Name','Label','Type','Controlled','Terms,','Codelist','or','Format1','Format¹','Format','1','Role','CDISC','Notes','Core'}
rows=[];xs=None
for p in pages:
    W=[(float(m[1]),float(m[2]),float(m[3]),html.unescape(m[5])) for m in re.finditer(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">(.*?)</word>',open(f'{S}/bb_{p}.html').read())]
    ctl=[w for w in W if w[3]=='Controlled']
    hy=None
    for c in sorted(ctl,key=lambda w:w[1]):
        H=[w for w in W if abs(w[1]-c[1])<2]
        if any(w[3]=='Core' for w in H) and any(w[3]=='CDISC' for w in H):
            hy=c[1]; hx=lambda t:[w[0] for w in H if w[3]==t]
            xs={'name':hx('Variable')[0],'label':hx('Variable')[1],'type':hx('Type')[0],'ct':hx('Controlled')[0],'role':hx('Role')[0],'notes':hx('CDISC')[0],'core':hx('Core')[0]}
            break
    top=hy+1 if hy is not None else 0
    order=['name','label','type','ct','role','notes','core']; bounds=[xs[k]-3 for k in order]
    body=[w for w in W if w[1]>top and not (hy is not None and w[1]<hy+22 and w[3] in HV)]
    ends=[w[1] for w in W if w[1]>top and (w[3].startswith('©') or (w[3]=='this' and w[0]<130) or (w[3]=='Assumptions' and w[0]<130) or (w[3] in ('1In','In') and w[0]<90))]
    ylim=min(ends+[740])-1
    body=[w for w in body if w[1]<ylim]
    def col(w):
        c=0
        for i,b in enumerate(bounds):
            if w[0]>=b: c=i
        return order[c]
    starts=sorted([w for w in body if col(w)=='name' and re.match(r'^[A-Z][A-Z0-9]+$',w[3])],key=lambda w:w[1])
    if starts and rows:
        pre=sorted([w for w in body if w[1]<starts[0][1]-1],key=lambda w:(round(w[1]),w[0]))
        for w in pre: rows[-1][col(w)]=(rows[-1][col(w)]+' '+w[3]).strip()
        if pre: print('CONT p%d -> %s: %s'%(p,rows[-1]['name'],' '.join(w[3] for w in pre)))
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
print('pdf vars',len(rows),'kb vars',len(K))
pn=[r['name'] for r in rows]; print('order same:',pn==list(K.keys()))
if pn!=list(K.keys()): print(pn); print(list(K.keys()))
ords=[K[n].get('Order') for n in K]; print('KB Order 1..n:',ords==[str(i) for i in range(1,len(K)+1)])
for r in rows:
    k=K.get(r['name'],{}); out=[]
    for f,kf in [('label','Label'),('type','Type'),('ct','Controlled Terms'),('role','Role'),('core','Core'),('notes','CDISC Notes')]:
        a=norm(r[f]); b=norm(k.get(kf,''))
        ok=re.sub(r'\s','',a)==re.sub(r'\s','',b)
        if not ok: out.append(f'{f}: PDF[{a}] KB[{b}]')
    print(r['page'],r['name'],'OK' if not out else ' || '.join(out))
    if V: print('   ',{f:r[f] for f in ['label','type','ct','role','core']})
