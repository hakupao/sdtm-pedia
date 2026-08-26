#!/bin/sh
# 启用本仓的 git hooks (一次性)。core.hooksPath 是 local config, 不随 clone 传播。
set -e
cd "$(git rev-parse --show-toplevel)"
git config core.hooksPath .githooks
echo "已启用: core.hooksPath = $(git config core.hooksPath)"
echo "停用:   git config --unset core.hooksPath"
