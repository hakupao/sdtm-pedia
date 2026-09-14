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

## 7. N2 单元: 画面出处接地闸 (来源标签捏造, 登记于实现前, 2026-09-11)

起源: V3 §4 第 3 条 + N1 判分 2.2 #4 / 2.6 #11 — 三条同型: 底层事实为真 (来自 builder 写进 label 的元数据「同一画面: …」/ 块表), 但被挂上『画面目視判読 p.NN』, 页面上并无此注记。页号越界闸与 N1 作用域规则都不覆盖。

**闸 (零 LLM, eval 侧, 不改服务)**: `scripts/study/c2r_eval/check_visual_grounding.py <runs_dir>...`
- 主张单元 = 含 `画面目[視视]判[読读] … p.N` 的句/条目 (按换行与「。」切); 页归属: 出处内 pdf 名, 缺省时按 `pdf_pages` 附页唯一匹配, 否则 AMBIGUOUS。
- 实体 = 页索引里的 activity OID (token 边界) / form OID / 活动短名 (≥3 字, 去空白子串)。
- 判定: 句中实体全在该页文本层 → PAGE_GROUNDED; 有实体不在页上但在该页 label 元数据 (同 form 同 hidden_items 的折叠块集合, 由索引复算) → **LABEL_ATTRIBUTED**; 不在页上也不在元数据 → OFF_PAGE; 引用页不在附页集 → OUT_OF_RANGE。
- 输出: 脱敏计数表 (默认不打印 OID/名) + `runs/<dir>/visual_grounding.json` (gitignored, 含实体明细)。

**预登记验证** (V3 B 臂 12 份 + N1 6 份 = 18 份, 真值 = 两轮 judge 的逐条 census): 已知 3 条 LABEL 型捏造召回 **3/3**; 假阳性 (被闸标 LABEL/OFF_PAGE 但 judge 判 verified) **≤ 5**; 结果 `evidence/checkpoints/c2r_n2_visual_grounding.md`。不达 = failures/ 归档, 不放宽判据。

**不做 (归下一单元 N3, 与 3b 面板分组合并一轮复测)**: label 元数据改标『頁索引』出处 + `_PDF_SOURCE_RULE` 第 3 条「label のメタ情報は画像由来ではない」。原因: 改 prompt 须重跑模型, 与 T6 面板分组的 label 改动合并省一轮。

## 8. N3 单元: annotated label 附项目组序列 + label 元数据出处分离 (登记于实现前, 2026-09-11)

起源: (a) V3 §4 第 5 条 + N1 2.5 #8 / 2.6 #7 / #9 — 两模型都把无标题面板并入前一个有题面板 (或把首项目标签当组名), 而该边界与 catalog 项目组边界逐字重合; (b) N2 起源的三条「label 元数据被当画面注记」。两者都改 label/prompt, 合并一轮复测。

**改法 (label + prompt, 检索/选页/触发零改动)**:
- `_ann_label(form_oid, page)`: 由 catalog (`group_oid`/`group_name`, 按 `row` 序) × 页索引 `item_pages` 算出**本页**出现的项目组序列, 追加 `（本頁の項目グループ順: 名A [n 項目] › (無題) [m 項目] › …）`; 无名组写「(無題)」。数据源: 服务启动时已加载的 catalog (若 builder 无 catalog 句柄, 由页索引构建脚本预计算进 `annotated.page_groups`, 索引 schema 加字段, 旧索引缺字段则不加注)。
- label 元数据 (块范围 / 同一画面 / 本頁の項目グループ) 集中到 label 尾部一段, 前缀「頁索引メタ:」; `_PDF_SOURCE_RULE` 第 3 条: 「頁索引メタ」の内容は画像から読み取った事実ではない。引用時は『頁索引』を出典とし『画面目視判読』にしない。
- 测试: 多组页 label 含组序列且无名组写 (無題); 单组页/无 item 页不加; 元数据前缀; prompt 第 3 条; `画面目視判読` 计数仍 1。

**复测 (B 臂, T1/T3/T6, gpt-terra/gpt-sol; opus-5 待供给)**: 判据 ① T6 ② (布局与组一致) 两模型 ≥ V3/N1 (gpt-terra 0 → 目标 1); ② N2 闸 LABEL_ATTRIBUTED = 0 (两模型三题; 闸实体集已并入 annotated 页组名, 续页组的见出し不在本页 ⇒ 引用即标红, 故对 (a) 有判别力); ③ T1/T3 逐点不低于 N1; ④ 规则 A 全量主张核验同型 contradicted (面板合并 / 元数据挂画面) 各 = 0。不达 = failures/ 归档。

**attempt 1 结果 (2026-09-11)**: gpt-terra ①②③④ 全 PASS (9→10); gpt-sol ③④ FAIL ⇒ 归档 `evidence/failures/c2r_n3_attempt_1.md`, 判据不改。
**attempt 2 前置 (登记)**: ① 先修页索引短 OID 撞页缺陷 (确定性, 不改 prompt); ② 同一 prompt 重跑两模型 T1/T3/T6 (n=2) 分辨 gpt-sol ③ 是否噪声; ③ 仅当 ④「无视 label 组序列」在 n=2 复现, 才允许 prompt 层改动, 且须按 pattern 登记; ④ opus-5 补跑仍是默认 ON 硬前置。
**attempt 2 结果**: 两模型 10/12; gpt-sol 全 PASS; gpt-terra ② 字面 FAIL (闸 1 = 假阳性) + ④ FAIL (对冲跨页推测 1) ⇒ 归档 `evidence/failures/c2r_n3_attempt_2.md`。「无视 label 组序列」未复现 ⇒ **prompt 不改**。N3 工程件保留 (靶向错误已修好), 单元以「预登记 FAIL / 实质改善」收口。

## 9. N4 单元: 沉默维度显式化 (登记于实现前, 2026-09-14; brainstorm 经用户批准)

PATTERN (来自 N3 a2 归档): 页级元数据在某维度沉默 (单组页不写组序列; 无「前頁からの続き」≠ 明示「本頁で開始」) 时, 模型用视觉推测填补并在跨页方向给出无证据续接。反证据: 写了组序列的页两模型两轮零错; 没写的 ann p.161 三轮两错分属两模型。p.161 真值: 单组无题枠 16 項目, 不续自 p.160, **续到 p.162** (索引已知, label 沉默)。85 个 annotated 页中 46 页单组页同样沉默。前置: T1 元数据引用率已 n=2 坐实为 0 (不再是前置); opus-5 补跑按用户 2026-09-14 指示跳过 (仍是默认 ON 硬前置)。

**改法 (索引 + label + prompt, 检索/选页/触发/SSE 零改动)**:
- `build_pdf_page_index.py` `page_groups_by_form`: 每组新增 `continues` (该组项目在同 form **更后**页也有定位 = 枠在本頁で閉じない), 与 `continued` 对称; 重生成真索引 (仅新增字段)。
- `_ann_label`: 每个 annotated 页**都**写连续状态, 不再对单组页沉默。单组页: `本頁の枠: 1 (名 or (無題) [n 項目]；前頁からの続き: なし/あり；次頁へ続く: なし/あり)`; 多组页: 现有序列不变, 每组后缀补 `・次頁へ続く`。只声明状态不写顺序 (单组页无顺序信息, 避免狼少年)。旧索引缺 `continues` → 不写「次頁へ続く」维度 (静默降级, 启动提示)。
- `_PDF_SOURCE_RULE`: 頁索引メタが前頁/次頁との連続状態を宣言している枠について、画面判読はそれと矛盾する・それを超える続き推測をしない; 「前頁からの続き: なし」= 見出しは本頁に描画, 「次頁へ続く: あり」= 枠は本頁で閉じない。画面由来出典名出现次数仍钉在 1。
- 测试: 索引 `continues` 判别性 (首页/中页/末页三态); 单组页 label 含状态段; 多组页每组含次頁标记; 缺字段降级; 规则句 wiring。

**复测 (B 臂, T1/T3/T6, gpt-terra/gpt-sol; opus-5 跳过)**, 判据:
① 跨页续接型 (label 已声明状态而画面推测与之矛盾/超出) contradicted = 0 (两模型三题, 规则 A 全量主张核验);
② N2 闸 LABEL_ATTRIBUTED 核验后 = 0 (字面计数照报, 不得省略);
③ T1/T3/T6 逐点 ≥ N3 a2 (gpt-terra 10, gpt-sol 10);
④ 新增状态文本被引用时出典 = 『頁索引』, 挂画面出典 = 0。
不达 = failures/ 归档, 判据不改。n=1 不足以下 prompt 层结论时按 N3 attempt 2 规则处理。

**attempt 1 结果 (2026-09-14)**: 两模型四判据全 PASS (N 系列首次; ② 字面闸 1 = 假阳性照报); 靶心页两模型显式引用状态文本且方向正确; 64 条主张 0 contradicted。**新暴露**: gpt-terra T1 卡片层捏造 + 假出处 (三道闸均不覆盖)。收口 `evidence/checkpoints/c2r_n4_silent_dimensions.md` + `evidence/step_c2r_n4_audit.md`。opus-5 补跑仍是默认 ON 硬前置。

## 10. N5 单元: 卡片层接地闸 + census 扩围 + prompt 规则 (登记于实现前, 2026-09-14; brainstorm 经用户批准, 范围「测量 + prompt 一起做」为用户选择)

PATTERN (来自 N4 judge §7): 挂 study `[Source: …]` 出典 (EDC 項目カード / 手順書章節) 的句子所列 OID 不在被引文件里 (n=1: gpt-terra T1 一条活动 OID 被列为某卡片的非表示活动, 与真值方向相反; **勘误 2026-09-14**: 该 OID 在同 run 检索到的兄弟卡片非表示列表里, N4 审计「16 源 0 次」是 preview 300 字 grep 的误判 ⇒ 形态 = 移植 + 挂真出典, 对应闸的 CONTEXT_MISCITED 类)。画面层三单元把『画面目視判読』『頁索引』各钉了闸, study 出典无任何机器闸 ⇒ 错误挪层。修法是**全部 study 出典句**的通用接地, 不限「非表示アクティビティ」一种。

**三层防御 (各自独立)**:
1. **零 LLM 闸** `scripts/study/c2r_eval/check_card_grounding.py <runs_dir>...` (eval 侧, 不改服务): 主张单元 = 以 study `[Source: st01__…]` 结尾的句/条目 (切分规则与 N2 共用: 前一出典之后起, 出典行无中身时向上吞整块列表); 实体 = catalog 的 activity / form / event / item / item-group OID (token 边界; **≤2 字 OID 不查**, 计数报; **不查日语名** — 名字合法来源是対応表非卡片); 出典标记本身内的 OID 不算实体。判定: `SOURCE_GROUNDED` (在任一被引文件文本) / `CONTEXT_MISCITED` (不在被引文件但在本 run 检索到的其他 study 源 = 挂错出典) / `UNGROUNDED` (检索源里都没有 = 捏造候选) / `BAD_SOURCE` (被引路径磁盘不存在 = 出典本身捏造); 无实体单元记 `NO_ENTITY` 不标红。被引文件文本从磁盘 `data/study/st01/{cards,docs}` 复算, 检索源集合取 run json `response.sources` (corpus=study)。文书节按整节文件 (超集, 宽松方向)。盲点写明: 不看极性; 单元只向前伸到出典; 不识别 catalog 外的 OID 形字符串。输出脱敏表 + `runs/<dir>/card_grounding.json`。
2. **census 扩围** (judge 侧): 规则 A 范围从「归因画面/頁索引的主张」扩到「归因 study 出典的 OID 级主张」(每条: 该 OID 是否在被引文件; 所述关系 (显示/非表示/所属组等) 是否与文件一致)。
3. **prompt 规则** (答题侧, pattern 级, 只进 `_STUDY_OID_RULES` = study 引擎; CDISC 侧 prompt 逐字节不变): 挂カード / 文書節出典的记述所列 OID 限于该文本实际写有的; 列举类字段 (非表示アクティビティ等) 只照抄本文列举, 不补不推 (与 rule 7「只能抄那一行」同族); 要提文脈里没有的 OID 就写明不在文脈, 不挂出典。wiring 测试: 规则只出现一次; CDISC/study 差异仍只有该块。

**预登记判据**:
- 闸回扫 (零 LLM, 验证集 = 全部 c2r run 文件: v3 A+B+N 臂 + n1 + n3 + n3_a2 + n4; 真值 = 各轮 judge census + 本轮 judge 对标红条目逐条核): 已知真阳性 1 条 (n4 gpt-terra T1) 召回 **1/1**; 被闸标 UNGROUNDED / MISCITED / BAD_SOURCE 而核验为真的假阳性 **≤ 5**, **上限钉在本验证集上, 不做跨轮累计预算** (a2 教训); 标红条目全部列出供 judge 核。
- 模型复测 (B 臂 T1/T3/T6 × gpt-terra/gpt-sol, 与 N4 同口径, 独立 judge): ① 卡片层 UNGROUNDED 核验后 = 0 (字面计数照报); ①′ (2026-09-14 复审 MAJOR-1 事实性补记, 登记于复测前) n4 型「兄弟卡片移植」CONTEXT_MISCITED 核验后 = 0 —— 已知真阳性的类是 MISCITED, 只有 ① 对它无判别力; ② T1/T3/T6 逐点 ≥ N4 (terra 10 / sol 10); ③ N4 判据 ①④ 不退 (跨页续接 0; 状态文本出典『頁索引』); ④ N2 闸不新增标红。
- 零回归: prompt 动 study 引擎全局 ⇒ study golden v2 48 题 (gpt-terra) 与基线 Δ0, 或逐题列差异并归档。
不达 = failures/ 归档, 判据不改。opus-5 仍挂起 (默认 ON 硬前置)。

**不做**: 服务端答案过滤/剥离 (第三方案); 检索/选页/触发; 日语名实体 (用户选「只查 OID」)。

**闸回扫 attempt 1 结果 (2026-09-14)**: 召回 PASS (1/1 + 预登记外新真阳性 1: 被引卡属性推广到另两个项目组); 假阳性字面 **7 > 5 FAIL** (CITATION_ERROR 3 + 纯 FP 4); 归档 `evidence/failures/c2r_n5_gate_attempt_1.md`, 判分 `evidence/step_c2r_n5_scan_audit.md`。**用户裁定 (2026-09-14)**: CITATION_ERROR 计入假阳性, 维持 FAIL, 走 attempt 2。
**attempt 2 登记 (实现前)**: 只加一条 pattern 规则 —— **画面描述句不归卡片出典单元**: 单元内以画面指称开头 (画面では / 画面上 / 画面には / 添付頁 / 頁画像 / p.NN の画面 等) 且自身不带任何出典标记的句子, 是画面主张 (N2 的地盘), 其 OID 不计入卡片出典的实体集 (计数报为 `screen_sentences`)。理由: 出典是后置归属, 但画面句的归属是「画面」而非其后的卡片; 4 条纯 FP 中 2 条是这一机械形。**不改**其它规则, 不改判据; 复扫后 judge 只核 delta (预期: 标红 9 → 7, 假阳性 5 ≤ 5); 若不达, 闸以 FAIL 收口保留信号层。
**attempt 2 结果 (2026-09-14)**: 标红 9 → 7 (消失恰为 attempt 1 两条纯 FP, 新增 0), 假阳性字面 **5 ≤ 5 PASS (压线)**; screen_dropped = 2 (验收面 example 级, 通用性为机制论证); judge 全核 SIBLING_NAMED 16 条抓到 1 漏检 ⇒ 真实召回 2/3。
**模型复测结果 (2026-09-14, c2r_n5)**: ①/①′/②/③ 两模型全 PASS (terra 10 / sol 11); ④ 字面 FAIL 2→3 (核验后真错 0, 其中 1 条是闸惩罚正确引用元数据); 卡片出典 31 条 31/31 接地; **副作用: T1 CDISC 出典 2→0 ⇒ N6 候选**。两处口径敏感性 (T1 ⑤ / ④ 字面) 由 PLAN 所有者裁。收口 `evidence/checkpoints/c2r_n5_card_grounding.md` + `evidence/step_c2r_n5_{scan,retest}_audit.md`。

