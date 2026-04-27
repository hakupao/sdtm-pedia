# ChatGPT GPT 制作教程 — SDTM 知识库发布版

> 从零开始搭建一个能查 CDISC SDTM 标准 (63 域 + terminology + chapters) 的 Custom GPT.
> 读完本教程你会得到: 一个可用的 ChatGPT GPT, 能精确回答 SDTM 变量定义 / codelist / examples / 跨域关联, 且能识破常见虚构前提 (如 LBCLINSIG / SUPPTS / PF deprecated).
> 总耗时: **30-60 分钟** (含 indexing 等待).

---

## 0. 前置要求

- [ ] **ChatGPT Plus / Team / Enterprise** 套餐 (免费版无法建 Custom GPT)
- [ ] **网页访问** [chatgpt.com](https://chatgpt.com): 本教程全程 Web UI 操作
- [ ] **本地 clone 本仓库**: 需要读 `../../chatgpt_gpt/current/` 下的 `system_prompt.md` (约 8.6KB) 和 `uploads/` 下 9 个 .md 文件

**关于"团队共享 vs GPT Store 公开发布"**:
- Org/Team 套餐内可直接 invite 成员, **免审核**
- GPT Store 公开发布需 OpenAI 审核 (一般 1-3 工作日), 任何 ChatGPT 用户都可访问

---

## 1. 新建 Custom GPT

1. 登录 [chatgpt.com](https://chatgpt.com)
2. 左下角点 "**Explore GPTs**" → 右上角 "**+ Create**"
3. 进 **Configure** tab (不是 Create tab 的对话模式)
4. **Name**: 建议 `SDTM Expert` 或 `CDISC SDTM Knowledge`
5. **Description** (英文一句, ~130 字符): `CDISC SDTMIG v3.4 + SDTM v2.0 Expert — Variable definitions, rule reasoning, controlled terminology, cross-domain linking.`
6. **Capabilities**: 关闭 **Web Search / Code Interpreter / DALL-E** (本 GPT 纯知识问答, 启用反而扩大幻觉面)

---

## 2. 配置 Instructions (System Prompt)

1. 仍在 Configure tab, 找 "**Instructions**" 框
2. **完整复制** `../../chatgpt_gpt/current/system_prompt.md` 全文 (v2.2 LIVE, 8,582 chars) 粘贴进去
3. **不能截断**: ChatGPT UI 字数指示器写 8000 chars 限, 实测接受 8,582 chars (verified, 已部署运行). 如果你的 ChatGPT UI 拒收, 优先剔除 §Conversation Starters 段 (非核心)
4. **保存**

**v2.2 LIVE 关键能力** (粘贴后保留, 别改):
- GFINHERT 7 字母精确 (修复 R1 GFINHERTG extra-G 拼写漂移)
- L858R / Exon 19 科学一致性主动识别 (anti-hallucination bonus)
- AHP × 3 反虚构锚 (变量级 / 跨域级 / deprecated 级)

---

## 3. 上传 9 个知识库文件

1. 在 Configure tab 找 "**Knowledge**" 面板, 点 "**Upload files**" 或拖拽
2. 选 `../../chatgpt_gpt/current/uploads/` 下**全部 9 个 .md 文件**, 顺序: `01 → 02 → 03 → 04 → 05 → 06 → 07 → 08 → 09`
3. **不要重命名 / 不要拆合并**: 文件名前缀是 System Prompt 路由的锚点

**文件清单 (9 文件, 总 ~2.5M tokens)**:
- `01_navigation.md` (~46K) — ROUTING + INDEX + VARIABLE_INDEX
- `02_chapters_all.md` (~60K) — SDTMIG ch01/02/03/04/08/10
- `03_model_all.md` (~17K) — SDTM v2.0 Model 6 段
- `04_domain_specs_all.md` (~185K) — 63 域 spec 全量平权
- `05_domain_assumptions_all.md` (~54K) — 63 域 assumptions
- `06_domain_examples_all.md` (~220K) — 63 域 examples
- `07_terminology_core_high_freq.md` (~200K) — core 高频 15 codelist
- `08_terminology_quest_and_supp.md` (~1M) — questionnaires + supplemental
- `09_terminology_core_mid_tail.md` (~698K) — core 中尾段

ChatGPT GPT Builder Knowledge **20 文件硬限**, 当前 9/20 (11 文件 headroom).

**常见 Q**:
- "File too large" → 检查文件被 editor 误加 BOM / CRLF; 重存 UTF-8 LF
- 上传卡 90% → 网络问题, 刷新页面 (已传文件保留, 续传剩余)

---

## 4. 等 Indexing

ChatGPT File Search RAG indexing 一般 **5-15 分钟**. UI 上每个文件状态从 "Processing..." → "Ready". 全部 Ready 再进 §5.

实测无明确"全部 indexing complete"指示器, 单个文件 Ready 即视为可用.

---

## 5. Smoke Test (3 题, ~5 分钟)

**右上角 Preview**, 一题一新 chat 提问:

| # | 提问 | 期望要点 | 验证点 |
|---|------|---------|------|
| T1 | `AESER 的 Core 属性是什么? 列出 NY codelist (C66742) 全部 term 值.` | Core = **Exp** (非 Req); 4 term: **Y / N / U / NA** + C-code | 最高频易错 + 高频 codelist 命中 |
| T2 | `GFINHERT 是什么变量? 在哪个域?` | GF (Genomics Findings, v3.4 新域); INHERT 全称 Inherited; 7 字母精确 (不是 GFINHERTG) | v3.4 新域识别 + v2.2 拼写修 |
| T3 | `LBCLINSIG 在哪个 codelist?` (虚构变量) | GPT 应**识破**: LBCLINSIG 不存在 LB 域 v3.4 spec; 建议改用 LBNRIND / LBSTRESC | AHP1 anti-hallucination |

**3/3 PASS** = 部署成功; 任一 FAIL → 看 §7 排错.

---

## 6. 完整回归 (10 题, ~30 分钟, 可选)

打开 `../DEMO_QUESTIONS.md`, 逐题提问 Q1-Q10. **一题一新 chat** 避免上下文污染. 评分 ≥ 8/10 = 等同基线发布版.

---

## 7. 排错手册

| 症状 | 可能原因 | 处理 |
|------|---------|------|
| 答 GFINHERTG (extra G) | Instructions 不是 v2.2 LIVE | 检查 system_prompt.md 末尾"v3.4 新域变量名精确校验"段是否在 |
| 答 PF 域变量清单 (PF deprecated) | AHP3 锚未生效 | 重检查 system_prompt §CO-5 AHP-V3 + 反虚构段 |
| 答 "SUPPTS 是 dataset" | SUPP scope 段缺失 | 检查 system_prompt §SUPP scope 是否完整 (SUPPQUAL 不适用 Trial Design) |
| File Search 召回错段 | 文件分段失败 | 检查 system_prompt §P13 TableAware 提示是否在; 重传问题文件 |
| 答 "AESER Core = Req" | 04_domain_specs_all.md 未传 / 截断 | 重传; 检查文件大小 ≥ 180KB |
| 上传 ≥ 20 文件警告 | 触发 GPT Builder 硬限 | 按降级路径 §8 移除 |
| 首 token 慢 / 频繁限流 | Plus 套餐 RAG 限流 | 等 30-60 秒重试; 持续 → Team/Enterprise |

---

## 8. 升级 / 降级路径

**升级 (扩 KB)**:
- 当前 9/20 文件, 11 文件 headroom
- 加 v3.5 SDTMIG 新域 / questionnaires 长尾时, 在 `dev/scripts/` 加 bucket → merge → 增量上传

**降级 (容量警告)**:
按移除优先级 (保留最有用):
1. 先删 `09_terminology_core_mid_tail.md` (中尾低频)
2. 再删 `08_terminology_quest_and_supp.md` (questionnaires 长尾)
3. 再删 `06_domain_examples_all.md` (examples)

底线保留: `01-05 + 07` (导航 + chapters + model + spec + assumptions + 高频 CT) = 6 文件核心.

---

## 9. 团队协作 / GPT Store 发布

**Org/Team 共享**:
- 免审核, 直接 invite by email
- 成员看到的是**同一个 GPT**, 修改 Instructions 全员同步生效
- 建议锁 edit 权限给 1-2 人, 防误改

**GPT Store 公开**:
- 需 OpenAI 审核 (~1-3 工作日)
- 全网可访问, 适合开放知识库
- 注意名称 / Description 不要含敏感关键词或公司内部代号

---

## 10. 后续路径

- 本发布版已是**完整终态**, 短期内不会再扩容
- 长尾 questionnaires + 6 个 MedDRA 级 giant codelist 归后续 Phase 7 自建 RAG
- 知识库内容如有错漏, 反馈到项目 issue tracker; 修复后会重 build 发布版

---

## 附: 验证清单

- [ ] ChatGPT Plus / Team / Enterprise 套餐已启用
- [ ] Custom GPT 已建, 命名清晰
- [ ] Instructions 粘贴了完整 system_prompt.md (v2.2 LIVE, 8,582 chars)
- [ ] Knowledge 面板显示 9 个文件全 Ready
- [ ] T1 AESER + C66742 smoke PASS
- [ ] T2 GFINHERT 精确拼写 PASS (不是 GFINHERTG)
- [ ] T3 LBCLINSIG 反虚构识破 PASS

全部 ☑ = 部署成功, 可以开始日常使用.

---

*v1.0 — 2026-04-27 — 公司发布版*
