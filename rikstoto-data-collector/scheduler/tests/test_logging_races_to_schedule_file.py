import unittest
from scheduler.scheduler import log_races_of_date_to_schedule
from api.raceday.tests.preset_raceday_data import (
    response_data,
    response_date,
    expected_number_of_races,
)
import os

class TestRaceScheduling(unittest.TestCase):
    def test_writing_a_list_of_schedulable_races_to_file(self):
        schedule_filename = "test_schedule.txt"

        log_races_of_date_to_schedule(response_data["result"], response_date, schedule_filename)

        scheduled_races = []

        with open(schedule_filename, "r") as races:
            for race in races:
                scheduled_races.append(race)

        os.remove(schedule_filename)

        self.assertEqual(expected_number_of_races, len(scheduled_races))





