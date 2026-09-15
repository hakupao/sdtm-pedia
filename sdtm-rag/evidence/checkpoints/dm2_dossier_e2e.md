# DM2 — L3 e2e (2026-09-15)

## §0 判据 (跑前登记)

> 本文件在**任何一次跑之前**提交 (commit `docs(rag): DM2 T9 e2e 判据预登记 (跑前)`).
> 判分由**异 subagent** (opus, 不看本 session) 做, 结果写 §2; §1/§2 跑前为空.

题: 3 题 × 模型: 2 个 = **N=6**.

| id | 域 | 语言 / 域的给出方式 | 问题原文 |
|----|----|--------------------|----------|
| dm01 | DS | zh, 小写码 `ds` (用户原句, 逐字保留) | 本研究中，哪些数据适合进入 sdtm 的 ds domain？ |
| dm02 | DS | ja, 大写码 `DS` | この試験で収集しているデータのうち、SDTM の DS ドメインに入れるべきものはどれですか？ |
| dm05 | AE | en, 小写码 `ae` | In our study, which collected data items belong in the ae domain? |

模型: `opus-5`, `sonnet-5` (两者均走 `/api/ask_stream`, `dossier:"auto"`, `history:[]`).

**每题 PASS = 三条全过**:

① **定义齐**: 按域定义列出全部记录类别 (DS: 3 类, 即 `DISPOSITION EVENT` / `PROTOCOL MILESTONE` / `OTHER EVENT`; AE: 见 `knowledge_base/domains/AE/assumptions.md` item_1).

② **候选齐**: gold 4 卡 ≥ 3 张被点名 (表单 OID + 项目 OID 原样); 额外点名的 OID 全部在一览中存在 (零捏造, 用 `check_code_grounding` 码闸 + 一览 grep).

③ **标推测**: 每条归属带 推測/inference 标记; 明说无候选的类别.

**目标 ≥ 5/6 PASS**.

判分 = 异 subagent (opus, 不看本 session), 每题独立报告写 §2.

**成本**: 每题记 `usage.prompt_tokens` / `usage.completion_tokens` / 是否 cache 命中 (Bedrock 返回 `cache_read_input_tokens` 时).

**失败处置**: 若 < 5/6, 归档 `evidence/failures/dm2_task9_attempt_1.md`; 只允许改 `_DOSSIER_RULES` 的**规则层**措辞 (模式级), 不许加题面 example; 改后重跑 6 题**全部** (不只失败题).

gold 卡 basename 与一览文本仅在 gitignored runs/ 目录, 判分 agent 读那里。
