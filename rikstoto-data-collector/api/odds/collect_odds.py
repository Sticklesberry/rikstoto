"""
Script to collect odds for a race X times before it starts.

The purpose of this is to have some data to analyze the market.

One interesting thing to analyze are sudden odds moves close to the start of races.
"""

from components.race import Race
from typing import List, Dict, Any, Union
from numbers import Number
import csv


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
