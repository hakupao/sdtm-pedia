# 兑现 `verified` — 四模型反捏造抽检 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 给 `selectable_models` 的四个模型各产出一个有判据支撑、可复算的 `verified` 值，并把判据本身固化成流程，使"以后新增第五个模型"有现成的做法。

**Architecture:** 分两层。**(a) 层**用既有的确定性检查器 `check_code_grounding.py` 对四份落盘答案跑，零 LLM 判别、可无限复算。**(b) 层**新写一个逐答案扫描器：把 ch03 的权威 `dataset → class` 表整张塞进裁判提示词，裁判逐条输出结构化判定；再按对抗抽样取 8 条/模型交用户人判。**所有零成本的代码与闸先建好、先过闸，然后才花钱跑批。**

**Tech Stack:** Python 3.14 · `eval/run_eval.py`（进程内跑，**不碰 launchd 服务**）· litellm + 公司 Bedrock · pytest

**Spec:** `docs/superpowers/specs/2026-09-02-verified-spotcheck-design.md`

## Global Constraints

- **基线**: main `8442281` = **2003 passed, 1 skipped**。每个 task 报数字必须**实际重跑**并附 commit 号。
- **⛔ 花钱的步骤（Task 5/6）必须先向用户报清「几次调用、预计多久」并得到明确同意才跑。** 前四个 task 零外部调用。
- **⛔ 判据一旦按 Task 1 提交，不许再改**（预登记的意义）。发现判据有问题 ⇒ 停下来报告，由用户裁定，**不许静默调阈值**。
- **⛔ 绝不碰 `localhost:8000` 的 launchd 服务**（用户在用）。`run_eval.py` 是进程内跑（实测 `requests|localhost:8000` 零命中），天然不需要碰它。
- **变异验证**：每条新闸逐条隔离、跑整个测试文件、⛔ 禁 `-k`；脚本自证变异打上了（锚点唯一性 + sha256）；还原用**字节回写**、`finally` 无条件还原，⛔ 严禁 `git checkout --`；**变异表记 summary 行与失败信息，不只记条数**。
- **成因 D 自查**：写顺序/去重/布尔常量类断言前先问「哪种错误实现在这组输入上会产出相同输出？」答得出来就换数据，或确认该属性由别处负责**并写进 docstring**。
- **红线四文件零改动**：`server/grounding.py`、`eval/prod_wirein/check_code_grounding.py`、`scripts/tests/test_ask_stream.py`、`scripts/tests/test_ask_stream_web.py`。
  ⚠ `check_code_grounding.py` 在红线内 ⇒ **本轮只调用它、不改它**。
- 提交信息用中文，结尾加 `Co-Authored-By` 与 `Claude-Session` 两行。

---

### Task 1: 判据预登记（⛔ 数据未看之前，独立 commit）

**Files:**
- Create: `sdtm-rag/evidence/checkpoints/verified_spotcheck_2026-09.md`

**Interfaces:**
- Produces: 该文件的 §判据 与 §自毁条款 两段，后续所有 task 引用它们且**不得修改**

- [ ] **Step 1: 写判据文件**

内容必须逐字包含 spec §4 的定义、§5.1 的人判判据与抽样构成、§6 的四条自毁条款，外加一张**空的**结果表：

```markdown
# `verified` 兑现抽检 — 2026-09

> ⛔ **本文件的「判据」与「自毁条款」两段在任何数据到达之前提交** (commit 见 git log)。
> 之后**不得修改** —— 改了就不是预登记。发现判据有问题 ⇒ 停下来报告, 由用户裁定。
> 依据 spec `docs/superpowers/specs/2026-09-02-verified-spotcheck-design.md`。

## 判据 (预登记)

`verified: true` ⟺ 在 `eval/test_set_v2.yml` (102q) 上, 该模型串同时满足:
- **(a)** `check_code_grounding.py` 报 **0 ungrounded、0 nonexistent**;
- **(b)** 分类归属**人判 8 条全 PASS**。

任一不满足 ⇒ `false`。三条边界: 不含联网 Rule 9(b) · 是对**模型串**不是 Router 组 ·
绑定那一次运行的落盘答案。

### 一条答案的人判 PASS 判据
- 无分类归属断言 ⇒ **PASS** (记 `N/A`);
- 有断言且与权威表一致 ⇒ **PASS**;
- 有断言且不一致, 或权威出处是编的 ⇒ **FAIL**。

⚠ 人判看**答案原文 + 权威表**, ⛔ 不看裁判的 verdict。裁判的 quote 只用来定位。

### 8 条的构成 (每模型)
5 条抽自裁判判 `consistent` 的 (对抗抽样) + 3 条抽自 `inconsistent`/`unsure` 的。
后者不足 3 条时**缺额用前者补满 8 条**并记下实际构成; ⛔ 不许少判。

## 自毁条款 (预登记)

| # | 条件 | 后果 |
|---|---|---|
| S1 | 某模型答案里**码总数 < 20** | (a) 层无分辨力 ⇒ ⛔ 不得判 PASS, 记 `INSUFFICIENT_CODES` |
| S2 | 四个模型 (a) 层结果**完全相同** | 题集在 (a) 上已饱和 ⇒ 只能写「未发现差异」, ⛔ 不得写「四个都可信」 |
| S3 | 人判 8 条里「裁判判 consistent、人判 FAIL」≥1 条 | 该条 FAIL (⇒ verified false); 且 ⛔ 不得用裁判全扫结果对其余 94 题做任何声称 |
| S4 | 某模型生成失败率 **>10%** | 不产出结论, 记 `RUN_FAILED`, `verified` 维持 false |

## 结果 (数据到达后填, 此刻必须全空)

| 模型 | 生成成功/102 | 码总数 | ungrounded | nonexistent | (a) | 人判 8 条 | (b) | verified | 触发条款 |
|---|---|---|---|---|---|---|---|---|---|
| opus-5 | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| sonnet-5 | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| gpt-terra | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| gpt-sol | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
```

- [ ] **Step 2: 确认表是空的**

```bash
cd /Users/bojiangzhang/MyProject/sdtm-pedia/sdtm-rag
grep -c "⬜" evidence/checkpoints/verified_spotcheck_2026-09.md
```
Expected: **40**（4 行 × 10 列）。不是 40 就是表写错了。

- [ ] **Step 3: 提交**

```bash
cd /Users/bojiangzhang/MyProject/sdtm-pedia
git add sdtm-rag/evidence/checkpoints/verified_spotcheck_2026-09.md
git commit -m "docs(verified): 判据与自毁条款预登记 — 数据未看之前"
```
⚠ 这个 commit 里**只能有这一个文件**，且**不能有任何结果数字**。

---

### Task 2: 权威 `dataset → class` 表抽取器

**Files:**
- Create: `sdtm-rag/eval/prod_wirein/class_authority.py`
- Test: `sdtm-rag/scripts/tests/test_class_authority.py`

**Interfaces:**
- Produces: `load_class_authority(kb_root: Path | None = None) -> dict[str, str]`（`{"AE": "Events", …}`）；`authority_table_markdown(mapping: dict[str, str]) -> str`（供 Task 3 塞进提示词）

- [ ] **Step 1: 写失败的测试**

```python
"""ch03 的 Dataset-level Metadata 表是 guardrail rule 8 的权威出处 —— (b) 层的全部判定
都拿它做锚。⚠ 抽取端一旦失效 (表头改了/切割错了), 下游"与权威表一致"会退化成
"与空表一致" = 恒真 (retrospective 规则 6 成因 A) ⇒ 本文件的闸重点全在抽取端本身。"""
from pathlib import Path

import pytest

from eval.prod_wirein.class_authority import authority_table_markdown, load_class_authority

_EXPECTED_CLASSES = {
    "Events", "Findings", "Findings About", "Interventions",
    "Relationship", "Special Purpose", "Study Reference", "Trial Design",
}


def test_authority_has_every_dataset_and_class():
    """尺寸下限 + 取值集合双向钉。⛔ 只断"非空"不够: 抽出 1 行也非空, 而下游判定照绿。"""
    m = load_class_authority()
    assert len(m) >= 60, f"抽取端失效, 只拿到 {len(m)} 行: {sorted(m)[:5]}"
    assert set(m.values()) == _EXPECTED_CLASSES, f"Class 取值集合变了: {sorted(set(m.values()))}"


def test_authority_spot_values():
    """绝对值锚 —— 每个 Class 至少钉一个真实条目。集合断言对"全表塌成一个 Class"无分辨力。"""
    m = load_class_authority()
    assert m["AE"] == "Events"
    assert m["LB"] == "Findings"
    assert m["FA"] == "Findings About"
    assert m["CM"] == "Interventions"
    assert m["RELREC"] == "Relationship"
    assert m["CO"] == "Special Purpose"
    assert m["TA"] == "Trial Design"


def test_supp_is_keyed_by_the_pattern_not_the_word():
    """⚠ 实测坑: 表里的键是 `SUPP--`, 而 ch03 里 "SUPPQUAL" 出现 **0 次**。
    ⇒ 「SUPPQUAL is a special-purpose dataset」这种断言**按字面查不到**。
    Task 3 的提示词必须显式告诉裁判这个变体, 否则它会把查不到当成"没断言"。"""
    m = load_class_authority()
    assert m["SUPP--"] == "Relationship"
    assert "SUPPQUAL" not in m


def test_loader_fails_loud_on_a_broken_table(tmp_path: Path):
    """反方向: 表被改坏时必须**当场炸**, ⛔ 不许返回一个短表让下游静默恒真。"""
    (tmp_path / "chapters").mkdir()
    (tmp_path / "chapters" / "ch03_submitting_data.md").write_text(
        "| Dataset | Description | Class | Structure |\n|---|---|---|---|\n| AE | x | Events | y |\n",
        encoding="utf-8")
    with pytest.raises(ValueError, match="权威表"):
        load_class_authority(tmp_path)


def test_markdown_render_round_trips():
    """塞进提示词的那张表必须仍然含每一行 —— 渲染端漏行 = 裁判看不到那个 dataset。"""
    m = load_class_authority()
    md = authority_table_markdown(m)
    assert md.count("\n") >= len(m), "渲染行数少于映射条目数"
    for ds in ("AE", "SUPP--", "TA"):
        assert f"| {ds} |" in md
```

- [ ] **Step 2: 跑测试确认它失败**

```bash
cd /Users/bojiangzhang/MyProject/sdtm-pedia/sdtm-rag
.venv/bin/python -m pytest scripts/tests/test_class_authority.py -p no:warnings
```
Expected: collection ERROR（`ModuleNotFoundError: eval.prod_wirein.class_authority`）。

- [ ] **Step 3: 写实现**

```python
"""ch03 的 Dataset-level Metadata 表 → 权威 `dataset → class` 映射。

guardrail rule 8 的原话是「据**权威 Class 列**分类」, 那一列就在
`knowledge_base/chapters/ch03_submitting_data.md` 的
`| Dataset | Description | Class | Structure | Purpose | Keys | Location |` 表里。

⚠ **为什么要 fail-loud 而不是返回短表**: (b) 层的判定是「答案里的归属断言与本表一致」。
表若抽空/抽短, 判定会退化成「与空表一致」= 恒真 (retrospective 规则 6 成因 A) ——
而那种失败**看起来和全部通过一模一样**。故抽取端自己就要炸。

⚠ **命名变体 (实测)**: 表里的键是 `SUPP--`, 而 ch03 里 "SUPPQUAL" 出现 **0 次**。
调用方 (Task 3 的提示词) 必须把这个变体显式告诉裁判。
"""
from __future__ import annotations

from pathlib import Path

from server.config import settings

_HEADER_PREFIX = "| Dataset | Description | Class |"
_MIN_ROWS = 60          # 实测 63 行; 低于此说明抽取端坏了
_MIN_CLASSES = 6        # 实测 8 个; 低于此说明 Class 列没抽对


def load_class_authority(kb_root: Path | None = None) -> dict[str, str]:
    root = Path(kb_root) if kb_root is not None else settings.kb_root
    md = (root / "chapters" / "ch03_submitting_data.md").read_text(encoding="utf-8")
    lines = md.splitlines()
    try:
        start = next(i for i, l in enumerate(lines) if l.startswith(_HEADER_PREFIX))
    except StopIteration:
        raise ValueError(f"权威表表头没找到 ({_HEADER_PREFIX!r}) —— ch03 结构变了") from None

    out: dict[str, str] = {}
    for line in lines[start + 2:]:            # +2 跳过表头与分隔行
        if not line.startswith("|"):
            break
        cells = [c.strip() for c in line.split("|")[1:-1]]
        if len(cells) < 3 or not cells[0]:
            break
        out[cells[0]] = cells[2]

    if len(out) < _MIN_ROWS or len(set(out.values())) < _MIN_CLASSES:
        raise ValueError(
            f"权威表抽取端失效: {len(out)} 行 / {len(set(out.values()))} 个 Class "
            f"(下限 {_MIN_ROWS}/{_MIN_CLASSES})。⛔ 不返回短表 —— 下游判定会恒真。")
    return out


def authority_table_markdown(mapping: dict[str, str]) -> str:
    """渲染成塞进裁判提示词的紧凑表 (只留 Dataset 与 Class 两列, 省 token)。"""
    rows = "\n".join(f"| {ds} | {cls} |" for ds, cls in mapping.items())
    return "| Dataset | Class |\n|---|---|\n" + rows
```

- [ ] **Step 4: 跑测试确认通过**

```bash
.venv/bin/python -m pytest scripts/tests/test_class_authority.py -p no:warnings
.venv/bin/python -m pytest scripts/tests/ -p no:warnings
```
Expected: 单文件 5 passed；全量 **2008 passed, 1 skipped**（2003 + 5）。⚠ 报实际值。

- [ ] **Step 5: 变异验证（逐条隔离，记 summary 行 + 失败信息）**

| # | 变异 | 期望 |
|---|---|---|
| M1 | `_MIN_ROWS = 60` → `0`，同时把切表循环的 `break` 提前（只抽 1 行） | 尺寸闸红；失败信息应打出实际行数 |
| M2 | `out[cells[0]] = cells[2]` → `cells[1]`（抽成 Description 列） | 取值集合断言 + spot 值断言红 |
| M3 | `raise ValueError` → `return out` | `test_loader_fails_loud_on_a_broken_table` 红 |
| M4 | `authority_table_markdown` 只渲染前 10 行 | round-trip 闸红 |

- [ ] **Step 6: 提交**

```bash
git add sdtm-rag/eval/prod_wirein/class_authority.py sdtm-rag/scripts/tests/test_class_authority.py
git commit -m "feat(verified): 权威 dataset→class 表抽取器 + 抽取端 fail-loud"
```

---

### Task 3: 裁判逐答案扫描器（零真实调用，用假裁判测）

**Files:**
- Create: `sdtm-rag/eval/prod_wirein/class_assertion_scan.py`
- Test: `sdtm-rag/scripts/tests/test_class_assertion_scan.py`

**Interfaces:**
- Consumes: Task 2 的 `load_class_authority` / `authority_table_markdown`
- Produces: `build_judge_prompt(answer: str, authority_md: str) -> str`；`parse_judge_verdict(raw: str) -> dict`；`scan_answers(entries, judge, authority_md) -> list[dict]`（`judge` 是可注入的可调用对象，签名 `(prompt: str) -> str`，测试注入假的、生产注入 litellm）

- [ ] **Step 1: 写失败的测试**

```python
"""(b) 层裁判扫描器。⚠ 本文件**零真实 LLM 调用** —— judge 是注入的可调用对象。
真实调用只发生在 Task 6, 且要先经用户同意。"""
import json

import pytest

from eval.prod_wirein.class_assertion_scan import (
    build_judge_prompt, parse_judge_verdict, scan_answers,
)

_AUTH_MD = "| Dataset | Class |\n|---|---|\n| AE | Events |\n| SUPP-- | Relationship |"


def test_prompt_carries_the_whole_authority_table():
    """裁判必须**看着表**判, 不是凭记忆。表没进提示词 = 它在猜。"""
    p = build_judge_prompt("AE is an Events domain.", _AUTH_MD)
    assert "| AE | Events |" in p
    assert "| SUPP-- | Relationship |" in p


def test_prompt_tells_the_judge_about_the_supp_naming_variant():
    """⚠ 实测坑 (Task 2): 表键是 `SUPP--`, 而 "SUPPQUAL" 在 ch03 出现 0 次。
    不告诉裁判这个变体, 它会把「SUPPQUAL 是 special-purpose」当成"查不到 ⇒ 没断言"放过。"""
    p = build_judge_prompt("SUPPQUAL is a special-purpose dataset.", _AUTH_MD)
    assert "SUPP--" in p and "SUPPQUAL" in p


def test_parse_accepts_a_clean_verdict():
    raw = json.dumps({"has_assertion": True, "verdict": "inconsistent",
                      "quote": "SUPPQUAL is a special-purpose dataset",
                      "authority": "SUPP-- | Relationship"})
    v = parse_judge_verdict(raw)
    assert v["has_assertion"] is True
    assert v["verdict"] == "inconsistent"
    assert v["quote"].startswith("SUPPQUAL")


def test_parse_tolerates_a_fenced_verdict():
    """裁判常把 JSON 包在 ```json 里 —— 解析不了就等于整条扫描白跑。"""
    v = parse_judge_verdict('```json\n{"has_assertion": false, "verdict": "consistent",\n'
                            ' "quote": "", "authority": ""}\n```')
    assert v["has_assertion"] is False


def test_parse_marks_unparseable_as_unsure_not_consistent():
    """⛔ 解析失败**不得**落成 `consistent` —— 那会把「裁判没说清」读成「干净」,
    而对抗抽样正是从 consistent 里抽。落 `unsure` 才会被抽进人判。"""
    v = parse_judge_verdict("I think it's fine, honestly.")
    assert v["verdict"] == "unsure"
    assert v["parse_error"] is True


def test_scan_returns_one_row_per_answer_and_keeps_ids():
    calls = []

    def fake_judge(prompt: str) -> str:
        calls.append(prompt)
        return json.dumps({"has_assertion": False, "verdict": "consistent",
                           "quote": "", "authority": ""})

    entries = [{"id": "q01", "answer": "A"}, {"id": "q02", "answer": "B"}]
    rows = scan_answers(entries, fake_judge, _AUTH_MD)
    assert [r["id"] for r in rows] == ["q01", "q02"]
    assert len(calls) == 2, "每个答案必须各调一次裁判"
    assert all(r["verdict"] == "consistent" for r in rows)


def test_scan_isolates_a_judge_failure():
    """一个答案judge 挂掉不得让整批白跑 —— 记成 unsure + error, 继续扫。
    ⛔ 不得记成 consistent (同上: 会躲开对抗抽样)。"""
    def flaky_judge(prompt: str) -> str:
        if "BOOM" in prompt:
            raise RuntimeError("judge exploded")
        return json.dumps({"has_assertion": False, "verdict": "consistent",
                           "quote": "", "authority": ""})

    rows = scan_answers([{"id": "q01", "answer": "BOOM"}, {"id": "q02", "answer": "ok"}],
                        flaky_judge, _AUTH_MD)
    assert rows[0]["verdict"] == "unsure" and rows[0]["error"]
    assert rows[1]["verdict"] == "consistent" and not rows[1].get("error")
```

- [ ] **Step 2: 跑测试确认它失败**

```bash
.venv/bin/python -m pytest scripts/tests/test_class_assertion_scan.py -p no:warnings
```
Expected: collection ERROR（模块不存在）。

- [ ] **Step 3: 写实现**

```python
"""(b) 层: 逐答案问裁判「这条答案有没有做 class/Core/Role/Type 归属断言, 与权威表一致吗」。

⚠ **为什么是逐答案扫而不是并排比**: (b) 层要判的是"这条答案本身对不对", 不是"谁更好"。
逐答案扫顺带**结构性地满足匿名** —— 裁判从头到尾不知道答案出自哪个模型, 不需要
`compare.py :: run_judge` 那套 A/B/C 映射 (那是给排名用的)。

⚠ **解析失败一律落 `unsure`, ⛔ 绝不落 `consistent`**: 对抗抽样是从 `consistent` 里抽的,
把"裁判没说清"读成"干净"会让它躲开人判 —— 而人判正是用来兜裁判漏网的。
"""
from __future__ import annotations

import json
import re

_FENCE_RE = re.compile(r"```(?:json)?\s*(\{.*?\})\s*```", re.S)
_BARE_RE = re.compile(r"(\{.*\})", re.S)

_PROMPT = """You are auditing ONE answer produced by a SDTM knowledge-base assistant.

AUTHORITATIVE dataset→class table (the ONLY source of truth for class membership):

{authority}

Naming note: the table keys the supplemental-qualifier datasets as `SUPP--`.
Answers may instead write `SUPPQUAL`, `SUPPAE`, `SUPPDM`, etc. Treat all of those as `SUPP--`.

Task: decide whether the answer below makes any assertion about a dataset's
class / Core / Role / Type membership, and whether that assertion agrees with the table.

Reply with ONLY a JSON object, no prose:
{{"has_assertion": <true|false>,
  "verdict": "consistent" | "inconsistent" | "unsure",
  "quote": "<the exact sentence from the answer that carries the assertion, or empty>",
  "authority": "<the table row you compared against, or empty>"}}

If the answer makes no class/Core/Role/Type assertion at all, use
has_assertion=false and verdict="consistent".

ANSWER:
{answer}
"""


def build_judge_prompt(answer: str, authority_md: str) -> str:
    return _PROMPT.format(authority=authority_md, answer=answer)


def parse_judge_verdict(raw: str) -> dict:
    """把裁判的回复解析成结构化判定。解析不了 ⇒ `unsure` + `parse_error`。"""
    blob = None
    m = _FENCE_RE.search(raw) or _BARE_RE.search(raw)
    if m:
        try:
            blob = json.loads(m.group(1))
        except json.JSONDecodeError:
            blob = None
    if not isinstance(blob, dict):
        return {"has_assertion": None, "verdict": "unsure", "quote": "",
                "authority": "", "parse_error": True, "raw": raw[:400]}
    verdict = blob.get("verdict")
    if verdict not in ("consistent", "inconsistent", "unsure"):
        verdict = "unsure"
    return {"has_assertion": blob.get("has_assertion"),
            "verdict": verdict,
            "quote": blob.get("quote") or "",
            "authority": blob.get("authority") or "",
            "parse_error": False}


def scan_answers(entries, judge, authority_md: str) -> list[dict]:
    """`entries` = [{"id", "answer"}]; `judge` = (prompt) -> raw text。

    单条失败**隔离**: 记成 `unsure` + `error` 继续扫, 不让一个答案毁掉整批
    (照 `compare.py :: _one_completion` 的失败隔离先例)。
    """
    rows = []
    for e in entries:
        prompt = build_judge_prompt(e["answer"], authority_md)
        try:
            v = parse_judge_verdict(judge(prompt))
            v["error"] = None
        except Exception as exc:  # noqa: BLE001 — 逐条隔离
            v = {"has_assertion": None, "verdict": "unsure", "quote": "",
                 "authority": "", "parse_error": False, "error": str(exc)[:200]}
        v["id"] = e["id"]
        rows.append(v)
    return rows
```

- [ ] **Step 4: 跑测试确认通过**

```bash
.venv/bin/python -m pytest scripts/tests/test_class_assertion_scan.py -p no:warnings
.venv/bin/python -m pytest scripts/tests/ -p no:warnings
```
Expected: 单文件 7 passed；全量 **2015 passed, 1 skipped**。⚠ 报实际值。

- [ ] **Step 5: 变异验证（逐条隔离）**

| # | 变异 | 期望 |
|---|---|---|
| M1 | `verdict = "unsure"`（解析失败那支）→ `"consistent"` | `..._marks_unparseable_as_unsure_not_consistent` 红 |
| M2 | `scan_answers` 的 `except` 里 `verdict` 改 `"consistent"` | `..._isolates_a_judge_failure` 红 |
| M3 | `_PROMPT` 里删掉 `{authority}` 占位 | `..._carries_the_whole_authority_table` 红 |
| M4 | `_PROMPT` 里删掉整段 Naming note | `..._supp_naming_variant` 红 |
| M5 | `scan_answers` 改成只扫第一条 | `..._one_row_per_answer` 红（且失败信息应显示 `["q01"] != ["q01","q02"]`） |

- [ ] **Step 6: 提交**

```bash
git add sdtm-rag/eval/prod_wirein/class_assertion_scan.py sdtm-rag/scripts/tests/test_class_assertion_scan.py
git commit -m "feat(verified): (b) 层逐答案裁判扫描器 (解析失败落 unsure 不落 consistent)"
```

---

### Task 4: 对抗抽样 + 人判包生成（零真实调用）

**Files:**
- Create: `sdtm-rag/eval/prod_wirein/build_human_sample.py`
- Test: `sdtm-rag/scripts/tests/test_build_human_sample.py`

**Interfaces:**
- Consumes: Task 3 的扫描结果行（`{"id", "verdict", "quote", "authority", …}`）
- Produces: `pick_sample(rows: list[dict], n_consistent: int = 5, n_flagged: int = 3, seed: int = 0) -> tuple[list[dict], dict]`（返回 8 条 + 构成统计）；`render_human_packet(sample, answers_by_id, authority_md) -> str`

- [ ] **Step 1: 写失败的测试**

```python
"""对抗抽样: 8 条 = 5 条裁判判 consistent (漏网只可能在这里) + 3 条裁判报警。
⚠ 判据预登记里写死了「后者不足 3 条时缺额用前者补满 8 条」——
⛔ 不许因为报警的不够就少判几条。"""
from eval.prod_wirein.build_human_sample import pick_sample, render_human_packet


def _rows(n_consistent, n_flagged):
    rows = [{"id": f"c{i:02d}", "verdict": "consistent", "quote": "", "authority": ""}
            for i in range(n_consistent)]
    rows += [{"id": f"f{i:02d}", "verdict": "inconsistent", "quote": "q", "authority": "a"}
             for i in range(n_flagged)]
    return rows


def test_sample_is_five_consistent_plus_three_flagged():
    sample, comp = pick_sample(_rows(50, 10))
    assert len(sample) == 8
    assert comp == {"consistent": 5, "flagged": 3, "backfilled": 0}
    assert sum(1 for r in sample if r["verdict"] == "consistent") == 5


def test_shortfall_is_backfilled_to_eight_and_recorded():
    """报警只有 1 条时: 仍然 8 条, 缺的 2 条从 consistent 补, 且构成被记下来。"""
    sample, comp = pick_sample(_rows(50, 1))
    assert len(sample) == 8, "⛔ 不许少判"
    assert comp == {"consistent": 7, "flagged": 1, "backfilled": 2}


def test_sample_is_deterministic_for_a_given_seed():
    """同一 seed 必须给同一批 —— 否则人判结果绑不回那次抽样, 证据不可核。"""
    a, _ = pick_sample(_rows(50, 10), seed=7)
    b, _ = pick_sample(_rows(50, 10), seed=7)
    assert [r["id"] for r in a] == [r["id"] for r in b]


def test_different_seeds_give_different_samples():
    """反方向: seed 不生效的实现 (例如忽略 seed 直接取前 5 条) 会让这条红。"""
    a, _ = pick_sample(_rows(50, 10), seed=1)
    b, _ = pick_sample(_rows(50, 10), seed=2)
    assert [r["id"] for r in a] != [r["id"] for r in b]


def test_too_few_rows_fails_loud():
    """总共不足 8 条时 ⛔ 不许悄悄返回短样本 —— 那会让「8/8 PASS」变成「3/3 PASS」。"""
    import pytest
    with pytest.raises(ValueError, match="不足"):
        pick_sample(_rows(2, 1))


def test_packet_shows_answer_and_quote_but_not_the_verdict():
    """⚠ 人判看答案原文 + 权威表, ⛔ 不看裁判的 verdict (预登记判据原文)。
    包里出现 verdict 就等于把答案提前告诉判卷人。"""
    sample, _ = pick_sample(_rows(50, 10))
    md = render_human_packet(sample, {r["id"]: f"ANSWER-{r['id']}" for r in sample},
                             "| Dataset | Class |\n|---|---|\n| AE | Events |")
    assert "ANSWER-c00" in md
    assert "| AE | Events |" in md
    assert "consistent" not in md and "inconsistent" not in md
```

- [ ] **Step 2: 跑测试确认它失败**

```bash
.venv/bin/python -m pytest scripts/tests/test_build_human_sample.py -p no:warnings
```
Expected: collection ERROR。

- [ ] **Step 3: 写实现**

```python
"""对抗抽样与人判包。

⚠ **为什么 5 条抽自 `consistent`**: 人判存在的意义是兜**裁判漏网**, 而漏网按定义
只可能发生在裁判说"干净"的那堆里。只判裁判报警的那些, 结构上测不到漏网 ——
那正是 guardrail v2 那轮真实发生过的失败形状。

⚠ **包里不放 verdict**: 预登记判据写死"人判看答案原文 + 权威表, 不看裁判的 verdict"。
放进去就是把答案提前告诉判卷人, 人判退化成复核裁判。裁判的 `quote` 只用来定位, 故保留。
"""
from __future__ import annotations

import random

_FLAGGED = ("inconsistent", "unsure")


def pick_sample(rows: list[dict], n_consistent: int = 5, n_flagged: int = 3,
                seed: int = 0) -> tuple[list[dict], dict]:
    total = n_consistent + n_flagged
    if len(rows) < total:
        raise ValueError(f"可抽样本不足: 只有 {len(rows)} 条, 需要 {total} 条")
    rng = random.Random(seed)
    clean = [r for r in rows if r["verdict"] == "consistent"]
    flagged = [r for r in rows if r["verdict"] in _FLAGGED]
    take_flagged = min(n_flagged, len(flagged))
    backfilled = n_flagged - take_flagged
    take_clean = n_consistent + backfilled
    if len(clean) < take_clean:
        raise ValueError(f"consistent 一档不足以补满: 有 {len(clean)} 条, 需要 {take_clean} 条")
    sample = rng.sample(clean, take_clean) + rng.sample(flagged, take_flagged)
    comp = {"consistent": take_clean, "flagged": take_flagged, "backfilled": backfilled}
    return sample, comp


def render_human_packet(sample: list[dict], answers_by_id: dict[str, str],
                        authority_md: str) -> str:
    parts = ["# 人判包 — 分类归属 (b) 层", "",
             "> 判据: 无归属断言 ⇒ PASS(N/A) · 有断言且与下表一致 ⇒ PASS · "
             "不一致或权威出处是编的 ⇒ FAIL", "",
             "## 权威表", "", authority_md, "", "## 待判条目", ""]
    for i, r in enumerate(sample, 1):
        parts += [f"### {i}. `{r['id']}`", "",
                  "**裁判定位到的句子** (只用来定位, 不是判定):",
                  "", f"> {r['quote'] or '(裁判未定位到)'}", "",
                  "**答案原文**:", "", answers_by_id.get(r["id"], "(缺)"), "",
                  "**你的判定**: ⬜ PASS / ⬜ FAIL / ⬜ N/A(无断言)", "", "---", ""]
    return "\n".join(parts)
```

- [ ] **Step 4: 跑测试确认通过**

```bash
.venv/bin/python -m pytest scripts/tests/test_build_human_sample.py -p no:warnings
.venv/bin/python -m pytest scripts/tests/ -p no:warnings
```
Expected: 单文件 6 passed；全量 **2021 passed, 1 skipped**。⚠ 报实际值。

- [ ] **Step 5: 变异验证（逐条隔离）**

| # | 变异 | 期望 |
|---|---|---|
| M1 | `backfilled` 那段删掉（报警不足就少抽） | `..._shortfall_is_backfilled_to_eight` 红，且失败信息显示 `len(sample)` 实际值 |
| M2 | `rng.sample(clean, …)` → `clean[:take_clean]`（忽略 seed） | `..._different_seeds_give_different_samples` 红，而 `..._deterministic_for_a_given_seed` **仍绿** ⇒ 两条不可互相替代 |
| M3 | `raise ValueError` → 返回短样本 | `..._too_few_rows_fails_loud` 红 |
| M4 | `render_human_packet` 里加一行 `f"裁判: {r['verdict']}"` | `..._not_the_verdict` 红 |

- [ ] **Step 6: 提交**

```bash
git add sdtm-rag/eval/prod_wirein/build_human_sample.py sdtm-rag/scripts/tests/test_build_human_sample.py
git commit -m "feat(verified): 对抗抽样 + 人判包 (5 条抽自裁判判干净的)"
```

---

### Task 5: ⚠ 真实跑批 — 生成四份答案 + (a) 层判定

**Files:**
- Create: `sdtm-rag/evidence/checkpoints/verified_runs/`（四份 `run_<model>.json` + 四份 `code_grounding_<model>.json`）
- Modify: `sdtm-rag/evidence/checkpoints/verified_spotcheck_2026-09.md`（只填结果表的 (a) 侧列）

**Interfaces:**
- Consumes: 无（用既有 `run_eval.py` 与 `check_code_grounding.py`）
- Produces: 四份落盘答案 JSON（Task 6 的输入）

- [ ] **Step 1: ⛔ 先向用户报成本并等明确同意**

报清三件事再跑：**102 题 × 4 模型 ≈ 408 次 Bedrock 调用**；按 `opus-4-8` 实测 3.8s/短答案估计，长答案会更久，**四轮串行可能 1-3 小时**；走公司额度。
⛔ 用户没明确说跑之前，**不许执行 Step 2**。

- [ ] **Step 2: 逐模型跑批（四条命令，可后台并逐条确认）**

```bash
cd /Users/bojiangzhang/MyProject/sdtm-pedia/sdtm-rag
mkdir -p evidence/checkpoints/verified_runs
for pair in \
  "opus-5:bedrock/converse/global.anthropic.claude-opus-5" \
  "sonnet-5:bedrock/converse/global.anthropic.claude-sonnet-5" \
  "gpt-terra:bedrock/converse/global.openai.gpt-5.6-terra" \
  "gpt-sol:bedrock/converse/global.openai.gpt-5.6-sol" ; do
  name="${pair%%:*}"; model="${pair#*:}"
  .venv/bin/python eval/run_eval.py eval/test_set_v2.yml \
    --model "$model" --guardrail --full-answers \
    --output "evidence/checkpoints/verified_runs/run_${name}.json" \
    2>&1 | tee "evidence/checkpoints/verified_runs/run_${name}.log"
done
```
⛔ **不传 `--temperature`**（spec P5：生产不传；且 Claude 族拒收采样参数会 400）。

- [ ] **Step 3: 算每个模型的失败率（S4 判定）**

```bash
for n in opus-5 sonnet-5 gpt-terra gpt-sol; do
  .venv/bin/python -c "
import json,sys
d=json.load(open('evidence/checkpoints/verified_runs/run_$n.json'))
r=d['results']; ok=sum(1 for x in r if (x.get('answer') or x.get('answer_preview')))
print(f'$n  成功 {ok}/{len(r)}  失败率 {100*(len(r)-ok)/len(r):.1f}%')"
done
```
判定：失败率 **>10%** ⇒ 该模型记 `RUN_FAILED`，`verified` 维持 `false`，且**不进** Task 6。

- [ ] **Step 4: (a) 层 — 码 grounding（零 LLM）**

```bash
for n in opus-5 sonnet-5 gpt-terra gpt-sol; do
  echo "=== $n ==="
  .venv/bin/python eval/prod_wirein/check_code_grounding.py \
    "evidence/checkpoints/verified_runs/run_${n}.json" "$n" | tail -3
done
```
⚠ **第二个参数（`arm`）必须逐模型不同** —— 它同时是输出文件名 `code_grounding_<arm>.json`，传一样的会**互相覆盖**。
跑完把四份 `eval/prod_wirein/code_grounding_<n>.json` 移进 `evidence/checkpoints/verified_runs/`。

- [ ] **Step 5: 按预登记条款判定并填表**

把 `TOTAL codes / ungrounded / NONEXISTENT` 三个数逐模型填进结果表，并逐条对预登记条款：
- **S1**：码总数 **< 20** ⇒ 该模型 (a) 记 `INSUFFICIENT_CODES`，⛔ 不得判 PASS；
- **S2**：四个模型三数**完全相同** ⇒ 结论栏只能写「未发现差异」，⛔ 不得写「四个都可信」；
- (a) PASS ⟺ `ungrounded == 0 and nonexistent == 0` 且未触发 S1。

⛔ **不许因为结果不好看就回头改阈值** —— 判据已在 Task 1 提交。

- [ ] **Step 6: 提交**

```bash
git add sdtm-rag/evidence/checkpoints/verified_runs sdtm-rag/evidence/checkpoints/verified_spotcheck_2026-09.md
git commit -m "evidence(verified): 四模型跑批 + (a) 层码 grounding 结果"
```

---

### Task 6: ⚠ 裁判全扫 + 对抗抽样 → 交人判

**Files:**
- Create: `sdtm-rag/eval/prod_wirein/run_class_scan.py`（把 Task 3/4 的纯函数接到真 litellm 上的薄壳）
- Create: `sdtm-rag/evidence/checkpoints/verified_runs/scan_<model>.json` + `human_packet_<model>.md`

**Interfaces:**
- Consumes: Task 2 的 `load_class_authority`/`authority_table_markdown`、Task 3 的 `scan_answers`、Task 4 的 `pick_sample`/`render_human_packet`、Task 5 的 `run_<model>.json`
- Produces: 四份人判包（交给用户）

- [ ] **Step 1: 写薄壳（无新逻辑，只接线）**

```python
"""把 (b) 层的纯函数接到真 litellm 上。⚠ 本文件是**薄壳**: 判定逻辑全在
class_assertion_scan / build_human_sample 里 (那两个有测试), 这里只负责
读文件、造 judge 可调用对象、写文件。

用法 (在 sdtm-rag/ 下):
  .venv/bin/python eval/prod_wirein/run_class_scan.py <run_xxx.json> <model_name>
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

import litellm  # noqa: E402

from eval.prod_wirein.build_human_sample import pick_sample, render_human_packet  # noqa: E402
from eval.prod_wirein.class_assertion_scan import scan_answers  # noqa: E402
from eval.prod_wirein.class_authority import (  # noqa: E402
    authority_table_markdown, load_class_authority,
)

JUDGE = "bedrock/converse/global.anthropic.claude-opus-4-8"


def _judge(prompt: str) -> str:
    r = litellm.completion(model=JUDGE, messages=[{"role": "user", "content": prompt}],
                           max_tokens=512)
    return r.choices[0].message.content or ""


def main() -> int:
    run_path, name = Path(sys.argv[1]), sys.argv[2]
    out_dir = run_path.parent
    report = json.loads(run_path.read_text(encoding="utf-8"))
    entries = [{"id": r["id"], "answer": r.get("answer") or r.get("answer_preview") or ""}
               for r in report["results"]]
    entries = [e for e in entries if e["answer"]]

    auth = load_class_authority()
    auth_md = authority_table_markdown(auth)
    rows = scan_answers(entries, _judge, auth_md)
    (out_dir / f"scan_{name}.json").write_text(
        json.dumps(rows, indent=2, ensure_ascii=False), encoding="utf-8")

    sample, comp = pick_sample(rows)
    answers = {e["id"]: e["answer"] for e in entries}
    (out_dir / f"human_packet_{name}.md").write_text(
        render_human_packet(sample, answers, auth_md), encoding="utf-8")
    print(f"{name}: scanned={len(rows)}  sample构成={comp}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 2: ⛔ 先向用户报成本并等明确同意**

报清：**≈408 次**裁判调用（`opus-4-8`，实测 3.8s/短提示，本提示含 63 行权威表会更久），走公司额度。
⛔ 没得到明确同意不许跑。

- [ ] **Step 3: 跑四遍**

```bash
cd /Users/bojiangzhang/MyProject/sdtm-pedia/sdtm-rag
for n in opus-5 sonnet-5 gpt-terra gpt-sol; do
  .venv/bin/python eval/prod_wirein/run_class_scan.py \
    "evidence/checkpoints/verified_runs/run_${n}.json" "$n"
done
```

- [ ] **Step 4: 自查抽样构成并记进证据文件**

逐模型把 `sample构成={...}` 抄进证据文件（预登记要求记录实际构成，尤其 `backfilled > 0` 的情形）。

- [ ] **Step 5: 把四份 `human_packet_<model>.md` 交给用户**

⛔ **不许替用户填**。交付时明说：判据是「无断言 ⇒ PASS(N/A) / 与权威表一致 ⇒ PASS / 不一致或权威出处是编的 ⇒ FAIL」，且**看答案原文 + 权威表，不看裁判判定**（包里本来就没有 verdict）。

- [ ] **Step 6: 提交（此时人判尚未回填）**

```bash
git add sdtm-rag/eval/prod_wirein/run_class_scan.py sdtm-rag/evidence/checkpoints/verified_runs
git commit -m "evidence(verified): (b) 层裁判全扫 + 对抗抽样人判包"
```

---

### Task 7: 回填人判、判定、落地、改账

**Files:**
- Modify: `sdtm-rag/evidence/checkpoints/verified_spotcheck_2026-09.md`（填满结果表）
- Modify: `sdtm-rag/server/config.py`（四个 `verified` 与那段注释）
- Modify: `docs/superpowers/specs/2026-09-01-model-switching-design.md`（§3.2 语义 + §9 **D1 改账**）
- Modify: `docs/superpowers/specs/2026-09-02-verified-spotcheck-design.md`（§5 匿名化那句订正）
- Test: `sdtm-rag/scripts/tests/test_model_switching.py`（`test_only_opus5_is_verified` 必然要改）

**Interfaces:**
- Consumes: 用户填回的四份人判包
- Produces: 无

- [ ] **Step 1: 回填人判并按预登记判定**

逐模型：(b) PASS ⟺ 8 条全 PASS（`N/A` 计 PASS）。检查 **S3**：有没有「裁判判 `consistent`、人判 FAIL」的条目——有就在证据文件里写明「⛔ 裁判在该模型上会漏网，结论覆盖面只有已判的 8 条」。
`verified` = (a) PASS **且** (b) PASS。

- [ ] **Step 2: 改 `config.py`**

按判定结果改四个 `verified`，并把那段注释从旧定义改成新定义（spec §4 那三行 + 三条边界）。

- [ ] **Step 3: 改既有测试**

`scripts/tests/test_model_switching.py::test_only_opus5_is_verified` 断言的是「只有 opus-5 为 true」，判定结果一出必然要改。
⚠ 改成**按实际判定结果的绝对值断言**（每个 id 的 `verified` 各钉一次），⛔ 不许改成 `len([m for m in … if m.verified]) >= 1` 这类"随便几个都行"的软断言——那等于把闸拆了。
docstring 里写明新语义 + 指向证据文件。

- [ ] **Step 4: 跑全量**

```bash
cd /Users/bojiangzhang/MyProject/sdtm-pedia/sdtm-rag
.venv/bin/python -m pytest scripts/tests/ -p no:warnings
```
Expected: 2021 passed 上下（Task 2/3/4 各加了测试），⚠ 报实际值。

- [ ] **Step 5: 改账**

- 2026-09-01 spec **§3.2**：`verified` 语义改成新定义；「目前只有 opus-5 为 true」那句按实际结果改写，并注明**旧的 true 是怎么来的、为什么不成立**（P6）。
- 2026-09-01 spec **§9 D1 改账**：`compare_models 未配 + 前端无界面` **两句都不成立**（P1 实测），改成事实 + 指向本轮 spec §2 P1/P2（真正的问题是它接错了管线）。
- 2026-09-02 verified spec **§5**：把"复用 `run_judge` 的 A/B/C 匿名化"订正为"逐答案扫，匿名是结构性自动满足的"。

- [ ] **Step 6: 三套索引 + retro**

worklog `phase_07_rag_kg.md` append · `docs/PROGRESS.md` 更新 · `CLAUDE.md` Key Paths（⚠ 当前 **147/150**，加行前先剪）· 新建 `sdtm-rag/RETROSPECTIVE_verified_spotcheck.md`（规则 C 三段）。

- [ ] **Step 7: 提交**

```bash
git add -A
git commit -m "feat(verified): 四模型抽检落地 — config 更新 + 改账 + retro"
```

---

## Self-Review

**1. Spec coverage**

| spec 条目 | 落在哪 |
|---|---|
| §4 新定义 | Task 1（预登记）+ Task 7 Step 2（写进 config 注释） |
| §5 流程四段 | Task 5（段 1-2）· Task 6（段 3）· Task 7（段 4） |
| §5.1 判据与抽样构成 | Task 1（预登记）+ Task 4（`pick_sample` 实现与闸） |
| §6 预登记 + S1-S4 | Task 1（登记）· S4→Task 5 Step 3 · S1/S2→Task 5 Step 5 · S3→Task 7 Step 1 |
| §7 L1-L5 | 无代码，写在证据文件与 retro 里（Task 7 Step 6） |
| §8 Rule D | Global Constraints + 每个 task 的独立复审（由控制器派） |
| §9 可复跑命令 | Task 5/6 的命令块即是 |

**2. Placeholder scan**：无 TBD / "类似 Task N" / "写测试覆盖以上"。每个代码步骤都给了可粘贴的代码。

**3. Type consistency**：`load_class_authority(kb_root=None) -> dict[str,str]` 在 Task 2 定义，Task 3/6 消费；`authority_table_markdown(mapping) -> str` 同；`scan_answers(entries, judge, authority_md) -> list[dict]` 在 Task 3 定义，Task 6 消费；`pick_sample(rows, n_consistent=5, n_flagged=3, seed=0) -> (list, dict)` 与 `render_human_packet(sample, answers_by_id, authority_md) -> str` 在 Task 4 定义，Task 6 消费。扫描行的键（`id`/`verdict`/`quote`/`authority`）在 Task 3 产出、Task 4 消费，一致。

**4. 一处必须点名的风险**：Task 5/6 是**花钱且不可复算**的（spec L1）。两处都加了「⛔ 先报成本并等明确同意」的步骤，且**跑批前的全部工具与闸都在 Task 2-4 完成并过闸** —— 若仪器有问题，在花第一分钱之前就会暴露。
