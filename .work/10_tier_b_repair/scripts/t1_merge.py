"""T1.4 merge: writer class, overridden by reviewer class where reviewer disagreed (last review row per atom wins).
Run from repo root: python3 -I .work/10_tier_b_repair/scripts/t1_merge.py"""
import json, collections, pathlib
B = pathlib.Path(__file__).resolve().parent.parent / 'work'
out, cnt, ovr = [], collections.Counter(), []
lane_of = {}
for L in 'ABCD':
    w = {}
    for l in open(B/f'triage/lane_{L}.jsonl'):
        r = json.loads(l); w[r['atom_id']] = r
    rv = {}
    for l in open(B/f'triage/review_lane_{L}.jsonl'):
        r = json.loads(l)
        if r.get('reviewer_class'): rv[r['atom_id']] = r
    for aid, r in w.items():
        c = r['class']; src = 'writer'
        if aid in rv and rv[aid]['reviewer_class'] != c:
            ovr.append((L, aid, c, rv[aid]['reviewer_class'])); c = rv[aid]['reviewer_class']; src = 'reviewer'
        out.append({'atom_id': aid, 'lane': L, 'pack_id': r.get('pack_id'), 'final_class': c, 'src': src,
                    'reviewed': aid in rv, 'pdf_typo_suspect': r.get('pdf_typo_suspect', False),
                    'kb_loc': (rv.get(aid) or {}).get('kb_loc') or r['evidence'].get('kb_loc'),
                    'ie_cat': r['evidence']['reason'].split('IE类别=')[1].split(',')[0].split(' ')[0].rstrip(';') if 'IE类别=' in r['evidence']['reason'] else None})
        cnt[(L, c)] += 1
E = json.load(open(B/'t1_errata.json'))
pre = {json.loads(l)['atom_id']: json.loads(l) for l in open(B/'triage_prefilter.jsonl')}
for r in out:
    a = r['atom_id']
    if a in E['kb_loc']:
        v = E['kb_loc'][a]
        r['kb_loc'] = (r['kb_loc'].split(':')[0] + ':' + v[6:]) if v.startswith('@line:') and r['kb_loc'] else v
    if a in E['pending_user']:
        r['final_class'] = E['pending_user'][a]; r['src'] = 'pending_user'
    p = pre.get(a, {})
    backed = (r['final_class'] == 'IE_CAND' and r['ie_cat'] == 'SPEC_TABLE_ROW' and p.get('prefilter_class') == 'SPEC_MATCH'
              and (p.get('spec_detail') or {}).get('match_via') == 'section_domain') or \
             (r['final_class'] == 'PRESENT' and p.get('prefilter_class') == 'FP_HIT_SECTION')
    r['det_backed'] = bool(backed)
    r['needs_extra_review'] = (not r['reviewed']) and (not backed) and r['final_class'] in ('IE_CAND', 'PRESENT')
json.dump(out, open(B/'triage_merged.json', 'w'), ensure_ascii=False, indent=0)
print('needs_extra_review', sum(r['needs_extra_review'] for r in out), collections.Counter((r['lane'],r['final_class']) for r in out if r['needs_extra_review']))
tot = collections.Counter(r['final_class'] for r in out)
print('total', len(out), dict(tot.most_common()))
print('reviewed', sum(r['reviewed'] for r in out))
print('overrides', len(ovr)); [print(' ', *o) for o in ovr]
ie = collections.Counter(r['ie_cat'] for r in out if r['final_class'] == 'IE_CAND')
print('IE_CAND by cat', dict(ie.most_common()))
print('typo', sum(r['pdf_typo_suspect'] for r in out))
