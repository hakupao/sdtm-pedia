# ChatGPT GPTs — SDTM 知识库

## 状态

> **待开始** (范本就绪, 等 Phase 0 启动) · 最后更新 2026-04-20
>
> 本目录按 [`ai_platforms/_template/`](../_template/) 四层结构组织.
> 预期产出: 1 份 Custom GPT, 约 8-10 个合并文件, 特色是"全量覆盖 (~9.6MB) + 可公开发布到 GPT Store".

---

## 我想做什么?

### 部署一个可用的 SDTM Custom GPT
→ **(等启动完成后)** 去 [current/](current/), 读 `UPLOAD_TUTORIAL.md`.
→ 当前 `current/` 仅占位, 等 Phase 3 产出发布版.

### 理解这套知识库会怎么做出来 (方法论参考)
→ 去 [docs/](docs/) 看 [platform_profile.md](docs/platform_profile.md) (Phase 0 填空初稿).
→ 启动后会补 `PLAN.md` / `research.md` / `RETROSPECTIVE.md`.

### 考古 / 复盘
→ 暂无. 启动后 [dev/](dev/) 会有过程产物, [archive/](archive/) 会有历史版本.

---

## 目录结构

```
chatgpt_gpt/
├── README.md                        本文件 (入口)
├── ROADMAP.md                       路线图 (状态 / 策略 / 步骤)
├── 🟢 current/                      发布版 (待填, 启动后会有 uploads/ + system_prompt + UPLOAD_TUTORIAL)
├── 🟡 docs/                         方法论
│   ├── README.md                    目录说明
│   └── platform_profile.md          平台特化填空 (Phase 0 初稿)
├── 🔵 dev/                          过程产物 (启动后填)
└── ⚫ archive/                      历史归档 (暂无历史版本)
```

---

## 范本来源

所有流程 / 规范 / 目录约定继承自 [`ai_platforms/_template/`](../_template/).
本目录是**填充实例**, 不重复规范定义.

**启动时必读**:
1. [`../_template/README.md`](../_template/README.md) — 范本 10 维度总览
2. [`../_template/APPLY_CHECKLIST.md`](../_template/APPLY_CHECKLIST.md) — 启动清单 (Phase 0-5)
3. 本目录 [docs/platform_profile.md](docs/platform_profile.md) — 本平台的填空初稿

---

## 关键事实 (待 Phase 5 收束时回填)

- 知识库覆盖: (Phase 5 回填)
- 合并文件数: ~8-10 (<20 文件硬限)
- 总 tokens: (Phase 5 回填)
- A/B 矩阵 PASS 比: (Phase 5 回填)
- 发布范围: Private / 团队 / GPT Store (Phase 0 用户定)

---

*建立: 2026-04-20 (按 `_template/` 升级).*
