# VI §三 交叉引用完整性 — 实施计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 删掉 KB 生成器里的交叉引用条数上限, 让"哪些变量引用这个码表"在正文里答得全, 并自带一把现有检索闸给不出的尺子。

**Architecture:** 截断在 **KB 源文件生成器**, 不在切块层。改两个生成器 → 重生成 KB → 重灌索引。验收靠两层自带尺子: 层① 对全部 135 行断言"正文条目数 == 自己声称的 N"(数据不变量, 零 LLM, 常驻, 同时打 KB 层与 chunk 层); 层② 2 道规则驱动的 gold 题走独立文件 + context A/B 对照。

**Tech Stack:** Python 3.12 · Chroma · OpenAI text-embedding-3-small · pytest · `sdtm-rag/.venv`

## Global Constraints

- 仓库根 `/Users/bojiangzhang/MyProject/sdtm-pedia`; Python 一律 `sdtm-rag/.venv/bin/python`。
- **KB markdown 是生成物, 永远不手改** —— 只改生成器再重生成 (文件头就写着 `Auto-generated — do not edit manually`)。
- 两处同病一起修: `generate_variable_index.py` (上限 15) + `generate_cross_references.py` (上限 5)。
- **不往 `eval/test_set_v3.yml` 加题** —— 会换掉 140 分母, 毁掉 98.93% 基线与全部历史 run 的可比性。
- 不改 `scripts/chunkers/variable_index.py`; 不碰 `web/` (站点读 `milestones/release/v1.4`, 已核实)。
- **验收纪律**: v3 检索闸期望**逐题 Δ0**, 那是"没回归"不是"修好了"。**引用本轮成果不得用 v3 数字。**
- 规则 D: 实现 / 审查 / 抽检各用不同 `subagent_type`, 不自审。
- 写"实测"必须附可复跑的一行命令。

---

### Task 1: 层① 完整性不变量 (先红 — 当前数据就是错的)

**Files:**
- Create: `sdtm-rag/scripts/tests/test_kb_crossref_completeness.py`

**Interfaces:**
- Consumes: `knowledge_base/VARIABLE_INDEX.md`、`knowledge_base/domains/*/spec.md`、`server.config.settings`。
- Produces: 常驻不变量闸。Task 2 之后必须转绿, 且**将来谁再加截断当场红**。

- [ ] **Step 1: 写失败测试**

```python
"""KB 交叉引用完整性 — "正文条目数 == 自己声称的 N"。

这不是对某道题的补丁, 是数据不变量: 一次覆盖 9 个宽码表的 226 条隐藏条目, 并永久钉住
(将来谁再往生成器加条数上限, 这里当场红)。

section 级 source recall 对截断**零判别力** (只看 section 名, 不看正文是否被截), 所以
这层断言是本单元唯一能证明"修好了"的东西 —— v3 检索闸改完会一动不动。
"""
from __future__ import annotations

import re
from pathlib import Path

import pytest

from server.config import settings

KB_ROOT = Path(settings.kb_root)
VI = KB_ROOT / "VARIABLE_INDEX.md"
_TRUNC_RE = re.compile(r"\.\.\. \(\d+ total\)")
_CT_ROW_RE = re.compile(r"^\| (C\d+) \| (\d+) \| (.+?) \|$", re.M)


def _ct_rows() -> list[tuple[str, int, str]]:
    sec3 = VI.read_text(encoding="utf-8").split("## 3. CDISC Controlled Terminology")[1]
    return [(c, int(n), v) for c, n, v in _CT_ROW_RE.findall(sec3)]


def test_every_ct_row_lists_all_the_variables_it_claims():
    """每行列出的条目数必须等于该行 References 列自己声称的数字。

    截断行的表现: 声称 123 个引用, 正文只给 15 个 + `... (123 total)` —— 该行是这个问题
    的唯一权威来源, 半张表等于答不出来。"""
    bad = [(c, n, len([x for x in v.split(", ") if x.strip()]))
           for c, n, v in _ct_rows()
           if len([x for x in v.split(", ") if x.strip()]) != n]
    assert not bad, f"这些 CT 行的正文条目数 != 声称的 N: {bad[:5]} (共 {len(bad)} 行)"


def test_no_truncation_marker_anywhere_in_variable_index():
    hits = _TRUNC_RE.findall(VI.read_text(encoding="utf-8"))
    assert not hits, f"VARIABLE_INDEX.md 仍有 {len(hits)} 处截断标记"


def test_no_truncation_marker_in_domain_specs():
    bad = [p.relative_to(KB_ROOT).as_posix()
           for p in sorted((KB_ROOT / "domains").glob("*/spec.md"))
           if _TRUNC_RE.search(p.read_text(encoding="utf-8"))]
    assert not bad, f"这些域 spec 仍有截断标记: {bad}"


def test_ct_row_count_is_stable():
    # 防"把截断行整行删掉"这种假修法: 135 行一个都不能少
    assert len(_ct_rows()) == 135
```

- [ ] **Step 2: 跑测试确认失败 (失败原因必须是数据错, 不是代码错)**

Run: `cd sdtm-rag && .venv/bin/python -m pytest scripts/tests/test_kb_crossref_completeness.py -v`
Expected: 前 3 条 FAIL (`test_ct_row_count_is_stable` 应 PASS)。
FAIL 信息应显示 9 行条目数不符 + VI 有 9 处截断标记 + AE/LB 两个 spec 有截断标记。

- [ ] **Step 3: 提交 (先提交红测试, 让"数据是错的"这件事进历史)**

```bash
git add sdtm-rag/scripts/tests/test_kb_crossref_completeness.py
git commit -m "test(kb): 交叉引用完整性不变量 (当前红 — 9 行被截, 隐藏 226 条)"
```

---

### Task 2: 拆掉两个生成器的条数上限 + 重生成 KB

**Files:**
- Modify: `.work/04_optimization/scripts/generate_variable_index.py:249-257`
- Modify: `.work/04_optimization/scripts/generate_cross_references.py:232-236`
- Regenerate: `knowledge_base/VARIABLE_INDEX.md`、`knowledge_base/domains/AE/spec.md`、`knowledge_base/domains/LB/spec.md`

**Interfaces:**
- Consumes: Task 1 的不变量闸 (改完必须转绿)。
- Produces: 完整的 KB 交叉引用数据, 供 Task 3 重灌。

- [ ] **Step 1: 改前先确认生成器没漂移 (否则重生成会带出一堆无关 diff)**

Run:
```bash
cd /Users/bojiangzhang/MyProject/sdtm-pedia
sdtm-rag/.venv/bin/python .work/04_optimization/scripts/generate_variable_index.py /tmp/vi_baseline.md
diff /tmp/vi_baseline.md knowledge_base/VARIABLE_INDEX.md
```
Expected: 只有 1 处差异, 即 `> Auto-generated — do not edit manually | Generated: <日期>` 那行。
**若还有别的差异, 停下** —— 说明 KB 被手改过或生成器已漂移, 重生成会丢掉那些改动。

- [ ] **Step 2: 拆 VI §三 的上限**

`.work/04_optimization/scripts/generate_variable_index.py`, 把

```python
    for ct_code in sorted(ct_index.keys()):
        refs = sorted(ct_index[ct_code])
        ref_count = len(refs)
        # Truncate if too many
        if len(refs) > 15:
            refs_str = ", ".join(refs[:15]) + f" ... ({ref_count} total)"
        else:
            refs_str = ", ".join(refs)
        lines.append(f"| {ct_code} | {ref_count} | {refs_str} |")
```

改为

```python
    for ct_code in sorted(ct_index.keys()):
        refs = sorted(ct_index[ct_code])
        ref_count = len(refs)
        # 不截断: 这张表是"哪些变量引用该码表"的唯一权威来源, 截到 15 条等于半张表。
        # 全展开对最宽的 C66742 (123 个引用) 也只有约 1.5K 字符, 全库 +2.6 KB —— 旧的
        # 15 条上限几乎没买到任何东西, 却让 9 个最需要它的宽码表答不全。
        # 检索侧判据看不出这个缺陷 (section 名不变), 故 scripts/tests/
        # test_kb_crossref_completeness.py 钉住"条目数 == 声称的 N"。
        lines.append(f"| {ct_code} | {ref_count} | {', '.join(refs)} |")
```

- [ ] **Step 3: 拆域 spec 交叉引用段的上限**

`.work/04_optimization/scripts/generate_cross_references.py`, 把

```python
            vars_str = ", ".join(var_names[:5])
            if len(var_names) > 5:
                vars_str += f" ... ({len(var_names)} total)"
```

改为

```python
            # 同 VARIABLE_INDEX §三: 不截断 (本处仅 AE/LB 两个文件命中, 共隐藏 10 条)
            vars_str = ", ".join(var_names)
```

- [ ] **Step 4: 重生成三个 KB 文件**

Run:
```bash
cd /Users/bojiangzhang/MyProject/sdtm-pedia
sdtm-rag/.venv/bin/python .work/04_optimization/scripts/generate_variable_index.py
sdtm-rag/.venv/bin/python .work/04_optimization/scripts/generate_cross_references.py
git diff --stat knowledge_base/
```
Expected: 只有 `VARIABLE_INDEX.md` + `domains/AE/spec.md` + `domains/LB/spec.md` 三个文件变化。
**若有第四个文件变化, 停下查清原因再继续。**

- [ ] **Step 5: 层① 转绿**

Run: `cd sdtm-rag && .venv/bin/python -m pytest scripts/tests/test_kb_crossref_completeness.py -v`
Expected: 4 passed

- [ ] **Step 6: 眼看一眼最宽那行真的全了**

Run:
```bash
cd /Users/bojiangzhang/MyProject/sdtm-pedia && grep -c ", " <(grep "^| C66742 |" knowledge_base/VARIABLE_INDEX.md)
sdtm-rag/.venv/bin/python -c "
import re
row = [l for l in open('knowledge_base/VARIABLE_INDEX.md') if l.startswith('| C66742 |')][0]
n, v = row.split('|')[2].strip(), row.split('|')[3].strip()
print(f'声称 {n} 个, 正文 {len(v.split(chr(44)))} 个, 末位 {v.split(chr(44))[-1].strip()}')"
```
Expected: `声称 123 个, 正文 123 个, 末位 <某变量>`

- [ ] **Step 7: 提交**

```bash
git add -A
git commit -m "fix(kb): 拆掉交叉引用条数上限 — 9 个宽码表补回 226 条隐藏引用"
```

---

### Task 3: 重灌索引 + chunk 层断言

**Files:**
- Modify: `sdtm-rag/scripts/tests/test_kb_crossref_completeness.py` (追加 chunk 层断言)
- Rebuild: `sdtm-rag/data/chroma`

**Interfaces:**
- Consumes: Task 2 重生成的 KB。
- Produces: 与 KB 一致的向量库; chunk 层完整性断言。

- [ ] **Step 1: 先加 chunk 层断言 (KB 对而 chunker 截断仍然会伤)**

追加到 `scripts/tests/test_kb_crossref_completeness.py`:

```python
# ---- chunk 层 (真正进索引的那段文本) ----------------------------------------


def test_indexed_ct_chunks_carry_every_variable():
    """KB 对而索引里是旧的 / chunker 截断, 照样答不出来。

    `scripts/kb_freshness.py` 的存在动因正是 2026-08-04 实测到"部署中的向量库把
    VARIABLE_INDEX.md 欠切 70%" —— 同一个文件有前科, 所以 KB 层断言不够, 必须打到
    真正被检索到的那段文本上。"""
    import chromadb

    try:
        col = chromadb.PersistentClient(
            path=str(settings.chroma_dir)).get_collection(settings.collection_name)
    except Exception:  # noqa: BLE001 — 打不开库的原因不重要, 都是"本机没索引"
        pytest.skip("本机无索引; 跑 .venv/bin/python -m scripts.ingest 后此闸才生效")

    vi_abs = str((KB_ROOT / "VARIABLE_INDEX.md").resolve())
    rows = col.get(where={"source": vi_abs}, include=["documents", "metadatas"])
    by_section = {m.get("section"): d
                  for m, d in zip(rows["metadatas"], rows["documents"], strict=True)}

    bad = []
    for code, n, refs in _ct_rows():
        doc = by_section.get(f"§三 CT 交叉引用: {code}")
        if doc is None:
            bad.append((code, "section 不在索引"))
            continue
        missing = [r.strip() for r in refs.split(", ") if r.strip() and r.strip() not in doc]
        if missing:
            bad.append((code, f"正文缺 {len(missing)} 个, 例: {missing[:3]}"))
    assert not bad, f"索引里的 CT chunk 与 KB 不一致: {bad[:5]} (共 {len(bad)})"
```

- [ ] **Step 2: 跑它确认现在是红的 (索引还是旧的)**

Run: `cd sdtm-rag && .venv/bin/python -m pytest scripts/tests/test_kb_crossref_completeness.py::test_indexed_ct_chunks_carry_every_variable -v`
Expected: FAIL, 报 9 个 CT chunk 正文缺条目 (KB 已修但索引未重灌)

- [ ] **Step 3: 重灌**

Run:
```bash
cd sdtm-rag && .venv/bin/python -m scripts.ingest 2>&1 | tail -20
```
Expected: 结束时报 chunk 数 (基线 4303, 允许小幅变化 —— §三 行变长可能改变分块); 无 ERROR。
成本约 $0.02 (text-embedding-3-small 重嵌全库)。

- [ ] **Step 4: chunk 层转绿 + 新鲜度回到 fresh**

Run:
```bash
cd sdtm-rag
.venv/bin/python -m pytest scripts/tests/test_kb_crossref_completeness.py -v   # 5 passed
.venv/bin/python scripts/check_index_freshness.py
```
Expected: 5 passed; freshness 报 in sync

- [ ] **Step 5: reconcile_meta 实跑 (不许靠推断)**

Run: `cd sdtm-rag && .venv/bin/python scripts/reconcile_meta.py 2>&1 | tail -15`
Expected: 全 PASS。它读 VI 的 header 计数与 §一 行, §三 改动理论上不影响 —— **但这条必须实跑**。
若报错, 停下: 说明 §三 的改动波及了 meta↔KB 对账, 需要先查清。

- [ ] **Step 6: 提交**

```bash
git add -A
git commit -m "feat(kb): 重灌索引 — CT chunk 正文补齐, 新增 chunk 层完整性断言"
```

---

### Task 4: 层② 端到端 gold 题 + context A/B

**Files:**
- Create: `sdtm-rag/eval/test_set_vi_completeness.yml`
- Create: `sdtm-rag/eval/vi_completeness_ab.py`

**Interfaces:**
- Consumes: Task 3 重灌后的索引。
- Produces: 独立计分的 2 题 gold 集 + 截断/完整 context 的对照结果。

- [ ] **Step 1: 按规则机械生成题目**

出题规则 (spec §3.2, 写死):
> 凡 `N > 15` 的码表, 问"哪些变量引用它", **gold fact 取位置 > 15 的条目 (按字母序末位)**。

9 个宽码表按 N 降序: `C66742`(123) `C71620`(58) `C99079`(44) `C66789`(36) `C66728`(26)
`C74456`(19) `C78735`(19) `C85492`(19) `C99073`(17)。取前两个。

gold fact **已在写计划时算出** (对未截断的重生成结果执行同一规则, 见 spec §5.3):

| 码表 | N | 第 16 位 (旧正文的第一个不可见项) | 末位 = gold fact |
|---|---|---|---|
| `C66742` | 123 | `BS.BSBLFL` | **`VS.VSLOBXFL`** |
| `C71620` | 58 | `FA.FAORRESU` | **`UR.URSTRESU`** |

Task 2 完成后用这条命令**复核真值没变** (若变了, 说明生成器行为与写计划时不一致, 停下):
```bash
cd /Users/bojiangzhang/MyProject/sdtm-pedia && sdtm-rag/.venv/bin/python - <<'PY'
for code in ("C66742", "C71620"):
    row = [l for l in open("knowledge_base/VARIABLE_INDEX.md") if l.startswith(f"| {code} |")][0]
    refs = [r.strip() for r in row.split("|")[3].split(",")]
    print(f"{code}: N={len(refs)} 第16位={refs[15]} 末位={refs[-1]}")
PY
# 期望: C66742: N=123 第16位=BS.BSBLFL 末位=VS.VSLOBXFL
#       C71620: N=58 第16位=FA.FAORRESU 末位=UR.URSTRESU
```

写进 `sdtm-rag/eval/test_set_vi_completeness.yml`:

```yaml
# VI 交叉引用完整性 — 独立题集 (不并入 test_set_v3.yml)
#
# 为什么独立: 并进 v3 会换掉 140 的分母, 使 98.93% 基线与全部历史 run 失去可比性
# ("一版一把尺子")。
#
# 出题规则 (规则驱动, 非挑例子 — 任何人可机械重生成同一批题):
#   凡 N > 15 的码表, 问"哪些变量引用它", gold fact 取位置 > 15 的条目 (字母序末位)。
#   规则作用于 9 个宽码表全体; 此处只落 2 道控体量, 其余 7 个由
#   scripts/tests/test_kb_crossref_completeness.py 的数据不变量全覆盖。
#
# 判别力声明: source recall 对本题集**失明** (gold section 本来就命中), 判别力只在
# fact 侧。用 --judge 或 fact_recall 读成绩, 不要看 source recall。
questions:
  - id: vic01
    category: cross_domain
    question: >-
      Which SDTM domain variables reference the No Yes Response codelist C66742?
      List them exhaustively.
    expected_sources:
      - "VARIABLE_INDEX.md#§三 CT 交叉引用: C66742$"
    expected_facts:
      - "VS.VSLOBXFL"      # 第 123 位 = 旧正文 (只到第 15 位) 结构上答不出
  - id: vic02
    category: cross_domain
    question: >-
      Which SDTM domain variables reference the Unit codelist C71620?
      List them exhaustively.
    expected_sources:
      - "VARIABLE_INDEX.md#§三 CT 交叉引用: C71620$"
    expected_facts:
      - "UR.URSTRESU"      # 第 58 位 = 同上
```

> **注意 C71620 与 v3 的 q69 用同一个码表** —— 这不是重复题: q69 的 gold fact 是
> `EX.EXDOSU` (第 15 位, 旧正文可见), 本题问的是位置 > 15 的条目, 正是旧正文答不出来的部分。

- [ ] **Step 2: 写 context A/B 对照 (改动前数字, 不做两次重灌)**

Create `sdtm-rag/eval/vi_completeness_ab.py`:

```python
"""截断 vs 完整 context 的对照 — 本单元"改动前/后"数字的来源。

不做两次全量重灌: 同一问句喂两份 context (旧的 15 条截断版 / 新的完整版) 跑同一模型,
变量隔离得更干净 (只有那段正文变了)。

答题调用复用 eval/run_eval.py:332-340 的方式 (rag.build_messages + litellm.completion),
不另起一套模型配置。temperature=0.0 保证配对可复算。

用法: .venv/bin/python -m eval.vi_completeness_ab
"""
from __future__ import annotations

import litellm

from server.config import settings as s
from server.rag import RAGEngine

# gold fact = 该码表引用列表按字母序的末位 (必在第 15 位之后 = 旧正文结构上答不出)
CASES = [
    ("C66742", "VS.VSLOBXFL",
     "Which SDTM domain variables reference the No Yes Response codelist C66742? "
     "List them exhaustively."),
    ("C71620", "UR.URSTRESU",
     "Which SDTM domain variables reference the Unit codelist C71620? "
     "List them exhaustively."),
]


def _truncate_ct_line(text: str, keep: int = 15) -> str:
    """把完整的 CT chunk 正文退回旧生成器的 15 条截断形态。"""
    head, sep, tail = text.partition("variable(s): ")
    if not sep:
        return text
    refs = [r.strip().rstrip(".") for r in tail.split(",")]
    if len(refs) <= keep:
        return text
    return f"{head}{sep}{', '.join(refs[:keep])} ... ({len(refs)} total)."


def _answer(rag: RAGEngine, question: str, context: str) -> str:
    resp = litellm.completion(
        model=s.default_model,
        messages=rag.build_messages(question, context),
        temperature=0.0,
    )
    return resp.choices[0].message.content or ""


def main() -> int:
    rag = RAGEngine(
        chroma_dir=s.chroma_dir, kb_root=s.kb_root, collection_name=s.collection_name,
        embedding_model=s.embedding_model, top_k=s.top_k,
        structured_lookup_enabled=s.structured_lookup_enabled,
        hybrid_enabled=s.hybrid_enabled, hybrid_fusion=s.hybrid_fusion,
        hybrid_alpha=s.hybrid_alpha, hybrid_pool=s.hybrid_pool,
        prompt_guardrail_enabled=s.prompt_guardrail_enabled,
    )
    failures = 0
    for code, gold_fact, question in CASES:
        full_ctx = rag.format_context(rag.retrieve(question))
        trunc_ctx = "\n".join(_truncate_ct_line(seg) for seg in full_ctx.split("\n"))

        got_full = gold_fact in _answer(rag, question, full_ctx)
        got_trunc = gold_fact in _answer(rag, question, trunc_ctx)
        ok = got_full and not got_trunc
        failures += 0 if ok else 1
        print(f"{code}  gold={gold_fact}  截断版={got_trunc}  完整版={got_full}"
              f"  -> {'判别力成立' if ok else '无判别力'}")

    print("\n注: 这里隔离的是 context 变量, 证明的是因果, 不等于线上答题必然变好。")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 3: 跑 A/B, 记录两个数字**

Run: `cd sdtm-rag && .venv/bin/python -m eval.vi_completeness_ab 2>&1 | tail -20`
Expected: 截断 context 下**答不出**位置 >15 的那个变量; 完整 context 下答得出。
**若截断版也答对了**, 停下 —— 说明模型是从别处 (域 spec / 参数知识) 拿到的, 该题没有判别力,
需按规则换下一个宽码表重出。

- [ ] **Step 4: 跑独立 gold 集**

Run:
```bash
cd sdtm-rag && .venv/bin/python eval/run_eval.py eval/test_set_vi_completeness.yml \
    --hybrid --structured-lookup --judge --output evidence/checkpoints/vi_completeness_after.json 2>&1 | tail -12
```
Expected: fact 侧 2/2。**source recall 不看** (对本题集失明, 见 yml 头部声明)。

- [ ] **Step 5: 提交**

```bash
git add -A
git commit -m "test(eval): VI 完整性独立题集 + 截断/完整 context 对照"
```

---

### Task 5: 全量闸 + 服务重启 + 证据收口

**Files:**
- Create: `sdtm-rag/evidence/checkpoints/vi_crossref_completeness.md`
- Modify: `docs/PROGRESS.md`、`.work/meta/worklog/phase_07_rag_kg.md`、`milestones/07_rag_kg/NEXT_ROUND_KICKOFF.md`

- [ ] **Step 1: v3 检索闸 — 期望逐题 Δ0**

Run:
```bash
cd sdtm-rag && .venv/bin/python eval/run_eval.py eval/test_set_v3.yml \
    --retrieval-only --hybrid --structured-lookup \
    --output evidence/checkpoints/vi_trunc_v3_after.json 2>&1 | tail -12
```
Expected: **98.93%**, 与 `evidence/checkpoints/s1_vi_after.json` **逐题相同**。

逐题比对:
```bash
cd sdtm-rag && .venv/bin/python - <<'PY'
import json
load = lambda p: {x["id"]: x["source_recall"]
                  for x in (lambda d: d["results"] if isinstance(d, dict) else d)(json.load(open(p)))}
a = load("evidence/checkpoints/s1_vi_after.json")
b = load("evidence/checkpoints/vi_trunc_v3_after.json")
diff = {k: (a[k], b[k]) for k in a if a[k] != b[k]}
print("逐题相同:", not diff, "| 变化:", diff)
PY
```
Expected: `逐题相同: True`。
**这条绿只证明"没回归", 不证明"修好了"** —— 证明修好的是层①/层②。
若有题变化: 停下, 重灌改变了检索行为, 必须先定位。

- [ ] **Step 2: 全量测试**

Run: `cd sdtm-rag && .venv/bin/python -m pytest -p no:warnings 2>&1 | tail -1`
Expected: 852 + 5 = **857 passed** (层① 4 条 + chunk 层 1 条)

- [ ] **Step 3: 重启服务并确认预热仍能建表**

Run:
```bash
launchctl kickstart -k gui/$(id -u)/com.sdtmrag.api
until curl -sf localhost:8000/api/health >/dev/null; do sleep 2; done
grep -a "s1_vi_section_map\|ready" /Users/bojiangzhang/MyProject/sdtm-pedia/sdtm-rag/logs/api.launchd.log | tail -2
```
Expected: `s1_vi_section_map entries=159` (上一轮装的启动期闸重灌后仍成立) + `ready chunks=<新值>`

- [ ] **Step 4: 生产端到端冒烟**

Run:
```bash
curl -s -X POST localhost:8000/api/ask -H 'content-type: application/json' \
  -d '{"question":"Which SDTM domain variables reference the No Yes Response codelist C66742? List them exhaustively."}' \
  > /tmp/vic_smoke.json
cd sdtm-rag && .venv/bin/python -c "
import json; d = json.load(open('/tmp/vic_smoke.json'))
print('引用块:', [s.get('section') for s in (d.get('sources') or [])[:2]])
ans = d.get('answer') or ''
print('答案长度:', len(ans), '| 含末位变量:', '<Task4 Step1 算出的末位变量>' in ans)"
```
Expected: 首块是 `§三 CT 交叉引用: C66742`, 答案含旧正文里根本没有的那个末位变量。

- [ ] **Step 5: 写收口 checkpoint**

新建 `sdtm-rag/evidence/checkpoints/vi_crossref_completeness.md`, 必含:
- **顶部声明**: v3 的 98.93% 一动不动是**预期**, 那把尺子对本修复失明; 引用本轮成果只能用层①/层②
- 截断规模表 (9/135 行, 226 条; 域 spec 2 文件 10 条) 与全展开代价 (+2.6 KB)
- 层① 断言覆盖面 (135 行全覆盖, KB 层 + chunk 层双打)
- 层② 出题规则原文 + 三层反"对症下药"防线 + A/B 前后数字
- v3 逐题 Δ0 的证据
- 已知限制: ① A/B 只隔离了 context 变量, 不等于线上答题必然变好 ② 只落 2 道题, 其余 7 个宽码表靠层① 而非端到端验证 ③ 重灌改变全库 embedding, 逐题 Δ0 是实测非推断

- [ ] **Step 6: 索引三件套同步**

- `docs/PROGRESS.md`: milestone 条目 + Phase 7 行; **必须写明"v3 数字不变是预期"**
- `.work/meta/worklog/phase_07_rag_kg.md`: append work record
- `milestones/07_rag_kg/NEXT_ROUND_KICKOFF.md`: §2.D.2 的"⚠️ 遗留"标 DONE

- [ ] **Step 7: 提交 + push**

```bash
git add -A
git commit -m "docs(kb): VI 交叉引用完整性收口 — 226 条隐藏引用补回"
git push origin main
```

---

### Task 6: 规则 D 三方隔离审查

- [ ] **Step 1: 审查方 (与实现方不同 `subagent_type`)**

重点: ① 生成器改动有无副作用 (行变长是否影响 §一/§二 的解析) ② 重灌是否真的只改了预期的东西
③ 层① 断言会不会被"删掉截断行"这类假修法骗过 ④ A/B 脚本有没有把变量隔离干净
⑤ 独立题集是否真的不污染 v3 的任何统计。

- [ ] **Step 2: 抽检方 (第三个 `subagent_type`, 规则 A)**

**抽样总体 = 本轮实际变更集合 = 9 个被截断的 CT 行 + 2 个域 spec 段**, 不是 135 行全集。
独立复核: 对 N≥5 个宽码表, 从**原始数据源**(meta.yaml / xlsx) 独立算出"应该有哪些变量引用该码表",
与重生成后的 KB 逐条比对 —— 证明补回来的 226 条是**对的**, 而不只是"变多了"。

- [ ] **Step 3: 裁定入档 + 提交**

```bash
git add -A && git commit -m "docs(kb): 规则 D 三方隔离审查裁定入档"
```
