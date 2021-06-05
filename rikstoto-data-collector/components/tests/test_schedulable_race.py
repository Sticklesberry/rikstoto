import unittest
from components.schedulable_race import SchedulableRace
from datetime import date, datetime

class TestRaceSchedule(unittest.TestCase):
    def setUp(self):
        self.raceday_key = "S1_NR_2021-05-30"
        self.race_number = 1
        self.start_time = "2021-05-30T13:00:00"
        self.race_schedule = SchedulableRace(self.start_time, self.raceday_key, self.race_number)

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
        self.assertFalse(self.race_schedule.is_today)

    def test_is_today_when_false(self):
        today = date.today()
        today_start_time = f"{today.year}-{today.month}-{today.day}T12:00:00"
        today_schedulable = SchedulableRace(today_start_time, self.raceday_key, self.race_number)

        self.assertTrue(today_schedulable.is_today)

    def test_initialize_from_string_representation_gives_correct_object(self):
        """
        Check that it is possible to initialize a SchedulableRace given an output
        from its __repr__() method using SchedulableRace.init_from_string()
        """
        representation = "(N1_NR_2021-06-01,1,2021-06-01T09:05:00)"

        expected_race_key = "N1_NR_2021-06-01"
        expected_race_number = 1
        expected_start_time = datetime(2021, 6, 1, 9, 5, 0)
        sr = SchedulableRace.init_from_string(representation)

        self.assertEqual(expected_race_key, sr.raceday_key)
        self.assertEqual(expected_race_number, sr.race_number)
        self.assertEqual(expected_start_time, sr.start_time)

