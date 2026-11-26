# S-CT transform (U5/U6 + KB note + SR T-5). Source of truth = work/t2_batches/S-CT.dryrun.jsonl (from ct_extract.py).
# usage: python3 ct_apply.py [KB_ROOT]     (default: repo knowledge_base/); writes a writer.jsonl to stdout-path arg 2 if given
import json, re, sys
REPO = '/Volumes/DevSSD/Project/sdtm-pedia'
KB = sys.argv[1] if len(sys.argv) > 1 else f'{REPO}/knowledge_base'
WJ = sys.argv[2] if len(sys.argv) > 2 else None
NOTE = '> KB note (not in SDTMIG): C-codes after the parenthesised codelist names are NCI codelist codes added by this KB (CDISC CT).'
SRDY_OLD = '- **CDISC Notes:** Actual study day of visit/collection/exam expressed in integer days relative to sponsor- defined RFSTDTC in Demographics.'
SRDY_NEW = SRDY_OLD.replace('sponsor- defined', 'sponsor-defined')
CT = '- **Controlled Terms:** '
R = [json.loads(l) for l in open(f'{REPO}/.work/10_tier_b_repair/work/t2_batches/S-CT.dryrun.jsonl')]
plan = {}
for r in R:
    if r['class'] in ('1', '6'): plan.setdefault(r['domain'], {})[r['var']] = r
log = []
for dom in sorted({r['domain'] for r in R}):
    path = f'{KB}/domains/{dom}/spec.md'
    L = open(path).read().split('\n')
    var, n_ct, has_code, sep = None, 0, False, None
    for i, line in enumerate(L):
        if line == '---' and sep is None: sep = i
        if sep is not None: continue
        m = re.match(r'### (\S+)$', line)
        if m: var = m[1]
        if line.startswith('- **Controlled Terms:**') and var in plan.get(dom, {}):
            r = plan[dom][var]
            cur = line[len(CT):] if line.startswith(CT) else ''
            assert cur == r['kb_ct'], (dom, var, cur, r['kb_ct'])
            if r['class'] == '1':
                codes = re.findall(r'C\d+', cur); names = r['xlsx_check']['pdf_names']
                assert len(codes) == len(names) and cur == '; '.join(codes), (dom, var)
                new = '; '.join(f'({n}) {c}' for n, c in zip(names, codes)); has_code = True
            else:
                assert var == 'DOMAIN' and cur == '' and r['pdf_ct'] == dom; new = dom
            L[i] = CT + new; n_ct += 1
            log.append({'ref': f"pdf:p{r['page']}:{var} CT", 'action': 'REPLACED', 'kb_file': f'knowledge_base/domains/{dom}/spec.md',
                        'kb_line_after': i + 1, 'pdf_page': r['page'], 'note': ('U5: ' if r['class'] == '1' else 'U6: ') + f"'{cur}' -> '{new}'"})
        if dom == 'SR' and var == 'SRDY' and line == SRDY_OLD:
            L[i] = SRDY_NEW
            log.append({'ref': 'pdf:p377:SRDY CDISC Notes', 'action': 'REPLACED', 'kb_file': 'knowledge_base/domains/SR/spec.md',
                        'kb_line_after': i + 1, 'pdf_page': 377, 'note': 'SR T-5 (PDF_TYPO): "sponsor- defined" -> "sponsor-defined"'})
    assert n_ct == len(plan.get(dom, {})), (dom, n_ct)
    if has_code:
        assert NOTE not in L
        j = next(k for k in range(sep, len(L)) if L[k] == '## Cross References')
        assert L[j - 1] == ''
        L[j:j] = [NOTE, '']
        log.append({'ref': 'U5 KB note', 'action': 'INSERTED', 'kb_file': f'knowledge_base/domains/{dom}/spec.md', 'kb_line_after': j + 1,
                    'pdf_page': None, 'note': 'KB note line before Cross References (after spec footnotes)'})
    open(path, 'w').write('\n'.join(L))
if WJ:
    with open(WJ, 'w') as f:
        for x in log: f.write(json.dumps(x, ensure_ascii=False) + '\n')
from collections import Counter
print(Counter(x['note'][:3] if x['action'] == 'REPLACED' else 'NOTE' for x in log))
