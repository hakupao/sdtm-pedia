# Plan B Phase 2 — study 结构化直查通道 (S2) 实施计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 给 study 引擎加一条确定性结构化直查通道 (S2, 对齐 S1 的 union-add 契约), 把 golden v1.1 下 hybrid+CJK bigram 配置仍 miss 的 4 道题 (`st01_v11_q08/q14/q16/q21`) 转为命中, 且 study 25 计分题逐题零回归。

**Architecture:** 新建 `server/study_lookup.py` (`StudyLookup.resolve(query) -> StudyLookupResult`), 三条确定性通道 (label 全文子串→卡+OID 首段家族 / 拉丁 token→OID 段精确匹配 / 手工别名表→form scope), 数据源只有 catalog.json + 本地别名 yml (零 LLM, 不碰卡片)。RAGEngine 加注入层 `_apply_study_lookup` (精确卡 1 chunk each + form scope 域内 cosine top-3, 前置注入, 与 S1 共用 merge)。默认关, 验收闸全绿后翻开。

**Tech Stack:** Python 3 / pytest / Chroma metadata filter (`source` / `form_oid`) / yaml。

## Global Constraints

- **红线 (spec §3)**: study 数据零入库 — 真实 form/field OID、label、题面、别名词**只允许**出现在 `data/study/` (gitignored) 下; committed 代码/测试/文档一律用合成假名 (仿 `scripts/tests/study_fixtures.py` 的 FAKEFORM1/FAKEIT1 风格)。commit 前扫真名。
- 全程 TDD; 全量测试基线 **720 passed** 只增不减 (junitxml 计数, 套件不打印 summary 行)。
- 真数据映射与探针结论见本地 `data/study/st01/eval/PLANB_P2_NOTES.md` (gitignored) — 执行 Task 6/8 前必读。
- 基线记账: study **88.53%** (golden v1.1, 25 计分题, hybrid+CJK bigram, `runs/v1_1_hybrid_bigram.json`); CDISC 81.07% (hybrid-only) / 98.93% (+S1)。
- study chunk 元数据: `source` = 裸文件名 (非绝对路径), 另有 `form_oid`/`field_oid` 字段 — S2 注入 filter 依赖这一点, **不能**复用 S1 的绝对路径 filter。
- 路由闸资产不碰: `_ROUTER_SYSTEM` prompt / 路由 gold 本计划零改动 (不触发闸 1 重跑条件)。
- 已知偏差声明: spec §Phase 2 表中"近义双卡"的直查依据写的是 "codelist ID / item group / 显示条件"; 实装用**拉丁 token→OID 段精确匹配**达成同一判别 (query 中的拉丁 token 是 EDC 用语; 干扰卡的 OID 段不含该 token, 判别天然成立 — 实测见 NOTES)。catalog 的 codelist/显示条件字段留作未来 fallback, 本轮 YAGNI。

## File Structure

| 文件 | 动作 | 职责 |
|---|---|---|
| `server/study_lookup.py` | Create | `StudyLookup` + `StudyLookupResult`: catalog/别名 → resolve |
| `scripts/tests/test_study_lookup.py` | Create | S2 单元测试 (合成 catalog, 零真名) |
| `server/rag.py` | Modify | ctor `study_lookup` 参数 + `_apply_study_lookup` + merge 抽共用 |
| `server/config.py` | Modify | `study_lookup_enabled` (默认 False) + catalog/别名路径 |
| `server/main.py` | Modify | study 引擎构建时按开关注入 StudyLookup |
| `eval/run_eval.py` | Modify | `--study-lookup` flag (collection 模式 + federated study 引擎) |
| `scripts/tests/test_run_eval_flags.py` | Modify | flag 接线测试 |
| `data/study/st01/lookup_aliases.yml` | Create (本地, 不入库) | 手工别名表 (1 条, 见 NOTES) |
| `sdtm-rag/evidence/checkpoints/planb_phase2_study_lookup.md` | Create (Task 8) | 收口证据 |

---

### Task 1: StudyLookup 核心 — catalog 索引 + label 通道 + 家族扩张

**Files:**
- Create: `sdtm-rag/server/study_lookup.py`
- Test: `sdtm-rag/scripts/tests/test_study_lookup.py`

**Interfaces:**
- Consumes: catalog dict (`build_catalog` 产物形态: `{"study": str, "items": [{form_oid, item_oid, label, ...}]}`)
- Produces: `StudyLookup(catalog: dict, aliases: list[dict] | None = None)`; `resolve(query: str) -> StudyLookupResult`; `StudyLookupResult(cards: list[str], form_scopes: list[str])` — `cards` 元素是**裸卡文件名** `f"{study}__{form_oid}__{item_oid}.md"`。Task 2/3 在同一个类上加通道; Task 4 只依赖 `resolve` 签名与 result 两个字段。

- [ ] **Step 1: 写失败测试** (合成 catalog; 家族 = 同 form + OID 首段相同)

```python
"""S2 StudyLookup 单元测试 — 合成 catalog, 零真实 OID/label (红线)."""
import pytest

from server.study_lookup import StudyLookup, StudyLookupResult


def _item(form, oid, label):
    return {"form_oid": form, "item_oid": oid, "label": label}


CATALOG = {
    "study": "stx",
    "items": [
        # 家族甲: 同 form + OID 首段 GRP → 3 卡 (label 只有其一可被题面引用)
        _item("FRM_A", "GRP_TOX", "偽末梢症状グレード"),
        _item("FRM_A", "GRP_REL", "治療との関係"),
        _item("FRM_A", "GRP_SER", "重い/重くない"),
        # 家族乙 (干扰): 同 form 不同首段, 不得被家族甲扩张带出
        _item("FRM_A", "OTH_TOX", "別症状グレード"),
        # 近义双卡: ABC_DEF_R vs XABC_DEF_R (label 相同; 段 ABC 只属前者)
        _item("FRM_B", "ABC_DEF_R", "実施の理由"),
        _item("FRM_B", "XABC_DEF_R", "実施の理由"),
        # 段家族: token QST 命中 QST_Q1/Q2
        _item("FRM_C", "QST_Q1", "1. 偽質問その一"),
        _item("FRM_C", "QST_Q2", "2. 偽質問その二"),
        # 短 label (<4 字, 不入 label 索引)
        _item("FRM_C", "SHT_X", "熱"),
    ],
}


def test_label_substring_hits_card_and_expands_family():
    lk = StudyLookup(CATALOG)
    res = lk.resolve("偽末梢症状グレードと治療との関係は別々の項目ですか?")
    assert "stx__FRM_A__GRP_TOX.md" in res.cards
    assert "stx__FRM_A__GRP_REL.md" in res.cards      # 家族扩张
    assert "stx__FRM_A__GRP_SER.md" in res.cards
    assert "stx__FRM_A__OTH_TOX.md" not in res.cards  # 别的首段不带出


def test_label_shorter_than_4_never_fires():
    lk = StudyLookup(CATALOG)
    assert lk.resolve("熱がありますか").cards == []


def test_ambiguous_label_over_cap_is_skipped():
    # 同 label 两卡 + 各自家族合计 > cap 时该 label 不 fire (保守)
    big = {"study": "stx", "items": [
        _item("FRM_D", f"FAM{i}_R", "同名ラベルです") for i in range(9)
    ]}
    lk = StudyLookup(big)
    assert lk.resolve("同名ラベルですはどこ?").cards == []


def test_no_match_returns_empty_result():
    lk = StudyLookup(CATALOG)
    res = lk.resolve("全然関係ない質問")
    assert res == StudyLookupResult(cards=[], form_scopes=[])


def test_nfkc_and_whitespace_normalized_label_match():
    lk = StudyLookup(CATALOG)
    # 全角/空白差异不阻断匹配
    res = lk.resolve("偽末梢症状　グレード について")
    assert "stx__FRM_A__GRP_TOX.md" in res.cards
```

- [ ] **Step 2: 跑测试确认失败**

Run: `cd sdtm-rag && .venv/bin/python -m pytest scripts/tests/test_study_lookup.py -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'server.study_lookup'`

- [ ] **Step 3: 最小实现**

```python
"""S2: study 侧确定性结构化直查 (Plan B Phase 2, spec 2026-08-04 §Phase 2).

golden v1.1 实测四类 miss 的确定性修复层: 数据源只有 catalog.json (+ 本地手工别名表),
零 LLM、不写卡片。契约对齐 S1: resolve(query) -> 要 union-add 的目标, 由 RAGEngine
前置注入。三条通道全部保守 — 不 fire 就回落纯检索, 绝不猜。

  ① label 全文子串: 卡 label (NFKC+去空白归一化, >=4 字) 逐字出现在问句里 →
     该卡 + 其 OID 首段家族 (同 form + item_oid 首段相同; group 不是家族单元,
     真实数据里一个 group 可混装几十个家族)。歧义 label (卡+家族 > cap) 整体跳过。
  ② 拉丁 token → OID 段: 问句中的大写 token (>=3 位) 精确匹配 item_oid 的下划线段
     → 该段的卡集合 (1 <= n <= cap 才 fire)。近义双卡 (X vs 前缀加长的 X') 的判别
     天然成立: token 是段级精确匹配, 不是子串。
  ③ 别名表 → form scope: 手工别名 (自然语言词 -> form_oid, 本地 yml, 有据可查,
     不写入卡片) 命中 → 交给注入层做域内 cosine top-N (词面排序对该类实测失效)。
"""
from __future__ import annotations

import re
import unicodedata
from collections import defaultdict
from dataclasses import dataclass, field

_LATIN_TOKEN_RE = re.compile(r"\b[A-Z][A-Z0-9]{2,}\b")
_MIN_LABEL_LEN = 4
_MIN_SEG_LEN = 3
_MAX_CARDS_PER_MATCH = 8   # 单个 label/token 命中集合上限, 超过 = 不具判别力, 跳过
_MAX_CARDS_TOTAL = 10      # resolve 输出的精确卡总上限 (k=15 里给 cosine 留位)


def _norm(s: str) -> str:
    """匹配用归一化: NFKC + 去全部空白 (label 与问句同变换)。"""
    return "".join(unicodedata.normalize("NFKC", s).split())


@dataclass
class StudyLookupResult:
    cards: list[str] = field(default_factory=list)
    form_scopes: list[str] = field(default_factory=list)


class StudyLookup:
    def __init__(self, catalog: dict, aliases: list[dict] | None = None):
        self.study_id = catalog["study"]
        items = catalog["items"]
        self.aliases: list[dict] = []   # Task 3 填充校验
        # label(归一化) -> [card_src]; (form, OID首段) -> [card_src]; 段 -> [card_src]
        self._label_index: dict[str, list[str]] = defaultdict(list)
        self._family: dict[tuple[str, str], list[str]] = defaultdict(list)
        self._segment_index: dict[str, list[str]] = defaultdict(list)
        self._card_family: dict[str, tuple[str, str]] = {}
        for it in items:
            src = f"{self.study_id}__{it['form_oid']}__{it['item_oid']}.md"
            ln = _norm(it["label"])
            if len(ln) >= _MIN_LABEL_LEN:
                self._label_index[ln].append(src)
            segs = it["item_oid"].split("_")
            fam = (it["form_oid"], segs[0])
            self._family[fam].append(src)
            self._card_family[src] = fam
            for seg in set(segs):
                if len(seg) >= _MIN_SEG_LEN:
                    self._segment_index[seg].append(src)

    def resolve(self, query: str) -> StudyLookupResult:
        qn = _norm(query)
        cards: list[str] = []

        def add(src: str) -> None:
            if src not in cards:
                cards.append(src)

        # ① label 全文子串 → 卡 + OID 首段家族 (歧义超 cap 整体跳过)
        for ln, srcs in self._label_index.items():
            if ln not in qn:
                continue
            expanded: list[str] = []
            for s in srcs:
                for member in self._family[self._card_family[s]]:
                    if member not in expanded:
                        expanded.append(member)
            if len(expanded) <= _MAX_CARDS_PER_MATCH:
                for s in expanded:
                    add(s)

        return StudyLookupResult(cards=cards[:_MAX_CARDS_TOTAL], form_scopes=[])
```

- [ ] **Step 4: 跑测试确认通过**

Run: `cd sdtm-rag && .venv/bin/python -m pytest scripts/tests/test_study_lookup.py -v`
Expected: 5 passed

- [ ] **Step 5: Commit**

```bash
git add sdtm-rag/server/study_lookup.py sdtm-rag/scripts/tests/test_study_lookup.py
git commit -m "feat(s2): StudyLookup label 通道 + OID 首段家族扩张 (Plan B P2 Task 1)"
```

---

### Task 2: 拉丁 token → OID 段通道

**Files:**
- Modify: `sdtm-rag/server/study_lookup.py` (resolve 内加通道②)
- Test: `sdtm-rag/scripts/tests/test_study_lookup.py` (追加)

**Interfaces:**
- Consumes: Task 1 的 `_segment_index`
- Produces: `resolve` 行为扩展, 签名不变

- [ ] **Step 1: 写失败测试**

```python
def test_latin_token_matches_oid_segment_family():
    lk = StudyLookup(CATALOG)
    res = lk.resolve("QSTは何問の設問で構成されていますか?")
    assert "stx__FRM_C__QST_Q1.md" in res.cards
    assert "stx__FRM_C__QST_Q2.md" in res.cards


def test_token_is_segment_exact_not_substring():
    # ABC 匹配段 ABC (ABC_DEF_R), 不匹配段 XABC (XABC_DEF_R) — 近义双卡判别
    lk = StudyLookup(CATALOG)
    res = lk.resolve("ABCを選択した場合、DEFの理由はどの項目?")
    assert "stx__FRM_B__ABC_DEF_R.md" in res.cards
    assert "stx__FRM_B__XABC_DEF_R.md" not in res.cards


def test_token_hitting_oversized_set_does_not_fire():
    big = {"study": "stx", "items": [
        _item("FRM_E", f"TOK_F{i}", f"別々のラベル{i}号") for i in range(9)
    ]}
    lk = StudyLookup(big)
    assert lk.resolve("TOK はどこですか").cards == []


def test_short_or_lowercase_tokens_ignored():
    lk = StudyLookup(CATALOG)
    # 2 位大写 (段 R 等) 与小写/混写词不触发
    assert lk.resolve("Q1 の grade を教えて").cards == []


def test_total_cards_capped_at_10():
    items = [_item("FRM_F", f"AAA_{i:02d}", f"箱{i:02d}のラベル") for i in range(12)]
    lk = StudyLookup({"study": "stx", "items": items})
    # cap=8 以内的两个 token 各 fire 也不超过总 cap —— 用两个 6 卡段验证
    items2 = ([_item("FRM_G", f"BBB_K{i}", f"甲{i}のラベル") for i in range(6)]
              + [_item("FRM_G", f"CCC_K{i}", f"乙{i}のラベル") for i in range(6)])
    lk2 = StudyLookup({"study": "stx", "items": items2})
    res = lk2.resolve("BBB と CCC の項目を全部")
    assert len(res.cards) == 10
```

- [ ] **Step 2: 跑测试确认失败**

Run: `cd sdtm-rag && .venv/bin/python -m pytest scripts/tests/test_study_lookup.py -v`
Expected: 新增 5 条 FAIL (token 通道未实装), Task 1 的 5 条仍 PASS

- [ ] **Step 3: 实现** — `resolve` 在通道①之后、`return` 之前插入:

```python
        # ② 拉丁 token → OID 段精确匹配 (段级, 非子串; 集合超 cap 不 fire)
        for tok in dict.fromkeys(_LATIN_TOKEN_RE.findall(query)):
            hits = self._segment_index.get(tok, [])
            if 1 <= len(hits) <= _MAX_CARDS_PER_MATCH:
                for s in hits:
                    add(s)
```

- [ ] **Step 4: 跑测试确认通过**

Run: `cd sdtm-rag && .venv/bin/python -m pytest scripts/tests/test_study_lookup.py -v`
Expected: 10 passed

- [ ] **Step 5: Commit**

```bash
git add sdtm-rag/server/study_lookup.py sdtm-rag/scripts/tests/test_study_lookup.py
git commit -m "feat(s2): 拉丁 token→OID 段通道 — 近义双卡段级判别 (Plan B P2 Task 2)"
```

---

### Task 3: 别名表通道 + from_paths 装载

**Files:**
- Modify: `sdtm-rag/server/study_lookup.py`
- Test: `sdtm-rag/scripts/tests/test_study_lookup.py` (追加)

**Interfaces:**
- Consumes: 别名 yml 形态 `{"aliases": [{"term": <自然语言词>, "form": <FORM_OID>}]}`
- Produces: `StudyLookup.from_paths(catalog_path: Path, aliases_path: Path | None) -> StudyLookup` (别名文件缺失 → 空别名不报错; catalog 缺失 → FileNotFoundError 响亮失败; 别名 form 不在 catalog → ValueError); `resolve` 填 `form_scopes`

- [ ] **Step 1: 写失败测试**

```python
import json


def test_alias_term_in_query_yields_form_scope():
    lk = StudyLookup(CATALOG, aliases=[{"term": "偽光線", "form": "FRM_A"}])
    res = lk.resolve("偽光線に関する項目はどれですか?")
    assert res.form_scopes == ["FRM_A"]


def test_alias_unknown_form_fails_loud():
    with pytest.raises(ValueError, match="NOFORM"):
        StudyLookup(CATALOG, aliases=[{"term": "偽語", "form": "NOFORM"}])


def test_from_paths_missing_aliases_file_is_empty(tmp_path):
    cat = tmp_path / "catalog.json"
    cat.write_text(json.dumps(CATALOG), encoding="utf-8")
    lk = StudyLookup.from_paths(cat, tmp_path / "no_such.yml")
    assert lk.aliases == []


def test_from_paths_missing_catalog_fails_loud(tmp_path):
    with pytest.raises(FileNotFoundError):
        StudyLookup.from_paths(tmp_path / "no_catalog.json", None)


def test_from_paths_loads_aliases(tmp_path):
    cat = tmp_path / "catalog.json"
    cat.write_text(json.dumps(CATALOG), encoding="utf-8")
    al = tmp_path / "lookup_aliases.yml"
    al.write_text("aliases:\n  - term: 偽光線\n    form: FRM_A\n", encoding="utf-8")
    lk = StudyLookup.from_paths(cat, al)
    assert lk.resolve("偽光線の項目").form_scopes == ["FRM_A"]
```

- [ ] **Step 2: 跑测试确认失败**

Run: `cd sdtm-rag && .venv/bin/python -m pytest scripts/tests/test_study_lookup.py -v`
Expected: 新增 5 条 FAIL

- [ ] **Step 3: 实现**

`__init__` 里替换 `self.aliases = []` 段:

```python
        known_forms = {it["form_oid"] for it in items}
        self.aliases = []
        for a in aliases or []:
            if a["form"] not in known_forms:
                raise ValueError(
                    f"alias form {a['form']!r} not in catalog forms — 别名表指向不存在的 form")
            self.aliases.append({"term": _norm(a["term"]), "form": a["form"]})
```

`resolve` 里 `return` 前加通道③, 并把 `form_scopes=[]` 改为 `form_scopes=scopes`:

```python
        # ③ 别名 → form scope (注入层做域内 cosine top-N; 词面排序对该类实测失效)
        scopes: list[str] = []
        for a in self.aliases:
            if a["term"] in qn and a["form"] not in scopes:
                scopes.append(a["form"])
```

类尾加装载器 (import 区补 `import json` / `from pathlib import Path` / `import yaml`):

```python
    @classmethod
    def from_paths(cls, catalog_path: Path, aliases_path: Path | None) -> "StudyLookup":
        """catalog 缺失 = 配置错误, 响亮失败; 别名表是可选增强, 缺失降级为空。"""
        catalog = json.loads(Path(catalog_path).read_text(encoding="utf-8"))
        aliases: list[dict] = []
        if aliases_path is not None and Path(aliases_path).exists():
            data = yaml.safe_load(Path(aliases_path).read_text(encoding="utf-8")) or {}
            aliases = data.get("aliases", []) or []
        return cls(catalog, aliases=aliases)
```

- [ ] **Step 4: 跑测试确认通过**

Run: `cd sdtm-rag && .venv/bin/python -m pytest scripts/tests/test_study_lookup.py -v`
Expected: 15 passed

- [ ] **Step 5: Commit**

```bash
git add sdtm-rag/server/study_lookup.py sdtm-rag/scripts/tests/test_study_lookup.py
git commit -m "feat(s2): 别名表通道 + from_paths 装载 (缺 catalog 响亮失败) (Plan B P2 Task 3)"
```

---

### Task 4: RAGEngine 注入层 `_apply_study_lookup`

**Files:**
- Modify: `sdtm-rag/server/rag.py` (ctor + retrieve 尾部 + 新方法 + merge 抽共用)
- Test: `sdtm-rag/scripts/tests/test_study_lookup.py` (追加 engine 段)

**Interfaces:**
- Consumes: Task 1-3 的 `resolve` / `StudyLookupResult`
- Produces: `RAGEngine(..., study_lookup=None)` 新关键字参数 (对象注入, rag.py 不 import study_lookup 模块); 注入行为: `cards` 每卡 `_search(query, 1, {"source": <裸文件名>})`, `form_scopes` 每 form `_search(query, 3, {"form_oid": <FORM>})`, 全部 `via_lookup=True` 前置, 与 cosine 去重合并到 k

- [ ] **Step 1: 写失败测试** (仿 `test_ja_tokenize.py` 的 `RAGEngine.__new__` + monkeypatch `_search` 模式)

```python
from types import SimpleNamespace

from server import rag as rag_mod


class _StubLookup:
    def __init__(self, cards=(), scopes=()):
        self._res = StudyLookupResult(cards=list(cards), form_scopes=list(scopes))

    def resolve(self, query):
        return self._res


def _chunk(cid, source):
    return SimpleNamespace(chunk_id=cid, source=source, via_lookup=False)


def _engine(lookup, search_log):
    eng = rag_mod.RAGEngine.__new__(rag_mod.RAGEngine)
    eng._study_lookup = lookup
    eng._structured_lookup = None

    def fake_search(query, n, where=None, query_embedding=None):
        search_log.append((n, where))
        if where and "source" in where:
            return [_chunk(f"lk:{where['source']}", where["source"])]
        if where and "form_oid" in where:
            return [_chunk(f"sc:{where['form_oid']}:{i}", f"x{i}.md") for i in range(n)]
        return []

    eng._search = fake_search
    return eng


def test_apply_study_lookup_prepends_cards_and_scopes_dedup_to_k():
    log = []
    eng = _engine(_StubLookup(cards=["stx__F__A.md"], scopes=["FRM_Z"]), log)
    cosine = [_chunk("lk:stx__F__A.md", "stx__F__A.md")] + [
        _chunk(f"c{i}", f"c{i}.md") for i in range(14)
    ]
    out = eng._apply_study_lookup("q", cosine, 15, query_embedding=None)
    assert out[0].chunk_id == "lk:stx__F__A.md" and out[0].via_lookup
    assert [c.chunk_id for c in out[1:4]] == ["sc:FRM_Z:0", "sc:FRM_Z:1", "sc:FRM_Z:2"]
    assert len(out) == 15
    assert len([c for c in out if c.chunk_id == "lk:stx__F__A.md"]) == 1  # 去重
    assert (1, {"source": "stx__F__A.md"}) in log
    assert (3, {"form_oid": "FRM_Z"}) in log


def test_apply_study_lookup_noop_when_resolve_empty():
    log = []
    eng = _engine(_StubLookup(), log)
    cosine = [_chunk(f"c{i}", f"c{i}.md") for i in range(20)]
    out = eng._apply_study_lookup("q", cosine, 15, query_embedding=None)
    assert [c.chunk_id for c in out] == [f"c{i}" for i in range(15)]
    assert log == []  # 不 fire 就零额外检索


def test_ctor_rejects_both_lookups(tmp_path):
    with pytest.raises(ValueError, match="study_lookup"):
        rag_mod.RAGEngine(
            chroma_dir=tmp_path, kb_root=tmp_path, collection_name="x",
            embedding_model="m", structured_lookup_enabled=True,
            study_lookup=_StubLookup(),
        )
```

- [ ] **Step 2: 跑测试确认失败**

Run: `cd sdtm-rag && .venv/bin/python -m pytest scripts/tests/test_study_lookup.py -v -k "apply_study or both_lookups"`
Expected: FAIL — `_apply_study_lookup` / `study_lookup` 参数不存在

- [ ] **Step 3: 实现** (rag.py 四处):

① ctor 签名加 `study_lookup=None`, 且在 `structured_lookup_enabled` 处理块**之前**加互斥闸:

```python
        if structured_lookup_enabled and study_lookup is not None:
            raise ValueError("structured_lookup (S1/CDISC) 与 study_lookup (S2/study) 互斥 — 一台引擎只挂一条直查通道")
        self._study_lookup = study_lookup
```

② `retrieve()` 里 `need_q_emb` 行加一个或:

```python
        need_q_emb = (
            self._structured_lookup is not None
            or self._study_lookup is not None
            or self.query_expansion != "hyde"
        )
```

③ `retrieve()` 尾部 S1 分支后加:

```python
        if self._study_lookup is not None:
            return self._apply_study_lookup(query, cosine, k, query_embedding=q_emb)
```

④ 新方法 + merge 抽共用 (把 `_apply_structured_lookup` 尾部的 merged/seen_ids 循环替换为 `return self._merge_lookup_first(lookup_chunks, cosine, k)`):

```python
    _STUDY_SCOPE_CHUNKS = 3   # form scope 域内 cosine 注入条数 (实测 gold 域内第 2 位)
    _STUDY_MAX_CARDS = 10     # 与 StudyLookup._MAX_CARDS_TOTAL 同值, 双保险

    def _apply_study_lookup(self, query, cosine, k, query_embedding=None):
        """S2 union-add: 精确卡每卡注入其 chunk (source=裸文件名 — study collection
        的元数据约定, 与 CDISC 的绝对路径不同), form scope 注入域内 cosine top-N
        (别名类 gold 与问句词面零重合, 词面排序实测失效, 只能语义收窄)。前置注入
        + 去重合并, resolve 不 fire 时零开销回落。"""
        res = self._study_lookup.resolve(query)
        if not res.cards and not res.form_scopes:
            return cosine[:k]
        lookup_chunks = []
        for src in res.cards[: self._STUDY_MAX_CARDS]:
            for ch in self._search(query, 1, {"source": src}, query_embedding=query_embedding):
                ch.via_lookup = True
                lookup_chunks.append(ch)
        for form in res.form_scopes:
            for ch in self._search(
                query, self._STUDY_SCOPE_CHUNKS, {"form_oid": form},
                query_embedding=query_embedding,
            ):
                ch.via_lookup = True
                lookup_chunks.append(ch)
        if not lookup_chunks:
            return cosine[:k]
        return self._merge_lookup_first(lookup_chunks, cosine, k)

    @staticmethod
    def _merge_lookup_first(lookup_chunks, cosine, k):
        merged, seen = [], set()
        for ch in lookup_chunks + cosine:
            if ch.chunk_id in seen:
                continue
            seen.add(ch.chunk_id)
            merged.append(ch)
        return merged[:k]
```

- [ ] **Step 4: 跑本文件 + S1 回归**

Run: `cd sdtm-rag && .venv/bin/python -m pytest scripts/tests/test_study_lookup.py scripts/tests/test_structured_lookup.py -v`
Expected: 全 passed (S1 merge 抽共用零行为变化)

- [ ] **Step 5: Commit**

```bash
git add sdtm-rag/server/rag.py sdtm-rag/scripts/tests/test_study_lookup.py
git commit -m "feat(s2): RAGEngine study_lookup 注入层 — 精确卡+form scope, S1/S2 互斥 (Plan B P2 Task 4)"
```

---

### Task 5: 接线 — config 开关 + main.py + run_eval `--study-lookup`

**Files:**
- Modify: `sdtm-rag/server/config.py`
- Modify: `sdtm-rag/server/main.py` (study 引擎构建块)
- Modify: `sdtm-rag/eval/run_eval.py`
- Test: `sdtm-rag/scripts/tests/test_run_eval_flags.py` (追加)

**Interfaces:**
- Consumes: `StudyLookup.from_paths` (Task 3), `RAGEngine(study_lookup=...)` (Task 4)
- Produces: settings `study_lookup_enabled: bool = False` / `study_catalog_path` / `study_aliases_path`; CLI `--study-lookup` (需 `--collection` 或 `--federated`, 否则 parser.error); summary 键 `study_lookup: true`

- [ ] **Step 1: 写失败测试** (仿 test_run_eval_flags.py 既有风格追加; 下面是意图, 断言方式对齐该文件现有 parse/构造测试的写法)

```python
def test_study_lookup_requires_collection_or_federated():
    # run_eval --study-lookup 单独给 → parser.error (SystemExit 2)
    with pytest.raises(SystemExit):
        run_eval_main(["dummy.yml", "--study-lookup", "--retrieval-only"])


def test_settings_study_lookup_defaults():
    from server.config import Settings
    s = Settings()
    assert s.study_lookup_enabled is False        # Task 8 才翻 True
    assert s.study_catalog_path.name == "catalog.json"
    assert s.study_aliases_path.name == "lookup_aliases.yml"
```

- [ ] **Step 2: 跑测试确认失败**

Run: `cd sdtm-rag && .venv/bin/python -m pytest scripts/tests/test_run_eval_flags.py -v -k study_lookup`
Expected: FAIL

- [ ] **Step 3: 实现**

`server/config.py` (study 设置块内, 沿用 `_SDTM_RAG_ROOT` 既有写法):

```python
    # S2 study 结构化直查 (Plan B Phase 2)。默认关; 验收闸全绿后翻 True (对齐 Phase 1 rollout 惯例)
    study_lookup_enabled: bool = False
    study_catalog_path: Path = _SDTM_RAG_ROOT / "data" / "study" / "st01" / "catalog.json"
    study_aliases_path: Path = _SDTM_RAG_ROOT / "data" / "study" / "st01" / "lookup_aliases.yml"
```

`server/main.py` study 引擎块 (federation 分支内, `rag_study = RAGEngine(...)` 前):

```python
        study_lookup = None
        if s.study_lookup_enabled:
            from server.study_lookup import StudyLookup
            # catalog 缺失时这里响亮失败 — 开关开着但数据不在 = 配置错误, 不静默降级
            study_lookup = StudyLookup.from_paths(s.study_catalog_path, s.study_aliases_path)
```

并在 `rag_study = RAGEngine(...)` 调用里加 `study_lookup=study_lookup,`; 该块原有注释 "S1 ... 恒关" 后补一句 `S2 (study_lookup) 按 settings 开关注入`。

`eval/run_eval.py`:

```python
    parser.add_argument(
        "--study-lookup", action="store_true",
        help="S2: study 侧确定性直查 union-add (catalog+别名表)。需 --collection <study "
             "collection> 或 --federated (作用于其 study 引擎)",
    )
```

flag 校验 (federated 互斥检查同段):

```python
    if args.study_lookup and not (args.collection or args.federated):
        parser.error("--study-lookup 需要 --collection 或 --federated")
```

构造 (两个注入点):

```python
    study_lookup = None
    if args.study_lookup:
        from server.study_lookup import StudyLookup
        study_lookup = StudyLookup.from_paths(
            settings.study_catalog_path, settings.study_aliases_path)
```

- collection 模式: 主 `RAGEngine(...)` 调用加 `study_lookup=study_lookup,` (S1 已被 `--collection` 强制 OFF, 互斥闸不会触发);
- federated 模式: `study_rag = RAGEngine(...)` 调用加 `study_lookup=study_lookup,`, 并把打印行 `structured_lookup=OFF` 后补 `, study_lookup={'ON' if study_lookup else 'OFF'}`;
- summary: `if args.study_lookup: summary["study_lookup"] = True`。

- [ ] **Step 4: 跑测试 + 全量**

Run: `cd sdtm-rag && .venv/bin/python -m pytest scripts/tests/test_run_eval_flags.py scripts/tests/test_study_lookup.py -v` 然后全量 `.venv/bin/python -m pytest scripts/tests/ -q`
Expected: 新增全 passed; 全量 ≥ 720 + 本计划新增, 0 failed

- [ ] **Step 5: Commit**

```bash
git add sdtm-rag/server/config.py sdtm-rag/server/main.py sdtm-rag/eval/run_eval.py sdtm-rag/scripts/tests/test_run_eval_flags.py
git commit -m "feat(s2): 接线 — config 开关(默认关)/main.py 注入/run_eval --study-lookup (Plan B P2 Task 5)"
```

---

### Task 6: 真数据别名文件 + 验收闸 (4 miss 转命中 + 25 题逐题零回归)

**Files:**
- Create (本地, 不入库): `sdtm-rag/data/study/st01/lookup_aliases.yml` (内容 = NOTES §q08 的 1 条别名)
- Create (本地, 不入库): `sdtm-rag/data/study/st01/eval/runs/planb_p2_s2_hybrid.json`

**Interfaces:**
- Consumes: Task 5 的 CLI; 本地 `PLANB_P2_NOTES.md` (别名条目 + 4 题预期)
- Produces: 验收数字 (写入 Task 8 checkpoint)

- [ ] **Step 1: 按 NOTES §q08 写 `data/study/st01/lookup_aliases.yml`** (1 条 term→form; 真名只进这个 gitignored 文件)

- [ ] **Step 2: 跑 S2 组**

```bash
cd sdtm-rag && .venv/bin/python -m eval.run_eval \
  data/study/st01/eval/test_set_study_v1_1.yml \
  --retrieval-only --hybrid --study-lookup \
  --collection study_st01 --kb-root data/study/st01/cards \
  --output data/study/st01/eval/runs/planb_p2_s2_hybrid.json
```

Expected: 无异常, summary 含 `"study_lookup": true`

- [ ] **Step 3: 逐题配对 diff vs 基线** (基线 = `runs/v1_1_hybrid_bigram.json`, 88.53%)

```bash
cd sdtm-rag && .venv/bin/python - <<'EOF'
import json
base = {q["id"]: q.get("source_recall") for q in json.load(open(
    "data/study/st01/eval/runs/v1_1_hybrid_bigram.json"))["results"]}
new = {q["id"]: q.get("source_recall") for q in json.load(open(
    "data/study/st01/eval/runs/planb_p2_s2_hybrid.json"))["results"]}
regressions = {k: (base[k], new[k]) for k in base
               if base[k] is not None and new[k] < base[k]}
fixed = {k: (base[k], new[k]) for k in ("st01_v11_q08", "st01_v11_q14",
             "st01_v11_q16", "st01_v11_q21")}
print("fixed:", fixed)
print("regressions:", regressions)
assert not regressions, "零回归闸 FAIL"
assert all(v[1] == 1.0 for v in fixed.values()), "4 miss 转命中闸 FAIL"
print("PASS")
EOF
```

Expected: `regressions: {}` 且 4 题全 `→ 1.0`, 打印 PASS。(若 results 键名与实际 run JSON 不符, 以 run JSON 实际结构为准调整脚本 — 断言语义不变: 4 题=1.0, 其余逐题不降。)

- [ ] **Step 4: FAIL 时** — 按规则 B 把失败 run 归档 `data/study/st01/eval/runs/` 下 (attempt 序号), 回 Task 1-4 修通道, **不得**用改 gold / 改题面的方式过闸

- [ ] **Step 5: Commit** (只有代码/测试可提交; 别名 yml 与 run JSON 在 gitignore 区, 不入库。若本 task 零代码改动则跳过 commit)

---

### Task 7: 规则 D 独立复审

- [ ] **Step 1: 派独立 reviewer** (与实现方不同 subagent_type, 如 `feature-dev:code-reviewer` 或 `oh-my-claudecode:code-reviewer`), 审查范围: Task 1-6 全部 diff + 本计划偏差声明 (近义双卡用 OID 段判别替代 codelist/显示条件) + 红线扫描 (committed 内容零真名: `git diff b_start..HEAD | grep` 逐一核对 NOTES 里列出的真实 OID/label/term 不出现)
- [ ] **Step 2: reviewer 发现的 BLOCKER/HIGH 全修, 复跑 Task 6 Step 2-3 闸**
- [ ] **Step 3: 修复 commit** (`fix(s2): 复审 round N — <要点>`)

---

### Task 8: Rollout — 默认翻 True + 联邦复核 + 生产冒烟 + 收口

**Files:**
- Modify: `sdtm-rag/server/config.py` (`study_lookup_enabled: bool = True`)
- Create: `sdtm-rag/evidence/checkpoints/planb_phase2_study_lookup.md`
- Modify: `docs/PROGRESS.md` / `.work/meta/worklog/phase_07_rag_kg.md` (收尾)

- [ ] **Step 1: 联邦通道复核** — S2 经 federated 路径生效性 (对齐 Phase 1 闸 3 惯例):

```bash
cd sdtm-rag && .venv/bin/python -m eval.run_eval \
  data/study/st01/eval/test_set_study_v1_1.yml \
  --retrieval-only --hybrid --study-lookup --federated \
  --output data/study/st01/eval/runs/planb_p2_s2_federated.json
```

Expected: 25 计分题 avg 与 Task 6 S2 组一致 (routed both 的题允许 top5 集合差异但 recall 不降 — Phase 1 已知形态); CDISC 侧零改动不需重跑 (S2 不触碰 cdisc 引擎与路由 prompt, 代码层面可证)

- [ ] **Step 2: 翻默认** — `study_lookup_enabled: bool = True` (注释改为 "默认开 (2026-08-XX, Phase 2 验收闸全绿后翻 True)")

- [ ] **Step 3: 全量测试**

Run: `cd sdtm-rag && .venv/bin/python -m pytest scripts/tests/ -q`
Expected: ≥ 720 + 新增, 0 failed 0 skipped

- [ ] **Step 4: 重启生产 + 冒烟**

```bash
launchctl kickstart -k gui/$(id -u)/com.sdtmrag.api
sleep 5 && curl -s localhost:8000/api/info | python3 -m json.tool | head -20
```

再用本地题集里 q08 的题面 (从 NOTES/题集读, 不写进任何 committed 文件) POST `/api/ask` (`corpus: "study"`), 确认 sources 含其 gold 卡。启动日志零 traceback。

- [ ] **Step 5: 写收口证据** `evidence/checkpoints/planb_phase2_study_lookup.md` — 红线同 Phase 1 (只含统计/题 id/结构描述): 范围表 / 三通道机制 / 验收数字 (4 题修复前后 + 25 题 avg 前后 + 逐题零回归声明 + 联邦复核) / 测试数演进 / 决策与已知限制 (近义双卡实装偏差; 别名表当前 1 条; `_FederatedAdapter.build_messages` corpus 硬编码仍是答题 eval 硬前置 — 本轮未动) / 复跑与回滚 (`SDTM_RAG_STUDY_LOOKUP_ENABLED=false`)

- [ ] **Step 6: 收尾** — 按 CLAUDE.md wrap-up checklist: worklog `phase_07_rag_kg.md` append + `docs/PROGRESS.md` (Phase 7 行 Plan B Phase 2 DONE + 下一步改 Phase 3/4) + memory `project_plan_b_phase1` 更新 (Phase 2 收口, 剩 3/4) + 单 commit push

```bash
git add -A ':!sdtm-rag/data/study' && git commit -m "feat(s2): Plan B Phase 2 收官 — study 结构化直查三通道, 4 miss 转命中 + 25 题零回归, 默认启用" && git push
```

---

## Self-Review 记录 (规划时已做)

1. **Spec 覆盖**: spec §Phase 2 四类 miss → 通道映射齐 (家族=①/②, 近义双卡=② [偏差已声明], ID 语义脱钩=① label 子串 [q21 同机制], form 缩写=③); S1 契约对齐 (resolve→union-add 前置注入); 验收两条全进 Task 6; "数据源全部来自 catalog/config report 确定性产物" ✓ (catalog.json + 手工别名表, 零 LLM)。
2. **机制实证**: 4 题通道全部经 2026-08-06 探针实测 (见 NOTES): q21 label 唯一命中+家族恰为 gold 3 卡; q16 段集合 6⊇gold5; q14 段级判别天然成立; q08 域内 dense gold 第 2 位 (词面排序实测失效, 故 scope 用 cosine)。
3. **类型一致**: `StudyLookupResult.cards/form_scopes` 贯穿 Task 1-4; `resolve(query)->StudyLookupResult` 签名三处一致; `from_paths(catalog_path, aliases_path)` Task 3 定义 = Task 5 调用。
4. **红线自查**: 本文件零真实 OID/label/term/题面; 真名只在 `data/study/st01/{lookup_aliases.yml,eval/PLANB_P2_NOTES.md}` (gitignored)。
