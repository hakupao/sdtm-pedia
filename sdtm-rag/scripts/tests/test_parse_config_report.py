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
