#!/usr/bin/env python3
import json
from datetime import datetime, timezone

ts = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
batch_id = 'batch_111'
prompt_version = 'P4a_forward_matcher_v1.0'
subagent_type = 'oh-my-claudecode:executor'

matched_by = {
    'subagent_type': subagent_type,
    'batch_id': batch_id,
    'prompt_version': prompt_version,
    'ts': ts
}

def row(pdf_atom_id, verdict, md_atom_ids, score,
        discrepancy=None, exclusion_reason=None, category=None, approved_by=None):
    return {
        'pdf_atom_id': pdf_atom_id,
        'md_atom_ids': md_atom_ids,
        'verdict': verdict,
        'similarity_score': score,
        'discrepancy': discrepancy,
        'exclusion_reason': exclusion_reason,
        'category': category,
        'approved_by': approved_by,
        'matched_by': matched_by
    }

IE_reason = 'Appendix A contributor listing: team member name/affiliation not SDTM content knowledge'
IE_cat = 'authorship-metadata'
IE_approved = 'pre-approved-category'

records = [
    # --- Atoms 1-22: Appendix A SDS Team contributor rows ---
    row('ig34_p0445_a019','INTENTIONAL_EXCLUDE',[],None,None,IE_reason,IE_cat,IE_approved),
    row('ig34_p0445_a020','INTENTIONAL_EXCLUDE',[],None,None,IE_reason,IE_cat,IE_approved),
    row('ig34_p0445_a021','INTENTIONAL_EXCLUDE',[],None,None,IE_reason,IE_cat,IE_approved),
    row('ig34_p0445_a022','INTENTIONAL_EXCLUDE',[],None,None,IE_reason,IE_cat,IE_approved),
    row('ig34_p0445_a023','INTENTIONAL_EXCLUDE',[],None,None,IE_reason,IE_cat,IE_approved),
    row('ig34_p0445_a024','INTENTIONAL_EXCLUDE',[],None,None,IE_reason,IE_cat,IE_approved),
    row('ig34_p0445_a025','INTENTIONAL_EXCLUDE',[],None,None,IE_reason,IE_cat,IE_approved),
    row('ig34_p0445_a026','INTENTIONAL_EXCLUDE',[],None,None,IE_reason,IE_cat,IE_approved),
    row('ig34_p0445_a027','INTENTIONAL_EXCLUDE',[],None,None,IE_reason,IE_cat,IE_approved),
    row('ig34_p0445_a028','INTENTIONAL_EXCLUDE',[],None,None,IE_reason,IE_cat,IE_approved),
    row('ig34_p0445_a029','INTENTIONAL_EXCLUDE',[],None,None,IE_reason,IE_cat,IE_approved),
    row('ig34_p0445_a030','INTENTIONAL_EXCLUDE',[],None,None,IE_reason,IE_cat,IE_approved),
    row('ig34_p0445_a031','INTENTIONAL_EXCLUDE',[],None,None,IE_reason,IE_cat,IE_approved),
    row('ig34_p0445_a032','INTENTIONAL_EXCLUDE',[],None,None,IE_reason,IE_cat,IE_approved),
    row('ig34_p0445_a033','INTENTIONAL_EXCLUDE',[],None,None,IE_reason,IE_cat,IE_approved),
    row('ig34_p0445_a034','INTENTIONAL_EXCLUDE',[],None,None,IE_reason,IE_cat,IE_approved),
    row('ig34_p0445_a035','INTENTIONAL_EXCLUDE',[],None,None,IE_reason,IE_cat,IE_approved),
    row('ig34_p0445_a036','INTENTIONAL_EXCLUDE',[],None,None,IE_reason,IE_cat,IE_approved),
    row('ig34_p0445_a037','INTENTIONAL_EXCLUDE',[],None,None,IE_reason,IE_cat,IE_approved),
    row('ig34_p0445_a038','INTENTIONAL_EXCLUDE',[],None,None,IE_reason,IE_cat,IE_approved),
    row('ig34_p0445_a039','INTENTIONAL_EXCLUDE',[],None,None,IE_reason,IE_cat,IE_approved),
    row('ig34_p0445_a040','INTENTIONAL_EXCLUDE',[],None,None,IE_reason,IE_cat,IE_approved),

    # --- Atom 23: Appendix B section heading ---
    row('ig34_p0446_a001','EXACT',['md_ch10_a001'],0.9),

    # --- Atoms 24-25: Appendix B intro prose ---
    row('ig34_p0446_a002','EXACT',['md_ch10_a002'],0.9),
    row('ig34_p0446_a003','EXACT',['md_ch10_a003'],0.9),

    # --- Atom 26: generic table header | Term | Definition | ---
    # MD has different column structure (QNAM/QLABEL/Definition), score 0.6 -> PARTIAL
    row('ig34_p0446_a004','PARTIAL',['md_ch10_a004'],0.6,
        'PDF has 2-column header Term/Definition; KB version has different column structure'),

    # --- Atoms 27-56: Glossary entries EXACT ---
    row('ig34_p0446_a005','EXACT',['md_ch10_a005'],0.9),
    row('ig34_p0446_a006','EXACT',['md_ch10_a006'],0.9),
    row('ig34_p0446_a007','EXACT',['md_ch10_a007'],0.9),
    row('ig34_p0446_a008','EXACT',['md_ch10_a008'],0.9),
    row('ig34_p0446_a009','EXACT',['md_ch10_a009'],0.9),
    row('ig34_p0446_a010','EXACT',['md_ch10_a010'],0.9),
    row('ig34_p0446_a011','EXACT',['md_ch10_a011'],0.9),
    row('ig34_p0446_a012','EXACT',['md_ch10_a012'],0.9),
    row('ig34_p0446_a013','EXACT',['md_ch10_a013'],0.9),
    row('ig34_p0446_a014','EXACT',['md_ch10_a014'],0.9),
    row('ig34_p0446_a015','EXACT',['md_ch10_a015'],0.9),
    row('ig34_p0446_a016','EXACT',['md_ch10_a016'],0.9),
    row('ig34_p0446_a017','EXACT',['md_ch10_a017'],0.9),
    row('ig34_p0446_a018','EXACT',['md_ch10_a018'],0.9),
    row('ig34_p0446_a019','EXACT',['md_ch10_a019'],0.9),
    row('ig34_p0446_a020','EXACT',['md_ch10_a020'],0.9),
    row('ig34_p0446_a021','EXACT',['md_ch10_a021'],0.9),
    row('ig34_p0446_a022','EXACT',['md_ch10_a022'],0.9),
    row('ig34_p0446_a023','EXACT',['md_ch10_a023'],0.9),
    row('ig34_p0446_a024','EXACT',['md_ch10_a024'],0.9),
    row('ig34_p0446_a025','EXACT',['md_ch10_a025'],0.9),
    row('ig34_p0446_a026','EXACT',['md_ch10_a026'],0.9),
    row('ig34_p0446_a027','EXACT',['md_ch10_a027'],0.9),
    row('ig34_p0446_a028','EXACT',['md_ch10_a028'],0.9),
    row('ig34_p0446_a029','EXACT',['md_ch10_a029'],0.9),
    row('ig34_p0446_a030','EXACT',['md_ch10_a030'],0.9),
    row('ig34_p0446_a031','EXACT',['md_ch10_a031'],0.9),
    row('ig34_p0446_a032','EXACT',['md_ch10_a032'],0.9),
    row('ig34_p0446_a033','EXACT',['md_ch10_a033'],0.9),
    row('ig34_p0446_a034','EXACT',['md_ch10_a034'],0.9),

    # --- Atom 57: SDTMIG row, score 0.8294, same section, slightly truncated ---
    row('ig34_p0446_a035','EQUIVALENT',['md_ch10_a035'],0.8294,
        'MD slightly truncates full title wording but conveys identical meaning'),

    row('ig34_p0446_a036','EXACT',['md_ch10_a036'],0.9),

    # --- Atoms 59-66: remaining glossary entries ---
    row('ig34_p0447_a001','EXACT',['md_ch10_a037'],0.9),
    row('ig34_p0447_a002','EXACT',['md_ch10_a038'],0.9),
    row('ig34_p0447_a003','EXACT',['md_ch10_a039'],0.9),
    row('ig34_p0447_a004','EXACT',['md_ch10_a040'],0.9),
    row('ig34_p0447_a005','EXACT',['md_ch10_a041'],0.9),
    row('ig34_p0447_a006','EXACT',['md_ch10_a042'],0.9),
    row('ig34_p0447_a007','EXACT',['md_ch10_a043'],0.9),
    row('ig34_p0447_a008','EXACT',['md_ch10_a044'],0.9),

    # --- Atom 67: Appendix C heading ---
    row('ig34_p0447_a009','EXACT',['md_ch10_a045'],0.9),

    # --- Atom 68: Appendix C intro prose ---
    row('ig34_p0447_a010','EXACT',['md_ch10_a046'],0.9),

    # --- Atom 69: 3-month development period condensed ---
    row('ig34_p0447_a011','EQUIVALENT',['md_ch10_a047'],0.5005,
        'MD condenses detail about development period and quarterly process into shorter bullet'),

    # --- Atom 70: URL prose condensed ---
    row('ig34_p0447_a012','EQUIVALENT',['md_ch10_a048'],0.5638,
        'MD condenses long URL prose into shorter bullet retaining key URLs'),

    # --- Atom 71: questionnaire terminology note merged ---
    row('ig34_p0447_a013','EQUIVALENT',['md_ch10_a049'],0.5918,
        'MD merges note about questionnaire terminology into combined bullet with subsequent sentence'),

    # --- Atom 72: "merged into single publication" — no KB match (top score 0.4771, wrong domain) ---
    row('ig34_p0447_a014','MISSING',[],None),

    # --- Atom 73: earlier versions appendices condensed ---
    row('ig34_p0447_a015','EQUIVALENT',['md_ch10_a050'],0.518,
        'MD merges with SDTMIG 3.2 simplification sentence into single bullet'),

    # --- Atom 74: "Starting with SDTMIG 3.2, Appendix C was simplified" — no standalone match ---
    row('ig34_p0447_a016','MISSING',[],None),

    # --- Atom 75: "Appendix C1 will be considered for expansion" — not found in KB ---
    row('ig34_p0447_a017','MISSING',[],None),

    # --- Atom 76: Appendix C1 heading ---
    row('ig34_p0448_a001','EXACT',['md_ch10_a051'],0.9),

    # --- Atom 77: SUPP-- intro prose, EQUIVALENT ---
    row('ig34_p0448_a002','EQUIVALENT',['md_ch10_a052'],0.6761,
        'MD shortens intro sentence but retains meaning about initial standard name codes for SUPP-- datasets'),

    # --- Atom 78: QNAM/QLABEL table header ---
    row('ig34_p0448_a003','EXACT',['md_ch10_a053'],0.9),

    # --- Atoms 79-80: SUPP-- table rows ---
    row('ig34_p0448_a004','EXACT',['md_ch10_a054'],0.9),
    row('ig34_p0448_a005','EXACT',['md_ch10_a055'],0.9),

    # --- Atom 81: --REAS row, score 0.8909, minor condensation ---
    row('ig34_p0448_a006','EQUIVALENT',['md_ch10_a056'],0.8909,
        'MD omits "for an intervention" qualifier and slightly shortens domain applicability clause; same meaning'),

    # --- Atom 82: Appendix D heading ---
    row('ig34_p0448_a007','EXACT',['md_ch10_a057'],0.9),

    # --- Atom 83: fragment intro prose, EQUIVALENT ---
    row('ig34_p0448_a008','EQUIVALENT',['md_ch10_a058'],0.6833,
        'MD slightly truncates sentence but same SUPP-- and --TESTCD fragment guidance content'),

    # --- Atom 84: "more than 1 fragment for a given keyword" — no §10.D match ---
    row('ig34_p0448_a009','MISSING',[],None),

    # --- Atom 85: 8-character limit --TESTCD/QNAM sentence — no §10.D match ---
    row('ig34_p0448_a010','MISSING',[],None),

    # --- Atom 86: general rule for fragments, EQUIVALENT ---
    row('ig34_p0448_a011','EQUIVALENT',['md_ch10_a059'],0.5683,
        'MD condenses rule about longest fragment within 8-char limit into shorter bullet'),

    # --- Atom 87: drop characters rule, EQUIVALENT ---
    row('ig34_p0448_a012','EQUIVALENT',['md_ch10_a060'],0.5986,
        'MD condenses drop-characters rule into shorter bullet; same guidance'),

    # --- Atom 88: same fragment multiple meanings — no good match ---
    row('ig34_p0448_a013','MISSING',[],None),

    # --- Atom 89: | Keyword(s) | Fragment | header ---
    row('ig34_p0448_a014','EXACT',['md_ch10_a061'],0.9),

    # --- Atoms 90-100: fragment table rows ---
    # MD stores 2 fragments per row (merged table format); PDF has 1 per row. Same content -> EQUIVALENT
    row('ig34_p0448_a015','EQUIVALENT',['md_ch10_a062'],0.55,
        'MD stores fragment rows in merged 2-per-row table format; ACTION/ACN content matches'),
    row('ig34_p0448_a016','EQUIVALENT',['md_ch10_a063'],0.5286,
        'MD stores fragment rows in merged 2-per-row table format; ADJUSTMENT/ADJ content matches'),
    row('ig34_p0448_a017','EQUIVALENT',['md_ch10_a064'],0.6882,
        'MD stores fragment rows in merged 2-per-row table format; ANALYSIS DATASET/AD content matches'),
    row('ig34_p0448_a018','EQUIVALENT',['md_ch10_a065'],0.4385,
        'MD stores fragment rows in merged 2-per-row table format; ASSAY/AS content matches'),
    row('ig34_p0448_a019','EQUIVALENT',['md_ch10_a066'],0.5118,
        'MD stores fragment rows in merged 2-per-row table format; BASELINE/BL content matches'),
    row('ig34_p0448_a020','EQUIVALENT',['md_ch10_a067'],0.54,
        'MD stores fragment rows in merged 2-per-row table format; BIRTH/BRTH content matches'),
    row('ig34_p0448_a021','EQUIVALENT',['md_ch10_a068'],0.4714,
        'MD stores fragment rows in merged 2-per-row table format; BODY/BOD content matches'),
    row('ig34_p0448_a022','EQUIVALENT',['md_ch10_a069'],0.54,
        'MD stores fragment rows in merged 2-per-row table format; CANCER/CAN content matches'),
    row('ig34_p0448_a023','EQUIVALENT',['md_ch10_a070'],0.75,
        'MD stores fragment rows in merged 2-per-row table format; CATEGORY/CAT content matches'),
    row('ig34_p0448_a024','EQUIVALENT',['md_ch10_a071'],0.72,
        'MD stores fragment rows in merged 2-per-row table format; CHARACTER/C content matches'),
    row('ig34_p0448_a025','EQUIVALENT',['md_ch10_a072'],0.5571,
        'MD stores fragment rows in merged 2-per-row table format; CLASS/CLAS content matches'),
]

# Verify count
assert len(records) == 100, f'Expected 100 records, got {len(records)}'

from collections import Counter
counts = Counter(r['verdict'] for r in records)
print('Verdict counts:', dict(counts))
print('Total:', len(records))

# Write ledger
ledger_path = '/Users/bojiangzhang/MyProject/sdtm-pedia/branches/06_deep_verification/evidence/p4a_batches/batch_111_ledger.jsonl'
with open(ledger_path, 'w', encoding='utf-8') as f:
    for r in records:
        f.write(json.dumps(r, ensure_ascii=False) + '\n')
print(f'Written: {ledger_path}')

# Build trace entry
trace_entry = {
    'ts': ts,
    'phase': 'P4a',
    'slot': 'batch_quality_sample',
    'batch_id': batch_id,
    'subagent_type': subagent_type,
    'prompt_version': prompt_version,
    'stats': {
        'total': 100,
        'EXACT': counts.get('EXACT', 0),
        'EQUIVALENT': counts.get('EQUIVALENT', 0),
        'PARTIAL': counts.get('PARTIAL', 0),
        'MISPLACED': counts.get('MISPLACED', 0),
        'MISSING': counts.get('MISSING', 0),
        'ERROR': counts.get('ERROR', 0),
        'INTENTIONAL_EXCLUDE': counts.get('INTENTIONAL_EXCLUDE', 0),
    },
    'samples': [
        {'pdf_atom_id': records[0]['pdf_atom_id'],  'verdict': records[0]['verdict'],  'top1_score': None},
        {'pdf_atom_id': records[22]['pdf_atom_id'], 'verdict': records[22]['verdict'], 'top1_score': 0.9},
        {'pdf_atom_id': records[55]['pdf_atom_id'], 'verdict': records[55]['verdict'], 'top1_score': 0.8294},
        {'pdf_atom_id': records[71]['pdf_atom_id'], 'verdict': records[71]['verdict'], 'top1_score': None},
        {'pdf_atom_id': records[88]['pdf_atom_id'], 'verdict': records[88]['verdict'], 'top1_score': 0.9},
    ]
}

trace_path = '/Users/bojiangzhang/MyProject/sdtm-pedia/branches/06_deep_verification/trace.jsonl'
with open(trace_path, 'a', encoding='utf-8') as f:
    f.write(json.dumps(trace_entry, ensure_ascii=False) + '\n')
print(f'Appended to: {trace_path}')
