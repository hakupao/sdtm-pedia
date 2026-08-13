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

════════════════════════════════════════════════════════════════════════
⚠ 题面不许出现在 pytest 输出里 —— 有**三条**路, 全部要堵
════════════════════════════════════════════════════════════════════════
本仓惯例是把 pytest 实测输出贴进 evidence/ 的 markdown 并提交 (evidence/ 下上百个 tracked
文件), 所以一次贴了失败输出的收口证据 = 题面进 git。红线的成立条件是「所有路径」。

1. **assert 的比较值** —— pytest 会把两边整个打出来。
   ⇒ 题面只比 sha256 摘要; 其余字段 (id/gold/group/chapter) 才允许裸比。
2. **traceback 的栈帧实参** —— `--tb=long` / `--tb=auto`(**不写 --tb 时的默认**)会给每个
   栈帧打一行 `参数名 = repr(值)`。收 `list[dict]` 的 helper 只要出现在栈上, 题面就跟着走。
   ⇒ 本文件所有 helper **一律只收 `Path`**, 内部自己加载; 任何 helper 都不得以
     `list[dict]` / `dict` 作形参。测试体内也不留含题面的局部变量 (只留投影后的元组)。
   实测 (审阅方 M-E + 本 session 复现, 变异 = FINAL 去掉某题的 `id` 字段):
     修前 `--tb=short` 泄 1 条 / `--tb=long` 泄 3 条 / `--tb=auto` 泄 3 条; 修后三者均为 0。
3. **生产码的异常消息** —— `run_routing_eval.load_docs_routing_gold` 原本抛
   `f"...: {q!r}"`, 把整条 item (含题面) 写进消息。已改成只打序号 + 缺的键名 + id。
   本文件的 `_load` 同理: 校验放在**收 Path 的函数里**, 消息不带值。

残余边界 (诚实标注): `--showlocals` / `-l` 会打局部变量, 那时
`test_real_load_gold_enforces_authored_group_sizes` 里 `load_gold()` 的返回值仍会露 ——
那是生产函数自身的局部, 测试侧堵不住。默认三种 tb 模式已实测为 0。
"""
import hashlib
import subprocess
from pathlib import Path

import pytest
import yaml

DRAFT = Path("data/study/st01/eval/routing_gold_docs_draft.yml")
FINAL = Path("data/study/st01/eval/routing_gold_docs.yml")

# Task 4 出题结束 ⇒ draft 冻结 (用户裁定 2026-08-14)。摘要钉在**这里**而不是数据文件里:
# 测试文件进 git 进 code review, 两个 yml 两者都不进。
# 它堵的是 test_final_gold_preserves_draft_questions 单独堵不住的那条路 —— 那条比的是
# FINAL 对 DRAFT, 同方向改动两个文件即可全绿通过。要改这个常量就得过 review, 正是要的效果。
# 只钉 draft 不钉 final: final 的数据段已被 ..._deterministic_split_of_the_draft 逐条钉住,
# 而它的文件头注释是给人读的, 不该因为改一句说明就变红。
DRAFT_SHA256 = "b1373fd81214b11816b817b5c24539fac3e9753c6f1ada7b34f4921b88d94099"

_REQUIRED = ("id", "question", "gold", "chapter")


def _load(path: Path) -> list[dict]:
    """读 + 校验。**只收 Path** (见文件头 ⚠ 第 2 条)。

    校验必须在这里做, 不能留给下游: 缺字段的条目一旦流到 `sorted(key=lambda x: ...)`,
    KeyError 就发生在一个**以该条目为实参**的 lambda 帧里 —— traceback 照样打出题面。
    """
    items = yaml.safe_load(path.read_text(encoding="utf-8"))
    for i, x in enumerate(items):
        missing = [k for k in _REQUIRED if k not in x]
        if missing:  # 只报序号 / 缺的键名 / id —— 报值就是把题面写进异常消息
            raise ValueError(f"{path} 第 {i} 条缺字段 {missing} (id={x.get('id')!r})")
    return items


def _question_digests(path: Path) -> dict[str, str]:
    """题面 → 摘要。失败时 pytest 打的是 id + 十六进制, 不是手順書原文 (见文件头 ⚠ 第 1 条)。"""
    return {x["id"]: hashlib.sha256(x["question"].encode("utf-8")).hexdigest()[:16]
            for x in _load(path)}


def _routing_fields(path: Path) -> list[tuple]:
    """划分相关的全部字段, 不含题面 —— 这几个裸比才安全。"""
    return [(x["id"], x["gold"], x["group"], int(x["chapter"])) for x in _load(path)]


def _deterministic_split(draft_path: Path) -> list[dict]:
    """spec §5.3 第 4 条的划分规则, 逐字复刻.

    Task 5 的划分脚本是一次性的 (产物 yml 又 gitignored), 所以规则本身若不在这里留一份,
    git 里就没有任何一处写着「划分应该长什么样」—— 事后谁把 group 改一个字都无从对照。
    这份复刻是规则在 git 中的**唯一**存根, 它进 code review, 而 yml 不进。
    """
    items = [dict(x) for x in _load(draft_path)]
    docs = sorted([x for x in items if x["gold"] == "study"],
                  key=lambda x: (int(x["chapter"]), x["id"]))
    for i, x in enumerate(docs):
        x["group"] = "dev" if i % 2 == 0 else "heldout"
    for x in items:
        if x["gold"] == "cdisc":
            x["group"] = "distractor_cdisc"
        elif x["gold"] == "both":
            x["group"] = "ambiguous_both"
    return items


def _expected_routing_fields(draft_path: Path) -> list[tuple]:
    """规则作用在 draft 上应当产出的字段投影。中间的 list[dict] 不跨函数边界。"""
    return [(x["id"], x["gold"], x["group"], int(x["chapter"]))
            for x in _deterministic_split(draft_path)]


def _authored_group_sizes() -> tuple[int, dict[str, int]]:
    """真实 load_gold() 的题量。只把**计数**交回测试体, 含题面的 gold 列表留在本帧内。"""
    from eval.run_routing_eval import load_gold

    gold = load_gold()  # 组量不符时它自己 raise
    authored = ("dev", "heldout", "distractor_cdisc", "ambiguous_both")
    return len(gold), {n: sum(1 for g in gold if g["group"] == n) for n in authored}


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


def test_draft_is_frozen_at_the_authored_bytes():
    """出题已结束, draft 冻结在 Task 4 交付时的字节上 —— 改一个字节这条就红.

    比字节而非 yaml 语义: 连「语义等价的重排」也算改动。出题隔离一旦结束,
    题集就不该再有任何理由变动; 真有正当需求, 改常量走 review。
    失败信息只有两个十六进制串, 不含题面 (见文件头 ⚠)。
    """
    actual = hashlib.sha256(DRAFT.read_bytes()).hexdigest()
    assert actual == DRAFT_SHA256, (
        f"draft 已变动 (实际 {actual} / 冻结值 {DRAFT_SHA256}) —— "
        "出题已结束, 题面变动必须走 code review")


def test_dev_and_heldout_cover_disjoint_ids():
    """继承自 brief。**近似装饰品**(审阅方 Minor-2), 留着但不计进闸的条数:

    每个条目只有一个 group, 故 dev & hold 只可能在「同 id 出现两次且组不同」时非空,
    而那种情形已被 ..._deterministic_split_of_the_draft 的列表比对与 load_gold 的
    dupes 闸各抓一遍。保留是因为它零成本且读起来是这组断言的自然一环。
    """
    fields = _routing_fields(FINAL)
    dev = {i for i, _g, grp, _c in fields if grp == "dev"}
    hold = {i for i, _g, grp, _c in fields if grp == "heldout"}
    assert dev and hold and not (dev & hold)


def test_final_gold_preserves_draft_questions():
    """划分只许加 group, 不许改题面 —— 改题面等于绕过 Task 4 的出题隔离.

    比摘要而非原文: 见文件头 ⚠ 第 1 条。改一个字摘要就变, 检出能力不打折, 只是失败时不打原文。
    """
    assert _question_digests(FINAL) == _question_digests(DRAFT)


def test_final_gold_is_exactly_the_deterministic_split_of_the_draft():
    """反 cherry-pick: 最终 gold 必须**恰好**等于规则作用在 draft 上的结果.

    对调一对 dev/heldout 后组量仍是 12/12, EXPECTED_GROUP_SIZES 与任何计数型断言都看不见;
    只有重跑规则逐条比对能看见。held-out 的效力全压在这条上。
    列表相等而非集合相等: 连条目顺序被动过也算改动。
    题面不进这条断言 (见文件头 ⚠), 它由 test_final_gold_preserves_draft_questions 按摘要盯。
    """
    assert _routing_fields(FINAL) == _expected_routing_fields(DRAFT)


def test_split_rule_sorts_by_chapter_not_by_id(tmp_path):
    """规则存根的**区分性**不许依赖数据巧合 (审阅方 Minor-3, 存活变异 T1).

    真实 draft 里出题方的编号恰好与章号同序, 于是 `key=(chapter, id)` 与 `key=id` 在那份
    数据上恒等 —— 把排序键改成只按 id, 上面那条 10 passed 全绿。后果不是「现在错了」,
    而是 git 里唯一那份规则存根, 其正确性没有任何断言在看。
    这里用**合成数据**把编号与章号故意反序, 把 `(chapter, id)` 这个键本身钉住。
    合成题面是无意义占位串, 不涉红线。
    """
    p = tmp_path / "synthetic_draft.yml"
    # 章号与 id 故意反序: 按 (chapter, id) 排 = s_04,s_03,s_02,s_01 ⇒ dev={s_04,s_02}
    #                     若退化成只按 id 排 = s_01,s_02,s_03,s_04 ⇒ dev={s_01,s_03}
    # 两个结果**完全不相交**, 故键一退化这条必红。
    p.write_text(yaml.safe_dump(
        [{"id": f"s_0{n}", "question": f"placeholder {n}", "gold": "study", "chapter": c}
         for n, c in ((1, 4), (2, 3), (3, 2), (4, 1))], allow_unicode=True), encoding="utf-8")
    fields = _expected_routing_fields(p)
    assert {i for i, _g, grp, _c in fields if grp == "dev"} == {"s_04", "s_02"}
    assert {i for i, _g, grp, _c in fields if grp == "heldout"} == {"s_03", "s_01"}


def test_double_chapters_are_split_one_each():
    """spec §5.3 对该规则的承诺是「恰好 12/12 且跨章对称」—— 对称性在这里独立核一遍.

    不经由 _deterministic_split: 那份复刻万一抄错, 上一条会跟着错得一致而全绿。
    这条只读 FINAL 的数据本身, 断言同章两题必分处两组。
    """
    by_chapter: dict[int, list[str]] = {}
    for _id, _gold, group, chapter in _routing_fields(FINAL):
        if group in ("dev", "heldout"):
            by_chapter.setdefault(chapter, []).append(group)
    doubles = {c: sorted(g) for c, g in by_chapter.items() if len(g) == 2}
    assert doubles, "没有任何章出现两题 —— 对称性无从谈起, 划分规则的前提变了"
    assert all(g == ["dev", "heldout"] for g in doubles.values()), doubles


def test_real_load_gold_enforces_authored_group_sizes():
    """拿**真实**的 253 题跑一遍 load_gold() —— 纯函数, 不发任何 LLM 请求.

    load_gold() 内建的题量闸此前只在 monkeypatch 过 EXPECTED_GROUP_SIZES 的 fixture 上跑过,
    真实的 routing_gold_docs.yml 没有任何测试碰过 ⇒ 「四组题量对不对」在 CI 里是空白,
    只有人工跑 eval (要发 LLM 请求) 才会发现。这条把那次相遇搬进单测。
    """
    from eval.run_routing_eval import EXPECTED_GROUP_SIZES

    total, sizes = _authored_group_sizes()
    assert total == sum(EXPECTED_GROUP_SIZES.values()) == 253
    assert sizes == {"dev": 12, "heldout": 12, "distractor_cdisc": 12, "ambiguous_both": 6}
