from time import sleep # type: ignore
from api.constants import base_url
from components.schedulable_race import SchedulableRace
from datetime import date
from typing import Dict, Any, List
import requests

"""
collect.py

Functionality for fetching info about todays trot races and scheduling processes
to run for each of them.

Scheduling: https://pypi.org/project/python-crontab/
"""

# raceday constants
todays_races_url = f"{base_url}/racedays/"

def find_races_of_date(tracks: List[Dict[str, Any]], date: date) -> List[SchedulableRace]:
    """
    Given a track list dict, create a list of todays trot races represented
    as dictionaries with three key-value pairs.

    A track list is the same as the "result" attribute of the response from 
    https://www.rikstoto.no/api/racedays/

    Input:
    [
        {
            ...
            "raceDayKey": "...",
            "races": [],
            ...
        },
        {
            ...
        }

    ]

    Output:
    [RaceSchedule]
    """

    races_of_date: List[SchedulableRace] = []

    for track in tracks:
        raceday_key = track["raceDayKey"]
        races = track["races"]
        sport_type = track["sportType"]

        if sport_type == "T":
            for race in races:
                race_number = race["raceNumber"]
                start_time = race["startTime"]

                race_schedule = SchedulableRace(start_time, raceday_key, race_number)

                if race_schedule.is_same_date_as(date):
                    races_of_date.append(race_schedule)

    return races_of_date

def find_todays_races(tracks: List[Dict[str, Any]]) -> List[SchedulableRace]:
    return find_races_of_date(tracks, date.today())


def fetch_todays_raceday_tracks():
    return requests.get(todays_races_url).json()["result"]

