"""HTTPClient — OpenBB Platform API HTTP 调用的基础类

T1 占位。T2 实施细节:
  - 集中超时 + 指数退避重试(3 次 + 抖动)
  - 集中错误归一化(ProviderError / DataUnavailableError / AuthError)
  - 结构化请求日志(symbol / endpoint / 耗时 / 状态码 / trace_id)
  - 客户端不做缓存(缓存下沉到业务层 / swr_cached 装饰器)
"""

from __future__ import annotations

from typing import Any


class HTTPClient:
    """OpenBB API 调用的薄 wrapper 基础类(T1 占位,T2 实施)"""

    def __init__(self, base_url: str, timeout: float = 10.0) -> None:
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

    def request(self, endpoint: str, params: dict[str, Any] | None = None) -> Any:
        """发送 HTTP 请求并返回 (data, response_meta) 二元组。T2 实施。"""
        raise NotImplementedError("base.HTTPClient.request 由 T2 实施")
