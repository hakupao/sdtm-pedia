# PLAN — C2R: 表单 PDF 按需旁路 (画面判读通道) + 活動 OID 日语 label 补齐

> 状态: **进行中** (2026-09-09 开工) · Tier 2 · 进度 `_progress_c2r.json`
> 起源: dogfood 2026-09-09 10:49 (LB Form 身高体重题) 用户反馈 ①OID 旁缺官方日语 label ②卡片层答不全显示/时点类问题
> 前置判定: C2 两份 PDF (`ENSEMBLE 59.0 workflow.pdf` 933p / `ENSEMBLE_59.0_Annotated.pdf` 212p) **维持 DROP 不 chunk** (`evidence/checkpoints/c2_pre_survey.md` §8)。本单元不改这个判定: 不入向量库, 只做按需旁路。

## 0. 设计要点 (与用户 2026-09-09 对齐)

1. 钥匙不是问题原文, 是**已命中卡片的 OID → catalog 日语名 → PDF 页**。勘察实测 (S0-0): PDF 文本层 OID 几乎搜不到 (Annotated: 体重STAT项 1 / 术前LB活动 0 / LBG4 0; workflow 全 0), 日语活动名可命中 (术前LB活动名 4 / C1-Day8活动名 8)。
2. 触发依据是**命中结果的形状** (跨 ≥2 活动 / 显示条件·时点·visit 类属性), 不是让路由模型读题。路由模型只做末道确认。
3. 两份 PDF 分工: Annotated 按 form 定位 (字段在画面上的样子/并列关系); workflow 按 activity/event 定位 (活动实际显示项目与条件)。
4. 抽出页**渲染成图** (`pdftoppm`) 走多模态, 不抽文本 (短行占比 80% 是文本层不适合的证据)。答案来源三分: 卡片事实 / 标准引用 / 画面目视判读 p.NN。
5. 附加通道, 不替代现有检索; 默认关, 开关打开; 48 题 study golden v2 零回归为硬闸。

## 1. 步骤与闸

| Step | 内容 | 产物 | 闸 |
|---|---|---|---|
| L1 | **活動 OID 日语 label 补齐** (独立小单元, 先做) — 答题时确定性附「活動 OID 対応表」, **不改卡片文本** (卡片共享文本已实证致挤占回归, 见 `evidence/failures/t4_step7_retrieval_regression.md`) | `server/rag.py` 或 federation 的 context 拼装 + 测试 | pytest 绿; 检索层零改动 (无需 golden 重跑, 但跑一次做证据) |
| S0-1 | 两份 PDF 逐页 `pdftotext`, 建 `名称 → 页` 索引; 覆盖率: 77 activity / forms / 961 item label 各多少能定位 | `data/study/st01/pdf_page_index.json` + `evidence/checkpoints/c2r_s0_survey.md` | — |
| S0-2 | 每页 Form/Activity 标识可识别性; 规则 A: N=12 页人眼核对 | 同上 §2 | — |
| S0-3 | Bedrock `selectable_models` 图像输入实测 (一页 pdftoppm 图), 记 token 成本 | 同上 §3 | **G0**: 定位率 ≥80% 且 ≥2 模型支持图像; 否则改形并归档 failures/ |
| P1 | 预登记判据: LB 题 + 5-8 真实「卡片答不全」题, 期待答案+判分点; 触发规则初版 + 不触发反例集 | `evidence/checkpoints/c2r_pre_registration.md` | 判据先于实现 |
| I2-1 | `scripts/study/build_pdf_page_index.py` 确定性页索引进仓库 | 脚本 + 测试 | — |
| I2-2 | `server/pdf_context.py`: OID 集合 → 页集合 → 图 → 多模态片段; 页数上限+token 预算, 超限降级为页号提示 | 模块 + 测试 | — |
| I2-3 | 路由接线: 纯函数判触发, 默认关, 开关 | 接线 + 测试 | **G2**: 48 题零回归 IDENTICAL; 反例集零误触 |
| I2-4 | 答案侧「画面目视判读 p.NN」来源标签 + citations.js 渲染 | 前端 | — |
| V3 | 预登记题 Writer 出答案 / Reviewer 异 subagent 独立判分 (规则 D); LB dogfood 回归 | `evidence/checkpoints/c2r_v3_eval.md` | 规则 A N 写死 |
| C4 | RETROSPECTIVE_c2r.md 三段; `_progress_c2r.json` 收口; CLAUDE.md Key Path 一行 | — | — |

## 2. 不做

- 不把任何 PDF 页入向量库 (C2 DROP 判定不变)
- 不改卡片文本 / 不重 ingest (L1 走答题时拼装)
- 不让 LLM 自主决定"搜什么词去 PDF" (钥匙来自 catalog)

## 3. G2 零回归复跑命令 (登记于实现前)

```bash
.venv/bin/python -m eval.run_eval data/study/st01/eval/test_set_study_v2.yml \
  --retrieval-only --hybrid --study-lookup \
  --collection study_st01 --kb-root data/study/st01/cards \
  --output data/study/st01/eval/runs/c2r_g2_after.json     # 基线 87.50%, 逐题须 IDENTICAL vs runs/v2_baseline_s2on.json
.venv/bin/python -m pytest -q
```

## 4. S0 后设计修订 (2026-09-09, G0 PASS, 详见 `evidence/checkpoints/c2r_s0_survey.md`)

- 页索引形态从「名称 → 页列表」改为**块表**: workflow 每块 = 一条 `(event, activity, form)` assignment 的页区间 (110 块, 断言 `块数 == len(assignments)`); Annotated 每块 = 一个 form 的页区间 (21) + code-list 块 (21)。
- 钥匙: Annotated 用 **item OID 直查** (941/959 可定位) + form 块; workflow 用 **(activity, form) 双键** (单键 activity 仅 76.6%, 不达线)。短 OID (PS / K / LB) 必须 token 边界 + 配 form_oid。
- 页预算: 上限 6-8 页/次, `pdftoppm -r 110`, 每页 ≈1.5k token; 超限降级为只给页号提示。
- I2-1 以 `scripts/study/survey_pdf_pages.py` 的切块逻辑为起点收敛成 `build_pdf_page_index.py`, 索引进 `data/study/st01/` (gitignore 内, 由脚本重生成)。

## 5. V3 评测设计 (登记于 I2 复审后, 2026-09-09)

- 运行形态: 本机另起服务 `SDTM_RAG_PDF_CONTEXT_ENABLED=true uvicorn server.main:app --port 8010` (auth 关), 走真实 `/api/ask` (非流式), 不绕过路由/检索/触发任何一环。
- 题集: P1 §1 T1-T6 (真值题面取 gitignored `data/study/st01/eval/c2r_pre_registration_realvalues.md`) + N1-N3, N5。
- 臂: A = flag OFF (同题同模型), B = flag ON。模型 ≥2 (opus-5 + 一个非 Anthropic 家的 selectable model)。T 组 6×2×2 = 24 次 LLM 调用; N 组只看 `pdf_trigger` 是否为 null, 每题 1 次。
- 记录: 每次调用存 `data/study/st01/eval/runs/c2r_v3/<arm>_<model>_<qid>.json` (含 `pdf_pages` / `pdf_trigger` / 全文答案); 掩码后的汇总进 `evidence/checkpoints/c2r_v3_eval.md`。
- 判分: Reviewer 为**非本 session 作者**的 subagent, 按 P1 §1 判分点逐条 0/1, 并对 A/B 两臂逐题打分; 规则 A: 12 份 B 臂答案全部人工级逐条核验, 结果 `evidence/step_c2r_v3_audit.md`。
- 通过判据 (预登记): B 臂 T 组判分总分 > A 臂; T1 ⑤ 三分来源标注与 T5 ③ 「不把项目级常時表示误读为活动级」在 B 臂 ≥ 1 个模型满分; N 组 4 题 `pdf_trigger` 全 null。不达 = 归档 failures/, 不改判分点。

## 6. N1 单元: 附页子集语义 (登记于实现前, 2026-09-11)

起源: V3 判分 (`evidence/step_c2r_v3_audit.md` §4 第 1/2 条; RETRO §2) — opus-5 在 T3/T6 把「附上的块首页没有 X」外推成「整个活动/表单没有 X」, 实测 X 在同块后续页。两条捏造页号都在附上的页内, 页号越界闸天然盲。

**改法 (只动 label + prompt, 不碰检索 / 选页 / 触发)**:
- `PdfContextBuilder._wf_label` / `_ann_label`: 块跨多页时 label 写明 `本頁は p.a–b ブロックのうち p.x` (块范围来自页索引 `blocks[].start/end`; 单页块不加)。
- `router._PDF_SOURCE_RULE` 追加一条 (复审 MAJOR-1 / MINOR-2 后口径): label 写了「p.a–b のうち p.x」的页只附了块的一部分; 添付頁に無い ≠ 画面に無い; **画面由来**的否定断言须限定「添付頁 p.x の範囲では」, 未添付頁不断定; **卡片事实 (非表示アクティビティ 等) 的否定不在此限** (否则误伤 T1④/T5③)。
- 前端 / SSE 契约 / `pdf_pages` 报告形状不变。G2 零回归无需重跑 (同 r3b 理由: 检索链逐字节不变; 以 `git diff --stat` 证明只动 `pdf_context.py` label 函数 + `router.py` 常量 + 测试)。

**测试 (先红后绿)**: label 含块范围 (多页块) / 不含 (单页块); annotated 同; prompt 规则加后 wiring 测试 `画面目視判読` 计数仍为 1; 规则文含「添付頁」限定语。

**复测 (V3 同题同 runner, 仅 B 臂, 判分点沿用 P1 §1)**:
- 题: T3 + T6 (出问题的两题) + T1 (回归哨兵, V3 B 臂两模型均满分/次满分)。
- 模型: Bedrock 账号自 2026-09-11 起拒绝所有 Anthropic 模型 (`Access to Anthropic models is not allowed for this account`, 复现命令见 `evidence/checkpoints/c2r_n1_subset_semantics.md`), 故本轮只能跑 gpt-terra + gpt-sol; **opus-5 复测挂起**, 账号恢复后补跑同一命令, 补跑前不得改判「默认 ON」。
- 规则 A: 复测答案的**全部**画面主张 (不抽样) 逐条对照真实页 (pdftotext 文本层 + 渲染页), 记 verified / contradicted / unverifiable。
- 通过判据 (预登记, 不改判分点): ① 「附页缺席 → 整块缺席」同型 contradicted = 0 (两模型); ② T3/T6 各判分点得分 ≥ V3 B 臂同模型得分; ③ T1 得分不低于 V3。不达 = 归档 `evidence/failures/c2r_n1_attempt_X.md`。
- 默认 ON 裁定: 需 ①②③ PASS **且** opus-5 补跑同样 PASS; 本轮只能得出「gpt 家 PASS/FAIL」, 默认 OFF 不动。

**命令** (runner 已从 scratchpad 迁入 `scripts/study/c2r_eval/`, 题面仍只读 gitignored `runs/c2r_v3/questions.json`):
```
cd sdtm-rag
nohup env SDTM_RAG_AUTH_ENABLED=false SDTM_RAG_PDF_CONTEXT_ENABLED=true \
  .venv/bin/uvicorn server.main:app --port 8011 > /tmp/armB_8011.log 2>&1 &
until curl -s -m 2 localhost:8011/api/health >/dev/null; do sleep 1; done
.venv/bin/python scripts/study/c2r_eval/run_v3.py --group T --arms B --models gpt-terra,gpt-sol --qids T1,T3,T6 --timeout 900 --out c2r_n1
```
