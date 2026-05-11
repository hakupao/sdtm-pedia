# Claude Project 制作教程 — SDTM 知识库发布版 v1.1

> release v1.0 自部署教程 (从零搭一个能查 CDISC SDTM 的 Claude Project).
> 读完本教程: 30-60 分钟得到一个完整可用的 Claude Project (含 indexing 后台等待时间). 19 文件 1.29M tokens, 完整 24 题测试全通过基线.
> 信源: 项目仓库 ./ (system_prompt.md + uploads/ × 19).

---

## 0. 前置要求

- [ ] **Claude Pro ($18/月) / Max ($100 或 $200/月, 比 Pro 多 5x/20x 用量) / Team / Enterprise 任意套餐。** Max 是 2025 年新增套餐, 定位在 Pro 之上、Enterprise 之下。Free 套餐最多创建 5 个 Project, 但读入本 KB 的 1.29M tokens 需要 Pro 以上。
- [ ] **网页访问** [claude.ai](https://claude.ai): 本教程全程在 Web UI 操作
- [ ] **本地 clone 本仓库**: 需要读 `./uploads/` 下的 19 个文件和 `./system_prompt.md`

**关于"能力 vs 容量"**:
- 覆盖范围: core codelist 99.3% / supp codelist 100% / questionnaires codelist 55.8% / 63 域 examples 100% / 6 章 chapters 全展开
- 单文件上限已提升到 **30 MB** (2025 年从 1 MB 大幅扩容), 本 KB 最大文件 11b (~890 KB) 完全在范围内, 无需分割。

---

## 1. 新建 Claude Project

1. 登录 [claude.ai](https://claude.ai)
2. 点击左侧边栏的 "**Projects**" → 右上的 "**+ New Project**" (或中部的 "**Create Project**") 按钮。
3. **命名建议**: `SDTM Knowledge Base` 或 `CDISC SDTM Expert`
4. **Description** (可选): `SDTM (Study Data Tabulation Model) knowledge base from CDISC standards. Answers variable definitions, codelist terms, example datasets, cross-domain references.`
5. **访问权限** (当前 UI 只有 2 个选项):
   - "**Keep it private**": 个人用 (默认)
   - "**Share with your broader organization**": Team / Enterprise 套餐可用; 共享权限分 "Can use" / "Can edit" 两级
   - 注意: "Public" 选项 **2026 年现在已从 UI 中移除**。独立的"公开分享链接"仍不支持。

---

## 2. 配置 System Prompt (Set project instructions)

System Prompt 是 Project 的"角色与行为说明书", 定义模型如何路由查询、引用源、处理边界.

### 操作

1. 打开刚建好的 Project, 右上角点 "**Edit project**"
2. 找到 "**Set project instructions**" 按钮 (或 "**Project instructions**" 输入框)。注: 2025 年 UI 标签已从 "Custom instructions" 改为 "Set project instructions"。
3. **完整复制** `./system_prompt.md` 的全部内容 (不要截断)
4. 粘贴到框里
5. **保存**

### 为什么 System Prompt 这么长

发布版的 System Prompt 约 **4-6K tokens**, 包含 6 段累积指令:
- Stage 1 段: 章节全展开使用规则
- Stage 2 段: examples 高频域数据查询优先级
- Stage 3 段: examples 剩余域回落策略
- Stage 4 段: terminology 高频 codelist (`11*`) 优先, fallback 到 `08_terminology_map`
- Stage 5 段: terminology 中频 codelist (`12*`) 加入 CT 查询链
- Stage 6 段: terminology 尾部 + 6 个 MedDRA 级 giant codelist 走 Deferred stub 声明

每段都是一个覆盖层, 合起来就是"对所有文件的查询路由策略". 缺任何一段会导致 Claude 不知道去 11* 查 CT Code.

---

## 3. 上传 19 个知识库文件

### 操作

1. 仍在 "Edit project" 界面, 找 "**Project Knowledge**" 面板
2. 把 `./uploads/` 目录下的**全部 19 个 `.md` 文件**一次性选中
3. 拖拽到 Knowledge 面板 (或点 "Add files" 选择)
4. Claude 会开始 upload (~1-2 分钟) → 然后进入 Indexing

### 文件清单 (19 个, 总 1,286,161 tokens)

顺序无所谓, 全传即可. `./uploads/` 目录下共 19 个 `.md` 文件, 全部上传即可.

**关键概念**:
- 文件名前缀 `00-13c` 是查询优先级的信号 (System Prompt 里引用这些前缀做路由)
- **不要重命名**任何文件 — Project Knowledge 的文件名本身就是 Claude 引用源的锚点
- **不要拆/合并**文件 — 尤其 11b (~890 KB, 最大单文件), 在 30 MB/file 上限下完全无需分割。旧的 1 MB / 256K tokens 限制已是过去式, 现在没有问题。

### 常见问题

**Q: UI 显示某个文件 "File is too large"**
A: 单项目文件上限是 **30 MB** (2025 年从 1 MB 大幅扩容). 本 KB 最大文件 11b (~890 KB) 完全在范围内, 无需分割. 检查是否文件有被 editor 附加 BOM 或 CRLF 即可. 文件数量无上限 (在 context window 范围内).

**Q: 我只想上传部分, 测试看看**
A: 不建议. T1-T22 + 优先级验证的 24/24 PASS 基线是**全 19 文件**的产物. 少传会退化.

**Q: 上传进度一直卡在 90%**
A: 一般是网络问题. 刷新页面, Claude 会保留已上传文件, 继续上传剩余.

---

## 4. 等 Indexing (重要: 不用真等)

上传完成后, UI 可能显示 "**Indexing**" 指示器, 持续时间 **30-60 分钟** 甚至更长.

### 不要真等 Indexing 完成

实测观察:
- Indexing indicator **不可靠**: 即使显示还在 indexing, 立即提问也能命中新内容
- 真等的话 60 分钟起步, 还可能提示 indexing 失败需重试
- 部署流程的正确判断方式是 **直接试问 1-2 题** (下一步), 命中即可用

**Indexing 进度显示是否出现在官方文档中并无明确说明** — 2026 年现在的 UI 中该指示器有时根本不出现. 实用上通过 §5 smoke test 验证更可靠.

上传完, 直接进入 §5 smoke test.

---

## 5. Smoke Test (3 题, ~5 分钟)

在 Project 新建一个 chat, 依次问下面 3 题, 每题对照期望答案.

### T1: 变量定义查询 (最基础)

**提问**: `AE.AEDECOD 的 Core 属性是什么? 引用哪些章节?`

**期望**:
- Core = **Required** (或 Req)
- 引用源 `05_mega_spec.md §AE` + `04_variable_index.md (Sy/R)` + `02_chapters.md §4.3.6` (三元结构 AETERM/AEMODIFY/AEDECOD)
- 提到 AEPTCD 配套变量

如果 Claude 答 Core=Permissible 或答不出章节号, 说明 Indexing 还没生效, 等 5-10 分钟再试.

### T17: Codelist Term 表查询 (RAG 深度)

**提问**: `C66742 codelist 的所有 Term 值是什么?`

**期望**:
- 4 个 Term: **C49487 N / C48660 NA / C17998 U / C49488 Y**
- Extensible: **No**
- 列出 41 个 Related Domains (AE/AG/BS/CE/...)
- 源标 `11a_terminology_high_core.md` + `02_chapters.md §4.3.7`

如果只给 Y/N/U/NA 但不给 C-code, 说明 11a 没被 RAG 拿到, 检查 11a 是否成功上传.

### T22: Giant Codelist 边界识别 (stub 验证)

**提问**: `C65047 codelist 有哪些 Term 值?`

**期望** (这是最关键的边界测试):
- Claude 应**声明** "C65047 是 Laboratory Test Code, 含 2,536 terms, 超大规模, Project 内未完整列出所有 Term 值"
- 引用源 `13a_terminology_tail_core.md` (stub 定义) + `../../../knowledge_base/terminology/core/lb_part*.md` (源文件) + NCI EVS Browser 入口
- **零臆造**: 不能给出具体 term 值 (如果 Claude 列出了 term, 是幻觉, 必须排错)

如果 Claude 试图列 term 或说"不知道", 说明 System Prompt 里的 Stage 6 Deferred stub 规则没生效, 请重新检查 System Prompt 中是否包含 Stage 6 (在内部版本 v2.6 中确定的 Deferred stub 规则)。

### Release v1.0 完整 demo
除上述 T1/T17/T22, release v1.0 还提供 10 题完整 demo (含 anti-hallucination probe), 见 [../../DEMO_QUESTIONS.zh.md](../../DEMO_QUESTIONS.zh.md). 用户 onboarding 推荐先跑 D0 + D1 + D6 三题 (5 分钟).

---

## 6. 完整回归测试 (可选, 24 题, ~40 分钟)

如果想确认"我部署的 Project 等同于项目基线 Project":

1. 打开 `../../claude_projects/dev/test_results.md` (从仓库)
2. 逐题提问 T1 → T22 + T-core-reb + T-supp-reb (共 24 题)
3. 对比 Claude 回答 vs 矩阵里记录的 v2.6 终态答案
4. 全部一致 = 部署 PASS; 有偏差 = 记录 A/B 差异, 可能是新上传 / indexing 状态差异

建议:
- **一题一新 chat** (避免上下文污染)
- 每题等首 token ~20-30 秒; 如果 60 秒无响应, 可能触发了限流, 等一分钟重试
- 重点关注 **T3** (跨批 RELREC) 和 **T7/T17** (C66742 原文命中) — 这两道检验 RAG 能跨文件召回

---

## 7. 排错手册

| 症状 | 可能原因 | 处理 |
|------|---------|------|
| 所有查询都答"不知道" | System Prompt 没贴全 | 检查 Set project instructions 是否包含全部 6 段 stage, 尤其 Stage 6 |
| 给的章节号是错的 (如 §4.3.6 实际应是 §4.3.7) | 02_chapters.md 没上传或被截断 | 重上传 02_chapters.md, 检查文件大小 > 200KB |
| T22 C65047 列了具体 term 值 (幻觉) | Stage 6 Deferred stub 规则没生效 | 检查 System Prompt Stage 6 段 + 检查 13a_terminology_tail_core.md 是否上传 |
| 问 CT code 只返回 08 而不是 11*/12*/13* | CT 查询优先级规则缺失 | 检查 System Prompt 末尾是否包含 `CT 查询优先级 11*>12*>13*>08` |
| 出现 Capacity 警告 | Claude Projects 政策调整 — **官方目前没有 "X% capacity" UI 的正式说明**, 如有显示仅供参考 | 按移除优先级: 13c > 12c > 12b > 11c (保留 11a/11b/09/05/02 核心) |
| 某题答得很慢 / 频繁限流 | Pro 套餐 RAG 限流 | 等 30-60 秒重试; 如持续, 考虑升级 Team/Enterprise |
| 问 questionnaires (quest) codelist 约 44% 答不上 | 发布版只覆盖 quest 55.8% (设计决定) | 正常现象, quest 长尾 296 个 codelist 归后续 Phase 7 RAG 处理 |

---

## 8. 升级 / 降级路径

当前 30 MB/file 上限下, 本 KB 无需降级 — 全部 19 个文件均有充足余量. 以下优先级列表供旧环境容量受限时参考.

### 如果想推高覆盖 (可选, 默认不做)

- 把 quest 覆盖从 55.8% 推到 ~80%: 需追加一批 quest tail extraction (+~180K tokens)
- 把 6 个 giant (MedDRA 级 codelist) 从 Deferred stub 换成 inline: 需 +500K tokens, 不推荐

### 如果想降级 (旧环境容量不够时)

按移除优先级 (保留最有用的):
1. 先删 `13c_terminology_tail_supp.md` (43K, supp 长尾)
2. 再删 `13a_terminology_tail_core.md` (146K, 但含 6 giants stub — 删了 T22 会 FAIL)
3. 再删 `12c_terminology_mid_supp.md` (23K)
4. 再删 `12b_terminology_mid_questionnaires.md` (225K)
5. 再删 `12a_terminology_mid_core.md` (130K)

保留底线: `11a/b/c_terminology_high_*` + `09/10_examples_data_*` + `00-08` 核心结构 = 约 800K tokens.

---

## 9. 团队协作注意

- Claude Projects 的 Knowledge 上传是 **per-Project** 的, 无法跨 Project 共享
- Team/Enterprise 套餐内成员共享 Project, 但每人看到的是同一份 Knowledge (不是 fork)
- 如果团队成员修改了 System Prompt 或删除了文件, **所有人**都受影响; 建议锁定 edit 权限给 1-2 人
- 不支持 "发布到公开链接": 如果要给外部用户, 只能每人自己按本教程搭一遍

---

## 10. 后续路径

- 本发布版已是**完整终态**, 短期内不会再扩容
- 长尾 302 个 codelist (296 quest + 6 giants) 归属后续 Phase 7 自建 RAG (设计文档: 本项目 `../../claude_projects/docs/`)
- Claude 在 2025 年已为付费套餐的 Projects 自动引入 **RAG (Retrieval-Augmented Generation)** — 超过 200K context window 的知识库会自动切换到 RAG 模式, 使本 KB 的 1.29M tokens 得以处理. Enterprise 部分模型支持 500K context window.
- 发布版使用过程中如果发现知识库内容有缺失/错误, 反馈到项目 issue tracker; 知识库更新后会重新 build 发布版

---

## 附: 验证清单 (部署后自查)

- [ ] Claude Pro 以上套餐已启用
- [ ] Project 已创建, 命名清晰
- [ ] Set project instructions 粘贴了完整 System Prompt (含 6 段 stage)
- [ ] Project Knowledge 面板显示 19 个文件已上传
- [ ] T1 AEDECOD Core 查询 PASS (答 Req + 引 §4.3.6/§4.3.5)
- [ ] T17 C66742 Term 表查询 PASS (4 term + 41 related domains)
- [ ] T22 C65047 giant 边界查询 PASS (声明 stub, 零臆造)
- [ ] UI capacity 显示 ~77% (如有显示的话)

全部 ☑ = 部署成功, 可以开始日常使用.

---

*v1.1 — 2026-05-11 — UI 术语同步至 2026 年官方规范 (Custom instructions → Set project instructions / 30MB 上限 / Max 套餐)*
*方法论细节见 ../../claude_projects/docs/ ; release v1.0 总览见 ../README.zh.md*
