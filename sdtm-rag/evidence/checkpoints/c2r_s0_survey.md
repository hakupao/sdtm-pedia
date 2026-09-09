# C2R S0 勘察 — PDF 页索引可行性 / 页面可识别性 / Bedrock 多模态

> 单元: `PLAN_c2r_pdf_bypass.md` S0-1 / S0-2 / S0-3 · 闸 **G0**
> 日期: 2026-09-09 · 除 S0-3 外**零 LLM**, 全部确定性
> 结论: **G0 PASS** (三条判据全过, 其中一条子读数低于线, §5 明写)

## 0. 红线与真值伴生件

本文按红线 (`scripts/oidscan_evidence.py`, 策略见 `evidence/checkpoints/c1_redline_triage.md`)
**不写任何真实 item/activity/event OID 与 label/name**, 一律改成结构化描述 (下方 §0-1 词表)。
页码 / 计数 / 百分比 / 判定**原样保留**。

含真值的表 (逐实体命中列表、人眼核对的页面内容、四模型回答摘录) 逐字存于:

    data/study/st01/eval/c2r_s0_survey_realvalues.md      (落在 .gitignore:10 的 data/study/ 下, 不进 git)

### 0-1 结构化词表 (本文用词 → 指代对象)

| 本文用词 | 指代 |
|---|---|
| 短 OID (LB / DM / AE / QOL / NAC / OPE / TME / POC / OC / PF / RC / GN / RCT) | 表单 OID, 长度 ≤3, 低于红线闸 `DEFAULT_MIN_LEN=4`, 可直写 |
| 化放疗表单 / 分配因子表单 / 完遂中止表单 / 登录表单 / 四张后治疗表单 | 其余 8 张表单 (OID ≥4 字符, 不直写) |
| 体格测量项目组 | LB 表单下的那个身体测量 item group |
| 身高项 / 身高未实施项 / 体重项 / 体重未实施项 / PS 项 / 血检实施项 | 体格测量组及其下方的 6 个 item |
| 术前 LB 活动 | 手术事件下的那个术前临床检查活动 |
| 中止 PS 活动 | 完遂中止事件下的那个 PS 单项活动 |
| 第 1 周期 day8 LB 活动 | 化疗 A 臂下的那个 day8 临床检查活动 |
| 背景活动 / 再评价活动 / 术前 AE 活动 | 各自同名事件下的主活动 |
| 随访族 F1 / F2 / F3 | 三个随访事件族 (非手术转归 / 手术后 / 中止后) |
| 事件 E1…E14 · 活动 A1…A77 | 需要点名个体时的匿名编号 (对应关系只在伴生件里) |

## 1. 复跑

```bash
cd /Users/bojiangzhang/MyProject/sdtm-pedia/sdtm-rag
# S0-1 全量页索引 (1,145 页, ~20s)
uv run python scripts/study/survey_pdf_pages.py --out-dir /tmp/c2r_s0
# S0-3 四模型图像输入实测 (4 次调用, 一页图)
uv run python scripts/study/survey_pdf_pages.py probe --pdf workflow --page 315 --dpi 110 --out-dir /tmp/c2r_s0/probe
```

产物: `data/study/st01/pdf_page_index_survey_draft.json` (勘察草案, 1.16 MB) ·
`/tmp/c2r_s0/coverage_stats.json` · `/tmp/c2r_s0/probe/model_probe.json`。

⚠ **生产索引不是这个文件**。`data/study/st01/pdf_page_index.json` 是 I2-1 的生产件, 由
`uv run python scripts/study/build_pdf_page_index.py` 重建。本勘察脚本 2026-09-09 13:04 那次
重跑曾把生产索引覆盖成草案格式并在运行时打断生产加载器 —— 修法是脚本默认输出改名 (I2-pdf-bypass
改的 argparse 默认值与模块 docstring, 无逻辑改动), 且 `server/pdf_context.py::PdfPageIndex`
现在遇到 `meta.draft=true` 会带名报错而不是抛裸 `TypeError`。

抽取口径 (与 `scripts/study/pdf_text.py::extract_pages` 同一纪律, 逐页子进程):

```bash
pdftotext -layout -f N -l N <pdf> -
pdftotext -v      # poppler 版本
```

匹配口径两种并取并集: ①空白折叠后子串 ②空白全删后子串 (`-layout` 会把日文串拆开)。
**纯 ASCII 的 OID 串另走 token 边界正则** `(?<![A-Za-z0-9_])OID(?![A-Za-z0-9_])` ——
无边界时一个 2 字符的表单 OID 会命中以它开头的每个长 item OID, 单字符 OID 命中一切,
会把 OID 定位率虚高到接近 100%。这条是本勘察中途自纠的一处方法错误, 下面所有 `*_oids`
数字都是**改正后**的。

## 2. S0-1 页索引覆盖率

### 2-1 朴素「名称 → 页」子串索引

| PDF | 实体类 | 总数 | 能定位 ≥1 页 | 1–20 页 (可用) | 中位页数 |
|---|---|---|---|---|---|
| workflow (933p) | activities | 77 | 77 (100%) | **76 (98.7%)** | 3 |
| workflow | events | 14 | 14 (100%) | 11 (78.6%) | 14.5 |
| workflow | forms | 21 | 21 (100%) | 15 (71.4%) | 7 |
| workflow | items (label) | 959 | 926 (96.6%) | 600 (62.6%) | 8 |
| workflow | item groups (name) | 65 | 65 (100%) | 55 (84.6%) | 12 |
| annotated (212p) | forms | 21 | 21 (100%) | **20 (95.2%)** | 4 |
| annotated | items (label) | 959 | 921 (96.0%) | 745 (77.7%) | 3 |
| annotated | activities | 77 | 18 (23.4%) | 18 (23.4%) | 2.5 |
| annotated | events | 14 | 8 (57.1%) | 8 (57.1%) | 7 |

原始 OID 串 (S0-0 的量化确认):

| PDF | activity_oids | form_oids | item_oids | group_oids |
|---|---|---|---|---|
| annotated | 0/77 | **21/21 (100%)** | **941/959 (98.1%, 中位 1 页)** | 0/126 |
| workflow | 0/77 | 4/21 | 21/959 | 0/126 |

⚑ **修正 S0-0 的一条判断**。原勘察写「PDF 文本层 OID 几乎搜不到 (Annotated: 某 item OID 命中 1)」,
被读成了否定证据。实际上 **`1` 就是命中 1 页**, 而全量看是 **941/959 的 item OID 在 Annotated
文本层可定位, 中位 1 页** —— Annotated 版蓝色 `id` 徽章的文字就在文本层里 (与
`c2_pre_survey.md` §7-5 的观察一致, 只是当时没量化)。原勘察举的另两个例子 (一个活动 OID、
一个 item-group OID) 为 0 的原因是**活动 OID 与 item-group OID 本来就不印在页面上**,
不是文本层缺失。

⇒ **Annotated 的钥匙不必绕日语名, item OID 直接就是钥匙**; workflow 才需要日语名。

复跑验证 (肉眼可见的原始证据; OID 取自卡片文件名, 不直写):

```bash
# 体重未实施项的 OID —— 用 redline-safe 选择子取, 结果唯一确定
OID=$(ls data/study/st01/cards | grep -E '__LB__W' | sort | tail -1 | sed -E 's/^st01__LB__(.+)\.md$/\1/')
pdftotext -layout -f 174 -l 174 ../source/study/ensemble/ENSEMBLE_59.0_Annotated.pdf - | grep -cn "$OID"
# → 1   (该 OID 在 p.174 出现且仅出现一次)
```

### 2-2 ★ 更强的结构: 标题行切块 (本勘察最主要的发现)

两份 PDF 每页都有页眉 `ENSEMBLE | ENSEMBLE [59.0]` 与页脚 `VIEDOC 4.82 | … | Page N of M`,
**两份各 100% 命中, 且页脚页码与实际页序 100% 相符** (自校验)。在页眉之后, **块首页**带标题行:

- workflow: `<event 名> / <activity 名>` + `<form 名>`
- annotated: `<form 名> <form_oid>`, 或 `<form 名> - Code Lists`

按标题行切块的结果:

| PDF | 块数 | 与 catalog 的对应 | 块长中位 | 块长最大 | ≤20 页 |
|---|---|---|---|---|---|
| workflow | **110** | **= 110 条 `assignments`, 1:1 零缺口** | 6 | 36 | 92 (83.6%) |
| annotated | 42 | = 21 form 块 + 21 code-list 块, 每 form 恰好 1 次 | 3 | 24 | 41 (97.6%) |

workflow 的 110 块覆盖 930/933 页 (1–3 页是封面与目录), **77/77 活动全部落在块内, 零缺口**。

⇒ 切块比子串搜索准得多: 子串搜索把交叉引用页也算进去 (再评价活动的名称命中 17 页),
切块则让**每页唯一归属**于一个 (event, activity, form)。

不同检索键下的「1–20 页可用率」:

| 键 | 分母 | 1–20 页 | 中位 | 最大 |
|---|---|---|---|---|
| workflow `(activity_oid, form_oid)` ← **推荐** | 110 | **92 (83.6%)** | 6 | 36 |
| workflow `activity_oid` (跨其全部 form 取并) | 77 | 59 (**76.6%**) ⚠ | 7 | 52 |
| annotated `form_oid` (仅 form 块) ← **推荐** | 21 | **21 (100%)** | 3 | 14 |
| annotated `form_oid` (form 块 + code-list 块) | 21 | 18 (85.7%) | 6 | 38 |

超 20 页的 18 个活动全部是**挂了 QOL 表单**的活动, 页数 23–52: 背景活动 52 / 再评价活动 40 /
术前 AE 活动 36 / 随访族 F1 的四个时点各 30 / 随访族 F2 的四个时点各 28 / 中止时 QOL 活动 27 /
随访族 F3 的四个时点 24–26 / 两个放射线合并症活动 23 与 25。按 `(activity, form)` 拆开后
这些块本身就 ≤36 页。

### 2-3 dogfood 具体案 (LB 身高体重题)

| 对象 | annotated | workflow |
|---|---|---|
| 表单 LB | form 块 **174–176** + code-list 块 **177–179** | 39 页命中 (名称); 按活动分散在各块 |
| 体格测量项目组 | 由成员 OID 推出 **p.174** (身高/身高未实施/体重/体重未实施 4 项全在 174) | 名称命中 12 页 |
| 体重未实施项 | **p.174 (唯一)** | 0 (workflow 无 OID) |
| 术前 LB 活动 | 名称命中 174, 177 | 块 **315–319** |
| 第 1 周期 day8 LB 活动 | 0 | 名称 72 / 87 / 135 / 152 |
| 背景活动 | 名称 62, 65 | 块并 52 页 (含 QOL) |
| 再评价活动 | 名称 11 页 | 块并 40 页 |
| 中止 PS 活动 | 0 | 块 **373** (单页) |

⚠ 体格测量组的成员之一 **PS 项的 OID 只有 2 字符**, 在 Annotated 命中 6 页
(152 / 154 / 174 / 177 / 200 / 206) —— 它在别的表单里也出现。**短 OID 会跨表单串味**,
实现时须用 `(form_oid, item_oid)` 双键或先按 form 块裁剪。

### 2-4 ★ 这个通道到底能答什么 (两份 PDF 的分工被实测坐实)

- **annotated p.174** = LB 表单的**完整**画面 + OID 徽章, 6 个 item 齐全:
  身高项 / 身高未实施项 / 体重项 / 体重未实施项 / PS 项 / 血检实施项。
- **workflow p.315** = 同一表单在**术前 LB 活动**下的**实际显示**: **只有 体重项 +
  体重未实施项 + PS 项, 身高那一对整个不显示**。

这正是 dogfood 那道题卡片答不出的东西。而且**体重未实施项在 `catalog.json` 里 `label` 是空串**
(959 个 item 中有 **30 个空 label**), 它的官方日语标签**只存在于画面上** —— 既是 L1 的直接证据,
也是 PDF 旁路的第一等价值。

## 3. S0-2 每页标识可识别性 + 规则 A 人眼核对

### 3-1 页面模式 (确定性测量)

| 模式 | 正则 | annotated | workflow |
|---|---|---|---|
| 页眉 | `^ENSEMBLE \| ENSEMBLE \[59\.0\]` | 212/212 (100%) | 933/933 (100%) |
| 页脚 | `VIEDOC ([\d.]+) \| (\S+) UTC \| Page (\d+) of (\d+)` | 212/212 (100%) | 933/933 (100%) |
| 页脚页码 == 实际页序 | — | 212/212 | 933/933 |
| **块首标题行** | 见 §2-2 | 42/212 (19.8%) | 110/933 (11.8%) |

⇒ **每页都能自证页码**, 但**只有约 12–20% 的页自带 Form/Activity 标识**; 其余是延续页,
必须靠标题行**前向填充**才知道自己属于谁。这是本节最重要的一条: 「按页判身份」不成立,
「按块判身份」成立。

### 3-2 规则 A: N=12 页人眼核对 (6 页/份, 等距取样)

取样页号写死: annotated `1, 43, 85, 127, 169, 211`; workflow `1, 187, 373, 559, 745, 931`。

```bash
pdftoppm -r 80 -png -f N -l N <pdf> <out>/<stem>
```

| # | 页 | 索引判定 | 页上实际所见 (结构化) | 页自带标题? | 判定 |
|---|---|---|---|---|---|
| 1 | ann p.1 | form NAC | NAC 表单块首页, 标题 + OID 徽章 + 治疗开始有无等单选项 | 是 | **PASS** |
| 2 | ann p.43 | codelist 分配因子表单 | 该表单的 Code Lists 页, 两张 TNM 分期码表 | 是 | **PASS** |
| 3 | ann p.85 | form RC | RC 表单延续页, 第 16–20 组「事象名 / 最恶 Grade / 重笃性」三联 + OID 徽章 | 否 (延续页) | **PASS** |
| 4 | ann p.127 | codelist AE | AE 的 Code Lists 页, 消化道毒性项的 CTCAE 分级码表 | 否 | **PASS** |
| 5 | ann p.169 | codelist TME | TME 的 Code Lists 页, 淋巴结分期码表 + 肿瘤总体疗效码表 | 否 | **PASS** |
| 6 | ann p.211 | codelist GN | GN 的 Code Lists 页, 基因突变 codon 码表 | 否 | **PASS** |
| 7 | wf p.1 | (无块) | 封面, 设计版本 59 / 表单总数 110 等统计 | — | **PASS** (正确地不归属) |
| 8 | wf p.187 | 化疗 B 臂 / 第 4 周期活动 / NAC | irinotecan 给药状况面板 (irinotecan 只出现在 B 臂方案) | 否 | **PASS** |
| 9 | wf p.373 | 完遂中止事件 / 中止 PS 活动 / LB | 标题行原文一致; 画面只有体格测量组的 PS 项 | 是 | **PASS** |
| 10 | wf p.559 | 随访族 F1 / 48 个月时点活动 / TME | 标题行原文一致; 内镜与盆腔 MRI 两个面板 | 是 | **PASS** |
| 11 | wf p.745 | 随访族 F3 / 4 个月时点活动 / QOL | QOL 问卷第 9–11 组题目 | 否 | **PASS** |
| 12 | wf p.931 | 转归事件 / 晚期术后并发症活动 / POC | Clavien-Dindo 分级码表 (第 5–7 组) | 否 | **PASS** |

**12/12 PASS**。逐页的真实标题原文与项目名见伴生件同节。

⚠ **这个 PASS 的强度要说清楚**: 12 页里只有 **4 页自带标题行**, 另 7 页是延续页 ——
对它们的判定是「页上项目内容是否属于索引所说的那个表单」, 属**间接**核验, 不是逐字比对。
wf p.187 的 B 臂判定依据是 irinotecan 只出现在该臂方案, 属推理而非页面原文。
另: 本次取样是**等距无偏**取的, 没有挑好例子; 但 12 页对 1,145 页而言只能证「没有明显系统性错位」,
不能证 100% 正确。

## 4. S0-3 Bedrock 多模态实测

四个 `selectable_models` (`server/config.py:59-73`, 与 Chat UI 下拉同一事实源), 全部走
`server/llm_config.py::create_router` 构造的 litellm `Router`, 调用形式与
`server/router.py:449` 的 `llm_router.acompletion(model=…, messages=…)` 相同。区域
`ap-northeast-1` (`.env` `AWS_REGION`), 凭据走 `AWS_BEARER_TOKEN_BEDROCK`。

图像走 OpenAI 风格 content block: `{"type":"image_url","image_url":{"url":"data:image/png;base64,…"}}`。
测试页 = workflow **p.315** (术前 LB 活动的块首页), `-r 110`。
提问 (日语, 要求列出画面上显示的项目名, 用画面日语标签而非 OID)。

| id | 模型串 | 结果 | prompt tok | completion tok | 墙钟 |
|---|---|---|---|---|---|
| opus-5 | `bedrock/converse/global.anthropic.claude-opus-5` | **OK** | 1564 | 326 | 8.39s |
| sonnet-5 | `bedrock/converse/global.anthropic.claude-sonnet-5` | **OK** | 1564 | 302 | 7.94s |
| gpt-terra | `bedrock/converse/global.openai.gpt-5.6-terra` | **OK** | 1370 | 281 | 6.42s |
| gpt-sol | `bedrock/converse/global.openai.gpt-5.6-sol` | **OK** | 1370 | 222 | 8.73s |

**4/4 支持图像输入, 零失败。** 一页图 ≈ 1.4–1.6k prompt token (Claude 1564 / GPT 1370)。

四条回答的**结构**判读 (逐字摘录见伴生件 §3 与 `model_probe.json`):

| 模型 | 是否读出体格测量组 | 是否读出 PS 项 | 是否读出血检实施项 | 是否捏造身高项 |
|---|---|---|---|---|
| opus-5 | 是 | 是 | 摘录在 300 字符处被截断 | **否** |
| sonnet-5 | 是 | 是 (含 6 个选项) | 是 | **否** |
| gpt-terra | 是 | 是 (含 6 个选项) | 是 | **否** |
| gpt-sol | 是 | 是 | 是 | **否** |

**独立核验 (我本人看了同一张图)**: p.315 实际显示 = 面包屑 (事件 / 活动) → 表单 LB →
#1 重复确认勾选 → 体格测量组 {**体重项**, 体重未实施项, PS 项} → 血检实施项。
**页面上没有身高项。** 四个模型**全部没有捏造身高项**, 判读与实图一致 (opus-5 摘录在 300
字符处被我截断, 未列血检实施项是截断所致而非漏读)。这是本通道最关键的一条判别力: 卡片层
的体格测量组无条件含身高项, 只有画面能证明它在该活动下不显示。

PNG 体积 (workflow p.315):

| dpi | bytes |
|---|---|
| 80 | 44,851 |
| 110 | 66,933 |
| 150 | 98,289 |

## 5. 对设计的影响 (I2-1 / I2-2 必须吸收)

1. **索引形态改为「块」而非「名称 → 页列表」**。`(event, activity, form) → [起页, 止页]`,
   workflow 110 块与 `assignments` 1:1; annotated 21 form 块 + 21 code-list 块。
   `build_pdf_page_index.py` 应产出块表, 并把「块数 == len(assignments)」「块覆盖 930/933 页」
   写成断言 —— 这两条一旦被将来的 PDF 版本打破, 必须响地失败而不是静默给错页。
2. **两份 PDF 的钥匙不同**: annotated 用 **item OID 直查** (941/959, 中位 1 页) 或 form 块;
   workflow 用 **(activity, form) 块**。不要对 workflow 找 OID (0 命中), 也不要对 annotated
   找活动名 (23%)。
3. **短 OID 要防串味**: ≤2 字符的 item OID 必须配 `form_oid` 双键, 否则跨表单命中
   (§2-3 那条 6 页命中就是实例)。
4. **页数上限的现实值**: 推荐键下中位 3–6 页、最大 36 页。一页图 ≈1.5k prompt token,
   ⇒ 6 页 ≈9k token, 36 页 ≈54k token。**上限建议 6–8 页**, 超限降级为页号提示 (PLAN I2-2 已写)。
5. **`-r 110` 够用**: 四模型在 110 dpi 下全部正确读出日语标签, 无需 150。
6. **L1 有了确定性素材**: 30 个空 label 的 item, 其官方日语标签只在 annotated 画面上。
   但 L1 是「答题时附对照表」的确定性单元, 若要从 PDF 取标签属新增单元, 不在 L1 范围内 —— 别混。

## 6. G0 判定

| 判据 | 实测 | 结论 |
|---|---|---|
| (a1) workflow 中 ≥80% 活动可定位到 1–20 页 | 朴素名称索引 **76/77 = 98.7%**; 块键 `(activity, form)` **92/110 = 83.6%** | **PASS** |
| (a2) 同上, 但按 `activity_oid` 跨表单取并 | 59/77 = **76.6%** | ⚠ **低于 80 线** |
| (b) annotated 中 ≥80% 表单可定位 | form 块 **21/21 = 100%** (中位 3 页, 最大 14) | **PASS** |
| (c) ≥2 个 selectable model 接受图像输入 | **4/4** | **PASS** |

**G0 = PASS。**

⛔ 引用时不得把 (a) 写成「活动定位率 98.7%」就完事。诚实口径是:
**按 `(activity, form)` 检索时 83.6% 落在 1–20 页; 按活动整体取并时只有 76.6%, 不达线,
超线的 18 个活动全部是挂了 QOL 表单的。** 实现必须用 `(activity, form)` 双键,
这不是优化项而是 G0 成立的前提。

## 7. 已知限制

- 勘察索引落在 `.gitignore` 覆盖的 `data/study/` 下 (`.gitignore:10`), **不进 git**。
- 勘察索引是**草案**, 未进生产路径: `data/study/st01/pdf_page_index_survey_draft.json`
  由一次性勘察脚本 `scripts/study/survey_pdf_pages.py` 生成。生产索引另有其人 ——
  `data/study/st01/pdf_page_index.json`, 由 I2-1 的 `scripts/study/build_pdf_page_index.py`
  产出, **两者不可互换**, 草案带 `meta.draft=true` 会被生产加载器拒收。
- 草案 1.16 MB, 含全部实体的逐页命中列表; 生产版只留块表 + OID→页 两张小表 (I2-1 已落地, 约 100 KB)。
- 规则 A 只做了 12 页, 且其中 8 页无页面自带标题 (§3-2 的 ⚠)。
- S0-3 只测了**一页**、一个提问。「模型能读这一页」不等于「模型在任意页上都读得准」,
  更不等于「答题质量会提升」—— 后者归 P1 预登记 + V3。
- annotated 与 workflow 都停在 **ENSEMBLE 59.0 / 2025-02-20**; catalog 是 V59。版本一致,
  但若将来 PDF 与 ConfigReport 版本漂移, 块数断言会响。
