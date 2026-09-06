"""机械抽取人判对照索引 (零 LLM): 答案里出现了哪些权威表 dataset 键 + 权威表 Class。

用法 (从 sdtm-rag/): .venv/bin/python eval/prod_wirein/make_human_packet_index.py <tag>
读 human_packet_<tag>.md 的条目顺序 (blind_order 已打乱, 本脚本不改序) + run_<tag>.json 答案。
对 opus-5 复算与 2026-09-04 手工生成版零 diff。
"""
import json, re, sys
from pathlib import Path
sys.path.insert(0, "eval/prod_wirein"); sys.path.insert(0, ".")
from class_authority import load_class_authority
tag = sys.argv[1]
packet = Path(f"evidence/checkpoints/human_packet_{tag}.md").read_text()
order = re.findall(r"^### \d+\. `([^`]+)`", packet, re.M)
rep = json.load(open(f"evidence/checkpoints/verified_runs/run_{tag}.json"))
ans = {r["id"]: r for r in rep["results"]}
auth = load_class_authority()
out = [f"# 人判对照索引 — {tag} (b) 层 8 条", "",
"> ⛔ 纯机械抽取, **不含任何判定倾向**: 只做「答案里出现了哪些权威表里的 dataset 键」",
"> + 「权威表对它的 Class 是什么」。Class 一列直接抄自权威表, 不是对答案的评价。", "",
"> ⚠ 2 字母键在英文里噪声高 (如 `IS`/`RE`/`PP` 也是普通词/缩写), 下表按**出现次数**",
"> 排序并原样给出, 请以答案原文为准, 不要把本表当成断言清单。", ""]
for i, qid in enumerate(order, 1):
    r = ans[qid]; a = r["answer"] or ""
    rows = []
    for k, cls in auth.items():
        n = len(re.findall(rf"\b{re.escape(k)}\b", a))
        if n: rows.append((n, k, cls))
    rows.sort(key=lambda x: (-x[0], x[1]))
    out += [f"## {i}. `{qid}`", "", f"**题**: {r['question']}", "", f"**答案长度**: {len(a)} 字符", ""]
    if rows:
        out += ["| 权威表键 | 答案中出现次数 | 权威表 Class |", "|---|---|---|"]
        out += [f"| {k} | {n} | {cls} |" for n, k, cls in rows]
    else:
        out.append("(答案中未出现任何权威表键)")
    out += ["", "---", ""]
Path(f"evidence/checkpoints/human_packet_{tag}_index.md").write_text("\n".join(out))
print(tag, "order:", order)
