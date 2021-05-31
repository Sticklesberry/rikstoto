from constants.rikstoto_api_constants import base_url
from typing import List, Dict, Any

class RaceInterface:
    """
    """
    @property
    def win_odds_url(self) -> str:
        raise NotImplementedError

    @property
    def place_odds_url(self) -> str:
        raise NotImplementedError

    @property
    def twin_odds_url(self) -> str:
        raise NotImplementedError

    @property
    def triple_odds_url(self) -> str:
        raise NotImplementedError

class Race(RaceInterface):
    def __init__(self, raceday_key: str, race_number: int, *args: List[Any], **kwargs: Dict[Any, Any]):
        super().__init__(*args, **kwargs)
        self.raceday_key: str = raceday_key
        self.race_number: int = race_number

        self.betdistribution_base_url = f"{base_url}/game/{raceday_key}/betdistribution"
        self.odds_base_url = f"{base_url}/game/{raceday_key}/odds"

    @property
    def win_odds_url(self) -> str:
        return f"{self.betdistribution_base_url}/winodds/{self.race_number}"

    @property
    def place_odds_url(self) -> str:
        return f"{self.betdistribution_base_url}/placeodds/{self.race_number}"

    @property
    def twin_odds_url(self) -> str:
        return f"{self.odds_base_url}/tv/{self.race_number}"

    @property
    def triple_odds_url(self) -> str:
        return f"{self.odds_base_url}/t/{self.race_number}"