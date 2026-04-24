import re

from .. import BaseApi, Endpoint
from .urls import DataDragonUrls


class DataDragonApi:
    def __init__(self, base_api: BaseApi):
        self._base_api = base_api

    def arenas(self, version: str, locale: str = None):
        pass

    def augments(self, version: str, locale: str = None):
        pass

    def champions(self, version: str, locale: str = None):
        pass

    def items(self, version: str, locale: str = None):
        pass

    def queues(self, version: str, locale: str = None):
        pass

    def regalia(self, version: str, locale: str = None):
        pass

    def tacticians(self, version: str, locale: str = None):
        pass

    def traits(self, version: str, locale: str = None):
        pass

    def versions_for_region(self, region: str):
        pass

    def versions_all(self):
        pass

    def _request(self, endpoint: Endpoint, version: str, locale: str):
        pass
