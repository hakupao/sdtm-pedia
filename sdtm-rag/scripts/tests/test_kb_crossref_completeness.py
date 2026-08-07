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


def _spec_own_ct_map(spec: Path) -> dict[str, set[str]]:
    """单个 spec.md 自身变量表反建 `码 -> {VAR}` (裸变量名, 无域前缀)。"""
    out: dict[str, set[str]] = {}
    var = None
    for line in spec.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^###\s+(\S+)\s*$", line)
        if m:
            var = m.group(1)
            continue
        m2 = re.match(r"^-\s+\*\*Controlled Terms:\*\*\s*(.*)$", line)
        if m2 and var:
            for code in re.findall(r"C\d+", m2.group(1)):
                out.setdefault(code, set()).add(var)
    return out


def test_domain_spec_crossref_lists_every_variable_of_that_codelist():
    """域 spec 的交叉引用段必须列全该域引用该码表的所有变量。

    此前这一侧**只查 `... (N total)` 字符串**, 比 VI 侧弱得多: 把
    `generate_cross_references.py` 改回 `", ".join(var_names[:5])` 但不写 marker,
    10 条隐藏引用回来了而断言全绿 (审查方 MEDIUM-3)。

    参照物是**该 spec 自己的变量表**, 不是 §三 —— 用 §三 当参照会把两处的差异混为一谈。"""
    line_re = re.compile(r"^-\s+\[.*?\((C\d+)\)\]\([^)]*\)\s+—\s+(.+)$")
    bad = []
    for spec in sorted((KB_ROOT / "domains").glob("*/spec.md")):
        own = _spec_own_ct_map(spec)
        for line in spec.read_text(encoding="utf-8").splitlines():
            m = line_re.match(line)
            if not m:
                continue
            code, listed = m.group(1), {x.strip() for x in m.group(2).split(",") if x.strip()}
            expected = own.get(code, set())
            if expected and listed != expected:
                bad.append((spec.parent.name, code,
                            f"少 {sorted(expected - listed)} 多 {sorted(listed - expected)}"))
    assert not bad, f"域 spec 交叉引用段与自身变量表不符: {bad[:5]} (共 {len(bad)})"


def _spec_ct_pairs() -> dict[str, set[str]]:
    """从 domains/*/spec.md 的 CT 字段反建 `码 -> {DOMAIN.VAR}` —— §三 的外部锚。

    **取全部 C 码, 不是首码**: CT 字段可以是 `C85494; C128684; C128683; ...`,
    该变量对这几个码表都是真引用。
    """
    out: dict[str, set[str]] = {}
    for spec in sorted((KB_ROOT / "domains").glob("*/spec.md")):
        domain = spec.parent.name
        var = None
        for line in spec.read_text(encoding="utf-8").splitlines():
            m = re.match(r"^###\s+(\S+)\s*$", line)
            if m:
                var = m.group(1)
                continue
            m2 = re.match(r"^-\s+\*\*Controlled Terms:\*\*\s*(.*)$", line)
            if m2 and var:
                for code in re.findall(r"C\d+", m2.group(1)):
                    out.setdefault(code, set()).add(f"{domain}.{var}")
    return out


def test_section3_covers_every_ct_reference_declared_by_the_specs():
    """§三 必须覆盖 domains/*/spec.md 声明的每一个 (码, 变量) 引用。

    **这条是外部锚, 上面那条不是。** `test_every_ct_row_lists_all_the_variables_it_claims`
    比的是"条目数 == 该行自己声称的 N", 两个值出自生成器同一条 f-string —— 自洽即通过。
    有人把切片放在计数之前 (`refs = sorted(...)[:15]` 再 `ref_count = len(refs)`), 5 条
    断言全绿而 226 条静默消失 (审查方已构造伪造 KB 实证)。

    本条改用 spec.md 的 CT 字段反建期望集, 于是"§三 少了谁"当场显形。
    它也是 12 个码表整行缺失 (生成器只取 CT 字段首码) 这个既有缺陷的捕获者。

    局限: spec.md 是该生成器的**输入**, 故本条证明的是"输入→输出忠实", 不是"输入本身对"。
    输入正确性由 source/cdisc/*.xlsx 的独立对照负责 (规则 A 抽检, 非 CI 常驻)。"""
    expected = _spec_ct_pairs()
    actual = {c: {x.strip() for x in v.split(", ") if x.strip()} for c, _n, v in _ct_rows()}

    missing_rows = sorted(set(expected) - set(actual))
    incomplete = {c: sorted(expected[c] - actual[c])
                  for c in set(expected) & set(actual) if expected[c] - actual[c]}
    spurious = {c: sorted(actual[c] - expected[c])
                for c in set(expected) & set(actual) if actual[c] - expected[c]}

    assert not missing_rows, f"§三 整行缺失的码表 ({len(missing_rows)}): {missing_rows}"
    assert not incomplete, f"§三 少列的引用: {dict(list(incomplete.items())[:5])}"
    assert not spurious, f"§三 多列的引用 (spec 里没有): {dict(list(spurious.items())[:5])}"


def test_ct_row_count_matches_the_specs():
    """§三 行数必须等于 spec.md 声明的**不同码表数** —— 不写死数字。

    原先写死 135 有两个毛病: (a) 它同时充当 `_CT_ROW_RE` 漏匹配的哨兵却没说;
    (b) 修好首码提取后 135 会变, 硬编码等于每次都要人改。改为对外部锚推导。"""
    assert len(_ct_rows()) == len(_spec_ct_pairs())


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
    for code, _n, refs in _ct_rows():
        doc = by_section.get(f"§三 CT 交叉引用: {code}")
        if doc is None:
            bad.append((code, "section 不在索引"))
            continue
        missing = [r.strip() for r in refs.split(", ") if r.strip() and r.strip() not in doc]
        if missing:
            bad.append((code, f"正文缺 {len(missing)} 个, 例: {missing[:3]}"))
    assert not bad, f"索引里的 CT chunk 与 KB 不一致: {bad[:5]} (共 {len(bad)})"
