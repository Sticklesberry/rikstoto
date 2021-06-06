from datetime import datetime
from api.constants import timestamp_format
import requests
from typing import Dict, Any, List

def convert_timestamp_to_datetime(timestamp: str) -> datetime:
    """
    Convert a rikstoto timestamp to a python datetime object
    """
    return datetime.strptime(timestamp, timestamp_format)

def result_of_get_request(url) -> List[Dict[str, Any]]:
    return requests.get(url).json()["result"]