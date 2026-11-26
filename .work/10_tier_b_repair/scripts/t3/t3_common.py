"""T3 shared helpers: ref expander (writer.jsonl refs -> atom ids), checkpoint / verdict pointers, KB reader."""
import glob, json, os, re, sys

ROOT = "/Volumes/DevSSD/Project/sdtm-pedia"
TB = f"{ROOT}/.work/10_tier_b_repair"
W = f"{TB}/work"
CK = f"{TB}/evidence/checkpoints"
sys.path.insert(0, f"{TB}/scripts")
from fp_match import norm, norm_pdf, lj  # noqa: E402

FIX_ACTIONS = {"INSERTED", "REPLACED", "TABLE_REBUILT", "MOVED", "RELOCATE", "R3_RESTORED"}
_TOK = re.compile(r"(?P<full>(?P<src>ig34|sv20)_p(?P<pg>\d{4})_a(?P<an>\d+))"
                  r"|(?P<sep>\.\.|/|\+|,|-(?=(?:p\d{4}_)?a\d))"
                  r"|(?<![A-Za-z0-9_])(?P<part>(?:p(?P<ppg>\d{4})_)?a(?P<pan>\d+))(?![A-Za-z0-9])")


def atom_order():
    ids = [a["atom_id"] for a in lj(f"{W}/pdf_atoms.jsonl")]
    return ids, {i: n for n, i in enumerate(ids)}


def expand_ref(ref, idx, order):
    """Return (atom_ids, unparsed_bits). Handles a010..a018, a0014/a0015, X..p0367_a003, '+' / ',' lists.
    Refs carrying ':src' or '-adj' are source/adjacency markers, not fix claims -> ([], [])."""
    if ":src" in ref or "-adj" in ref:
        return [], []
    out, bad, last, pend = [], [], None, None
    for m in _TOK.finditer(ref):
        if m.group("sep"):
            pend = m.group("sep")
            continue
        if m.group("full"):
            cur = m.group("full")
            src = m.group("src")
        elif m.group("part") and last and pend in ("..", "/", "-"):
            src, pg = last.split("_")[0], last.split("_")[1][1:]
            cur = f"{src}_p{m.group('ppg') or pg}_a{m.group('pan')}"
        else:
            pend = None
            continue
        if cur not in idx:
            bad.append(cur)
            pend = None
            continue
        if pend in ("..", "-") and last:
            lo, hi = idx[last], idx[cur]
            if hi < lo or hi - lo > 60:
                bad.append(f"{last}..{cur}")
            else:
                out.extend(order[lo + 1:hi + 1])
        else:
            out.append(cur)
        last, pend = cur, None
    return list(dict.fromkeys(out)), bad


def writer_rows():
    """[(batch, writer_file_rel, line_no, row)] over all T2 (B-*) and T2S (S-*) writer logs."""
    rows = []
    for f in sorted(glob.glob(f"{W}/t2_batches/*.writer.jsonl")):
        b = os.path.basename(f).split(".writer")[0]
        for n, l in enumerate(open(f, encoding="utf-8"), 1):
            if l.strip():
                rows.append((b, os.path.relpath(f, ROOT), n, json.loads(l)))
    return rows


_ck_cache = {}
def ck_lines(path):
    if path not in _ck_cache:
        _ck_cache[path] = open(path, encoding="utf-8").read().splitlines() if os.path.exists(path) else []
    return _ck_cache[path]


def ck_line_of(batch, atom_id):
    """First line of evidence/checkpoints/t2_<batch>.md mentioning atom_id (or its pNNNN_aNNN tail)."""
    p = f"{CK}/t2_{batch}.md"
    tail = atom_id.split("_", 1)[1]
    for n, l in enumerate(ck_lines(p), 1):
        if atom_id in l or tail in l:
            return f"{os.path.relpath(p, ROOT)}:{n}"
    return None


def ck_find(batch, needles):
    """First line of evidence/checkpoints/t2_<batch>.md containing any needle (tried in order)."""
    p = f"{CK}/t2_{batch}.md"
    for nd in needles:
        for n, l in enumerate(ck_lines(p), 1):
            if nd and nd in l:
                return f"{os.path.relpath(p, ROOT)}:{n}"
    return None


_VERD = re.compile(r"(结论|判定|裁定|总判|签字|verdict|Verdict|VERDICT|RESULT|→)[^\n]{0,80}\bPASS\b|\*\*PASS\*\*")
def verdict_ptr(batch, kind):
    """kind in ('review','audit'): file:line of a PASS verdict line (strong pattern first, else last line with
    the word PASS), else None. Tries *_review_a*.md too (latest attempt sorted last)."""
    for p in reversed(sorted(glob.glob(f"{CK}/t2_{batch}_{kind}*.md"))):
        ls = ck_lines(p)
        hit = next((n for n, l in enumerate(ls, 1) if _VERD.search(l) and "FAIL" not in l), None) or \
            next((n for n in range(len(ls), 0, -1) if re.search(r"\bPASS\b", ls[n - 1]) and "FAIL" not in ls[n - 1]), None)
        if hit:
            return f"{os.path.relpath(p, ROOT)}:{hit}"
    return None


def batch_commits():
    """batch id -> short hash of its '(PASS; local)' KB commit (git log subjects)."""
    import subprocess
    out = subprocess.run(["git", "-C", ROOT, "log", "--format=%h %s"], capture_output=True, text=True).stdout
    m = {}
    for l in out.splitlines():
        h, s = l.split(" ", 1)
        g = re.search(r"Tier B (?:scan )?batch (\S+) —", s)
        if g and "PASS" in s and g.group(1) not in m:
            m[g.group(1)] = h
    m.setdefault("B-PCPP", "97e1895")  # subject has no PASS tag; batch closed by user ack (t2_B-PCPP_user_ack.md)
    return m


_kb = {}
def kb_norm(rel, kb_root=f"{ROOT}/knowledge_base"):
    """rel = 'knowledge_base/...'. Normalized text of that file under kb_root ('' if missing)."""
    key = (kb_root, rel)
    if key not in _kb:
        p = os.path.join(kb_root, rel[len("knowledge_base/"):])
        _kb[key] = norm(open(p, encoding="utf-8").read()) if os.path.exists(p) else ""
    return _kb[key]


# ── attempt 2 (审计 K1/K2/K11): word-boundary + section-anchor hit search on per-line normalized text ──
INDEX_FILES = {"knowledge_base/VARIABLE_INDEX.md", "knowledge_base/INDEX.md", "knowledge_base/ROUTING.md"}
_NUM = re.compile(r"§?\s*(\d+(?:\.\d+)+)")
_lines_cache = {}


def kb_lines(rel, kb_root=f"{ROOT}/knowledge_base"):
    """(joined, starts, lines): norm of each line joined by ' '; starts[k] = offset of line k (0-based) in joined."""
    key = (kb_root, rel)
    if key not in _lines_cache:
        p = os.path.join(kb_root, rel[len("knowledge_base/"):])
        raw = open(p, encoding="utf-8").read().splitlines() if os.path.exists(p) else []
        parts, starts, off = [], [], 0
        for l in raw:
            n = norm(l)
            starts.append(off)
            parts.append(n)
            off += len(n) + 1
        _lines_cache[key] = (" ".join(parts), starts, raw)
    return _lines_cache[key]


def atom_secnum(parent_section):
    m = re.match(r"^§\s*(\d+(?:\.\d+)*)", parent_section or "")
    return m.group(1) if m else None


def _heading(l):
    """(level, number|None) for a markdown heading line, else None. Number = leading '§n.n' / 'n.n' / 'n' after the
    hashes, or a '§n.n' anywhere; version strings like 'v3.4' / 'v2.0' are not section numbers."""
    m = re.match(r"^\s*(#{1,6})\s", l)
    if not m:
        return None
    n = re.match(r"^\s*#{1,6}\s*(?:\*\*)?(?:§\s*)?(\d+(?:\.\d+)*)(?=[\s.:\])]|$)", l) or re.search(r"§\s*(\d+(?:\.\d+)*)", l)
    return len(m.group(1)), (n.group(1) if n else None)


def anchor_ok(raw_lines, line_idx, secnum, same_source):
    """The governing numbered heading of the hit line must be the atom's section, an ancestor or a descendant.
    Governing = nearest heading if numbered; else the nearest numbered heading of strictly higher rank (smaller level)
    than every unnumbered heading passed on the way up (an unnumbered '## LB – Assumptions' is not governed by an earlier
    sibling '## §6.3.5.1'). Nothing numbered governs, no atom section number, or other-PDF file -> accepted."""
    if not secnum:
        return True, "atom section has no number"
    if not same_source:
        return True, "file numbering is the other PDF"
    cap = 99
    for k in range(line_idx, -1, -1):
        h = _heading(raw_lines[k])
        if not h or h[0] >= cap:
            continue
        lvl, num = h
        if num:
            ok = num == secnum or num.startswith(secnum + ".") or secnum.startswith(num + ".")
            return ok, f"heading:{k + 1} §{num} vs atom §{secnum}"
        cap = lvl
    return True, "no governing numbered heading"


def valid_hits(rel, v, atom_id, parent_section, kb_root=f"{ROOT}/knowledge_base"):
    """Line numbers (1-based) of occurrences of normalized verbatim v in file rel with word boundaries
    (if v starts/ends with an alnum char the neighbour must not be alnum) and an accepted section anchor."""
    if not v:
        return [], []
    joined, starts, raw = kb_lines(rel, kb_root)
    src = atom_id.split("_")[0]
    same = ("sv20" if rel.startswith("knowledge_base/model/") else "ig34") == src
    sec = atom_secnum(parent_section)
    out, rej, i = [], [], joined.find(v)
    import bisect
    while i != -1:
        pre_fn = i >= 1 and joined[i - 1] == "1" and (i == 1 or not joined[i - 2].isalnum()) and \
            v.startswith("in this column")  # NFKC turns the '¹' footnote marker into '1' ('¹In this column')
        b_ok = (not v[0].isalnum() or i == 0 or not joined[i - 1].isalnum() or pre_fn) and \
               (not v[-1].isalnum() or i + len(v) >= len(joined) or not joined[i + len(v)].isalnum())
        li = bisect.bisect_right(starts, i) - 1
        if b_ok:
            ok, why = anchor_ok(raw, li, sec, same)
            (out if ok else rej).append((li + 1, why))
        else:
            rej.append((li + 1, "word boundary"))
        i = joined.find(v, i + 1)
    return out, rej
