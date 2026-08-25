"""item 実収集範囲の推導 (spec §2.3): 表单分配 − 该 item 的隐藏清单.

独立成模块 (2026-08-25 Task 6; 原住 `build_field_cards.py`, Task 4 review M5 指出
生产渲染路径永远不调它, 卡片渲染器不该是这个纯推导函数的家, 依赖方向别扭)。
现由两处各自按需消费: 渲染器 (`build_field_cards.py`, 生产传 `assignments=None`
关闭 収集アクティビティ 行, spec §6 S3 退回) 与 `server/study_lookup.py` 的
`resolve_events` (类型6/item_collection_scope 问法, Task 6 接线)。
"""
from __future__ import annotations

# EDC ConfigReport 原始列名, 值是逗号/换行分隔的 activity OID 清单 (231/959 项非空,
# 231/231 全部是 activities 池里存在的 activity **OID**, 0 个是 activity 名称 —
# 已用真实数据核验, 见 task-4-review.md §5 "语义前提成立")。
_HIDDEN_ACT_KEY = "Visibility::Hidden in activity"


def collect_scope(item: dict, assignments: list[dict]) -> list[str]:
    """item 实际被采集的 activity OID (有序去重).

    = (该 item 所属 form 被分配到的 activity) − (该 item 的 Hidden in activity)
    两个输入都出自同一份 ConfigReport, 故本推导是确定性的, 无推断成分。

    返回 `[]` 有两种诱因, 调用方不得混淆: ①该 item 所属 form 在 `assignments` 池里
    确实零分配 (真实数据 0 例, 见 `test_collect_scope_empty_when_form_has_no_assignments`
    的合成 fixture — Task 4 review M4); ②该 form 的全部分配恰好都在隐藏清单里。两者
    对本函数而言无区别 (都是合法的"哪里都不采集"), 但调用方 (如 `resolve_events`)
    若把"没查到任何命中"也表现成同一个 `[]` 空返回, 会让"确实哪都不采"与"没查到
    这个 item / 上游数据缺失"在外部不可区分 —— 这是已知限制, 需在消费方 checkpoint
    里记录, 不是本函数的缺陷。
    """
    # `.get("raw") or {}` 而非 `item["raw"]`: 生产 catalog 恒有 raw 键 (asdict() 输出),
    # 但 resolve_events (2026-08-26 修复轮1) 让本函数首次被"任意手搭 fixture"调用到
    # (测试文件里已有十几处不带 raw 的手搭 item), 缺 raw 键应视同无隐藏清单, 不该 KeyError
    # (规则 D 审查方实测复现 KeyError 场景, 见 task-6-report.md 修复轮1记录)。
    hidden = {
        x.strip()
        for x in str((item.get("raw") or {}).get(_HIDDEN_ACT_KEY) or "").replace("\n", ",").split(",")
        if x.strip()
    }
    out: list[str] = []
    for a in assignments:
        if a["form_oid"] != item["form_oid"]:
            continue
        oid = a["activity_oid"]
        if oid and oid not in hidden and oid not in out:
            out.append(oid)
    return out
