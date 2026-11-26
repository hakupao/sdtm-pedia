# direction gate over every curly quote that differs from HEAD (tree-based, no plan): context rule; whitelist = PDF-verified errata (MH as:27 x2)
import sys,subprocess,os
REPO='/Volumes/DevSSD/Project/sdtm-pedia'; KB=sys.argv[1]
WL={('domains/MH/assumptions.md',27)}
bad=[]
for f in subprocess.run(['git','-C',REPO,'ls-tree','-r','--name-only','HEAD','knowledge_base/'],capture_output=True,text=True).stdout.split():
    r=f[len('knowledge_base/'):]; p=os.path.join(KB,r)
    if not p.endswith('.md') or not os.path.exists(p): continue
    o=subprocess.run(['git','-C',REPO,'show','HEAD:'+f],capture_output=True,text=True).stdout.split('\n'); n=open(p).read().split('\n')
    for i,(a,b) in enumerate(zip(o,n)):
        if a==b or (r,i+1) in WL: continue
        oc=[c for c in a.replace('...','…') if not c.isspace()]; nc=[c for c in b.replace('...','…') if not c.isspace()]
        # locate changed chars in new line by walking non-space positions
        pos=[k for k,c in enumerate(b) if not c.isspace()]
        for j,(x,y) in enumerate(zip(oc,nc)):
            if x==y or y not in '“”‘’': continue
            k=pos[j]; pv=b[k-1] if k else ' '; nx=b[k+1] if k+1<len(b) else ' '
            ok={'“':(pv.isspace() or pv in '([{|*_—–/=') and not nx.isspace(),
                '”':(not pv.isspace()) and (nx.isspace() or nx in '.,;:)]}|*!?’-—–s'),
                '’':not pv.isspace(),
                '‘':pv.isspace() or pv in '(“'}[y]
            if not ok: bad.append(f'{r}:{i+1} {y} ctx={b[max(0,k-15):k+15]!r}')
for x in bad: print('FAIL',x)
print('PASS' if not bad else 'FAIL'); sys.exit(1 if bad else 0)
