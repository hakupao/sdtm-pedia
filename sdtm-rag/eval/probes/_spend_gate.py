"""探针的共用花钱闸。

`eval/probes/` 下的脚本会**真打 provider**, 每次运行都产生费用。它们被提交进仓库是为了
让 checkpoint 里的"实测"可复跑 (否则那些数字只在写它的那台机器上成立), 但可提交也意味着
它们会被 tab 补全、被 `python eval/probes/*.py` 顺手扫到、被 CI 误收。
⇒ 一律要求显式 `--yes-spend`, 空跑只打印说明并以 0 退出。
"""
from __future__ import annotations

import sys


def require_spend_consent(what: str, cost: str) -> None:
    """没有 `--yes-spend` 就打印说明并退出 (退出码 0 —— 这不是错误, 是没被授权)。"""
    if "--yes-spend" in sys.argv:
        return
    print(f"{what}\n\n预计花费: {cost}\n\n"
          f"这个探针会真打 provider。确认要花这笔钱, 请加 --yes-spend 重跑:\n"
          f"    .venv/bin/python {sys.argv[0]} --yes-spend")
    raise SystemExit(0)
