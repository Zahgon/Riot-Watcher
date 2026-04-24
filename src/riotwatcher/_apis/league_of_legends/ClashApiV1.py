from .. import BaseApi, NamedEndpoint
from .urls import ClashApiV1Urls


class ClashApiV1(NamedEndpoint):
    """
    This class wraps the Clash-v1 endpoint calls provided by the Riot API.

    See https://developer.riotgames.com/apis#clash-v1 for more detailed information
    """

    def __init__(self, base_api: BaseApi):
        """
        Initialize a new ClashApiV1 which uses the provided base_api

        :param BaseApi base_api: the root API object to use for making all requests.
        """
        super().__init__(base_api, self.__class__.__name__)

    def by_summoner(self, region: str, summoner_id: str):
        """
        This endpoint returns a list of active Clash players for a given summoner ID.
        If a summoner registers for multiple tournaments at the same time (e.g.,
        Saturday and Sunday) then both registrations would appear in this list.

        :param string region:               The region to execute this request on.
        :param string summoner_id:          The summoner ID.

        :returns: List[PlayerDTO]: represents the summoner's info for the current clash.
        """
        pass

    def by_team(self, region: str, team_id: str):
        """
        Get team by ID.

        :param string region:               The region to execute this request on
        :param string team_id:              Team ID

        :returns: TeamDTO: represents a clash team
        """
        pass

    def tournaments(self, region: str):
        """
        Returns a list of active and upcoming tournaments.

        :param string region:           The region to execute this request on

        :returns: List[TournamentDTO]: represents all of the current tournaments active
        """
        pass

    def tournament_by_team(self, region: str, team_id: str):
        """
        Get tournament by team ID.

        :param string region:                   The region to execute this request on
        :param string team_id:                  Team ID

        :returns: TournamentDTO: represents a clash tournament
        """
        pass

    def by_tournament(self, region: str, tournament_id: str):
        """
        Get tournament by ID.

        :param string region:                   The region to execute this request on
        :param string tournament_id:            Tournament ID

        :returns: TournamentDTO: represents a clash tournament
        """
        pass
