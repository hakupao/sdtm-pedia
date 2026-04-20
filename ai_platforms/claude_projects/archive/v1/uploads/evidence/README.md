<!-- chain: B (工作日志链) -->

# Evidence 目录

> 用途: 记录 Phase 6.5 Claude Project 压缩部署每个 Step 的完整执行证据
> 关联计划: [`../../PLAN.md`](../../PLAN.md) §7.10
> 进度索引: [`../_progress.json`](../_progress.json)

## 目录结构

```
evidence/
├── README.md                       ← 本文件
├── trace.jsonl                     ← 全局执行轨迹（append-only）
├── step_01_count_tokens.md         ← 每个 Step 一份 evidence（PASS 或 FAIL 都保留）
├── step_02_compress_index.md
├── ...
├── step_12_build_all.md
├── step_14_layer2_test.md
├── checkpoints/                    ← 每个 checkpoint 的用户对话归档
│   ├── ckpt_step03.md
│   ├── ckpt_step05.md
│   └── ...
├── subagent_prompts/               ← 调用 subagent 时的完整 prompt 归档
│   ├── step_06_executor.md
│   ├── step_06_reviewer.md
│   └── ...
└── failures/                       ← 失败的 Step 单独归档（不删除）
    └── step_XX_attempt_N.md
```

## Evidence 文件命名规范

- 成功: `step_<NN>_<short_name>.md` (NN 两位数)
- 失败重试: `failures/step_<NN>_attempt_<M>.md` (M 从 1 起)
- Checkpoint: `checkpoints/ckpt_step<NN>.md`
- Subagent prompt: `subagent_prompts/step_<NN>_<role>.md` (role: executor/reviewer/verifier)

## 何时写 evidence

- ✅ 每次 subagent 调用结束后（无论 PASS/FAIL）
- ✅ 每次 checkpoint 用户回应后
- ✅ 每次 build_all.py 跑完后
- ✅ Layer 2 每个测试 T1-T8 跑完后

## Evidence 不可变原则

- evidence 文件**只追加，不修改**（除非修订错别字）
- 失败 evidence 必须保留，不允许删除（用于根因分析）
- 如需勘误，在文件末尾追加 `## 勘误 (YYYY-MM-DD)` 段

## trace.jsonl 格式

每行一个 JSON 对象，append-only：

```json
{"ts": "2026-04-17T10:00:00Z", "step": 1, "event": "step_start", "agent": "executor", "model": "opus"}
{"ts": "2026-04-17T10:02:13Z", "step": 1, "event": "step_done", "tokens": 0, "status": "PASS"}
{"ts": "2026-04-17T10:02:15Z", "step": 2, "event": "step_start", ...}
```
