import unittest
from api.odds.tests.mock_odds_data import (
    mock_win_odds_response,
    expected_win_odds_number_of_rows,
    expected_win_odds_labels,
    mock_place_odds_response,
    expected_place_odds_number_of_rows,
    expected_place_odds_labels,
    mock_triple_odds_response,
    expected_twin_odds_number_of_rows,
    expected_twin_odds_labels,
    mock_twin_odds_response,
    expected_triple_odds_number_of_rows,
    expected_triple_odds_labels,
)
from api.odds.collect_odds import save_list_of_dicts_to_csv
import os
import csv

class TestOddsStoring(unittest.TestCase):
    def help_test_writing_odds_response_to_a_csv_file(self, odds_response, filename, expected_labels, expected_number_of_rows):
        #filename = "test_store_win_odds.csv"
        save_list_of_dicts_to_csv(odds_response["result"], filename)

        # check the produced csv file's contents
        with open(filename, "r") as csvfile:
            csv_rows = list(csv.reader(csvfile, delimiter=","))
            self.assertEqual(expected_labels, csv_rows[0])
            self.assertEqual(expected_number_of_rows, len(csv_rows))

        # remove file
        os.remove(filename)

    def test_labels_and_number_of_rows_in_written_csv_file_from_win_odds_response(self):
        self.help_test_writing_odds_response_to_a_csv_file(
            mock_win_odds_response,
            "test_store_win_odds.csv", 
            expected_win_odds_labels,
            expected_win_odds_number_of_rows
        )

    def test_labels_and_number_of_rows_in_written_csv_file_from_place_odds_response(self):
         self.help_test_writing_odds_response_to_a_csv_file(
             mock_place_odds_response,
             "test_store_place_odds.csv",
             expected_place_odds_labels,
             expected_place_odds_number_of_rows
         )

    def test_labels_and_number_of_rows_in_written_csv_file_from_twin_odds_response(self):
         self.help_test_writing_odds_response_to_a_csv_file(
             mock_twin_odds_response,
             "test_store_twin_odds.csv",
             expected_twin_odds_labels,
             expected_twin_odds_number_of_rows
         )

    def test_labels_and_number_of_rows_in_written_csv_file_from_triple_odds_response(self):
         self.help_test_writing_odds_response_to_a_csv_file(
             mock_triple_odds_response,
             "test_store_triple_odds.csv",
             expected_triple_odds_labels,
             expected_triple_odds_number_of_rows
         )