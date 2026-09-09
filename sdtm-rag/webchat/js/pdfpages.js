// C2R 画面 PDF 旁路 (I2-4): done 事件 / AskResponse 的 `pdf_pages` · `pdf_trigger` → 可渲染形状。
// 纯函数、零 DOM —— render.js 要整套 DOM shim 才跑得起来, 这层单拆出来才测得动 (同
// citations.js 与 render.js 的分工)。
//
// 后端 (server/router.py maybe_attach_pdf_pages) 的三态在这里必须原样保留:
//   trigger=null, pages=null → 通道关 (默认) 或规则未命中。**什么都不画**: DOM 与本功能
//                              上线前逐字节相同, 这是"默认关"这条承诺在前端的落点。
//   trigger="R1", pages=[]   → 规则命中但一页都没画出来 (pdftoppm 缺失等)。后端特意不把它
//                              塌成 null (M4), 前端也不能: 否则"没触发"与"触发了但图没生成"
//                              在界面上长得一模一样, 用户与排障的人都无从分辨。
//   trigger="R1", pages=[…]  → 实际附上的页。答案正文里「画面目視判読 p.NN」的出处就是这些
//                              页, 这一行是把那句话对回具体 PDF 页的**唯一**记录 (M3)。
//
// 规则文案取自 server/pdf_trigger.py 的 R1/R2/R3。改那边的判据时这里要一起改 —— 说错触发
// 理由比不说更坏, 用户会照着一个不存在的规则去解释为什么这次附了图。
export const PDF_RULE_HINT = {
  R1: "R1: 命中卡片含 ≥2 个非显示活动 × 提问带时点/差异类词 (visit / 時点 / 違い …)",
  R2: "R2: 命中卡片含条件式来自别处的项目 × 提问带条件/显示类词 (条件 / いつ / 表示 …)",
  R3: "R3: 提问带画面/布局类词 (画面 / レイアウト / 並び …) × 命中卡片过关联性下限",
};

const LEAD_PAGES = "画面页附图";
const LEAD_NONE = "画面页: 未附图 (渲染失败)";
const HINT_PAGES = "答案里「画面目視判読 p.NN」的出处就是以下页。";
const HINT_NONE = "触发规则命中, 但没有一页渲染成功, 本次答案不含画面判读依据。";

// `{pdf, page}` → "annotated p.174"。元素级形状由后端保证 (那里是
// `{"pdf": i.pdf, "page": i.page}`, ImagePart 的字段是 str/int), 故这里不加逐元素防御 ——
// 为不可达路径写防御, 下一个人会以为它可达 (同 render.js modelBadgeText 的注释)。
export function pdfPageLabel(p) {
  return `${p.pdf} p.${p.page}`;
}

// ⚑ 上报用的一行摘要; 无页时返回空串 (调用方据此决定加不加这一行)。
export function pdfPagesSummary(pdfPages) {
  if (!Array.isArray(pdfPages) || !pdfPages.length) return "";
  return pdfPages.map(pdfPageLabel).join(", ");
}

// 返回 null = 什么都不画。⚠ `Array.isArray` 是**容器级**契约闸, 与 modelBadgeText 同一理由:
// 后端发回什么形状不由前端说了算 (onDone 是 `?? null`, 零形状校验), 而这里一抛异常死的不是
// 一行徽章, 是整段对话历史渲染不出来。
export function pdfAttachView(pdfPages, pdfTrigger) {
  const rule = typeof pdfTrigger === "string" && pdfTrigger ? pdfTrigger : null;
  const hint = (rule && PDF_RULE_HINT[rule]) || "";
  const pages = Array.isArray(pdfPages) ? pdfPages : null;
  if (pages && pages.length) {
    return {
      mode: "pages",
      lead: LEAD_PAGES,
      chips: pages.map(pdfPageLabel),
      rule: rule ? `规则 ${rule}` : "",
      hint: hint ? `${HINT_PAGES}\n${hint}` : HINT_PAGES,
    };
  }
  // 规则命中却没有页 —— 空列表 (描画全失败) 与"通道压根没动"必须分开说 (M4)。
  if (rule) {
    return { mode: "none", lead: LEAD_NONE, chips: [], rule: `规则 ${rule}`,
             hint: hint ? `${HINT_NONE}\n${hint}` : HINT_NONE };
  }
  return null;
}
