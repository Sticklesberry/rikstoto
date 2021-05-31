"""
rikstoto_api_constants.py

Global constants in the rikstoto API
"""

from datetime import datetime

base_url = "https://www.rikstoto.no/api"

timestamp_format = "%Y-%m-%dT%H:%M:%S"

def convert_timestamp_to_datetime(timestamp: str):
    return datetime.strptime(timestamp, timestamp_format)