import importlib.util
import json
import tempfile
import textwrap
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
SCRIPTS_DIR = REPO_ROOT / ".codex" / "scripts"


def load_script_module(module_name: str):
    path = SCRIPTS_DIR / f"{module_name}.py"
    spec = importlib.util.spec_from_file_location(module_name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class TerminologyValidationTests(unittest.TestCase):
    def test_parse_terminology_markdown_file_extracts_codelists_and_terms(self):
        module = load_script_module("validate_terminology")
        sample = textwrap.dedent(
            """\
            # Sample Codelists

            > Sample description.

            ## Action Taken with Study Treatment (C66767)

            Extensible: No

            | Code | CDISC Submission Value | CDISC Synonym(s) | CDISC Definition |
            |------|------------------------|------------------|------------------|
            | C49503 | DOSE INCREASED |  | Dose increased. |
            | C49504 | DOSE NOT CHANGED |  | Dose not changed. |
            """
        )
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "ae.md"
            path.write_text(sample, encoding="utf-8")
            parsed = module.parse_terminology_markdown_file(path)

        self.assertIn("C66767", parsed)
        self.assertEqual(parsed["C66767"]["name"], "Action Taken with Study Treatment")
        self.assertEqual(parsed["C66767"]["extensible"], "No")
        self.assertEqual(len(parsed["C66767"]["terms"]), 2)
        self.assertEqual(parsed["C66767"]["terms"][0]["code"], "C49503")

    def test_compare_codelists_reports_missing_and_field_mismatches(self):
        module = load_script_module("validate_terminology")
        expected = {
            "C111": {
                "name": "Example List",
                "extensible": "No",
                "terms": [
                    {
                        "code": "C1",
                        "submission_value": "YES",
                        "synonym": "",
                        "definition": "Positive.",
                    }
                ],
            }
        }
        actual = {
            "C111": {
                "name": "Example List",
                "extensible": "Yes",
                "terms": [
                    {
                        "code": "C1",
                        "submission_value": "YES",
                        "synonym": "",
                        "definition": "Positive.",
                    }
                ],
            }
        }
        result = module.compare_codelists(expected, actual)
        self.assertEqual(result["summary"]["expected_codelists"], 1)
        self.assertEqual(len(result["errors"]), 1)
        self.assertIn("extensible mismatch", result["errors"][0])


class PageIndexValidationTests(unittest.TestCase):
    def test_validate_page_index_data_accepts_shared_example_ranges(self):
        module = load_script_module("validate_page_index")
        data = {
            "_meta": {"source": "x.pdf", "total_pages": 10},
            "chapters": {},
            "shared_specs": {},
            "model": {"source": "y.pdf", "total_pages": 1, "files": {}},
            "domains": {
                "EX": {
                    "section": [1, 4],
                    "spec": [1, 2],
                    "assumptions": [2, 3],
                    "examples": [5, 6],
                },
                "EC": {
                    "section": [4, 5],
                    "spec": [4, 4],
                    "assumptions": [4, 5],
                    "examples": [5, 6],
                },
            },
        }
        result = module.validate_page_index_data(data)
        self.assertEqual(result["errors"], [])

    def test_validate_page_index_data_rejects_invalid_range_order(self):
        module = load_script_module("validate_page_index")
        data = {
            "_meta": {"source": "x.pdf", "total_pages": 10},
            "chapters": {},
            "shared_specs": {},
            "model": {"source": "y.pdf", "total_pages": 1, "files": {}},
            "domains": {
                "DM": {
                    "section": [8, 7],
                    "spec": [1, 2],
                    "assumptions": [3, 4],
                    "examples": [5, 6],
                }
            },
        }
        result = module.validate_page_index_data(data)
        self.assertTrue(result["errors"])
        self.assertIn("invalid range", result["errors"][0])


class PdfSpotcheckTests(unittest.TestCase):
    def test_contains_anchor_matches_normalized_text(self):
        module = load_script_module("spotcheck_page_index_pdf")
        text = "DM \u2013Assumptions\nExample 1\n"
        self.assertTrue(module.contains_anchor(text, ["DM", "Assumptions"]))
        self.assertTrue(module.contains_anchor(text, ["Example 1"]))
        self.assertFalse(module.contains_anchor(text, ["Exposure"]))

    def test_build_checks_for_domain_uses_assumptions_and_examples_pages(self):
        module = load_script_module("spotcheck_page_index_pdf")
        page_index = {
            "domains": {
                "DM": {
                    "assumptions": [65, 74],
                    "examples": [74, 78],
                    "verified": "partial",
                }
            }
        }
        checks = module.build_domain_checks(page_index, ["DM"])
        self.assertEqual(len(checks), 2)
        self.assertEqual(checks[0]["page"], 65)
        self.assertEqual(checks[1]["page"], 74)
        self.assertIn("Assumptions", checks[0]["anchors"])
        self.assertIn("Example", checks[1]["anchors"][0])


class Phase4ValidationTests(unittest.TestCase):
    def test_contains_all_anchors_normalizes_spacing_and_case(self):
        module = load_script_module("validate_phase4_outputs")
        text = "Trial Design Model   and trial arms"
        self.assertTrue(module.contains_all_anchors(text, ["trial design model", "Trial Arms"]))
        self.assertFalse(module.contains_all_anchors(text, ["Supplemental Qualifiers"]))


class Phase3InventoryAuditTests(unittest.TestCase):
    def test_audit_inventory_reports_missing_and_empty_files(self):
        module = load_script_module("audit_phase3_inventory")
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            domains_root = root / "knowledge_base" / "domains"
            (domains_root / "DM").mkdir(parents=True)
            (domains_root / "AE").mkdir(parents=True)
            (domains_root / "DM" / "assumptions.md").write_text("ok", encoding="utf-8")
            (domains_root / "DM" / "examples.md").write_text("", encoding="utf-8")
            (domains_root / "AE" / "assumptions.md").write_text("ok", encoding="utf-8")

            page_index = {"domains": {"DM": {}, "AE": {}}}
            result = module.audit_inventory(page_index, domains_root, min_size_bytes=2)

        self.assertEqual(result["summary"]["domain_count"], 2)
        self.assertTrue(any("AE" in item for item in result["errors"]))
        self.assertTrue(any("DM/examples.md" in item for item in result["errors"]))


class AssumptionsAuditTests(unittest.TestCase):
    def test_extract_assumptions_section_trims_examples_tail(self):
        module = load_script_module("audit_assumptions_pdf_vs_md")
        text = textwrap.dedent(
            """\
            DM – Assumptions
            1. First assumption
            2. Second assumption
            DM – Examples
            Example 1
            """
        )
        section = module.extract_assumptions_section(text, domain="DM")
        self.assertIn("First assumption", section)
        self.assertNotIn("Examples", section)

    def test_extract_numbered_markers_detects_nested_items(self):
        module = load_script_module("audit_assumptions_pdf_vs_md")
        text = textwrap.dedent(
            """\
            1. First
               a. Child
                  i. Grandchild
            2. Second
            """
        )
        markers = module.extract_numbered_markers(text)
        self.assertIn("1.", markers)
        self.assertIn("a.", markers)
        self.assertIn("i.", markers)

    def test_analyze_assumptions_text_flags_missing_anchor_tokens(self):
        module = load_script_module("audit_assumptions_pdf_vs_md")
        pdf_text = "1. SITEID must be present. 2. USUBJID must be unique."
        md_text = "1. SITEID must be present."
        result = module.analyze_assumptions_text(pdf_text, md_text, domain="DM")
        self.assertGreater(result["pdf_numbered_count"], result["md_numbered_count"])
        self.assertIn("USUBJID", result["missing_anchor_tokens"])


class ExamplesAuditTests(unittest.TestCase):
    def test_extract_examples_section_skips_intro_material(self):
        module = load_script_module("audit_examples_pdf_vs_md")
        text = textwrap.dedent(
            """\
            Intro text
            TV – Examples
            Example 1
            tv.xpt
            """
        )
        section = module.extract_examples_section(text, domain="TV")
        self.assertTrue(section.startswith("TV"))
        self.assertIn("Example 1", section)
        self.assertNotIn("Intro text", section)

    def test_extract_example_headings_and_dataset_names(self):
        module = load_script_module("audit_examples_pdf_vs_md")
        text = textwrap.dedent(
            """\
            # DM — Examples

            ## Example 1

            **dm.xpt**

            | Row | STUDYID |
            |-----|---------|
            | 1 | ABC |

            ### Example 2

            **suppdm.xpt (secondary table)**
            """
        )
        self.assertEqual(module.extract_example_headings(text), ["Example 1", "Example 2"])
        self.assertEqual(module.extract_dataset_names(text), ["dm.xpt", "suppdm.xpt"])

    def test_build_markdown_example_signature_captures_table_rows(self):
        module = load_script_module("audit_examples_pdf_vs_md")
        text = textwrap.dedent(
            """\
            ## Example 1

            **dm.xpt**

            | Row | STUDYID | DOMAIN |
            |-----|---------|--------|
            | 1 | ABC | DM |
            | 2 | DEF | DM |
            """
        )
        signature = module.build_markdown_example_signature(text)
        self.assertEqual(signature["example_count"], 1)
        self.assertEqual(signature["dataset_names"], ["dm.xpt"])
        self.assertEqual(signature["tables"][0]["row_count"], 2)
        self.assertIn("STUDYID", signature["tables"][0]["headers"])

    def test_compare_example_signatures_flags_missing_primary_dataset(self):
        module = load_script_module("audit_examples_pdf_vs_md")
        pdf_text = "EX – Examples\nExample 1\nex.xpt\nrelrec.xpt\nSTUDYID DOMAIN USUBJID"
        md_text = textwrap.dedent(
            """\
            ## Example 1

            **relrec.xpt**

            | Row | STUDYID | DOMAIN |
            |-----|---------|--------|
            | 1 | ABC | DM |
            """
        )
        result = module.compare_examples_text(pdf_text, md_text, domain="EX")
        self.assertIn("ex.xpt", result["missing_primary_dataset_names"])
        self.assertIn("missing dataset blocks", result["flags"])


if __name__ == "__main__":
    unittest.main()
