#!/usr/bin/env python3
# Mutation test for typo_assert.py (retrospective rule 5). Each mutant = scratch copy of (HEAD + S-TYPO plan) with one planted defect;
# typo_assert.py must exit 1 on every mutant and 0 on the two controls. usage: python3 typo_mutate.py SCRATCH_DIR
import os, re, sys, json, shutil, subprocess
REPO = '/Volumes/DevSSD/Project/sdtm-pedia'
T = f'{REPO}/.work/10_tier_b_repair'
PLAN = f'{T}/work/t2_batches/S-TYPO.plan.jsonl'
SD = sys.argv[1]
BASE = f'{SD}/kb_mut_base'

def run(root, plan=True):
    a = ['python3', f'{T}/scripts/t2s/typo_assert.py', root] + (['--plan', PLAN] if plan else [])
    r = subprocess.run(a, capture_output=True, text=True)
    return r.returncode, (r.stdout.strip().split('\n') + [''])[1].strip()[:150]

def fresh(name):
    d = f'{SD}/kb_mut_{name}'
    shutil.rmtree(d, ignore_errors=True); shutil.copytree(BASE, d)
    return d

def edit(root, rel, pred, fn):
    if rel is None:  # first in-scope file (sorted) holding a matching line
        import glob
        for g in sorted(glob.glob(f'{root}/chapters/*.md') + glob.glob(f'{root}/domains/*/*.md') + glob.glob(f'{root}/model/*.md')):
            if any(pred(l) for l in open(g).read().split('\n')): rel = os.path.relpath(g, root); break
    p = f'{root}/{rel}'; L = open(p).read().split('\n')
    for i, l in enumerate(L):
        if pred(l):
            n = fn(l); assert n != l, (rel, l[:80]); L[i] = n; open(p, 'w').write('\n'.join(L)); return f'{rel}:{i + 1}'
    raise SystemExit(f'no target line in {rel}')

def sub1(pat, rep):
    return lambda l: re.sub(pat, rep, l, count=1)

shutil.rmtree(BASE, ignore_errors=True); shutil.copytree(f'{REPO}/knowledge_base', BASE)
subprocess.run(['python3', f'{T}/scripts/t2s/typo_plan.py', '--apply', PLAN, BASE], check=True, capture_output=True)
M = [  # (id, description, file, line predicate, transform)
    ('M1', 'alnum change in a planned line', None, lambda l: '“NOT DONE”' in l, sub1('NOT DONE', 'NOT DONF')),
    ('M2', 'delete one hyphen', None, lambda l: not l.lstrip().startswith(('#', '>', '`')) and 'sponsor-defined' in l, sub1('sponsor-defined', 'sponsordefined')),
    ('M3', 'heading typo change', 'domains/AE/assumptions.md', lambda l: l.startswith('#') and '—' in l, sub1('—', '–')),
    ('M4', '--VAR prefix -> en dash', 'chapters/ch04_general_assumptions.md', lambda l: not l.startswith('#') and '--TESTCD' in l, sub1('--TESTCD', '–TESTCD')),
    ('M5', 'registry span B-TA T-4 hyphen -> en dash', 'domains/TA/examples.md', lambda l: 'Randomized to 5 mg - 10 mg - Placebo' in l, sub1('5 mg - 10', '5 mg – 10')),
    ('M5b', 'registry span B-FA T-1 curly -> straight', 'domains/FA/assumptions.md', lambda l: '“findings about”' in l, sub1('“findings about”', '"findings about"')),
    ('M6', 'non-table char substitution (“ -> «)', None, lambda l: '“NOT DONE”' in l, sub1('“NOT', '«NOT')),
    ('M7', 'delete one extra quote', None, lambda l: '“NOT DONE”' in l, sub1('“NOT DONE”', '“NOT DONE')),
    ('M8', 'delete a plain inter-word space', None, lambda l: not l.lstrip().startswith(('#', '>', '`')) and 'sponsor-defined' in l and '—' not in l and '–' not in l, sub1(r'(\w) (\w)', r'\1\2')),
    ('M9', "cross-class replace (' -> “)", None, lambda l: not l.lstrip().startswith(('#', '>', '`')) and "'" in l, sub1("'", '“')),
    ('M10', 'change inside fenced code (mermaid)', 'domains/DM/examples.md', lambda l: '["' in l, sub1('"', '“')),
    ('M11', 'change inside KB note', None, lambda l: l.startswith('> KB note') and ('"' in l or '-' in l), lambda l: l.replace('"', '“', 1) if '"' in l else l.replace('-', '–', 1)),
    ('M12', 'out-of-scope file (terminology)', 'terminology/core/ae.md', lambda l: '-' in l and not l.startswith('#'), sub1('-', '–')),
    ('M13', 'CRF box not in fixed list ([ ] -> □, ch04)', 'chapters/ch04_general_assumptions.md', lambda l: '[ ] Brown' in l, sub1(r'\[ \] Brown', '□ Brown')),
    ('M14', 'non-variable "--" -> en dash outside fixed list (CE "--/---/--")', 'domains/CE/examples.md', lambda l: l.startswith('| Date of collection |'), sub1('--/', '–/')),
    ('M16b', 'space added next to a hyphen in a date', None, lambda l: not l.lstrip().startswith(('#', '>', '`')) and re.search(r'\| \d{4}-\d\d-\d\d \|', l), sub1(r'(\| \d{4})-', r'\1 -')),
    ('M15', 'inline code hyphen -> en dash', 'chapters/ch04_general_assumptions.md', lambda l: re.search(r'`[^`]*-[^`]*`', l) and not l.startswith('#'), lambda l: re.sub(r'(`[^`-]*)-', r'\1–', l, count=1)),
    ('M16', 'space removed next to a hyphen (not en/em)', None, lambda l: not l.lstrip().startswith(('#', '>', '`')) and re.search(r'\w - \w', l) and '—' not in l and '–' not in l, sub1(r'(\w) - (\w)', r'\1-\2')),
    ('M17', 'line inserted', 'domains/AE/assumptions.md', lambda l: not l.lstrip().startswith(('#', '>', '`')) and 'AE' in l, lambda l: l + '\n'),
    ('M18', 'list marker "-" -> en dash', 'domains/AE/spec.md', lambda l: l.startswith('- **Label:**'), sub1('^-', '–')),
    ('M19', 'CRF ( ) -> ○ (removed from plan by a2 ruling)', 'domains/CE/examples.md', lambda l: l.startswith('| Nausea |'), sub1(r'\( \) Yes', '○ Yes')),
    ('M19b', 'fixed-list position given wrong char (ch04 U+2212 -> en dash)', 'chapters/ch04_general_assumptions.md', lambda l: 'as VSDTC-VSRFTDTC.' in l, sub1('VSDTC-VSRFTDTC', 'VSDTC–VSRFTDTC')),
    ('M20', 'fixed-list superscript wrong digit (ch08 ¹ -> ²)', 'chapters/ch08_relationships.md', lambda l: l.startswith('¹In this column'), sub1('¹', '²')),
    ('V1', 'open quote written as close (“ -> ”)', None, lambda l: '“NOT DONE”' in l, sub1('“NOT DONE”', '”NOT DONE”')),
    ('V4', 'apostrophe written as left single quote (’ -> ‘)', None, lambda l: 'sponsor’s' in l and not l.lstrip().startswith(('#', '>')), sub1('sponsor’s', 'sponsor‘s')),
    ('V6', 'bold-only pseudo-heading changed', 'chapters/ch08_relationships.md', lambda l: l.strip() == '**RELREC — Description/Overview**', sub1('—', '–')),
    ('V9', 'close quote written as open (” -> “)', None, lambda l: '“NOT DONE”' in l, sub1('“NOT DONE”', '“NOT DONE“')),
]
rows, ok = [], True
c0, _ = run(BASE); c1, _ = run(f'{REPO}/knowledge_base', plan=False)
rows.append(('C0', 'positive control: HEAD + plan (--plan)', '-', c0, 'PASS' if c0 == 0 else 'FAIL'))
rows.append(('C1', 'positive control: repo knowledge_base as written (no --plan)', '-', c1, 'PASS' if c1 == 0 else 'FAIL'))
ok = c0 == 0 and c1 == 0
for mid, desc, rel, pred, fn in M:
    d = fresh(mid)
    if rel and rel.startswith('terminology/') and not os.path.exists(f'{d}/{rel}'):
        rel = next(os.path.relpath(os.path.join(a, f), d) for a, _, fs in os.walk(f'{d}/terminology') for f in fs if f.endswith('.md'))
    loc = edit(d, rel, pred, fn)
    code, msg = run(d, plan=False)
    rows.append((mid, desc, loc, code, msg))
    ok &= code == 1
    shutil.rmtree(d, ignore_errors=True)
for r in rows: print(' | '.join(str(x) for x in r))
print('MUTATION SUITE', 'OK' if ok else 'BROKEN')
sys.exit(0 if ok else 1)
