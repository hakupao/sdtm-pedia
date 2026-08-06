# Plan B Phase 2 (S2) — study 结构化直查收口证据

> 状态: **DONE / 默认启用** (2026-08-06)。`SDTM_RAG_STUDY_LOOKUP_ENABLED` 默认 `True`,
> 生产服务 `com.sdtmrag.api` 已带 S2 重启并冒烟通过。
> 红线: 本文件**只含统计、题 id、结构描述** —— 无 study 题面、无 EDC 字段名/OID、无 form 标签、无别名词。
> plan: `docs/superpowers/plans/2026-08-06-plan-b-phase2-study-structured-lookup.md`
> 前置: `evidence/checkpoints/planb_phase1_federation.md` (Phase 0+1 联邦路由)

## 1. 范围

| 块 | 内容 | 落点 |
|---|---|---|
| Task 1 | `StudyLookup` 核心: label 通道 (①) + OID 首段家族扩张 | `server/study_lookup.py` (新建) |
| Task 2 | 拉丁 token → OID 段通道 (②) + 多 token 交集 (②a) | 同上 |
| Task 3 | 别名表通道 (③) + `from_paths` 装载 (缺 catalog 响亮失败) | 同上 |
| Task 4 | `RAGEngine` 注入层 `_apply_study_lookup` (精确卡 + form scope), S1/S2 互斥闸 | `server/rag.py` |
| Task 5 | 接线: config 开关 / `main.py` 注入 / `run_eval --study-lookup` | `server/{config,main}.py`, `eval/run_eval.py` |
| Task 6 | 真数据别名表 + 验收闸 (两闸) | 数据在 gitignore 区 |
| Task 7 | 规则 D 独立终审 + fix wave (补测试锁) | `scripts/tests/*` |
| Task 8 (本文件) | 联邦复核 + 默认翻 True + 生产冒烟 + 收口 | `server/config.py` |

**不在本 plan**: Phase 3 (eval chunk 粒度判据后续) / Phase 4 (CDISC 变量索引挤占)。

分支共动 **8 个文件** (+1229/-8), 其中生产代码 5 个; **路由 prompt 与路由 gold 零改动**,
CDISC 侧引擎零改动 (终审逐文件 sha256 验证), 故 CDISC 侧无需重跑。

## 2. 三通道 (+②a) 机制 — 抽象描述

全部为**确定性**规则, 零 LLM, 数据源仅 `catalog.json` (959 items) + 本地手工别名表:

| 通道 | 触发形状 | 产出 |
|---|---|---|
| ① label | 题面含某卡 label (NFKC + 去空白归一, 长度下界 4) 作子串 | 该卡 + 其 **OID 首段家族** (家族键 = `(form_oid, 首段)`) |
| ② 段 | 题面里的**单个**拉丁大写 token (ASCII 词边界, 长度下界 3) 恰为某 OID 的一个段 | 该段索引下的全部卡 |
| ②a 段交集 | 题面里 **≥2** 个 token 各自命中段, 但单段集合过宽被 cap 挡 | 各段集合的**交集** (严格全 token 合取) |
| ③ 别名 | 题面含别名表某 term 作子串 | form **scope** (非精确卡), 最多 3 个名额 |

注入在检索前置, 与 dense/hybrid 结果 union-add 合并 (与 S1 共用 `_merge_lookup_first`)。
每个通道有同一个 cap (`_STUDY_MAX_CARDS = _MAX_CARDS_TOTAL = 8`, 同值锁钉住): 单次命中集合超 cap 则**整体跳过**。

日文题面注意: `\b` 在 CJK 下失效 (CJK 属 `\w`), 通道② 用 ASCII-only 词边界, 否则该通道在日文题集上是死代码。

## 3. 验收数字

### 闸 1 / 闸 2 — golden v1.1 (25 计分题 / 27 总题, `--retrieval-only --hybrid`)

| 组 | source recall avg | 说明 |
|---|---|---|
| 基线 (S2 off) | **88.53%** | 与 Phase 1 记账基线一字不差 (终审自跑控制组复现) |
| S2 无别名组 | 92.00% | 分离通道①②贡献 |
| S2 全开 (attempt 1) | 96.00% | q14 仍 FAIL → 归档 `..._attempt1_FAIL_q14.json` (规则 B) |
| **S2 全开 (attempt 2, 过闸)** | **100.00% (+11.47pt)** | 四题 q08/q14/q16/q21 全转 1.0 |

- **闸 1** (4 题转 1.0): PASS。四题分别由通道③ / ②a / ② / ① 修复。
- **闸 2** (零回归): PASS。`regressions=[]`, 对基线与对 attempt 1 **双向**逐题零回归; `improved` 恰为那四题。
- 计分口径未变: `out_of_scope = {q26, q27}` 与基线一致。
- 四题的 9 条 gold 经终审逐条核对 **全部唯一定位到 1 张卡**, `misses` 全空且 `n_hits` 与 gold 数匹配
  → 修复为真, 非打分器假象。

### 闸 3 — 联邦通道复核 (2026-08-06, Task 8)

```
--retrieval-only --hybrid --study-lookup --federated
→ data/study/st01/eval/runs/planb_p2_s2_federated.json
```

| 项 | 值 |
|---|---|
| 25 计分题 avg | **100.0%** (与 collection 组一致) |
| 逐题 source_recall 差异 | **0 题** |
| 逐题 top5 来源集合差异 | **0 题** (本轮连 both 题也无集合变化) |
| routing 分布 | `{'study': 25, 'both': 2}` — 与 Phase 1 形态一致 |
| 分类别 | field_lookup 100% (22q) / form_overview 100% (2q) / version_diff 100% (1q) |

### 测试演进

**720 → 799 passed** (+79, 0 failed / **0 skipped**, junitxml 计数)。
默认翻 True 后全量重跑 **799 passed**; 唯一需同 commit 改的是
`scripts/tests/test_run_eval_flags.py::test_settings_study_lookup_defaults` 的默认值断言
—— 这是刻意设计的"默认值改动必须显式过测试"闸, 本次首次触发。

## 4. 生产冒烟 (默认翻 True 后, 2026-08-06)

`launchctl kickstart -k gui/$(id -u)/com.sdtmrag.api` 重启:

| 检查 | 结果 |
|---|---|
| 启动日志 | `federation study_collection=study_st01 study_lookup='959 items/1 aliases'` → `ready` (同字段) → `Application startup complete`; **零 traceback** |
| S2 可见性闸 (Task 5 F1/F2) | `ready` 日志报**实际加载量**而非开关值 —— 本次首次派上用场, 确认别名表真被读到 (1 条) |
| `GET /api/info` | 200; `federation: true`; `index_fresh: true`; `chunk_count: 4303` |
| `POST /api/ask` (`corpus: study`, id `q08`) | 200; `routed_corpus: study`; 15 sources; **gold 卡命中 1/1** |
| `POST /api/ask` (`corpus: study`, id `q14`) | 200; `routed_corpus: study`; 15 sources; **gold 卡命中 1/1** |

## 5. 已知限制 (必读)

### 5.1 「25 题 100%」的成色

**其中 1 题 (q23, field_lookup, 计分题) 的唯一 gold 是 17 张卡的公共子串, 判别力≈0** ——
只要召回那 17 张里任意一张就得 1.0。这是**既存缺陷** (打分器 `check_source_recall` 按路径子串匹配,
且 42 条 gold 里有 30 条省略 `.md` 后缀), 基线里该题亦为 1.0, **不影响 +11.47pt 的归因**,
但意味着「25/25」里有一题近乎不可证伪。其余 41/42 条 gold 唯一定位。

### 5.2 ②a 的证据强度 — 本轮最大的未证伪面

- 全库形状统计的正确表述是「**8 个独立 token 对形状 (覆盖 19 张卡)**」, 不是「19 个同形态样本」
  —— **段对**才是 query 形状的单位, 多张卡可共享同一对。全库 338 个共现段对中: 8 对属
  「双单段皆超 cap 而交集落回 cap 内」(②a 独有新解锁的形状, q14 那对是其一) / 38 对双单段皆在 cap 内
  (②a 只影响排序) / 292 对混合形态 / **0 对交集超 cap**。359 张 ≥2 段的卡交集规模 min1 p50 1 p90 2 max 6。
- **这些统计证明的是「形状的 cap 安全性与复现性」, 不是「在这些形状上 fire 会提高召回」。**
  后者的证据仍然只有 **n=1** (爆炸半径: 27 题中 5 题有 ≥2 token, ②a 实际 fire **1 题**, 改变最终 cards 集合 **1 题**)。
  8 > 1 让「pattern 级修法」的结论成立, 但强度比原台账写的弱一档。

### 5.3 cap 常数: 平台性 (反过拟合证据) 与对称的无知

cap 扫描 (注入侧 gold 覆盖为指标, 27 题): cap = **6 / 8 / 10 / 16 下全 gold 被覆盖的题数恒为 4**;
`_MAX_CARDS_TOTAL` 扫 6–15 亦恒为 4。→ cap=8 落在一段很宽的**平台**上而非尖峰,
说明 100% 不是靠把常数调到某个悬崖边得来 —— 这是**反过拟合的正面证据**。

代价确实存在且未被证伪:

- label 通道: 515 条 label 中 **193 条 (37.5%)** 家族扩张后超 cap 被**整体跳过**, 其中 **107 条 label 本身唯一** (连坐误伤);
- 段通道: 458 段中 **20 段 (4.4%)** 超 cap 被跳过;
- 抬到 12/16 只让注入量 17→23, **gold 覆盖零增益**。

即现状是**对称的无知**: 无损害证据, 也无收益证据。**本题集无代价 ≠ 该规格无代价。**

### 5.4 生词否决 (刻意保守)

②a 是**严格全 token 合取**: 题面含任一非段的大写词 → 交集必空 → ②a 让路。
27 题中 5 题含 ≥2 大写 token, 其中 4 题含生词, 但**实际损失 0** (四题 recall 1.0/1.0/1.0/oos)。
裁决方向: **宁可保守漏 fire, 不误 fire**; 放宽 = 把未测量面铺开。

### 5.5 通道③ 的通用性无从评估

别名表当前**仅 1 条** (n=1)。该别名在 27 题中 fire 3 题: 1 题 miss→1.0, 另 2 题基线即 1.0 且保持不变
(已知风险实际发生, 被 3 个 scope 名额吸收)。机制本身极简 (子串 → form scope), 但泛化性属实无法判断。

### 5.6 终审模型降档

原定终审模型 **fable** 因额度耗尽不可用, 改由 **opus** 承担 (用户 2026-08-06 确认可接受)。
**非为省钱**。规则 D 隔离靠 5 种不同 `subagent_type` 维持
(feature-dev:code-reviewer / oh-my-claudecode:code-reviewer / oh-my-claudecode:critic /
pr-review-toolkit:silent-failure-hunter / oh-my-claudecode:architect), 实现方与各审阅方互不相同。

### 5.7 规划期缺陷复盘

**q14 attempt 1 FAIL 的根因是规划缺陷, 不是实现缺陷**: 规划期探针口径隐含「限定首段 + 单一 form」,
而实装规格是「全段 + 全 form」(规格如此)。故 NOTES 里 q14 的通道预期在真实索引下被证伪
(两 token 的段命中 21/12 卡双双超 cap → 通道② 完全不 fire)。
这直接触发了 ②a 的设计。失败 run 已按规则 B 归档 `..._attempt1_FAIL_q14.json` (未删, mtime 未触碰)。
**教训**: 规划期探针的口径必须与实装规格逐条对齐, 否则「机制已实证」是假的。

### 5.8 open follow-ups (未做, 显式入档)

1. **M-f**: `_apply_study_lookup` 的「注入量 ≥k 时 `log.warning`」廉价观测点**从未实装** (Task 4→6 交办 (b))。
   当前实测 max slot = 6 << k=15, 非阻塞。
2. **M-d**: 别名 `aliases` 的 `raw` 字段**无生产消费方** —— 注释称「供命中日志排查」但没有任何日志读它, 只有测试断言它存在。
3. **M-e**: `_apply_study_lookup` **完全忽略 `where` 入参** (`server/rag.py`)。当前安全, 因为
   `server/federation.py` 只以无 `domain` / `file_type` 的形式调用 study 引擎 —— 属**未言明的不变量**, 应在 docstring 点明。
4. 继承自 Phase 1: `_FederatedAdapter.build_messages` 把 `corpus` 硬写成 `"both"` ——
   **检索闸不受影响** (全部 `--retrieval-only`), 但**做任何联邦答题 eval 之前必须先修**。本轮未动。

## 6. commit 链

`fbd0d76` (Phase 1 收官) → `HEAD`, 11 commits + 本次:

```
1918129 feat(s2)  StudyLookup label 通道 + OID 首段家族扩张 (Task 1)
62ae9b6 feat(s2)  拉丁 token→OID 段通道 (Task 2)
a943e8e fix(s2)   通道② 先入队 + 正则边界补锁 (Task 2 fix r1)
de23aba feat(s2)  别名表通道 + from_paths (Task 3)
96cbe93 fix(s2)   空别名 term 响亮拒绝 + scope 去重补测 + raw 留存 (Task 3 fix r1)
6f4bf16 feat(s2)  RAGEngine study_lookup 注入层, S1/S2 互斥 (Task 4)
1123eff test(s2)  retrieve 接线锁 + scopes-only 锁 + 常量同值锁 (Task 4 fix r1)
e7d8569 feat(s2)  接线 — config(默认关)/main.py/run_eval --study-lookup (Task 5)
53dfe5e fix(s2)   S2 可见性 — 别名条数入回执/日志 + 联邦关时告警 (Task 5 fix r1)
8121ee8 feat(s2)  通道②a 多 token 交集 (Task 2 fix r2, 承载 q14 修复)
41324fd test(s2)  终审补锁 — 家族 form 分量/NFKC 实证/标签长度双向/常数同值/回执多尺度 (Task 7)
+ 本 task: 默认翻 True + 本文件 + 收尾索引
```

## 7. 复跑 / 回滚

```bash
cd sdtm-rag
# 验收组 (collection 模式)
.venv/bin/python -m eval.run_eval data/study/st01/eval/test_set_study_v1_1.yml \
  --retrieval-only --hybrid --study-lookup \
  --collection study_st01 --kb-root data/study/st01/cards
# 联邦复核组 (闸 3)
.venv/bin/python -m eval.run_eval data/study/st01/eval/test_set_study_v1_1.yml \
  --retrieval-only --hybrid --study-lookup --federated
.venv/bin/python -m pytest                      # 799 passed
launchctl kickstart -k gui/$(id -u)/com.sdtmrag.api
```

回滚: 在 `.env` 设 `SDTM_RAG_STUDY_LOOKUP_ENABLED=false` 并重启服务
(此时 study 检索退回纯 hybrid, 联邦路由本身不受影响)。
