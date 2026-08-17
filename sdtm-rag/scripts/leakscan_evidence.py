#!/usr/bin/env python3
"""题面泄漏扫描 —— 检查拟进 git 的证据文件是否含 gold 题面片段。

红线背景: `data/study/` 下的 gold 集是 gitignored 的真实试验内容, 证据文件进 git
时只许带统计值 / 题号 / 命令 / rc, 不许带题面。本脚本把那条红线做成可复跑的闸。

用法:
    ./.venv/bin/python scripts/leakscan_evidence.py <file> [--min-len N] [--show N]
                                                   [--allow-missing]

判定规则 (与 --min-len 一起决定结果, 引用数字时必须连阈值一起写):
    needle 来源 : GOLD_SETS 各 yml 里每条 `question:` 字段的值
    归一化      : 只去首尾空白与包裹的成对引号; **不做**大小写折叠 / 全半角转换
    滑窗        : 对每条 question 以 stride=STRIDE 取长度 min_len 的连续子串
    命中        : 任一滑窗原文出现在目标文件即算该 question 命中 (每条最多计 1 次)

退出码:
    0  CLEAN 且 needle 集完整  ← 只有这个才算过闸
    1  发现泄漏
    2  needle 集不完整, 拒绝给结论 (未加 --allow-missing)
    3  needle 集不完整 + --allow-missing 放行, 且无命中 —— **CLEAN 不可信**

为什么缺 gold 必须硬失败 (fail-closed):
    GOLD_SETS 里 4 个在 `data/study/` 下, 是 **gitignored** 的。新克隆 / CI /
    别人的机器上这 4 个不存在, needle 会从 306 掉到 156, **日文 study 题面
    needle 全部消失** —— 此时一个确实含 study 题面的文件会被扫成 "CLEAN rc=0"。
    红线闸 fail-open 比没有闸更危险 (它给假保证), 所以缺任一 set 一律
    非零退出; 要放行必须显式 --allow-missing, 且那种情况下 rc 仍非 0。

阈值选取 (重要, 别照抄小阈值):
    gold 里 CDISC 侧 (`eval/test_set_v3.yml`) 是英文题面, 与证据文件里的命令行、
    指标名共享大量通用英文子串 ("source ", "study ", "the SDTM" 等)。因此
    min_len 取小会产生**通用词假阳性**, 那些命中不是题面泄漏。
    经验: 8 有可观假阳性, 12 起基本只剩真片段。默认 12, 并建议同时看
    `--min-len 8` 的命中明细人工判读, 不要只看一个数字就下结论。
    日文题面 (study 侧) 无此问题 —— 中文正文不含假名, 见配套的 kana 扫描。
"""

import argparse
import re
import sys
from pathlib import Path

GOLD_SETS = (
    "eval/test_set_v3.yml",
    "eval/routing_gold_ja_supplement.yml",
    "data/study/st01/eval/test_set_study_v1_1.yml",
    "data/study/st01/eval/test_set_study_v2.yml",
    "data/study/st01/eval/test_set_docs_v1.yml",
    "data/study/st01/eval/routing_gold_docs.yml",
)

STRIDE = 4
QUESTION_RE = re.compile(r"^\s*question:\s*(.+)$", re.M)


def collect_needles(sets=GOLD_SETS):
    """→ (needles, missing, per_set): needles=[(来源文件, question 原文)]。

    缺失只如实返回, **不在这里决定放行与否** —— 那是 main 的闸。
    """
    needles, missing, per_set = [], [], {}
    for name in sets:
        path = Path(name)
        if not path.exists():
            missing.append(name)
            continue
        text = path.read_text(encoding="utf-8")
        count = 0
        for match in QUESTION_RE.finditer(text):
            question = match.group(1).strip()
            # YAML 块标量 (`question: |`) 下行级正则只会取到指示符本身, 真题面在后续行。
            # 静默按 '|' 当题面扫 = 该 set 事实上零覆盖, 必须炸而不是悄悄放过。
            if question in ("|", ">", "|-", ">-", "|+", ">+"):
                raise SystemExit(
                    f"{name}: 检测到 YAML 块标量 question ({question!r}), "
                    "行级正则提取不安全 (会把指示符当题面, 该 set 实际零覆盖)。"
                    "请改用 yaml.safe_load 重写 collect_needles 后再跑。")
            if len(question) >= 2 and question[0] == question[-1] and question[0] in "\"'":
                question = question[1:-1]
            if question:
                needles.append((name, question))
                count += 1
        per_set[name] = count
    return needles, missing, per_set


def scan(target_text, needles, min_len):
    """→ [(来源文件, 命中的滑窗原文)]; 每条 question 最多一条。"""
    hits = []
    for source, question in needles:
        if len(question) < min_len:
            continue
        for i in range(0, len(question) - min_len + 1, STRIDE):
            fragment = question[i:i + min_len]
            if fragment in target_text:
                hits.append((source, fragment))
                break
    return hits


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("target", help="待扫描的证据文件")
    parser.add_argument("--min-len", type=int, default=12, help="滑窗长度 (默认 12)")
    parser.add_argument("--show", type=int, default=20, help="最多打印几条命中明细")
    parser.add_argument("--allow-missing", action="store_true",
                        help="显式放行缺 gold set 的扫描; 放行后 CLEAN 不可信, rc 仍非 0")
    args = parser.parse_args(argv)

    target_text = Path(args.target).read_text(encoding="utf-8")
    needles, missing, per_set = collect_needles()

    print(f"target      : {args.target}")
    print(f"needles     : {len(needles)} 条 question "
          f"({len(GOLD_SETS) - len(missing)}/{len(GOLD_SETS)} 个 gold set 可读)")
    for name in GOLD_SETS:
        status = f"{per_set[name]} 条" if name in per_set else "**缺失**"
        print(f"                {name}: {status}")
    print(f"rule        : stride={STRIDE}, min_len={args.min_len}, 原文匹配 (不折叠大小写)")

    # 闸 (fail-closed): needle 集不完整时, "没扫到" 不构成任何保证。
    if missing and not args.allow_missing:
        print()
        print("=" * 68)
        print(f"ABORT: {len(missing)}/{len(GOLD_SETS)} 个 gold set 缺失, 拒绝给结论。")
        for name in missing:
            print(f"    缺失: {name}")
        print()
        print("这些多半是 gitignored 的 data/study/ 侧 set。少了它们, 日文 study")
        print("题面根本不在 needle 里, 扫描'干净'只是因为压根没找 —— 那是假保证。")
        print("确实要在 needle 不全的情况下跑, 请显式加 --allow-missing (rc 仍非 0)。")
        print("=" * 68)
        return 2

    hits = scan(target_text, needles, args.min_len)
    if hits:
        print(f"LEAK: {len(hits)} 条 question 有片段出现在目标文件 (min_len={args.min_len})")
        for source, fragment in hits[:args.show]:
            print(f"    {source}: {fragment!r}")
        if len(hits) > args.show:
            print(f"    ... 另 {len(hits) - args.show} 条")
        return 1

    if missing:
        print()
        print("!" * 68)
        print(f"!! 无命中, 但 needle 集不完整 ({len(missing)}/{len(GOLD_SETS)} 个 set 缺失)")
        print("!! —— 本次 CLEAN **不可信**, 不得作为红线过闸证据引用。")
        for name in missing:
            print(f"!!     缺失: {name}")
        print("!" * 68)
        return 3

    print(f"CLEAN: 0 条 question 片段出现在目标文件 (min_len={args.min_len})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
