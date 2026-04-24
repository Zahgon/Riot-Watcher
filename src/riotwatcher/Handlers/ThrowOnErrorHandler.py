import requests

from .RequestHandler import RequestHandler

ApiError = requests.HTTPError


class ThrowOnErrorHandler(RequestHandler):
    def after_request(
        self,
        region: str,
        endpoint_name: str,
        method_name: str,
        url: str,
        response: requests.Response,
    ) -> None:
        pass
