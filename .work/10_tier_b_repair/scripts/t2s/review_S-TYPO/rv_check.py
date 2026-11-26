#!/usr/bin/env python3
# Independent S-TYPO reviewer gate (does not import writer code). usage: rv_check.py KB_ROOT
import sys, os, re, json, subprocess, collections
REPO='/Volumes/DevSSD/Project/sdtm-pedia'; W=REPO+'/.work/10_tier_b_repair'
KB=sys.argv[1]
def git(*a, check=True): return subprocess.run(['git','-C',REPO,*a],capture_output=True,text=True,check=check).stdout
# approved fixed-position substitutions (main-control ruling, hard-coded, not read from writer's fixed.jsonl)
APPROVED={('chapters/ch04_general_assumptions.md',1101):[('−','-')],
          ('chapters/ch04_general_assumptions.md',1485):[(' -- ',' – ')],
          ('chapters/ch04_general_assumptions.md',1514):[(' -- ',' – ')],
          ('chapters/ch08_relationships.md',96):[('^1^ ','¹')],('chapters/ch08_relationships.md',212):[('^1^ ','¹')],
          ('chapters/ch08_relationships.md',363):[('^1^ ','¹')],('chapters/ch08_relationships.md',438):[('^1^ ','¹')]}
TBL=str.maketrans({'’':"'",'‘':"'",'“':'"','”':'"','–':'-','—':'-'})
def norm(s): return s.replace('…','...').translate(TBL)
errs=[]; stats=collections.Counter(); changes=[]
headfiles={f[len('knowledge_base/'):] for f in git('ls-tree','-r','--name-only','HEAD','knowledge_base/').split()}
tree=set()
for d,_,fs in os.walk(KB):
    for f in fs:
        r=os.path.relpath(os.path.join(d,f),KB)
        if not any(p.startswith('.') for p in r.split('/')): tree.add(r)
for f in sorted(tree^headfiles): errs.append(f'(c) file added/removed {f}')
reg=collections.defaultdict(list)
for l in open(W+'/work/t2_pdf_typo_registry.jsonl'):
    r=json.loads(l); reg[r['kb_file'][len('knowledge_base/'):]].append(r)
def okscope(f): return re.fullmatch(r'chapters/[^/]+\.md|domains/[^/]+/[^/]+\.md|model/[^/]+\.md',f) is not None
for f in sorted(tree&headfiles):
    raw_new=open(os.path.join(KB,f),'rb').read()
    raw_old=subprocess.run(['git','-C',REPO,'show','HEAD:knowledge_base/'+f],capture_output=True,check=True).stdout
    if raw_new==raw_old: continue
    stats['files']+=1
    if not okscope(f): errs.append(f'(c) out-of-scope changed {f}'); continue
    old=raw_old.decode(); new=raw_new.decode()
    Lo,Ln=old.split('\n'),new.split('\n')
    if len(Lo)!=len(Ln): errs.append(f'(a) line count {f}'); continue
    # registry spans: every occurrence position (whole file) must survive identical
    for r in reg.get(f,[]):
        sp=r['kb_text_span']
        po=[m.start() for m in re.finditer(re.escape(sp),old)]; pn=[m.start() for m in re.finditer(re.escape(sp),new)]
        if len(po)!=len(pn): errs.append(f'(b) registry span count {f} {r["id"]} {len(po)}->{len(pn)}')
        for i,(o,n) in enumerate(zip(Lo,Ln)):
            if o!=n and o.count(sp)!=n.count(sp): errs.append(f'(b) registry span altered {f}:{i+1} {r["id"]}')
        # also: fragment matched on normalized text (catches edits inside span that keep... no: a typo change inside span alters exact count)
    fence=False
    for i,(o,n) in enumerate(zip(Lo,Ln)):
        isf=bool(re.match(r'\s*(```|~~~)',o))
        infence=fence or isf
        if isf: fence=not fence
        if o==n: continue
        stats['lines']+=1; loc=f'{f}:{i+1}'
        if infence: errs.append(f'(b) code fence line changed {loc}')
        if o.lstrip().startswith('#'): errs.append(f'(b) heading changed {loc}')
        if re.fullmatch(r'\s*\*\*[^*]+\*\*:?\s*',o): errs.append(f'(b) bold pseudo-heading changed {loc}')
        if re.match(r'\s*>\s*KB note',o): errs.append(f'(b) KB note changed {loc}')
        o2=o
        for a,b in APPROVED.get((f,i+1),[]):
            if o2.count(a)!=1: errs.append(f'(a) approved sub not unique {loc}')
            o2=o2.replace(a,b,1); stats['approved']+=1
        # (a) closed table only: normalized, whitespace-free strings identical
        if re.sub(r'\s','',norm(o2))!=re.sub(r'\s','',norm(n)): errs.append(f'(a) non-table change {loc}')
        # whitespace changes only adjacent to – / — in new
        if norm(o2)!=norm(n):
            a_,b_=norm(o2),norm(n)
            import difflib
            for tag,i1,i2,j1,j2 in difflib.SequenceMatcher(None,a_,b_,autojunk=False).get_opcodes():
                if tag=='equal': continue
                if (a_[i1:i2]+b_[j1:j2]).strip(' '): errs.append(f'(a) odd ws diff {loc}'); continue
                ctx=n[max(0,j1-1):j2+1]
                if '–' not in ctx and '—' not in ctx: errs.append(f'(a) space change not at en/em dash {loc}')
        # character class identity per unit: walk aligned non-space chars
        so=[c for c in o2.replace('...','…') if not c.isspace()]; sn=[c for c in n.replace('...','…') if not c.isspace()]
        if len(so)!=len(sn): errs.append(f'(a) unit count {loc}'); continue
        for k,(x,y) in enumerate(zip(so,sn)):
            if x!=y: changes.append((f,i+1,x,y))
        # (b) protected tokens identical
        for rx,name in ((r'`[^`]*`','inline code'),(r'https?://\S+|www\.\S+','URL'),(r'\]\([^)]*\)','link target'),
                        (r'--[A-Z][A-Z0-9]*','--VAR'),(r'\([A-Z0-9_]+\) C\d+','(SHORT) Cxxxx'),(r'<!--.*?-->','comment')):
            if re.findall(rx,o)!=re.findall(rx,n): errs.append(f'(b) {name} changed {loc}')
        if re.match(r'^\s*([-*+]|\d+\.)\s',o) and re.match(r'^\s*([-*+]|\d+\.)\s',o).group(0)!=n[:len(re.match(r'^\s*([-*+]|\d+\.)\s',o).group(0))]:
            errs.append(f'(b) list marker changed {loc}')
        if o.count('|')!=n.count('|'): errs.append(f'(b) pipe count {loc}')
    # (d) spec.md DOMAIN CT and (SHORT) Cxxxx file-wide
    if f.endswith('spec.md'):
        if re.findall(r'\([A-Z0-9_]+\) C\d+',old)!=re.findall(r'\([A-Z0-9_]+\) C\d+',new): errs.append(f'(d) CT notation changed {f}')
        def dom(t):
            m=re.search(r'(?ms)^#+ .*?\bDOMAIN\b.*?(?=^#+ )',t); return m.group(0) if m else None
        if dom(old)!=dom(new): errs.append(f'(d) DOMAIN block changed {f}')
cls=collections.Counter((x,y) for _,_,x,y in changes)
print('changed files',stats['files'],'lines',stats['lines'],'unit changes',len(changes),'approved',stats['approved'])
for k,v in sorted(cls.items(),key=lambda x:-x[1]): print('  ',repr(k[0]),'->',repr(k[1]),v)
json.dump(changes,open(os.environ.get('RV_OUT','/tmp')+'/changes_'+os.path.basename(KB.rstrip('/'))+'.json','w'),ensure_ascii=False)
for e in errs[:40]: print('  FAIL',e)
print('violations',len(errs)); print('PASS' if not errs else 'FAIL'); sys.exit(1 if errs else 0)
