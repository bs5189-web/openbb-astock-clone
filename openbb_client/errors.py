"""OpenBB API 错误类型 — T1 占位,T2 实施。

错误归一化:
  - ProviderError       OpenBB / 第三方 provider 返回错误
  - DataUnavailableError 字段缺失(provider 返回但字段为 None/NaN)
  - AuthError          401 / 403 — V1 不触发(认证已关闭)
"""

from __future__ import annotations


class OpenBBClientError(Exception):
    """openbb_client 所有错误的基类。T2 实施。"""


class ProviderError(OpenBBClientError):
    """OpenBB / provider 返回 5xx 或非预期 payload。T2 实施。"""


class DataUnavailableError(OpenBBClientError):
    """provider 返回 200 但关键字段为 None / NaN。T2 实施。"""


class AuthError(OpenBBClientError):
    """401 / 403 — V1 不会触发(OPENBB_API_AUTH=false)。T2 占位。"""
