# doc 轨 U6 判库欠账重启修法 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 修掉判库欠账 (基线 fatal 10, docs 侧 auto source_recall −10pt), 走确定性检索信号层 (widen-only), 且先把 U3/U5 点名的判据仪器缺陷修掉并重冻基线。

**Architecture:** Phase 0 (Task 0-6) 修仪器 + gold 复核 + 新基线三遍冻结; 硬闸后 Phase 1 (Task 7-13) 实现 `decide_corpus` 同源信号层 + 可见集标定 + 全闸七条款 + 答题侧 spot-check + 规则 D 五方核验 + 收口。历史判定脚本 `u3_task8_verdict.py` / `u5_verdict.py` **冻结不改** (保 U3/U5 收口 §8 复跑可重放), 修订判据落新文件 `u6_gate_verdict.py` / `u6_answer_verdict.py`; `run_routing_eval.py` 是活仪器, 原地修。

**Tech Stack:** Python 3 (`sdtm-rag/.venv`), pytest, yaml, Bedrock (router=light 模型; 答题=sonnet)。

**Spec:** `docs/superpowers/specs/2026-08-17-doc-track-u6-routing-debt-restart-design.md` (含四项用户裁定)

## Global Constraints

- 一切命令在 `sdtm-rag/` 下跑, python 一律 `./.venv/bin/python`。
- **红线**: 零真名零正文进 git; 路由 gold 题面 gitignored; 异常消息只打序号/id 不打题面 (`{q!r}` 禁用, 有回归守卫 test); stdout 不打题目文本。
- **判据冻结**: Task 6 基线冻结后, 阈值 / gold / `score_run` fatal 定义 / `LEGACY_EXACT_FLOOR=178` / `EXPECTED_GROUP_SIZES` 一字不许改。
- **可见集纪律** (U3 防线 2): Phase 1 实现方只许看 group ∈ {legacy, dev} 的数字与 id; held-out/amb/dist/final 题面与逐题结果全程封存。**实现方不许打开任何 `data/study/st01/eval/runs/*.json` 原件** (detail 含题面), 只许用 Task 9 的可见集提取物。
- **subagent 一律 opus** (用户偏好); Writer/Reviewer 不同 subagent_type (规则 D)。
- 每个跑批声称"三遍"必须真跑 3 遍; 写「实测」必附可复跑命令。
- **退回预登记 (先于结果, 2026-08-17)**: Task 10 全闸任一条款触发 ⇒ Phase 1 代码 commit 全部 revert, Phase 0 仪器与基线存续, 失败归档 `evidence/failures/u6_task10_attempt_1.md` (规则 B), 上报用户; **不许改阈值不许删题, 没有第二轮标定后重闸** (要重启须新单元)。
- 标定迭代上限预登记: Task 9 词表/阈值迭代 ≤ 5 轮, 超出 = 停下上报 (不许无限调)。

---

### Task 0: 开工自检 + 基线三遍预跑归档

**Files:**
- 无代码改动; 产物 `data/study/st01/eval/runs/routing_run_{1,2,3}.json` (gitignored) + `evidence/` 记录

**Interfaces:**
- Produces: 修仪器前的 rc=1/fatal=10 观测记录 (给 Task 6 对照; 不是冻结基线)

- [ ] **Step 1: 三条环境自检** (已于 2026-08-17 实测过一遍, 开工日重跑确认)

```bash
./.venv/bin/python -m pytest -p no:warnings --tb=no | tail -2        # → 1353 passed
./.venv/bin/python -c "import chromadb; cl=chromadb.PersistentClient(path='data/chroma'); print({c.name: c.count() for c in cl.list_collections()})"   # → 4329/959/114
./.venv/bin/python -m eval.run_eval data/study/st01/eval/test_set_study_v2.yml --retrieval-only --hybrid --study-lookup --collection study_st01 --kb-root data/study/st01/cards --output /tmp/chk.json | tail -3   # → 87.5%
```

- [ ] **Step 2: 路由基线预跑三遍** (设计日未跑的那条, LLM 走 Bedrock light)

```bash
./.venv/bin/python -m eval.run_routing_eval --runs 3   # 预期 rc=1, 每遍 fatal_excl_final=10, legacy≈179/181
echo "rc=$?"
```

- [ ] **Step 3: 归档观测值** — 把三遍的 stdout (只有统计零题面) 存 `evidence/u6_task0_selfcheck.txt`, 三条自检值 + fatal_ids 列表抄录。若 fatal ≠ 10 或 legacy < 178, **停下上报** (环境与 U3 收口不符), 不开工。

- [ ] **Step 4: Commit** (`git add sdtm-rag/evidence/u6_task0_selfcheck.txt && git commit -m "evidence(u6): task0 开工自检 + 路由基线预跑三遍观测"`)

---

### Task 1: `run_routing_eval.py` 活仪器修缮 (A-3 run 元数据 + I-1 runs 守卫 + I-4 by_group.passed + `--out-prefix`)

**Files:**
- Modify: `eval/run_routing_eval.py`
- Test: `scripts/tests/test_run_routing_eval.py` (追加, 不改既有 case)

**Interfaces:**
- Produces: run json 顶层新增 `"meta"` 键 `{generated_at, git_rev, runs_arg, run_index, n_gold, out_prefix}`; `gate_verdict()` 的 `by_group` 子项**不再含** `passed` 键; `main(argv)` 支持 `--out-prefix` (默认 `routing_run`) 与 `--allow-nonstandard-runs`; `--runs != 3` 且无该 flag ⇒ `SystemExit`。Task 2/6/9/11 全依赖这些。

- [ ] **Step 1: 写失败测试** (追加到 `scripts/tests/test_run_routing_eval.py`; fixture 风格照抄该文件里既有的 fake-router/monkeypatch 写法)

```python
def test_runs_guard_rejects_non_three(monkeypatch):
    import eval.run_routing_eval as rre
    with pytest.raises(SystemExit, match="三遍纪律"):
        rre.main(["--runs", "1"])          # gold 加载之前就该拒绝

def test_meta_written_and_prefix(tmp_path, monkeypatch, fake_gold_and_router):
    # fake_gold_and_router: 按本文件既有 test 的做法 monkeypatch load_gold / create_router / route_corpus
    import eval.run_routing_eval as rre
    monkeypatch.setattr(rre, "RUNS_DIR", tmp_path)
    rre.main(["--runs", "3", "--out-prefix", "u6_x"])
    for i in (1, 2, 3):
        d = json.loads((tmp_path / f"u6_x_{i}.json").read_text())
        m = d["meta"]
        assert set(m) >= {"generated_at", "git_rev", "runs_arg", "run_index", "n_gold", "out_prefix"}
        assert m["run_index"] == i and m["runs_arg"] == 3

def test_by_group_has_no_passed_key(fake_gold_preds):
    import eval.run_routing_eval as rre
    v = rre.gate_verdict(fake_gold_preds.gold, fake_gold_preds.preds)
    assert all("passed" not in grp for grp in v["by_group"].values())  # I-4: 0.95 阈值误导字段
```

- [ ] **Step 2: 跑测试确认失败** — `./.venv/bin/python -m pytest scripts/tests/test_run_routing_eval.py -q` → 新 3 条 FAIL。

- [ ] **Step 3: 实现** (最小改动)

```python
# 文件头新增 import: datetime (timezone), subprocess

def _git_rev() -> str:
    try:
        return subprocess.run(["git", "rev-parse", "--short", "HEAD"],
                              capture_output=True, text=True, check=True).stdout.strip()
    except Exception:
        return "unknown"

# gate_verdict 内 by_group 行改为同时剥掉 fatal_items 与 passed (I-4):
        "by_group": {k: {kk: vv for kk, vv in v.items() if kk not in ("fatal_items", "passed")}
                     for k, v in by_group.items()},

# main() 开头, parser 定义后:
    parser.add_argument("--out-prefix", default="routing_run")
    parser.add_argument("--allow-nonstandard-runs", action="store_true",
                        help="调试用; 打开时不打稳定性行, rc 恒非 0")
    args = parser.parse_args(argv)
    if args.runs != 3 and not args.allow_nonstandard_runs:
        raise SystemExit("三遍纪律: --runs 必须为 3 (审查 I-1 修缮); 调试请加 --allow-nonstandard-runs")

# 写盘处 (原 routing_run_{run_i}.json):
        meta = {"generated_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
                "git_rev": _git_rev(), "runs_arg": args.runs, "run_index": run_i,
                "n_gold": len(gold), "out_prefix": args.out_prefix}
        (RUNS_DIR / f"{args.out_prefix}_{run_i}.json").write_text(
            json.dumps({"meta": meta, "summary": v, "detail": detail}, ensure_ascii=False, indent=1))

# 稳定性行 (I-1): 只在真三遍时打; 非标准 runs 时 rc 恒非 0:
    if args.runs >= 3 and not args.allow_nonstandard_runs:
        print(f"stability: {stable}/{len(gold)} 题三遍判定一致")
    else:
        print("⚠ 非三遍纪律运行, 稳定性/一致性结论无效, rc 强制非 0")
        return 1
```

- [ ] **Step 4: 跑测试确认通过 + 全量回归** — `./.venv/bin/python -m pytest scripts/tests/test_run_routing_eval.py -q` 全绿; `./.venv/bin/python -m pytest -p no:warnings --tb=no | tail -2` ≥ 1353 passed (既有 case 若有依赖 `routing_run` 文件名或 by_group.passed 的, 按新契约修 test 而非改回实现; 逐条在 commit message 点名)。

- [ ] **Step 5: Commit** — `git commit -m "fix(u6-t1): run_routing_eval 仪器修缮 — run 元数据(A-3)/三遍守卫(I-1)/by_group.passed 移除(I-4)/--out-prefix"`

---

### Task 2: `eval/u6_gate_verdict.py` — 修订判据判定脚本 (七条款, I-2 输入校验, rc 语义)

**Files:**
- Create: `eval/u6_gate_verdict.py`
- Test: `scripts/tests/test_u6_gate_verdict.py`
- 不动: `eval/u3_task8_verdict.py` (历史冻结件)

**Interfaces:**
- Consumes: Task 1 的 run json 结构 (`meta`/`summary`/`detail`; `summary.by_group[g]` 含 `exact`/`fatal`/`n`)
- Produces: CLI `./.venv/bin/python -m eval.u6_gate_verdict --baseline B1 B2 B3 --after A1 A2 A3 [--output out.json]`; `verdict(base: list[dict], after: list[dict]) -> tuple[dict, int]`; rc=0 仅当条款 1/2/3/4/7 全 PASS。Task 6/11 依赖。

**冻结判据 (写死在源码常量, 与 spec §4.2 一致):**
- 条款 1: 三遍每遍 `fatal_excl_final==0` 且 `legacy_exact>=178`
- 条款 2: heldout% ≥ dev% − 25.0pt (三遍均值; 多数类基线并排, 不得单独引用)
- 条款 3: dev 三遍均值 ≥ 10/12
- 条款 4 (修订, 双列双闸): `distractor_cdisc` 组 — 三遍均值 fatal `after ≤ base` **AND** exact `base − after ≤ 1`
- 条款 7 (新增, 双列双闸): `u1_doc` 组 — 同条款 4 口径
- 条款 5: final 组只报告 (打印逐题 pred, 不进 rc)
- 条款 6: 三遍不稳定题点名 (打印, 不进 rc)

- [ ] **Step 1: 写失败测试** (合成 run fixture, 零题面; helper 构造最小 run dict)

```python
# scripts/tests/test_u6_gate_verdict.py
import copy, json, pytest
from eval.u6_gate_verdict import verdict, validate_inputs, main

def mk_run(idx, *, fatal=0, legacy=179, dist_exact=12, dist_fatal=0,
           u1_exact=27, u1_fatal=0, dev=12, heldout=12, gen="t0"):
    return {"meta": {"generated_at": f"{gen}-{idx}", "git_rev": "abc", "runs_arg": 3,
                     "run_index": idx, "n_gold": 254, "out_prefix": "x"},
            "summary": {"fatal_excl_final": fatal, "fatal_ids_excl_final": [],
                        "legacy_exact": legacy, "legacy_floor": 178,
                        "by_group": {"legacy": {"n": 181, "exact": legacy, "fatal": fatal},
                                     "dev": {"n": 12, "exact": dev, "fatal": 0},
                                     "heldout": {"n": 12, "exact": heldout, "fatal": 0},
                                     "distractor_cdisc": {"n": 12, "exact": dist_exact, "fatal": dist_fatal},
                                     "u1_doc": {"n": 27, "exact": u1_exact, "fatal": u1_fatal},
                                     "final": {"n": 4, "exact": 0, "fatal": 4}}},
            "detail": [{"id": "final_x", "group": "final", "gold": "study", "pred": "cdisc"}]}

BASE = [mk_run(i, fatal=10, dist_fatal=2, u1_fatal=1, dev=6, gen="base") for i in (1, 2, 3)]

def test_all_pass_rc0():
    after = [mk_run(i, gen="after") for i in (1, 2, 3)]
    out, rc = verdict(BASE, after)
    assert rc == 0 and out["clause1"]["pass"] and out["clause4"]["pass"] and out["clause7"]["pass"]

def test_clause4_fatal_column_trips():       # 非致命→致命 (exact 持平也要拦; U3 尺子盲区)
    after = [mk_run(i, dist_fatal=3, gen="after") for i in (1, 2, 3)]
    out, rc = verdict(BASE, after)
    assert rc == 1 and not out["clause4"]["pass"] and out["clause4"]["fatal"] == {"base": 2.0, "after": 3.0}

def test_clause4_exact_column_trips():
    after = [mk_run(i, dist_exact=10, dist_fatal=0, gen="after") for i in (1, 2, 3)]
    out, rc = verdict(BASE, after)
    assert rc == 1 and not out["clause4"]["pass"]

def test_clause7_u1doc_drift_trips():        # I-3 真空修复: u1_doc exact 掉 2 就拦
    after = [mk_run(i, u1_exact=25, gen="after") for i in (1, 2, 3)]
    out, rc = verdict(BASE, after)
    assert rc == 1 and not out["clause7"]["pass"]

def test_input_validation_same_content_rejected():   # I-2: baseline=after 拷贝错
    after = copy.deepcopy(BASE)
    with pytest.raises(SystemExit, match="baseline 与 after 内容相同"):
        validate_inputs(BASE, after)

def test_input_validation_needs_three_each():
    with pytest.raises(SystemExit, match="各需 3 份"):
        validate_inputs(BASE[:2], BASE)

def test_input_validation_needs_meta():
    b = copy.deepcopy(BASE); del b[0]["meta"]
    with pytest.raises(SystemExit, match="缺 meta"):
        validate_inputs(b, [mk_run(i, gen="a") for i in (1, 2, 3)])
```

- [ ] **Step 2: 跑测试确认失败** — `pytest scripts/tests/test_u6_gate_verdict.py -q` → import error (模块不存在)。

- [ ] **Step 3: 实现 `eval/u6_gate_verdict.py`**

```python
"""U6 修订判据判定 (spec 2026-08-17 §4.2, 冻结): 条款 1/2/3 沿 U3, 条款 4/7 双列双闸.
历史件 eval/u3_task8_verdict.py 不动 (U3 收口 §8 复跑用). rc=0 仅当 1/2/3/4/7 全 PASS.
诚实声明: 本单元机制 widen-only, 条款 4/7 的 fatal 半由构造保证, 判别力在 exact 半 (spec §4.2).
"""
from __future__ import annotations
import argparse, json

LEGACY_FLOOR = 178          # spec §7 不许下调
C2_GAP_PT = 25.0
C3_DEV_MIN = 10.0
DUAL_GATE_GROUPS = {"clause4": "distractor_cdisc", "clause7": "u1_doc"}

def _g(run, name, key):
    return run["summary"]["by_group"][name][key]

def validate_inputs(base: list[dict], after: list[dict]) -> None:
    if len(base) != 3 or len(after) != 3:
        raise SystemExit(f"baseline/after 各需 3 份, 得 {len(base)}/{len(after)} — 三遍纪律")
    for i, r in enumerate([*base, *after]):
        if "meta" not in r or not r["meta"].get("generated_at"):
            raise SystemExit(f"第 {i} 份 run 缺 meta.generated_at — 先用 Task 1 修缮后的 run_routing_eval 重产")
    bdump = {json.dumps(r["summary"], sort_keys=True) for r in base}
    adump = {json.dumps(r["summary"], sort_keys=True) for r in after}
    if bdump & adump and {r["meta"]["generated_at"] for r in base} & {r["meta"]["generated_at"] for r in after}:
        raise SystemExit("baseline 与 after 内容相同 (含同 meta) — 疑似拷贝错文件 (审查 I-2)")

def _dual_gate(base, after, group):
    fb = sum(_g(r, group, "fatal") for r in base) / 3
    fa = sum(_g(r, group, "fatal") for r in after) / 3
    eb = sum(_g(r, group, "exact") for r in base) / 3
    ea = sum(_g(r, group, "exact") for r in after) / 3
    return {"group": group, "fatal": {"base": round(fb, 2), "after": round(fa, 2)},
            "exact": {"base": round(eb, 2), "after": round(ea, 2)},
            "pass": fa <= fb + 1e-9 and eb - ea <= 1 + 1e-9,
            "note": "widen-only 机制下 fatal 半由构造保证, 判别力在 exact 半 (spec §4.2)"}

def verdict(base: list[dict], after: list[dict]) -> tuple[dict, int]:
    validate_inputs(base, after)
    c1 = all(r["summary"]["fatal_excl_final"] == 0 and r["summary"]["legacy_exact"] >= LEGACY_FLOOR
             for r in after)
    dev = sum(_g(r, "dev", "exact") for r in after) / 3 / 12 * 100
    hold = sum(_g(r, "heldout", "exact") for r in after) / 3 / 12 * 100
    c2, c3 = hold >= dev - C2_GAP_PT, sum(_g(r, "dev", "exact") for r in after) / 3 >= C3_DEV_MIN
    out = {"clause1": {"pass": c1, "per_run": [
               {"fatal": r["summary"]["fatal_excl_final"], "legacy": r["summary"]["legacy_exact"],
                "fatal_ids": r["summary"]["fatal_ids_excl_final"]} for r in after]},
           "clause2": {"pass": c2, "dev_pct": round(dev, 2), "heldout_pct": round(hold, 2),
                       "majority_note": "dev/heldout 多数类基线 100%, 不得单独引用 (U3 §7.1)"},
           "clause3": {"pass": c3, "dev_mean": round(sum(_g(r, "dev", "exact") for r in after) / 3, 2)}}
    for name, grp in DUAL_GATE_GROUPS.items():
        out[name] = _dual_gate(base, after, grp)
    out["clause5_final_report_only"] = [
        {d["id"]: d["pred"] for d in r["detail"] if d["group"] == "final"} for r in after]
    preds = [{d["id"]: d["pred"] for d in r["detail"]} for r in after]
    out["clause6_unstable"] = sorted(
        k for k in preds[0] if len({p.get(k) for p in preds}) > 1)
    rc = 0 if all(out[c]["pass"] for c in ("clause1", "clause2", "clause3", "clause4", "clause7")) else 1
    return out, rc

def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--baseline", nargs=3, required=True)
    p.add_argument("--after", nargs=3, required=True)
    p.add_argument("--output")
    a = p.parse_args(argv)
    load = lambda f: json.load(open(f, encoding="utf-8"))
    out, rc = verdict([load(f) for f in a.baseline], [load(f) for f in a.after])
    if a.output:
        json.dump(out, open(a.output, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    for k in ("clause1", "clause2", "clause3", "clause4", "clause7"):
        print(k, "PASS" if out[k]["pass"] else "⛔ 触发", json.dumps(
            {kk: vv for kk, vv in out[k].items() if kk not in ("pass", "per_run")}, ensure_ascii=False))
    print("clause5 (只报告):", out["clause5_final_report_only"])
    print("clause6 unstable:", out["clause6_unstable"])
    print(f"rc={rc}")
    return rc

if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 4: 跑测试确认通过 + 全量回归** — 新测试全绿, 全量 ≥ 1353 passed。

- [ ] **Step 5: Commit** — `git commit -m "feat(u6-t2): u6_gate_verdict 修订判据 — 条款4/7 双列双闸 + I-2 输入校验 + rc 语义; u3 历史件冻结不动"`

---

### Task 3: gold 变更 — `st01_v2_q07` 入 final 组 (出题侧, 基线冻结前)

**Files:**
- Modify: `eval/run_routing_eval.py` (FINAL_IDS / 新 loader / EXPECTED_GROUP_SIZES)
- Test: `scripts/tests/test_run_routing_eval.py` (追加)

**Interfaces:**
- Produces: `FINAL_IDS = ("docs_v1_q15", "docs_v1_q17", "docs_v1_q53", "st01_v2_q07")`; `load_v2_final()`; `EXPECTED_GROUP_SIZES` final 3→4, 合计 254; fatal 口径不变 (全集减 final = 250)。Task 6 基线在此之后冻结。

- [ ] **Step 1: 写失败测试**

```python
def test_final_group_has_four_including_v2_q07(monkeypatch_gold_files):
    import eval.run_routing_eval as rre
    gold = rre.load_gold()
    final = sorted(g["id"] for g in gold if g["group"] == "final")
    assert final == ["docs_v1_q15", "docs_v1_q17", "docs_v1_q53", "st01_v2_q07"]
    assert len(gold) == 254

def test_v2_final_loader_missing_id_raises(tmp_path):
    import eval.run_routing_eval as rre
    p = tmp_path / "v2.yml"; p.write_text("- id: other\n  question: x\n", encoding="utf-8")
    with pytest.raises(ValueError, match="st01_v2_q07"):
        rre.load_v2_final(p)
```

- [ ] **Step 2: 跑测试确认失败**。

- [ ] **Step 3: 实现** — 常量与 loader:

```python
STUDY_SET_V2 = Path("data/study/st01/eval/test_set_study_v2.yml")
FINAL_IDS = ("docs_v1_q15", "docs_v1_q17", "docs_v1_q53", "st01_v2_q07")   # U5 观测: q07 auto 打空
V2_FINAL_IDS = ("st01_v2_q07",)
EXPECTED_GROUP_SIZES = {"legacy": 181, "u1_doc": 27, "final": 4, "dev": 12,
                        "heldout": 12, "distractor_cdisc": 12, "ambiguous_both": 6}

def load_v2_final(path: Path) -> list[dict]:
    """v2 题集中被条款 5 收编的题 (id 硬编码源码, 同 FINAL_IDS 的 review 可见性理由)。"""
    items = {q["id"]: q for q in load_test_set(str(path))}
    missing = sorted(set(V2_FINAL_IDS) - set(items))
    if missing:
        raise ValueError(f"{path}: v2 final 题缺失 {missing} — 条款 5 报告对象不完整, 拒绝继续")
    return [{"id": i, "question": items[i]["question"], "gold": "study", "group": "final"}
            for i in V2_FINAL_IDS]

# load_gold() 里 load_docs_routing_gold 之后追加:
    items += load_v2_final(STUDY_SET_V2)
```

注意 `load_u1_doc_gold` 的 FINAL_IDS 完整性检查只看 docs 题集, 改为 `missing = sorted({i for i in FINAL_IDS if i.startswith("docs_")} - ids)`; `load_gold` 末尾的 `final_ids != set(FINAL_IDS)` 恒等检查不动 (自动覆盖 4 题)。v2 题 id 若与 v1.1 的 `st_` 前缀 id 重复, 既有 dupe 检查会拦 — 若拦, 停下上报而不是改 id。

- [ ] **Step 4: 跑测试确认通过 + 全量回归** (既有 EXPECTED sizes 相关 test 按新常量更新, commit message 点名)。

- [ ] **Step 5: Commit** — `git commit -m "feat(u6-t3): st01_v2_q07 入路由 gold final 组 (只报告不作判据, 条款 5 纪律; 254 题)"`

---

### Task 4: `u3_amb_01/04/06` gold 复核 (隔离 subagent + 用户裁定门)

**Files:**
- 复核报告: `evidence/u6_amb_gold_review.md` (进 git, 零题面 — 只写 id/结论/理由类型)
- 可能改: `data/study/st01/eval/routing_gold_docs.yml` (gitignored) 的这 3 题 gold 值

**Interfaces:**
- Produces: 三题 gold 的终值 (维持 both 或改 study), Task 6 冻结前生效。**controller 与 Phase 1 实现方都不读题面** — 只有本 task 的隔离 subagent 读。

- [ ] **Step 1: 派隔离出题侧 subagent** (opus, 独立 session), prompt 要点: 读 `routing_gold_docs.yml` 中 id 为 `u3_amb_01/04/06` 的三题; 审查方 U3 点名「两种独立决策形式都判不需要 cdisc 侧」; 逐题独立判定 gold 应为 both 还是 study, 判据 = 「不查 cdisc 语料该题能否完整作答」; **边做边落盘** `evidence/u6_amb_gold_review.md`, 报告零题面 (结论 + 理由类型 + 判定依据描述, 不引原文); 不许看任何路由 run 结果 (防按结果定 gold)。
- [ ] **Step 2: 读报告, 向用户呈报三题结论与建议** (AskUserQuestion: 每题 维持 both / 改 study), 用户裁定后才动 yml。
- [ ] **Step 3: 按裁定改 yml** (若有); `load_gold()` 冒烟 (`./.venv/bin/python -c "from eval.run_routing_eval import load_gold; print(len(load_gold()))"` → 254)。
- [ ] **Step 4: Commit** — `git commit -m "evidence(u6-t4): amb gold 复核报告 (裁定结果见报告; yml gitignored 不进 git)"`

---

### Task 5: `eval/u6_answer_verdict.py` — 答题侧修订判定 (E1 支配 + E4 并集闸 + I-1 抑制 + divergent_readings)

**Files:**
- Create: `eval/u6_answer_verdict.py` (复用 `eval.u5_verdict` 的 `scores_by_id` / `stability` import; `u5_verdict.py` 本体不动)
- Test: `scripts/tests/test_u6_answer_verdict.py`

**Interfaces:**
- Consumes: run_eval 答题 run json (同 u5_verdict 输入形状: `results[].judge_fact_recall/judge_parse_ok`, `summary.n_questions/judge_model`)
- Produces: `compare_arms(arm_a: list, arm_b: list, n_scored: int, family: str) -> dict` (A=off 臂, B=on 臂) 与 CLI `--arm-a A1 A2 A3 --arm-b B1 B2 B3 --family {cards,docs} --output`; 输出含 `E1{confirmed_cost/gain(stable ∪ dominance)}`, `E4{union, gate_pass}`, `aggregate_mean_diff_pt`, `paired_net_pt`, `divergent_readings`。Task 12 用。

**冻结判据 (spec §4.3, 用户裁定 2026-08-17):**
- E1 纳入 = 两侧稳定且分差 ≠ 0, **∪** 支配题: 六个值全 parse_ok 且 `max(B 三遍) < min(A 三遍)` (计代价) 或 `max(A) < min(B)` (计收益), 支配题额 = 三遍均值差
- E4 并集闸: `|unstable(A) ∪ unstable(B)|` ≤ {cards: 9, docs: 6} (=20%), 超 ⇒ rc=2 不下结论
- I-1 抑制: I1 (judge 重判, 若提供 probe) 不过 ⇒ 结论词字段 = `"advisory_no_verdict"`, 只出数字
- divergent_readings: `aggregate_mean_diff_pt` (逐题三遍均值的全池均值差 ×100, 只含双臂全 parse_ok 题) 与 `paired_net_pt` (=gain−cost) 符号相反且均非 0 ⇒ `true`

- [ ] **Step 1: 写失败测试** (合成 run helper `mk_answer_run(scores: dict[str, float|None])` 造 `results`/`summary`; 家族 n 用小合成集时以 `--expected-n` 覆盖)

```python
from eval.u6_answer_verdict import compare_arms

def runs(*score_maps):   # 每 map = 一遍; None = parse fail
    return [mk_answer_run(m) for m in score_maps]

def test_dominance_unstable_but_robust_counts_as_cost():
    a = runs({"q1": 1.0, "q2": 1.0}, {"q1": 1.0, "q2": 1.0}, {"q1": 0.9, "q2": 1.0})   # q1 A 侧档内不稳
    b = runs({"q1": 0.5, "q2": 1.0}, {"q1": 0.6, "q2": 1.0}, {"q1": 0.4, "q2": 1.0})   # max(B)=0.6 < min(A)=0.9
    out = compare_arms(a, b, n_scored=2, family="cards", expected_n=2)
    assert "q1" in out["E1"]["confirmed_cost_ids"] and "q1" in out["E1"]["dominance_ids"]

def test_e4_union_gate_trips():
    a = runs({f"q{i}": 1.0 for i in range(48)}, ...)  # 构造 10 题不稳定 (>9) → rc=2
    out, rc = ...  # compare_arms 返回 gate_pass=False; CLI rc=2
    assert not out["E4"]["gate_pass"]

def test_divergent_readings_flag():
    # 构造: 配对净额为正 (1 题 +0.5) 但全池均值差为负 (另 3 题各 -0.3 但不稳定/被支配排除)
    ...
    assert out["divergent_readings"] is True

def test_i1_fail_suppresses_verdict_word():
    out = compare_arms(a, b, n_scored=2, family="cards", expected_n=2,
                       probe={"same_rate": 0.5, "n": 9, "n_orig_parse_fail": 0})
    assert out["verdict_word"] == "advisory_no_verdict"
    assert "cheap" not in json.dumps(out)
```

(`test_e4_union_gate_trips` / `test_divergent_readings_flag` 两条的 `...` 处由实现方按同 helper 写完整数据 — 数据行数多不在 plan 里全铺, 断言与构造规则如上写死, 不许改断言。)

- [ ] **Step 2: 跑测试确认失败**。
- [ ] **Step 3: 实现** — 结构: `_raw_maps(runs) -> list[dict]`; `_dominance(maps_a, maps_b) -> (cost: dict, gain: dict)` 按上述冻结口径; `compare_arms` 组装 E1 (stable-diff ∪ dominance, id 排序, 双清单都报) / E4 (并集 + `{"cards": 9, "docs": 6}[family]` 闸) / aggregate vs paired 与 `divergent_readings` / `verdict_word` (E4 过闸且 cost 空 = `"cheap_on_this_ruler_comparable_pool"` — 词面即带池限定, U5 §9-1; cost 非空 = `"cost_reported"`; probe 提供且 same_rate < 0.95 = `"advisory_no_verdict"`)。CLI 同 u5_verdict 风格, rc: 0 正常 / 2 = E4 闸触发。
- [ ] **Step 4: 跑测试确认通过 + 全量回归**。
- [ ] **Step 5: Commit** — `git commit -m "feat(u6-t5): u6_answer_verdict — E1 支配纳入 + E4 并集闸 + I-1 结论词抑制 + divergent_readings; u5 历史件冻结不动"`

---

### Task 6: 新基线三遍冻结 (Phase 0 收口硬闸)

**Files:**
- 产物: `data/study/st01/eval/runs/u6_baseline_run_{1,2,3}.json` (gitignored) + `evidence/u6_task6_baseline_freeze.md` (进 git, 零题面)

**Interfaces:**
- Produces: 冻结基线三份 (含 meta); Phase 1 一切对比的参照物。**此后阈值/gold/判据一字不许改。**

- [ ] **Step 1: 跑基线** — `./.venv/bin/python -m eval.run_routing_eval --runs 3 --out-prefix u6_baseline_run` (预期 rc=1; fatal 数视 Task 4 裁定结果, 如实记录)。
- [ ] **Step 2: 判定脚本自检** — `./.venv/bin/python -m eval.u6_gate_verdict --baseline u6_baseline_run_{1,2,3} --after u6_baseline_run_{1,2,3}` 应 `SystemExit` (I-2 拒同内容) — 这条负例证明校验活着; 再以 Task 0 的 `routing_run_*` 作 after 跑一次, 输出条款表 (条款 4/7 双列可见)。命令与输出摘要进 evidence。
- [ ] **Step 3: 落盘 evidence** — 基线 fatal 数 / legacy exact / 各组 exact/fatal 三遍表 + 复跑命令 + 「冻结自此生效」声明。
- [ ] **Step 4: Commit** — `git commit -m "evidence(u6-t6): 新基线三遍冻结 (判据修订+gold 变更后; Phase 0 收口)"`

---

### Task 7: `decide_corpus` 同源重构 (行为不变的准备手术)

**Files:**
- Modify: `server/federation.py`, `eval/run_routing_eval.py`
- Test: `scripts/tests/test_federation.py`, `scripts/tests/test_run_routing_eval.py` (追加)

**Interfaces:**
- Produces: `decide_corpus(llm_router, question, signals=None) -> tuple[str, bool, str | None]` (corpus, fallback, widened_by); `FederatedEngine.__init__(..., signals=None)`; 观测属性 `self.last_signal_widened: str | None`; `run_routing_eval.main` 增 `--signal-layer {off,on}` (默认 off, Task 9 后 on 才有意义), on 时经生产工厂构造 signals。生产 `retrieve(auto)` 与 eval 走同一 `decide_corpus` (同源闸, 同 `make_docs_engine` 先例)。

- [ ] **Step 1: 写失败测试**

```python
def test_decide_corpus_no_signals_identical_to_route_corpus(monkeypatch):
    # monkeypatch route_corpus → ("cdisc", False); decide_corpus(llm, q) == ("cdisc", False, None)

def test_engine_auto_uses_decide_corpus_and_records_widened(monkeypatch):
    # signals stub: widen_reason 返回 "study_sig" → retrieve(auto) 走 both 分支,
    # engine.last_signal_widened == "study_sig"; corpus 强制档 (cdisc/study/both) 不经信号层, 属性恒 None

def test_routing_eval_signal_flag_off_bypasses_signals(...):
    # --signal-layer off 时 preds 与 route_corpus 裸跑一致
```

- [ ] **Step 2: 跑测试确认失败**。
- [ ] **Step 3: 实现** — `federation.py`:

```python
def decide_corpus(llm_router, question: str, signals=None) -> tuple[str, bool, str | None]:
    """判库 + 确定性信号纠偏 (U6). widen-only: 只做 单库→both, 永不收窄/换库."""
    corpus, fallback = route_corpus(llm_router, question)
    widened_by = None
    if signals is not None and corpus in ("cdisc", "study"):
        widened_by = signals.widen_reason(corpus, question)
        if widened_by is not None:
            corpus = "both"
    return corpus, fallback, widened_by
```

`FederatedEngine.__init__` 增 `signals=None` 存 `self.signals`; `retrieve` 的 auto 分支改为 `routed, fallback, widened = decide_corpus(self.llm_router, question, self.signals)`, 记 `self.last_signal_widened = widened`, log 加 `widened=widened` 字段; 强制档把属性置 None。`run_routing_eval.main` 增 flag, on 时构造生产同款 signals (工厂见 Task 8), 循环里改用 `decide_corpus(llm, g["question"], signals)`, run json `meta` 增 `"signal_layer": args.signal_layer`。
- [ ] **Step 4: 跑测试确认通过 + 全量回归** (行为不变: signals=None 路径逐字节同旧)。
- [ ] **Step 5: Commit** — `git commit -m "refactor(u6-t7): decide_corpus 同源抽取 (生产与 eval 共用), signals 挂点 + 观测字段; 默认行为不变"`

---

### Task 8: `server/routing_signals.py` — 双向确定性信号 + 生产接线

**Files:**
- Create: `server/routing_signals.py`
- Modify: `server/main.py` (照 `test_main_study_lookup_wiring.py` 对应的接线模式, FederatedEngine 构造处传 signals; grep `FederatedEngine(` 定位)
- Test: `scripts/tests/test_routing_signals.py`, `scripts/tests/test_main_signal_wiring.py` (照 `test_main_study_lookup_wiring.py` 的写法)

**Interfaces:**
- Consumes: `StudyLookup.resolve(query) -> StudyLookupResult(cards, form_scopes)` (已有确定性件)
- Produces: `RoutingSignals(study_lookup)` 带 `widen_reason(routed: str, question: str) -> str | None` (返回 `"study_sig"` / `"cdisc_sig"` / None); `build_signals(settings) -> RoutingSignals | None` 工厂 (eval 与 main 同用)。词表常量 `CDISC_STRUCT_TERMS` 在源码 (进 code review; 只含标准结构词汇, **零临床概念** — 红线同 U3 §6.1 词表纪律)。

- [ ] **Step 1: 写失败测试**

```python
def test_study_signal_fires_on_lookup_hit():
    sl = FakeLookup(cards=["x.md"])           # resolve 返回非空 cards
    s = RoutingSignals(sl)
    assert s.widen_reason("cdisc", "何かの質問") == "study_sig"
    assert s.widen_reason("study", "何かの質問") is None      # study 判定不需要 study 信号

def test_cdisc_signal_fires_on_struct_terms():
    s = RoutingSignals(FakeLookup())
    assert s.widen_reason("study", "この項目は SDTM のどの変数にマッピングされますか") == "cdisc_sig"
    assert s.widen_reason("study", "この項目の入力方法は?") is None   # 纯 study 问句不 fire

def test_widen_only_never_fires_on_both():
    assert RoutingSignals(FakeLookup(cards=["x"])).widen_reason("both", "q") is None

def test_deterministic():   # 同问句 100 次同结果
    ...

def test_terms_contain_no_clinical_concepts():
    # 红线闸: 词表不许含 CJK 临床词 — 对照一个硬编码禁形态断言 (疾病/検査/薬剤 等字根)
    from server.routing_signals import CDISC_STRUCT_TERMS
    banned_roots = ("病", "癌", "検査値", "薬", "投与量", "mg", "腫")
    assert not [t for t in CDISC_STRUCT_TERMS for b in banned_roots if b in t]
```

- [ ] **Step 2: 跑测试确认失败**。
- [ ] **Step 3: 实现**

```python
"""U6 确定性路由信号 (spec §5.1). widen-only; 词表只含标准结构词汇, 零临床概念 (红线).
词表/正则的最终形态由 Task 9 可见集标定冻结; 本文件初版是标定起点。"""
from __future__ import annotations
import re, unicodedata

# 标准结构词汇 (NFKC 归一后小写比对)。初版 — Task 9 标定后冻结, 冻结 commit 后不许再动。
CDISC_STRUCT_TERMS = (
    "sdtm", "cdisc", "マッピング", "どの変数", "対応する変数", "どのドメイン",
    "controlled terminology", "提出データ",
)
_CT_CODE_RE = re.compile(r"\bC\d{5,6}\b")            # NCI C-code
_DOMAIN_VAR_RE = re.compile(r"\b[A-Z]{2}[A-Z]{2,6}\b")   # SDTM 变量形态 (如 AESEV); 两字母裸域码刻意不收

def _norm(s: str) -> str:
    return unicodedata.normalize("NFKC", s).lower()

class RoutingSignals:
    def __init__(self, study_lookup):
        self.study_lookup = study_lookup

    def _study_signal(self, question: str) -> bool:
        r = self.study_lookup.resolve(question)
        return bool(r.cards or r.form_scopes)

    def _cdisc_signal(self, question: str) -> bool:
        qn = _norm(question)
        return (any(t in qn for t in CDISC_STRUCT_TERMS)
                or bool(_CT_CODE_RE.search(question))
                or bool(_DOMAIN_VAR_RE.search(question)))

    def widen_reason(self, routed: str, question: str) -> str | None:
        if routed == "cdisc" and self._study_signal(question):
            return "study_sig"
        if routed == "study" and self._cdisc_signal(question):
            return "cdisc_sig"
        return None

def build_signals(settings) -> RoutingSignals | None:
    """生产与 eval 同源工厂; StudyLookup 构造照 main.py 现有 study_lookup 接线复用."""
```

`main.py` 接线: 在现有 StudyLookup 构造处复用实例, `FederatedEngine(..., signals=RoutingSignals(lookup))`。wiring test 断言 main 构造出的 engine `.signals is not None` 且与 study_lookup 同一实例。
- [ ] **Step 4: 跑测试确认通过 + 全量回归 + 生产冒烟** — `curl localhost:8000/api/info` (launchd 服务) 正常; 若接线破坏启动, 修复后再冒烟。
- [ ] **Step 5: Commit** — `git commit -m "feat(u6-t8): RoutingSignals 双向确定性信号 (widen-only) + 生产接线; 词表初版待 t9 标定冻结"`

---

### Task 9: 可见集标定 (只看 legacy+dev; 词表/正则冻结)

**Files:**
- Create: `eval/u6_calibrate_signals.py` + `scripts/tests/test_u6_calibrate_signals.py`
- Modify: `server/routing_signals.py` (仅词表/正则常量, 按标定结果)
- 产物: `evidence/u6_task9_calibration.md` (进 git, 零题面 — 只有 id/组/计数)

**Interfaces:**
- Consumes: Task 6 冻结基线 run 的 preds (从 `u6_baseline_run_1.json` 提取 id→pred, **脚本内部读, 不打印题面**); `load_gold()`; `RoutingSignals`
- Produses: 标定报告 (可见集上逐信号 fire 计数 + widen 后 exact/fatal 变化表); 冻结后的词表 commit

**预登记选择规则 (先于标定数据写死):** 采纳一版词表 iff 可见集 (legacy 181 + dev 12) 上 — (a) legacy exact 相对基线不降; (b) dev exact 降 ≤ 1; (c) `study_sig` 与 `cdisc_sig` 各至少 fire 1 次 (无死信号)。迭代 ≤ 5 轮, 超出停下上报。

- [ ] **Step 1: 写失败测试** — `visible_subset(gold) -> list` 只留 legacy/dev 两组 (断言组集恒等 `{"legacy","dev"}`); `simulate(gold_subset, base_preds, signals) -> report` 纯离线 (对 base pred 施加 widen_reason, 不再调 LLM — 信号层不依赖 router 输出以外的东西, 离线模拟与真跑等价, 用一条对照测试钉住: 对 stub signals, simulate 结果 == decide_corpus 逐题结果)。
- [ ] **Step 2: 跑测试确认失败 → 实现 → 通过**。CLI: `./.venv/bin/python -m eval.u6_calibrate_signals --baseline data/study/st01/eval/runs/u6_baseline_run_1.json` 输出: 每信号 fire 的 id 列表 (按组) / widen 前后 exact/fatal per 组 / 选择规则三条的判定。**stdout 零题面**。
- [ ] **Step 3: 标定循环 (≤5 轮)** — 每轮: 跑 calibrate → 若违反选择规则, 只调 `CDISC_STRUCT_TERMS`/正则 (方向: 删过宽词, 不加临床概念词) → 记轮次表进 evidence。达标即冻结。
- [ ] **Step 4: 词表冻结 commit** — `git commit -m "feat(u6-t9): 信号词表标定冻结 (N 轮; 可见集 legacy Δexact≥0, dev drop≤1, 双信号活跃)"` + evidence 落盘 commit。**此后词表不许再动。**

---

### Task 10: 全闸三遍 (七条款判定; 结果预登记)

**Files:**
- 产物: `data/study/st01/eval/runs/u6_after_run_{1,2,3}.json` (gitignored) + `evidence/u6_task10_gate.md` (进 git)

- [ ] **Step 1: after 三遍** — `./.venv/bin/python -m eval.run_routing_eval --runs 3 --out-prefix u6_after_run --signal-layer on`
- [ ] **Step 2: 判定** — `./.venv/bin/python -m eval.u6_gate_verdict --baseline .../u6_baseline_run_{1,2,3}.json --after .../u6_after_run_{1,2,3}.json --output .../u6_gate.json`
- [ ] **Step 3: 按预登记执行** — rc=0 ⇒ 记录七条款表 + fatal_ids 前后对照 + widen fire 统计, 进 Task 11; rc=1 ⇒ **Global Constraints 的退回预登记生效**: revert Task 7/8/9 代码 commit (Phase 0 存续), `evidence/failures/u6_task10_attempt_1.md` 归档 (输入/产物/技术判定/业务判定/下一 attempt 输入), 上报用户, 单元转 FAIL 收口 (跳到 Task 12 的核验与 Task 13 收口, 按 FAIL 形态写)。
- [ ] **Step 4: Commit** — evidence 归档。

---

### Task 11: 答题侧 spot-check (auto off vs on, 修订仪器)

**Files:**
- 产物: 答题 run json (gitignored) + `evidence/u6_task11_spotcheck.md` (进 git)

**范围 (spec §5.3):** 信号层实际改判的题 (从 u6_baseline vs u6_after run diff 提取 id) + 检索脆弱 4 题 (`st01_v11_q19, st01_v2_q14, st01_v2_q15, st01_v2_q21`) + `q23r` 在池检查。

- [ ] **Step 1: 提取改判 id 清单** (零题面, 只 id) → evidence。改判题落在哪个题集决定跑哪侧: docs 侧必跑; cards 侧仅当有 v2 题改判 (q07 在 final, 必有) ⇒ 两侧都跑。
- [ ] **Step 2: 答题双臂各三遍** (Bedrock 成本点名: 最多 12 个答题 run; 跑前向用户报成本并确认) — 每侧: `--corpus auto --judge` ×3 (信号 off 臂: 临时以 `signals=None` 构造 — run_eval 侧加 `--signal-layer off|on` 透传, 实现于本 task, 带 wiring test) ×3 (on 臂)。
- [ ] **Step 3: 判读** — `./.venv/bin/python -m eval.u6_answer_verdict --arm-a <off×3> --arm-b <on×3> --family docs ...` (cards 同); E1/E4/divergent_readings + 改判题逐题点名 + 脆弱 4 题 E3 式点名 + q23r 是否在不可判池。**引用纪律**: 结论词自带池限定; E4 触发则不下结论。
- [ ] **Step 4: evidence 落盘 + Commit**。

---

### Task 12: 规则 D 三方核验 (五方不同 session)

- [ ] **Step 1: 审查方** (code-reviewer, opus): 审 Task 7-9 代码与判定链 vs spec §4/§5 零偏离; 专项: 信号层是否泄漏 held-out 概念 (词表逐词裁定) / widen-only 断言是否被测试钉死 / 引用纪律越界扫描。报告落盘。
- [ ] **Step 2: 抽检方 A** (debugger, opus): 非自洽复算 — 七条款判定逐条用 Fraction/异源写法复算; widen fire 计数从 run detail 独立重数; spot-check E1/支配清单复算。落盘 `evidence/step_u6_audit.md` (进 git)。
- [ ] **Step 3: 抽检方 B** (test-engineer, opus): 变异测试 `u6_gate_verdict` / `u6_answer_verdict` / `routing_signals` / `run_routing_eval` 修缮点 — 必含: 对调型 (baseline/after 对调, off/on 臂对调, fatal/exact 两列对调) + **合取/并集项每一半** (条款 4 的 AND 两半 / E4 并集 / validate_inputs 各分支) + purge `__pycache__` + compile 前置检查。落盘 `evidence/step_u6_audit_mutation.md` (进 git)。
- [ ] **Step 4: controller 收敛** — findings 处置 (修 / 记已知限制), 「派了审查」≠「审过了」: 任一报告缺失 = 该环没发生, 在证据里点名。

---

### Task 13: 收口 (checkpoint + 链更新 + retro)

- [ ] **Step 1: checkpoint** — `sdtm-rag/evidence/checkpoints/doc_track_u6_routing_debt.md`: 结构照 U5 收口 (一句话 / 改动面 / 数字 / 触发豁免 / 三方核验表 / 已知限制逐条注明看不见什么 / 不能证明什么 / 复跑命令逐字 / 给下一单元硬约束 / 任务台账)。**引用纪律自检闸**: cheap/免费类判词必带池限定; fallback 引用带打空限定; 条款 2/3 不单独引用; 强制档并列 auto 触发面。
- [ ] **Step 2: 链更新** (Chain B + wrap-up checklist) — `DOC_TRACK_KICKOFF.md` §0′ (U6 收口状态 + 剩余候选) / `docs/PROGRESS.md` / `.work/meta/worklog/phase_07_rag_kg.md` / `CLAUDE.md` Key Paths 一行。
- [ ] **Step 3: RETROSPECTIVE** (规则 C, Tier 3): 保留的做法 / 必须补的缺口 / 关键决策复盘, 并入 checkpoint 或独立文件。
- [ ] **Step 4: 全量回归最终跑** — pytest 全绿数字记录; Commit + push。

---

## Self-Review 记录 (写完 plan 后自查)

1. **Spec 覆盖**: §4.1 六项 → Task 1 (I-1/I-4/A-3) + Task 2 (I-2/条款 4) + Task 2 条款 7; §4.2 → Task 2; §4.3 四项 → Task 5; §4.4 → Task 3 + Task 4; §4.5 → Task 6; §5.1/5.2 → Task 7/8/9; §5.3 → Task 11; §5.4 → Task 10 evidence 里报 (docs 侧 source_recall 差并入 Task 11 Step 3 判读); §6 → Task 12 + subagent 约束; §7 → Global Constraints 预登记; §8 → Task 13 checkpoint。无缺口。
2. **占位符**: Task 5 Step 1 两条测试的 `...` 已附冻结的构造规则与断言 (数据由实现方铺开, 断言不许改) — 有意为之并声明; 其余无 TBD。
3. **类型一致性**: `decide_corpus` 三元组签名 Task 7 定义 = Task 8/9/11 消费; `widen_reason` 返回值 `"study_sig"/"cdisc_sig"/None` 全文一致; run json `meta` 键集 Task 1 定义 = Task 2 校验; `FINAL_IDS` 4 题 Task 3 = Task 2 fixture (`final n=4`)。
