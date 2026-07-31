from pathlib import Path

import openpyxl
import pytest

from scripts.study.parse_demo import sample_demo_values


@pytest.fixture()
def demo(tmp_path) -> Path:
    p = tmp_path / "fake_demo.xlsx"
    wb = openpyxl.Workbook()
    wb.active.title = "README"
    ws = wb.create_sheet("FAKEFORM1")
    ws.append(["SubjectId", "FAKEIT1", "FAKEIT2"])
    for r in [("S1", 1, "値甲"), ("S2", 0, "値乙"), ("S3", 1, ""), ("S4", 1, "値甲")]:
        ws.append(r)
    wb.create_sheet("Items")     # 字典 sheet, 应跳过
    wb.save(p)
    return p


def test_sample_demo_values(demo):
    samples, unmatched = sample_demo_values(demo, {"FAKEIT1", "FAKEIT2", "FAKEIT3"})
    assert samples["FAKEIT1"] == ["1", "0"]          # 去重保序
    assert samples["FAKEIT2"] == ["値甲", "値乙"]     # 空值跳过
    assert "FAKEIT3" not in samples                   # DEMO 里没有的项目不出现
    assert unmatched == ["SubjectId"]                 # 非 OID 列记录在案


def test_max_per_item(demo):
    samples, _ = sample_demo_values(demo, {"FAKEIT1"}, max_per_item=1)
    assert samples["FAKEIT1"] == ["1"]
