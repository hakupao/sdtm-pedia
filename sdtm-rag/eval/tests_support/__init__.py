"""可复用的开发期探针 (非 pytest 用例, 手动跑)。

这里的脚本不进 pytest 收集范围: 它们要么起子进程、要么调 git、要么耗时以分钟计,
不适合放进常规测试。放这里是为了**不随 scratchpad / SDD workspace 消失**。
"""
