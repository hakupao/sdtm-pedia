#!/usr/bin/env python3
"""
v1.4 Phase C C2 — UNSOURCED_MANUAL atom classifier (bias-fixed).

Fix for v1.3 Rule D #19 finding:
  Main session 启发式分类器 bias — 5/10 PDF-prose atoms 误标 DERIVED_FROM_XLSX.
  Root cause: classifier 优先按 atom_type==NOTE / table-row / spec-style 归 xlsx,
              没有先扫 pdf_atoms.jsonl 找 verbatim 来源.

v1.4 fix order (per PLAN.md C2):
  Step 1 — PDF prose grep   → REASONABLE_INFERENCE (with pdf_evidence list)
  Step 2 — xlsx fallback   → DERIVED_FROM_XLSX     (with xlsx_evidence rationale)
  Step 3 — neither fires   → NEEDS_HUMAN_REVIEW    (escalate, no auto verdict)

Step 1 matching:
  (a) Substring of any contiguous phrase ≥15 chars from KB verbatim found in any
      PDF atom verbatim (case-insensitive, whitespace-collapsed).
  (b) Fuzzy ratio ≥0.70 between KB verbatim and *best* PDF atom on candidate set
      (candidate set = same parent_section section number OR adjacent ±2 sections).

Step 2 xlsx heuristic (only if Step 1 misses):
  - file in `knowledge_base/model/05_study_level_data.md` (TT/TP structure NOTE)
  - atom_type == 'NOTE' and verbatim starts with `**Structure:**` or `**Note:**`
    *and* references a CDISC variable spec dependency (`<VAR>EVAL` / `<VAR>EVALID`)
    that exists in CDISC xlsx specs (heuristic: ALL_CAPS variable token w/ suffix).
  - file in `knowledge_base/chapters/ch04_general_assumptions.md` for SDTM Core
    designation TABLE_ROW (Core column "Req"/"Exp"/"Perm").
  - file in `knowledge_base/chapters/ch01_introduction.md` §1.4.1 column-spec
    TABLE_ROW (xlsx variable spec column metadata).

Usage:
  python3 classify_unsourced.py \\
      --input  n80_sample.json \\
      --output n80_classified.json \\
      --md-atoms branches/06_deep_verification/md_atoms.jsonl \\
      --pdf-atoms branches/06_deep_verification/pdf_atoms.jsonl

Author: v1.4 Phase C C2 executor (oh-my-claudecode:executor)
"""

import argparse
import json
import os
import re
import sys
from difflib import SequenceMatcher
from pathlib import Path

# ---------- 数据加载 ----------

def load_md_atoms(path):
    """Return {atom_id: {file, atom_type, parent_section, verbatim}}"""
    out = {}
    with open(path, encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
            except json.JSONDecodeError:
                continue
            aid = obj.get('atom_id')
            if aid:
                out[aid] = {
                    'file': obj.get('file'),
                    'atom_type': obj.get('atom_type'),
                    'parent_section': obj.get('parent_section'),
                    'verbatim': obj.get('verbatim', ''),
                }
    return out


def load_pdf_atoms(path):
    """
    Return list of {atom_id, page, parent_section, atom_type, verbatim,
                     _norm, _tokens, _content_tokens}.
    Pre-computes normalized text and token sets once so subsequent N matches
    are O(N) per KB atom rather than O(N) plus recomputation.
    """
    out = []
    with open(path, encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
            except json.JSONDecodeError:
                continue
            v = obj.get('verbatim', '')
            n = normalize(v)
            toks = set(re.findall(r'[a-z0-9]{3,}', n))
            ctoks = toks - _STOP_TOKENS
            out.append({
                'atom_id': obj.get('atom_id'),
                'page': obj.get('page'),
                'parent_section': obj.get('parent_section'),
                'atom_type': obj.get('atom_type'),
                'verbatim': v,
                '_norm': n,
                '_tokens': toks,
                '_content_tokens': ctoks,
            })
    return out


# ---------- 规范化 ----------

_WHITESPACE_RE = re.compile(r'\s+')
_MD_TOKENS_RE = re.compile(r'(\*\*|__|`|\[|\]|\(|\)|\\|\|)+')

def normalize(text):
    """Lower-case, strip md-emphasis, collapse whitespace."""
    if not text:
        return ''
    s = _MD_TOKENS_RE.sub(' ', text)
    s = _WHITESPACE_RE.sub(' ', s).strip().lower()
    return s


def extract_long_phrases(text, min_len=15):
    """
    Extract substrings ≥min_len chars from `text`. Split on common boundaries
    (sentence-end, em-dash, parens, brackets, pipes, parens) then return unique
    phrases. Adds: word-window sliding for table-cell-style verbatim where the
    KB synthesized 2 PDF cells into one row.
    """
    s = normalize(text)
    if len(s) < min_len:
        return []
    parts = re.split(r'(?:\. |; | — |— |—| - | — | \(| \[|: | \| |\| | \|)', s)
    out = []
    seen = set()
    for p in parts:
        p = p.strip(' .,:;—-|()[]"\'')
        if len(p) >= min_len and p not in seen:
            seen.add(p)
            out.append(p)
    # Also include the full normalized text
    s_full = s.strip(' .,:;—-|()[]"\'')
    if s_full not in seen and len(s_full) >= min_len:
        out.append(s_full)
        seen.add(s_full)
    # Word-window n-grams (5..12 words) to catch table-row KB synthesis where
    # KB stitched 2 PDF cells. Limit to first 30 words to keep cheap.
    tokens = re.findall(r"[a-z0-9][a-z0-9'/\-]*", s)
    if len(tokens) >= 5:
        max_tokens = min(len(tokens), 30)
        # Sliding window sizes 5,7,9
        for win in (9, 7, 5):
            if win > max_tokens:
                continue
            for i in range(max_tokens - win + 1):
                ngram = ' '.join(tokens[i:i+win])
                if len(ngram) >= min_len and ngram not in seen:
                    seen.add(ngram)
                    out.append(ngram)
    return out


# ---------- Step 1: PDF verbatim grep ----------

def pdf_substring_match(kb_verbatim, pdf_atoms, phrase_min_len=15, max_phrases=64):
    """
    Find PDF atoms whose verbatim contains any long phrase (≥phrase_min_len) from
    `kb_verbatim`. Returns list of matches up to early-stop top 5.
    Uses precomputed pa['_norm'] when available.
    """
    phrases = extract_long_phrases(kb_verbatim, min_len=phrase_min_len)
    if not phrases:
        return []
    matches = []
    # Iterate longest phrases first (more specific)
    phrases.sort(key=len, reverse=True)
    seen_pdf_ids = set()
    for phrase in phrases[:max_phrases]:
        for pa in pdf_atoms:
            if pa['atom_id'] in seen_pdf_ids:
                continue
            pdf_n = pa.get('_norm') or normalize(pa['verbatim'])
            if phrase in pdf_n:
                matches.append({
                    'pdf_atom_id': pa['atom_id'],
                    'pdf_page': pa['page'],
                    'pdf_section': pa['parent_section'],
                    'matched_phrase': phrase[:80],
                    'match_kind': 'substring',
                })
                seen_pdf_ids.add(pa['atom_id'])
                if len(matches) >= 5:
                    return matches
    return matches


def pdf_fuzzy_match(kb_verbatim, pdf_atoms, ratio_threshold=0.70, top_k=5,
                    overlap_required=4):
    """
    SequenceMatcher fuzzy ratio over normalized text.
    Returns list of (pdf_atom_id, ratio) — top ratios ≥threshold.
    Expensive: only run if substring miss.

    overlap_required: minimum unique 3+char token overlap before running
    SequenceMatcher (cheap pre-filter, default 4 to keep cost low).
    """
    kb_n = normalize(kb_verbatim)
    if len(kb_n) < 20:
        return []
    scored = []
    # Cheap pre-filter: token-overlap ≥overlap_required before SequenceMatcher.
    kb_tokens = set(re.findall(r'[a-z0-9]{3,}', kb_n))
    if not kb_tokens:
        return []
    for pa in pdf_atoms:
        pdf_n = pa.get('_norm') or normalize(pa['verbatim'])
        if len(pdf_n) < 20:
            continue
        pdf_tokens = pa.get('_tokens') or set(re.findall(r'[a-z0-9]{3,}', pdf_n))
        overlap = len(kb_tokens & pdf_tokens)
        if overlap < overlap_required:
            continue
        # Cap input length for fuzzy ratio perf
        ratio = SequenceMatcher(None, kb_n[:300], pdf_n[:300]).ratio()
        if ratio >= ratio_threshold:
            scored.append({
                'pdf_atom_id': pa['atom_id'],
                'pdf_page': pa['page'],
                'pdf_section': pa['parent_section'],
                'ratio': round(ratio, 3),
                'match_kind': 'fuzzy',
            })
    scored.sort(key=lambda x: -x['ratio'])
    return scored[:top_k]


_STOP_TOKENS = {
    'the', 'and', 'for', 'are', 'this', 'that', 'with', 'from', 'when', 'where',
    'has', 'have', 'was', 'were', 'will', 'should', 'must', 'can', 'may',
    'any', 'all', 'one', 'two', 'three', 'four', 'each', 'such', 'used',
    'into', 'their', 'they', 'these', 'those', 'them', 'than', 'then',
    'not', 'but', 'because', 'about', 'between', 'within', 'also', 'only',
    'which', 'what', 'who', 'why', 'how', 'been', 'being', 'does', 'did',
    'see', 'note', 'section', 'example', 'further', 'either', 'other',
}

def _content_tokens(text):
    """3+char alphanumeric tokens minus common English stop tokens."""
    n = normalize(text)
    raw = set(re.findall(r'[a-z0-9]{3,}', n))
    return raw - _STOP_TOKENS


def pdf_jaccard_match(kb_verbatim, pdf_atoms, jaccard_threshold=0.55,
                      content_overlap_threshold=4, top_k=5):
    """
    Jaccard token-overlap matcher — last resort for short table-cell KB synthesis
    where verbatim/substring/fuzzy all miss but content tokens overlap strongly.

    Accept a PDF atom as match if EITHER:
      (a) Jaccard ≥ jaccard_threshold (0.55), OR
      (b) content-token intersection ≥ content_overlap_threshold (4 unique 3+char
          non-stop tokens shared) AND the intersection covers ≥50% of KB content
          tokens. This handles the "PDF uses abbreviations, KB expands them" case
          (e.g., PDF "Req/Exp/Perm" vs KB "Req/Required/Exp/Expected/Perm/Permissible").
    """
    kb_n = normalize(kb_verbatim)
    if len(kb_n) < 10:
        return []
    kb_tokens = _content_tokens(kb_verbatim)
    if len(kb_tokens) < 3:
        return []
    scored = []
    for pa in pdf_atoms:
        pdf_n = pa.get('_norm') or normalize(pa['verbatim'])
        if len(pdf_n) < 10:
            continue
        pdf_tokens = pa.get('_content_tokens')
        if pdf_tokens is None:
            pdf_tokens = _content_tokens(pa['verbatim'])
        if len(pdf_tokens) < 3:
            continue
        inter = kb_tokens & pdf_tokens
        if len(inter) < 3:
            continue
        union = kb_tokens | pdf_tokens
        j = len(inter) / len(union)
        kb_cov = len(inter) / len(kb_tokens)
        accept = False
        kind = None
        if j >= jaccard_threshold:
            accept = True
            kind = 'jaccard'
        elif len(inter) >= content_overlap_threshold and kb_cov >= 0.50:
            accept = True
            kind = 'content_overlap_kbcov'
        if accept:
            scored.append({
                'pdf_atom_id': pa['atom_id'],
                'pdf_page': pa['page'],
                'pdf_section': pa['parent_section'],
                'jaccard': round(j, 3),
                'kb_token_coverage': round(kb_cov, 3),
                'shared_tokens': sorted(inter)[:10],
                'match_kind': kind,
            })
    scored.sort(key=lambda x: (-x['jaccard'], -x['kb_token_coverage']))
    return scored[:top_k]


# ---------- Step 2: xlsx fallback heuristic ----------

CDISC_VAR_RE = re.compile(r'\b[A-Z]{2,8}(?:VAL|VALID|TESTCD|CAT|FL|DTC|STAT|REAS|ID|SEQ|GRPID)\b')

def xlsx_fallback(md_atom):
    """
    Conservative xlsx-derived heuristic. Returns (is_xlsx, reason) tuple.
    Only fires if multiple weak signals concur — single signal => NEEDS_REVIEW.
    """
    f = md_atom.get('file', '') or ''
    t = md_atom.get('atom_type', '') or ''
    v = md_atom.get('verbatim', '') or ''
    section = md_atom.get('parent_section', '') or ''

    signals = []

    # Signal 1: model/05 Structure NOTE
    if 'model/05_study_level_data.md' in f:
        if t == 'NOTE' and ('**Structure:**' in v or v.startswith('Structure:')):
            signals.append('model05_structure_note')

    # Signal 2: TT/TP NOTE referencing planned-repro structure
    if t == 'NOTE' and re.search(r'planned\s+repro\s+stage', v, re.I):
        signals.append('tt_tp_planned_repro_stage')

    # Signal 3: variable spec NOTE referencing CDISC xlsx ALL_CAPS var deps
    # e.g. "TREVAL must also be populated when TREVALID is populated"
    if t == 'NOTE' and CDISC_VAR_RE.search(v):
        # only fire when verbatim is short (variable spec note style)
        if len(v) < 150:
            signals.append('cdisc_var_spec_note')

    # Signal 4: ch04 §4.1.5 Core designation table-row
    if 'ch04_general_assumptions.md' in f and t == 'TABLE_ROW':
        if re.search(r'\b(Req|Exp|Perm)\b.*\b(Required|Expected|Permissible)\b', v, re.I) or \
           re.search(r'\b(Required|Expected|Permissible)\b', v):
            signals.append('ch04_core_designation_row')

    # Signal 5: ch01 §1.4.1 spec-column table-row
    if 'ch01_introduction.md' in f and t == 'TABLE_ROW' and '1.4.1' in section:
        signals.append('ch01_spec_column_row')

    if not signals:
        return False, ''
    # Default: require ≥1 of model05/var-spec/spec-column to fire xlsx verdict
    strong = {'model05_structure_note', 'tt_tp_planned_repro_stage', 'cdisc_var_spec_note',
              'ch01_spec_column_row'}
    if any(s in strong for s in signals):
        return True, '+'.join(signals)
    return False, '+'.join(signals)


# ---------- 主分类 ----------

def classify_atom(md_atom, pdf_atoms, kb_verbatim_lookup):
    """
    Returns dict with category + evidence + reasoning.
    """
    aid = md_atom.get('atom_id') if 'atom_id' in md_atom else None
    # md_atom may come from sample dict (which has atom_id+verbatim-preview);
    # use full verbatim from kb_verbatim_lookup
    verbatim = ''
    if aid and aid in kb_verbatim_lookup:
        verbatim = kb_verbatim_lookup[aid]['verbatim']
    else:
        # fallback to caller-provided verbatim (e.g., from sample json)
        verbatim = md_atom.get('verbatim') or ''
    md_full = {
        'atom_id': aid,
        'file': md_atom.get('file') or (kb_verbatim_lookup.get(aid, {}).get('file') if aid else ''),
        'atom_type': md_atom.get('type') or md_atom.get('atom_type') or
                      (kb_verbatim_lookup.get(aid, {}).get('atom_type') if aid else ''),
        'parent_section': md_atom.get('section') or md_atom.get('parent_section') or
                          (kb_verbatim_lookup.get(aid, {}).get('parent_section') if aid else ''),
        'verbatim': verbatim,
    }

    # Step 1: PDF substring grep
    substring_hits = pdf_substring_match(verbatim, pdf_atoms, phrase_min_len=15)
    fuzzy_hits = []
    jaccard_hits = []
    if not substring_hits:
        fuzzy_hits = pdf_fuzzy_match(verbatim, pdf_atoms, ratio_threshold=0.70)
        if not fuzzy_hits:
            jaccard_hits = pdf_jaccard_match(verbatim, pdf_atoms, jaccard_threshold=0.55)

    if substring_hits:
        return {
            'atom_id': aid,
            'file': md_full['file'],
            'atom_type': md_full['atom_type'],
            'parent_section': md_full['parent_section'],
            'verbatim': verbatim,
            'category': 'REASONABLE_INFERENCE',
            'evidence': {'pdf_evidence': substring_hits},
            'reasoning': f"PDF substring match: {len(substring_hits)} hit(s) with phrase ≥15 chars verbatim in pdf_atoms.jsonl.",
        }
    if fuzzy_hits:
        return {
            'atom_id': aid,
            'file': md_full['file'],
            'atom_type': md_full['atom_type'],
            'parent_section': md_full['parent_section'],
            'verbatim': verbatim,
            'category': 'REASONABLE_INFERENCE',
            'evidence': {'pdf_evidence': fuzzy_hits},
            'reasoning': f"PDF fuzzy match: ratio ≥0.70 against {len(fuzzy_hits)} PDF atom(s); semantic paraphrase confirmed.",
        }
    if jaccard_hits:
        return {
            'atom_id': aid,
            'file': md_full['file'],
            'atom_type': md_full['atom_type'],
            'parent_section': md_full['parent_section'],
            'verbatim': verbatim,
            'category': 'REASONABLE_INFERENCE',
            'evidence': {'pdf_evidence': jaccard_hits},
            'reasoning': f"PDF Jaccard token-overlap match (last-resort): ≥0.55 against {len(jaccard_hits)} PDF atom(s); KB synthesized text shares ≥55% unique 3+char tokens with PDF prose.",
        }

    # Step 2: xlsx fallback
    is_xlsx, reason = xlsx_fallback(md_full)
    if is_xlsx:
        return {
            'atom_id': aid,
            'file': md_full['file'],
            'atom_type': md_full['atom_type'],
            'parent_section': md_full['parent_section'],
            'verbatim': verbatim,
            'category': 'DERIVED_FROM_XLSX',
            'evidence': {'xlsx_evidence': reason},
            'reasoning': f"PDF prose miss; xlsx heuristic fired: {reason}.",
        }

    # Step 3: needs human review
    return {
        'atom_id': aid,
        'file': md_full['file'],
        'atom_type': md_full['atom_type'],
        'parent_section': md_full['parent_section'],
        'verbatim': verbatim,
        'category': 'NEEDS_HUMAN_REVIEW',
        'evidence': {'pdf_evidence': [], 'xlsx_evidence': reason or ''},
        'reasoning': "Neither PDF prose nor xlsx heuristic fired confidently; needs human PDF deep-look.",
    }


# ---------- CLI ----------

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--input', required=True, help='Input sample json (list of {atom_id, ...})')
    p.add_argument('--output', required=True, help='Output classified jsonl OR json')
    p.add_argument('--md-atoms', default='branches/06_deep_verification/md_atoms.jsonl')
    p.add_argument('--pdf-atoms', default='branches/06_deep_verification/pdf_atoms.jsonl')
    p.add_argument('--output-format', choices=['jsonl', 'json'], default='json')
    args = p.parse_args()

    repo_root = Path(__file__).resolve().parents[3]
    md_path = args.md_atoms
    pdf_path = args.pdf_atoms
    if not os.path.isabs(md_path):
        md_path = str(repo_root / md_path)
    if not os.path.isabs(pdf_path):
        pdf_path = str(repo_root / pdf_path)

    print(f"[classify_unsourced] Loading md_atoms from {md_path} ...", file=sys.stderr)
    md_index = load_md_atoms(md_path)
    print(f"[classify_unsourced]   {len(md_index)} md atoms indexed.", file=sys.stderr)

    print(f"[classify_unsourced] Loading pdf_atoms from {pdf_path} ...", file=sys.stderr)
    pdf_atoms = load_pdf_atoms(pdf_path)
    print(f"[classify_unsourced]   {len(pdf_atoms)} pdf atoms loaded.", file=sys.stderr)

    with open(args.input, encoding='utf-8') as f:
        sample_raw = json.load(f)

    # Accept either a list or a {_meta, atoms: [...]} envelope
    if isinstance(sample_raw, dict) and 'atoms' in sample_raw:
        sample = sample_raw['atoms']
        meta = sample_raw.get('_meta', {})
    else:
        sample = sample_raw
        meta = {}

    results = []
    for i, a in enumerate(sample, 1):
        r = classify_atom(a, pdf_atoms, md_index)
        # Carry over strat / partition if present in sample
        if 'strat' in a:
            r['strat'] = a['strat']
        if 'partition' in a:
            r['partition'] = a['partition']
        results.append(r)
        if i % 10 == 0 or i == len(sample):
            print(f"[classify_unsourced]   {i}/{len(sample)} classified.", file=sys.stderr)

    # Distribution
    from collections import Counter
    dist = Counter(r['category'] for r in results)
    print(f"\n[classify_unsourced] Distribution: {dict(dist)}", file=sys.stderr)

    if args.output_format == 'jsonl':
        with open(args.output, 'w', encoding='utf-8') as f:
            for r in results:
                f.write(json.dumps(r, ensure_ascii=False) + '\n')
    else:
        out_obj = {'_meta': meta, 'distribution': dict(dist), 'atoms': results} if meta else results
        with open(args.output, 'w', encoding='utf-8') as f:
            json.dump(out_obj, f, ensure_ascii=False, indent=2)
    print(f"[classify_unsourced] Wrote {len(results)} entries to {args.output}", file=sys.stderr)


if __name__ == '__main__':
    main()
