# DM2 研读包旁路 (Study Dossier) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 域级映射题 (「本研究哪些数据进 SDTM 的 X 域」) 触发时, 丢弃 study 侧检索结果, 把 PRT 第 4-12 章原文 + 全 EDC 项目一览确定性地喂进上下文, 并在 UI / 存档里如实标出.

**Architecture:** 仿 C2R PDF 通道 (`server/pdf_context.py` + `pdf_trigger.py` + `router.maybe_attach_pdf_pages`) 的三件套: 启动时构建一次的纯数据对象 `StudyDossier`, 零 LLM 纯函数触发器 `decide_dossier`, 一个被 `/api/ask` 与 `/api/ask_stream` 共用的接线 helper `maybe_attach_dossier`. 不触发的路径与主线逐字节相同.

**Tech Stack:** Python 3.14 / FastAPI / pydantic-settings / pytest (`scripts/tests/`), litellm `token_counter`, 原生 JS webchat (`webchat/`, node 测试 `webchat/tests/*.test.mjs`).

**Spec:** `docs/superpowers/specs/2026-09-15-study-dossier-design.md`

## Global Constraints

- 所有命令从 `sdtm-rag/` 跑, 解释器 `.venv/bin/python`; pytest = `.venv/bin/python -m pytest -q scripts/tests/<file>`.
- **红线**: committed 文件 (代码 / 测试 / 文档 / 计划) 里不得出现真实 study OID / 表单名 / 日文 label; 测试用 `st99` / `FA` / `偽フォーム` 之类伪值 (见 `scripts/tests/test_pdf_context_wiring.py` 的 `CARD`). pre-commit 闸 `scripts/precommit_oidscan.py` 会拦. 代称表 (gitignored) `data/study/st01/eval/dm1_codenames.md`.
- **零回归硬闸**: 不触发路径 (总闸 OFF, 或 auto 未命中) 的 `messages` 与本功能引入前逐字节相同. 140q CDISC 集触发数必须为 0.
- **不静默截断**: 研读包超 `dossier_max_chars` 启动报错; 不裁章不裁行.
- **实测必附命令** (memory `feedback_measured_claims_need_commands`): 任何数字进证据文件都要带可复跑命令.
- 失败归档 `sdtm-rag/evidence/failures/dm2_task<N>_attempt_<X>.md`, 不删 (规则 B).
- commit 只用显式路径 (`git add <files>`), 不用 `git add -A`; 每个 task 一个 commit; 提交信息前缀 `feat(rag): DM2 T<N> …`.
- 修复轮不与下一 task 并行 (DM1 RETRO 教训: 共用 git index 撞车).

---

## File Structure

| 文件 | 职责 | Task |
|---|---|---|
| `server/study_dossier.py` (新) | `StudyDossier` 数据类 + `build_dossier()` 纯文件读构建; 章节白名单过滤 / 排序 / part 拼接; 卡片一览行生成 | 1 |
| `eval/prod_wirein/dm2_dossier_tokens.py` (新) | 用真实 settings 构建研读包, 逐可选模型量 token, 打印表 | 2 |
| `sdtm-rag/evidence/checkpoints/dm2_dossier_tokens.md` (新) | Task 2 数字 + 命令 + 用户裁定 | 2 |
| `server/dossier_trigger.py` (新) | `DossierDecision` + `decide_dossier()` 纯函数 | 3 |
| `server/config.py` (改) | `dossier_enabled / dossier_prt_sections / dossier_max_chars / dossier_docs_dir / dossier_cards_dir` | 4 |
| `server/main.py` (改) | `maybe_build_dossier(s)` + `app.state.dossier` | 4 |
| `server/router.py` (改) | `maybe_attach_dossier()` helper; `AskRequest/AskStreamRequest.dossier`; `AskResponse.dossier`; `sources`/`done` 事件 `dossier` 字段; `_DOSSIER_RULES` | 5 |
| `eval/run_eval.py` + `eval/prod_wirein/check_code_grounding.py` (改) | `retrieval_levers["dossier"]` 实收值 (bool), 缺键 = OFF | 6 |
| `webchat/index.html` + `webchat/js/ui.js` + `webchat/app.js` + `webchat/js/dossier.js` (新) + `webchat/tests/dossier.test.mjs` (新) | 三态控件 + 徽章 + 存档 | 7 |
| `eval/prod_wirein/dm2_trigger_sweep.py` (新) + `sdtm-rag/evidence/checkpoints/dm2_gates.md` (新) | L2 零 LLM 闸 | 8 |
| `sdtm-rag/evidence/checkpoints/dm2_dossier_e2e.md` (新) | L3 判据预登记 + 结果 | 9 |
| `sdtm-rag/RETROSPECTIVE_dossier.md` + `_progress_dossier.json` + worklog / PROGRESS / CLAUDE.md Key Path | 收口 | 10 |
| (可选) `server/router.py` prompt cache | 成本优化, e2e 后再做 | 11 |

---

### Task 1: `StudyDossier` 构建器

**Files:**
- Create: `server/study_dossier.py`
- Test: `scripts/tests/test_study_dossier.py`

**Interfaces:**
- Produces:
  ```python
  @dataclass(frozen=True)
  class StudyDossier:
      text: str            # 整段研读包 (spec §3 形状)
      sha: str             # sha256(text) 前 12 位
      chars: int           # len(text)
      sections: tuple[str, ...]   # 进包的 section_number, 已排序, 如 ("4.1","4.2","6.2.3.1")
      n_items: int         # 一览行数
      study: str
      version: str
  def build_dossier(docs_dir: Path, cards_dir: Path, *, sections: Sequence[str],
                    max_chars: int) -> StudyDossier
  class DossierBuildError(RuntimeError): ...
  ```

- [ ] **Step 1: 写失败测试 (tmp 目录造 3 章 + 4 卡)**

`scripts/tests/test_study_dossier.py`:

```python
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
```

- [ ] **Step 2: 跑测试确认失败**

Run: `.venv/bin/python -m pytest -q scripts/tests/test_study_dossier.py`
Expected: FAIL `ModuleNotFoundError: server.study_dossier`

- [ ] **Step 3: 实现 `server/study_dossier.py`**

```python
"""DM2: 研读包 (Study Dossier) —— 域级映射题「整本喂」的原料, 启动时构建一次.

spec: docs/superpowers/specs/2026-09-15-study-dossier-design.md §3
纯文件读, 无 LLM 无网络; 同一输入永远得到同一 text/sha. 超预算抛错不截断.
⚠ 本文件不写任何 study OID / 表单名 / 日文 label.
"""
from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Sequence

_FM_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
_TYPE_RE = re.compile(r"^- 型:\s*(?P<typ>[^\s(]+)(?:\s*\(len [^)]*\))?\s*/\s*(?P<req>\S+)", re.MULTILINE)
_CL_ENTRY_RE = re.compile(r"^\s+-\s+(?P<code>\S+)\s*=\s*(?P<label>.+?)\s*$", re.MULTILINE)


class DossierBuildError(RuntimeError):
    pass


@dataclass(frozen=True)
class StudyDossier:
    text: str
    sha: str
    chars: int
    sections: tuple[str, ...]
    n_items: int
    study: str
    version: str


def _frontmatter(text: str) -> tuple[dict[str, str], str]:
    m = _FM_RE.search(text)
    if not m:
        return {}, text
    fm: dict[str, str] = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip()
    return fm, text[m.end():]


def _sec_key(sec: str) -> tuple[int, ...]:
    return tuple(int(p) for p in sec.split(".") if p.isdigit())


def _load_sections(docs_dir: Path, whitelist: Sequence[str]) -> list[tuple[str, str, str, str]]:
    """→ [(section_number, title, page_range, body)] 按自然序; 多 part 拼成一条."""
    want = set(whitelist)
    parts: dict[str, list[tuple[int, str, str, str]]] = {}
    for p in sorted(docs_dir.glob("*.md")):
        fm, body = _frontmatter(p.read_text(encoding="utf-8"))
        if fm.get("doc_type") != "protocol_section":
            continue
        sec = fm.get("section_number", "")
        if sec.split(".")[0] not in want:
            continue
        lines = body.strip("\n").splitlines()
        title = next((l.strip() for l in lines if l.strip()), sec)
        rest = "\n".join(lines[1:]).strip("\n") if lines else ""
        pages = f"(p.{fm.get('page_start','?')}-{fm.get('page_end','?')})"
        parts.setdefault(sec, []).append((int(fm.get("part", "1") or 1), title, pages, rest))
    out = []
    for sec in sorted(parts, key=_sec_key):
        ps = sorted(parts[sec], key=lambda t: t[0])
        title, pages = ps[0][1], ps[0][2]
        body = "\n".join(t[3] for t in ps)
        out.append((sec, title, pages, body))
    return out


def _load_items(cards_dir: Path) -> list[tuple[str, int, str]]:
    """→ [(form_oid, source_row, line)] 排序后返回; 只取 doc_type=field_card."""
    rows = []
    for p in cards_dir.glob("*.md"):
        fm, body = _frontmatter(p.read_text(encoding="utf-8"))
        if fm.get("doc_type") != "field_card":
            continue
        title = next((l[2:].strip() for l in body.splitlines() if l.startswith("# ")), p.stem)
        m = _TYPE_RE.search(body)
        typ = f"{m['typ']} {m['req']}" if m else "?"
        choices = " ".join(f"{e['code']}={e['label']}" for e in _CL_ENTRY_RE.finditer(body))
        line = f"{title} | {typ}" + (f" | {choices}" if choices else "")
        try:
            row = int(fm.get("source_row", "0") or 0)
        except ValueError:
            row = 0
        rows.append((fm.get("form_oid", ""), row, line))
    rows.sort(key=lambda t: (t[0], t[1], t[2]))
    return rows


def build_dossier(docs_dir: Path, cards_dir: Path, *, sections: Sequence[str],
                  max_chars: int) -> StudyDossier:
    secs = _load_sections(Path(docs_dir), sections)
    if not secs:
        raise DossierBuildError(f"dossier: 0 sections matched whitelist {list(sections)} in {docs_dir}")
    items = _load_items(Path(cards_dir))
    if not items:
        raise DossierBuildError(f"dossier: 0 field cards in {cards_dir}")
    fm0, _ = _frontmatter(next(Path(cards_dir).glob("*.md")).read_text(encoding="utf-8"))
    study, version = fm0.get("study", "?"), fm0.get("version", "?")
    lo, hi = sections[0], sections[-1]
    buf = [f"## A. 研究計画書 (PRT) 抜粋: 第 {lo}-{hi} 章"]
    for sec, title, pages, body in secs:
        buf.append(f"### {title}  {pages}\n{body}")
    buf.append(f"## B. EDC 項目一覧 (全 {len(items)} 件; 表単 / 項目 / OID / 型 / 選択肢)")
    buf.extend(line for _, _, line in items)
    body_text = "\n\n".join(buf)
    sha = hashlib.sha256(body_text.encode("utf-8")).hexdigest()[:12]
    head = (f"# 【本研究 研読パッケージ】 (study={study}, version={version}, sha={sha}, "
            f"{len(secs)} 章 / {len(items)} 項目)\n\n")
    text = head + body_text
    if len(text) > max_chars:
        raise DossierBuildError(
            f"dossier: {len(text)} chars > max_chars={max_chars}; 收窄 dossier_prt_sections, 不截断")
    return StudyDossier(text=text, sha=sha, chars=len(text),
                        sections=tuple(s for s, *_ in secs), n_items=len(items),
                        study=study, version=version)
```

- [ ] **Step 4: 跑测试确认通过**

Run: `.venv/bin/python -m pytest -q scripts/tests/test_study_dossier.py`
Expected: 5 passed. 若 `test_sections_filtered_ordered_and_parts_joined` 因 part 拼接字符串形状失败, 调整断言为实际 `"P1\nP2"` (实现用 `"\n".join`), 不改实现.

- [ ] **Step 5: Commit**

```bash
git add server/study_dossier.py scripts/tests/test_study_dossier.py
git commit -m "feat(rag): DM2 T1 StudyDossier 构建器 (PRT 白名单章 + EDC 一览, 纯文件读, 超预算抛错)"
```

---

### Task 2: 研读包 token 计量 (硬前置闸, 用户裁范围)

**Files:**
- Create: `eval/prod_wirein/dm2_dossier_tokens.py`
- Create: `evidence/checkpoints/dm2_dossier_tokens.md`

**Interfaces:**
- Consumes: `build_dossier` (Task 1); `settings.selectable_models` (`server/config.py:59`), `settings.study_kb_root` (cards 目录), docs 目录 = `study_kb_root.parent / "docs"`.
- Produces: 数字 + 用户对范围的裁定 (写进 checkpoint, 后续 Task 4 的默认白名单以此为准).

- [ ] **Step 1: 写脚本**

```python
"""DM2 T2: 研读包到底多少 token —— 每个可选模型各量一次, 数字进 evidence.

跑 (从 sdtm-rag/):
  .venv/bin/python eval/prod_wirein/dm2_dossier_tokens.py [--sections 4,5,6,7,8,9,10,11,12] [--no-choices]
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from litellm import token_counter  # noqa: E402

from server.config import settings  # noqa: E402
from server.study_dossier import build_dossier  # noqa: E402


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--sections", default="4,5,6,7,8,9,10,11,12")
    ap.add_argument("--max-chars", type=int, default=400_000)
    args = ap.parse_args()
    cards = Path(settings.study_kb_root)
    docs = cards.parent / "docs"
    d = build_dossier(docs, cards, sections=args.sections.split(","), max_chars=args.max_chars)
    a_end = d.text.index("## B. EDC")
    print(f"sections={args.sections}  chars={d.chars}  (A={a_end}, B={d.chars - a_end})  "
          f"n_sections={len(d.sections)} n_items={d.n_items} sha={d.sha}")
    print(f"{'model id':10s} {'litellm model':60s} tokens")
    for m in settings.selectable_models:
        try:
            n = token_counter(model=m.model, text=d.text)
        except Exception as e:  # noqa: BLE001 — 记下来, 不让一个模型的 tokenizer 缺失挡住其它
            n = f"ERR {type(e).__name__}"
        print(f"{m.id:10s} {m.model:60s} {n}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 2: 跑 (默认范围) 并记录**

Run: `.venv/bin/python eval/prod_wirein/dm2_dossier_tokens.py`
Expected: 一行 chars 汇总 + 四行模型 token. 若某模型 `ERR`, 在 checkpoint 注明 litellm 对该 id 无 tokenizer, 用 Claude 档数字代表.

- [ ] **Step 3: 写 checkpoint (数字 + 命令), 交用户裁**

`evidence/checkpoints/dm2_dossier_tokens.md`:

```markdown
# DM2 — T2 研读包 token 计量 (2026-09-15)

复跑: `.venv/bin/python eval/prod_wirein/dm2_dossier_tokens.py`

| 范围 | chars (A/B) | opus-5 | sonnet-5 | gpt-terra | gpt-sol |
|---|---|---|---|---|---|
| s4-s12 + 一览含选择肢 | … | … | … | … | … |

## 裁定规则 (spec §3)
Claude 档 ≤ 150K token → 按默认范围实施. 否则由用户点收窄顺序: (1) 一览去选择肢 (2) 收白名单.

## 用户裁定
(待填: 范围 / 日期)
```

- [ ] **Step 4: 用 AskUserQuestion 把数字给用户, 拿到裁定后写回 checkpoint**

若 Claude 档 > 150K: 选项 = 「去选择肢」/「白名单收到 s4-s8+s11」/「照喂 (接受溢出风险, 只用 1M 档模型)」. 若 ≤ 150K: 只需用户确认「按默认范围实施」.

- [ ] **Step 5: Commit**

```bash
git add eval/prod_wirein/dm2_dossier_tokens.py evidence/checkpoints/dm2_dossier_tokens.md
git commit -m "feat(rag): DM2 T2 研读包 token 计量 + 用户范围裁定"
```

---

### Task 3: 触发器 `decide_dossier`

**Files:**
- Create: `server/dossier_trigger.py`
- Test: `scripts/tests/test_dossier_trigger.py`

**Interfaces:**
- Consumes: 域码识别函数 (由调用方注入; 生产用 `app.state.rag._structured_lookup._query_domains`, 见 `server/structured_lookup.py:399`).
- Produces:
  ```python
  @dataclass(frozen=True)
  class DossierDecision:
      attach: bool
      reason: str   # "disabled" | "forced_off" | "forced_on" | "auto:domain+scope" | "auto:no_match"
      domains: tuple[str, ...]
  DossierMode = Literal["auto", "on", "off"]
  def decide_dossier(question: str, mode: DossierMode, enabled: bool,
                     query_domains: Callable[[str], list[str]]) -> DossierDecision
  ```

- [ ] **Step 1: 写失败测试 (判定表)**

`scripts/tests/test_dossier_trigger.py`:

```python
"""DM2 T3: 触发器是纯函数, 判定表可枚举. 域码识别是注入的 (D1 口径), 这里只测组合逻辑
和范围词类; 不重测 _query_domains 本身 (它有自己的测试)."""
import pytest
from server.dossier_trigger import decide_dossier

def _qd_hit(q): return ["DS"]
def _qd_none(q): return []

@pytest.mark.parametrize("q", [
    "本研究中，哪些数据适合进入 sdtm 的 ds domain？",
    "この試験で収集しているデータのうち、SDTM の DS ドメインに入れるべきものはどれですか？",
    "Which data collected in our study should go into the Disposition dataset?",
    "In this study, which EDC items belong in DS?",
    "当試験の EDC 項目で DS に入るもの",
])
def test_auto_fires_on_domain_plus_scope(q):
    d = decide_dossier(q, "auto", True, _qd_hit)
    assert d.attach and d.reason == "auto:domain+scope" and d.domains == ("DS",)

@pytest.mark.parametrize("q", [
    "DS 域有哪些变量？",                       # 域码但无范围词 (纯 CDISC 题)
    "What are the DSCAT values?",
])
def test_auto_quiet_without_scope(q):
    d = decide_dossier(q, "auto", True, _qd_hit)
    assert not d.attach and d.reason == "auto:no_match"

def test_auto_quiet_without_domain():
    d = decide_dossier("本研究の登録手順を教えて", "auto", True, _qd_none)
    assert not d.attach and d.reason == "auto:no_match" and d.domains == ()

def test_forced_on_and_off_override_auto():
    assert decide_dossier("何でも", "on", True, _qd_none).reason == "forced_on"
    assert decide_dossier("本研究 DS", "off", True, _qd_hit).reason == "forced_off"

def test_master_switch_beats_forced_on():
    d = decide_dossier("本研究 DS", "on", False, _qd_hit)
    assert not d.attach and d.reason == "disabled"

def test_query_domains_exception_is_quiet_not_500():
    def boom(q): raise RuntimeError("x")
    d = decide_dossier("本研究 DS", "auto", True, boom)
    assert not d.attach and d.reason == "auto:no_match"
```

- [ ] **Step 2: 跑测试确认失败**

Run: `.venv/bin/python -m pytest -q scripts/tests/test_dossier_trigger.py`
Expected: FAIL `ModuleNotFoundError`

- [ ] **Step 3: 实现**

`server/dossier_trigger.py`:

```python
"""DM2: 研读包要不要挂 —— 纯函数, 零 LLM (与 pdf_trigger 同一纪律: 可枚举可复现).

spec §4. 范围词是**词类** (研究指代 + study/試験/研究 / EDC), 不是某题的字面; 不加表单名/项目名.
域码识别注入 (D1 `_query_domains`), 这里不重写正则.
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Callable, Literal

DossierMode = Literal["auto", "on", "off"]

_SCOPE_RE = re.compile(
    r"本研究|本試験|当試験|当研究|この試験|この研究|本 ?study|our study|this study|in our\b|EDC",
    re.IGNORECASE,
)


@dataclass(frozen=True)
class DossierDecision:
    attach: bool
    reason: str
    domains: tuple[str, ...] = ()


def decide_dossier(question: str, mode: DossierMode, enabled: bool,
                   query_domains: Callable[[str], list[str]]) -> DossierDecision:
    if not enabled:
        return DossierDecision(False, "disabled")
    if mode == "off":
        return DossierDecision(False, "forced_off")
    if mode == "on":
        return DossierDecision(True, "forced_on")
    try:
        domains = tuple(query_domains(question))
    except Exception:  # noqa: BLE001 — 识别炸了 = 不触发, 不是 500
        domains = ()
    if domains and _SCOPE_RE.search(question):
        return DossierDecision(True, "auto:domain+scope", domains)
    return DossierDecision(False, "auto:no_match", domains)
```

- [ ] **Step 4: 跑测试确认通过**

Run: `.venv/bin/python -m pytest -q scripts/tests/test_dossier_trigger.py`
Expected: 11 passed

- [ ] **Step 5: Commit**

```bash
git add server/dossier_trigger.py scripts/tests/test_dossier_trigger.py
git commit -m "feat(rag): DM2 T3 decide_dossier 纯函数触发器 (域码 D1 注入 + 范围词类)"
```

---

### Task 4: 配置 + 启动装配

**Files:**
- Modify: `server/config.py` (在 `pdf_annotated_path` 之后, `# Server` 之前, 约 line 289)
- Modify: `server/main.py` (`maybe_build_pdf_context` 之后新增函数; `app.state.pdf_context = …` 之后接一行)
- Test: `scripts/tests/test_main_dossier_wiring.py`

**Interfaces:**
- Consumes: `build_dossier`, `DossierBuildError` (T1).
- Produces: `settings.dossier_enabled: bool`, `dossier_prt_sections: list[str]`, `dossier_max_chars: int`, `dossier_docs_dir: Path` (property), `dossier_cards_dir: Path` (property); `main.maybe_build_dossier(s) -> StudyDossier | None`; `app.state.dossier`.

- [ ] **Step 1: 写失败测试**

`scripts/tests/test_main_dossier_wiring.py`:

```python
"""DM2 T4: 总闸 OFF → None (一行不跑); ON → 构建; ON 但目录缺/超限 → 启动 RuntimeError (fail-loud)."""
import pytest
from server import main as main_mod
from server.config import Settings

def test_off_returns_none_without_touching_disk(tmp_path):
    s = Settings(dossier_enabled=False, dossier_docs_dir_override=str(tmp_path / "nope"),
                 dossier_cards_dir_override=str(tmp_path / "nope"))
    assert main_mod.maybe_build_dossier(s) is None

def test_on_missing_dir_fails_loud(tmp_path):
    s = Settings(dossier_enabled=True, dossier_docs_dir_override=str(tmp_path / "nope"),
                 dossier_cards_dir_override=str(tmp_path / "nope"))
    with pytest.raises(RuntimeError, match="dossier"):
        main_mod.maybe_build_dossier(s)

def test_on_builds(tmp_path):
    docs = tmp_path / "docs"; cards = tmp_path / "cards"; docs.mkdir(); cards.mkdir()
    (docs / "a.md").write_text("---\ndoc_type: protocol_section\nsection_number: 4.1\npart: 1\n---\n\n4.1 T\nB\n", encoding="utf-8")
    (cards / "c.md").write_text("---\nstudy: st99\nversion: V\ndoc_type: field_card\nform_oid: FA\nsource_row: 1\n---\n\n# [偽 FA] x (I) \n- 型: text (len 1) / 必須\n", encoding="utf-8")
    s = Settings(dossier_enabled=True, dossier_prt_sections=["4"],
                 dossier_docs_dir_override=str(docs), dossier_cards_dir_override=str(cards))
    d = main_mod.maybe_build_dossier(s)
    assert d is not None and d.sections == ("4.1",) and d.n_items == 1

def test_default_settings_have_dossier_on_with_s4_to_s12():
    s = Settings()
    assert s.dossier_enabled is True
    assert s.dossier_prt_sections == ["4", "5", "6", "7", "8", "9", "10", "11", "12"]
```

- [ ] **Step 2: 跑测试确认失败**

Run: `.venv/bin/python -m pytest -q scripts/tests/test_main_dossier_wiring.py`
Expected: FAIL (`Settings` 拒绝未知字段 / `maybe_build_dossier` 不存在)

- [ ] **Step 3: 加配置 (`server/config.py`, 紧接 `pdf_annotated_path: str = ""` 之后)**

```python
    # ── DM2 研读包旁路 (docs/superpowers/specs/2026-09-15-study-dossier-design.md) ──
    # 域级映射题 (「本研究哪些数据进 X 域」) 触发时: 丢 study 侧 top-k, 把 PRT 白名单章原文 +
    # 全 EDC 项目一览整段喂进上下文. 默认 **ON** (用户裁定 2026-09-15); 不触发的路径与
    # 引入前逐字节相同 (test_router_dossier_wiring 钉). kill switch = 这一行.
    dossier_enabled: bool = True
    # PRT 章号白名单 (匹配 section_number 首段). 范围由 T2 token 计量 + 用户裁定
    # (evidence/checkpoints/dm2_dossier_tokens.md). 改这里 = 改研读包 sha, 存档徽章会变.
    dossier_prt_sections: list[str] = ["4", "5", "6", "7", "8", "9", "10", "11", "12"]
    # 超限 = 启动报错, 不截断 (spec §3). 日文 ≈ 1 字 1 token, 这个上限就是 token 上限量级.
    dossier_max_chars: int = 200_000
    # 空 = 从 study_kb_root (cards/) 推导: docs = cards 的兄弟目录. 与 pdf_* 同一纪律,
    # 显式给值可让 self-contained service dir 或测试 tmp 目录也能跑.
    dossier_docs_dir_override: str = ""
    dossier_cards_dir_override: str = ""
```

并在 `pdf_context_cache_dir` property 附近加:

```python
    @property
    def dossier_docs_dir(self) -> Path:
        if self.dossier_docs_dir_override:
            return Path(self.dossier_docs_dir_override)
        return Path(self.study_kb_root).parent / "docs"

    @property
    def dossier_cards_dir(self) -> Path:
        if self.dossier_cards_dir_override:
            return Path(self.dossier_cards_dir_override)
        return Path(self.study_kb_root)
```

- [ ] **Step 4: 加装配 (`server/main.py`, 紧接 `maybe_build_pdf_context` 函数之后)**

```python
def maybe_build_dossier(s):
    """DM2 研读包. OFF → None (一行不跑). ON 且目录缺 / 0 章 / 超 max_chars → **起动失败**:
    静默 None 会得到「开了却一题都不挂」的无症状状态 (与 maybe_build_pdf_context 同一理由)."""
    if not s.dossier_enabled:
        return None
    from server.study_dossier import DossierBuildError, build_dossier
    docs, cards = s.dossier_docs_dir, s.dossier_cards_dir
    if not docs.is_dir() or not cards.is_dir():
        raise RuntimeError(f"dossier_enabled=true 但目录缺: docs={docs} cards={cards}")
    try:
        return build_dossier(docs, cards, sections=list(s.dossier_prt_sections),
                             max_chars=s.dossier_max_chars)
    except DossierBuildError as e:
        raise RuntimeError(f"dossier_enabled=true 但构建失败: {e}") from e
```

在 `app.state.pdf_context = maybe_build_pdf_context(s)` 块之后:

```python
    # DM2 研读包 (默认 ON). 构建一次, 请求期只读.
    app.state.dossier = maybe_build_dossier(s)
    if app.state.dossier is not None:
        d = app.state.dossier
        log.info("dossier", sha=d.sha, chars=d.chars, sections=len(d.sections), items=d.n_items)
```

- [ ] **Step 5: 跑测试 + 全量 pytest 确认通过**

Run: `.venv/bin/python -m pytest -q scripts/tests/test_main_dossier_wiring.py && .venv/bin/python -m pytest -q scripts/tests -x -q 2>&1 | tail -3`
Expected: 4 passed; 全量绿 (其它 `Settings()` 用例不受影响, 因为默认目录存在于本仓).
⚠ 若全量里有测试用 `Settings()` 且 `study_kb_root` 指向不存在目录 → `maybe_build_dossier` 只在 `main.create_app` 里调, `Settings()` 本身不构建, 应无影响; 若有影响, 记 failures 后改测试 fixture 传 `dossier_enabled=False`, 不改默认值.

- [ ] **Step 6: 真启动一次 (fail-loud 自检)**

Run: `.venv/bin/python -c "from server.main import create_app; a=create_app(); d=a.state.dossier; print(d.sha, d.chars, len(d.sections), d.n_items)"`
Expected: 打印 sha / chars (≤ 200000) / 章数 / 959. 若 chars 超限报错 → 这正是 T2 该裁的, 回 T2 checkpoint 按用户裁定改 `dossier_prt_sections` 默认值.

- [ ] **Step 7: Commit**

```bash
git add server/config.py server/main.py scripts/tests/test_main_dossier_wiring.py
git commit -m "feat(rag): DM2 T4 dossier 配置 (默认 ON, s4-s12, 200K 上限) + 启动 fail-loud 装配"
```

---

### Task 5: router 接线 (`/api/ask` + `/api/ask_stream`)

**Files:**
- Modify: `server/router.py`:
  - `AskRequest` (line ~110-140, 与 `model: str = "default"` 同处) 与 `AskStreamRequest` (line 472-482): 加 `dossier: Literal["auto", "on", "off"] = "auto"`
  - `AskResponse` (line ~163 `pdf_pages` 之后): 加 `dossier: dict | None = None`
  - 新增 `_DOSSIER_RULES` 常量 (紧接 `_PDF_SOURCE_RULE` 之后) 与 `maybe_attach_dossier()` (紧接 `maybe_attach_pdf_pages` 之后)
  - `ask` (line 284-470) 与 `ask_stream` (line 486-835) 各接线 4 处
- Test: `scripts/tests/test_router_dossier_wiring.py`

**Interfaces:**
- Consumes: `app.state.dossier: StudyDossier | None` (T4), `decide_dossier` (T3), `app.state.rag._structured_lookup` (可能为 None → `query_domains` 返回 `[]`), `app.state.federation` (`FederatedEngine`, 有 `.cdisc` 引擎与 `.top_k`).
- Produces:
  ```python
  def maybe_attach_dossier(request, question: str, chunks, routed: str | None, mode: str
                           ) -> tuple[list, str | None, str | None, dict | None]:
      """→ (chunks, routed, dossier_block, dossier_info). 通道 OFF → 原样 (…, None, None)."""
  _DOSSIER_RULES: str
  ```
  `dossier_info` 形状 (同时进 `AskResponse.dossier` / SSE `sources` 与 `done` 事件): `{"attached": bool, "reason": str, "domains": [...], "sha": str, "sections": [...], "chars": int}`; 通道 OFF 时整个字段 `None`.

- [ ] **Step 1: 写失败测试**

`scripts/tests/test_router_dossier_wiring.py`:

```python
"""DM2 T5: 接线守两方向 (与 test_pdf_context_wiring 同构):
  ① app.state.dossier is None (总闸 OFF) → messages / sources / done 与引入前逐字节同, dossier 字段 null
  ② 挂上时: study chunks 从 sources 消失, routed=both, context 含包头, system 多且只多一条规则句,
     done/sources/AskResponse 的 dossier.attached=True; auto 未命中时 attached=False 带 reason
"""
from __future__ import annotations
import json
from types import SimpleNamespace
from fastapi import FastAPI
from fastapi.testclient import TestClient
from server.config import Settings
from server.router import _DOSSIER_RULES, api_router
from server.study_dossier import StudyDossier

Q_MAP = "本研究中，哪些数据适合进入 sdtm 的 ds domain？"
Q_CDISC = "DS 域有哪些变量？"


def _chunk(i, corpus, ft="assumptions"):
    return SimpleNamespace(chunk_id=f"{corpus}{i}", source=f"{corpus}/{i}.md", domain="DS",
                           file_type=ft, section=None, similarity=0.5, text="t", corpus=corpus)


class _Cdisc:
    system_prompt = "SYS"
    def __init__(self): self._structured_lookup = SimpleNamespace(_query_domains=lambda q: ["DS"] if "ds" in q.lower() else [])
    def retrieve(self, q, *, domain=None, file_type=None, top_k=None): return [_chunk(i, "cdisc") for i in range(2)]
    def format_context(self, chunks): return "CD:" + ",".join(c.chunk_id for c in chunks)
    def build_messages(self, q, ctx, history=None):
        return [{"role": "system", "content": "SYS"}, {"role": "user", "content": f"CTX={ctx}\nQ={q}"}]


class _Fed:
    top_k = 4
    def __init__(self, cdisc): self.cdisc = cdisc
    def retrieve(self, q, *, corpus="auto", top_k=None, domain=None, file_type=None):
        return [_chunk(0, "cdisc"), _chunk(1, "cdisc"), _chunk(0, "study", "field_card"), _chunk(1, "study", "field_card")], "both"
    def format_context(self, chunks):
        return "FED:" + ",".join(c.chunk_id for c in chunks)
    def build_messages(self, q, ctx, history=None, *, corpus):
        return [{"role": "system", "content": f"SYS[{corpus}]"}, {"role": "user", "content": f"CTX={ctx}\nQ={q}"}]


class _Router:
    def __init__(self): self.messages = None
    def completion(self, model, messages, **kw):
        self.messages = messages
        return SimpleNamespace(model="m", choices=[SimpleNamespace(message=SimpleNamespace(content="ans"), finish_reason="stop")],
                               usage=SimpleNamespace(prompt_tokens=1, completion_tokens=1, total_tokens=2))
    async def acompletion(self, model, messages, stream=False, **kw):
        self.messages = messages
        async def agen():
            yield SimpleNamespace(model="m", usage=None, choices=[SimpleNamespace(delta=SimpleNamespace(content="ans"), finish_reason="stop")])
        return agen()


DOSSIER = StudyDossier(text="# 【本研究 研読パッケージ】 X", sha="abc", chars=17, sections=("4.1",), n_items=1, study="st99", version="V")


def _client(dossier):
    app = FastAPI(); app.include_router(api_router)
    cd = _Cdisc()
    app.state.rag = cd; app.state.federation = _Fed(cd); app.state.llm_router = _Router()
    app.state.settings = Settings(dossier_enabled=dossier is not None)
    app.state.dossier = dossier; app.state.pdf_context = None; app.state.study_lookup = None
    app.state.answerer = None
    return TestClient(app), app


def _done(text):
    return json.loads(text.split("event: done\ndata: ")[1].split("\n\n")[0])

def _sources(text):
    return json.loads(text.split("event: sources\ndata: ")[1].split("\n\n")[0])


def test_off_is_byte_identical_and_reports_null():
    c, app = _client(None)
    r = c.post("/api/ask", json={"question": Q_MAP, "history": []})
    assert r.json()["dossier"] is None
    assert app.state.llm_router.messages == [{"role": "system", "content": "SYS[both]"},
                                              {"role": "user", "content": f"CTX=FED:cdisc0,cdisc1,study0,study1\nQ={Q_MAP}"}]
    t = c.post("/api/ask_stream", json={"question": Q_MAP, "history": []}).text
    assert _done(t)["dossier"] is None and _sources(t)["dossier"] is None
    assert len(_sources(t)["sources"]) == 4


def test_auto_attach_drops_study_chunks_and_adds_rule_once():
    c, app = _client(DOSSIER)
    t = c.post("/api/ask_stream", json={"question": Q_MAP, "history": []}).text
    src = _sources(t)
    assert [s["chunk_id"] for s in src["sources"]] == ["cdisc0", "cdisc1"]
    assert src["routed_corpus"] == "both"
    assert src["dossier"] == {"attached": True, "reason": "auto:domain+scope", "domains": ["DS"],
                              "sha": "abc", "sections": ["4.1"], "chars": 17}
    assert _done(t)["dossier"]["attached"] is True
    msgs = app.state.llm_router.messages
    assert msgs[0]["content"] == "SYS[both]" + _DOSSIER_RULES
    assert msgs[0]["content"].count(_DOSSIER_RULES) == 1
    assert msgs[-1]["content"] == f"CTX=FED:cdisc0,cdisc1\n\n{DOSSIER.text}\nQ={Q_MAP}"


def test_auto_no_match_reports_reason_and_leaves_messages_alone():
    c, app = _client(DOSSIER)
    r = c.post("/api/ask", json={"question": Q_CDISC, "history": []})
    assert r.json()["dossier"] == {"attached": False, "reason": "auto:no_match", "domains": ["DS"],
                                   "sha": "abc", "sections": ["4.1"], "chars": 17}
    assert app.state.llm_router.messages[0]["content"] == "SYS[both]"
    assert len(r.json()["sources"]) == 4


def test_forced_on_and_off():
    c, _ = _client(DOSSIER)
    assert c.post("/api/ask", json={"question": Q_CDISC, "history": [], "dossier": "on"}).json()["dossier"]["reason"] == "forced_on"
    assert c.post("/api/ask", json={"question": Q_MAP, "history": [], "dossier": "off"}).json()["dossier"]["reason"] == "forced_off"


def test_bad_mode_is_422():
    c, _ = _client(DOSSIER)
    assert c.post("/api/ask", json={"question": Q_MAP, "history": [], "dossier": "yes"}).status_code == 422


def test_study_routed_gets_cdisc_side_refetched():
    c, app = _client(DOSSIER)
    app.state.federation.retrieve = lambda q, **kw: ([_chunk(0, "study", "field_card")], "study")
    t = c.post("/api/ask_stream", json={"question": Q_MAP, "history": []}).text
    src = _sources(t)
    assert src["routed_corpus"] == "both"
    assert [s["chunk_id"] for s in src["sources"]] == ["cdisc0", "cdisc1"]
```

- [ ] **Step 2: 跑测试确认失败**

Run: `.venv/bin/python -m pytest -q scripts/tests/test_router_dossier_wiring.py`
Expected: FAIL `ImportError: _DOSSIER_RULES`

- [ ] **Step 3: 实现 — 常量 + helper (紧接 `maybe_attach_pdf_pages` 之后)**

```python
_DOSSIER_RULES = (
    "\n\n## Study dossier rules\n"
    "- The context ends with 【本研究 研読パッケージ】: this study's protocol (PRT) chapters "
    "verbatim (part A) and the COMPLETE list of EDC items (part B). Study-side retrieval was "
    "skipped on purpose: part B is exhaustive, so if an item is not there, it does not exist.\n"
    "- Domain-level mapping questions: (1) enumerate the record categories the standard defines "
    "for the domain from 【標準 CDISC】; (2) for each category scan part B form by form for "
    "candidate items (status / date / reason), quoting each as `[form OID] item (OID)` exactly "
    "as written; (3) when the PRT defines the event (完了の定義 / 中止規準 / 登録手順 …), cite "
    "the section number from part A; (4) every EDC→SDTM assignment is inference — label it "
    "(推測); (5) say explicitly which categories have no candidate item.\n"
)


def maybe_attach_dossier(request: Request, question: str, chunks, routed: str | None, mode: str):
    """DM2: 域级映射题触发时, 丢 study 侧 chunks, 返回研读包文本块供拼进 context.

    → (chunks, routed, dossier_block | None, dossier_info | None).
    通道 OFF (`app.state.dossier is None`) → 原样返回, info=None —— 「OFF 与引入前逐位同一」由
    这一行早期 return 担保. 跑了但没挂 → info.attached=False 带 reason (与 pdf 通道 None/[]
    的区分同一教训). /api/ask 与 /api/ask_stream 都调这一个函数.
    """
    dossier = getattr(request.app.state, "dossier", None)
    if dossier is None:
        return chunks, routed, None, None
    from server.dossier_trigger import decide_dossier

    lookup = getattr(getattr(request.app.state, "rag", None), "_structured_lookup", None)
    query_domains = lookup._query_domains if lookup is not None else (lambda q: [])
    s = request.app.state.settings
    decision = decide_dossier(question, mode, s.dossier_enabled, query_domains)
    info = {"attached": decision.attach, "reason": decision.reason,
            "domains": list(decision.domains), "sha": dossier.sha,
            "sections": list(dossier.sections), "chars": dossier.chars}
    if not decision.attach:
        return chunks, routed, None, info
    fed = getattr(request.app.state, "federation", None)
    if fed is not None and routed == "study":
        # study 单库路由下没有 CDISC 定义段 (D2), 补取 CDISC 侧; 席位口径与 both 相同 (k/2 上取整)
        import math
        k_each = math.ceil((fed.top_k or 15) / 2)
        cd = fed.cdisc.retrieve(question, top_k=k_each)
        for c in cd:
            c.corpus = "cdisc"
        chunks = list(cd)
    else:
        chunks = [c for c in chunks if getattr(c, "corpus", None) != "study"]
    if fed is not None:
        routed = "both"
    log.info("dossier_attached", reason=decision.reason, domains=list(decision.domains),
             sha=dossier.sha, chars=dossier.chars, kept_chunks=len(chunks))
    return chunks, routed, dossier.text, info
```

- [ ] **Step 4: 实现 — 请求/响应字段**

`AskRequest` 与 `AskStreamRequest` 各加 (紧接 `model: str = "default"` 之后):

```python
    # DM2 研读包: auto = 域码+范围词自动判; on/off = 手动强开/强关 (总闸 OFF 时 on 也不挂).
    dossier: Literal["auto", "on", "off"] = "auto"
```

`AskResponse` 加 (紧接 `pdf_pages` 之后):

```python
    # DM2 研读包. None = 通道没跑 (总闸 OFF); dict = 跑了 (attached 说挂没挂, reason 说为何).
    dossier: dict | None = None
```

- [ ] **Step 5: 实现 — `ask` 接线 (line ~328-346 之间)**

在 `engine = fed if fed is not None else rag` **之前**插:

```python
    chunks, routed, dossier_block, dossier_info = maybe_attach_dossier(
        request, body.question, chunks, routed, body.dossier)
```

`context = engine.format_context(chunks)` 与 `_NO_CONTEXT` 处理之后、`augment_context` 之前插:

```python
    if dossier_block:
        context = (dossier_block if (not context or context == _NO_CONTEXT)
                   else context + "\n\n" + dossier_block)
```

`messages = …build_messages(…)` 之后、`maybe_attach_pdf_pages` 之前插:

```python
    if dossier_block:
        messages[0]["content"] += _DOSSIER_RULES
```

`return AskResponse(…)` 加 `dossier=dossier_info,`.

- [ ] **Step 6: 实现 — `ask_stream` 接线 (line ~528-560)**

与 Step 5 相同的三处插入 (在 `engine = fed if …` 前 / `context` 后 / `messages` 后), 变量名相同. 然后:

- `yield sse("sources", {"sources": sources, "routed_corpus": routed})` → `yield sse("sources", {"sources": sources, "routed_corpus": routed, "dossier": dossier_info})`
- `done` 事件 dict 末尾加 `"dossier": dossier_info,`
- D6 落盘那行 `log.info("ask_stream", …)` 加 `dossier=(dossier_info or {}).get("reason")`.

- [ ] **Step 7: 跑测试 + 全量**

Run: `.venv/bin/python -m pytest -q scripts/tests/test_router_dossier_wiring.py scripts/tests/test_pdf_context_wiring.py scripts/tests/test_federation_api.py && .venv/bin/python -m pytest -q scripts/tests 2>&1 | tail -3`
Expected: 全绿. ⚠ 其它 wiring 测试的 fake app 没设 `app.state.dossier` → `getattr(..., None)` 兜住, 应不受影响; 若有测试比对 `done` 事件整个 dict 相等, 需在期望里加 `"dossier": None` (那是 OFF 的如实值, 不是回归).

- [ ] **Step 8: Commit**

```bash
git add server/router.py scripts/tests/test_router_dossier_wiring.py
git commit -m "feat(rag): DM2 T5 router 接线: maybe_attach_dossier 共用 helper, dossier 字段/徽章, OFF 逐字节不变"
```

---

### Task 6: eval 侧 lever 记录 (缺键 = OFF)

**Files:**
- Modify: `eval/run_eval.py:1161-1171` (`summary["retrieval_levers"]`)
- Modify: `eval/prod_wirein/check_code_grounding.py:85-107` (`engine_kwargs_from_levers`)
- Test: `scripts/tests/test_code_grounding_fidelity.py` (加 1 例)

**Interfaces:**
- Produces: `retrieval_levers["dossier"]: bool` — run_eval 走的是 `RAGEngine` 直连 (无 router), 研读包**永远不经过** eval 检索路径, 所以实收值恒 `False`; 记它是为了让报告自证「这轮没有研读包」. `engine_kwargs_from_levers` 对 `dossier=True` 的报告 **拒绝重建** (抛 `ValueError`): 研读包路径的答案不能用检索层 fidelity 复现.

- [ ] **Step 1: 写失败测试 (加到 `test_code_grounding_fidelity.py` 末尾)**

```python
def test_dossier_lever_missing_reads_off_and_true_refuses_rebuild():
    from eval.prod_wirein.check_code_grounding import engine_kwargs_from_levers, levers_from_report
    lv = levers_from_report({"summary": {"retrieval_levers": {"top_k": 15, "structured_lookup": True,
                                                            "hybrid": True, "rerank": False, "query_expansion": "none"}}})
    assert lv["dossier"] is False
    engine_kwargs_from_levers(lv)   # 不抛
    with pytest.raises(ValueError, match="dossier"):
        engine_kwargs_from_levers({**lv, "dossier": True})
```

- [ ] **Step 2: 跑确认失败**

Run: `.venv/bin/python -m pytest -q scripts/tests/test_code_grounding_fidelity.py -k dossier`
Expected: FAIL (`KeyError: 'dossier'` 或无 ValueError)

- [ ] **Step 3: 实现**

`check_code_grounding.py` `_RUN_EVAL_DEFAULT_LEVERS` 加 `"dossier": False,`; `engine_kwargs_from_levers` 开头加:

```python
    if levers.get("dossier", False):
        # DM2: 研读包不走 RAGEngine, 检索层无法复现那轮的 top5 —— 与其重建出一台
        # 「看起来一样」的引擎给假 fidelity, 不如拒绝.
        raise ValueError("dossier=True 的报告不能用检索层 fidelity 重建 (DM2 spec §7)")
```

`run_eval.py` `summary["retrieval_levers"]` 加 `"dossier": False,  # DM2: run_eval 直连 RAGEngine, 研读包只在 router 层, 恒 OFF`.

- [ ] **Step 4: 跑确认通过**

Run: `.venv/bin/python -m pytest -q scripts/tests/test_code_grounding_fidelity.py`
Expected: 全绿

- [ ] **Step 5: Commit**

```bash
git add eval/run_eval.py eval/prod_wirein/check_code_grounding.py scripts/tests/test_code_grounding_fidelity.py
git commit -m "feat(rag): DM2 T6 retrieval_levers.dossier (恒 OFF 于 eval; True 拒绝 fidelity 重建)"
```

---

### Task 7: webchat 三态控件 + 徽章 + 存档

**Files:**
- Modify: `webchat/index.html:56-62` (fieldset `#scope`)
- Modify: `webchat/js/ui.js:117` (`webEnabled` 之后加 `dossierMode()`)
- Create: `webchat/js/dossier.js` (`renderDossierBadge`, `dossierBadgeText`)
- Modify: `webchat/app.js:95,134,143,168-172` (state / persist / request / onDone / onSources)
- Modify: `webchat/js/flag.js:82` 附近 (⚑ 存档多一行 `dossier: …`)
- Create: `webchat/tests/dossier.test.mjs`

**Interfaces:**
- Consumes: `sources` 事件 `dossier` / `done` 事件 `dossier` (T5 形状).
- Produces: 请求体 `dossier: "auto"|"on"|"off"`; `dossierBadgeText(info) -> string | null`.

- [ ] **Step 1: 写失败测试 `webchat/tests/dossier.test.mjs`** (照 `pdf_pages.test.mjs` 的 node:test 形式)

```js
import test from "node:test";
import assert from "node:assert/strict";
import { dossierBadgeText } from "../js/dossier.js";

test("null = channel off -> no badge", () => assert.equal(dossierBadgeText(null), null));
test("attached -> badge with sections & chars", () => {
  assert.equal(dossierBadgeText({ attached: true, reason: "auto:domain+scope", sha: "abc", sections: ["4.1", "4.2"], chars: 123456 }),
               "📖 研读包 · 2 章 · 123,456 字 · auto:domain+scope · abc");
});
test("ran but not attached -> quiet hint, not a badge", () => {
  assert.equal(dossierBadgeText({ attached: false, reason: "auto:no_match", sha: "abc", sections: [], chars: 0 }), null);
});
test("forced off -> shows it was forced", () => {
  assert.equal(dossierBadgeText({ attached: false, reason: "forced_off", sha: "abc", sections: [], chars: 0 }), "📖 研读包 · 已手动关闭");
});
test("malformed -> null, never throws", () => assert.equal(dossierBadgeText("junk"), null));
```

- [ ] **Step 2: 跑确认失败**

Run: `cd webchat && node --test tests/dossier.test.mjs`
Expected: FAIL `Cannot find module '../js/dossier.js'`

- [ ] **Step 3: 实现 `webchat/js/dossier.js`**

```js
// DM2 研读包: done/sources 事件的 `dossier` → 徽章文案. 三态原样保留 (后端 T5):
//   null = 通道没跑; {attached:false, reason} = 跑了没挂; {attached:true,…} = 挂了.
export function dossierBadgeText(info) {
  if (!info || typeof info !== "object" || Array.isArray(info)) return null;
  if (info.attached === true) {
    const n = Array.isArray(info.sections) ? info.sections.length : 0;
    const chars = Number.isFinite(info.chars) ? info.chars.toLocaleString("en-US") : "?";
    return `📖 研读包 · ${n} 章 · ${chars} 字 · ${info.reason || "?"} · ${info.sha || "?"}`;
  }
  if (info.reason === "forced_off") return "📖 研读包 · 已手动关闭";
  return null;
}

export function renderDossierBadge(turn, info) {
  const old = turn.querySelector(".dossier-badge");
  if (old) old.remove();
  const text = dossierBadgeText(info);
  if (!text) return;
  const el = document.createElement("div");
  el.className = "badge dossier-badge";
  el.title = "本题跳过了 study 侧检索, 整段喂入 PRT 章节 + EDC 全项目一览";
  el.textContent = text;
  turn.appendChild(el);
}
```

- [ ] **Step 4: 控件 + 接线**

`index.html` 在 `联网参考` label 之后加:

```html
              <label title="研读模式: 域级映射题自动整段喂入 PRT + EDC 一览 (auto), 或手动强开/强关">
                📖 <select id="scope-dossier">
                  <option value="auto" selected>研读:自动</option>
                  <option value="on">研读:开</option>
                  <option value="off">研读:关</option>
                </select>
              </label>
```

`js/ui.js` 加:

```js
export function dossierMode() { const el = $("scope-dossier"); return el ? el.value : "auto"; }
```

`app.js`:
- import 行加 `dossierMode` (from ui.js) 与 `import { renderDossierBadge } from "./js/dossier.js";`
- line 95 附近加 `let gotDossier = null;`
- line 134 persist 对象加 `dossier: gotDossier`
- line 143 请求加 `dossier: dossierMode(),`
- `onSources: (s, routed, extra) => { … gotDossier = (extra || {}).dossier ?? null; }` — ⚠ 查 `webchat/js/stream.js` 的 `onSources` 回调签名: 若它只传 `(sources, routed_corpus)`, 改 stream.js 把整个 data 作为第 3 参传出 (向后兼容, 老回调忽略第 3 参), 并在 `stream.test.mjs` 加一例断言第 3 参含 `dossier`.
- onDone 里 `gotDossier = (data || {}).dossier ?? gotDossier;` 然后 `renderDossierBadge(turn, gotDossier);`
- 历史重渲染处 (搜 `renderPdfPages(` 的第二个调用点, 历史回放) 同样加 `renderDossierBadge(turn, msg.dossier ?? null)`.

`js/flag.js` line 82 附近, 在 `pdf_pages:` 行之后加:

```js
  const dLine = `dossier: ${msg.dossier ? JSON.stringify({attached: msg.dossier.attached, reason: msg.dossier.reason, sha: msg.dossier.sha}) : "null"}`;
```
并拼进 note 文本 (照 `line` 的拼法).

`style.css`: `.dossier-badge { … }` 复用 `.badge` 已有样式, 只加 `margin-top: 4px`.

- [ ] **Step 5: 跑 node 测试 + 手工冒烟**

Run: `cd webchat && node --test tests/`
Expected: 全绿 (含 stream.test.mjs 新例).
手工: `.venv/bin/uvicorn server.main:app --port 8010` 后开 `http://127.0.0.1:8010/`, 选「研读:开」问任意题, 应看到 📖 徽章; 选「研读:关」不出现. (生产 launchd 在 8000 读主工作树, 不动它.)

- [ ] **Step 6: Commit**

```bash
git add webchat/index.html webchat/js/ui.js webchat/js/dossier.js webchat/js/stream.js webchat/js/flag.js webchat/app.js webchat/style.css webchat/tests/dossier.test.mjs webchat/tests/stream.test.mjs
git commit -m "feat(rag): DM2 T7 webchat 研读模式三态控件 + 📖 徽章 + ⚑ 存档"
```

---

### Task 8: L2 零 LLM 闸 (触发扫描 + 零回归)

**Files:**
- Create: `eval/prod_wirein/dm2_trigger_sweep.py`
- Create: `evidence/checkpoints/dm2_gates.md`

**Interfaces:**
- Consumes: `decide_dossier` (T3), 真实 `StructuredLookup` (从 `RAGEngine` 构造, 用 `settings`), 三个题集 yml.

- [ ] **Step 1: 写脚本**

```python
"""DM2 T8: 三个题集各有多少题会被 auto 触发 —— 140q 必须 0 (纯 CDISC 题不该整本喂).

跑 (从 sdtm-rag/):  .venv/bin/python eval/prod_wirein/dm2_trigger_sweep.py
"""
from __future__ import annotations
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
import yaml  # noqa: E402
from server.config import settings  # noqa: E402
from server.dossier_trigger import decide_dossier  # noqa: E402
from server.structured_lookup import StructuredLookup  # noqa: E402

SETS = {
    "cdisc140": "eval/test_set_v3.yml",
    "study48": "data/study/st01/eval/test_set_study_v2.yml",
    "mapping8": "data/study/st01/eval/test_set_domain_mapping_v1.yml",
}

def main() -> int:
    lookup = StructuredLookup.from_kb(settings.kb_root)   # ⚠ 若构造器名不同, 照 rag.py:198 的写法
    for name, path in SETS.items():
        rows = yaml.safe_load(Path(path).read_text(encoding="utf-8"))
        fired = [r["id"] for r in rows if decide_dossier(r["question"], "auto", True, lookup._query_domains).attach]
        print(f"{name}: {len(fired)}/{len(rows)} fired  {fired if len(fired) <= 12 else fired[:12] + ['…']}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 2: 跑**

Run: `.venv/bin/python eval/prod_wirein/dm2_trigger_sweep.py`
Expected: `cdisc140: 0/140`, `mapping8: 8/8`, `study48: N/48` (记 N 与题号). 若 cdisc140 ≠ 0 → 归档 `evidence/failures/dm2_task8_attempt_1.md` (列出误触题与命中的范围词), 收窄 `_SCOPE_RE` 的**词类**后重跑; 不许对题面加黑名单.

- [ ] **Step 3: 零回归复跑 (检索层不应变: 研读包不经 run_eval)**

```bash
.venv/bin/python -m eval.run_eval eval/test_set_v3.yml --retrieval-only --hybrid --structured-lookup --output eval/runs/dm2_cdisc_after.json
.venv/bin/python -m eval.run_eval data/study/st01/eval/test_set_study_v2.yml --retrieval-only --hybrid --study-lookup --collection study_st01 --kb-root data/study/st01/cards --output data/study/st01/eval/runs/dm2_study_after.json
```
逐题 diff 对 `dm1_*_after.json` (脚本见 `evidence/checkpoints/dm1_gates.md` 末尾, 把 before/after 路径换成 dm1_after/dm2_after). Expected: worse=[] better=[] 两集 (检索层一字未动).

- [ ] **Step 4: 写 `evidence/checkpoints/dm2_gates.md`** (命令 + 三行数字 + study48 触发题号 + diff 输出), commit

```bash
git add eval/prod_wirein/dm2_trigger_sweep.py evidence/checkpoints/dm2_gates.md eval/runs/dm2_cdisc_after.json
git commit -m "feat(rag): DM2 T8 L2 闸: 140q 零触发, 映射 8/8 触发, 检索层零回归"
```

---

### Task 9: L3 语义 e2e (规则 A/D, 需用户 kickstart)

**Files:**
- Create: `evidence/checkpoints/dm2_dossier_e2e.md` (§0 判据**先**写, 再跑)
- Create: `eval/prod_wirein/dm2_e2e_run.py` (打 `/api/ask_stream`, 存全文 + usage + dossier 徽章到 gitignored `data/study/st01/eval/runs/dm2_e2e/`)

**Interfaces:**
- Consumes: 生产服务 `http://127.0.0.1:8000/api/ask_stream` (登录门若开, 用 `server/auth.py` 的 session cookie; 本机 launchd 默认关), 请求体 `{question, history:[], model, dossier:"auto"}`.

- [ ] **Step 1: 写 §0 判据 (预登记, 与 spec §7 L3 逐字一致), commit 后再跑**

```markdown
# DM2 — L3 e2e (2026-09-xx)
## §0 判据 (跑前登记)
题: 用户原句 (dm01) / dm02 (DS 日文) / dm05 (AE 英文小写). 模型: opus-5, sonnet-5. N=6.
每题 PASS = 三条全过:
 ① 定义齐: 按域定义列出全部记录类别 (DS: 3 类; AE: 见 assumptions item_1)
 ② 候选齐: gold 4 卡 ≥ 3 张被点名 (表单 OID + 项目 OID 原样); 额外点名的 OID 全部在一览中存在 (零捏造, 用 check_code_grounding 码闸 + 一览 grep)
 ③ 标推测: 每条归属带 推測/inference; 明说无候选的类别
目标 ≥ 5/6. 判分 = 异 subagent (opus, 不看本 session), 每题独立报告写 §2.
成本: 每题记 usage.prompt_tokens / completion_tokens / 是否 cache 命中 (Bedrock 返回 cache_read_input_tokens 时).
```

- [ ] **Step 2: 用户 kickstart** — 用 AskUserQuestion 请用户执行 `launchctl kickstart -k gui/$(id -u)/com.sdtmrag.api` 并确认 `curl -s localhost:8000/api/info | grep -o '"federation":[a-z]*'`.

- [ ] **Step 3: 跑 6 次, 全文落 gitignored runs/, 徽章 attached 必须 6/6 True**

- [ ] **Step 4: 派异 subagent 判分** (subagent_type 不同于本 session; prompt 只给 §0 判据 + 答案全文 + gold 卡 basename 列表 + 一览文本, 不给本 plan), 结果写 §2 表 (代称).

- [ ] **Step 5: 若 < 5/6: 归档 `evidence/failures/dm2_task9_attempt_1.md`, 只允许改 `_DOSSIER_RULES` 的**规则层**措辞 (模式级), 不许加题面 example; 改后重跑 6 题**全部** (不只失败题).**

- [ ] **Step 6: Commit**

```bash
git add evidence/checkpoints/dm2_dossier_e2e.md eval/prod_wirein/dm2_e2e_run.py
git commit -m "feat(rag): DM2 T9 L3 e2e: N=6 三判据 <X>/6 + 成本记录"
```

---

### Task 10: 收口

**Files:**
- Create: `RETROSPECTIVE_dossier.md` (三段: 保留 / 缺口 / 决策复盘, 规则 C)
- Create: `_progress_dossier.json` (照 `_progress_domain_mapping.json` 形状)
- Modify: `../.work/meta/worklog/phase07.md` (append), `../docs/PROGRESS.md` (最后更新行), `../CLAUDE.md` Key Paths 加一行 (≤ 80 字符): `| Phase 7 DM2 研读包旁路 (整本喂, 默认 ON) | `sdtm-rag/server/study_dossier.py`; spec/plan `docs/superpowers/*2026-09-15-study-dossier*`; 证据 `dm2_{gates,dossier_e2e}.md` |`
- Modify: `_progress_domain_mapping.json` step 10 → `"done (D4 裁定: 整本喂 = DM2)"`; memory `project_dm1_domain_mapping.md` 加一行指向 DM2.

- [ ] **Step 1-4**: 逐个写, 每个 `git add <path>`; 最后一个 commit `docs(rag): DM2 收口 — RETRO + progress + worklog + Key Path`; `git push origin main`.

---

### Task 11 (可选, e2e 之后): Bedrock prompt cache

只在 T9 成本数字显示每题 ≥ 150K prompt tokens 且用户要求降本时做. 做法: `maybe_attach_dossier` 不再把研读包拼进 context 字符串, 而是让 `build_messages` 后把 user 消息改成 content parts `[{"type":"text","text":<context+question>}, {"type":"text","text":<dossier>, "cache_control":{"type":"ephemeral"}}]` —— 仅当 `body.model` 解析到的 litellm 模型串含 `anthropic` 时. 需先查 litellm 对 `bedrock/converse` 的 cache_control 透传 (Context7 查 litellm docs), 并加一条 fidelity 测试「非 anthropic 模型 messages 形状不变」. 与 C2R parts 共存要测. 本 task 未在 spec 里承诺, 是否做由用户点.

---

## Self-Review

- **Spec coverage**: §2 组件 → T1/T3/T4/T5/T7; §3 内容形状 + Task 0 token 闸 → T1/T2; §4 触发规则 → T3 (含 `EDC` 词与异常静默); §5 数据流 (丢 study / 强制 both / study 单库补取 CDISC / 规则句 / sources+done+存档三态 / `ask` 同接线 / 不经 4000 字截断) → T5; §5 prompt cache → T11 (spec 标「优化非前提」, 故可选); §6 错误处理 → T4 (启动 fail-loud) / T5 (422 由 Literal 保证; LLM 溢出走既有 error 事件, 无需新码); §7 L1 → T1/T3/T4/T5/T6/T7 测试, L2 → T8, L3 + 成本 → T9; §8 不做 → 无 task (正确).
- **Placeholder scan**: T8 Step 1 `StructuredLookup.from_kb` 标了 ⚠ 要照 `rag.py:198` 实际构造写 — 实现者第一步 `sed -n 195,205p server/rag.py` 取真实签名. T7 `onSources` 第 3 参依赖 stream.js 实际签名, 已写明分支. 其余无 TBD.
- **Type consistency**: `dossier_info` 六键 (`attached/reason/domains/sha/sections/chars`) 在 T5 helper / T5 测试 / T7 `dossierBadgeText` 一致; `DossierDecision.domains: tuple` → info 里 `list(...)`; `StudyDossier.sections: tuple` → `list(...)`. `decide_dossier(question, mode, enabled, query_domains)` 参数序在 T3/T5/T8 一致.
