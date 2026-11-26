# reviewer mutation suite: each mutant = working-tree KB copy + one planted defect; run writer gate (both modes) + reviewer gate
import os,shutil,subprocess,sys,re
REPO='/Volumes/DevSSD/Project/sdtm-pedia'; S=os.environ.get('RV_OUT',os.path.dirname(os.path.abspath(__file__))); X=os.path.dirname(os.path.abspath(__file__)); W=REPO+'/.work/10_tier_b_repair'
PLAN=W+'/work/t2_batches/S-TYPO.plan.jsonl'
def M(f,ln,old,new,nth=1): return (f,ln,old,new)
MUT=[('V0 control (no mutation)',None),
 ('V1 open quote written as close (MH as:31 “Y”->”Y”)',('domains/MH/assumptions.md',31,'“Y”','”Y”')),
 ('V2 registry span B-IS T-6 hyphen->en (closed-table legal)',('domains/IS/examples.md',205,'AUREUS-EPITOPE','AUREUS–EPITOPE')),
 ('V3 registry span B-MK T-1 2nd occurrence 76-95->76–95',('domains/MK/examples.md',57,'76-95%','76–95%')),
 ('V4 apostrophe -> left single quote (DS ex:73 789102’s)',('domains/DS/examples.md',73,'789102’s','789102‘s')),
 ('V5 heading straight->curly quote (ch04:290)',('chapters/ch04_general_assumptions.md',290,'"Subject"','“Subject”')),
 ('V6 bold pseudo-heading quote (TA ex:871)',('domains/TA/examples.md',871,'"options"','“options”')),
 ('V7 inline code quote (PP ex:163)',('domains/PP/examples.md',163,'`RELID = "1"`','`RELID = “1”`')),
 ('V8 --VAR prefix -> en dash (AE as:78)',('domains/AE/assumptions.md',78,'--','–')),
 ('V9 close quote written as open (DS as:32 EVENT”->EVENT“)',('domains/DS/assumptions.md',32,'EVENT”','EVENT“')),
]
rows=[]
for name,m in MUT:
    d=f'{S}/mut/kb'; shutil.rmtree(f'{S}/mut',ignore_errors=True); shutil.copytree(REPO+'/knowledge_base',d,ignore=shutil.ignore_patterns('.*'))
    if m:
        f,ln,a,b=m; p=f'{d}/{f}'; L=open(p).read().split('\n')
        assert a in L[ln-1],(name,L[ln-1][:120]); L[ln-1]=L[ln-1].replace(a,b,1); open(p,'w').write('\n'.join(L))
    r1=subprocess.run(['python3',W+'/scripts/t2s/typo_assert.py',d],capture_output=True,text=True).returncode
    r2=subprocess.run(['python3',W+'/scripts/t2s/typo_assert.py',d,'--plan',PLAN],capture_output=True,text=True).returncode
    r3=subprocess.run(['python3',X+'/rv_check.py',d],capture_output=True,text=True).returncode
    r4=subprocess.run(['python3',X+'/rv_dir2.py',d],capture_output=True,text=True).returncode
    fmt=lambda r:'PASS' if r==0 else 'FAIL'
    rows.append((name,fmt(r1),fmt(r2),fmt(r3),fmt(r4))); print(rows[-1],flush=True)
