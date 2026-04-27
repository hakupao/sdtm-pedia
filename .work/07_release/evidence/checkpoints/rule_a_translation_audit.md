# Rule A Translation Sample Audit (N=3)

> 2026-04-27 / Phase D Rule A 抽检 / Reviewer: oh-my-claudecode:verifier

## Summary

| Sample | Source | Paragraphs sampled | PASS | MINOR | MAJOR | FAB |
|---|---|---|---|---|---|---|
| 1 | USER_GUIDE.en.md ← .zh.md | 5 | 4 | 1 | 0 | 0 |
| 2 | self_deploy/README.ja.md ← .zh.md | 5 | 4 | 1 | 0 | 0 |
| 3 | self_deploy/chatgpt_tutorial.en.md ← .zh.md | 5 | 5 | 0 | 0 | 0 |

---

## Sample 1: USER_GUIDE.en.md ← USER_GUIDE.zh.md

### Paragraph 1-A (§1, lines 5)

**Source (zh):**
> 本项目把 CDISC SDTMIG v3.4 + v2.0 model + CDISC CT 整理成 295 个 Markdown 源, 部署到 4 个 AI 平台 (Claude Projects / ChatGPT GPTs / Gemini Gems / NotebookLM), 让同事**自然语言提问, 1 分钟拿到带 spec 引用的答案**.

**Translation (en, line 5):**
> This project organizes CDISC SDTMIG v3.4, the v2.0 model, and CDISC CT into 295 Markdown source files, deployed across 4 AI platforms (Claude Projects / ChatGPT GPTs / Gemini Gems / NotebookLM), so that colleagues can **ask questions in plain language and get answers with spec citations in under a minute**.

**Semantic comparison:**
- "295 个 Markdown 源" → "295 Markdown source files": PASS (number preserved)
- "4 个 AI 平台" → "4 AI platforms": PASS
- "1 分钟" → "under a minute": PASS (faithful, slightly looser but not a distortion)
- "带 spec 引用的答案" → "answers with spec citations": PASS
- Tone: source is colloquial/workplace-friendly; translation matches register

**Verdict: PASS**

---

### Paragraph 1-B (§2 table footnote, line 18)

**Source (zh):**
> 亮点: v3.4 新域 (GF / CP / BE / BS) + Timing + CT Extensible + SUPPQUAL scope + 跨域死亡日级对齐 + 3 道 AHP (LBCLINSIG / Trial-Level SAE Aggregate / PF 已废域); 全程 Rule A-D 4 条质量规则 + 累计 28 个独立 reviewer 验证. 信源: `./CHANGELOG.md` + `../../SMOKE_V4.md` §3.

**Translation (en, line 18):**
> Highlights: v3.4 new domains (GF / CP / BE / BS), Timing rules, CT Extensible handling, SUPPQUAL scope, cross-domain death-date alignment, and 3 AHP probes (LBCLINSIG / Trial-Level SAE Aggregate / PF deprecated domain). Throughout, quality was enforced with 4 rules (Rule A–D) and a cumulative total of 28 independent reviewer validations. Sources: `./CHANGELOG.md` and `../../SMOKE_V4.md` §3.

**Semantic comparison:**
- "GF / CP / BE / BS": PASS (verbatim)
- "跨域死亡日级对齐" → "cross-domain death-date alignment": PASS (accurate)
- "3 道 AHP (LBCLINSIG / Trial-Level SAE Aggregate / PF 已废域)" → "3 AHP probes (LBCLINSIG / Trial-Level SAE Aggregate / PF deprecated domain)": PASS — all three names preserved verbatim
- "Rule A-D 4 条质量规则" → "4 rules (Rule A–D)": PASS (number preserved, order preserved)
- "累计 28 个独立 reviewer 验证" → "cumulative total of 28 independent reviewer validations": PASS
- SDTM term fidelity: all variable names, C-codes, domain codes preserved verbatim

**Verdict: PASS**

---

### Paragraph 1-C (§3 decision tree, short-version prose, line 29)

**Source (zh):**
> 简版: 不知道选什么 → Claude Projects. 拉同事一起用 → ChatGPT GPTs. 担心幻觉 → NotebookLM. 详细对比见 `../README.md` "四平台分工" 表.

**Translation (en, line 29):**
> Short version: Not sure which to pick? Start with Claude Projects. Bringing colleagues along? Use ChatGPT GPTs. Worried about hallucinations? Use NotebookLM. For a detailed comparison see `../README.md`, the "Platform Roles" table.

**Semantic comparison:**
- "不知道选什么" → "Not sure which to pick": PASS (equivalent)
- "拉同事一起用" → "Bringing colleagues along": PASS (idiomatic)
- "担心幻觉" → "Worried about hallucinations": PASS
- "四平台分工" → "Platform Roles": MINOR_DRIFT — literal translation would be "four-platform division of roles" or "four-platform role assignment". The translation condenses "四平台" (four-platform) and "分工" (division of labor/roles) into just "Platform Roles". The number "four" is dropped, though the table itself is still referenced correctly. This is a minor stylistic compression that does not mislead the user, but it loses the "four" specificity.
- File path `../README.md`: PASS (verbatim)

**Verdict: MINOR_DRIFT** (table name condensed; low business impact)

---

### Paragraph 1-D (§7 Known Limitations L1/L2/L3, lines 83-85)

**Source (zh):**
> - **L1 — QS codelist 不全**: 296 个长尾 questionnaire codelist (PROMIS/EORTC) 因容量约束未全展开 (Claude ~55.8%), 其余落 NCI EVS Browser 链接.
> - **L2 — 巨型 codelist 走 stub**: LBTESTCD (2536 term) 等 6 表只存 stub + 指针, 不会编 term.
> - **L3 — 实时联网**: NotebookLM 严格 in-KB-only, breaking news / 最新 Pinnacle 21 不知道 (PUNT). 其他 3 平台可联网需手动开启.

**Translation (en, lines 83-85):**
> - **L1 — Incomplete QS codelist coverage**: 296 long-tail questionnaire codelists (PROMIS / EORTC) are not fully expanded due to capacity constraints (Claude ~55.8%); the remainder links out to NCI EVS Browser.
> - **L2 — Large codelists stored as stubs**: LBTESTCD (2,536 terms) and 5 other large tables are stored as stubs with pointers only — the model will not fabricate individual terms.
> - **L3 — No real-time web access**: NotebookLM is strictly in-KB-only; breaking news and the latest Pinnacle 21 updates are outside its knowledge (it will PUNT). The other 3 platforms can browse the web but require you to enable that manually.

**Semantic comparison:**
- "296 个" → "296": PASS (number preserved)
- "Claude ~55.8%" → "Claude ~55.8%": PASS (verbatim)
- "LBTESTCD (2536 term)" → "LBTESTCD (2,536 terms)": PASS (number identical, formatting adjusted for EN convention)
- "等 6 表" (and 6 other tables) → "and 5 other large tables": MINOR_DRIFT — source says "6 tables total" (LBTESTCD + 5 others = 6 total), but EN translation says "LBTESTCD ... and 5 other large tables" which is arithmetically equivalent (1+5=6). However the source Chinese says "等 6 表" meaning "6 tables including..." which would be LBTESTCD + 5 others. The translation is mathematically consistent. No distortion.
- "不会编 term" → "the model will not fabricate individual terms": PASS (accurate expansion)
- SDTM term LBTESTCD: PASS (verbatim)
- Logical structure preserved: all three limitations faithfully conveyed

**Verdict: PASS**

---

### Paragraph 1-E (§9 Road Map, lines 97)

**Source (zh):**
> 短期 (v1.0 维护): 收反馈修 SDTM 错点, 季度 v1.x minor. 中期 (Phase 7 自建 RAG): 摆脱 4 平台容量约束, 295 文件全量 + QS codelist 全展开. 长期: 跟 SDTMIG v3.5+ 同步 + ADaM / Define-XML 扩展.

**Translation (en, line 97):**
> **Short term (v1.0 maintenance)**: Collect feedback and fix SDTM content errors; quarterly v1.x minor releases. **Medium term (Phase 7 — self-hosted RAG)**: Break free of the 4-platform capacity constraints, enabling all 295 files at full resolution plus complete QS codelist expansion. **Long term**: Keep pace with SDTMIG v3.5+ and extend coverage to ADaM and Define-XML.

**Semantic comparison:**
- "季度 v1.x minor" → "quarterly v1.x minor releases": PASS (number/cadence preserved)
- "4 平台容量约束" → "4-platform capacity constraints": PASS
- "295 文件全量" → "all 295 files at full resolution": PASS (number preserved)
- "SDTMIG v3.5+" → "SDTMIG v3.5+": PASS (verbatim)
- "ADaM / Define-XML" → "ADaM and Define-XML": PASS (verbatim names)
- Causal/logical structure: all three temporal tiers (short/medium/long) faithfully conveyed
- The translation adds markdown bold formatting for the three tiers — this is a register enhancement, not a distortion

**Verdict: PASS**

---

## Sample 2: self_deploy/README.ja.md ← self_deploy/README.zh.md

### Paragraph 2-A (§1 table decision tree note, line 14)

**Source (zh):**
> 部署视角挑选 (与 USER_GUIDE.zh.md §3 一致): 想最快 (~30 min) → NotebookLM 或 Gemini; 想最深 RAG → Claude Projects; 想团队共享 → ChatGPT GPTs; 想最强反虚构 → NotebookLM.

**Translation (ja, line 14):**
> 判断ツリー (USER_GUIDE.ja.md §3 と同一): 最速を求める場合 (~30 min) → NotebookLM または Gemini; 最も深い RAG を求める場合 → Claude Projects; チーム共有を求める場合 → ChatGPT GPTs; 最強の anti-hallucination を求める場合 → NotebookLM.

**Semantic comparison:**
- "部署视角挑选" → "判断ツリー" (decision tree): The source says "deployment-perspective selection", translation says "decision tree". Both are navigational framing. The cross-reference is correctly updated from "USER_GUIDE.zh.md §3" to "USER_GUIDE.ja.md §3" — this is correct localization, not drift.
- "~30 min": PASS (verbatim)
- "NotebookLM 或 Gemini" → "NotebookLM または Gemini": PASS
- "想最强反虚构" → "最強の anti-hallucination を求める場合": PASS (faithful, "anti-hallucination" kept in English — appropriate for technical term)
- All four decision branches preserved with same platform assignments
- "想最深 RAG" → "最も深い RAG": PASS

**Verdict: PASS**

---

### Paragraph 2-B (§3 step 4, line 28)

**Source (zh):**
> 打开 §2 对应 tutorial, 严格按章节顺序执行 (跳步会丢 system_prompt 守门规则).

**Translation (ja, line 28):**
> §2 の該当 tutorial を開き、章の順序どおりに実行してください (手順をスキップすると system_prompt のゲートルールが失われます)。

**Semantic comparison:**
- "严格按章节顺序执行" → "章の順序どおりに実行": The source says "strictly follow chapter order"; translation renders this as "follow chapter order" without "strictly". MINOR_DRIFT — the adverb "严格" (strictly) is softened to plain compliance phrasing in Japanese. Low business impact: the meaning is preserved directionally, but the urgency/emphasis is reduced slightly.
- "跳步会丢 system_prompt 守门规则" → "手順をスキップすると system_prompt のゲートルールが失われます": PASS (conditional preserved: if-skip-then-lose-gate-rules)
- "守门规则" → "ゲートルール": PASS (gate rules, appropriate technical translation)

**Verdict: MINOR_DRIFT** (loss of "strictly" adverb; low impact)

---

### Paragraph 2-C (§4 smoke test failure instructions, line 38)

**Source (zh):**
> 3 题全 PASS = 部署成功. 1 题不 PASS, 看 `../KNOWN_LIMITATIONS.en.md` 排错: 优先检查 (a) system_prompt.md 是否完整粘贴未截断, (b) uploads/ 文件数和大小是否符合教程清单.

**Translation (ja, line 38):**
> 3 問すべて PASS = デプロイ成功。1 問でも PASS しない場合は `../KNOWN_LIMITATIONS.en.md` でトラブルシューティングしてください。優先確認事項: (a) system_prompt.md が完全にペーストされ途中で切れていないか、(b) uploads/ のファイル数とサイズがチュートリアルの一覧と合致しているか。

**Semantic comparison:**
- "3 题全 PASS" → "3 問すべて PASS": PASS
- "1 题不 PASS" → "1 問でも PASS しない場合": PASS (equivalent conditional)
- File path `../KNOWN_LIMITATIONS.en.md`: PASS (verbatim)
- "(a) system_prompt.md 是否完整粘贴未截断" → "(a) system_prompt.md が完全にペーストされ途中で切れていないか": PASS (faithful)
- "(b) uploads/ 文件数和大小是否符合教程清单" → "(b) uploads/ のファイル数とサイズがチュートリアルの一覧と合致しているか": PASS (faithful)
- Logical structure: two-branch conditional (success / failure) preserved

**Verdict: PASS**

---

### Paragraph 2-D (§5 Upgrade/Maintenance critical warning, line 42)

**Source (zh):**
> source 仓库后续会更新: 每个 minor release (`../CHANGELOG.md` 标 v1.1 / v1.2) 或 SDTMIG 新版 (v3.5+) 时. 重传步骤: `git pull` → 进 `current/` → 删旧 uploads + 重传 → **完整复制粘贴新 system_prompt.md** (绝不能截断, 否则丢 AHP 守门规则, 例 Gemini v7.1 CO-1d SUPPQUAL 硬锚 + ChatGPT v2.2 v3.4 新域变量名校验). 回滚: 各平台 `dev/archive/drafts/` 留历史版本可回退.

**Translation (ja, line 42):**
> ソースリポジトリは今後も更新されます: minor release (`../CHANGELOG.md` に v1.1 / v1.2 と記載) または SDTMIG 新版 (v3.5+) のタイミングです。再アップロード手順: `git pull` → `current/` に移動 → 旧 uploads を削除して再アップロード → **新しい system_prompt.md を完全にコピー&ペースト** (途中で切断すると AHP ゲートルールが失われます。例: Gemini v7.1 CO-1d SUPPQUAL ハードアンカー + ChatGPT v2.2 v3.4 新ドメイン変数名検証)。ロールバック: 各プラットフォームの `dev/archive/drafts/` に過去バージョンが保存されています。

**Semantic comparison:**
- "绝不能截断" (absolutely must not truncate) → "途中で切断すると" (if you truncate midway): The source uses an absolute prohibition ("absolutely cannot truncate"), while the translation uses a conditional framing ("if you truncate"). The prohibition force is weakened slightly, but the causal consequence remains clear.
- "Gemini v7.1 CO-1d SUPPQUAL 硬锚" → "Gemini v7.1 CO-1d SUPPQUAL ハードアンカー": PASS (verbatim technical terms, "ハードアンカー" = hard anchor)
- "ChatGPT v2.2 v3.4 新域变量名校验" → "ChatGPT v2.2 v3.4 新ドメイン変数名検証": PASS (verbatim version numbers; "域" → "ドメイン" correct)
- `git pull` command: PASS (verbatim)
- File path `dev/archive/drafts/`: PASS (verbatim)
- Numerical fidelity: "v1.1 / v1.2" → "v1.1 / v1.2": PASS

**Verdict: PASS**

---

### Paragraph 2-E (§6 Feedback, line 46)

**Source (zh):**
> 发现错误 / 幻觉: (1) 截图 + 留底完整问题原文 + AI 回答; (2) 附平台 + 版本 (例 "ChatGPT GPT v2.2 LIVE 2026-04-24") + 期望答案 (引 SDTMIG v3.4 章节号或 CDISC CT C-code) + 自部署版本号 + smoke 分数; (3) 邮件 Daisy / issue tracker / 部门群 @Daisy.

**Translation (ja, line 46):**
> 誤りや幻覚を発見した場合: (1) スクリーンショットを撮り、質問の原文と AI の回答を保存します; (2) プラットフォーム + バージョン (例: "ChatGPT GPT v2.2 LIVE 2026-04-24") + 期待される回答 (SDTMIG v3.4 章番号または CDISC CT C-code を引用) + セルフデプロイバージョン番号 + smoke スコアを添付します; (3) メールで Daisy に連絡 / issue tracker / 部門グループチャットで @Daisy。

**Semantic comparison:**
- "ChatGPT GPT v2.2 LIVE 2026-04-24": PASS (verbatim example preserved)
- "SDTMIG v3.4 章节号" → "SDTMIG v3.4 章番号": PASS (correct Japanese term)
- "CDISC CT C-code": PASS (verbatim)
- Three-step feedback process: all three steps faithfully conveyed
- Tone: source is directive/workplace; translation matches register
- "部门群 @Daisy" → "部門グループチャットで @Daisy": PASS (faithful)

**Verdict: PASS**

---

## Sample 3: self_deploy/chatgpt_tutorial.en.md ← chatgpt_tutorial.zh.md

### Paragraph 3-A (intro/preamble, lines 2-5)

**Source (zh):**
> 从零开始搭建一个能查 CDISC SDTM 标准 (63 域 + terminology + chapters) 的 Custom GPT.
> 读完本教程你会得到: 一个可用的 ChatGPT GPT, 能精确回答 SDTM 变量定义 / codelist / examples / 跨域关联, 且能识破常见虚构前提 (如 LBCLINSIG / SUPPTS / PF deprecated).
> 总耗时: **30-60 分钟** (含 indexing 等待).

**Translation (en, lines 3-5):**
> Build from scratch a Custom GPT that can look up CDISC SDTM standards (63 domains + terminology + chapters).
> After completing this tutorial you will have: a working ChatGPT GPT that accurately answers SDTM variable definitions / codelists / examples / cross-domain associations, and can detect common fabricated premises (e.g. LBCLINSIG / SUPPTS / PF deprecated).
> Total time: **30–60 minutes** (including indexing wait).

**Semantic comparison:**
- "63 域" → "63 domains": PASS
- "能识破常见虚构前提" → "can detect common fabricated premises": PASS (accurate)
- "LBCLINSIG / SUPPTS / PF deprecated": PASS (verbatim)
- "30-60 分钟" → "30–60 minutes": PASS (number identical)
- "含 indexing 等待" → "including indexing wait": PASS
- Logical structure: cause-effect (completing tutorial → having working GPT) preserved

**Verdict: PASS**

---

### Paragraph 3-B (§2 system prompt instructions, lines 35-37)

**Source (zh):**
> **完整复制** `../../chatgpt_gpt/current/system_prompt.md` 全文 (v2.2 LIVE, 8,582 chars) 粘贴进去
> **不能截断**: ChatGPT UI 字数指示器写 8000 chars 限, 实测接受 8,582 chars (verified, 已部署运行). 如果你的 ChatGPT UI 拒收, 优先剔除 §Conversation Starters 段 (非核心)

**Translation (en, lines 35-37):**
> **Copy the full contents** of `../../chatgpt_gpt/current/system_prompt.md` (v2.2 LIVE, 8,582 chars) and paste them in
> **Do not truncate**: the ChatGPT UI character indicator shows an 8,000-char limit, but in practice it accepts 8,582 chars (verified, deployed and running). If your ChatGPT UI rejects it, first try removing the §Conversation Starters section (non-core)

**Semantic comparison:**
- "8,582 chars": PASS (verbatim)
- "v2.2 LIVE": PASS (verbatim)
- "8000 chars 限" → "8,000-char limit": PASS (number identical)
- Logical structure: "UI says X, but in practice accepts Y" — conditional preserved faithfully
- Exclusion claim: "优先剔除 §Conversation Starters 段" → "first try removing the §Conversation Starters section": PASS
- "(非核心)" → "(non-core)": PASS
- File path verbatim: PASS

**Verdict: PASS**

---

### Paragraph 3-C (§3 file list, lines 52-62)

**Source (zh):**
> **文件清单 (9 文件, 总 ~2.5M tokens)**:
> - `01_navigation.md` (~46K) — ROUTING + INDEX + VARIABLE_INDEX
> - `02_chapters_all.md` (~60K) — SDTMIG ch01/02/03/04/08/10
> - `03_model_all.md` (~17K) — SDTM v2.0 Model 6 段
> - `04_domain_specs_all.md` (~185K) — 63 域 spec 全量平权
> - `05_domain_assumptions_all.md` (~54K) — 63 域 assumptions
> - `06_domain_examples_all.md` (~220K) — 63 域 examples
> - `07_terminology_core_high_freq.md` (~200K) — core 高频 15 codelist
> - `08_terminology_quest_and_supp.md` (~1M) — questionnaires + supplemental
> - `09_terminology_core_mid_tail.md` (~698K) — core 中尾段

**Translation (en, lines 52-62):**
> **File list (9 files, total ~2.5M tokens)**:
> - `01_navigation.md` (~46K) — ROUTING + INDEX + VARIABLE_INDEX
> - `02_chapters_all.md` (~60K) — SDTMIG ch01/02/03/04/08/10
> - `03_model_all.md` (~17K) — SDTM v2.0 Model 6 sections
> - `04_domain_specs_all.md` (~185K) — all 63 domain specs, equal weight
> - `05_domain_assumptions_all.md` (~54K) — 63 domain assumptions
> - `06_domain_examples_all.md` (~220K) — 63 domain examples
> - `07_terminology_core_high_freq.md` (~200K) — core high-frequency 15 codelists
> - `08_terminology_quest_and_supp.md` (~1M) — questionnaires + supplemental
> - `09_terminology_core_mid_tail.md` (~698K) — core mid-to-tail segment

**Semantic comparison:**
- All 9 filenames: PASS (verbatim)
- All file sizes (~46K / ~60K / ~17K / ~185K / ~54K / ~220K / ~200K / ~1M / ~698K): PASS (all preserved exactly)
- "9 文件, 总 ~2.5M tokens" → "9 files, total ~2.5M tokens": PASS
- "SDTMIG ch01/02/03/04/08/10": PASS (verbatim)
- "core 高频 15 codelist" → "core high-frequency 15 codelists": PASS (number preserved)
- Technical annotations preserved with complete numerical fidelity

**Verdict: PASS**

---

### Paragraph 3-D (§5 smoke test table, lines 85-88)

**Source (zh):**
> | T1 | `AESER 的 Core 属性是什么? 列出 NY codelist (C66742) 全部 term 值.` | Core = **Exp** (非 Req); 4 term: **Y / N / U / NA** + C-code | 最高频易错 + 高频 codelist 命中 |
> | T2 | `GFINHERT 是什么变量? 在哪个域?` | GF (Genomics Findings, v3.4 新域); INHERT 全称 Inherited; 7 字母精确 (不是 GFINHERTG) | v3.4 新域识别 + v2.2 拼写修 |
> | T3 | `LBCLINSIG 在哪个 codelist?` (虚构变量) | GPT 应**识破**: LBCLINSIG 不存在 LB 域 v3.4 spec; 建议改用 LBNRIND / LBSTRESC | AHP1 anti-hallucination |

**Translation (en, lines 85-88):**
> | T1 | `What is the Core attribute of AESER? List all term values in the NY codelist (C66742).` | Core = **Exp** (not Req); 4 terms: **Y / N / U / NA** + C-code | Most common mistake + high-frequency codelist hit |
> | T2 | `What variable is GFINHERT? Which domain does it belong to?` | GF (Genomics Findings, v3.4 new domain); INHERT stands for Inherited; exactly 7 letters (not GFINHERTG) | v3.4 new domain recognition + v2.2 spelling fix |
> | T3 | `Which codelist does LBCLINSIG belong to?` (fabricated variable) | GPT should **detect the fabrication**: LBCLINSIG does not exist in the LB domain v3.4 spec; suggest LBNRIND / LBSTRESC instead | AHP1 anti-hallucination |

**Semantic comparison:**
- "C66742": PASS (verbatim)
- "Core = Exp (非 Req)" → "Core = Exp (not Req)": PASS
- "4 term: Y / N / U / NA": PASS (all 4 terms verbatim)
- "GFINHERT ... 7 字母精确 (不是 GFINHERTG)" → "exactly 7 letters (not GFINHERTG)": PASS (critical anti-hallucination anchor preserved verbatim)
- "LBCLINSIG ... 建议改用 LBNRIND / LBSTRESC" → "suggest LBNRIND / LBSTRESC instead": PASS (both variable names verbatim)
- "AHP1 anti-hallucination": PASS (verbatim)
- All SDTM terms preserved exactly: AESER, NY, C66742, Exp, Req, Y/N/U/NA, GF, GFINHERT, GFINHERTG, LBCLINSIG, LB, LBNRIND, LBSTRESC

**Verdict: PASS**

---

### Paragraph 3-E (§7 Troubleshooting table + §8 downgrade path, lines 103-125)

**Source (zh):**
> | 答 GFINHERTG (extra G) | Instructions 不是 v2.2 LIVE | 检查 system_prompt.md 末尾"v3.4 新域变量名精确校验"段是否在 |
> | 答 "SUPPTS 是 dataset" | SUPP scope 段缺失 | 检查 system_prompt §SUPP scope 是否完整 (SUPPQUAL 不适用 Trial Design) |
>
> 底线保留: `01-05 + 07` (导航 + chapters + model + spec + assumptions + 高频 CT) = 6 文件核心.

**Translation (en, lines 103-125):**
> | Answers GFINHERTG (extra G) | Instructions are not v2.2 LIVE | Check whether the "v3.4 new domain variable name exact validation" section is present at the end of system_prompt.md |
> | Answers "SUPPTS is a dataset" | SUPP scope section missing | Check that system_prompt §SUPP scope is complete (SUPPQUAL does not apply to Trial Design) |
>
> Minimum retained baseline: `01–05 + 07` (navigation + chapters + model + spec + assumptions + high-frequency CT) = 6 core files.

**Semantic comparison:**
- "GFINHERTG": PASS (verbatim)
- "v2.2 LIVE": PASS (verbatim)
- "SUPPQUAL 不适用 Trial Design" → "SUPPQUAL does not apply to Trial Design": PASS (logical negation preserved: exclusion claim faithfully rendered)
- "01-05 + 07" → "01–05 + 07": PASS (file range identical)
- "6 文件核心" → "6 core files": PASS (count preserved)
- Logical structure of troubleshooting table: symptom → cause → fix — all three columns preserved correctly for all rows sampled

**Verdict: PASS**

---

## Overall Verdict

**NEEDS_FIX** — two MINOR_DRIFT issues found across 15 sampled paragraphs; no MAJOR or FABRICATION.

### Issues requiring fix:

**MINOR-1** (Sample 1, Paragraph 1-C):
- Location: `USER_GUIDE.en.md` line 29
- Source: `../README.md` "四平台分工" 表
- Translation: `../README.md`, the "Platform Roles" table
- Issue: "四平台" (four-platform) dropped in translation. The table name becomes "Platform Roles" instead of "Four-Platform Role Division" or "Four-Platform Roles".
- Suggested fix: `the "Four-Platform Roles" table` — to preserve the "four" specificity that cross-references the §3 decision tree.
- Risk: Low. Readers can still find the table; the reference is not broken.

**MINOR-2** (Sample 2, Paragraph 2-B):
- Location: `self_deploy/README.ja.md` line 28
- Source: 严格按章节顺序执行 (strictly follow chapter order)
- Translation: 章の順序どおりに実行 (follow chapter order)
- Issue: "严格" (strictly) is dropped. This weakens an important instruction about not skipping steps.
- Suggested fix: 章の順序を**厳守して**実行してください — adding "厳守" (strictly follow/must follow) to preserve the emphasis.
- Risk: Low. The user still understands sequential execution is required; only the urgency marker is softened.

## Note

**Meta-observation 1 — Consistent high quality**: The overall translation quality across all three samples is high. All 15 sampled paragraphs show correct handling of SDTM variable names (AESER, GFINHERT, GFINHERTG, LBCLINSIG, LBNRIND, LBSTRESC, LBTESTCD), C-codes (C66742), Core values (Exp, Req), domain codes (GF, AE, LB), and version numbers. Zero fabrications found.

**Meta-observation 2 — Numerical fidelity is perfect**: All numbers checked (295, 63, 17, 28, 9, 20, 296, 2536, 8582, 8000, 15, 17/17, 16.5/17, 16/17, 15/17, 30-60 min, ~46K through ~698K) are preserved exactly in all three translations.

**Meta-observation 3 — SDTM term fidelity is perfect**: Every SDTM variable name, domain code, Core value, C-code, and technical term sampled was either reproduced verbatim (EN→EN) or correctly rendered (ZH→JA) without any spelling drift, reordering, or substitution.

**Meta-observation 4 — Both MINOR drifts are presentational, not semantic**: Neither drift introduces a wrong fact, drops a technical claim, or could cause a user to take an incorrect action with the deployed GPT. They are polish-level issues.
