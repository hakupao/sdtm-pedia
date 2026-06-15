"""S1: deterministic structured-lookup retrieval lever.

Three query classes that cosine + BM25 both miss, but whose answer lives in the KB
as structured data:

  (1) terminology / CT-code queries (e.g. "values allowed for AESEV", "codelist
      code for VSTESTCD"). The gold is a terminology file whose heading is the CT
      *code* (e.g. "C66769"); the variable name never appears in it, so embeddings
      and lexical search both fail. KB still encodes the mapping deterministically:
      variable -> (codelist name, CT code, terminology file).

  (2) distribution / relationship queries ("which domains use EPOCH", "which
      domains share codelist C66742"). The gold is VARIABLE_INDEX.md.

  (3) concept-definition queries about a variable whose *definition home* is a
      chapters/ or model/*.md file, not a domain spec. Two sub-cases:
        (3a) a concrete variable defined in a model/*.md chapter ("what does RDOMAIN
             identify", "what does RELTYPE mean") -> the model file that introduces
             it with a real definition (RDOMAIN -> model/06_relationship_datasets.md).
        (3b) a generic '--'-prefix variable ("what does --DUR represent", "difference
             between --LNKID and --LNKGRP") -> ch04 General Assumptions, the SDTM home
             of cross-domain variable conventions.
      cosine routes these to whatever domain spec mentions the variable, and the
      distribution channel routes "which domains carry RDOMAIN" to VARIABLE_INDEX —
      both miss the definition file. Both sub-cases key on a strict definitional-verb
      (or comparison) shape, so they fire only on genuine definition asks, never on
      distribution / usage / attribute questions that merely name the same variable.

`StructuredLookup` parses the read-only KB once at engine init and exposes
`resolve(query)` returning the *gold file paths* (relative to KB root) that should
be union-added into the retrieval result. It is conservative: when no intent
keyword matches, it returns `[]` and the caller falls back to plain cosine.

Data sources (all already verified to exist in the KB):
  - spec.md "Cross References" block  -> var -> (codelist, CT code, term file)
  - spec.md "### VAR" entries          -> known-variable vocabulary + CT cross-check
  - terminology "## Name (Cxxxxx)"      -> CT code -> term file
  - VARIABLE_INDEX.md §一/§二/§三       -> general vars, domain vars, CT->vars
  - VARIABLE_INDEX.md §二 headings      -> domain long name -> code (long-name-only
                                           queries reach domains/<CODE>/spec.md)
  - model/*.md variable-def tables      -> var -> model definition-home file (rows
                                           with a non-empty Notes cell; single-file
                                           vars only) for the concept-definition channel (3a)
  - chapters/ch04*.md                    -> ch04 General Assumptions, the definition
                                           home for generic '--'-prefix variables (3b)
"""
from __future__ import annotations

import re
from collections import defaultdict
from pathlib import Path

# spec.md cross-reference line, e.g.:
#   - [Severity/Intensity Scale for Adverse Events (C66769)](../../terminology/core/ae.md) — AESEV
# The variable tail may be truncated ("AEPRESP, AESER ... (13 total)"); we keep
# whatever explicit tokens are present (the truncation is harmless: the same vars
# get their CT code from their own "### VAR" entry too).
_XREF_RE = re.compile(
    r"^- \[(.+?)\s*\((C\d{4,6})\)\]\(([^)]+)\)\s*[—-]+\s*(.+)$"
)
# spec.md single-variable header: "### AESEV"
_VAR_HEADER_RE = re.compile(r"^###\s+([A-Z][A-Z0-9]+)\s*$")
# "- **Controlled Terms:** C66769"
_CT_FIELD_RE = re.compile(r"^- \*\*Controlled Terms:\*\*\s*(C\d{4,6})\s*$")
# terminology heading: "## Severity/Intensity Scale for Adverse Events (C66769)"
_TERM_HEADER_RE = re.compile(r"^##\s+.*\((C\d{4,6})\)\s*$")
# VARIABLE_INDEX §一 / §三 table rows
_GEN_VAR_ROW_RE = re.compile(r"^\|\s*([A-Z][A-Z0-9]+)\s*\|\s*\d+\s*\|")
_SEC3_ROW_RE = re.compile(r"^\|\s*(C\d{4,6})\s*\|\s*\d+\s*\|\s*(.+?)\s*\|")
# VARIABLE_INDEX §二 domain heading: "### AE — Adverse Events (Events)"
# Captures code + long name; the trailing "(Class)" parenthetical is dropped.
_DOMAIN_HEADER_RE = re.compile(r"^###\s+([A-Z][A-Z0-9]+)\s+[—-]+\s+(.+?)\s+\([^)]+\)\s*$")
# uppercase token candidates in a query (>=2 chars so "AE"/"VS" qualify)
_QUERY_VAR_TOKEN_RE = re.compile(r"\b([A-Z][A-Z0-9]{1,})\b")
_QUERY_CT_RE = re.compile(r"\bC\d{4,6}\b")

# Terminology / CT-code intent.
_TERM_INTENT_KW = (
    "codelist",
    "controlled term",
    "controlled terminology",
    "codelist code",
    "allowed value",
    "allowed values",
    "values for",
    "extensible",
    "codelist for",
)
# Distribution / relationship intent (gold = VARIABLE_INDEX.md).
#
# Generalized from a fixed keyword list ("which domains", "use the", ...) which
# was brittle: "Which SDTM domains include VISITNUM" never literally contains
# "which domains", and "List several domains where EPOCH is used" contained none
# of the old keywords. Two anchor shapes both route to VARIABLE_INDEX.md:
#
#   (A) variable-distribution — "in which domains does variable X appear":
#         (a) the query names a known SDTM variable, AND
#         (b) it mentions plural `domains` (or its everyday synonym `datasets` —
#             users phrase distribution queries over "datasets" as often as
#             "domains"; the variable + verb double-anchor keeps the synonym
#             from widening the trigger beyond variable-distribution), AND
#         (c) it carries a cross-domain-membership verb/qualifier (_DIST_VERB_KW:
#             use/include/appear/across/carry/share/which/where/list/...).
#       Any "variable X across domains" phrasing is caught; requiring a named
#       variable keeps it off unrelated multi-domain prose.
#
#   (B) codelist-sharing — "which domains share codelist Cxxxx" (q34/q67/q68/
#       q71 name a CT code, not a variable): a CT code is present AND a
#       membership verb/qualifier fires. Gold is still VARIABLE_INDEX.md §三.
#
# This is a generalized pattern, NOT hardcoded question forms or variable names.
_DIST_DOMAINS_RE = re.compile(r"\b(?:domains|datasets)\b", re.IGNORECASE)
_DIST_VERB_KW = (
    "use",
    "used",
    "uses",
    "using",
    "include",
    "includes",
    "including",
    "appear",
    "appears",
    "across",
    "carry",
    "carries",
    "share",
    "shared",
    "shares",
    "which",
    "what",
    "where",
    "list",
    "contain",
    "contains",
)

# Concept-definition intent (gold = a model/*.md definition-home file).
#
# Fires ONLY on a strict definitional-verb shape: "what does/is [the] <VAR>
# [variable] <def-verb>", where <def-verb> is identify/define/mean/represent/
# capture/do. This is the load-bearing discriminator that separates a genuine
# definition ask ("what does RDOMAIN identify") from a distribution ask ("which
# domains carry RDOMAIN", routed to VARIABLE_INDEX) or an attribute ask ("what is
# RACE's Core designation in DM", routed to a domain spec) that names the same
# variable. The <VAR> group is case-sensitive (uppercase, like _QUERY_VAR_TOKEN_RE)
# so the surrounding case-insensitive prose cannot capture a lowercase common word;
# the captured token must still hit the model def-home map, so a non-variable
# capture resolves to nothing and the channel stays silent.
#
# Deliberately NOT matched: "used"/"role"/"core"/bare mention — broadening the verb
# set would spray model files (the def-home map holds high-frequency vars like
# RACE/SEX/EPOCH -> model/03) into distribution/terminology/attribute questions.
_DEFVERB_RE = re.compile(
    r"(?i:\bwhat\s+(?:does|is)\s+(?:the\s+)?)"
    r"([A-Z][A-Z0-9]+)"
    r"(?i:(?:\s+variable)?\s+(?:do|does|identif\w*|defin\w*|mean\w*|represent\w*|capture\w*))"
)

# Generic-variable concept-definition intent (gold = the general-assumptions chapter
# ch04). Generic '--'-prefix variables (--LNKID, --DUR, --STDTC, ...) are the SDTM
# convention for cross-domain variable patterns; their authoritative definitions live
# in ch04 General Assumptions, not in any single domain spec — so neither cosine (which
# routes to whatever domain spec mentions them) nor the domain/distribution channels
# reach ch04. This channel fires on a definition/comparison ask about a '--' token:
#   * comparison: "difference between <--X> and <--Y>" (>= 2 '--' tokens), OR
#   * single-var definition: the q73-style verb shape on one '--' token
#     ("what does --DUR represent").
# It is suppressed when distribution intent already routed (so "which domains use
# --STAT" stays on VARIABLE_INDEX), and stays silent on usage asks ("is it acceptable
# to use --SEQ as the join key" -> ch08, no def/comparison verb). Pattern-level: keys
# on the '--' convention + definition intent, not on any specific variable.
#
# _DASHVAR_RE uses a negative lookbehind (not \b) because \b is NOT a boundary between
# a space and a hyphen, so r"\b--[A-Z]" matches nothing. The trailing negative
# lookahead (also excluding '-') rejects glued/typo'd compounds ("--SEQ--ENDTC",
# "--SE-Q") that could otherwise mis-satisfy the >=2-token compare count.
_DASHVAR_RE = re.compile(r"(?<![A-Za-z-])--[A-Z]{2,8}(?![A-Za-z-])")
_COMPARE_RE = re.compile(r"\bdifference(?:s)?\s+between\b", re.IGNORECASE)
_DASH_DEFVERB_RE = re.compile(
    r"(?i:\bwhat\s+(?:does|is)\s+(?:the\s+)?)"
    r"--[A-Z]{2,8}"
    r"(?i:(?:\s+variable)?\s+(?:do|does|identif\w*|defin\w*|mean\w*|represent\w*|capture\w*))"
)

_VARIABLE_INDEX = "VARIABLE_INDEX.md"


class StructuredLookup:
    """Parse the KB once, then resolve queries to gold file paths to union-add."""

    # Cap on domain spec.md files union-added from one query, so a multi-domain
    # question (e.g. 4 domain codes) can't flood the merge and crowd out the
    # cosine hits that hold its other gold files.
    _MAX_DOMAIN_SPECS = 3

    def __init__(self, kb_root: Path):
        self.kb_root = kb_root
        # var -> [(codelist_name, ct_code, termfile_rel), ...]
        self.var_to_termfiles: dict[str, list[tuple[str, str, str]]] = defaultdict(list)
        # ct_code -> termfile_rel
        self.ctcode_to_termfile: dict[str, str] = {}
        # ct_code -> [domain.var, ...]  (from VARIABLE_INDEX §三)
        self.ctcode_to_vars: dict[str, list[str]] = {}
        # all variable names seen (for extracting query tokens)
        self.known_variables: set[str] = set()
        # var -> ct_code from each variable's own "### VAR" entry (cross-check source)
        self._var_to_ctcode: dict[str, str] = {}
        # domain code -> domains/<CODE>/spec.md (KB dir structure, data-driven)
        self.domain_to_spec: dict[str, str] = {}
        # lowercased domain long name -> code (from VARIABLE_INDEX §二 headings).
        # Lets a query that names a domain only by its long name ("Demographics
        # dataset") reach domains/<CODE>/spec.md, which the 2-letter-code path misses.
        self.domain_longname_to_code: dict[str, str] = {}
        # compiled longname matchers, longest name first (so "Exposure as
        # Collected" wins over "Exposure"); built after the maps are populated.
        self._longname_matchers: list[tuple[re.Pattern[str], str]] = []
        # var -> model/<file>.md whose variable-def table introduces it with a real
        # definition (non-empty Notes cell, single model file). The concept-definition
        # channel's gold map; see _build_model_defhome_index.
        self.var_to_model_defhome: dict[str, str] = {}
        # the general-assumptions chapter (ch04), home of generic '--'-prefix variable
        # definitions; None if absent. Used by the generic-var definition channel.
        self.general_assumptions_file: str | None = None

        self._build_domain_index()
        self._build_terminology_index()
        self._build_spec_index()
        self._build_variable_index()
        self._build_domain_longname_index()
        self._build_model_defhome_index()
        self._cross_check_vars()

    # ---- build phases -------------------------------------------------------

    def _build_domain_index(self) -> None:
        """Map every SDTM domain code to its spec.md from the KB directory layout
        (data-driven: any domains/<CODE>/spec.md, no hardcoded code list)."""
        domains_dir = self.kb_root / "domains"
        if not domains_dir.exists():
            return
        for d in sorted(domains_dir.iterdir()):
            spec = d / "spec.md"
            if d.is_dir() and spec.exists():
                self.domain_to_spec[d.name] = spec.relative_to(self.kb_root).as_posix()

    def _build_terminology_index(self) -> None:
        term_dir = self.kb_root / "terminology"
        if not term_dir.exists():
            return
        for f in sorted(term_dir.rglob("*.md")):
            rel = f.relative_to(self.kb_root).as_posix()
            for line in f.read_text(encoding="utf-8").splitlines():
                m = _TERM_HEADER_RE.match(line.strip())
                if m:
                    # first file wins; a CT code maps to one terminology file
                    self.ctcode_to_termfile.setdefault(m.group(1), rel)

    def _build_spec_index(self) -> None:
        domains_dir = self.kb_root / "domains"
        if not domains_dir.exists():
            return
        for f in sorted(domains_dir.rglob("spec.md")):
            text = f.read_text(encoding="utf-8")
            for raw in text.splitlines():
                line = raw.strip()
                # cross-reference block: var -> term file
                xm = _XREF_RE.match(line)
                if xm:
                    name, code, relpath, var_tail = xm.groups()
                    target = (f.parent / relpath).resolve()
                    try:
                        target_rel = target.relative_to(self.kb_root).as_posix()
                    except ValueError:
                        target_rel = None
                    if target_rel:
                        for tok in _QUERY_VAR_TOKEN_RE.findall(var_tail):
                            self.var_to_termfiles[tok].append(
                                (name.strip(), code, target_rel)
                            )
                    continue
                # known-variable vocabulary + its own CT code
                hm = _VAR_HEADER_RE.match(line)
                if hm:
                    self._current_var = hm.group(1)
                    self.known_variables.add(self._current_var)
                    continue
                cm = _CT_FIELD_RE.match(line)
                if cm and getattr(self, "_current_var", None):
                    self._var_to_ctcode[self._current_var] = cm.group(1)
            self._current_var = None

    def _build_variable_index(self) -> None:
        vidx_path = self.kb_root / _VARIABLE_INDEX
        if not vidx_path.exists():
            return
        section = 0  # 1=§一 general vars, 3=§三 CT cross-ref
        for raw in vidx_path.read_text(encoding="utf-8").splitlines():
            line = raw.rstrip()
            if line.startswith("## 一"):
                section = 1
                continue
            if line.startswith("## 二"):
                section = 2
                continue
            if line.startswith("## 三"):
                section = 3
                continue
            if section == 1:
                m = _GEN_VAR_ROW_RE.match(line)
                if m:
                    self.known_variables.add(m.group(1))
            elif section == 3:
                m = _SEC3_ROW_RE.match(line)
                if m:
                    code, vars_raw = m.groups()
                    self.ctcode_to_vars[code] = [
                        v.strip() for v in vars_raw.split(",") if v.strip()
                    ]

    def _build_domain_longname_index(self) -> None:
        """Map each domain long name -> code from VARIABLE_INDEX §二 headings
        ("### AE — Adverse Events (Events)"), then compile word-boundary matchers
        sorted longest-name-first so a query phrased only with the long name (e.g.
        "the Demographics dataset", no "DM" token) still resolves the spec.md.

        Data-driven: the map is parsed from the read-only KB, no hardcoded names.
        Conservative guards — a long name is only registered as a matcher when:
          * its code has a real domains/<CODE>/spec.md (skips placeholder rows like
            SUPPQUAL "Supplemental Qualifiers for [domain name]"), AND
          * the long name has no '[' placeholder.
        Matcher form depends on specificity:
          * multi-word names ("Adverse Events") and long single words >=10 chars
            ("Demographics") match bare, word-boundary;
          * short generic single words ("Exposure"=EX, "Comments"=CO — both 8
            chars) match ONLY when followed by an explicit dataset reference
            ("Exposure dataset", "Comments domain") so they cannot spuriously
            inject a spec from unrelated prose (e.g. the "Cumulative Exposure"
            test-name example in a Findings-About query — not followed by
            dataset/domain, no fire). "data" is deliberately NOT an anchor
            (too loose: "exposure data" occurs in generic prose).
        Slash-compound KB names ("Concomitant/Prior Medications") additionally
        register one variant per slash alternative ("Concomitant Medications",
        "Prior Medications") — the slash is KB notation, not user phrasing.
        Generic transformation over the KB-derived map; no hardcoded names.
        """
        vidx_path = self.kb_root / _VARIABLE_INDEX
        if not vidx_path.exists():
            return
        for raw in vidx_path.read_text(encoding="utf-8").splitlines():
            m = _DOMAIN_HEADER_RE.match(raw.strip())
            if not m:
                continue
            code, longname = m.group(1), m.group(2).strip()
            if code not in self.domain_to_spec:
                continue
            if "[" in longname:
                continue
            key = longname.lower()
            # first heading wins per long name (headings are unique anyway)
            self.domain_longname_to_code.setdefault(key, code)

        # slash-compound variants: for each name token containing "/", register
        # one variant per alternative (one slash token at a time; original full
        # names keep priority via setdefault)
        for longname, code in list(self.domain_longname_to_code.items()):
            if "/" not in longname:
                continue
            words = longname.split()
            for i, w in enumerate(words):
                if "/" not in w:
                    continue
                for alt in w.split("/"):
                    if not alt:
                        continue
                    variant = " ".join(words[:i] + [alt] + words[i + 1:])
                    self.domain_longname_to_code.setdefault(variant, code)

        matchers: list[tuple[str, re.Pattern[str], str]] = []
        for longname, code in self.domain_longname_to_code.items():
            words = longname.split()
            if len(words) < 2 and len(longname) < 10:
                # too-generic single short word -> anchored match only
                pattern = re.compile(
                    r"\b" + re.escape(longname) + r"\s+(?:dataset|domain)s?\b",
                    re.IGNORECASE,
                )
            else:
                pattern = re.compile(
                    r"\b" + re.escape(longname) + r"\b", re.IGNORECASE
                )
            matchers.append((longname, pattern, code))
        # longest long name first so "exposure as collected" beats "exposure"
        matchers.sort(key=lambda m: len(m[0]), reverse=True)
        self._longname_matchers = [(p, c) for (_n, p, c) in matchers]

    def _build_model_defhome_index(self) -> None:
        """Map each variable to its model/*.md DEFINITION HOME for the
        concept-definition channel.

        The KB has TWO variable-table shapes: the 6-column canonical *definition*
        table `| # | VAR | Label | Type | Role | Notes |` and a 5-column *usage*
        table `| # | VAR | Label | Type | Role |` (no Notes column). The
        `len(inner) == 6` filter is the LOAD-BEARING discriminator: it isolates the
        definition table from the usage tables. This matters because in a 5-column
        row the last cell is Role, not Notes — admitting 5-column rows would read
        "Record Qualifier" as a non-empty "Notes" and push a single-home variable to
        multiple files. Example: RDOMAIN has a 6-col definition row in model/06 AND a
        5-col usage row in model/03; keeping only 6-col rows leaves it single-home
        (model/06). The non-empty-Notes check is a secondary filter (skip the rare
        6-col row with a blank Notes cell = a bare entry, not a definition).
        Do NOT relax `len(inner) == 6` on the assumption it is arbitrary — doing so
        would re-admit the usage tables and silently drop RDOMAIN/EPOCH/ETCD/... to
        multi-file, un-fixing the channel.

        Conservative guards (keep the map a clean single-home, no ambiguity):
          * keep a variable only when its Notes-bearing 6-col rows are in EXACTLY ONE
            model file (drops cross-file vars like DOMAIN/USUBJID/POOLID);
          * exclude generic '--'-prefix vars (their home is the general-assumptions
            layer, not a single concept chapter — out of this channel's scope).
        Data-driven: parsed from the read-only KB, no hardcoded variable names. If a
        future KB rebuild changes the table layout the map goes empty and the channel
        degrades to [] (safe); pytest canaries assert RDOMAIN/EPOCH -> their files.

        Also discovers the general-assumptions chapter (ch04) here — it is the
        generic '--'-prefix variable definition channel's gold file (a sibling
        concept-definition source).
        """
        # generic '--' var definition home: ch04 General Assumptions (glob, not a
        # hardcoded filename, so a KB rename degrades gracefully to no-channel).
        chapters_dir = self.kb_root / "chapters"
        if chapters_dir.exists():
            for f in sorted(chapters_dir.glob("ch04*.md")):
                self.general_assumptions_file = f.relative_to(self.kb_root).as_posix()
                break

        model_dir = self.kb_root / "model"
        if not model_dir.exists():
            return
        tmp: dict[str, set[str]] = defaultdict(set)
        for f in sorted(model_dir.glob("*.md")):
            rel = f.relative_to(self.kb_root).as_posix()
            for raw in f.read_text(encoding="utf-8").splitlines():
                if "|" not in raw:
                    continue
                cells = [c.strip() for c in raw.split("|")]
                inner = cells[1:-1]  # drop the row's leading/trailing empty cells
                if len(inner) != 6:
                    continue  # load-bearing: isolates the 6-col definition table
                              # from the 5-col usage table (whose last cell is Role)
                num, var, _label, _type, _role, notes = inner
                if not num.isdigit():
                    continue
                if not re.fullmatch(r"(?:--)?[A-Z][A-Z0-9]*", var):
                    continue
                if not notes:  # no definition text -> bare usage row, skip
                    continue
                tmp[var].add(rel)
        self.var_to_model_defhome = {
            var: next(iter(files))
            for var, files in tmp.items()
            if len(files) == 1 and not var.startswith("--")
        }

    def _cross_check_vars(self) -> None:
        """Back-fill var->termfile from each variable's own CT code when the
        cross-reference block missed it (e.g. truncated "... (13 total)" tail).
        Uses _var_to_ctcode (from "### VAR" entries) + ctcode_to_termfile."""
        for var, code in self._var_to_ctcode.items():
            termfile = self.ctcode_to_termfile.get(code)
            if not termfile:
                continue
            existing = {(c, f) for (_n, c, f) in self.var_to_termfiles.get(var, [])}
            if (code, termfile) not in existing:
                self.var_to_termfiles[var].append((code, code, termfile))

    # ---- resolve ------------------------------------------------------------

    def _query_variables(self, query: str) -> list[str]:
        return [
            tok
            for tok in _QUERY_VAR_TOKEN_RE.findall(query)
            if tok in self.known_variables
        ]

    def _is_distribution_intent(self, query: str, ql: str) -> bool:
        """Generalized distribution detector -> VARIABLE_INDEX.md (no hardcoded
        variable names or question forms). Fires on either anchor:

          (A) variable-distribution: a known variable is named AND plural
              `domains` is mentioned AND a membership verb/qualifier fires.
          (B) codelist-sharing: a CT code (Cxxxx) is named AND a membership
              verb/qualifier fires (gold lives in VARIABLE_INDEX §三).
        """
        has_verb = any(kw in ql for kw in _DIST_VERB_KW)
        if not has_verb:
            return False
        # (A) variable X across domains
        if self._query_variables(query) and _DIST_DOMAINS_RE.search(query):
            return True
        # (B) which domains share codelist Cxxxx
        return bool(_QUERY_CT_RE.search(query))

    def _query_longname_domains(self, query: str) -> list[str]:
        """Domain codes whose *full long name* appears in the query (word-boundary,
        case-insensitive), longest name first, de-duped. Catches queries that name
        a domain only by its long name ("the Demographics dataset") with no
        2-letter code token. Conservative: generic short single-word names only
        match with a dataset/domain anchor (see `_build_domain_longname_index`)."""
        out: list[str] = []
        for pattern, code in self._longname_matchers:
            if code not in out and pattern.search(query):
                out.append(code)
        return out

    def _query_domains(self, query: str) -> list[str]:
        """Known SDTM domain codes referenced by the query, de-duped. Code tokens
        first (`RELSPEC`, `TR`, `SV`, ... — KB-derived, not hardcoded), then any
        domain named only by its long name (union-add, code-token matches win on
        order). All KB-derived, no hardcoded names."""
        out: list[str] = []
        for tok in _QUERY_VAR_TOKEN_RE.findall(query):
            if tok in self.domain_to_spec and tok not in out:
                out.append(tok)
        for code in self._query_longname_domains(query):
            if code not in out:
                out.append(code)
        return out

    def _query_concept_definition(self, query: str) -> list[str]:
        """Model definition-home file(s) for a variable asked about with a strict
        definitional-verb shape (_DEFVERB_RE). Returns [] unless the query matches
        that shape AND the captured variable is in the model def-home map — so a
        distribution/attribute ask that merely names the variable never fires."""
        out: list[str] = []
        for m in _DEFVERB_RE.finditer(query):
            var = m.group(1).upper()
            f = self.var_to_model_defhome.get(var)
            if f and f not in out:
                out.append(f)
        return out

    def _query_generic_var_definition(self, query: str, dist_intent: bool) -> list[str]:
        """The general-assumptions chapter (ch04) for a definition/comparison ask
        about a generic '--'-prefix variable. Returns [] unless: ch04 exists, the
        query is NOT a distribution ask (those route to VARIABLE_INDEX), and the query
        either compares >= 2 '--' tokens ("difference between --X and --Y") or asks the
        definitional-verb shape on a '--' token ("what does --DUR represent"). Keys on
        the '--' convention, not on any specific variable."""
        if not self.general_assumptions_file or dist_intent:
            return []
        dashvars = _DASHVAR_RE.findall(query)
        if not dashvars:
            return []
        # compare branch counts DISTINCT generic vars (so a repeated token can't
        # satisfy ">= 2 vars being compared")
        two_var_compare = _COMPARE_RE.search(query) and len(set(dashvars)) >= 2
        if two_var_compare or _DASH_DEFVERB_RE.search(query):
            return [self.general_assumptions_file]
        return []

    def resolve(self, query: str) -> list[str]:
        """Return KB-relative gold file paths to union-add, or [] when no intent
        keyword fires (conservative: fall back to plain cosine, never guess)."""
        ql = query.lower()
        term_intent = any(kw in ql for kw in _TERM_INTENT_KW)
        dist_intent = self._is_distribution_intent(query, ql)
        named_domains = self._query_domains(query)
        concept_defs = self._query_concept_definition(query)
        generic_defs = self._query_generic_var_definition(query, dist_intent)
        if (not term_intent and not dist_intent and not named_domains
                and not concept_defs and not generic_defs):
            return []

        targets: list[str] = []

        # Distribution intent -> VARIABLE_INDEX.md (which-domains / share-codelist).
        # Checked first so a "share codelist Cxxxx" query (which also trips term
        # keywords) routes to the index, where its gold actually lives.
        if dist_intent:
            targets.append(_VARIABLE_INDEX)

        # Named-domain intent -> that domain's spec.md. The domain *code* (e.g.
        # RELSPEC) frequently does not appear in its own spec chunks (they are
        # per-variable rows), so neither cosine nor BM25 can reach it; the KB dir
        # structure maps it deterministically. Capped at _MAX_DOMAIN_SPECS so a
        # 4-domain query can't flood the union-add and crowd real cosine hits.
        for dom in named_domains[: self._MAX_DOMAIN_SPECS]:
            targets.append(self.domain_to_spec[dom])

        # Terminology intent -> the codelist's terminology file.
        if term_intent:
            for var in self._query_variables(query):
                for (_name, _code, termfile) in self.var_to_termfiles.get(var, []):
                    targets.append(termfile)
            for code in _QUERY_CT_RE.findall(query):
                termfile = self.ctcode_to_termfile.get(code)
                if termfile:
                    targets.append(termfile)

        # Concept-definition intent -> the variable's model definition-home file.
        # Union-added last (recall-additive tail); strict _DEFVERB_RE gate keeps it
        # off distribution/attribute questions that name the same variable.
        targets.extend(concept_defs)

        # Generic '--' var definition/comparison intent -> ch04 general assumptions.
        targets.extend(generic_defs)

        # de-dupe, preserve order
        seen: set[str] = set()
        ordered: list[str] = []
        for t in targets:
            if t not in seen:
                seen.add(t)
                ordered.append(t)
        return ordered
