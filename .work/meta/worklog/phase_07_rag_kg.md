# Phase 07 RAG+KG (branches/07_rag_kg/) — 工作日志

> Phase 7 (RAG + Knowledge Graph) 旁枝 entries. PLAN 在 `branches/07_rag_kg/PLAN.md` + EXECUTION_PLAN 在 `branches/07_rag_kg/EXECUTION_PLAN.md` + 上游设计 `docs/DESIGN_RAG_KG.md`.

> **新 entry** append 到本文件 (按日期顺序), 保持 H2 标题 `## YYYY-MM-DD <topic> <verb>` 格式.

---

## 2026-05-22 branches/07_rag_kg/ Phase 0 Research CLOSED (调研 + PLAN v0.2 + critic Rule D PASS 1 + 用户 ack)

- **触発**: 用户「Phase 7 RAG+KG 启动」(2026-05-22), 指示「先调研+写方案, 尽量保证不返工」+ LLM 配置 (DeepSeek V4 Pro + ChatGPT Plus 代理 + Anthropic API 接口预留)
- **完了の作業**:
  - **STEP A 仓库骨架** (T1): `branches/07_rag_kg/` 创建 (PLAN.md / EXECUTION_PLAN.md / CHANGELOG.md / _progress.json / research/ / evidence/checkpoints/ / evidence/failures/ / prompts/). Tier 2 schema _progress.json
  - **STEP B T2 LLM 调研 (background document-specialist)**: WebSearch 调研 DeepSeek V4 Pro / ChatGPT Plus 代理 / Anthropic 2026 模型 / LiteLLM 兼容性. 落档 `research/llm_providers_2026-05-22.md` (含决策表 + 6 个 [UNVERIFIED] + Sources 18 个 URL)
  - **STEP C T3 chunker feasibility 调研 (main session 直接)**: KB 真实 grep — 296 md / 64 domain (DI 仅 assumptions Issue 15 修复后加) / 2164 spec.md 变量 / 1005 codelists / lb_part1-4 / VARIABLE_INDEX 63 H3 / PC examples 14 H4 / TA 20 mermaid / ch04 130KB. 落档 `research/chunker_feasibility_2026-05-22.md` (含 7 风险 R-1~R-7 + Phase 1A.0 6 [UNVERIFIED] + 5 chunker 实现规范)
  - **STEP D PLAN.md v0.1 + EXECUTION_PLAN.md v0.1 起草** (main session writer, 整合 T2 + T3): 5 处偏离设计 (A-1 examples domain-aware + A-2 INDEX 整体注入 + A-3 LLM 默 Sonnet + B-1 eval 提前 + B-2 KG defer gate); Phase 1A-1D + Phase 2 拆分; 12 决策表 (LLM/embedding/framework/chunker); 21 风险表 R-1~R-12; PASS 五条 + 工期 10-13 d (v0.1)
  - **STEP E critic Rule D PASS 1** (foreground): `oh-my-claudecode:critic` subagent 派发 (writer=main session 异 type), 审 PLAN + EXECUTION_PLAN + 2 research + 上游 design doc + CLAUDE.md. ADVERSARIAL 模式触发 (因第 1 处事实错误 lb_part4 漏列 surface). Verdict = **CONDITIONAL_PASS**, 32 findings (3 HIGH / 7 MED / 6 LOW / 4 INFO). 落档 `evidence/review_pass_1.md`
  - **STEP F v0.1 → v0.2 修订** (main session writer): 31 处 Edit 跨 3 文件
    - chunker_feasibility 10 处 (F-2 4 事实 + §0 TL;DR 数字 + §1 KB 表 + §6 LB part4 + §8 VARIABLE_INDEX H3 + §13 supplementary_part 命名 + §9 总数表)
    - PLAN 12 处 (F-1 PASS 术语 + F-2 §3/§6.5 同步 + F-3 R-13~R-21 加 + F-4/5 evidence 说明 + F-19/20/21 工期 + F-23 PASS 按 Phase + F-24 规则 A 抽检 N + F-27 1C reviewer.py + F-32 06 P7 表述)
    - EXECUTION_PLAN 9 处 (F-6 V4 Pro 非思考 + F-8 1A.2.d-e + F-11 1A.1.c-d + F-22 §9 注解 + F-25 main session 注 + F-23 §11 Per-Phase PASS 五条 + Phase 1A.0 sanity step)
  - **STEP G 5 LOW 当场修** (用户 ack 后):
    - F-12 (100MB 上限 + chunksize) — v0.2 主修订时 PLAN §5 1C.1 已含
    - F-13 (单用户/单租户) — PLAN §0.2 Out-of-scope 加明示
    - F-15 (metadata null vs omit) — PLAN §7 metadata schema 加 F-15 注释
    - F-16 (pyreadstat fallback) — EXECUTION_PLAN 1A.1.d 已含
    - F-17 (Streamlit timeout UX) — PLAN R-21 已含
  - **STEP H 顶层文档同步**:
    - `.work/MANIFEST.md`: 加 Chain 07_RAG + Plan Map 加 1 行 + Quick Ref 加 1 行
    - `CLAUDE.md` Key Paths: 加 1 行 (≤ 80 字符)
    - `docs/PROGRESS.md`: Phase 7 状态 ⏸ → 🟢 + milestone 列加 2026-05-22 entry
    - `.work/meta/worklog/INDEX.md`: 加 phase_07_rag_kg.md 行
    - `.work/meta/worklog/phase_07_rag_kg.md`: 新建本文件
  - **STEP I single commit + push**: Phase 0 closure
- **関鍵決定 (用户全 ack 2026-05-22)**:
  - **D-1**: 仓库布局 `branches/07_rag_kg/sdtm-rag/` (跟 SDTM-pedia git 一起, 不开 sibling 项目)
  - **D-2**: LLM 主力 = `claude-sonnet-4-6` 主答 + `deepseek-v4-flash` 复检 (非思考模式绕 LiteLLM Issue #26395) + `claude-opus-4-7` 难题 + `claude-haiku-4-5` 轻分类
  - **D-3**: ChatGPT Plus 代理**不入生产** (违反 OpenAI ToS + 极低稳定性 + 数据安全风险), 仅在 chatgpt.com 网页用 Plus 配额做 prototype, LiteLLM 留 `openai/` base_url 接口供后续独立 OpenAI API 账户接入
  - **D-4**: Embedding = OpenAI `text-embedding-3-small` (1536d, 全 KB embedding 约 $0.01) + bge-m3 local fallback
  - **D-5**: Phase 2 KG **默认 defer**, 启动 gate = Phase 1D eval RELATION 类 12 题召回 < 50% (50% 阈值 1D 后用户 + main 复评, 不锁死)
  - **D-6**: chunker 三策略 — (a) examples.md domain-aware (探测最深 heading level, PC H4 嵌套 14 chunk 不是 16) + (b) chapters size-aware (>50KB → ### / 20-50KB → ## / <20KB → 整文件) + (c) terminology LB part 模式识别 (part1-3 各 1 codelist + part4 含 2 codelist 异常)
  - **D-7**: ROUTING.md (2K tok) + INDEX.md (4K tok) 都整体注入 system prompt (~6K base, 给 LLM 64 域 + 6 chapters + 91 terminology 入口映射)
  - **D-8**: Eval 提前 — Phase 1B5 sanity (20 题) 在 ingest 后立刻跑, Phase 1D 全 eval (50 题) 留收口前; 避免最后才发现召回拉胯
  - **D-r522-1 critic Rule D PASS 1 ADVERSARIAL 触发**: critic 在 spot-check 第 1 处事实错误 (lb_part4 漏列) 后升级 ADVERSARIAL 模式, 重新独立 grep 验证所有数字, surface F-2 系统性 evidence-vs-claim drift (4 处). 教训: chunker feasibility 类 evidence 文档下次写时, main session 自己 grep 后必须等 critic 异 type 再做 1 轮独立 grep verify
  - **D-r522-2 Phase 0 → Phase 1A.0 sanity 强制 gate**: PLAN.md v0.2 新增 Phase 1A.0 step (re-grep verify R-13 6 项 [UNVERIFIED]), 不信任 chunker_feasibility 估算; 6 项落实到 `evidence/checkpoints/phase_1a_0_sanity.md` 才进 1A.3 chunker writer
- **Carry-over for next session**:
  - **NEXT**: Phase 1A.0 sanity re-grep verify (supplementary_part / qs_part / questionnaires 43 文件 H2 / mermaid 嵌套 / 表格变体 / tiktoken 实测) — 工期 0.3 d
  - **その後**: Phase 1A.1 仓库脚手架 `branches/07_rag_kg/sdtm-rag/` 起 → 1A.2 LiteLLM v1.85.1 sanity (5 sub-step 含 R-8/R-14/R-19 验证) → 1A.3 chunker 6 类 fan-out 3 batch 并列 → 1A.4 chunker 测试套件 → 1A.5 ingest 全量 + Chroma backup → 1A.6 规则 A 抽检 (06 P5 reverse_ledger N=10 atom)
  - **Phase 2 deferred** (gated): KG 启动条件 = Phase 1D eval RELATION 召回 < 50%
  - **PASS 五条 Open**: 全 PASS for Phase 0; Phase 1A PASS 待 1A.6 完成
- **下一步**: commit + push (Phase 0 closure single commit)

---

## 2026-06-08 Phase 1.5 检索优化 round 完成 — 单杠杆全测, 接受 baseline

- **触発**: 用户「帮我开始」执行 I-4 检索优化 backlog (`TODO_retrieval_quality.md`, 目标全 4 类别 src recall > 95%)
- **方法**: workflow 并行侦察 (sdtm-rag eval 框架 + 检索代码 + baseline + 运行就绪) → 逐杠杆实验 → 每步独立 Rule D (异 subagent_type) → evidence 全留 (规则 B). retrieval-only 模式跑 src recall (与答主 LLM 无关, 免费)
- **完了の作業 (6 次实验, 全归档 `sdtm-rag/eval/ablation_retrieval_2026-06-08.md` 4 部分 + `ablation_t1/*.json` raw)**:
  - **T1 Top-K 扫描 (诊断)**: 加 `run_eval.py --top-k` flag. K=15→100 cross_domain 61.5%→92.3% = **排序问题非表示问题**; K=100 天花板 95.3%. **副产物: 全量审计 53 题 expected_sources, 修复 q37 gold-label bug** (`model/04_special_purpose.md` 不存在 → `03_special_purpose_domains.md`). Rule D verifier 独立重算 PASS + 抓到把 ae/vs 误归因"截断"(实为语义距离) 的错
  - **T2 Cohere rerank — ❌ FAILED**: 实现宽召回→rerank pipeline (rag.py, 默认 off) + Rule D code-review CONDITIONAL PASS (2 HIGH 修: 429 重试 + copy 防污染). 实测全 pool 80.2% < baseline 84.0%; rank-tracing 证实通用 reranker 系统性降级 spec.md (q08 cosine#2→rerank#17)
  - **T4 multiquery — ❌ FAILED** (76.4%, 4列表 RRF 稀释单域); **T4 HyDE — 最佳 +3.7pt** (87.7%, mixed 100%, single 回退 1 题, cross 仅 69.2%); **T4 hyde_rrf — ❌** (83.0% 融合稀释回 baseline). 全实现在 rag.py 默认 none
  - **re-chunk 4 硬核 — partial, net -1.9pt**: cosine-sim 廉价验证 (候选 chunk 0.77/0.78/0.58 均进 top-15) → 委托 executor 实现 (§一 24-row→per-var, §三 135-row→per-CT-code, terminology 注入"Used by 域.变量"; VARIABLE_INDEX 65→222 chunk; pytest 216 PASS) → Rule D code-review CONDITIONAL PASS (4 必修全应用) → 修 ingest.py embed 429 重试 bug (重 ingest 撞 OpenAI TPM 崩溃, R-16 备份救回) → 重 ingest 4303 chunk → eval. 修好 q07/q34 (cross 61.5→76.9%) 但 222 索引 chunk 在域内查询挤占 spec.md (q02/q13/q43 回归); terminology 注入太简短未修 q16/s04/s05
- **結論 (铁律)**: 每个单一检索杠杆都帮某类伤另类; cosine top-15 baseline (84.0%, single/mixed 92-96%) 是强局部最优; **全类 95% @ top-15 单杠杆做不到 (已证, 非没找对方法)**. 唯一未来路径 = **P1 查询条件路由** (各杠杆只对其擅长类生效, 需 query classifier) 或接受 baseline
- **用户决策 2026-06-08**: 接受 baseline. live collection 恢复 v1 (4146 chunk, `data/chroma_backup_20260608T104724Z/`); 全实验代码保留 (默认 off + chunker Rule D 通过) 供未来 P1 复用
- **Rule D 教训**: verifier 抓到 2 处 main 的事实/归因错误 (q37 gold-label bug 连带发现 + ae/vs 截断误判) — 再次验证 chunker/检索 evidence 类工作 writer≠reviewer 隔离的价值 (呼应 D-r522-1)
- **下一步**: commit (单 commit) + push; 若未来追 95% → P1 查询条件路由 (新 backlog)

---

## 2026-06-09 P1 杠杆接入生产 + 端到端验证 DONE (用户 ① 第一优先)

- **触発**: 用户「① 第一优先 — 把杠杆接进生产 + 端到端验证(把数字变成真能力)」: structured_lookup+hybrid 从 eval flag → `/ask` 默认开; 跑带答题模型 full eval 确认 fact recall 不被噪声稀释 (真闸非走过场); 测延迟 (BM25 建索引 + 查表开销)
- **方法**: 主 session 实读全代码 → wire-in (writer=main) → 客观回归闸 + 独立 Rule D 代码审 → 配对 full eval (temp=0) + 独立 Rule A 语义裁判 → 修 q02 → 重验 → 收尾. evidence 全留 `sdtm-rag/evidence/checkpoints/prod_wirein_*.md` + `eval/prod_wirein/`
- **完了の作業**:
  - **接入生产**: `config.py` `structured_lookup_enabled=True` + `hybrid_enabled` 翻 True (均 `SDTM_RAG_` env 可关); `main.py` lifespan 转发 5 杠杆参数 + 计时 + log 杠杆态 + **hybrid-on-without-S1 守卫 warning** (Rule D M-1); `router.py` `/info` 暴露杠杆态
  - **embed-once 重构** (`rag.py`): query 原文嵌一次复用 (`_embed_query` + `_search(query_embedding=)`), S1 多次 lookup 重嵌 (最多 ~6 往返) → 1; 实测 2-target query embedding 调用 3→1; retrieval-only 逐题字节一致 (embedding 确定性)=行为保持; `_embed_query` 加 429 退避 (Rule D M-2)
  - **q02 修复** (`rag.py`): S1 resolve() 恰返回单个域 spec.md (纯单域查询) 时注入该文件 4 chunk (非 1), `_SINGLE_DOMAIN_SPEC_CHUNKS=4`, 最窄触发; q02 33→67 (枚举出变量表; 残留 miss=gold 标错 RFSTDTC/AGE 当 Req 实为 Exp)
  - **eval 工具**: `run_eval.py` 加 `--temperature` (确定性配对必需) + answer_preview 300→600 (取证)
- **验证 (全闸过)**: pytest **214 passed**; retrieval-only v2 102q **99.02% 未动** (single 100/cross 96/concept 100/mixed 100, q02 修后仍逐题一致); FastAPI /info smoke 杠杆 on startup 0.41s; **full eval** DeepSeek temp=0 配对 OFF/ON: **src 80.9→99.0% / fact 96.3→95.2% 噪声带内持平**; **延迟** +14ms/查询 (S1-fired p50 116ms=embed-once 生效) + BM25 建索引 0.5s 一次性
- **Rule D** (代码审, 异 type `oh-my-claudecode:code-reviewer`): APPROVE_WITH_NITS; 12 分支 trace `need_q_emb` guard 正确 + behavior-preserving 确认; 采纳 2 MEDIUM
- **Rule A** (语义抽检, 异 type `oh-my-claudecode:scientist`, KB 逐一核验 n=15): 4 better/6 equal/2 artifact/**3 real-worse** (q02/q37/q93) — **噪声稀释假说坐实** (少数); cross 92.7 的"掉"大部分 substring 假阴 (OFF 在 q34/s05 反而编造/错误)
- **关键决策 (用户 ack)**: q02 修复保留 (净语义正向, 高频题; 但 relocation 到 q100 多变量问=前沿固有); **停手不再调** (遵复盘"不做帮一类伤一类全局切换"); 残留 known limitations q100/q37/q93/C-code 幻觉 [答题侧, 提示护栏 declined per 用户"不动提示词"]
- **方法论收获**: substring fact-recall 是结构检查不可单独判业务 (gold 双向有错+措辞差异)→必须语义裁判 override; DeepSeek temp=0 仍有残留非确定性 (q78 context 未变答案变, ±1pt 噪声底); src (确定) +18pt 是硬增益
- **下一步**: commit + push (单 commit, 限定 P1 wire-in 文件, 不碰无关 README/web 改动)

---

## 2026-06-09 答题侧可信度护栏 DONE (P1 接入生产后续 ①)

- **触発**: 路由词「RAG 答题护栏 开始任务」→ `KICKOFF_answering_guardrail.md`。修 P1 Rule A 裁判挖出的两类答题侧硬伤: (1) **per-value C-code 幻觉** (q90/q91/q93 给对取值名配错/编 NCI 码), (2) **关系类误判 special-purpose** (q37 把 RELREC/SUPPQUAL 当 special-purpose)。约束: 仅动系统提示词 + eval gold, **不碰已验证检索层** (用户明确)。
- **方法**: 先修 gold (writer=main, scientist 独立核验) → 写护栏 (writer=main) → 客观闸 + code-reviewer → 配对 full-eval + **对抗式多-lens scientist 语义裁判** → v1 FAIL Rule B 归档 → v2 重写 → 重验重判 → 用户 ack SHIP。Rule D 全程异 type 隔离。
- **先修 eval gold** (`test_set_v2.yml`): q02 expected_facts → 真 7 Req (STUDYID/DOMAIN/USUBJID/SUBJID/SITEID/SEX/COUNTRY; 原含 RFSTDTC/AGE/ARM 全是 Exp); q37 移误判 SUPPQUAL (实为 model/06 关系类) → SE。`oh-my-claudecode:scientist` 独立 KB 枚举核验 **PASS** (规则 A 4.c)。
- **护栏 v1 (FAIL)**: rule 7 "码 verbatim 出现才输出" + rule 8 "context 陈述才断言分类"。**4-lens 对抗式 scientist 裁判 (KB 逐一核验) 判 gate FAIL**: q90/q91 真修 (mass-fabrication 类 codelist 巨大模型放弃→name-only), **但 q93/q44 漏穿** — q44 (过度拒答探针) ON **反而新增 6 个错 VSTESTCD 码 + 递增猜, C49672/C49675 全 KB 不存在**, OFF 本是 name-only 安全; q37 把 RELREC/SUPPQUAL 从 OFF 对冲表并进 ON "确定属于"表=**变糟**。根因: 两规则查 **presence-of-string 非 authoritativeness**; small/familiar codelist 模型自信顶穿; KB IG 松散 prose "RELREC special-purpose dataset" 橡皮图章。**substring 指标对两类缺陷全盲** (q37 100/100, 编码不罚)。Rule B 归档 `evidence/failures/guardrail_v1_attempt_1.md`。
- **护栏 v2 (PASS)** (`rag.py` `_GUARDRAIL_RULES`): **rule 7** 个体 codelist 值**默认 name-only**, 仅当该值整行 (值名+码同现) 字面在 context 才附码; 禁凭记忆/自信、递增/类比、"present but not shown" 合理化 (扩 q90/q91 已证 name-only 安全行为)。**rule 8** 分类据**权威 Class 列** (或明确 "the following domains are X" 枚举), 非 domain 自身 assumptions 松散 prose; relationship dataset (Class=Relationship) ≠ Special-Purpose。通用 pattern (无缺陷靶题号/RELREC/VSTESTCD 泄漏, C66742 沿用 rule 5 中性示例); OFF **逐字节一致** (22453 chars)。
- **新增确定性闸** `eval/prod_wirein/check_code_grounding.py`: 抽答案所有 Cxxxxx 对**重检索 context** + 全 KB (23402 distinct codes) 核 grounded / ungrounded(mis-cited) / nonexistent(fabricated)。补 substring 盲区, v1/v2 before-after 可比。
- **v2 验证 (全闸过)**: pytest **214**; OFF 字节一致; retrieval-only 99.0% 未动; **确定性码闸 全 102 ON-v2 答案: 147 码 grounded 147 / ungrounded 0 / nonexistent 0 → PASS** (v1 16q 子集已 10 违规); **3-lens scientist 裁判 (over-refusal 决定性 + 分类 + ship)**: gate_pass=TRUE, code_fabrication=eliminated, q37=fixed (抵 SUPPQUAL prose 诱饵用 ch03 Class 列), **over_refusal=0** (9 drop = 4 子串假阴 [codepoint 级查实 U+202F narrow-space/U+2011 nbhyphen/U+2013 en-dash/word-number] + 5 正确弃答 [gold 事实确实不在检索 context, OFF 仅靠未 grounded 记忆"赢"]), real_regressions=[]; fact 94.8→93.4 (-1.4pt) 噪声带内 (OFF-vs-OFF 噪声底实测 +0.9avg/±3pt cat/per-q 100→33); **SHIP_DEFAULT_ON** + 用户 ack。
- **Rule D 隔离**: writer=main(opus) / gold 核验=`scientist` / 代码审=`code-reviewer` APPROVE_WITH_NITS / 语义裁判=`scientist`×2 轮 (v1 4-lens + v2 3-lens, 全 opus, agentType 经 Workflow)。
- **残留 known limitations (护栏两规则范围外)**: q93 INJECTION-vs-INJECTABLE (值名; INJECTION/C42946 不在检索 context, 模型用 SU spec prose "INJECTABLE") + q96 Diameter (标准值未检索) = 检索覆盖 artifact, 非码/类缺陷; per-value 右归属仅 bundle spot-check (确定性 checker 覆盖全 102 码 presence)。
- **方法论收获**: (1) substring 指标对码 fabrication + 误分类**结构性盲** → 必须确定性码闸 + 语义裁判双补; (2) 对抗式异-type 裁判抓到主 session 眼检漏掉的 v1 漏穿 (q44 过度拒答探针反而新增编码) = Rule D 真闸; (3) 提示护栏对 small/familiar codelist 的强模型先验需 forceful 反自信措辞才压得住; (4) "证据优先" — OFF 重跑测噪声底把 fact "回归" 证为噪声。
- **收口**: `evidence/checkpoints/guardrail_v2_summary.md` (规则 C retro)。新资产: `check_code_grounding.py` / `forensic_guardrail.py` / `judge_workflow{,_v2}.js`。

---
