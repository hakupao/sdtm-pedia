# stratified sample (seed 20261126) of S-TYPO plan edits; locate in PDF via pdftotext -bbox; crop render per sample
import json,random,re,subprocess,collections,os,html
REPO='/Volumes/DevSSD/Project/sdtm-pedia'; S=os.environ.get('RV_OUT',os.path.dirname(os.path.abspath(__file__))); X=os.path.dirname(os.path.abspath(__file__))
PDF={'ig':REPO+'/source/cdisc/SDTMIG v3.4 (no header footer).pdf','sv':REPO+'/source/cdisc/SDTM_v2.0.pdf'}
P=[json.loads(l) for l in open(REPO+'/.work/10_tier_b_repair/work/t2_batches/S-TYPO.plan.jsonl')]
F=[json.loads(l) for l in open(REPO+'/.work/10_tier_b_repair/work/t2_batches/S-TYPO.fixed.jsonl')]
def strat(p):
    c=p['class']
    if p in F or any(p['file']==q['file'] and p['line']==q['line'] and p['col']==q['col'] for q in F):
        return 'fixed-ch04' if 'ch04' in p['file'] else 'sup'
    return {'dq:straight->left':'dqL','dq:straight->right':'dqR','sq:straight->right':'sq'}.get(c, c.split(':')[0])
G=collections.defaultdict(list)
for p in P: G[strat(p)].append(p)
N={'dqL':6,'dqR':6,'sq':6,'space':4,'dash':6,'ell':4,'sup':2,'fixed-ch04':3,'dashpair':0,'minus':0}
rnd=random.Random(20261126); out=[]
for k in sorted(G):
    g=G[k]; n=min(N.get(k,len(g)),len(g)); out+= [dict(p,strat=k) for p in rnd.sample(g,n)]
print({k:len(v) for k,v in G.items()}, len(out))
bbcache={}
def words(pg):
    if pg not in bbcache:
        t=subprocess.run(['pdftotext','-bbox','-f',str(pg),'-l',str(pg),PDF['ig'],'-'],capture_output=True,text=True).stdout
        bbcache[pg]=[(float(a),float(b),float(c),float(d),html.unescape(w)) for a,b,c,d,w in re.findall(r'xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">([^<]*)<',t)]
    return bbcache[pg]
an=lambda s: re.sub(r'[^A-Za-z0-9]','',s)
res=[]
for i,p in enumerate(out):
    H=subprocess.run(['git','-C',REPO,'show','HEAD:'+p['file']],capture_output=True,text=True).stdout.split('\n')[p['line']-1]
    c=p['col']; left=an(H[max(0,c-30):c])[-8:]; right=an(H[c+len(p['before']):c+40])[:8]
    W=words(p['pdf_page']); best=None
    # find consecutive words whose alnum concat contains left+right
    for j in range(len(W)):
        s=''; 
        for k in range(j,min(j+8,len(W))):
            s+=an(W[k][4])
            if (left+right) in s: best=(j,k); break
        if best: break
    ent=dict(i=i,strat=p['strat'],file=p['file'].split('knowledge_base/')[1],line=p['line'],before=p['before'],after=p['after'],page=p['pdf_page'],kbctx=H[max(0,c-25):c+25])
    if best:
        ws=W[best[0]:best[1]+1]; ent['pdf_words']=' '.join(w[4] for w in ws)
        x0=min(w[0] for w in ws)-60; y0=min(w[1] for w in ws)-3; x1=max(w[2] for w in ws)+60; y1=max(w[3] for w in ws)+3
        r=250; f=r/72
        subprocess.run(['pdftoppm','-f',str(p['pdf_page']),'-l',str(p['pdf_page']),'-r',str(r),'-x',str(int(max(0,x0)*f)),'-y',str(int(y0*f)),'-W',str(int((x1-x0)*f)),'-H',str(int((y1-y0)*f)),'-png','-singlefile',PDF['ig'],f'{S}/s{i:02d}'])
    res.append(ent)
json.dump(res,open(S+'/samples.json','w'),ensure_ascii=False,indent=0)
for e in res: print(e['i'],e['strat'],e['file'],e['line'],repr(e['before']),'->',repr(e['after']),'p',e['page'],'| KB:',e['kbctx'],'| PDF:',e.get('pdf_words','NOT FOUND'))
