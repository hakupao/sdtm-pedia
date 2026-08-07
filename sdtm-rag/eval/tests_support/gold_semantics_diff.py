"""判据等价性差分对拍: 旧版 `check_source_recall` vs 当前工作树版。

**什么时候必须跑它**: 改 `eval/run_eval.py` 的 `source_matches` /
`check_source_recall` **之前和之后**各跑一次。这两个函数是 CDISC 140 题全部
分数的判据实现 —— 改动一旦悄悄改变语义, 所有历史分数当场不可比, 而 eval
本身**看不出来** (140 题里 138 题是 1.0, 用到 `#` / `$` 语法的只有个位数,
三条抛错分支在 eval 里根本走不到)。

**为什么不能只看 eval 的 Δ0**: 这是 2026-08-07 Task 2 评审推翻控制器验收标准时
定下的举证序 —— 主证据是单测 + 本差分对拍, eval 逐题 Δ0 只能当"生产口径没冒烟"
的旁证。低分辨率的仪器给出的 Δ0 不构成等价性证明。

对拍内容, 逐格比较**三样**:
  1. 返回的 `(recall, hits, misses)` 三元组 (不只 recall 标量);
  2. 抛出的异常类型 + 异常消息全文;
  3. docstring 的非空行集合 (防止重构时把成文纪律注释删掉)。

输入网格 = 合成用例 (含空路径 / 多 `#` / `$` 不在末尾 / 空 gold 等边界)
× 仓内**全部真实 gold 字符串** × 检索结果集 × section 列表 (含 `None` 混入)。
2026-08-07 首跑规模 12870 格, mismatches 0。

用法:

    cd sdtm-rag
    # 默认: 工作树 vs HEAD (改之前跑一次拿基线, 改之后再跑一次)
    .venv/bin/python -m eval.tests_support.gold_semantics_diff

    # 复现 Task 2 那次历史对拍 (重构前 501875b vs 重构后)
    .venv/bin/python -m eval.tests_support.gold_semantics_diff --old-ref 501875b

退出码: 0 = 逐格一致; 1 = 有 mismatch (逐条打印); 2 = 取旧版本失败。

注意 `--old-ref` 指向的那一版**会被 exec**, 只传你信得过的 ref。
"""

from __future__ import annotations

import argparse
import importlib.util
import itertools
import subprocess
import sys
import tempfile
from pathlib import Path

import yaml

# sdtm-rag/ 仓根 (本文件在 eval/tests_support/ 下)
ROOT = Path(__file__).resolve().parents[2]
# 旧版本在 git 里的路径是**仓根相对**的, 而本文件所在的 python 包根是 sdtm-rag/
GIT_PATH = "sdtm-rag/eval/run_eval.py"

# ---- 输入网格 ---------------------------------------------------------------
SRC_SETS: list[list[str]] = [
    [],
    ["kb/chapters/ch04_general_assumptions.md"],
    ["kb/chapters/ch04_general_assumptions.md", "kb/chapters/ch02_fundamentals.md"],
    ["kb/VARIABLE_INDEX.md", "kb/VARIABLE_INDEX.md"],
    [
        "kb/domains/TE/spec.md",
        "kb/chapters/ch04_general_assumptions.md",
        "kb/model/02_observation_classes.md",
    ],
]
SEC_SETS: list[list[str | None] | None] = [
    None,
    [],
    ["4.2.2 Two-character Domain Identifier"],
    [None],
    ['4.2.3 Use of "Subject" and USUBJID'],
    ["§一 通用变量: ARMCD"],
    ["§一 通用变量: ARM"],
    [None, "4.2.2 Two-character Domain Identifier"],
    ["4.2.2 Two-character Domain Identifier", None],
    ["whole_file", "whole_file"],
    ["DOMAIN", "4.2.2 Two-character Domain Identifier", None],
]
SYNTHETIC_GOLDS: list[str] = [
    "chapters/ch02",
    "chapters/ch04_general_assumptions.md#4.2.2 Two-character Domain Identifier$",
    "chapters/ch04_general_assumptions.md#4.2.2 Two-character Domain Identifier",
    "chapters/ch04_general_assumptions.md#4.2.2",
    "chapters/ch04_general_assumptions.md#",
    "chapters/ch04_general_assumptions.md#$",
    "chapters/ch04_general_assumptions.md#   ",
    "chapters/ch04_general_assumptions.md#   $",
    "VARIABLE_INDEX.md#§一 通用变量: ARM",
    "VARIABLE_INDEX.md#§一 通用变量: ARM$",
    "#4.2.2",  # 空路径
    "a#b#c",  # 多个 #
    "a#b$c",  # $ 不在末尾
    "domains/TE/spec.md",
    "no/such/path",
    "",  # 空 gold
    "whole_file",
]
# 多 gold 组合 (对顺序 / 短路敏感): (expected_sources, any_of)
COMBOS: list[tuple[list[str], list[str] | None]] = [
    (
        [
            "chapters/ch02",
            "chapters/ch04_general_assumptions.md#4.2.2 Two-character Domain Identifier$",
        ],
        None,
    ),
    (["chapters/ch02"], ["chapters/ch04_general_assumptions.md#4.2.2", "no/such"]),
    ([], ["no/such", "domains/TE/spec.md"]),
    (["chapters/ch04_general_assumptions.md#"], ["chapters/ch02"]),  # AND 侧抛错
    (["chapters/ch02"], ["chapters/ch04_general_assumptions.md#"]),  # OR 侧抛错
    (["a#b", "chapters/ch02"], ["whole_file"]),
    ([], []),
    ([], None),
]
TEST_SETS = [
    "eval/test_set_v1.yml",
    "eval/test_set_v2.yml",
    "eval/test_set_v3.yml",
    "eval/test_set_vi_completeness.yml",
]


def load_old_impl(ref: str):
    """从 git 取 `ref` 版本的 run_eval.py 并 exec 成独立模块。"""
    try:
        src = subprocess.run(
            ["git", "show", f"{ref}:{GIT_PATH}"],
            cwd=ROOT.parent,
            capture_output=True,
            check=True,
        ).stdout.decode("utf-8")
    except subprocess.CalledProcessError as e:
        print(f"取旧版本失败: git show {ref}:{GIT_PATH}\n{e.stderr.decode('utf-8', 'replace')}")
        raise SystemExit(2) from e

    with tempfile.TemporaryDirectory() as td:
        path = Path(td) / "old_run_eval.py"
        with open(path, "w", encoding="utf-8") as f:
            f.write(src)
        spec = importlib.util.spec_from_file_location("old_run_eval", path)
        assert spec and spec.loader
        mod = importlib.util.module_from_spec(spec)
        sys.modules["old_run_eval"] = mod
        spec.loader.exec_module(mod)
    return mod


def collect_real_golds() -> set[str]:
    """仓内四个题集里出现过的**全部** gold 字符串。"""
    golds: set[str] = set()
    for name in TEST_SETS:
        p = ROOT / name
        if not p.exists():
            print(f"  (缺失, 跳过) {name}")
            continue
        with open(p, encoding="utf-8") as f:
            for q in yaml.safe_load(f) or []:
                for key in ("expected_sources", "expected_sources_any"):
                    for g in q.get(key) or []:
                        golds.add(g)
    return golds


def call(fn, *args, **kwargs):
    """把返回值与异常统一成可比较的元组。"""
    try:
        return ("ok", fn(*args, **kwargs))
    except Exception as e:  # noqa: BLE001 — 差分对拍要覆盖所有异常类型
        return ("raise", type(e).__name__, str(e))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument(
        "--old-ref",
        default="HEAD",
        help="旧版本的 git ref (默认 HEAD, 即拿工作树与已提交版对拍)。"
        " 501875b = Task 2 重构前的历史基线。",
    )
    ap.add_argument("--max-print", type=int, default=10, help="最多打印几条 mismatch")
    args = ap.parse_args()

    sys.path.insert(0, str(ROOT))
    from eval.run_eval import check_source_recall as new_csr

    old = load_old_impl(args.old_ref)
    old_csr = old.check_source_recall

    real_golds = collect_real_golds()
    print(f"旧版本: {args.old_ref}:{GIT_PATH}")
    print(f"真实 gold 字符串: {len(real_golds)} 条")

    mismatches: list[tuple] = []
    n = 0

    # pass 1: 单 gold, AND 侧与 OR 侧各一遍
    all_golds = SYNTHETIC_GOLDS + sorted(real_golds)
    for gold, srcs, secs in itertools.product(all_golds, SRC_SETS, SEC_SETS):
        for kwargs in ({"expected_sources": [gold]}, {"expected_sources": [], "any_of": [gold]}):
            n += 1
            a = call(old_csr, srcs, retrieved_sections=secs, **kwargs)
            b = call(new_csr, srcs, retrieved_sections=secs, **kwargs)
            if a != b:
                mismatches.append((gold, srcs, secs, kwargs, a, b))

    # pass 2: AND + OR 同时给 (对顺序 / 短路敏感)
    for (exp, anyof), srcs, secs in itertools.product(COMBOS, SRC_SETS, SEC_SETS):
        n += 1
        a = call(old_csr, srcs, exp, anyof, secs)
        b = call(new_csr, srcs, exp, anyof, secs)
        if a != b:
            mismatches.append((exp, anyof, srcs, secs, a, b))

    print(f"对拍格数: {n}")
    print(f"mismatches: {len(mismatches)}")
    for m in mismatches[: args.max_print]:
        print("  MISMATCH", m)

    # docstring 非空行集合 (防重构顺手删掉成文纪律)
    old_lines = [ln.strip() for ln in (old_csr.__doc__ or "").splitlines() if ln.strip()]
    new_lines = [ln.strip() for ln in (new_csr.__doc__ or "").splitlines() if ln.strip()]
    dropped = [ln for ln in old_lines if ln not in new_lines]
    added = [ln for ln in new_lines if ln not in old_lines]
    print(f"docstring: 旧 {len(old_lines)} 非空行 / 新 {len(new_lines)}")
    print(f"  dropped: {dropped}")
    print(f"  added:   {added}")

    return 1 if mismatches else 0


if __name__ == "__main__":
    raise SystemExit(main())
