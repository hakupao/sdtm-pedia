import json, random
W='/Volumes/DevSSD/Project/sdtm-pedia/.work/10_tier_b_repair'
P=[json.loads(l) for l in open(f'{W}/work/t2_batches/S-TYPO.plan.jsonl')]
def stratum(r):
    c=r['class']
    if c=='dq:straight->left': return 'dq_open'
    if c=='dq:straight->right': return 'dq_close'
    if c.startswith('sq:'): return 'sq'
    if c=='space:del@—': return 'em_space'
    if c.startswith('dash:'): return 'dash'
    if c.startswith('ell:'): return 'ell'
    if c.startswith('sup:'): return 'sup'
    return 'ch04_fixed'  # minus + dashpair
Q={'dq_open':6,'dq_close':6,'sq':6,'em_space':3,'dash':3,'ell':2,'sup':2,'ch04_fixed':1}
rng=random.Random(20261126)
for i,r in enumerate(P): r['idx']=i
S=[]
for k in Q:
    pool=[r for r in P if stratum(r)==k]
    S+=rng.sample(pool,Q[k])
rest=[r for r in P if r not in S]
S+=rng.sample(rest,30-len(S))
for r in S: print(json.dumps({'idx':r['idx'],'stratum':stratum(r),'file':r['file'],'line':r['line'],'col':r['col'],'before':r['before'],'after':r['after'],'pdf_page':r['pdf_page']},ensure_ascii=False))
R=[json.loads(l) for l in open(f'{W}/work/t2_batches/S-TYPO.residual.jsonl')]
rng2=random.Random(20261126)
for i in rng2.sample(range(len(R)),10): print('RES',i,json.dumps(R[i],ensure_ascii=False))
