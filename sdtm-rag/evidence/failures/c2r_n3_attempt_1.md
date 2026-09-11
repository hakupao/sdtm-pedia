# C2R N3 attempt 1 — gpt 家整体 FAIL (2026-09-11)

> 归档理由: 规则 B。PLAN §8 四条判据 gpt-terra 全 PASS, gpt-sol ③④ FAIL ⇒ 预登记口径下 gpt 家 FAIL。判分点未改。
> 判分: `evidence/step_c2r_n3_audit.md` (非作者 judge, 规则 A 60 条全量); 真值明细 gitignored `data/study/st01/eval/runs/c2r_n3/audit_detail.md`。

## 输入
- 代码: N3 (label 附项目组序列 + 「前頁からの続き」+ 元数据段「頁索引メタ:」+ prompt 第 3 条), 复审 PASS 后的版本 (工作树, 未提交时刻 14:33)。
- 复测: B 臂 T1/T3/T6 × gpt-terra/gpt-sol, 6/6 成功, 页集与 N1 逐字相同, 路由 `both` (与 N1 同)。
- 闸: `check_visual_grounding.py c2r_n3` → 40 单元, LABEL_ATTRIBUTED 0, OFF_PAGE 1 (judge 判假阳性: 否定极性)。

## 产物 (分数, 满分 12)
| 模型 | N1 | N3 | 变化 |
|---|---|---|---|
| gpt-terra | 9 | **10** | T6 ② 0→1 |
| gpt-sol | 9 | 9 | T6 ② 0→1; T1 ⑤ 1→0 |

主张 census: 60 条 verified 57 / contradicted 2 / unverifiable 1 (N1: 53 条 47/5/1)。

## 技术判定
- N3 瞄准的两类错误**都修好了**: N1 的四处面板合并靶点两模型全部分开; LABEL 型元数据挂画面 0 条; 无人把「前頁からの続き」当本页可见见出し; 『頁索引』8 条归因方向零错误。
- 判据 ①② 本轮在**真正犯过该错的模型**上有判别力 (与 N1 不同)。

## 业务判定 (FAIL 的两条, 均 gpt-sol)
- ③ T1 ⑤ 1→0: 标准维引用从 2 条变 0 条, 答案反而变长 612 字符, 非篇幅挤压; 与 N3 改动无直接关系 (n=1, 可能是噪声, 也可能是 prompt 变长挤掉了标准维)。
- ④ 面板合并 2 条 (T1 ann p.174 把有题面板与紧随的无题面板合并 —— 该页 label 已写明组序列, 模型未读; T6 ann p.161 对「前頁に続く」作无证据推测)。第一条是相对 N1 的倒退, 且发生在组序列首次覆盖到该页时 —— 对 N3 的因果故事是反证。

## 附带发现 (非本单元判据)
- 页索引缺陷: 2 字母 item OID 撞上邻页日文标题前缀 ⇒ p.162 组项目数高估 1 (gpt-sol 如实指出不一致; gpt-terra 引错数未说明)。已派修 (pattern 级: OID 徽章形态约束)。
- N2 闸新盲点: 否定极性 (「这页不是本题表单」被标 OFF_PAGE)。记入闸证据 §6, 不放宽判据。
- N1 审计一处真值更正: ann p.161 是面板起始页而非续页 ⇒ N1 gpt-terra T6 主张层 26/27 → 25/27 (分数不变)。

## 下一 attempt 的输入 (登记于 PLAN §8 attempt 2)
1. 先落地索引缺陷修复 (确定性, 不改 prompt)。
2. 同一 prompt 重跑 gpt-sol + gpt-terra 各一次 (n=2) 以分辨 ③ 是否噪声; 判据不改。
3. 若 ④ 的「无视 label 组序列」在 n=2 上复现, 才考虑 prompt 层改动 (须按 pattern 登记, 不对着 p.174 写)。
4. opus-5 补跑 (供给恢复后) 仍是默认 ON 的硬前置。
