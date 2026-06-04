"""degraded_banner — OpenBB 故障降级 UI 组件

T1 占位。T2 实施细节:
  - 顶部 banner: 橙色背景 + "数据可能延迟 5min" + trace_id
  - 严重降级: 主面板替换为"系统维护中,预计 < 5min 恢复"占位
  - 与 health.py HealthState 联动
  - 健康恢复后自动消失
"""

from __future__ import annotations

import streamlit as st


def render_top_banner(trace_id: str | None = None) -> None:
    """第一层降级: 顶部 banner 提示数据延迟。T2 实施。"""
    raise NotImplementedError("render_top_banner 由 T2 实施")


def render_severe_degradation() -> None:
    """第二层降级: 严重降级占位。T2 实施。"""
    raise NotImplementedError("render_severe_degradation 由 T2 实施")
