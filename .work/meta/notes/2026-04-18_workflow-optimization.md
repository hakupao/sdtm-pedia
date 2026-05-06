# 2026-04-18 — 我的工作流被 AI 优化了一次

> 上下文: Phase 6.5 Claude Projects (Step 1-12) 跑完后, 我问 AI: "我和你合作的这个流程规范吗? 有什么优化空间? 我想推广到其他项目"

---

## 起因

我在 `ai_platforms/claude_projects/` 里搭了一套挺重的流程:
- PLAN.md 五段式
- _progress.json + trace.jsonl + evidence/ 三套状态
- Writer / Reviewer / 主控三角色
- failures/ 归档 / subagent_prompts/ 留档 / checkpoints/ 记录

当时感觉"很规范", 但心里其实不确定: 是真规范, 还是我在自嗨造仪式?

---

## AI 的反馈 (我意外但认同的部分)

**整体评价 7/10**. 不是规范, 是"自研 + 凭直觉补齐". 要推广必须先做减法.

### 值得保留的 5 件 (R1-R5)

1. PLAN.md 五段式 — 3 个月后还能复原 why
2. 失败不删 — 这是我这套流程最稀缺的部分
3. Writer ≠ Reviewer — 自审 = 无审
4. 源只读 + 产物独立目录
5. 预授权 + 硬 checkpoint 两级

### 我过度工程化的 4 处

1. **状态三写**: `_progress.json` + `trace.jsonl` + `evidence/step_NN.md` 记同一件事
2. **PLAN.md 41KB** 但没 TL;DR, 自己回看要读 10 分钟
3. **subagent_prompts 只留了 9/14** — 半截反而制造"完整"的错觉
4. **evidence 模板小项目里是仪式** — 3 步任务套 11 个 evidence.md 太重

### 我真正漏的 2 块

**这两个是最扎心的:**

1. **语义抽检不统一**: Step 6 做了 20 变量抽样揪出 20% 信息丢失 (救了整个产物). 但 Step 7/9 压缩率 >50%, 我没做同等审计. **Layer 1 的 10/10 PASS 都是结构检查 (md5/token/文件数), 不是内容正确性**. 我怎么知道 Step 7/9 没有丢 20%?

2. **没有 retro**. 跑完就等上传, 踩过的坑没被抽象成规则. 下次项目还会在 Step 6 再踩一遍.

---

## 真正刺痛的一刀

AI 说: **"结构检查 ≠ 语义检查. reviewer 的 PASS 不能免掉业务抽样这一刀."**

我在 Step 6 做对了这件事 (所以救回来了). 但 Step 7/9 我没做. 我只是凭感觉觉得"压缩率没那么高应该还好". 这就是直觉开始掺水的地方.

---

## 被提炼出来的 4 条规则 (已写进全局 CLAUDE.md)

| 规则 | 内容 |
|------|------|
| A 语义抽检 | 压缩率 >50% 必须做 N 样本独立抽检, N 写 PLAN |
| B 失败归档 | 失败 attempt 绝不删, 结构化归档 |
| C Retro 强制 | Tier 2/3 收尾前必写 retro (保留/补上/复盘三段) |
| D 审阅隔离 | Writer 和 Reviewer 不能同一 agent 同一 session |

## 3 档模板 (Tier 1/2/3)

| Tier | 体量 | 配备 |
|------|------|------|
| 1 | <5 step, <1h | 直跑, 收尾 1 段 retro |
| 2 | 5-15 step, 半天-1天 | PLAN + _progress + checkpoints/ + failures/ + retro |
| 3 | >15 step, 多天 | Tier 2 + trace.jsonl + prompts 全留 + audit_matrix |

模板落在 `~/.claude/templates/workflow-tier2.md` 和 `tier3.md`.

---

## 自己的感悟

1. **"自我感觉流程很规范" 和 "流程真的规范" 之间有鸿沟**. 我这次自嗨了一半.
2. **仪式 ≠ 规范**. evidence/ 有 11 个文件不代表严谨, 留了 9/14 prompts 反而是反证.
3. **AI 能给出我自己给不出的诚实**. 找朋友他可能客气, 我自己可能骄傲, AI 反倒能说 "7/10, 有两个结构瑕疵".
4. **规则 A 是今天最大的收获**. 结构检查只能证明产物长得对, 不能证明意思对. 以后所有改写/压缩类任务, 语义抽检跟结构检查同等地位.
5. **Tier 分档的思路可以外推**: 做任何重复性工作前, 先问 "这是 Tier 几", 再选工具量级. 小任务用重流程是浪费, 大任务用轻流程是失责.

---

## 行动

- [x] 写项目 retro: `ai_platforms/claude_projects/RETROSPECTIVE.md`
- [x] 抽 Tier 2/3 模板: `~/.claude/templates/workflow-tier{2,3}.md`
- [x] 4 规则写进全局 CLAUDE.md 的 `<personal_operating_principles>`
- [x] 这一篇随笔 (现在)
- [ ] 下次新项目起手, 先 `cat ~/.claude/templates/workflow-tier<N>.md` 再开干, 不再凭直觉堆结构

---

## 一句话带走

> **结构检查 ≠ 语义检查. 流程仪式 ≠ 流程规范. 自己的直觉到某个点就会掺水, 需要有人 (或 AI) 敢说 "7/10, 漏了这两件".**
