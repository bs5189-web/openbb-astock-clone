"""ta 模块 — 技术指标本地计算(基于 pandas_ta)

T1 占位。T2 实施细节:
  - calc_ma(close, periods=[5, 10, 20])     简单移动平均
  - calc_rsi(close, period=14)              RSI
  - calc_macd(close, fast=12, slow=26, signal=9)  MACD
  - calc_volume_indicators(ohlcv)           成交量指标(V1 不强需)
"""

from __future__ import annotations

import pandas as pd


def calc_ma(close: pd.Series, periods: list[int] | None = None) -> pd.DataFrame:
    """简单移动平均。T2 实施。"""
    raise NotImplementedError("ta.calc_ma 由 T2 实施")


def calc_rsi(close: pd.Series, period: int = 14) -> pd.Series:
    """RSI(14)。T2 实施。"""
    raise NotImplementedError("ta.calc_rsi 由 T2 实施")


def calc_macd(
    close: pd.Series, fast: int = 12, slow: int = 26, signal: int = 9
) -> pd.DataFrame:
    """MACD(12, 26, 9)。T2 实施。"""
    raise NotImplementedError("ta.calc_macd 由 T2 实施")
