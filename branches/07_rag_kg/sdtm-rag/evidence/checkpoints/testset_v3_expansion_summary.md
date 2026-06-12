# 题集 v3 扩充 + s3 长名通道端到端验证 — Result Record

> 状态: **题集扩充 DONE / s3 验证 PASS / 但 v3 暴露 per-category gate FAIL (修复提案见 §6)** (2026-06-12)
> 任务: 扩题集增 margin (cross 25→50) + 补长名 single 题 13 道 (顺手验 s3)
> 上游: `_progress.json` phase_p1_query_routing.followup + `TODO_retrieval_quality.md` §5 未决 follow-up

## 1. 题集 v3 (140q)

`eval/test_set_v3.yml` = v2 102q **逐字节保留** + 38 新题 (q103-q140):

| 类别 | v2 | v3 | 新增 |
|------|----|----|------|
| single_domain | 27 | 40 | +13 (全部纯长名题, 题面零域码/零变量名) |
| cross_domain | 25 | 50 | +25 (5 主题×5: 变量分布/codelist 共享/关系机制/模型概念/域对比) |
| concept | 25 | 25 | 0 |
| mixed | 25 | 25 | 0 |

**出题流程 (沿用 v2 防过拟合)**: 7 writer agent 盲对检索实现 (只读 knowledge_base/) → 7 个独立
scientist 审计员逐题开 gold 文件核验 (Rule D 异 type): **37 PASS + 1 FIX (q128 补 VSSTRESC) + 0 REJECT**
→ 程序化防漏检 0 问题 (fact 全 verbatim 在 gold / 源全存在 / 长名题零码泄漏 / 零重复)
→ **verifier 异 type 抽检 N=8 (含 FIX 题 q128): 8/8 PASS APPROVE** (Rule D 第二道)。
审计 trail: `evidence/checkpoints/testset_v3_authoring_audit.json`。

**长名探针设计 (q128-q140)**: 10 道 s3 可匹配名 (多词或单词 ≥10 字符) + 3 道**故意的边界探针**
(q134 "Concomitant Medications" 自然措辞 ≠ KB 名 "Concomitant/Prior Medications" / q139 "Exposure" +
q140 "Comments" 被 s3 短词防撞守卫排除)。边界探针按设计是诚实探针, 允许失败, 失败即记录边界。

## 2. s3 端到端验证 — ✅ PASS

探针脚本 (新增): `eval/probe_s3_longname.py` — resolve() 通道级归因 (题面无码 token 时, 返回
domains/<CODE>/spec.md 的唯一可能路径就是 s3 长名 matcher → 归因确定)。

| 验证项 | 结果 |
|--------|------|
| 10 道可匹配长名题 s3 fire | **10/10** (`eval/ablation_t1/v3_s3_probe.json`), 全部零码 token |
| 同 10 题 retrieval-only ON src recall | **10/10 = 100%** |
| 其中 OFF 下本会 miss 的 | q135 (Demographics) OFF=0% → ON=100% = s3 净救回 |
| 3 道边界探针 s3 不 fire | 符合设计 (q134 名称变体 / q139 q140 守卫排除) |

**结论: s3 (2026-06-09 实现, v2 未实测) 首次被真实 eval 题穿透验证, 工作正常。**

## 3. Eval 结果 (retrieval-only, top-15)

环境零漂移 sanity: v2 102q ON 复跑 = 99.0%, 与 2026-06-09 逐题一致 (`v2_sanity_20260612.json`);
v3 中 v2 子集 vs sanity 逐题 diff = 0。

| 类别 | v3 OFF | v3 ON (--structured-lookup --hybrid) | gate ≥95% |
|------|--------|--------------------------------------|-----------|
| single_domain (40) | 93.75% | **92.5%** ← **ON 净负** | ❌ |
| cross_domain (50) | 53.0% | **93.0%** | ❌ |
| concept (25) | 92.0% | 100% | ✅ |
| mixed (25) | 80.0% | 100% | ✅ |
| **overall** | 76.4% | **95.4%** | (avg PASS, **per-category FAIL**) |

杠杆在 38 新题上净救 10 题; 但 single 类 OFF→ON 逐题账 = s05 +0.5 / q135 +1 / q139 q140 各 -1
→ **净 -0.5 题, ON 在扩充集上对 single 类首次净负** (v2 上不可见, 因无此类题)。

**判定: v3 把 v2 的天花板分数 (99.0%) 拉回真实边界 — per-category gate 在扩充集上 FAIL。**
这正是扩 margin 的目的: v2 上 single/cross 100/96 是小样本天花板, 不是真实能力。

## 4. ON 7 个 miss 的根因分类 (微型消融钉死)

| # | 题 | 根因类 | 证据 |
|---|----|--------|------|
| 1 | q139 q140 | **hybrid collateral 回归** (OFF=100% → ON=0%): s3 守卫排除短词名 → 无注入保护; BM25 融合把 rank 10/12 的 spec 挤出 top-15 | 四配置消融: s1-only=rank10/12 (无害), hybrid-only=MISS (元凶) |
| 2 | q134 | **斜杠复合长名变体**: "Concomitant Medications" ≠ KB 名 "Concomitant/Prior Medications"; 语义检索四配置全 MISS, 只有确定性注入能救 | 消融 OFF/s1/hybrid/ON 全 MISS |
| 3 | q107 | **dist 锚缺 "datasets" 同义词**: 题面 "Which SDTM datasets carry..." 无 "domains" 字样 → dist intent 不 fire | probe: resolve()=[] |
| 4 | q119 q126 q73 | **概念/定义型 gold 在 chapters/model, 题面不点名域** (--LNKID/--LNKGRP 定义在 ch04; SE-TE 对比 TE/spec 排 >15; q73 已知残留) | 与 P1 已记录的"变量→定义文件通道"缺口同类 |

## 5. 新发现 (本轮最有价值)

**s3 守卫排除 + hybrid collateral 的组合伤害此前不可见**: P1 时路由隔离守住了 "S1 fire 的题";
但 "S1/s3 都不 fire 而 hybrid 在跑" 的长名题 (q139/q140) 无保护, ON 反而劣于 OFF。
v2 没有这类题, 所以 P1 的零回归 gate 没探测到。这是真实用户措辞 ("the Exposure dataset") 会踩中的。

## 6. 修复提案 (pattern-level, 未实施 — 待用户 ack 后另开 attempt + Rule D)

| 修 | 内容 | 性质 | 预期 |
|----|------|------|------|
| (a) | dist 锚 `\bdomains\b` → `\b(domains|datasets)\b` | 同义词泛化, 仍需 已知变量+成员动词 双锚 | q107 救回 |
| (b) | 长名 matcher 对含 "/" 的 KB 名生成自然变体 ("X/Y Z" → "X Z" + "Y Z"), KB 数据驱动通用变换 | 非硬编码 CM; 同时覆盖 TU/TR/IE 等斜杠名 | q134 救回 |
| (c) | 短词单词长名 (现守卫排除) 改为**上下文锚定匹配**: 仅当后跟 dataset/domain/data 时 fire ("Exposure dataset" ✓, q96 "Cumulative Exposure)" ✗ 已验无撞车) | 守卫放宽但保留防撞 | q139 q140 救回 (注入置顶, 压过 hybrid collateral) |
| — | 上述落地后预期: single 100% / cross 95.0% (q73+q119+q126 残留) / concept mixed 100% | cross 恰好压线 | gate 恢复但 cross 零 margin |
| (d) | **真正的 margin 杠杆**: 通用变量 (--LNKID 类) / 概念定义 → chapters/model 定义文件通道 (q73 q119 q126 同类), 即 P1 时记录的 "变量→model 定义文件通道" | 架构件, 单独立项 | cross 95→98+ |

**防过拟合多层防御 (修复 attempt 必带)**: ① 三修全为 KB 数据驱动的通用变换, 零硬编码题面/域名;
② 零回归 gate = v3 140q + v2 102q OFF/ON 配对全复跑, 逐题 diff; ③ 集外泛化探针 (修后新写
"Prior Medications dataset" / "Comments domain" / "which datasets include SITEID" 等不在题集的探针);
④ pytest 补用例; ⑤ Rule D 异 type 代码审。

## 7. 产物清单

| 文件 | 内容 |
|------|------|
| `eval/test_set_v3.yml` | 140q (v2 逐字节保留 + q103-q140) |
| `eval/probe_s3_longname.py` | s3 通道归因探针脚本 (新) |
| `eval/ablation_t1/v2_sanity_20260612.{json,log}` | v2 ON 复跑 99.0% 零漂移 |
| `eval/ablation_t1/v3_off.{json,log}` / `v3_on.{json,log}` | v3 OFF/ON 配对 eval |
| `eval/ablation_t1/v3_s3_probe.json` | 13 长名题 resolve 归因 |
| `evidence/checkpoints/testset_v3_authoring_audit.json` | 38 题出题+审计完整 trail |
| 本文件 | 收口记录 |

## 8. 规则合规

- **Rule A** (出题=高改写率内容创作): 独立审计员全量 38/38 逐题核验 (超过抽检要求) + verifier 二道抽检 N=8。
- **Rule B**: 本轮无失败 attempt (eval FAIL 是题集揭示的系统缺口, 非工件失败; 修复另开 attempt)。
- **Rule D**: writer (workflow 默认 agent) ≠ 审计 (oh-my-claudecode:scientist) ≠ 抽检 (oh-my-claudecode:verifier), 三 type 隔离; main session 仅做编排+组装+程序化检查。
- **生产未动**: 本轮零 server 代码改动 (probe 脚本为 eval 侧新增); 生产 /ask 行为不变。
