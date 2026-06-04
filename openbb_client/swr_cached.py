"""swr_cached 装饰器 — Stale-While-Revalidate 缓存

T1 占位。T2 实施细节:
  - 接受 ttl / refresh_on_error 等参数
  - 业务层 equity.py 用它替代内联 @st.cache_data
  - 行为: 命中返回缓存;TTL 过期返回旧值并触发后台刷新;刷新失败返回旧值 + 记录 failure
  - 与 health.py 状态机联动(刷新连续 3 次失败 → is_degraded 触发)
  - 不破坏 st.session_state(Streamlit 行为,装饰在普通函数上)
"""

from __future__ import annotations

from typing import Any, Callable


def swr_cached(ttl_seconds: int = 300, refresh_on_error: bool = True) -> Callable[[Any], Any]:
    """SWR 装饰器。T2 实施。"""

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        raise NotImplementedError("swr_cached 由 T2 实施")
        return func

    return decorator
