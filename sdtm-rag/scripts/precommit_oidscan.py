#!/usr/bin/env python3
"""pre-commit 闸: 对**暂存文件**跑 oidscan_evidence, 拦下带真实 OID/label 的提交。

为什么只扫暂存文件而不是整个默认面: 闸的匹配是"1600+ needle 编进一条交替正则,
逐文件逐行跑", 实测 **62 ms/文件** —— 默认面 205 个文件要 10 秒。一个每次 commit
加 10 秒的 hook 迟早被 `--no-verify` 绕过, 那是"纸面规则等于没规则"换个死法。
暂存文件典型 1-5 个, 约 0.3 秒。

为什么不做成 pytest / GitHub Actions: needle 源 `data/study/st01/catalog.json` 是
gitignored 且**永远不能推**(它就是要保护的东西), 所以 CI 里根本没有 needle 源,
闸只会 fail-closed。一条在干净检出里永远 skip 的测试就是装饰闸。
"""

import argparse
import os
import subprocess
import sys
from pathlib import Path

from scripts import oidscan_evidence
from scripts.oidscan_evidence import _BINARY_EXT, DEFAULT_CATALOG, GIT_ROOT


def select_targets(staged: list[str], repo_root: Path) -> list[Path]:
    """暂存清单 → 实际要扫的文件。

    剔除两类: (1) 已删除/已改名走掉的路径 —— 留着会让闸因"路径不存在"fail-closed,
    把一次纯删除的提交误拦; (2) 二进制扩展名 —— 闸自己也会跳过, 留着只是白跑。
    """
    out = []
    for rel in staged:
        p = repo_root / rel
        if p.suffix.lower() in _BINARY_EXT:
            continue
        if not p.is_file():
            continue
        out.append(p)
    return out


def git_staged_files(repo_root: Path) -> list[str]:
    """暂存区里新增/修改/改名后存在的路径 (相对仓库根)。用 -z 以容忍带空格/非 ASCII
    的路径名 —— 本仓有大量中日文文件名。"""
    out = subprocess.run(
        ["git", "diff", "--cached", "--name-only", "--diff-filter=ACM", "-z"],
        cwd=repo_root, capture_output=True, text=True, check=True,
    ).stdout
    return [x for x in out.split("\0") if x]


def main(argv=None, staged=None) -> int:
    ap = argparse.ArgumentParser(description="pre-commit OID/label 泄漏闸 (只扫暂存文件)")
    ap.add_argument("--catalog", type=Path, default=DEFAULT_CATALOG)
    ap.add_argument("--repo-root", type=Path, default=GIT_ROOT)
    args = ap.parse_args(argv)

    if staged is None:
        staged = git_staged_files(args.repo_root)
    targets = select_targets(staged, args.repo_root)
    if not targets:
        print("[oidscan] 无可扫文件 (暂存项全是二进制/删除), 放行")
        return 0

    if not args.catalog.is_file():
        if os.environ.get("OIDSCAN_NO_CATALOG") == "1":
            print(f"[oidscan] ⚠ 已按 OIDSCAN_NO_CATALOG=1 跳过: catalog 不在本机 "
                  f"({args.catalog})。**本次提交未经任何 OID/label 泄漏检查。**")
            return 0
        print(f"[oidscan] ⛔ 拦下提交: catalog 不在本机 ({args.catalog})。\n"
              f"          没有 needle 源就没有任何扫描保证 —— 与闸自身同一 fail-closed 纪律。\n"
              f"          确实要在无 catalog 的机器上提交, 用具名逆转:\n"
              f"              OIDSCAN_NO_CATALOG=1 git commit ...\n"
              f"          (别用 --no-verify: 它会顺手关掉未来所有 hook, 且不留痕。)")
        return 1

    # 复用闸的 main —— 不另写一套匹配/掩码逻辑, 免得 hook 与手跑两条路径悄悄分叉
    rc = oidscan_evidence.main([*(str(t) for t in targets), "--catalog", str(args.catalog)])
    if rc == 0:
        return 0
    print(f"\n[oidscan] ⛔ 拦下提交 (闸 rc={rc})。上面是掩码明细, 定位够用但不泄漏真值。\n"
          f"          真要看真值 (仅限本机排查):\n"
          f"              ./.venv/bin/python scripts/oidscan_evidence.py <文件> --show-values\n"
          f"          若判定是撞车而非泄漏, 往 oidscan_evidence.py 的 ALLOWLIST 加一条 "
          f"(路径, needle) 并附理由 —— 别用 --no-verify 蒙混过去。")
    return 1


if __name__ == "__main__":
    sys.exit(main())
