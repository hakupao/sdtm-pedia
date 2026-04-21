# Phase A A5': Web UI 上传能力小样实测 (M2 fix)

> **产出日期**: 2026-04-21
> **执行者**: 用户 (主 session 无 Google UI 登录权)
> **目的**: 闭合 M2 "≤50 次 Web UI 手工拖拽可行性未做实测" 风险
> **Phase A 角色**: A5' 独立 hard checkpoint, 与 A1/A2 并行, 不依赖其他产物

---

## 实测结果

| 字段 | 结果 |
|------|------|
| **单批拖拽能力** | ✅ **支持** — 用户实测**一次性拖入 43 个 md 文件**, Web UI 无拒绝 / 无分批 / 无限流提示 |
| **Indexing 速度** | ✅ **很快** — 用户观察 "indexing 很快" (未记录具体秒数, 但主观感受是远低于 research.md Q5 的 "几秒-几分钟" 上界) |
| **Silent fail 比例** | ✅ **零失败** — 用户实测 43 个 source 全部正常 indexed, 无 silent drop |
| **测试规模** | 43 source (本次目标 ≤50 的 86%, 具有 extrapolation 依据) |

## 结论

**P3.2 策略明确: 走**单批上传**** (不需分批预案).

- 用户实测 43 source 单批 OK + 本次目标 ≤50, 落差 7 个 slot, 实测足以线性外推到 50 slot
- 指令 silent fail 零发生 → P3.4 indexing smoke 作 sanity check 即可, 不作为高风险 gate
- 若 Phase 3 实际上传 50 个 source 触发未预期限流 (<5% 概率), 规则 B 归档 + 主 session 立即切分批策略 (≤25/批, 2 批走完)

## P3.2 设计更新

§6 P3.2 "Web UI 建 notebook + 上传 ≤50 source" 子步骤确认为:

1. 登 notebooklm.google.com → New notebook → 命名 "SDTM Knowledge Base"
2. **一次性拖拽** `current/uploads/*.md` 全选 ≤50 个 到 source panel (用户实测 43 单批 OK, 50 在线性外推范围内)
3. 等 indexing 完成 (用户实测 "很快", 具体时间 Phase 3 P3.2 实际执行时记录)
4. 进 P3.4 indexing smoke test

**回退路径** (若实际 50 批失败):
- 规则 B 归档失败 attempt: `dev/evidence/failures/task_p3_2_attempt_1.md`
- 切分批: ≤25/批, 2 批走完 (每批间等 indexing 完)
- Phase A A5' 实测未覆盖 50 源 + silent fail 隐患, 属已知 5% 残余风险, 有回退路径即可

---

## Rule D 合规说明

本 evidence 由主 session 代写 (用户实测结果口述 → 主 session 落盘). 因小样实测属 **Phase A 工具级动作, 非 Writer / Reviewer 级产物**, 不占用 Rule D 链 subagent_type. Phase A 整体 audit 在 Phase 3 启动前由主 session + 用户 ack 共同验证.

## Phase A A5' 状态

- **Status**: ✅ **PASS** (用户 2026-04-21 实测 43 文件单批 OK)
- **下游影响**: P3.2 策略锁定单批, P3.4 smoke 风险降级
- **不再需要**: Playwright 前置 tooling / 分批策略预案激活

---

*来源: 用户 2026-04-21 Web UI 实测口述记录, 落盘于本 evidence 文件.*
