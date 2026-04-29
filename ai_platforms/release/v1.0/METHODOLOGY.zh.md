---
lang: zh
slug: methodology
order: 15
title: "构建方法与可信度"
---

# 构建方法与可信度 — 这份知识库怎么造的, 你为什么可以信它

> 最近更新: 2026-04-29 · 与构建过程同步维护, 不是营销文案.

第一次看到一份"AI 提取的 SDTM 知识库", 正常反应都是: *它会不会幻觉? 会不会漏页? 有人真的核过吗?* 这一页就是在回答这个问题. 它说明做了什么, 哪些可以追溯, 中途发现了哪些错, 以及你怎么自己核任何一条具体答案.

如果只看一节, 看 [§4 — 验证与已知问题](#4-验证与已知问题).

---

## 1. 数据来源

`knowledge_base/` 里每一条产出都能追到 4 个 CDISC 官方源文件之一. 没有第三方总结, 没有概述代替原文.

| 来源 | 版本 | 范围 |
|---|---|---|
| SDTM Implementation Guide PDF | v3.4 (2021-11-29) | 461 页 — 域 spec / assumptions / examples |
| SDTM Model PDF | v2.0 Final (2021-11-29) | 74 页 — 概念模型 |
| SDTMIG xlsx | v3.4 | 63 个域 / 1,917 个变量 |
| CDISC Controlled Terminology xlsx | 2024 发布 | 1,005 个 codelist / 37,939 个 term |

原始文件不在仓库里 (CDISC 版权). 详见 [项目免责声明](https://github.com/hakupao/sdtm-pedia/blob/main/DISCLAIMER.md).

## 2. 构建过程

7 阶段流水线. 每个阶段都有独立的 plan / 执行日志 / 验证记录, 放在仓库 [`.work/`](https://github.com/hakupao/sdtm-pedia/tree/main/.work) 目录里 — 是源代码的一部分, 不是另起一份文档站.

| 阶段 | 做了什么 | 主要产出 |
|---|---|---|
| 1 | Python 把 xlsx 转 Markdown | 63 份 `spec.md` + terminology |
| 2 | PDF 页码索引 (程序化, 非视觉) | `page_index.json` |
| 3 | AI 辅助 PDF 抽取, 分 11 批 | 每个域的 `assumptions.md` + `examples.md` |
| 4 | 补充内容抽取 | 6 份 model + 6 份 chapter |
| 5 | 全量校验 + 主索引 | `INDEX.md` + 验证报告 |
| 6 | 检索优化 (路由 + 反向索引) | `ROUTING.md` + `VARIABLE_INDEX.md` (1,523 变量) |
| 6.5 | AI 平台部署 | 4 平台发布包 |

另有一条**字面级深度验证**作为长跑独立 track 持续推进. 它把知识库里每一条原子事实跟 PDF 逐页比对. 截至 2026-04-29, 覆盖范围内 **97% 页码已验证完成**, 审计仍在进行. 每批审计报告在 [`.work/06_deep_verification/evidence/checkpoints/`](https://github.com/hakupao/sdtm-pedia/tree/main/.work/06_deep_verification/evidence/checkpoints).

## 3. 可追溯性 — 任何一条答案怎么自己核

仓库结构刻意做成"读到一条答案 → 几秒内能找到原始 PDF 页"这样的形态. 没有"信我"那一层.

**核一条域级答案:**

1. 记下答案里的域代码 (`AE` / `LB` / `DM` 等).
2. 打开 `knowledge_base/domains/<DOMAIN>/`:
   - `spec.md` — 变量级 spec (源自 xlsx, 含 Core / type / codelist 绑定)
   - `assumptions.md` — 域内业务规则 (源自 PDF)
   - `examples.md` — 实施示例 (源自 PDF)
3. 文件头部都标了对应 PDF 页码区间. 拿 SDTMIG v3.4 PDF 对照即可.
4. 变量的 Core / codelist 绑定, 有 SDTMIG xlsx 的话直接对照.

**核章节级答案**: 打开 `knowledge_base/chapters/chXX_*.md`. 页码区间和小节号跟 PDF 目录直接对应.

**核术语答案**: `knowledge_base/terminology/` 每份 codelist 都标了 CDISC C-code (例如 `C66731`), 可以拿到 NCI EVS Browser 反查.

完整的 source-to-output 映射表在仓库 [`docs/TRACEABILITY.md`](https://github.com/hakupao/sdtm-pedia/blob/main/docs/TRACEABILITY.md).

## 4. 验证与已知问题

校验阶段抓到过两个系统性问题, 都已公开存档. 不藏 — 因为这两个发现是"验证流程在真起作用"最有力的证据.

### Issue 1 — 页码索引偏移 (2026-04-15, 已解决)

第一次做 PDF 图像/图表索引时, 让 AI agent 视觉识别页码. 领域专家抽检发现 TD example 页码偏了 4 页, 类似的 ±2–4 页偏移在大约 60 张图上都有.

**根因**: AI 看 PDF 时其实没法准确观测页边界, 它在估算. 流程当时没有区分"精确值"和"估算值".

**修复**: 页码索引重构为程序化生成, `page_index.json` 成为唯一权威源, 所有下游文件统一引用; AI 给出的页码估算值现在显式标 `(estimated)`, 不再直接写进权威索引.

完整调查: [`.work/03_verification/issue1_investigation.md`](https://github.com/hakupao/sdtm-pedia/blob/main/.work/03_verification/issue1_investigation.md).

### Issue 2 — 骨架内容被判 PASS (2026-04-15, 已解决)

`ch04_general_assumptions.md` 第一轮校验时被判 PASS, 但其中约 30% 的小节只有 1–2 句占位文字加 `<!-- 待补全 -->` 标记. PDF 这一章是 38 页详细规则; 当时文件每页约 9 行, 修复后每页约 17 行.

**根因**: PASS 标准把 *"缺失内容已经清楚标了出来"* 等同于 *"内容已完整"*. 此外, 同一个 agent 既写又审 — 没有独立 reviewer 去读 PDF.

**修复**: 所有被标记的小节按 PDF 重写. PASS 标准改成定量: 行数/页数比值要达到基线, 零占位标记, 要点覆盖率 ≥95%. 从此往后, 写一个文件的 agent 不能是审同一个文件的 context.

完整记录: [`.work/03_verification/issues_found.md`](https://github.com/hakupao/sdtm-pedia/blob/main/.work/03_verification/issues_found.md).

### 已知边界

有些限制无法在 AI 平台部署形态内彻底解决 (大型 codelist 以 stub 形式保存 / 实时外部查询无法内嵌等). 这些单独跟踪在: [已知限制](./known-limitations/).

## 5. 独立复核机制

上面两个 issue 沉淀出 4 条常驻规则. 仓库每个阶段每条 track 都强制执行.

1. **定量 PASS 标准.** 覆盖率, 行数/页数比, 零占位标记 — 不再用"看起来对"这种主观判断.
2. **写者和审者必须分开.** 写一个文件的 agent / 进程, 不能是审它的那个. Reviewer 独立读 PDF, 输出结构化覆盖率报告.
3. **AI 估算值必须标注.** 凡是 AI 没法程序化确认的数字, 标 `(estimated)`, 不直接写进权威索引.
4. **人工抽检是流程的一部分.** 每个阶段收尾都做一次随机抽样核对 PDF — 不是最后才补的兜底.

4 条规则和它们对应的失败案例完整记录在 [`.work/meta/retrospective.md`](https://github.com/hakupao/sdtm-pedia/blob/main/.work/meta/retrospective.md).

另外, 验证 track 本身是迭代的 — §2 提到的深度验证审计写这段时已经走到第 14 轮, 每一轮都有归档, 发现的差异回推到知识库.

## 6. 这对你意味着什么

- **质疑是欢迎的.** 几秒钟就能定位到源页; 觉得哪个数对不上, 直接对 PDF 验证.
- **发现差异请反馈.** 深度验证如果漏了什么, 欢迎在 [GitHub issue](https://github.com/hakupao/sdtm-pedia/issues) 提. 审计 track 是开放的.
- **不能替代法规提交.** 这份知识库是给工程师/程序员/审核员日常 SDTM 工作用的辅助参考. 法规提交场景, 始终以 CDISC 官方发布为准.

---

**仓库:** [github.com/hakupao/sdtm-pedia](https://github.com/hakupao/sdtm-pedia) · **许可证:** CC BY 4.0
