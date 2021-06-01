from datetime import datetime
from api.constants import timestamp_format

def convert_timestamp_to_datetime(timestamp: str) -> datetime:
    """
    Convert a rikstoto timestamp to a python datetime object
    """
    return datetime.strptime(timestamp, timestamp_format)