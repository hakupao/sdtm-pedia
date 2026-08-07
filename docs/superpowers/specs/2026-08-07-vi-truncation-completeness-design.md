# VI §三 15 变量截断 — 交叉引用完整性设计

> 建立: 2026-08-07
> 来源: `sdtm-rag/evidence/checkpoints/s1_variable_index_literal_section.md` §4 已知限制 1 (规则 A 抽检 D-3)
> 状态: 设计已认可, 待实施

## 1. 问题

`knowledge_base/VARIABLE_INDEX.md` §三 CT 交叉引用表, 每行只列前 15 个引用变量就写
`... (N total)`。**该表是"哪些变量引用这个码表"这个问题的唯一权威来源**, 被截断意味着
注入的 chunk 正文**结构上答不全**这个问题。

实测规模 (可复跑, 见 §5.1):

| 处 | 上限 | 命中 | 隐藏条目 | 生成器 |
|---|---|---|---|---|
| VI §三 CT 交叉引用 | 15 | **9 / 135 行 (6.7%)** | **226** | `.work/04_optimization/scripts/generate_variable_index.py:253` |
| 域 spec 交叉引用段 | 5 | 2 文件 (AE / LB) | 10 | `.work/04_optimization/scripts/generate_cross_references.py:236` |

最宽的几个: `C66742` 123 个引用 / `C71620` 58 / `C99079` 44 / `C66789` 36 / `C66728` 26。

### 1.1 为什么现在必须修 —— 它封住了上一轮成果的读法

上一轮 (S1 字面 section 定位) 把 18 题 VI 子集拉到 100.00%, 但抽检方指出该分数**不能读作
"VI 类问题已解决"**: section 级 source recall **只看 section 名对不对, 不看正文是否被截断**。
实测两个零余量样本:

- **q109** (`C99073`, 17 个引用): gold 要的 `TU.TULAT` 恰好排在**第 15 位 = 截断边界最后一位**;
  被截掉的是 `UR.URLAT` 与 `VS.VSLAT`。
- **q69** (`C71620`, 58 个引用): gold 要的 `EX.EXDOSU` 同样恰好在**第 15 位**。

即当前满分是压线过关。gold fact 只要落在第 15 位之后, source recall **仍判 1.00**, 而注入正文
根本答不出来 —— 判据在这一维度上判别力为零。

## 2. 修法

删掉两个生成器里的条数上限, 重生成 KB, 重灌索引。

全展开 **129.6 KB → 133.8 KB (+4.2 KB)** —— 实测非估算, 命令见 §5.3。最宽的 `C66742`
那行约 1.5K 字符, 远在 chunk 尺度内。
**截断买到的是 4.2 KB**, 代价是把该表在最需要它的那 9 个宽码表上变成了半张表。

范围: **两处同病一起修**。同一种病同一次重灌解决; 分两轮做要重灌两次。

## 3. 验收 —— 这个单元真正难的地方

**现有 CDISC 检索闸对这个修复结构上失明。** section 名一个字不变, 所以改完 recall 仍是 98.93%、
配对 diff 全 Δ0。**"闸绿了"只能证明没回归, 证明不了修好了。** 故本轮必须自带尺子。

### 3.1 层① 确定性完整性断言 (主护栏, 零 LLM, 常驻)

对**全部 135 行**断言"正文列出的条目数 == 该行自己声称的 References 数", 且全库无
`... (N total)` 残留。域 spec 交叉引用段同理。

这是**数据不变量, 不是对某道题的补丁** —— 它一次性覆盖 9 个宽码表的全部 226 条隐藏条目,
且永久钉住 (将来谁再加截断当场红)。

断言必须同时打在**两层**:
- **KB markdown 层**: 生成器输出正确;
- **chunk 层**: 真正进索引的那段文本正确。KB 对而 chunker 截断仍然会伤 —— `kb_freshness.py`
  的存在动因正是 2026-08-04 实测到"部署中的向量库把 VARIABLE_INDEX.md 欠切 70%", 同一文件有前科。

### 3.2 层② 端到端 gold 题 (佐证, 少量)

新增 2 道 gold 题, 独立文件 `sdtm-rag/eval/test_set_vi_completeness.yml`。

**出题规则 (写死, 规则驱动而非挑例子)**:
> 凡 `N > 15` 的码表, 问"哪些变量引用它", **gold fact 取位置 > 15 的条目 (按字母序末位, 确定性可复现)**。

三层防线, 说明这不是对 example 的"对症下药":
1. 规则作用于 **9 个宽码表全体**, 不是挑 `C66742` 一个; 只落 2 道进题集控体量, 其余 7 个由层① 全覆盖。
2. 出题规则可机械执行 —— 任何人拿这条规则能重新生成同一批题, 不依赖"我知道哪里坏了"。
3. 真正的护栏是层① 的数据不变量; 题只是端到端佐证。**题若与层① 结论冲突, 以层① 为准。**

### 3.3 为什么不进 `test_set_v3.yml`

往 v3 加题会换掉 140 的分母, 刚立住的 98.93% 基线连同全部历史 run 一起失去可比性 ——
正是本项目"三版题集互不可比, 一版一把尺子"那条教训。故独立文件独立计分。

### 3.4 "改动前"数字怎么拿 —— 不做两次重灌

同一问句喂**两份 context** (截断版 vs 完整版) 跑同一模型的对照。变量隔离得更干净
(只有那段正文变了), 且省一次全量重嵌。

### 3.5 必须随结果一起声明

- **v3 的 98.93% 改完会一动不动。那不是没效果, 是那把尺子量不到。**
  引用本轮成果时**不得**用 v3 数字, 只能用层①/层② 的结果。
- source recall 对本修复同样失明 (gold section 本来就命中), 层② 的判别力**只在 fact 侧**。

## 4. 连带必须过的闸

| 闸 | 为什么 |
|---|---|
| `scripts/reconcile_meta.py` | 它读 VI 的 header 计数与 §一 行做 meta↔KB 对账。§三 改动理论上不影响, **必须实跑确认**而不是推断 |
| `scripts/check_index_freshness.py` | 重灌后必须回到 `index_fresh: true` |
| v3 检索闸 (140 题) | 期望**逐题 Δ0**。这里的绿是"没回归", **不是**"修好了" (见 §3) |
| 全量 pytest | 重灌改变 chunk 内容, 既有 chunker/ingest 测试须全绿 |
| 服务重启 + `s1_vi_section_map` 预热 | 上一轮新装的启动期闸, 重灌后必须仍能建表 (159 键) |

## 5. 复跑

### 5.1 量截断规模

```bash
cd /Users/bojiangzhang/MyProject/sdtm-pedia && sdtm-rag/.venv/bin/python - <<'PY'
import re
txt = open("knowledge_base/VARIABLE_INDEX.md").read()
sec3 = txt.split("## 3. CDISC Controlled Terminology")[1]
rows = re.findall(r"^\| (C\d+) \| (\d+) \| (.+?) \|$", sec3, re.M)
trunc = [(c, int(n)) for c, n, v in rows if "total)" in v]
print(f"§三 {len(rows)} 行; 被截 {len(trunc)} 行; 隐藏 {sum(n-15 for _, n in trunc)} 条")
print("最宽:", sorted(trunc, key=lambda x: -x[1])[:5])
PY
```

### 5.2 确认生成器仍能复现已提交 KB (改之前必做)

```bash
cd /Users/bojiangzhang/MyProject/sdtm-pedia
sdtm-rag/.venv/bin/python .work/04_optimization/scripts/generate_variable_index.py /tmp/vi_regen.md
diff /tmp/vi_regen.md knowledge_base/VARIABLE_INDEX.md    # 只应有日期行 1 处差异
```

实测已确认: 唯一 diff 是 `Generated: 2026-08-07` vs `2026-08-04`。**生成器未漂移, 重生成安全。**

### 5.3 全展开的体积代价 (实测)

```bash
cd /Users/bojiangzhang/MyProject/sdtm-pedia
cp .work/04_optimization/scripts/generate_variable_index.py .work/04_optimization/scripts/_tmp_gvi.py
# 把 _tmp_gvi.py 里 `if len(refs) > 15:` 那四行换成 `refs_str = ", ".join(refs)`
# (副本必须留在原目录 — 生成器用 Path(__file__).parents[3] 定位 KB_ROOT)
sdtm-rag/.venv/bin/python .work/04_optimization/scripts/_tmp_gvi.py /tmp/vi_full.md
rm .work/04_optimization/scripts/_tmp_gvi.py
ls -l knowledge_base/VARIABLE_INDEX.md /tmp/vi_full.md
```

实测: **129.6 KB → 133.8 KB (+4.2 KB)**。补回的 226 条引用平均每条约 19 字节。

## 6. 不做

- 不动 §一 / §二 / 域变量表的任何格式 —— 它们没有截断。
- 不改 chunker (`scripts/chunkers/variable_index.py`) —— 截断在 KB 源文件, 不在切块层。
- 不往 `test_set_v3.yml` 加题 (见 §3.3)。
- 不碰 `web/` —— 站点构建指向 `milestones/release/v1.4`, 不直接读 `knowledge_base/`。
