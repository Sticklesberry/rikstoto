import unittest
from racedays.race import Race

class TestSchedulable(unittest.TestCase):
    def setUp(self):
        self.raceday_key = "S1_NR_2021-05-30"
        self.race_number = 1
        self.race = Race(self.raceday_key, self.race_number)

    def test_win_odds_url(self):
        expected_win_odds_url = f"https://www.rikstoto.no/api/game/{self.raceday_key}/betdistribution/winodds/{self.race_number}"

        self.assertEqual(
            self.race.win_odds_url,
            expected_win_odds_url
        )

    def test_place_odds_url(self):
        expected_place_odds_url = f"https://www.rikstoto.no/api/game/{self.raceday_key}/betdistribution/placeodds/{self.race_number}"

        self.assertEqual(
            self.race.place_odds_url,
            expected_place_odds_url
        )

    def test_twin_odds_url(self):
        expected_twin_odds_url = f"https://www.rikstoto.no/api/game/{self.raceday_key}/odds/tv/{self.race_number}"

        self.assertEqual(
            self.race.twin_odds_url,
            expected_twin_odds_url
        )

    def test_triple_odds_url(self):
        expected_triple_odds_url = f"https://www.rikstoto.no/api/game/{self.raceday_key}/odds/t/{self.race_number}"

        self.assertEqual(
            self.race.triple_odds_url,
            expected_triple_odds_url
        )