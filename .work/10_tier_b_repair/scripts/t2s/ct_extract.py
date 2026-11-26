# S-CT extractor (dry-run): PDF spec tables (pdftotext -bbox per page) -> per-variable cells; compare with KB spec.md;
# classify Controlled Terms (U5/U6) with SDTM Terminology.xlsx cross-check; full-field diff for all domains.
# usage: python3 ct_extract.py BBDIR OUTDIR      (BBDIR holds bb_<page>.html; xlsx/PDF text never written to repo)
import re, sys, os, json, html, unicodedata, zipfile
import xml.etree.ElementTree as ET
ROOT = '/Volumes/DevSSD/Project/sdtm-pedia'
BB, OUT = sys.argv[1], sys.argv[2]
NPAGES = 461
ORDER = ['name', 'label', 'type', 'ct', 'role', 'notes', 'core']
HV = {'Variable', 'Name', 'Label', 'Type', 'Controlled', 'Terms,', 'Terms', 'Codelist', 'or', 'Format1', 'Format¹', 'Format',
      '1', 'Role', 'CDISC', 'Notes', 'Core'}

def norm(s):
    s = unicodedata.normalize('NFKC', s)
    for a, b in [('‘', "'"), ('’', "'"), ('“', '"'), ('”', '"'), ('–', '-'), ('—', '-'), ('‑', '-'), ('•', ' '), ('▪', ' ')]:
        s = s.replace(a, b)
    return re.sub(r'\s+', ' ', s).strip()

_cache = {}
def words(p):
    if p not in _cache:
        t = open(f'{BB}/bb_{p}.html').read()
        _cache[p] = [(float(m[1]), float(m[2]), float(m[3]), float(m[4]), html.unescape(m[5])) for m in
                     re.finditer(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">(.*?)</word>', t)]
    return _cache[p]

def lines(W):
    L = {}
    for w in W:
        k = next((y for y in L if abs(y - w[1]) < 2.5), None)
        L.setdefault(k if k is not None else w[1], []).append(w)
    return {y: sorted(v) for y, v in sorted(L.items())}

def reading_order(ws):  # group by baseline (yMax) so smaller-font words stay on their line
    out, cur, base = [], [], None
    for w in sorted(ws, key=lambda w: w[3]):
        if base is not None and w[3] - base > 3: out += sorted(cur); cur = []
        if not cur: base = w[3]
        cur.append(w)
    return out + sorted(cur)

def find_start(dom):
    pat = re.compile(r'^8\.4\.1 Supplemental Qualifiers' if dom == 'SUPPQUAL' else r'^%s [–-] Specification' % dom)
    for p in range(20, NPAGES + 1):  # skip TOC
        for y, L in lines(words(p)).items():
            if L[0][0] < 100 and pat.match(' '.join(w[4] for w in L)):
                return p, y
    raise SystemExit('no start for ' + dom)

def header(W, top):
    """header band: lines below top containing 'Controlled' and lines near it made only of header words"""
    LL = lines([w for w in W if w[1] > top])
    for y, L in LL.items():
        t = [w[4] for w in L]
        if 'Controlled' in t and 'Core' in t and 'Variable' in t:
            band = [yy for yy, LB in LL.items() if y - 1 <= yy <= y + 40 and all(w[4] in HV for w in LB)]
            # contiguous from y
            keep = [];
            for yy in band:
                if not keep or yy - keep[-1] < 16: keep.append(yy)
                else: break
            HW = [w for yy in keep for w in LL[yy]]
            var = sorted([w for w in HW if w[4] == 'Variable'], key=lambda w: (w[0], w[1]))
            vx = sorted({round(w[0]) for w in var})
            hx = lambda s: min(w[0] for w in HW if w[4] == s)
            xs = {'name': vx[0], 'label': vx[1] if len(vx) > 1 else hx('Label'), 'type': hx('Type'), 'ct': hx('Controlled'),
                  'role': hx('Role'), 'notes': hx('CDISC'), 'core': hx('Core')}
            return xs, set(keep), max(keep)
    return None, set(), top

def is_stop(L, dom):
    t = ' '.join(w[4] for w in L)
    if L[0][0] > 100: return False
    return bool(re.match(r'^1? ?In this column', t) or re.match(r'^1In ', t) or re.match(r'^[A-Z][A-Za-z]+ [–-] (Assumptions|Examples|Description)', t)
                or re.match(r'^\d+(\.\d+)+ [A-Z]', t) or re.match(r'^Assumptions for', t))

def extract(dom):
    p, top = find_start(dom)
    rows, xs, pages, notes = [], None, [], []
    while True:
        W = words(p)
        hxs, band, hb = header(W, top)
        if hxs: xs = hxs
        elif xs is None: raise SystemExit(f'{dom}: no header p{p}')
        else: notes.append(f'p{p} no header (reuse x)')
        LL = lines([w for w in W if w[1] > hb + 1])
        ylim, stopped = 9999, False
        for y, L in LL.items():
            if y in band: continue
            if L[0][4].startswith('©'): ylim = y - 1; break
            if is_stop(L, dom): ylim, stopped = y - 1, True; break
        body = [w for y, L in LL.items() if y not in band and y < ylim for w in L]
        hts = sorted(w[3] - w[1] for w in body)
        med = hts[len(hts) // 2] if hts else 10
        def _sup(w):  # small glyphs whose bottom sits clearly above the neighbouring baseline = superscript
            if w[3] - w[1] >= 0.7 * med: return False
            nb = sorted(v[3] for v in body if v is not w and v[3] - v[1] >= 0.7 * med and abs(v[3] - w[3]) < 8 and abs(v[0] - w[0]) < 120)
            return bool(nb) and w[3] < nb[len(nb) // 2] - 2
        sup = [w for w in body if _sup(w)]
        if sup: notes.append(f'p{p} superscript-size words dropped: ' + ' '.join(w[4] for w in sup))
        body = [w for w in body if w not in sup]
        bounds = [xs[k] - 3 for k in ORDER]
        col = lambda w: ORDER[max([i for i, b in enumerate(bounds) if w[0] >= b] or [0])]
        starts = sorted([w for w in body if col(w) == 'name' and re.match(r'^[A-Z][A-Z0-9]{1,7}$', w[4])], key=lambda w: w[1])
        pre = [w for w in body if not starts or w[1] < starts[0][1] - 1]
        if pre and rows:
            for w in reading_order(pre): rows[-1][col(w)].append(w[4])
            notes.append(f'p{p} CONT -> {rows[-1]["name"][0]}: ' + ' '.join(w[4] for w in pre))
        for i, s in enumerate(starts):
            y0 = s[1] - 1; y1 = starts[i + 1][1] - 1 if i + 1 < len(starts) else 9999
            r = {k: [] for k in ORDER}; r['page'] = p
            for w in reading_order([w for w in body if y0 <= w[1] < y1]): r[col(w)].append(w[4])
            rows.append(r)
        pages.append(p)
        if stopped or p >= NPAGES: break
        p += 1; top = -1
    out = []
    for r in rows:
        out.append({k: ' '.join(r[k]) for k in ORDER} | {'page': r['page']})
    return out, pages, notes

def kb(dom):
    t = open(f'{ROOT}/knowledge_base/domains/{dom}/spec.md').read()
    K = {}
    for n, b in re.findall(r'### (\S+)\n(.*?)(?=\n### |\n---|\Z)', t, re.S):
        if not re.search(r'- \*\*Order:\*\*', b): continue
        K[n] = {m[1]: m[2].strip() for m in re.finditer(r'- \*\*(.+?):\*\* ?(.*)', b)}
    return K

def xlsx_rows(path, sheet_idx):
    NS = '{http://schemas.openxmlformats.org/spreadsheetml/2006/main}'
    z = zipfile.ZipFile(path)
    ss = [''.join(t.text or '' for t in si.iter(NS + 't')) for si in ET.fromstring(z.read('xl/sharedStrings.xml')).iter(NS + 'si')]
    for r in ET.fromstring(z.read(f'xl/worksheets/sheet{sheet_idx}.xml')).iter(NS + 'row'):
        row = {}
        for c in r.iter(NS + 'c'):
            v = c.find(NS + 'v')
            row[re.match(r'[A-Z]+', c.get('r'))[0]] = (ss[int(v.text)] if c.get('t') == 's' else v.text) if v is not None else ''
        yield row

def main():
    os.makedirs(OUT, exist_ok=True)
    doms = sorted(d for d in os.listdir(f'{ROOT}/knowledge_base/domains') if os.path.exists(f'{ROOT}/knowledge_base/domains/{d}/spec.md'))
    name2code, code2name = {}, {}
    for r in xlsx_rows(f'{ROOT}/source/cdisc/SDTM Terminology.xlsx', 2):
        if r.get('A', '').startswith('C') and not r.get('B') and r.get('E'):
            name2code.setdefault(r['E'], set()).add(r['A']); code2name[r['A']] = r['E']
    ig = {}
    for r in xlsx_rows(f'{ROOT}/source/cdisc/SDTMIG_v3.4.xlsx', 2):
        if r.get('A', '').startswith('SDTMIG'): ig[(r['D'], r['E'])] = r.get('H', '')
    summary, recs, fdiffs, wsdiffs = {}, [], [], []
    for d in doms:
        P, pages, notes = extract(d)
        K = kb(d)
        pn, kn = [r['name'] for r in P], list(K)
        ords = [K[n].get('Order') for n in kn]
        summary[d] = {'pages': [pages[0], pages[-1]], 'pdf_n': len(P), 'kb_n': len(K), 'order_same': pn == kn,
                      'kb_order_seq': ords == [str(i) for i in range(1, len(K) + 1)], 'notes': notes,
                      'pdf_only': [n for n in pn if n not in K], 'kb_only': [n for n in kn if n not in pn]}
        for r in P:
            k = K.get(r['name'], {})
            for f, kf in [('label', 'Label'), ('type', 'Type'), ('role', 'Role'), ('core', 'Core'), ('notes', 'CDISC Notes')]:
                a, b = norm(r[f]), norm(k.get(kf, ''))
                if re.sub(r'\s', '', a) != re.sub(r'\s', '', b):
                    fdiffs.append({'domain': d, 'var': r['name'], 'page': r['page'], 'field': kf, 'pdf': a, 'kb': b})
                elif re.sub(r'(?<=\w)- (?=\w)', '-', a) != b:  # whitespace-only diff (PDF line-break hyphen joined)
                    wsdiffs.append({'domain': d, 'var': r['name'], 'page': r['page'], 'field': kf, 'pdf': a, 'kb': b})
            pct, kct = norm(r['ct']), norm(k.get('Controlled Terms', ''))
            pc = re.sub(r'\s', '', pct)
            names = re.findall(r'\(([A-Za-z0-9_]+)\)', pc)
            resid = re.sub(r'\([A-Za-z0-9_]+\)', '', pc).strip(';,')
            codes = re.findall(r'C\d+', kct)
            kres = re.sub(r'C\d+', '', kct).replace(';', '').strip()
            mapped = [sorted(name2code.get(n, [])) for n in names]
            xchk = {'pdf_names': names, 'name_to_code': mapped, 'kb_code_to_name': [code2name.get(c) for c in codes],
                    'igxlsx': ig.get((d, r['name']))}
            if r['name'] == 'DOMAIN':
                cls = '6'
            elif not codes and not names:
                cls = '7' if re.sub(r'\s', '', kct) == pc else '8'
            elif codes and not names:
                cls = '4'
            elif names and not codes:
                cls = '3'
            elif len(names) != len(codes):
                cls = '2'
            elif all(c in m for c, m in zip(codes, mapped)) and not kres and not resid:
                cls = '1'
            elif sorted(codes) == sorted(m[0] for m in mapped if m) and len([m for m in mapped if m]) == len(codes) and not kres and not resid:
                cls = '1o'   # same set, different order
            elif not kres and not resid:
                cls = '5'
            else:
                cls = '8'
            recs.append({'domain': d, 'var': r['name'], 'page': r['page'], 'kb_ct': kct, 'pdf_ct': pct, 'class': cls, 'xlsx_check': xchk})
        for n in summary[d]['kb_only']:
            recs.append({'domain': d, 'var': n, 'page': None, 'kb_ct': K[n].get('Controlled Terms', ''), 'pdf_ct': None, 'class': 'X', 'xlsx_check': None})
    json.dump(summary, open(f'{OUT}/summary.json', 'w'), indent=1, ensure_ascii=False)
    json.dump(fdiffs, open(f'{OUT}/fdiffs.json', 'w'), indent=1, ensure_ascii=False)
    json.dump(wsdiffs, open(f'{OUT}/wsdiffs.json', 'w'), indent=1, ensure_ascii=False)
    with open(f'{OUT}/S-CT.dryrun.jsonl', 'w') as f:
        for r in recs: f.write(json.dumps(r, ensure_ascii=False) + '\n')
    bad = {d: s for d, s in summary.items() if not (s['pdf_n'] == s['kb_n'] and s['order_same'] and s['kb_order_seq'])}
    from collections import Counter
    print('domains', len(summary), 'count/order gate fails:', {d: (s['pdf_n'], s['kb_n'], s['pdf_only'], s['kb_only']) for d, s in bad.items()})
    print('classes', Counter(r['class'] for r in recs)); print('field diffs', len(fdiffs), 'whitespace-only diffs', len(wsdiffs))

main()
