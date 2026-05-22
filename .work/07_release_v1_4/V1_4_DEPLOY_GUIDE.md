# V1.4 Deploy Guide (4-Platform, Gemini MAINTAINED_NO_SANITY)

> **Release**: v1.4 (planned tag `v1.4-company-release`)
> **Date**: 2026-05-22 draft
> **Predecessor**: v1.3-company-release (KB pass + 4-platform rebuild)
> **Status**: 🟡 Phase C — C4 + 3-platform rebuild done; C1 done (with v1.5 carry); C2 in flight; Gemini optimization 增补
> **Scope**: 4 平台 deliverable (ChatGPT GPTs + Claude Projects + NotebookLM + Gemini Gems), 其中 **Gemini 测试不继续** (优化继续, 用户自验)

---

## ⚠️ TOP NOTICE — Gemini Gems 部署须知

**Self-deploy 用户**: v1.4 起本项目**继续维护** Gemini Gem prompt + KB delta, 但**不再跑 sanity / R4 回归测试**.

- ✅ **可以继续用**: v1.4 提供 Gemini gem 增量 (Method label anchor + 5 essential rules + clean rewrite)
- ⚠️ **无 sanity 覆盖**: v1.4 起 Gemini 答题正确性**用户自验**, 不再有本项目的 cross-platform 矩阵保证
- 📌 **替代选项 (推荐)**: ChatGPT GPTs / Claude Projects / NotebookLM 三家本 release 仍有完整 sanity 覆盖 (B1 12/12 PASS)

### 0. v1.4 changes 总览 (vs v1.3)

| 平台 | 变更 | 用户操作 |
|---|---|---|
| **ChatGPT GPTs** | system_prompt v3 clean rewrite (120→119L + Method label anchor mapping) + KB `PP/examples.md §6.3.5.9.3` 加显式 mapping table + 04_examples_data.md bundle rebuild | ① 替换 GPT custom instructions (复制 `release/v1.4/self_deploy/chatgpt/system_prompt.md`) ② 重新上传 4 个 bundle 文件 |
| **Claude Projects** | system_prompt v3 clean rewrite (125→133L) + Files A-S table 保留 + bundle pipeline architectural fix (`## §N.N.N` capture) + 09_examples_data_high rebuild | ① 替换 Project system prompt ② 重新上传 19 个文件 (按 Files A-S table) |
| **NotebookLM** | instructions v3 clean rewrite (157→156L footer Sources 语义等价) + bucket 16 PP 文件 rebuild (含 Method label anchor) | ① 替换 custom instructions ② 重新上传 bucket 16 文件 |
| **Gemini Gems** | system_prompt v9 clean rewrite + Method label anchor (Phase A + 2026-05-22 增补) | 替换 Gem instructions (复制 `release/v1.4/self_deploy/gemini/system_prompt.md`). **本平台无 sanity 测试覆盖**, 用户自验. |

---

## 1. ChatGPT GPTs 部署

(详细步骤参考 v1.3 V1_3_DEPLOY_GUIDE.md §1 — 流程相同, 仅 system_prompt + 04_examples_data.md 内容变了)

**v1.4 specific 变更点**:
- system_prompt 必须替换 (v3 clean rewrite, 移除 v1.0-v1.3 迭代注释)
- 04_examples_data.md 重新上传 (PP/examples §6.3.5.9.3 Method label mapping table 已落 KB, 经 rebuild 进入 bundle)

**Sanity 验证 (用户自检)**:
- 问: "Explain the PP RELREC Method A/B/C/D label assignments."
- 期望: ChatGPT 列出 A=Many-to-Many (PCGRPID/PPGRPID), B=One-to-Many (PCSEQ/PPGRPID), C=Many-to-One (PCGRPID/PPSEQ), D=One-to-One (PCSEQ/PPSEQ). 不允许 label drift.

---

## 2. Claude Projects 部署

(详细步骤参考 v1.3 V1_3_DEPLOY_GUIDE.md §2 — 19 文件 Files A-S table 不变, 仅 09_examples_data_high.md 内容变了)

**v1.4 specific 变更点**:
- system_prompt v3 clean rewrite (含 5 essential rules + regex-gated CO-N)
- 09_examples_data_high.md 重新上传 (`## §N.N.N` capture pipeline fix 已应用, Quick Reference 段进入 bundle)

**Sanity 验证**:
- 问: "Where is the PP RELREC Method Quick Reference table?"
- 期望: Claude 引用 09_examples_data_high.md 中的 §6.3.5.9.3 段 + Method A/B/C/D mapping byte-aligned KB.

---

## 3. NotebookLM 部署 (★ v1.4 加强教程)

(整体流程参考 v1.3 V1_3_DEPLOY_GUIDE.md §3)

### 3.A. 旧 source 清理 (CRITICAL — 不删会造成 stale citation)

> **⚠️ 红色警告**: NotebookLM 不会自动 deduplicate. 上传新 source 后, **如不手动删除对应旧 source, 会留 stale 引用**.

#### 3.A.1. bucket 25 命名变更回顾

| Release | bucket 25 文件名 | 内容差异 |
|---|---|---|
| v1.0 - v1.2 | `25_td_meta_ti_ts_oi.md` | TD/META/TI/TS/OI 5 文件 |
| v1.1 onwards | `25_td_meta_ti_ts_oi_di.md` | 加 DI domain (06 deep verification phase 6 new domain) |

> 自 v1.1 起 bucket 25 已含 DI; v1.4 内容**继续含 DI** (Method label anchor 不影响 bucket 25). 但用户实操中常漏删旧 source — v1.4 强化提示.

#### 3.A.2. 操作步骤 (UI walkthrough)

**Step 1**: 打开 NotebookLM, 进入您的 SDTM Pedia notebook.

**Step 2**: 上传新 bucket 文件 (`release/v1.4/self_deploy/notebooklm/uploads/25_td_meta_ti_ts_oi_di.md`).

**Step 3**: ★ **必须**: 在左侧 Sources panel 找到旧 `25_td_meta_ti_ts_oi.md`:
- 鼠标 hover 文件名 → 出现 `⋮` (三点菜单) → 点击 → 选择 "Delete" 或 "Remove from notebook".
- 确认删除.

**Step 4**: 检查 sources 计数:
- v1.4 NotebookLM bundle 共 **42 个 source** (不是 43).
- 如显示 43, 说明旧 `25_td_meta_ti_ts_oi.md` 未删 → 回 Step 3.

#### 3.A.3. Screenshot 教程 [TODO]

> **[Phase C C3 carry-over]** Screenshot 教程图待加入:
> - `screenshots/nbm_source_list.png` — sources panel 显示 43 vs 42 对比
> - `screenshots/nbm_delete_button.png` — `⋮` 菜单 → Delete 操作
> - 由 Chrome MCP 截图 (需用户协作打开 NotebookLM 登录态)

### 3.B. v1.4 specific 变更点

- `instructions.md` v3 clean rewrite (157→156L footer Sources citation 语义等价保留)
- bucket 16 (含 PP/PC/RELREC) 重新上传 (Method label anchor mapping table 已落 KB, 经 rebuild 进入 bucket 16)
- 其他 bucket 0-15, 17-24 byte-identical 继承 v1.3 (不需重传, 但全量重传也无害)

### 3.C. Sanity 验证

- 问: "List the four PP RELREC Methods and the IDVAR pairs."
- 期望: NotebookLM 答 A/B/C/D + (PCGRPID,PPGRPID) / (PCSEQ,PPGRPID) / (PCGRPID,PPSEQ) / (PCSEQ,PPSEQ) + footer Sources cite bucket 16.

---

## 4. Phase C 收尾验证 (post-rebuild Q-S2 复测)

C4 KB anchor + 3-platform rebuild 完成后, 跑 Q-S2 (PP RELREC Method A/B/C/D) × 3 平台 sanity 复测 (Chrome MCP fire-and-forget):

- ChatGPT v3: 期望 PASS+ (Method labels byte-aligned KB)
- Claude v3: 期望 PASS+ (extended thinking 取 09 bundle Quick Reference)
- NotebookLM v3: 期望 PASS+ (bucket 16 RAG-native + footer cite)

如 3/3 PASS → C4 + rebuild 闭合, 进 Phase D release cut.
如 ≤2/3 → 回溯 root cause (KB / bundle / prompt 哪层 mismatch).

---

## 5. 已知限制 (carry from v1.3, 详 KNOWN_LIMITATIONS.{en,zh,ja}.md §0)

- Tier B 156 节 (排名 1-10 + 21-25 + level-2 24 节) 仍 defer v1.5
- 437 UNSOURCED_MANUAL 全量分类 defer v1.5 (v1.4 仅启发式 fix + N=80 抽检)
- Gemini Gems 平台 MAINTAINED_NO_SANITY_TEST (维护但不测试; 详 §0.A 顶部 NOTICE; 用户自验)

---

**Updated**: 2026-05-22 Phase C draft
**Next**: Phase D 阶段把此文 promote 到 `release/v1.4/V1_4_DEPLOY_GUIDE.md` (或 self_deploy/ 各平台子文档拆分)
