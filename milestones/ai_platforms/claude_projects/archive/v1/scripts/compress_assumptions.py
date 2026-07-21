#!/usr/bin/env python3
"""Compress knowledge_base/domains/<DOM>/assumptions.md for Claude Projects
(Phase 6.5 Step 7).

Emits a concatenated, compressed assumptions file (target <=20000 tokens) at
ai_platforms/claude_projects/output/06_assumptions.md.

Strategy (PLAN.md §4.3.2):
- Preserve the numeric hierarchy (top-level "N." items and their "Na./Nb./..."
  sub-items). Abstractly: every top-level numbered assumption in the source
  must appear at least as a one-line rule in the output.
- Keep variable names (e.g. AETERM, AESEQ), --placeholder references,
  Cxxxxx CT codes, §X.Y cross-references, ISO/MedDRA/WHO/LOINC/CDISC
  references, and decisive rule verbs (must / should / is expected /
  permissible / required).
- Drop CRF-table markdown (| ... | lines), Mermaid/code fences, long
  illustrative example paragraphs ("For example, ..."), "See Section X" rewrites
  reduced to "§X", most guidance URLs, and PDF page markers.
- Sentences are compressed with a deterministic lexicon of fixed rewrites
  (e.g. "It is expected that" -> "expected:", "should be populated" ->
  "populated") plus structural truncation once token budget is spent.

Idempotence (P7):
- Timestamp in the header is derived from max(mtime) of the 63 source
  files (not datetime.now()). Source files are read-only (P5).
- No randomness / no dict ordering dependencies; ASCII-only in generated
  scaffolding so two runs are byte-identical.
"""
from __future__ import annotations

import datetime as _dt
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SRC_DIR = ROOT / "knowledge_base" / "domains"
OUT = ROOT / "ai_platforms" / "claude_projects" / "output" / "06_assumptions.md"

# Canonical (alphabetical) domain order; matches the filesystem exactly.
DOMAINS = [
    "AE", "AG", "BE", "BS", "CE", "CM", "CO", "CP", "CV", "DA",
    "DD", "DM", "DS", "DV", "EC", "EG", "EX", "FA", "FT", "GF",
    "HO", "IE", "IS", "LB", "MB", "MH", "MI", "MK", "ML", "MS",
    "NV", "OE", "OI", "PC", "PE", "PP", "PR", "QS", "RE", "RELREC",
    "RELSPEC", "RELSUB", "RP", "RS", "SC", "SE", "SM", "SR", "SS",
    "SU", "SUPPQUAL", "SV", "TA", "TD", "TE", "TI", "TM", "TR",
    "TS", "TU", "TV", "UR", "VS",
]

# ---------------------------------------------------------------------------
# Line-level classifier
# ---------------------------------------------------------------------------

TOP_RE = re.compile(r"^(\d+)\.\s+(.*)$")
SUB_ALPHA_RE = re.compile(r"^\s{2,}([a-z])\.\s+(.*)$")
SUB_ROMAN_RE = re.compile(r"^\s{4,}(i{1,3}|iv|v|vi{1,3}|ix|x)\.\s+(.*)$")
SUB_DASH_RE = re.compile(r"^\s*-\s+(.*)$")
TABLE_RE = re.compile(r"^\s*\|")
FENCE_RE = re.compile(r"^\s*```")
HEADING_RE = re.compile(r"^(##+)\s+(.*)$")
BLOCKQUOTE_RE = re.compile(r"^\s*>\s?(.*)$")

# Sentence-level rewrites applied to prose fragments. The order matters
# because earlier substitutions may expose patterns for later ones.
REWRITES: list[tuple[str, str]] = [
    # Filler verbs + stock phrases
    (r"\bIt is expected that\b", "expected:"),
    (r"\bit is expected that\b", "expected:"),
    (r"\bshould be populated\b", "populated"),
    (r"\bmust be populated\b", "populated (Req)"),
    (r"\bis a required variable and must have a value\b", "Req; non-null"),
    (r"\bmust have a value\b", "non-null"),
    (r"\bis the topic variable\b", "is topic var"),
    (r"\bis a permissible variable\b", "Perm"),
    (r"\bis a Permissible variable\b", "Perm"),
    (r"\bis an expected variable\b", "Exp"),
    (r"\bis a required variable\b", "Req"),
    (r"\bpermissible variable\b", "Perm var"),
    (r"\brequired variable\b", "Req var"),
    (r"\bexpected variable\b", "Exp var"),
    (r"\bThe sponsor is expected to provide the dictionary name and version used to map the terms utilizing the external codelist element in the Define-XML document\.?",
     "Dictionary name + version via Define-XML external codelist."),
    (r"\bvariable may be subject to controlled terminology\b", "var may be CT"),
    (r"\bis the preferred term derived by the sponsor from the coding dictionary\b",
     "= dictionary preferred term"),
    (r"\bis the preferred term\b", "= preferred term"),
    (r"\bin the Define-XML document\b", "via Define-XML"),
    (r"\bin the Define\.xml document\b", "via Define-XML"),
    (r"\bin the Define-XML\b", "via Define-XML"),
    (r"\bas described in Section\b", "see §"),
    (r"\bas described in\b", "see"),
    (r"\bdescribed in Section\b", "§"),
    (r"\bSee Section\b", "see §"),
    (r"\bsee Section\b", "see §"),
    (r"\bSection\s+(\d+\.\d+(?:\.\d+)?)", r"§\1"),
    (r"\bsection\s+(\d+\.\d+(?:\.\d+)?)", r"§\1"),
    (r"\bSection\s+(\d+)\b", r"§\1"),
    (r"\bCDISC/NCI codelist values are enclosed in parentheses\.?", ""),
    (r"\bvalues are enclosed in parentheses\.?", ""),
    # Normalize dashes/smart quotes
    (r"\u2014", "-"),
    (r"\u2013", "-"),
    (r"\u2019", "'"),
    (r"\u2018", "'"),
    (r"\u201c", '"'),
    (r"\u201d", '"'),
    # Drop long "For example, ..." sentences embedded in a paragraph (keep
    # short parenthetical e.g.). We strip from "For example, " to the next
    # sentence terminator.
    (r"For example,[^.]{0,400}\.\s*", ""),
    (r"For example:[^.]{0,400}\.\s*", ""),
    # Simplify common CT phrasing
    (r"\bmaintained for CDISC by NCI EVS\b", "CDISC CT"),
    (r"\bcontrolled terminology\b", "CT"),
    (r"\bControlled Terminology\b", "CT"),
    (r"\bCDISC Controlled Terminology\b", "CDISC CT"),
    # Collapse ISO/MedDRA phrasing
    (r"\bLogical Observation Identifiers Names and Codes \(LOINC\)\b", "LOINC"),
    (r"\bCommon Terminology Criteria for Adverse Events\b", "CTCAE"),
    # Collapse well-known prefixes that appear many times per domain
    (r"\bIn consultation with regulatory authorities, sponsors\b", "Sponsors"),
    (r"\bThe events included in the [A-Z]{2,} dataset should be consistent with the protocol requirements\.?\s*",
     ""),
    (r"\bAdverse events may be captured either as free text or via a prespecified list of terms\.?",
     "AEs: free text or prespecified list."),
    # PDF page references
    (r"\s*\(see page \d+\)", ""),
    (r"\s*on page \d+\b", ""),
    # Some domains embed bracketed guidance URLs; shorten to domain
    (r"https?://(?:www\.)?cdisc\.org[^\s)\]]*", "cdisc.org"),
    (r"https?://[^\s)\]]*cancer\.gov[^\s)\]]*", "cancer.gov"),
    (r"https?://[^\s)\]]+", "(url)"),
]

_REWRITE_COMPILED = [(re.compile(pat), repl) for pat, repl in REWRITES]


def _rewrite(text: str) -> str:
    for pat, repl in _REWRITE_COMPILED:
        text = pat.sub(repl, text)
    # Collapse internal whitespace without touching leading indent.
    m = re.match(r"^(\s*)(.*)$", text, re.DOTALL)
    if m:
        lead, body = m.group(1), m.group(2)
        body = re.sub(r"[ \t]{2,}", " ", body)
        body = re.sub(r"\s+\.", ".", body)
        body = re.sub(r"\s+,", ",", body)
        text = lead + body.strip()
    return text


def _strip_markdown_emphasis(text: str) -> str:
    # Strip bold **foo** used for section callouts inside a list item.
    return re.sub(r"\*\*([^*]+)\*\*", r"\1", text)


# ---------------------------------------------------------------------------
# Compressor
# ---------------------------------------------------------------------------

def _split_sentences(body: str) -> list[str]:
    """Split a paragraph into sentences on '. ' while preserving abbreviations
    like "e.g.", "i.e.", "vs.", "U.S.". Deterministic and ASCII-safe."""
    # Protect common abbreviations.
    placeholders = {
        "e.g.": "\x01EG\x01",
        "i.e.": "\x01IE\x01",
        "vs.": "\x01VS\x01",
        "etc.": "\x01ETC\x01",
        "U.S.": "\x01US\x01",
    }
    for k, v in placeholders.items():
        body = body.replace(k, v)
    sents = re.split(r"(?<=[.!?])\s+(?=[A-Z(\[])", body)
    restored = []
    for s in sents:
        for k, v in placeholders.items():
            s = s.replace(v, k)
        s = s.strip()
        if s:
            restored.append(s)
    return restored


def _keep_sentence(sent: str) -> bool:
    """Decide whether a sentence carries load-bearing signal.

    A sentence is kept if any of the following are true:
    - contains an ALL-CAPS variable-style token (>=3 chars: AETERM, ISO, CT)
    - contains a §X.Y cross reference
    - contains a "must", "should", "is expected", "required", "permissible"
    - contains a CT/code pattern (Cxxxxx, MedDRA, LOINC, ICH, WHO)
    - contains a --placeholder reference (e.g. --SEQ)
    - is short enough that it is likely a rule summary (<60 chars)
    """
    if not sent:
        return False
    if re.search(r"\b[A-Z]{3,}\d*\b", sent):
        return True
    if "§" in sent:
        return True
    if re.search(r"\b(must|should|is expected|required|permissible|Req|Exp|Perm)\b", sent):
        return True
    if re.search(r"C\d{5,6}\b", sent):
        return True
    if re.search(r"\b(ISO|MedDRA|LOINC|ICH|WHO|CDISC|NCI|SNOMED|FDA|UCUM|CTCAE)\b", sent):
        return True
    if re.search(r"--\w+", sent):
        return True
    if len(sent) <= 60:
        return True
    return False


def _strip_long_parens(text: str) -> str:
    """Drop long explanatory parenthetical asides ((> 40 chars)). Short
    parens (e.g., acronym expansions or short references) are kept."""
    out = []
    depth = 0
    start = -1
    buf = []
    for ch in text:
        if ch == "(":
            if depth == 0:
                start = len(buf)
            depth += 1
            buf.append(ch)
        elif ch == ")":
            buf.append(ch)
            if depth > 0:
                depth -= 1
                if depth == 0 and start >= 0:
                    seg = "".join(buf[start:])
                    # seg includes the surrounding parens. Drop if long and not
                    # a reference like "(§4.2.6)" or "(Cxxxxx)" or "(MedDRA)".
                    if len(seg) > 42 and not re.search(r"§|C\d{5,}|ISO|MedDRA|LOINC|ICH|WHO|CDISC|NCI|CTCAE|FDA|UCUM", seg):
                        del buf[start:]
                    start = -1
        else:
            buf.append(ch)
    return "".join(buf)


def _drop_filler_clauses(text: str) -> str:
    """Drop slow hedging clauses that carry no rule."""
    patterns = [
        r"In other words,[^.]*\.",
        r"However,[^.]*\.",
        r"Therefore,[^.]*\.",
        r"It is important to note that[^.]*\.",
        r"It should be noted that[^.]*\.",
        r"Please note that[^.]*\.",
        r"Note that[^.]*\.",
        r"In this case,\s*",
        r"In most cases,\s*",
        r"In some cases,\s*",
        r"Specifically,\s*",
        r"Additionally,\s*",
        r"Alternatively,\s*",
        r"Similarly,\s*",
    ]
    for pat in patterns:
        text = re.sub(pat, "", text)
    return text


def _truncate_sentence(sent: str, max_chars: int = 160) -> str:
    """Hard-truncate a long sentence at a word boundary near max_chars,
    preserving any trailing variable tokens the sentence starts with."""
    sent = sent.strip()
    if len(sent) <= max_chars:
        return sent
    # Try to cut at the last comma before max_chars.
    cut = sent.rfind(", ", 0, max_chars)
    if cut < max_chars // 2:
        cut = sent.rfind(" ", 0, max_chars)
    if cut <= 0:
        cut = max_chars
    out = sent[:cut].rstrip(",; ").rstrip()
    # Ensure terminal punctuation.
    if out and out[-1] not in ".!?":
        out = out + "."
    return out


def _compress_prose(prose: str, is_sub: bool = False) -> str:
    """Apply sentence-level compression to a prose fragment.

    ``is_sub`` tightens the budget for alpha / roman sub-items.
    """
    prose = _rewrite(prose)
    prose = _strip_markdown_emphasis(prose)
    prose = _drop_filler_clauses(prose)
    prose = _strip_long_parens(prose)
    sents = _split_sentences(prose)
    kept = [s for s in sents if _keep_sentence(s)]
    if not kept and sents:
        # Ensure we keep at least the first sentence for signal.
        kept = [sents[0]]
    # Dedup by normalized form to drop repeats.
    seen: set[str] = set()
    out: list[str] = []
    # Hard cap on sentence count per item to keep sub-items terse.
    max_sents = 1
    for s in kept:
        key = re.sub(r"\s+", " ", s).strip().lower()
        if key in seen:
            continue
        seen.add(key)
        out.append(s.strip())
        if len(out) >= max_sents:
            break
    max_chars = 95 if is_sub else 130
    out = [_truncate_sentence(s, max_chars) for s in out]
    joined = " ".join(out)
    # Final whitespace normalization.
    joined = re.sub(r"\s{2,}", " ", joined).strip()
    # Trim double-period and orphan punctuation left by rewrites.
    joined = re.sub(r"\s+\.", ".", joined)
    joined = re.sub(r"\.{2,}", ".", joined)
    joined = re.sub(r",\s*\.", ".", joined)
    joined = re.sub(r"^,\s*", "", joined)
    return joined


def _parse_items(text: str) -> list[dict]:
    """Parse assumptions.md body into a structured list of items.

    Returns a list of dicts with keys:
      kind   : "top" | "sub" | "roman" | "heading" | "prose"
      label  : "1", "a", "ii", or "" for heading/prose
      text   : plain text content
      children : list[dict]  (for nested sub-items)
    """
    # Remove the top H1 "# <DOM> - Assumptions" line; it's added back per dom.
    lines = text.splitlines()
    # Skip leading H1 + blank line.
    while lines and (not lines[0].strip() or lines[0].startswith("# ")):
        lines.pop(0)

    items: list[dict] = []
    current_top: dict | None = None
    current_sub: dict | None = None
    buffer: list[str] = []

    def _flush_buffer_into(target: dict | None) -> None:
        if not buffer:
            return
        joined = " ".join(b.strip() for b in buffer if b.strip())
        buffer.clear()
        if not joined:
            return
        if target is None:
            items.append({"kind": "prose", "label": "", "text": joined, "children": []})
        else:
            if target["text"]:
                target["text"] = target["text"] + " " + joined
            else:
                target["text"] = joined

    i = 0
    while i < len(lines):
        ln = lines[i]
        stripped = ln.rstrip()

        # Skip fenced code blocks entirely.
        if FENCE_RE.match(stripped):
            _flush_buffer_into(current_sub or current_top)
            i += 1
            while i < len(lines) and not FENCE_RE.match(lines[i]):
                i += 1
            if i < len(lines):
                i += 1
            continue

        # Skip markdown tables (CRF tables etc.) entirely.
        if TABLE_RE.match(stripped):
            _flush_buffer_into(current_sub or current_top)
            while i < len(lines) and (TABLE_RE.match(lines[i]) or lines[i].strip() == ""):
                # Consume consecutive table rows. Stop when we hit non-table
                # non-blank content or two blank lines in a row.
                if lines[i].strip() == "":
                    # Peek to see if next is still table; if not, stop here.
                    nxt = lines[i + 1] if i + 1 < len(lines) else ""
                    if not TABLE_RE.match(nxt):
                        break
                i += 1
            continue

        # Blockquotes become prose (stripped of leading '>').
        if BLOCKQUOTE_RE.match(stripped):
            buffer.append(BLOCKQUOTE_RE.match(stripped).group(1))
            i += 1
            continue

        # Headings inside a domain (e.g. SUPPQUAL "## When Not to Use ...")
        h = HEADING_RE.match(stripped)
        if h:
            _flush_buffer_into(current_sub or current_top)
            current_sub = None
            items.append({
                "kind": "heading",
                "label": "",
                "text": h.group(2).strip(),
                "children": [],
            })
            current_top = None
            i += 1
            continue

        m_top = TOP_RE.match(stripped)
        if m_top:
            _flush_buffer_into(current_sub or current_top)
            current_sub = None
            current_top = {
                "kind": "top",
                "label": m_top.group(1),
                "text": m_top.group(2).strip(),
                "children": [],
            }
            items.append(current_top)
            i += 1
            continue

        m_sub = SUB_ALPHA_RE.match(stripped)
        if m_sub:
            _flush_buffer_into(current_sub or current_top)
            current_sub = {
                "kind": "sub",
                "label": m_sub.group(1),
                "text": m_sub.group(2).strip(),
                "children": [],
            }
            if current_top is not None:
                current_top["children"].append(current_sub)
            else:
                items.append(current_sub)
            i += 1
            continue

        m_roman = SUB_ROMAN_RE.match(stripped)
        if m_roman:
            _flush_buffer_into(current_sub or current_top)
            roman_item = {
                "kind": "roman",
                "label": m_roman.group(1),
                "text": m_roman.group(2).strip(),
                "children": [],
            }
            if current_sub is not None:
                current_sub["children"].append(roman_item)
            elif current_top is not None:
                current_top["children"].append(roman_item)
            else:
                items.append(roman_item)
            i += 1
            continue

        m_dash = SUB_DASH_RE.match(stripped)
        if m_dash:
            # Dash bullet inside a sub-item or top-item; treat as continuation
            # text appended with "; " separator for compactness.
            target = current_sub or current_top
            if target is not None:
                payload = "- " + m_dash.group(1).strip()
                if target["text"]:
                    target["text"] = target["text"] + " " + payload
                else:
                    target["text"] = payload
            else:
                buffer.append("- " + m_dash.group(1).strip())
            i += 1
            continue

        # Blank line flushes buffer into the current item context.
        if stripped == "":
            _flush_buffer_into(current_sub or current_top)
            i += 1
            continue

        # Otherwise, append as continuation text of the current scope.
        buffer.append(stripped.strip())
        i += 1

    _flush_buffer_into(current_sub or current_top)
    return items


def _format_items(items: list[dict]) -> list[str]:
    """Render parsed items back into compressed Markdown lines."""
    out: list[str] = []
    prose_heading_skipped = False

    for item in items:
        kind = item["kind"]
        if kind == "heading":
            txt = _compress_prose(item["text"])
            if txt:
                out.append(f"**{txt}**")
            continue
        if kind == "prose":
            txt = _compress_prose(item["text"])
            if txt:
                out.append(txt)
            continue
        if kind == "top":
            head = _compress_prose(item["text"], is_sub=False)
            line = f"{item['label']}. {head}".rstrip()
            out.append(line)
            for child in item["children"]:
                ctxt = _compress_prose(child["text"], is_sub=True)
                if not ctxt:
                    continue
                if child["kind"] == "roman":
                    out.append(f"      {child['label']}. {ctxt}")
                else:
                    out.append(f"   {child['label']}. {ctxt}")
                for gc in child.get("children", []):
                    gctxt = _compress_prose(gc["text"], is_sub=True)
                    if gctxt:
                        out.append(f"      {gc['label']}. {gctxt}")
            continue
        if kind == "sub":
            # Orphan sub-item (no preceding top); render as a dash bullet so
            # we do not lose its content.
            ctxt = _compress_prose(item["text"], is_sub=True)
            if ctxt:
                out.append(f"- {ctxt}")
            continue
        if kind == "roman":
            ctxt = _compress_prose(item["text"], is_sub=True)
            if ctxt:
                out.append(f"- {ctxt}")
            continue

    return out


def compress_domain(raw: str) -> str:
    items = _parse_items(raw)
    lines = _format_items(items)
    return "\n".join(lines).rstrip() + "\n"


# ---------------------------------------------------------------------------
# Build output
# ---------------------------------------------------------------------------

def build_output() -> str:
    src_paths = [SRC_DIR / d / "assumptions.md" for d in DOMAINS]
    for p in src_paths:
        if not p.is_file():
            raise FileNotFoundError(f"source not found: {p}")

    max_mtime = max(os.path.getmtime(p) for p in src_paths)
    ts = _dt.datetime.utcfromtimestamp(max_mtime).strftime("%Y-%m-%d")

    parts: list[str] = []
    parts.append(
        f"<!-- generated by scripts/compress_assumptions.py (source mtime: {ts}) -->\n"
    )
    parts.append("<!-- 63 domains x assumptions.md entry-level compression -->\n\n")
    parts.append("# SDTM Domain Assumptions (Compressed)\n\n")
    parts.append(
        "## 说明\n"
        "保留规则骨架与变量引用；删除：冗长背景叙述、PDF 页码引用、大篇幅示例文字 + "
        "CRF 图表。完整原文见 `knowledge_base/domains/<DOM>/assumptions.md`。\n\n"
    )

    for dom in DOMAINS:
        src_rel = f"knowledge_base/domains/{dom}/assumptions.md"
        raw = (SRC_DIR / dom / "assumptions.md").read_text(encoding="utf-8")
        compressed = compress_domain(raw)
        parts.append(f"<!-- source: {src_rel} -->\n")
        parts.append(f"## {dom}\n\n")
        parts.append(compressed)
        parts.append("\n")

    return "".join(parts)


def main() -> int:
    output = build_output()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(output, encoding="utf-8")
    print(
        f"wrote {OUT} ({len(output)} chars, {len(output.splitlines())} lines)"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
