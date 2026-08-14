"""U3 Task 8 判定脚本 (eval/u3_task8_verdict.py) 的六条条款.

**为什么这个文件存在** (抽检方 B 变异验证, Task 9 Step 3): 该脚本此前**零测试**, 而它是
本单元 FAIL 结论的唯一出处。实测五个变异全部存活 —— 放宽条款 1 的 floor (178→170) /
让条款 1 的 fatal 判据恒真 (`==0`→`>=0`) / 对调条款 2 的两个口径 (`hold>=dev-25`→
`dev>=hold-25`) / 对调条款 4 的基线与改动后 (`b-a`→`a-b`) / 放宽条款 3 的阈值 (10→5)。
每一个都能把「⛔ 触发」翻成「未触发 (PASS)」而不留任何痕迹, 结论翻面却无人察觉。

后两个是**对调型**: 两侧都是同形状的数, 差一个减号方向, 眼睛读不出来 —— 本仓已因此吃过 5 次亏。

做法: 在 tmp_path 里造**合成** run 产物再跑真脚本 (脚本按相对路径读 runs/, 故用 cwd 隔离)。
不碰真实产物, 不发任何 LLM 请求; 合成题面是占位串, 不涉红线。
"""
import json
import subprocess
import sys
from pathlib import Path

import pytest

SCRIPT = Path(__file__).resolve().parents[2] / "eval" / "u3_task8_verdict.py"
FINAL_IDS = ("docs_v1_q15", "docs_v1_q17", "docs_v1_q53")

# 一份四条条款全部 PASS 的干净底稿; 每个用例只动其中一个维度, 好让「哪条条款红」可归因。
CLEAN = {"fatal": 0, "legacy": 180, "dev": 12, "heldout": 12, "distractor": 12}


def _payload(*, fatal, legacy, dev, heldout, distractor):
    """一遍 run 的合成产物. 组量按 spec §5.2 (12/12/12/6 + final 3)."""
    detail = [{"id": q, "group": "final", "gold": "study", "pred": "study"}
              for q in FINAL_IDS]
    for i in range(12):
        detail += [
            {"id": f"dev_{i}", "group": "dev", "gold": "study", "pred": "study"},
            {"id": f"hold_{i}", "group": "heldout", "gold": "study", "pred": "study"},
            {"id": f"dist_{i}", "group": "distractor_cdisc", "gold": "cdisc",
             "pred": "cdisc"},
        ]
    detail += [{"id": f"amb_{i}", "group": "ambiguous_both", "gold": "both", "pred": "both"}
               for i in range(6)]
    return {"summary": {"fatal_excl_final": fatal,
                        "legacy_exact": legacy,
                        "fatal_ids_excl_final": [],
                        "by_group": {"dev": {"exact": dev, "n": 12},
                                     "heldout": {"exact": heldout, "n": 12},
                                     "distractor_cdisc": {"exact": distractor, "n": 12}}},
            "detail": detail}


def _verdicts(tmp_path, *, after=None, base=None) -> dict[int, str]:
    """跑真脚本, 回收条款 1-4 的判定. 返回 {条款号: "触发" | "PASS"}."""
    runs = tmp_path / "data/study/st01/eval/runs"
    runs.mkdir(parents=True, exist_ok=True)
    a = {**CLEAN, **(after or {})}
    b = {**CLEAN, **(base or {})}
    for i in (1, 2, 3):
        (runs / f"u3_after_run_{i}.json").write_text(
            json.dumps(_payload(**a)), encoding="utf-8")
        (runs / f"u3_baseline_run_{i}.json").write_text(
            json.dumps(_payload(**b)), encoding="utf-8")
    r = subprocess.run([sys.executable, str(SCRIPT)], cwd=tmp_path,
                       capture_output=True, text=True)
    assert r.returncode == 0, r.stderr
    out: dict[int, str] = {}
    for line in r.stdout.splitlines():
        s = line.strip()
        for n in (1, 2, 3, 4):
            if s.startswith(f"条款 {n}:"):
                out[n] = "触发" if "⛔" in s else "PASS"
    assert set(out) == {1, 2, 3, 4}, f"没能解析出四条条款的判定: {sorted(out)}"
    return out


def test_clean_run_passes_all_four_clauses(tmp_path):
    """底稿必须四条全 PASS —— 否则下面每条「触发」用例都可能是假红。"""
    assert _verdicts(tmp_path) == {1: "PASS", 2: "PASS", 3: "PASS", 4: "PASS"}


def test_clause_1_triggers_when_legacy_is_below_the_floor(tmp_path):
    # 178 是 spec §7「不许下调」的那个数; 175 必须触发 (变异 M43: 下调到 170 会让它 PASS)
    assert _verdicts(tmp_path, after={"legacy": 175})[1] == "触发"


def test_clause_1_triggers_on_any_non_final_fatal(tmp_path):
    # 变异 M44: 把 `fatal_excl_final == 0` 改成 `>= 0` 即恒真, 条款 1 就再也不会触发
    assert _verdicts(tmp_path, after={"fatal": 3})[1] == "触发"


def test_clause_2_measures_heldout_against_dev_not_the_reverse(tmp_path):
    """**对调型**: dev 满分而 held-out 零分, 是条款 2 要抓的那一格 (泛化崩了).

    变异 M45 把 `hold >= dev - 25` 对调成 `dev >= hold - 25`: 同样的数据下变成「未触发」,
    因为 dev 高于 held-out 永远满足反向不等式 —— 条款 2 从此只在 dev 崩掉时才响。
    """
    v = _verdicts(tmp_path, after={"dev": 12, "heldout": 0})
    assert v[2] == "触发"
    assert v[1] == "PASS" and v[3] == "PASS", "应当只有条款 2 红, 否则归因不成立"


def test_clause_3_triggers_below_the_dev_floor(tmp_path):
    # 变异 M47: 阈值 10 → 5 后 dev=7/12 就成了 PASS
    v = _verdicts(tmp_path, after={"dev": 7})
    assert v[3] == "触发"
    assert v[1] == "PASS", "应当只有条款 3 (与可能的条款 2) 红"


def test_clause_4_measures_drop_from_baseline_not_the_reverse(tmp_path):
    """**对调型**: 干扰题从基线 12 掉到 0, 是条款 4 要抓的那一格 (改动伤了 CDISC 侧).

    变异 M46 把 `b - a <= 1` 对调成 `a - b <= 1`: 下降 12 题变成「未触发」,
    条款 4 从此只在干扰题**变好**太多时才响 —— 与它的用途正好相反。
    """
    v = _verdicts(tmp_path, after={"distractor": 0}, base={"distractor": 12})
    assert v[4] == "触发"
    assert v[1] == "PASS", "应当只有条款 4 红, 否则归因不成立"


@pytest.mark.parametrize("field", ["dev", "heldout", "distractor"])
def test_clause_4_and_2_are_not_reading_the_same_group(tmp_path, field):
    """三个组各自独立进不同条款 —— 防「口径接错组」这一类静默.

    只动一个组, 断言另外两条条款不受牵连。
    """
    v = _verdicts(tmp_path, after={field: 0})
    expected_red = {"dev": 3, "heldout": 2, "distractor": 4}[field]
    assert v[expected_red] == "触发"
    assert v[1] == "PASS"
