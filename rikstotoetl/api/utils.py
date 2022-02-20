from datetime import datetime
from rikstotoetl.api.constants import (
    timestamp_format,
    base_url,
)
import requests
from typing import Dict, Any, List

def convert_timestamp_to_datetime(timestamp: str) -> datetime:
    """
    Convert a rikstoto timestamp to a python datetime object
    """
    return datetime.strptime(timestamp, timestamp_format)


def convert_datetime_to_datestring(date: datetime) -> str:
    return f"{date.year}-{date.month}-{date.day}"


def result_of_get_request(url) -> List[Dict[str, Any]]:
    response = requests.get(url)

    return response.json()["result"]



def racedays_interval_url(fra: datetime, til: datetime) -> str:
    interval_start = convert_datetime_to_datestring(fra)
    interval_end = convert_datetime_to_datestring(til)

    return f"{base_url}/results/racedays/{interval_start}/{interval_end}/list"