# DM2 研读包答案 生成后确定性闸 (design, 2026-09-25)

> 起因: DM2 attempt 5/6 opus 主口径均 5/6, 失败落在不同低频模式 (示例值自造 OID / 语言漂移) —— 规则句措辞边际收益≈0
> (`sdtm-rag/evidence/checkpoints/dm2_dossier_e2e.md` §2.5/§2.6)。用户裁定 (2026-09-25): 做生成后确定性检查。

## §1 范围
- **只在研读包挂上时**运行 (B 部是穷尽一览, 「不在一览 = 不存在」只在此时成立; 不挂时行为逐字节不变)。
- 两端点共用一个纯函数 + 一个编排函数; 禁止两处各写一份。

## §2 闸定义 (纯函数 `server/dossier_gate.py::check_answer`)
输入: 答案全文、问句、`OidIndex` (启动时从 `catalog.json` 构建: 表单 OID 集 + 项目 OID 集)。输出 `GateResult`:
`{ok, unknown_oids: [...], lang_expected, lang_observed, reasons: [...]}`。

- **G-OID (窄提取)**: 只看规则句强制的引用形态 —— 反引号内、`[...]` 内、紧随 `]` 或项目文本的 `(...)` 内, 形如 `[A-Z][A-Z0-9_]{1,}` 的 token。
  - 在 表单∪项目 OID 集中 → 过。
  - 不在集中, 但属于**白名单**之一 → 不计: SDTM 变量名 / 域码 (从 `knowledge_base/domains/*/spec.md` 的 `### VAR` 标题与目录名构建)、NCI C 码、`CT`/`OID`/`EDC`/`PRT` 等缩写、占位写法 (含 `_n` / `nn` / `〜` 未给端点)、族前缀 (一览中有以其为前缀的成员)、区间简写端点 (两端均存在)。
  - 其余 → `unknown_oids`。
- **G-LANG**: `lang_expected = answer_language(question)` (已有)。`lang_observed`: 去掉反引号 / `[...]` / `[Source: …]` / 固定标记后计数 —— 平仮名 ≥ **100** ⇒ ja; 否则 漢字数 > 拉丁词数 ⇒ zh; 否则 en。阈值由 §4 回放校准, 校准后写死。
- `ok = not unknown_oids and lang_observed == lang_expected`。

## §3 不过时的行为 (流式约束决定)
`/api/ask_stream` 在判定前已把答案流给用户, 故**不做「顶部警示」**, 改为:
1. 首轮流完 → 跑闸 → 发 SSE `grounding` 事件 (GateResult)。
2. 不过且重答预算 > 0 (**上限 1 次**): 发 SSE `regenerate` 事件 (含原因), 前端插可见分隔线「首次答案未过确定性核验: <原因>, 重答中」, 然后流第二轮。
   第二轮 = 原 messages + 首轮答案 (assistant) + 一条 user 反馈: 列出**本次运行时**查到的不存在 OID 与应答语言, 要求完整重答。反馈内容是运行时数据, 非预置 example。
3. 第二轮流完再跑闸, `done` 带 `grounding: {final: GateResult, first: GateResult|None, regenerated: bool}`。第二轮仍不过 → 不再重试, `final.ok=false` 如实呈现 (徽章琥珀色)。
- `/api/ask` (Streamlit): 同一编排, 只返回最终轮答案 + `grounding` 字段。
- webchat: `grounding` 徽章 (过 / 重答后过 / 未过 + 原因); `flag.js` 存档行带 `grounding`。
- 续写 (auto-continue) 与联网工具轮: 闸在**整轮答案拼好之后**跑, 不在分片上跑。
- **重答失败 / 中断的口径 (实现后补, 2026-09-25 复审)**: 重答轮任何失败 (开流 / 流中途 / 工具轮; `/api/ask` 另有墙钟不足 `budget`) 或用户在重答中停止 / 断流时, 半截重答不作数, 答案**还原为未过闸的首轮**, `grounding = {final: 首轮判定, first: null, regenerated: false, regenerate_error: <异常类名 | "budget" | "interrupted">}`, 徽章琥珀色 (「重答失败 / 时间不足 / 重答中断」)。这份首轮**会进入后续对话的 history** —— 它是唯一可用的答案, 属**有意为之**; 警示随徽章与存档一起留下。中断情形由前端以最后一份 `grounding` 事件合成同形状 payload (形状由测试与后端 `GateRun.payload()` 对钉)。重答成功时首轮另存 `firstAnswer` (折叠展示), **不**进 history。

## §4 离线回放校准 (零 LLM, 实跑前必过)
回放对象: gitignored `runs/dm2_e2e_{claude,attempt4,attempt5,attempt6}/judge_pack.json` 共 42 份已独立判分答案。
**预期 (以判分方逐 run 结论为真值)**:
- G-OID 必须恰好标出: attempt 3 opus dm07 (1 个项目 OID)、attempt 3 sonnet dm07 (3 个表单 OID)、attempt 5 opus dm09 (1 个示例 OID); attempt 4 / attempt 6 共 18 份零标记。
- G-LANG 必须恰好标出: attempt 3 opus dm01 (zh→ja)、attempt 3 sonnet dm05 (en→ja)、attempt 4 sonnet dm05 (en→ja)、attempt 6 opus dm10 (zh→ja); attempt 5 12 份零标记。
- 其余份数零标记 (假阳性 = 0)。回放不达预期 ⇒ 先修闸, 不进实跑。

## §5 成本与预期收益 (预登记, 防过度宣称)
- 重答 = 再一次 ~150K prompt 全价调用 (无 cache; T11 价值因此上升, 本单元不做)。
- 若两个独立低频模式各 ≈1/6, 一次重答把残差约平方化 (≈1/36 量级), **不是**消除; 闸看不见的失败 (precision / 分类轴 / ⑤) 不受影响。

## §6 不做
- 不改 `_DOSSIER_RULES`; 不改触发器; 不恢复 auto (恢复与否待本单元实测后由用户裁定)。

## §7 已知限制 (实现后补)
- 老存档 (本闸上线前后的首版 webchat) 里「首轮 + 分隔线 + 重答」拼在同一条 content 的消息会原样进 history, 不做迁移。
- 闸假设 item OID 在全研究内唯一 (一览按 OID 集合比对)。换研究时若有跨表单复用, 启动一致性检查 (items 数 ≠ 研读包条数) 会关闭闸, `/api/info` 的 `dossier_gate=false` 可见 —— 换研究的 runbook 须检查这一项。
- `/api/ask` 重答轮在 completion 之外仍有 502 路径: provider 返回结构异常 (如 `choices[0]` 缺失) 时走外层 502, 不还原首轮。
- 引用 span 里**选中槽之后**的括号只计「像 OID」的 (与一览某 OID 共享 ≥3 字符前缀, 或带数字/下划线): 新词干的纯字母捏造 (如与一览无共同前缀的 `ZQWEIGHT` 型) 出现在槽后会漏报; 换来槽后散文里 `(UNK)`/`(TBD)`/`(BID)` 等不误报 (复审第三轮裁定)。
- `ask_stream` 重答失败还原首轮时只还原 `model_used`; `models_used` 保留两轮累计, 重答轮的回退仍经 `fell_back` 可见。
- 漏报形态 (M3 纯字母近似单独 token / M5 表格单元格 / M6 粗体 / M10 表单 OID 加后缀)、词干规则对命名习惯敏感、G-LANG 把繁体中文判成 ja: 见 `server/dossier_gate.py` 模块 docstring。
