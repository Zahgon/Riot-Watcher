import datetime
import logging
import threading

from typing import Dict, List, Optional

from .InternalLimiter import InternalLimiter
from .Limits import LimitCollection, RawLimit

LOG = logging.getLogger(__name__)


class HeaderBasedLimiter(InternalLimiter):
    def __init__(self, limit_header: str, count_header: str, friendly_name: str = None):
        super().__init__()
        self._limit_header = limit_header
        self._count_header = count_header
        self._friendly_name = friendly_name

        self._limits: Dict[str, LimitCollection] = {}
        self._limits_lock = threading.Lock()

    @property
    def friendly_name(self) -> str:
        pass

    def _get_limit_scope(
        self, region: str, endpoint_name: str, method_name: str
    ) -> str:
        pass

    def __get_limit(
        self, region: str, endpoint_name: str, method_name: str
    ) -> LimitCollection:
        pass

    def wait_until(
        self, region: str, endpoint_name: str, method_name: str
    ) -> datetime.datetime:
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

    def _extract_headers(self, headers: Dict[str, str]) -> Optional[List[RawLimit]]:
        pass

    @staticmethod
    def _extract_single_header(
        header: str, headers: Dict[str, str]
    ) -> Optional[List[List[int]]]:
        pass
