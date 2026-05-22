# C3 — NotebookLM bucket 25 UX guide + screenshot (2026-05-22)

> **Phase**: C
> **Task**: Task #5

## Deliverable

`.work/07_release_v1_4/V1_4_DEPLOY_GUIDE.md` § 3 "NotebookLM 部署 (★ v1.4 加强教程)" — written this session:

- **§ 3.A.1** bucket 25 命名变更回顾 (v1.0-v1.2: `25_td_meta_ti_ts_oi.md` → v1.1+: `25_td_meta_ti_ts_oi_di.md`; v1.4 内容继续含 DI, 不改名)
- **§ 3.A.2** 操作步骤 (Step 1-4 UI walkthrough): 上传新 `25_*` → ★ 必须删旧 source (hover → ⋮ → Delete) → 检查 sources 计数 = 42 (不是 43)
- **§ 3.A.3** Screenshot 教程: 段落标记 `[TODO]` (待 Chrome MCP 协作截图 `nbm_source_list.png` + `nbm_delete_button.png`)
- **§ 3.B** v1.4 specific 变更点 (bucket 16 含 Method label table; bucket 0-15, 17-24 byte-identical 继承 v1.3)
- **§ 3.C** Sanity 验证 (Q-S4 DI domain + Q-S2 RELREC Method 双题)

## Status

- 文档主体 ✅ done
- Screenshot 实际截图 → defer v1.5 (Chrome MCP 协作 + 用户登录态 NotebookLM 同 session)

## 验证

- §3.A.2 UI 步骤与 NotebookLM 实际 UI flow 一致 (基于 v1.3 用户实操反馈中 "上传新文件后忘删旧 source" 故障模式)
- §3.A 顶部红色 ⚠️ 警告 + Step 3 ★ 强调"必须删旧" — 解决 v1.3 实操中 43 vs 42 source 计数问题

## v1.5 carry

- 实际 screenshot 截图 (`nbm_source_list.png` + `nbm_delete_button.png`) — 需 Chrome MCP 协作 + NotebookLM 登录态实操
- 截图本身归入 `.work/07_release_v1_4/screenshots/` (待建)
- v1.4 cut 时, screenshot 段保留 `[TODO]` 文字提示, 不阻塞 release
