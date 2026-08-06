"""S1: deterministic structured-lookup retrieval lever (meta.yaml-backed).

Three query classes that cosine + BM25 both miss, but whose answer lives in the KB
as structured data:

  (1) terminology / CT-code queries (e.g. "values allowed for AESEV", "codelist
      code for VSTESTCD"). The gold is a terminology file whose heading is the CT
      *code* (e.g. "C66769"); the variable name never appears in it, so embeddings
      and lexical search both fail. The variable -> (codelist name, CT code,
      terminology file) mapping is deterministic.

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

`StructuredLookup` builds its indices ONCE at engine init and exposes `resolve(query)`
returning the *gold file paths* (relative to KB root) that should be union-added into
the retrieval result. It is conservative: when no intent keyword matches, it returns
`[]` and the caller falls back to plain cosine.

DATA SOURCE (SP2 Phase 2): all of the resolution maps are derived from
`data/meta/meta.yaml` via the injected `MetaStore` — the deterministic SP1 metadata
layer that was independently reconciled against the KB. This RETIRES the previous
regex "shadow KG" that re-parsed KB markdown at init (the load-bearing `len(inner)==6`
model-table parse, the spec.md "Cross References" parse, the terminology-header parse,
the VARIABLE_INDEX parse, and the truncation back-fill). The query-parsing regex
(intent cues, variable/CT tokens, definitional-verb shapes) and the resolve()/longname
matcher logic are UNCHANGED — only where the maps come from changed. The ONLY index
still read from KB files is the ch04 general-assumptions glob (3b), which meta.yaml
does not cover.

Migration is behaviour-equivalent: every map reproduces the old regex output exactly
(verified by eval/prod_wirein/sp2p2_equiv_snapshot.py — 8 maps + 9891 resolve() outputs
byte-identical) and the full test_structured_lookup.py suite stays green.
"""
from __future__ import annotations

import re
from collections import defaultdict
from pathlib import Path

from server.meta_store import MetaStore

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
    """Build resolution maps from the MetaStore once, then resolve queries to gold
    file paths to union-add."""

    # Cap on domain spec.md files union-added from one query, so a multi-domain
    # question (e.g. 4 domain codes) can't flood the merge and crowd out the
    # cosine hits that hold its other gold files.
    _MAX_DOMAIN_SPECS = 3

    def __init__(self, kb_root: Path, store: MetaStore):
        self.kb_root = kb_root
        self.store = store

        # var -> [(codelist_name, ct_code, termfile_rel), ...]
        self.var_to_termfiles: dict[str, list[tuple[str, str, str]]] = defaultdict(list)
        # ct_code -> termfile_rel
        self.ctcode_to_termfile: dict[str, str] = {}
        # all variable names (for extracting query tokens)
        self.known_variables: set[str] = set(store.known_variables)
        # domain code -> domains/<CODE>/spec.md (every counts_toward_63 domain has one)
        self.domain_to_spec: dict[str, str] = {}
        # lowercased domain long name -> code (from meta.yaml labels).
        # Lets a query that names a domain only by its long name ("Demographics
        # dataset") reach domains/<CODE>/spec.md, which the 2-letter-code path misses.
        self.domain_longname_to_code: dict[str, str] = {}
        # compiled longname matchers, longest name first (so "Exposure as
        # Collected" wins over "Exposure"); built after the maps are populated.
        self._longname_matchers: list[tuple[re.Pattern[str], str]] = []
        # var -> model/<file>.md whose variable-def table introduces it with a real
        # definition (single model file). The concept-definition channel's gold map.
        self.var_to_model_defhome: dict[str, str] = dict(store.model_defhome_map)
        # the general-assumptions chapter (ch04), home of generic '--'-prefix variable
        # definitions; None if absent. Used by the generic-var definition channel.
        self.general_assumptions_file: str | None = None

        self._build_domain_index()
        self._build_terminology_index()
        self._build_var_termfile_index()
        self._build_domain_longname_index()
        self._discover_general_assumptions()

    # ---- build phases (all meta.yaml-backed except the ch04 glob) ------------

    def _build_domain_index(self) -> None:
        """Map every counts_toward_63 domain code to its spec.md. Each such domain
        has a domains/<CODE>/spec.md by construction (SP1: counts_toward_63 == spec.md
        exists), so the path is deterministic from the code — no directory scan."""
        for dom in sorted(self.store.known_domains):
            self.domain_to_spec[dom] = f"domains/{dom}/spec.md"

    def _build_terminology_index(self) -> None:
        """ct_code -> terminology file, straight from the codelist records."""
        for code in self.store.known_ctcodes:
            cl = self.store.codelist(code)
            if cl and cl.get("termfile"):
                self.ctcode_to_termfile[code] = cl["termfile"]

    def _build_var_termfile_index(self) -> None:
        """var -> [(codelist_name, ct_code, termfile), ...] from the UNION of each
        variable's CT codes across all domains (MetaStore.ct_codes_for_variable) joined
        to the codelist termfile. The union (not first-seen) is required for the few
        variables whose CT is domain-specific (e.g. FOCID -> C119013 only in OE) —
        matching the old spec.md cross-reference + back-fill behaviour exactly.

        NOTE: only the termfile (3rd) element is observable downstream — resolve() reads
        only termfile. The name/code fields are kept for parity/debuggability and are NOT
        equivalence-load-bearing (the old back-fill path put the code in the name slot)."""
        for var in self.store.known_variables:
            for code in self.store.ct_codes_for_variable(var):
                cl = self.store.codelist(code)
                if cl and cl.get("termfile"):
                    self.var_to_termfiles[var].append((cl["name"], code, cl["termfile"]))

    def _build_domain_longname_index(self) -> None:
        """Map each domain long name -> code from meta.yaml labels, then compile
        word-boundary matchers sorted longest-name-first so a query phrased only with
        the long name (e.g. "the Demographics dataset", no "DM" token) still resolves
        the spec.md.

        Data-driven from meta.yaml (SP1, independently reconciled); the transformation
        is identical to the previous VARIABLE_INDEX-heading parse, only the source of
        the (code, longname) pairs changed.
        Conservative guards — a long name is only registered as a matcher when:
          * its code has a real domains/<CODE>/spec.md (always true for the 63), AND
          * the long name has no '[' placeholder (skips SUPPQUAL's
            "Supplemental Qualifiers for [domain name]").
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
        Generic transformation over the meta-derived map; no hardcoded names.
        """
        for dom in sorted(self.store.known_domains):
            info = self.store.domain_info(dom)
            if info is None:
                continue
            longname = info["label"]
            if dom not in self.domain_to_spec:
                continue
            if "[" in longname:
                continue
            key = longname.lower()
            # first registration wins per long name (labels are unique anyway)
            self.domain_longname_to_code.setdefault(key, dom)

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

    def _discover_general_assumptions(self) -> None:
        """Discover the ch04 general-assumptions chapter — the generic '--'-prefix
        variable definition channel's gold file (3b). This is the ONLY index still read
        from KB files: meta.yaml does not cover chapters/, so the ch04 glob is retained
        (a KB rename degrades gracefully to no-channel)."""
        chapters_dir = self.kb_root / "chapters"
        if chapters_dir.exists():
            for f in sorted(chapters_dir.glob("ch04*.md")):
                self.general_assumptions_file = f.relative_to(self.kb_root).as_posix()
                break

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
        first (`RELSPEC`, `TR`, `SV`, ... — meta-derived, not hardcoded), then any
        domain named only by its long name (union-add, code-token matches win on
        order). All meta-derived, no hardcoded names."""
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

    def variable_index_anchors(self, query: str) -> list[str]:
        """VARIABLE_INDEX 内部定位用的**字面锚点候选** (CT 码 + 已知变量名), CT 码在前,
        去重保序, **不截断**。

        返回 token 而非 section 串: section 的命名格式只有索引自己知道, 在这里拼格式串
        等于把同一份格式定义写两遍 (chunker 改名时会静默全 miss)。映射交给 RAGEngine
        从索引反建。无锚点时返回 [] → 调用方回落 cosine 选块。

        **这里不截断是有意的** (规则 A 抽检 D-1): known_variables 有 ~1500 个变量, 而
        VI §一 只有 24 个有 section。若在这里先截前 3, 一个被题面顺带提到、却没有 VI
        条目的变量会白占名额, 把真正能解出 section 的锚点挤出去 —— 实证: q107 题面加一
        句 "our EXDOSU and CMDOSU mappings aside" 就会把 ARMCD 挤掉。哪些锚点真能解出
        section 只有索引侧知道, 故上限 (RAGEngine._MAX_VI_SECTIONS) 在解析之后才施加。"""
        anchors: list[str] = []
        for tok in _QUERY_CT_RE.findall(query) + self._query_variables(query):
            if tok not in anchors:
                anchors.append(tok)
        return anchors

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
        # per-variable rows), so neither cosine nor BM25 can reach it; meta.yaml
        # maps it deterministically. Capped at _MAX_DOMAIN_SPECS so a 4-domain
        # query can't flood the union-add and crowd real cosine hits.
        for dom in named_domains[: self._MAX_DOMAIN_SPECS]:
            targets.append(self.domain_to_spec[dom])

        # Terminology intent -> the codelist's terminology file.
        if term_intent:
            for var in self._query_variables(query):
                for (_name, _code, termfile) in self.var_to_termfiles.get(var, []):
                    targets.append(termfile)
            for code in _QUERY_CT_RE.findall(query):
                ct_termfile = self.ctcode_to_termfile.get(code)
                if ct_termfile:
                    targets.append(ct_termfile)

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
