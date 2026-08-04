"""CJK 字符 bigram 切词 — BM25 稀疏通道的日文修复.

bm25s 默认 `token_pattern=(?u)\\b\\w\\w+\\b`: Unicode 下 `\\w` 含日文, 而日文句无空白,
故整句被切成**一个 token**, 在语料中零匹配。实测后果 (study collection, golden v1.1):
BM25 单通道 gold recall 仅 12.0%, 且对纯日文查询返回近似常量的无关集合, 经 RRF 融合
挤掉真实 dense 命中。

字符 bigram 是 CJK 检索的定式: 无需词典、确定性、对未登录词稳健。同一探针实测
BM25 单通道 recall 12.0% → 60.9%。

**无条件适用的依据**: 变换只作用于 CJK 连续串, 纯拉丁文本恒等返回 —— CDISC 英文主库
的切词结果逐字节不变 (见 test_ja_tokenize.py 的不变性测试)。
"""
from __future__ import annotations

import re

# ひらがな / カタカナ (含半角ｦ-ﾟ以外の全角) / CJK 統合漢字 / 々 (踊り字) / ー (長音)
_CJK_CLASS = r"぀-ゟ゠-ヿ一-鿿々ー"
_CJK_RUN = re.compile(f"[{_CJK_CLASS}]+")


def _bigrams(run: str) -> str:
    if len(run) == 1:
        return f" {run} "      # bigram が取れない 1 文字は原字を残す (欠落防止)
    return " " + " ".join(run[i:i + 2] for i in range(len(run) - 1)) + " "


def cjk_bigrams(text: str) -> str:
    """CJK 連続串を重疊 bigram (空白区切り) に展開; 拉丁/数字/記号は原様.

    CJK を含まない文字列は**そのまま返す** (英文コーパスへの影響ゼロ)。
    """
    if not text or not _CJK_RUN.search(text):
        return text
    return _CJK_RUN.sub(lambda m: _bigrams(m.group(0)), text)
