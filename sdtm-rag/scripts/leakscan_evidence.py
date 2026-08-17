#!/usr/bin/env python3
"""题面泄漏扫描 —— 检查拟进 git 的证据文件是否含 gold 题面片段。

红线背景: `data/study/` 下的 gold 集是 gitignored 的真实试验内容, 证据文件进 git
时只许带统计值 / 题号 / 命令 / rc, 不许带题面。本脚本把那条红线做成可复跑的闸。

用法:
    ./.venv/bin/python scripts/leakscan_evidence.py <file> [--min-len N] [--show N]

判定规则 (与 --min-len 一起决定结果, 引用数字时必须连阈值一起写):
    needle 来源 : GOLD_SETS 各 yml 里每条 `question:` 字段的值
    归一化      : 只去首尾空白与包裹的成对引号; **不做**大小写折叠 / 全半角转换
    滑窗        : 对每条 question 以 stride=STRIDE 取长度 min_len 的连续子串
    命中        : 任一滑窗原文出现在目标文件即算该 question 命中 (每条最多计 1 次)
    退出码      : 有命中 → 1; 无命中 → 0

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
    """→ [(来源文件, question 原文)]; 缺失的 set 只报告不报错 (gitignored 可能不在)。"""
    needles, missing = [], []
    for name in sets:
        path = Path(name)
        if not path.exists():
            missing.append(name)
            continue
        text = path.read_text(encoding="utf-8")
        for match in QUESTION_RE.finditer(text):
            question = match.group(1).strip()
            if len(question) >= 2 and question[0] == question[-1] and question[0] in "\"'":
                question = question[1:-1]
            if question:
                needles.append((name, question))
    return needles, missing


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
    args = parser.parse_args(argv)

    target_text = Path(args.target).read_text(encoding="utf-8")
    needles, missing = collect_needles()
    for name in missing:
        print(f"  (缺失, 跳过) {name}")

    print(f"target      : {args.target}")
    print(f"needles     : {len(needles)} 条 question (来自 {len(GOLD_SETS) - len(missing)} 个 gold set)")
    print(f"rule        : stride={STRIDE}, min_len={args.min_len}, 原文匹配 (不折叠大小写)")

    hits = scan(target_text, needles, args.min_len)
    if hits:
        print(f"LEAK: {len(hits)} 条 question 有片段出现在目标文件 (min_len={args.min_len})")
        for source, fragment in hits[:args.show]:
            print(f"    {source}: {fragment!r}")
        if len(hits) > args.show:
            print(f"    ... 另 {len(hits) - args.show} 条")
        return 1

    print(f"CLEAN: 0 条 question 片段出现在目标文件 (min_len={args.min_len})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
