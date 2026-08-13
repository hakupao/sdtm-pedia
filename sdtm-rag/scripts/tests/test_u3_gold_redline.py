"""U3: gold 文件的红线 + 划分完整性闸.

前两组不是「代码正确性」测试, 是**数据红线**测试 —— 手順書题面一旦进 git 就撤不回来了。

后面几条钉的是**划分本身**。与 run_routing_eval.EXPECTED_GROUP_SIZES 的分工:
  - EXPECTED_GROUP_SIZES 只管**数**, 而且只在 load_gold() 真跑到真实文件上时才生效。
    test_run_routing_eval.test_real_gold_files_match_expected_sizes 明写了它只核 legacy
    与 u1_doc 两组, 「余下四组在 Task 5 之后由 load_gold() 的题量闸覆盖」——
    但那一路上的 load_gold() 调用全部 monkeypatch 掉了 EXPECTED_GROUP_SIZES 与四个路径,
    真实的 routing_gold_docs.yml 至今没被任何测试加载过。
    ⇒ test_real_load_gold_enforces_authored_group_sizes 补的就是这个: 让常量与真数据见面。
  - 数对了不等于划分没被挑过: dev/heldout 之间对调任意一对, 12/12 纹丝不动。
    held-out 的全部效力都压在「划分不是挑出来的」上, 所以还需要
    test_final_gold_is_exactly_the_deterministic_split_of_the_draft ——
    它拿 draft 重新跑一遍规则, 逐条比对。这条断言在本仓是**唯一**能抓住 cherry-pick 的。

⚠ 本文件的断言一律**不得直接比较题面字符串**。pytest 失败时会把两边的值整个打进 stdout,
   而 CI 日志不是 gitignored —— 一条 `assert final_questions == draft_questions` 在红的那天
   就把手順書题面泄进日志里 (实测: 初版这么写, 制造一次 cherry-pick 变异即打出整条日文题面)。
   故题面只比 sha256 摘要, 其余字段 (id/gold/group/chapter) 才允许裸比。
"""
import hashlib
import subprocess
from pathlib import Path

import pytest
import yaml

DRAFT = Path("data/study/st01/eval/routing_gold_docs_draft.yml")
FINAL = Path("data/study/st01/eval/routing_gold_docs.yml")


def _load(path: Path) -> list[dict]:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def _question_digests(items: list[dict]) -> dict[str, str]:
    """题面 → 摘要。失败时 pytest 打的是 id + 十六进制, 不是手順書原文 (见文件头 ⚠)。"""
    return {x["id"]: hashlib.sha256(x["question"].encode("utf-8")).hexdigest()[:16]
            for x in items}


def _routing_fields(items: list[dict]) -> list[tuple]:
    """划分相关的全部字段, 不含题面 —— 这几个裸比才安全。"""
    return [(x["id"], x["gold"], x["group"], int(x["chapter"])) for x in items]


def _deterministic_split(draft_items: list[dict]) -> list[dict]:
    """spec §5.3 第 4 条的划分规则, 逐字复刻.

    Task 5 的划分脚本是一次性的 (产物 yml 又 gitignored), 所以规则本身若不在这里留一份,
    git 里就没有任何一处写着「划分应该长什么样」—— 事后谁把 group 改一个字都无从对照。
    这份复刻是规则在 git 中的**唯一**存根, 它进 code review, 而 yml 不进。
    """
    items = [dict(x) for x in draft_items]
    docs = sorted([x for x in items if x["gold"] == "study"],
                  key=lambda x: (int(x["chapter"]), x["id"]))
    for i, x in enumerate(docs):
        x["group"] = "dev" if i % 2 == 0 else "heldout"
    for x in items:
        if x["gold"] == "cdisc":
            x["group"] = "distractor_cdisc"
        elif x["gold"] == "both":
            x["group"] = "ambiguous_both"
    return [{"id": x["id"], "question": x["question"], "gold": x["gold"],
             "group": x["group"], "chapter": x["chapter"]} for x in items]


@pytest.mark.parametrize("path", [DRAFT, FINAL])
def test_gold_file_is_gitignored(path):
    """红线: 两个题集文件都必须被 gitignore 覆盖."""
    assert path.exists(), f"{path} 不存在 —— Task 4/5 未完成"
    rc = subprocess.run(["git", "check-ignore", "-q", str(path)]).returncode
    assert rc == 0, f"{path} 未被 gitignore 覆盖 —— 手順書题面会进 git"


@pytest.mark.parametrize("path", [DRAFT, FINAL])
def test_gold_file_is_not_tracked(path):
    """红线补强: 就算 gitignore 写对了, 文件也可能已被 `git add -f` 跟踪过."""
    rc = subprocess.run(["git", "ls-files", "--error-unmatch", str(path)],
                        capture_output=True).returncode
    assert rc != 0, f"{path} 已被 git 跟踪 —— 必须 git rm --cached"


def test_dev_and_heldout_cover_disjoint_ids():
    items = _load(FINAL)
    dev = {x["id"] for x in items if x["group"] == "dev"}
    hold = {x["id"] for x in items if x["group"] == "heldout"}
    assert dev and hold and not (dev & hold)


def test_final_gold_preserves_draft_questions():
    """划分只许加 group, 不许改题面 —— 改题面等于绕过 Task 4 的出题隔离.

    比摘要而非原文: 见文件头 ⚠。改一个字摘要就变, 检出能力不打折, 只是失败时不打原文。
    """
    assert _question_digests(_load(FINAL)) == _question_digests(_load(DRAFT))


def test_final_gold_is_exactly_the_deterministic_split_of_the_draft():
    """反 cherry-pick: 最终 gold 必须**恰好**等于规则作用在 draft 上的结果.

    对调一对 dev/heldout 后组量仍是 12/12, EXPECTED_GROUP_SIZES 与任何计数型断言都看不见;
    只有重跑规则逐条比对能看见。held-out 的效力全压在这条上。
    列表相等而非集合相等: 连条目顺序被动过也算改动。
    题面不进这条断言 (见文件头 ⚠), 它由 test_final_gold_preserves_draft_questions 按摘要盯。
    """
    assert _routing_fields(_load(FINAL)) == _routing_fields(_deterministic_split(_load(DRAFT)))


def test_double_chapters_are_split_one_each():
    """spec §5.3 对该规则的承诺是「恰好 12/12 且跨章对称」—— 对称性在这里独立核一遍.

    不经由 _deterministic_split: 那份复刻万一抄错, 上一条会跟着错得一致而全绿。
    这条只读 FINAL 的数据本身, 断言同章两题必分处两组。
    """
    items = _load(FINAL)
    by_chapter: dict[int, list[str]] = {}
    for x in items:
        if x["group"] in ("dev", "heldout"):
            by_chapter.setdefault(int(x["chapter"]), []).append(x["group"])
    doubles = {c: sorted(g) for c, g in by_chapter.items() if len(g) == 2}
    assert doubles, "没有任何章出现两题 —— 对称性无从谈起, 划分规则的前提变了"
    assert all(g == ["dev", "heldout"] for g in doubles.values()), doubles


def test_real_load_gold_enforces_authored_group_sizes():
    """拿**真实**的 253 题跑一遍 load_gold() —— 纯函数, 不发任何 LLM 请求.

    load_gold() 内建的题量闸此前只在 monkeypatch 过 EXPECTED_GROUP_SIZES 的 fixture 上跑过,
    真实的 routing_gold_docs.yml 没有任何测试碰过 ⇒ 「四组题量对不对」在 CI 里是空白,
    只有人工跑 eval (要发 LLM 请求) 才会发现。这条把那次相遇搬进单测。
    """
    from eval.run_routing_eval import EXPECTED_GROUP_SIZES, load_gold

    gold = load_gold()  # 组量不符时它自己 raise
    assert len(gold) == sum(EXPECTED_GROUP_SIZES.values()) == 253
    authored = ("dev", "heldout", "distractor_cdisc", "ambiguous_both")
    sizes = {name: sum(1 for g in gold if g["group"] == name) for name in authored}
    assert sizes == {"dev": 12, "heldout": 12, "distractor_cdisc": 12, "ambiguous_both": 6}
