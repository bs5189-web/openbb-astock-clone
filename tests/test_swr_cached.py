"""swr_cached 装饰器测试 — T1 占位,T2 实施。

R3.6 验收: TTL 命中 / TTL 过期返回旧值 / 显式刷新 /
装饰在 equity.py 业务函数上不破坏 st.session_state。
"""
