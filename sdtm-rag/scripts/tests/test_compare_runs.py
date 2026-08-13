"""U3 Task 1: run_eval 产物比对器. 每条断言对应一种「静默报无差异」的失败形态."""
import json

import pytest

from eval.compare_runs import diff_scores, load_scores, main, unstable_ids


def _write(tmp_path, name, results):
    p = tmp_path / name
    p.write_text(json.dumps({"summary": {}, "results": results}), encoding="utf-8")
    return p


def test_load_scores_reads_id_and_recall(tmp_path):
    p = _write(tmp_path, "r.json", [{"id": "a", "source_recall": 1.0},
                                    {"id": "b", "source_recall": 0.5}])
    assert load_scores(p) == {"a": 1.0, "b": 0.5}


def test_load_scores_rejects_empty_results(tmp_path):
    # 空产物比对恒等于「无差异」—— 最危险的假绿灯
    p = _write(tmp_path, "empty.json", [])
    with pytest.raises(ValueError):
        load_scores(p)


def test_load_scores_rejects_duplicate_id(tmp_path):
    # 后者覆盖前者 = 静默改变比对结果
    p = _write(tmp_path, "dup.json", [{"id": "a", "source_recall": 1.0},
                                      {"id": "a", "source_recall": 0.0}])
    with pytest.raises(ValueError):
        load_scores(p)


def test_diff_empty_when_identical():
    assert diff_scores({"a": 1.0}, {"a": 1.0}) == {}


def test_diff_reports_value_change():
    assert diff_scores({"a": 1.0}, {"a": 0.5}) == {"a": (1.0, 0.5)}


def test_diff_detects_missing_key_on_either_side():
    # 「一边少了几题」被读成「无差异」是本仓反复吃过的亏
    assert diff_scores({"a": 1.0, "b": 1.0}, {"a": 1.0}) == {"b": (1.0, None)}
    assert diff_scores({"a": 1.0}, {"a": 1.0, "b": 1.0}) == {"b": (None, 1.0)}


def test_unstable_ids_flags_varying_question():
    runs = [{"a": 1.0, "b": 1.0}, {"a": 1.0, "b": 0.5}, {"a": 1.0, "b": 1.0}]
    assert unstable_ids(runs) == {"b": [1.0, 0.5, 1.0]}


def test_unstable_ids_empty_when_all_runs_agree():
    runs = [{"a": 1.0}, {"a": 1.0}, {"a": 1.0}]
    assert unstable_ids(runs) == {}


def test_unstable_ids_requires_two_runs():
    # 单遍谈不上稳定性; 返回 {} 会被读成「三遍一致」
    with pytest.raises(ValueError):
        unstable_ids([{"a": 1.0}])


def test_unstable_ids_flags_key_present_in_only_some_runs():
    runs = [{"a": 1.0, "b": 1.0}, {"a": 1.0}]
    assert unstable_ids(runs) == {"b": [1.0, None]}
    # 反向: 缺题出现在后面的遍次 (第 2/3 遍中途崩了少写几题)。键集合若只取 runs[0],
    # 这一格返回 {} —— 字面意义的「遍遍一致」, 正是本模块要防的那一格。
    assert unstable_ids([{"a": 1.0}, {"a": 1.0, "b": 1.0}]) == {"b": [None, 1.0]}


# --- CLI 入口: 它自己就是闸 (rc 与 unstable 计数是判据), 故必须有守护 ---


def test_main_rejects_same_path_passed_twice(tmp_path):
    # 三遍 --output 忘带轮次变量 = 三份「产物」是同一个文件, 自我比对恒等于稳定
    p = _write(tmp_path, "r.json", [{"id": "docs_v1_q1", "source_recall": 1.0}])
    with pytest.raises(SystemExit):
        main([str(p), str(p)])


def test_main_returns_zero_when_runs_agree(tmp_path):
    rows = [{"id": "docs_v1_q1", "source_recall": 1.0},
            {"id": "docs_v1_q2", "source_recall": 1.0}]
    assert main([str(_write(tmp_path, "a.json", rows)),
                 str(_write(tmp_path, "b.json", rows))]) == 0


def test_main_returns_one_and_names_unstable_id(tmp_path, capsys):
    a = _write(tmp_path, "a.json", [{"id": "docs_v1_q1", "source_recall": 1.0},
                                    {"id": "docs_v1_q2", "source_recall": 1.0}])
    b = _write(tmp_path, "b.json", [{"id": "docs_v1_q1", "source_recall": 1.0},
                                    {"id": "docs_v1_q2", "source_recall": 0.5}])
    assert main([str(a), str(b)]) == 1
    assert "docs_v1_q2" in capsys.readouterr().out


def test_main_reads_every_run_not_just_the_first_two(tmp_path, capsys):
    # 只有第 3 遍偏离: 若 main 静默丢掉尾部遍次 (如 scored[:2]), 这里会报「一致」rc=0
    same = [{"id": "docs_v1_q1", "source_recall": 1.0}]
    a = _write(tmp_path, "a.json", same)
    b = _write(tmp_path, "b.json", same)
    c = _write(tmp_path, "c.json", [{"id": "docs_v1_q1", "source_recall": 0.5}])
    assert main([str(a), str(b), str(c)]) == 1
    assert "docs_v1_q1" in capsys.readouterr().out
