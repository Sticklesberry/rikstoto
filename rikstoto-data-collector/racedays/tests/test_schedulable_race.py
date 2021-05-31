import unittest
from racedays.schedulable_race import SchedulableRace
from datetime import datetime

class TestRaceSchedule(unittest.TestCase):
    def setUp(self):
        self.raceday_key = "S1_NR_2021-05-30"
        self.race_number = 1
        self.start_time = "2021-05-30T13:00:00"
        self.race_schedule = SchedulableRace(self.raceday_key, self.race_number, self.start_time)

    def test_win_odds_url(self):
        expected_win_odds_url = f"https://www.rikstoto.no/api/game/{self.raceday_key}/betdistribution/winodds/{self.race_number}"

        self.assertEqual(
            self.race_schedule.win_odds_url,
            expected_win_odds_url
        )

    def test_place_odds_url(self):
        expected_place_odds_url = f"https://www.rikstoto.no/api/game/{self.raceday_key}/betdistribution/placeodds/{self.race_number}"

        self.assertEqual(
            self.race_schedule.place_odds_url,
            expected_place_odds_url
        )

    def test_twin_odds_url(self):
        expected_twin_odds_url = f"https://www.rikstoto.no/api/game/{self.raceday_key}/odds/tv/{self.race_number}"

        self.assertEqual(
            self.race_schedule.twin_odds_url,
            expected_twin_odds_url
        )

    def test_triple_odds_url(self):
        expected_triple_odds_url = f"https://www.rikstoto.no/api/game/{self.raceday_key}/odds/t/{self.race_number}"

        self.assertEqual(
            self.race_schedule.triple_odds_url,
            expected_triple_odds_url
        )

    def test_is_today_when_true(self):
        pass

    def test_is_today_when_false(self):
        pass

    def test_json_representation_is_as_expected(self):
        pass
