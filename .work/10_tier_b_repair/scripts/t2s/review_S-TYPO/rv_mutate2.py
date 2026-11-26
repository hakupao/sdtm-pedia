import os,shutil,subprocess
REPO='/Volumes/DevSSD/Project/sdtm-pedia'; W=REPO+'/.work/10_tier_b_repair'; S=os.environ['RV_OUT']; X=W+'/scripts/t2s/review_S-TYPO'
PLAN=W+'/work/t2_batches/S-TYPO.plan.jsonl'
MUT=[('V0 control',None),
 ('V1 open->close MH as:31',('domains/MH/assumptions.md',31,'“Y”','”Y”')),
 ('V4 apostrophe->‘ DS ex:73',('domains/DS/examples.md',73,'789102’s','789102‘s')),
 ('V6 bold pseudo-heading TA ex:871',('domains/TA/examples.md',871,'"options"','“options”')),
 ('V9 close->open DS as:32',('domains/DS/assumptions.md',32,'EVENT”','EVENT“')),
 ('N1 plural-possessive ’ ->‘ mid-line ch08:232',('chapters/ch08_relationships.md',232,'variables’ names','variables‘ names')),
 ('N2 close after period -> open FA ex:302',('domains/FA/examples.md',302,'stools.”','stools.“')),
 ('N3 whitelisted line, correct “ -> ” MH as:27',('domains/MH/assumptions.md',27,'if “General','if ”General')),
 ('N4 open after = -> close ch08:42',('chapters/ch08_relationships.md',42,'=“COMBO','=”COMBO')),
 ('N5 ’ (apostrophe) -> ” same class? cross-class DQ (control of class check) FT as:55',('domains/FT/assumptions.md',55,'instrument’s','instrument”s')),
]
for name,m in MUT:
    d=f'{S}/mut2/kb'; shutil.rmtree(f'{S}/mut2',ignore_errors=True); shutil.copytree(REPO+'/knowledge_base',d,ignore=shutil.ignore_patterns('.*'))
    if m:
        f,ln,a,b=m; p=f'{d}/{f}'; L=open(p).read().split('\n'); assert a in L[ln-1],name; L[ln-1]=L[ln-1].replace(a,b,1); open(p,'w').write('\n'.join(L))
    r1=subprocess.run(['python3',W+'/scripts/t2s/typo_assert.py',d],capture_output=True,text=True)
    r2=subprocess.run(['python3',W+'/scripts/t2s/typo_assert.py',d,'--plan',PLAN],capture_output=True,text=True)
    why=[l.strip() for l in r1.stdout.split('\n') if l.strip().startswith('FAIL ')][:1]
    print(name,'| no-plan',['PASS','FAIL'][r1.returncode!=0],'| --plan',['PASS','FAIL'][r2.returncode!=0],'|',why)
