# SP5 图增强校验器 — 验收 Summary (KG 重启 5/5 收官)

> 2026-07-09 · 给现有 Validator (Phase 1C, 7 规则) 接进 DESIGN §5.6 三类图增强跨域校验。
> 确定性、只读内存 `GraphEngine` (over meta.yaml)、全 advisory (WARN/INFO, 绝不 ERROR)、不碰 Neo4j。
> 单域 `/validate` 零改动零回归。spec `docs/superpowers/specs/2026-07-09-sp5-graph-validator-design.md`
> / plan `docs/superpowers/plans/2026-07-09-sp5-graph-validator.md`。

## 三类检查验收表

| 检查 | 码 | 严重度 | 语义 | 门 / 测试 | 结果 |
|------|----|--------|------|-----------|------|
| impact | GIMPACT | INFO | 变量/codelist 跨 ≥10 域 → 提示高 impact | `test_impact_*` + Rule A (USUBJID=55✓ / AETERM=1✓ / C66742=41域123变量✓) | PASS |
| cross-domain completeness | GXDOM | WARN | 提交域 RELREC-链接的**伙伴域**缺席 → 提示 | `test_completeness_*` + e2e + Rule A (AE→{CM,PR} 唯二 RELREC 边, 全 63 域扫仅 AE 触发) | PASS |
| CT cascade | GCASCADE | WARN | ≥2 域共享 codelist 的实际值集合跨域不一致 → 提示 | `test_ct_cascade_*` + e2e (AESER{Y,N} vs MHPRESP{U} → C66742 命中) + Rule A | PASS |

## 验收门 (规则 A/B/C/D)

- **程序门**: 全套 **493 passed 零回归** (单域 `validate_dataset` 函数体逐字节 IDENTICAL, 无 pre-existing 测试被触碰);
  golden 精确命中 (pass study {AE,CM,PR}=0 graph-WARN / fail study {AE,MH}=精确 GXDOM(CM)+GCASCADE(C66742));
  新码 `graph_validator.py` ruff+mypy 干净。
  > 注: plan 反复引用的 `test_validator.py`(37 测试) 实际不存在 (Rule D 订正); 零回归依据 = 493 全绿 + 端点纯追加字节未变。
- **规则 D (异 subagent_type `pr-review-toolkit:code-reviewer`, opus)**: **APPROVE_WITH_NITS, 0 BLOCKER / 0 HIGH**。
  独立复跑证 advisory-only 构造级成立 (`generate_study_json` 里 graph 侧 `g_err` 恒 0 → 图层永不把 study 顶成 FAIL)、
  单域零回归、诚实性属实且偏保守 (router 11→12 唯一新增 idiomatic B008 / report 5→**4** 反清一条旧 F401 / mypy 新增 0)。
  1 MED (M1 back-fill 死码) 已修; LOW 见下。证据 `sp5_ruleD_review.md`。
- **规则 A (异 subagent_type `general-purpose` scientist, opus)**: **PASS, 8/8 样本零 mismatch**。
  EXPECTED 侧只 `yaml.safe_load` 自建反向索引 (不 import graph_validator / 不用 MetaStore/GraphEngine 算期望),
  ACTUAL 侧跑 `run_graph_checks`, Finding 四元组逐字全串匹配 (含消息内嵌数字)。独立复算 USUBJID=55 / C66742=41/123 /
  AE RELREC={CM,PR} 全自核无误。证据 `sp5_ruleA_audit.md`。
- **规则 B**: `evidence/failures/sp5_attempt_1.md` 归档 plan 数据假设 vs 真值 5 处对齐 (MHSER 不绑 codelist / AE RELREC=CM+PR /
  pass study 非 RELREC-闭合 / Task 3 fixture 列长笔误), 实测证据附。
- **规则 C**: `RETROSPECTIVE_sp5.md` 三段齐 (保留做法 / 补缺口 / 关键决策)。

## 交付物

- `server/graph_validator.py` (新, 3 纯函数 `check_impact`/`check_completeness`/`check_ct_cascade` + `run_graph_checks`)
- `server/report.py` `generate_study_json` (study-level 聚合: verdict + 图层 findings, 纯追加)
- `server/router.py` `POST /api/validate-study` (多文件 study 校验, 单域 `/validate` 不动)
- `ui/streamlit_app.py` study 多文件上传 + 报告渲染 (现有单域上传不动)
- 测试: `test_graph_validator.py` (9) + `test_graph_validator_e2e.py` (2) + `test_report_study.py` (3) + `test_validate_study_endpoint.py` (2) + 合成 fixture `fixtures/sp5_study/`
- commits `c871b04..HEAD` (Task 1-7 + Rule D/A fix)

## 诚实缺口 (披露, 非缺陷)

1. **completeness 真实触发面极窄**: meta.yaml 全域仅 **2 条显式 RELREC 边** (AE→CM, AE→PR)。故 completeness 只在
   "提交含 AE 而缺 CM 或 PR" 时触发。检查正确, 但真实覆盖面小。
2. **back-fill 撤销 (M1 修复)**: spec §3.2 设计的 mechanism back-fill (null-mech + target∈{RELREC,RELSPEC,RELSUB}) 经数据
   核验**不适用** — 那些 null-mech 边的 target 是关系数据集本身 (LB/BS/IS/MB/MS → RELSPEC "specimen hierarchy"),
   即 target==机制而非伙伴域, 激活会产 "X RELSPEC-linked to RELSPEC, absent" 的无意义 WARN。故 completeness 收窄为
   **仅显式 mechanism=='RELREC'**, RELSPEC/RELSUB 关系不属完整性范围。真实数据行为逐字不变 (仍只 AE→CM/PR)。
3. **CT cascade 有合法误报面**: 两域对同一 codelist 合法地用不同值子集会触发 WARN。设计选择 (advisory 非 ERROR)。
4. **impact INFO 含通用标识符噪声**: STUDYID/DOMAIN/USUBJID (跨 59-63 域) 每个 dataset 必被标 GIMPACT INFO — 正确但对
   多域 study 会刷屏。未加硬编排除表 (避免 example-tuning 嫌疑), 留 dogfood 信号 (同 AGG 长尾处理)。
5. **无真实 study 数据**: 用合成 fixture {AE,CM,PR}/{AE,MH}; 真实误报率未测。
6. **每请求重建 GraphEngine** (LOW): `/validate-study` 每次 `GraphEngine(MetaStore(meta_path))`; meta.yaml 解析快, 校验端点非高 QPS, 接受。
7. **未暴露 go-live webchat / back-fill 不写回 meta.yaml** (spec §5 范围外)。
