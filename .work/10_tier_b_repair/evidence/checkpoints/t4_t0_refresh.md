# T4: T0 变异验证在现 KB 上重新证明 (G-TB9)

<!-- chain: E (plans) -->
> 状态: **写作者稿: ALL MATCH (exit 0), 2026-11-27**; 独立审查结论见文末. KB 未改 (只在 `work/scratch/t0_head/` 的临时副本上变异).
> 关闭的缺口: 总闸 attempt 2 G-TB9 "t0_mutation 在现 KB MISMATCH → table_census / fp_match 在现 KB 无 '变红再复原' 证明".
> 写作者 = 主控 (脚本 + 本文); 其中 **M4a 换靶是主控决定 M-8, 待主人追认** (见 §3; 提问在 `t4_owner_decisions_round2.md` 问题 5).

## 1. 查清的原因: 不只是基线过期

`work/t4/t0_mutation_thaw.log` (解冻后 KB 上跑原脚本 `scripts/t0_mutation.sh`) 的 MISMATCH 有三个来源:

| 来源 | 表现 | 涉及用例 |
|---|---|---|
| 基线过期 | M0 / RESTORE 也是 `got=[1 1 1]`: T0 基线是 2026-11-25 的 KB 和台账, 之后 82 批改过 KB | 全部 |
| 变异没施加 | 脚本按写死的行号断言目标行, KB 行号变了 → `AssertionError`, 文件没改 | M2 / M2b / M2c / M2d / M3 / M4d |
| 被断言的 KB 状态已不存在 | M4d0 断言 "MB Ex3 relrec 缺表" (T2 已补表); M4a 改的是 MB 第二份副本 (D2 去重后只剩一份) → `IndexError` | M4 setup (M4d0) / M4a |

所以只重建基线不够: 那样 M0 / RESTORE 转绿, 但 6 个变异仍没施加.

## 2. 做了什么

- 新脚本 `scripts/t4/t0_mutation_head.sh`; 原脚本 `scripts/t0_mutation.sh` 与 T0 基线 (`work/fp_baseline.jsonl`, `work/section_coverage.wc.baseline.jsonl`, `work/census_BPCPP.v2.json`, `work/census_mut_{MB,EG}.v2.json`) **原样保留**. 其中 `fp_baseline.jsonl` 与 `section_coverage.wc.baseline.jsonl` 还被 T3 / T4 脚本读 (`t3_direct_hit.py`, `t3_writeback.py`, `s0_*.py`, `t3_mutation.sh`, `t4_sample.py`; T3 复跑命令预期 "regressions=72" 就是相对 T0 基线), 覆盖会破坏它们; 三个 census 基线只有原 `t0_mutation.sh` 自己读 (`scripts/helpers/regen.sh` 会重写它们), 保留是为了原脚本与 T0 记录可对照 (规则 B).
- 现 KB 基线写到新目录 `work/t4/t0_head/` (在真 KB 上只读生成): `fp_baseline.head.jsonl` / `section_coverage.wc.head.jsonl` / `census_BPCPP.v2.head.json` / `census_mut_{MB,EG,REL}.v2.head.json`.
- 三道闸 (fp_match / table_census / t3_recompute) 的调用与原脚本相同, 只换基线路径; fp_match 加 `--sections work/section_coverage.wc.baseline.jsonl` (HANDOFF 规程).
- 每个变异目标改为**按内容定位** (唯一命中, 或在指定标题之下), 不再用行号.
- 新增一道检查: 变异脚本没跑到底 (定位不到 / 断言失败) → 该用例记 "mutation applied: NO" → 整体 MISMATCH. 原脚本只把 AssertionError 打进日志, 靠三道闸的退出码间接发现. 这道检查**只管 "定位失败"**, 管不了 "改了等于没改" (空操作也会记 yes); 后者仍靠三道闸的退出码与定点断言抓 (独立审查的反向验证 rev1: 把 M2 / M4a 改成空操作 → `applied: yes` 但结果 MISMATCH).
- 依据: `t0_mutation.md` §6.3 已预告 "T2 补上该表后此断言会失败 → 届时改断言并重做 v2 基线"; 该文档连同 T0.4 结果在 2026-11-25 经用户 ack (`t0_user_ack.md`). 重做基线属于预告过的维护, 不改闸的定义与红绿判据.

## 3. 逐用例: 与 T0 是否同一目标

| 用例 | T0 的目标 | 现在 | 性质 |
|---|---|---|---|
| M0 / RESTORE | 原样副本 | 同 | 同 |
| M1 | ch01 一句 (原子 `ig34_p0008_a022`) | 同一句 (文件内唯一) | 同目标 |
| M2 | PC/examples Ex1 Method C relrec 第 5 行 IDVARVAL 4→9 (T0 行 78) | 同一行, 定位改为 "第二个 `### Example 1` 之下的 `#### Method C` 段内" (现行 131; 该行文本在 Ex2 Method C 还有一处, 故须按标题限定) | 同目标 |
| M2b | PC/assumptions relrec 第 1 行 MANY 挪到空的邻格 | 同一行 (现行 35, 唯一) | 同目标 |
| M2c | PC/assumptions pc.xpt 第 13 行 PCORRES 10→11 (折行记录) | 同一行 (现行 73) | 同目标 |
| M2d | PC/examples Ex1 Method D relrec 第 20 行删除 | 同一行 (现行 172, 唯一) | 同目标 |
| M3 | 删 ch04 `#### 4.5.1.2 Tests Not Done` 整节 (T0 37 行) | 同一节, 按两个标题定位 (现 39 行) | 同目标 |
| M4b / M4b2 / M4c / M4c2 / M4e | EG/examples Ex3 表第 1 / 5 / 10-24 行 | 同行同改法, 按行内容定位 (表头行仍是 :62) | 同目标 |
| M4d0 | 真 KB 性质: MB:229 (副本 2 的 Ex1 relrec) 配 PDF Ex1, 且 PDF Ex3 relrec = PDF_ONLY (当时的 KB 缺陷) | 改为: MB 的 Ex1 relrec 配 PDF Ex1 (p257), Ex3 relrec 配 PDF Ex3 (p263), 两者都没有 PDF_ONLY | **按 `t0_mutation.md` §6.3 预告改的断言** (不是新决定) |
| M4d | 删 MB **两份** Ex2 suppbe.xpt → 该 PDF 表应成 PDF_ONLY | 删 Ex2 下**唯一一份** suppbe.xpt → 同断言 | 同一张表, 份数随 D2 去重从 2 变 1 |
| **M4a** | 模式 (a) "每份 KB 副本都要查": 只改 MB 副本 2 的 suppbe 第 1 行, 副本 1 不动 | MB 已无第二份副本. **换靶**: PDF p431 relrec Ex1 在 KB 有两份 (D7: `chapters/ch08_relationships.md:164` 与 `domains/RELREC/examples.md:63`); 只改 ch08 那份第 2 行 RELTYPE MANY→ONE. 断言: ch08 那张表报该格差异且基线里没有; RELREC 那份仍 OK | **换靶 = 主控决定 M-8, 待主人追认** (与 attempt 2 的 M-5 同类). 新增 census 配置 `--pages ig34:427-431` + 基线 `census_mut_REL.v2.head.json` |

## 4. 结果

```bash
cd /Volumes/DevSSD/Project/sdtm-pedia
bash .work/10_tier_b_repair/scripts/t4/t0_mutation_head.sh --make-baseline     # 只读; 打印 6 个基线文件 md5
bash .work/10_tier_b_repair/scripts/t4/t0_mutation_head.sh > .work/10_tier_b_repair/evidence/checkpoints/t0_mutation_head.log 2>&1; echo $?   # 0
```

日志 `t0_mutation_head.log` 末尾 (HEAD `d46f8af` 的 KB, 树 `63f857774a42cfaa71798705ad40ab51bc5e378a`):

```
MUTATIONS APPLIED: M1 M2 M2b M2c M2d M3 M4a M4b M4b2 M4c M4c2 M4e M4d — 13/13 yes
M0       expect=[0 0 0] got=[0 0 0] OK
M1       expect=[1 0 1] got=[1 0 1] OK      (fp regressions=1 → t3 §1.4 密度 1.0 → 0.9333)
M2       expect=[0 1 0] got=[0 1 0] OK      (census PC/examples.md 表 :125 第 5 行 IDVARVAL KB 9 / PDF 4)
M2b      expect=[0 1 0] got=[0 1 0] OK
M2c      expect=[0 1 0] got=[0 1 0] OK      (折行记录 PCORRES KB 11 / PDF 10)
M2d      expect=[0 1 0] got=[0 1 0] OK      (PDF_ROW_MISSING 第 20 行)
M3       expect=[1 0 1] got=[1 0 1] OK      (fp regressions=23 → t3 §4.5.1.2 SKELETON_ONLY)
RESTORE  expect=[0 0 0] got=[0 0 0] OK
M4a..M4d v2=1(expect 1) assert=0(expect 0) OK ×7   (v1: M4b / M4b2 GREEN-blind, 其余 RED)
M4d0     pairds relrec.xpt ex 1 → (:26, OK, p257); ex 3 → (:222, OK, p263); PDF_ONLY 无 — PASS ×2
RESTORE census v2 MB / EG / REL vs baselines: GREEN GREEN GREEN
MUTATION RESULT: ALL MATCH (exit 0)
real KB md5 before = after e2d862e25f04a3757a5ba5436092c416; git status knowledge_base/ archive/ releases/ 空
```

(上面 "MUTATIONS APPLIED" 一行与括号里的说明是主控对日志相应段落的压缩; 逐行原文见日志.)

基线 md5 (`--make-baseline` 输出): fp `5126f4bd388b30e83cd7858d0421d903` / section_coverage `ad9a6dadd45288bd5aa9f54c651ee4d1` / BPCPP `9ea5a2c9f49ddbbfe985f3f6d10d0d66` / MB `f3a24f55889750ab07f213fff9d8c662` / EG `2d54e7858455b3bb1e6c50c5d1b70e38` / REL `c367be79a975880f11eafd0312c81382`.

## 5. 限制 (如实)

- 基线绑定当前 KB 与当前台账 (`coverage_ledger.wc.jsonl` md5 `60729f7b…`). KB 或台账再改 (例如 `t4_relabel_pending.md` 的改标执行后) 须重跑 `--make-baseline` 再跑一遍变异.
- fp_match 仍只能检出 "基线里命中、现在没命中" 的原子 (`t0_mutation.md` §3 限制 2 未变); t3 侧的直接命中与锚点变异由 `scripts/t3/t3_mutation.sh` 负责 (HEAD 上 M0/M2/M7 绿、M1/M3-M6 红, 见 `t4_gate_review.md` §attempt 2 主控补跑).
- M4a 换了靶; 原靶 (同一文件内的第二份副本) 这种形态在现 KB 的 MB / EG 单元里已不存在, 新靶是跨文件的两份副本.
- fp_match 的 `--sections` 仍用 T0 的 `section_coverage.wc.baseline.jsonl` (只取其中 "节 → 目标文件" 的映射), 所以现基线的取靶范围同样绑定在 T0 的节划分上.
- 脚本里的 `kbsum` 只算 `*.md` (真 KB 目录下另有一个未跟踪的 `.omc`); 独立审查另用全文件 md5 清单 + `cmp` 证明运行前后 KB 无变化.

<!-- REVIEW -->
## 独立审查 (誊录; 审查者 `oh-my-claudecode:verifier` opus, 只读, 2026-11-27; 对象 HEAD `1df9f60`; 主控不改判)

**结论 (A 部分 = T0 变异重证): CONDITIONAL** — 技术上通过; 条件 = M4a 换靶 (M-8) 待主人追认 + 下列 LOW 项文字更正 (已在上文按意见改). HIGH 0.

审查者做的事 (原话摘要):
- 自己复跑 `t0_mutation_head.sh`: exit 0, 耗时 1:13; 与本目录 `t0_mutation_head.log` 逐行 diff, 唯一差别是写作者日志末行的 `exit=0`. 13/13 applied; EXPECT 8/8 OK; M4 7/7 OK; M4d0 PASS ×2; RESTORE 三个 GREEN; 6 个基线 md5 与 §4 相同.
- 真 KB: 运行前后用全文件 md5 清单 + `cmp` → 不变.
- 反向验证 2 组 (脚本拷到 scratch 改写): rev1 把 M2 与 M4a 改成空操作 → `M2 got=[0 0 0] MISMATCH`、`M4a v2=0 assert=1 MISMATCH`, exit 1; rev2 让 M2c 定位不到、把 M4a 改到 RELREC 那份 → `M2c mutation applied: NO` → MISMATCH, M4a 的 cell 断言与 `ok RELREC` 断言都 FAIL, exit 1.
- 逐用例对照 T0 提交 `e3c2f5d` 的 KB: M1 / M2 / M2b / M2c / M2d / M3 / EG 各例都是同一句 / 同一行 / 同一节 (M3 37 行 → 39 行, 多的 2 行是 KB note); M4d0 的改法与 `t0_mutation.md` §6.3 预告一致; M4d 是同一张 Ex2 suppbe; M4a 的两份确为同一张 PDF 表 (p431 relrec Ex1) 的两份 KB 副本, 断言确实检验了 "只改一份". **没有发现换了目标却写成同目标的用例.**
- expect() 与 M4 判据与原脚本逐字相同, 没有放宽; 基线与被测对象不是同一个文件.

发现 (全部 LOW; 编号沿用审查报告): #10 §2 "还在读" 对三个 census 基线不成立 (已改); #11 "mutation applied" 的检查能力写过头 (已改); #12 §5 漏两条限制 (已补).
审查报告全文 (含 B 部分) 的誊录见 `t4_c3_closeout.md` 文末; 审查者的脚本与日志在 gitignored 的 `work/scratch/review_a/`.
