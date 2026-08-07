# VI 交叉引用完整性 — 收口 checkpoint

> 状态: **实现完成, 三方审查进行中** (2026-08-07)
> 设计 `docs/superpowers/specs/2026-08-07-vi-truncation-completeness-design.md`
> 计划 `docs/superpowers/plans/2026-08-07-vi-truncation-completeness.md`
> 上游: `evidence/checkpoints/s1_variable_index_literal_section.md` §4 已知限制 1 (规则 A 抽检 D-3)

---

## ⚠️ 引用前必读 — v3 的 98.93% 一动不动是**预期**, 不是没效果

```
CDISC v3 检索闸 (140q, --retrieval-only --hybrid --structured-lookup, section 级判据)

    改动前  98.9286%
    改动后  98.9286%      140 题逐题相同, 变化集为空
```

**那把尺子对本修复结构上失明**: section 级 source recall 只看 section 名对不对,
**不看正文是否被截断**。本轮一个 section 名都没改, 所以它必然不动。

**引用本轮成果不得用 v3 数字。** 能证明"修好了"的只有:
- 层① 数据不变量 (§3.1): 3 红 → 5 绿
- 层② context A/B (§3.2): 截断答不出 / 完整答得出
- 生产端到端 (§3.4): 答案含旧语料**结构上产不出**的变量

---

## 1. 问题

`VARIABLE_INDEX.md` §三 CT 交叉引用表每行只列前 15 个引用变量就写 `... (N total)`。
**该表是"哪些变量引用这个码表"的唯一权威来源**, 被截断意味着注入的 chunk 正文结构上答不全。

| 处 | 上限 | 命中 | 隐藏条目 | 生成器 |
|---|---|---|---|---|
| VI §三 CT 交叉引用 | 15 | **9 / 135 行 (6.7%)** | **226** | `.work/04_optimization/scripts/generate_variable_index.py:253` |
| 域 spec 交叉引用段 | 5 | 2 文件 (AE / LB) | 10 | `.work/04_optimization/scripts/generate_cross_references.py:236` |

最宽: `C66742` 123 / `C71620` 58 / `C99079` 44 / `C66789` 36 / `C66728` 26。

**为什么现在修**: 上一轮把 18 题 VI 子集拉到 100.00%, 但那个分数**不能读作"VI 类问题已解决"**
—— q109 的 `TU.TULAT` 与 q69 的 `EX.EXDOSU` 都恰好排在**第 15 位 = 截断边界最后一位**, 属压线过关。
gold fact 只要落在第 15 位之后, source recall **仍判 1.00** 而正文根本答不出来。

## 2. 修法

删掉两个生成器的条数上限, 重生成 KB, 重灌索引。**KB 是生成物, 全程未手改。**

体积 **129.6 KB → 133.8 KB (+4.2 KB)** —— 旧上限买到的就是这 4.2 KB, 代价是把该表在最需要它的
9 个宽码表上变成半张表。最宽的 `C66742` 那行约 1.5K 字符, 远在 chunk 尺度内 (重灌后 chunk 总数
**4303 = 与基线同数**, 说明行变长未改变分块边界)。

生成器幂等已验: 二次运行零新增变更。改动前已确认生成器未漂移 (重生成与已提交 KB 唯一 diff 是日期行)。

## 3. 实测

### 3.1 层① 数据不变量 (主护栏, 零 LLM, 常驻)

`scripts/tests/test_kb_crossref_completeness.py` —— **先红后绿, 红是数据错不是代码错**:

| 断言 | 改动前 | 改动后 |
|---|---|---|
| 每 CT 行正文条目数 == 自己声称的 N | ❌ 9 行不符 | ✅ |
| VI 全文无截断标记 | ❌ 9 处 | ✅ |
| 域 spec 无截断标记 | ❌ AE / LB | ✅ |
| §三 仍是 135 行 (防"删掉截断行"这种假修法) | ✅ | ✅ |
| **索引里的 CT chunk 正文与 KB 逐条一致** | ❌ 9 个 chunk 不符 (C66742 缺 108 个) | ✅ |

最后一条不能省: KB 对而索引是旧的照样答不出来, 且 `kb_freshness.py` 的存在动因正是
2026-08-04 实测到"部署中的向量库把 `VARIABLE_INDEX.md` 欠切 70%" —— **同一个文件有前科**。

```bash
cd sdtm-rag && .venv/bin/python -m pytest scripts/tests/test_kb_crossref_completeness.py -q   # 5 passed
```

### 3.2 层② context A/B (改动前/后数字的来源)

不做两次全量重灌: 同一问句喂两份 context (旧的 15 条截断版 / 新的完整版), 同模型 temperature=0,
变量隔离得更干净。

```bash
cd sdtm-rag && .venv/bin/python -m eval.vi_completeness_ab
```

| 码表 | gold (字母序末位) | 截断 context | 完整 context | 判定 |
|---|---|---|---|---|
| `C66742` (N=123) | `VSLOBXFL` (第 123 位) | ❌ 答不出 | ✅ 答得出 | **判别力成立** |
| `C71620` (N=58) | `URSTRESU` (第 58 位) | ❌ 答不出 | ✅ 答得出 | **判别力成立** |

脚本内置两条前置断言 (gold 必须在完整 context 里 / 必须不在截断 context 里), 防止对照本身失效。

### 3.3 层② 独立 gold 集

`eval/test_set_vi_completeness.yml` (2 题, **不并入 v3**)。

```bash
cd sdtm-rag && .venv/bin/python eval/run_eval.py eval/test_set_vi_completeness.yml \
    --hybrid --structured-lookup --judge
```
source 100% / fact 子串 100% / fact judge 100%。

**出题规则 (规则驱动, 非挑例子)**:
> 凡 `N > 15` 的码表, 问"哪些变量引用它", gold fact 取位置 > 15 的条目 (按字母序末位)。

三层防线:
1. 规则作用于 **9 个宽码表全体**, 不是挑一个; 只落 2 道控体量, 其余 7 个由层① 全覆盖。
2. 规则可机械执行 —— 任何人拿它能重新生成同一批题, 不依赖"我知道哪里坏了"。
3. 真护栏是层① 的数据不变量; 题只是端到端佐证。**题与层① 冲突时以层① 为准。**

> `C71620` 与 v3 的 q69 是同一个码表, 但**不是重复题**: q69 的 gold 是 `EX.EXDOSU` (第 15 位,
> 旧正文可见), 本题问的是位置 > 15 的条目 —— 正是旧正文答不出来的那部分。

### 3.4 生产端到端

重启服务 (`launchctl kickstart -k`) 后:
- 启动期预热仍成立: `s1_vi_section_map entries=159`; `ready chunks=4303`
- 冒烟一道宽码表题, 首个引用块 `§三 CT 交叉引用: C66742`, **答案含 `VSLOBXFL`** ——
  该变量在旧语料里**结构上不存在**。

### 3.5 连带闸 (全部实跑, 非推断)

| 闸 | 结果 |
|---|---|
| `scripts/reconcile_meta.py` | 8 项全 OK (含 `TAETORD->43` / `VISITDY->36` / 1917 entries / 1523 vars) |
| `scripts/check_index_freshness.py` | in sync (`f44813babbf5…`) |
| v3 检索闸 140 题 | **98.9286% → 98.9286%, 逐题相同, 变化集为空** (见顶部声明) |
| 全量 pytest | **852 → 857 passed** (+5 = 层① 4 + chunk 层 1) |

## 4. 过程中的两件事 (都必须点名)

### 4.1 顺带修好一个既有缺陷 (非本次引入)

重生成时冒出**第四个**文件变化: `knowledge_base/domains/PC/spec.md` 多了一行
`- [Relationships (Ch8)](...) — RELREC, SUPPQUAL usage`。

按计划"若有第四个文件变化, 停下查清"执行, 根因: `generate_cross_references.py` 的
`check_relrec_reference()` 读 `assumptions.md` 判断是否该加该链接; `PC/assumptions.md` 大篇幅讲
RELREC (PC↔PP 关联的四种方法) 故**确实该有**。而已提交的 `PC/spec.md` 生成于 `eb51ca5`
(Phase 6 P0+P1), **早于 06 深审给 `PC/assumptions.md` 补进那些 RELREC 正文**。

即: **生成器是对的, 已提交的 spec 自 06 以来陈旧了。** 爆炸半径就这一个域 (重生成只动了它)。

### 4.2 我自己造了一个判据缺陷并修掉

A/B 初版用 `DOMAIN.VAR` 点号形式做子串匹配, 判 `C71620` **无判别力**。查看原始答案后发现
模型**答对了** —— 它用按域分组的表格作答 (`| UR | URORRESU, URSTRESU |`), 点号形式在这种
答案里永远不出现。

改用**裸变量名** (SDTM 变量名自带域前缀故全局唯一), 并实测确认裸名在截断 context 里同样不存在,
判别力未被削弱。`expected_facts` 同步改。

**这是本项目第 1 条硬规矩的同一个病**: 判据检查工具必须与被检查对象逐字同语义。
上一轮是 lint 与真判据不同语义制造 8 条假阳性, 这一轮是 A/B 判据与答案表达形式不同语义,
把一次正确作答误判成失败。

## 5. 已知限制

1. **A/B 隔离的是 context 变量, 证明的是因果, 不等于线上答题必然变好**。真实查询的 context
   组成与本对照不同。
2. **只落 2 道端到端题**; 其余 7 个宽码表靠层① 的数据不变量而非端到端验证 —— 层① 证明的是
   "数据完整", 不是"模型用得上"。
3. **重灌改变全库 embedding**, v3 逐题 Δ0 是**实测**非推断 (两份 report 工件均在
   `evidence/checkpoints/`, 可从文件复算)。
4. **`VS.VSLOBXFL` / `UR.URSTRESU` 这类"字母序末位"是本轮的 gold 选法**, 不代表它们在业务上
   比中间位置的条目更重要; 选末位只为最大化与旧截断边界的距离。
5. **域 spec 交叉引用段只有 AE / LB 两个文件命中**, 样本太少, 无法评估该处修复的普遍收益。

## 6. 三方隔离 (规则 D)

| 角色 | 承担 | 裁定 |
|---|---|---|
| 实现 | 主 session | — |
| 审查 | *待回填* | *待回填* |
| 抽检/验收 (规则 A, 抽样总体 = 9 个被截 CT 行 + 2 个域 spec 段) | *待回填* | *待回填* |

## 7. 复跑

```bash
cd sdtm-rag
.venv/bin/python -m pytest scripts/tests/test_kb_crossref_completeness.py -q   # 5 passed
.venv/bin/python -m eval.vi_completeness_ab                                    # 两题判别力成立
.venv/bin/python eval/run_eval.py eval/test_set_vi_completeness.yml \
    --hybrid --structured-lookup --judge                                       # fact 100%
.venv/bin/python scripts/reconcile_meta.py                                     # 8 项全 OK
.venv/bin/python scripts/check_index_freshness.py                              # in sync
.venv/bin/python -m pytest -p no:warnings 2>&1 | tail -1                       # 857 passed
```

v3 逐题 Δ0 从工件复算 (不必重跑):

```bash
cd sdtm-rag && .venv/bin/python - <<'PY'
import json
load = lambda p: {x["id"]: x["source_recall"]
                  for x in (lambda d: d["results"] if isinstance(d, dict) else d)(json.load(open(p)))}
a = load("evidence/checkpoints/s1_vi_after.json")
b = load("evidence/checkpoints/vi_trunc_v3_after.json")
diff = {k: (a[k], b[k]) for k in a if a[k] != b[k]}
print("逐题相同:", not diff, "| 变化:", diff)
PY
# 逐题相同: True | 变化: {}
```
