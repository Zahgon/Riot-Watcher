import re

from .. import BaseApi, Endpoint
from .urls import DataDragonUrls


class DataDragonApi:
    def __init__(self, base_api: BaseApi):
        self._base_api = base_api

    def champions(self, version: str, full: bool = False, locale=None):
        pass

    def items(self, version: str, locale: str = None):
        pass

    def languages(self, version: str, locale: str = None):
        pass

    def maps(self, version: str, locale: str = None):
        pass

    def masteries(self, version: str, locale: str = None):
        pass

    def profile_icons(self, version: str, locale: str = None):
        pass

    def runes(self, version: str, locale: str = None):
        pass

    def runes_reforged(self, version: str, locale: str = None):
        pass

    def summoner_spells(self, version: str, locale: str = None):
        pass

    def versions_for_region(self, region: str):
        pass

    def versions_all(self):
        pass

    def _request(self, endpoint: Endpoint, version: str, locale: str):
        pass
