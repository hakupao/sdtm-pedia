<!-- chain: 07_RAG (Phase 7 RAG+KG 旁枝 / Phase 1.5→P1 检索优化) -->

# RETROSPECTIVE — P1 查询条件路由 (全类 src recall ≥95% 达成)

> 日期: 2026-06-09 (单 session)
> 目标: eval 4 类别**最低分**也 ≥95% src recall (用户 2026-06-09 上调; 前一日 2026-06-08 单杠杆 round 结论是"接受 baseline 84.0%")
> 结果: **达成 (retrieval-only, v2 102 题)** — single 100% / cross 96% / concept 100% / mixed 100% / overall 99.0%。唯一残留 q73 (cross, gold model/06)。独立复跑验证 (main session, 非 writer)。
> 上游: 方法调研 `research/retrieval_methods_survey_2026-06-09.md` (9 方法族 multi-agent 调研) → 实施。

## 达成路径 (4 杠杆组合, 全在"检索逻辑"层, 未碰源/向量索引/提示词)

| 杠杆 | 机制 | 贡献 |
|------|------|------|
| S1 确定性查表 | 非向量通道: 变量→CT码→术语文件 两跳精确 join + 分布查询→VARIABLE_INDEX | single+mixed → 100% (救术语/分布题) |
| 分布意图泛化 | query 含变量名+"domains"+用法动词 → 注入 VARIABLE_INDEX (通用 pattern) | cross 76→96% |
| Hybrid BM25 | 新增关键词索引 (从现有 chunk 文本免费建) + RRF 加法融合 | concept 92→100%; 救字面 token cross |
| 路由隔离 + s3 长名映射 | 激进杠杆只对其擅长类生效; 域长名→码兜住长名 single | hybrid 单独砸 single 96→83, 组合后稳 100 |

## §1 保留下来的做法 (有效, 继续用)

1. **先调研后动手 (workflow 调研 → 定方法 → 再 build)**: 9 方法族并行调研排出"确定性查表 = 头号性价比", build 直接执行头号推荐, 一刀 2 类打满 100%。比"在向量路上瞎调参"高效得多。
2. **对抗审查实地 grep KB**: 推翻了调研 survey 的招牌宣传 (BM25 救"AESEV"是假的——AESEV 根本不在术语文件里), 挖出真解 (走 CT-code 两跳精确 join)。结构检查 ≠ 语义检查, 必须真读数据。
3. **加法 + 路由 = 绕开 precision/recall 前沿的唯一设计**: hybrid 单独把 single 砸到 83% (前沿警告实测复现), 但"加法不替换 + S1 确定性 prepend + 路由隔离"让组合稳在 100%。**任何全局切换都会帮一类伤另一类; 路由让每个杠杆只碰它擅长的题**。
4. **Rule D 隔离 + 反过拟合证据**: writer (executor) ≠ reviewer (code-reviewer) 异 type; 反过拟合不靠嘴说——用 8 个测试集外变量泛化探针 + "在从没见过的新题上救回 6 道" 实证。
5. **题集扩充对杠杆设计盲 + genuine mixed**: 出题 agent 不知道 S1 怎么设计 (防为杠杆量身定制); mixed 升级为"必须问具体取值"才真考跨源。
6. **每杠杆 single 当 kill-switch**: 任何改动 single 跌破阈值即弃 (s3 带零回退硬 gate)。

## §2 必须补上的缺口 (下次/后续)

1. **q73 残留** (cross 24/25): RDOMAIN 分布题 gold 是定义它的 `model/06`, 分布路由注入了 VARIABLE_INDEX、hybrid 没把 model 章节顶进 top-15。通用补法 = "变量→定义它的 model 文件"通道, 但有 example-patching 风险, 留作已知残留 (cross 仍 96% 达标)。
2. **n=25 余量**: cross 96% = 24/25 是 1 题 margin。即使 n=25, "≥95%"也等于"最多漏 1 题"。要 bulletproof 需再扩题集。
3. **s3 长名边界在 v2 上未被实测**: v2 single 题全用域码, 长名映射是防御 (6 探针验证) 但 no-op on v2。应补几道长名 single 题真正 exercise 它。
4. ✅ **full eval 已跑 (2026-06-09)**: DeepSeek temp=0 配对 OFF/ON v2 102q — src 80.9→99.0%, fact 96.3→95.2% (噪声带内持平, 全类 ≥95% 除 cross 92.7%=substring 假阴)。Rule A 语义裁判 KB 核验: 净中性偏正, 但抓到 3 例真稀释 (q02/q37/q93)。详 `sdtm-rag/evidence/checkpoints/prod_wirein_summary.md`。
5. ✅ **已接入生产 /ask (2026-06-09)**: `config.py` 两杠杆默认开 (env 可关) + `main.py` 转发 + embed-once 重构 (S1 多次 query 嵌入→1) + q02 修复 (单域 spec 注入 4 chunk)。延迟 +14ms/查询 + 0.5s 一次性启动。Rule D 代码审 APPROVE_WITH_NITS。
6. **代码未 commit**: 在 main 工作树 validated + 全闸过, 待用户"收尾"入库。
7. **新残留 (full eval 暴露, 已 ack 不修)**: q100 (多变量具体单域问广度) / q37+q93 (答题侧, 提示护栏 declined) / C-code 幻觉 (off+on 通病)。详 prod_wirein_summary.md §残留。

## §3 关键决策复盘

1. **从"接受 baseline 84%"到"追全类 95%" (隔一天反转)**: 值。前一日"单杠杆做不到"的结论是**对的**——答案不是更好的单杠杆, 是**多个路由杠杆**。之前所有人 (含我) 都在调向量路 (rerank/HyDE/re-chunk), 而真正的解锁是**一条非向量通道** (确定性查表): RAG 不需要更强的 embedding, 它需要给"结构化事实查询"一条不走向量的路。
2. **确定性查表是最高 ROI**: 零成本 (KB 现成对照表)、零副作用 (union-add)、2 类直接 100%。教训: 当答案以**结构化形式**已存在于 KB (对照表/索引), 别让向量去"猜", 直接查表。
3. **Hybrid 必须路由/加法, 绝不全局**: 实测印证研究的前沿警告 (hybrid 单独 -overall, 砸 single)。
4. **RRF (无参) 优于 weighted alpha**: 既最优又零 alpha 过拟合风险。

---

> 证据链: `research/retrieval_methods_survey_2026-06-09.md` (调研) + `sdtm-rag/eval/ablation_t1/v2_*.json` (消融矩阵 raw) + `sdtm-rag/evidence/checkpoints/s{1,2,3}_*.md` (实施 + result) + `s{1,2}_rule_d_review.md` (Rule D 独立复核) + `evidence/failures/s2_attempt_1.md` (规则 B)。
