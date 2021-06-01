from time import sleep # type: ignore
from api.constants import base_url
from data.schedulable_race import SchedulableRace

from typing import Dict, Any, List

"""
collect.py

Functionality for fetching info about todays trot races and scheduling processes
to run for each of them.

Scheduling: https://pypi.org/project/python-crontab/
"""

# raceday constants
todays_races_url = f"{base_url}/racedays/"

def find_todays_races(tracks: List[Dict[str, Any]]):
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

    todays_races: List[SchedulableRace] = []

    for track in tracks:
        raceday_key = track["raceDayKey"]
        races = track["races"]
        sport_type = track["sportType"]

        if sport_type == "T":
            for race in races:
                race_number = race["raceNumber"]
                start_time = race["startTime"]

                race_schedule = SchedulableRace(start_time, raceday_key, race_number)

                if race_schedule.is_today:
                    todays_races.append(race_schedule)

    return todays_races


#def race_dict_to_odds_links(race_schedule: RaceSchedule):
#    """
#    Given a dictionary of todays trot race schedules return a list of dictionaries 
#    that contain urls for odds endpoints.
#
#    The input are represented as the following
#    triples:
#
#    {
#        "start_time":  datetime object of the race's start time,
#        "raceday_key": a unique string representing a track's raceday,
#        "race_number": the number of the race
#    }
#    """
#    raceday_key = race_schedule["raceday_key"]
#    race_number = race_schedule["race_number"]
#
#    betdistribution_base_url = f"{base_url}/game/{raceday_key}/betdistribution"
#    odds_base_url = f"{base_url}/game/{raceday_key}/odds"
#
#    win_odds_url = f"{betdistribution_base_url}/winodds/{race_number}"
#    place_odds_url = f"{betdistribution_base_url}/placeodds/{race_number}"
#    twin_odds_url = f"{odds_base_url}/tv/{race_number}"
#    triple_odds_url = f"{odds_base_url}/t/{race_number}"
#
#    return {
#        "win_odds": win_odds_url,
#        "place_odds": place_odds_url,
#        "twin_odds": twin_odds_url,
#        "triple_odds": triple_odds_url,
#    }


#def todays_races_to_odds_urls(todays_races: List[Dict[str, Any]]):
#    """
#    Given a list of todays races, create a list of the given race's
#    odds endpoint urls (win, place, twin, triple).
#    """
#    return list(map(race_dict_to_odds_links, todays_races))

