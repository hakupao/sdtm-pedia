# v1.3 部署指南 — 4 平台更新步骤

> Date: 2026-05-20
> 范围: v1.2 LIVE → v1.3 KB pass 更新
> 注: v1.3 release tag 尚未 cut (待 Phase D), 本指南可先在用户 GPT/Gem/Project/Notebook 实例上 dry-run 部署

---

## 速览 — 哪些动了

| 平台 | uploads 改 | system_prompt / instructions 改 |
|---|---|---|
| **ChatGPT (GPTs)** | 3 / 9 文件 | 不变 |
| **Gemini (Gems)** | 3 / 3 文件 (全改) | 不变 |
| **Claude (Projects)** | 5 / 19 文件 | 不变 |
| **NotebookLM** | 7 改 + 1 改名 / 42 buckets | **改了** (citation style refactor) |

---

## 1. ChatGPT (GPTs)

**部署 UI**: https://chat.openai.com/gpts → "我的 GPT" → 找到你的 SDTM Pedia GPT → "Configure" → "Knowledge"

**本地源文件路径**:
```
/Users/bojiangzhang/MyProject/sdtm-pedia/ai_platforms/chatgpt_gpt/current/uploads/
```

**操作步骤**:
1. 打开 ChatGPT GPT Builder, 进入你的 SDTM Pedia GPT → Configure tab → Knowledge section
2. **删除** 旧的 3 个文件 (点文件旁的 ✕):
   - `04_domain_specs_all.md`
   - `05_domain_assumptions_all.md`
   - `06_domain_examples_all.md`
3. **上传** 新的 3 个文件 (Upload files → 选下面 3 个):
   - `ai_platforms/chatgpt_gpt/current/uploads/04_domain_specs_all.md` (+284 bytes vs v1.2)
   - `ai_platforms/chatgpt_gpt/current/uploads/05_domain_assumptions_all.md` (+333 bytes)
   - `ai_platforms/chatgpt_gpt/current/uploads/06_domain_examples_all.md` (+5,432 bytes)
4. **不动** 的 6 文件 (跳过): `01_navigation.md` · `02_chapters_all.md` · `03_model_all.md` · `07_terminology_core_high_freq.md` · `08_terminology_quest_and_supp.md` · `09_terminology_core_mid_tail.md`
5. **Instructions** 段不动 (v8.1 prompt 没改)
6. Save → 在 chat 区跑一个 sanity 题 (e.g., "BECAT 有哪些 sponsor-extensible 值?") 验证新内容已生效

---

## 2. Gemini (Gems)

**部署 UI**: https://gemini.google.com → "Gems" → 左侧 Gem Manager → 找到你的 SDTM Pedia Gem → "Edit"

**本地源文件路径**:
```
/Users/bojiangzhang/MyProject/sdtm-pedia/ai_platforms/gemini_gems/current/uploads/
```

**操作步骤**:
1. 打开 Gemini 网站 → Gem Manager → 你的 SDTM Pedia Gem → Edit
2. **Knowledge** (Files) 段: **删除** 3 个旧文件:
   - `01_navigation_and_quick_reference.md`
   - `02_domains_spec_and_assumptions.md`
   - `03_domains_examples.md`
3. **上传** 3 个新文件 (Add files):
   - `ai_platforms/gemini_gems/current/uploads/01_navigation_and_quick_reference.md` (+3,103)
   - `ai_platforms/gemini_gems/current/uploads/02_domains_spec_and_assumptions.md` (+617)
   - `ai_platforms/gemini_gems/current/uploads/03_domains_examples.md` (+5,432)
4. **Instructions** 段不动 (v8.1 LIVE, v1.2 已 promoted, v1.3 没动)
5. Update Gem → 跑 sanity 题验证 (e.g., "PP RELREC Method C 在 PDF 哪页?")

**注意**: Gemini Gem Files 上限有限 (~10 文件 / ~100MB), 3 文件全替换是常规操作.

---

## 3. Claude Projects

**部署 UI**: https://claude.ai → 你的 Project → "Project knowledge" 段

**本地源文件路径**:
```
/Users/bojiangzhang/MyProject/sdtm-pedia/ai_platforms/claude_projects/current/uploads/
```

**操作步骤**:
1. 打开 Claude 网站 → 左侧 sidebar 你的 SDTM Pedia Project
2. **Project knowledge** 段右上角 "Add content" / 文件列表区
3. **删除** 5 个旧文件 (找到文件 → ⋯ → Delete):
   - `02_chapters.md`
   - `03_model.md`
   - `06_assumptions.md`
   - `09_examples_data_high.md`
   - `10_examples_data_others.md`
4. **上传** 5 个新文件 (Add content → Upload):
   - `ai_platforms/claude_projects/current/uploads/02_chapters.md` (+2,581)
   - `ai_platforms/claude_projects/current/uploads/03_model.md` (+522)
   - `ai_platforms/claude_projects/current/uploads/06_assumptions.md` (+220)
   - `ai_platforms/claude_projects/current/uploads/09_examples_data_high.md` (+592)
   - `ai_platforms/claude_projects/current/uploads/10_examples_data_others.md` (+142)
5. **不动** 14 文件: `00_routing.md`, `01_index.md`, `04_variable_index.md`, `05_mega_spec.md`, `07_examples_catalog.md`, `08_terminology_map.md`, `11a/11b/11c/12a/12b/12c/13a/13c_terminology_*.md`
6. **Custom instructions / Project knowledge instructions** 段不动 (v2.6 LIVE 没改)
7. Project 自动 re-index → 跑 sanity 题验证

---

## 4. NotebookLM

**部署 UI**: https://notebooklm.google.com → 你的 SDTM Pedia Notebook → "Sources" panel (左侧)

**本地源文件路径**:
```
/Users/bojiangzhang/MyProject/sdtm-pedia/ai_platforms/notebooklm/current/uploads/        ← 42 bucket md files
/Users/bojiangzhang/MyProject/sdtm-pedia/ai_platforms/notebooklm/current/instructions.md ← citation style 改
```

**操作步骤**:

### 4.1 改 instructions (citation style refactor)

NotebookLM 没有原生 "system prompt" 字段, instructions 由用户在每次 query 时引用. v1.3 instructions.md 的变化是 **写作风格 reference doc**, 实际部署方式:

选项 A (推荐 — 注入 Notebook Note):
1. NotebookLM 左侧 Sources → 找一个 "instructions" / "system prompt" 的 source bucket (你之前可能加过) — 删掉
2. 上传新的 `ai_platforms/notebooklm/current/instructions.md` 作为新 source
3. 命名: "00_instructions.md" 让它排在 Sources 列表顶端

选项 B (不上传, 仅 user-side memo):
- 你自己看 `instructions.md`, 在每次 query 前 prefix "请按 instructions.md citation style 答" — 但不可靠
- 不推荐

### 4.2 改 7 个 bucket + 1 个改名

**改 7 个 bucket** (删旧 + 加新):
| Bucket | 文件路径 | Delta |
|---|---|:-:|
| 10_ev_history_mh_ho_be.md | `ai_platforms/notebooklm/current/uploads/10_ev_history_mh_ho_be.md` | +284 |
| 16_fnd_pharma_pc_pp.md | `.../16_fnd_pharma_pc_pp.md` | +2,620 |
| 23_td_arms_ta_tv.md | `.../23_td_arms_ta_tv.md` | +2,812 |
| 24_td_elements_te_tm_td.md | `.../24_td_elements_te_tm_td.md` | +333 |
| 28_ig_ch01_ch02_ch03.md | `.../28_ig_ch01_ch02_ch03.md` | +2,581 |
| 31_model_obs_classes.md | `.../31_model_obs_classes.md` | +327 |
| 32_model_concepts_study_rel.md | `.../32_model_concepts_study_rel.md` | +195 |

操作 each: NotebookLM Sources → 找旧 source → ⋯ → Delete → "Add source" → upload 新文件

**关键: bucket 25 改名**:
| Old (删) | New (加) |
|---|---|
| `25_td_meta_ti_ts_oi.md` | `25_td_meta_ti_ts_oi_di.md` (含 DI) |

操作:
- 在 NotebookLM Sources 找 `25_td_meta_ti_ts_oi.md` → ⋯ → Delete
- "Add source" → 上传 `ai_platforms/notebooklm/current/uploads/25_td_meta_ti_ts_oi_di.md`
- 验证 source 列表显示新名 + 包含 DI domain

### 4.3 不动的 35 个 bucket

跳过, 保持原状.

### 4.4 验证

- Notebook 自动 re-index (~30s)
- 跑 sanity 题: e.g., "DI 域有哪些变量?" — 应能命中 bucket 25 (新名), 答出 DI 是 Device Identifiers (SDTMIG-MD)
- 引用风格应是 footer "Sources: 25_td_meta_ti_ts_oi_di.md, ..." (新 instructions citation style)

---

## 5. 部署完成后

### 5.1 用户 sanity 题 (4 平台各 1-2 个, 验 v1.3 KB 改动生效)

| 题 | 期望命中 | 用于 |
|---|---|---|
| "BECAT 哪些值是 sponsor-extensible?" | EXTRACTION (per A2 v1.3 fix) | 4 平台 |
| "PP 域如何与 PC 通过 RELREC 关联? 列 4 种 Method." | Method A/B/C/D + relrec.xpt 示例 (A1 v1.3) | 4 平台 |
| "TRSTRESN 还是 TRSTRESU 是标准化单位?" | TRSTRESU (A3 §6.3.12.2 typo fix) | 4 平台 |
| "DI 域属于哪个 SDTM dataset class?" | Study Reference / SDTMIG-MD | NotebookLM bucket 25 重点 |

### 5.2 回滚步骤 (如发现 regression)

baseline 在: `.work/07_release_v1_3/backups/` (4 platform 子目录 × 25.5 MB).

如果 v1.3 部署后某平台答题质量下降:
1. 各平台 UI 重 upload `backups/<platform>_uploads/*.md` (覆盖 v1.3 新文件)
2. NotebookLM: 删除 v1.3 重命名的 `25_td_meta_ti_ts_oi_di.md` source → 重新上传 baseline `25_td_meta_ti_ts_oi.md`
3. 记 finding 在 `.work/07_release_v1_3/evidence/failures/`

---

## 6. 我能帮你的

需要时告诉我:
- "把 4 平台 sanity 题 paste 给我", 我从 SMOKE_V4.md 选 3-5 题给你直接复制到 ChatGPT/Gemini/Claude/NotebookLM 跑
- "做 Phase C R4 17 题 Pro 回归", 我用 Chrome MCP 自动化 Gemini 跑
- "verify XX 文件在新 bundle 里", 我 grep 验证

---

## 7. Phase 后续

部署完成 (本指南操作) 后:
- **Phase C** — R4 sanity / 17 题 回归 (验答案质量)
- **Phase D** — cut release/v1.3/ tag v1.3-company-release (官方 release artifact)
- **Phase E** — Post-audit pass
- **Phase F** — RETROSPECTIVE + commit + push
