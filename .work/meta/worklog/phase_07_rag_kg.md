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

## 2026-06-12 题集 v3 扩充 + s3 端到端验证 + S4 三修 DONE (P1 后续 ②③)

- **触发**: 用户选 follow-up「扩题集增 margin + 补长名 single 题 (顺手验 s3)」; v3 暴露 gate FAIL 后用户 ack「可以继续」→ S4 修复 attempt。
- **题集 v3** (`eval/test_set_v3.yml`, 140q = v2 102q 逐字节保留 + 38 新题): cross 25→50 (5 主题×5: 变量分布/codelist 共享/关系机制/模型概念/域对比) + 13 道纯长名 single (题面零域码零变量名; 10 道 s3 可匹配 + 3 道故意边界探针)。**防过拟合流程沿用 v2**: 7 writer 盲对检索实现 (Workflow, 只读 KB) → 7 独立 scientist 审计逐题开 gold 核验 (37 PASS + 1 FIX [q128 补 VSSTRESC] + 0 REJECT) → 程序化防漏检 0 问题 → `verifier` 异 type 抽检 N=8 **8/8 PASS** (Rule D 三 type 隔离)。审计 trail `evidence/checkpoints/testset_v3_authoring_audit.json`。
- **s3 端到端验证 ✅**: 新探针脚本 `eval/probe_s3_longname.py` (resolve() 通道级归因, 零码 token 时长名通道是唯一可能路径); 10/10 可匹配长名题 fire + eval 100%; q135 (Demographics) OFF 0%→ON 100% = s3 净救回。**s3 (06-09 实现) 首次被真实 eval 题穿透验证。**
- **v3 暴露 per-category gate FAIL (扩 margin 的目的达成)**: ON overall 95.4% 但 cross 93.0/single 92.5 <95; **核心新发现 q139/q140 (Exposure/Comments 边界探针) OFF 100%→ON 0% 真回归** — s3 短词守卫排除→无注入保护, hybrid BM25 把 rank 10/12 的 spec 挤出 top-15 (四配置微型消融钉死: hybrid-only=MISS 元凶, s1-only 无害); P1 零回归 gate 没抓到因 v2 无此类题。其余: q134 自然措辞≠KB 斜杠名 (四配置全 MISS) / q107 dist 锚缺 "datasets" / q119 q126 q73 同根因=概念定义型 gold 在 chapters/model 题面不点名域。环境零漂移 sanity: v2 复跑 99.0% 逐题一致 + v3 中 v2 子集 diff=0。
- **S4 三修** (`server/structured_lookup.py`, 全 pattern 级): (a) `_DIST_DOMAINS_RE` 加 `datasets` 同义词 [已知变量+动词双锚不放宽] (b) 斜杠复合长名按备选展开变体 [KB 数据驱动, 自动覆盖 CM/IE/TI/TU/TR 5 名 10 变体] (c) 短词长名 (<10 字符) 由跳过改锚定匹配 `<name> dataset|domain` ["data" 故意不作锚; q96 "Cumulative Exposure)" 实测不撞] + 附带排序键修复 (pattern 串长→长名长度)。
- **验证 (五层全过)**: pytest **236 passed** (新增本模块首个单测 22 用例, 含集外泛化探针+负例); s3 探针 **13/13**; **零回归 gate**: v3 ON 逐题 diff 救回恰好预测 4 题 (q107/q134/q139/q140 全 0%→100%) 回归 0; **修后 v3: single 100 / cross 95.0 / concept 100 / mixed 100, overall 98.2%, 全类 ≥95% 恢复**; OFF 臂构造上不变。
- **Rule D** (代码审 `oh-my-claudecode:code-reviewer` 异 type): **APPROVE_WITH_NITS** (0 C/H, 2 MED 当场采纳为测试加固 [多斜杠守卫断言 + union-add 保序探针], 4 LOW 记录); 审查员独立复跑 pytest + git stash 对照 + grep 确认 logic 零 eval 题面 token ("genuinely pattern-level, not example-tuned"); 抓到**存量** known boundary ("Procedures"/"Disposition" ≥10 字符裸匹配误触面, 本修未引入未恶化, 按建议记录不反应式修)。
- **Rule A/B**: 出题=高改写率→独立审计全量 38/38 (超抽检) + verifier 二道 N=8; 本轮无失败 attempt (gate FAIL 是题集揭示的系统缺口, S4 一次过闸)。
- **收口**: `evidence/checkpoints/testset_v3_expansion_summary.md` + `s4_longname_dist_fixes_result.md` + `s4_rule_d_review.md`。
- **残留 (下一杠杆)**: q73/q119/q126 同类 = **(d) 概念定义→chapters/model 通道** (--LNKID/--LNKGRP 定义 / SE-TE 对比 / RDOMAIN 载体); cross 95.0% 零 margin, 拉开必须做 (d), 架构件单独立项。可选: v3 full eval (答题侧 DeepSeek temp=0 配对) 确认 fact recall 不稀释 (S4 改了生产检索行为, retrieval-only 已零回归, full eval 是惯例闸)。

---

## 2026-06-15 v3 full eval 收 S4 尾账 (CLEAN_CLOSE) + (d) 概念定义双通道 SHIP

- **触发**: 用户「先 v3 full eval 配对收 S4 尾账, 然后开 (d) 概念定义通道」(入口 TODO §6); 后续选「现在就做 q119 + 补跑 guardrail 确认 + 做完再收尾」。

### Task 1 — S4 三修 v3 full eval 配对收尾账 (CLEAN_CLOSE)
- **为什么**: S4 retrieval-only (src) 已过, 但 S4 是 union-add 注入, prod_wirein 立规矩=union-add 可能稀释答案 (注入 spec.md 挤掉 assumptions.md 叙述事实); 必须带答题模型的配对 full eval 测 fact recall。
- **配对** (DeepSeek temp=0, v3 140q, 两臂 guardrail OFF 隔离 S4 检索变量): **src OFF 76.4→ON 97.5 (+21.1pt)** 全类跳 (cross 53→95/mixed 80→100/single 93.8→100/concept 92→96); **fact OFF 82.8→ON 82.6 (净 −0.2pt, 噪声带内)** = 无系统性稀释。8 gain 抵 11 drop。
- **11 掉分独立语义裁判** (`oh-my-claudecode:scientist`, Rule D 非 S4 writer, 逐题 KB 核验 OFF/ON 答案+源构成): **7 FALSE_NEGATIVE / 3 NONDETERMINISM / 1 REAL_DILUTION (q57 PR/spec×4 挤掉 PR/assumptions 的 "Interventions class" 标签) / 0 PREEXISTING → VERDICT CLEAN_CLOSE**。主 session 抽验头号嫌疑 q114 (实测 ON 答案确含两 fact = substring 假阴, 裁判正确非走过场)。q133/q140 (新 S4 长名单域题) 判 NONDETERMINISM (对的 spec×4 在场, 模型误读 role 列/改写结构句, 非文件被挤)。
- **code-grounding 旁证**: guardrail OFF (隔离用) → ON 引更多码更多 ungrounded (54) = 无护栏基线, 正交。
- **belt-and-suspenders 补跑** (用户选): `--guardrail` ON + S4 终态码 (q73+q119) code-grounding: **287 码 / 286 grounded / 1 mis-cited (q35 C66742, KB 真实存在) / 0 fabricated = 99.65%**。护栏在 S4 浮出更多码后仍把 ungrounded 54→1、fabricated 3→0 → 护栏与 S4 正交且组合后码 grounding ~100% 坐实。
- **收口**: `evidence/checkpoints/s4_full_eval_closure.md`。新产物 `eval/prod_wirein/v3_full_{off,on,on_guardrail}_t0.{json,log}` + `v3_full_paired_t0.log` + `v3_drops_forensic.json`。

### Task 2 — (d) 概念定义→chapters/model 通道 (q73+q119 双通道 SHIP, q126 永久 defer)
- **研究法**: 6-agent Workflow (3 题并行分诊 + 数据源清单 + 对抗式 over-fire + 综合, 只读) + 主 session 独立复核 + Rule D。
- **q73 (3a, BUILT)**: `var → 单一 model 文件` def-home 映射 (解析 model/*.md **6 列定义表**, 6 列形状是载重判别器隔离 5 列 usage 表; 59 vars, RDOMAIN→model/06) + 严格定义动词锚 `_DEFVERB_RE`。**恰触发 q73+q83 (均 gold model/06)**, q73 (cross) 0→100 载重, q83 冗余无害。
- **q119 (3b, BUILT)**: workflow 综合曾判 DEFER (称 q119 与 q114 锚不可分); **主 session 独立复核推翻** — 两题意图可分 (q119 "difference between --LNKID/--LNKGRP variables"=比较意图 / q114 "use --SEQ as join key"=用法 / q68/q71 "which domains use"=分布)。通道: 通用 `--` 前缀变量定义/比较 → ch04 General Assumptions; `_query_generic_var_definition` = ch04存在 AND 非dist AND 有`--`token AND (("difference between"+≥2 不同`--`token) OR `_DASH_DEFVERB_RE`); ch04 glob 发现; dist 抑制守 q68/q71。regex 修 `(?<![A-Za-z-])--[A-Z]{2,8}(?![A-Za-z-])` (`\b--` 匹配空 + 防畸形 token)。
- **q126 (永久 DEFER)**: 双重独立阻断 — (1) 每个区分性短语 140q 中恰命中 q126 自己 = 例级作弊 (放宽到单词喷 8+ 题); (2) **架构阻断** `domain_to_spec` 只映 spec.md 但 q126 SE gold=SE/assumptions.md, 需新 sub-file 判别器。记为 §6 预警的"无实体锚概念对比边界案"。
- **验证**: retrieval-only v3 cross **95.0→99.0** (q73 +2 / q119 +2), single/concept/mixed 100%, **0 回归** (逐题 diff 仅 q73+q119 改善); pytest **250** (+`TestConceptDefinitionChannel` 8 + `TestGenericVarDefinitionChannel` 6, 含 2 canary + 集外泛化 + must-not-fire battery)。
- **Rule D** (`oh-my-claudecode:code-reviewer` 异 type, 两轮): **q73 APPROVE_WITH_NITS** (MED doc 正确性 [真载重判别器是 6 列形状非 Notes 单元, 放宽 `!=6` 会 un-fix q73] + LOW EPOCH canary, 已采纳) + **q119 APPROVE** (clean; 决定性 pattern 级证明 = 集外电池 8/8 应触发 + 10/10 应静默, 用非题集变量/措辞, 区别于 q126 退化单例; 1 LOW 畸形 token 正则加固已采纳)。
- **抗过拟合** (用户敏感点): 全代码零引用 q73/q83/q119/--LNKID 等; held-out 探针证明两通道 pattern 级泛化。
- **收口**: `evidence/checkpoints/d_channel_concept_definition.md`。产物 `eval/ablation_t1/v3_on_dchannel{,2}.{json,log}`。
- **结果**: cross 95.0% 零 margin → **99.0%**; 剩余 cross 缺口主要是 q126 (defer)。

---

## 2026-06-15 (续) 检索线收口 — ① 本地部署修复/加固 + ② KG 关闭 + 语义 fact eval + 总 retro

> 用户「先①再②一起做」(检索质量已打满 99%, 进入边际收益递减区)。

### ① 本地 Docker Compose 部署 (修复+加固+实服 e2e 证)
- 现状: Dockerfile + docker-compose.yml Phase 1A 脚手架但从未构建/跑过 (H-2 defer)。本机**无 docker** → 修+加固+实服 e2e 证内容, 容器构建交用户 Docker 主机。
- **修 Dockerfile 构建 bug**: `pip install .` 前先 COPY 源码包 (原顺序只有 pyproject 时构建必失败) + 新增 `.dockerignore` 瘦身 (data/KB 运行时 bind-mount 不烘镜像) + compose 加 healthcheck + ui `depends_on: service_healthy`。
- **实服 e2e (核心)**: `.venv` uvicorn 起真服务 (非 TestClient): startup 三杠杆默认全开 (structured_lookup/hybrid/prompt_guardrail) init 0.72s; /health ok; /info 杠杆 true; /ask "RDOMAIN identify" 真实准确答案 **sources 含 model/06 ((d) 通道实服命中)**, `model_used=deepseek-v4-pro` (Anthropic credits 耗尽 Router 自动回退实证)。**首次以实服验全栈端到端。**
- 静态校验: compose YAML valid / Dockerfile COPY 6/6 路径在 / 包 import 解析。README Docker 段重写 (data 复用 vs ingest / env 必需性校正 [OPENAI 硬必需无 fallback / DeepSeek 实际主答 / Anthropic 实务可选] / fallback 说明)。收口 `evidence/checkpoints/deploy_local_compose.md`。**待用户**: Docker 主机跑 `docker compose up --build -d`。

### ② 收口固化
- **Phase 2 KG 正式关闭**: gate = RELATION/cross 召回 <50% 才启; Phase 1D 61.5% defer; 现检索路由 (P1+(d)) 把 retrieval-only cross 拉到 **99%** (远超 gate) → 纯向量+路由已解决跨域召回, **KG 作为检索杠杆不再有理由, 正式关闭** (作为独立产品特性[关系/CT 影响图遍历]仍可选未来增强, 重启需新立项+P3 meta.yaml)。`_progress.json` phase_2_kg + TODO T6 更新。
- **语义 LLM-judge fact recall**: substring 82.6% 是假象 → 7-shard Workflow (sonnet) 逐 gold fact 语义判 140q/466 facts: **overall 93.9%** (concept 100/cross 93.5/mixed 92.0/single 91.7), 落在 93-96% band。**主 session Rule A 抽验校准** (q104 fr=0 / q02 fr=0.43 实查均判对, judge 未过松); 121/140 全覆盖, 残留 miss (q104 VISITDY label / q133 TU topic / q02 枚举) 均真 miss 答题侧。缺口: 语义 judge 未固化进 run_eval (建议加 `--judge`)。收口 `evidence/checkpoints/llm_judge_fact_recall.md` + `eval/prod_wirein/judge_{input,result}_v3.json`。
- **总 retro**: `RETROSPECTIVE_retrieval_arc.md` (检索弧线 Phase 1.5→P1→S4→(d)→KG 关闭; Rule C 三段 + 6 关键决策复盘 D1-D6)。

### 净结果
检索质量目标达成 (cross 61.5→99%, 全类 ≥99%, 语义 fact 93.9%); 部署 artifacts 就绪; KG 关闭; 残留 = q126 (架构受限) + 语义 judge 固化 + 跨模型 eval (credits) = 下迭代候选, 非阻塞。

---

## 2026-06-15 (续 2) 语义 fact judge 固化进 run_eval (--judge)

> 用户「把 --judge 固化进 run_eval」(收口缺口: 否则下次 fact 数字又只剩误导性 substring)。

- **实现** (`eval/run_eval.py`): `_parse_covered` (纯 JSON 解析器, 容忍 ```json fence/散文, 长度不符→None) + `check_fact_recall_judge` (单 litellm 判, 429 backoff 同答题, 空 gold 不调 LLM 直接 1.0) + `run_evaluation(judge, judge_model)` 逐题判 (解析失败回退 substring 且 `judge_parse_ok=False` 计数) + `print_summary` 报 substring(次)+judge(主) 分类别 + `judge_parse_failures` 计数, **verdict 用 judge** (overall=(src+judge)/2); flags `--judge` + `--judge-model` (默认 deepseek, 与 --model 独立); summary 存 judge_model/overall_metric。judge 收**整答案** (非 600 char preview)。默认 (无 --judge) 路径字节等价 (仅加 overall_metric 键)。
- **Rule D** (`oh-my-claudecode:code-reviewer` 异 type): **REQUEST_CHANGES → 修后 clean**。抓到 **HIGH**: `[bool(x) for x in raw]` 对非 bool 元素 (array-of-objects / 字符串裁决 "no") 会 truthy 膨胀为**全 covered 且 judge_parse_ok=True 静默** = 正是本功能要防的信任违背 (审查员实证复现) → 加类型守卫 `all(isinstance(x,(bool,int)))` 拒绝→计数回退; + 2 MED (backoff 末次空睡跳过+封顶 120s / judge_fact_hits 对称) + LOW (zip strict) 全采纳。审查员独立复跑 pytest + 审 analyze_paired 消费键 (source_recall/fact_recall 未动, 无 backward-compat 破坏)。
- **验证**: pytest **260** (新 `test_run_eval_judge.py` 含 HIGH 回归: array-of-objects/字符串裁决→None, 0/1 int 仍接受); ruff clean; **5q 集成 smoke** (DeepSeek temp=0 + 杠杆 + --judge): 真 judge 响应解析 0 fail, judge 97.1% vs substring 70.5%, **q119 substring 0%→judge 100%** (gold 是长句从不 substring 命中) / q73 67→100, verdict PASS on judge。
- **收口**: `evidence/checkpoints/llm_judge_fact_recall.md` (缺口段更新为已固化); README Eval 段 + retro §2 #2 更新。**约定: 下次报 fact recall 一律 --judge。**

---

## 2026-06-15 (续 3) 本地部署 + 多模型对比/裁判 — 规划立项

> 用户决定把 RAG 在本机 (Mac mini M4 基础款 / 16GB / 公司网) 24/7 部署, **先 localhost 自用调优 → 再共享同事**; 并新增「一题跑多模型对比 + 第 4 模型裁判」功能。本 session **纯规划, 未改代码、未跑 eval**。

### 关键讨论结论
- **硬件评估**: Mac mini M4 基础款 10C CPU/10C GPU/**16GB 统一内存**/95GB 盘。**本地大模型推理不可行** (16GB 天花板, 用户两次崩溃已验证; 7-8B Q4 ~6-7.5GB 叠 macOS ~5-7GB 底盘+服务即崩溃区; 14B swap; 32B OOM); **服务本地 + ML 云端 = 场景 A, 绰绰有余** (服务常驻 ~0.5-0.9GB, CPU 亚毫秒, GPU 不用)。
- **成本** (完全云端): = 固定托管 + per-query API。实测每题 ~15k in / 0.5k out (top_k=15 + 整文件 system prompt 注入); prod 配置 rerank/expansion 关 → 只算嵌入(可忽略)+生成。DeepSeek V4 Pro $0.435/$0.87/1M → **~0.7¢/题**; ~300 题/月 **API ~$2/月**, 主成本是托管 ($5-15/月)。Sonnet ~5.3¢/Opus ~8.8¢/Haiku ~1.8¢ 每题。
- **决定不租云主机, 用本机 launchd 24/7** (电费 ~$1-2/月, 比云主机还省); 部署方案选 **原生 launchd (非容器)** — 16GB 紧, 容器 VM 白吃内存; 探讨过 Apple `container` (macOS 26 够格但 v1.0.0 太新+不直接吃 compose) / OrbStack (商用授权) / Docker Desktop (锁 4GB)。
- **前端无需做**: `ui/streamlit_app.py` 现成 (Q&A 聊天 + Dataset Validation 双标签 + sidebar 设置), launchd 起的就是它。
- **多模型对比设计** (folded 进阶段 2): 检索跑一次 → 3 模型**并行扇出同一 context** → 三栏并排 + 延迟/token/成本 badge; **第 4 模型匿名 (A/B/C) 裁判** → 排名+点评+最佳; **每个模型槽可自定义** (FR7, `.env` 默认 + UI sidebar 覆盖, 本期不固定型号)。`/api/ask_compare` 复用 retrieve/format/build, 仅生成步骤改并行 (asyncio.gather)。

### 产出
- **`branches/07_rag_kg/sdtm-rag/DEPLOY_PLAN.md`** (草案 v1, 9 段): 背景/目标 · 全局锁定设计 · 多模型对比+裁判需求(FR/NFR/API契约/裁判/UI) · **四阶段执行稿**(0 冒烟 → 1 launchd 本机 → 2 对比开发+定模型 → 3 共享) · 实现拆解 T1-T8 · 验收 · 路线图 · 待确认 · 风险 · 价格表。
- 全局设计锁定: 服务目录 `~/sdtm-rag-service/` (阶段 3 启用, 与 repo 隔离), kb 复制进去自包含, 索引复用不重建, LaunchAgent, 端口 8000/8501 阶段 0-2 绑 127.0.0.1, deploy.sh 发版。

### 下一步 / 残留
- 阶段 0 冒烟测试 (不依赖任何开放问题, 全程 localhost 零风险): 查 .env/uv sync/起服务/health check/问一题。
- 开放问题 (非阻塞, 走到再定): 各模型槽默认值 (全可自定义) / kb 路径 config 变量名 / 阶段 3 登录门 + 自动登录 vs LaunchDaemon。
- 用户将开**新 session 继续** (路由词: 「读 DEPLOY_PLAN.md 继续本地部署」或「RAG 本地部署 阶段0」)。

---

## 2026-06-15 (续 4) 本地部署 阶段0 冒烟 + 阶段1 launchd 常驻 + 主力切 DeepSeek + 中文回答 + KG 路径定

> 用户:「先做 kg 还是先部署」→ 调研后定「先部署冒烟, 再建 meta.yaml」;「先用 DeepSeek 当主力, 进阶段1」。本 session 执行 DEPLOY_PLAN 阶段 0+1, **未跑 eval**。

### KG 决策 (4-agent 证据调研)
- 用户问「当年为什么关 KG, 开 KG 不是能增加检索精度吗」。4-agent Workflow (关闭理由/测试集覆盖/KG 能力/反方论证):
  - **当年只关「KG 当检索杠杆」**: gate = cross 召回 <50% 才建; 路由把 cross 拉到 99% → gate 永不满足 → 关。**从没建过/测过** (纯推理推导; T1 证 cross 是排名问题非关系缺失)。
  - **开 KG 不提检索精度**: 检索已 99%; `knowledge_base/VARIABLE_INDEX.md` 已把图遍历 (哪些域含变量 X / codelist 分组) 预 materialize 成平铺文本。
  - **KG 真价值在评测从没测的地方**: 多跳/计数/穷举 (q103「43」q104「36」今天答错) + 影响/级联分析 + 替换 `structured_lookup.py` 脆弱正则「影子 KG」(故意丢多归属变量 USUBJID/POOLID)。fact 仍 93.9% 非 ~100%, 部分残留是结构化层可补的枚举型。closure 自己写明 KG 产品价值仍开口。
- **选定路径** (用户定): deploy → **meta.yaml 结构化层** (便宜/立刻修计数穷举/q126/Neo4j 硬前置) → 可选 Neo4j。memory `project_kg_decision.md`。

### 阶段 0 冒烟 (PASS)
- 4 API key 齐 (ANTHROPIC/DEEPSEEK/OPENAI/COHERE, 值未打印); `uv sync` 完成 (补 bm25s 进 lock); chroma **4146 chunks** 确认。
- 端到端 `/api/ask`「AE/AETERM」答案接地正确 (15 sources, AE/spec.md+assumptions.md), `/info` = 4146 + structured_lookup/hybrid/guardrail 全 ON; `model_used=deepseek-v4-pro` = Anthropic credits 耗尽 DeepSeek 回退实证。

### 中文回答修复
- 根因: `server/rag.py` `_build_system_prompt` 整段英文 + 无语言规则 + 英文 context → 默认英文 (非 bug)。
- 修: 系统提示头部加「**回答跟随提问语言**; SDTM 标识符 (域码/变量名/码/CT 值/Type·Role·Core) + `[Source:]` 引用一律保留英文原文」(用户选「匹配提问语言」)。无测试断言系统提示内容。
- 实测: 中文问「DM/USUBJID」→ 中文答 + USUBJID/Char/Req 英文标识符保留 + 引用保留。

### 主力模型切 DeepSeek
- 用户「先用 DeepSeek 当主力」(Anthropic credits 耗尽; 原 default=Sonnet 每次先失败再回退 = 浪费一跳)。`.env` `SDTM_RAG_DEFAULT_MODEL=deepseek/deepseek-v4-pro` (fallback 也 deepseek = 主力+自重试); /info 确认。**API 走 Anthropic/DeepSeek 官方 API 按量付费, 接不到 Claude Code 订阅 plan**。DEPLOY_PLAN §1 主力模型行更新; 阶段 2 用 eval+对比再定是否充值上 Sonnet。

### 阶段 1 launchd 常驻 (验收全过)
- 2 个 LaunchAgent `~/Library/LaunchAgents/com.sdtmrag.{api,ui}.plist`: 绑 127.0.0.1, RunAtLoad+KeepAlive+ThrottleInterval 10, WorkingDirectory=sdtm-rag, 日志 `logs/{api,ui}.launchd.log`。
- **关键修正: 直连 `.venv/bin/{uvicorn,streamlit}` 不走 `uv run`**。uv run 时杀 uvicorn worker 子进程 ~30s 才恢复 (uv 父+server 子两进程, launchd 只盯父进程, 子崩父不退); 改直连后 launchd 直接盯真服务 (PPID=1), 杀监听进程即重启。venv 二进制 shebang 指 venv python + 包 editable 装 (`import server.main` ok, 不依赖 cwd)。
- **坑**: `launchctl bootout` 异步, 紧接 bootstrap → `Bootstrap failed: 5: I/O error`; 解 = bootout 后轮询确认卸载完 + bootstrap 带重试。
- **验收**: health ok / `/api/info` default=deepseek + 4146 chunks / **KeepAlive 实测 kill 监听进程 70991→自起 71267** / UI `_stcore/health` ok / 两端口 127.0.0.1 监听。LaunchAgent = **登录时**自起 (无人值守开机自启属阶段 3 自动登录/LaunchDaemon)。

### 产物 / 残留
- 改: `server/rag.py` (+语言规则) / `.env` (default→deepseek, gitignored) / `DEPLOY_PLAN.md` (阶段0+1 勾 + §1) / `uv.lock` (+bm25s) / `~/Library/LaunchAgents/*.plist` (repo 外) / `logs/` gitignore。
- 下一步 = **阶段 2** (核心): `/api/ask_compare` 一题 3 模型并行 + 第 4 模型匿名裁判 + Streamlit 三栏 UI + eval 跑 DeepSeek vs Sonnet 定主力 (T1-T7, 按 Tier 2 开发/审阅分离)。
- 可选: 用户重启/重登录验 launchd 自恢复; plist 另存模板进 repo (阶段 3 deploy.sh)。

## 2026-06-16 阶段 2 多模型对比+裁判 实现 + 四方 eval + 主力拍板 DONE

DEPLOY_PLAN §3 阶段 2 (★核心) 收口。retro `branches/07_rag_kg/RETROSPECTIVE_phase2_compare.md`; 证据 `evidence/checkpoints/phase2_{compare_judge,model_comparison}.md`。

### 实现 (T1-T6)
- `server/compare.py` (新): `run_compare` asyncio.gather 并行 `litellm.acompletion`, 每模型独立 try → 失败隔离 (NFR2), 返回 ModelAnswer(model/answer/usage/latency_ms/cost_usd/error)。`run_judge`: 答案匿名 A/B/C 喂裁判 → `_parse_judge` 容错 JSON → 映射回真名; <2 有效答案返回 None + judge_skipped 日志。
- `server/cost.py` (新): §9 价格表 (前缀锚定+最长键优先) + `litellm.cost_per_token` 兜底; 未知模型 → None → UI "—" (绝不编造数字)。
- `server/router.py`: `POST /api/ask_compare` (async, 复用 retrieve/format/build → FR1 检索仅一次) + Pydantic 契约 + 模型去重; `/api/info` 加 compare_models/judge_model 供 UI 预填。
- `server/config.py`: compare_models (3 参考占位, env JSON 覆盖) / judge_model (默认 deepseek-chat 可跑, §2.6 Opus 待 credits) / compare_timeout_s / compare_num_retries; host 默认 0.0.0.0→127.0.0.1 (对齐 §1)。
- `ui/streamlit_app.py`: sidebar Single/Compare 模式 + 3 模型槽 (预填 /api/info) + Enable Judge; `_render_compare` 三栏 badge + 共用 Sources + 裁判区; 修过时 "default=Sonnet" 文案; `_get_info` 不缓存失败。
- 设计: compare/judge **绕过命名 Router** 直接 acompletion(任意串) → 满足 FR7。无新依赖 (litellm 1.88.1 含 acompletion+cost_per_token)。

### 验证 + 审阅
- 端到端实测 (临时实例 127.0.0.1:8011, 不碰 launchd:8000): FR1 检索一次 / FR2 并行 8.9s≈最慢家 / NFR2 失败隔离 (Anthropic credits 耗尽单栏报错另两家正常 + HTTP 200) / FR3 badge / FR5 裁判匿名+映射 **真抓出 gpt-4o 编造 cited source 未含的 verbatim term**。
- 验证抓修真 bug: cost.py 用错 `completion_cost(prompt_tokens=)` (1.88.1 不支持) → 改 `cost_per_token`; 裁判偶发 None 定位 provider 空返回 (非 bug) → 加 judge_skipped 观测日志。
- **规则 D 双独立审阅** (code-reviewer 并发/正确性 + security-reviewer 匿名/注入, 异 subagent_type) 均 SHIP, 0 BLOCKER/HIGH; 8 项加固落 (去重/注入加固/best 直接索引/cost 锚定/host 收环回/_get_info/观测日志/注释)。三承重信任点 PASS: 失败隔离 textbook-correct / _parse_judge 抗 8 类畸形 / 裁判匿名代码层零泄漏 + label→model 映射含部分失败子集也正确。

### 四方 eval (140 题 v3, 同条件配对: top_k=15/temp=0/检索杠杆全 ON/同判官 deepseek-chat)
- **判官 fact-recall (per-q 均值)**: Sonnet 96.0 > DeepSeek 93.6 > GPT-4o 90.4 ≈ GPT-5.4-mini 90.2。source recall 全 ~100% (与模型无关)。
- **每题成本**: DeepSeek $0.0075 < GPT-5.4-mini $0.0123 < GPT-4o $0.0391 < Sonnet $0.0721。延迟: mini 4.1s 最快 (Sonnet/4o 被限速灌水)。
- 抽检 (规则 A): "枚举弱"是便宜模型共性 (q02 DM 全部 Req 变量 DeepSeek 14%/mini 43% 弃答, Sonnet/4o 100% 完整枚举); GPT-5.4-mini 失分=不完整非编造 (grounding 正常)。gpt-5.4-mini=2026-03 发布晚于知识截止, 经 OpenAI /models 查实 + 冒烟 temp=0 才跑。
- **GPT-5.4-mini 完胜 GPT-4o** (同质量/1-3 成本/7x 速度); DeepSeek 比两 OpenAI 都准且最便宜。

### 决策 + 部署
- **主力维持 DeepSeek-v4-pro** (用户 2026-06-16, 四方数据支撑; Sonnet 留 hard 档/Compare 手动)。无需改 .env (默认已是)。
- launchd kickstart -k 重载 api+ui → `localhost:8000` 上线新代码 (/api/info 含 compare_models), UI Compare 模式可用。Sonnet 充值生效 (用户 2026-06-16)。
- 残留 (阶段 3 共享前 gate, 非阻塞): 错误串 sanitize (SEC MED) / 限流 / asyncio 外层超时 / pip-audit; Compare 多轮追问 (后端 history 已预留, 用户当期选 Single 追问)。

---

## 2026-06-16 (续) ChatGPT 风格单模型流式聊天前端 DONE + 规则 D 修复 + IME 回车修复

### 触发
- 用户「RAG 阶段3 共享 + ChatGPT 式聊天 UI 开始任务」。计划就绪 `branches/07_rag_kg/sdtm-rag/PLAN_chat_ui.md` (6 task TDD) + 设计 `DESIGN_chat_ui.md` (brainstorming 批准 2026-06-16)。执行用 `superpowers:executing-plans` (异 subagent 审阅段用 Workflow)。

### 完了の作業 (6 task, 全 TDD + 逐 task commit)
- **Task 1 后端 SSE** (TDD 先红后绿): `server/router.py` 加 `AskStreamRequest` + `POST /api/ask_stream` (走 Router `default`=deepseek, 复用 retrieve/format/build; `sources→token*→done/error`; 检索失败开流前 502; 中途失败 error 事件; usage 拿不到 null 不编造)。`scripts/tests/test_ask_stream.py`。
- **Task 2 静态托管**: `server/main.py` 挂 `/static`→`webchat/` + `GET /`→index.html (exists 守卫; 与 `/api/*` 不冲突)。
- **Task 3 vendor**: marked@12.0.2 / dompurify@3.1.6 / highlight.js@11.9.0(+github.css) 进 `webchat/vendor/` (**修计划包名笔误** `@highlight.js`→`@highlightjs`); 运行时全本地 serve 无外网 CDN。
- **Task 4 骨架+样式**: `webchat/index.html` + `style.css` (ChatGPT 式两栏侧栏+气泡+粘底输入)。
- **Task 5 app.js**: localStorage 多对话 + 侧栏 + SSE 手动分帧解析 + marked→DOMPurify 净化 + highlight + 来源默认折叠 + history 截断 (近 10 轮) + 错误不白屏。
- **Task 6 集成核验**: 真模型 e2e — curl SSE `1 sources→42 token→1 done` (usage 真实, DeepSeek 接受 `stream_options.include_usage`) + Playwright 浏览器 (中文流式/多轮 history「它」=AETERM 解析/侧栏新建·切换/刷新持久/删除/断网气泡)。证据 `evidence/checkpoints/chat_ui_smoke.md` + `chat_ui_smoke_{main,error}.png`。

### 规则 D 独立审阅 (Workflow `chat-ui-rule-d-review`, 3 lens 异 subagent_type, 218k tok)
- **security-reviewer = SHIP** (全 DOM sink 经 `mdToSafeHTML=DOMPurify.sanitize(marked.parse())` 或 textContent; sourcesEl 只 innerHTML 静态字面量; DOMPurify 3.1.6 默认拦 `<img onerror>`/`javascript:`/`data:`; 后端 error 发服务端常量不回显)。code-reviewer + critic 各报 1 HIGH。
- **2 HIGH + 4 MED 全修并验证**:
  - HIGH 干净 EOF 无 done/error 帧 → 答案在屏但不落盘, 刷新丢失 → `streamAsk` terminal 追踪 + 尾 buf flush + `onClose` 落盘 (stub fetch 实证「Partial answer」落盘 + 「连接中断」提示)。
  - HIGH 每 token 重解析 markdown+重高亮 (违 DESIGN §4, O(n²) jank + hljs 重高亮刷屏) → 流中纯文本追加, done 后整体渲染一次 (终态 DOM `<ul><li><strong>` + console **0 warning**)。
  - MED 空回答占位「(无内容)」(DESIGN §6, stub done 零 token 实证); MED busy 复位入 try/finally (回调抛异常不再永久锁 send); MED `save()` try/catch 配额保护 + 淘汰最旧对话; MED `stream_options` 不支持 → `_open_stream` 去 kwarg 重试一次 (usage→null, +单测 `test_ask_stream_falls_back_without_stream_options`)。
- **延后阶段 3** (记 DEPLOY_PLAN §3): Stop/Abort+重试 UX (DESIGN §2/§6) / topbar 读 `/api/info` default_model / CSP+`X-Content-Type-Options` 头 / 请求超时。

### IME 回车修复 (用户报 bug)
- 中文输入法**组字中**按回车 (本意=上屏字母/确认候选) 被误当发送。`webchat/app.js` keydown 加 `!e.isComposing && e.keyCode!==229` 守卫。浏览器 dispatch 实测: 组字回车**不发送/不清空**, 普通回车照发, Shift+回车照换行。

### 验证 + 上线
- **263 pytest 全绿** (含 SSE 序列/422/stream_options 回退); Streamlit 8501 Compare/Judge **不回归**; launchd `com.sdtmrag.api` kickstart 重载 → chat UI 上 **`localhost:8000`** (仍 127.0.0.1; StaticFiles 按需读盘, 改前端无需重启)。
- 环境差异: 测试用 `uv run --extra dev pytest` (部署期 `uv sync` 剪掉 dev extras, `.venv/bin/pytest` 不存在); 仅增 dev 工具不动 runtime, 不扰 launchd。

### 阶段 3 决策 (用户 2026-06-16) → DEFERRED
- 用户「先本地试用 chat UI」→ **阶段 3 共享 DEFERRED** (待试用满意 + 谈完 IT)。已定: **对外面=8000 chat UI** (8501 留 localhost 当开发者工具); **登录门=FastAPI 共享口令** (登录表单+签名 session cookie 中间件, 最轻无需 IT)。**go-live 硬阻塞 (用户动作)** = 找 IT 要固定内网 IP + 安全签字 (数据出境)。记 `DEPLOY_PLAN.md` §3/§7 + memory `project_local_deploy_plan`。

## 2026-06-16 (续 2) 阶段 3 共享 工程件 DONE + 规则 D 三审 + pip-audit 修 starlette CVE

### 触发
- 用户「RAG 阶段3 共享 开始任务」(路由词 → DEPLOY_PLAN §3)。开工前 3 决策 (AskUserQuestion, 用户确认推荐项): 范围=**build-to-localhost + 审, 不翻对外** (go-live 硬阻塞 IT 内网 IP+签字); 登录门=**Starlette SessionMiddleware + 口令哈希**; 限流=**手写内存 per-IP 令牌桶**。计划 `PLAN_phase3_share.md` (Tier 2)。

### 完了の作業 (全 localhost 可测+审; 全开关默认 OFF; 现役 launchd:8000 不受扰)
- **登录门** `server/auth.py` (新): scrypt 哈希共享口令 + Starlette `SessionMiddleware` (itsdangerous 签名 cookie, 无新依赖) + **纯 ASGI 中间件** (非 BaseHTTPMiddleware → 不破 SSE 流式) 覆盖 `GET /`+`/api/*`, health/login/logout 豁免; 未登录 /api→401 / HTML→302 `/login`; open-redirect 守卫 `_safe_next`; `install_security` fail-loud (auth on 缺 secret/hash 即抛)。
- **硬化**: `TokenBucketLimiter`+`RateLimitMiddleware` (per-IP, Retry-After, health 豁免, XFF 默认不信) + `SecurityHeadersMiddleware` (CSP/nosniff/X-Frame-Options/Referrer, 默认 ON) + 错误串脱敏 `sanitize_compare_errors` (`/api/ask_compare`) + `asyncio.wait_for` 外层超时 (compare fan-out + stream open)。
- **chat UI 延后项** `webchat/app.js`+`style.css`: AbortController Stop/中止 + 重试 (`runGeneration` 抽取, 不复发用户消息) + topbar 读 `/api/info` 显真实 default_model。
- **config** `server/config.py`: phase-3 开关全默认 OFF + `kb_root`/`chroma_dir` env 覆盖 (解 §7 开放项, 服务目录自包含)。**main** `server/main.py`: `create_app(app_settings)` 工厂 (单配置源)。
- **deploy/** (写好**不激活**): `deploy.sh` (rsync→`~/sdtm-rag-service/`+uv sync; additive 不碰 .env/.venv; --delete 限子目录) + `com.sdtmrag.api.service.plist.template` (`0.0.0.0`, 指服务目录) + `.env.service.template` + `README.md` go-live runbook; `scripts/gen_password_hash.py` (口令哈希 CLI)。
- **TDD**: `scripts/tests/test_phase3_security.py` (新); 修 `test_ask_stream.py` (fake app 补 `app.state.settings`)。

### 验证
- **287 pytest 全绿**; 新代码 ruff 全清 (router 新增 0 UP041); `deploy.sh` 语法 OK + `--dry-run` 通过。
- **活体 smoke** (临时实例 127.0.0.1:8033/8034, **不碰 8000**): 真 DeepSeek **SSE 621 token 帧穿全中间件 0 error** (纯 ASGI 不破流式实证); 登录流/401/302/`next`/错口令/登出全过; v2 boot health=ok (证 create_app+lifespan 修); **暴力锁 401×5→429** + 锁定中对口令仍 429。两次 smoke 后 8000 healthy。
- **pip-audit**: 发现并**修 starlette CVE-2026-54282/54283** (pin `starlette>=1.3.1` → 1.2.1→1.3.1, fastapi→0.136.3, 全量重测过); chromadb CVE-2026-45829 无修 → **ACCEPTED/MONITORED** (只读·进程内·登录门后·内网)。

### 规则 D 三 lens Workflow (security/code/critic, 异 subagent_type, fresh context) — 0 BLOCKER/HIGH
- 三 verdict 均 FIX_RECOMMENDED; security lens 对抗式探 path-trick/open-redirect 变体/暴力/XFF 伪造, 确认无可利用绕过 + CSP 不破前端资产。
- **8 finding (4 MED+4 LOW) 全修复验**: MED 登录无暴力锁 → 加 `LoginThrottle` (失败计数+指数退避); MED session 7d 无短上限 + `ts` 死字段 → TTL 12h (itsdangerous 服务端强制) + 删 ts; MED `create_app` 配置分裂 → 单配置源 (`state.settings=app_settings` + lifespan 读 it); LOW `_safe_next` 控制符/空白可过 → 收紧; LOW 2 处 `except asyncio.TimeoutError` UP041 → `except TimeoutError`; LOW deploy 模板硬编码路径 → `__SERVICE_DIR__` 占位 + deploy.sh seed 时 sed; LOW dry-run 无 -v → 加 `-v --itemize-changes`。

### 证据 / 决策 / 未做
- 证据 `evidence/checkpoints/phase3_share_hardening.md` + `phase3_share_pip_audit.txt`; retro `RETROSPECTIVE_phase3_share.md` (Rule C 三段); 进度 `_progress_phase3_share.json`; 计划 `PLAN_phase3_share.md`。
- **残余风险** (显式承认): 纯 HTTP over LAN, 口令/cookie 明文可嗅探 → 短 TTL + 暴力锁 + 强口令闸 (CLI <8 拒/<16 警) 缓解; TLS/VPN/Cloudflare Tunnel 路线 §6。
- **未做** (go-live 系统动作, 待用户侧 IT): 翻 `0.0.0.0` / `pmset` 禁睡 / macOS 防火墙 / 装服务目录 plist — 步骤已写进 `deploy/README.md` runbook。go-live 硬阻塞 = IT 内网 IP/主机名 + 安全签字。

## 2026-06-17 KG 重启 SP1 — meta.yaml 元数据层 DONE (brainstorm→spec→plan→TDD→Rule A/D)

### 触发 / 范围
- 路由词「KG 重启 开始任务」→ `KG_ROADMAP.md` (SP1-5 拆分已 ack)。本 session 完成 **SP1 (meta.yaml 元数据层)** = SP1-5 第一个、硬前置。
- 范围 = **纯数据层** (确定性生成 + 验证)。不答题 / 不翻 eval / 不碰 `structured_lookup` (退役是 SP2) / 不碰 `knowledge_base` (只读)。设计 `SP1_meta_yaml_design.md` + 计划 `PLAN_sp1_meta_yaml.md` (用户批准)。

### brainstorming (5 设计决策, 接地 recon workflow 5 路并行侦察)
- 粒度 = 纯数据层 (q103/q104 翻绿留 SP2); schema = 标量 + 变量(name/role/type/core/`ct_codes`/`ct_dict`) + `same_class`(按 Class group-by) + `relations_curated`(机制**仅字面**, 标低保真) + `model_defhome` + `codelists`(只存 term_count); relations = 确定性 core + 策划边; 验收 = 两门 (独立锚对账 + N=8 分层 Rule A); 输出 `data/meta/`。

### 产出 (9 Task TDD, subagent 驱动 + 两段式审)
- `scripts/build_meta.py` — 确定性生成器 (无 LLM, 幂等) → `data/meta/meta.yaml` (64 域 = 63 真域 + DI 桩)。
- `scripts/reconcile_meta.py` — 独立锚对账 (**不复用** spec_loader; VARIABLE_INDEX/INDEX 文本 + 裸 `Order:` grep; anchor drift loud-fail)。
- `scripts/tests/test_build_meta.py` (13 单测) + 证据 `evidence/checkpoints/sp1_meta_audit.md`。

### 重大发现 — reconcile gate 抓到 spec_loader 系统性 bug
- `spec_loader._parse_spec` 的 `### (\w+)` 变量扫描**不在 `## Cross References` / `---` 处停** → 4 个子节标题 (Controlled Terminology/Related Domains/General References/Model Definition) 误当变量, 全 63 域产生 **247 幻变量** (2164 vs 真实 1917)。**独立锚对账揪出** (spec_loader 自我对账永远发现不了 = 反套套逻辑的价值)。手术式修 (startswith 守卫), **全量 300 测试不受扰** (validation/chunkers 等消费者全过)。
- 纠正 recon 错误: 缺 spec.md 的桩域是 **DI** 非 SUPPQUAL; `counts_toward_63 = spec.md 存在` (含 SUPPQUAL → 63)。

### 三门验证
- **Gate 1 reconcile 8/8**: 63 / 1917 / 1523 / 1005 / 37939 / TAETORD→43 / VISITDY→36 / 裸 Order 1917。
- **Rule D** opus 异 type 代码审: build_meta APPROVE (6 LOW 收 3); reconcile REQUEST_CHANGES (1 HIGH anchor loud-fail + 2 MED + 3 LOW) → 修 → 复审 APPROVE; mypy 0 / ruff clean / 300 pytest。
- **Rule A** 独立 opus N=8 分层语义抽检: **PASS** (零 invented 机制 / 零错码 / 零漏数据; mechanism 分布 {null:50, RELREC:2} 与设计 §6 吻合)。

### next
- **SP2** (确定性结构化答题通道: meta.yaml 载内存 → /api/ask 计数/穷举/精确查找走确定数据, q103/q104 翻绿 + 退役 structured_lookup 正则影子 KG)。路由词「KG 重启 开始任务」现指向 SP2 (走同样 brainstorm→spec→plan→impl 流程)。
