# study golden 题集 v2 扩容 — 实施计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 把 study golden 从 25 计分题扩到 ~48 计分题, 并从判据上堵掉"gold 非唯一定位"这一类结构性满分, 让这把尺子重新具备对 study 侧改动的判别力。

**Architecture:** 三段式, 三方隔离 (规则 D): ①出题 (按 form 卡数加权配额 + 难度形态清单) → ②独立审题 (不同 subagent_type, 逐题核验 gold 唯一性与可答性) → ③验收 (第三方跑基线, 出 v2 下的真实 recall)。新增确定性 gold lint 工具, 把"唯一定位"变成可执行闸而非人工约定。

**Tech Stack:** Python / pytest / 现有 `eval/run_eval.py` harness / catalog.json 确定性产物。

## Global Constraints

- **红线**: 真实 study 的 form/field OID、label、题面、别名词**只允许**出现在 `sdtm-rag/data/study/` (gitignored)。committed 代码/测试/文档零真名; 任何报告只给聚合数字与题 id。
- **不改历史可比性**: 不得修改 `check_source_recall` 的匹配语义 (子串匹配)。历史 run (v0/v1/v1.1/Phase 2 三组) 必须保持可复算。判别力靠**出题侧的 lint 闸**保证, 不靠改 harness 语义。
- **出题人 ≠ 审题人 ≠ 验收人** (规则 D)。出题依据必须是 protocol/catalog 等**独立于被测库**的来源, 不得看着 field card 起草 (v0 的教训: 出题泄漏导致 100% 假象)。
- **规则 A**: 新题集定稿前必须做 N 样本独立抽检 (N 写进 PLAN, 见 Task 4), 结果留 `evidence/`。
- **规则 B**: 任何被否决的候选题归档不删。
- 全量测试基线 **799 passed** 只增不减。
- 现有 v1.1 题集**不得就地修改** —— v2 是新文件, v1.1 保留为历史基线可复算。

## 勘察依据 (2026-08-06 实测, 决定本计划的三个设计)

> **表述约定 (红线)**: 下文一律用 **F1..F21** 指代 form (按卡数降序编号), 不写真实 form OID —— form OID 属 study 私有结构, 只允许存在于 gitignored 区。编号↔真实 OID 的对照表写在本地 `data/study/st01/eval/V2_DRAFT_NOTES.md`。

| 发现 | 数据 | 对 v2 的约束 |
|---|---|---|
| **题密度与 form 规模严重脱节** | 前五大 form (F1-F5) 合计 518 卡 (54%) 仅 7 题; F1 175 卡仅 2 题 (87 卡/题) | 配额必须按卡数加权 (Task 2) |
| **gold 非唯一定位** ~~面比终审发现的更广~~ **实为 1 条** | ~~42 条 gold 中 9 条多卡匹配~~ → **已更正 (2026-08-06)**: 其中 8 条是 lint 假阳性 (工具剥 `.md` 后匹配, 严于真实判据); 真实只有 **1 条** (17 卡家族前缀)。详见下方「判据语义订正」 | 仍需 lint 闸 (Task 1), 但**工具必须与 `check_source_recall` 逐字同语义** |
| **form 覆盖尚可但有死角** | 18/21 覆盖; 3 个未覆盖 form 合计 55 卡; 另有 1 个 17 卡 form 实质 0 题 (其唯一题的 gold 是家族前缀, 即判别力≈0 的那题) | 死角各补题 + 该题重写 (Task 2) |

注: q14 经实测确认是**真命中** (S2 注入 4 张卡全为同族, 无干扰卡, `source_hits` 记录 gold 本尊)。~~但其 gold 写法不具防伪能力~~ → **已更正**: 其 gold 带 `.md`, 真实判据下唯一定位, **本来就有判别力**。先前"无防伪能力"的判断源自 lint 假阳性。

### 判据语义订正 (2026-08-06, 本计划执行中发现)

`check_source_recall` 末行是 `any(exp in src for src in retrieved_sources)` —— **gold 原样 (含 `.md`) 对含 `.md` 的完整 source 串做子串匹配**。因此 `.md` **参与匹配且有判别力**: `…__ITEM_R.md` 不是 `…__ITEM_RX.md` 的子串。

Task 1 按本计划初稿实现的 lint 却先剥掉 `.md` 再匹配无后缀卡名 → **严于真实判据 → 假阳性**。实测: v1.1 的 9 条 finding 中 **8 条为假阳性** (gold 带 `.md`, 真实匹配数 = 1), 真问题仅剩那条 17 卡家族前缀。

**连锁后果 (记录以儆效尤)**: Task 2 出题人为迁就这些假阳性, 删过 2 条本来合法的 gold、多加了 5 条不必要的 `gold_max_matches` 声明; 我本人也基于错误结论对 q14 等做出过错误判断。

**修正**: lint 改为与 `check_source_recall` **逐字同语义** (gold 原样匹配带 `.md` 的完整卡名), 并新增一条测试直接钉住两者等价 —— 将来改任一侧都会红。**教训: 判据检查工具必须与被检查的判据同语义, 否则会制造连锁误判。**

---

### Task 1: gold 唯一性 lint 工具

**Files:**
- Create: `sdtm-rag/eval/lint_gold.py`
- Test: `sdtm-rag/scripts/tests/test_lint_gold.py`

**Interfaces:**
- Produces: `lint_gold(test_set_path, catalog_path) -> list[Finding]`; `Finding(qid, gold, n_matches, matched_sample)`; CLI `python -m eval.lint_gold <test_set> [--catalog PATH] [--max-matches N]`, 退出码非 0 表示有 gold 非唯一定位。Task 2/3 用它做闸。

- [ ] **Step 1: 写失败测试** (合成 catalog + 合成题集, 零真名)

```python
"""gold 唯一性 lint — 合成数据, 零真实 OID/label."""
import json
import pytest
from eval.lint_gold import lint_gold

CARDS = ["stx__FRM_A__ITEM_R", "stx__FRM_A__ITEM_RX", "stx__FRM_A__XITEM_R",
         "stx__FRM_B__SOLO", "stx__FRM_C__FAM_1", "stx__FRM_C__FAM_2"]
# 注: 兄弟卡形态必须用 ITEM_RX (gold 的**超串**), 不能只用 XITEM_R ——
# 匹配是在完整卡名上做的 (与 check_source_recall 对完整路径做子串一致),
# 而 `stx__FRM_A__ITEM_R` 并不是 `stx__FRM_A__XITEM_R` 的子串 (中间隔着 X)。
# 依据: 真实 v1.1 的 9 条 finding 全部是"gold 为更长兄弟卡的前缀"形态, 无一例中缀。


def _catalog(tmp_path):
    items = []
    for c in CARDS:
        _, form, oid = c.split("__")
        items.append({"form_oid": form, "item_oid": oid, "label": "偽ラベル"})
    p = tmp_path / "catalog.json"
    p.write_text(json.dumps({"study": "stx", "items": items}), encoding="utf-8")
    return p


def _testset(tmp_path, golds):
    import yaml
    qs = [{"id": f"q{i:02d}", "question": "偽質問", "expected_sources": g}
          for i, g in enumerate(golds)]
    p = tmp_path / "ts.yml"
    p.write_text(yaml.safe_dump({"questions": qs}, allow_unicode=True), encoding="utf-8")
    return p


def test_unique_gold_passes(tmp_path):
    ts = _testset(tmp_path, [["stx__FRM_B__SOLO"]])
    assert lint_gold(ts, _catalog(tmp_path)) == []


def test_substring_of_sibling_is_flagged(tmp_path):
    # 完整卡名 ITEM_R 是 ITEM_RX 的前缀 → 子串匹配下命中兄弟卡也算对
    ts = _testset(tmp_path, [["stx__FRM_A__ITEM_R"]])
    f = lint_gold(ts, _catalog(tmp_path))
    assert len(f) == 1 and f[0].n_matches == 2


def test_oid_level_substring_alone_is_not_flagged(tmp_path):
    # 语义边界: OID 层互含但完整卡名不互含 → 不该报。
    # 防止后人"修"成 OID 级匹配 —— 那会误报好 gold, 且与 check_source_recall 脱节。
    ts = _testset(tmp_path, [["stx__FRM_A__XITEM_R"]])
    assert lint_gold(ts, _catalog(tmp_path)) == []


def test_family_prefix_gold_is_flagged(tmp_path):
    ts = _testset(tmp_path, [["stx__FRM_C__FAM_"]])
    f = lint_gold(ts, _catalog(tmp_path))
    assert len(f) == 1 and f[0].n_matches == 2


def test_md_suffix_stripped_before_match(tmp_path):
    ts = _testset(tmp_path, [["stx__FRM_B__SOLO.md"]])
    assert lint_gold(ts, _catalog(tmp_path)) == []


def test_gold_matching_nothing_is_flagged(tmp_path):
    # 打错的 gold 恒 miss, 比多匹配更隐蔽 (永远 0 分, 看起来像检索差)
    ts = _testset(tmp_path, [["stx__FRM_Z__NOPE"]])
    f = lint_gold(ts, _catalog(tmp_path))
    assert len(f) == 1 and f[0].n_matches == 0


def test_max_matches_option_allows_declared_families(tmp_path):
    # 家族题合法: 显式声明允许 N 卡
    ts = _testset(tmp_path, [["stx__FRM_C__FAM_"]])
    assert lint_gold(ts, _catalog(tmp_path), max_matches=2) == []
```

- [ ] **Step 2: 跑测试确认失败**

Run: `cd sdtm-rag && .venv/bin/python -m pytest scripts/tests/test_lint_gold.py -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'eval.lint_gold'`

- [ ] **Step 3: 实现**

```python
"""gold 唯一性 lint — 把"期望来源必须唯一定位"变成可执行闸。

动机 (2026-08-06 勘察): v1.1 的 42 条 gold 里 9 条是多卡匹配。`check_source_recall`
是**子串**匹配, 所以 gold 写成家族前缀 (`..__FAM_`) 或写成兄弟卡的子串
(`ITEM_R` ⊂ `XITEM_R`) 时, 召回**任意**一张匹配卡都判满分 —— 答错也得分。
最极端的一例是一条 gold 匹配 17 张卡, 该题判别力≈0。

本工具不改 `check_source_recall` 的语义 (改了历史 run 就不可复算), 而是在出题侧
把这类 gold 拦下来。0 匹配同样报 —— 打错的 gold 恒 miss, 比多匹配更隐蔽。
"""
from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path

import yaml


@dataclass
class Finding:
    qid: str
    gold: str
    n_matches: int
    matched_sample: list[str]


def _card_names(catalog: dict) -> list[str]:
    study = catalog["study"]
    return [f"{study}__{it['form_oid']}__{it['item_oid']}" for it in catalog["items"]]


def lint_gold(test_set_path, catalog_path, max_matches: int = 1) -> list[Finding]:
    """返回所有"匹配卡数 != 期望"的 gold。max_matches=1 要求唯一定位;
    家族题可显式放宽 (与出题人声明的家族规模一致)。"""
    catalog = json.loads(Path(catalog_path).read_text(encoding="utf-8"))
    names = _card_names(catalog)
    data = yaml.safe_load(Path(test_set_path).read_text(encoding="utf-8"))
    qs = data["questions"] if isinstance(data, dict) else data

    findings: list[Finding] = []
    for q in qs:
        if q.get("out_of_scope"):
            continue
        allowed = q.get("gold_max_matches", max_matches)
        for gold in (q.get("expected_sources") or []):
            key = gold[:-3] if gold.endswith(".md") else gold
            hits = [n for n in names if key in n]
            if len(hits) != allowed:
                findings.append(Finding(q["id"], gold, len(hits), sorted(hits)[:3]))
    return findings


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="lint study golden gold 唯一性")
    ap.add_argument("test_set")
    ap.add_argument("--catalog", required=True)
    ap.add_argument("--max-matches", type=int, default=1)
    args = ap.parse_args(argv)
    findings = lint_gold(args.test_set, args.catalog, args.max_matches)
    for f in findings:
        verdict = "匹配 0 卡 (gold 打错?)" if f.n_matches == 0 else f"匹配 {f.n_matches} 卡"
        print(f"{f.qid}: {verdict} — 期望唯一定位")
    print(f"\n{len(findings)} 条 gold 未唯一定位")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 4: 跑测试确认通过**

Run: `cd sdtm-rag && .venv/bin/python -m pytest scripts/tests/test_lint_gold.py -v`
Expected: 6 passed

- [ ] **Step 5: 对 v1.1 实跑, 确认复现勘察数字**

Run: `cd sdtm-rag && .venv/bin/python -m eval.lint_gold data/study/st01/eval/test_set_study_v1_1.yml --catalog data/study/st01/catalog.json`
Expected: 报出 **9 条** (与勘察一致: 1 条 17 卡 + 3 条 3 卡 + 5 条 2 卡)。这既验证工具正确, 也是 v1.1 的存档诊断。

- [ ] **Step 6: Commit**

```bash
git add sdtm-rag/eval/lint_gold.py sdtm-rag/scripts/tests/test_lint_gold.py
git commit -m "feat(eval): gold 唯一性 lint — 把结构性满分变成可执行闸"
```

---

### Task 2: v2 出题 (出题人视角, 独立于被测库)

**Files:**
- Create (本地, 不入库): `sdtm-rag/data/study/st01/eval/test_set_study_v2.yml`
- Create (本地): `sdtm-rag/data/study/st01/eval/V2_DRAFT_NOTES.md` (逐题出题依据)

**配额 (按 form 卡数加权, 新增 ~23 题 → 合计 ~48 计分题)**

form 用 **F1..F21** 编号 (卡数降序), 真实 OID 对照见本地 `V2_DRAFT_NOTES.md`。

| form | 卡数 | v1.1 题 | v2 新增 | 理由 |
|---|---|---|---|---|
| F1 | 175 | 2 | **+4** | 最大 form, 现密度 87 卡/题 |
| F2 | 144 | 2 | **+3** | 第二大 |
| F3 | 75 | 1 | **+2** | 问卷族, 多卡家族题的天然场景 |
| F4 | 68 | 1 | **+2** | |
| F5 | 56 | 1 | **+2** | |
| F6 | 53 | 4 | +0 | 已充分 |
| F7 | 46 | 3 | +0 | 已充分 |
| F8 | 40 | 1 | **+1** | |
| F9 | 36 | 1 | **+1** | |
| F10 | 33 | 1 | **+1** | |
| F11 | 32 | 2 | +0 | |
| F12 | 21 | **0** | **+1** | 未覆盖死角 |
| F13 | 18 | 1 | +0 | |
| F14 | 17 | **0** | **+1** | 未覆盖死角 |
| F15 | 17 | **0** | **+1** | 未覆盖死角 |
| F16 | 17 | 0 (唯一题无效) | **+2** | 判别力≈0 那题重写 + 补 1 |
| 其余小 form | — | — | **+2** | 长尾抽样 |

**难度形态清单 (每类至少 2 题, 防止清一色单卡直查)**

| 形态 | 说明 |
|---|---|
| 单卡精确 | 唯一可答, gold 唯一定位 |
| 多卡家族 | 显式声明 `gold_max_matches: N`, N = 家族真实规模 |
| 近义双卡判别 | 两卡语义极近, gold 必须是**不被兄弟卡包含**的写法 |
| 跨 form 关联 | 答案需要两个 form 的卡 |
| 词面零重合 | 问句用自然语言, 卡面用缩写/术语 (通道③ 的场景) |
| 反幻觉 (out_of_scope) | 问库里不存在的东西, 期望模型说"没有"; 排除出 recall 平均 |

- [ ] **Step 1: 出题** — 依据 protocol 概念 + catalog 结构 (**不得看着 field card 起草**), 按配额与形态清单产出 ~23 题, 逐题在 `V2_DRAFT_NOTES.md` 记录: 出题依据 / gold 定位方式 / 形态归类 / 预期难点
- [ ] **Step 2: 自查 lint** — `python -m eval.lint_gold data/study/st01/eval/test_set_study_v2.yml --catalog data/study/st01/catalog.json`; 家族题在题目里写 `gold_max_matches: N` 显式声明, 其余必须唯一定位。**lint 退出码必须为 0 才能进 Task 3**
- [ ] **Step 3: 合并 v1.1** — v2 文件 = v1.1 全部题目 (含 2 道 out_of_scope) + 新增题; **q23 按上表重写**为唯一定位 (原题归档进 NOTES, 规则 B); 另外 8 条多卡 gold 逐条收紧或显式声明家族规模
- [ ] **Step 4: 复跑 lint 直到 0 findings**
- [ ] **Step 5: 不 commit** (题集在 gitignore 区; 本 task 无代码改动)

---

### Task 3.5: 审题后统一修订 (与 Task 3 意见合并做一轮, 避免审阅期间题集变动)

- [ ] **加固: 单卡 gold 一律补全 `.md` 后缀** (2026-08-06 实测): v2 的 76 条 gold 中 63 条不带后缀, **今天全部已唯一定位**, 故补后缀不改变当前判定 —— 但它是**面向未来的免费判别力**: 今天唯一 ≠ 明天唯一, catalog 将来新增一张兄弟卡 (如 `…_RX`) 会让不带后缀的 gold 静默变成多匹配, 而 lint 只在跑时才发现。
      **例外: 2 道家族题** (`gold_max_matches` = 20 / 30) 的 gold 是家族前缀, 补 `.md` 后匹配 0 卡, **必须保持不带后缀**。
- [ ] 合并 Task 3 审题意见一并修订, 修订后重跑 lint (须 EXIT 0) 与 `load_test_set` schema 校验
- [ ] 复跑独立复算脚本 (不依赖 lint): 逐条按 `gold 原样 in 带 .md 的完整卡名` 计数, 确认每条匹配数等于其声明值

### Task 3: 独立审题 (规则 D — 必须与 Task 2 不同 subagent_type)

- [ ] **Step 1: 逐题核验** — 审题人拿到 v2 题集 + catalog (**不给 Task 2 的 NOTES**, 避免被出题人的推理带走), 逐题判定: ①该题在库里是否真的可答 ②gold 是否为唯一正确落点 (而非"其中一个合理落点") ③期望事实串是否足够长且不是干扰项子串 ④问句是否泄漏了卡面字面 (出题泄漏)
- [ ] **Step 2: 出具 REVISE/APPROVE** — 每条问题给题 id + 类型 + 建议。历史经验 (v1.1 两轮审阅) 是**每轮都会抓到出题人自查漏掉的硬伤**, 一次 APPROVE 反而可疑
- [ ] **Step 3: 出题人修订 → 复审** 直到 APPROVE; 每轮否决的候选题归档进 NOTES (规则 B)

---

### Task 4: 规则 A 语义抽检 (N=10) + v2 基线验收

**规则 A 要求**: 改写率 >50% 必须做 N 样本独立抽检。v2 相对 v1.1 新增 ~23 题 (改写率 ~85%), **N=10**。

- [ ] **Step 1: 抽检** — 第三方 (与 Task 2/3 均不同) 随机抽 10 题, 独立到 catalog 里核对 gold 是否正确、题目是否可答, 结果留 `sdtm-rag/evidence/checkpoints/study_golden_v2_audit.md`
- [ ] **Step 2: 跑 v2 基线 (S2 开)**

```bash
cd sdtm-rag && .venv/bin/python -m eval.run_eval \
  data/study/st01/eval/test_set_study_v2.yml \
  --retrieval-only --hybrid --study-lookup \
  --collection study_st01 --kb-root data/study/st01/cards \
  --output data/study/st01/eval/runs/v2_baseline_s2on.json
```

- [ ] **Step 3: 跑 v2 对照 (S2 关)** — 同命令去掉 `--study-lookup`, 输出 `v2_baseline_s2off.json`。**这一组是本次扩容最重要的产出**: 它给出 S2 在一把有判别力的尺子上的真实增益 (v1.1 上是 88.53%→100%, 但那把尺子已饱和)
- [ ] **Step 4: 判读** — v2 下的 S2 增益若显著低于 v1.1 的 +11.47pt, 说明原增益部分来自题集偏科, **如实记录不粉饰**; 若 v2 满分再现, 说明题还不够难, 需再加难题
- [ ] **Step 5: 写 checkpoint** `sdtm-rag/evidence/checkpoints/study_golden_v2.md` — 只含统计与结构描述: 三版对照 (v0/v1.1/v2) / 配额与形态分布 / lint 闸结果 / 审题抓到的问题类型 / S2 开关两组数字 / 已知限制
- [ ] **Step 6: 收尾** — worklog + PROGRESS + memory 更新; 单 commit push (排除 `sdtm-rag/data/study`)

---

## Self-Review 记录

1. **依据充分性**: 三个设计 (加权配额 / lint 闸 / RETRT 补题) 全部来自 2026-08-06 实测, 数字在勘察表内可复算。
2. **不破坏历史**: 不改 `check_source_recall` 语义, v1.1 文件不动 → v0/v1/v1.1/Phase 2 全部历史 run 仍可复算比对。
3. **三方隔离**: Task 2 出题 / Task 3 审题 / Task 4 抽检分属三个不同 subagent_type (规则 D)。
4. **类型一致**: `lint_gold(test_set_path, catalog_path, max_matches=1) -> list[Finding]` 在 Task 1 定义, Task 2 Step 2 与 Task 3 调用一致; `gold_max_matches` 题目字段在 Task 1 实现与 Task 2 Step 2 用法一致。
5. **红线**: 本文件零真名 —— form 一律用 F1..F21 编号, 真实 OID 对照只存本地 gitignored 区。
   **教训 (值得记)**: 本 PLAN 初稿直接写了 17 个真实 form OID, 并在这一条里自我辩解"属 CDISC 域名与通用缩写"放行 —— 实际上其中多个是本研究私有的 form 标识, 与公开标准无关。是写完后的**程序化复扫**(与 catalog 比对) 抓出来的, 目测和自我论证都没拦住。**红线检查必须程序化, 且不能由作者的"我觉得这个不算"来豁免。**
