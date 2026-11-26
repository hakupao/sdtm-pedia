#!/usr/bin/env python3
# S-TYPO planner (dry-run; never writes knowledge_base/). U1/U4/O59: typographic chars -> PDF original chars.
# For each typographic unit (quote / dash / ellipsis) in a KB line, a context window (whitespace-free, typo-normalised)
# is searched only in that file's own PDF page range (layout text work/pdf_pages + raw text RAW_DIR); a change is planned
# only when every hit agrees on the PDF char. CRF boxes / superscripts come from a render-checked fixed list (FIXED below).
# usage: python3 typo_plan.py RAW_DIR [OUT_PLAN] [OUT_STATS]
#        python3 typo_plan.py --apply PLAN KB_ROOT [--allow-repo]   (HEAD-based columns; repo tree only with --allow-repo)
#   RAW_DIR = dir of `pdftotext -raw -enc UTF-8 -f p -l p` pages named ig34_pNNNN.txt / sv20_pNNNN.txt (scratch, not committed)
#   default OUT_PLAN = work/t2_batches/S-TYPO.plan.jsonl; OUT_STATS (residuals + stats json) default = RAW_DIR/../typo_stats.json
import re, sys, os, json, glob, ast, subprocess, collections
REPO = '/Volumes/DevSSD/Project/sdtm-pedia'
W = f'{REPO}/.work/10_tier_b_repair'
RAW = sys.argv[1] if sys.argv[1:2] != ['--apply'] else ''
OUT = sys.argv[2] if len(sys.argv) > 2 else f'{W}/work/t2_batches/S-TYPO.plan.jsonl'
STATS = sys.argv[3] if len(sys.argv) > 3 else os.path.join(os.path.dirname(RAW.rstrip('/')), 'typo_stats.json')
FIXED_OUT = f'{W}/work/t2_batches/S-TYPO.fixed.jsonl'
RESID_OUT = f'{W}/work/t2_batches/S-TYPO.residual.jsonl'
SRCS = {'layout': f'{W}/work/pdf_pages', 'raw': RAW}

# ---- tokens -------------------------------------------------------------------------------------------------
SQ, DQ, DA, EL, VA, BX, PB = '\ue001', '\ue002', '\ue003', '\ue004', '\ue005', '\ue006', '\ue00f'
SQC, DQC, DAC = "'’‘", '"“”', '-–—‑‐−'
BOXC = '○□☐◦'
DROP = '•▪\uf0b7'
SUP = {'¹': '1', '²': '2', '³': '3'}
CLS = {SQ: 'SQ', DQ: 'DQ', DA: 'DASH', EL: 'ELL'}

def tokenize(chars):
    """chars: list of (ch, idx). Returns (norm str, spans list[(i0,i1)] of orig idx, unit text list). Whitespace dropped."""
    out, spans, txt = [], [], []
    n, k = len(chars), 0
    while k < n:
        c, i = chars[k]
        if c.isspace() or c in DROP:
            k += 1; continue
        if c in DAC:
            j = k
            while j < n and chars[j][0] in DAC and j - k < 2: j += 1
            run = ''.join(x[0] for x in chars[k:j])
            nxt = ''.join(x[0] for x in chars[j:j + 2])
            prv = chars[k - 1][0] if k else ' '
            if re.fullmatch(r'[A-Z]{2}', nxt) and not prv.isalnum() and (len(run) == 2 or run[0] != '-' or prv in '(“"\' /,'):
                out.append(VA); spans.append((i, chars[j - 1][1] + 1)); txt.append(run); k = j; continue
            if run == '--':  # non-variable double hyphen: one unit (dash pair)
                out.append(DA); spans.append((i, chars[k + 1][1] + 1)); txt.append(run); k += 2; continue
            out.append(DA); spans.append((i, i + 1)); txt.append(c); k += 1; continue
        if c == '.' and k + 2 < n and chars[k + 1][0] == '.' and chars[k + 2][0] == '.':
            j = k
            while j < n and chars[j][0] == '.': j += 1
            if j - k == 3:
                out.append(EL); spans.append((i, chars[k + 2][1] + 1)); txt.append('...'); k = j; continue
            for x in chars[k:j]: out.append('.'); spans.append((x[1], x[1] + 1)); txt.append('.')
            k = j; continue
        if c == '…': out.append(EL)
        elif c in SQC: out.append(SQ)
        elif c in DQC: out.append(DQ)
        elif c in BOXC: out.append(BX)
        elif c in SUP: out.append(SUP[c])
        else: out.append(c)
        spans.append((i, i + 1)); txt.append(c); k += 1
    return ''.join(out), spans, txt

# ---- PDF side -----------------------------------------------------------------------------------------------
_pdf = {}
def pdf_page(src, mode, p):
    key = (src, mode, p)
    if key not in _pdf:
        fn = f'{SRCS[mode]}/{src}_p{p:04d}.txt'
        t = open(fn, encoding='utf-8').read() if os.path.exists(fn) else ''
        if mode == 'raw':  # drop copyright footer lines
            t = '\n'.join(l for l in t.split('\n') if not re.match(r'© 20\d\d Clinical Data Interchange|^20\d\d-\d\d-\d\d$', l))
        norm, spans, txt = tokenize([(c, i) for i, c in enumerate(t)])
        _pdf[key] = (t, norm, spans, txt)
    return _pdf[key]

def ws(t, i, step):
    j = i if step > 0 else i - 1
    if j < 0 or j >= len(t): return 'nl'
    c = t[j]
    return 'nl' if c == '\n' else ('sp' if c in ' \t\u00a0' else 'none')

def search(pages, pat, off):
    hits = []
    for mode in SRCS:
        for src, p in pages:
            t, norm, spans, txt = pdf_page(src, mode, p)
            s = norm.find(pat)
            while s >= 0:
                q = s + off
                a, b = spans[q]
                hits.append(dict(mode=mode, page=p, src=src, ch=txt[q], before=ws(t, a, -1), after=ws(t, b, 1)))
                s = norm.find(pat, s + 1)
    return hits

# ---- page ranges --------------------------------------------------------------------------------------------
def ranges():
    R = collections.defaultdict(set)
    for f in sorted(glob.glob(f'{W}/work/t2_batches/*.json')):
        d = json.load(open(f))
        for r in d.get('pdf_ranges') or []:
            for fl in ([r['file']] if 'file' in r else d['kb_files']): R[fl].add((r['src'], r['lo'], r['hi']))
        if not d.get('pdf_ranges') and d.get('pdf_pages') and not d.get('sections'):  # e.g. B-DI: only pdf_pages given
            for fl in d['kb_files']: R[fl].update(('ig34', p, p) for p in d['pdf_pages'])
        s = d.get('sections')
        if isinstance(s, str): s = ast.literal_eval(s)
        for x in s or []:
            u = x['unit'].split(' ')[0]
            fs = [f'knowledge_base/{u}'] if u.endswith('.md') else sorted(os.path.relpath(g, REPO) for g in glob.glob(f'{REPO}/knowledge_base/{u}/*.md'))
            if d.get('spec_only'): fs = [g for g in fs if g.endswith('spec.md')]
            for g in fs: R[g].add((x.get('src', 'ig34'), x['lo'], x['hi']))
    P = {}
    for f, rs in R.items():
        P[f] = {(s, p) for s, lo, hi in rs for p in range(lo, hi + 1)}
    dom = collections.defaultdict(set)  # domains/: page set = union over the domain dir (the domain's own section)
    for f, ps in P.items():
        if f.startswith('knowledge_base/domains/'): dom[f.split('/')[2]] |= ps
    return P, dom

# ---- KB line -> visible chars + protection --------------------------------------------------------------------
def visible(line, prot):
    """Returns list of segments; each a list of (ch, idx). Markdown syntax removed; prot: set of protected idx (updated)."""
    n = len(line)
    keep = [True] * n
    def protect(a, b, drop=False):
        for i in range(a, b):
            prot.add(i)
            if drop: keep[i] = False
    m = re.match(r'^(\s*(?:>\s*)*)', line); protect(0, m.end(), True)
    pos = m.end()
    m2 = re.match(r'([-*+]|\d+\.)\s+', line[pos:])
    if m2 and not line[pos:].startswith('|'): protect(pos, pos + m2.end(), True)
    for m in re.finditer(r'<!--.*?-->|<[/]?[a-zA-Z][^>]*>', line): protect(m.start(), m.end(), True)
    for m in re.finditer(r'`[^`]*`', line): protect(m.start(), m.end()); keep[m.start()] = keep[m.end() - 1] = False
    for m in re.finditer(r'\]\(([^)]*)\)', line): protect(m.start(), m.end(), True)
    for m in re.finditer(r'(?<!\\)\[(?=[^\]]*\]\()', line): protect(m.start(), m.end(), True)
    for m in re.finditer(r'https?://[^\s)>|`]+|www\.[^\s)>|`]+', line): protect(m.start(), m.end())
    for m in re.finditer(r'\*\*', line): protect(m.start(), m.end(), True)
    for m in re.finditer(r'(?<![\w*\\])\*(?=[^\s*])([^*\n]+?)(?<=\S)\*(?![\w*])', line):
        protect(m.start(), m.start() + 1, True); protect(m.end() - 1, m.end(), True)
    for m in re.finditer(r'\\([|*_\[\]#`<>-])', line): protect(m.start(), m.start() + 1, True)
    for m in re.finditer(r'--(?=[A-Z])', line): protect(m.start(), m.end())
    for m in re.finditer(r'\((?:[A-Z0-9_]+)\) C\d+', line): protect(m.start(), m.end())
    segs, cur = [], []
    table = line.lstrip(' >').startswith('|')
    for i, c in enumerate(line):
        if table and c == '|' and not (i and line[i - 1] == '\\'):
            prot.add(i); segs.append(cur); cur = []; continue
        if keep[i]: cur.append((c, i))
    segs.append(cur)
    return [s for s in segs if s]

def is_sep(line):
    return bool(re.fullmatch(r'\s*\|?[\s:|\-]+\|?\s*', line)) and '-' in line and line.count('|') >= 1 or bool(re.fullmatch(r'\s*(-{3,}|\*{3,}|_{3,})\s*', line))

def target_char(pdfc, kbtxt):
    return '-' if pdfc in '‑‐' else pdfc

def cls_name(b, a):
    k = lambda c: {"'": 'straight', '’': 'right', '‘': 'left', '"': 'straight', '“': 'left', '”': 'right',
                   '-': 'hyphen', '–': 'en', '—': 'em', '...': 'three_dots', '…': 'ellipsis', '--': 'dashpair', '−': 'minus'}.get(c, c)
    fam = 'sq' if a in SQC else 'dq' if a in DQC else 'dash' if a in DAC else 'ell'
    return f'{fam}:{k(b)}->{k(a)}'

# ---- fixed list (render-checked; pdftotext cannot be trusted for these glyphs) ----------------------------------
FIXED_RULES = [  # (file, line-regex or HEAD line no, before, after, class, pdf_page, evidence)
    # S-TYPO a2 coordinator ruling (2): closed table extended for exactly these 3 ch04 positions (rendered)
    ('knowledge_base/chapters/ch04_general_assumptions.md', 1101, '−', '-', 'minus:U+2212->hyphen', 46, 'render p46: "VSDTC-VSRFTDTC." hyphen-minus'),
    ('knowledge_base/chapters/ch04_general_assumptions.md', 1485, ' -- ', ' – ', 'dashpair:-- ->en', 56, 'render p56: "Supplemental Qualifiers – SUPP-- Datasets" (not a variable prefix)'),
    ('knowledge_base/chapters/ch04_general_assumptions.md', 1514, ' -- ', ' – ', 'dashpair:-- ->en', 57, 'render p57: "Supplemental Qualifiers – SUPP-- Datasets" (not a variable prefix)'),
    # CRF ○ □ (CE 33+6, ch04/ML/DM): removed in a2 by coordinator ruling (3) -> T4 user decision
]
for _ln, _pg, _tb in ((96, 429, 'RELREC'), (212, 432, 'SUPPQUAL'), (363, 438, 'RELSUB'), (438, 439, 'RELSPEC')):  # HEAD line numbers
    FIXED_RULES.append(('knowledge_base/chapters/ch08_relationships.md', _ln, '^1^ ', '¹', 'sup:^1^ ->¹', _pg, f'render p{_pg}: {_tb} spec footnote starts with superscript ¹ directly before "In" (no space)'))

def main():
    P, DOM = ranges()
    files = sorted(os.path.relpath(g, REPO) for g in glob.glob(f'{REPO}/knowledge_base/chapters/*.md') + glob.glob(f'{REPO}/knowledge_base/domains/*/*.md') + glob.glob(f'{REPO}/knowledge_base/model/*.md'))
    reg = [json.loads(l) for l in open(f'{W}/work/t2_pdf_typo_registry.jsonl')]
    plan, resid, errs = [], [], []
    st = collections.Counter()
    lines_stat = collections.defaultdict(collections.Counter)
    unit_stat = collections.defaultdict(collections.Counter)
    for f in files:
        top = f.split('/')[1] if not f.startswith('knowledge_base/domains/') else 'domains'
        text = subprocess.run(['git', '-C', REPO, 'show', f'HEAD:{f}'], capture_output=True, text=True, check=True).stdout
        L = text.split('\n')
        regprot = collections.defaultdict(set)
        for r in reg:
            if r['kb_file'] != f: continue
            sp = r['kb_text_span']
            cnt = text.count(sp)
            if cnt != r.get('span_count_in_file', cnt) or cnt == 0:
                errs.append(f"WARN registry {r['id']}: span count {cnt} != {r.get('span_count_in_file')} in {f}")
            for li, line in enumerate(L):
                s = line.find(sp)
                while s >= 0:
                    regprot[li].update((i, r['id'], r.get('cat', '-')) for i in range(s, s + len(sp)))
                    s = line.find(sp, s + 1)
        if f.startswith('knowledge_base/domains/'): pages = sorted(DOM.get(f.split('/')[2], set()) | P.get(f, set()))
        else: pages = sorted(P.get(f, set()))
        fence = False; note = False; comment = False; nav = False
        for li, line in enumerate(L):
            s = line.strip()
            if re.match(r'^\s*(```|~~~)', line): fence = not fence; continue
            if fence: continue
            if comment:
                if '-->' in line: comment = False
                continue
            if '<!--' in line and '-->' not in line: comment = True; continue
            if re.match(r'^\s*>\s*KB note', line): note = True
            elif not s.startswith('>'): note = False
            if not s or is_sep(line): continue
            # fixed list
            for (ff, rx, b, a, c, pg, ev) in FIXED_RULES:
                if ff == f and (rx == li + 1 if isinstance(rx, int) else re.search(rx, line)):
                    col = line.find(b)
                    while col >= 0:
                        plan.append(dict(file=f, line=li + 1, col=col, before=b, after=a, **{'class': c}, pdf_page=pg, evidence=ev, fixed=True))
                        col = line.find(b, col + len(b))
            heading = s.startswith('#') or bool(re.fullmatch(r'\*\*[^*]+\*\*', s))  # a2 ruling (5): bold-only pseudo-headings = headings (O60)
            kind = 'heading' if heading else 'kb_note' if note else 'body'
            if heading: nav = bool(re.search(r'cross.?ref|related|see also|navigation|quick (ref|link)', s, re.I))
            navline = nav or bool(re.search(r'\]\([^)]*(\.md|/)(#[^)]*)?\)', line)) or bool(re.match(r'^\s*>\s*\*?\*?(Class|Structure)\b', line))
            istable = line.lstrip(' >').startswith('|')
            if f.endswith('/spec.md'): line_v = re.sub(r'^(\s*- \*\*[A-Za-z ]+:\*\*)', lambda m: '\x00' * len(m.group(1)), line)
            else: line_v = line
            prot = set()
            segs = visible(line_v, prot)
            segs = [[x for x in sg if x[0] != '\x00'] for sg in segs]
            line_units = []
            for seg in segs:
                norm, spans, txt = tokenize(seg)
                for k, tk in enumerate(norm):
                    if tk not in CLS: continue
                    a0, a1 = spans[k]
                    kbtxt = line[a0:a1]
                    u = dict(cls=CLS[tk], kb=kbtxt, col=a0, end=a1)
                    line_units.append(u)
                    if not pages: u['res'] = 'no_range'; continue
                    hits, win = [], None
                    short = istable and sum(ch.isalnum() for ch in norm) < 6
                    for (wl, wr) in ((0, 0),) if short else ((24, 24), (16, 16), (10, 10), (0, 16), (0, 10), (16, 0), (10, 0)):
                        left = norm[:k] if short else norm[max(0, k - wl):k] if wl else ''
                        right = norm[k + 1:] if short else norm[k + 1:k + 1 + wr] if wr else ''
                        na = sum(ch.isalnum() for ch in left + right)
                        if na < (3 if short else 6): continue
                        hits = search(pages, left + tk + right, len(left))
                        if hits: win = 'cell' if short else f'{wl}/{wr}'; break
                    if not hits: u['res'] = 'zero_hit'; continue
                    chars = {target_char(h['ch'], kbtxt) for h in hits}
                    u['hits'] = hits; u['win'] = win
                    if len(chars) > 1: u['res'] = 'inconsistent'; u['pdf'] = sorted(chars); continue
                    pc = chars.pop(); u['pdf'] = pc
                    # spacing (O59): only when the resulting char is an en/em dash and every hit gives a definite answer
                    sp_ops = []
                    if pc in '–—':
                        for side, kbi in (('before', a0 - 1), ('after', a1)):
                            vals = {h[side] for h in hits} - {'nl'}
                            if len(vals) != 1 or kbi < 0 or kbi >= len(line): continue
                            want = vals.pop() == 'sp'
                            have = line[kbi] == ' '
                            nb = line[kbi - 1] if side == 'before' and kbi > 0 else line[kbi + 1] if side == 'after' and kbi + 1 < len(line) else ''
                            if have and not want and nb != ' ' and line[kbi] == ' ' and nb not in '|': sp_ops.append((kbi, ' ', ''))
                            elif want and not have and line[kbi] not in '|': sp_ops.append((a0 if side == 'before' else a1, '', ' '))
                    if pc == kbtxt and not sp_ops: u['res'] = 'same'; continue
                    blocked = None
                    if any(i in prot for i in range(a0, a1)): blocked = 'protected_md'
                    rp = {x for i in range(a0, a1) for x in regprot.get(li, ()) if x[0] == i}
                    if rp: blocked = 'registry:' + ','.join(sorted({x[1] + '/' + x[2] for x in rp}))
                    if kind != 'body': blocked = kind
                    if pc != kbtxt and (kbtxt in ('--', '−') or pc == '−'): blocked = blocked or 'needs_rule:' + kbtxt + '->' + pc
                    if blocked:
                        u['res'] = 'blocked'; u['why'] = blocked; continue
                    u['res'] = 'planned'
                    pgs = sorted({h['page'] for h in hits})
                    modes = collections.Counter(h['mode'] for h in hits)
                    ctx = ''.join(ch for ch in line[max(0, a0 - 25):a1 + 25])
                    ev = f"hits={dict(modes)} pages={pgs} win={win} kbctx={ctx!r}"
                    if pc != kbtxt:
                        plan.append(dict(file=f, line=li + 1, col=a0, before=kbtxt, after=pc, **{'class': cls_name(kbtxt, pc)}, pdf_page=pgs[0], evidence=ev))
                    for (col, b, a) in sp_ops:
                        plan.append(dict(file=f, line=li + 1, col=col, before=b, after=a, **{'class': 'space:' + ('del' if b else 'add') + '@' + pc}, pdf_page=pgs[0], evidence=ev))
            if not line_units: continue
            res = collections.Counter(u['res'] for u in line_units)
            for u in line_units: unit_stat[top][u['cls'] + ':' + u['res']] += 1
            diff = any(u.get('pdf') not in (None, u['kb']) and isinstance(u.get('pdf'), str) for u in line_units)
            if kind != 'body':
                if diff or res['inconsistent']:
                    resid.append(dict(file=f, line=li + 1, kind=kind, units=[(u['kb'], u.get('pdf'), u['res'], u.get('why')) for u in line_units if u['res'] != 'same']))
                lines_stat[top]['skip_' + kind] += 1
                continue
            ls = lines_stat[top]
            ls['eligible'] += 1
            if res['planned']: ls['planned'] += 1
            if res['zero_hit'] or res['no_range']: ls['has_zero_hit'] += 1
            if res['inconsistent']: ls['has_inconsistent'] += 1
            if res['blocked']: ls['has_blocked'] += 1
            if set(res) <= {'same', 'planned'}:
                ls['fully_resolved'] += 1
                ls['fully_resolved_same' if not res['planned'] else 'fully_resolved_planned'] += 1
            if diff or res['inconsistent']: ls['known_diff'] += 1
            if diff and set(res) <= {'same', 'planned'} and not res['blocked']: ls['known_diff_resolved'] += 1
            fx_cols = {(p['col'], p['col'] + len(p['before'])) for p in plan if p.get('fixed') and p['file'] == f and p['line'] == li + 1}
            bad = [u for u in line_units if u['res'] in ('zero_hit', 'inconsistent', 'blocked', 'no_range') and not any(a <= u['col'] < b for a, b in fx_cols)]
            if bad:
                rk = 'kb_nav' if navline else 'table_elision' if all(u['kb'] == '...' and u['res'] == 'zero_hit' for u in bad) and istable else kind
                if rk != kind: ls['zero_hit_' + rk] += 1
                resid.append(dict(file=f, line=li + 1, kind=rk, units=[(u['kb'], u.get('pdf'), u['res'], u.get('why'), u['col']) for u in bad]))
    with open(FIXED_OUT, 'w') as fo:  # render-checked fixed list: the only alnum/bracket changes typo_assert.py lets through
        for p in sorted(plan, key=lambda x: (x['file'], x['line'], x['col'])):
            if p.get('fixed'): fo.write(json.dumps({k: p[k] for k in ('file', 'line', 'col', 'before', 'after', 'class', 'pdf_page', 'evidence')}, ensure_ascii=False) + '\n')
    with open(OUT, 'w') as fo:
        for p in sorted(plan, key=lambda x: (x['file'], x['line'], x['col'])): fo.write(json.dumps(p, ensure_ascii=False) + '\n')
    with open(RESID_OUT, 'w') as fo:  # residual list (KB side only; no PDF text)
        for r in resid: fo.write(json.dumps(r, ensure_ascii=False) + '\n')
    json.dump(dict(lines=lines_stat, units=unit_stat, resid=resid, errs=errs, n_plan=len(plan)), open(STATS, 'w'), ensure_ascii=False, indent=0)
    print('plan', len(plan), 'resid lines', len(resid), 'errs', len(errs))
    for e in errs: print('ERR', e)


def apply(plan_path, kb_root, allow_repo=False):
    """Apply a plan to a KB tree (repo knowledge_base/ only with --allow-repo, i.e. an authorised write attempt). Columns refer to HEAD lines."""
    assert allow_repo or os.path.realpath(kb_root) != os.path.realpath(f'{REPO}/knowledge_base'), 'refusing to write repo knowledge_base/ without --allow-repo'
    by = collections.defaultdict(list)
    for l in open(plan_path):
        p = json.loads(l); by[p['file']].append(p)
    for f, ps in by.items():
        path = os.path.join(kb_root, os.path.relpath(f, 'knowledge_base'))
        L = subprocess.run(['git', '-C', REPO, 'show', f'HEAD:{f}'], capture_output=True, text=True, check=True).stdout.split('\n')
        for p in sorted(ps, key=lambda x: (x['line'], x['col']), reverse=True):
            ln = L[p['line'] - 1]
            assert ln[p['col']:p['col'] + len(p['before'])] == p['before'], p
            L[p['line'] - 1] = ln[:p['col']] + p['after'] + ln[p['col'] + len(p['before']):]
        open(path, 'w').write('\n'.join(L))
    print('applied', sum(map(len, by.values())), 'edits to', len(by), 'files under', kb_root)

if __name__ == '__main__':
    if sys.argv[1] == '--apply': apply(sys.argv[2], sys.argv[3], '--allow-repo' in sys.argv[4:])
    else: main()
