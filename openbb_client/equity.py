"""equity 模块 — A 股行情/财务/估值接口

T1 占位。T2 实施细节:
  - 5 个核心端点封装(equity/price/historical, equity/price/quote, equity/profile,
    equity/fundamental/metrics, equity/fundamental/balance/income/cash)
  - A 股 symbol 映射: sh -> .SS / sz -> .SZ / bj -> .BJ
  - 业务层 page-level 缓存(用 swr_cached 装饰器,不在 base.py 缓存)
  - 财务字段降级装饰器: 任一字段为 None/NaN 时返回 None + FieldUnavailable 标志位
"""

from __future__ import annotations


def get_historical_price(symbol: str, start_date: str, end_date: str | None = None) -> list[dict]:
    """A 股 K 线数据。T2 实施。"""
    raise NotImplementedError("equity.get_historical_price 由 T2 实施")
