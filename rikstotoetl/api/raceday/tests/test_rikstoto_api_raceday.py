import unittest
import requests # type: ignore
from api.raceday.collect_races import todays_races_url

class TestRaceDay(unittest.TestCase):
    def setUp(self):
        self.raceday_response = requests.get(todays_races_url)
        self.raceday_json = self.raceday_response.json()

    def test_rikstoto_api_racedays(self):
        self.assertEqual(self.raceday_response.status_code, 200)

