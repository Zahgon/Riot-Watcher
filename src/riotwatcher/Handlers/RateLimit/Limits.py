import datetime
import logging
import threading

from collections import namedtuple
from typing import Iterable, Optional


LOG = logging.getLogger(__name__)

RawLimit = namedtuple("RawLimit", ["count", "limit", "time"])


class LimitCollection:
    def __init__(self):
        self._limits = {}
        self._limits_lock = threading.Lock()

    def wait_until(self) -> datetime.datetime:
        # we dont really want to update the limits as we process them
        # may be able to move the max() call outside the lock though
        pass

    def update_limits(self, raw_limits: Iterable[RawLimit]):
        pass


class Limit:
    def __init__(self):
        self._start_time = None
        self._raw_limit = RawLimit(0, 0, 0)

        self._lock = threading.Lock()

    @property
    def start_time(self) -> Optional[datetime.datetime]:
        pass

    @property
    def duration(self) -> int:
        pass

    @property
    def count(self) -> int:
        pass

    @property
    def limit(self) -> int:
        pass

    def set_raw_limit(self, raw_limit: RawLimit):
        pass

    def wait_until(self) -> datetime.datetime:
        pass
