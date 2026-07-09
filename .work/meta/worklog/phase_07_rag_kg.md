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

---

## 2026-06-20 KG 重启 SP2 Phase 1 (确定性答题通道) DONE 默认 ON (brainstorm→spec→plan→subagent-driven 14 task)

- **触发**: 用户「KG 重启 开始任务」(2026-06-19 续 2026-06-20)。续 SP2 brainstorming 断点 (5 决策已锁) → 走查全设计 → 定稿 spec → writing-plans → subagent-driven 执行。
- **流程**: brainstorming (接断点确认架构两块, 锁 Q1-Q5 + 2 参数: Rule A N=8 / 闸只硬校验计数) → spec `docs/superpowers/specs/2026-06-19-sp2-structured-answer-design.md` (自审消歧 grounding 位置 + 用户审过) → plan `docs/superpowers/plans/2026-06-19-sp2-structured-answer.md` (18 task TDD; 写前 4 路 Explore 并行侦察代码锚点; self-review 闭 Q4 缺口/修 lifespan 测试范式/pin run_evaluation) → subagent-driven (每组 implementer + spec审 + 质量审 + fix loop, 异 subagent_type)。
- **产出 (Phase 1, 14 task)**: `server/meta_store.py` (MetaStore 载 meta.yaml + 内存反向索引 + 确定性查询 API) + `server/structured_answer.py` (StructuredAnswerer 实体锚定+意图检测+事实装配 + augment_context) + `server/grounding.py` (apply_counting_gate 高精度 v2) + `config.py` flag (默认 ON) + `main.py` (maybe_build_answerer + lifespan) + `router.py` (ask/ask_stream 注入+闸) + `eval/run_eval.py --structured-answer` + `eval/prod_wirein/heldout_probes.py`。370 pytest / ruff 清 / mypy 0。
- **验收 (Task 13/14)**: 140q OFF-vs-ON paired eval (deepseek-chat temp0): **q103 TAETORD→43 / q104 VISITDY→36 翻绿** (fr 0.5→1.0); 检索零回归 (src 99.6%→99.6%; fact 负 delta 逐题核证全为 temp0 噪声/翻译伪降); **0 闸 violation** (闸 v2 oracle)。**Rule D** (critic 异 subagent_type) **APPROVE「safe default-ON」** (0 CRITICAL, 2 MAJOR 非破坏性转 backlog)。**Rule A** 独立 opus **N=8 分层语义抽检 PASS** (4 能力类各 2, 2 题对账原始 KB)。
- **评测暴露并修两缺陷 (规则 A/D 价值实证, 程序门漏)**:
  - **接地闸 v1 36 全假阳** → 整句扫数字把术语数/字符限值/章节号误判为域计数。重建 **v2 高精度** (缺席前提: 正确值在答案出现就跳过 + 双语 kind 词邻近 + 合理性), **36→0** (oracle 复跑 saved 140 答案); 36 案例写进回归测试。Rule B 归档 `evidence/failures/step_13_attempt_1.md`。
  - **q67 codelist 变量计数幻觉** (Rule A 抽检揪出): 答「106 变量」真值 123, 而 fact_recall 子串假阳给 1.0。根因 codelist 只发 domain 计数 CheckableCount 无变量计数 → 补 `codelist_variables` 闸 + 注入显式计数行。
- **决策复盘**: Q5「闸追加更正」方向对但实现 heuristic 欠设计 (两轮返工); 用户被请来基于新证据复议 Q5 → 选「高精度闸 + 保留生产追加」。两阶段 (Phase 1 上线 / Phase 2 缓做) 验证为好决策。复盘 `RETROSPECTIVE_sp2_phase1.md` (规则 C)。
- **backlog (转复盘 §2)**: 词典词变量 (RACE/SEX) 锚定 relevance gate / s05 codelist 元数据注入 / enumerate corpus 列表 / FP2 是否改 eval-log-only / first-seen 属性跨域分歧 (→SP3)。
- **教训**: subagent 多次中途截断 (长评测 / fix 没 commit / eval 仍在跑) — 每次独立核验状态抓到, 长付费评测改用可追踪后台任务自驱。

### next
- **SP2 Phase 2** (退役 structured_lookup 正则影子 KG → 读 meta.yaml, 含 load-bearing `len==6`): 入口 plan §Phase 2 (Tasks 15-18), 已有 spec+plan **直接接 plan 无需 brainstorm**; 零回归门 = 既有 `test_structured_lookup.py` 全套 + retrieval-only paired eval ≥99% + Rule D 一轮。之后 **SP3** (内存图遍历, 关系/影响查询) = 新设计单元需 brainstorm。

## 2026-06-20 KG 重启 SP2 Phase 2 (退役 structured_lookup 正则影子 KG) DONE — 严格行为等价

接 plan §Phase 2 (Tasks 15-18), 无需 brainstorm。把 `server/structured_lookup.py` 的 7 个索引数据源从「init 时正则解析 KB markdown」换成 `data/meta/meta.yaml` (MetaStore)。

### 做了什么
- **重写 `server/structured_lookup.py`** (净 −185 行): `known_variables`/`domain_to_spec`/`domain_longname_to_code`/`var_to_model_defhome`/`ctcode_to_termfile`/`var_to_termfiles` 全改读 MetaStore; 退役 load-bearing **`len(inner)==6` model 表解析** + spec.md Cross-References 正则 + terminology `## Name (Cxxxxx)` 解析 + VARIABLE_INDEX §一/§二/§三 解析 + `_cross_check_vars` 截断回填 + 死代码 `ctcode_to_vars`。**意图检测 / 实体锚定 / `resolve()` / 长名匹配 (含 `[`-guard + slash 变体 + 长短名锚定) 逐字保留**, 只换数据源。唯一仍读 KB 文件的是 ch04 general-assumptions glob (meta 不覆盖 chapters/)。
- **`server/meta_store.py`** 加 2 个纯加法 API: `ct_codes_for_variable(var)` (跨域 union, 区别于 first-seen `variable_attributes`) + `model_defhome_map` property。Phase 1 first-seen 路径未动。
- **`server/rag.py`**: structured_lookup 块懒构造 `MetaStore(settings.meta_path)` 注入 StructuredLookup; **RAGEngine 签名不变** → 另 5 个 RAGEngine 调用点零改动。
- 构造点 3 改: rag.py / `eval/probe_s3_longname.py` / 测试 fixture (新签名 `StructuredLookup(kb_root, store)`)。

### 零回归门 (穷举快照等价, 比 retrieval eval 更强)
- 新工具 `eval/prod_wirein/sp2p2_equiv_snapshot.py`: 同一脚本跑旧码/新码, dump 7 个 map + `resolve()` 在**穷举语料** (140 v3 题 + 全量 1523 变量/1005 CT/63 域扫描 = 9891 查询) 上的输出, 逐字节 diff → **8/8 maps + 9891/9891 resolve() identical**。理由: structured_lookup 只经 union-add 影响检索, cosine/hybrid 未碰 → resolve 同 ⇒ 检索确定性同 (∴ 不跑带 embedding 非确定的 live retrieval eval, 快照是 superset)。
- **迁移前预分析 4 风险点** (锁定唯一 divergence FOCID): var_to_termfiles 必须**跨域 union** 才与旧 524 逐项同 (FOCID 的 C119013 只在 OE 域, first-seen 丢) → 加 `ct_codes_for_variable`; model_defhome meta 与旧 `len==6` 图 **59=59 逐项同** → 退役安全; domain_longname 62/63 同 (SUPPQUAL `[`-guard 排除); ctcode_to_termfile 1005=1005 同。
- 完整套 **375 passed** (test_structured_lookup 39 [36 + 3 新漂移闸] + test_meta_store 20 [+2 新]) + held-out 探针 4/4 + ruff/mypy (改动文件) clean + 运行时 smoke (真 `RAGEngine(structured_lookup_enabled=True)` 构出 meta-backed lookup) + 端到端 union-add 实证 (`retrieve` union-add terminology/core/ae.md)。

### Rule D (Task 17) — APPROVE
异 subagent_type (oh-my-claudecode:code-reviewer, opus) 对抗式独立审 **APPROVE 0 BLOCKER/HIGH/MEDIUM** (1 LOW + 2 NIT)。reviewer 真独立: 从 git HEAD 重建旧码同进程对跑 + 从零重生 golden (逐字节同证非伪造) + **自建 4177 查询对抗语料专门绕开 writer 语料 → 0 divergence**。
- NIT (tuple name-slot 旧/新不同但只 termfile 可观测) → 加 docstring 注记。
- LOW (meta/KB 漂移自愈丢失: 旧码实时重解析 KB 自愈, 新码读 meta 会静默漂移) → 加 `TestMetaKBDriftGuard` 域级闸 (spec 路径在盘 + 域数对账 + ch04 存在); var/CT 级仍需手动 `scripts/reconcile_meta.py` (KB 重建后跑) — 列入 backlog。

### 产出
- 代码: `server/{structured_lookup,meta_store,rag}.py` + `eval/probe_s3_longname.py` + 测试 `scripts/tests/test_{structured_lookup,meta_store}.py`。
- 工具: `eval/prod_wirein/sp2p2_equiv_snapshot.py` (等价 harness, 可复用)。
- 文档: `RETROSPECTIVE_sp2_phase2.md` (规则 C 三段) + `evidence/checkpoints/sp2_phase2_{paired_eval,ruleD_review}.md`。

### 决策复盘
- D1 用穷举快照等价证明替代 live retrieval eval (确定性 superset, 无 embedding 非确定噪声) = evidence over assumptions。
- D2 var_to_termfiles 用跨域 union 而非 first-seen (FOCID 暴露同一实体「first-seen 属性」≠「全域聚合」)。
- D3 保留 ch04 glob (meta 未覆盖 chapters/, 不为「全 meta 化」硬塞)。
- D4 rag.py 懒加载不改 RAGEngine 签名 (low-churn, 不碰 Phase 1 answerer 的 MetaStore)。

### next
- **SP3** (关系/影响查询, meta.yaml 之上内存图遍历 networkx/纯 Python) = **新设计单元, 必须先 `superpowers:brainstorming`** (HARD-GATE, 无现成 spec/plan)。SP4 (可选 Neo4j) / SP5 (可选 图增强校验)。路由词「KG 重启 开始任务」现 → 读 KG_ROADMAP + memory `project_kg_decision` → 接 SP3 brainstorm。

## 2026-06-20 KG 重启 SP3 (关系/影响图查询) DONE — 内存图引擎 + NL 答题 默认 ON

全流程 brainstorm(Q1-Q5)→spec→plan(16 task)→subagent-driven(per-phase impl + per-phase 异type 独立审 + 最终全量 Rule D)→Rule A N=8。

### 做了什么
- **图引擎 (数据层)** `server/graph_engine.py`: `GraphBackend` Protocol + `DictBackend` (over MetaStore 反向索引, 3 原语: nodes_of_type/out_neighbors/edge_data) + `GraphEngine` (impact_of_codelist/variable · variables_in_min_domains · most_shared_codelists · same_class_domains · codelist_co_users · domain_relations · domains_in_class/class_sizes)。拓扑经 backend (可换 networkx/Neo4j), 节点元数据经 MetaStore。MetaStore 加 `same_class`/`relations_curated` 访问器。
- **NL 图答题** `server/graph_answer.py`: `detect_graph_intents` + `GraphAnswerer.resolve()→StructuredFacts|None`。NL 暴露 4 意图: impact (codelist/variable→域/变量集合 + 基数接地闸) · relationship-discovery (单域→same_class 权威块 + curated relations advisory 块非穷尽) · aggregate (variables_in_min_domains[domain-guarded] + most_shared_codelists)。
- **集成** `structured_answer.py`: `StructuredFacts.advisory_block` (低保真单独 header) + `merge_facts` (去重) + `CompositeAnswerer` (合并 SP2+SP3 resolve) → `maybe_build_answerer` 组合; **router/ask_stream/run_eval 调用点零改** (composite 透明)。`grounding.py` 加 impacted_domains/impacted_variables kinds (rare-subject 安全)。config `graph_answer_enabled` 默认 ON。run_eval `--graph-answer`。
- **engine-only 未接 NL** (deliberate): domains_in_class/class_sizes (class 名常用词→NL 检测脆弱) + codelist_co_users + model_defhome 邻接 (留 SP4/API)。

### review 揪出并修的真缺陷 (印证写审隔离 + at-scale 独立扫)
- **HIGH (Phase2 独立审, 我 4 样本 smoke 漏)**: 140q 零污染门破 5/140 (class-roster 意图 + relationship narrative 撞散文)。修: **从 NL 去掉 class-roster** (class 名常用词固有脆弱; 用户决策非 whack-a-mole; 引擎保留) + relationship 加单域+definition-verb 守卫。
- **MED**: class_domains 接地闸 reintroduce SP2 36→0 假阳 (common-word subject collision) → ungate, 闸只锚 rare-subject (var/C 码); degenerate 0-impact codelist (858 个) 注入误导 → 跳过; "more than N" off-by-one → strict n+1。
- 意图振荡 (修 5 题撞 5 题) 时**停 subagent、自己诊断根因 (class 名常用词)、把 scope 岔路交用户** (反 example-tuning)。

### 验收 (三门 PASS)
- **程序门**: 引擎 vs raw meta.yaml 穷举对账 (反套套) + 意图 must-fire/not-fire 电池 + **140q 零污染 0/140 (composite ON==OFF byte-identical, reviewer 独立重跑)** + 接地闸单测 + 盲写 10 题 NL 端到端 (基数对账 meta.yaml) + 全套 **414 passed** + mypy/ruff (SP3 文件) clean + held-out 探针。
- **Rule D**: 三轮异 subagent_type APPROVE (Phase1 / Phase2[REQUEST_CHANGES→修→APPROVE] / 最终全量), 0 BLOCKER/HIGH; reviewer 自建 from-scratch `RawBackend` 证 seam byte-identical。证据 `evidence/checkpoints/sp3_ruleD_review.md`。
- **Rule A**: 独立 scientist N=8 分层 (4 能力族×2) vs meta.yaml+KB 双源核验 PASS (含 degenerate 抑制 / advisory 隔离 / held-out 泛化)。证据 `evidence/checkpoints/sp3_ruleA_audit.md`。

### 产出
- 代码: `server/{graph_engine,graph_answer}.py` (新) + `structured_answer.py`/`grounding.py`/`meta_store.py`/`config.py`/`main.py`/`run_eval.py` (扩展)。
- 测试/工具: `test_graph_engine.py`/`test_graph_answer.py` + `eval/prod_wirein/sp3_graph_probes.py` (held-out + 140q 零污染) + `eval/test_set_sp3_graph.yml` (盲写 10 题)。
- 文档: spec/plan `docs/superpowers/{specs,plans}/2026-06-20-sp3-graph-queries*.md` + `RETROSPECTIVE_sp3.md` + 证据 2 份。

### next
- **SP4 (可选)** Neo4j+Cypher+可视化 / **SP5 (可选)** 图增强校验器 = 新设计单元需 brainstorm。可选小补: codelist_co_users NL 接入 (Q2 选过, 干净可加) / mechanism:null back-fill / SP2 同源 degenerate 0-impact 修。**SP1-3 已交付 KG 全部「能力」**; 若不要可视化/校验器, KG 主线收口。路由词「KG 重启 开始任务」→ SP4/SP5 brainstorm。

## 2026-07-07 服务目录迁移 ~/sdtm-rag-service → ~/MyProject/sdtm-rag-service

- 用户要求: deploy 目标目录不放家目录根, 挪到 `~/MyProject/` 下。目录当时为空 (仅 `deploy.sh --dry-run` 的 `mkdir -p` 残留空 `data/`, go-live 未发生), 移动零风险。
- 更新 8 文件默认路径 (不改则下次 deploy 会在根目录重建): `deploy/deploy.sh` DEST 默认值 → `$HOME/MyProject/sdtm-rag-service` / `deploy/com.sdtmrag.api.service.plist.template` 4 处硬编码 / `deploy/.env.service.template` / `deploy/README.md` (runbook) / `scripts/gen_password_hash.py` 提示 / `server/config.py` 注释 / `DEPLOY_PLAN.md` / `PLAN_phase3_share.md`。
- 验证: `bash -n` PASS + `--dry-run` 确认 DEST=新路径 + 现役 8000 health 200 不受影响 (launchd plist 指 repo 树, 与服务目录无关) + 全仓 grep 无旧路径残留 (worklog/PROGRESS 历史记录按 append-only 惯例保留原文)。
- go-live 语义不变, 仍待 IT 内网 IP + 签字; `SDTM_RAG_SERVICE_DIR` env 覆盖机制不变。

## 2026-07-07 AGG (aggregate 独立通道) DONE 默认 ON — 价值 eval 榨值建议落地

全流程 brainstorm(3 决策)→spec→plan(10 task)→subagent-driven(每 task fresh implementer + 异 lane 审查)→Rule D 全量(fable 异 type)→Rule A N=6。**用户批准「诚实披露」收口口径。**

### 做了什么
- **通道**: `server/aggregate_answer.py` (新) — `detect_aggregate_intents` (threshold/superlative 两意图, 9 语言形状类 + `_normalize_numbers` 拼写数字归一 + word-boundary anchor 同义词 datasets/vars) + `AggregateAnswerer` (装配逐字平移 SP3, golden 单测钉死, 顺修「抓第一个裸数字」遗留 bug)。注册 CompositeAnswerer (SP2→AGG→SP3); `graph_answer.py` 删 aggregate 回归纯图; flag `aggregate_answer_enabled` 默认 ON (env 可回滚); run_eval `--aggregate-answer`。
- **评测资产**: 3 轮盲写 held-out (16 题/轮, 烧毁轮全保留作回归) + **novelty-check 工具** `eval/novelty_check.py` (内容词 Jaccard, Rule D 流程缺口的沉淀) + 补充轮 12 题 + e2e 26 题 (heldout+kgval 回归) + `agg_fire_probe.py`/`analyze_agg_e2e.py`。

### 五门与诚实口径
- 单测 48 (must-fire 9 形状类 / must-not-fire 上界·版本号·散文·跨从句·量化 dozen) + 全套 460/460; 140q 零污染 **0/140** (5 轮 pattern 扩展每轮重跑, artifact 落盘); **ds e2e Δ+41.7pp** (held-out OFF 58.3%→ON **100%**, 26 题零退化, 审查者独立复算逐数吻合); Rule A N=6 双源零错配。
- **fire-rate 门史**: r1 4/16 FAIL → 6 形状类修 → r2 12/16 FAIL → +N-plus/top-N → r3 15/16 门过 → **Rule D 抓出盲写收敛重叠** (r3 与烧毁集 4 逐字+~7 近逐字) → novelty 补充轮 2/12 → anchor 词汇修 → **6/12 (阈值族 4/4=100%, 最高级族 2/8=25%)**。2 次失败归档 `failures/agg_attempt_{1,2}.md` (规则 B)。
- **已知限**: KL-1 双插入 / KL-2 隐喻最高级 (champion) / KL-3 "most often" 无 the / KL-4 最高级长尾造册; 注入侧 backlog MED-1/2/3 (维度错配优先)。安全模型: 静默=与无通道等价, 永不致害。

### 关键学习 (印证规则 D/A)
- **盲写收敛**: 同一 need card 跨轮盲写措辞收敛 → "fresh held-out" 独立性被高估; 全部 task 审查都没抓到, Rule D 全量审 (异 type + 最强模型) 抓出 → fire-rate 门必须带 novelty check (工具已沉淀, 下次直接用)。
- **词法天花板**: 每轮盲写挖出新最高级同义表达 (3 数据点); 用户决策不追 whack-a-mole, 长尾等 dogfood ⚑ 真实信号。
- Reviewer 对抗式探针 2 轮抓 4 个测试盲区真缺陷 (负向守卫只护一个分支 / 量化 dozen 错数值注入 / 跨从句过宽 / 版本号误触发); 修复者反过来抓出 reviewer 处方本身的洞 ("2 dozen" 间隙词路径) — 双向制衡有效。

### 产出
代码 5 文件 + 测试 2 文件 + 评测资产 9 文件 + 证据 6 文件 (checkpoint/RuleD/RuleA/零污染 artifact/2 failures); spec/plan `docs/superpowers/{specs,plans}/2026-07-07-agg-*.md`; 15 commits (c42fff7..收口)。

### next
- SP4/SP5 可选 (产品 UX 理由, 需 brainstorm 硬门) — 用户已预告要做「KG 重启执行落地」; AGG backlog (KL-4 长尾 + MED-1/2/3) 等 dogfood 信号。

## 2026-07-08 SP4 (Neo4j 探索层) brainstorm + spec 批准 — 待 writing-plans (新 session)

- 用户决策: **SP4+SP5 两个都做, SP4 先**。brainstorm 3 决策: ① 底座 **Neo4j** (用户否决纯前端推荐项, 要完整愿景; 生产答题继续内存 DictBackend, Neo4j 纯探索层) ② 安装 **brew + launchd** (核实机器无 Docker) ③ 交付面 **数据层 + Neo4j Browser + Cypher 查询库** (webchat Graph tab 二期)。
- Spec `docs/superpowers/specs/2026-07-08-sp4-neo4j-exploration-design.md` (d318874) 用户批准。要点: 4 节点/5 边 SP3 同构建模 (逐域权威值在 HAS_VARIABLE 边属性, curated 边 advisory 标注), Term 不物化; 四道验收门 (独立对账 N≥8 / cookbook golden / **停机 byte-identical 生产不受扰** / Rule D); 生产隔离硬约束 (server/ 零 neo4j 依赖, `grep -r neo4j server/` 零命中入门)。
- **接续 (新 session)**: 读 spec → 直接 `superpowers:writing-plans` (不重新 brainstorm) → subagent-driven 执行 (照 AGG 模式)。KG_ROADMAP 恢复方式行 + memory `project_kg_decision` 均已更新指针。

## 2026-07-09 KG 重启 SP4 (Neo4j 探索层) DONE — brew+launchd 本机探索层, 数据接地偏差 D1-D4 披露

全流程 spec (批准 2026-07-08) → plan (9 task) → subagent-driven (每 task fresh sonnet implementer + task 内 review-fix 循环) → Rule D `feature-dev:code-reviewer` 异 type 全量审。**用户全程要求「SP4+SP5 都做」, SP4 先, SP5 待另起 brainstorm。**

### 做了什么
- **数据层**: `scripts/build_neo4j.py` — 纯函数 `extract_graph(meta) -> rows` (meta.yaml → 5 节点标签/5 边类型行, golden-anchored TDD) + 导入层 `import_graph(driver, rows)` (全清 `MATCH(n) DETACH DELETE n` + UNWIND 批量写 + 5 唯一性约束 + 写计数器自校验 `created==input` fail-loud, 幂等)。
- **对账**: `scripts/reconcile_neo4j.py` — 独立码路 (禁 import `build_neo4j`/`MetaStore`/`GraphEngine`, 只用 `yaml.safe_load` + neo4j driver 读库), Gate 1 = Rule A lane。
- **查询库**: `docs/cypher_cookbook.md` (7 条锚定 Cypher 查询, APOC 缺失→plain-Cypher 变体) + `eval/prod_wirein/sp4_cookbook_golden.py` (锚定生产 `GraphEngine`/`MetaStore` 等价 lane, Gate 2)。
- **运维**: `deploy/com.sdtmrag.neo4j.plist.template` (沿用 `com.sdtmrag.{api,ui}` 命名族, localhost-only 7474/7687) + `deploy/README.md` §Neo4j runbook (brew 安装/heap 配置走 `neo4j.conf` 非 docker 式 env var/验证)。
- **依赖隔离**: pyproject `[project.optional-dependencies].dev` 追加 `neo4j>=6.2.0` (不进 `[project.dependencies]`); `.env.example` 追加 NEO4J_* 空值行。
- **生产隔离验证**: `eval/prod_wirein/sp4_isolation_probe.py` (12-query battery, Gate 3)。

### 4 数据接地偏差 (D1-D4, plan 期程序实测 meta.yaml 抓出)
D1 C66742 影响域数 spec 笔误 44→实测 41 (变量数 123 吻合) / D2 USES_CT 边加 `domains` 属性 (FOCID/C119013 逐域精确 vs closure 3 域) / D3 新增第 5 节点标签 ModelChapter (DEFHOME 目标是 model 章节文件非 Domain) / D4 18 个 model-only 变量也建 Variable 节点 (`model_only: true`, 否则 DEFHOME 静默丢 18 边)。D2 由 3 条独立代码路三角验证一致; D4 经证不污染计数类 cookbook 查询。

### 四门
- **Gate1 reconcile**: 41/41 `[OK]` exit 0 + 幂等 (两建 snapshot 5254 行逐字节同 empty diff) + N=9 分层邻域抽检 + 2 确定性锚点。`sp4_reconcile_gate.txt`。
- **Gate2 cookbook golden**: 15/15 PASS (7 drift + 8 golden) exit 0, 锚定生产 GraphEngine/MetaStore 等价 lane。`sp4_cookbook_golden.txt`。
- **Gate3 生产隔离**: Neo4j 停机全套 **477 passed** exit 0 + composite off/on **byte-identical** (6225B, 9/12 battery 双态一致) + `server/` 零 neo4j 引用 (import-grep + 字面量-grep + 运行时 `sys.modules` 三重 clean)。`sp4_isolation_gate.txt`。
- **Gate4 Rule D**: `feature-dev:code-reviewer` 全量审 `b2e2f92..6dc123c` (11 commits) → **APPROVE_WITH_NITS** 0 BLOCKER/HIGH, 1 MED (localhost 绑定证据缺口) + 2 LOW 均修补验证。`sp4_ruleD_review.md` + `sp4_localhost_binding.txt`。

### 关键学习
- **plan 期写 golden 数字表天然强制实测**, D1-D4 都是这一步抓出而非 brainstorm 期臆测 — plan 阶段是"逐字段核对"的正确粒度, 早于此 (brainstorm) 过早优化, 晚于此 (review) 要走返工。
- **纯函数/导入层分层是 Gate 3 停机全绿的架构性前提**, 非事后补丁 — `extract_graph` 零 I/O 独立可测, driver 写入薄到只做 I/O+自校验。
- **两 lane 分工 (reconcile 独立 yaml vs cookbook GraphEngine 等价) 真互补**: reviewer 验证 `expected_from_yaml` 遍历结构不同形 (非表面镜像), 对 D2 难例三角验证。
- **Task 7 首派遭 API 登出中断** — 复用未提交探针脚本 (与 brief 逐字比对一致) + 诊断根因 (pytest 命令行 `-q` 叠加 `pyproject.toml addopts=-ra -q` → verbosity -2 → pytest 9.x 静默省略汇总行), 干净重跑收口, 无需重写。
- **限制诚实披露**: Term 节点未物化 (spec §3 backlog) / webchat Graph tab 二期 / 两 lane 同源 meta.yaml (抓代码路径 bug 非源头真值, 源头真值是 SP1 `reconcile_meta.py` 职责) / heap 配置走 `neo4j.conf` 非 env-var (brew 原生安装 docker 式 env var 无效, 已验证)。

### 产出
代码 2 脚本 + 1 plist + 1 runbook 段 + 1 cookbook + 2 评测工具 + pyproject/.env.example 改动; 证据 6 文件 (`sp4_{reconcile_gate,cookbook_golden,isolation_gate,ruleD_review,localhost_binding,neo4j_summary}.{txt,md}`); `RETROSPECTIVE_sp4.md` (Rule C 三段+); 11 commits (`9de80ee..0b8ac79`)。

### next
- **SP5** (图增强校验器: impact/跨域完整性/CT 级联一致性接进 Validator, DESIGN §5.6) = **新设计单元, 必须先 `superpowers:brainstorming`** (HARD-GATE, 无现成 spec/plan)。路由词「KG 重启 开始任务」现 → 读 KG_ROADMAP + memory `project_kg_decision` → SP5 brainstorm, 或 KG 主线 (SP1-3+AGG) + 探索层 (SP4) 已全收口。

## 2026-07-09 KG 重启 SP5 (图增强校验器) DONE — KG 重启全线收官

承接已批 spec (74c27a0) + plan (2d5b5b9) → 执行 8-task plan (superpowers:executing-plans, TDD 逐 task commit)。给现有 Validator (Phase 1C, 7 规则) 接进 DESIGN §5.6 三类图增强跨域校验。**全 advisory (WARN/INFO 绝不 ERROR), 确定性只读内存 GraphEngine (over meta.yaml), 不碰 Neo4j。单域 `/validate` 零改动零回归。**

### 三类检查 (`server/graph_validator.py` 新, 3 纯函数 + `run_graph_checks`)
- **impact** (GIMPACT/INFO): 变量或其 codelist 跨 ≥10 域 → 提示高 impact, 从不 pass/fail。
- **completeness** (GXDOM/WARN): 提交域经**显式 mechanism=='RELREC'** 链接的伙伴域缺席 → WARN。
- **CT cascade** (GCASCADE/WARN): ≥2 提交域共享同一 codelist, 实际数据值集合跨域不一致 → WARN (列各域 distinct 值)。

### 架构接线
- `report.generate_study_json` (study-level 聚合: worst-of verdict + 图层 findings, 纯追加)。
- `POST /api/validate-study` (多 UploadFile, 逐域 parse+validate + 跑 3 类跨域 check; 单域 `validate_dataset` 函数体逐字节不变)。
- `ui/streamlit_app.py` study 多文件 uploader + 报告渲染 (现有单域上传不动)。

### 开工数据核验 (verification-first, 抓 plan 3 处硬伤, 归档 `sp5_attempt_1.md`)
plan 把测试/fixture 实体写死, 开工用 MetaStore/GraphEngine 逐条打表: ① **MHSER 实际不绑任何 codelist** → cascade 对换 MHPRESP (同绑 C66742); ② **AE 的 RELREC target 是 {CM, PR} 两个**非一个; ③ **pass study {AE,CM,MH} 非 RELREC-闭合** (AE→PR 悬空误报) → 改 RELREC-闭合的 {AE,CM,PR}。全改测试数据对齐真值, **实现逻辑一字未改去凑**。另修 plan Task 3 fixture 列长笔误 (pandas ValueError)。

### Rule A/D 双抓 M1 — spec back-fill 撤销 (重大)
spec §3.2 设计 mechanism back-fill (null-mech + target∈{RELREC,RELSPEC,RELSUB}→mech=target)。**实测 meta.yaml: 这类 null-mech 边 (LB/BS/IS/MB/MS→RELSPEC "specimen hierarchy") 的 target 是关系数据集本身而非伙伴域**, back-fill 在 `mech=='RELREC'` 守卫下是死码, 放宽会产 "X RELSPEC-linked to RELSPEC, absent" 无意义 WARN。**收窄 completeness 为仅显式 RELREC** (真实数据行为逐字不变: 全域仅 AE→CM/PR 两条 RELREC 边)。教训: 连"确定性 back-fill 非臆造"也须真实数据打表验证语义。

### 三门
- **程序门**: 全套 **493 passed 零回归** (单域 validate 函数体逐字节 IDENTICAL) + golden pass/fail 精确命中 ({AE,CM,PR}=0 graph-WARN / {AE,MH}=GXDOM(CM)+GCASCADE(C66742)) + 新码 `graph_validator.py` ruff+mypy 干净。测试 16 (9+2+3+2)。
- **Rule D** (异 type `pr-review-toolkit:code-reviewer`, opus): **APPROVE_WITH_NITS 0 BLOCKER/HIGH**。构造级证 advisory-only (`generate_study_json` graph 侧 `g_err` 恒 0 → 图层永不顶 FAIL); 诚实性偏保守核实 (router 11→12 唯一新增 idiomatic B008 / report 5→4 反清旧 F401 / mypy +0); 1 MED (M1) 已修 + LOW (dead param 已删 / test_validator.py 不存在订正 / impact 通用标识符噪声接受)。
- **Rule A** (异 type `general-purpose` scientist, opus): **PASS 8/8 零 mismatch**。raw-yaml `safe_load` 自建索引算 EXPECTED (不 import graph_validator / 不用 MetaStore-GraphEngine 算期望), ACTUAL 跑 run_graph_checks, Finding 四元组逐字全串匹配。独立复算 USUBJID=55 / C66742=41域123变量 / AE RELREC={CM,PR} 自核无误。

### 诚实缺口 (披露)
completeness 真实触发面极窄 (全域仅 2 条 RELREC 边) / CT cascade 有合法误报面 (advisory 缓解) / impact INFO 含 STUDYID/DOMAIN/USUBJID 通用标识符噪声 (未硬编排除避 example-tuning, 留 dogfood) / 无真实数据用合成 fixture / 每请求重建 GraphEngine (LOW 接受) / 未暴露 go-live webchat + back-fill 不写回 meta.yaml (范围外)。

### 产出
代码 4 文件改 (graph_validator 新 + report/router/streamlit 追加) + 测试 4 文件 + 合成 fixture 5 csv; 证据 `evidence/checkpoints/sp5_{summary,ruleD_review,ruleA_audit}.md` + 偏差 `evidence/failures/sp5_attempt_1.md`; `RETROSPECTIVE_sp5.md` (Rule C 三段); commits `c871b04..HEAD` (7 task + 1 Rule D/A fix)。

### next
**KG 重启全线收官 — SP1-5 + AGG 全 DONE。** 路由词「KG 重启 开始任务」无剩余单元, 子项目线关闭。未来可选小补 (codelist_co_users NL / mechanism 写回 meta.yaml / webchat Graph tab / study 校验对外 / impact 降噪) 均属新设计单元, 需另起 brainstorm。
