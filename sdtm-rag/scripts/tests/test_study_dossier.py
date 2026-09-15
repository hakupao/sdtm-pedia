"""DM2 T1: 研读包构建是纯文件读 + 确定性拼接. 守三件事:
  ① 白名单章进、非白名单章不进, 章按 section_number 自然序, 分 part 章拼回一段
  ② 一览每卡一行: 标题行 | 型/必須 | 选择肢 (无 codelist 则省), INDEX/ROUTING 不进
  ③ sha 稳定; 超 max_chars 抛 DossierBuildError, 不截断
"""
from pathlib import Path
import pytest
from server.study_dossier import DossierBuildError, build_dossier

DOC = """---
study: st99
doc_type: protocol_section
doc_no: 1
section_number: {sec}
part: {part}
parts_total: {total}
page_start: 10
page_end: 11
version: VNEW
---

{title}
{body}
"""
CARD = """---
study: st99
version: VNEW
doc_type: field_card
form_oid: {form}
field_oid: {item}
source_sheet: Items and Groups
source_row: {row}
generated_by: t
---

# [偽フォーム {form}] 偽項目{item} ({item})
- Form: 偽フォーム ({form})
- 型: {typ} (len 1) / 必須
- Control: X
{codelist}- Edit checks: —
"""
CL = "- Codelist: CL_X\n  - 1 = はい\n  - 2 = いいえ\n"
NOCL = "- Codelist: なし (自由記述)\n"


def _mk(tmp_path):
    docs = tmp_path / "docs"; cards = tmp_path / "cards"
    docs.mkdir(); cards.mkdir()
    (docs / "st99__doc01__s4_2.md").write_text(DOC.format(sec="4.2", part=1, total=1, title="4.2 除外", body="B42"), encoding="utf-8")
    (docs / "st99__doc01__s4_1.md").write_text(DOC.format(sec="4.1", part=1, total=1, title="4.1 選択", body="B41"), encoding="utf-8")
    (docs / "st99__doc01__s8_2__part01.md").write_text(DOC.format(sec="8.2", part=1, total=2, title="8.2 評価", body="P1"), encoding="utf-8")
    (docs / "st99__doc01__s8_2__part02.md").write_text(DOC.format(sec="8.2", part=2, total=2, title="(cont)", body="P2"), encoding="utf-8")
    (docs / "st99__doc01__s13_1.md").write_text(DOC.format(sec="13.1", part=1, total=1, title="13.1 倫理", body="NO"), encoding="utf-8")
    (cards / "st99__FB__I2.md").write_text(CARD.format(form="FB", item="I2", row=9, typ="date", codelist=NOCL), encoding="utf-8")
    (cards / "st99__FA__I1.md").write_text(CARD.format(form="FA", item="I1", row=5, typ="integer", codelist=CL), encoding="utf-8")
    (cards / "st99__FA__I0.md").write_text(CARD.format(form="FA", item="I0", row=3, typ="text", codelist=NOCL), encoding="utf-8")
    (cards / "INDEX.md").write_text("# index\n", encoding="utf-8")
    return docs, cards


def test_sections_filtered_ordered_and_parts_joined(tmp_path):
    docs, cards = _mk(tmp_path)
    d = build_dossier(docs, cards, sections=["4", "8"], max_chars=100_000)
    assert d.sections == ("4.1", "4.2", "8.2")
    assert "NO" not in d.text and "13.1" not in d.text
    a = d.text.index("### 4.1 選択"); b = d.text.index("### 4.2 除外"); c = d.text.index("### 8.2 評価")
    assert a < b < c
    assert "P1\nP2" in d.text or "P1\n\nP2" in d.text      # part 拼回一段, 只有一个 8.2 标题
    assert d.text.count("### 8.2") == 1
    assert "(p.10-11)" in d.text


def test_items_one_line_each_sorted_by_form_then_row(tmp_path):
    docs, cards = _mk(tmp_path)
    d = build_dossier(docs, cards, sections=["4"], max_chars=100_000)
    lines = [l for l in d.text.splitlines() if l.startswith("[偽フォーム")]
    assert lines == [
        "[偽フォーム FA] 偽項目I0 (I0) | text 必須",
        "[偽フォーム FA] 偽項目I1 (I1) | integer 必須 | 1=はい 2=いいえ",
        "[偽フォーム FB] 偽項目I2 (I2) | date 必須",
    ]
    assert d.n_items == 3 and "index" not in d.text


def test_sha_stable_and_header(tmp_path):
    docs, cards = _mk(tmp_path)
    d1 = build_dossier(docs, cards, sections=["4"], max_chars=100_000)
    d2 = build_dossier(docs, cards, sections=["4"], max_chars=100_000)
    assert d1.sha == d2.sha and len(d1.sha) == 12 and d1.chars == len(d1.text)
    assert d1.text.startswith("# 【本研究 研読パッケージ】")
    assert d1.study == "st99" and d1.version == "VNEW"


def test_over_budget_raises_not_truncates(tmp_path):
    docs, cards = _mk(tmp_path)
    with pytest.raises(DossierBuildError, match="max_chars"):
        build_dossier(docs, cards, sections=["4"], max_chars=50)


def test_empty_whitelist_hit_raises(tmp_path):
    docs, cards = _mk(tmp_path)
    with pytest.raises(DossierBuildError, match="0 sections"):
        build_dossier(docs, cards, sections=["99"], max_chars=100_000)
