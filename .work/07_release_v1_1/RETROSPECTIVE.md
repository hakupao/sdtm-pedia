# Release v1.1 — RETROSPECTIVE

> 完成日期: 2026-05-15
> 阶段跨度: P0 (用户决策走 v1.1 路线 2026-05-15 AM) → cut + push 2026-05-15
> 规则 C 强制产物 (Tier 2 项目收尾)
> 上一版反思: `.work/07_release/RETROSPECTIVE.md` (v1.0)

---

## § 一、保留下来的做法

**1. release 包用 `release/v1.X/` 平行目录, tag 不可变**
v1.0 (`release/v1.0/` + tag `v1.0-company-release` 2026-04-27) 完全保留, v1.1 平行建 `release/v1.1/` 与 v1.0 同结构. 不 in-place 修改 v1.0 任何文件. 历史溯源完整, 自部署用户能精确指向某 tag.

**2. 4 平台 build 脚本对 KB 完全 read-only**
所有 merge_for_*.py + extract_*.py + merge_sources.py 严格 P5 规则: 只 read knowledge_base/, 写到 platform current/uploads/. 没有任何脚本回污染 KB. v1.1 rebuild 跑完, KB diff 为空.

**3. baseline 先备份再 rebuild**
开工先把 4 平台 current/uploads (25MB) 备份到 `.work/07_release_v1_1/backups/`, 失败时可回滚. 实战中 chatgpt 05 第一次 rebuild 时 fail-fast 中止写入, baseline 完好无损; 修脚本后 re-run 成功.

**4. 改动 diff 与 KB 06 改动量级一致是关键 sanity 信号**
chatgpt 05 +74KB, gemini 02 +74KB — 两个平台对同源 KB (assumptions/) 的聚合 delta 完全一致 (74,178 字节). 这证明:
- 两个 build pipeline 都正确捕获了 06 改动
- 没有 silent 数据损失
- 改动是真改动, 不是空跑导致的字节扰动

跨平台 delta cross-check 是 v1.X rebuild 的天然 oracle, 后续 release 应保留这个验证步骤.

**5. DI 新加 domain 主动加进 notebooklm bucket_config**
notebooklm 用 hardcoded bucket file list, 不像 chatgpt/gemini 自动扫目录. 如果不主动加 DI 到某 bucket, 它会被静默漏掉. 把 DI 加进 bucket 25 (td_meta_ti_ts_oi) 因 DI 是 study reference dataset 与 TI/TS/OI 同类 — 选择有据可依.

**6. 元文档/system prompts/教程 v1.0 → v1.1 完全不变**
06 是内容修复 (KB 内的事实), 不动方法论. system_prompt 引用的 routing/index 也未变. 把 release 包元文档分层 — "稳定层 (方法/教程)" + "易变层 (uploads/)" — 让 v1.1 cut 只需重 build 易变层. 这个 release 分层设计应该写进 v1.2+ 模板.

---

## § 二、必须补上的缺口

**1. claude_projects 双 builder 系统的路径修复 (待 executor 完成判定)**
v1 (archive/v1/scripts/) 写到 `output/`, v2 (dev/scripts/) 写到 `output_v2/`. 两个 output 目录都不存在 (文件已 move 到 current/uploads/). v1.1 rebuild 需要先 mkdir + run scripts + copy 回 current/uploads/. 如果 executor 失败需 fallback 单文件人工 rebuild.
→ **后续建议**: 加 `--output-dir` 参数到 v1/v2 各 builder, 或者改默认写到 current/uploads/, 避免 stale output_v2 路径.

**2. chatgpt 05 expected_segments 硬编码**
原 63 → DI 加入后 64. 修复方式 = 改一行 expected_segments + token_cap. 但本质问题: 任何 hardcoded "63 domains" 假设都会随新 domain 加入而坏掉.
→ **后续建议**: 把 domain count 改成运行时 `len(_collect_domain_assumptions())`, 仅在与"上次 build 数"diff 大时 warn, 不 fail-fast.

**3. notebooklm bucket_config.json 缺新域 detection 自动化**
DI 加入是我主动 grep + 决策的, 没有自动检测. 如果 06 加了 5 个新域, 我会逐个 grep 然后做 5 个决策, error-prone.
→ **后续建议**: 写 `validate_bucket_coverage.py`: 列出 KB 所有 domain/* 文件, 比对 bucket_config.json 覆盖的文件, 漏掉的 fail + 建议 bucket. 集成进 CI / 跟 KB 改动 chain.

**4. 没跑 SMOKE_V4 验证 06 修复对部署后回答质量的影响**
本次 v1.1 cut 只验证了"上传包结构 + 改动量"层面. 没有验证 06 修复是否真的改善了之前 smoke test 答得差的题. 比如 PC RELREC linking 是 P7 抽样发现的真实缺口, 加进 06 后理论上能改善"PC 怎么和 PP 关联"问题. 没测.
→ **后续建议**: v1.2 cut 时, 先把 v1.1 uploads 部署一遍, 跑 SMOKE_V4 R3, 对比 R1 baseline, 列出 06 修复带来的题目级改善 — 这才是 v1.1 cut 的真正业务价值证据.

**5. Rule D reviewer 选择是事后决定**
本次 reviewer subagent_type 选 `oh-my-claudecode:verifier` (opus) 是临时决定的. 没有事前 plan 写明哪个 subagent_type 是 reviewer.
→ **后续建议**: PLAN.md 里 step 7 写明候选 reviewer subagent_type list (≥3 个备选, 区别于 main session), 避免临场选择.

---

## § 三、关键决策复盘

**决策 1: 走 v1.1 路线 (而非 in-place 更新 v1.0)**
*做法*: cut 新 tag `v1.1-company-release`, `release/v1.1/` 平行 v1.0 完整目录.
*为什么*: tag 是不可变 artifact 原则; 如果有外部用户 self-deploy 用了 v1.0, 他们能精确指向 v1.0 tag, 也能选择升 v1.1. 在 v1.0 上 force-push 会破坏 git tag 一致性.
*结论*: 正确. 多花的成本 (~20MB 重复 release dir) 远小于 tag 完整性价值. 后续所有内容 refresh 走 vX.Y patch tag.

**决策 2: DI 加进 notebooklm bucket 25 (td_meta), 不加进 bucket 18 (device findings)**
*做法*: bucket 25 现叫 "td_meta_ti_ts_oi" + DI assumption.
*为什么*: DI 在 SDTM v1.7+ 分类是 "study reference dataset" (与 TI/TS/OI 一致), 不是 findings; bucket 18 (device findings) 含 DA/DD/GF/IS 都是 findings classes, 类型不符.
*结论*: 决策正确 (无现成更好的备选). 但 bucket 25 名字现在叫 "td_meta_ti_ts_oi" 而内容含 DI, 命名 mismatch — 应改 bucket name 到 `25_td_meta_ti_ts_oi_di.md` 或 `25_study_ref_ti_ts_oi_di.md`. 推后到 v1.2 处理 (本次只加文件, 不改 bucket name 避免破坏部署 URL 引用).

**决策 3: terminology bundles (11/12/13 + 07/08/09) 不重 build**
*做法*: 重 build 时让 idempotent skip 检查到内容相同直接 "skipped (same)".
*为什么*: 06 完全未触 terminology/. 重 build terminology 浪费 (~3M tokens 重处理) 且无变化.
*结论*: 正确. 节省 ~5 分钟 build 时间 + ~10MB diff 噪声.

**决策 4: 把 claude_projects rebuild 派给 executor subagent 后台跑**
*做法*: 主 session 处理 3 简单平台, 把 v1+v2 复杂双 builder 派给 sonnet executor 异步.
*为什么*: claude 路径 stale + 多 script + DI 适配 = 实质上是一个 self-contained sub-project. 主 session 同时跑 3 平台 rebuild + Rule D + release 包装 + worklog 更新. 利用 background subagent 拿到 parallelism.
*结论*: 正确. Executor (sonnet) 在 ~6.3 分钟内完成全部 claude rebuild (7 文件 rebuilt + 12 unchanged), 自己解决了 stale 路径问题 (mkdir output_v2/ + output/ + workaround REPO_ROOT bug), 自己适配了 DI 新增 (06_assumptions 64 域 vs 05_mega_spec 63 域 split), 自己写了 failures/claude_rebuild_failures.md (F1-F4) — Rule B 合规. 主 session 同时完成了 release v1.1 包结构, 时间并行重叠.

**决策 5: 三语 CHANGELOG (en/zh/ja) 主 session 手写, 不派 writer subagent**
*做法*: 我直接写三份 CHANGELOG.
*为什么*: 信息密度高 + 三语翻译需要 cross-check, 派 writer subagent 不一定比主 session 快.
*结论*: 正确. 三份 CHANGELOG 一致 + 风格统一; subagent 协调成本可能反超.

---

## 附: v1.1 终态数字

| 指标 | 值 |
|------|----|
| KB 文件总数 | 296 (含新 DI domain) |
| Domain 总数 | 64 (原 63) |
| 4 平台 uploads 总大小 | ~21 MB (chatgpt 9.3M + claude 4.6M + gemini 2.2M + notebooklm 9.5M) |
| 重建文件数 | 24 (chatgpt 4 + gemini 3 + notebooklm 12 + claude 6 真改 + 1 idempotent) |
| 06 修复涉及 KB 文件 | 43 (+1,405 / -234 行) |
| Build 脚本改动 | 2 (merge_for_chatgpt.py + notebooklm bucket_config.json) |
| 工程耗时 | <1 天 (2026-05-15 决策 → 同日 cut) |
| Rule D reviewer slot | `oh-my-claudecode:verifier` (opus) — ALL_PASS, 5/5 评估, Rule A 5/5 KB→uploads 抽检 (20 platform-strings zero miss), 跨平台 delta oracle 自洽 (chatgpt 05 ≡ gemini 02 = +74,178 bytes) |
| Cross-platform delta oracle | chatgpt 05_assumptions delta == gemini 02_specs_and_assumptions delta == +74,178 bytes (同 KB 源, 双 pipeline, 字节级一致) |
