# NotebookLM Phase 3 P3.2 — 用户 Web UI 上传手顺

> **Node**: Phase 3 P3.2 (建 notebook + 42 source 单批上传 + indexing 收敛)
> **前置**: P3.1 完成 (42 uploads md + instructions.md 落盘, 2026-04-21)
> **执行者**: 用户 (NotebookLM 无 API, Web UI only, Rule E ack personal Gmail)
> **估时**: ~10-15 min (开 notebook ~1 min + 拖拽 ~30 s + indexing ~3-5 min 按 A5' 小样外推 + tile 速览 ~5 min)
> **Checkpoint 级别**: **HARD** (上传完成 + indexing 基本 sanity 过, 不过 gate 不进 P3.3)
> **下游**: P3.3 (贴 instructions.md 到 Chat Custom mode + H3 切换验证)
> **PLAN 引用**: `docs/PLAN.md` §6 P3.2 / §2.5 A5'
> **Evidence 归档**: `dev/evidence/p3_2_upload_log.md` (本手顺末尾模板)

---

## 背景 (≤200 字)

P3.1 把 `knowledge_base/` 295 md 合成为 42 个 bucket md (总 1,582,085 words, 最大 bucket 302K < 500K/source cap, Q1 红线结构级 ∅ gap 已审). A5' 小样用户 2026-04-21 实测 **43 文件单批拖拽 OK + indexing 快 + 零 silent fail**, 故 P3.2 策略锁定**单批拖拽全部 42 文件**, 不分批预案. 上传完 + 基本 sanity 过即 P3.2 收, 深度 indexing smoke (每 tile 预览 + 10 题 citation) 挪 P3.4 完成 (避免 P3.2 scope 膨胀).

**架构**: 单 notebook × 42 sources (Pro 300 slot 的 14%), 命名 `SDTM Knowledge Base`. 三档分享 (Restricted / Anyone with link / Public) 在 P3.9 演练, P3.2 不动分享设置, 保持默认 Restricted (owner only).

---

## 前置检查 (开工前 2 min)

在浏览器操作**前**, 用户在本地终端跑这 3 条, 全 PASS 才开始:

```bash
# 1. 确认 42 个 md 存在, 无遗漏
ls ai_platforms/notebooklm/current/uploads/*.md | wc -l
# 期望: 42

# 2. 确认最大单文件 < 500K words (NotebookLM per-source cap)
cd ai_platforms/notebooklm/current/uploads && \
  for f in *.md; do echo "$(wc -w < $f) $f"; done | sort -rn | head -3
# 期望第一行: 302027 words 38_ct_questionnaires_part1_22.md (< 500K, 60% of cap)

# 3. 确认 MANIFEST.md 清单和目录一致
head -60 ai_platforms/notebooklm/current/uploads/MANIFEST.md
# 期望: "上传文件数: 42" + 42 行 source 表
```

三条任一 FAIL → 回 P3.1 修, 不进 P3.2.

---

## Step 1: 登录 + 建 notebook (~1 min)

1. 浏览器开 `https://notebooklm.google.com` → 登录 **personal Gmail** (Rule E ack 账号, 非 Workspace/EDU, 2026-04-21 ack)
2. 左上角确认 Pro tier 状态 (头像下拉应见 `Google AI Pro`, 500 notebook cap; 若见 Free tier 立即停, 先切账号)
3. 主页点 **"+ New notebook"** (或 "+ Create new")
4. 命名 notebook: **`SDTM Knowledge Base`** (严格字面, 后续 UPLOAD_TUTORIAL 引用同名)
5. 此时 notebook 空, UI 应弹出 "Add sources" 对话框 (或自动停在 Sources 面板)

**失败回退**:
- 登录跳 Workspace SSO → 切 personal Gmail 账号 (Rule E 限制)
- "+ New notebook" 灰 → 已达 500 notebook 上限, 清理旧 notebook 后重试
- 命名被占用 → 加日期后缀 `SDTM Knowledge Base 2026-04-21` (手顺内所有引用同步更新)

---

## Step 2: 单批拖拽 42 个 source (~30 s 拖拽 + 3-5 min indexing)

### 2.1 打开本地目录

- Finder 打开: `ai_platforms/notebooklm/current/uploads/`
- Cmd+A 全选 42 个 md (**不要选 MANIFEST.md**, 它是元数据不是 source)

**确认选中 42 个**: Finder 底栏应显示 `42 项已选定`. 若显示 43 (含 MANIFEST), 按 Cmd+点击 MANIFEST.md 取消选中.

### 2.2 单批拖入 NotebookLM

- 从 Finder 选中区域直接拖到 NotebookLM "Add sources" 对话框的 **Upload** 区域 (或 "Drag & drop files here" 提示框)
- 松开鼠标 → UI 立即显示 42 个 source tile 进入 "Uploading..." → "Indexing..." → 最后 ✓ ready 状态

**A5' 已验证**: 43 文件单批 OK, 42 在外推范围内, 无需分批.

### 2.3 等 indexing 全部完成

- 等到每个 source tile 右下角小圆圈从 spinner 变成 checkmark (或状态字变 "Ready")
- 按 A5' 小样 "很快" 外推, **42 × ~5 s/source ≈ 3-5 min 总**; 若单 tile 超过 3 min 仍在 spinning, 先继续等到 10 min, 仍 stuck 视为 silent fail (见 2.4)
- 用秒表记实际 indexing 总用时 (evidence 需要)

### 2.4 清点 (Silent fail 防线)

indexing 结束后:

1. Sources 面板顶部应显示 **`42 sources`** (或 "42 / 300")
2. 若显示 <42, 对照 `uploads/MANIFEST.md` 清单找出**缺失 bucket 名**, 逐个单文件 retry (Web UI → Add source → Upload 单文件), 记录 retry 次数
3. 若出现 duplicate tile (同一 bucket 上传两次), 用 tile 右上角菜单 Delete 重复项, 保留最新 indexed 的一份

**Silent fail 归档** (若发生):
```bash
# 写 failure 记录 (规则 B)
cat > ai_platforms/notebooklm/dev/evidence/failures/task_p3_2_attempt_1.md <<EOF
# P3.2 attempt 1 failure record

- 日期: <填>
- 单批拖入: 42 期望 / <实际 indexed 数>
- 缺失 bucket: <列表>
- retry 策略: 单文件补传, 记录最终补齐 bucket + 累计耗时
- 下一 attempt 输入: <必要的设计修正, 如果有>
EOF
```

---

## Step 3: 基本 sanity 速览 (~5 min, silent-fail 二道防线)

**不是 P3.4 full smoke**, 只做 3 条低成本 sanity:

### 3.1 Tile 随机速览 (5 个)

点 5 个 tile 的预览:
- 必选: `01_navigation_and_routing.md` (顶部导航)
- 必选: `29_ig_ch04_general_assumptions.md` (权威规则源)
- 必选: `38_ct_questionnaires_part1_22.md` (最大 bucket 302K, 测大文件是否截断)
- 必选: `42_req_variable_coverage_audit.md` (Q1 红线元审计 source)
- 任选: 中段一个 (如 `17_fnd_oncology_tr_tu_rs_oe.md`)

每个 tile 预览应:
- 显示 metadata header (source name / concept / covered_req_set 字段)
- 正文可读, 无乱码, 无空白, 无截断提示

任一 FAIL → 该 source 删 + 重新单文件上传, 归档到 failures/.

### 3.2 一题 Chat 冒烟 (默认 mode, P3.3 前)

Chat 面板 (默认非 Custom mode) 问一题, 只测 RAG 活性**不测 Custom 行为**:

```
问: STUDYID 变量的 Core 属性是什么?
```

**PASS 判据**: 回答含 "Req" 字样 + 有 inline citation 回指任一 source. 具体哪个 source 不挑 (navigation / common_identifiers / variable_index 都合理).

**FAIL 判据** (任一):
- 回答 "未收录" 或类似 (indexing 没生效)
- 无 citation (RAG 未激活)
- Core 写成 "Exp" / "Perm" (严重 RAG 污染, 不该发生, 回 P3.1 查 merge_sources 产物)

### 3.3 Sources 面板 source count 锁定

最终 source count = **42**, 截屏 (或文字记录) Sources 面板顶部计数, 作 evidence.

---

## Step 4: 落盘 evidence (~2 min)

创建 `ai_platforms/notebooklm/dev/evidence/p3_2_upload_log.md`, 按下面模板填 (大部分字段本手顺已预给, 用户只需填时间 / 实测数):

```markdown
# Phase 3 P3.2 — Web UI 上传执行 log

> 日期: <YYYY-MM-DD HH:MM>
> 执行者: 用户 (personal Gmail)
> 前置 commit: <执行前 git rev-parse HEAD 的 7 位>
> 手顺: dev/checkpoints/CHECKPOINT_P3.2_HANDOFF.md

## 结果摘要

| 字段 | 结果 |
|------|------|
| Notebook 创建 | ✅ `SDTM Knowledge Base` (或记实际命名) |
| 单批拖入数 | 42 / 42 |
| Indexed 成功数 | <N> / 42 (期望 42) |
| Silent fail 数 | <N> (期望 0) |
| Retry 次数 | <N> |
| Indexing 总用时 | <MM:SS> |
| Tile 速览 5 个 | PASS / 列 FAIL 的 bucket |
| Chat 一题 sanity (STUDYID Core) | PASS / FAIL 答案摘录 |

## 截屏 / 状态 (可选但推荐)

- Sources 面板顶部 source count 截屏: <文件路径或 "已拍未附">
- 任一 tile 预览截屏: <同上>

## 异常记录

<如无异常, 写 "无">
<如有异常, 列 timeline + 对应 failures/task_p3_2_attempt_<X>.md 路径>

## 下游 handoff

P3.2 hard checkpoint 状态: <PASS / FAIL>

如 PASS → 进 P3.3:
- 贴 `current/instructions.md` 全文 (9,011 chars) 到 Chat → Configure → Custom mode → Save
- 跑 P3.3 子步骤 (b) H3 三档 (Default / Learning Guide / Custom) 切换验证
- evidence: `dev/evidence/chat_mode_toggle_test.md`

如 FAIL → 规则 B 归档 attempt_<X> + 回本手顺 Step 2/3 对应失败条重试
```

---

## Step 5: 更新 _progress.json + git commit (~2 min, 本手顺外)

**不在 P3.2 scope 内**, 主 session 收到 `p3_2_upload_log.md` 后做:

1. 更新 `dev/evidence/_progress.json`:
   - `phase_states.3_execute.status` → `p3_2_done_ready_for_p3_3`
   - `phase_states.3_execute.p3_2_completion` 新增子节点 (含 indexed 数 / indexing 用时 / sanity 结果)
2. 若 P3.2 PASS, 主 session 用户 ack 后 commit + push (Chain 检查见 CLAUDE.md "Session Wrap-up" 规则)
3. 主 session 派 P3.3 指导 (非 subagent, 因 P3.3 也是用户 UI 动作)

---

## 失败回退决策树

| 症状 | 判定 | 动作 |
|------|------|------|
| 登录时强制 Workspace SSO | Rule E 账号问题 | 切 personal Gmail 重试; 持续失败调研 Workspace 限制, 补 research.md |
| Pro tier 未激活 | 订阅问题 | 确认 Google AI Pro 已 active; 若过期, 停工, 先续订 |
| 拖拽 42 后 UI 冻结 / 部分 upload 失败 | A5' 外推失败 | 规则 B 归档; 切分批 ≤25/批 × 2 批, 每批间等 indexing 完 |
| Indexing 超 15 min 仍未完 | 官方承认 silent fail 可能性 | 拍当前状态截屏, 继续等 30 min; 超 30 min 仍 stuck 的 tile 删 + 单文件重传 |
| Tile 数 <42 且找不到缺失 bucket | Web UI 清单 bug | 用 MANIFEST.md 比对, 找出缺的单文件重传; 3 次 retry 仍缺即升级为 Phase 3 blocker, 回主 session 决策 |
| Chat 冒烟 STUDYID Core 返回 "未收录" | RAG 未激活 | 重启 chat; 等多 5 min 二次尝试; 仍失败挪去 P3.4 深查是否 merge_sources 产物有结构问题 |
| 大 bucket (38_ct_questionnaires_part1_22.md, 302K words) indexing 失败 | 接近 500K cap 的边界 | 单独重传该 bucket; 2 次失败则拆分本 bucket (Phase A A3 回炉, 暂不触发) |

---

## 不在 P3.2 scope (明示)

**P3.2 只做上传 + sanity**, 以下全挪 P3.3/P3.4/P3.9, 用户**不在本手顺**做:

- ❌ 贴 `instructions.md` 到 Chat Custom mode → **P3.3**
- ❌ Default / Learning Guide / Custom 三档切换 H3 验证 → **P3.3 (b)/(c)**
- ❌ 每个 source 全量 tile 预览 (42/42) → **P3.4 (a)**
- ❌ 10 题 RAG 冒烟 (SMOKE v2) → **P3.4 (b)**
- ❌ Req 变量业务问答 N=10 (Q1 语义自证) → **P3.4.5**
- ❌ Audio Overview / Mind Map / Study Guide 生成 → **P3.5/3.6/3.7**
- ❌ A/B 15 题 → **P3.8**
- ❌ 三档分享切换演练 → **P3.9**

**P3.2 只关注**: notebook 建出 + 42 source 全 indexed + 基本活性 (5 tile 速览 + 1 题 Chat sanity).

---

## Rule D 合规说明

本 P3.2 是**用户 UI 工具级动作**, 非 Writer / Reviewer 级产物, **不占用 Rule D 链 subagent_type**. 主 session 落 evidence 后, Rule D 下一 slot (第 10 种 subagent_type) 留给 P3.4 indexing smoke 深度审 / Phase 4 跨平台对比审.

## 关联 Rule E / Q1 / Q2

- **Rule E**: personal Gmail + Pro + Web UI only, 本手顺 Step 1 已落实
- **Q1 红线**: 本步不验 Q1 语义 (挪 P3.4.5), 但**结构前提** (42 source 全 indexed) 是 Q1 语义验证的地基; 若本步 indexed <42, Q1 语义验证无意义
- **Q2 质量第一**: indexing 若卡, 优先等完 + retry, 不赶进度跳 P3.3

---

*本手顺产出日期: 2026-04-21. 来源: `docs/PLAN.md` §6 P3.2 + `dev/evidence/phase_a_webui_small_sample.md` (A5') + `current/uploads/MANIFEST.md` (42 源清单).*
