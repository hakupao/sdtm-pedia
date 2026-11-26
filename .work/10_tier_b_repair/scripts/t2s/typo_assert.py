#!/usr/bin/env python3
# S-TYPO gate: KB_ROOT (a full knowledge_base/ tree) vs `git show HEAD:knowledge_base/...`. Independent of typo_plan.py logic.
# Every changed line must be its HEAD line under the closed substitution table only:
#   ' ’ ‘ (SQ) | " “ ” (DQ) | - – — (DASH) | ... … (ELL) — same class, unit for unit; spaces may be added/removed only next to – / —;
#   bracket/alnum changes ( ( )->○, [ ]->□, ^1^ ->¹ ) only at positions listed in work/t2_batches/S-TYPO.fixed.jsonl (render-checked).
# Never touched: files outside chapters/*.md domains/*/*.md model/*.md; headings; fenced code; HTML comments; `> KB note` blocks;
#   `--X` variable prefixes; inline code; URLs / link targets; list markers; table pipes; `**`; S-CT "(SHORT) Cxxxx";
#   every registry kb_text_span occurrence (work/t2_pdf_typo_registry.jsonl) — its count per file must also stay equal.
# usage: python3 typo_assert.py [KB_ROOT] [--plan PLAN.jsonl]   (--plan: also require KB_ROOT == HEAD + plan exactly). Exit 1 on violation.
import re, sys, os, json, glob, fnmatch, difflib, subprocess, collections
REPO = '/Volumes/DevSSD/Project/sdtm-pedia'
W = f'{REPO}/.work/10_tier_b_repair'
args = [a for a in sys.argv[1:]]
PLAN = None
if '--plan' in args:
    i = args.index('--plan'); PLAN = args[i + 1]; del args[i:i + 2]
KB = args[0] if args else f'{REPO}/knowledge_base'
SCOPE = ['chapters/*.md', 'domains/*/*.md', 'model/*.md']
UNIT = {"'": 'SQ', '’': 'SQ', '‘': 'SQ', '"': 'DQ', '“': 'DQ', '”': 'DQ', '-': 'DASH', '–': 'DASH', '—': 'DASH', '…': 'ELL'}
errs = []

def head(path):
    r = subprocess.run(['git', '-C', REPO, 'show', f'HEAD:knowledge_base/{path}'], capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else None

def in_scope(rel):
    return any(fnmatch.fnmatchcase(rel, g) and rel.count('/') == g.count('/') for g in SCOPE)

def units(s):
    out, k = [], 0
    while k < len(s):
        if s.startswith('...', k): out.append('ELL'); k += 3; continue
        c = s[k]
        if c not in UNIT: return None
        out.append(UNIT[c]); k += 1
    return out

def protected(line, spans):
    P = set()
    def add(a, b): P.update(range(a, b))
    m = re.match(r'^\s*(?:>\s*)*(?:(?:[-*+]|\d+\.)\s+)?', line); add(0, m.end())
    for rx in (r'--(?=[A-Z])', r'`[^`]*`', r'\]\([^)]*\)', r'https?://[^\s)>|`]+|www\.[^\s)>|`]+', r'<!--.*?-->|</?[a-zA-Z][^>]*>',
               r'\*\*', r'\|', r'\((?:[A-Z0-9_]+)\) C\d+'):
        for mm in re.finditer(rx, line): add(mm.start(), mm.end())
    for sp in spans:
        s = line.find(sp)
        while s >= 0: add(s, s + len(sp)); s = line.find(sp, s + 1)
    return P

def check_line(old, new, P):
    """returns None if new is old under the closed table, else a reason"""
    sm = difflib.SequenceMatcher(None, old, new, autojunk=False)
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == 'equal': continue
        a, b = old[i1:i2], new[j1:j2]
        if any(i in P for i in range(i1, i2)) or (i1 == i2 and i1 - 1 in P and i1 in P):
            return f'touches protected position {i1}: {a!r}->{b!r}'
        an, bn = re.sub(r'\s', '', a), re.sub(r'\s', '', b)
        ua, ub = units(an), units(bn)
        if ua is None or ub is None: return f'non-table char change {a!r}->{b!r} @{i1}'
        if ua != ub: return f'unit class/count change {a!r}->{b!r} @{i1}'
        wa, wb = re.sub(r'\S', '', a), re.sub(r'\S', '', b)
        if wa != wb:
            if set(wa + wb) - {' '}: return f'non-space whitespace change @{i1}'
            near = new[max(0, j1 - 1):j2 + 1]  # the resulting char must be the en/em dash (a hyphen never gains/loses spaces)
            if not ('–' in near or '—' in near): return f'space change not next to an en/em dash @{i1}: {a!r}->{b!r}'
    return None

# quote direction (a2 hardening): every curly quote a change introduces must fit its neighbours.
# open “ ‘ : left neighbour not alnum, right neighbour not whitespace; close ” : left not whitespace, right not alnum;
# ’ (close / apostrophe): left not whitespace. Whitelist: MH/assumptions.md:27 — PDF p173 prints `History“` / `History,“` (reversed “) twice, copied per U1.
QWL = {('domains/MH/assumptions.md', 27): 2}

def quote_dir(old, new):
    bad = []
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, old, new, autojunk=False).get_opcodes():
        if tag == 'equal': continue
        for j in range(j1, j2):
            c = new[j]
            if c not in '“”‘’': continue
            L = new[j - 1] if j else ' '
            R = new[j + 1] if j + 1 < len(new) else ' '
            ok = {'“': not L.isalnum() and not R.isspace(), '‘': not L.isalnum() and not R.isspace(),
                  '”': not L.isspace() and not R.isalnum(), '’': not L.isspace()}[c]
            if not ok: bad.append((j, c, new[max(0, j - 12):j + 12]))
    return bad

def ctx_flags(L):
    """per HEAD line: 'heading' / 'fence' / 'comment' / 'kbnote' / '' """
    out, fence, note, com = [], False, False, False
    for line in L:
        s = line.strip()
        if re.match(r'^\s*(```|~~~)', line): out.append('fence'); fence = not fence; continue
        if fence: out.append('fence'); continue
        if com: out.append('comment'); com = '-->' not in line; continue
        if '<!--' in line and '-->' not in line: out.append('comment'); com = True; continue
        if re.match(r'^\s*>\s*KB note', line): note = True
        elif not s.startswith('>'): note = False
        out.append('heading' if s.startswith('#') or re.fullmatch(r'\*\*[^*]+\*\*', s) else 'kbnote' if note else '')  # bold-only line = pseudo-heading (O60)
    return out

def main():
    reg = collections.defaultdict(list)
    for l in open(f'{W}/work/t2_pdf_typo_registry.jsonl'):
        r = json.loads(l); reg[r['kb_file'][len('knowledge_base/'):]].append(r['kb_text_span'])
    fixed = collections.defaultdict(list)
    for l in open(f'{W}/work/t2_batches/S-TYPO.fixed.jsonl'):
        r = json.loads(l); fixed[(r['file'][len('knowledge_base/'):], r['line'])].append(r)
    plan = collections.defaultdict(list)
    if PLAN:
        for l in open(PLAN):
            r = json.loads(l); plan[r['file'][len('knowledge_base/'):]].append(r)
    headfiles = set(subprocess.run(['git', '-C', REPO, 'ls-tree', '-r', '--name-only', 'HEAD', 'knowledge_base/'], capture_output=True, text=True, check=True).stdout.split())
    headfiles = {f[len('knowledge_base/'):] for f in headfiles}
    treefiles = {os.path.relpath(os.path.join(d, f), KB) for d, _, fs in os.walk(KB) for f in fs}
    treefiles = {f for f in treefiles if not any(c.startswith('.') for c in f.split('/'))}  # .DS_Store / .omc hook state (untracked, ignored)
    for f in sorted(treefiles ^ headfiles): errs.append(f'{f}: file added/removed vs HEAD')
    nchg_lines = nchg_files = 0
    for f in sorted(treefiles & headfiles):
        old_t = head(f)
        try: new_t = open(os.path.join(KB, f), encoding='utf-8').read()
        except UnicodeDecodeError:
            if open(os.path.join(KB, f), 'rb').read() != subprocess.run(['git', '-C', REPO, 'show', f'HEAD:knowledge_base/{f}'], capture_output=True, check=True).stdout: errs.append(f'{f}: binary changed')
            continue
        if PLAN and in_scope(f):
            L = old_t.split('\n')
            for p in sorted(plan.get(f, []), key=lambda x: (x['line'], x['col']), reverse=True):
                ln = L[p['line'] - 1]
                if ln[p['col']:p['col'] + len(p['before'])] != p['before']: errs.append(f'{f}:{p["line"]}: plan before mismatch'); continue
                L[p['line'] - 1] = ln[:p['col']] + p['after'] + ln[p['col'] + len(p['before']):]
            if '\n'.join(L) != new_t: errs.append(f'{f}: tree != HEAD + plan')
        if old_t == new_t: continue
        nchg_files += 1
        if not in_scope(f): errs.append(f'{f}: out-of-scope file changed'); continue
        for sp in set(reg.get(f, [])):
            if old_t.count(sp) != new_t.count(sp): errs.append(f'{f}: registry span count changed {sp!r}')
        Lo, Ln = old_t.split('\n'), new_t.split('\n')
        if len(Lo) != len(Ln): errs.append(f'{f}: line count {len(Lo)} -> {len(Ln)}'); continue
        flags = ctx_flags(Lo)
        for i, (o, n) in enumerate(zip(Lo, Ln)):
            if o == n: continue
            nchg_lines += 1
            if flags[i]: errs.append(f'{f}:{i + 1}: changed {flags[i]} line'); continue
            qb = quote_dir(o, n)
            if len(qb) > QWL.get((f, i + 1), 0) or any(x[1] != '“' for x in qb):
                errs.append(f'{f}:{i + 1}: quote direction {[(x[0], x[1], x[2]) for x in qb]}')
            P = protected(o, reg.get(f, []))
            why = check_line(o, n, P)
            if why:
                fx = fixed.get((f, i + 1), [])
                if fx:  # retry with the render-checked fixed substitutions applied to the HEAD line
                    o2, shift, fxp = o, 0, set()  # fixed substitutions applied left to right; their results are then frozen
                    for r in sorted(fx, key=lambda x: x['col']):
                        c = r['col'] + shift
                        if o2[c:c + len(r['before'])] == r['before']:
                            o2 = o2[:c] + r['after'] + o2[c + len(r['before']):]
                            fxp.update(range(c, c + len(r['after'])))
                            shift += len(r['after']) - len(r['before'])
                    why2 = check_line(o2, n, protected(o2, reg.get(f, [])) | fxp)
                    if why2 is None: continue
                    why = why + ' | with fixed list: ' + why2
                errs.append(f'{f}:{i + 1}: {why}')
    print(f'changed files {nchg_files}, changed lines {nchg_lines}, violations {len(errs)}')
    for e in errs[:60]: print('  FAIL', e)
    print('PASS' if not errs else 'FAIL')
    sys.exit(1 if errs else 0)

main()
