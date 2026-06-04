"""index 模块 — 主要指数接口

T1 占位。T2 实施细节:
  - index/available?provider=yfinance        列出可订阅指数
  - index/price/historical?symbol=000300.SS  获取指数 K 线
  - 主流 A 股指数: 上证综指 000001.SS / 深证成指 399001.SZ / 创业板指 399006.SZ / 沪深300 000300.SS
"""

from __future__ import annotations


def list_indices() -> list[dict]:
    """列出可订阅指数。T2 实施。"""
    raise NotImplementedError("index.list_indices 由 T2 实施")
