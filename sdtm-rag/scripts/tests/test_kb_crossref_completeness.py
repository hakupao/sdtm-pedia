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
