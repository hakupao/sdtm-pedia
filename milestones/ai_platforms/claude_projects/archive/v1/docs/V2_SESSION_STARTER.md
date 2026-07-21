# Phase 6.5 v2 — 新 Session 启动提示词

> 用于在**新 Claude Code session** 中启动 Phase 6.5 v2 扩容执行。
> 复制下面 ``` 围起来的全文, 粘贴到新 session 的第一条消息即可。
> 创建日期: 2026-04-18
> 上游: PLAN_V2.md (1852 行) + design doc

---

## 启动提示词 (复制下面整段)

```
启动 Phase 6.5 Claude Project v2 扩容执行。

## 上下文
你接管 SDTM 知识库 Phase 6.5 v2 扩容工作。前置 session 已完成:
- design doc: docs/superpowers/specs/2026-04-18-phase6.5-claude-v2-expansion-design.md
- 实施计划: ai_platforms/claude_projects/PLAN_V2.md (1852 行, 8 阶段 ~30 Tasks)
- v1 baseline 已上传到第一个 Claude Project (192K, 12% capacity)
- 用户已批准计划 + 全部预授权

## 你必须立刻做
1. 读 CLAUDE.md (全文, 含 v2 Key Paths)
2. 读 .work/MANIFEST.md (含 v2 计划注册)
3. 读 ai_platforms/claude_projects/PLAN_V2.md (你的执行手册, 全文)
4. 读 docs/superpowers/specs/2026-04-18-phase6.5-claude-v2-expansion-design.md (设计依据)
5. 读 ai_platforms/claude_projects/RETROSPECTIVE.md (v1 复盘 + 4 条规则 A/B/C/D)
6. 调用 superpowers:subagent-driven-development skill (执行模式必须)
7. 从 PLAN_V2.md §3 Phase A Task A1 开始执行

## 预授权 (用户已给, 不要再问)
- Phase A (Setup) + Phase B (Tooling) 连续推进, 不需逐个 ack
- Stage v2.X 全 PASS 且 0 衰减 → 自动进 v2.(X+1)
- 衰减 ≥1 题 → 必须停下汇报用户, 等回应
- 衰减 ≥2 题 → 立即停, 视当前为 v2 终态, 直接进 Phase H 收尾

## 关键约束 (强制遵守, 违反必修)
- 规则 A: 压缩率 >50% 步骤强制 N=10 样本独立抽检 (reviewer 5 + 主控 5 不重叠)
- 规则 B: 失败 attempt 不删, 归档到 evidence_v2/failures/
- 规则 C: 收尾必写 RETROSPECTIVE_V2.md (PLAN §H1)
- 规则 D: writer 与 reviewer 必不同 subagent_type
- P5: knowledge_base/ 全程只读
- P6: 每个脚本独立 executor subagent, 主控不读脚本源码
- P7: 每 Step 完成立即更新 output_v2/evidence_v2/_progress.json
- P10: A/B 衰减强制响应 (≥2 立即停)

## 第一个 hard checkpoint 在哪
PLAN_V2 §5 Task C3 (完成批 1 chapters 全展开后), 你停下汇报:
- 02_chapters.md 实测 token
- C2-C5 自动检查结果
- 让用户在 Claude.ai 新建第二个 Project + 上传 11 文件 + 跑 T1-T12 A/B 测试

在此之前 (Phase A Setup + Phase B Tooling + Phase C Task C1/C2), 你可以自主连续推进。

## 用户期望
- 不怕麻烦, 多轮上传/删除/测试都可以
- 希望执行复杂详细
- v2 终态目标: ~50% 容量 (~1.3-1.5M tokens, 16-18 文件)
- 70% 留作 Phase 6.5+ 第二轮

## 现在开始
读完上面 6 个文件, 用 1 段简短 (≤150 字) 向用户汇报你的理解 + 准备从 Task A1 开始。等用户简短确认后开干。
```

---

## 备用: 主控如果丢失上下文

如果新 session 中途 crash 或丢上下文, 用以下恢复提示词:

```
恢复 Phase 6.5 v2 扩容执行。

## 1. 立刻读取 (找到当前进度)
- ai_platforms/claude_projects/output_v2/evidence_v2/_progress.json (current_stage + completed_*)
- tail -20 ai_platforms/claude_projects/output_v2/evidence_v2/trace.jsonl
- ls ai_platforms/claude_projects/output_v2/evidence_v2/failures/ (如有, 上次断在重试)

## 2. 然后读
- ai_platforms/claude_projects/PLAN_V2.md §对应 current_stage 的 Phase
- 上一个 evidence stage_v2.X_*.md (了解上次做完什么)

## 3. 续跑
按 PLAN §10 (Wrap-up) 之外的 Tasks 续跑, 跳过 _progress.json.completed 中的 Step。
新写 trace.jsonl 行: {"event":"session_resume","ts":"...","prev_stage":"...","resume_at_task":"..."}.

## 预授权 + 约束 (同首次)
(复制启动提示词中的预授权 + 关键约束段)
```

---

## 操作建议

1. 在新 Claude Code session 第一条消息: 粘贴上面"启动提示词"全文
2. 等主控读完 6 个文件后简短汇报理解
3. 简短回 "ok 开始" 或 "调整: ..."
4. 主控自主走完 Phase A (Setup) + Phase B (Tooling), 进 Phase C Task C1 (写 rebuild_chapters_full.py)
5. Phase C Task C3 时主控停下, 你在 Claude.ai 新建第二个 Project + 上传 + 测试
6. 测试结果回报给主控, 它判定进 Phase D 或回退
7. 重复 5-6 直到 Phase G (v2.5 终测) 或提前终止
8. Phase H 主控写 RETROSPECTIVE_V2 + 收尾 commit + push
