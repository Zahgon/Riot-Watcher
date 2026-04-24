from requests import session


class BaseApi:
    def __init__(self, api_key, request_handlers=None, timeout=None):
        self._api_key = api_key
        self._request_handlers = request_handlers
        self._timeout = timeout
        self._session = session()

    @property
    def api_key(self):
        pass

    def raw_request(
        self,
        endpoint_name: str,
        method_name: str,
        region: str,
        url: str,
        query_params: dict,
    ):
        pass

    def raw_request_static(self, url, query_params):
        pass
