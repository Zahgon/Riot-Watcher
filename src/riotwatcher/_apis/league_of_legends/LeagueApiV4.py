from .. import BaseApi, NamedEndpoint
from .urls import LeagueApiV4Urls


class LeagueApiV4(NamedEndpoint):
    """
    This class wraps the League-v4 Api calls provided by the Riot API.

    See https://developer.riotgames.com/api-methods/#league-v4/ for more detailed
    information
    """

    def __init__(self, base_api: BaseApi):
        """
        Initialize a new LeagueApiV4 which uses the provided base_api

        :param BaseApi base_api: the root API object to use for making all requests.
        """
        super().__init__(base_api, self.__class__.__name__)

    def challenger_by_queue(self, region: str, queue: str):
        """
        Get the challenger league for a given queue.

        :param string region:   the region to execute this request on
        :param string queue:    the queue to get the challenger players for

        :returns: LeagueListDTO
        """
        pass

    def grandmaster_by_queue(self, region: str, queue: str):
        """
        Get the grandmaster league for a given queue.

        :param string region:   the region to execute this request on
        :param string queue:    the queue to get the grandmaster players for

        :returns: LeagueListDTO
        """
        pass

    def masters_by_queue(self, region: str, queue: str):
        """
        Get the master league for a given queue.

        :param string region:   the region to execute this request on
        :param string queue:    the queue to get the master players for

        :returns: LeagueListDTO
        """
        pass

    def by_id(self, region: str, league_id: str):
        """
        Get league with given ID, including inactive entries

        :param string region:       the region to execute this request on
        :param string league_id:    the league ID to query

        :returns: LeagueListDTO
        """
        pass

    def by_summoner(self, region: str, encrypted_summoner_id: str):
        """
        Get league entries in all queues for a given summoner ID

        :param string region:                   the region to execute this request on
        :param string encrypted_summoner_id:    the summoner ID to query

        :returns: Set[LeagueEntryDTO]
        """
        pass

    def by_puuid(self, region: str, puuid: str):
        """
        Get league entries in all queues for a given puuid

        :param string region:                   the region to execute this request on
        :param string puuid:                    the puuid to query

        :returns: Set[LeagueEntryDTO]
        """
        pass

    def entries(self, region: str, queue: str, tier: str, division: str, page: int = 1):
        """
        Get all the league entries

        :param string region:   the region to execute this request on
        :param string queue:    the queue to query, i.e. RANKED_SOLO_5x5
        :param string tier:     the tier to query, i.e. DIAMOND
        :param string division: the division to query, i.e. III
        :param int page:        the page for the query to paginate to. Starts at 1.

        :returns: Set[LeagueEntryDTO]
        """
        pass
