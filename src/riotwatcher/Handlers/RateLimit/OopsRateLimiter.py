import datetime
import logging

from typing import Dict

from .InternalLimiter import InternalLimiter

LOG = logging.getLogger(__name__)


class OopsRateLimiter(InternalLimiter):
    def __init__(self):
        super().__init__()
        self._friendly_name = "429_Limit"
        self._retry_at = None

    @property
    def friendly_name(self) -> str:
        pass

    def wait_until(self, region: str, endpoint_name: str, method_name: str) -> datetime:
        pass

    def update_limiter(
        self,
        region: str,
        endpoint_name: str,
        method_name: str,
        status: int,
        headers: Dict[str, str],
    ):
        pass
