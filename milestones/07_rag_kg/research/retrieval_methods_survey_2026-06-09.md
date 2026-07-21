<!-- chain: 07_RAG (Phase 7 RAG+KG 旁枝 / Phase 1.5 检索优化)
  本文件是"全类 src recall ≥95%"方法调研的 evidence 产物.
  关联:
  → ../TODO_retrieval_quality.md §5 (P1 NEXT DIRECTION — 本调研为其方法学输入)
  → ../_progress.json I-4 (检索优化进度)
  → sdtm-rag/eval/ablation_retrieval_2026-06-08.md (前置: 6 次单杠杆实验, 已证 top-15 单杠杆撞天花板)
  产出方式: 9 路并行 multi-agent 调研 (survey + 对抗审查), 主 session 综合. 2026-06-09.
-->

# 检索方法调研 — 把 4 类别**最低分**都拉到 ≥95% 的可行方法

> 日期: 2026-06-09
> 触发: 用户上调目标 — 不再是"平均逼近 100%", 而是 **4 类别每一类的 src recall 都 ≥95%** (最低那类也要过).
> 方法: 9 个检索方法族并行调研 (每族 1 个 survey agent 带 web 检索 + 1 个对抗审查 agent 实地 grep KB 核验), 共 19 agent / 121 万 token / 228 次工具调用.
> 前置: `sdtm-rag/eval/ablation_retrieval_2026-06-08.md` 已证 — cosine top-15 (84.0%) 是强局部最优, 6 次单杠杆 (rerank/multiquery/HyDE/re-chunk) 在 top-15 全部撞天花板.

---

## 0. 一句话结论

**全类 ≥95% 不是靠某一个"神方法", 而是靠一个【路由架构】把 3-4 个各管一类的专用杠杆拼起来。其中性价比最高、零副作用、最该先做的是【确定性查表】(用 KB 里已有的"变量→CT code→术语文件"映射做精确 join, 不靠向量)。**

诚实预判 (详见 §7):
- **single_domain + mixed → ≥95% 把握高** (确定性查表 + 已有的 HyDE, 几乎零风险).
- **cross_domain + concept → ≥95% 有可能但不保证**, 卡在"正确 chunk 排在 cosine 第 30-100 名"这种**排名深度**问题, 需要一个"不降级结构化内容的重排/上下文增强"杠杆, 且至少 1-2 道题 (尤其 concept 的散文定义题) 可能在 top-15 仍救不回来.
- **n=13 的统计陷阱**: 每类只有 13 题, "≥95%" 实际等于"每类最多漏半题" (12/13=92.3% 不及格, 必须 ~13/13). 要让 95% 有统计意义、且确认是修了 pattern 不是补 example, **强烈建议先扩题集** (每类 ≥25 题).

---

## 1. 给非专家的背景 (3 分钟看懂)

**什么是 source recall**: 用户问一个问题, 系统从 4300 个知识片段 (chunk) 里挑 15 个喂给 AI 答题。"source recall" = 这 15 个里**有没有包含标准答案所在的那个文件**。包含了=召回成功。我们要的是 4 类问题每一类的召回率都 ≥95%。

**为什么现在某些类不达标 (3 个病根)**:
1. **排名深度问题** (cross_domain 主病): 正确片段其实**搜得到**, 但排在第 30-100 名, 进不了 top-15。证据: 把 K 放大到 100, cross 召回从 61.5% 涨到 92.3%。—— 这是"排序"问题, 不是"找不到"。
2. **变量名 ↔ CT code 语义鸿沟** (mixed/single 的几道硬题): 用户问"AESEV 的取值", 但标准答案那个片段标题是 CT 编码"C66769", 正文是"轻/中/重", **整段里根本没出现"AESEV"这个词**。向量搜索算的是语义距离, 这俩离得太远, 正确片段连 top-100 都进不去。
3. **VARIABLE_INDEX 信号稀释** (q34 这类"哪些域用了变量 X"): 答案分散在按域切开的 65 个索引片段里, 没有任何单片集中信号, 所以排不上来。

**为什么之前 6 次单杠杆都失败**: 这个 KB 处在"精度/召回前沿"—— 权威答案往往是一条**简洁的结构化片段** (一行变量规格、一个索引条目)。任何**全局**性的换排序/改写/加片段, 一抬难类就把已经 96% 的 single_domain 那条简洁片段挤下去。rerank 把 DM/spec.md 从第 2 名压到第 17 名, 就是这个机制。

**所以出路是"路由"**: 不做全局切换, 先判断这个问题是哪种类型, 再走对应的专用管道。激进杠杆只作用于它擅长的那类问题, 永远不碰简单类。

---

## 2. 9 方法总览评级表

(can_reach_95 = 对抗审查判定"在 top-15 有可能把哪类拉到 95%"; 推荐角色已极度浓缩)

| 方法族 | 一句话是什么 | 能帮哪类到95% | 副作用风险 | 成本/成熟度 | 综合判定 | 推荐角色 |
|--------|------------|--------------|-----------|-----------|---------|---------|
| **① 确定性查表 / 结构化检索** | 用 KB 已有的"变量→CT码→术语文件""变量→域"映射表精确查, 不用向量 | cross_domain, mixed | **零** (union-add, 单独存) | 几小时/$0/无需重建 | ⭐**首选** | **主力**: 救 q34 + q16/s04/s05 (两跳精确 join), 100% 命中 |
| **② Hybrid 混合 (BM25+向量融合)** | 加一路关键词精确匹配, 与向量结果融合 | cross_domain | 低 (加法, 非替换) | 1-2天/$0 (纯CPU)/无需重建 | 🟢 **推荐** | 救"查询与答案共享字面 token"的深位题; 但**救不了** q16/s04/s05 (无共享词) |
| **③ 路由 / 集成架构** | 先分类问题, 再走对应专用管道 | single_domain, mixed | 安全 (隔离 collateral) | 中等/$0/复用现有 | 🟢 **推荐** | **底座 chassis**: 把各杠杆拼起来不互相伤害的唯一方式 |
| **④ Contextual 上下文增强切分** | 嵌入前给片段加一句"它是什么"的说明头 | single_domain, mixed | 低 (选择性注入) | 0.5-1天/几$/需重建 | 🟡 条件 | 备选 mode2/3 解; "更厚的头能进 top-15"**尚未实测证实** (上次注入太简陋停在50%) |
| **⑤ 更强/领域微调 embedding** | 换更好的嵌入模型 / 在 SDTM 上微调 | single_domain, mixed | 安全 (不重排) | 0.5天-数周/需重建 | 🟡 条件 | 先花30分钟试 3-large (大概率没用); voyage-context-3 是有针对性的备选; 微调=最后手段 |
| **⑥ 多向量 ColBERT** | 逐词匹配的重排器, 在 top-100 里重排 | concept | 中 (长度偏好, 同 rerank 病根) | 1天/免费层/无需重建 | 🟡 条件 | 只能救"已在 top-100"的排名深度题; 救不了 q34; 须隔离防伤 single |
| **⑦ 不降级结构内容的 reranker** | 可加指令的重排器 (Voyage 2.5 / LLM listwise) | concept | 中-高 (软指令未必压得住) | 1天/免费层/无需重建 | 🟡 条件 | 只对 concept 的深位题; 须 router 隔离 + single 当 kill-switch |
| **⑧ Learned sparse (SPLADE/ELSER)** | 神经版关键词检索 | mixed, single_domain | 风险 (可能重新污染域内) | 中/换向量库/需重建 | 🟠 弱 | 不值得: 要换向量库 + 重建, 收益多被 HyDE/查表覆盖 |
| **⑨ HyDE (已有, 对照基线)** | LLM 先写假想答案再去搜 | mixed(已100%), concept | 低 | 已实现 | ✅ 保留 | 走 concept/术语路由, 复用已证 +3.7pt |

**最重要的一条认知**: 排前三的 (①②③) 全是"**加法/隔离**"机制 —— 不替换排序、不稀释、不新增竞争片段。这正是它们能绕开前 6 次失败的根本原因。

---

## 3. 推荐架构 — 路由底座 + 4 个隔离杠杆

```
                    ┌─ 用户问题 ─┐
                    │  轻量分类器 │  (sklearn 头 或 haiku/deepseek, 不用本地模型)
                    └──────┬──────┘
        ┌──────────────┬───┴────┬──────────────┐
    域内/spec       分布/关系    术语/CT码      概念/定义
        │              │           │              │
   纯cosine        ①确定性     ①两跳查表     HyDE路由
   (不动它,        查表(域分布) +②BM25      (+⑥/⑦深位重排
    96.4%)         +②BM25union  union        或 ④contextual)
        │              │           │              │
        └──────────────┴── union-add 合并 ──┴──────┘  ← 永远"加候选", 不替换 cosine 排序
                           │
                    top-15 → 答题 LLM
```

**四条铁律** (来自对抗审查的反复强调):
1. **加法不替换** (union-add): 专用杠杆只**追加**候选片段, 绝不重排/替换 cosine 的强命中 → 结构上不可能重演 rerank 的"#2→#17"。
2. **物理隔离**: 索引条目 chunk 单独存 (SQLite/dict 或单独 collection), **不回灌进主 ChromaDB** → 避免 re-chunk v2 的 -1.9pt 污染。
3. **single_domain 当 kill-switch**: 任何杠杆上线前跑 53q retrieval-only, single 掉到 <96% 立即回退。
4. **不用 RRF 分数融合做难易混合**: 本地已证 hyde_rrf 把增益稀释回 baseline (83.0%); 用"池 union + 池内 cosine 排序"或"置信度硬路由 + cosine 兜底"。

---

## 4. 逐病根的最佳解

| 病根 | 最佳解 | 机制 (为什么是真 pattern 不是补丁) | 把握 |
|------|--------|----------------------------------|------|
| **病根2: 变量名↔CT码鸿沟** (q16/s04/s05) | **①确定性两跳 join** | KB 里 spec.md 每个变量都标了"Controlled Terms: C66769"(570 个映射), 每个术语文件 section 标题都是"...(C66769)"。于是 `AESEV →(查spec)→ C66769 →(精确串匹配术语标题)→ ae.md`, **零向量距离, 对所有 CT 变量都成立** (不止这3题)。⚠️ BM25/embedding 救不了, 因为"AESEV"这词**根本不在** ae.md 里 (审查实地 grep: count=0)。 | **高** |
| **病根3: 索引稀释** (q34) | **①确定性查表** | q34 的 gold 就是 VARIABLE_INDEX.md; 索引已编码"变量→{域}"(1523变量全覆盖), 直接按 key 查, 100% 命中, 对任何"哪些域用 X"题同理生效。 | **高** |
| **病根1: 排名深度** (cross 的 q07/08/09/32/33; concept 大多数) | **②Hybrid (共享字面词时)** + **⑥/⑦非降级重排 或 ④contextual (无共享词时)** | 深位题分两种: (a) 查询与 gold 共享字面 token (域码/变量名) → BM25 补一票顶上来; (b) 只共享常见词 (USUBJID/EPOCH) → BM25 无鉴别力, 需逐词重排(ColBERT)/listwise/上下文增强抬内在排名。 | **中** (b 类最不确定) |

---

## 5. 关键发现 (对抗审查实地核验, 推翻了几个 survey 夸大)

1. **【实锤】"AESEV"不在 ae.md, "VSTESTCD"不在 vs.md** (grep count=0)。→ **Hybrid 的招牌宣传(BM25救变量↔CT)对本 KB 是假的**; 同理纯 embedding 升级也救不了 (向量低通滤波抹掉精确码)。唯一真解是**①绕开向量、走 CT code 精确 join**。

2. **【实锤】评分口径放大了某些题的权重**: source recall 是**每题分数制** (命中数/期望源数), 类别分 = 各题均值。q16/s04(mixed)、s05(single) 都恰好 0.5 分 —— spec.md 那半已召回, **永远缺的是术语 CT 文件那半**。所以要把 mixed/single 拉到 95%, 必须把 ae.md/vs.md 这些术语文件顶进 top-15 (= 病根2, 由①解决)。

3. **【关键天花板】即使"完美路由"用现有 3 个杠杆 (cosine/HyDE/re-chunk), 逐题取最优, top-15 天花板 ≈ single 92.9% / cross 84.6% / concept 92.3% / mixed 100%** —— **4 类里 3 类过不了 95%**。结论: **路由是必要的底座, 但光路由+现有杠杆不够, 必须造新的 per-route 火力** (①确定性查表 + 深位重排)。q32/q33/q38/s05 这几题现有任何路由在 top-15 都救不回 (只在 cosine K=100 才出现)。

4. **cross_domain 是两种病的混合**: q34 是关系/分布题 (①查表 100% 解决); q07/08/09/32/33 是纯排名深度题 (①完全无效, 需②/⑥/⑦)。**所以 cross 过 95% 必须两个杠杆叠加, 单个不行。**

5. **concept 全是散文/定义的排名深度** (84.6%→100% @K=100)。其中 **q38**("域缩写码怎么定的", gold=章节) 是纯散文、无稀有词, HyDE/BM25/re-chunk 全失败 —— 这是**最硬的一题**, 决定 concept 能否过 95%。

---

## 6. 建议实验顺序 (便宜→贵, 全程先 retrieval-only 免费验证)

| 步 | 做什么 | 成本 | 预期效果 (per-category) | 风险闸 |
|----|--------|------|------------------------|--------|
| **S1** | **①确定性查表** (变量→CT码→术语文件两跳 join + 变量→域分布查表), 保守 regex 触发, union-add, 单独存 | 几小时-1天 / $0 / 无需重建 | mixed→~100%, single→~100%(救s05), cross +q34 | single 不降即可 |
| **S2** | **②Hybrid BM25+dense** (bm25s 纯CPU, dense-leaning 融合) | 1-2天 / $0 / 无需重建 | cross 补字面-token深位题(q33等); single 必须保持 ≥96% | single<96% 立即回退 |
| **S3** | **③路由 chassis** (sklearn 头 或 haiku 分类器) 把 S1/S2 + HyDE路由 + 纯cosine 隔离拼好 | 中等 / $0 | 锁定 mixed=100/single=96.4 不互伤 | mis-route 用 union 兜底 |
| **S4** | **病根1 深位杠杆** (二选一/都试): (a) ④contextual 选择性注入(术语+索引, 重建); (b) ⑥Jina ColBERT 或 ⑦GPT-4o-mini listwise 在隔离深池里重排, 只对 routed cross/concept | 1天-数天 | cross/concept 的 rank-30-100 题; **make-or-break, 最不确定** | single 当 kill-switch, 掉即弃 |
| **S5** | 若 cross/concept 仍差: voyage-context-3 全量重建(嵌入级抬深位) 或 接受残留 + **扩题集**让 95% 有统计意义 | 数天 | 兜底 | — |

S1-S3 全部 retrieval-only 可测、免费、低风险, 应连做。S4 是真正决定 cross/concept 能否过线的硬骨头。

---

## 7. 老实话 — 能不能保证全类 95%?

**不能打包票, 但分两半看:**

| 类别 | 现状 | 能到95%? | 靠什么 | 把握 |
|------|------|---------|--------|------|
| single_domain | 96.4% | ✅ | 隔离不动它 + ①查表救 s05 | **高** |
| mixed | 92.3% | ✅ | HyDE(已100%) + ①查表救 q16/s04 | **高** |
| cross_domain | 61.5% | ⚠️ | ①查表(q34) + ②/⑥/⑦救深位(q07/08/09/32/33) | **中** |
| concept | 84.6% | ⚠️ | ⑥/⑦非降级重排 或 ④contextual 救深位; q38最硬 | **中** |

**两个必须正视的风险**:

1. **n=13 的统计陷阱 (最该先解决)**: 每类 13 题, 每题 7.7pt, 分数制下 **"≥95%"= 每类最多漏半题** (12/13=92.3% 直接不及格, 实际要 ~12.5/13 以上 = 几乎全对)。这意味着追 95% = **必须逐题修光 cross/concept 现存的每一道失败题**。这正好踩中你一贯警惕的"对症下药 vs 通用机制"红线:
   - ✅ 安全的修法: ①确定性查表、②Hybrid、④contextual 都是**结构性机制** (对所有同型未见问题生效), 不是补 q34 这一题。
   - ❌ 危险的修法: 调分类器阈值"刚好只对那 3 题触发"= 在 53 题上过拟合。
   - **解法: 先把题集每类扩到 ≥25 题**, 95% 才有统计意义, 且"修好"才能证明是 pattern。否则你在 13 题上跑到 100%, 也无法说服自己(或团队)它在真实查询上 ≥95%。

2. **q38 类纯散文深位题可能救不回**: 无稀有词、无 CT 码、gold 是章节散文, 现有任何杠杆都没顶进 top-15。若它(及个别 cross 深位题)在 top-15 始终救不回, 则 concept 封顶 ~92.3%。诚实兜底: 要么接受这一两题(明确口径为"已知失败题清零, 个别散文题除外"), 要么上 voyage-context-3 嵌入级重建赌它抬排名。

**建议的现实路径**: 先做 S1-S3 (便宜、几乎稳拿 single+mixed 两类 95%), 同时**扩题集**; 再用扩充后的题集做 S4 攻 cross/concept。不要在 13 题上宣布胜利。

---

## 8. 排除项 (别再走的路)

| 方法 | 为什么排除 |
|------|-----------|
| 通用 Cohere rerank | 已证死 (80.2%<84.0%, 系统性降级 spec.md) |
| multiquery + RRF | 已证死 (76.4%, 稀释 single 96→78) |
| hyde_rrf 分数融合 | 已证死 (83.0%, 把增益稀释回 baseline) |
| re-chunk 全量回灌主库 | 已证 -1.9pt (222 索引 chunk 污染域内查询); 改为**单独存 + 路由** |
| Learned sparse (⑧) | 要换向量库 + 全量重建, 收益多被 ①查表/HyDE 覆盖; 且 SPLADE 子词切分会把"C66769"切碎; 不值得 |
| 纯 embedding 升级救病根2 | 向量低通滤波结构上抹掉精确码, 3-small→3-large 仅 +2.33 MTEB, 太小; 救不了变量↔CT |
| 全量 LLM contextual (不选择性) | 变成无隔离的全局开关, 有 within-chunk 稀释风险伤 single; 必须**选择性**注入 |
| Late chunking | 需 token 级嵌入 + 自定义池化, OpenAI embedding API 不暴露, 被云端约束排除 |
| 本地模型 (任何) | 用户已定: 两次崩溃, 只用云端 API |
| 完整 LLM GraphRAG (微软式) | 过度工程: 关系已是干净表格 (VARIABLE_INDEX), 无需 LLM 抽图; 用①轻量查表即可 |

---

## 附录 A — 9 族对抗审查浓缩

| # | 族 | can_reach_95_on | skeptic判定 | 预期影响 | 一句话角色 |
|---|----|-----------------| ------------|---------|-----------|
| ① | 确定性查表/图 | cross_domain, mixed | conditional | **high** | 关系/CT码题的主力, 零副作用, 先做 |
| ② | Hybrid BM25 | cross_domain | conditional | **high** | 字面-token深位题; 救不了无共享词的q16/s04/s05 |
| ③ | 路由架构 | single_domain, mixed | conditional | **high** | 整合底座, 必要但不充分 |
| ④ | Contextual切分 | single_domain, mixed | conditional | medium | mode2/3备选; 富头进top-15未实测 |
| ⑤ | 强/微调embedding | single_domain, mixed | conditional | medium | 先试3-large(估没用); voyage-context-3备选 |
| ⑥ | ColBERT多向量 | concept | conditional | medium | top-100内深位重排; 救不了q34; 长度偏好风险 |
| ⑦ | 非降级reranker | concept | conditional | low | 只concept深位; 软指令未必压住偏见 |
| ⑧ | Learned sparse | mixed, single_domain | conditional | medium | 不值得(换库+重建) |
| ⑨ | (HyDE基线) | mixed, concept | recommend | — | 走concept/术语路由保留 |

## 附录 B — 核心来源 (按方法族)

- **确定性查表/图**: [When to use Graphs in RAG (GraphRAG-Bench, arXiv 2506.05690)](https://arxiv.org/html/2506.05690v3); [FalkorDB/Diffbot KG-LM benchmark (vector RAG ~0% on aggregation)](https://www.falkordb.com/blog/graphrag-accuracy-diffbot-falkordb/); [Retrieval for structured data: precision-first (embedding swamping)](https://medium.com/@alejandro.r.amaro/retrieval-for-structured-data-a-precision-first-alternative-to-vector-only-rag-on-tables-388444816379)
- **领域词典扩展**: [Query2doc (EMNLP 2023, arXiv 2303.07678)](https://arxiv.org/abs/2303.07678); [Ontology-Guided Query Expansion for Biomedical (arXiv 2508.11784)](https://arxiv.org/pdf/2508.11784); [CDISC CT = NCI EVS C-codes](https://www.cdisc.org/kb/articles/controlled-terminology-faqs)
- **Hybrid/BM25**: [T2-RAGBench: From BM25 to Corrective RAG (arXiv 2604.01733)](https://arxiv.org/html/2604.01733v1); [Fusion Functions for Hybrid Retrieval (Bruch, ACM TOIS 2023)](https://dl.acm.org/doi/10.1145/3596512); [DAT Dynamic Alpha Tuning (arXiv 2503.23013)](https://arxiv.org/html/2503.23013v1); [bm25s (arXiv 2407.03618)](https://arxiv.org/pdf/2407.03618)
- **路由**: [Adaptive-RAG (NAACL 2024, arXiv 2403.14403)](https://arxiv.org/abs/2403.14403); [RAGRouter-Bench (router 93.2% acc, arXiv 2604.03455)](https://arxiv.org/html/2604.03455v1); [Tier-Based Adaptive Query Routing (arXiv 2604.14222)](https://arxiv.org/html/2604.14222v1); [RouterRetriever (AAAI 2025, arXiv 2409.02685)](https://arxiv.org/abs/2409.02685)
- **Contextual**: [Anthropic Contextual Retrieval](https://www.anthropic.com/news/contextual-retrieval); [ConTEB/InSeNT (HuggingFace)](https://huggingface.co/blog/manu/conteb); [Claude Cookbook — Contextual Embeddings](https://platform.claude.com/cookbook/capabilities-contextual-embeddings-guide)
- **Embedding**: [voyage-context-3](https://blog.voyageai.com/2025/07/23/voyage-context-3/); [voyage-3-large](https://blog.voyageai.com/2025/01/07/voyage-3-large/); [Harvey×Voyage custom legal embeddings](https://www.harvey.ai/blog/harvey-partners-with-voyage-to-build-custom-legal-embeddings); [CLEAR lexical-gap (arXiv 2004.13969)](https://arxiv.org/pdf/2004.13969)
- **ColBERT**: [answerai-colbert-small](https://www.answer.ai/posts/2024-08-13-small-but-mighty-colbert.html); [ColBERTv2 (arXiv 2112.01488)](https://arxiv.org/pdf/2112.01488); [White Box Analysis of ColBERT (arXiv 2012.09650)](https://arxiv.org/pdf/2012.09650); [Late interaction length bias (arXiv 2603.26259)](https://arxiv.org/html/2603.26259v2)
- **Reranker**: [Drowning in Documents (arXiv 2411.11767)](https://arxiv.org/html/2411.11767v2); [Voyage rerank-2.5 instruction-following](https://blog.voyageai.com/2025/08/11/rerank-2-5/); [Contextual AI instruction-following reranker](https://contextual.ai/blog/introducing-instruction-following-reranker)
- **Learned sparse**: [Pinecone sparse (whole-word, terminology-heavy)](https://www.pinecone.io/learn/learn-pinecone-sparse/); [Elastic ELSER](https://www.elastic.co/docs/explore-analyze/machine-learning/nlp/ml-nlp-elser)

---

> 完整 9 族 survey + applicability 原始结构化数据 (含每族 mechanism / evidence / collateral 详述) 见 workflow 产物:
> `/private/tmp/.../tasks/wa4xosgbe.output` (142KB JSON, 已读入本报告; 如需归档可另存 evidence/)。
