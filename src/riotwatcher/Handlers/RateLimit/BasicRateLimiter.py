import datetime
import logging

from typing import Dict, Optional, Tuple

from ...RateLimiter import RateLimiter

from . import (
    ApplicationRateLimiter,
    MethodRateLimiter,
    OopsRateLimiter,
    InternalLimiter,
)

LOG = logging.getLogger(__name__)


class BasicRateLimiter(RateLimiter):
    __application_rate_limiter = ApplicationRateLimiter()

    def __init__(self):
        super().__init__()

        self._limiters: Tuple[InternalLimiter, InternalLimiter, InternalLimiter] = (
            BasicRateLimiter.__application_rate_limiter,
            MethodRateLimiter(),
            OopsRateLimiter(),
        )

    def wait_until(
        self, region: str, endpoint_name: str, method_name: str,
    ) -> Optional[datetime.datetime]:
        pass

    def record_response(
        self,
        region: str,
        endpoint_name: str,
        method_name: str,
        status: int,
        headers: Dict[str, str],
    ):
        pass
