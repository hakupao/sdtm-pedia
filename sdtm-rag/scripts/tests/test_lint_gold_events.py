"""event 侧 gold 的唯一性闸. 零真名: 全部用伪 OID."""
import json

import pytest

from eval.lint_gold import event_target_names


def test_event_target_names_covers_three_pools(tmp_path):
    cat = {
        "events": [{"oid": "偽EV1"}, {"oid": "偽EV2"}],
        "activities": [{"oid": "偽AC1", "event_oid": "偽EV1"}],
        "assignments": [{"event_oid": "偽EV1", "activity_oid": "偽AC1", "form_oid": "偽F"}],
    }
    p = tmp_path / "catalog.json"
    p.write_text(json.dumps(cat), encoding="utf-8")
    names = event_target_names(p)
    assert "event:偽EV1" in names
    assert "event:偽EV2" in names
    assert "activity:偽EV1/偽AC1" in names
    assert "assignment:偽EV1/偽AC1/偽F" in names
    assert len(names) == 4


def test_event_target_names_are_unique(tmp_path):
    cat = {"events": [{"oid": "偽EV1"}, {"oid": "偽EV1"}],
           "activities": [], "assignments": []}
    p = tmp_path / "catalog.json"
    p.write_text(json.dumps(cat), encoding="utf-8")
    with pytest.raises(ValueError, match="duplicate"):
        event_target_names(p)
