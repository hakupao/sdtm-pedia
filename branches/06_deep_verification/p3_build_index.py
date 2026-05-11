#!/usr/bin/env python3
"""P3 — Build candidate index: each pdf_atom → top-5 md_atom candidates.

Output: branches/06_deep_verification/p3_candidates.jsonl (12,487 lines)

Algorithm:
  1. Domain route: extract domain code from pdf parent_section → scope md pool
  2. Chapter route: §1-4 → chapter md files
  3. Atom type filter: FIGURE-only, HEADING-prefer
  4. Verbatim Jaccard (3-gram char tokens)
  5. Composite score = verbatim*0.6 + type_match*0.3 + domain_match*0.1
"""
import json
import re
import time
from pathlib import Path
from collections import defaultdict
from typing import Optional

BASE = Path(__file__).parent
PDF_ATOMS = BASE / "pdf_atoms.jsonl"
MD_ATOMS = BASE / "md_atoms.jsonl"
OUTPUT = BASE / "p3_candidates.jsonl"

W_VERBATIM = 0.6
W_TYPE = 0.3
W_DOMAIN = 0.1
MIN_SCORE = 0.05
MIN_SCORE_SHORT = 0.02  # for verbatim <= 5 tokens
TOP_K = 5
TOP_K_SHORT = 10


# Same-family type compatibility: cross-type allowed but down-weighted
_TYPE_COMPAT: dict[str, dict[str, float]] = {
    "SENTENCE":     {"SENTENCE": 1.0, "LIST_ITEM": 0.7, "NOTE": 0.7, "TABLE_ROW": 0.4,
                     "TABLE_HEADER": 0.3, "HEADING": 0.2, "CODE": 0.3, "FIGURE": 0.0},
    "LIST_ITEM":    {"LIST_ITEM": 1.0, "SENTENCE": 0.7, "TABLE_ROW": 0.5, "NOTE": 0.5,
                     "TABLE_HEADER": 0.4, "HEADING": 0.2, "CODE": 0.3, "FIGURE": 0.0},
    "TABLE_ROW":    {"TABLE_ROW": 1.0, "TABLE_HEADER": 0.8, "SENTENCE": 0.4,
                     "LIST_ITEM": 0.4, "NOTE": 0.3, "HEADING": 0.1, "CODE": 0.2, "FIGURE": 0.0},
    "TABLE_HEADER": {"TABLE_HEADER": 1.0, "TABLE_ROW": 0.8, "HEADING": 0.4, "SENTENCE": 0.3,
                     "LIST_ITEM": 0.3, "NOTE": 0.2, "CODE": 0.2, "FIGURE": 0.0},
    "HEADING":      {"HEADING": 1.0, "SENTENCE": 0.3, "NOTE": 0.2,
                     "LIST_ITEM": 0.2, "TABLE_ROW": 0.1, "TABLE_HEADER": 0.1, "FIGURE": 0.0},
    "FIGURE":       {"FIGURE": 1.0},
    "NOTE":         {"NOTE": 1.0, "SENTENCE": 0.7, "LIST_ITEM": 0.5, "TABLE_ROW": 0.3,
                     "HEADING": 0.2, "FIGURE": 0.0},
    "CODE":         {"CODE": 1.0, "SENTENCE": 0.3, "NOTE": 0.3, "FIGURE": 0.0},
}


def type_score(pdf_type: str, md_type: str) -> float:
    return _TYPE_COMPAT.get(pdf_type, {}).get(md_type, 0.3)


def tokenize(text: str) -> frozenset:
    """3-gram character tokens on lowercased, punct-stripped text."""
    t = re.sub(r"[^a-z0-9 ]", " ", text.lower())
    tokens: set[str] = set()
    for word in t.split():
        if len(word) >= 3:
            for i in range(len(word) - 2):
                tokens.add(word[i : i + 3])
    return frozenset(tokens)


def jaccard(a: frozenset, b: frozenset) -> float:
    if not a or not b:
        return 0.0
    union = len(a | b)
    return len(a & b) / union if union else 0.0


def extract_domain_code(parent_section: str, known_domains: set) -> Optional[str]:
    """Extract SDTM domain code from pdf parent_section string."""
    if not parent_section:
        return None

    # Pattern 1: explicit code in parentheses — (DM), (RELREC), (SUPPQUAL)
    for m in re.finditer(r"\(([A-Z]{2,8})\)", parent_section):
        if m.group(1) in known_domains:
            return m.group(1)

    # Pattern 2: code at start of bracket content — [DM –, [DM/
    m = re.search(r"\[([A-Z]{2,8})[\s\-/]", parent_section)
    if m and m.group(1) in known_domains:
        return m.group(1)

    # Pattern 3: §DOMAIN.N style — §DM.1
    m = re.search(r"§([A-Z]{2,8})\b", parent_section)
    if m and m.group(1) in known_domains:
        return m.group(1)

    # Pattern 4: standalone all-caps word that is a known domain code
    for word in re.findall(r"\b([A-Z]{2,8})\b", parent_section):
        if word in known_domains:
            return word

    return None


def get_chapter_key(parent_section: str) -> Optional[str]:
    """Map §1-4 / §8 / §10 to chapter key (e.g. 'ch01')."""
    m = re.match(r"§(\d+)", parent_section or "")
    if not m:
        return None
    n = int(m.group(1))
    mapping = {1: "ch01", 2: "ch02", 3: "ch03", 4: "ch04", 8: "ch08", 10: "ch10"}
    return mapping.get(n)


def load_jsonl(path: Path) -> list:
    with open(path) as f:
        return [json.loads(line) for line in f if line.strip()]


def main() -> None:
    t0 = time.time()

    print("Loading pdf_atoms.jsonl and md_atoms.jsonl …")
    pdf_atoms = load_jsonl(PDF_ATOMS)
    md_atoms = load_jsonl(MD_ATOMS)
    print(f"  pdf={len(pdf_atoms):,}  md={len(md_atoms):,}")

    # ── Build domain set from md file paths ───────────────────────────────
    known_domains: set[str] = set()
    for a in md_atoms:
        f = a.get("file", "")
        if "/domains/" in f:
            parts = f.split("/")
            idx = parts.index("domains")
            if idx + 1 < len(parts):
                known_domains.add(parts[idx + 1])
    print(f"  known domains: {len(known_domains)}")

    # ── Index md atoms by domain, chapter, type ───────────────────────────
    md_by_domain: dict[str, list] = defaultdict(list)
    md_by_chapter: dict[str, list] = defaultdict(list)
    md_by_type: dict[str, list] = defaultdict(list)  # for FIGURE/HEADING global

    for a in md_atoms:
        f = a.get("file", "")
        atype = a.get("atom_type", "")
        md_by_type[atype].append(a)

        if "/domains/" in f:
            parts = f.split("/")
            idx = parts.index("domains")
            if idx + 1 < len(parts):
                md_by_domain[parts[idx + 1]].append(a)
        elif "/chapters/" in f:
            parts = f.split("/")
            if len(parts) >= 3:
                ch_key = parts[2][:4]  # "ch01", "ch02", …
                md_by_chapter[ch_key].append(a)

    # ── Precompute md token sets ──────────────────────────────────────────
    print("Precomputing md tokens …")
    md_tokens: dict[str, frozenset] = {
        a["atom_id"]: tokenize(a.get("verbatim", "")) for a in md_atoms
    }

    # ── Process each pdf_atom ─────────────────────────────────────────────
    print("Building candidates …")
    results: list[dict] = []
    zero_count = 0
    global_count = 0

    for i, pdf_a in enumerate(pdf_atoms):
        if (i + 1) % 2000 == 0:
            print(f"  {i+1:,}/{len(pdf_atoms):,}  ({time.time()-t0:.1f}s)")

        pdf_id = pdf_a["atom_id"]
        pdf_type = pdf_a.get("atom_type", "SENTENCE")
        pdf_verbatim = pdf_a.get("verbatim", "")
        pdf_section = pdf_a.get("parent_section", "")
        pdf_source = pdf_a.get("source", "SDTMIG_v3.4")

        pdf_tok = tokenize(pdf_verbatim)
        is_short = len(pdf_tok) <= 5
        min_score = MIN_SCORE_SHORT if is_short else MIN_SCORE
        top_k = TOP_K_SHORT if is_short else TOP_K

        # ── FIGURE atoms: search global FIGURE pool ───────────────────────
        if pdf_type == "FIGURE":
            fig_pool = md_by_type.get("FIGURE", [])
            if not fig_pool:
                results.append({
                    "pdf_atom_id": pdf_id,
                    "pdf_atom_type": pdf_type,
                    "pdf_source": pdf_source,
                    "pdf_parent_section": pdf_section,
                    "candidates": [],
                    "candidate_count": 0,
                    "zero_candidate": True,
                })
                zero_count += 1
                continue
            pool = fig_pool
            route_basis = "global_figure"
            domain_matched = False
        else:
            # ── Domain route ──────────────────────────────────────────────
            domain = extract_domain_code(pdf_section, known_domains)
            if domain and domain in md_by_domain:
                pool = md_by_domain[domain]
                route_basis = f"domain_route:{domain}"
                domain_matched = True
            else:
                # ── Chapter route (§1-4, §8, §10) ────────────────────────
                ch_key = get_chapter_key(pdf_section)
                if ch_key and md_by_chapter.get(ch_key):
                    pool = md_by_chapter[ch_key]
                    route_basis = f"chapter_route:{ch_key}"
                else:
                    pool = md_atoms
                    route_basis = "global_search"
                    global_count += 1
                domain_matched = False

            # HEADING atoms: narrow pool to HEADING type
            if pdf_type == "HEADING":
                heading_pool = [a for a in pool if a.get("atom_type") == "HEADING"]
                if heading_pool:
                    pool = heading_pool

        # ── Score candidates ──────────────────────────────────────────────
        scored: list[tuple[float, dict]] = []
        for md_a in pool:
            md_id = md_a["atom_id"]
            md_type = md_a.get("atom_type", "SENTENCE")
            s_verb = jaccard(pdf_tok, md_tokens[md_id])
            s_type = type_score(pdf_type, md_type)
            s_dom = 1.0 if domain_matched else 0.0
            score = s_verb * W_VERBATIM + s_type * W_TYPE + s_dom * W_DOMAIN
            if score >= min_score:
                scored.append((score, md_a))

        scored.sort(key=lambda x: x[0], reverse=True)
        top = scored[:top_k]

        candidates = [
            {
                "md_atom_id": md_a["atom_id"],
                "md_file": md_a.get("file", ""),
                "md_atom_type": md_a.get("atom_type", ""),
                "score": round(score, 4),
                "match_basis": f"verbatim_token+{route_basis}",
            }
            for score, md_a in top
        ]

        is_zero = not candidates
        if is_zero:
            zero_count += 1

        results.append({
            "pdf_atom_id": pdf_id,
            "pdf_atom_type": pdf_type,
            "pdf_source": pdf_source,
            "pdf_parent_section": pdf_section,
            "candidates": candidates,
            "candidate_count": len(candidates),
            "zero_candidate": is_zero,
        })

    # ── Write output ──────────────────────────────────────────────────────
    with open(OUTPUT, "w") as f:
        for r in results:
            f.write(json.dumps(r) + "\n")

    elapsed = time.time() - t0
    print(f"\nDone in {elapsed:.1f}s")
    print(f"Output rows : {len(results):,}")
    print(f"Zero-cand   : {zero_count:,} ({zero_count/len(results)*100:.1f}%)")
    print(f"Global srch : {global_count:,} ({global_count/len(results)*100:.1f}%)")
    print(f"Written to  : {OUTPUT}")


if __name__ == "__main__":
    main()
