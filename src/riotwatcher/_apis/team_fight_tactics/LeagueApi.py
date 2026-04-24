from .. import BaseApi, NamedEndpoint
from .urls import LeagueApiUrls


class LeagueApi(NamedEndpoint):
    """
    This class wraps the Tft-League-v1 Api calls provided by the Riot API.

    See https://developer.riotgames.com/apis#tft-league-v1 for more detailed information
    """

    def __init__(self, base_api: BaseApi):
        """
        Initialize a new LeagueApi which uses the provided base_api

        :param BaseApi base_api: the root API object to use for making all requests.
        """
        super().__init__(base_api, self.__class__.__name__)

    def challenger(self, region: str):
        """
        Get the challenger league

        :returns: LeagueListDTO
        """
        pass

    def by_summoner(self, region: str, encrypted_summoner_id: str):
        """
        Get league entries for a given summoner ID

        :returns: Set[LeagueEntryDTO]
        """
        pass

    def entries(self, region: str, tier: str, division: str, page: int = 1):
        """
        Get all the league entries

        :returns: Set[LeagueEntryDTO]
        """
        pass

    def grandmaster(self, region: str):
        """
        Get the grandmaster league.

        :returns: LeagueListDTO
        """
        pass

    def by_id(self, region: str, league_id: str):
        """
        Get league with given ID, including inactive entries

        :returns: LeagueListDTO
        """
        pass

    def master(self, region: str):
        """
        Get the master league

        :returns: LeagueListDTO
        """
        pass

    def rated_ladders(self, region: str, queue: str):
        """
        Get the top rated ladders

        :returns: TopRatedLadderEntryDto
        """
        pass
