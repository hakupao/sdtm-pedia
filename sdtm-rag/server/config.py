"""Application settings (pydantic-settings, loaded from .env).

PLAN §4 decision table + .env.example define all knobs.
API keys are loaded into os.environ via dotenv for LiteLLM auto-detection.
App settings use SDTM_RAG_ prefix.
"""
from __future__ import annotations

from pathlib import Path

from dotenv import load_dotenv
from pydantic import BaseModel
from pydantic_settings import BaseSettings

_SDTM_RAG_ROOT = Path(__file__).resolve().parent.parent
_REPO_ROOT = _SDTM_RAG_ROOT.parent  # sdtm-pedia repo root

load_dotenv(_SDTM_RAG_ROOT / ".env")


class SelectableModel(BaseModel):
    """用户可在 Chat UI 选择的答题模型。

    这是 Router 模型组与前端下拉的**唯一事实源** —— 两者都从这张表派生, 故
    「UI 提供了 Router 没有的模型」在结构上不可能发生 (spec §3.1)。
    """

    id: str          # Router 组名 = 前端提交值
    label: str       # 下拉显示文字
    model: str       # litellm 模型串
    verified: bool   # ⟺ 该模型跑过反捏造抽检 (Rule 9 + 答题侧 guardrail) 并通过
    # 单次回答的输出上限 (token)。**必须显式写出来**: `bedrock/converse/...` 这条路径下
    # litellm 只在"开了 thinking 又没给 max_tokens"那一支才补 `maxTokens`, 其余情况整个
    # 字段缺席, Bedrock 于是落到一个远低于模型上限的服务端默认值 —— 2026-09-08 一条
    # ~3.5k 汉字的答案在 ≈4k output token 处半句话被切断, 那次截断本身就是"缺席时拿到的
    # 不是模型上限"的证据。默认 128000 是为了让 `SDTM_RAG_SELECTABLE_MODELS` 的 JSON
    # 覆盖可以省略本字段 (省略 ⇒ 有天花板, 而不是没有)。
    max_output_tokens: int = 128000


class Settings(BaseSettings):
    # LLM models (PLAN §4.2 D-2)
    default_model: str = "anthropic/claude-sonnet-4-6"
    fallback_model: str = "deepseek/deepseek-v4-pro"
    hard_model: str = "anthropic/claude-opus-4-7"
    light_model: str = "anthropic/claude-haiku-4-5"

    # 用户可选答题模型 (spec §3.2)。只作用于**答题**; 判库(light)/检索改写不受影响 (C1)。
    # verified 的语义写死: 跑过反捏造抽检并通过。2026-09 兑现抽检 (102q, 预登记判据
    # evidence/checkpoints/verified_spotcheck_2026-09.md): opus-5 / gpt-terra / gpt-sol 过;
    # sonnet-5 (a) 层 1 条 ungrounded (q35 C66742) ⇒ false。sonnet-5 是 Claude 不代表验过。
    #
    # max_output_tokens 的出处 (evidence/checkpoints/autocontinue_2026-09/research-max-output-tokens.md):
    # · opus-5 / sonnet-5 = 128000 —— AWS Bedrock model card 明写 "Max output tokens: 128K"。
    # · gpt-terra / gpt-sol = 128000 —— ⚠ **未经一手文档确认**: AWS 那两张 model card 只列
    #   1M context window, 没有 max-output 行; 128000 只来自 litellm 的静态 model_cost 表。
    #   由探针实测兜底 (evidence/checkpoints/autocontinue_2026-09.md): provider 若拒收这个
    #   值会当场 ValidationException, 是**响的**失败, 不是静默截断。
    selectable_models: list[SelectableModel] = [
        SelectableModel(id="opus-5", label="Claude Opus 5",
                        model="bedrock/converse/global.anthropic.claude-opus-5",
                        verified=True, max_output_tokens=128000),
        SelectableModel(id="sonnet-5", label="Claude Sonnet 5",
                        model="bedrock/converse/global.anthropic.claude-sonnet-5",
                        verified=False, max_output_tokens=128000),
        SelectableModel(id="gpt-terra", label="GPT-5.6 Terra",
                        model="bedrock/converse/global.openai.gpt-5.6-terra",
                        verified=True, max_output_tokens=128000),  # 未验证值, 见上
        SelectableModel(id="gpt-sol", label="GPT-5.6 Sol",
                        model="bedrock/converse/global.openai.gpt-5.6-sol",
                        verified=True, max_output_tokens=128000),  # 未验证值, 见上
    ]

    # ── 内部组的输出上限 (2026-09-08) ────────────────────────────────────
    # 与 selectable_models 的 max_output_tokens 同一件事, 只是内部四组的模型串是上面四个
    # 标量字段, 没地方挂。⚠ 四个值**不能共用一个**: 各模型的真实上限不同, 抄高了会被
    # provider 当场拒 (响的失败), 抄低了则是静默截断 —— 后者正是本次要修的病。
    # 环境覆盖走既有 SDTM_RAG_ 前缀 (SDTM_RAG_LIGHT_MAX_OUTPUT_TOKENS 等), 无需额外代码。
    #
    # ⚠ **接缝** (2026-09-08 实测): `.env` 改的是上面四个**模型串**, 不会自动改这四个天花板。
    # 生产 .env 就把 default/hard/light 三个全指到了 `bedrock/converse/global.anthropic.
    # claude-opus-5`, 而下面的注释写的是 config.py 里那几个**默认**模型的上限。两者错配时:
    #   · 天花板 < 模型真实上限 ⇒ 只是把输出封得更低, 触顶自动续写兜得住 (light 现在正是
    #     这种情况: 64K 封在一个 128K 的模型上, 而判库/改写本来就只吐几十个 token)。
    #   · 天花板 > 模型真实上限 ⇒ provider 当场 ValidationException, **响的**失败。
    # 换模型串时请连着这里一起看一眼; 两个方向都不会静默截断, 但第二个会拒服务。
    default_max_output_tokens: int = 128000   # claude-sonnet-4-6: 128K (platform.claude.com)
    hard_max_output_tokens: int = 128000      # claude-opus-4-7: 128K (AWS model card)
    light_max_output_tokens: int = 64000      # claude-haiku-4-5: 64K —— ⚠ 只有上面两个的一半
    # DeepSeek: 研究报告找不到一手文档, 只有第三方博客说 384K (litellm 静态表 393216)。
    # 32000 是**保守值**, 不是实测上限: fallback 是容灾路径, 宁可让极长回答多续写两轮
    # (触顶自动续写兜得住), 也不拿一个没有一手背书的大数去赌 provider 不拒。
    fallback_max_output_tokens: int = 32000

    # 输出触顶后自动续写的最大轮数 (0 = 关掉自动续写)。这是**跑飞兜底**, 不是预期值:
    # 天花板抬到 128K 之后正常回答一轮就该写完, 真跑到 8 轮说明模型在打转 ——
    # 那时 done 事件会报 truncated: true, 前端挂警告, 而不是假装答案是完整的。
    max_continue_rounds: int = 8

    # Embedding (D-4 v3: OpenAI cloud)
    embedding_model: str = "text-embedding-3-small"
    embedding_dim: int = 1536

    # RAG
    top_k: int = 15
    collection_name: str = "sdtm_kb_v1"

    # ── Plan B 联邦路由 (spec docs/superpowers/specs/2026-08-04-plan-b-federated-routing-design.md) ──
    # 默认开 (2026-08-04, Phase 1 三闸全绿后翻 True): 服务启动时构建 study 引擎 + 联邦层,
    # /api/ask 的 corpus=auto 走 LLM 判库。闸结果与已知边界见
    # evidence/checkpoints/planb_phase1_federation.md; 需要回退到纯 CDISC 单库时设
    # SDTM_RAG_FEDERATION_ENABLED=false (corpus 参数此时被静默忽略, 刻意的前向兼容)。
    federation_enabled: bool = True
    study_collection_name: str = "study_st01"
    # study 侧 KB 根。RAGEngine 要求 kb_root 下直接躺着 ROUTING.md + INDEX.md, 而 study 侧这两个
    # 文件与 959 张卡同在 cards/ (scripts/study/paths.py: cards_dir = out_dir / "cards"), 所以根
    # 指到 cards/ 而不是 st01/ —— 指错时开着 federation 启动即 FileNotFoundError。仿 kb_root 的
    # 默认构造方式从模块级根常量拼出; 服务目录自包含部署用 SDTM_RAG_STUDY_KB_ROOT 覆盖。
    study_kb_root: Path = _SDTM_RAG_ROOT / "data" / "study" / "st01" / "cards"

    # S2 study 结构化直查 (Plan B Phase 2)。默认开 (2026-08-06, Phase 2 验收闸全绿后翻 True)
    study_lookup_enabled: bool = True
    study_catalog_path: Path = _SDTM_RAG_ROOT / "data" / "study" / "st01" / "catalog.json"
    study_aliases_path: Path = _SDTM_RAG_ROOT / "data" / "study" / "st01" / "lookup_aliases.yml"

    # U2 doc 通道 (spec 2026-08-12 §4.5): study 侧除 959 张卡片外, 还有 114 个手順書章节
    # chunk 在独立 collection 里。加席不抢席 —— cards 的 top_k 不动, doc 另取 seats 席。
    # collection 不存在而开关开着 = 配置错误, 启动响亮失败 (见 main.py), 不静默降级。
    #
    # 默认 True (2026-08-13 翻转)。收益侧: doc 侧答题 0.0333→0.9517、doc 侧检索 0→1.0
    # (evidence/step_u2_answerside.md)。代价侧: 卡片侧回归**未被建立** —— ON-ON 对照显示
    # 驱动自毁条款 3 的 q23r 不复现, ON 臂自身噪声 +2.78pt 已达声称效应量, 四种 OFF×ON
    # 组合跨 −4.17 到 +0.00pt。**自毁条款 3 因此是触发状态**, 由用户 2026-08-13 裁定豁免
    # 后翻转 (不是"未触发", 也不是"验收通过")。回退: SDTM_RAG_STUDY_DOCS_ENABLED=false。
    study_docs_enabled: bool = True
    study_docs_collection_name: str = "study_st01_docs"
    study_docs_seats: int = 8

    # Rerank (T2, PLAN §5 1B.2): wide retrieve -> Cohere rerank -> top_k.
    # COHERE_API_KEY read from env (LiteLLM-style provider key, no SDTM_RAG_ prefix).
    # NOTE: T2 ablation (2026-06-08) found rerank degrades source recall on this KB
    # (demotes structured spec.md). Kept off by default; see eval/ablation_retrieval_2026-06-08.md.
    rerank_enabled: bool = False
    rerank_model: str = "rerank-v3.5"
    rerank_candidates: int = 100  # candidate pool size before rerank (T1: ~100 needed)

    # Query expansion (T4): improve cosine recall by rewriting the query, NOT by
    # reordering results. "multiquery" = LLM decomposes -> per-subquery search -> RRF
    # fuse. "hyde" = LLM writes a hypothetical answer, embed that. Generic prompts
    # (not tuned to any eval set). expansion_model uses an existing cloud key.
    query_expansion: str = "none"  # none | multiquery | hyde
    expansion_model: str = "deepseek/deepseek-chat"
    expansion_n_queries: int = 4  # multiquery: original + (n-1) generated sub-queries

    # ── P1 retrieval levers (validated combination, default ON in production) ──
    # S1 + S2 are the validated P1 query-condition-routing combination (retrieval-
    # only v2 102q: single 100 / cross 96 / concept 100 / mixed 100 / overall 99.0%,
    # 2026-06-09). They MUST ship together: hybrid alone demotes single_domain
    # (96→83); only S1's deterministic prepend + routing keeps the combination
    # stable. Each is env-overridable (SDTM_RAG_STRUCTURED_LOOKUP_ENABLED=false /
    # SDTM_RAG_HYBRID_ENABLED=false) for an instant rollback to plain cosine.

    # Structured lookup (S1): deterministic var/CT-code -> gold-file resolution on a
    # non-vector channel (spec.md xref + VARIABLE_INDEX), union-added ahead of cosine
    # for terminology/distribution queries embeddings can't reach. Zero side effect
    # (union-add, capped at top_k), so safe to default on.
    structured_lookup_enabled: bool = True

    # DM1 D2: S1 命中域且问法是域级 (问句没点名任何已知变量) 时, 该域 assumptions.md
    # 的定义块保底占注入首席。单域时名额从 S1 自己的 N 席里出 (N-1 条 spec 行), 总注入
    # 席位不增 —— 所以对非域级问法零影响, 可默认开。
    domain_definition_seat_enabled: bool = True

    # DM1 D3: 问句里认出的域码 (≤3 个) 追加该域 meta.yaml 里的正式名 (label), **只**喂
    # 稠密/BM25 (见 rag.py `q_ret`)。零 LLM、纯确定性; 问句里没有已知域码时恒等于原句,
    # 所以对绝大多数问法零影响, 可默认开。LLM 看见的仍是原问题。
    # ⚠ 只加 label 不加 structure —— 后者是跨域通用的记录粒度模板, 加了会回归
    # (evidence/failures/dm1_task5_attempt_1.md)。
    domain_expand_enabled: bool = True

    # Hybrid BM25 (S2): lexical retrieval over the SAME indexed chunks (bm25s, pure
    # CPU arithmetic — no neural model), additively fused with dense cosine so
    # literal domain/relationship/variable-name hits that cosine buries re-float
    # without demoting cosine's wins. RRF is parameter-free; the weighted path's
    # alpha is the dense weight (1-alpha goes to BM25).
    hybrid_enabled: bool = True
    hybrid_fusion: str = "rrf"  # rrf | weighted
    hybrid_alpha: float = 0.5
    hybrid_pool: int = 30  # per-list fusion pool depth (v2 robust sweet spot; deeper adds tail noise)

    # DM1 D5: query 侧 BM25 停用泛用语 (sdtm/cdisc/domain/dataset 等 —— 见 rag.py
    # `_BM25_QUERY_STOPWORDS`)。只改查询 tokenize 的停用表, index 侧分毫不动, 故零副作用
    # 可默认开。关掉退回 bm25s 内置 english stopwords (T6 之前的行为)。
    bm25_query_stopwords_enabled: bool = True

    # ── Answer-side trust guardrail (system-prompt only; orthogonal to retrieval) ──
    # Two grounding rules appended to the system prompt that forbid the answering
    # model from emitting content the retrieved context does not contain:
    #   (1) never output a controlled-terminology code (Cxxxxx) not present verbatim
    #       in context — fixes per-value CT-code fabrication (q90/q91/q93, where the
    #       model copied one code then guessed the rest by incrementing);
    #   (2) never assert a domain's SDTM class/category unless context states it —
    #       fixes special-purpose misclassification of relationship datasets (q37).
    # These are answer-side defects present OFF and ON the retrieval levers, surfaced
    # by the P1 wire-in Rule A semantic judge; substring fact-recall is blind to them.
    # Env-overridable (SDTM_RAG_PROMPT_GUARDRAIL_ENABLED=false) for an A/B rollback;
    # when off, the system prompt is byte-identical to the pre-guardrail production one.
    prompt_guardrail_enabled: bool = True

    # ── 联网参考通道 (spec 2026-08-31) ──
    # 联网与 corpus 判库正交: 请求级 `web` 只决定是否把 web_search 工具挂上去,
    # **不动 system prompt**; 本开关才决定 Rule 9 是否进 system prompt。
    # 关掉 ⇒ system prompt 与本功能引入前逐字节相同 (A/B 回滚, 同 prompt_guardrail 先例)。
    web_search_enabled: bool = True
    web_max_rounds: int = 5          # 工具循环轮数上限 (用户裁定)
    web_max_searches: int = 15       # 单次请求搜索次数上限 (用户裁定)
    web_results_per_search: int = 3  # 每次搜索取回条数 (§6.1: 5 条 ≈ 3K token, 收到 3)
    web_result_max_chars: int = 1200 # 单条正文截断 (§6.1 上下文预算)
    web_daily_quota: int = 200       # 日配额兜底, 防忘关跑飞 (§7)
    web_timeout_s: float = 30.0      # 单次 Tavily 调用超时

    # ── Structured answer channel (SP2): deterministic count/enumerate/attribute/CT
    # answers from data/meta/meta.yaml, injected as an authoritative context block +
    # a counting grounding gate. Orthogonal to retrieval (Phase 1 never touches
    # retrieve()). Default ON: validated by the OFF-vs-ON paired eval (v3 140q,
    # 2026-06-20) — q103/q104 green, zero retrieval regression, 0 gate violations
    # (gate v2) + Rule D APPROVE + Rule A PASS. Env-overridable for instant rollback
    # (SDTM_RAG_STRUCTURED_ANSWER_ENABLED=false).
    structured_answer_enabled: bool = True

    # SP3: deterministic relationship/impact/aggregate graph answers from meta.yaml,
    # merged into the structured-answer injection. Default ON after validation
    # (140q zero-pollution=0 + composite ON==OFF byte-identical + Rule D APPROVE);
    # env-overridable (SDTM_RAG_GRAPH_ANSWER_ENABLED=false) for rollback.
    graph_answer_enabled: bool = True

    # AGG: aggregate metadata channel (variables-in-min-domains / most-shared
    # codelists), split out of SP3 after the KG value eval (its only positive niche).
    # Default ON since 2026-07-07 (five AGG gates passed, see
    # evidence/checkpoints/agg_channel_summary.md); env override:
    # SDTM_RAG_AGGREGATE_ANSWER_ENABLED.
    aggregate_answer_enabled: bool = True

    # ── Multi-model compare + judge (Phase 2; DEPLOY_PLAN §2.5–2.7) ──
    # One question → these N models answer over the SAME retrieved context (FR1),
    # shown side-by-side; an optional judge scores the anonymized answers (FR5).
    # FR7: every slot is env/UI-overridable and accepts ANY litellm model string.
    # These are REFERENCE PLACEHOLDERS — DEPLOY_PLAN §7 marks slot defaults as
    # explicitly non-binding (one Anthropic + one OpenAI + one DeepSeek for vendor
    # diversity). Override via .env using JSON list syntax, e.g.
    #   SDTM_RAG_COMPARE_MODELS=["deepseek/deepseek-v4-pro","openai/gpt-4o"]
    # (pydantic-settings parses complex fields as JSON); the UI sidebar exposes a
    # friendly per-slot text box that does not require touching .env.
    compare_models: list[str] = [
        "deepseek/deepseek-v4-pro",
        "openai/gpt-4o",
        "anthropic/claude-sonnet-4-6",
    ]
    # Judge model (DEPLOY_PLAN §2.6). Default = deepseek/deepseek-chat so the judge
    # is runnable TODAY (Anthropic credits exhausted, 2026-06-15). §2.6 prefers Opus
    # for judge quality once credits return — set SDTM_RAG_JUDGE_MODEL then.
    judge_model: str = "deepseek/deepseek-chat"
    # Per-model generation timeout (s): one slow/hung vendor must not stall the whole
    # parallel request beyond this (NFR2/NFR4). Each model also gets one retry.
    compare_timeout_s: float = 120.0
    compare_num_retries: int = 1

    # ── C2R 画面 PDF 按需旁路 (PLAN_c2r_pdf_bypass.md I2-3) ──
    # 2 份画面 PDF はベクトル庫に**入らない** (C2 の DROP 判定は不変)。命中カードの OID を
    # 鍵に確定的に頁を選び、その頁だけを画像で答題文脈に足す附加通道。
    #
    # 既定 **OFF**: ON にすると答題リクエストの形が変わる (user メッセージが文字列から
    # content parts へ, prompt token +1.5k/頁)。48 題 study golden v2 の零回帰が硬闸で、
    # それが通るまで生産では開けない。OFF のとき挙動は本機能導入前と逐位同一。
    pdf_context_enabled: bool = False
    # 頁予算。S0 §4-4 実測で 1 頁 ≈1.5k prompt token ⇒ 6 頁 ≈9k。推奨 6-8。
    pdf_context_max_pages: int = 6
    # S0-3 で 4 モデル全部が 110 dpi の画像から日本語ラベルを正しく読めた。150 は不要。
    pdf_context_dpi: int = 110
    # PDF の実ファイル名は studies.local.yaml にしか無い (真名を code に置かない纪律)。
    # 空 = 起動時に registry から解決する; 明示すれば self-contained な service dir でも動く。
    pdf_context_study_id: str = "st01"
    # 空 = `pdf_context_study_id` から導出 (下の property)。st01 を焼き込むと、study を
    # 切り替えたとき索引だけ前の study のものを読み続ける —— PNG キャッシュ先は study 連動
    # なので、片方だけずれて「頁は出るが中身が別研究」になる。
    pdf_page_index_path_override: str = ""
    pdf_workflow_path: str = ""
    pdf_annotated_path: str = ""

    # ── DM2 研读包旁路 (docs/superpowers/specs/2026-09-15-study-dossier-design.md) ──
    # 域级映射题 (「本研究哪些数据进 X 域」) 触发时: 丢 study 侧 top-k, 把 PRT 白名单章原文 +
    # 全 EDC 项目一览整段喂进上下文. 默认 **ON** (用户裁定 2026-09-15); 不触发的路径与
    # 引入前逐字节相同 (test_router_dossier_wiring 钉). kill switch = 这一行.
    dossier_enabled: bool = True
    # PRT 章号白名单 (匹配 section_number 首段). 范围由 T2 token 计量 + 用户裁定
    # (evidence/checkpoints/dm2_dossier_tokens.md). 改这里 = 改研读包 sha, 存档徽章会变.
    dossier_prt_sections: list[str] = ["4", "5", "6", "7", "8", "9", "10", "11", "12"]
    # 超限 = 启动报错, 不截断 (spec §3). 日文 ≈ 1 字 1 token, 这个上限就是 token 上限量级.
    dossier_max_chars: int = 200_000
    # 空 = 从 study_kb_root (cards/) 推导: docs = cards 的兄弟目录. 与 pdf_* 同一纪律,
    # 显式给值可让 self-contained service dir 或测试 tmp 目录也能跑.
    dossier_docs_dir_override: str = ""
    dossier_cards_dir_override: str = ""

    # Server
    log_level: str = "INFO"
    # Loopback by default (DEPLOY_PLAN §1: 阶段 0–2 绑 127.0.0.1, zero exposure). The
    # launchd plists already pass --host 127.0.0.1 explicitly; this default makes a bare
    # `python -m server.main` safe too. Set SDTM_RAG_HOST=0.0.0.0 explicitly for the
    # phase-3 shared/container binding (which also adds the §7 login gate).
    host: str = "127.0.0.1"
    port: int = 8000

    # ── Phase 3 sharing: login gate + hardening (DEPLOY_PLAN §3) ──
    # Every knob below defaults OFF/permissive so the current localhost dev + launchd
    # service are byte-unchanged. They are flipped ON together at go-live (after IT
    # signoff) via the service-dir .env (see deploy/). Building + testing them here
    # touches no live behavior. SECURITY HEADERS are the one exception — default ON
    # (harmless on localhost, good practice everywhere).

    # Shared-password login gate. When auth_enabled, requests to GET / and /api/* (except
    # /api/health and the /login,/logout routes) require a signed session cookie obtained
    # by POSTing the shared password to /login. The password is stored ONLY as a scrypt
    # hash (server/auth.hash_password -> "salt_hex$hash_hex"); generate via
    # `python -m scripts.gen_password_hash`. session_secret signs the cookie (itsdangerous
    # via Starlette SessionMiddleware) — set to >=32 random bytes hex. Both MUST be set
    # when auth_enabled or the app refuses to start (fail-loud, never silent allow-all).
    auth_enabled: bool = False
    shared_password_hash: str = ""
    session_secret: str = ""
    # 12h. The itsdangerous-signed cookie's max_age is the SERVER-enforced absolute session
    # cap (Starlette rejects an older signed session — the client cannot extend it). A short
    # window limits replay of a sniffed cookie (plain-HTTP-on-LAN residual risk). Rotating
    # SDTM_RAG_SESSION_SECRET is the only revocation lever and is global (logs everyone out).
    session_max_age_s: int = 43200
    session_cookie_name: str = "sdtm_session"

    # Error-string sanitization (SEC MED, deferred from phase 2). On localhost the upstream
    # error text ("credit balance too low") is USEFUL to the single operator, so default
    # OFF. At go-live (shared) set true: /api/ask_compare per-model errors collapse to a
    # generic string for the client; the full detail stays in the server log.
    sanitize_errors: bool = False

    # Per-IP rate limit (hand-rolled in-memory token bucket; no new dep). Applies to all
    # HTTP except /api/health. burst = bucket capacity (max instantaneous), per_min = refill
    # rate. Generous for humans, throttles brute-force / runaway scripts. Single-process /
    # single Mac mini scope (§1); a multi-worker move (§6) would need shared state.
    rate_limit_enabled: bool = False
    rate_limit_per_min: int = 30
    rate_limit_burst: int = 10
    # Trust X-Forwarded-For for the client IP. FALSE by default: §1 serves 8000 directly
    # (no reverse proxy), so the socket peer IS the client and a spoofed XFF must be ignored.
    # Set true ONLY behind a trusted reverse proxy that overwrites the header (§6).
    rate_limit_trust_forwarded: bool = False

    # Security response headers (CSP / X-Content-Type-Options / frame-ancestors etc.).
    # Default ON — the chat UI loads only same-origin assets (vendored marked/dompurify/
    # highlight + app.js), so a strict CSP is defense-in-depth atop DOMPurify.
    security_headers_enabled: bool = True

    # Outer ceiling (s) on a single async /api request's generation phase, on top of
    # litellm's per-call timeout. Guards an unbounded wait if a provider hangs without
    # honoring its own timeout (REV MED-b). Applied to /api/ask_compare's fan-out and the
    # /api/ask_stream open step.
    request_timeout_s: float = 180.0

    # Self-contained service dir overrides (DEPLOY_PLAN §1 + §7 open item): deploy.sh
    # copies knowledge_base/ and data/chroma into ~/MyProject/sdtm-rag-service/ so the service no
    # longer depends on the repo tree. Set SDTM_RAG_KB_ROOT / SDTM_RAG_CHROMA_DIR there.
    # Empty (default) = use the repo-relative paths below (dev / current localhost).
    kb_root_override: str = ""
    chroma_dir_override: str = ""
    dogfood_log_override: str = ""

    model_config = {"env_prefix": "SDTM_RAG_", "extra": "ignore"}

    @property
    def chroma_dir(self) -> Path:
        return Path(self.chroma_dir_override) if self.chroma_dir_override else _SDTM_RAG_ROOT / "data" / "chroma"

    @property
    def kb_root(self) -> Path:
        return Path(self.kb_root_override) if self.kb_root_override else _REPO_ROOT / "knowledge_base"

    @property
    def meta_path(self) -> Path:
        return _SDTM_RAG_ROOT / "data" / "meta" / "meta.yaml"

    @property
    def pdf_page_index_path(self) -> Path:
        if self.pdf_page_index_path_override:
            return Path(self.pdf_page_index_path_override)
        return _SDTM_RAG_ROOT / "data" / "study" / self.pdf_context_study_id / "pdf_page_index.json"

    @property
    def pdf_context_cache_dir(self) -> Path:
        # 描画済み PNG の置き場。data/study/ は .gitignore 配下 ⇒ 版本库に入らない。
        return _SDTM_RAG_ROOT / "data" / "study" / self.pdf_context_study_id / ".pdf_page_png"

    @property
    def dossier_docs_dir(self) -> Path:
        if self.dossier_docs_dir_override:
            return Path(self.dossier_docs_dir_override)
        return Path(self.study_kb_root).parent / "docs"

    @property
    def dossier_cards_dir(self) -> Path:
        if self.dossier_cards_dir_override:
            return Path(self.dossier_cards_dir_override)
        return Path(self.study_kb_root)

    @property
    def dogfood_log_path(self) -> Path:
        # Append-only backlog of chat answers flagged as wrong/weak (⚑ in the chat UI).
        return (
            Path(self.dogfood_log_override)
            if self.dogfood_log_override
            else _SDTM_RAG_ROOT / "dogfood_failures.md"
        )


settings = Settings()
