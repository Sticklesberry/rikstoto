import unittest
from pprint import pprint
from api.raceday.collect_races import (
    find_races_of_date,
)
from api.raceday.tests.preset_raceday_data import (
    response_data,
    win_odds_urls,
)
from datetime import date

#pprint(todays_races_to_odds_urls(find_todays_races(raceday)))

class TestRaceDay(unittest.TestCase):
    """
    Assumes preset data variables in preset_raceday_data are as expected.
    """
    def setUp(self):
        self.date = date(2021, 6, 1)
        self.races = find_races_of_date(response_data["result"], self.date)
        self.odds_urls = win_odds_urls

    def test_find_todays_races_finds_correct_amount_of_races(self):
        expected_amount_of_races = 43
        self.assertEqual(expected_amount_of_races, len(self.races))

    def test_race_dict_to_odds_links(self):
        #for schedulable_race in self.races:
        #    print(schedulable_race.win_odds_url)
        pass

    def test_races_to_odds_urls(self):
        pass