"""Streamlit 多页入口 — openbb-astock-clone

A 股智能投研平台复刻。数据源: 本地 OpenBB Platform API (http://192.168.1.12:6900).

页面通过 `pages/` 目录自动发现;本文件仅配置全局设置与首页内容。
"""

import os

import streamlit as st

st.set_page_config(
    page_title="A 股智能投研平台",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded",
)

OPENBB_API_URL = os.environ.get("OPENBB_API_URL", "http://192.168.1.12:6900")

st.title("📈 A 股智能投研平台")
st.caption(f"数据源: `{OPENBB_API_URL}` — 基于 OpenBB Platform API")

st.info(
    "👈 请从左侧导航选择功能模块。\n\n"
    "- 🏠 **首页**: 平台入口与大盘概览\n"
    "- 📊 **行情看板**: 单股综合配置面板\n"
    "- 🎯 **动量回测**: 股票池 + 调仓周期 + 收益曲线\n"
    "- 📈 **投资组合**: Markowitz 风格多股票组合优化\n"
    "- 🔍 **股票查询**: K 线 + MA / RSI / MACD"
)

st.markdown("---")
st.markdown("**T1 骨架已就绪。** 后续 T2/T3 将填充 OpenBB 客户端与各页面实现。")
