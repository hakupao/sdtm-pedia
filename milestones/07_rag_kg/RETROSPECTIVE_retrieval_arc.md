# 检索质量弧线 — 总 Retrospective (Phase 1.5 → P1 → S4 → (d) → KG 关闭)

> 创建: 2026-06-15. 范围: Phase 1 CLOSED (2026-05-24) 之后整条"检索质量"工作线的复盘
> (单杠杆 round → P1 路由 → 接入生产 → 答题护栏 → 题集 v3 → S4 → S4 尾账 → (d) 双通道 → KG 关闭)。
> 配套: `RETROSPECTIVE_P1_retrieval95.md` (P1 专题) + 各 `evidence/checkpoints/*.md`。
> Rule C 三段: 保留下来的做法 / 必须补上的缺口 / 关键决策复盘。

## 结果总览 (起点 → 终点)

| 指标 | Phase 1D baseline (2026-05-24) | 终态 (2026-06-15) |
|------|------|------|
| retrieval-only src recall — single | 96.4% | **100%** |
| — cross_domain | **61.5%** | **99.0%** |
| — concept | 76.9% | **100%** |
| — mixed | 92.3% | **100%** |
| 题集规模 | 53q | **140q** (v3, cross 扩到 50) |
| 端到端 full eval src (DeepSeek temp=0) | — | OFF 76.4 → **ON 97.5** |
| 端到端 fact recall (substring) | 94.8% (53q) | 82.6% (140q, substring 假阴重) |
| 端到端 fact recall (语义 LLM-judge, 140q/466 facts) | — | **93.9%** (concept 100/cross 93.5/mixed 92.0/single 91.7; 替代误导性 82.6% substring) |
| Phase 2 KG | deferred (gate 61.5%>50%) | **正式关闭** (cross 99%, gate 远不满足) |
| 部署 | 仅本地 venv | Docker Compose 修复/加固 + 实服 e2e 证过 (容器构建待 Docker 主机) |

**一句话**: 跨域召回从 61.5% 拉到 99%, 全类 ≥99%, 全程**未碰源数据/向量索引/答题模型选型**, 只在检索逻辑层加确定性路由通道 + 答题侧 grounding 护栏。

## 1. 保留下来的做法 (有效, 下个项目继续用)

1. **retrieval-only 先行, full eval 把关**: src recall 是检索器的活, 免费可跑无数轮; 先用 retrieval-only 快速迭代杠杆, 只在收口用带答题模型的 **配对** full eval (OFF vs ON, 同模型同题) 验"答案不被注入稀释"。配对 Δ 是闸, 不是绝对值。
2. **按查询类型路由, 不做全局切换**: 单杠杆 round (2026-06-08) 6 次实验证明每个全局杠杆都"帮某类伤另类", cosine top-15 是强局部最优。出路是**按意图路由**, 让每个杠杆/通道只对它擅长的类生效 (S1 查表 / 分布意图 / hybrid / 长名 / (d) 概念定义), kill-switch + union-add 隔离 collateral。
3. **确定性通道补向量盲区**: 变量→CT码→术语文件、变量→model 定义文件、--前缀→ch04 —— 这些 gold 的标题是 CT 码或概念, 变量名根本不出现, embedding+BM25 都瞎; KB 结构里却是确定可 join 的。确定性查表 (union-add, 只增不删) 是这类的对症解。
4. **union-add 语义 = 召回可加、零删除**: 新通道只追加 gold 文件到候选集, 永不移除。最坏是 top-15 尾部挤压 (零回归 gate 实测可控), 不会把对的答案换成错的。这是敢于加通道的安全底座。
5. **pattern-level 强制 + held-out 探针证泛化**: 每条通道都用 KB 结构驱动 (零题号/变量名硬编码), 并用**题集外**探针 (应触发 + 应静默) 证明它泛化到整类问题, 而非拟合到那一道题。这是区分"真 pattern"与"例级作弊"的决定性证据 (q126 正因探针真阳集=单例而被判 defer)。
6. **Rule D 异 type 隔离 + 对抗式裁判**: writer (改检索) ≠ reviewer (跑 eval/裁判), 不同 subagent_type。掉分用独立 scientist 逐题 KB 语义裁判 (非 substring), 代码用 code-reviewer。多次抓到主 session 眼检漏掉的真问题 (护栏 v1 漏穿、6 列形状才是真判别器)。
7. **多-agent Workflow 做分诊/调研/裁判**: 9 方法族调研、(d) 三题并行分诊+over-fire、11 掉分语义裁判、140q LLM-judge —— 可并行的发散/核验工作交 workflow, 主 session 留结论与决策。
8. **失败归档不删 (规则 B)**: 护栏 v1 FAIL、各 ablation 全留, 是重跑和复盘最贵的资料。

## 2. 必须补上的缺口 (本线未做完 / 已知限制)

1. **q126 (无实体锚概念对比)**: 永久 known limitation。两重独立阻断 — 题面零实体锚 (区分性短语 140q 中恰命中自己=例级作弊) + **架构阻断** `domain_to_spec` 只映 spec.md, 但 q126 SE gold=assumptions.md。**要做先给 structured_lookup 加 domain sub-file (assumptions/examples/spec) 判别能力** (架构件), 再谈概念→sub-file 路由。
2. **fact recall 评测口径**: substring 法对 paraphrase/同义/数字异形/码 fabrication **结构性盲** (82.6% 是假象)。✅ **已补**: 语义 judge 固化进 `run_eval.py --judge` (2026-06-15, Rule D code-reviewer 抓修 HIGH 静默膨胀 bug); 报 substring(次)+judge(主), verdict 用 judge, 解析失败计数回退。下次报 fact recall 一律用 `--judge`。收口 `evidence/checkpoints/llm_judge_fact_recall.md`。
3. **跨模型 eval**: Sonnet/Opus 自 Phase 1D 起被 Anthropic credits 耗尽 block; 全线只在 DeepSeek 上验。credits 补足后应补跑确认结论稳健。
4. **答题侧残留**: q93 (值名 INJECTION vs INJECTABLE) / q96 (标准值未检索) = 检索覆盖 artifact; per-value C-code 右归属只 bundle spot-check。属护栏范围外的答题侧个例。
5. **容器实测**: Docker 本机不可用, 容器构建 (`docker compose up --build`) 未在本环境跑过 (artifacts 已修+静态校验+实服 e2e 证内容)。需在 Docker 主机首次实跑确认。
6. **q57 类前沿 tradeoff**: structured_lookup 给"描述某域"单域问注入 spec×4, 可能挤掉 assumptions 的叙述事实。单题级 (CLEAN_CLOSE 裁判), 但属 top-15 预算固有前沿, 记录不反应式修。

## 3. 关键决策复盘

- **D1 不追"更好的单杠杆", 改追"多个路由杠杆"** (2026-06-09): 隔日反转前一日"接受 baseline 84%"。事后看是全线最关键的方向转弯 —— 答案不是某个银弹杠杆, 是一组各管一类的路由通道 + 一条非向量确定性查表。
- **D2 S4 尾账坚持跑 full eval** (2026-06-15): S4 retrieval-only 已过, 但 union-add 改了检索组成, 必须带答题模型验稀释。结果 CLEAN_CLOSE (净 −0.2pt 带内, 11 掉分 10=假阴/非确定+1 已知前沿)。**没有这一步就不能说 S4 端到端安全。**
- **D3 推翻 workflow 对 q119 的 defer** (2026-06-15): 综合 agent 称 q119 与 q114 锚不可分→defer; 主 session 独立复核发现两题**意图可分** (比较 vs 用法), 据此建成通道。教训: **subagent 的"不可行"结论要复核其依赖的关键事实**, 别照单全收。
- **D4 q126 诚实 defer 而非硬做** (2026-06-15): 能做出只触发 q126 的规则, 但那就是 q126 硬编码 (用户敏感点)。选择 defer + 记录架构前置, 而非为一道题污染通道。**"做不到"也是一种交付** (把不可达性钉死)。
- **D5 正式关闭 Phase 2 KG** (2026-06-15): gate (cross<50%) 因路由通道把 cross 拉到 99% 而决定性不满足。把长期"deferred/未决"转为"已决: 检索质量不需要 KG, 重启需新立项"。避免悬而未决的技术债。
- **D6 护栏与检索正交且组合后码 grounding ~100%** (belt-and-suspenders): guardrail-OFF 隔离 S4 检索变量是对的实验设计; 但补跑 guardrail-ON+S4 确认了生产真实配置 (287 码 1 mis-cite 0 fabricated)。

## 现状一句话

**检索质量目标 (全类 src recall 逼近 100%) 已达成 (cross 99%, 余下 q126 单题架构受限)。** 这条线进入"已收口"状态: 生产默认开全部杠杆+护栏, 部署 artifacts 就绪, KG 关闭, 评测口径缺口 (语义 judge 固化) 与跨模型 eval 为下一迭代候选, 非阻塞。
