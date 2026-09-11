# C2R N3 — annotated label 项目组序列 + label 元数据出处分离 (2026-09-11)

> 状态: **工程 DONE + 复审 PASS (二轮) + 复测 a1/a2 各归档 (预登记口径 gpt 家 FAIL, 但靶向错误已修好且两模型 10/12)**; 默认 OFF 不动; prompt 层改动未触发
> PLAN §8 · 判分 `evidence/step_c2r_n3_audit.md` · 归档 `evidence/failures/c2r_n3_attempt_1.md` · 闸 `evidence/checkpoints/c2r_n2_visual_grounding.md`

## 1. 改了什么 (6 文件, +377 −22; 检索/选页/触发/SSE 零改动, AST 函数级哈希与 HEAD 比对)
- `scripts/study/build_pdf_page_index.py`: 新字段 `annotated.page_groups[form][page] = [{group_oid, name, n_items, continued}]` (catalog `row` 序 × `item_pages`; `continued` = 该组在同 form 更早页已有定位项目)。真索引重生成: 仅新增该字段 + 时间戳; 85 页 / 153 条 / continued 29 (名前付き 25, 全部见出し不在续页 — 对照本页起始枠 59/65 有见出し)。
- `server/pdf_context.py`: `PdfPageIndex.page_groups` (旧索引缺字段 → 静默不加注, 启动一次性提示); `_with_index_meta` 把块范围 / 同一画面 / 组序列集中到 label 尾段「頁索引メタ:」; 组序列仅 ≥2 组时写, 无名组 `(無題)`, 续枠 `[n 項目・前頁からの続き]`; 组 OID 不进 label (文本层出现 0/153)。
- `server/router.py` `_PDF_SOURCE_RULE` 第 3 条: 頁索引メタ非画像事实, 引用出典『頁索引』; 組順 = 枠境界, 無題枠独立; 前頁からの続き = 見出しは前頁。第 2 条引用形与两类 label 逐字节统一 (『p.a–b のうち本頁 p.x』)。
- 测试 +19 (2230 → 2249 本单元; 全量含 N2 闸 2316 passed); 复审 9 次变异全部被抓 (1 次由不相干测试兜住 → 已改判别性测试)。

- **索引缺陷修复 (attempt 1 后)**: 2 字母 item OID 撞邻页日文标题前缀 → `_is_badge_hit` (徽章两侧不得紧邻非 ASCII; 实测候选规则 A 落掉 2 对/0 真命中损失, 规则 B「列独立」会误杀 52 真徽章故弃)。索引 delta: (item,页) 942→940, page_groups 153→152, continued 29→28, 发火页 40→39; p.162 组数 8→7 (judge 所见), p.7 凭空的 1 项目续枠消失。1 个 item 由「唯一一页 = 误命中」变为不定位 (走表单首页降级)。

## 2. 复审 (规则 D, code-reviewer opus, 两轮)
第一轮 **FAIL**: 续页组被当成本页独立枠而见出し不在本页 (真索引 25/25 续枠见出し缺失) → 加 `continued` 标记 + label 后缀 + 规则句。第二轮 PASS。另 MINOR-3 判别力 / MINOR-4 口径统一 / 7 NIT 全修。

## 3. 复测 attempt 1 (B 臂 T1/T3/T6 × gpt-terra/gpt-sol; opus-5 挂起)
```bash
cd sdtm-rag
nohup env SDTM_RAG_AUTH_ENABLED=false SDTM_RAG_PDF_CONTEXT_ENABLED=true .venv/bin/uvicorn server.main:app --port 8011 > /tmp/armB_8011.log 2>&1 &
until curl -s -m 2 localhost:8011/api/health >/dev/null; do sleep 1; done
.venv/bin/python scripts/study/c2r_eval/run_v3.py --group T --arms B --models gpt-terra,gpt-sol --qids T1,T3,T6 --timeout 900 --out c2r_n3
.venv/bin/python scripts/study/c2r_eval/tabulate_v3.py c2r_n3
.venv/bin/python scripts/study/c2r_eval/check_visual_grounding.py c2r_n3
```
| 判据 (PLAN §8) | gpt-terra | gpt-sol |
|---|---|---|
| ① T6 ② ≥ N1 | PASS (0→1) | PASS (0→1) |
| ② 闸 LABEL_ATTRIBUTED = 0 | PASS | PASS |
| ③ T1/T3 逐点 ≥ N1 | PASS | **FAIL** (T1 ⑤ 1→0) |
| ④ 同型 contradicted = 0 | PASS | **FAIL** (面板合并 2) |

分数 gpt-terra 9→10, gpt-sol 9→9; 主张 60 条 verified 57 / contradicted 2 / unverifiable 1 (N1 47/5/1)。**N3 靶向的两类错误在两模型上都修好了**; FAIL 来自 gpt-sol 的标准维引用消失 (n=1) 与两处新的面板判断错误 (其一无视 label 已给的组序列)。细节与下一 attempt 输入见 failures 归档。

## 4. 诚实边界
- 判据 ①② 本轮有判别力 (被测模型正是犯过该错的模型); 与 N1 相反。
- 『頁索引』被两模型只在 T6 引用; T1 的组序列/同一画面清单无人读, T1 ③ 仍双双 0。元数据「在」≠「被用」。
- 元数据的错误会被原样转述 (索引缺陷 → label 8 項目 vs 实画 7)。
- 路由 `both` (供给侧), opus-5 未测。

## 5. attempt 2 (索引修复后同 prompt 重跑, n=2)
```bash
.venv/bin/python scripts/study/c2r_eval/run_v3.py --group T --arms B --models gpt-terra,gpt-sol --qids T1,T3,T6 --timeout 900 --out c2r_n3_a2
.venv/bin/python scripts/study/c2r_eval/check_visual_grounding.py c2r_n3_a2
```
| 判据 | gpt-terra | gpt-sol |
|---|---|---|
| ① | PASS | PASS |
| ② | **字面 FAIL** (闸 1, 核验假阳性) | PASS |
| ③ | PASS | PASS (a1 掉分 = 噪声) |
| ④ | **FAIL** (带对冲的跨页推测 1) | PASS |

两模型均 10/12; 46 条主张 45 verified / 1 contradicted。a1 的 gpt-sol 两条同型未复现 ⇒ prompt 改动未触发。FAIL 换了模型 ⇒ 残余失败为共享失败库。下一 PATTERN (N4 候选, 须 brainstorm+预登记): 元数据沉默维度被视觉推测填补 → 让 label 在沉默维度显式声明状态。归档 `evidence/failures/c2r_n3_attempt_2.md`, 判分 `evidence/step_c2r_n3_a2_audit.md`。
