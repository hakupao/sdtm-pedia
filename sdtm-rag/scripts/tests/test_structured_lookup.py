"""Unit tests for server/structured_lookup.py (S1 + S3 levers).

First test coverage for this module (added with the 2026-06-12 pattern fixes).
Covers: pre-existing behaviors (locked), plus the three v3-driven fixes:
  (a) distribution anchor accepts "datasets" as synonym of "domains"
  (b) slash-compound long names register per-alternative variants
  (c) short single-word long names match only with a dataset/domain anchor
"""
from __future__ import annotations

from pathlib import Path

import pytest

from server.config import settings
from server.meta_store import MetaStore
from server.structured_lookup import StructuredLookup

KB_ROOT = Path(__file__).resolve().parents[3] / "knowledge_base"


@pytest.fixture(scope="module")
def lookup() -> StructuredLookup:
    return StructuredLookup(KB_ROOT, MetaStore(settings.meta_path))


# ---- pre-existing behaviors (locked) ----------------------------------------

class TestExistingBehavior:
    def test_code_token_resolves_spec(self, lookup):
        assert "domains/DM/spec.md" in lookup.resolve(
            "What are the required variables in the DM domain?"
        )

    def test_multiword_longname_bare_match(self, lookup):
        assert "domains/VS/spec.md" in lookup.resolve(
            "What is the structure of the Vital Signs dataset?"
        )

    def test_long_single_word_bare_match(self, lookup):
        assert "domains/DM/spec.md" in lookup.resolve(
            "How is the Demographics dataset structured?"
        )

    def test_dist_intent_domains_routes_variable_index(self, lookup):
        assert "VARIABLE_INDEX.md" in lookup.resolve(
            "Which SDTM domains include the VISITNUM timing variable?"
        )

    def test_no_intent_returns_empty(self, lookup):
        assert lookup.resolve("How should missing values be represented?") == []


# ---- fix (a): "datasets" synonym in distribution anchor ----------------------

class TestDatasetsSynonym:
    def test_datasets_with_known_variable_fires(self, lookup):
        # v3 q107 shape: "datasets" instead of "domains"
        assert "VARIABLE_INDEX.md" in lookup.resolve(
            "Which SDTM datasets carry both the ARM and ARMCD variables, "
            "and what are the labels of these two variables?"
        )

    def test_datasets_generalizes_beyond_q107(self, lookup):
        # out-of-set probe: different variable, different phrasing
        assert "VARIABLE_INDEX.md" in lookup.resolve(
            "Which datasets include the SITEID variable?"
        )

    def test_datasets_without_known_variable_does_not_fire(self, lookup):
        # double-anchor: no known variable, no CT code -> no dist route
        assert "VARIABLE_INDEX.md" not in lookup.resolve(
            "What datasets exist in the SDTM standard?"
        )

    def test_datasets_synonym_is_recall_additive(self, lookup):
        # Rule-D review MED-2 probe: a var+datasets+verb query that also names a
        # domain must still surface the domain spec — the dist injection is
        # union-add, never a replacement
        targets = lookup.resolve(
            "What datasets include the AGE variable in Demographics?"
        )
        assert "domains/DM/spec.md" in targets


# ---- fix (b): slash-compound long-name variants ------------------------------

class TestSlashVariants:
    def test_concomitant_medications_variant(self, lookup):
        # v3 q134 shape: natural phrasing of "Concomitant/Prior Medications"
        assert "domains/CM/spec.md" in lookup.resolve(
            "In the Concomitant Medications dataset, what does each row "
            "correspond to?"
        )

    def test_prior_medications_variant(self, lookup):
        # out-of-set probe: the other slash alternative
        assert "domains/CM/spec.md" in lookup.resolve(
            "What goes into the Prior Medications dataset?"
        )

    def test_tumor_identification_variant(self, lookup):
        assert "domains/TU/spec.md" in lookup.resolve(
            "How granular is each record in the Tumor Identification dataset?"
        )

    def test_lesion_results_variant(self, lookup):
        assert "domains/TR/spec.md" in lookup.resolve(
            "What does the Lesion Results dataset capture?"
        )

    def test_full_slash_name_still_matches(self, lookup):
        assert "domains/TU/spec.md" in lookup.resolve(
            "Describe the Tumor/Lesion Identification dataset."
        )


# ---- fix (c): anchored short single-word long names ---------------------------

class TestAnchoredShortNames:
    def test_exposure_dataset_fires(self, lookup):
        # v3 q139 shape
        assert "domains/EX/spec.md" in lookup.resolve(
            "When dosing data goes into the Exposure dataset, what does a "
            "single record cover?"
        )

    def test_comments_dataset_fires(self, lookup):
        # v3 q140 shape
        assert "domains/CO/spec.md" in lookup.resolve(
            "In the Comments dataset, what does each record correspond to?"
        )

    def test_comments_domain_anchor_fires(self, lookup):
        # out-of-set probe: "domain" anchor
        assert "domains/CO/spec.md" in lookup.resolve(
            "Which class does the Comments domain belong to?"
        )

    def test_bare_exposure_in_prose_does_not_fire(self, lookup):
        # v2 q96 collision case: "Cumulative Exposure" is a FATEST test name
        targets = lookup.resolve(
            "In the FA (Findings About) domain, what is the FATEST variable "
            "and its controlled terminology codelist code, and give some "
            "example test names from that codelist (such as Diameter or "
            "Cumulative Exposure)?"
        )
        assert "domains/EX/spec.md" not in targets

    def test_bare_exposure_generic_prose_does_not_fire(self, lookup):
        assert "domains/EX/spec.md" not in lookup.resolve(
            "Several subjects had high exposure recorded during the study."
        )

    def test_exposure_as_collected_not_shadowed(self, lookup):
        # "Exposure as Collected dataset": EC's full name matches; the anchored
        # "Exposure dataset" pattern must NOT fire ("exposure" followed by "as")
        targets = lookup.resolve(
            "What is the structure of the Exposure as Collected dataset?"
        )
        assert "domains/EC/spec.md" in targets
        assert "domains/EX/spec.md" not in targets


# ---- map hygiene --------------------------------------------------------------

class TestLongnameMapHygiene:
    def test_no_placeholder_keys(self, lookup):
        assert not [k for k in lookup.domain_longname_to_code if "[" in k]

    def test_variants_registered_for_all_slash_names(self, lookup):
        # every slash name with a real spec must have produced >=2 variants
        slash_names = [
            k for k in lookup.domain_longname_to_code if "/" in k
        ]
        assert slash_names, "expected slash-compound long names in KB"
        # Rule-D review MED-1 guard: the variant loop resolves ONE slash token
        # per variant; a future KB name with two slash tokens would register
        # half-resolved variants silently. Fail loudly here instead.
        multi_slash = [
            n for n in slash_names
            if sum(1 for w in n.split() if "/" in w) > 1
        ]
        assert not multi_slash, (
            f"multi-slash-token long names need cartesian variants: {multi_slash}"
        )
        for name in slash_names:
            code = lookup.domain_longname_to_code[name]
            words = name.split()
            for i, w in enumerate(words):
                if "/" not in w:
                    continue
                for alt in w.split("/"):
                    variant = " ".join(words[:i] + [alt] + words[i + 1:])
                    assert lookup.domain_longname_to_code.get(variant) == code


# ---- (d) concept-definition -> model channel (2026-06-15) --------------------

class TestConceptDefinitionChannel:
    """Variable asked about with a strict definitional-verb shape routes to its
    model/*.md definition-home file. Pattern-level (59-var def-home map), gated so
    it never fires on distribution/attribute/terminology asks naming the same var."""

    def test_defhome_canary_rdomain(self, lookup):
        # Canary (risk note): if a KB rebuild breaks the 6-col table parse, the map
        # goes empty and this fails loudly rather than silently regressing q73/q83.
        assert lookup.var_to_model_defhome.get("RDOMAIN") == \
            "model/06_relationship_datasets.md"

    def test_defhome_canary_epoch_six_col_isolation(self, lookup):
        # Second canary (Rule D LOW): EPOCH, like RDOMAIN, has a 6-col definition row
        # (model/03) AND a competing 5-col usage row elsewhere; it stays single-home
        # ONLY because the len==6 filter excludes the usage table. Guards the 6-col
        # isolation invariant beyond RDOMAIN alone.
        assert lookup.var_to_model_defhome.get("EPOCH") == \
            "model/03_special_purpose_domains.md"

    def test_defhome_map_hygiene(self, lookup):
        m = lookup.var_to_model_defhome
        assert len(m) >= 50, "def-home map unexpectedly small (KB parse drift?)"
        # every value is a model/*.md file
        assert all(v.startswith("model/") and v.endswith(".md") for v in m.values())
        # conservative guards: no generic '--' vars; cross-file ambiguous vars dropped
        assert not any(k.startswith("--") for k in m)
        for ambiguous in ("DOMAIN", "USUBJID", "POOLID"):
            assert ambiguous not in m, f"{ambiguous} has Notes in >1 model file -> must be dropped"

    def test_q73_union_adds_model_defhome(self, lookup):
        # q73 also trips the distribution anchor (-> VARIABLE_INDEX); the new channel
        # must UNION-ADD model/06, not replace.
        out = lookup.resolve(
            "Which special-purpose and relationship domains carry the RDOMAIN "
            "variable, and what does RDOMAIN identify?"
        )
        assert "model/06_relationship_datasets.md" in out
        assert "VARIABLE_INDEX.md" in out  # pre-existing distribution route preserved

    def test_fires_on_definitional_verbs(self, lookup):
        # held-out generalization (NOT in the test set): different vars, different
        # verb stems, all resolve to the correct model definition home.
        assert lookup._query_concept_definition(
            "What does RELTYPE identify in a RELREC relationship?"
        ) == ["model/06_relationship_datasets.md"]
        assert lookup._query_concept_definition(
            "What does the QNAM variable represent?"
        ) == ["model/06_relationship_datasets.md"]
        assert lookup._query_concept_definition(
            "What does ETCD identify in trial design?"
        ) == ["model/03_special_purpose_domains.md"]

    def test_silent_on_distribution_attribute_terminology(self, lookup):
        # must-NOT-fire: the strict verb gate keeps the channel off questions that
        # name a def-home variable but ask a non-definition question.
        for q in (
            "Which SDTM domains carry the ARMCD variable and what are their labels?",  # distribution
            "In the DM domain what is the RACE variable Core designation?",            # attribute
            "What controlled terminology codelist does the SEX variable use?",         # terminology ('use' not a def verb)
            "What is the difference between RFSTDTC and RFENDTC?",                      # comparison
            "What is EPOCH used for across domains?",                                  # 'used for' not a def verb
        ):
            assert lookup._query_concept_definition(q) == [], f"should not fire: {q}"

    def test_bare_mention_does_not_fire(self, lookup):
        # mere variable mention without the definitional-verb shape -> no fire
        assert lookup._query_concept_definition(
            "RDOMAIN appears in supplemental qualifier datasets."
        ) == []

    def test_lowercase_var_token_not_captured(self, lookup):
        # the <VAR> group is case-sensitive (uppercase only), so a lowercase common
        # word inside the verb frame cannot be captured as a variable.
        assert lookup._query_concept_definition(
            "what does the system mean for a sponsor?"
        ) == []


# ---- (d) generic '--' var definition -> ch04 channel (2026-06-15) ------------

class TestGenericVarDefinitionChannel:
    """A definition/comparison ask about a generic '--'-prefix variable routes to
    ch04 General Assumptions (the SDTM home of cross-domain variable conventions).
    Pattern-level (keys on the '--' convention + def/comparison intent), gated off
    distribution ('which domains use --STAT') and usage ('use --SEQ as join key')."""

    def _gd(self, lookup, q):
        return lookup._query_generic_var_definition(
            q, lookup._is_distribution_intent(q, q.lower())
        )

    def test_ch04_discovered(self, lookup):
        assert lookup.general_assumptions_file == "chapters/ch04_general_assumptions.md"

    def test_q119_union_adds_ch04(self, lookup):
        # q119 already trips named-domain (RELREC/TU/TR); ch04 must union-add, not replace.
        out = lookup.resolve(
            "We need a dataset-to-dataset link between our tumor identification records "
            "and tumor results records. What exactly is the difference between the "
            "--LNKID and --LNKGRP variables, and how do they typically come into play "
            "in RELREC?"
        )
        assert "chapters/ch04_general_assumptions.md" in out

    def test_comparison_of_two_dash_vars_fires(self, lookup):
        # held-out generalization: any two-generic-var comparison -> ch04
        assert self._gd(
            lookup, "What is the difference between the --STDTC and --ENDTC variables?"
        ) == ["chapters/ch04_general_assumptions.md"]

    def test_single_dash_var_definitional_verb_fires(self, lookup):
        # held-out generalization: single-var definitional ask -> ch04
        assert self._gd(lookup, "What does the --DUR variable represent?") == \
            ["chapters/ch04_general_assumptions.md"]

    def test_silent_on_distribution_usage_and_non_dash(self, lookup):
        for q in (
            "Which domains use the --STAT variable?",                  # distribution -> VARIABLE_INDEX
            "Is it acceptable to use --SEQ as the join key in RELREC?",  # usage -> ch08
            "What is the difference between the AE and CE domains?",     # comparison but no '--' token
            "How should I populate --DTC for partial dates?",           # usage, no def/comparison verb
        ):
            assert self._gd(lookup, q) == [], f"should not fire: {q}"

    def test_compare_needs_two_dash_tokens(self, lookup):
        # 'difference between' with only ONE '--' token does not fire the compare
        # branch (avoids "difference between --SEQ and the visit number" type asks).
        assert self._gd(
            lookup, "What is the difference between --SEQ and the record sequence?"
        ) == []


# ---- meta.yaml <-> KB drift guard (SP2 Phase 2, Rule-D LOW) -------------------

class TestMetaKBDriftGuard:
    """The meta.yaml-backed lookup no longer self-heals from KB edits (the old regex code
    re-parsed KB markdown live). Guard against SILENT meta.yaml<->KB drift: a KB rebuild
    that adds/removes a domain without regenerating meta.yaml must fail HERE, not silently
    degrade retrieval. Full var/CT reconciliation lives in scripts/reconcile_meta.py — run
    it after any KB rebuild; this is the cheap always-on canary."""

    def test_domain_specs_exist_on_disk(self, lookup):
        for code, rel in lookup.domain_to_spec.items():
            assert (KB_ROOT / rel).exists(), f"{code} -> {rel} missing on disk (meta/KB drift)"

    def test_domain_count_matches_kb(self, lookup):
        on_disk = sum(
            1 for d in (KB_ROOT / "domains").iterdir() if (d / "spec.md").exists()
        )
        assert len(lookup.domain_to_spec) == on_disk, (
            "meta.yaml domain count != domains/*/spec.md on disk — regenerate meta.yaml "
            "(scripts/build_meta.py) then scripts/reconcile_meta.py"
        )

    def test_general_assumptions_file_exists(self, lookup):
        assert lookup.general_assumptions_file is not None
        assert (KB_ROOT / lookup.general_assumptions_file).exists()


# ---- VI 锚点抽取 (S1 字面 section 定位) --------------------------------------

class TestVariableIndexAnchors:
    def test_ct_code_anchor(self, lookup):
        assert lookup.variable_index_anchors(
            "Which domains use codelist C99073 for laterality?"
        ) == ["C99073"]

    def test_variable_anchor(self, lookup):
        assert lookup.variable_index_anchors(
            "In how many domains does TAETORD appear?"
        ) == ["TAETORD"]

    def test_ct_codes_come_before_variables(self, lookup):
        # 混合题: CT 码是更具体的锚点, 必须排在变量前 (否则 3 个名额可能被变量占满)
        out = lookup.variable_index_anchors(
            "Which domains share codelist C66742 through the RDOMAIN variable?"
        )
        assert out[0] == "C66742"
        assert "RDOMAIN" in out

    def test_two_variable_anchors_preserved(self, lookup):
        # q107 形态: 一题要两节 (ARM + ARMCD), 这正是"1 文件只注 1 块"限制的解除点
        out = lookup.variable_index_anchors("What are the labels of ARM and ARMCD?")
        assert "ARM" in out and "ARMCD" in out

    def test_dedup_preserves_order(self, lookup):
        assert lookup.variable_index_anchors(
            "codelist C66742 and again C66742"
        ) == ["C66742"]

    def test_not_capped_here(self, lookup):
        # 上限施加在 RAGEngine 侧 (section 解析之后)。若在这里先截, 没有 VI 条目的
        # 变量会白占名额, 把真能解出 section 的锚点挤掉 —— 规则 A 抽检 D-1。
        out = lookup.variable_index_anchors(
            "codelists C66742, C66734, C99073, C78735 and C71620"
        )
        assert out == ["C66742", "C66734", "C99073", "C78735", "C71620"]

    def test_no_anchor_returns_empty(self, lookup):
        assert lookup.variable_index_anchors("What is an SDTM domain?") == []

    def test_unknown_variable_token_is_not_an_anchor(self, lookup):
        # 未知大写 token 不是变量 → 不得当锚点 (否则会去查一个不存在的 section)
        assert lookup.variable_index_anchors("What does ZZZQQQ mean?") == []


class TestAnchoredLowercaseCodes:
    """DM1 D1: 2-8 letter codes in any case count as domain references when a
    domain word follows them or sdtm/cdisc precedes them. Unanchored lowercase
    never matches (English words like 'is'/'or' collide with real codes IS/OR)."""

    @pytest.mark.parametrize("q,code", [
        ("本研究中，哪些数据适合进入 sdtm 的 ds domain？", "DS"),
        ("DS域にはどんなデータが入りますか", "DS"),
        ("aeドメインに入る項目は？", "AE"),
        ("what goes into the dm dataset for our study", "DM"),
        ("SDTM的lb域应该包含本研究哪些数据", "LB"),
    ])
    def test_anchored_code_resolves(self, lookup, q, code):
        assert code in lookup._query_domains(q)
        assert f"domains/{code}/spec.md" in lookup.resolve(q)

    @pytest.mark.parametrize("q", [
        "is the dataset required?",          # 'is' collides with IS
        "or the domain must be listed",      # 'or' collides with OR
        "ds without any anchor word",
    ])
    def test_unanchored_or_stopword_code_does_not_resolve(self, lookup, q):
        assert not any(c in ("IS", "OR", "DS") for c in lookup._query_domains(q))

    def test_uppercase_behaviour_unchanged(self, lookup):
        assert lookup._query_domains("What are the required variables in the DM domain?") == ["DM"]
