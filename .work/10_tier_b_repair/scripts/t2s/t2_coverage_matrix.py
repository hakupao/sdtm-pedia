#!/usr/bin/env python3
"""T2 coverage matrix (read-only over KB). Run from repo root:
   python3 .work/10_tier_b_repair/work/scratch/t2/global/t2_coverage_matrix.py
Outputs: .work/10_tier_b_repair/work/t2_coverage_matrix.json + evidence/t2_coverage_matrix.md
"""
import json, re, os, glob, subprocess, unicodedata, sys
ROOT = os.getcwd()
TAG = os.environ.get('MATRIX_TAG')  # set -> write to scratch, keep committed evidence untouched
def OUTP(rel):
    if not TAG: return W + '/' + rel
    b = os.path.basename(rel); return W + '/work/scratch/t2/global/' + b.replace('t2_coverage_matrix', 't2_coverage_matrix.' + TAG)
W = '.work/10_tier_b_repair'
KB = 'knowledge_base'

# ---------- normalisation ----------
def norm(s):
    s = unicodedata.normalize('NFKC', s)
    for a, b in (('\u2018', "'"), ('\u2019', "'"), ('\u02bc', "'"), ('\u201c', '"'), ('\u201d', '"'),
                 ('\u2013', '-'), ('\u2014', '-'), ('\u2011', '-'), ('\u2026', '...'), ('\u00a0', ' ')):
        s = s.replace(a, b)
    s = re.sub(r'\\([*_\[\]|#>-])', r'\1', s)
    s = s.replace('**', '').replace('__', '').replace('`', '')
    s = re.sub(r'\s+', ' ', s).strip().lower()
    return s

def norm_line(l):
    l = re.sub(r'^\s*(#+|>+|[-*+]\s|\d+[.)]\s|[a-z][.)]\s)\s*', '', l)
    l = l.replace('|', ' ')
    return norm(l)

def strip_fn(s):
    return re.sub(r'^\s*(\u00b9|\u00b2|\u00b3|[1-3](?=\s?[A-Z]))\s*', '', s)

# ---------- KB corpus ----------
EXCL = ('knowledge_base/terminology/', 'knowledge_base/INDEX.md', 'knowledge_base/ROUTING.md', 'knowledge_base/VARIABLE_INDEX.md')
corpus = {}
for p in sorted(glob.glob(KB + '/**/*.md', recursive=True)):
    if p.startswith(EXCL):
        continue
    lines = open(p, encoding='utf-8').read().split('\n')
    parts, offs, pos = [], [], 0
    for i, l in enumerate(lines):
        n = norm_line(l)
        offs.append(pos); parts.append(n); pos += len(n) + 1
    corpus[p] = (' '.join(parts), offs, lines)

def line_of(offs, i):
    lo, hi = 0, len(offs) - 1
    while lo < hi:
        m = (lo + hi + 1) // 2
        if offs[m] <= i: lo = m
        else: hi = m - 1
    return lo + 1

def kb_find_seq(alist, prefer=None):
    """sequential: short atoms (<40 norm chars) only count if within 15 lines after previous hit in same file"""
    res, anchor = [], None
    for a in alist:
        t = re.sub(r'^(\d+|[a-z]|[ivx]+)[.)]\s+', '', norm(strip_fn(a['verbatim'])))
        if len(t) < 40:
            st = ('SHORT_UNANCHORED', None)
            if anchor:
                f, ln = anchor
                lines = corpus[f][2]
                for k in range(max(0, ln - 1), min(len(lines), ln + 15)):
                    if t in norm_line(lines[k]):
                        st = ('EXACT', f'{f[len(KB)+1:]}:{k+1}'); anchor = (f, k + 1); break
        else:
            st = kb_find(a['verbatim'], prefer)
            anchor = (KB + '/' + st[1].rsplit(':', 1)[0], int(st[1].rsplit(':', 1)[1])) if st[0] == 'EXACT' else None
        res.append(st)
    return res

def kb_find(text, prefer=None, only=False):
    """return (status, loc) status EXACT/PARTIAL/NONE; prefer = path prefix searched first"""
    t = re.sub(r'^(\d+|[a-z]|[ivx]+)[.)]\s+', '', norm(strip_fn(text)))
    if len(t) < 12:
        return ('SHORT', None)
    order = sorted(corpus, key=lambda p: 0 if (prefer and p.startswith(prefer)) else 1)
    if only and prefer:
        order = [p for p in order if p.startswith(prefer)]
    for p in order:
        s, offs, _ = corpus[p]
        i = s.find(t)
        if i >= 0:
            return ('EXACT', f'{p[len(KB)+1:]}:{line_of(offs, i)}')
    k = 45 if len(t) > 90 else max(20, len(t) // 2)
    for frag in (t[:k], t[-k:]):
        for p in order:
            s, offs, _ = corpus[p]
            i = s.find(frag)
            if i >= 0:
                return ('PARTIAL', f'{p[len(KB)+1:]}:{line_of(offs, i)}')
    return ('NONE', None)

# ---------- PDF atoms (IG only, by atom_id prefix) ----------
atoms = []
for l in open(W + '/work/pdf_atoms.jsonl', encoding='utf-8'):
    a = json.loads(l)
    m = re.match(r'ig34_p(\d+)_a(\d+)', a['atom_id'])
    if m:
        a['_k'] = (int(m.group(1)), int(m.group(2)))
        atoms.append(a)
atoms.sort(key=lambda a: a['_k'])
for i, a in enumerate(atoms):
    a['_i'] = i
pages = {}
for p in glob.glob(W + '/work/pdf_pages/ig34_p*.txt'):
    pages[int(re.search(r'p(\d+)', os.path.basename(p)).group(1))] = open(p, encoding='utf-8').read()

# numbered headings (§5-§9 + 1-4 for chapters), monotonic filter
HRE = re.compile(r'^\s*§?\s*(\d{1,2}(?:\.\d{1,2})*)\.?\s+(\S.*)$')
heads, dropped, last = [], [], ()
for a in atoms:
    if a['atom_type'] != 'HEADING' or a['page'] < 7:
        continue
    m = HRE.match(a['verbatim'])
    if not m:
        continue
    num = tuple(int(x) for x in m.group(1).split('.'))
    if num[0] > 10 or num <= last:
        dropped.append((a['atom_id'], a['verbatim'][:60])); continue
    last = num
    heads.append({'num': num, 'id': '.'.join(map(str, num)), 'title': m.group(2).strip(), 'page': a['page'], 'i': a['_i']})
hidx = {h['id']: h for h in heads}

def sec_end(h):
    for h2 in heads:
        if h2['i'] > h['i'] and len(h2['num']) <= len(h['num']):
            return h2
    return None

def sec_range(h):
    e = sec_end(h)
    return (h['page'], e['page'] if e else 446), (e['i'] if e else len(atoms))

def intro_atoms(h):
    out = []
    # extraction sometimes emits a section NOTE box just before its heading on the same page
    j = h['i'] - 1
    pre = []
    while j >= 0 and atoms[j]['atom_type'] == 'NOTE' and atoms[j]['page'] == h['page']:
        pre.insert(0, atoms[j]); j -= 1
    out.extend(pre)
    for a in atoms[h['i'] + 1:]:
        if a['atom_type'] == 'HEADING':
            break
        if a['atom_type'] in ('SENTENCE', 'NOTE', 'LIST_ITEM'):
            out.append(a)
    return out

# ---------- domain -> section ----------
doms = sorted(os.path.basename(d) for d in glob.glob(KB + '/domains/*') if os.path.isdir(d))
OVR = {'DI': '9.1', 'SUPPQUAL': '8.4', 'RELREC': '8.2', 'RELSUB': '8.7', 'RELSPEC': '8.8'}
dsec = {}
for h in heads:
    m = re.search(r'\(([A-Z]{2,8})\)\s*$', h['title'])
    if m and m.group(1) in doms and h['num'][0] in (5, 6, 7, 8, 9) and m.group(1) not in dsec:
        dsec[m.group(1)] = h['id']
dsec.update(OVR)
XPT = {'SUPPQUAL': 'supp--'}

def dom_atoms(D):
    h = hidx[dsec[D]]
    (p0, p1), end = sec_range(h)
    return h, p0, p1, atoms[h['i']:end]

def dir_files(D):
    return sorted(glob.glob(f'{KB}/domains/{D}/*.md'))

def kb_regex(D, rx):
    hits = []
    for f in dir_files(D):
        for n, l in enumerate(open(f, encoding='utf-8').read().split('\n'), 1):
            if re.search(rx, l):
                hits.append(f'{f[len(KB)+1:]}:{n}')
    return hits

def pdf_page_rx(p0, p1, rx):
    for p in range(p0, p1 + 1):
        m = re.search(rx, pages.get(p, ''), re.M)
        if m:
            return p, m.group(0).strip()
    return None

# ---------- batches ----------
batches = {}
for f in sorted(glob.glob(W + '/work/t2_batches/[BS]-*.json')):
    if f.endswith('.writer.jsonl'):
        continue
    b = json.load(open(f, encoding='utf-8'))
    batches[b['batch_id']] = b
glog = subprocess.run(['git', 'log', '--reverse', '--format=%h %s'], capture_output=True, text=True).stdout.split('\n')
commit_order = {}
for l in glog:
    m = re.search(r'Tier B (?:batch|scan batch) ([BS]-[A-Za-z0-9]+)', l)
    if m and m.group(1) not in commit_order:
        commit_order[m.group(1)] = (len(commit_order) + 1, l.split()[0])
MK = {'scan': r'双向全扫', 'fullrange': r'完整节页范围', 'range': r'O20|页范围', 'brief': r'通用(主控)?授权|common_brief|通用 brief'}
binfo = {}
for bid, b in batches.items():
    cp = f'{W}/evidence/checkpoints/t2_{bid}.md'
    txt = open(cp, encoding='utf-8').read() if os.path.exists(cp) else ''
    mk = {k: len(re.findall(v, txt)) for k, v in MK.items()}
    lines = [l.strip()[:170] for l in txt.split('\n') if re.search('|'.join(MK.values()), l)][:3]
    scan = mk['scan'] > 0 or mk['fullrange'] > 0
    rng = mk['range'] > 0 or mk['fullrange'] > 0
    tier = 'FINAL' if (scan and rng) else ('PARTIAL' if (scan or rng or mk['brief']) else 'NARROW')
    binfo[bid] = {'batch': bid, 'commit_seq': commit_order.get(bid, (None,))[0], 'commit': commit_order.get(bid, (None, None))[1],
                  'units': b['units'], 'kb_files': b['kb_files'], 'markers': mk, 'tier': tier, 'marker_lines': lines, 'cp_text': txt}
unit2b = {}
for bid, bi in binfo.items():
    for u in bi['units']:
        unit2b[u] = bid

FILE2B = {f: bid for bid, bi in sorted(binfo.items()) if bid.startswith('S-') for f in bi['kb_files']}
def file_scan(bid, path):
    bid = FILE2B.get(path, bid)
    if not bid: return 'NO_BATCH'
    bi = binfo[bid]
    rel = path[len(KB)+1:] if path.startswith(KB) else path
    inkf = path in bi['kb_files']
    d, fn = rel.split('/')[-2], rel.split('/')[-1]
    mentioned = (f'{d}/{fn}' in bi['cp_text']) or (fn in bi['cp_text'] and len(bi['units']) == 1)
    if bi['tier'] == 'FINAL' and (inkf or (mentioned and fn == 'assumptions.md')):
        return 'FINAL'  # 通用授权明确覆盖 assumptions.md; spec.md 仅点名 -> FINAL_MENTION (O21)
    if bi['tier'] == 'FINAL' and mentioned:
        return 'FINAL_MENTION'
    if inkf or mentioned:
        return bi['tier'] if bi['tier'] != 'FINAL' else 'PARTIAL'
    return 'UNTOUCHED_IN_BATCH'

# ---------- per-domain matrix ----------
rows = []
for D in doms:
    r = {'domain': D}
    if D not in dsec:
        r['error'] = 'no PDF section'; rows.append(r); continue
    h, p0, p1, sat = dom_atoms(D)
    r['section'] = '§' + h['id'] + ' ' + h['title']; r['pages'] = [p0, p1]
    pref = f'{KB}/domains/{D}/'
    # Description
    di = next((a for a in sat if re.match(rf'^\s*{D}\s*[-\u2013\u2014]\s*Description', a['verbatim'])), None)
    if di:
        body = [a for a in atoms[di['_i'] + 1:] if True]
        first = None
        for a in body:
            if a['atom_type'] == 'HEADING': break
            if a['atom_type'] in ('SENTENCE', 'NOTE', 'LIST_ITEM', 'CODE_LITERAL') and len(a['verbatim']) > 25:
                first = a; break
        r['desc_pdf'] = 'Y'; r['desc_pdf_atom'] = di['atom_id']; r['desc_first'] = first['atom_id'] if first else None
        st = kb_find(first['verbatim'], pref, True) if first else ('NO_ATOM', None)
    else:
        pg = pdf_page_rx(p0, min(p0 + 1, p1), rf'^\s*{D}\s*[-\u2013\u2014]\s*Description/Overview\s*$')
        r['desc_pdf'] = 'Y(page_txt p%d)' % pg[0] if pg else 'N'
        st = ('NO_ATOM', None)
    r['desc_kb_heading'] = kb_regex(D, rf'^#{{2,}}\s.*\b\(?{D}\)?\s*[-\u2013\u2014]\s*Description')
    r['desc_kb_text'] = st
    # spec first sentence
    x = XPT.get(D, D.lower())
    sp = None
    for a in sat:
        if a['verbatim'].lower().startswith(f'{x}.xpt'):
            v = a['verbatim']
            if len(v) < 20:
                nx = atoms[a['_i'] + 1] if a['_i'] + 1 < len(atoms) else None
                if nx and nx['atom_type'] in ('SENTENCE', 'CODE_LITERAL') and ' \u2014 ' in nx['verbatim']:
                    nv = nx['verbatim']
                    v = nv if nv.lower().startswith(f'{x}.xpt') else (v + nv if nv.startswith(',') else v + ', ' + nv)
                elif not re.search(r'Example|Row', atoms[a['_i'] - 1]['verbatim']):
                    pass
            if ' \u2014 ' in v or 'One record per' in v:
                sp = (a['atom_id'], v); break
            nx = atoms[a['_i'] + 1]
            if nx['atom_type'] == 'SENTENCE' and nx['verbatim'].startswith('One record per'):
                sp = (a['atom_id'], v + ' ' + nx['verbatim']); break
    if not sp:
        pg = pdf_page_rx(p0, p1, rf'^\s*{re.escape(x)}\.xpt, [^\n]*\u2014[^\n]*')
        if pg: sp = (f'page_txt p{pg[0]}', pg[1])
    r['spec_pdf'] = sp[1][:120] if sp else None
    r['spec_pdf_src'] = sp[0] if sp else None
    r['spec_kb'] = kb_regex(D, rf'{re.escape(x)}\.xpt,\s')
    r['spec_kb_text'] = kb_find(sp[1], pref, True) if sp else ('NO_PDF', None)
    # Assumptions heading
    ah = next((a for a in sat if re.match(rf'^\s*{D}\s*[-\u2013\u2014]\s*Assumptions', a['verbatim'])), None)
    if not ah:
        pg = pdf_page_rx(p0, p1, rf'^\s*{D}\s*[-\u2013\u2014]\s*Assumptions\s*$')
        r['assum_pdf'] = ('Y(page_txt p%d)' % pg[0]) if pg else 'N'
    else:
        r['assum_pdf'] = 'Y'
    r['assum_kb'] = kb_regex(D, rf'^#{{2,}}\s.*\b\(?{D}\)?\s*[-\u2013\u2014]\s*Assumptions')
    # spec footnotes
    fns = [a for a in sat if a['atom_type'] in ('NOTE', 'SENTENCE') and
           (re.search(r'In this column, an asterisk', a['verbatim']) or re.match(r'^\s*(\u00b2|\u00b3|[2-3](?=[A-Z]))', a['verbatim']))]
    r['fn_pdf'] = [a['atom_id'] for a in fns]
    if not fns:
        pg = pdf_page_rx(p0, p1, r'^.{0,3}In this column, an asterisk[^\n]*')
        if pg:
            fa = {'atom_id': f'page_txt p{pg[0]}', 'verbatim': pg[1]}
            fns = [fa]; r['fn_pdf'] = [fa['atom_id']]
    r['fn_kb'] = [(a['atom_id'],) + kb_find(a['verbatim'], pref, True) for a in fns]
    r['fn_kb_elsewhere'] = [kb_find(a['verbatim'])[1] for a in fns]
    # own intro + ancestor intros
    own = intro_atoms(h)
    r['intro_own'] = [(a['atom_id'], a['atom_type']) + st for a, st in zip(own, kb_find_seq(own, pref))]
    anc = []
    for k in range(1, len(h['num'])):
        aid = '.'.join(map(str, h['num'][:k]))
        if aid in hidx:
            ia = intro_atoms(hidx[aid])
            res = kb_find_seq(ia)
            anc.append({'sec': aid, 'n': len(ia), 'exact': sum(1 for s in res if s[0] == 'EXACT'),
                        'partial': sum(1 for s in res if s[0] == 'PARTIAL'),
                        'loc': sorted({s[1].rsplit(':', 1)[0] for s in res if s[1]})})
    r['intro_anc'] = anc
    # batch
    bid = unit2b.get(f'domains/{D}')
    r['batch'] = bid; r['batch_tier'] = binfo[bid]['tier'] if bid else None
    r['batch_seq'] = binfo[bid]['commit_seq'] if bid else None
    r['files'] = {os.path.basename(f): file_scan(bid, f) for f in dir_files(D)}
    rows.append(r)

# ---------- gap flags ----------
def flag(r):
    g = {}
    g['desc'] = (r['desc_pdf'] != 'N') and (not r['desc_kb_heading'] or r['desc_kb_text'][0] in ('NONE', 'PARTIAL'))
    g['spec'] = bool(r['spec_pdf']) and not r['spec_kb'] and r['spec_kb_text'][0] != 'EXACT'
    g['assum'] = (r['assum_pdf'] != 'N') and not r['assum_kb']
    g['fn'] = any(x[1] in ('NONE', 'PARTIAL') for x in r['fn_kb'])
    g['intro'] = any(x[2] != 'EXACT' for x in r['intro_own'])
    g['notfinal'] = sorted(k for k, v in r['files'].items() if v != 'FINAL')
    return g
for r in rows:
    if 'error' not in r: r['gaps'] = flag(r)

# ---------- chapter / model files ----------
cm_rows = []
for f in sorted(glob.glob(KB + '/chapters/*.md') + glob.glob(KB + '/model/*.md')):
    u = f[len(KB)+1:]
    bid = unit2b.get(u)
    cm_rows.append({'file': u, 'batch': bid, 'tier': binfo[bid]['tier'] if bid else None,
                    'seq': binfo[bid]['commit_seq'] if bid else None, 'scan': file_scan(bid, f) if bid else 'NO_BATCH'})

# ---------- §5-§9 non-domain sections (step 4) ----------
dom_ids = set(dsec.values())
def owner(hid):
    for D, s in dsec.items():
        if hid == s or hid.startswith(s + '.'):
            return 'domains/' + D
    return None
sec_rows = []
for h in heads:
    if h['num'][0] not in (5, 6, 7, 8, 9): continue
    if h['id'] in dom_ids: continue
    o = owner(h['id'])
    ia = intro_atoms(h)
    res = [(a['atom_id'], a['atom_type'], a['verbatim'][:70]) + st for a, st in zip(ia, kb_find_seq(ia))]
    sec_rows.append({'sec': h['id'], 'title': h['title'][:60], 'page': h['page'], 'owner_by_numbering': o,
                     'n_intro': len(ia), 'exact': sum(1 for x in res if x[3] == 'EXACT'),
                     'partial': sum(1 for x in res if x[3] == 'PARTIAL'),
                     'none': sum(1 for x in res if x[3] not in ('EXACT', 'PARTIAL')), 'atoms': res})

# ---------- assertions (known answers) ----------
R = {r['domain']: r for r in rows}
S = {s['sec']: s for s in sec_rows}
checks = []
def chk(name, cond): checks.append((name, bool(cond)))
SCANNED = {u.split('/')[-1] for bid, bi in binfo.items() if bid.startswith('S-') for u in bi['units']} | {f.split('/')[-2] for bid, bi in binfo.items() if bid.startswith('S-') for f in [x['file'] for x in batches[bid].get('narrow_files', [])]}
def chkb(name, cond, host):
    if host in SCANNED: checks.append((name + ' [baseline; host ' + host + ' scanned -> n/a]', True))
    else: chk(name, cond)
chkb('O49 DS desc gap', R['DS']['gaps']['desc'], 'DS')
chkb('O45 §6.1.3 intro 0 exact', S['6.1.3']['exact'] == 0 and S['6.1.3']['n_intro'] > 0, 'EX')
chkb('O50 §6.2 intro 0 exact', S['6.2']['exact'] == 0 and S['6.2']['n_intro'] > 0, 'AE')
chkb('O39 §6.3 intro 0 exact', S['6.3']['exact'] == 0 and S['6.3']['n_intro'] > 0, 'DA')
chkb('O46 §9 intro in ch10', any(x[4] and x[4].startswith('chapters/ch10') for x in S['9']['atoms']), 'DI')
chk('O47 §7.3 intro in TV/assumptions', any(x[4] and x[4].startswith('domains/TV/assumptions.md') for x in S['7.3']['atoms']))
chkb('O31 MO box heading+first sentence absent', [x[3] for x in S['6.3.6']['atoms'][:2]] != ['EXACT','EXACT'] and S['6.3.6']['atoms'][1][3] == 'NONE', 'NV')
G17 = set('AG CP DI EG DS EX OE MB PP OI PE PR SE SS TD TR UR'.split())
chk('grep -L ".xpt, " 17 dirs + LB (generic --.xpt only) == no own spec sentence in assumptions.md', {D for D in doms if D not in SCANNED and not any('assumptions.md' in h for h in R[D].get('spec_kb', []))} == (G17 | {'LB'}) - SCANNED)
G19 = set('AG DI DS EX FA OE OI PP PR RELREC RS SS SUPPQUAL TA TD TE TM TR UR'.split())
chk('grep -L en-dash Assumptions heading 19 dirs minus TE (em dash "## TE — Assumptions") == no ## XX - Assumptions', {D for D in doms if D not in SCANNED and not any('assumptions.md' in h for h in R[D].get('assum_kb', []))} == G19 - {'TE'} - SCANNED)
chk('CM desc+spec+assum present', not R['CM']['gaps']['desc'] and not R['CM']['gaps']['spec'] and not R['CM']['gaps']['assum'])

out = {'generated_by': 'work/scratch/t2/global/t2_coverage_matrix.py', 'domains': rows, 'chapters_model': cm_rows,
       'sections_5_9': sec_rows, 'batches': {k: {kk: vv for kk, vv in v.items() if kk != 'cp_text'} for k, v in binfo.items()},
       'dropped_headings': dropped, 'checks': checks}
json.dump(out, open(OUTP('work/t2_coverage_matrix.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
for n, ok in checks:
    print(('PASS ' if ok else 'FAIL ') + n)
print('domains', len(rows), 'sections', len(sec_rows), 'dropped_headings', len(dropped))

# ======================= render md =======================
def c_desc(r):
    if r['desc_pdf'] == 'N': return 'NA'
    t = r['desc_kb_text'][0]; hd = bool(r['desc_kb_heading'])
    if hd and t == 'EXACT': return 'Y'
    if t == 'EXACT': return 'Y文/无标题'
    if hd: return '标题/文' + t
    return '**缺**'
def c_spec(r):
    if not r['spec_pdf']: return 'NA'
    return 'Y' if r['spec_kb_text'][0] == 'EXACT' else ('**缺**' if not r['spec_kb'] else '异:' + r['spec_kb_text'][0])
def c_assum(r):
    if r['assum_pdf'] == 'N': return 'NA'
    return 'Y' if r['assum_kb'] else '**缺**'
def c_fn(r):
    n = len(r['fn_kb'])
    if n == 0: return 'NA'
    k = sum(1 for x in r['fn_kb'] if x[1] == 'EXACT')
    return f'{k}/{n}' if k == n else f'**{k}/{n}**'
def c_intro(r):
    n = len(r['intro_own'])
    if n == 0: return '-'
    k = sum(1 for x in r['intro_own'] if x[2] == 'EXACT')
    return f'{k}/{n}' if k == n else f'**{k}/{n}**'
def c_anc(r):
    return ' '.join(f"§{a['sec']}:{a['exact']}/{a['n']}" for a in r['intro_anc'] if a['n'] > 0) or '-'
AB = {'FINAL_MENTION': 'Fm', 'FINAL': 'F', 'PARTIAL': 'P', 'NARROW': 'N', 'NO_BATCH': '-', 'UNTOUCHED_IN_BATCH': 'U'}
def c_files(r):
    return ' '.join(f"{k[0]}:{AB[v]}" for k, v in sorted(r['files'].items()))

L = []
L.append('# T2 覆盖矩阵 (T2 后扫描批定范围用)\n')
L.append('<!-- chain: E (plans) -->')
L.append('> 状态: 机械生成 (2026-11-26), 只读 KB. 机器可读: `work/t2_coverage_matrix.json`.\n')
L.append('## 复跑命令\n')
L.append('```bash\ncd /Volumes/DevSSD/Project/sdtm-pedia\npython3 .work/10_tier_b_repair/work/scratch/t2/global/t2_coverage_matrix.py\n```\n')
L.append('脚本在 gitignored 的 `work/scratch/t2/global/`; 输入 = `knowledge_base/**/*.md` (排除 terminology/ INDEX ROUTING VARIABLE_INDEX), '
         '`work/pdf_atoms.jsonl` (atom_id 前缀 `ig34_`, 不按 source 字段), `work/pdf_pages/ig34_p*.txt` (atom 缺失时回退), '
         '`work/t2_batches/B-*.json`, `evidence/checkpoints/t2_B-*.md` (writer 报告), `git log`.\n')
L.append('## 判据\n')
L.append('- PDF 节 = IG 编号标题 (HEADING 原子) 起, 至下一个同级或更高级编号标题止; 页 = [起页, 止页].')
L.append('- 匹配: NFKC + 弯引号/en-em dash/省略号归一 + 去 markdown 标记 + 空白折叠 + 小写. EXACT = 整句子串命中; PARTIAL = 仅首/尾 45 字命中 (改写/截断); '
         '短原子 (<40 字, 如域名列表项) 只在前一原子命中处后 15 行内命中才算 EXACT, 否则 SHORT_UNANCHORED (= 未承载).')
L.append('- Description / spec 首句 / 脚注: 只在本域目录内找. Description = PDF `XX – Description/Overview` 后首句 EXACT 且 KB 有 `## … XX – Description` 标题. '
         'spec 首句 = PDF `xx.xpt, <Domain> — <Class>. One record per …` (原子拆开的自动拼接) 在本域目录 EXACT (spec.md `> Class: | Structure:` 行不算). '
         'Assumptions 标题 = KB `##+ … XX –/—/- Assumptions` (H1 `# XX — Assumptions` 不算). 脚注 = PDF 节内 "In this column, an asterisk …" 及 ²/³ 类 NOTE.')
L.append('- 引言: 本节引言 = 域节标题与其后第一个 HEADING 之间的 SENTENCE/NOTE/LIST_ITEM; 父节引言 = 各祖先编号节同口径. 父节引言全 KB 搜 (不限域目录).')
L.append('- 批口径 (writer checkpoint 字样): FINAL = (双向全扫 或 完整节页范围) 且 (O20 或 页范围); PARTIAL = 只有其一或仅通用授权; NARROW = 均无. '
         '文件级: F = 批 FINAL 且该文件在 kb_files 或被 checkpoint 点名; P/N = 同条件但批非 FINAL; U = 批开过但该文件不在 kb_files 也未点名; - = 从未开批.')
L.append('- Fm = 批 FINAL 但该文件不在 kb_files、只被 checkpoint 点名 (几乎全是 spec.md; 通用授权不含 spec.md, O21/O24/O26) → 计入未终版. assumptions.md 被点名即算 F (通用授权明确覆盖).')
L.append('- 列缩写: 文件 a=assumptions.md e=examples.md s=spec.md; 粗体 = 缺口.\n')
L.append('## 已知答案自检 (失败 = 匹配器错, 不是 KB 错)\n')
for n, ok in checks:
    L.append(f'- {"PASS" if ok else "FAIL"} {n}')
L.append('')

# domain table
L.append('## 1. 域矩阵 (64 目录)\n')
L.append('| 域 | PDF 节 | 页 | Desc | spec 首句 | Assum 标题 | 脚注 | 本节引言 | 父节引言 (§:EXACT/总) | 批 | 序 | 批口径 | 文件 |')
L.append('|---|---|---|---|---|---|---|---|---|---|--:|---|---|')
for r in rows:
    L.append(f"| {r['domain']} | §{r['section'].split(' ',1)[0].lstrip('§')} | {r['pages'][0]}-{r['pages'][1]} | {c_desc(r)} | {c_spec(r)} | {c_assum(r)} | {c_fn(r)} | {c_intro(r)} | {c_anc(r)} | "
             f"{r['batch'] or '-'} | {r['batch_seq'] or '-'} | {r['batch_tier'] or '无批'} | {c_files(r)} |")
L.append('')

# stats
def lst(f): return [r['domain'] for r in rows if f(r)]
miss_desc = lst(lambda r: c_desc(r) not in ('Y', 'NA'))
miss_spec = lst(lambda r: c_spec(r) not in ('Y', 'NA'))
miss_assum = lst(lambda r: c_assum(r) == '**缺**')
miss_fn = lst(lambda r: c_fn(r).startswith('**'))
fn_has = lst(lambda r: c_fn(r) not in ('NA',) and not c_fn(r).startswith('**'))
miss_intro = lst(lambda r: c_intro(r).startswith('**'))
nobatch = lst(lambda r: not r['batch'])
notfinal_files = []
for r in rows:
    for k, v in sorted(r['files'].items()):
        if v != 'FINAL': notfinal_files.append((f"domains/{r['domain']}/{k}", v))
for c in cm_rows:
    if c['scan'] != 'FINAL': notfinal_files.append((c['file'], c['scan']))
L.append('## 2. 统计\n')
L.append(f'- 缺 Description ({len(miss_desc)}): ' + ', '.join(f'{d} ({c_desc(R[d])})' for d in miss_desc))
L.append(f'- 缺 spec 首句 ({len(miss_spec)}): ' + ', '.join(miss_spec))
L.append(f'- 缺 `## XX – Assumptions` 标题 (PDF 有) ({len(miss_assum)}): ' + ', '.join(miss_assum))
L.append(f'- 缺 spec 表脚注 ({len(miss_fn)} 域; 已承载 {len(fn_has)}: ' + ', '.join(fn_has) + '): ' + ', '.join(miss_fn))
L.append(f'- 本节引言未全承载 ({len(miss_intro)}): ' + ', '.join(f'{d} {c_intro(R[d])}' for d in miss_intro))
L.append(f'- 从未开批的域 ({len(nobatch)}): ' + ', '.join(nobatch))
L.append(f'- 批口径分布: ' + ', '.join(f"{t} {sum(1 for b in binfo.values() if b['tier']==t)}" for t in ('FINAL', 'PARTIAL', 'NARROW')) + f' (共 {len(binfo)} 批)')
cnt = {}
for _, v in notfinal_files: cnt[v] = cnt.get(v, 0) + 1
L.append(f'- 未终版全扫文件 ({len(notfinal_files)}): ' + ', '.join(f'{k} {v}' for k, v in sorted(cnt.items())) + ' — 清单见 §5.\n')

# sections
HOST = {'5': 'CO (已承载)', '6.1': '待定 (model/02 或 chapters)', '6.1.3': 'EX/assumptions.md 顶 (O45)', '6.2': '待定 (O50)', '6.3': '待定 (O39)',
        '6.3.5': 'LB', '6.3.5.1': 'LB', '6.3.5.7': 'MB', '6.3.5.9': 'PC', '6.3.5.9.3': 'PC', '6.3.6': 'NV §6.3.7 前 (O31)', '6.3.7': 'NV', '6.3.7.1': 'NV',
        '6.3.9': 'FT', '6.3.12': 'TU', '6.4': 'FA', '6.4.1': 'FA', '6.4.2': 'FA', '6.4.3': 'FA', '7.1.1': 'TA', '7.1.2': 'TA', '7.1.3': 'TA', '7.2': 'TA',
        '7.3': 'TV (O47)', '7.4': 'TI', '7.5': 'TI', '9': 'ch10 (O46) + DI/OI 交叉引用'}
def file_status(rel):
    if rel.startswith('domains/'):
        D, fn = rel.split('/')[1], rel.split('/')[2]
        return R[D]['files'].get(fn, '?') if D in R else '?'
    c = next((c for c in cm_rows if c['file'] == rel), None)
    return c['scan'] if c else '?'
def in_range(rel, page):
    if rel.startswith('domains/'):
        D = rel.split('/')[1]
        if D in R and R[D]['pages'][0] <= page <= R[D]['pages'][1]:
            return True
        bid = R[D]['batch'] if D in R else None
    else:
        bid = unit2b.get(rel)
    if bid:
        for pr in batches[bid].get('pdf_ranges', []):
            if pr['file'] == KB + '/' + rel and pr['lo'] <= page <= pr['hi']:
                return True
    return False
host_flag = []
for s_ in sec_rows:
    hs = sorted({x[4].rsplit(':', 1)[0] for x in s_['atoms'] if x[4]})
    s_['hosts'] = [{'file': h, 'status': file_status(h), 'in_batch_range': in_range(h, s_['page'])} for h in hs]
    for hh in s_['hosts']:
        D = hh['file'].split('/')[1] if hh['file'].startswith('domains/') else None
        bid = R[D]['batch'] if D in R else unit2b.get(hh['file'])
        cpt = binfo[bid]['cp_text'] if bid else ''
        hh['cp_mentions_sec'] = bool(re.search(rf'§{re.escape(s_["sec"])}(?![.\d])|\bp{s_["page"]}\b', cpt))
        if hh['status'] == 'FINAL' and not hh['in_batch_range'] and not hh['cp_mentions_sec']:
            host_flag.append((s_['sec'], hh['file']))
L.append('## 3. §5–§9 章级 / 父节 / 无域节 引言承载 (O17/O39/O45/O46/O50)\n')
L.append('| 节 | 标题 | 页 | 编号归属 | 引言原子 | EXACT/PARTIAL/未承载 | KB 位置 (首个命中) | 宿主文件级 / 节页在该批范围内 | 宿主 (先例/候选) |')
L.append('|---|---|--:|---|--:|---|---|---|---|')
for s_ in sec_rows:
    locs = sorted({x[4] for x in s_['atoms'] if x[4]})
    loc = ', '.join(f'`{l}`' for l in locs[:3]) + (' …' if len(locs) > 3 else '') if locs else '-'
    L.append(f"| §{s_['sec']} | {s_['title'][:48]} | {s_['page']} | {s_['owner_by_numbering'] or '-'} | {s_['n_intro']} | "
             f"{s_['exact']}/{s_['partial']}/{s_['none']} | {loc} | "
             + (' '.join(f"{h['file'].split('/')[-2] if h['file'].startswith('domains') else h['file'].split('/')[-1][:4]}:{AB.get(h['status'], h['status'])}/{'in' if h['in_batch_range'] else '**out**'}" for h in s_['hosts']) or '-')
             + f" | {HOST.get(s_['sec'], '-')} |")
L.append('')
L.append('注: §6.1/§6.2/§6.3 的 PARTIAL 命中都是 `chapters/ch02_fundamentals.md:49` (§2.3 "…according to 1 of the 3 SDTM general observation classes: …") —'
         ' 只是首 45 字前缀相同, 不是该引言句; §6.2 域列表 7 项 SHORT_UNANCHORED. 实质上三处类引言 KB 均无 (与 O39/O50 一致). '
         '§6.3.6 MO 框: 标题 + 首句无; 后 2 句在 `chapters/ch10_appendices.md:222-224` (变更附录) 有近似/原句 — O31 "全 KB 无" 需修正为 "MO 框标题与首句无".\n')

# chapters/model
L.append('宿主 F 但节页不在该域节/批 pdf_ranges 内、且该批 checkpoint 未提及该节号或页 (节正文未核, 须进扫描批): ' + (', '.join(f'§{a} `{b}`' for a, b in host_flag) or '无') + '\n')
L.append('## 4. chapters / model 文件\n')
L.append('| 文件 | 批 | 序 | 批口径 | 文件级 |')
L.append('|---|---|--:|---|---|')
for c in cm_rows:
    L.append(f"| `{c['file']}` | {c['batch'] or '-'} | {c['seq'] or '-'} | {c['tier'] or '无批'} | {AB.get(c['scan'], c['scan'])} |")
L.append('')

L.append('## 5. 未终版全扫文件清单\n')
by = {}
for f, v in notfinal_files: by.setdefault(v, []).append(f)
for v in ('NO_BATCH', 'UNTOUCHED_IN_BATCH', 'NARROW', 'PARTIAL', 'FINAL_MENTION'):
    if v in by:
        L.append(f'- **{v}** ({len(by[v])}): ' + ', '.join(f'`{x}`' for x in by[v]))
L.append('')

L.append('## 6. 附录: 批口径判定依据 (writer checkpoint 命中行, 每批 ≤3 行)\n')
L.append('| 批 | 序 | 口径 | 双向全扫/完整节页范围/O20|页范围/通用授权 | 命中行 |')
L.append('|---|--:|---|---|---|')
for bid, b in sorted(binfo.items(), key=lambda kv: kv[1]['commit_seq'] or 999):
    m = b['markers']
    ml = ' / '.join(x.replace('|', '¦').replace('`', "'") for x in b['marker_lines'])[:300] or '-'
    L.append(f"| {bid} | {b['commit_seq']} | {b['tier']} | {m['scan']}/{m['fullrange']}/{m['range']}/{m['brief']} | {ml} |")
L.append('')
# ---------- proposed scan batches (each file exactly once) ----------
GROUPS = [
  ('S-INT', '§6.1 Interventions (+§6.1.3 引言 O45 → EX 顶)', ['AG', 'PR', 'EX', 'EC'], []),
  ('S-EVT', '§6.2 Events', ['AE', 'DS'], []),
  ('S-SPC1', '§6.3.5 Specimen 上半', ['CP', 'GF', 'IS', 'LB'], []),
  ('S-SPC2', '§6.3.5.7 Micro + §6.3.5.9 PK', ['MB', 'MS', 'PC', 'PP'], []),
  ('S-FND', '§6.3.3/§6.3.7/§6.3.8/§6.3.11', ['EG', 'OE', 'UR', 'PE', 'SS'], []),
  ('S-TUFA', '§6.3.12 Tumor + §6.4 FA/SR', ['TR', 'FA', 'SR'], []),
  ('S-TDM', '§7 Trial Design', ['TA', 'TD', 'TM'], []),
  ('S-SPREL', '§5.3 SE + §8 RELREC/RELSUB/RELSPEC + §9.2 OI', ['SE', 'RELREC', 'RELSUB', 'RELSPEC', 'OI'], []),
  ('S-CH', 'chapters 未终版', [], ['chapters/ch01_introduction.md', 'chapters/ch02_fundamentals.md', 'chapters/ch04_general_assumptions.md', 'chapters/ch08_relationships.md', 'chapters/ch10_appendices.md']),
  ('S-MODEL', 'model 未终版 (SDTM v2.0)', [], ['model/01_concepts_and_terms.md', 'model/02_observation_classes.md', 'model/03_special_purpose_domains.md', 'model/04_associated_persons.md', 'model/05_study_level_data.md']),
]
assigned = {}
for g, _, ds, fs in GROUPS:
    for D in ds:
        for f in R[D]['files']:
            assigned.setdefault(f'domains/{D}/{f}', []).append(g)
    for f in fs:
        assigned.setdefault(f, []).append(g)
# S-FN: spec.md of FINAL domains still missing footnotes (policy O24/O26 first)
fn_files = [f'domains/{r["domain"]}/spec.md' for r in rows if (r['domain'] in miss_fn or r['files'].get('spec.md') != 'FINAL') and f'domains/{r["domain"]}/spec.md' not in assigned and 'spec.md' in r['files']]
fn_assum = [r['domain'] for r in rows if r['domain'] in miss_fn and f'domains/{r["domain"]}/spec.md' not in assigned and 'spec.md' not in r['files']]
GROUPS.append(('S-SPEC', 'FINAL 域 spec.md: 全扫 (Fm 未逐格核, O21) + 表脚注 (先定 O24/O26 统一口径/放置)', [], fn_files))
for f in fn_files: assigned.setdefault(f, []).append('S-SPEC')
hf = sorted({b for _, b in host_flag if b not in assigned})
if hf: GROUPS.append(('S-HOST', '宿主 F 文件承载的范围外非域节 (节正文未核): ' + ', '.join(f'§{a}' for a, b in host_flag), [], hf))
for f in hf: assigned.setdefault(f, []).append('S-HOST')
dup = {f: g for f, g in assigned.items() if len(g) > 1}
uncov = [f for f, _ in notfinal_files if f not in assigned]
chk('scan batches: every file in exactly one batch', not dup)
chk('scan batches: every not-FINAL file covered', not uncov)
L.append('## 7. 建议扫描批分组 (每文件只进一批, 按共享父节分组)\n')
L.append('| 批 | 范围 | 单元 | 文件数 | 缺口摘要 (Desc/spec/Assum/脚注) |')
L.append('|---|---|---|--:|---|')
for g, desc, ds, fs in GROUPS:
    nfiles = sum(1 for f, gg in assigned.items() if g in gg)
    if ds:
        gap = '; '.join(f"{D}:{''.join(x for x, c in (('D', D in miss_desc), ('S', D in miss_spec), ('A', D in miss_assum), ('F', D in miss_fn)) if c) or '-'}" for D in ds)
        unit = ', '.join(ds)
    else:
        gap = '-'; unit = ', '.join(f.split('/')[1] if g == 'S-SPEC' else (f.split('/')[-2] + '/' + f.split('/')[-1] if f.startswith('domains') else f.split('/')[-1]) for f in fs)
    L.append(f'| {g} | {desc} | {unit} | {nfiles} | {gap} |')
L.append('| (宿主待主控定) | §6.1/§6.2/§6.3 类引言 (O39/O50, ch02 §2.3 只有近似句) + §6.3.6 MO 框标题/首句 (O31) | 无文件 | 0 | 宿主一定, 该引言并入拥有该文件的批 (ch02→S-CH, model/02→S-MODEL, NV/assumptions.md→S-HOST 或另开) |')
L.append('')
L.append('')
L.append('缺口摘要字母: D=Description, S=spec 首句, A=Assumptions 标题, F=脚注. S-SPEC 外的批内脚注随本批做. '
         + (f'无 spec.md 的 FINAL 域 (脚注在 assumptions.md 处理): {", ".join(fn_assum)}. ' if fn_assum else '')
         + f'自检: 重复 {len(dup)} / 未覆盖 {len(uncov)}.\n')
L.append('## 8. 局限\n')
L.append('- 纯字符串机检: PARTIAL 可能是改写 (O33 类) 也可能是共享前缀假阳 (见 §3 注); EXACT 不等于位置正确. 承载判定须扫描批人工复核.')
L.append('- BE §6.2.2 PDF 原子与页文本均未找到 spec 脚注 → 记 NA, 扫描批需看 PDF 原页 (p143-144) 确认.')
L.append('- LB/CV/OE/MI/TU/DI 部分 spec 首句或脚注来自 `pdf_pages` 文本回退 (原子缺失/拆分), JSON `*_src` 字段标 `page_txt`.')
L.append('- 文件级 F 判据宽松: checkpoint 只要点名该文件名即算 (单域批); spec.md 常被点名但未逐格扫 (O21), F 不代表 spec 表已逐格核.')
L.append('- 批口径只看 writer checkpoint 字样, 不读 audit/review; B-OE 有 "双向全扫" 无页范围核, B-LB/B-SR/B-model05 有页范围字样无全扫 → PARTIAL.')
L.append('## 9. 分组自检\n')
for n, ok in checks[-2:]:
    L.append(f'- {"PASS" if ok else "FAIL"} {n}')
open(OUTP('evidence/t2_coverage_matrix.md'), 'w', encoding='utf-8').write('\n'.join(L) + '\n')
for n, ok in checks[-2:]:
    print(('PASS ' if ok else 'FAIL ') + n)
json.dump({**out, 'checks': checks, 'scan_batches': [{'batch': g, 'scope': d, 'domains': ds, 'files': sorted(f for f, gg in assigned.items() if g in gg)} for g, d, ds, fs in GROUPS]},
          open(OUTP('work/t2_coverage_matrix.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('md written', len(L), 'lines')
