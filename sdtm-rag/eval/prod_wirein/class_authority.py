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
