import unittest
from api.odds.tests.mock_odds_data import (
    mock_win_odds_response,
    mock_place_odds_response,
    mock_triple_odds_response,
    mock_twin_odds_response,
)
from api.odds.collect_odds import save_list_of_dicts_to_csv
import os

class TestOddsStoring(unittest.TestCase):
    def test_writing_win_odds_response_to_a_csv_file(self):
        filename = "test_store_win_odds.csv"
        save_list_of_dicts_to_csv(mock_win_odds_response["result"], filename)

    def test_writing_place_odds_response_to_a_csv_file(self):
        filename = "test_store_place_odds.csv"
        save_list_of_dicts_to_csv(mock_place_odds_response["result"], filename)

    def test_writing_twin_odds_response_to_a_csv_file(self):
        filename = "test_store_twin_odds.csv"
        save_list_of_dicts_to_csv(mock_twin_odds_response["result"], filename)

    def test_writing_triple_odds_response_to_a_csv_file(self):
        filename = "test_store_triple_odds.csv"
        save_list_of_dicts_to_csv(mock_triple_odds_response["result"], filename)