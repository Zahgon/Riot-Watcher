from typing import Any

from requests import Response

from .RequestHandler import RequestHandler
from ..Deserializer import Deserializer


class DeserializerAdapter(RequestHandler):
    def __init__(self, deserializer: Deserializer):
        super().__init__()
        self._deserializer = deserializer

    def after_request(
        self,
        region: str,
        endpoint_name: str,
        method_name: str,
        url: str,
        response: Response,
    ) -> Any:
        pass

    def after_static_request(self, url: str, response: Response) -> Any:
        pass
