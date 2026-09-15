# 研读包旁路 (Study Dossier) — 域级映射题的「整本喂」模式

> 日期: 2026-09-15 · 单元代号 **DM2** · 起源: DM1 D4 区分实验裁定 (`sdtm-rag/evidence/checkpoints/dm1_d4_discrimination.md`): study 侧候选卡 0/32 是「SDTM 域定义 ↔ EDC 日文 label」语义鸿沟, 检索层无廉价桥. 用户裁定 (2026-09-15): 走「整本喂」, 不做人手表.
> 用户已定: 触发 = 自动 + 可手动强开/强关; 范围 = PRT 核心章 s4-s12 + catalog 一览; 方案 = A (旁路替换 study 检索, 总闸默认 ON).

## 1. 目标与非目标

**目标**: 用户问「本研究哪些数据进 SDTM 的 X 域」型问题时, 模型上下文里**确定性地**含 (a) X 的域定义 (CDISC 侧, DM1 D2 已做) (b) 本研究 PRT 核心章原文 (c) 全部 EDC 项目一览. 模型据此按域定义类别枚举候选字段并标推测. 任意域 / 任意语言 / 任意问法生效.

**非目标**: 不做「域→表单/章节」人手表; 不用 LLM 选章或改写; 不改 KB / 不重 ingest; 不动 CDISC 侧检索 (D1-D5 保持); 不动 doc 轨席位规则; 不做多研究 (st01 唯一, 但 study id 走 config 不焼き込み).

## 2. 组件

| 组件 | 文件 | 职责 | 依赖 |
|---|---|---|---|
| 研读包构建器 | `server/study_dossier.py` `StudyDossier` | 启动时一次性读 `data/study/<id>/docs/` 白名单章节 + `cards/` (排除 INDEX.md / ROUTING.md, 只取 doc_type=field_card) 生成一览, 拼成一段文本; 记 sha256 / 字数 / 章节清单. 纯文件读, 无 LLM, 无网络. | settings |
| 触发器 | `server/dossier_trigger.py` `decide_dossier()` | 纯函数: (问句, 请求档位, 总闸, 域码识别函数) → `DossierDecision(attach: bool, reason: str)`. 域码识别函数注入 (CDISC 引擎 `app.state.rag` 的 `StructuredLookup._query_domains`, D1 口径), 不在触发器里重写正则. | D1 |
| 接线 | `server/router.py` `ask_stream` / `ask` | 在 `fed.retrieve` 之后 `format_context` 之前: 触发则丢 study chunks, corpus 强制 both, 上下文追加研读包块, system 追加研读规则句; SSE `sources` 事件 + 存档记 `dossier` 状态. | 上两者 |
| 请求字段 | `AskStreamRequest.dossier: Literal["auto","on","off"] = "auto"` (`AskRequest` 同) | 手动覆盖. | — |
| UI | `webchat/index.html` + `app.js` | 「研读模式」三态控件 (自动/开/关), 与「联网参考」同一行; 回答区徽章「📖 研读包 ·  N 章 · M 字」. | — |
| 配置 | `server/config.py` | `dossier_enabled: bool = True` (总闸); `dossier_prt_sections: list[str] = ["4","5",...,"12"]` (章号白名单, 匹配 `section_number` 首段); `dossier_max_chars: int = 200_000` (超出 fail-loud 启动报错, 不截断); `dossier_study_id` 复用 `pdf_context_study_id`. | — |

## 3. 研读包内容 (确定性, 与文件字节一一对应)

```
# 【本研究 研読パッケージ】 (study=st01, version=V59, sha=…, N 章 / 959 項目)
## A. 研究計画書 (PRT) 抜粋: 第 4-12 章
### 4.1 選択規準  (p.NN-NN)
<st01__doc01__s4_1.md 正文, 去 frontmatter>
… (按 section_number 自然序; 分 part 的章按 part 顺序拼回一段)
## B. EDC 項目一覧 (全 959 件; フォーム / 項目 / OID / 型 / 選択肢)
[<フォーム label> F_REG] <項目 label> (I_REG_DAT) | date 必須
[<フォーム label> OC] <項目 label> (I_OUTC) | integer 必須 | 1=<値> 2=<値> 99=<値>
(代称见 gitignored data/study/st01/eval/dm1_codenames.md; 真实行形 = 卡片标题行原样)
…
```

- A 部来源 `docs/*.md`, 章节顺序 = `section_number` 版本号排序 (4.1 < 4.2 < 6.2.3.1 …). 前付 / s2-s3 / s13-s22 不进 (白名单外).
- B 部来源 `cards/*.md`: 每卡一行 = 标题行 + `型/必須` + Codelist 值 (有则列, 无则省). 不含 Edit checks / 表示条件 / 非表示アクティビティ (那是 C2R 通道的事). 按 form_oid 再 item 行号排序 (catalog `row`), 与 catalog 同序.
- 估算: A ≈ 99K 字 + B ≈ 60-80K 字 (标题 37K + 选择肢) ≈ 160-180K 字. **日文 token 密度接近 1 字 ≈ 1 token**, 所以这可能逼近 200K token —— 仓库里目前没有任何输入 token 计量, `SelectableModel` 也无上下文窗口字段.
- **Task 0 硬前置 (实现前)**: 用 litellm `token_counter` 对四个可选模型逐个量研读包 token 数, 写进 plan; 若 Claude 档 > 150K token, 先收 B 部 (去选择肢, 只留标题行 + 型) 再收白名单, 由用户点; 不在代码里静默截.
- 上限 `dossier_max_chars` (默认 200K 字) 超限启动即报错, 绝不静默截断. 徽章里报字数与 token 数 (启动时量一次).
- 每题输入 ≈ 研读包 + CDISC 8 chunk (≤ 4000 字/chunk) + system. 选了装不下的模型时由 LLM 侧报错 → SSE error 事件原样透传, 不降级不截包.

## 4. 触发规则 (`decide_dossier`, 纯函数, 可枚举可测)

```
输入: question, mode ∈ {auto,on,off}, enabled(总闸)
enabled=False           → attach=False, reason="disabled"       (无论 mode)
mode=off                → attach=False, reason="forced_off"
mode=on                 → attach=True,  reason="forced_on"
mode=auto:
  domains = StructuredLookup._query_domains(question)   # D1 口径, 含小写/中日文锚定
  scope   = 问句含研究范围词 (本研究|本試験|当試験|当研究|この試験|この研究|\bour study\b|\bthis study\b|\bour trial\b|\bthis trial\b|\bin (our|this) (study|trial|research)\b)
            # fix round 1: 裸 "EDC" / 裸代词 "in our" 已剔除 (纯 CDISC 定义题误触发); EDC 需搭配 study/trial/研究 锚定才算范围词
            # fix round 2 (DM2 T8 attempt 1): 英文分支加 \b 词边界, 否则 "f<our Trial>" 跨词边误触发; CJK 分支不加 \b
  domains 非空 且 scope → attach=True,  reason="auto:domain+scope"
  否则               → attach=False, reason="auto:no_match"
```

- 范围词表是**词类**不是 example (与 C2R 触发器同一纪律): 「研究所指代词 + study/試験/研究」; 不加任何表单名或项目名.
- 纯 CDISC 题 (「DS 域有哪些变量」无范围词) 不触发 → 140q 集 0 触发, 逐字节不变.
- study v2 48q 里若有题被 auto 触发 (含域码 + 范围词), 该题走研读包路径; 检索闸对这类题的判据改为「gold 卡 basename 出现在研读包文本中」(必然 100%, 因为一览全含) —— 这不是作弊, 是该模式的定义; 真实判据在答题层 (§7).

## 5. 数据流 (ask_stream)

```
retrieve(question, corpus=body.corpus)  →  chunks, routed
decision = decide_dossier(question, body.dossier, s.dossier_enabled)
if decision.attach:
    if routed == "study": 重跑 cdisc.retrieve(k_each) 取 CDISC 侧 (需要 D2 定义段); routed = "both"
    chunks = [c for c in chunks if c.corpus == "cdisc"]        # study top-k 丢弃
    context = format_context(chunks) + "\n\n" + dossier.text  # 研读包块在 CDISC 块之后
    system  += _DOSSIER_RULES
sources 事件: {..., "dossier": None | {"attached": bool, "reason": str, "sha": str, "sections": [...], "chars": int, "tokens": int}}
#   None = 总闸 OFF 通道没跑 (与 pdf_trigger None/[] 的区分同一教训); attached=False 带 reason = 跑了没挂
存档 (flag / 历史): 同一 dossier 字段, 与 web_status / fell_back / pdf_trigger 并列
```

- `_DOSSIER_RULES` (system 追加, 仅触发时): 「上下文含本研究 PRT 第 4-12 章原文与 EDC 全项目一览. 域级映射题: ① 沿域自身的类别变量 `--CAT` 的 CT 逐类穷举 (【標準 CDISC】块在时按块里的列; 块不在时明说并标 (推測)), **每个类别值各起一个小标题**, 按标准顺序, **在看任何 EDC 项目之前**; 不许用子类别 `--SCAT` / epoch / 时点轴顶替类别轴; ② 每个类别小标题下**要么**逐表单在一览里找候选项目 (状态 / 日期 / 理由) 并原样引用 `[フォーム OID] 項目 (OID)`, **要么**明写「候補なし / no candidate item in the EDC」—— 任何类别不得静默跳过; ③ PRT 里定义了该事件 (完了の定義 / 中止規準 / 登録手順 等) 时引用章号; ④ **每一条** EDC→SDTM 归属行内带 (推測), 不能只在开头做一次全局声明.」T7 联邦规则句保留 (它管无研读包时的行为).
  - ①/② 的当前形态来自 T9 attempt 1 的失败 (4/6, `evidence/failures/dm2_task9_attempt_1.md`): 原 ① 没说沿哪条轴, 模型用 `--SCAT` 子类别 / 阶段轴凑够条数而漏掉一个真实类别; 原 ⑤「明说哪类没候选」挂在 ① 的产物上, ① 漏了 ⑤ 就跟着哑 —— 故并入 ②, 让"漏"变成看得见的空标题. 修法停在模式级 (轴名, 不写某域有几类): 凡分类轴不止一条的域都会复发.
- 研读包块**不进** `sources` 列表 (它不是 chunk), 只进徽章; 引用可追溯性靠模型引用章号 / OID, 由 §7 判据核.
- Prompt cache: 研读包块作为 messages 里独立的 system/user 段, 对 Bedrock Claude 模型加 `cache_control: {"type":"ephemeral"}` (litellm 透传). 非 Claude 模型忽略该标记. **这是优化不是正确性前提**: 加不上也照常工作, 只是每题全价.
- `ask` (非流式) 同样接线, 走同一 `decide_dossier` + 同一拼装 helper `maybe_attach_dossier(request, question, chunks, routed, context)`, 避免两处漂移 (C2R 教训: `maybe_attach_pdf_pages` 是共用 helper). 研读包块**不经过** `RAGEngine.format_context` 的 4000 字/chunk 截断 —— 它是独立文本段, 不是 chunk.
- 与 C2R PDF 通道共存: 两者可同时触发 (PDF 页挂在 user 消息末尾的 parts, 研读包在 context 文本里), 互不知道对方; 默认 PDF 通道 OFF, 不在本单元验证共存.

## 6. 错误处理

- 研读包构建失败 (目录缺 / 章节 0 / 超 `dossier_max_chars`) → **启动 fail-loud** (与 pdf_page_index 缺失同处理), 不是运行时静默 OFF. 总闸 OFF 时不构建.
- 触发但 CDISC 侧检索异常 → 502 (沿用现有 `stream_retrieve_failed`).
- LLM 侧上下文溢出 → SSE `error` 事件原样透传, 徽章仍显示「研读包已挂」让用户知道是包太大不是模型没看到.
- `dossier` 字段非法值 → pydantic 422.

## 7. 验证

**L1 结构 (pytest)**
- `scripts/tests/test_dossier_trigger.py`: 判定表 ≥ 12 例: 三语言域码 (大小写 / 长名) × 有无范围词; 纯 CDISC 题; `on`/`off` 覆盖; 总闸 OFF 压过 `on`.
- `scripts/tests/test_study_dossier.py`: 用 tmp 目录造 3 章 + 4 卡, 断言文本逐字节 (章序 / part 拼接 / 一览行格式 / 选择肢); sha 稳定; 超限抛错; 白名单外章不进.
- `scripts/tests/test_router_dossier_wiring.py`: 触发时 study chunks 不在 sources、routed=both、context 含包头、system 含规则句; 不触发时 messages 与主线逐字节相同 (fidelity); 请求缺 `dossier` 键 = auto.
- `eval/prod_wirein/check_code_grounding.py` `retrieval_levers` 加 `dossier` 实收值 (缺键 = OFF 读回), 与 D1-D5 同模板.

**L2 检索闸 (零 LLM)**
- 140q: `decide_dossier` 触发数 = 0, `dm1_cdisc_after.json` 逐题 IDENTICAL. 48q: 记触发题数; 未触发题逐题 IDENTICAL.
- 映射 8q: 触发 8/8; 一览含 gold 卡 32/32 (定义性检查, 只证接线).

**L3 语义 (规则 A, 异 agent 判, 判据先登记)**
- 原句 + dm02 + dm05 (三域: DS / DS 日文 / AE) × 2 模型 (Opus 5, Sonnet 5) 走 `/api/ask_stream`, N=6.
- 判据 (每题 PASS 需三条全过): ① 定义齐: 按域定义列出全部记录类别; ② 候选齐: gold 4 卡中 ≥ 3 张被点名 (表单+项目 OID 原样), 且额外点名的候选**在一览中真实存在** (零捏造 OID, 用 `check_code_grounding` 码闸核); ③ 标推测: 每条归属带 推測/inference 标记, 并明说无候选的类别.
- 目标 ≥ 5/6 PASS; 失败归档 `evidence/failures/dm2_*.md`. 证据 `sdtm-rag/evidence/checkpoints/dm2_dossier_e2e.md`.
- 需用户 kickstart 生产 (prod 读主工作树).

**成本记录**: 每题记 input tokens (litellm usage) 与 cache 命中, 写进 e2e 证据; 这是「整本喂」的代价面, 必须留数字.

## 8. 不做 / 已知限制

- 研读包对所有触发题是同一份 (无按域裁剪): 用户裁定的代价换确定性. 若将来要裁剪, 那是「域→章节」表 = 新单元.
- 研读包只含 st01 的 docs/ + cards/; PRT 第 2-3 / 13-22 章 (背景 / 倫理 / 組織) 与前付不进. 问「研究代表医師是谁」不该由本通道答 (也不会触发: 无域码).
- 一览不含表示条件 / 非表示アクティビティ; 「某项目在哪个 visit 出现」仍属 C2R 通道.
- 非 Claude 模型无 prompt cache, 每题约 200K 输入 token 全价.
- 48q 集里被触发的题改走研读包, 其检索闸判据变为定义性 100%; 这类题的真实质量只在 L3 可见.
