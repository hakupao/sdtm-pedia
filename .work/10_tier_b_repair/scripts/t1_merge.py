"""T1.4 merge: writer class, overridden by reviewer class where reviewer disagreed (last review row per atom wins),
then t1_errata.json (kb_loc / pending_user), then t1_rulings.json (user rulings R1/R2/R4; skip with --no-rulings).
Run from repo root: python3 -I .work/10_tier_b_repair/scripts/t1_merge.py [--no-rulings] [--out PATH]"""
import json, collections, pathlib, argparse
B = pathlib.Path(__file__).resolve().parent.parent / 'work'
ap = argparse.ArgumentParser(); ap.add_argument('--no-rulings', action='store_true'); ap.add_argument('--out', default=str(B/'triage_merged.json'))
args = ap.parse_args()
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
if not args.no_rulings:
    RU = json.load(open(B/'t1_rulings.json'))['atoms']
    byid = {r['atom_id']: r for r in out}
    assert set(RU) <= set(byid), set(RU) - set(byid)
    before = {a: r['final_class'] for a, r in byid.items()}
    for a, e in RU.items():
        r = byid[a]
        assert r['final_class'] == e['from'], (a, r['final_class'], e['from'])
        r['final_class'] = e['to']; r['src'] = 'ruling:' + e['rule']
        if e['to'] == 'IE':
            r['ie_cat'] = e.get('ie_cat', r['ie_cat'])
        if e.get('target'): r['target'] = e['target']
        if e.get('t2_recheck'): r['t2_recheck'] = True
        if e.get('note'): r['ruling_note'] = e['note']
    for r in out:
        if r['final_class'] == 'IE_CAND':
            r['final_class'] = 'IE'                       # R4: IE list acked as a whole
        if r['final_class'] != 'IE':
            r['ie_cat'] = None
    changed = {a for a in byid if before[a] != byid[a]['final_class'] and not (before[a] == 'IE_CAND' and byid[a]['final_class'] == 'IE')}
    expect = {a for a, e in RU.items() if e['from'] != e['to'] and not (e['from'] == 'IE_CAND' and e['to'] == 'IE')}
    assert changed == expect, (changed ^ expect)
    assert len(out) == 1461 and not any(r['final_class'] in ('IE_CAND', 'LOCATE') for r in out)
    print('rulings applied', len(RU), 'class changes', len(changed), collections.Counter(e['rule'] for e in RU.values()))
json.dump(out, open(args.out, 'w'), ensure_ascii=False, indent=0)
print('needs_extra_review', sum(r['needs_extra_review'] for r in out), collections.Counter((r['lane'],r['final_class']) for r in out if r['needs_extra_review']))
tot = collections.Counter(r['final_class'] for r in out)
print('total', len(out), dict(tot.most_common()))
print('reviewed', sum(r['reviewed'] for r in out))
print('overrides', len(ovr)); [print(' ', *o) for o in ovr]
ie = collections.Counter(r['ie_cat'] for r in out if r['final_class'] in ('IE_CAND', 'IE'))
print('IE by cat', dict(ie.most_common()))
print('typo', sum(r['pdf_typo_suspect'] for r in out))
