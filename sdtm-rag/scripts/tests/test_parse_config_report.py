from pathlib import Path

import openpyxl
import pytest

from scripts.tests.study_fixtures import build_config_report
from scripts.study.parse_config_report import read_sheet_records


@pytest.fixture()
def report(tmp_path) -> Path:
    return build_config_report(tmp_path / "fake_report.xlsx")


def test_read_sheet_records_keys_and_forward_fill(report):
    wb = openpyxl.load_workbook(report, read_only=True)
    recs = read_sheet_records(wb["Items and Groups"])
    assert len(recs) == 4
    first = recs[0]
    assert first["Type and container::Form ID"] == "FAKEFORM1"
    # 分组前向填充: 第 2 列同属 Type and container
    assert first["Type and container::Form Name"] == "偽フォーム一"
    assert recs[1]["Validation::Item ID"] == "FAKEIT1"
    assert recs[1]["General::Choices"] == "CL_FAKE1"


def test_read_sheet_records_row_numbers(report):
    wb = openpyxl.load_workbook(report, read_only=True)
    recs = read_sheet_records(wb["Items and Groups"])
    assert recs[0]["_row"] == 4          # 数据从 xlsx 行 4 起
    assert recs[3]["_row"] == 7


def test_read_sheet_records_skips_blank_rows(tmp_path):
    p = build_config_report(tmp_path / "r.xlsx",
                            items_rows=[("", "") + ("",) * 19])
    wb = openpyxl.load_workbook(p, read_only=True)
    assert read_sheet_records(wb["Items and Groups"]) == []


def test_read_sheet_records_two_row_header(report):
    """真实 Code lists 是两行表头 (行1 sheet名 / 行2 列名), 分组名取 sheet 名."""
    wb = openpyxl.load_workbook(report, read_only=True)
    recs = read_sheet_records(wb["Code lists"], has_section_row=False)
    assert len(recs) == 3                     # 三行不能被表头吃掉一条
    assert recs[0]["_row"] == 3               # 数据从 xlsx 行 3 起
    assert recs[0]["Code lists::OID"] == "CL_FAKE1"
    assert recs[0]["Code lists::Code text"] == "偽選択肢はい"
    assert recs[2]["Code lists::OID"] == "CL_UNUSED"


class _StubSheet:
    """短行 sheet: openpyxl read_only 会自动补到 max_column, 故用 stub 直喂短 tuple."""

    title = "Stub"

    def __init__(self, rows):
        self._rows = rows

    def iter_rows(self, values_only=True):
        return iter(self._rows)


def test_read_sheet_records_pads_short_rows():
    ws = _StubSheet([
        ("Stub", "Stub", "Stub"),
        ("A", "A", "B"),
        ("c1", "c2", "c3"),
        ("v1",),                      # 短行: 缺 c2 / c3
    ])
    recs = read_sheet_records(ws)
    assert len(recs) == 1
    assert recs[0]["A::c1"] == "v1"
    assert recs[0]["A::c2"] == ""     # 缺列补空串, 不得静默丢 key
    assert recs[0]["B::c3"] == ""
