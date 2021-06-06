"""
Script to collect odds for a race X times before it starts.

The purpose of this is to have some data to analyze the market.

One interesting thing to analyze are sudden odds moves close to the start of races.
"""

from components.race import Race
from typing import List, Dict, Any, Union
from numbers import Number
import csv
from components.schedulable_race import SchedulableRace
import requests
from datetime import datetime
import time


def save_list_of_dicts_to_csv(list_of_dicts: List[Dict[str, Any]], filename: str, open_mode="w"):
    """
    Given a list of dicts, store them in a csv file

    Assumes all of the dicts have the same keys
    """
    header = list_of_dicts[0].keys()

    with open(filename, open_mode, encoding="utf-8") as output_file:
        dict_writer = csv.DictWriter(output_file, header) # type: ignore
        dict_writer.writeheader()
        dict_writer.writerows(list_of_dicts)


class OddsCollector:
    """
    Given a SchedulableRace, collect oddses of the race until it starts.
    """
    def __init__(self, race: SchedulableRace, *args, **kwargs):
        self.race = race

    @staticmethod
    def store(oddses: List[Dict[str, Any]], timestamp: datetime, filename: str):
        for dict in oddses:
            dict.update(timestamp=timestamp)

        save_list_of_dicts_to_csv(oddses, filename)

    # 1. hvordan fikse venting mellom oddsene blir hentet?
    def collect(self):
        self.store(
            requests.get(self.race.win_odds_url).json()["result"],
            datetime.now(),
            f"{self.race.race_name}-win.csv",
        )

        self.store(
            requests.get(self.race.place_odds_url).json()["result"],
            datetime.now(),
            f"{self.race.race_name}-place.csv",
        )

        self.store(
            requests.get(self.race.twin_odds_url).json()["result"],
            datetime.now(),
            f"{self.race.race_name}-twin.csv",
        )

        self.store(
            requests.get(self.race.triple_odds_url).json()["result"],
            datetime.now(),
            f"{self.race.race_name}-triple.csv",
        )

    def run(self):
        current_time = datetime.now()

        # TODO: it is not always correct that the race has started on schedule due to being postponed etc
        # but assume for now for simplicity that this is correct
        if current_time < self.race.start_time:
            self.collect()
            time.sleep(60*15) # TODO: need to find a clever way of dynamically choosing how long to wait until the next race

