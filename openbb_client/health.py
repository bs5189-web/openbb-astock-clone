"""健康检查 — OpenBB API 健康状态机

T1 占位。T2 实施细节:
  - check()                调用 /health 端点,200 视为健康
  - record_failure(kind)   累计连续失败次数,3 次触发降级
  - record_success()       单次成功即恢复 (R3.4, 不要求连续 2 次)
  - is_degraded()          UI 层查询接口

R3.4 — failure_kind 三种:
  - 'http_error'       非 2xx 响应
  - 'retry_exhausted'  重试 3 次后仍失败
  - 'timeout'          单次请求超时

60s 滑动窗口,连续 3 次失败后切严重降级。
"""

from __future__ import annotations

from typing import Literal

FailureKind = Literal["http_error", "retry_exhausted", "timeout"]


class HealthState:
    """OpenBB API 健康状态机(T1 占位,T2 实施)"""

    def __init__(self, window_seconds: int = 60, failure_threshold: int = 3) -> None:
        self.window_seconds = window_seconds
        self.failure_threshold = failure_threshold

    def check(self) -> bool:
        """调用 /health 端点探测可用性。T2 实施。"""
        raise NotImplementedError("HealthState.check 由 T2 实施")

    def record_failure(self, kind: FailureKind) -> None:
        """累计一次失败,达到阈值触发降级。T2 实施。"""
        raise NotImplementedError("HealthState.record_failure 由 T2 实施")

    def record_success(self) -> None:
        """重置失败计数(R3.4: 单次成功即恢复)。T2 实施。"""
        raise NotImplementedError("HealthState.record_success 由 T2 实施")

    def is_degraded(self) -> bool:
        """UI 层查询: 当前是否处于严重降级状态。T2 实施。"""
        raise NotImplementedError("HealthState.is_degraded 由 T2 实施")
