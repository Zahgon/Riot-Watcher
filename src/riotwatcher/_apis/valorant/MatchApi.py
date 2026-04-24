from .. import BaseApi, NamedEndpoint
from .urls import MatchApiUrls


class MatchApi(NamedEndpoint):
    """
    This class wraps the Val-Match-v1 Api calls provided by the Riot API.

    See https://developer.riotgames.com/apis#val-match-v1 for more detailed information
    """

    def __init__(self, base_api: BaseApi):
        """
        Initialize a new MatchApi which uses the provided base_api

        :param BaseApi base_api: the root API object to use for making all requests.
        """
        super().__init__(base_api, self.__class__.__name__)

    def by_id(self, region: str, match_id: str):
        """
        Get match by id

        :returns: MatchDto
        """
        pass

    def matchlist_by_puuid(self, region: str, puuid: str):
        """
        Get matchlist for games played by puuid

        :returns: MatchlistDto
        """
        pass

    def recent_matches(self, region: str, queue: str):
        """
        Get recent matches.

        Note: Returns a list of match ids that have completed in the last 10 minutes.
        NA/LATAM/BR share a match history deployment. As such, recent matches will
        return a combined list of matches from those three regions. Requests are load
        balanced so you may see some inconsistencies as matches are added/removed from
        the list.

        :returns: RecentMatchesDto
        """
        pass
