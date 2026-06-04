"""openbb_client — OpenBB Platform API 客户端封装

T1 骨架: 仅占位,T2 实施将填充以下模块:
  - base.py         HTTPClient: 重试 + 结构化日志 + 错误归一化
  - errors.py       ProviderError / DataUnavailableError / AuthError
  - health.py       /health 探活 + 滑动窗口失败计数 + 3 种 failure_kind
  - equity.py       行情/财务/估值接口 + 业务层 page-level 缓存
  - index.py        指数接口
  - swr_cached.py   swr_cached 装饰器 (R3.6 微调单列)
  - ta.py           技术指标本地计算 (基于 pandas_ta)
"""

__version__ = "0.1.0-skeleton"
