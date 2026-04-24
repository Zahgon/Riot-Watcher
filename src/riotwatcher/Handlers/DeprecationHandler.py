import logging
from datetime import datetime

from requests import Response

from . import RequestHandler

LOG = logging.getLogger(__name__)


class DeprecationHandler(RequestHandler):
    def __init__(self):
        super().__init__()
        self._warned = set()

    def after_request(
        self,
        region: str,
        endpoint_name: str,
        method_name: str,
        url: str,
        response: Response,
    ) -> Response:
        pass
