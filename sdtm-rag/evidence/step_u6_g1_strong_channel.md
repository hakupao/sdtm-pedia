# U6 G1 — study 信号收紧强通道 (证据)

> 2026-08-18 · 实现方 u6-t8-impl · controller 裁定采纳 Task 9 标定方 G1 提案
> 关联: `evidence/u6_task9_calibration.md` §5 (阻断) · `server/routing_signals.py` 模块头 G1 段

## 1. 改了什么

`RoutingSignals._study_signal` 由「`StudyLookup.resolve()` 有任意命中」收紧为
「**强通道**命中」= `StudyLookup.strong_hit()`:

| 通道 | 内容 | 强/弱 | 作 widen 依据 |
|---|---|---|---|
| ① | label 全文子串 (+ OID 首段家族扩张) | 强 | ✅ |
| ②a | 多 token 段**交集** (合取) | 强 | ✅ |
| ②b | 单 token 段命中 | **弱** | ❌ (G1 排除) |
| ③ | 别名 → form scope | 强 | ✅ |

排除 ②b 的判据 (Task 9 可见集实测): 本研究 EDC 的 item OID 段沿用 SDTM 风味命名, 一道
**纯标准题**里的变量名会精确撞段 ⇒ 6 道纯标准题被误拓宽 (150 道 cdisc 判定题的 4.0%),
每触 −1 exact, 模拟 legacy exact 173 < 冻结阈值 178。误触 6/6 全部出自 ②b。

实现落点是 `StudyLookup.strong_hit()` (加法式只读方法), 与 `resolve()` **共用**同一个
`_channel_hits()`。共用而非另写一份: 两份筛选逻辑漂移的症状是静默的 —— 信号层照常 fire,
只是它 fire 的依据与 resolve 实际注入的卡不再是一回事。

`strong_hit` 用的是 **cap 过滤后**的命中: 命中集超 `_MAX_CARDS_PER_MATCH` 在 resolve 里
就是"不具判别力, 整体跳过", 没有理由在信号层反倒算作依据。

## 2. `resolve()` 逐位不变 (差分实测, 真 catalog)

共用 `_channel_hits` 意味着重构动了 `resolve` 的内脏, 而 `resolve` 在 S2 生产注入路径上
(`server/rag.py:386`)。故做了**老实现 vs 新实现**的差分:

```
queries=7070  resolve_mismatch=0
any_hit(cards)=5031  any_hit(scopes)=60  strong_hit=1425  weak_only=3610
VERDICT: IDENTICAL
```

- 语料: 真实 `data/study/st01/catalog.json` (959 items) + 真实别名表。
- 题面: 由 catalog 自身机械合成 (每 item 的 label / 首段 / 段对 + 3000 条随机多 token 组合
  + 别名词 + 4 条边界串), 覆盖 ①/②a/②b/③ 四通道与 cap 边界。
- `weak_only=3610` = 旧口径 (任意命中) 会 fire 而新口径不会的题量。**注意读法**: 这是
  合成题面分布下的分离度, **不是**生产/评测题面上的 widen 率 —— 那个数字由 Task 9 标定台
  与 Task 10 全闸给。

**复跑** (脚本一次性, 内容如下; 红线: 只打计数与布尔, 不打任何 label / OID / 题面):

```bash
cd sdtm-rag
git show <G1 之前的 commit>:sdtm-rag/server/study_lookup.py > /tmp/study_lookup_old.py
./.venv/bin/python /tmp/diffcheck.py      # 脚本见下
```

```python
"""resolve() 逐位不变的差分验证 (老实现 vs 新实现, 真 catalog)。"""
import importlib.util, json, random, sys
from pathlib import Path
sys.path.insert(0, "sdtm-rag")  # 仓内绝对路径
from server.config import settings
from server.study_lookup import StudyLookup as New

spec = importlib.util.spec_from_file_location("old_sl", "/tmp/study_lookup_old.py")
old_mod = importlib.util.module_from_spec(spec)
sys.modules["old_sl"] = old_mod          # dataclass 装饰器要求模块已注册
spec.loader.exec_module(old_mod)
Old = old_mod.StudyLookup

new = New.from_paths(settings.study_catalog_path, settings.study_aliases_path)
old = Old.from_paths(settings.study_catalog_path, settings.study_aliases_path)
items = json.loads(Path(settings.study_catalog_path).read_text(encoding="utf-8"))["items"]
rnd = random.Random(20260818)

queries = []
for it in items:
    lab, oid = it["label"], it["item_oid"]
    segs = [s for s in oid.split("_") if len(s) >= 3]
    queries += [lab, f"{lab}はどの変数ですか"]
    if segs:
        queries += [f"{segs[0]}について", f"{lab} {segs[0]} の話"]
    if len(segs) >= 2:
        queries.append(f"{segs[0]} と {segs[1]} は別ですか")
for _ in range(3000):
    picks = [rnd.choice(items)["item_oid"].split("_")[0] for _ in range(rnd.randint(2, 4))]
    queries.append(" ".join(picks) + " について")
for a in (old.aliases or []):
    queries.append(a["raw"] + " の項目")
queries += ["", "   ", "この項目の入力方法は?", "SDTM のどの変数ですか"]

mismatch = n_cards = n_scopes = n_strong = n_weak_only = 0
for q in queries:
    o, n = old.resolve(q), new.resolve(q)
    if (o.cards, o.form_scopes) != (n.cards, n.form_scopes):
        mismatch += 1
    n_cards += bool(n.cards); n_scopes += bool(n.form_scopes)
    strong = new.strong_hit(q); n_strong += strong
    if (n.cards or n.form_scopes) and not strong:
        n_weak_only += 1
print(f"queries={len(queries)}  resolve_mismatch={mismatch}")
print(f"any_hit(cards)={n_cards}  any_hit(scopes)={n_scopes}  strong_hit={n_strong}  "
      f"weak_only={n_weak_only}")
print("VERDICT:", "IDENTICAL" if mismatch == 0 else "DIFFERS")
```

## 3. 变异测试 (10 条, 存活 0)

| # | 变异 | 转杀者 |
|---|---|---|
| G1a | 收紧改回 `resolve()` 任意命中 | `test_weak_single_token_channel_does_not_fire_the_study_signal` 等 9 条 |
| G1b | 强通道漏掉 ③ 别名 | `test_strong_hit_true_for_each_strong_channel[③]` |
| G1c | 强通道漏掉 ②a 交集 | 同上 [②a] |
| G1d | 强通道漏掉 ① label | 同上 [①] |
| G1e | 强通道混进 ②b | `test_strong_hit_false_for_the_weak_single_token_channel` |
| G1f | 一票否决式收紧 (`and not single_token`) | `test_strong_hit_true_when_strong_and_weak_both_hit` |
| G1g | `resolve` 合并顺序 label 提前 | `test_resolve_puts_segment_hits_before_label_substring` |
| G1h | `resolve` 丢掉 ②b (注入面回归) | 既有 S2 用例 |
| G1i | `resolve` 忘了总 cap 截断 | `test_resolve_total_cap_still_truncates_after_the_refactor` |
| G1j | `resolve` 忘了跨通道去重 | 既有 S2 用例 |

另复跑 Task 8 修复环的 15 条变异 (其中 M9/M10 按 Task 9 冻结版正则更新锚点, M11 靶子已移入
`strong_hit` 由 G1b/c/d 覆盖): **存活 0**。

## 4. 回归

```bash
cd sdtm-rag
./.venv/bin/python -m pytest                       # 1641 passed, 0 failed (1628 → +13)
./.venv/bin/python -m pytest scripts/tests/test_study_lookup.py -q      # 64 passed (S2 既有全绿)
./.venv/bin/python -m ruff check server/study_lookup.py server/routing_signals.py \
    scripts/tests/test_study_lookup.py scripts/tests/test_routing_signals.py
./.venv/bin/python -m mypy server/study_lookup.py server/routing_signals.py    # Success
curl -sS -o /dev/null -w "%{http_code}\n" localhost:8000/api/info              # 200
```

Task 9 冻结的三张词表/正则常量、Task 8 冻结的方向表/白名单/异常语义: **一字未动**。
S2 生产注入路径 (`rag.py` 的 `_apply_study_lookup`): 零改动。零 LLM。
