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

---

## 2026-07-10 SP6 (隐性关系挖掘 + 网状富节点查看器) DONE — 收官后新设计单元, 合并 main

- **触发**: 用户想「看隐性关系」(如 RECIST 肿瘤评估 PR→TR/MI→RS→TU 数据流) + 把 KG 查看器从树状升级成网状点击展开、富节点带详情。属 KG 收官后的新图能力单元, 走完整 brainstorm→spec→plan→实现。
- **决策 (brainstorm 4 项)**: 定位=**探索线索·证据锚定** (advisory 非权威); 关系三类 (数据流有向 / 显式链接 RELREC / 共现无向); 广度=试点肿瘤簇 TU/TR/RS/PR/MI + 一跳邻居; 富节点详情=混合 (离线内嵌 + 可选联网 RAG)。spec `docs/superpowers/specs/2026-07-10-sp6-implicit-relations-networked-viewer-design.md`, plan `docs/superpowers/plans/2026-07-10-sp6-implicit-relations-networked-viewer.md`。

### 交付 (subagent-driven 9 task + 硬化, 合并 main `247fd53`)
- **挖掘管线** `scripts/mine_implicit_relations.py`: 从 IG 散文 (`knowledge_base/domains/*/{assumptions,examples}.md`) 挖 `data/meta/implicit_relations.json` = **30 边 (12 data_flow + 9 explicit_link + 9 co_occurrence)**。确定性优先: explicit_link=RELREC 正则 / co_occurrence=计数 / 仅 data_flow 用 LLM (deepseek)。**分层反捏造闸**: gate1 逐字引文命中源文件 → **gate1b target 必须在引文里出现 (确定性反捏造)** → gate2 对抗裁判 (fail-closed on inconclusive) → 置信≥0.6 → 每无序对 ≤2。**绝不写 meta.yaml** (硬软彻底分层); 被毙边归档 `failures/sp6_rejected_edges.json` (Rule B)。
- **查看器** `scripts/build_kg_viewer.py` → `kg_viewer.html`: 新增 **explore 网状点击无限展开** (EXPLORE_CAP=40 防毛线球) + **两层边线型区分** (数据流实线+箭头 / 显式链接绿虚线 / 共现点线 / 硬关联灰实线, 非仅颜色) + **富节点分层关系面板** (跨域 CURATED + 推断分层, 带 tag/置信/✓核验) + **点推断边看逐字 IG 引文证据弹窗** (quote + source_file:line + 置信 + 核验) + 可选 **RAG 深入解释** (探活 /api/health, graceful-hide 离线)。

### data_flow 标定 saga (核心教训, 进 anti-cheating 谱系)
LLM 挖有向 data_flow 本质吵: 首跑 **0** 条 (fail-closed judge + 精确引文匹配过严) → 用户选放松重跑 **24** 条, 但 opus 独立 Rule A 抽检 (N=8) 发现 **~50% 是「引文逐字真、但 target 是捏造的过度解读」** (如 FT→LB 引文根本没提 LB, MI→EG, RS→TU) → 加**确定性「有向边 target 必须在引文出现」闸 (gate1b, no-LLM) + 去重 + judge 复位 fail-closed → 12 条干净** (Rule A 复审 N=10 **0 FAIL / 0 WEAK**)。确定性通道 (RELREC/共现) 全程净。**结论: 确定性反捏造闸 > 软化 LLM 裁判**。核心肿瘤流 PR→MI/TR↔TU/TR↔RS/TR→PR 全在且可点开看原文。

### 三门 + 硬化
per-task TDD 审阅 (每任务 implementer+reviewer, 多轮修) + **Rule A opus 独立语义抽检 (Rule D 隔离) 复审 PASS** + **opus 全分支终审 READY TO MERGE 5/5 不变量** (不碰 meta.yaml / 反捏造闸链非旁路 / 确定性 / 自包含+RAG graceful / 测试真实) + 2 条 defense-in-depth 硬化 (IMPL_PATH 可 patch → test 不动冻结数据 / DATA JSON 注入转义 `<`)。521 passed。SDD ledger `.superpowers/sdd/progress.md`。

### next
**SP6 收口。** 隐性关系是 advisory 层与 meta.yaml 硬软分层。可选扩展 (全 63 域 / 更多边类型 / webchat 嵌图 / RAG 常态化) 均属新设计单元, 需另起 brainstorm。合并 main 未 push (用户选本地合并)。


---

## SP7 KG 查看器 UX 重构 (2026-07-24) — subagent-driven 9 task + fit/visual/polish + ovlabel

用户抱怨 `kg_viewer.html` "点一下到处飞到处弹"。诊断: 力导向物理常驻 (`frame` rAF 循环) + 每次交互全量重排 (`seed` 螺旋播种 + `alpha=1`)。重构为**每视图确定性布局 + 缓动补间 + 无常驻物理**。分支 `kg-viewer-ux-redesign` (e6f7fe1 → merged)。spec/plan `docs/superpowers/*2026-07-24-kg-viewer-ux*`。

### 交付
- **源码拆分**: 单文件 `TEMPLATE` → `sdtm-rag/viewer/{template.html,style.css,layout.mjs,app.js}`, build 单遍 `re.sub` 内联 (产物仍零依赖离线单 HTML; `TEMPLATE` 模块属性保留供既有 pytest)。**勿手改 `kg_viewer.html`, 改 viewer/* 重新生成。**
- **纯定位模块** `layout.mjs` (DOM-free, `node --test` 15 例): positionOverview(放射星座) / positionDomain(左→右分层轨道) / positionImpact(轮辐) / positionExploreFresh(ego 雷达 BFS 分环) / positionExploreAccumulate(锚定累积)。
- **补间引擎** `animateTo` 替代物理; 退役 tick/frame/seed/物理常数。
- **explore 锚定累积**: 展开只加新邻居到 anchor 周围, 已有节点零位移 (实测 MAXΔ=0.00px; 代数证明 accumulate value-copy → start==target → lerp 塌缩到 a)。
- **精密仪器视觉**: 发丝网格 / 信号色 amber(落 8 类色外) / 等宽码值 / 标线环 reticle / 边辉光 / 面板棱; 暗色优先双主题, CVD `--c1..--c8` 保留。
- **fit-to-content** 自动取景 (content-key gate: 换视图/域/码表/seed 重取景; explore 展开不重取景; 整理/resize 重取景)。
- **overview 域码按需显隐** (hover 焦点+邻居 / 缩放 T.k≥1.3 全显; 解 Findings 30 域标签重叠 — 用户决策)。
- 面板 sticky 头 (负 margin flush) + 搜索回车居中。

### 验证 / 治理
- `node --test` 15/15 + `pytest` 6/6 (含新 `test_no_persistent_physics`) + 全仓 525 无回归; `kg_viewer.html` 与源逐字节一致 (regen no-op 反复查)。
- **规则 D**: 每 task executor/reviewer 异 subagent 异 session; **opus 全分支终审 READY WITH FOLLOW-UPS** (6 硬不变量全 HOLD: no-explode/纯函数/零依赖/CVD双主题/物理删净/layout 未被视觉触碰)。
- **规则 B**: review 抓到的真缺陷当轮修 — T3 拖拽不重绘 CRITICAL (draw() 只在物理循环) / T8a 重生成 html 脱漏提交 CRITICAL (HEAD 静默退回旧逻辑) / T9 sticky 双 padding。轨迹 `.superpowers/sdd/progress.md` + `task-*-report.md`。
- **规则 C**: RETROSPECTIVE `docs/superpowers/2026-07-24-sp7-kg-viewer-ux-RETROSPECTIVE.md` (三段)。evidence `sdtm-rag/evidence/checkpoints/kg_viewer_ux_redesign.md`。

### 关键教训 (进谱系)
- **"生成物必须与源同步" 当硬约束反复查**: T8a fix 只提交 app.js 漏提交重生成 html → HEAD 静默退回旧逻辑, headless 却 PASS (测的是未提交工作区)。派单必须 `git add 源+产物` 且 commit 后 status 必空回贴。
- **controller 自写 spec 也有 bug 且会被忠实实现**: fit `freshView` coarse `cur.v`-only / sticky 漏负 margin / 整理·resize 漏重取景 → 审阅者(实测 29px)+实现者(主动 flag)比 brief 更靠谱。
- **headless 验证陷阱**: `--virtual-time-budget` 挂 rAF; 晚触 resize→render 清面板/重置 .zoomed; CSS `transition` 令 sync opacity 读数偏 0 → 用 `transition:none` + sync 读破之。

### next
SP7 收口, 合并 main。overview 密集类曾评估"松包破 nearest-hub 不变量" → 用户选 hover/缩放显域码 (已实现)。视觉偏克制, 若要更鲜明性格可再加强 (已知方向)。可选扩展 (整理/resize 已修; M2/M3 已闭) 无剩余单元。

---

## SP7.1 查看器间距重排 (2026-07-25) — Tier 1, 用户反馈"有些点离得太近看不清"

**症状 (实测截图确认)**: 总览里每类的域挤在固定 ±0.42rad 楔形内, 最内环 r=46px → 6 个点只有 38px 弧长可分而节点直径 18px, Findings 20+ 域糊成一坨; 域钻取两列只隔 70px, `AEHLGTCD` 这类长变量名横向撞; explore 4 个节点被 fit 上限 2.2 放大成海报。

**改法 — 从"固定角宽塞节点"翻成"最小间距反推布局"** (`viewer/layout.mjs` + `app.js`, build 重生成):
- 新增 `ringPack()`: 给定最小圆心距 (域 38 / explore 62 / 变量 30 / 码表 42), 按半径反推每环容量, 放不下自动外扩一环。
- 总览改**扇区制**: 每类独占扇区 (跨类不撞), 宽度按域数加权 (基数 10 保底, 大类不挤死小类); 枢纽环半径由"最窄扇区放得下类名 ~110px"反推; 类名移到枢纽**内侧**避开域环。
- 域钻取: 每列 22 行自动分列 (60 变量 → 3 列), 列宽 150, 码表列偏移 200 / 纵距 42。
- explore: BFS 环半径取 `max(深度名义值, 该环节点数所需周长, 上一环+最小环距)`; 累积展开槽位半径随新节点数放大, 一圈放不下外推一圈。
- fit: 包围盒计入节点半径+标签占位; 缩放上限 2.2 → 1.35。标签显隐阈值 1.3 → **0.8** (新布局下贴合视图即不重叠, 开箱可读)。

**教训 (值得进谱系)**: 补的 3 条最小间距测试**当场抓到自己刚写的真缺陷** — 扇区间隙原按比例留 (12%), 窄扇区在大半径处实际只剩 ~13px。改成按**绝对弧长**留白 (`halfR = half − step/2`, 半径越大留白角越小)。**比例留白在极坐标里是错的, 必须留绝对量**; 几何不变量写成断言比肉眼看截图可靠 (截图恰好没触发那个组合)。

**验证**: `node --test viewer/tests/layout.test.mjs` **18/18** (新增 3 条: overview/impact 两两 ≥36px, domain 3 列列距 ≥140px); `pytest` 全仓 exit 0 零回归; 产物 regen no-op (md5 一致); 四视图逐一 headless 截图确认无节点/标签重叠 (总览 / AE 60 变量 8 码表 / C99079 波及 44 域 / explore 4→11 节点+整理)。

---

## 2026-08-04 — Study 轨确定性轨收官 + 三层"测量/基础设施在说谎"的修复

**入口**: 交接文档 `.work/meta/study_rag_handoff_2026-08-04.md` (下个 session 从那里进)。

**起点是一次日常提问**("分支进度如何"), 收尾时变成了对三层可信度的连环排查。链条如下:

1. **P1/P2/P3 backlog 清账** — paths.py 三合一 (空串守卫统一 is None + assert→raise, `python -O` 实测)、停用 form 语义钉死、反回声闸告警按 sheet 分流、diff_available 贯通卡片、embed 维度闸改全量检查等。两轮独立复审, 第二轮抓到我修订过程**新引入的 3 个 MAJOR**。

2. **golden set 重做 (v0 12 题 → v1.1 27 题)** — 用户要求"参考 protocol 出题"。这一步直接推翻了此前所有好看的数字: v0 由 controller **看着卡片起草** (出题人=答题人), 题目偏软 + 覆盖偏科 (21 form 只覆盖 6 个)。改 protocol 概念驱动后 form 覆盖 18/21, 真实基线 **88.5%** (原记录 100% 作废)。两轮独立审阅每轮都抓到出题人自查漏掉的硬伤 (打分器子串匹配导致 3 题恒满分 / 同标题双卡漏标 / 问句里的因子在 EDC 根本不存在)。

3. **BM25 对日文零信号** — `bm25s` 无日文分词, 整句一个 token。修法 CJK 字符 bigram (对英文恒等), 单通道 12.0%→60.9%, 端到端 83.3%→88.5%。**关键认知**: v0 的 100% 有一部分正是出题泄漏喂饱了 BM25 (题目带着从卡片抄来的拉丁标识符)。

4. **部署索引长期陈旧** — 顺着"CDISC 英文库为何有 CJK"查到 `VARIABLE_INDEX.md` 的中文来自生成脚本硬编码 (非源 PDF), 重灌时发现该文件被欠切 70% (65 vs 222 chunk), 跨越 chunker 一次演进无人察觉, recall 白丢 5.7pt。→ 新增**索引陈旧闸** (内容指纹, 四处接入; 既有 kb_commit_sha 因用整仓 HEAD 而误报太多, 从未被消费)。

5. **一次被驳回的 gold 放宽 (最该记的教训)** — 我把一题判为"gold 太窄"并放宽, 独立复核**驳回**: 我核验到"文件含答案", 没核验"**被召回的 chunk** 含答案"; 且**判据双标** (否决别的题用"能否回答", 通过这题用"文件含文字", 松的那把恰好用在唯一加分的题上)。已撤回, 四条编辑纪律固化进 `check_source_recall` docstring。

**贯穿性教训**: 本轮至少 4 次出现"测试/演习假绿" (bigram 是原串子串导致接线闸假绿、空 expected_sources 恒得 1.0 导致 out_of_scope 测试假绿…), 每次都是靠"这条断言在旧码下会不会真红"才发现。**闸能通过 ≠ 闸能报警**; 运维闸最后是靠真改 KB 文件做实弹演习才确认它会响。

**验证**: 全量 669 passed (基线 531 起算, 本轮净 +138); 服务重启后 `ready chunks=4303` 且索引闸绿; 端到端问答冒烟正常。

**收尾附带**: 按用户要求关闭服务认证 (`AUTH_ENABLED=false`), 局域网免密访问。⚠ **Plan B 前置**: 当前 API 只服务 CDISC 库 (源自公开标准); 一旦把 study 库接进去, 等于把真实临床研究字段数据暴露给整个局域网 —— 必须是一次明确决策, 不能作为路由接线的副作用。

---

## 2026-08-04 (下半场) — Plan B Phase 0+1 双库联邦路由收官, 联邦默认启用

**入口**: spec `docs/superpowers/specs/2026-08-04-plan-b-federated-routing-design.md` →
plan `docs/superpowers/plans/2026-08-04-plan-b-phase01-federated-core.md` (7 task, TDD + 三 eval 闸)。
收口证据: `sdtm-rag/evidence/checkpoints/planb_phase1_federation.md` (+ 闸 1 明细 `routing_gate.md`)。

**做了什么**: 上半场交接文档留的"下一步 Plan B 联邦路由"落地 —— CDISC 标准库与 study (st01)
EDC 库合成一台联邦引擎, 用 light 模型判库 (`cdisc` / `study` / `both`), API 出 `routed_corpus`,
前端给下拉 + 来源库徽章 + 判定行。7 个 task 逐个 TDD + 逐段独立复审 (每段 diff 一份 review)。

**三闸结果**:
- **闸 1 路由准确率**: gold 181 题 (英文 cdisc 140 / 日文 cdisc 11 / 日文 both 5 / study 25),
  三遍 **178/181 = 98.3%**, **fatal=0**, fallback=0 (543 次调用), **稳定性 181/181 三遍一致**。
- **闸 2/3 检索无回归** (控制组 vs 联邦组配对, 全 `--retrieval-only`): CDISC hybrid-only
  **81.07% → 81.07% (Δ0)**; CDISC hybrid+S1 **98.93% → 98.93% (Δ0)**; study **88.53% → 88.53% (Δ0)**;
  三组逐题 recall 差异均 **0 题**。both 配额预案未触发。
- 判库分布: CDISC 侧 140/140 判 cdisc (逐题 top5 与控制组完全一致 = 对主库恒等变换);
  study 侧 25 study + 2 both (那 2 题是全部三组里唯一 top5 变化的题, recall 仍 1.0)。

**golden 路由题补充 (16 题)**: 初版 gold 里语言与语料一一对应 (cdisc 全英 / study 全日) 且
无 both 题 —— 任何"按语言判库"或"见到『項目』就判 study"的规则都**无法被证伪**。补 11 道
日文 CDISC 标准题 + 5 道日文跨库题后, 闸从 165 题 163/165 → 176 题 174/176 → 181 题 178/181,
每次扩充都逼着 prompt 判据再改一版。**闸集扩充比 prompt 调参更能提高判据质量**。

**LLM 供给切换 (Anthropic 直连 → AWS Bedrock)**: 直连额度耗尽 (credit balance too low),
改走 Bedrock (`jp.anthropic.*` haiku-4-5 / sonnet-4-6 / opus-4-7, `.env` + boto3)。
基线 prompt 在两个通道给出**完全相同**的 156/165, 说明闸对通道不敏感 —— 但**换模型必须重跑闸 1**。

**审阅循环**: 12 commit 逐段独立复审 (`review-<from>..<to>.diff` 各一份)。复审抓到的实质问题
包括: brief 把 81.1% 与 `--structured-lookup` 旗标串了 (实测该组合是 98.93%, 81.07% 对应
hybrid-only, 已按两套配置各跑一遍配对避免选择性挑数)、b03 题面用了日语不存在的中文构词
「受控術語」、两条"该方向不可证伪"的限制此前没入档。

**rollout (本 task)**: `federation_enabled` 默认翻 **True** (本轮唯一生产代码改动),
全量 **720 passed** (669 → 720, +51, 无测试因默认值改变需修改); launchd 重启后
`/api/info` `federation: true` + 索引新鲜度绿; 英文标准题 → `routed_corpus=cdisc` 全 cdisc 源,
日文 study 题 → `routed_corpus=study` 全 study 源 (expected_facts 3/3); 浏览器四点冒烟全过
(下拉默认「自動」/ study 题 15 个「本研究」徽章 / 标准题 15 个「標準」徽章 / 判定行正确)。

**记档的决策**: ① 局域网免密开放**含 study 库** (用户决策 D2, `auth.py` 代码保留待启用);
② `/api/ask_compare` 联邦后仍是 CDISC 单库, 响应无 corpus 信号 (已知限制);
③ federation 关时 `corpus` 入参静默忽略 (刻意前向兼容); ④ `both` 对奇数 k 返回 k+1 条 (单测钉住)。

**已知缺口 (下轮必读)**: ① 调优集 == 闸集, 无 holdout; ② **反向盲区** —— "英文提问 study EDC
字段"一题未覆盖; ③ both 组全带规则 3 线索词、无"含线索词但 gold≠both"的负例, 无法区分
路由器是读懂了跨库需求还是见词就判 both; ④ **`run_eval` 的联邦适配器把 `corpus` 硬写成
`"both"`**, 与生产的 `routed` 不同 —— 检索闸不受影响, 但**做联邦答题 eval 前必须先修**。

**next**: Phase 2 (study 结构化直查) / Phase 3 (eval chunk 粒度判据) / Phase 4 (CDISC 变量
索引挤占) 各自独立成 plan, 均不在本轮范围。

---

## 2026-08-06 — Plan B Phase 2 (S2) study 结构化直查 DONE ✅ 默认启用

**目标**: study 侧 golden v1.1 上 4 道 dense/hybrid 打不中的题, 靠**确定性**结构直查补上 —
数据源只有 `catalog.json` (959 items) 与本地手工别名表, **零 LLM**。

**做法** (`sdtm-rag/server/study_lookup.py` 新建, 8 task TDD): 三通道 + 一个补充形状 —
① 题面含卡 label (NFKC+去空白归一, 长度下界 4) → 该卡 + 其 OID 首段家族 (家族键含 `form_oid`,
不跨 form); ② 单个拉丁大写 token 命中 OID 段 → 该段全部卡; **②a** ≥2 个 token 各自命中段但单段
集合过宽被 cap 挡 → 取**交集** (严格全 token 合取); ③ 别名 term → form scope (≤3 名额)。
命中卡在检索前置 union-add 合并 (与 S1 共用 `_merge_lookup_first`), 与 S1 互斥。

**验收**: 25 计分题 **88.53% → 100.00% (+11.47pt)**, 四题 (q08/q14/q16/q21) 分别由通道
③/②a/②/① 修复; `regressions=[]` 对基线与对 attempt1 双向零回归; 计分口径 (oos={q26,q27}) 未变。
**联邦复核** (`--federated`): 100.0%, 逐题 recall 与 top5 集合**双双零差异**, routing `{study:25, both:2}`。
测试 **720 → 799** (0 failed / 0 skipped)。生产 launchd 重启零 traceback, `ready` 日志显示
`study_lookup='959 items/1 aliases'` (Task 5 加的可见性闸首次派上用场), q08/q14 端到端各命中 gold 1/1。

**日文题面的真 bug**: `\b` 在 CJK 下失效 (CJK 属 `\w`), 通道② 若照计划用 `\b` 会成死代码 →
改 ASCII-only 词边界。这是实现方在 TDD 中发现并按规格纠正的计划缺陷。

**q14 attempt 1 FAIL 的根因 = 规划缺陷, 不是实现缺陷**: 规划期探针口径隐含「限定首段 + 单一 form」,
实装规格是「全段 + 全 form」, 故 NOTES 里 q14 的通道预期在真实索引下被证伪 (两 token 的段命中
21/12 卡双双超 cap=8 → 通道② 完全不 fire)。这直接催生了 ②a。失败 run 已按规则 B 归档
`..._attempt1_FAIL_q14.json` (未删, mtime 未触碰)。**教训**: 规划期探针口径必须与实装规格逐条对齐,
否则「机制已实证」是假的。

**为破"单样本无法证伪"做的全库证据**: 359 张 ≥2 段的卡里交集规模 min1/p50 1/p90 2/max 6,
**0 张超 cap**; 以段对为单位 (段对才是 query 形状的单位) 全库 338 个共现段对中 **8 对**属
「双单段皆超 cap 而交集落回」= ②a 独有解锁的形状 → q14 非孤例, ②a 是 pattern 级修法。
**但必须同时记住**: 这些统计证明的是**形状的 cap 安全性与复现性**, **不是 fire 正确性** —
后者证据仍是 **n=1** (27 题中 ②a 实际 fire 1 题)。这是本轮最大的未证伪面。

**cap=8 的反过拟合证据**: cap 扫 6/8/10/16 全 gold 覆盖题数**恒为 4**, `_MAX_CARDS_TOTAL` 扫
6-15 亦恒为 4 → 落在**平台**上而非尖峰, 100% 不是靠调常数得来。代价也如实入档: label 侧
193/515 (37.5%) 超 cap 被整体跳过 (含 107 条唯一 label), 段侧 20/458 (4.4%); 抬到 12/16 注入量
17→23 而 gold 覆盖零增益 → **对称的无知** (无损害证据也无收益证据)。本题集无代价 ≠ 该规格无代价。

**审阅循环 (规则 D)**: 实现方与各审阅方全部不同 `subagent_type`; 终审 37 变异独立自跑 31 杀 6 存活,
其中 3 条真缺口 (家族键 form 分量 / NFKC 空转断言 / `_MIN_LABEL_LEN` 双向) 在 fix wave 全部补锁,
终审复核 6/6 ADDRESSED 且逐文件 sha256 证明生产代码零改动 → 验收数字无需重跑。终审还发现
**q23 (计分题) 的唯一 gold 是 17 张卡的公共子串, 判别力≈0** —— 既存缺陷、基线亦 1.0、不影响
+11.47pt 归因, 但「25/25」里有一题近乎不可证伪, 已写进 checkpoint。

**终审模型降档如实入档**: 原定 fable 因额度耗尽改由 opus 承担 (用户 2026-08-06 确认), **非为省钱**;
规则 D 隔离靠 5 种不同 `subagent_type` 维持。

**open follow-ups**: ① M-f 注入量 ≥k 时 `log.warning` 从未实装 (实测 max slot 6 << k=15, 非阻塞);
② `aliases.raw` 字段无生产消费方; ③ `_apply_study_lookup` 忽略 `where` 属未言明的不变量
(当前安全: federation 只以无 domain/file_type 形式调 study 引擎); ④ 继承自 Phase 1 —
`_FederatedAdapter.build_messages` 把 `corpus` 硬写成 `"both"`, **做联邦答题 eval 前必须先修**。

**证据**: `sdtm-rag/evidence/checkpoints/planb_phase2_study_lookup.md` ·
plan `docs/superpowers/plans/2026-08-06-plan-b-phase2-study-structured-lookup.md`

**next**: Plan B Phase 3 (eval chunk 粒度判据) / Phase 4 (CDISC 变量索引挤占), 各自独立成 plan。

---

## 2026-08-06 (收官) — study golden v2 扩容 DONE ✅ 尺子恢复判别力

**动机**: Plan B Phase 2 收口时 study golden v1.1 在 S2 下达到 100.00%, 该题集**判别力耗尽** ——
后续 study 侧改动只能测出"不回归", 测不出"有没有变好"。v2 的目标不是分数更高, 是**让尺子重新能区分**。

**交付**: 25 → **48 计分题** (+3 反幻觉); form 覆盖 18/21 → **21/21**; 按 form 卡数加权配额消灭
"前五大 form 占 54% 卡量只有 7 题"的偏科。v1.1 题集**不动**, v2 是新文件 (历史 run 仍可复算)。
新增确定性 gold 唯一性 lint `eval/lint_gold.py` (AND + OR 双侧, 17 tests)。

### 验收数字与诚实修正

| 尺子 | S2 关 | S2 开 | 增益 |
|---|---|---|---|
| v1.1 (旧, 已饱和) | 88.53% | 100.00% | +11.47 pt |
| **v2 (新)** | **80.49%** | **87.50%** | **+7.01 pt** |

改善 5 题 / 回归 0 题; 仍失分 6 题全部是 **0.00 的完全 miss**(无部分命中)。

**但 +7.01 这个数字本身还不够诚实 —— 拆开两半才是真相** (本轮最重要的一个数):

| 子集 | n | S2 关 | S2 开 | 增益 |
|---|---|---|---|---|
| v1.1 逐字继承 | 24 | 88.06% | **100.00%** | **+11.94 pt** |
| **本轮新写** | 24 | 72.92% | **75.00%** | **+2.08 pt** |

即 **S2 的实测增益几乎完全局限在旧题集恰好包含的题型上; 在新写的题上只有约 2 个点**
(24 道新题里 S2 只多修好 1 题)。这不是 S2 变差了, 是旧尺子测不出 S2 测不到的东西。

**口径有效性交叉验证**: 24 道继承题在 v2 run 里与历史 v1.1 run **逐题 Δ0** (S2 开关两组皆是),
故 v2 的分数变化全部来自新题, 不含"换题集导致继承题也测出别的结果"的混淆。

### 三方隔离 (规则 D) — 审阅抓到的实质问题

出题 / 独立审题 / 第三方规则 A 抽检三个不同 subagent_type; 审题人未读出题 NOTES, 抽检人既未读 NOTES
也未读审题报告、**且拒绝复用对方的 audit 脚本**(复用会把对方判据的盲区一并继承)。三轮 REVISE→APPROVE,
**每轮都抓到出题人自查漏掉的硬伤**(与 v1.1 两轮审阅的历史经验一致, 一次就 APPROVE 反而可疑):

- **审题推翻了 lead 与出题人已准备接受的妥协**: 两道家族题"判别力≈0 属已知结构性限制"**不成立**,
  二者都能改单卡 gold 且零信息损失 (家族最终枚卡面自带序号, 本身就是"共 N 枠"的直接证据) →
  **该限制声明当场收回, 不入档**。修完后 48 题里没有任何一题的 source_recall 是结构性白送的。
- **一道题的 gold 漏了第二问的答案卡** (3 条 fact 中 2 条只在那张非 gold 卡上 = 完全不答第二问照样
  满分) —— 属 gold 不完整, 出题人与 lead **双双漏看**。
- 一条 fact 是**语义相反**的兄弟 OID 的真子串 (gold 问"日", 超串是"日数(自动计算)") ——
  把日期答成自动计算天数**正是本题要抓的错误**却仍满分。出题人原判"影响有限", 审题判其**更危险**。
- **R1 的修法本身引入了新缺陷**: 改成 OR 组后一个成员只覆盖 1/3 fact → 只召回该成员即 source 满分,
  但该卡产不出其余 fact, **source 指标为一个产不出期望答案的检索背书**。差回单卡 AND。

正面记两笔: 出题人把审题给的**单点修法外推成一类模式**并自查全题集, 另找出 1 条同形态缺陷
(符合"区分 pattern vs example"纪律); 反幻觉题那句错误"实测", 审题只看到题集里那份,
**出题人自查发现 NOTES 里还有一份复制并一并改掉**。

### 教训 1: 检查工具与被检查的判据不同语义 = 制造连锁误判

初版 lint 先剥 gold 末尾 `.md` 再匹配无后缀卡名, 而真判据 `check_source_recall` 是 gold **原样**对
**带 `.md`** 的完整 source 串匹配 —— `.md` 参与匹配且**有判别力**。初版因此**比真判据严** → 假阳性:
v1.1 报的 9 条 finding **8 条是假的**, 真问题只有 1 条。

**连锁后果**: 出题人为迁就假阳性删过 2 条合法 gold、多加 5 条不必要的 `gold_max_matches`、
把 1 道新题从单卡降级为家族题; lead 本人也据此对某题做出错误判断。修正后让步全部回退。
已加测试直接钉住 lint 与判据的等价性 (改任一侧都会红), 并对"把剥离逻辑加回去"做变异验证。

### 教训 2 (已立为规矩): 写"实测"必须附可复跑的一行命令

一轮之内出现**两次**写错的"实测"声明 (反幻觉题"零命中"、OR 组"实测满足纪律")。两次都不是结论错,
而是**把推论写成了实测**。写错的"实测"比缺陷本身更值得纠正 —— 它让下一个人跳过复验。
对策落地为制度: 出题人把体检固化成 `audit_v2.py` 一条命令, 全部文档"实测"字样逐条洗过,
**写不出复跑命令的措辞直接删掉**。

### 判据加固 (结构性产出, 不只修实例)

lint 只查"gold 唯一定位"(单向); `audit_v2.py` **import 真正的 `check_source_recall`** 做双向断言 ——
只喂 gold 得 1.0 / 只喂其余全部非 gold 得 0.0, **48/48**, 证明的是"**只有 gold 能得分**"。
79 条 gold 全部补 `.md`(今天判定不变, 防的是将来 catalog 新增兄弟卡导致的**静默**多匹配)。
审题抓到的 OR 纪律已从"人工判"固化成脚本闸 —— 当前 OR 组为 0 而空转, 但将来任何人再引入都会自动开火。

### 已知限制 (全部入档 checkpoint §7)

① **继承题存量债**: 3 题 fact 命中 >100 卡 (最宽 574/481/352) / 3 题 20-100 / **1 题全部 fact 无判别力
(fact_recall 结构上恒 1.0)** / **7 题题面回声即得分**; 新写题四类**均为 0**。为保 v1.1 历史可比性
刻意不动, 属正确取舍但**必须声明** —— 否则等于用这把尺子对外报数字而不告知。
② **子串判据看不出"两项互换"**: 8 道近义双卡判别题, 把两个 OID 语义**对调**后 source 与 fact
**仍双满分**, 而这类题的出题意图正是考这个映射 → **这类题成绩必须在 `--judge` 语义模式下读**。
③ **规则 A 抽样总体今后应等于本轮变更集**, 而非变更后全集 (本次均匀抽样把 6/10 力量投在未变更区,
抽检人自行补抽到新增区 9/23)。④ form_overview 仅 n=4, 50% 不足以作类别指标。

### next

`--judge` 语义模式下的 v2 基线 (§7.2 那类题的答案正确性**尚无任何测量**) / v2 联邦模式复核 /
form_overview 扩题 / 修 `_FederatedAdapter.build_messages` 硬编码 corpus (联邦答题 eval 的硬前置)。

**证据**: `sdtm-rag/evidence/checkpoints/study_golden_v2.md` ·
plan `docs/superpowers/plans/2026-08-06-study-golden-v2-expansion.md` · 全量 **823 passed**

---

## 2026-08-07 S1 对 VARIABLE_INDEX 按字面定位 section DONE (检索续跑 D2; 18 题子集 75% → 100%)

- **触発**: 用户路由词「检索续跑 开始任务」→ `milestones/07_rag_kg/NEXT_ROUND_KICKOFF.md`。用户在 A/B/D 四个候选靶子中选 D2 (S1 对 VARIABLE_INDEX 改按 CT 码/变量名字面定位)。
- **完了の作業**:
  - **设计** `docs/superpowers/specs/2026-08-07-s1-variable-index-literal-section-design.md` + **计划** `docs/superpowers/plans/2026-08-07-s1-variable-index-literal-section.md` (5 任务 TDD)
  - **实现** (commit `25da6cf` + `2667f63`): 锚点抽取 `StructuredLookup.variable_index_anchors` (CT 码 + 已知变量名, CT 在前) / 映射反建 `RAGEngine._vi_section_map` (**从 Chroma 元数据反建, 不拼格式串**) / 注入 `_lookup_chunks_for_variable_index` (`{"$and": [source, section]}` 精确过滤, 复用已算好的 embedding, 零新增 round-trip) / 回落: 锚点解不出或 section 不在索引 → 回落原 cosine
  - **三方隔离修复** (commit `8dcd1d2`): 抽检方 D-1 锚点饥饿 (先 resolve 再 cap) + 审查方 HIGH-1 (失败点从请求期挪到启动期预热) + HIGH-2 (guard 改两族都必须在 + CI 漂移闸) + MEDIUM/LOW 5 条
- **成果**: CDISC section 级判据 **95.71% → 98.93%**; **18 题 VI 子集 75.00% → 100.00%** (q107 0.5→1.0, q108/109/110/112 0→1.0, 5 升 0 回归); 其余 122 题 **98.77% 逐题相同**; 全量测试 **823 → 852 passed**
- **教训 (三条)**:
  1. **拼格式串 = 把同一份格式定义写两遍**。若 chunker 改 section 命名, 拼串方案会静默全 miss 并回落 cosine —— 分数无声退回改动前, 任何闸都拦不住。从索引反建则只有一份事实源。这与本轮第 1 条硬规矩 (工具须与被检查判据逐字同语义) 同源。
  2. **"响亮失败"放错位置比不放更糟**。首版把 fail-loud 放在请求期, 审查方实测出 deploy.sh 拷贝路径下 140 题里 71 题会 502 且缓存永不赋值 —— 而改动前同样错配只是静默退化、服务照常出答案。修法是把它挪到启动期: 部署错配在 launchd 启动即失败, 不是用户收到偶发 502。
  3. **"当前题集无此形态"这种话不能凭印象写**。抽检方查出 q104 的 anchors 恰好打满上限 3 且 gold 在第 3 位 = 零余量, 我写的"无此形态"是事实错误 —— 正是"写错的实测比缺陷更害人"那一类。
- **已知限制 (7 条)**: 见 `sdtm-rag/evidence/checkpoints/s1_variable_index_literal_section.md` §4。最要紧两条: ① **VI §三 正文在 15 变量处截断**, section 级判据对此零判别力, q109/q69 的 gold 都压在第 15 位过关 —— 禁止把"18 题 100%"读作"VI 类问题已解决"; ② **数字在这里没有判别力**: 新的三元组 (98.93/100.00/98.77) 与已作废的路径级口径**逐位全同**, 是结构必然非巧合, 判别只能靠 section 名 (q109 旧召回 C66734 / 新召回 C99073)
- **evidence**: `sdtm-rag/evidence/checkpoints/s1_variable_index_literal_section.md` + 前后工件 `s1_vi_{before,after}.json` (配对 diff 可从工件复算, 不必 revert 重跑)

---

## 2026-08-07 VI §三 交叉引用完整性 DONE (拆掉 15 条上限, 补回 226 条隐藏引用)

- **触発**: 上一轮 S1 字面 section 定位收口时, 规则 A 抽检提出 D-3 —— VI §三 正文在 15 变量处截断, section 级判据对此**零判别力**, 故"18 题子集 100%"不能读作"VI 类问题已解决"。用户在四个候选靶子中选它。
- **完了の作業**:
  - **设计** `docs/superpowers/specs/2026-08-07-vi-truncation-completeness-design.md` + **计划** `docs/superpowers/plans/2026-08-07-vi-truncation-completeness.md` (6 任务)
  - **修了两个独立缺陷**: (a) 条数上限截断 —— `generate_variable_index.py` VI §三 上限 15 (9/135 行, 隐藏 226 条) + `generate_cross_references.py` 域 spec 上限 5 (AE/LB, 隐藏 10 条); (b) **只取 CT 字段首码** (三方审查在收口前抓出) —— CT 字段可列多码 (`PP.PPORRESU = C85494; C128684; ...`), 只取首码导致 **12 个码表在 §三 整行不存在** + 18 个引用对遗漏, §二 渲染全码串故同一文件自相矛盾; 修为 `extract_ct_codes` 收全码, §三 **135 → 147 行**
  - 重生成 KB (131.3 → 133.8 KiB, +2527 B) + 重灌索引两轮 (4303 → **4315 chunks**, +12 = 新增的 12 个 §三 行; chunk 数由 chunker 逐行切块结构决定, **不是"没影响"的证据**)
  - **自带两层尺子** (现有检索闸对本修复结构上失明): 层① `scripts/tests/test_kb_crossref_completeness.py` 数据不变量 3 红 → **7 绿**, KB 层 + chunk 层双打, **含两条外部锚** (对 spec.md 反建, 审查方 REVISE 后补); 层② `eval/test_set_vi_completeness.yml` 2 题独立计分 + `eval/vi_completeness_ab.py` 截断/完整 context 对照
- **成果**: 层① 5 绿; 层② A/B 两题判别力均成立 (C66742→VSLOBXFL / C71620→URSTRESU, 截断答不出、完整答得出), 独立 gold 集 fact 子串与 judge 双 100%; 生产端到端答案含旧语料结构上产不出的 `VSLOBXFL`; **v3 逐题 Δ0 (98.9286% 不动)**; 852 → **859 passed**; reconcile_meta 8 项全 OK; freshness in sync
- **教训 (三条)**:
  1. **"闸绿了"与"修好了"是两件事**。v3 检索闸对本修复结构上失明 (section 名不变), 改完必然不动。若不自带尺子, 这轮就是"改了但说不清"。**引用本轮成果不得用 v3 数字。**
  2. **判据检查工具必须与被检查对象逐字同语义 (第二次栽在同一条)**。A/B 初版用 `DOMAIN.VAR` 点号形式做子串匹配, 把模型一次**正确作答** (按域分组表格 `| UR | URORRESU, URSTRESU |`) 误判成"无判别力"。改裸变量名后两题都成立。上一轮是 lint 与真判据不同语义制造 8 条假阳性, 这轮是 A/B 判据与答案表达形式不同语义。
  3. **"停下查清第四个文件"这条计划纪律真的抓到东西**。重生成时冒出预期外的 `PC/spec.md` 改动, 查清是**既有缺陷**: 交叉引用自 06 深审以来陈旧 (生成器按 assumptions.md 是否提及 RELREC 决定加链接, 而 PC/spec.md 生成于 Phase 6, 早于 06 给它的 assumptions 补进 RELREC 正文)。生成器是对的、已提交 spec 是旧的 —— 顺带修好而非回归。
- **已知限制 (5 条)**: 见 `sdtm-rag/evidence/checkpoints/vi_crossref_completeness.md` §5。最要紧: ① A/B 隔离的是 context 变量, 证明因果但不等于线上答题必然变好 ② 只落 2 道端到端题, 其余 7 个宽码表靠层① 数据不变量而非端到端验证 —— 层① 证明"数据完整", 不证明"模型用得上"
- **evidence**: `sdtm-rag/evidence/checkpoints/vi_crossref_completeness.md` + 工件 `vi_trunc_v3_after.json` / `vi_completeness_after.json`

**收口后追加 (三方审查结果)**: 审查方 **REVISE** (2 HIGH), 抽检方 **PASS** (数据正确性) + 4 项入档。三方各自抓到对方看不见的东西, **实现方自查全绿、三条真缺陷一条都没自己发现**:
- **审查方独有**: 层① **自洽即通过** —— 只比"条目数 == 该行自己声称的 N", 而两个值出自生成器同一条 f-string; 构造伪造 KB 实证 (切片放在计数之前) 226 条静默消失而当时 5 条断言全绿。修法 = 加对 `domains/*/spec.md` 反建的**外部锚**, 一条同时堵住自洽绕过并让缺陷 (b) 当场显形。另抓到: 域 spec 侧只有 marker 断言比 VI 侧弱 / `.pyc` 入库 / "chunk 总数不变"当证据是恒等式非观测。
- **抽检方独有**: 用 `source/cdisc/SDTMIG_v3.4.xlsx` (与生成器无共享代码) 独立重算, **全部 135 码表双向差集为 0、1917/1917 变量 CT 单元格逐字零偏差**, 证明补回的 226 条是**对的**而不只是"变多了"; 并发现 **vic01 答案写 "53 domains" 而真值 41** —— 1-fact 判据视野外的事实错误。
- **两方独立收敛**: 12 个码表整行缺失; **体积 "+4.2 KB 实测" 是错的** (真值 +2.5 KB, 且写进了生成器源码注释)。
- **新浮现的答题侧缺陷 (本轮不修)**: 宽码表下模型能读对变量数 (123) 却**估而不数域数** (答 "50+"/"53", 真值 41)。`vic01` 在 judge 口径下**故意保留失分 0.5** 作常驻探针, 修好前不要调绿。
- **第三条教训**: **我把估算值标成了"实测"**。附了命令段落但数字不是从那条命令来的 (Python 字符数 vs 生成器打印的 KiB 混用, delta 报大 68%)。第 2 条硬规矩要补一句: **标"实测"的数字必须真的来自那条附上的命令, 单位要对齐。**

---

## 2026-08-07 检索同质簇挤占 + gold 完整性 DONE (11 task, Task 7 SKIPPED; 层② 判定作废)

- **触発**: `NEXT_ROUND_KICKOFF.md` §2.A (q38 —— CDISC 140 题里唯一一道 recall 0.0)。诊断阶段**推翻了 kickoff 写的根因**, 遂立 spec 拆成三段: ① gold 完整性 ② 挤占是否有害 ③ chapters 切分。
- **设计 / 计划**: `docs/superpowers/{specs,plans}/2026-08-07-retrieval-crowding-and-gold-integrity{-design,}.md`
- **完了の作業**:
  - **段① gold 完整性** (Task 1/2/3/3C): 判据单条匹配抽成模块级 `source_matches` (扫描工具共用同一实现) → 扫描器 `eval/scan_gold_gaps.py` 扫出 97/140 题共 182 条 unmatched → **第三方独立判定** (`scientist`, 与工具作者/评审均不同 subagent) 给出 遗漏_应补 27 / 相关但非权威 119 / 不相关 36 → 按型成组补 **27 条 / 26 题** + terminology 抬头 **chunk 层断言** + section gold **存在性闸** (`test_section_gold_exists.py`, 49 条 / 37 题, missing=0)
  - **段② 挤占** (Task 4/5/6, Task 7 **SKIPPED**): 层① 结构探针 `eval/crowding_probe.py` 落库 (与 spec §0 六个数逐值相同) + 跨进程验稳 → top-k 抖动量化 `eval/jitter_probe.py` → 池深度不变性 `eval/pool_depth_probe.py` → 层② context A/B1/B2 用**答案正确性**作外部锚 (`eval/crowding_ab.py` + `server/diversity.py`)
  - **段③ chapters 切分** (Task 8): 取消 ≤20KB 整文件单块档, ch01/02/03 按 H2 切成 **5/9/3**, 重灌索引 4315 → **4329**
  - **段④ 收口** (Task 9): 总收口证据 + retro + 归档判据差分对拍 `eval/tests_support/gold_semantics_diff.py` + 索引三件套
- **成果**:
  - CDISC 全集 **99.17%** (140 题, retrieval-only, hybrid + structured_lookup, **含 gold 完整性修复后**); 非满分题 `{q38: 0.3333, q126: 0.5}`
  - **958 passed / 0 failed / 0 errors / 0 skipped**; `chunk_count` 4315 → **4329**
  - 层① 同名 section 簇 ≥3 席 **28.6% (40/140) → 23.6% (33/140)**; ch02 在全 140 题 top-15 席位 48 → **98**
  - q38 由"判据缺陷造成的假失分"变为"判据准了、检索确实缺一块"; **140 题逐题零回归** (切分前后 recall/hits/misses 完全相同)
- **⛔ 必须点名的三件事**:
  1. **Task 7 是 SKIPPED (前置未满足), 不是"判定挤占无害"**。层② 判定 `VOID_TIE` **作废** —— 33 臂全 1.00 零方差, 同分题 10/10 ≥ 8, 触发写死的自毁条款。**我们仍然不知道挤占是否有害。** 量具饱和是**本实验之前就已落库**的事实 (`llm_judge_fact_recall.md:29` 记 121/140 = 86.4% fact-recall 顶格), 且 **A 组自己也是 1.00** —— 对所有臂都顶格的尺子逻辑上无法区分"无效应"与"有效应"。**判 VOID 是唯一诚实读法。**
  2. **fact gold 的分辨力问题 (影响面远超本轮)**: 这 11 题 33 条 `expected_facts` 里 **28 条 (85%) 是 1–2 词关键词碎片**; q38 的两条"事实"字面就是 `two-character` 和 `DOMAIN`, **连只有 3 席 context 的 B1 都满分**。旁证: q38 源级 recall 0.3333 而**同一条 context** 的 fact-recall 1.00。⇒ **所有用 fact-recall 读出来的答案质量结论分辨力都存疑。** (用户裁定: 本轮不修, 换锚归下一轮; **句子级 gold 也未被证明够用** —— q118 n=1 同样同分。)
  3. **kickoff §2.A 的根因是错的**, 且它是**上一轮收口时写下的、未经诊断验证**。真实根因是 ①gold 漏权威源 ②同质簇挤占 (q38 top-15 被 14 席 `§DOMAIN` 占满) ③整文件稀释真实但非主因 —— 剔簇后 ch02 仍只到 #12; **Task 8 真切完实测, ch02 最好的块 #71→#63 而真正答题的 §2.6 在 #70, 仍在 top-15 外, q38 一分没涨**。
- **口径断裂声明**: **99.17% 与历史 98.93% 不可比 —— 换了一把尺子** (gold 集合本身变了)。**99.29% 是已作废的中间值** (曾随已提交 JSON 短暂进仓 `7c9ee68`, 后因 q38 从 OR 改回 AND 降为 99.17% `8930461`; 降幅 100% 来自 q38 一题)。
- **教训 (四条, 全表见 retro)**:
  1. **同一形态出现四次**: 结论方向对、但支撑它的那句话比证据能给的更强, 且四次都以断言形式进了源码注释或已提交证据 ("eval Δ0 证明逐字节等价" / "进程内 N 次 = 1 个样本" / "run1/run2 都在这 4 种里" / "两题稳定性依赖测量模式")。**给"不会发生 X"这类全称结论必须标样本量, 或改写成"在我查的 N 题里未见"。**
  2. **数字比它的适用条件传播得快 (三次)**: 99.29% 进仓而口径声明留在 gitignored 目录 / `max_cluster_section` 的禁忌写在 markdown 而下游读 JSON / spec §0 的 28.6% 依赖的豁免已被重灌击穿 (且含 `whole_file` 人造簇 5 题, 剔除后同口径 27.1%)。**数字与适用条件必须在同一个可提交载体里, 且载体格式要与下游读取方式一致。**
  3. **控制器按 example 层修了一个 pattern 层问题** —— Task 1 修掉 `open()` 缺 encoding, **两个 commit 后又在 Task 3 brief 里原样写一遍**; 提为 Global Constraint 的那次 commit 自己也没贯彻全文 (第三次)。**而本轮主题恰恰就是 pattern vs example。**
  4. **判定规则先于数据写死, 是"VOID 能被报出来"的唯一原因**。最省事的读法本来是"两组都不过门槛 ⇒ 无害 ⇒ 跳过 Task 7", 规则表里排在前面的是自毁条款。**`VOID` 是本轮最有价值的产出之一** —— 它把"我们不知道"保留了下来。
- **已知限制 (23 条全表)**: `sdtm-rag/evidence/checkpoints/crowding_and_gold_integrity.md` §5。最要紧: 挤占是否有害仍未知 / fact gold 分辨力存疑 / **CDISC 尺子接近饱和** (只剩 q38+q126, 余量 0.83pt) / **索引侧溯源缺口** (全库 4329 chunk 含 `Source: SDTMIG` 的 = 0 ⇒ **任何 chapter 都检索不到页码**; 源 md 仍有 —— 已记进 `.work/MANIFEST.md` Chain D) / **3 题新 OR 成员严格弱于旧成员, 动检索时会兑现**
- **evidence**: `sdtm-rag/evidence/checkpoints/crowding_and_gold_integrity.md` (总收口) + 分段 `{crowding_layer1,crowding_layer2,topk_jitter,pool_depth_invariance,chapters_chunking,gold_gap_verdicts}.md` + `step_09_audit.md` (规则 A 抽检) · **retro** `docs/superpowers/2026-08-07-crowding-gold-RETROSPECTIVE.md`

**收口后追加 (规则 A 独立抽检结果)**: 抽检方 (第三个 subagent_type, 规则 D 隔离) 判 **有条件 PASS** (7/8 样本干净), N=8 按风险配比抽本轮变更集合。
- **独立证实 (未采信任何既有 JSON, 全新重跑)**: `source_recall_avg = 0.9917` 与仓内 `gold_integrity_after.json` **逐位相同** (四个 category 全同); **q38 仍 0.3333 / q126 仍 0.5 —— 两条已声明限制独立证实为真, 未被粉饰**; 14 条注入抬头 gold 正文依据逐条属实; 两次"撤回 OR 改 AND"(q46/q38) 经正文实测证实成立且注释未夸大 (q46 `'Perm' in chunk -> False`; q38 的 §4.1.6 全文不含任何 two-character 变体); chapters 切分未切断语义单元 (含 mermaid 的 §2.6 完整落在一块内), `whole_file` 残留 0; 两道新闸**经变异测试证实会红**。
- **⚠️ 发现【中】OR 纪律第 1 条只在拒绝时执行、在自建时未执行**: 实现方对 q43/q45/q46/q59/q62 正确拒绝并成 OR, 却对自己新建的 15 个 OR 组未跑同一条纪律 (机械扫描 合格 7 / 不合格 8)。逐条读正文后分三层: **3 题真问题** (q117 0/4 · q73 1/3 · q115 1/3, 其 OR 组是该题**唯一计分单位**) / 3 题"纪律按字面套过严不构成问题" (q19/q91/q126 保留了 AND 成员) / 2 题**既有缺陷非本轮引入** (q34/q68)。**对 99.17% 无影响** (三题当前均已命中强成员), 风险在未来回归时隐性显形。**机制**: `eval/lint_gold.py` 是 study 轨的闸且第 66 行对 section 级 gold 直接 raise, **根本不作用于 test_set_v3.yml** ⇒ **该纪律在主题集上无任何自动闸, 唯一防线是人。**
- **本轮处置**: q115/q117 已在 yml **就地注释** (源判定成立但 facts 措辞与单一源强耦合 ⇒ source 满分而 fact_recall 会背离, 别误读成检索缺陷); q73 已注释**待裁定** (同形态 q25 补 AND 而它补 OR, 改它会动分数需重跑 eval, 本轮未做); "无自动闸"这一事实与 q68 缺陷已入档 (收口证据 §5 L20-L22 + kickoff §4)。
- **抽检把 C2 的范围改大了 (本文初稿写窄)**: 实测全库 **4329 chunk 里含 `Source: SDTMIG` 的 = 0、含 `Pages ` 的 = 0** —— ch04/ch08/ch10 **从来就没有过**这行, 本轮只是把 ch01-03 **对齐到既有行为**。两种读法都记下了: 「本轮改动无害」成立, 但更该记住的是 **RAG 索引里任何 chapter 都检索不到页码** (不是本轮造成的, 是本轮才查清的)。已改写 `.work/MANIFEST.md` Chain D 注。
- **抽检自陈两条**: ①流程失误 (低) —— 变异测试直接 sed 改了仓内 `eval/test_set_v3.yml` 而当时另一 agent 并发编辑同一文件; 终态已核实无损 (变异无残留 / 对方修改完整保留 / 三闸 13 passed / 评测 0.9917 与仓内一致), **正确做法应在 /tmp 副本上变异**; ②未覆盖项标成 **"⚠️ 无法从证据验证"而非写成断言** (层② 判定作废的原始论证 / 跨进程抖动统计充分性), 且明说本抽检**不能反证 gold 现在完整**。
- **新立硬规矩两条** (kickoff §3): **15. 成文纪律必须对"自己刚做的东西"也跑一遍** (同一条规则在同一位置的两个方向上被非对称应用 —— 这类靠人执行的纪律**半衰期等于写它那个人的记忆**); **16. 规则 A 抽检三件动作固化为模板** (不采信既有工件全新重跑 / 对新闸做变异测试 / 机械扫描后逐条读正文 —— **机械结果 ≠ 业务结论**)。

**抽检解除条件处置 (2026-08-07, 同 session)**: 抽检四条条件前三条已做完。
- **条件 1 — q73 OR → AND (与 q25 统一)**: `expected_sources_any` 改 `expected_sources`, 两成员不变。**实测改前改后各跑一次全 140 题** (`eval/run_eval.py eval/test_set_v3.yml --retrieval-only --hybrid --structured-lookup`): 全集 **0.9917 → 0.9917**, 四个 category 逐值相同, 非满分题仍是 `{q38: 0.3333, q126: 0.5}`, **逐题 recall 变化 0/140 题**。**不掉分的原因是两成员本就都命中** (`misses` 空), 改的是判据严格程度不是这题的检索表现。**判别力确实买到了 (反事实实测, 零 LLM)**: "只召回 VI `§一 通用变量: RDOMAIN` 那一行"旧 OR 给 **1.0** (与"两源都召回"同分, 不可区分), 新 AND 给 **0.5** (可区分) —— 与 Task 3 段二对 q46/q59 的实证同形。OR 组题数 **15 → 14**。
- **条件 2 — q115/q117 就地注释**: 记明 facts 措辞逐字抄自 ch08 一侧、与单一源强耦合 ⇒ 只召回另一 OR 成员时 **source_recall 满分而 fact_recall 会背离**, **不要误读成检索缺陷**。
- **条件 3 — "OR 纪律第 1 条在 CDISC 主题集上无自动闸"入档**: 收口证据 §5 L20 + kickoff **§2.D.4 列为下一轮候选闸** (含实现草案: 每个 OR 成员用 `source_matches` 取回全索引匹配 chunk 正文, 逐条 facts 子串核对; **并警告闸必须能表达"有 AND 成员时纪律按字面套过严"这个例外**, 否则会造假阳性 —— 那正是上一轮 lint 语义事故的形态)。
- **条件 4 — q68** 记进 kickoff §4 follow-up, 非本轮引入不阻塞收口。
- **retro 新增一条 (lead 自陈)**: **并行 agent 触碰同一文件没有约定隔离方式**。抽检做变异测试时直接 sed 改仓内 `eval/test_set_v3.yml`, 而收尾方正在编辑同一文件。终态已核实无损 (变异无残留 / 指针修改完整保留 / 13 passed / 0.9917 一致 / 与 HEAD 逐题 gold 语义差异 0 题), **但这是运气不是设计** —— 损坏对象恰是判据本身, 不会让任何测试变红, 只会让此后所有分数悄悄换一把尺子。责任在派单方: 并行派单前必须划分文件所有权, 写集合有交集就要么串行要么指定只读方。

---

## 2026-08-11 §2.A2 零 LLM 配额 × source recall 全集扫描 (路由词「检索续跑 开始任务」)

**任务来源**: `milestones/07_rag_kg/NEXT_ROUND_KICKOFF.md` §2.A2 (2026-08-09 定为下轮第一顺位)。
上一轮层② 用 LLM judge 作锚撞上量具饱和、判定 `VOID_TIE` 作废; §2.A2 指出那条"gold 判据对挤占
结构性失明"的论断有一个从未写出的限定条件 —— **它只对 S1 有注入的题成立**。

**做成的**:
- 新增 `sdtm-rag/eval/cap_recall_sweep.py`: 140 题 × `cap ∈ {None,1,2,3}` × `check_source_recall`,
  **零 LLM 调用**。管线复用 `eval.crowding_ab.build_arm` 不重写 (`fuse(60) → cap → 截 15 → S1`)。
  **判定规则先于数据写死在 docstring 里** (硬规矩 8): 两条自毁条款 (V1 接线闸 / V2 配额没生效)
  排在全部肯定性结论之前, 逐档 R1-R4 + **R5 default 行**, 全局组合规则 `overall_verdict`。
- **接线闸**: A 臂 (`cap=None`) 与生产 `rag.retrieve` **140/140 逐位相同**; A 臂均值
  **0.9916664 = 已发布的 99.17%** —— 本轮最强的控制组。
- **结果**: `cap=2` / `cap=3` **零回归** + q38 `0.3333 → 1.0000` ⇒ 全集 **0.9964** (+0.4762pt);
  `cap=1` **确定性有害** (0.9786, q08/q37/q127 回归)。
- **机制查明 (不是黑箱)**: 新增 `--fused-profile` 直接测融合池簇构成 ——
  q38 的 43 条候选里 **40 条 (93%) 是 §DOMAIN**, 只有 **4 个不同 section**;
  q08/q37/q127 回归的原因是**它们的 gold 本身就是同名簇的成员之一** (q08 要 `DM/spec.md`
  的 §USUBJID, 而簇里有 29 条同名), `cap=1` 只留簇内第一条恰好不是 gold 那条。
- **新增"影子信号"** `hidden_loss_shadow`: 分数没动但 `source_hits` 集合变了的题 ——
  为 kickoff §2.A′ 那条"OR 组会把回归吃掉"的存量债取证。**三档全 0 题** ⇒ 本轮的零回归
  不是 OR 组撑出来的 (**但这条债本身没消失**)。
- **稳定性**: 实现方 3 个独立进程 + 抽检方 2 个独立进程 = **5 个进程逐题逐档 560/560 全同**;
  context 有 13/560 逐位不同 (HNSW 抖动真实存在) 但没有一处把 recall 推过判据边界。
- **红线程序化复扫**: 对 `data/study/st01/catalog.json` 的 `oid/name/label/description/
  summary_format/question/alias` 值 (628 条) 逐字面扫 4 个新文件, **唯一命中是 `st01` 化名本身**。
- `pytest` **958 → 980 passed / 0 F / 0 E / 0 S**。**生产代码零改动** (`server/` 未动)。

**⛔ 三条必须点名**:
1. **拿到确定性证明的是「配额安全」(139 题零回归), 不是「配额有收益」**。上行分辨力被天花板
   封死 (138/140 已 1.0, 余量 0.83pt), **+0.4762pt 100% 来自 q38 一题, 而 q38 正是配额这条
   思路的设计出发点 —— 在设计它的那道题上验证它有效, 不构成独立确认**。
   **脚本里预注册的结论文字 "挤占有害被确定性证明" 比证据能给的更强**; 按硬规矩 8 不许看到
   数据后改, 故原样留在代码里, 正确读法写在收口证据 §5.1 (硬规矩 10: 方向与强度分开写)。
2. **「挤占是否伤害答案质量」仍然未知**。本实验测的是 gold 召回。且 q38 在 `cap=2` 下 context
   从 15 段缩到 **5 段** (其余 139 题保持满 15 席), 这个缩减是否伤答案**没测**。
   **§2.A′ 换锚重做层② 的紧迫性没有下降。**
3. **规则 D 只完成一半**。派出两方 (critic 审设计 / scientist 做抽检): **critic 零产出**;
   **scientist 工件齐全但 never 回传报告** (催两次无应答)。实现方只能事后读 `/tmp/audit_*`
   并**复跑它自己设计的变异 harness**。⇒ **可执行工件救回来了, 文字判断 (「这条限制是真是
   粉饰」「逐题机制是否成立」) 没救回来** —— 设计层面的对抗性复核**缺席**。

**抽检方的变异测试抓到一条真缺陷 (这就是规则 D 的价值)**: 11 条注入里 **M3 存活** ——
把 `hidden_loss_shadow` 改成恒返回空, 当时的 17 条单测**全绿**。⇒ **"三档全 0 题"那句话
当时没有任何闸保护, 那个信号是装饰**。根因: 该函数是写完单测**之后**才加的, 没补测试。
已补 5 条断言 (`test_shadow_*` + `test_analyze_carries_the_shadow_signal_through`),
复跑变异 harness **11/11 全红**。

**新立硬规矩两条** (kickoff §3):
- **17. 「派了审查」≠「审过了」** —— 拿不到报告就当那一环没发生, 在收口证据里点名;
  且派 agent 时要求它**边做边落盘**, 不要只在最终报告里给结论 (本轮正因抽检方落了盘才救回一半)。
- **18. 新加的"取证信号"当场补断言, 否则它就是装饰** (硬规矩 16② 的具体化)。

**evidence**: `sdtm-rag/evidence/checkpoints/cap_recall_sweep.{md,json}`
(§5 六类限制 + §5.5 规则 D 只完成一半的点名) · 工具 `sdtm-rag/eval/cap_recall_sweep.py`
(`--summarize` / `--fused-profile` 均零 LLM) · 单测 `sdtm-rag/scripts/tests/test_cap_recall_sweep.py` (22 条)

---

## 2026-08-11 · study C1 文档型 PDF 章节化入库 (DONE, 有条件)

**计划**: `docs/superpowers/plans/2026-08-11-study-c1-doc-pdf-sections.md` (Task 1-6 全走完, TDD 六步/任务)
**commit**: `0b621ea` → `02f4cac` (7 个)

**做成的**: st01 唯一一份有真实章节结构的 PDF (113 页, 日文为主) 按编号标题**确定性**切成
**114 个 chunk** (111 节, 其中 `8.2` 切 3 份 / `22.1` 切 2 份), 正文逐字保留 —— 文档顺序拼回
**逐字节等于**原文首锚点之后的全部内容; 连跑三次目录 sha256 相同 (幂等); 入独立 collection
`study_st01_docs`; `pytest` **980 → 1036 passed / 0 F** (新增 56 条)。

**三把闸, 参照物都在生成器之外**: 编号连续性 (参照文档自身编号序列) / 分割完备性 (参照原始页
文本) / **embedding 上限** (本轮新增, 按写出的**文件**实测, 参照 ingest 侧真实分词器与 8191 硬上限)。

**编号闸首跑 13 条违规的逐条裁定** (计划要求"不许放宽正则让它变绿", 未放宽):
- **3 条 = 切分器假锚点 (真缺陷)**: 正文里以节号开头的引用句满足锚点正则, 在第 8 章正文区凭空
  造出 2 个 `6.4` 节。判别器取「标题不含句末句点」—— 113 个锚点上命中 2 条、正好是这 2 条、
  **零误伤**; **刻意不用长度阈值** (实测真标题最长 53 字符 > 那两条假锚点的 45/40, 必误伤)。
- **10 条 = 闸自身口径 bug**: `check_numbering` 把 `6.2.3.1` 的父号当成 `6`, 把 9 个真四层标题
  全误报。改为父前缀 = 去掉末段。变异测试钉住"同父前缀下末段回退仍要红"。

**两处实质偏离计划**:
1. **D1 分库 (用户决策)**: 计划要求 cards + docs 同库合流。照做后实测 **study golden v2
   87.50% → 78.1% (6 题回归 / 0 上升)** —— 长篇日文章节在向量相似度上压过卡片, 在回归题里占掉
   top-5 的 **1-4 席**。改为 doc 进 `study_st01_docs`, 卡片侧回到 **87.50% 且逐题 Δ0**。
   `test_main_persists_docs_into_a_separate_collection` 钉死分库。**代价: doc 内容本轮检索不到。**
2. **D2 新增二次切分**: `embed_texts` 对超 8191 token 文本**截断后继续** (只打 WARNING) —— 文本
   整篇入库但向量只覆盖前半截, 而入库计数与前两把闸**全绿看不出来** (静默降级)。实测 2 节超限
   (16173/9738 token)。按行贪心切 + 优先回退到空行 + 页码逐份重算 + 份号进文件名与 provenance。

**规则 A 独立抽检 (N=9 + 全集 114 复扫)**: 判定**有条件 PASS**, 三条硬判据 (逐字/页码/文件名)
全过, 9 个样本正文串在全文里出现次数均为 1。**抽检方抓到 4 条实现方自查全漏的限制**, 最重的是:
**L1 首锚点之前 66,200 字符 = 全文 27.42% 不属于任何 chunk** (目录 49,320 排除合理, 但卷首 +
第 1 章约 16,880 字符是实体内容, 检索不到) —— 而**分割完备闸的口径是「首锚点之后」, 对这条
天然免疫**, 闸绿 ≠ 内容都能检索到。其余: 页眉/页脚渗入 (96/103 行 → 57 个 chunk, 属逐字保留的
必然结果)、第 15 章无子节其内容被标成 `14.4`、3 个 part 切点里 2 个疑似切断表格。

**⛔ 三条必须点名**:
1. **doc chunk 现在检索不到** —— 分库欠的账。接线前必须先有 doc 侧题集: 现有 48 题全是卡片题,
   对 doc chunk **零判别力**; 且**答题侧 context 席位挤占是同一个坑, 还没碰**。
2. **L1 的 27.42% 未覆盖**是设计口径的直接后果, 不是 bug, 但必须当显式限制读。
3. **实现方复核抽检结论时发现自己算错了一个数**: 第一版把未覆盖量算成 66,086 (按文件名排序当成
   文档顺序 + frontmatter 切分每文件多留 1 个换行 × 114 = 正好 114 字符差), 抽检方的 66,200 才对;
   已用**非自洽写法**复证 `allbody == full[66200:]` 逐字节相等。硬规矩 17 的另一面: 派了审查还得
   核验它, 但核验方自己也会错, 数字必须用非自洽写法复算。

**流程缺陷记账**: 抽检进行中实现方改名了产物目录 (`docs/` → `docs_staged/`) 去恢复生产 collection,
**并发写与抽检未隔离**; 抽检方在新路径完整重跑并诚实指出"纯改名"是推断而非哈希级证明, 事后用
sha256 补证现盘 == 三次跑同一份产物。硬规矩 17 的老毛病复发: **抽检报告落盘了但返回摘要没回传**,
实现方直接读盘并自行复核关键数字。

**evidence**: `sdtm-rag/evidence/checkpoints/study_c1_doc_sections.md` (9 条已知限制 + 复跑命令) ·
`sdtm-rag/evidence/step_c1_audit.md` (抽检方原始报告) · 代码 `sdtm-rag/scripts/study/{pdf_text,
split_sections,render_doc_chunks,build_docs}.py` + `paths.py`/`ingest_study.py` 改动
**下一单元入口**: `milestones/07_rag_kg/DOC_TRACK_KICKOFF.md` (路由词「doc 轨 开始任务」)

### 追记 2026-08-11 · C2 勘察 (零配额) + 路线裁定

C1 收尾后就"下一步做什么"做了一道**零配额勘察** (抽 20 页/份, 只读):

| | 933 页 | 212 页 | 对照 C1 (113 页) |
|---|---|---|---|
| 每页文本量 | 772 字符 | 684 字符 | ~2,100 字符 |
| 含 catalog OID 的抽样页 | 12/12 | 12/12 | — |
| 命中 catalog label | 65 | 71 | — |
| **命中 SDTM 域码 / SDTM 风格变量名** | **0 / 0** | 2 / 0 | 4 / 0 |

**结论 (它否掉了 C2 的主要价值假设)**: ① 两份 PDF 在标识符层面**已被 959 张 field card 覆盖**
(同源 ConfigReport); ② **没有 SDTM 标注** —— 原以为 aCRF 能提供的「st01 ↔ SDTM 知识库」那座桥
**不存在**; ③ 按页粗切会产出 ~1,145 个稀疏小 chunk (≈250 token/块), 是 C1 语料 10 倍、比卡片还多,
而 C1 实测 114 个混库就让 study golden v2 掉 9.4pt ⇒ 在已知会挤占的机制上加压十倍。

**用户裁定 2026-08-11**: 走「先接线」路线 —— 只做 U1 题集 → U2 接线, 用现有 114 chunk 量出挤占;
**C2 闸在 U2 之后**, 且 spec §2 的「页级粗切」**被否**, 必须是**理解语义的抽出**并前置独立勘察单元
(渲染看版面 → 判定信息承载形态 → 给可检验问题样例 → 5–10 页价值探针) 再写 plan。
**联网搜索 (Plan B Phase 4) 同样不插队** —— 其验收标准是"开关关=零回归", 而答题侧现无成规模闸;
且 spec 自己写明它会把 `check_code_grounding` 从阻断降级为 advisory (削弱现有确定性护栏)。
局域网现状 (已绑 0.0.0.0 / 登录门 false / 防火墙关 / 192.168.100.32) 经用户确认**维持现状**。

入口与解闸条件写进 `milestones/07_rag_kg/DOC_TRACK_KICKOFF.md` (路由词「doc 轨 开始任务」)。

---

## 2026-08-12 — doc 轨 U1 Task 6+7: 题集 12/30 → **30/30 建成**

**做成的**: 出题批 2 (跨节 8 + part 家族 5) 与批 3 (表格 5 + L1 池收口), 计分池 **30 题 / 79 fact /
章覆盖 17 / L6 探针 2**, 配比 `12/8/5/5` 与 spec §5 逐项一致。四闸 0 finding · `lint_gold` 0 条 ·
语义自查 0 触发 · **pytest 1106 → 1119**。停止条款三批实测 4.5% / 20% / 22.2%, **均未触发**。

**编制**: 出题 3 方 (`general-purpose`) / 审题 3 方 (`claude`) / 审计 2 轮 / 勘察 1 轮 / 实测 1 轮 /
编辑 2 轮 / 工具开发 1 轮, 共 **13 个 subagent**。规则 D 全程满足 (出题与审题不同 subagent_type + 不同 session)。

**两条系统性计分缺陷 (审题查出, 全池修复)**:
- **正方向**「题面没问的 fact」: `recall = hits/len(facts)` ⇒ 把题面问的全答对仍丢 1/N。
  全量审计 78 条 → 删 **9** 条 (B 6 / C 3)。**批 1 也不干净** (q08.f3 / q04.f2) ⇒ 只修批 2 会留下前后不一致的尺子。
- **反方向**「题面问了无 fact 覆盖」: 59 子问覆盖 58 (98.3%), 补 q18 三处。
  危害更大 —— **答对与否不影响分数, 且从分数上看不出来**。

**四条被实测推翻的既有结论**:
1. **L6 探针供给上限 = 2, 不是 plan 的 ≥4** —— 全语料 **113 切点全覆盖勘察**(无抽样): 可探针 **1** /
   冗余 6 / PII 阻塞 27 / 无劈开 76 / 边缘 2 / 空 1。根因: 「切分器不总切在自然边界」**不成立**
   (114 chunk 中 **111 个正文首行即自己的节标题**, 例外 3 个恰是 `__part` 续块) ⇒ 人为切点只有 3 个且已全查。
2. **`q40` 的 L6 探针被证伪撤销** —— part02 单侧自足 (号→名映射 + 表列 ○ + 凡例) ⇒ 冗余不是互补。
3. **PII chunk 10/114 是错的, 实为 27/114 且是下界** —— 联系方式形态 12 ∪ 人名形态 4 ∪ 第 20 章名簿 18;
   原名单只检**标签**(`email`/`TEL`/`〒`)漏掉**裸号码**与**人名**。
4. **`s10_3` 两个表体在 PDF 文本层就已丢失** (非切分器) ⇒ **L9 盲点第一个具名实例**, 该主题无 gold 可依。

**`q57` 探针经生成侧实测确立 (n=18)**: 三种召回组合 (part02 单侧 / part01+part02 / part02+part03)
下 f2 分别 0/6 · 0/6 · 6/6。反事实控制干净 (换个问法 3/3 能用上 part01) ⇒ 排除「靠模型漏读侥幸成立」。
机制改写为「**模型拒绝用类推冒充脚注原文**」, 非原 note 说的「起点错的可信误答」。
⚠ 是**生成侧**非检索侧; 单模型单温度; **换模型或修剪切口可能翻转**。

**工具**: `gold_semantic_check` 新增 `--mode selfsuff` —— 原 `flagged()` 只收 `not is_gold`,
**gold 按设计豁免** ⇒ 全池覆盖率 ≥0.7 的 24 个 (chunk,题) 对**全是 gold, 无一会被 FLAG**,
而 **L6 探针按定义就是多 gold 题** ⇒ 该工具对最需要它的题型覆盖率恒为 0。新模式在真实数据上只报 q24
(已人工判为真跨节)。物理变异实测 8 测试变红。⚠ **新模式不在默认输出里**, 须进 Task 10 收口清单。

**方法论 — 第八类失败形态**: 交接旧版 §4 记的七次是「绿灯不可能变红」; 本轮是**镜像**——
「**红灯从未发生过**」(把推断写成实测语气), 共 **6 例含 controller 自己 1 例**,
**全部由复现驳回抓出, 无一次自查发现**。对策与「变异必须先看到它变红」并列:
**写「实测」必附可复跑命令, 没跑就不写。** 同期另有**三次「数字分歧实为口径差」**, 每次都靠先查规范化口径才免于误驳。

**流程结论 (比技术发现更该传)**: 「边做边落盘 + 最终回传」写进 brief **约束力接近零** ——
措辞逐次加重, **7 个 agent 里 6 个零回传**。有效的是 controller **主动查盘 + 索取补发**;
**补发不是补救** —— 6 次补发中 4 次内容比首次交付更硬。

**用户提供的归因框架 (2026-08-12)**: **EDC 基于 PRT 但仍有非原则性出入; PRT 偏理论, EDC 偏落地。**
⇒ ① 闸 D 低约束力 (2/30) **不是闸设计坏**, 是两侧语域在流程域结构性不相交 (60 词扫描缺席 59/60);
② 「卡片答不出」对 PRT 流程题是**常态非成就**; ③ 四条「数据源冲突」里**只有 1 条是跨源**(其余是 PRT 自身不一致);
④ **给 U2 的硬约束**: PRT 出的题在 EDC 侧答不出**不一定是检索失败**, 归因须先分清结构性缺失与检索失败。
⑤ 本条**支持 C1 价值假设但属领域论据不是实证**, 不许与「低污染率」那个测量合并引用。

**下一步**: Task 8 (doc-only 上界基线 + 三条自毁条款裁定) —— 交接 `milestones/07_rag_kg/U1_RESUME.md`,
路由词「U1 续跑 开始任务」。⛔ 自毁阈值 **≥95% / ≤40% ⇒ 题集退回重写**, 2026-08-11 定稿写死, **不许改**。

---

## 2026-08-12 — doc 轨 U1 Task 8-10: 上界基线 + 三方核验 + 收口 (U1 CLOSED 有条件)

**结论**: 30 题题集收口。**doc-only 上界实测 100.0% (两遍逐题 NONE 差异), 触发 spec §7
第一条自毁条款 (≥95% ⇒ 退回重写)** —— 阈值与判定规则**未改**, 当场停下上报,
**用户裁定豁免 + 双尺子**: 100% 作 §6.1 接线损耗参照, **k=5 的 88.33% 作判别力尺子**, 题集不重写。

**豁免的实证依据 (k 曲线)**: `0.8667@3 → 0.8833@5 → 1.0000@8` 起饱和。机制是 **15 席 / 114 chunk
= 捞走全库 13.2%** 而每题 gold 仅 1–2 条 (`{1条:20题, 2条:10题}`, 40 条 gold 落 36 个 chunk = 31.6%)。
⇒ **100% 是窗口/语料比不是题太简单**, 按条款字面「出难题」不会降低它。k=5 时 5 题非满分,
`q01`/`q43` 的 gold **完全不在 top-5** ⇒ 题集在小 k 下确有判别力。
排除了三条替代解释: 口径过松 (lint 0 条未唯一定位) / 指标卡死 (k=3,5 给出 <1.0) / 坏基线。

**Task 9 三方核验 (规则 D 五方不同 session)**:
- **Step 1 闸 D 实测 (N=6 分层, 抽样规则先写死)**: 卡片库 judge fact-recall **0.0% ×6**,
  `judge_parse_ok` 全 True, 检索非空转 (每题 5 张卡, 相似度 0.44–0.54) ⇒ 无题移出, 基线不重跑。
  ⚠ **按 plan 字面跑这道闸是装饰品**: `check_fact_recall` 是裸子串而 79 条 fact 是 12–82 字整句
  ⇒ 恒绿不可证伪。改用 `--judge` 并补**阳性对照 (gold 原句拼接 → 1.00 ×6)**, 双向可证伪。
- **抽检方 A (debugger, N=8 哈希抽样)**: 三元组 **24/24 全 PASS**, `docs/` sha256 开工=收工。
  自己抓到 **plan 判据② 的字面写法是已废弃的数量口径**, 对多 gold 题会误判 FAIL (commit `1626f83` 已改逐 gold)。
- **抽检方 B (test-engineer, 物理变异)**: 四闸变异后分别红 **4 / 19 / 7 / 8** 条 ⇒ **0 个装饰闸**;
  闸 B 红名单含复审文档列的**四条 fail-open 回归** ⇒ 那四条是可执行断言不是注释。
  🔴 **点名两条装饰输出**: `[selfcov]` 行与 selfsuff 汇总行删掉后 **1119 passed 一条不红**,
  而同设计的闸 D `[probe]` 行**是被钉住的** ⇒ 照抄了设计没照抄断言。
- **Step 3 controller 非自洽复算**: A 的抽样 / 10 条锚串 PDF 命中页 / ③ 10/10 / L3 (q20 目次 p4)
  **全部逐条复现**; B 的 S4/M6 用不同变异手法 (sed 删整行) 复现。
  **全池扩测**: ① **40/40 条锚串在 PDF 逐字存在** · ② **30/30 题唯一定位** (`grep -F` 路径) ·
  ③ **40/40 页覆盖** ⇒ A 的条件 C1 解除 (⚠ 解除者是 controller 全池复算, **不是第二次独立抽检**)。

**当场修掉的缺陷 (硬规矩 18)**: 给 selfsuff 补两条**整句带数值**断言
(不写 `"1 处" in out` —— 它是 `"11 处"` 的子串, 只证明"打了"不证明"打对了")。
**变异复验两条都变红**, 还原后 1119 passed (加断言不加用例, 总数不变)。

**三次「数字分歧实为口径差」(全部先查口径才免于误驳)**: fact 最长 82(raw) vs 78(去空白) ·
`q40` 锚串同 chunk 内 2 次 (闸 B 是 membership 口径故非缺陷) · 抽中 8 题的 fact 逐字性 16(raw) vs 9(去空白)。
最后一条含义更硬: **21 条 fact 里 7 条只差空白** ⇒ 加强「是改述不是杜撰」, 也再证**跑分必须开 `--judge`**。

**新记的限制**: 闸 C 除零余量外**口径脆弱** —— 最短 fact raw 恰好 12=阈值 但含 2 个空白,
改成去空白口径就变 10 < 12 直接红。

**收口证据**: `sdtm-rag/evidence/checkpoints/doc_track_u1_question_set.md` (22 条已知限制 + §6 不能证明什么
+ §8 给 U2 的 6 条硬约束) · 抽检原件 `evidence/step_u1_audit{,_mutation}.md` ·
触发归档 (gitignored) `data/study/st01/eval/failures/task8_upper_bound_SELFDESTRUCT_TRIGGERED.md`。
**红线自查 PASS**: 三份进 git 文件对 959 个真实 item OID / PDF 真名 / ≥12 字语料 CJK 串**零命中**。

**下一步**: U2 接线 (路由词「doc 轨 开始任务」)。硬约束见收口证据 §8 ——
两把尺子都要报 / 必须跑 `--judge` / 失分不得默认归因到检索质量。

## 2026-08-13 doc 轨 U2 — doc chunk 检索接线 DONE (有条件), 生产默认启用

### 交付
- `server/study_corpus.py` — `StudyCorpusEngine` 组合器 (cards 15 席不动 + doc 追加 N=8) + `make_docs_engine` 工厂
- `server/main.py` / `eval/run_eval.py` — 两条路径共用工厂, 跨路径同源闸 `test_docs_engine_parity.py`
- `server/federation.py` — `_ROUTER_SYSTEM` 的 study 语料描述补上手順書章节
- `eval/judge_controls.py` — 阳性/阴性对照 harness (抽样规则先写死)
- 新 flag: `--study-docs` / `--doc-seats` / `--corpus {auto,cdisc,study,both}`
- 1119 → **1181 passed**

### 数字
| 尺子 | 值 |
|---|---|
| ① 接线损耗档 (强制 study, N=15) | 1.0000 ⇒ **接线损耗 0.00pt** |
| ② 判别力档 (强制 study, N=5) | 0.8833 (与 U1 逐位) |
| ③ 生产档 (auto, N=8) | 0.9000 ⇒ **判库损耗 10.00pt** |
| 卡片侧检索 三遍协议 | 0.875 逐题 Δ0 |
| doc 侧答题 OFF → ON | 0.0333 → 0.9517 |
| 路由闸 | 178/181 → 179/181, fatal=0 |

生产 N=8 = 召回天花板上的最小 N (N=10/15 零增益却把 context 推到 3.68x/5.19x)。

### ⛔ 自毁条款 3 触发, 用户 2026-08-13 裁定豁免
阈值一字未改。补测 **ON-ON 对照**后驱动它的 `q23r` 不复现 (ON-A 0.0 / ON-B 1.0),
ON 臂自身噪声 +2.78pt = 声称效应量, 四种 OFF×ON 组合跨 −4.17 到 +0.00。
⇒ **卡片侧回归「未被建立」而非「已被证明不存在」**。引用必须写「触发了, 用户豁免」。

### 方法论产出 (跨单元可复用)
1. **变异测试三个搜索方向不等价**: ①从断言出发 (上界 = 已有断言集合) · ②**从代码行出发**
   (抓到删光 27 行装配块测试一条不红) · ③**从断言的逻辑形状出发** (**对调型是集合/差集类
   断言的系统性盲区**, 本单元命中 5 次)。
2. **检索非确定性**: 源在 embedding API, 固定向量下检索完全确定 ⇒ 「逐题 Δ0」必须连跑 3 遍;
   本仓历史上所有「零回归」都是概率陈述。
3. **空臂 (OFF vs OFF) + ON-ON 是最低控制配置** —— 缺一条就会把不复现的抖动读成真回归。
4. **输出说成功不代表事情发生了** (自己栽过: shell 变量未加引号致 6 次跑批全失败而 echo 照打 done)。

evidence: `sdtm-rag/evidence/checkpoints/doc_track_u2_wirein.md`
spec/plan: `docs/superpowers/{specs,plans}/2026-08-12-doc-track-u2-wirein*`
下一单元: 无默认, 5 个独立候选见 `milestones/07_rag_kg/DOC_TRACK_KICKOFF.md` §0′

## 2026-08-13→15 doc 轨 U3 — 判库侧收口 (⛔ FAIL 收口, 修法退回; 尺子与 gold 存续)

> 分支 `doc-track-u3` · spec/plan `docs/superpowers/{specs,plans}/2026-08-13-doc-track-u3-corpus-routing*`
> 收口证据 `sdtm-rag/evidence/checkpoints/doc_track_u3_corpus_routing.md` (§6 已知限制 11 条 + §9 硬约束 6 条)
> 失败归档 `sdtm-rag/evidence/failures/u3_task{5,8}_attempt_1*.md` (规则 B) · 核验原件 `evidence/step_u3_audit{,_mutation}.md`

### 时间线 (10 task)

- Task 1-3: 量具 —— `eval/compare_runs.py` (run 比对器, 测试守护) / `both` 三档尺子 (三遍全一致,
  cards @both −5.21pt 悬着未付) / 路由闸支持手順書 gold + 分组计分 + 六条条款 `gate_verdict`。
- Task 4-5: 规则 D 隔离出题 42 题 (24 手順書 + 12 干扰 + 6 真两可) + 确定性 (chapter,id) 奇偶
  划分 dev/heldout 12/12 + 题面 gitignored 双红线闸。中途 attempt 1 失败归档: plan 初版把
  held-out 题型逐字写进派发段, task-brief 原样抽走 = 泄漏源 (u3_task5_attempt_1_question_leak)。
- Task 6: T3 基线冻结三遍 (fatal=10, 253/253 稳定)。途中「根因被证伪」结论自己又被撤回
  (基线只是第 4 个盲写实例), 目标由用户裁定重定向为两方向同修。
- Task 7: 唯一生产改动 —— `_ROUTER_SYSTEM` 规则 1 排除条款 + 规则 3 both 判据 + 兜底句, 5 轮
  (含用户裁定扩大改动面至兜底句 + 事前登记退回条件)。只看 dev, 出口 12/12。
- Task 8: 全闸三遍 → **条款 1 触发 (fatal 9 ≠ 0 三遍同, 距 0 非边缘)**。修 2 坏 1, `dist_05`
  both→study 非致命错变致命错, 条款 4 exact 口径 7/12 持平**没抓到**。归档停下上报;
  **用户三选一裁定「退回」**, `c754bed` revert, 退回验证与冻结基线逐题 EXACT MATCH。
- Task 9: 三方核验 (五方不同 session, 用户点单): 审查方 0C/4I/5M · 抽检 A 10/10 复现 + 7
  findings (2 HIGH) · 抽检 B 69 变异终态 SURVIVED 0 · controller 非自洽复算全对上。
  1259 → **1275 passed**。
- Task 10 (2026-08-15): 收口 —— checkpoint 补完 §4-§10, kickoff §0′ 重排 (C2 旧编号 §U3 更名),
  PROGRESS / AGENT_GUIDE / CLAUDE.md 同步。findings 处置 = 记已知限制 + 硬约束, 本单元不修。

### 复盘 (规则 C)

**保留下来的做法**:
1. **尺子先于修法 + 防对症下药三道防线** (基线冻结 / 实现方只看 dev / legacy floor) 全按设计
   工作 —— 可见集出口绿 (dev 12/12) 而全闸如实拦下, 这正是花钱买的那个判定力。
2. **事前登记退回条件** (Task 7 第 5 轮扩改动面时把「条款 1 触发即退回」写在跑之前) 让 FAIL
   收口无争议可执行, 用户裁定只花一轮。
3. 抽检方 B 的**机械 scrubber** (从 gitignored yml 提 244 敏感串逐字滤 stdout 再落盘) 是红线
   自动化的正确形态, 值得做成共用工具。
4. 变异测试三方向 (断言/代码行/逻辑形状-对调型) 第三次复用, 又抓到两大缺口 —— 该清单已稳定,
   写进了下一单元硬约束。

**必须补上的缺口**:
1. **判定脚本与判据仪器自身是本单元最弱一环**: `u3_task8_verdict.py` 整文件零测试 (FAIL 结论
   唯一出处, 5 变异可翻结论不留痕; 已补 9 case) / `--runs 0/1` 也打「三遍一致」 / 无输入校验 /
   `by_group.passed` 挂错阈值。**闸的代码要与生产代码同等对待, 立项时就写测试**。
2. **条款 4 的 exact 口径方向错** —— 对「非致命→致命」零敏感又误杀真改善; 尺子在立项评审时
   没人问过「它对哪类回归失明」(硬规矩 19 只被用在完备性闸上, 应推广到每条自毁条款)。
3. **u1_doc 27 题的漂移方向没有任何条款看着** (I-3) —— 修法受力方向上整组真空。
4. run json 无 run 级元数据, 「三遍」对事后读者不可证伪 (A-3) —— 跑批工具应写入时间戳/参数指纹。

**关键决策复盘**:
1. **用户裁定退回而非豁免/续攻是对的**: fatal 9 距 0 非边缘, 且审查方独立探针证明措辞杠杆已到底
   —— 续攻 prompt 层是把 token 花在没有行程的方向上。
2. **「修法失败」≠「单元失败」**: 存续产物 (253 题闸 + both 尺子 + 六条条款) 正是下一次修法
   能被诚实评估的前提; 本单元把「判库欠账」从传闻变成了带仪器的已量化问题。
3. **spec 初版把题型写进 plan 派发段**是本单元自己栽的坑 (泄漏 attempt 归档) —— 隔离设计的
   文本本身也是泄漏面, 「给 controller 的纪律」段不得随 brief 抽给被隔离方, 已写回 plan。
4. 审查方三问的答案 (「散文 pattern-level, 有效层 example-level」) 说明**反例词表闸挡得住
   字面泄漏, 挡不住决策结构等价于词表** —— 下一单元若重启修法, 防线要从「禁词」升级到
   「禁结构」或干脆离开 prompt 层。

## 2026-08-17 doc 轨 U5 both 答题侧代价 + 答题侧仪器 收口 (DONE 有条件)

**单元**: kickoff §0′ 原候选 #3+#4 合并 (用户点单 2026-08-16, 收益侧明确出局)。
spec/plan `docs/superpowers/{specs,plans}/2026-08-16-doc-track-u5-both-answer-cost*` (spec 含
修正案 1 federation 观测属性 / 修正案 2 I3 阈值对齐 U2 冻结判据, 均经用户批准)。
收口 `sdtm-rag/evidence/checkpoints/doc_track_u5_both_answer_cost.md` · 分支 `doc-track-u5`。

**产出**:
- 工具三件 (TDD, 判据先于数据): 逐题 routed/fallback 观测字段 (生产改动仅 federation.py 2 行
  零行为属性) · `eval/rejudge_run.py` judge 重判探针 · `eval/u5_verdict.py` 六段冻结判定
  (36 例 + 字面断言兜底)。任务级审查 9 轮 (T1×2 / T2×4 / T3×4), 每轮变异自证。
- 测量: I3 对照 1.0/0.0×2 → 12 答题 run (4 配置 ×3, parse_fail 全 0) → 2 rejudge probe →
  6 auto run → 判定 rc=0。1275 → **1353 passed**。

**数字与结论** (引用纪律见 checkpoint §6):
- E2 = cheap_on_this_ruler, **必须连可比池 (cards 41/48 · docs 29/30) 与最坏界并列口径**:
  最坏界 2.08pt 稳健退化在 `st01_v2_q14`/`q21` (检索脆弱题 ⇒ 传导实锤), 聚合 −0.69pt;
  +2.78pt 收益禁作放宽 router 论据。**修法线必要性未被解除**; auto 实判 both 的 5 题免费。
- 触发率演绎→观测: auto 分布逐位复现 U3; fallback 243/243 False **但 4 题路由打空未触发**
  (判库欠账 10pt 本体首次逐题观测); 脆弱 4 题 12/12 全 study。

**三方核验 (规则 D 五方)**: 审查方条件通过 (2C/4I/3M; C1 双口径反向与抽检 A F-1 同机制独立
命中; 引用纪律 11 条越界清单) · 抽检 A 64/64 全复现 + 7 findings (`evidence/step_u5_audit.md`)
· 抽检 B 148 变异终态 SURVIVED 0, 冻结期存活 0 (`evidence/step_u5_audit_mutation.md`) ·
controller 亲手复现 q14/q21/q08 逐遍数字。

**Retro (规则 C)**:
- 保留: 判据先于数据 + T5 前三轮加固窗口用尽 (U3 §6-10 教训落地); 逐题配对设计使 3.47pt 聚合
  噪声下仍能出可辩护结论; 抽检最坏界并列尺子应成为今后 E1 类判定的标配。
- 必须补的缺口: E1 稳定性过滤偏删代价信号 (F-1) / E4 并集无闸 (C2) / I-1 latent 结论词不抑制
  — 全属判据变更, 冻结期不修, 重启答题侧测量前须用户裁定后重建基线。
- 关键决策复盘: ① 「cheap 判词按冻结规则存续 + 并列口径入档」优于当场改判 — 判据可信度靠
  一次性冻结, 修尺子留给下一单元; ② 观测字段选「生产 2 行属性」而非「eval 自行判库」是对的
  (防两路径漂移); ③ 变异 harness 两坑 (pytest -rf 吞收集错 = 假阴性 / 同秒 pyc = 假还原)
  已固化进抽检 B 流程, 今后变异必 purge __pycache__ + compile 前置。
