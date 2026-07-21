# Q_sanity_2 — Gemini SDTM Expert 回答

> 题: LBNRIND 的 submission values 有哪些?
> 期望: HIGH / LOW / NORMAL / ABNORMAL (C78736); 若返 "H/N/L" 单字符说明 v5 CO-2 subclause 被改, 停 smoke
> 对话 URL: https://gemini.google.com/u/1/gem/3b572e310813/ebdda037c7b15d34
> 时间: 2026-04-22
> 账号: bojiang.zhang.0904@gmail.com (Pro)
> Mode: Pro

## 完整回答

根据 CDISC CT 官方标准以及本 Gem (v5 N5.2) 的边界子条款约束，LB.LBNRIND (Reference Range Indicator) 的官方 Submission Values 必须是全写单词，最常见的值包括：

ABNORMAL

HIGH

LOW

NORMAL

⚠️ 关键业务规则 (CO-2 边界条款)：
在映射或生成 SDTM 实例数据时，严禁使用单字符缩写 (如 H / L / N)。必须使用上述 CDISC 官方的完整全拼 Submission Value。

关于完整 Term 列表查询：
LBNRIND 绑定的 Controlled Terminology Code 为 C78736 (Reference Indicator)。根据本 Gem 不 inline 完整字典的策略，如果您需要查看 C78736 下包含的其他所有合法值（例如边界值指标），请前往 NCI EVS Browser 进行查询：
🔗 https://evsexplore.semantics.cancer.gov/evsexplore/ 搜索 C78736。

源路径:

knowledge_base/domains/LB/spec.md §LBNRIND (变量定义)

Gem Custom Instructions CO-2 子条款 (LBNRIND 全写硬锚)

## Verdict

**PASS** — 全写 ABNORMAL/HIGH/LOW/NORMAL 4 值完全命中期望; CO-2 子条款显式禁 H/L/N 单字符; C78736 CT code 正确引用; Gem 字典查询边界策略诚实说明. v5 CO-2 subclause 未回归.
