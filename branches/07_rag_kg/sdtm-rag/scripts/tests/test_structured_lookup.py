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

from server.structured_lookup import StructuredLookup

KB_ROOT = Path(__file__).resolve().parents[5] / "knowledge_base"


@pytest.fixture(scope="module")
def lookup() -> StructuredLookup:
    return StructuredLookup(KB_ROOT)


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
