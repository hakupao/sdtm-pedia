# S2 Rule D 独立审查 (code-reviewer, 非自审)

**日期**: 2026-06-09
**审查对象**: S2 = S1 分布意图泛化修复 + Hybrid BM25 加法融合
**复现解释器**: `.venv/bin/python` | collection `sdtm_kb_v1` (4146 chunks, 未重建)
**总判定**: **PASS**

---

## 1. 独立复现 (四类 ≥95%)

命令: `.venv/bin/python eval/run_eval.py eval/test_set_v2.yml --retrieval-only --structured-lookup --hybrid`

| 类别 | 自报 | 复现 | 一致 |
|------|------|------|------|
| single_domain | 100 | **100.0** | ✓ |
| cross_domain | 96 | **96.0** (24/25) | ✓ |
| concept | 100 | **100.0** | ✓ |
| mixed | 100 | **100.0** | ✓ |
| overall | 99.0 | **99.02** | ✓ |

唯一 miss: q73 (cross_domain, gold `model/06_relationship_datasets.md`). 四类 ≥95% **属实**, exit 0.
自报消融矩阵每格独立复现一致 (hybrid 单独 single=83.3 / overall=79.9 亦复现).

## 2. ★★ single 稳健性 (头号风险) — 结论: **稳健 (条件: query 命名 domain code)**

hybrid 单独把 single 砸到 83.3% (25/30). 被砸的 5 题:
- q02 (gold DM/spec.md), q04 (TV), q24 (EX), q64 (PC) — 全是 domain spec.md
- s05 (terminology/core/vs.md)

**恢复机制 = S1 named-domain union-add, 非 RRF 更温和**. 逐题 resolve() 验证:
- q02→[DM/spec.md], q04→[TV/spec.md], q24→[EX/spec.md], q64→[PC/spec.md], s05→[VS/spec.md, terminology/core/vs.md]
- 5 题全部被 S1 deterministically 重新注入其 gold.

q02 四格 rank 追踪 (gold=DM/spec.md):
| 配置 | gold@rank | via_lookup |
|------|-----------|-----------|
| cosine only | 12 (悬崖边) | False |
| hybrid only | **MISS** (掉出 top-15) | - |
| cosine+S1 | 0 | True |
| hybrid+S1 | 0 | True |

→ hybrid BM25 噪声把 spec.md 挤出 top-15; S1 prepend 把它强行钉到 rank 0, 不被挤掉.
机制根因: `retrieve()` 先做 hybrid 融合, 再 `_apply_structured_lookup` prepend (rag.py:200-201,231), 顺序正确.

**脆弱边界 (诚实披露)**: S1 named-domain 路由依赖 query 字面命名 2-字母 code.
对仅用长名的 single 查询 (如 "Demographics dataset" 不含 "DM"), resolve() 返回 []:
- 探针 "What are the required variables in the Demographics dataset?" → resolve()=[]
→ 此时 S1 网失效. 但端到端验证显示: 这类长名查询的 spec.md gold **在 cosine baseline 下也已 MISS** (DM/TV/PC 长名探针 cosine+S1 与 hybrid+S1 均 MISS, EX 均 HIT). 即 hybrid 未使其 *更差* — 是既有 embedding 盲区, 非 hybrid 引入的回归.

v2 single 集合事实: 27 题中 26 题命名 code; 唯一长名题 q03 (gold AE/assumptions.md 非 spec.md) 在 hybrid-only 与 optimal 下均 100% (hybrid 未降级它).
→ **结论**: 组合配置的 single=100% 是**真实的确定性下限**, 条件是 query 命名 domain code (SDTM single_domain 问法的常态). 不是 v2 巧合; 但若未来出现"长名 + spec.md gold + hybrid 降级"三者同时的 single 题, 可能跌破 95% (该 spec gold 在 cosine 下本就脆弱). 保守评级: **稳健 (有明确条件), 非脆弱**.

边际检查: optimal 配置下仅 1 个 gold (s02 concept) 落在 rank 12-14 脆弱区, 其余全部 rank<12. 100%/100% 非刀尖平衡.

## 3. ★ 分布修复反过拟合 — 结论: **通用 pattern, 未过拟合**

- grep 确认: 代码逻辑区 **无** 硬编码 q-number / 变量名. `q34/q67/q68/q71` 及 AESEV/VSTESTCD/EPOCH/C66742 仅出现在 docstring/注释作举例 (structured_lookup.py:6-13,80-81,270).
- pattern = 变量名 ∈ known_variables + `\bdomains\b` + membership-verb (A 锚) 或 CT-code + verb (B 锚). 纯数据驱动.

测试集外分布探针 (7 题, 不同变量/codelist) 全部正确路由 VARIABLE_INDEX.md:

| 探针 | resolve() |
|------|-----------|
| What domains contain the RACE variable? | [VARIABLE_INDEX.md] ✓ |
| List domains using DSDECOD | [VARIABLE_INDEX.md] ✓ |
| Which SDTM domains include VISITNUM? | [VARIABLE_INDEX.md] ✓ |
| In which domains does EPOCH appear? | [VARIABLE_INDEX.md] ✓ |
| Which domains share codelist C66742? | [VARIABLE_INDEX.md, +term] ✓ |
| Across which domains is USUBJID carried? | [VARIABLE_INDEX.md] ✓ |
| What domains use the variable AESEV? | [VARIABLE_INDEX.md] ✓ |

触发面统计 (resolve 非空): single 26/27, cross 24/25, mixed 23/25, concept **3/25**.
→ concept 几乎不被误触发 (安全). "wasted" (非 gold) 注入存在但因 prepend + `_MAX_DOMAIN_SPECS=3` cap + union-add, 四类 recall 仍 ≥96%, 未挤掉真 gold. 无 over-injection 致命问题.

## 4. Hybrid 融合正确性 — 全部 PASS

- (a) **不重 ingest**: collection.count()=4146 (未变), BM25 index size=4146 (匹配), 从 `collection.get()` 建 (rag.py:314-325). ✓
- (b) **RRF 加法**: `_hybrid_fuse` scores[cid] += 1/(c+rank+1) 跨 dense+bm25 两列累加 (rag.py:402-404), 双列命中=强化, 非替换. ✓
- (c) **叠加顺序**: hybrid 先, S1 prepend 后, S1 注入不被挤掉. ✓
- weighted 路径 `span = hi-lo or 1.0` 防除零; 空列表 guard. ✓
- `_meta_matches_where` 正确复刻 _build_where 产出的 flat-eq + $and 子集. ✓

## 5. pytest

`.venv/bin/python -m pytest -q` → **214 passed, exit 0**. ✓
ruff: 仅 1 个 pre-existing RET503 (rag.py:477 `_llm`, T4 路径, 非 S2 改动). py_compile OK.

## 6. q73 残留确认 — 属实, 机制清楚

Q73: "Which special-purpose and relationship domains carry the RDOMAIN variable...", gold=model/06_relationship_datasets.md
- resolve() → [VARIABLE_INDEX.md] (分布意图路由到 index, 非 model/06; S1 注入的是合理替代而非标注 gold)
- dense cosine: model/06 不在 top-50 (embedding 够不到)
- BM25: model/06 在 top-50 排 18/40; rank-18 进 pool-30 但与 dense (缺席) RRF 融合后进不了 top-15
→ 两杠杆机制都不指向 model-chapter 文件. 单一、已理解的残留, 非系统性失败. cross=24/25 属实.

---

## HIGH 问题
无.

## LOW 问题
- run_eval.py:302 `--hybrid-pool` help 文案陈旧, 写 "default settings.hybrid_pool=100", 实际 config.py:59 默认=30. 仅文档陈旧, 不影响行为 (config 默认 30 已复现).
- rag.py:392-397 `_hybrid_fuse` 的 best dict 两段循环略冗余 (setdefault 后被第二段覆盖), 功能正确无 bug.

## 正面观察
- S1 union-add 用 prepend + dedup 保证注入 gold 不被任何下游(含 hybrid)挤出, 是 single 恢复的确定性机制.
- 分布 pattern 真正泛化 (7 测试集外探针全过), 注释把 example 和 pattern 明确分开, 防过拟合意识到位.
- hybrid 不重 ingest (复用 4146 chunks), 加法 RRF 不降级 cosine 既有胜场, 设计正确.
- 边际分析显示 100% 非刀尖 (仅 s02 在脆弱区).
