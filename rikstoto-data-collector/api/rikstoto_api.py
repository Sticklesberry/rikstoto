from datetime import datetime
from unittest import result
from api.utils import (
    result_of_get_request,
    racedays_interval_url,
)
from api.constants import todays_races_url as racedays_url
from typing import Dict, Any, List


class RikstotoAPI:

    @staticmethod
    def get_racedays(start: datetime, end: datetime) -> List[Dict[str, Any]]:
        """
        Get racedays from start until end
        """
        return result_of_get_request(racedays_interval_url(start, end))
    
    @staticmethod
    def get_todays_racedays() -> List[Dict[str, Any]]:
        """
        Get today's racedays
        """
        return result_of_get_request(racedays_url)