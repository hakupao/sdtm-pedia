# Step 3 reviewer Prompt
> 调用时间: 2026-04-17 11:50
> Agent: oh-my-claudecode:code-reviewer
> Model: opus

## Prompt 正文

## 上下文
Step 3 独立复核。上一个 executor 已产出 `compress_chapters.py` 和 `output/02_chapters.md`。
Executor 自测: 44874 tokens, idempotent PASS, ch04 retention 99.96%, per-chapter ch01=1527, ch02=2178, ch03=3296, ch04=31294, ch08=4203, ch10=2192.

计划: `/Users/bojiangzhang/MyProject/SDTM-compare/ai_platforms/claude_projects/PLAN.md` §7.4 Step 3 + §5.1 C6
工作目录: `/Users/bojiangzhang/MyProject/SDTM-compare`

§7.1 P2 写审分离：你必须独立判断，不复述 executor 结论。这个 Step 是整个 PLAN 第一个关键检查点（ch04 是推理基础）。

## 需要复核的工件
1. 脚本: `ai_platforms/claude_projects/scripts/compress_chapters.py` (898 行)
2. 输出: `ai_platforms/claude_projects/output/02_chapters.md` (44874 tokens 实测)
3. 源文件（只读）:
   - knowledge_base/chapters/ch01_introduction.md
   - knowledge_base/chapters/ch02_fundamentals.md
   - knowledge_base/chapters/ch03_submitting_data.md
   - **knowledge_base/chapters/ch04_general_assumptions.md** ← 关键
   - knowledge_base/chapters/ch08_relationships.md
   - knowledge_base/chapters/ch10_appendices.md

## 复核清单（逐项 PASS/FAIL）

### A. ch04 完整性（PLAN §5.1 C6: 字符数 ≥ 源 95%）
- A1: ch04 在 output 中字符数 ≥ 源文件 95%（源 124603 字节, 需 ≥118373）
- A2: ch04 所有 `###` 三级标题完整保留（数一下：源有多少，output 有多少，必须 ≥95%）
- A3: ch04 所有 Specification 表完整（查关键变量如 STUDYID, USUBJID, DOMAIN, EPOCH, VISITNUM 等仍在）
- A4: ch04 的 numbered assumption 编号体系完整（1, 2, 2a, 2b, 3... 若有缺失需报告）

### B. 非 ch04 章节的结构骨架
- B1: ch01/02/03/08/10 每章都有 `<!-- source: -->` 注释头
- B2: 每章所有 `###` 三级标题保留（关键规则小节不能丢）
- B3: Specification 表完整（变量名/Label/Type/Role/Core 五列都在；Notes 可压缩但不能全删）
- B4: 编号规则列表 (1., 2., 2a., ...) 完整

### C. 脚本质量
- C1: 源文件只读（只有 .read_text / open 'r'）
- C2: 幂等（独立验证：md5 两次运行一致）
- C3: 时间戳来自 source mtime 而非 datetime.now()
- C4: 无明显 dead code

### D. Token 预算
- D1: 实测 ≤ 45000 tokens（跑 count_tokens.py 确认）
- D2: ch04 占用 ~31K 左右（不能明显缩水，也不能显著膨胀）

### E. P5 约束
- E1: knowledge_base/chapters/*.md 所有 6 个文件未被修改

## 可用工具
- Read (源 + 产出 + 脚本)
- Bash (跑 count_tokens / grep / md5 / wc / diff)
- Grep

## 独立抽样检查建议

对 ch04 做重点抽样（至少 3 个随机位置对比源 vs output）：
```bash
# ch04 源 vs output 中 ch04 段落
grep -n '^####' knowledge_base/chapters/ch04_general_assumptions.md | head -20
grep -n '^####' ai_platforms/claude_projects/output/02_chapters.md | grep -A0 '' | head -30
```

## 输出格式（≤400 字）

```
## Step 3 复核结论: PASS / CONDITIONAL_PASS / FAIL

### 检查项结果
A1-A4 (ch04): ...
B1-B4 (其他章节): ...
C1-C4 (脚本): ...
D1-D2 (token): ...
E1 (P5): ...

### 关键发现
(≤4 条)

### 风险（如有）
(≤2 条)

### 对 §5.1 C6 的判定
(专门回答: ch04 是否满足 ≥95% 完整性)

### 建议
(继续 / 修 / 用户 checkpoint)
```

只做只读复核，不改文件。