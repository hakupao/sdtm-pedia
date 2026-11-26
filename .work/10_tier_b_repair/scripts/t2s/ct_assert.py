# S-CT gate: every domains/*/spec.md under KB_ROOT vs `git show HEAD:knowledge_base/domains/<D>/spec.md`.
# allowed changes only: Controlled Terms lines (U5 "(SHORT) Cxxxx" prefixes / U6 DOMAIN = domain code), one KB note line (+ blank)
# before "## Cross References" in files that carry C-codes, and the SR SRDY whitelist line (SR T-5). Exit 1 on any violation.
# usage: python3 ct_assert.py [KB_ROOT]   (KB_ROOT = a full knowledge_base/ tree; non-spec.md files must equal HEAD)
import re, sys, os, subprocess, difflib, zipfile
import xml.etree.ElementTree as ET
REPO = '/Volumes/DevSSD/Project/sdtm-pedia'
KB = sys.argv[1] if len(sys.argv) > 1 else f'{REPO}/knowledge_base'
NOTE = '> KB note (not in SDTMIG): C-codes after the parenthesised codelist names are NCI codelist codes added by this KB (CDISC CT).'
SRDY_OLD = '- **CDISC Notes:** Actual study day of visit/collection/exam expressed in integer days relative to sponsor- defined RFSTDTC in Demographics.'
SRDY_NEW = SRDY_OLD.replace('sponsor- defined', 'sponsor-defined')
CTP = '- **Controlled Terms:**'
NS = '{http://schemas.openxmlformats.org/spreadsheetml/2006/main}'
z = zipfile.ZipFile(f'{REPO}/source/cdisc/SDTM Terminology.xlsx')
ss = [''.join(t.text or '' for t in si.iter(NS + 't')) for si in ET.fromstring(z.read('xl/sharedStrings.xml')).iter(NS + 'si')]
name2code = {}
for row in ET.fromstring(z.read('xl/worksheets/sheet2.xml')).iter(NS + 'row'):
    c = {}
    for cell in row.iter(NS + 'c'):
        v = cell.find(NS + 'v')
        c[re.match(r'[A-Z]+', cell.get('r'))[0]] = (ss[int(v.text)] if cell.get('t') == 's' else v.text) if v is not None else ''
    if c.get('A', '').startswith('C') and not c.get('B') and c.get('E'): name2code.setdefault(c['E'], set()).add(c['A'])
errs, n1, ncode, n6, nnote, nsr = [], 0, 0, 0, 0, 0
doms = sorted(d for d in os.listdir(f'{KB}/domains') if os.path.exists(f'{KB}/domains/{d}/spec.md'))
for d in doms:
    a = subprocess.run(['git', '-C', REPO, 'show', f'HEAD:knowledge_base/domains/{d}/spec.md'], capture_output=True, text=True, check=True).stdout.split('\n')
    b = open(f'{KB}/domains/{d}/spec.md').read().split('\n')
    def var_at(L, i):
        for k in range(i, -1, -1):
            m = re.match(r'### (\S+)$', L[k])
            if m: return m[1]
    has_code = any(l.startswith(CTP) and re.search(r'C\d+', l) for l in a)
    notes_here = 0
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
        if op == 'equal': continue
        if op == 'insert':
            ins = b[j1:j2]
            nn = ins.count(NOTE); notes_here += nn
            if set(ins) - {NOTE, ''} or nn != 1 or len(ins) != 2:
                errs.append(f'{d}: illegal insert at {j1+1}: {ins!r}'); continue
            k = j1 + ins.index(NOTE)
            nxt = next((x for x in b[k + 1:] if x != ''), None)
            if nxt != '## Cross References' or '---' not in b[:k]: errs.append(f'{d}: KB note misplaced at {k+1}')
            continue
        if op == 'delete' or (i2 - i1) != (j2 - j1):
            errs.append(f'{d}: {op} a{i1+1}-{i2} b{j1+1}-{j2} (line add/remove outside whitelist)'); continue
        for x, y, ia in zip(a[i1:i2], b[j1:j2], range(i1, i2)):
            v = var_at(a, ia)
            if d == 'SR' and v == 'SRDY' and x == SRDY_OLD and y == SRDY_NEW: nsr += 1; continue
            if not (x.startswith(CTP) and y.startswith(CTP)): errs.append(f'{d} {v}: non-CT line changed: {x!r} -> {y!r}'); continue
            xv, yv = x[len(CTP) + 1:], y[len(CTP) + 1:]  # byte-exact: no strip
            if v == 'DOMAIN' and x == CTP + ' ' and y == CTP + ' ' + d: n6 += 1; continue
            pairs = re.findall(r'\(([A-Za-z0-9_]+)\) (C\d+)', yv)
            codes = re.findall(r'C\d+', xv)
            if not pairs or x != CTP + ' ' + '; '.join(codes) or y != CTP + ' ' + '; '.join(f'({n}) {c}' for n, c in pairs) \
                    or [c for _, c in pairs] != codes:
                errs.append(f'{d} {v}: CT line != expected prefix-added line: {x!r} -> {y!r}'); continue
            bad = [(n, c) for n, c in pairs if name2code.get(n) != {c}]
            if bad: errs.append(f'{d} {v}: short name / C-code mismatch vs Terminology xlsx: {bad}'); continue
            n1 += 1; ncode += len(pairs)
    # every C-code CT line of a code-bearing file must now be prefixed
    left = [l for l in b if l.startswith(CTP) and re.search(r'(?<!\) )C\d+', l)]
    if left: errs.append(f'{d}: {len(left)} CT lines with un-prefixed C-code')
    dm = [l for l, v in ((l, var_at(b, i)) for i, l in enumerate(b) if l.startswith(CTP)) if v == 'DOMAIN']
    if dm and dm[0][len(CTP):].strip() != d: errs.append(f'{d}: DOMAIN CT != {d}')
    if notes_here != (1 if has_code else 0) or b.count(NOTE) != (1 if has_code else 0): errs.append(f'{d}: KB note count {b.count(NOTE)} (has_code={has_code})')
    nnote += b.count(NOTE)
# scope: only knowledge_base/domains/*/spec.md may differ from HEAD (byte compare of every file + added/removed files)
head = dict(l.split('\t', 1)[::-1] for l in subprocess.run(['git', '-C', REPO, 'ls-tree', '-r', 'HEAD', 'knowledge_base'], capture_output=True,
            text=True, check=True).stdout.splitlines())  # path -> "mode blob sha"
local = [os.path.relpath(os.path.join(dp, fn), os.path.dirname(KB.rstrip('/'))) for dp, _, fs in os.walk(KB) for fn in fs]
local = ['knowledge_base/' + p.split('/', 1)[1] for p in local]
ign = set(subprocess.run(['git', '-C', REPO, 'check-ignore', '--no-index', '--stdin'], input='\n'.join(local), capture_output=True, text=True).stdout.split('\n'))
local = [p for p in local if p not in ign]  # gitignored files (e.g. hook state under .omc/) are not part of the KB
shas = subprocess.run(['git', '-C', REPO, 'hash-object', '--stdin-paths'], input='\n'.join(os.path.join(KB, p.split('/', 1)[1]) for p in local),
                      capture_output=True, text=True, check=True).stdout.split()
changed = {p for p, h in zip(local, shas) if head.get(p, '').split()[-1:] != [h]} | (set(head) - set(local))
if os.path.realpath(KB) == os.path.realpath(f'{REPO}/knowledge_base'):
    changed |= set(subprocess.run(['git', '-C', REPO, 'diff', 'HEAD', '--name-only', '--', 'knowledge_base/'], capture_output=True, text=True, check=True).stdout.split())
for p in sorted(changed):
    if not re.fullmatch(r'knowledge_base/domains/[^/]+/spec\.md', p): errs.append(f'scope: non-spec.md file differs from HEAD: {p}')
exp = dict(class1=570, codes=588, class6=59, notes=59, srdy=1)
got = dict(class1=n1, codes=ncode, class6=n6, notes=nnote, srdy=nsr)
for k in exp:
    if exp[k] != got[k]: errs.append(f'count {k}: expected {exp[k]} got {got[k]}')
print('domains', len(doms), 'got', got)
for e in errs: print('FAIL', e)
print('RESULT', 'FAIL' if errs else 'PASS')
sys.exit(1 if errs else 0)
